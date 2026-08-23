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
<img src="https://cdn5.telesco.pe/file/QiVnFq6pQeUGCSTv6-K8IeAUwFEGF6XFGiU7uwKJ3Z-hjBoNMJ18Ks4020A-NVlDzGXbpni9vCO7PQqcbc6JcWedc-aW2hx2N4LOSUuiJL6a1Cc55f3vBPbJY0b_GC8f-9AE2gIBG4VYY0H57fup8_puLdlA05IOwdstjiNen0UlWVyEXfZUf11sBa1oT2ex_tBfBpTcOiml3fJDb_ti_Df0skIs7LMGsvYkTv4z_-M3vwlnde9JmJHgtL-x-I_HM1aGhGFsjB2pWJxbCrFIYeT0rR71EOtwyEZE6R9R-xUXx9hRTPlhzNij4eqUfIDL1CiQu0Kcdcc-U_4z4ZjnIw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 448K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 16:38:18</div>
<hr>

<div class="tg-post" id="msg-104451">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2308ddcaed.mp4?token=DCfyU0pgf-OFWACOi9etNegfXoCYIEUHsu1CJp3zPtv6nlPPVqj1vfsKWKK1yUmqUo037HnHAkKo9VDdvmQAX1wBotaBackNPMylx9fwTicFGwm4yx4PwmzNeoo83PJpXsaU_xBoiCl3NveMQoFr9a7Otv0xOaL1jKd0WXaOeZiOwB-ANc0D7GKZXt1OYg_mWtI_9se7TZNUVgjSSoIzyoNrNIkD8T57mJq6dqlSIFVI4Bzfzt9FEuXDk0eclYsAunZLnRKNUvQLUrdB4c_3uR1QVkiuG82iRTinF4b-sNSBas6q7bzM1wTgrzX0VzBkh_qBgo6RN6UTJ-Eov78h4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2308ddcaed.mp4?token=DCfyU0pgf-OFWACOi9etNegfXoCYIEUHsu1CJp3zPtv6nlPPVqj1vfsKWKK1yUmqUo037HnHAkKo9VDdvmQAX1wBotaBackNPMylx9fwTicFGwm4yx4PwmzNeoo83PJpXsaU_xBoiCl3NveMQoFr9a7Otv0xOaL1jKd0WXaOeZiOwB-ANc0D7GKZXt1OYg_mWtI_9se7TZNUVgjSSoIzyoNrNIkD8T57mJq6dqlSIFVI4Bzfzt9FEuXDk0eclYsAunZLnRKNUvQLUrdB4c_3uR1QVkiuG82iRTinF4b-sNSBas6q7bzM1wTgrzX0VzBkh_qBgo6RN6UTJ-Eov78h4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
هالند نادان با موهای تراشیده در بازی امروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 463 · <a href="https://t.me/Futball180TV/104451" target="_blank">📅 16:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104450">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da4f666bc.mp4?token=i6Z3cCYtZZGLxYpkBTyDCCoEAtQ4NthnNO-R695XLV6PZuRUvy5HLXs0xA2Qb-Jle7foLu7AW6ZP0AntHwb-4wAnsb2mK-bESyasJE2e0469GFwC6uByuMd4SjSyBpcfYSNb7o3baOzgV3lygBUrHDWYfF0Dph7NAj9xEaBDIFgIaKDH9ts5FjP187nnslnbNnzeyqoddHUwizUeg1KbHYbd96xKdo_x-h1G8OJXFNEGz_um4Cx0E8VDPe2PmS91tLDDuz6CWHZkWC27LNHeUsn3GPwv92EFdS600xCjmc2-jz0EpYNBowwNQ0QQS4rbWAVago_82jdHtkI2LLiCeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da4f666bc.mp4?token=i6Z3cCYtZZGLxYpkBTyDCCoEAtQ4NthnNO-R695XLV6PZuRUvy5HLXs0xA2Qb-Jle7foLu7AW6ZP0AntHwb-4wAnsb2mK-bESyasJE2e0469GFwC6uByuMd4SjSyBpcfYSNb7o3baOzgV3lygBUrHDWYfF0Dph7NAj9xEaBDIFgIaKDH9ts5FjP187nnslnbNnzeyqoddHUwizUeg1KbHYbd96xKdo_x-h1G8OJXFNEGz_um4Cx0E8VDPe2PmS91tLDDuz6CWHZkWC27LNHeUsn3GPwv92EFdS600xCjmc2-jz0EpYNBowwNQ0QQS4rbWAVago_82jdHtkI2LLiCeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیخ‌منصور قشنگ سیتی رو خالی کرد
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/Futball180TV/104450" target="_blank">📅 16:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104449">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ynlw_FAcM2ydff496f5UX1G4Rqwd6JEbMgz5M1hkS5QIET35caGNWYy8nuo7rBfMuSKLpgtP8_bU0imS4zJkC-E0ZdsDOT4952sHUXJBBHx3V6wowRV3HPCtVKC-QbuMlJKcQJQHgA4IXPAP20ql-VH4pCrHJt8nsa5qor06K1kTAbPnMn7MdPxjwP-SIq0yH133-2vy_0DKrIeHMWmxIwaRvWCVGRso-2r2CJwIprU5XFvis7TrM4uXGLBVDgW90pIhbe-6VC1dP9pENf5TzICp1GyIMFs4-ih__CIEtU_pIE4e71zPYfDIH0DjKqN8WibrZpWvINTo7lNwS_f1jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⚽️
بهترین بازیکنان یازده‌فصل اخیر پریمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/Futball180TV/104449" target="_blank">📅 16:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104448">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87c342598b.mp4?token=qBrpY4AKjcqWziTQ7tGqRuNo0E9LXnAbqsgaYdJ4wdmE5hO18hxvZNDcHi-qsrx1-sG6sSwUs3-TnSiKfZf1XxPYzwmbzsomQ1-hUNBqVAwDdUZkErbJDScodqQ4sUcvc9gdz4urVPSnD54cY6CCBiQ1YfUxbXs1UjXRf8DqAG9ROhR8_yBrH1d5pDnhICKcmIHe8Xf_WGZ7FVfJurrCkdDTQJpdcw8QKZuRQmkUGmX7wJufAlP-8p2bgRVRTe1vU6JcWaiUoQKo0okaRMK-jRBPBu-yAxvRdC26aoktB_8qhFY1MjISVCtday1lzgXqtLGrtLIbRw1eREEDxoBYeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87c342598b.mp4?token=qBrpY4AKjcqWziTQ7tGqRuNo0E9LXnAbqsgaYdJ4wdmE5hO18hxvZNDcHi-qsrx1-sG6sSwUs3-TnSiKfZf1XxPYzwmbzsomQ1-hUNBqVAwDdUZkErbJDScodqQ4sUcvc9gdz4urVPSnD54cY6CCBiQ1YfUxbXs1UjXRf8DqAG9ROhR8_yBrH1d5pDnhICKcmIHe8Xf_WGZ7FVfJurrCkdDTQJpdcw8QKZuRQmkUGmX7wJufAlP-8p2bgRVRTe1vU6JcWaiUoQKo0okaRMK-jRBPBu-yAxvRdC26aoktB_8qhFY1MjISVCtday1lzgXqtLGrtLIbRw1eREEDxoBYeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇳🇱
دومین‌نمایش درخشان ترشتگن در تیم‌آژاکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/104448" target="_blank">📅 15:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104447">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd1e841a3.mp4?token=hFcuyBHKgqVfYR4u18TmiS-tJWFGOXqyGM0L3-5_61KANXqqxXXEvz82kTs4crixOCyjibWxGKEDT1OepvQGf6bnxvq2Vn7adbWUBU2FXWsZagfhVPSaaakKJ9gXr8IAyGl8tOp0--PDLwxJCvII8JDcMSqSjA3Kw5Lfn_CLkM360KaNk7_0BNqngVsgC9PpR7X2179v-8zZKLTu_a2i4qKHSJAq_jvmUn2pcBiT-qxUxk52whP0VV-r0Q9msDolF1pdXNq_ZZHZ74N1BFdPL7IHzeHvu0Lbd_EApwg0MsFuHF-oMHUqNOnDkOEu5dL3IIT6xGuO_jsIn47wQeZ1vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd1e841a3.mp4?token=hFcuyBHKgqVfYR4u18TmiS-tJWFGOXqyGM0L3-5_61KANXqqxXXEvz82kTs4crixOCyjibWxGKEDT1OepvQGf6bnxvq2Vn7adbWUBU2FXWsZagfhVPSaaakKJ9gXr8IAyGl8tOp0--PDLwxJCvII8JDcMSqSjA3Kw5Lfn_CLkM360KaNk7_0BNqngVsgC9PpR7X2179v-8zZKLTu_a2i4qKHSJAq_jvmUn2pcBiT-qxUxk52whP0VV-r0Q9msDolF1pdXNq_ZZHZ74N1BFdPL7IHzeHvu0Lbd_EApwg0MsFuHF-oMHUqNOnDkOEu5dL3IIT6xGuO_jsIn47wQeZ1vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
👀
امیرحسین اصلانیان: در رستوران عابدزاده همبرگر خوردیم؛ غذای احمدرضا رو هم من حساب کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/Futball180TV/104447" target="_blank">📅 15:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104446">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d764ecc24.mp4?token=j0a2aWS40_anWajTAwEUsl_rK7YbYjsHNMuIDUv7FkQiURRCG8DHhaXyLNlo3r0Rc114LD2gnf5QT0ID_tEhhpk5C47toI5ZWwaMopldnit82YAAXYaGauOvxBhOiCMr9Q0DSHs4f0eNzAcfN8peYYDaZ0myjIdOXpn-b0UiOVCBjvNMViASzwPhbnOyCPxTJzSLMLTlNQhVsKIIjtNHPcae4ZgfcyuDv_bogg341mdMIwMOsKhn2RHB8oqLUpb6BtV4GeZ_gBEEJpoI6-0JhVD6yL7wa-Djfv7P0xN0aCp6_KefTGRW-0htF7pnbonT-EC6g36Ommxwq51VNUcx0mNAYwGZSUTs8TLTyo-A7Tj9EeS2S6ipm_qElAB6gGdomXBYuRY-DxlDxwJ5ACGRM3XWJKVCPah4ir0ydO9gb3hphRzekQcDo4n2BDoq9O4tDCDWLo5QYD9Zb6MpkEyRtMK8uVeJSxIU9mx4Aa_mzvJiZqsJ6ttgaQZoSAMnDkalNZh6m-6wlfQlkUqvY6T1dV1tSCyZE7W7okvhhNXZXFP7Jbmd56k6PbzvmG5K9SJgOOSGaMUyBYncGSjQd9yIDlyq7CnyVLXsCX2kBRXmGkChGJ_e3uvZXHZDKZokoR_jUjweNFYtCZy2OA_smOZwDNDX8-HEW1Y2weeED8wJivM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d764ecc24.mp4?token=j0a2aWS40_anWajTAwEUsl_rK7YbYjsHNMuIDUv7FkQiURRCG8DHhaXyLNlo3r0Rc114LD2gnf5QT0ID_tEhhpk5C47toI5ZWwaMopldnit82YAAXYaGauOvxBhOiCMr9Q0DSHs4f0eNzAcfN8peYYDaZ0myjIdOXpn-b0UiOVCBjvNMViASzwPhbnOyCPxTJzSLMLTlNQhVsKIIjtNHPcae4ZgfcyuDv_bogg341mdMIwMOsKhn2RHB8oqLUpb6BtV4GeZ_gBEEJpoI6-0JhVD6yL7wa-Djfv7P0xN0aCp6_KefTGRW-0htF7pnbonT-EC6g36Ommxwq51VNUcx0mNAYwGZSUTs8TLTyo-A7Tj9EeS2S6ipm_qElAB6gGdomXBYuRY-DxlDxwJ5ACGRM3XWJKVCPah4ir0ydO9gb3hphRzekQcDo4n2BDoq9O4tDCDWLo5QYD9Zb6MpkEyRtMK8uVeJSxIU9mx4Aa_mzvJiZqsJ6ttgaQZoSAMnDkalNZh6m-6wlfQlkUqvY6T1dV1tSCyZE7W7okvhhNXZXFP7Jbmd56k6PbzvmG5K9SJgOOSGaMUyBYncGSjQd9yIDlyq7CnyVLXsCX2kBRXmGkChGJ_e3uvZXHZDKZokoR_jUjweNFYtCZy2OA_smOZwDNDX8-HEW1Y2weeED8wJivM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
صحبت های مهدی توتونچی در مورد شادی شجاع خلیل زاده مقابل سپاهان اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/Futball180TV/104446" target="_blank">📅 14:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104445">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b843ddc780.mp4?token=qwMt9XAV7eK96wjosQ8j_9oZlrY2Y_Yme9RgVDyHuU4cy3DdCL4xT4DfELezuD3LjvEmIdyoOmo1vpxVrHV1TryrkSqnCPZ_VsOgFM3c1_GfWpWrZ66nb80wrO_ZpnvGrpddQgqvX5ZgI4hp3dBMuPHkRLxBQEO9ohSHLY3rOEZEfxHN0vw-uEGjgFYmNnRmo98dqMlwSPieO3KxJBXNqu2VKIRfZCV9ECArpC0yoyGMG1v1QRHHMOi-8s5rpXdKqB9SM44VRf5r8tlRsiiFThhadzVMyn5qsOUpb7ix48UqbPyuAwqiQfMjoJNSnSHvFIOznxlD1UkARW7bo6iFoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b843ddc780.mp4?token=qwMt9XAV7eK96wjosQ8j_9oZlrY2Y_Yme9RgVDyHuU4cy3DdCL4xT4DfELezuD3LjvEmIdyoOmo1vpxVrHV1TryrkSqnCPZ_VsOgFM3c1_GfWpWrZ66nb80wrO_ZpnvGrpddQgqvX5ZgI4hp3dBMuPHkRLxBQEO9ohSHLY3rOEZEfxHN0vw-uEGjgFYmNnRmo98dqMlwSPieO3KxJBXNqu2VKIRfZCV9ECArpC0yoyGMG1v1QRHHMOi-8s5rpXdKqB9SM44VRf5r8tlRsiiFThhadzVMyn5qsOUpb7ix48UqbPyuAwqiQfMjoJNSnSHvFIOznxlD1UkARW7bo6iFoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
ناراحتی شدید همسایه ورزشگاه وطنی از شعارهای رکیک هواداران در بازی‌های نساجی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/104445" target="_blank">📅 14:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104444">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90391f76b.mp4?token=rplt0aoXnyU5bLqrsPjsBqK4McjV8NeM1-w1eEs27S_JdVu1DqyD0vCGvyY2wBA4Lzbo6p7HtVMf0rq6RWPyobm-vzzMZbgsgqKjV4Z5U_fhu8zAhMgZhvs1sYxHDnGlBF_6SiPMONJu_P-aoxjfZTqIL-DkIZDRsnPMOjstW-cDV4rbEYuH2kf8IEkPdl9rfmJDh82kQQp39cCAqx6_98Fb97DwzzClkX55UFfAJg4Bav9jG7O4b6B0HkknsxwOxkybuQF0hgGJAGkjJrttyl73fkGYrCrZbU5M0_vuO-0jo8MqUEuvXi3NzjMLWTG7HplBSwgh7AZHsphIeyyfGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90391f76b.mp4?token=rplt0aoXnyU5bLqrsPjsBqK4McjV8NeM1-w1eEs27S_JdVu1DqyD0vCGvyY2wBA4Lzbo6p7HtVMf0rq6RWPyobm-vzzMZbgsgqKjV4Z5U_fhu8zAhMgZhvs1sYxHDnGlBF_6SiPMONJu_P-aoxjfZTqIL-DkIZDRsnPMOjstW-cDV4rbEYuH2kf8IEkPdl9rfmJDh82kQQp39cCAqx6_98Fb97DwzzClkX55UFfAJg4Bav9jG7O4b6B0HkknsxwOxkybuQF0hgGJAGkjJrttyl73fkGYrCrZbU5M0_vuO-0jo8MqUEuvXi3NzjMLWTG7HplBSwgh7AZHsphIeyyfGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
اسپانیول، اولین قربانیِ رئالِ مورینیو.
🥶
☠️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/104444" target="_blank">📅 14:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104443">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a456af91c.mp4?token=CVobrvKm4MGN0rG8YuWFo3Ea3SknFlJmOT7e7He3ag_hCwaCHGCLgQdp83GxMkbBjZe-HqoACFs3MwcE7AfRE9S_LZtUlHSG8EbzHFdA6vJQx_NTxqhhUOgYNu38NhroE82p2dMsMRbTgc64cMPKSU1hzJue5zyvcJkTk-voHDF5s53GLfqmxs-mFLQhjGq32jNPU8v2xKEHtSyuArTv3ZL7bmMMiUDaPKt3g1Mo_1N6sA2xE2fJbvTsLWZuXXs3kbJQZ3ig1PbVs9y-DwxFE2aMJbznxciu9v8HPT5i0NqMqT8NjBQG2okGqJtkqrulVjc_8YfPV7HhklaCiWUY7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a456af91c.mp4?token=CVobrvKm4MGN0rG8YuWFo3Ea3SknFlJmOT7e7He3ag_hCwaCHGCLgQdp83GxMkbBjZe-HqoACFs3MwcE7AfRE9S_LZtUlHSG8EbzHFdA6vJQx_NTxqhhUOgYNu38NhroE82p2dMsMRbTgc64cMPKSU1hzJue5zyvcJkTk-voHDF5s53GLfqmxs-mFLQhjGq32jNPU8v2xKEHtSyuArTv3ZL7bmMMiUDaPKt3g1Mo_1N6sA2xE2fJbvTsLWZuXXs3kbJQZ3ig1PbVs9y-DwxFE2aMJbznxciu9v8HPT5i0NqMqT8NjBQG2okGqJtkqrulVjc_8YfPV7HhklaCiWUY7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
جلوه‌هایی از مسابقه دیشب لیگ‌عربستان:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/104443" target="_blank">📅 13:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104441">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrF3qRuxtLlV_JXrUXjzEz4sRtTrifTPmhh95UJw-NvYs8RTu6MZ20HENUQZoaCN47lJrGMCO5oU09haLe2y9PLQqqQHKQ5jkmqGVwbTsq6bEt5J-rODw1WpJc-Mbwwc8In9N9MzZz2Xs1DZizuckq75KA-T1HDuTyusps9ydNPIOt6Nf1WD133XjdhXmYAuN4v2KkQYbw9WNPfczPDRl5qDe91uZhr3wX8WljaUUC0jHKRkt_Vb5CAUHc9QY87DuU1sNEyH6JwN-3LbZgDWL33cwAyL6nURqLUvptpBTH_PW_XPMtyxDtXpoTT8d_sdDlXNCgO-hbLiCVrW-p2lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfxXKFoqlhqAHjPZeM1g0sLBI1Qd3X39-28W63L2zqENDt6RVQO_o3SBDoZWdugJPgaMep-G0K785TPmzLpGCMDEomy_FpiU1YMXxp9W0BDsmLpdgoKDQ9iXQmNQsnrUiD8FcPl7IjACP0zkLqdiS2g2-lRxJI6qq6Bj6eTtrXHZ7WT-9u-5qFlcIBrO0x8daSX3YiV2lNYQ05iBqT0TcxzdaIgYsV9BOQCwp7bhQWMzYb8S34Kws0L_Dxc_dXaCqx62oDl5xcWpKYb6WeRqyb7WyXfL73fc5ifGYGDyTaYFJnwe7TmFd0fXMRAEXHwd3mAU1qGM1P-IMoGl_tuKFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیوفیس جدید ارلینگ‌هالند
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/104441" target="_blank">📅 13:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104440">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5669817976.mp4?token=ThiDaQuJUVJXWMt9auOR13jpe6E_1xVG4wx6-LcHFKr6Sufpy4uxQl8JL0s-LwcNfeNHuA5pkbu8alvOIBjliMBCUmDJKYydDdxVo9DOTc4HzN-SrTEqK4p3rzBlSe_h7OgT8dC-sPYXhORWce7mX4-XeS6og6TcpS2ttIEx6RFzr2KZRalMC7VpEsfE3v60fvzxS6QS6X9q47DIyVkLpEt1ijiuTe6hh-DP810SJ9j8tOsjLfLeaGvtEhjPbHQdCJcmoqLcNf3wYT9lGbFd4QJVm3IAwOQPyKGdcuIab_Iyvdx72akRYJQUYg7QhQETR7PuHYEvtwzQPgElVHxnMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5669817976.mp4?token=ThiDaQuJUVJXWMt9auOR13jpe6E_1xVG4wx6-LcHFKr6Sufpy4uxQl8JL0s-LwcNfeNHuA5pkbu8alvOIBjliMBCUmDJKYydDdxVo9DOTc4HzN-SrTEqK4p3rzBlSe_h7OgT8dC-sPYXhORWce7mX4-XeS6og6TcpS2ttIEx6RFzr2KZRalMC7VpEsfE3v60fvzxS6QS6X9q47DIyVkLpEt1ijiuTe6hh-DP810SJ9j8tOsjLfLeaGvtEhjPbHQdCJcmoqLcNf3wYT9lGbFd4QJVm3IAwOQPyKGdcuIab_Iyvdx72akRYJQUYg7QhQETR7PuHYEvtwzQPgElVHxnMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
ادعای عجیب و قابل تامل هواداران استقلال که مدعى هستند كه كيفيت پخش بازى هاى استقلال پايين تر از پرسپوليس هست و اين موضوع درحالى مطرح مى شود كه بازى هر دو تيم در يك ساعت مشخص و در يك ورزشگاه بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104440" target="_blank">📅 12:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104439">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcwhlQ5kqGu9sNo2pm-cofQ-rm7sZ0Efs3RUXpDFrzasf6Z5EBhrX51_BvtWyxuy1zC2viRHIaH8h-LKI7dsADR9vRvPRYdFRbanH2Mph70VT_QNBSVbDN5-oLnxS4P6w8dYrCQiXes1PnYVEkeai4J-0P0ZdFI8sf66lnEd3Eb03K-Jixm7On72zIdzWgoNwm-hU0AbmHMQ63e640ffJzlo4nq_mAgFtzigC6_pf8rYEvQD2JHVcz1t-z8gjIYgpmOgABvvXeLzgRE1puBh0_MeIzN7Ml4ZbXd8wDhpT9Y4_caLU3xGqEl0osFuCkhwWLX1RzU86-zKFB3EKi2xuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
لیست بازیکنان بارسلونا برای دیدار امشب با الچه بدون حضور بالده و رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104439" target="_blank">📅 12:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104438">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03e1a23b0e.mp4?token=ZmwSjfgjWWL6yofMpfeJAMsCM5zR1PCUTk5f0EsRed3bVrMCwn6Jy8mXRZGrTCJfxQlEisluXSxX6Tyfed505QJQFKuQ1qxKjN66b1M1pJhCEM59FxBvTihotPoVgNHI51y7TJ0JfaFv2jw7S3xrK1-GsI65CUAJo4AWetjEKqYBigJ0VNsgAYeWK2cibwRaqGpmoTiaus23NsZmwaqfHCWs5FU3HvOtY2MlJN0NQFqncRABnAMZQ3By1yQa__8beMr4cJGc1IlGhqMWOXPCDT7vTv9Xp23ngV3P2XDL1S4HHWenOiE1XYcMVdYbb6moTW68x18ahKLgi2IKe-9DJXJyvU5wq2wLqEuxky20KrywHcLCWVI9C1gADH3DUdg49Qh1RjpdQJYm7IeekzqUx30P1K9xS0ta1W4RvyhfvNHhzJoh6E3AIlCTFM3J_kLXAjbYL3ppzsHcOAEeI8duLkQb_3zbIy50LFngKZNrYPISflRQPKWV8j5BIo8BOJLAcK0ywZ2d72z3MQRvacD2Gm-JM0V4A0sTPULNLBa9xwyMmhzyDPFbtYKvdQPfcx_mx79zTL9S7AUDuYjKKNpObsMxIrKabknYC0g0EV10O4DOuA9qSTBx-xE5XddQxFfDNuge1MXahPARDKfHQzyjDHpLLaxdu_oiCQ64HH7D2Bo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03e1a23b0e.mp4?token=ZmwSjfgjWWL6yofMpfeJAMsCM5zR1PCUTk5f0EsRed3bVrMCwn6Jy8mXRZGrTCJfxQlEisluXSxX6Tyfed505QJQFKuQ1qxKjN66b1M1pJhCEM59FxBvTihotPoVgNHI51y7TJ0JfaFv2jw7S3xrK1-GsI65CUAJo4AWetjEKqYBigJ0VNsgAYeWK2cibwRaqGpmoTiaus23NsZmwaqfHCWs5FU3HvOtY2MlJN0NQFqncRABnAMZQ3By1yQa__8beMr4cJGc1IlGhqMWOXPCDT7vTv9Xp23ngV3P2XDL1S4HHWenOiE1XYcMVdYbb6moTW68x18ahKLgi2IKe-9DJXJyvU5wq2wLqEuxky20KrywHcLCWVI9C1gADH3DUdg49Qh1RjpdQJYm7IeekzqUx30P1K9xS0ta1W4RvyhfvNHhzJoh6E3AIlCTFM3J_kLXAjbYL3ppzsHcOAEeI8duLkQb_3zbIy50LFngKZNrYPISflRQPKWV8j5BIo8BOJLAcK0ywZ2d72z3MQRvacD2Gm-JM0V4A0sTPULNLBa9xwyMmhzyDPFbtYKvdQPfcx_mx79zTL9S7AUDuYjKKNpObsMxIrKabknYC0g0EV10O4DOuA9qSTBx-xE5XddQxFfDNuge1MXahPARDKfHQzyjDHpLLaxdu_oiCQ64HH7D2Bo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
🇮🇷
صحبت‌های زیبا و حرفه‌ای بانوی هوادار ملوان درخصوص شرایط این‌فصل تیمش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104438" target="_blank">📅 12:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104437">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWFRwhgg5j6Vk3GpSyufZn2eSobc7SD8hOX6klcU36ynr8O23m5PMDC7gTJoM4EGmsrhWKIjtoOUut3-r2KtFyY3WKN7xPV_y4w20pgT8nZBUTMzVhmorNnWQPIcOZdxVpi-Zp_w-zxcXL9Sf_aa2FxO0PaBDk2VcGMnCHZfGsfXaiyKTNnmSjjtmj8UJGb-519oFFweYgizN3fqjOOOHDjLRXdATzv7Z4_4vNrHVl3KEvt5gfYOCXmUyCnEFD7UGqxC1Q3dylUiKf9ILXHA275OCoDBgrlGjrEGKMsm8RjkqFiluWFJYYkRTgCSnaX0a40MFu3Lz7m-kJ_hhI7aMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
مدیرعامل فجرسپاسی: به سازمان نظام وظیفه برای جذب علیرضا بیرانوند نامه‌زده‌ایم و اگر‌ مورد موافقت قرار بگیرد، از ابتدای مهر در خدمت سنگربان تیم‌ملی خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/104437" target="_blank">📅 12:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104436">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1928a613f1.mp4?token=FKSOfVCWO5b256h_Xst6JfIQYZalrLXAgBXLsCjnim9kAnfz1fraR_sAZw6nLlMwITGgJXw-cLoFaa1CWlzj5sQBtxxZ3insXjzbfduD_BaoY0DgY_nuMq-V8c_nQPgkP6pI0mbghMMQ_5bedUNtzCwZz5jZsixctFKoG0HdPoLMOZhN8bA9Lq03a723sgRfp4Ox9Nkk8eKON0czqD2EZit6xiytnL0RoBmXqSiD1B-kk3rEQxki-1WT85Ma3jPi64Jk23BzfwnoiVucE5OLEAbF9hKoXLeIh22IG3OpO_jknVOZwvDH-rEtFQ699IP9K5ipgEC6dr-7S6CIU8F8Fayuu7wHRFteASUrmcMJJCUx4D6i5odZ7bQEoC-tLXuIJiZlnY0oM54oXud3lmXyKjRvBK5tOxmBASCLzwopnHMQkEdX0lvDFTlDADBL-KRAwcan-bYiuWZVTCgBElZlVjFUKMm8iqHECO8fSv4WsSZzikzqjpqM78xO-tyDI_YuZ7XZ3SYSe2uPkFYbw1yMKyy-QZoWMgjo_C_XwolwPqi89hdTJQQiehLHIfOBUEi9MvLVBbitC_8Ap0_CgUgkQ4Rn58pphfnn7rHO2hyCGVqjesKMpaT2tdEerVJ_dhwuNNbj52TZ2EEElLx6t2Js51Tizz8YGLhQFUmMN8SIOKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1928a613f1.mp4?token=FKSOfVCWO5b256h_Xst6JfIQYZalrLXAgBXLsCjnim9kAnfz1fraR_sAZw6nLlMwITGgJXw-cLoFaa1CWlzj5sQBtxxZ3insXjzbfduD_BaoY0DgY_nuMq-V8c_nQPgkP6pI0mbghMMQ_5bedUNtzCwZz5jZsixctFKoG0HdPoLMOZhN8bA9Lq03a723sgRfp4Ox9Nkk8eKON0czqD2EZit6xiytnL0RoBmXqSiD1B-kk3rEQxki-1WT85Ma3jPi64Jk23BzfwnoiVucE5OLEAbF9hKoXLeIh22IG3OpO_jknVOZwvDH-rEtFQ699IP9K5ipgEC6dr-7S6CIU8F8Fayuu7wHRFteASUrmcMJJCUx4D6i5odZ7bQEoC-tLXuIJiZlnY0oM54oXud3lmXyKjRvBK5tOxmBASCLzwopnHMQkEdX0lvDFTlDADBL-KRAwcan-bYiuWZVTCgBElZlVjFUKMm8iqHECO8fSv4WsSZzikzqjpqM78xO-tyDI_YuZ7XZ3SYSe2uPkFYbw1yMKyy-QZoWMgjo_C_XwolwPqi89hdTJQQiehLHIfOBUEi9MvLVBbitC_8Ap0_CgUgkQ4Rn58pphfnn7rHO2hyCGVqjesKMpaT2tdEerVJ_dhwuNNbj52TZ2EEElLx6t2Js51Tizz8YGLhQFUmMN8SIOKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
خاطره شنیدنی حسن‌روشن پیشکسوت استقلال از دربی معروف شش‌تایی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/104436" target="_blank">📅 11:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104435">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d84a4cfcf4.mp4?token=TZBlYY-gn0N8rTuhiBJ-jyfFGdE2PBR0g_kK7CF1OXSV0r9f9rPvllt_iIVt7M7eLVZe9uunrXpDpQAUcVJ3OSBJr20ZMk2DIZTbgDzthsA_fFJ8gK_Ow862aIJzvUCadYhssmy97l3686ygOqbqjMyZTLzc-DDjVxh7qqdLt1Qs6EKn6--_a_wLSeQGdMfufDsQHP5PCayZmWilEKq9-aFDytq39pzvtQJtZm2aiJF8-gNFkUZU804SjmhWgoVm9JH5wWx6ZDcVvs-aiGlTxvQhn87L29JieGj7n9B2uT_w_M_RGVmmgzftRi3KY2VwOjCYtAeZq5pwSpbjRsOPvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d84a4cfcf4.mp4?token=TZBlYY-gn0N8rTuhiBJ-jyfFGdE2PBR0g_kK7CF1OXSV0r9f9rPvllt_iIVt7M7eLVZe9uunrXpDpQAUcVJ3OSBJr20ZMk2DIZTbgDzthsA_fFJ8gK_Ow862aIJzvUCadYhssmy97l3686ygOqbqjMyZTLzc-DDjVxh7qqdLt1Qs6EKn6--_a_wLSeQGdMfufDsQHP5PCayZmWilEKq9-aFDytq39pzvtQJtZm2aiJF8-gNFkUZU804SjmhWgoVm9JH5wWx6ZDcVvs-aiGlTxvQhn87L29JieGj7n9B2uT_w_M_RGVmmgzftRi3KY2VwOjCYtAeZq5pwSpbjRsOPvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
کافه‌های مردم پلمب، بساط لاکچری بابک زنجانی پهن؛ عدالت یعنی
پشم!
در حالی که کافه‌های ساعدی‌نیا به‌طور کامل بسته شده‌اند، بابک زنجانی، مفسد اقتصادی حکومتی، شب گذشته یکی از لاکچری‌ترین کافه‌های تهران را با عنوان «VIP» افتتاح کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104435" target="_blank">📅 11:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104434">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ff1QydhtxWKsrEWo8XN3J0l0nfROwQiY6lBaVr_Ubm8s55PQ_EHuI9w-qKDY1ZRYRUtv4is36HrZhRti08Bzk7aHo7XZp2ijYqBivPZLilFqn93unC-qWg3mBh96YiltZfn7kgL81xtwm4XtSYKrDK0J96eFdgKpVvAKRN0b1dEAB2CCp1V6HWe_B0x3ONT187U0Dg3aBb5eAKvFgEzdiCAtjhs9RuWB6eFei2Xny9IdYLcyBjT298EEhxDeg-n-7rvxVthm2MeJ0x1CKHx7ATuQSBK2JmRwIiaAoPrJouVJM7ngNQWsVWvYByrHDErPS9SQnrWkTbbm42XsyuY1Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚽️
مصدومیت وحشتناک چادی‌ریاد بازیکن کریستال‌پالاس در بازی دیروز که فصل براش تموم شد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104434" target="_blank">📅 11:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104433">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if3pLbPNZHfrS77APPTGE0auNu_K7B1ZLVqgSV_ND9zJ4pmw1nJoJBgHO40LA2I8Up4u19fSLCn_O8LCpyqakboRyml5ML6IjaS4iWP8M9YDCnzbWHJPHZmk7aaDRIHYCmhO4kH3Ncfesea2-Irlyp_IZeH7YtilOoUQQbiJDIUsErhX8CF9chtKIaFRQ28sVAVpFvI6x-Ytpntgdor4dHwWer9zJ1M-wo4aXYsmVDqrnN_8PAfvy9EL-_ug0gF6a7IfZAYnZJHsYhcSQXIIukogcCOJr77Gs0w6yZyD8RSe37GHp1hUa1BImPXKZ46i8-d4Ptv7GBjchvh4hPIIAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
باشگاه استقلال با انتشار پوستری برای بازی با سپاهان نوشت: نبردی از جنس اصالت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104433" target="_blank">📅 11:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104432">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7773a1e510.mp4?token=odzuFcyF_eZ5A1N0k6NNnuefz83LaMOGJElwP3SOsR1hCBYkmcAeaDNKGzvM5eTnWDVMinrM8yS_4QFPCQh9H7ULb-0sN0fmK-GSKkMTPjbJzxFL_k1eH09va1F-1JCzWEvy26M1hOMeYrbLTZwpqVijmDR17WWiBVS3iOQe03JE83j_O0qHYWtQE8fo8rjBOifkLP6frQCv8gwO3Vv1oAhIcTW8HzaX7iVnhDfPwiEzWXoZxxI1dKmIKDJDEMO1sjdhCe1vYfWhhbkOC3QmU9XWC_KO1indMS70qmW4OkL5f7PerOdb09LdawdRQk-TMEmrhb0heVqmiDu8_y25yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7773a1e510.mp4?token=odzuFcyF_eZ5A1N0k6NNnuefz83LaMOGJElwP3SOsR1hCBYkmcAeaDNKGzvM5eTnWDVMinrM8yS_4QFPCQh9H7ULb-0sN0fmK-GSKkMTPjbJzxFL_k1eH09va1F-1JCzWEvy26M1hOMeYrbLTZwpqVijmDR17WWiBVS3iOQe03JE83j_O0qHYWtQE8fo8rjBOifkLP6frQCv8gwO3Vv1oAhIcTW8HzaX7iVnhDfPwiEzWXoZxxI1dKmIKDJDEMO1sjdhCe1vYfWhhbkOC3QmU9XWC_KO1indMS70qmW4OkL5f7PerOdb09LdawdRQk-TMEmrhb0heVqmiDu8_y25yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کریک بعد از شکست 2-0 مقابل هال سیتی:
این فقط یک بازیه، می‌دونید، فقط یک بازیه. اولین بازی فصله. خب به اندازه کافی ناامیدکننده هست و دردناکه، معلومه که هست. ولی فقط یک بازیه، پس یهو مسیر همه‌چی رو عوض نمی‌کنه، کل مسیرِ حرکت تیم یا باشگاه رو تغییر نمیده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/104432" target="_blank">📅 11:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104431">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/104431" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/104431" target="_blank">📅 11:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104430">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HptiEVJ3nRS-2-6FZBrab_3sq91lZem1h7zYGVv73L_TA8mDaLEwocG-U1hODfrGnLQd6ltSV2zQ_9QHXJTux6SZH4USheTQOISotIeWZgaVVWPEdaFiU1CSnO5D2iY7arB4jISmxx-dy2TBoKuxGtfyDDIAwFeuQfUgrgdYDHFb6FwL8S5xrs0uC27PMd8XjenZlMao56B4EJmj_7ueHt2E9xT3j8gCU5loDrGprYXoaGqHM2sLLXKXMXo7EXHlSD7zDM75bDBqNQ1uH5nawz6I9snQ7XO5ZRcuP6jkSQKZiyWgudOGo4Xmvl9EW2MH3ePuUhfn_dmP-LLtIGqJ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r1
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/104430" target="_blank">📅 11:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104428">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c490b878e2.mp4?token=hxyncpddpCIXFBNLXzQq37rMN2B7668QtXs0jz18U8pzS69FN-Zc6WZwbDKANtuMcR2P2R4QfVcMP5sC296rFL850ojZdCtfk9DVMxmMW8pUEH9AMi-TCFWlysiddgYgMO035dqiCR0On5--AcoybI0wum337dRMCtJkpwd1dYP8k8yWT5ZaDDNu272aeHFhAcuQx2eI04_b-e3Pl4-1zfYQABjOLC-qRLc__TtNc-kHJbg5YKuvDYpe6xJrrRVzDh3Ma-H56WaS08uewcLrDs0P52XGjg8jZju2h7cYnmmcOuAvE5rqN88S5kUIyidOA28AjMgWtbSxAFlzL4-Htg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c490b878e2.mp4?token=hxyncpddpCIXFBNLXzQq37rMN2B7668QtXs0jz18U8pzS69FN-Zc6WZwbDKANtuMcR2P2R4QfVcMP5sC296rFL850ojZdCtfk9DVMxmMW8pUEH9AMi-TCFWlysiddgYgMO035dqiCR0On5--AcoybI0wum337dRMCtJkpwd1dYP8k8yWT5ZaDDNu272aeHFhAcuQx2eI04_b-e3Pl4-1zfYQABjOLC-qRLc__TtNc-kHJbg5YKuvDYpe6xJrrRVzDh3Ma-H56WaS08uewcLrDs0P52XGjg8jZju2h7cYnmmcOuAvE5rqN88S5kUIyidOA28AjMgWtbSxAFlzL4-Htg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
خبرنگار: رئال مادرید ژوزه مورینیو رو چطور ارزیابی میکنید؟⁣
🇪🇸
هانسی فلیک: امروز با رئال مادرید بازی داریم؟! در مورد الچه سوال کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/104428" target="_blank">📅 10:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104427">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c2144e6b.mp4?token=e8icDRuEAKm2TicwqHcsOfpP38ZY6jBP2MKvZbmJrX0uATth2z8h539XWd3jIg8TvszxF9MYLM3UJrjfZ9Q8WlK-31QqaUaf2CXqEhZM2KiNadGfM2pqsxTpab5N2dNHzfKtRRenLCWwJK4wCgbvIm2JHA6JK5IBwOFNbue2AZ_DfpsdTV0k-Q-ik4mRd4-7OUxI0A7Dp1z30zw9uMZh2iWvHki8ZKPKA58xinNYNU9Hfr60t3N9MZwDTIyysHOQ5kKVtfuWX93jIr_x1IicL0armFSz6NmwNAsjBfB8n8ri1M0LHgKNz-KErhSpUpxo0LONH-w8PGZoasVTqrRkqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c2144e6b.mp4?token=e8icDRuEAKm2TicwqHcsOfpP38ZY6jBP2MKvZbmJrX0uATth2z8h539XWd3jIg8TvszxF9MYLM3UJrjfZ9Q8WlK-31QqaUaf2CXqEhZM2KiNadGfM2pqsxTpab5N2dNHzfKtRRenLCWwJK4wCgbvIm2JHA6JK5IBwOFNbue2AZ_DfpsdTV0k-Q-ik4mRd4-7OUxI0A7Dp1z30zw9uMZh2iWvHki8ZKPKA58xinNYNU9Hfr60t3N9MZwDTIyysHOQ5kKVtfuWX93jIr_x1IicL0armFSz6NmwNAsjBfB8n8ri1M0LHgKNz-KErhSpUpxo0LONH-w8PGZoasVTqrRkqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برونو فرناندز بعد از شکست 2-0 مقابل هال سیتی: "همون اشتباهاتی که فصل قبل تو هر بازی بیرون از خانه انجام می‌دادیم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104427" target="_blank">📅 10:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104426">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👀
💥
پسر رونالدو هم راه پدر رو خوب ادامه میده و در زدن ضربه‌پنالتی استاد شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/104426" target="_blank">📅 09:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104425">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f6325ec27.mp4?token=vrJvFBUwb3YXbC0qUlSgfuEWINSNJ-jtAdZDxDfAmWkMfPbN6iDeNfXgPXEY-a9ANAqjTysoCJZdzmsqJnd37tRudc290eY1Urw9iHM6wHOaebroPu7DuKXYcnxRNYJ6V0DtLu3JD5qbd1ulE2MOVbp2czjITPM0weJDOlqiQm6uN-d4XLzIh5rfqzzfdkET2Ykfdb5bXbizP9-ev18CY7F_M51NvBzpaML8nBnrN4ErTOwxe2OKU5MJ6mfRUZqlRhpVArBeAQ9YwU2hYmsPqD3Q6cH0kBfZOLWcpxAWVJwjYX7Rd1Ll-0O6oa4-mcT1DpVUFOQrexdGauapeVi-1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f6325ec27.mp4?token=vrJvFBUwb3YXbC0qUlSgfuEWINSNJ-jtAdZDxDfAmWkMfPbN6iDeNfXgPXEY-a9ANAqjTysoCJZdzmsqJnd37tRudc290eY1Urw9iHM6wHOaebroPu7DuKXYcnxRNYJ6V0DtLu3JD5qbd1ulE2MOVbp2czjITPM0weJDOlqiQm6uN-d4XLzIh5rfqzzfdkET2Ykfdb5bXbizP9-ev18CY7F_M51NvBzpaML8nBnrN4ErTOwxe2OKU5MJ6mfRUZqlRhpVArBeAQ9YwU2hYmsPqD3Q6cH0kBfZOLWcpxAWVJwjYX7Rd1Ll-0O6oa4-mcT1DpVUFOQrexdGauapeVi-1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلزنی‌ساعاتی‌پیش لیونل‌مسی در شب باخت‌ مجدد تیمش اینترمیامی مقابل تورنتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104425" target="_blank">📅 09:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104424">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/995ef211fc.mp4?token=BMFWZjObKZ4u0FzSgFxnThgae7_G2lwNMLepqCVvp9PAAyg9eB8QeCaI3MRmj9UD8z13e9ou8I--mWIsWDTPNf2jJCpTw7efZavn3btoHWGd0-HPPcXI2qME4qJ50iouX22kLKCswNkCFJlywOwGX4AUCKm7ZD0fCXtayuvZhcj4tT9zRE17I7R_MSisMSP7qFG43aEQQ_PlXC7jo9xIid_1LNZm4rh1qfvNSQbFsn_O_wauVeJ_DkFVY2bIkuUaL3cLshhdsVHRGdyGZNZvvFa0Q3hMGBfCCqIdu0_HT6BDN1QTEiZZqoSXeysDHNaG9eNKXbKELm6NuQ1oPocUlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/995ef211fc.mp4?token=BMFWZjObKZ4u0FzSgFxnThgae7_G2lwNMLepqCVvp9PAAyg9eB8QeCaI3MRmj9UD8z13e9ou8I--mWIsWDTPNf2jJCpTw7efZavn3btoHWGd0-HPPcXI2qME4qJ50iouX22kLKCswNkCFJlywOwGX4AUCKm7ZD0fCXtayuvZhcj4tT9zRE17I7R_MSisMSP7qFG43aEQQ_PlXC7jo9xIid_1LNZm4rh1qfvNSQbFsn_O_wauVeJ_DkFVY2bIkuUaL3cLshhdsVHRGdyGZNZvvFa0Q3hMGBfCCqIdu0_HT6BDN1QTEiZZqoSXeysDHNaG9eNKXbKELm6NuQ1oPocUlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
جنجال‌علیرضا کوشکی مقابل نساجی که باعث نیمکت‌نشین شدنش جلو سپاهان شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104424" target="_blank">📅 09:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104423">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
‼️
⚠️
رئیس مجلس عراق: قالیباف توی جلسه گفت خلیج فارس منم حرفشو قطع کردم گفتم خلیج عربی درسته، دوباره این کارو تکرار کرد و منم دوباره گفتم خلیج عربی درسته. قالیباف در واکنش بهم گفت مشکلی نیست شما اسم خودتونو دارید ماهم اسم خودمونو!
رئیس جمهور عراق هم گفت چطوره بگیم خلیج اسلامی که مشکلی بینمون پیش نیاد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/104423" target="_blank">📅 02:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104422">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qj8LtqIlxWHTPo4X178LPktTRNEUujg-4QkQmTmWgM4YBKle9wpVtWViuIGHN2chWIFn9tCg4Z_RazwQhxxjs8x4GdSGLPlcmZbaUuPLigTo8i1gbsjALnOy8qQds0mRuPeANCz2lxUzDGCnK0bTr9fg4dD1O67VcGW40d9q-onMCO3e8DiraQC1VxgqjJnEOCCzPuNTF1iIoED8Z0G5_qfQZvnV6ypC7Z62XW9MViu6TRywp8lh9WsJ_1hEJmZ-V0rffB80tViE_pQetW77-rk0fW2xGqbs7_pn3mCPa1pGS0Py-T9PZ-am2rWsazvTpLPFprUwmwwuge_93DyiGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
لیونل‌مسی در ترکیب اینترمیامی مقابل تورنتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104422" target="_blank">📅 02:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104421">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPTFxZCnNEeAYxCo6sfQg6fMAGxun--VnEXSe6paQcqzgwuIzUoczbxEmY1k2i-wWRHS9S4ufqcn0Q4ikKPbowtWINr3AjiXIhVtKRx_oer_yjhIFBTAmHjLG3y4Yr0tbcNvf4o8jGbxE44v1O3g585fs5LzrBMI7kzQuJ5B9eeyw94_N3c6E_FiyhGHzn4QgoOOBHZtgrxxEu6QQGNOr-tK2x7vTnD3EzG8fHPIIubHSngQl5yQlo40r_aucGmNV1jc7kf7R96uSk33ea5PA0xIkbMac9daSt-CYi_RTt9rLyKEMJxNhkteh22riQ-Ocz83X7evoASjLYLKVSpOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
‼️
🇪🇸
صفحه باشگاه اسپانیول در کنایه به قضاوت داوری بازی با رئال‌مادرید:  ‏" چند بار باید خطا کنید تا یک کارت زرد بگیرید؟ این سوال رو از طرف یه دوست مطرح می‌کنیم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/104421" target="_blank">📅 01:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104420">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8znfux4qOm7bBgmi6srqnL6bwDqmLpKpXkQC5UpvqNQLkzKPSepQnMfTIXcbaGh-xwBSTLaZe4kA44ca0sA7TeSuAVTbb-YEJLCYrKWLPUnU37sB-OoR42sFRiHnUC_6SmKBvoQurDJRvSga9Xu_4e3lf7dHP-RaDKs3CrEp2-eyHR3TRSWSEVWKrnSbSRWN2X8n43qZQKwJSt0Wp5Ff2lkIEa3wJusj-ILQvlT33NAhHcxG3nVbViley2Ab5K8EtiB618yBMUv28zjRUTXypmN3B0L8NkMnjUn9CFQiQ45Ae5pbPNrHNflzrAx3DFOUHnmUM16isyejEdf41FfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
‼️
🇪🇸
صفحه باشگاه اسپانیول در کنایه به قضاوت داوری بازی با رئال‌مادرید:
‏" چند بار باید خطا کنید تا یک کارت زرد بگیرید؟ این سوال رو از طرف یه دوست مطرح می‌کنیم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104420" target="_blank">📅 01:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104419">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIte8e1z5aJp9ggRDx24N-NGotkUjn5dbhDWGe95UFO5PZcRctdJRvVRfybSHPMmalinqROwc5MubXArWhj-FhWJfyyhsafADSybMZQzSXVB9IX3LlIc3GdNf4xDPBpnOQV0n1yq2kCz_unvjq0EoveRn7REG8TiVFUqoChrbelJfiI2fDBYboByF1GdCex2JquqA9AFvZcsQLm1lyRsLAd-YGcuXdJG9J8N2UTXF2_v_1twHAw06TZrcoaT-3u5amnT-YhJBRYjMvBL1sKilvTh2xHorfT0ONzGZV1o3tb5_4AHxuPcRA_iEacxKLCp__UysXaYngj1gbs3ZZv7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
👀
نجات‌دهنده ژوزه در قلب بارسلون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104419" target="_blank">📅 01:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104418">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ktxcl9FDkMFyHEfN4PeXsizNa1T1C4Mo3T6WiNIn4k1F59a8l3KFcJlnHcvEkogcI2o_s9D_sywt-Ac3rsibpDShZ1WUL94ah_USnA9B3sJlBFmGGMWR-N930EUKaYMpzlFeKzlN6WXAIV6mnLEknqTDrPy1KLd1G03XcyNKeYO8gXgyiWM0Da9ECR6Xr2l7D_R1gHKNMcjhU-VSlAfhVRql1JYiVIIP1tnzefYNZrskKda1hl87Cb6KQswbPhyBJNHoiks1N82A1VwwnDKN4OLHEs-8D6cuzOBm44S_F8GYoa9fvbEWFST5gnDadAyAv8tQJScl2_LOTxYL0TCvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
⚽️
گل کارلوس اسپی در دقیقه 89 و 54 ثانیه.
🔥
ریال مادرید با به ثمر رساندن گلی پس از دقیقه 90، برای دومین بار در تاریخ خود، در یک بازی افتتاحیه از لیگ اسپانیا به پیروزی رسید.
🗓
پیش از این، این دستاورد در 21 آگوست 1999 در مایورکا، با به ثمر رسیدن گل تعیین‌کننده رائول در دقیقه 90+3، حاصل شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104418" target="_blank">📅 01:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104417">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">💎
میدونستین تو دربی بت
✅
با شارژ بالاتر از ۱۰۰ دلار ۱۲۰٪ بیشتر حسابتون شارژ میشه
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104417" target="_blank">📅 01:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104416">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/104416" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر D
erby Bet
✅
✅
✅
✅
واریز و برداشت ارزی و ریالی
‼️
✅
بونوس 120% اولین واریز
‼️
✅
بونوس برای 4 واریز اول
‼️
🎁
بونوس ورزشی هر شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🎁
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a31
✔
@DerbyBetOfficial</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104416" target="_blank">📅 01:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104415">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cd1_bJKDcz_yvbbUWqjLxiRKm24XC9dU_sBeheeSgTa8GWKkLxF-4XvR38kGRMmHzRj4g2pqETPgrLuOzb5vom6M2wO_s2aTODdfEzkr7TRHG_B9FAG_KhxJXl7ezbRGUny6G4JS5uIJ9Ltnj-qlmJuolGIfYdaO6L9115Tb1GFqpHG4cXXilNGCsMT9mHJyYVt5Nhw9cKYMEET9IdQBytDgedHJrT2TF-I7qUEx-1ICfjEKNgk8p9OXg1YwzFMEDGo8jx7w2gXWvy8LDE-S7KpwbNkN3PW203AFx5z4nH93v0tmDdTOBl46P0mIpUOkfYt60C5QuRDeRqCOo1NI6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104415" target="_blank">📅 01:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104414">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYbrjm5ozjoCd08Lhq3I__dX7WrfuW2EdXGRn4yhVyw78BdDlzbhIbmib7B3qwjUNI1qYV0Mtuo1iGRV9gUq2VgtltwgW1I2nMFn0-oWR9P7wIssTQAZjCaJ21ybmFazo1bLxrST7BMBvbbX-2KI_QxjTSzbf7ESKjx9f5PUW1t1u9zffUTF32wT75aHGOhD_xqp6TBVaGdRscLsgVyZtA7Pe13q22uY8uo54ulLJMReZjZdEVSoqJMsxZl9yIGWZ8yqtEIvAcQka9lUfduXeIUsMKJsq042OUA5Z1rpxuC1_vVOh5MZ1-TKaFDZ3nrbfChiHbsbGdoSTtLklnvTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
هفته‌دوم لالیگا؛ پیروزی سخت و نفس‌گیر کهکشانی‌ها در خارج از خانه؛ مقاومت اسپانیول با گل یک بازیکن کمتر شناخته شده شکست!
🇪🇸
رئال‌مادرید
😀
-
😃
اسپانیول
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104414" target="_blank">📅 00:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104413">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/69ada12902.mp4?token=ZqzQOO1Vt1fVjAqR9N4jJ0Yj-NaaVtUEwx1-jk15y8TY6Q1Dj4SHShza4txsG5LYkdcnggUOsgnkWr0m63IwCJptP20L1hvzJfBXEAPZLJsC13HycPY-4Bw0GuolCPz6Xs01n2e8UnQa27oo0aK9WGTc6yqpzZjmxmuMsg1fybitZUC21GFHIXZMsufboVDWrqzVBxr1tIplB6KX2o737YGfa_RlX4wfchZQMS_zyYVFJ8IJZXktNvtklpZBNyWhCeUBXXOlF9e_7EOAEDy_v7hb4uWqTOpw0dVEAT4hhPowGgWdJOIs49JySZ8KjWJuJaRAOj2E915IbQNwAfqAJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/69ada12902.mp4?token=ZqzQOO1Vt1fVjAqR9N4jJ0Yj-NaaVtUEwx1-jk15y8TY6Q1Dj4SHShza4txsG5LYkdcnggUOsgnkWr0m63IwCJptP20L1hvzJfBXEAPZLJsC13HycPY-4Bw0GuolCPz6Xs01n2e8UnQa27oo0aK9WGTc6yqpzZjmxmuMsg1fybitZUC21GFHIXZMsufboVDWrqzVBxr1tIplB6KX2o737YGfa_RlX4wfchZQMS_zyYVFJ8IJZXktNvtklpZBNyWhCeUBXXOlF9e_7EOAEDy_v7hb4uWqTOpw0dVEAT4hhPowGgWdJOIs49JySZ8KjWJuJaRAOj2E915IbQNwAfqAJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
گلگلگلگلگگلگلگلگلگلل رررررررئاااااال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104413" target="_blank">📅 00:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104412">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اسپیییییییییی زددددددذذ
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104412" target="_blank">📅 00:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104411">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رئاااااالل دومیووووووو زددددددذ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104411" target="_blank">📅 00:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104410">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104410" target="_blank">📅 00:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104409">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">▶️
🇩🇪
🇩🇪
هایلایت دیدار دورتموند 1-2 بایرن مونیخ با گزارش روح الله مدرسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/104409" target="_blank">📅 00:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104408">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIQTZS7rvthPg4gAfEirAiTpZvq8Ju0q2vLmVXqbqtLOsyWSKeLhLN3kuiUNg9p549ihFVUkPhJPuhm_H6m5VwJwr1yYw6RJAVVX872Y8W9oPT9Kj4PlZbOec5CUd_t0UU2NLtK27WhkjBELhv8v0N7nkJFSqO55dRfzIfAnuGoB4y-HUEiqvxMWWFFCpljzyBf74Toxl05QCwp_F82xjhOTSHdypsWgZtwTnym9VEjG7WI4OYu6x7W-b4bb_zS2oKxOcDYyYGvB5IPcZZeVv0qzDpco6fCyRAelH4kZvKaoKoYFted-_kf6ox5wPQJTzmPkOdw4JTiKVZLlui2ayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇸🇦
رسمی؛ داروین نونیز مهاجم الهلال با قراردادی قرضی به الدرعیه عربستان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104408" target="_blank">📅 00:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104407">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RP1lzsuv_-IIMTHuL6Q9DpyhjBlmevr7eHftRw84XzSvWnYxk2KyyKgkuoghpkpL9KRqSfos1HJWzfIIlslnpvHYeKnI9sflr_fv49mWLipCYgitzXscQYvAwh0LZlltSp_n1OdEHYDdqUhLhBdsfkuglj6Az4hE0AXU01KMZmQ3xO4ButibkbrrAfbjPypr3i7CKlBnWR7PWgYqGkit8kWwnPfKVl_9Drnc-IWw0JFJy8GETtSjezFd3I_gobdynRwWO_T-M0AjcdN8KlqMpAkbpbA1WBhY7Iv5E39o606foR1b_gMvDC-YlAyH7FKsrIkx-ti05WGTLkDmwclu4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇩🇪
سوپرکاپ فوتبال آلمان؛ بایرن کمپانی اولین جام فصل را از رقیب سنتی گرفت؛ دورتمند بازهم مقابل باواریایی‌ها ناکام ماند
🇩🇪
بایرن‌مونیخ
😀
-
😃
دورتمند
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104407" target="_blank">📅 23:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104406">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/06034109f1.mp4?token=X6BzSsVBRaQlL0RhfDVWoVFFssDI2PApsKEyTju084Zv7uU-094GGC48-SwSIvYHppw9f1c2qmKmshMEXneCOMTuOtXjdeQJjQTEby1v5hyZ0jL55gXg5D56jSb76lc-WvLJXw3jv4dlegCpkI1PI7lUTDBl9k4G8D3HOj3lnKycSldHgB1YPZoE8_XmrJ7Mmw9C1p4_bYVE_8zirCyCv0x4n8jbKjlDrEFB3ydMnVv1chToQk6JzeI36jz_xHPutTXYVwnBHKgs9SjnWUOEinxUTRrUBlW2Mby7SY2cyF4ldfu6SbcHpx_Km5MOiwyC-uJQYdWUEgCRU3wG1gANVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/06034109f1.mp4?token=X6BzSsVBRaQlL0RhfDVWoVFFssDI2PApsKEyTju084Zv7uU-094GGC48-SwSIvYHppw9f1c2qmKmshMEXneCOMTuOtXjdeQJjQTEby1v5hyZ0jL55gXg5D56jSb76lc-WvLJXw3jv4dlegCpkI1PI7lUTDBl9k4G8D3HOj3lnKycSldHgB1YPZoE8_XmrJ7Mmw9C1p4_bYVE_8zirCyCv0x4n8jbKjlDrEFB3ydMnVv1chToQk6JzeI36jz_xHPutTXYVwnBHKgs9SjnWUOEinxUTRrUBlW2Mby7SY2cyF4ldfu6SbcHpx_Km5MOiwyC-uJQYdWUEgCRU3wG1gANVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇩🇪
گل‌اول دورتمند به بایرن‌مونیخ توسط سیلوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104406" target="_blank">📅 23:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104405">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1aebcbb396.mp4?token=pnZHBmI3nxrsK3cqwHdvMchzi2zPiqbgmEZ2XZ3P1pvrJX4ArzQKRZ6KX_IDAqIDpN6G3e7qqsyNop5FUewGkCNHqcIgvl6nrvQfHNMcFlqKIaC-Vi45eMdfkb2IjAbXPv5hxqxzENIoiJCrc0kAyJ8FRoDaf9sbK18C99BuHiTBs-6hnw_u7Cjza9AlxkKE3dxWdG064lRWz-ZWaVYizsJFTlJlxnknjoDmGUw5q8gSN7WKsdkGfo0iM0ZmBYJKcTqY7B9VTW75rgq8sB0FydSytIQwCaLvBre0weaYFvfMLZPeg0CHPx7pfF4s-GQ4Oaef2a8afLVcJClArX0Iow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1aebcbb396.mp4?token=pnZHBmI3nxrsK3cqwHdvMchzi2zPiqbgmEZ2XZ3P1pvrJX4ArzQKRZ6KX_IDAqIDpN6G3e7qqsyNop5FUewGkCNHqcIgvl6nrvQfHNMcFlqKIaC-Vi45eMdfkb2IjAbXPv5hxqxzENIoiJCrc0kAyJ8FRoDaf9sbK18C99BuHiTBs-6hnw_u7Cjza9AlxkKE3dxWdG064lRWz-ZWaVYizsJFTlJlxnknjoDmGUw5q8gSN7WKsdkGfo0iM0ZmBYJKcTqY7B9VTW75rgq8sB0FydSytIQwCaLvBre0weaYFvfMLZPeg0CHPx7pfF4s-GQ4Oaef2a8afLVcJClArX0Iow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
گل تساوی اسپانیول به رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104405" target="_blank">📅 23:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104404">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI-n4Vownr_hcsImjDCXScQSdQnLzVWFjiWbN-t3TgTnR8vvNn_c1A79OO4hOfnMkIWm558uOe9CqP720OeyN9BqU9YajMaVpvXkS1vklXRYadW3efdx8TDWz2PV-gsAb10knQzS4JYrJRtYBfzTcG62gEhBb3BUMxnDTx44UZeetrYLU_8fe3t8XZXzp2s0xmDTdNZVlv4Bme1vXZMthrVZx1EUssNzCgk08RaFjSJts8HYl6vqaq1i61kN8GZsn-bDfIii7tLlKqeOk24DKtAUKNANk3d4JRN7u7g9KCisdQC234lO1U5N1EID6dgdDpANFf1XwnTl0cpqbOIZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🚑
هویسن بنده‌خدا اوف شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104404" target="_blank">📅 23:27 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104403">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64261a7aea.mp4?token=rDiKSpxg7R5FFgI-juTUq49EH5itPUVg0in4Q-BY12aSnyMr9W_mzRwVYjOzgEi17wzJa9S5mgD_RLRpu8LYfFl4dS3HBnBxxXf0T1-EUOrn83XkEPMcvwKSx2Xky0UxKYkFG0E0IEbwSPBpPDGyBRz45v2jfQcjg9SkXFG3zL5Shvyt059N4xFCHQqktthsAF_nN86sk9cV0P0NHw047ZQEZZaLIEqb23VtjyzdDToblTy7Z8XMpjQt1rB_B2JhPtcGYw3GXw49D1qdGeXKO3mgJ_Rx1KLY26X_u06Er03Ct65RrOIPS_YLUMgCQpkWZktj-DDGE2y7KZwrX3qrWA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64261a7aea.mp4?token=rDiKSpxg7R5FFgI-juTUq49EH5itPUVg0in4Q-BY12aSnyMr9W_mzRwVYjOzgEi17wzJa9S5mgD_RLRpu8LYfFl4dS3HBnBxxXf0T1-EUOrn83XkEPMcvwKSx2Xky0UxKYkFG0E0IEbwSPBpPDGyBRz45v2jfQcjg9SkXFG3zL5Shvyt059N4xFCHQqktthsAF_nN86sk9cV0P0NHw047ZQEZZaLIEqb23VtjyzdDToblTy7Z8XMpjQt1rB_B2JhPtcGYw3GXw49D1qdGeXKO3mgJ_Rx1KLY26X_u06Er03Ct65RrOIPS_YLUMgCQpkWZktj-DDGE2y7KZwrX3qrWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇪🇸
گل‌اول رئال‌مادرید توسط جود بِلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104403" target="_blank">📅 23:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104402">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/96a06aa961.mp4?token=rv-lWjc6f_7mM6bXTsy5k4lHtNN-DbUhsH-q5PNWNolEX9FeKXkIBawAf7-PE4V91fa2LXUGTRk7wxVGv1k1Fpbjs42TnlmnkTmlIxJ8RonI7mq08Am1uKoWPdOWdxlKTImOohQ-udyw77BW08Livkrey-m-ZddNW6KMNar6BxgL3WhwFjywClJltmU994xJ71zaFubxjlzGitwa_v2cZoIl_pqoZ0ktr0fiOUWwbjlbz9rWhdeS6ppxiP-68SaghvRurXcVkrv5WhebJP4s6hpUGkSM9NjuZ3LzKyd_3xkjPauorGbmuIZoD1lMK527QVtFZnttQ_ZlrWqHdKj_nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/96a06aa961.mp4?token=rv-lWjc6f_7mM6bXTsy5k4lHtNN-DbUhsH-q5PNWNolEX9FeKXkIBawAf7-PE4V91fa2LXUGTRk7wxVGv1k1Fpbjs42TnlmnkTmlIxJ8RonI7mq08Am1uKoWPdOWdxlKTImOohQ-udyw77BW08Livkrey-m-ZddNW6KMNar6BxgL3WhwFjywClJltmU994xJ71zaFubxjlzGitwa_v2cZoIl_pqoZ0ktr0fiOUWwbjlbz9rWhdeS6ppxiP-68SaghvRurXcVkrv5WhebJP4s6hpUGkSM9NjuZ3LzKyd_3xkjPauorGbmuIZoD1lMK527QVtFZnttQ_ZlrWqHdKj_nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇩🇪
گل‌دوم بایرن‌مونیخ توسط مایکل‌اولیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104402" target="_blank">📅 22:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104401">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2962887cc1.mp4?token=pf6Kx79spGrdk1sNrpmWoO0hH_QVUJWZJk5sUOBqbbT-AY5CKog4Swq1R5M5OC-LK_i96EvauOmex73VAzfKVa922oj8EZkTaJy5Wpo52k-cnH6Yr09EHAPDknwJQojdtC-zu-drNI9Fi12ArXLHZrEfoJzamdk-2uwjHqKaBnUHNf5PgDFz8atZnUBgnWYGS_Ku-DjTbzgeZubZP3C2wDLAQTS6j4AupngyxgHqqVysAp1H7Ovs86uZuCuba6vErwWl3i_L0I0Fjd6CSzaCSjqmk1R7Zgp1NoCjiDmsRrz-w0oqkp7cgUOVqp5H4oa-BREtw5MHHXGUblAL4JmYEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2962887cc1.mp4?token=pf6Kx79spGrdk1sNrpmWoO0hH_QVUJWZJk5sUOBqbbT-AY5CKog4Swq1R5M5OC-LK_i96EvauOmex73VAzfKVa922oj8EZkTaJy5Wpo52k-cnH6Yr09EHAPDknwJQojdtC-zu-drNI9Fi12ArXLHZrEfoJzamdk-2uwjHqKaBnUHNf5PgDFz8atZnUBgnWYGS_Ku-DjTbzgeZubZP3C2wDLAQTS6j4AupngyxgHqqVysAp1H7Ovs86uZuCuba6vErwWl3i_L0I0Fjd6CSzaCSjqmk1R7Zgp1NoCjiDmsRrz-w0oqkp7cgUOVqp5H4oa-BREtw5MHHXGUblAL4JmYEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇩🇪
گل‌اول بایرن‌مونیخ به دورتمند توسط برون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104401" target="_blank">📅 22:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104400">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1145503d.mp4?token=H9fD3xrS9vDsGZEj_YsL5u5JsEQX5h07e0CTxQ7ZCNRoFC6JxZnqR0vdIAFHH8qHEqc2hbXXbOjoa0A7ao2tfI6OMGFXTu8B-WoavLDZq3Hoah_8YlVDjhJZ0WN2VRHCSluuICFfy_-P7B2qZcZV7pHY_sh6tnQ9-e2lZPjqwH60v2owYt8KNfUDAOOza7AFpAN56GenTR_qt5NvVoDD1oj1NRg2lAQCgi2d2I-JuMvs62jl-orDciCG7n2zkIMeu0Lms487GHeI3qzW69MoBTx9d69Ykpvxr_PqqrHdTkJ60mJHnRZ2qOqeZ1KGDRTZRJxhURYLRA_F2V-SFuISUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1145503d.mp4?token=H9fD3xrS9vDsGZEj_YsL5u5JsEQX5h07e0CTxQ7ZCNRoFC6JxZnqR0vdIAFHH8qHEqc2hbXXbOjoa0A7ao2tfI6OMGFXTu8B-WoavLDZq3Hoah_8YlVDjhJZ0WN2VRHCSluuICFfy_-P7B2qZcZV7pHY_sh6tnQ9-e2lZPjqwH60v2owYt8KNfUDAOOza7AFpAN56GenTR_qt5NvVoDD1oj1NRg2lAQCgi2d2I-JuMvs62jl-orDciCG7n2zkIMeu0Lms487GHeI3qzW69MoBTx9d69Ykpvxr_PqqrHdTkJ60mJHnRZ2qOqeZ1KGDRTZRJxhURYLRA_F2V-SFuISUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🔴
علی قلی‌زاده: امیدوارم سال آینده در پرسپولیس باشم
💬
فصل گذشته تمام کارهای انتقال من به پرسپولیس انجام شده بود اما ناگهان ورق برگشت/ باشگاه لخ‌پوزنان امروز یک‌رقم می‌خواست و فردا رقم رضایت‌نامه را افزایش می‌داد/ به هرحال این ماجراها بین باشگاه‌ها طبیعی است/ امیدوارم سال آینده در پرسپولیس حضور داشته باشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104400" target="_blank">📅 22:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104399">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8yz5H6oUWZKolgQpvLvSsQsPanMwFFNCx6oFKin0JLY7XqQzGbqtapBWhTmD9r75ag8_NivnQI_tzR8fHyyDhc6ShqEEXp02Tk6SULmdAKnHhnfQ28AUZhWZIYqg_IJ8khmoAerntTLwchoCdZgujXBQFzCtYwYb6LMrv0y_U3kpQC_0tGQkmq6JfFos1zB5ux2ikWEKlA4tSLHVqG4T249SrGIDyKK0LA63ksU6dqgB59ipRWB5LXSIwhq7qwL2kAHLF-C0qQV8extGcxk836DvYoUMv5IG_8xPL65Hf93-iguyXAoyCp61h5lKEHXHgxiUsdgRyCyjSt1-ZQrfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
رومانو: فابینیو به ترابوزان‌اسپور
HERE WE GO
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104399" target="_blank">📅 22:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104398">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d7144def.mp4?token=B2970oZBbPusszyXiQ4HdRtweb3AIvdCZatCuwfBdDHGOu6XJ6nI0shP0tpWaDHaUICoO9udJmepMwBY_cmAw4w4pNHvBFfOr8r6XDUdq8gA7kYgAD6aCdaXTZS_USh6EGAF81bYTlsT_oYHLdcRdS3BB6bQ7XvtEdD1JsYWvfPT7qhMgudWGKR226J009KhZPhWyhoQzt8iF905NobGvghB_9hfgrwIgbJf_czLPGo4Zguwgvxqdrw9kUWvgKbPnAKJxdyqYQw6bSOUDMI6j5d9eJZA-9aRgLtT52eC-U9qjFbC5HLCylVa92-k_Oc3ufdOGTwVf39mfIFo9E9QDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d7144def.mp4?token=B2970oZBbPusszyXiQ4HdRtweb3AIvdCZatCuwfBdDHGOu6XJ6nI0shP0tpWaDHaUICoO9udJmepMwBY_cmAw4w4pNHvBFfOr8r6XDUdq8gA7kYgAD6aCdaXTZS_USh6EGAF81bYTlsT_oYHLdcRdS3BB6bQ7XvtEdD1JsYWvfPT7qhMgudWGKR226J009KhZPhWyhoQzt8iF905NobGvghB_9hfgrwIgbJf_czLPGo4Zguwgvxqdrw9kUWvgKbPnAKJxdyqYQw6bSOUDMI6j5d9eJZA-9aRgLtT52eC-U9qjFbC5HLCylVa92-k_Oc3ufdOGTwVf39mfIFo9E9QDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🤯
🔥
🔥
🔥
سوپرگل تام بالارد بازیکن بریستول سیتی به بیرمنگام
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104398" target="_blank">📅 22:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104397">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nc7vuFu5bRSk9yjEZKTfNVdMESzpk3I2eJCJUmYoXEKVQwt452T4nb__B4GM0qZnm0Lmk5j2hB6nPjyRKDB0JwwrdXYmPNux_QKXduwQDQxEh2fk-WuaC4E08NY0_mR3tGH03GFcmk-ucvslCAitbYbDsM6fPOFhqin2B4WszpdHDfabBG_PNCqWTs1bJjXvPm7aN-9aJe9M34yEHl1uATWPHL4S9Q0jOOJtcyx3s329ox-V6eqIged4dQgI3mKydxHDsuVeAN-wY8un8sALuvQli2Tx6RVHclji_ixpSQ_gFZ0rCMymO5HZvxeFsZ4yRw2eEx5UX5surj2weN4Y1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
هفته‌دوم لالیگا؛ ترکیب رئال‌مادرید مقابل اسپانیول؛ ساعت ۲۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104397" target="_blank">📅 21:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104396">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6JkBcYMcETTqyDwFUgS67Mfg9ff-m7RyQDvmqi3aRc7KXNTHYXIUEHyGEJDP6-MdPkfEpx9WA6WqgVvUXnwSjAaqGnWin0Y0xnPAy5c56C3oLmnBRkg0Aj9csGY0zw3kZjCzchUylMLRrf0IWQmmHYpCSIz47P99YqE2kGUF6dXCvmO5_teJ10oFbXCxYrOoj4NOHXn73YoksftD0TtJjKxlWm3zJAcDJDv40Vi7l94o3R7Nbu9W7FceuevKtxksSKuhyBn4WOza2ED9nm6O0bNCGM0inER3ZGFjjyMyGDa631DS0xUoT5TBNbBLxJ6zVwjY87KhR295nOr2JLZKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
هفته‌دوم لالیگا؛ ترکیب رئال‌مادرید مقابل اسپانیول؛ ساعت ۲۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104396" target="_blank">📅 21:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104395">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usDS8M-ieiWb6EGifjBzggAo677Cvwhao8Lm1mzfnQJKtyt72tKAZDQjhe2xnlaqhW7xBOh58ZwZSlRK0zFU2bmfvTfdTSMIvPElsfBW-ZkQIOwYbbLayX4zZawtfI1LSI2Mr0_ZAi7yricMV0Jd4657lCKcy82f5Fba--RTZ_NKEXtxHgNmbS7tI4e_pvrhOK7DfCgRbNxDDxwYB8G9FQCq2ZZm3r4s3l5Zi0Q3JUAo5kwjb7-ysJaa8lPzXLwAFfX5TKBn2iazJLiSlfELfiMtK6HXbqS6VK-WuV_M24Wesnkq8whfiG3QlPLPhoeJu08UsKLaoj33nC-1B02-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇸
خولیان آلوارز در لیست اتلتیکومادرید برای بازی فرداشب مقابل ویارئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104395" target="_blank">📅 21:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104394">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dauRg_y5b7HDAQggnknT_bEvN68lrFhXHQ_Zqor6B5WiA9oxALVV158rmLjgwnqwVR76QQfCDBHz2JW3hcPrmoaw_mMkfLLISwJdmGjhVUDV8CgDd57h8e7igzsnWkKCLouv6OSNkFvJirSV_YcY2dCgQrXZX_U9F7Q7iuWi2TX4MVkVZ_iJ2sopvqG2jKlLiVFqHet4B9fUL6VgOHhJYDjblBIt6C9wI1NNOvW622mfaiZF4zWW12zBq1wau1VK2X1gT3Ap9zucKaTsSBBmsy1CuF7rnu8-XjF7I28qAeWLmxfTh3AIqeh4D4L_hp9jY3lLGrid1etTkStZvRYKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آخر و عاقبت تیمی که مربیش کصشر باشه و با ۳۰۰ میلیون یورو هزینه بازم بگا میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104394" target="_blank">📅 21:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104393">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOSQov7Qdt0SLYZHgyJaNBMLxNAkYE9DfGrIA4jI64uqNgGad1vcl2Ym0pTL1AtCexh38hoSA7p2fOnTAdKOCQdUF96g42iMw7_otiwEs4nypwxH0xFYCuyIizSL7_kMWltpdv46wXll2UFFmzQhA4gXjrdY0bZX3lnuLyfKW1dW4WOnJ9TS-PvT6iAHUX_5LbEisv_IBYBWUG81VHOjGOvvKngIaJteUNN6U3Xs0RHxIL5bz3Vx6l75wJUmHAW4RzxNIb9Y6pdCiHUSxLG8n5xhINJxSnSm-7UjF6wJqeYrvDYWIozleEwEDim_lbpzt28qPlV46FFtzuN1G-WlDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
سوپرجام آلمان؛ ترکیب دورتموند مقابل بایرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104393" target="_blank">📅 21:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104392">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lz9qAKRApH_PfkxtZgbYEz6Pl3IWQLr7XVNaGjoHYNthKLLcrrq2jZ6FtRmL9aUOgCB4LxDrDIRv3CqnTgAdYgsNuiQj_XUwaFXulsB_W-apBcVkr_CiYr1a_GKGn8vMeORKoKfA12GXrI33wEq7zY62SHRIazLvCmXTmAvIU4h31BG7t98Vd5WmAeLyEEcGlmWVntUhWbzlvWzRLVCUPZFTF7aK9-IitV1pI_ercDcBfORlOUDguwon-aU0_CmdYrfQfytXNSyQn7SJMdQk-kDDZqbPlkKtQdNtUHVtX0tkLDHgFEc1Z53drQOOL26FHmCLCAT3UoU0GjTB191Gxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
سوپرجام آلمان؛ ترکیب دورتموند مقابل بایرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/104392" target="_blank">📅 20:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104391">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f25fa8009.mp4?token=K0NtIVz-5quC4vXCplkFSIcEIvmhklHvOd-rYTiOHz6sMe0fd0LEBMMAPWT-QnrjvQpe5kdF6pcV261cGGNy3zL28nrxFQnqOznFz-Sk1QjEdKsz3M6Xs_IHTSqVMIABBecHZ626EKo3GYs0ub_SMHEbQOvEL5O4TpbYmzKhLD-D47RQUUI0weYOXJllGy8SmfYGZDW5Y_nkyGZTUqsPkkki5PFhdtM9ee55FyzTFIZ4aDEsByxQ5cnW26vSfDGLkG2vLbDTexScCJ3nOK7zZIAjffMW8ZdLpW33yC5Y01Ufx3QDMNemH58DSP64TJTiDy5U2ZZBA35fFzPBhJN4oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f25fa8009.mp4?token=K0NtIVz-5quC4vXCplkFSIcEIvmhklHvOd-rYTiOHz6sMe0fd0LEBMMAPWT-QnrjvQpe5kdF6pcV261cGGNy3zL28nrxFQnqOznFz-Sk1QjEdKsz3M6Xs_IHTSqVMIABBecHZ626EKo3GYs0ub_SMHEbQOvEL5O4TpbYmzKhLD-D47RQUUI0weYOXJllGy8SmfYGZDW5Y_nkyGZTUqsPkkki5PFhdtM9ee55FyzTFIZ4aDEsByxQ5cnW26vSfDGLkG2vLbDTexScCJ3nOK7zZIAjffMW8ZdLpW33yC5Y01Ufx3QDMNemH58DSP64TJTiDy5U2ZZBA35fFzPBhJN4oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این حرفای گواردیولا رو گوش بدید و عمل کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104391" target="_blank">📅 20:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104390">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4ecEwD6StIrpt8XbFP8B90Tjl_ICBd715USYqAW3Bgksc8Y4jminaWS3edJ38BGuS6A_NvJgK4oJBEnMS6Z06AWShNRYWGmBhOgrqsocvnoyJ6VXMdinzLuIj5sN2qfm7RY6wj7UQW9DkGaktl-4XDAFpkJ25NmHMBdiEhFk03JVnEMwEJJaqNdfEPiKwAy-kbN_j7hdu8YFT77wv-EDEP958bcXhumhfOvYrT3MT_ZC4RPqnM4JKES28ACQAvNT2B_87S9fYEz3XxOsz5Xe8wfaetWhGMwvqvsdN9SZ7_bPeNzwQzHdbq0PTeGzPM37iXN7JxCPIenCnj5vpI2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇺
لژیونرهای ایرانی حاضر در اروپا:
🇳🇱
علیرضا جهانبخش: اکسلسیور هلند
🇵🇱
الهیار صیادمنش و علی قلی‌زاده: لخ پوزنان لهستان
🇷🇺
محمدجواد حسین‌نژاد: دینامو ماخاچ‌قلعه روسیه
🇧🇾
میلاد محمدی: ویتبسک بلاروس
🇷🇺
نادر محمدی: دسته دو روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/104390" target="_blank">📅 20:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104389">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dba53081a0.mp4?token=a3WQ-JTuweHlqa77sHDdIu_5B2vGbnJ-M43Qi6d1h0tSg4jLqxxC_hdvRYdqS6T4wzmzMsY5hFv-Y_LDDM1j_kqrVTb2PdRWyaa18Y2MhoICrtmOhJ5br0kF96ywUtjfuzAAUhOhu2FNVFKcrQi6y99O13nDorIweYzrCawzCvwM-qkuE1ZdjIhseYoMVjBHq4ELg7PXuObNOQaKRS3mvjNxT-yf276SezfS4JINOq012Yi_H8QHMD9nvcSbeJ9SDIAK32R_F-S1umkeIGrU6ufWLOQQPofRDpGRg1ZYtmUD20Qi_Iv5tckwVMLrNTtSekqYUFp2jl3LpRASbI5KyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dba53081a0.mp4?token=a3WQ-JTuweHlqa77sHDdIu_5B2vGbnJ-M43Qi6d1h0tSg4jLqxxC_hdvRYdqS6T4wzmzMsY5hFv-Y_LDDM1j_kqrVTb2PdRWyaa18Y2MhoICrtmOhJ5br0kF96ywUtjfuzAAUhOhu2FNVFKcrQi6y99O13nDorIweYzrCawzCvwM-qkuE1ZdjIhseYoMVjBHq4ELg7PXuObNOQaKRS3mvjNxT-yf276SezfS4JINOq012Yi_H8QHMD9nvcSbeJ9SDIAK32R_F-S1umkeIGrU6ufWLOQQPofRDpGRg1ZYtmUD20Qi_Iv5tckwVMLrNTtSekqYUFp2jl3LpRASbI5KyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
🇮🇷
حمایت جانانه بهتاش فریبا عضو کمیته پیشکسوتان استقلال از رامین رضاییان: این‌که چه‌قدر پول بخواهد حق طبیعی اوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104389" target="_blank">📅 19:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104388">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2fde5e301.mp4?token=poaZx5bOshnLl8PHQYjDLoIKuyPF0EQeimAhF4rn4MEsa8tqzzS6k0SYAUASgx0lFyKoY2oP97xhz_GbltlWPxwPDlGnC-IMu6MEhyAVq1Q0EbEi53AxL4wjWaZ7BkJoaCzcNDmycRaHX6_GXUpszGhAPEBKzkt9YUk7g-DCMQPlbOeosFV5wxK1x5t5SsVURUGWFlwPb0RDoNodLJObVZFV2mboEOywiL0A5_HK4Bhto-HstquLtJPIyEvWC26qBlnBSYo3apb_zFMunw7vLYgNw1rAUYl96GonXynDlaLMWApKB5NvjAaf9-VqVzTOwS8toE2qHFzM_7CVc2J8DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2fde5e301.mp4?token=poaZx5bOshnLl8PHQYjDLoIKuyPF0EQeimAhF4rn4MEsa8tqzzS6k0SYAUASgx0lFyKoY2oP97xhz_GbltlWPxwPDlGnC-IMu6MEhyAVq1Q0EbEi53AxL4wjWaZ7BkJoaCzcNDmycRaHX6_GXUpszGhAPEBKzkt9YUk7g-DCMQPlbOeosFV5wxK1x5t5SsVURUGWFlwPb0RDoNodLJObVZFV2mboEOywiL0A5_HK4Bhto-HstquLtJPIyEvWC26qBlnBSYo3apb_zFMunw7vLYgNw1rAUYl96GonXynDlaLMWApKB5NvjAaf9-VqVzTOwS8toE2qHFzM_7CVc2J8DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عملکرد ریدمان محمد صلاح در بازی اولش در ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104388" target="_blank">📅 19:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104387">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbEzuPs-Rj1dgOtAw3r14mz-PWU465w9xGqLQ84eu2taom5rFtfuz9gsTXl7l3bxOBZDtWFd5QI15Mc10XJ46w-k_6CWj9V4SZZePK0egjEoTLpVmCcc3_edg90dqG9szLdgi6jk6isIGNtWHy31WX3lKT6BJpQPb9AuuY97gaAnLKucbsS14qjahxtZrtWzUhi0Vg1-lHH2lD5soRMzCN8wUbF-tFtMyFtTP3mGzP_nz5lqCqO17OyJNk1cFqV_Y84aFd6EroxzQkI61LctQIX0hFLfnCOkkZOYRLXxjKt_lRCDXYEMm_SYIYZn91GdoiOWjOoPdtgFQARe_e8vqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته دوم لالیگا اسپانیا
🇪🇸
اسپانیول
🆚
رئال مادرید
🇪🇸
⏰
ساعت ۲۳:۰۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ ‌‌بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/104387" target="_blank">📅 19:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104386">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54d02a0a5f.mp4?token=pNoEEctvo8OFTq-eO5pdxpz3Mxh8D3nL0JPnrZw6v7LmyiR6fr2nOZcU9ddM8M3PLozu0kLYwp1erR-8mh451WB3Qyoajez1NeHIgZ2_4uKy-4N6m0oga1I1_zz_8LubORSq9d7Z5fFUtZ-EJrR-DhEIbSiSzOnZ4Q2KYJSnbrPlEPiKt6uEX8EuSmKJ6qVwucl1fhejadwdN6QwyHsjz1YxRjx_r_vVwccOpmAalrBm-ocMaYrgSbtyYRdRdwvIX3M3yOn7ignPnUYQ5PDUi8f6I4At43jP0fneK7uE08n5-W0lqYuxQ2sRAXIz7N3NeIzmX4sk6mH6lDBTqDba1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54d02a0a5f.mp4?token=pNoEEctvo8OFTq-eO5pdxpz3Mxh8D3nL0JPnrZw6v7LmyiR6fr2nOZcU9ddM8M3PLozu0kLYwp1erR-8mh451WB3Qyoajez1NeHIgZ2_4uKy-4N6m0oga1I1_zz_8LubORSq9d7Z5fFUtZ-EJrR-DhEIbSiSzOnZ4Q2KYJSnbrPlEPiKt6uEX8EuSmKJ6qVwucl1fhejadwdN6QwyHsjz1YxRjx_r_vVwccOpmAalrBm-ocMaYrgSbtyYRdRdwvIX3M3yOn7ignPnUYQ5PDUi8f6I4At43jP0fneK7uE08n5-W0lqYuxQ2sRAXIz7N3NeIzmX4sk6mH6lDBTqDba1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اقدام زیبا و تحسین‌برانگیز بازیکنان اولسان کره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104386" target="_blank">📅 19:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104385">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UDh2pgpSk5T3U_syxEk6bSZ_DRSTxRuRHg12Bv0qtdFcbxY68W2hFhh14KKxJaE63BYi7PnTVcgVxEzNXAlYy6nVaCb9FDTb0sd0ipfN1goGx14E3FjdcSGhrl09gphCfxjNOmCJ3WnQ0Fkp2M9-l-4Mu4BqK32imaVsBMyDMfMvG5cFfIj1AXTLHVA8oCwYHyo_Sz3Yx_0ppq0qrAT9pKLxIUUHZ9I9hZUVDuaLM6Xe3-wPdzmz6n2ddcTET1KJEXBAy9Yt0aNX5UEpjPFw3b9_-VHGflLj1StR4SstG9We-LUbw8_dPKisRq90v4TephV_OUY9QWoSYhgw3yNzPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🇪🇸
#فوووووری
از رئیس باشگاه اینتر: بهتر است بارسلونا خیال جذب لائوتارو را از سرش بیرون کند چون هیچ راهی برای فروش این بازیکن وجود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/104385" target="_blank">📅 19:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104384">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33114edb2.mp4?token=Kuzg5hbW0eTFX4_CeWQRyGhqdHGfVNtBoH6EwkXLGzVYqnpqrsJKnBoGGhSARywOINrkfykjEsxKRWVm8VcJvAXYmLZ1UoGwuTnzM7qd92vdq0OjTMBnPRtjWLlLSjs_5j5SIFVN8aigP-CTxvRFVZRsq0_v5e5A5y3yMH7DVnbZSnlDoerm1szFDg5xaYQ-8aOioKRsu3lwnx2WMjk8hto7_oS8G3f4XglOoRs7qo2C2Oq2jweUdV3ZUNznRV4hM1a7vFy_R1_EKEY0LjSaMF-AlcCEFsbdqe5pIAAI6hBfOsF2UbLw75bqg4EPiNWdWCFTCx05vO3CKcQG1PMPow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33114edb2.mp4?token=Kuzg5hbW0eTFX4_CeWQRyGhqdHGfVNtBoH6EwkXLGzVYqnpqrsJKnBoGGhSARywOINrkfykjEsxKRWVm8VcJvAXYmLZ1UoGwuTnzM7qd92vdq0OjTMBnPRtjWLlLSjs_5j5SIFVN8aigP-CTxvRFVZRsq0_v5e5A5y3yMH7DVnbZSnlDoerm1szFDg5xaYQ-8aOioKRsu3lwnx2WMjk8hto7_oS8G3f4XglOoRs7qo2C2Oq2jweUdV3ZUNznRV4hM1a7vFy_R1_EKEY0LjSaMF-AlcCEFsbdqe5pIAAI6hBfOsF2UbLw75bqg4EPiNWdWCFTCx05vO3CKcQG1PMPow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل‌تماشایی ساندرلند در مقابل ایپسویچ
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104384" target="_blank">📅 19:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104383">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjvZgtMAFNlHIG5zatMfh1xbiUffuB7RrX9RxuzlBPr_FQm93exU_wgD-D0p7dDNaKc1fsse-okt__-2CSyqlHxwM_Rm1kDQ1PaHqi8WOA_MXW437KpXTGe9MOjZ4EnaOjPqgcgjo3PwSH8d6elhLyvdPo-PQFjNwBTpb1pxtmfxlwM4SybTrJMxMUWKOZNoo38V6n4lv9XF5IfjkQWBtZ7kjMIG_EIbv6T-o_J9lX9y_dq_nR1A0zuGCpAxPYVGjdKff48iT75IeCHHQNoY0Db-G3_FVMQ4nUYtUmu0LT0ooo7MPcwIao5mAhLXPyLs5665QOPt4B68Yt-zkyextg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: دو تیم شهر منچستر به جذب بالده بازیکن بارسلونا علاقه‌مند هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104383" target="_blank">📅 19:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104382">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqna2Y4Q3Y5CfdxUHZWzpKBKSOfKOoTo1WPrT_xNezo0pgoBT8EyFvaRZti0rn3Tg2YKt3q3w70kbTGRcKSZa5y2j0DhEVIYx43yH5jd8EIKEMqodKm-bza1CQydEJgPBiZBABb5vcWxFzUP9USJ33pAkcD9xOy5JCTqnc6nVmzG-A28YzgdvXBAOvWbl8qiAFL4mKoJmJmLp9vuS8EY3Tza7Oyy23Hcn6wCfR6B4SD_ulrgVKK5jNtu-L3xF5EwgCW-egGOo4bRT-Y4Zu4Z3FeqU5p5bAlv_tswTgopdqmxcRgTtDaWmATRVTX5053Hjrh6JkCdJZExS8RHlWz0eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته‌اول سری‌آ؛ ترکیب اینتر مقابل مونزا؛ 20:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/104382" target="_blank">📅 19:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104381">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45250f7e28.mp4?token=sQ6T9-x1aSmiBs1ihT3ZmoP2rsR6NAdB6_SlXGgEVjdN5fjzmaTh-XR03Wztzn9lqSJCUCiWFE9aRmFfNxms8Wz-lcY1gWRe6WpWo8fYi1TFBK1i3sPwB7Y-jbC0T1KNjBd2NSOP4evxEZiCJo4niUI01aNdSvFY8kVPTnzclYqQ_xO_hR50B8B_WJH9-LhwuSYZ5eNpj0qoysOrFWnHSZpeW97quZnF8IcIg4LjuHs1YCZa1Fg3_LRFuQy8OlZNeRl4Ow5a4oKkalAGHjAn9bpNMVfCWA0GWHhUn9kyboJLiiGAKtco0LrUBJBkVp8P21gp-2t6WimCLBwojmWmWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45250f7e28.mp4?token=sQ6T9-x1aSmiBs1ihT3ZmoP2rsR6NAdB6_SlXGgEVjdN5fjzmaTh-XR03Wztzn9lqSJCUCiWFE9aRmFfNxms8Wz-lcY1gWRe6WpWo8fYi1TFBK1i3sPwB7Y-jbC0T1KNjBd2NSOP4evxEZiCJo4niUI01aNdSvFY8kVPTnzclYqQ_xO_hR50B8B_WJH9-LhwuSYZ5eNpj0qoysOrFWnHSZpeW97quZnF8IcIg4LjuHs1YCZa1Fg3_LRFuQy8OlZNeRl4Ow5a4oKkalAGHjAn9bpNMVfCWA0GWHhUn9kyboJLiiGAKtco0LrUBJBkVp8P21gp-2t6WimCLBwojmWmWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
فوتبال روان سپاهان محرم نویدکیا که با چاشنی بدشانسی همراه است...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104381" target="_blank">📅 19:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104380">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
⚽
@Tipster_Mafiaa
@Tipster_Mafiaa
⚽
@Tipster_Mafiaa
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104380" target="_blank">📅 19:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104379">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗧𝗶𝗽𝘀𝘁𝗲𝗿 | 𝗠𝗮𝗳𝗶𝗮</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdSIgaAj6J6AmZMMR-CB_tl-Vm595zMsPz34tLSxF_L4AMAxs41HVvniWUVSyc_YY3a6LQt7hWMXfqdgzK2lqc7wDh7ivxe6QC6gBcMCMk57uZnurvXEwe4oQHbJSQtFDsmbPC0jNZN7pBLTfgz7v8iPxV1obdJ30UVpB2VJ71Y4afMxIv0opn_KA-qfnahoHe_xneGnglqIOCt23lDa7DRiv0YQn23mUo-ZMM_gmEEFBquW8BiOpQn7hSlQtA9LDpmDGGOBu2QcnrTLHpybUodvy0a7pchSGJIvPCN-RZSCrQLupECzEE1Dxrw11D8YX_em_Kg2Zamd-Mw-PoseMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/104379" target="_blank">📅 19:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104378">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b7ad297b.mp4?token=uyCylxNiF9cUFPbSaHJmBXFunfkrSia8KDgF_aKVIhnrHyhYACZp3BFNi70QAQrtrLQnVOZly3ilq4DE-cicq7Z4xluPNddyd1m5UwPprjAXGEahXY58e5xRkwUWJ79nQD6cKcC98_sYWxEwCSyIswIeBKAldr2t8vovkbQUaaI0qPwxFZSYM-ON5-6pH-PbHN2JWn6-VASwb7u3crPyG868E7HZ8rdEMFUwOzVQvHle4Tl7AXPbcBdiUa3vYQkDTaAvI2q9zQXDgMvhfZBsiWqF_OnqKHmqG8oVXm4POUg4Dw3WCmisHTkY8WaEDcaAluMKeWcyzRueBlbCLIfViw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b7ad297b.mp4?token=uyCylxNiF9cUFPbSaHJmBXFunfkrSia8KDgF_aKVIhnrHyhYACZp3BFNi70QAQrtrLQnVOZly3ilq4DE-cicq7Z4xluPNddyd1m5UwPprjAXGEahXY58e5xRkwUWJ79nQD6cKcC98_sYWxEwCSyIswIeBKAldr2t8vovkbQUaaI0qPwxFZSYM-ON5-6pH-PbHN2JWn6-VASwb7u3crPyG868E7HZ8rdEMFUwOzVQvHle4Tl7AXPbcBdiUa3vYQkDTaAvI2q9zQXDgMvhfZBsiWqF_OnqKHmqG8oVXm4POUg4Dw3WCmisHTkY8WaEDcaAluMKeWcyzRueBlbCLIfViw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
هیچوقت این صدای تاریخی استاد مرتضی فنونی‌زاده از ذهن و خاطرات پاک‌نمیشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/104378" target="_blank">📅 19:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104377">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGgS4fEfouQQHswEYHcC8vGuSCtEOnUWuzBX1yCnr_nskby_U0byJguRzN_SDwigLMtPtLcGJYQL4lImub4rNHOiL4Gq--GkI-nHzT22nPKyeQCEV00gTFxL_HhzkcTVnUF4J9IbLlYYBgoeUiDhTh_eJUPKeAwm3n_QwjE2u6XtdVGghYMOsqsCjDXIMLFKBmCYH0qd7fg7rtKMNYma68t6XltccBQ6Xt34V4oY0u4CFkHp_PidZ4KlLSzgVG4mzBKZXjKIL6ub24EhtHFE0YVNEow48azknl1-V8VtIOeYNgiKIz_Is0QDu2s8bPcYOpp-0AxInQKoh8GxeU9_eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر کنایه‌آمیز گل‌گهر سیرجان برای دیدار فرداشب مقابل چادرملو اردکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/104377" target="_blank">📅 18:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104376">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ed1c9346a.mp4?token=leGHl_LZQMPo91GRcyviMer9KnF-ERF8rLCW9sCOI4Jho_v4Q_PUxMzEJZVCeglPL7ZH-dR6fHD6q0eclU1JDBZGeE1TPqDyaVy9GE8DBcs3f8pcK6pXdRVuu99Xwbnm9e-u5ZCwFFuRScE3wsllGbKf-9EoLa8jNNBrAke_J1pJk5leb-zJYZn-6oYOhmtAd1BVlww2liYPeGShLkQCDFEC26y8KDT_gBujpSbjgmnFrsTSXVf0ni1JwniEjqC_2x-6mi0jTYb-ylEczeyIl08kbKSOtO5EECR-UtSff9CMpewXHYJ9LPZl6j1n7WeaWjVLrJjnzZaie_gdek9CMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ed1c9346a.mp4?token=leGHl_LZQMPo91GRcyviMer9KnF-ERF8rLCW9sCOI4Jho_v4Q_PUxMzEJZVCeglPL7ZH-dR6fHD6q0eclU1JDBZGeE1TPqDyaVy9GE8DBcs3f8pcK6pXdRVuu99Xwbnm9e-u5ZCwFFuRScE3wsllGbKf-9EoLa8jNNBrAke_J1pJk5leb-zJYZn-6oYOhmtAd1BVlww2liYPeGShLkQCDFEC26y8KDT_gBujpSbjgmnFrsTSXVf0ni1JwniEjqC_2x-6mi0jTYb-ylEczeyIl08kbKSOtO5EECR-UtSff9CMpewXHYJ9LPZl6j1n7WeaWjVLrJjnzZaie_gdek9CMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
از حواشی کمتر دیده شده بازی استقلال و نساجی؛ عصبانیت سهراب بختیاری‌زاده از حبیب فرعباسی بابت انجام حرکات خطرناک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/104376" target="_blank">📅 18:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104375">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6820414d13.mp4?token=sfqJN0zpvsehJDy-quZ8Fao7iWPKcCYB2JXS_rRPJ9XRWAKYEAoiJAT6tACGIiD2RH9lH6YCZEzwz5dNgA-8-a9K1aTPU2v3IM0JW7pE0qtzwNPKNyEEp_cx17TUj-YPyf8ipT9x_yXrQ8fZW9ehI8v3fqhqAiIA-E_JMCooxOp9h9ZW8rRnKgt9CBjXQ52WuMJzF0jwljCq5pPYlknmpClR0gnj7IKn_2StU5eGBtFkqkIBEBWKtpghfeRoYNrS5KvV361vT945k2VOESJfU9Ck9jopJdP2HL0IfRlRqh0BOofsaoBhGYfr9nzWviNTA0ksQw9kaLkUNOUeQ4e2wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6820414d13.mp4?token=sfqJN0zpvsehJDy-quZ8Fao7iWPKcCYB2JXS_rRPJ9XRWAKYEAoiJAT6tACGIiD2RH9lH6YCZEzwz5dNgA-8-a9K1aTPU2v3IM0JW7pE0qtzwNPKNyEEp_cx17TUj-YPyf8ipT9x_yXrQ8fZW9ehI8v3fqhqAiIA-E_JMCooxOp9h9ZW8rRnKgt9CBjXQ52WuMJzF0jwljCq5pPYlknmpClR0gnj7IKn_2StU5eGBtFkqkIBEBWKtpghfeRoYNrS5KvV361vT945k2VOESJfU9Ck9jopJdP2HL0IfRlRqh0BOofsaoBhGYfr9nzWviNTA0ksQw9kaLkUNOUeQ4e2wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آغاز قدرتمند منچستریونایتد در لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/104375" target="_blank">📅 17:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104374">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2QGpjKjmFf2G6mpcUVQatJwk-xR4ZZ7Kc70MwKj74D6LAFIt8-OKVvueFjsi7logdBlH5XPVNHD0WomhqC5UKKwBRSspgkiSC8BD6sBIrIPPi_GTOata6byF6f6OqII2KpCtOUooGQy1kYU59NY3V8hfLCJ2MZDs81d0-SnrY9r7TbdT1yUaNt53grnNtQWtgIv0QAfrLZ7tkAFFGnl4aCWjV6QJtLghhj8-5Z0LFzM7gVED10Aic6odNClpB6RHxn9oyePa2K83OjmJAfR4jPwKfSfY_bp-Yc18uYvlPk1Ui7Zrc7E8oeAaTglNSFRb_3Va3fktqqeig6L9Hltgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
از جرارد رومرو: آلخاندرو بالده مدافع چپ بارسلونا طی روزهای آینده از جمع شاگردان فلیک جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104374" target="_blank">📅 17:27 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104373">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyJ1lDPoOUYJpYAvnEF3ZV3xbQBwZje1PGL1Nj2oJ9GH8h1HVCFm54nydpD9XnQB6nshpofEvL_AQJp0xBiBfUB_5MlCGTRKFIUjobHNEYjdvSvsH88WhkCNH7Hs8HNnOwiIHnMvxHB72iZu-FeTEHXAmRENQI3Z1oVk_eNqznSOJ9Q0B_y-mrNgqYu6j1uIAhZYt9hk_LdnRSdQPufbPnbQqqKQIuJg1L1gA4FPhWwH-FdEPvl6lMZsIrhboGq1_qG4W_-UR8i6vwPlWFQMYTuWcozx3kIS3bRyKmxYRG49DaCtyhF4bjHCGfQXSteDWzSwe0t0AJTG8zY9OT_v7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
آمار پشم‌ریزون بازی منچستریونایتد که با شکست شاگردان کریک همراه بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104373" target="_blank">📅 17:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104372">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CO_DYQPwagZcU82Xr7qfy47Ry2UYnRMKULyAcPwDwWM4AwCU8ZHCE8EUwK429TUA_8q8xX9HjhO8t8KV98KekS775Fz-TiIwwvxVOBXWcuiDZtipk0a0Vdvv8H0V0OwXS4g_cbD87YuJ-_uaMP1LSdW-fzsqeQZIs-4KNnSIeH62qjHVPeFzBsFxnKZMoSjcu1LDKSCnswMj1rWjghCAwm-XrRV2nVLQqBX5VNGCSCMAOkqHPpbV9hKkzzHfNwiQ-6Rd5nfbtIjxry6theW2Pz8vaWyHv0r8IH0p1uXw_kKcX4ax4EZBJvO_nUWAbtW-nlAzj1yMr78R6oa_7cEnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
آمار پشم‌ریزون بازی منچستریونایتد که با شکست شاگردان کریک همراه بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104372" target="_blank">📅 17:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104371">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCmppvx27nUZ0iDE3NrzrNrrYfAqty5cjOT9Q6bLqNG9xVWamswtFOKt2dgoTycincDjvzE7rV-aenIh1OORSUztix8yXzjL4xUMNzGgTQAXg6tFq_4HXXqwrQBrjXunFEFnt9VC_9kfvm-78lYaTWHcLQ8b_xdP0x3mCto2__UzZ59xbo2Mm4dwyrbwH_RZjuiLO4Qw29HchHzLLjhvLhSO7DpHBxApLHpJR7N3AVgJ_pr60eq8Eo-y1SZIuqzX6ORuqu43rPYFW5P3LF-t5qh1Xtis66QgDVhawl4VQazrHsrs3SQMOzJw-YpRLfmeHYuGYeXn3oP-Ow_XIYnudg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌علیپور مهاجم پرسپولیس و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104371" target="_blank">📅 16:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104370">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMk4S9evEXfs9w49eWBI93SR9IZbX2axZlfUFf8w-cs6p_SupkvUSGv1DgAVQ8vbilIP6pkah-Ix4okbCaM3dtvF3-_9o6A21oMFv5C02UkAWlRaIeIMAOcl3OiXgXTYUOeCHTNer6YrmKvEydG9gwVGkPMpkxP8TP4C6Ohmt5DWp1JZvtXcCo6Qv6I-yGtotMCt52PPqf5sczwJLlD8ttASexUg7TXzmBbjAIM-nc-rSPbr34T5uQbafBnaoor6Gg9Gkn3vpkMJXNfGSrYhTVwqKm-rnGqfLsOVgpB-lJJqua-jPwil7BUPDO8I51khLDHFEggLSEvgGIpg4jZYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
تغییرات شگفت‌انگیز سرمربیان بیگ‌ سیکس پریمیرلیگ تنها پس از گذشت ۸ سال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104370" target="_blank">📅 16:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104369">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a75f897a8.mp4?token=oEsyDEkuXImRo3KV831w-2nQvetnIAo_PmZxgYTh6MWwWv37Zg-8_PnqGLn1x22txnM4SgR5I90LubQo3IiWI5EQUC46rvH4HWeV3v0SRnSS-vCGYr5I_2APuWRMmy4FpKCho3nWY9ozm0ouG6835CfC3aAXWEXgaGbGKYaiY4c10sfsYBHg13XmqWKepxgOIOrv1gtYThSz0fIhBkVpZanA_r1FIaefVS1QSmd43Cm5a_4osTg9qxbHrXMu9HasjflesR--ecNy8dperZYv9UCk_gBQOlh4FsDsdnWnDp1kJLlhKBn9Fi8GrFDeiGitN0qY4NY0-yn8eIJnVxhZIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a75f897a8.mp4?token=oEsyDEkuXImRo3KV831w-2nQvetnIAo_PmZxgYTh6MWwWv37Zg-8_PnqGLn1x22txnM4SgR5I90LubQo3IiWI5EQUC46rvH4HWeV3v0SRnSS-vCGYr5I_2APuWRMmy4FpKCho3nWY9ozm0ouG6835CfC3aAXWEXgaGbGKYaiY4c10sfsYBHg13XmqWKepxgOIOrv1gtYThSz0fIhBkVpZanA_r1FIaefVS1QSmd43Cm5a_4osTg9qxbHrXMu9HasjflesR--ecNy8dperZYv9UCk_gBQOlh4FsDsdnWnDp1kJLlhKBn9Fi8GrFDeiGitN0qY4NY0-yn8eIJnVxhZIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دوتا پیرمرد پرحاشیه سالیان اخیر :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/104369" target="_blank">📅 16:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104368">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc446632ea.mp4?token=WH6mSWlD1cH8Z87r-IMoifrx1mIRdxn6s-0EWxpxxEEyNXRkwbXNyeZItySJMtjEhk6eifl35pAv6SnnER93QnOuH2luQJtUxVGCXa696EIRK0zq4p3UCEZrtvsGkZveOK9xOrq4R-ALtWSrya84u2vJOAD4GwgPYtpaptvJedjvSAHuLqXOYK8dgiKdU_L1l23_McL4NKPVIyvCYIBDmNIMNtMG_fpG7-O645fY7Max_5ku69mlbctKeJwoHWeXnH_XJTfeQzgyQiigb7ugzSGrKWOfRAk-eFxmDmatbaKCLKd9wAbs-z0zxURVzniHdahh3iuXcS-huNbOhvjeDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc446632ea.mp4?token=WH6mSWlD1cH8Z87r-IMoifrx1mIRdxn6s-0EWxpxxEEyNXRkwbXNyeZItySJMtjEhk6eifl35pAv6SnnER93QnOuH2luQJtUxVGCXa696EIRK0zq4p3UCEZrtvsGkZveOK9xOrq4R-ALtWSrya84u2vJOAD4GwgPYtpaptvJedjvSAHuLqXOYK8dgiKdU_L1l23_McL4NKPVIyvCYIBDmNIMNtMG_fpG7-O645fY7Max_5ku69mlbctKeJwoHWeXnH_XJTfeQzgyQiigb7ugzSGrKWOfRAk-eFxmDmatbaKCLKd9wAbs-z0zxURVzniHdahh3iuXcS-huNbOhvjeDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
▶️
این ویدیو بسیار کاربردی برای زمانی که در باشگاه، دستگاهی برای تمرین خاص وجود نداره و باید از راه‌های جایگزین حرکات رو انجام داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104368" target="_blank">📅 15:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104367">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0deddd0d6c.mp4?token=n_ifwN0ZQPYjLmGtpuRk2Qgw4rxOEZwFEom8fiyiqMCxkcLBu5uP0sTQrVN4BrolQP-JjbA48fcv74GgHs6-d8H4Iq5q_F1O2U0Sbd88x3Pw-CzZt1nRPMOMQI_98ALz1g8b5Mu3ntr_Tu9GX4uODegpS5sdoe2QCGtl2AqG0qNh9SwZXnE6k-3D3MdDurmI_G1cAzgXEqDLLgheiNqwdSh9L3aYyKwELHzdQF9rFncTvnegHmpqiWgTgD9gsLfLfylgLu4MFtTIofp22_7v_aUBMRItzZ2cGuwaMa77ivXeABEx6WXJPHjKdY42MX1hhwSh5Zz2bCd91fttpMs4QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0deddd0d6c.mp4?token=n_ifwN0ZQPYjLmGtpuRk2Qgw4rxOEZwFEom8fiyiqMCxkcLBu5uP0sTQrVN4BrolQP-JjbA48fcv74GgHs6-d8H4Iq5q_F1O2U0Sbd88x3Pw-CzZt1nRPMOMQI_98ALz1g8b5Mu3ntr_Tu9GX4uODegpS5sdoe2QCGtl2AqG0qNh9SwZXnE6k-3D3MdDurmI_G1cAzgXEqDLLgheiNqwdSh9L3aYyKwELHzdQF9rFncTvnegHmpqiWgTgD9gsLfLfylgLu4MFtTIofp22_7v_aUBMRItzZ2cGuwaMa77ivXeABEx6WXJPHjKdY42MX1hhwSh5Zz2bCd91fttpMs4QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
هیچوقت این مصاحبه تاریخی مدیرعامل ابومسلم روی آنتن زنده با عادل فراموش نمیشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104367" target="_blank">📅 15:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104366">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b033bca880.mp4?token=Hnl16o9WsoEkqIKlPEeasZ8r3OOnX4wvwOiq4qh6skFW1g68hd1PHcjtFvXhZ3uUxailxXOcOzfy7i6anzScle8rrr-u7NaNQZAwmbKutPVP0SdAs58sDGA2tCvdvPy9_JeuBkn2SVWnsK4acWXbWWWECEhX4x10xT9IK5Cl13nRFy2FmDH3p9Ndn9HEyvtNiiRIiUSt-DQiQuE7xiHStZWwd8WNWn3u4n-JfdxVZvcnvqR466azBOjsI5CFfj7Rt43fJb17pNPOOI-QfhJB8IO6A2bAFzcZj8VG2VHlQPOX3_w9lMTd2qTPV3uFW5q2WrtP6eOI3OfUbiEr4yht_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b033bca880.mp4?token=Hnl16o9WsoEkqIKlPEeasZ8r3OOnX4wvwOiq4qh6skFW1g68hd1PHcjtFvXhZ3uUxailxXOcOzfy7i6anzScle8rrr-u7NaNQZAwmbKutPVP0SdAs58sDGA2tCvdvPy9_JeuBkn2SVWnsK4acWXbWWWECEhX4x10xT9IK5Cl13nRFy2FmDH3p9Ndn9HEyvtNiiRIiUSt-DQiQuE7xiHStZWwd8WNWn3u4n-JfdxVZvcnvqR466azBOjsI5CFfj7Rt43fJb17pNPOOI-QfhJB8IO6A2bAFzcZj8VG2VHlQPOX3_w9lMTd2qTPV3uFW5q2WrtP6eOI3OfUbiEr4yht_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
لحظاتی با لائوتارو گزینه احتمالی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104366" target="_blank">📅 15:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104365">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9536e07d63.mp4?token=b2tTeDCuUqqCrELzmmc0vv6zIEfmndA4QA5GEqCiNj8t6BOC9PBJVNAHzUBnKtVVS8B7GCPJ-GYQv1FBWkXClYk_RIo9o9ut_azPvMswRQaBbrmRdZU1oyqGMfkHr7HK-y3gUBDuQhdpEPZ_Quejizyx14xqk7Y_cl229z2XBAgMJ81BWP4dth_3GKppSgS5hETL54MQLUVGm2jxRFn1JVgVH8RYEOaOM47-G0iXHz0Cu-yQiRKGyJGF7B5WwDeZ1RO9Ppm9ZQTsCbyghlfGJkhK4Pxoz--vko9fTcmgbFT9844ylBloZxvcV-Mme44o19Y6myQSRAvU9VPWfDHPiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9536e07d63.mp4?token=b2tTeDCuUqqCrELzmmc0vv6zIEfmndA4QA5GEqCiNj8t6BOC9PBJVNAHzUBnKtVVS8B7GCPJ-GYQv1FBWkXClYk_RIo9o9ut_azPvMswRQaBbrmRdZU1oyqGMfkHr7HK-y3gUBDuQhdpEPZ_Quejizyx14xqk7Y_cl229z2XBAgMJ81BWP4dth_3GKppSgS5hETL54MQLUVGm2jxRFn1JVgVH8RYEOaOM47-G0iXHz0Cu-yQiRKGyJGF7B5WwDeZ1RO9Ppm9ZQTsCbyghlfGJkhK4Pxoz--vko9fTcmgbFT9844ylBloZxvcV-Mme44o19Y6myQSRAvU9VPWfDHPiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇪🇸
توصیه های دیدیه‌دروگبا به دیامونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104365" target="_blank">📅 14:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104364">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a301749a37.mp4?token=FWo13SVDI1nW-hnsjyDFfIkbacnSRxP5ptzIITNDKvFLNCf__PAl5Xt3Ixv4eNo1Le_1L0jZNvismdoc3tJtsFpHdlo__fm4x0lfo-CQ1UfPKLrei4LFLaPqw0NKsL-n6r8s7UGj_cGnhlE3NqwXudNje2L0Q97frsCaSbC2AmSew4yJTLJqkTDJlGFuQqc_O9dC7P7h8O8LHiYST9uTPsjjcs2H2ST0EDMXw1ULa23kqycxF0BCmYsKOk642EM6zCvDrQ2QBYBXxjt0EmIoXNIC9UD3WHQ1OwOFlse5oc3Gg5tEK0fiqdXimt3oNN14EKn7sDQhxKZQ2LArqPrREw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a301749a37.mp4?token=FWo13SVDI1nW-hnsjyDFfIkbacnSRxP5ptzIITNDKvFLNCf__PAl5Xt3Ixv4eNo1Le_1L0jZNvismdoc3tJtsFpHdlo__fm4x0lfo-CQ1UfPKLrei4LFLaPqw0NKsL-n6r8s7UGj_cGnhlE3NqwXudNje2L0Q97frsCaSbC2AmSew4yJTLJqkTDJlGFuQqc_O9dC7P7h8O8LHiYST9uTPsjjcs2H2ST0EDMXw1ULa23kqycxF0BCmYsKOk642EM6zCvDrQ2QBYBXxjt0EmIoXNIC9UD3WHQ1OwOFlse5oc3Gg5tEK0fiqdXimt3oNN14EKn7sDQhxKZQ2LArqPrREw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
بهنام ابوالقاسم‌پور: برای پژمان جمشیدی سند گذاشتم و او را آوردم بیرون ولی هنوز نرفتم سندم رو در بیاورم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104364" target="_blank">📅 14:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104363">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a5d5ff55a.mp4?token=LqitNLK6qmz1RxlSpB-IUTvjI-vi0J2qwM3W_WEh0HoqyD_kSnhuxKmluJltzBqwVIvjq0JFCB_RqpHoEFh2VrMnIHDhT5lic90aAymKTpYMSa_7ue3x4d6RA_NuszGQ3xEsf3yKdwub608tbAag5diUOJ2gbAATt6L4U7ad1H9W3KJD35Blyp05Sw_nTI-lRee5ftMIXlRh2ovT4c7KWZHReo0TrxK2j5iJQwrN6dOqjt2Kcx8gFfzrvc_9pn6fB-U3doYtxxfVw1f0NEAZ0qoehXD6wEe67MK6fcj9te3WXH9ZcvkIFTXzf8EpS35rdpro_q1HwceMr0B4n-VEA4ZO49aNbJVNJhC57m8NsNLjUODWdlxN7Ak-g3B1SB6U0SgA1W1x608K4s_dMoFKZYJcH_5mEo8VPMsTyoZiJFUg3-Z6cAFjKjriEL-SUw-T9whTD78rgnZhw-I1pdNVd15_6nuRAqX3-t4lCW53eM4EJaRIkZbBQWAjr1e-ISq6raPDVifJTfsVT6FAeODEiPrnzawgiiy9fDsojkiR6-1xEE_OPKxYL8K-DWLpa-Czle8c_3CUgEJtxFos87EQF1wLsRQ6SaD-8GSx5AAvFypIgb1N46KEiGUUNEIf1BGmSY4ChDMgl7MXuID02e1FBmMDZP8ulSkhO4vkaKKoywo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a5d5ff55a.mp4?token=LqitNLK6qmz1RxlSpB-IUTvjI-vi0J2qwM3W_WEh0HoqyD_kSnhuxKmluJltzBqwVIvjq0JFCB_RqpHoEFh2VrMnIHDhT5lic90aAymKTpYMSa_7ue3x4d6RA_NuszGQ3xEsf3yKdwub608tbAag5diUOJ2gbAATt6L4U7ad1H9W3KJD35Blyp05Sw_nTI-lRee5ftMIXlRh2ovT4c7KWZHReo0TrxK2j5iJQwrN6dOqjt2Kcx8gFfzrvc_9pn6fB-U3doYtxxfVw1f0NEAZ0qoehXD6wEe67MK6fcj9te3WXH9ZcvkIFTXzf8EpS35rdpro_q1HwceMr0B4n-VEA4ZO49aNbJVNJhC57m8NsNLjUODWdlxN7Ak-g3B1SB6U0SgA1W1x608K4s_dMoFKZYJcH_5mEo8VPMsTyoZiJFUg3-Z6cAFjKjriEL-SUw-T9whTD78rgnZhw-I1pdNVd15_6nuRAqX3-t4lCW53eM4EJaRIkZbBQWAjr1e-ISq6raPDVifJTfsVT6FAeODEiPrnzawgiiy9fDsojkiR6-1xEE_OPKxYL8K-DWLpa-Czle8c_3CUgEJtxFos87EQF1wLsRQ6SaD-8GSx5AAvFypIgb1N46KEiGUUNEIf1BGmSY4ChDMgl7MXuID02e1FBmMDZP8ulSkhO4vkaKKoywo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
بخشی‌دیگر از مصاحبه اخیر و جنجالی حسن روشن که‌ کی‌روش رو هم مورد عنایت قرار میده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104363" target="_blank">📅 14:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104362">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdb917925e.mp4?token=cXdR-Fbl-QJfNcFIv9C8iTlO8jJ2xKjOMDCa4-kNWzD4sJPOt2Zvh_3ayGKESsL9Xx7KUXdK3NYju6iNz7ZdphCO1l3Yfg6wS-4V1T6Ac0uA2XIMUZJVS-688TjaLDthg8I-bIubAfxGR-VlE0xZU5wxDXG2nBt4zJFMGnoAqEIqc5DmljxRXM8AuFtIKAN8az74c4VqJEIx7dheMfUT4n_bpVfZ5HJzBpFrBylf9C8h5tzyoz_9L4y9z-a-_Ig2VBCd-q2nxb4o9Ii5LJJhWGzRzDE2P_Cg_-PifFbO4nWMuhUVk42vW3BxEkNC3Nh1ABXMacVWbWoAfBAaO1VxHopJwe6RDhBDHYXcx_W79QNMgSkuLfFEe-WTG3zamxkKxA-5iBtCOoZlpEAri2TGiYqAyPMpowRBn5xqjWh-GZ8VT7TYfufjjlnTp1HziD3o-I9rGFRajTgVujatAtP15vwb6-gdS7oU6TTCLt9h-bxQCoEjdzXWH8pKK5cjOE5ZbEGv1X-28QIxk2KhYCCn9vgO3S7UFXh9RrikUahDfsSvFXREwqOELE0hMN5kqj8Y4v696dtYAti8BRIDDYg7JqNm-GpeoaYwwsqijEZ4b_gk6aTbglvPc4l0h4n7PL-axxCxUoFE8JN7Ex1iD6yfePxxIji2Y-gdfqbtFY2oLSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdb917925e.mp4?token=cXdR-Fbl-QJfNcFIv9C8iTlO8jJ2xKjOMDCa4-kNWzD4sJPOt2Zvh_3ayGKESsL9Xx7KUXdK3NYju6iNz7ZdphCO1l3Yfg6wS-4V1T6Ac0uA2XIMUZJVS-688TjaLDthg8I-bIubAfxGR-VlE0xZU5wxDXG2nBt4zJFMGnoAqEIqc5DmljxRXM8AuFtIKAN8az74c4VqJEIx7dheMfUT4n_bpVfZ5HJzBpFrBylf9C8h5tzyoz_9L4y9z-a-_Ig2VBCd-q2nxb4o9Ii5LJJhWGzRzDE2P_Cg_-PifFbO4nWMuhUVk42vW3BxEkNC3Nh1ABXMacVWbWoAfBAaO1VxHopJwe6RDhBDHYXcx_W79QNMgSkuLfFEe-WTG3zamxkKxA-5iBtCOoZlpEAri2TGiYqAyPMpowRBn5xqjWh-GZ8VT7TYfufjjlnTp1HziD3o-I9rGFRajTgVujatAtP15vwb6-gdS7oU6TTCLt9h-bxQCoEjdzXWH8pKK5cjOE5ZbEGv1X-28QIxk2KhYCCn9vgO3S7UFXh9RrikUahDfsSvFXREwqOELE0hMN5kqj8Y4v696dtYAti8BRIDDYg7JqNm-GpeoaYwwsqijEZ4b_gk6aTbglvPc4l0h4n7PL-axxCxUoFE8JN7Ex1iD6yfePxxIji2Y-gdfqbtFY2oLSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آنفیلد تا پاپارا پارک⁣؛ ایزاک، هوادار سرسخت لیورپول و محمد صلاح، به دعوت ترابزون‌اسپور مهمان این باشگاه شد تا بار دیگر با اسطوره‌اش دیدار کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104362" target="_blank">📅 13:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104361">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7Ds--Bz1Mf3Gnp0yPhvt43R2iUMnNpGw42JTpoKbN4mUoCPZ6oFhP8yyoNM2yQP-ClI7QrPpGe4Z5NCVXdRcaEmR1NlkQ4qVxAimMN0uz9vq6E9SoP21hPvKJxOsBxtp_TBDM4R76RJfPE-axpk6VFhYHExi7YVvi-knNGkeEQs-Hk-YXoyfpha7AWw3UMbJhP8N977pmPUkAtvgn8xe6bNyLcwWtcBkgNTa9L4l-f5mknAkOTi1V9Kp8Gbg7wwfPUXUyhTrKQ1qxsCw4mE3HUB7cN4Qa6amCuvcBlm8RKWEJxVSkGzhbQIsjhUmFw6vADsoB9TEvYlK_M-OHhLGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
شماره پیراهن این‌فصل بازیکنان منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104361" target="_blank">📅 13:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104360">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57b5cc35a2.mp4?token=NEkz3U58jstDP6LMjFVrmYESDtJ12eOTx-bebRG2NqOI_tfPCOKMsAxI9_GeQv0GT2DwpDbJJ43oSX1xbKt2xaJHSgH_Wp4imWe_onCOogZpptRQxTHChn3CufyGuZ0lGpEMbryy1m4DszKeJt4Eou40ISyN_BWF1lU8tc6Mw1LRaZx6JqE1ZugCkp0x5vtYC8pELMQxGh6BA92wkdH5av1kSZCctPyTulJxvi2dXmuA8XsgH4kYE6yv-Zxm4108KIgvMp4k6wW2S0KEyUdH8q-3E6p6KFXMSQ5s17hljiIWZ2QOt9fl3WDy7bAsYEtTnxDN1396H5XvlKV37GZDyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57b5cc35a2.mp4?token=NEkz3U58jstDP6LMjFVrmYESDtJ12eOTx-bebRG2NqOI_tfPCOKMsAxI9_GeQv0GT2DwpDbJJ43oSX1xbKt2xaJHSgH_Wp4imWe_onCOogZpptRQxTHChn3CufyGuZ0lGpEMbryy1m4DszKeJt4Eou40ISyN_BWF1lU8tc6Mw1LRaZx6JqE1ZugCkp0x5vtYC8pELMQxGh6BA92wkdH5av1kSZCctPyTulJxvi2dXmuA8XsgH4kYE6yv-Zxm4108KIgvMp4k6wW2S0KEyUdH8q-3E6p6KFXMSQ5s17hljiIWZ2QOt9fl3WDy7bAsYEtTnxDN1396H5XvlKV37GZDyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو وایرال شده از کنسرت خیابونی در تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104360" target="_blank">📅 13:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104359">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8Y6yeC1EVbk526l4vuxfvRsVTBFlchf3hAsg6sYFZjNnFLs6CcEmL9xJM2A5iLIJEbC2jwJJRik4Fe-mytYJUGFuhMCrcaxQzwiiWzrrUB5kD1ojDx7l8oaEDQwBWxOEXhb9mm2jPx8XzW4SWaTb-zlC-TB_M1KmE7iDBVJqP5E2Cpbw_zXGLfUNVnDK3XZvB8xO8QFnHB7leu2aFxVpUViKbQ1a-X5yz4MCSqHXTJh32BJeQw8579GY5vI8Na2qkHYgr7hzGtWctAuyQ28p8UkNSxXF8bNVA9GgiR9r2wksIwTmu1Q-cVcuZhl7d3ymxQt_w38NmBf0G0QQG1WpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
اعلام لیست نهایی بازیکنان تیم ملی امید برای بازی‌های آسیایی ناگویا؛ امیرحسین حسین‌زاده تنها بازیکن بزرگسال این لیست است.
🇮🇷
بازیکنان استقلال: محمد خلیفه، رزاقی‌نیا، اسماعیل قلی‌زاده، سعید سحرخیزان
🇮🇷
بازیکنان پرسپولیس: دانیال‌ایری، فرزین معامله‌گری، پوریا لطیفی‌فر، پوریا شهرابادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104359" target="_blank">📅 12:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104358">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc7ebac37.mp4?token=pWb6KdIWxltXq8RiFbgfMhFmWaPh393ak4YibVE5OX-pZ0rR6G7yJlxzOY7FHWjzQKgKoMVkiPRoCOTXr9sz5ne3TcgDNKsXXFiUp3Ymo1rS1rv0etX6b1iSr7I2OYNPcV7DWkoPv1Wn-FcGqKh63FzchiwlVEHoRTsfHV61YSf_UR4oCVieboOWzCHlkJzAvWIsIX1R2wr6zoiG7vu3mqkOCb58vS_8csYclpMjbPVeG5GILUKKsBDYo_UrPx3veUUs_S5NJe4e29RQX49kME5uQP_jxryhHt2qepTsR5sh-695Zd5uRygkcnAaCb622b2G0Lb_PLDvjqXseelH6kuqWAHgRRdqA7CgK1M0x-KFrjCVsQD6v5VA_w9tDUVVj_VXhb2R12vlKHWFpgK6yrZJDCzyPzmkSEqlsGwUNyTuY4Z9PXyu3XbuEkVdd8h0twRUgjS94bDs1zASURipMqtibjgX_wE2-nvjOPiWvrcaAYB-U88Qlc8aSMPHr6jWz3YRn18Rwlkm2z2P_CY2l3qFqhYTJjrHmDzO-hBVn5u177TjY9apRmGjfrbeyZCycae31oLb3r3YSmh4nC8jsOyp-13EteSQMrs7uyC3W8fI23XngSZ_iZJMs3ac9sSvmB_WH5gNGLh5pkpdF2VdOwdytJwPlrXtU3ek2nt-e9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc7ebac37.mp4?token=pWb6KdIWxltXq8RiFbgfMhFmWaPh393ak4YibVE5OX-pZ0rR6G7yJlxzOY7FHWjzQKgKoMVkiPRoCOTXr9sz5ne3TcgDNKsXXFiUp3Ymo1rS1rv0etX6b1iSr7I2OYNPcV7DWkoPv1Wn-FcGqKh63FzchiwlVEHoRTsfHV61YSf_UR4oCVieboOWzCHlkJzAvWIsIX1R2wr6zoiG7vu3mqkOCb58vS_8csYclpMjbPVeG5GILUKKsBDYo_UrPx3veUUs_S5NJe4e29RQX49kME5uQP_jxryhHt2qepTsR5sh-695Zd5uRygkcnAaCb622b2G0Lb_PLDvjqXseelH6kuqWAHgRRdqA7CgK1M0x-KFrjCVsQD6v5VA_w9tDUVVj_VXhb2R12vlKHWFpgK6yrZJDCzyPzmkSEqlsGwUNyTuY4Z9PXyu3XbuEkVdd8h0twRUgjS94bDs1zASURipMqtibjgX_wE2-nvjOPiWvrcaAYB-U88Qlc8aSMPHr6jWz3YRn18Rwlkm2z2P_CY2l3qFqhYTJjrHmDzO-hBVn5u177TjY9apRmGjfrbeyZCycae31oLb3r3YSmh4nC8jsOyp-13EteSQMrs7uyC3W8fI23XngSZ_iZJMs3ac9sSvmB_WH5gNGLh5pkpdF2VdOwdytJwPlrXtU3ek2nt-e9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
‼️
#فوووووری
از بختیاری‌زاده: ناراحتی کوشکی؟‌ حرکت او حرفه‌ای نبود و فردا مقابل سپاهان نیمکت‌نشین است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104358" target="_blank">📅 12:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104357">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5711b4d86b.mp4?token=fEI_0WzDt7nzU81-N6Cr0_BaWzsckzoluNKSEqrbrffouLJpSYVHoSNba7LJ7XvquygWXSYiyD8daXn9-EWEva2JPcjSMkH4wF7BYV-fAPFlc_F9-aJzC6qn40Sqv0kIrWhpQ3KlpVxvCld6B5-o_SE5tPg4v270YG7PRrUH2P4KRlchiaeAGFXPxCuJOWBqE_gGranhAQ7N-nwILsNTE-ArzGXDIzCxMXBSS-fily7uzD0XYNEin3hmHrbCpALf_Sd78M8eeaSrJL3mh5LFrxALdJZp-XmHxvcM39SLJDLqJz9k2HAfAfB_HTU4K9W4VtblHiye0zVVCu7oegxW3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5711b4d86b.mp4?token=fEI_0WzDt7nzU81-N6Cr0_BaWzsckzoluNKSEqrbrffouLJpSYVHoSNba7LJ7XvquygWXSYiyD8daXn9-EWEva2JPcjSMkH4wF7BYV-fAPFlc_F9-aJzC6qn40Sqv0kIrWhpQ3KlpVxvCld6B5-o_SE5tPg4v270YG7PRrUH2P4KRlchiaeAGFXPxCuJOWBqE_gGranhAQ7N-nwILsNTE-ArzGXDIzCxMXBSS-fily7uzD0XYNEin3hmHrbCpALf_Sd78M8eeaSrJL3mh5LFrxALdJZp-XmHxvcM39SLJDLqJz9k2HAfAfB_HTU4K9W4VtblHiye0zVVCu7oegxW3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
نظر جمعی از هواداران اتلتیکو مادرید درباره ماندن خولیان آلوارز و واکنش دیگو سیمئونه به توهین برخی هواداران در استادیوم به ستاره آرژانتینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104357" target="_blank">📅 12:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104356">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oP0QvT0Ru-_Nro_7IN8rua8tFy-q6ajsKBw-1C521joBln7y0cfLS52M2_RFSJMCs9svOiKCjdk4EDgxfQShMOEG3WrVeiEOIu5v1MH1Mw1he2tg739vjEkMh44G0dXPh6mRDp0y3zKcSn7XgVtngJxzYUlVeI_oIr8_GDvf-wmrPktCnbBp1cDszaMyP_RH9V9-zCpPGiysLy9iWE1uto8kh9NNEBgw8X7QltiIWKMZZgvCiHq5W4d1es-s1mbnYDHmznWgwNz-99QvHpLwYRydzQIuAxakjIfK-RcbCCFVhnr2iUJv3OLShW29oBjnGi4Oxfy-QjjFn8DbM6SwQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🚨
مالکوم با عقد قراردادی پس از جدایی از الهلال به تیم‌الجزیره امارات پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104356" target="_blank">📅 12:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104355">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5eHXEWhkyrhtFuB4zaPz5PKoEgXJAwtTbvZaSF-czjtMmxoOIhwp6Ye1YEENbyOC7duN3-GrWSVmPAbZJH_fnmjb1zQZczhdNnEBZOnePcWhi6exGKzxJYB4K6gfSFI_Mfy7O6X1zeCnSP5zu3nl5WZFILR-bktPoPh74r6ii_ETZN0J_GKhe7HXn2OqgSkc6vpGDULfl-9soH1cCeJMjdP0V8_nVIqPDLXnRDXufV1SLgUZLmnq_um1Lvgg6S8HF7WGH2zqg1x0wu3ovU1374fY08Z4SKLgQ_N1J2RWGv0NeK38foQB8IH8bSfmwxc8Apo81AuNg71Zq1vvK0kqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
سایت برنامه عادل فردوسی‌پور پس از گذشت چندین هفته رفع‌فیلتر شد و در دسترس قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104355" target="_blank">📅 12:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104354">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab7bebaf5f.mp4?token=nCTofgDvjQGpdbaB_q1dFWQbPcPb3FZAFO36_Gr2wihnGXW9wuKGklkr1taIyBEaHdft4z5sw_8wxVe7g6JBkUWhmXTEzk-emwy0jaF1-I5TFc3ueMQVhzg2gor4l17Lo7Z2IUhqnMOi7aq5TEOsEvkoq_hgo5gVG6AhpIOU66JxQF6sbMgXnuvigEidyhB9yTlQPJ8HlS4snidmGVru0Rn8M5O5UM7SPydoqHYQcyH53Utfkt7IvsHkSYNmDwsDJmJ_GMasePXqjOdiUQpFkei_Q0pEn03EyRcIMUfP2xo6FL8hUb4HTE6jkMF6oVig1kesDsu-ypA-paqmwdk1vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab7bebaf5f.mp4?token=nCTofgDvjQGpdbaB_q1dFWQbPcPb3FZAFO36_Gr2wihnGXW9wuKGklkr1taIyBEaHdft4z5sw_8wxVe7g6JBkUWhmXTEzk-emwy0jaF1-I5TFc3ueMQVhzg2gor4l17Lo7Z2IUhqnMOi7aq5TEOsEvkoq_hgo5gVG6AhpIOU66JxQF6sbMgXnuvigEidyhB9yTlQPJ8HlS4snidmGVru0Rn8M5O5UM7SPydoqHYQcyH53Utfkt7IvsHkSYNmDwsDJmJ_GMasePXqjOdiUQpFkei_Q0pEn03EyRcIMUfP2xo6FL8hUb4HTE6jkMF6oVig1kesDsu-ypA-paqmwdk1vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نگاه طنز به معروف ترین دعواهای تاریخ فوتبال.
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/104354" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104353">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
حجت‌کریمی مدیرعامل تراکتور: متاسفانه قانون ورزشکار قهرمان برای معافیت سربازی شامل علیرضا بیرانوند نشده است و به احتمال بسیار زیاد باید این بازیکن راهی سربازی شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104353" target="_blank">📅 11:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104352">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFmOyn-rC4_8nOy5W-kumqsmeijSBP9VZJWTYPqL1i3kzTlCdChFVlh2uE9Umuz23hdV7LvhRZTqMfPMy7sxEl19kjz58i6xnzxtRM3jabnwwAbLPXjfUx_r-6UQDN6gXVRQa0vPQ0F9OuUDXgvkVtAgpjvZxQ2L6nxw1V1qQKz7_EEyoMfxpOI1CK8bbU7tyihWiFbDKSFybvTipBpB451HASA0bq0p5XWbW23s2zdHRKcnFzfuzn-RWTPstAXoUe4BzOOLksauas-lmCUWViKpIjtFm_RwjbbHY4lcMVaJDXxjOgxmnEjegcRWVtdRD55c_iRXmGBMgZE_vhcLlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
حجت‌کریمی مدیرعامل تراکتور: متاسفانه قانون ورزشکار قهرمان برای معافیت سربازی شامل علیرضا بیرانوند نشده است و به احتمال بسیار زیاد باید این بازیکن راهی سربازی شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104352" target="_blank">📅 11:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104351">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlGY4ltJdjET7eUVAachkYfbmzZBI7p7e1dwlGX0pZ9RvvVuJVcGTTGKYEqcb5lGw_ujhXraLA7aj-4_H7FBHxkJm2uJp9R6LQVGYQak4Ml8QLb2F4sMiLolM61jBhgLLLqziAAsBdFrkBzWz73g3CnlHz2RCwMlu1vEYYEYF_zLgRQ2LeciYPAaDaJosPTOpHwRW-7YoJxAtxBJIAwfDPv58xMW933T5hzmmv_gdey5PnT4BUJAMVkPzYOfWBIkTxJkRBmPscajwlzlmMR26Ixe7xjCynJ3TNivYfBfZ_TLLEqoHzYxFANPSEs0hSPrNPqughmRZkCE90tAi6ZSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
اعلام اسامی داوران هفته‌سوم لیگ‌برتر
🇮🇷
🇮🇷
استقلال - سپاهان / پیام حیدری
🇮🇷
🇮🇷
پرسپولیس - تراکتور/ امیر عرب‌براقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104351" target="_blank">📅 11:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104350">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qd8nk4woITixfHsCpzSW3gMmgnUdzVTvKN_GkrtHj3J68itqnCoeoEYJI3ezf_sb4RAFKPqAy27DJ4TC2xN9EAXBlH6miZROSjBxkxe54VvImu9-4KFv4Dsm9UaEGfZo4cft2xvnuZI5hpnbjRynTUIU-qjq3nVLK76jt_gctuftMk9UW-nnG3W7q73Fmbl9c7IxN9BH_2AZprZMpzCVE4k1x-XE419ftXhkuk20O7CMy7mG7g8XN_DpMRbF1OtFO9OGdttX0jRJCo57uvD_YTT3u6t2M2vGYO01xKM_k1YdSxJqx_8Dqc0m-NzbU2s43Zf3fJ2f4FEnLXnqiFMABQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
پوستر باشگاه استقلال برای دیدار با سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104350" target="_blank">📅 11:17 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
