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
<img src="https://cdn4.telesco.pe/file/Z0TKig1_0FQeIX0S6sF2CfITDVNLwyGcZuc_AdPWU4nEpn459E6T7RLACl8ZKkuKfK_Nreejl2ljTx2wDeTemKRd5Kvt6BDyMQQfTq2Gz_CbkaeEADrafctv41ewt55nBlm53geb4yvpcXNp2VjDifj_4NLf1bQh-ByxDmA4JPaIsW1wp30yqO8vTvdwfUTW62VJixZPmF_qQt-pBlbCwF3-NpLXEm55OMFiIBSUvrI9sNp-x01sAjt-O5-dBv-Vte6a233XZr2Q-jcvJp8MoX--tOZLO9uHOUE5aQExL4rHo1tiWiYWF13ZvzRPnh8liKbWe6mmUS7e6q-q6QtgsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 00:22:43</div>
<hr>

<div class="tg-post" id="msg-82578">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
آف ویژه سرور های V2RAY مناسب نت ملی
🚨
🐿
خیالتون هم راحت باشه حتی اگر نتارم قطع کنن وصل نگهتون میدارن   لوکیشن ها:
🇩🇪
🇹🇷
🇺🇸
🇫🇮
🇳🇱
🇫🇷
🇮🇳
🇦🇪
🇦🇿
🇮🇹
🇵🇱
🇸🇪
🇬🇧
نامحدود 1 ماهه
▶️
120T
👑
نامحدود 3 ماهه
▶️
300T
👑
نامحدود 10 ماهه
▶️
600T
👑
100GIG
▶️
50T
👑
200GIG
▶️
100T
👑
300GIG…</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/funhiphop/82578" target="_blank">📅 00:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82576">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
آف ویژه سرور های V2RAY مناسب نت ملی
🚨
🐿
خیالتون هم راحت باشه حتی اگر نتارم قطع کنن وصل نگهتون میدارن
لوکیشن ها:
🇩🇪
🇹🇷
🇺🇸
🇫🇮
🇳🇱
🇫🇷
🇮🇳
🇦🇪
🇦🇿
🇮🇹
🇵🇱
🇸🇪
🇬🇧
نامحدود 1 ماهه
▶️
120T
👑
نامحدود 3 ماهه
▶️
300T
👑
نامحدود 10 ماهه
▶️
600T
👑
100GIG
▶️
50T
👑
200GIG
▶️
100T
👑
300GIG
▶️
130T
👑
500GIG
▶️
220T
👑
1000GIG
▶️
400T
👑
5000GIG
▶️
999T
👑
❌
بدون محدودیت کاربر
❌
😍
با سرعت بالا و پایداری بالا و دارای 10 لوکیشن
❌
فقط 20 عدد از هر کدوم موجوده
❌
💎
خرید فقط از طریق ربات انجام میشه
⬇️
▶️
▶️
▶️
@ZENTROVPNN_BOT
◀️
◀️
◀️
▶️
▶️
▶️
@ZENTROVPNN_BOT
◀️
◀️
◀️</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/funhiphop/82576" target="_blank">📅 00:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82575">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kzm-iMfE_nkbpNZIevJpYXLKuQdwLldprQcAdDcU3uOHUxjd7RTfnrLx4mwJITMvzz08Fr5UTGUzmHlylebnggluD6v3lb_ZMkLAVbBlY3iCyLgShXn8HP7LxZVO0WpCIA5Huq_tWOQF9TER7J6-uSgmJUmDoiZBSMIYBpjeh4uI4Stz-OcNyU6wURfAacMI5_WhARDyU39CxTYOvYIJGK1bHG3IaZwr3rO0ABV8nVHrBUPCmQPW8UuXoAixkx1BA5cUcGIOgqItyPfkxBAT5wJPlqBEQ8WZ0lEyoaOhytNInDrya3Rg02KcgDCWbaoVllybxNnm_vNWLaIjXXqnhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو میخواستم ۲ ساعت پیش پست کنم منتهی برقا رفت نتم قطع شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/funhiphop/82575" target="_blank">📅 23:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82574">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uvyy1ZG2VycmMoYUIJkz-Y2Cj8DwJFNuCjXBc49Ws_tvxcQ40aMuDVzTjoTNOOYxtBK-DPKHfGoxXN8MJyqwgWGdhBPefl57FfvlYUhzSJnVI3fW_76uKJ13ok3IeJae0nffuVrSn28VpPQkBtP5DzpqIjhtR5w0ekdv4VWqTUA-sE9PqL-DfuPV-S0PXs9NbOi5KJx0P_w6Dl_djErRFTOT_0oUqSnXD68UrchKub2-psRlGBrI3vtkURwdcZHLoAUjoB03Cv-5Z1u3ao_idYarLhon4cWHDy2hDlUAGA2ehuSsA0Lr37ERZwmEjRgp4xcLBbHeVmqyBNE4fkdrew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریر تلخون تا اینجا کلا دوتا نقطه عطف داشته:
یکی اونجا که فان هیپ هاپ تصمیم گرفت مسخره‌ش کنه.
یکی هم الان که خودش تصمیم گرفته از تیمارستان امین‌آباد تهران دوست دختر بدزده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/funhiphop/82574" target="_blank">📅 23:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82573">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfsizrtiG_0as0JNyIM9AnPuBw9rLXHfvm_W-kNVvZFTfcqYCM55SGLwooO6owuMYETUFGh60XKwAyN6ENVobrZyfRwzk0F58--dTNNW27gkU42ecQE68MMD9xnhIKHX9u5sEKmuXMWQo7bh-v_2JjCKqnP35DgNFsVd7O3SMVPT0baUWceIcrCG0rs58DJSaBqsYUg6E8pHWLZiBgfOx2sYd3ejKCWc6KEgHLDvwQJJyAudktBGGTMh0lb4V1kLvHcudCm6C7IsTHLmOySulIk2zOLNSOB_YFocblr3iEvYqTJm9tJV8I3jV3US7ptuua7c5qvqo9qysgYPP2gJdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهره هوشی اگه عکس بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/funhiphop/82573" target="_blank">📅 22:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82572">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdvmtDVTixvS86TLWUFZScEgqxAGtR0sYx5IekbtaiDDJQgcZazWZQoEIczohjS3qCQLXlwNvj7Lve7UTRQw8kO3uzCVbr7DD0G97vDqgRvcRdiz-65x-P16IJc5ByhlcrnaraAolQR7ovG36wL1KtLBYRZ8yXlFqR_OOUqcopVkRhV5Y75lQNSrIxmJM40JK7VAiOCsvE0WXOqkoqi-T4Wh7V1wg_xvOblX18H8zrO9mnwxJ3BcZfOty4Z3Jcz_U9ZCuYqFZU9DcMVnc5M1Nfgz5RADYTO4ajEawS62KT3cwTkpMbF93wBu-WW2EdvIttjW8uZ_xq40Gry6srdqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/funhiphop/82572" target="_blank">📅 22:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82571">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترک جدید داریوش تبهکار و بیگ شگی به نام "Vice City" منتشر شد.   YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/funhiphop/82571" target="_blank">📅 21:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82570">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMxgNudrz_a5w3P0fppWarah44JAv_seisGRfcNvh98laZfGLXbU1-EaqhOC7xMfOOjupCaYmV-ZGE_6Xu03jRVp5DpqY36NkHnzU3jZsp-_GTWVHKFe2eqgXkyeEJ8BEnlPIyBU7PWBRpOgZSRTyhEv2r5JaBacErRd6_GFOqlSR61vbe7YTH7SFv-dj20SuWr3RHUTlNNJCxuR1as2iC9n1lkeAlp6gU2tB09k1AhNylqy0cfxy4UGbGzu9G-WgAetRXxv21SezYRUdTygG6Y4KSjaYbrkOe4gaPr6z5ekEGar4NErX3bEgsrfoGNRjDwUZcnUD1lG50_6ueQqhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید داریوش تبهکار و بیگ شگی به نام "Vice City" منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/funhiphop/82570" target="_blank">📅 21:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82567">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49661a4016.mp4?token=EnSbJRHd1NMjlZiThleGe4GTzS95k1EOlGPFCTcLuDmPRvICOqkkspJGoeJlq1-tJcM-SVE1jFhdL_SQ9V5WbbAZWemEpeId0lRZ1smX3q2DDZbes5g76Pzm-mNnSKtqfjilx4Tnr_3GFT6bwMFruEq3txeKG5eBtuqrcRFpVb1ArfwUARqITsSy1eSyucAmGV9uzkYAvzBbTNoCw5U1FNwSU67DEaL-rpxl9iewPhhiG_KQ09uOK4VGkeKPHwXNIkhIqI-6J3RVJn6NY85sZurfbfa9fKonePX0r-skCV9KtRe0P7fpRiDW5DsRUFFNjsBANhrxGTzGWBgDt-pKyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49661a4016.mp4?token=EnSbJRHd1NMjlZiThleGe4GTzS95k1EOlGPFCTcLuDmPRvICOqkkspJGoeJlq1-tJcM-SVE1jFhdL_SQ9V5WbbAZWemEpeId0lRZ1smX3q2DDZbes5g76Pzm-mNnSKtqfjilx4Tnr_3GFT6bwMFruEq3txeKG5eBtuqrcRFpVb1ArfwUARqITsSy1eSyucAmGV9uzkYAvzBbTNoCw5U1FNwSU67DEaL-rpxl9iewPhhiG_KQ09uOK4VGkeKPHwXNIkhIqI-6J3RVJn6NY85sZurfbfa9fKonePX0r-skCV9KtRe0P7fpRiDW5DsRUFFNjsBANhrxGTzGWBgDt-pKyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#Mews
🗞️
“ NITROUS “ Don Toliver’s New Album
Coming Soon
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/funhiphop/82567" target="_blank">📅 21:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82566">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024532bfe.mp4?token=vHCDz0pgA1gNtj7ym0lw_J7aCiRwfME6BVi9Ut5PljDQiRqDsc6C6q1opv_5X5m2wcGpTNJJQTzS8S3Qs6zGvxOS8ND5Br36bjrv2SDxgm4ne9WBnV0du1oLx1tUdcNzyGes4AzhjA4jZkp_R4HSuFzxpCi1zQG43uizgwfWkMCjPRkU73wavp4XHyFzFduZLcs3x2rkErOmK1HS_tAjlulGkzwREXHr7mH-n8f5-sWzkq5K1FH_bWjUYqGKYZASkMJ4Q0rs93kE5i_VjXfjck7QfoId1RCxBMMj3-95oWRewaqWoPE2gjMAwAQqukWcX5zcJlYU6gNimUHSKP4EAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024532bfe.mp4?token=vHCDz0pgA1gNtj7ym0lw_J7aCiRwfME6BVi9Ut5PljDQiRqDsc6C6q1opv_5X5m2wcGpTNJJQTzS8S3Qs6zGvxOS8ND5Br36bjrv2SDxgm4ne9WBnV0du1oLx1tUdcNzyGes4AzhjA4jZkp_R4HSuFzxpCi1zQG43uizgwfWkMCjPRkU73wavp4XHyFzFduZLcs3x2rkErOmK1HS_tAjlulGkzwREXHr7mH-n8f5-sWzkq5K1FH_bWjUYqGKYZASkMJ4Q0rs93kE5i_VjXfjck7QfoId1RCxBMMj3-95oWRewaqWoPE2gjMAwAQqukWcX5zcJlYU6gNimUHSKP4EAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی حاجی پشمام از نسل جدید ناموسا اینجا ایرانه؟
😜
ناموسا تهران کِی انقلاب شد ما خبر نداریم؟
😅
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/funhiphop/82566" target="_blank">📅 21:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82565">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb65d06f1.mp4?token=Y5MqfT7Qu8U_W9LWFvOfR2WvMZW-7SUeJCCExtI42LFvKO7tMOwnwlUHwTQAmZewq-8k5KPeNLdOszF9fy19idRQ9HlimKoYBwoDN_eg6jR7PeNoKCG8a8vXcbckc70NlRdbjdbpKhT8-Q3FNiQryLJVFxZIGuUfniMMiAMxO15OfSEstBST5FwtGyJfPDVSfWNHQuNcSdU22lorNEgLVE2OPjPxVGw6fc3RnGh-_oyDj24cjkDdvl9-GIsrLu6nCssgFGaLNdDdv0YjCtjYpeWGj9GfKl-GypzjuEbLe_Q-x0TlndQ8m6QMj8EhK35uz9ln3pavuSJCJzz8yptPAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb65d06f1.mp4?token=Y5MqfT7Qu8U_W9LWFvOfR2WvMZW-7SUeJCCExtI42LFvKO7tMOwnwlUHwTQAmZewq-8k5KPeNLdOszF9fy19idRQ9HlimKoYBwoDN_eg6jR7PeNoKCG8a8vXcbckc70NlRdbjdbpKhT8-Q3FNiQryLJVFxZIGuUfniMMiAMxO15OfSEstBST5FwtGyJfPDVSfWNHQuNcSdU22lorNEgLVE2OPjPxVGw6fc3RnGh-_oyDj24cjkDdvl9-GIsrLu6nCssgFGaLNdDdv0YjCtjYpeWGj9GfKl-GypzjuEbLe_Q-x0TlndQ8m6QMj8EhK35uz9ln3pavuSJCJzz8yptPAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرات حسینی تو ۵۰ سالگی:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/funhiphop/82565" target="_blank">📅 20:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82564">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hg91-he-VDZRhibBzDQMriQDZh2lDZzyoiip4-fg1OIY369aLmWgg2XvFmoY0uD3RyednwRuNCiQaSzSED6ONRl_vYlQ8M_LblwmdEPe21BQHzPQvkYyt8-3zgelWI9FPsCw2XwWU0kIbi-w4NW1cqvdV4SKW1V6d7lmuJ7sIVDi3y_nx-KAmRrrgyBCg5felAsm12Nd9_fYmz4-OA-bwgvVZSbeV_XB9xVu9dSNc_nkFu0yiCsJ58QRUHoed6pztX_K4LEX2oVXZY76dZIkicTigTnrh-fDxxYKJ0v54f3_bITFT50ZuwNiFabHeJe-358YooCgaRXn-hIwGP8r2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل ما از خارج و تحریم ها نیستند مشکل ما مسئولین فاسد داخل هستند
اقایون مسئول خجالت خجالت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/funhiphop/82564" target="_blank">📅 20:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82563">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کانال 14 اسرائیل:
ترامپ به تهران دستور داد فوراً کشتار مردم خود را متوقف کند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/82563" target="_blank">📅 20:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82562">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">از زیر این توییت واقعا گیف های شاهکاری پیدا کردم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/82562" target="_blank">📅 19:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82561">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Orq05rJP_aYbkFFvlNrmVWwSrRX2nPlugl1noDySFx8PYxlG7dmjxDops_3PjIMtnnxTb6AHRjy9Te7NxGNCQx6FHvYqcFEdHw5JzCFRFKolvPuUqqdOahoDnDs87V3Lr0tJeXu12OjIxj7FImOMNq2hO9F_zOI7Ys8smWsGsECOqSIC3FkTjVevqWiqvOdzoQcUpCLiwyBajgRuxNKPQZL7FlfGNMDB0cQ_NMo6i-uiFwfjTj3jAm9odo5rHwgicyMEd_4CiB0-neH9C70pn7DuTyv8qkMYH0VUPrNuzXMWItyitAHs9bZnLiZhVUt7_8xePyowLd2cZncUDxZFhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زیر این توییت واقعا گیف های شاهکاری پیدا کردم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/82561" target="_blank">📅 19:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82560">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0RlpWLGwli5GXB8b4H4WodCiO20AH2_SrciXHDh3IpmTDo4LZgLDinTM0BqqAbeM8iPwF5gMfTJTlJ1opDf4OQceU9tcoitbnbMVcnAVaBORTcw7vxzDOFjrzsP-4Hrh6k-Pq97l2E1T3zOFOxWShGedflt4HdMFjK7y2TYuZIALy2441D0NTfJwV8J2nIciXWbwzvengMLehHg1uXLuHaN3eioVyvA4eonOuJy2ZZXR9MpVjekFG97Nt3iC0uR8CXPMMtENRjpHut3a0BAVXSyALMiP8Ds7GGA_mT8Di09FCVQ91q5hjycxJwf4jf71vOtqkVS0FgBgYcslTlAzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرادر آزمون دیس ویناک به پوری رو پست کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/82560" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82559">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">به بسنت باید بگیم عمو یا عمه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/82559" target="_blank">📅 19:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82558">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llMTd-VWWscVvLP_xMdDMMCqoXKwWzFYFmPM728sd02WEmUYC46yY6k3SUMJclpV4kqoNYuGSOpx7RYZPB5F-IE_hIlYtWbdcGH_u3M0Jkdz2EACDQmsBoJfJMKFHE8VMPR2AyFILpLvY_WdI83WlTbAYn6WO5_0HyBxyjkPQ_BPouywu465Q0fimRwNHGxBmjzhRjaadaTUAOp968jiaGeT37fQMc00N8OAECMZfbUGAfHQ7YZElvIlWIqsDmc4zekQXllPk_EjAATVQdpjcDPYG_baWkuYxtjOCZ8RpLf0pYY30ZmIpuJ80Ng9R_CFNVWBeb5DsC8bzE9X5WV7gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویسکا آسایش ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/82558" target="_blank">📅 19:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82557">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWjlLJTc7e80vHtqyat2rsKuGlJ_miC0UGv9HG_PcZ1gsVmDn7_wgD4btb01jFXcgwqfIw4mZj2h-ILHK94tjxT3ZRuxKRBB_uUGZq_3Ud0EApTqPXfeyMkfsJePSRXJY8XHpGSNAy5vk7EIDttcADjra-Z_kMSLTlNs-FjldrsJs5UMBm5cF85fIakuoQJRFJ4LqNjlLcC0h5eqNy2vqLyafZLulh3ggLcuW3v0WTUbsYlPQgvqM2F10OP6gpR_dhTuDy0E-Zz-BruXTjPc9kQQcBMViOFHgNAZmbt2QV2tF6KgjA9MD4jai-DEfXPxslemTkywKCb20DnahtG_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی ویژه هفته نخست لالیگا اسپانیا
💯
⚽️
در روزهای سه‌شنبه سوم تا پنج‌شنبه پنجم شهریور ماه، با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های هفته نخست لالیگا اسپانیا، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/LA-100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g3
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/82557" target="_blank">📅 19:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82556">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpLacm6naP_QKNHuaRwrzGJmAAJpSoMaUvMjXoE9kYP75lDp05SKslZrDnTk51CdrH0ShmXfN4Aantfc95qZO4_GeyRyq_8OhGnHQ01z07gzG0yiON5kp-r5AqVAVTYIZPj9xJClmH6ok_igWDuWRyj5cjufEKKfyA_YUXyRkJKHtFvyRTT2bdj-m3lBTSQhUYENEvfpFftuRPumrf_CM0b8sYxqX9xIkyQxDPYeSB5Bs8bPbv3PFXfJayV4fFtwUA_MkK3_0GBzAMEWC2sikwTP9F8vK6S_VbthB-XxUWoTgAlO-1ptHVDSbjuxiK2McwbRMitydre5ZX0iKZTxYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام HESOYAM ریلیز شد.
SoundCloud
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/82556" target="_blank">📅 18:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82555">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ:
همین الان از طریق نیروی دریایی ایالات متحده مطلع شدم که تمام مین‌ها از آب‌های بین‌المللی تنگه هرمز جمع‌آوری و/یا منفجر شده‌اند. به ایران اطلاع داده شده است که هر کشتی یا شناوری که مین‌های جدیدی در آب‌ها قرار دهد، فوراً و به طور سیستماتیک نابود خواهد شد.
از طریق نیروی فضایی، ما تمام مترهای مربع تنگه را زیر نظر داریم، همانطور که در کوه مکوش و سه سایت هسته‌ای دیگر که قبلاً نابود شده‌اند، این کار را انجام می‌دهیم.
سیاستی مبنی بر عدم تحمل مطلق نسبت به قرار دادن مین‌ها، به طور کامل اجرا می‌شود.
از توجه شما به این موضوع سپاسگزارم!
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/82555" target="_blank">📅 18:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82553">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17ebe602ff.mp4?token=FEUSs3QNjqB91mzyuZqjgalblwjziqqbVZbuNYDZOPOClthMigWkFzuD-9SWkcuu2kXvkOIopyMGYkdLHWlTp0lTArs9V0aEEgoLnfSRvtmR8ovyMgL5KI2NSWYiez0bor0Yl5LRUwHnyY0Fl8vvYdUtxSAl9b9QJyZNckaZBypBZ2IpIYgVB10Pukpu5MzAfjvYwwHM0qUQCEFgrU9REVeCjS-1G7OHf5c2pGpGTBsr79kWb6nm1O9xDjNWglPrL4safMr0hrxG2evxjE06Uy2GILNCadrkNT2GIs_S2iTFA5o-fM8zMK6H4INd-P_HDjWiutfOjrI3uSWB2Rce1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17ebe602ff.mp4?token=FEUSs3QNjqB91mzyuZqjgalblwjziqqbVZbuNYDZOPOClthMigWkFzuD-9SWkcuu2kXvkOIopyMGYkdLHWlTp0lTArs9V0aEEgoLnfSRvtmR8ovyMgL5KI2NSWYiez0bor0Yl5LRUwHnyY0Fl8vvYdUtxSAl9b9QJyZNckaZBypBZ2IpIYgVB10Pukpu5MzAfjvYwwHM0qUQCEFgrU9REVeCjS-1G7OHf5c2pGpGTBsr79kWb6nm1O9xDjNWglPrL4safMr0hrxG2evxjE06Uy2GILNCadrkNT2GIs_S2iTFA5o-fM8zMK6H4INd-P_HDjWiutfOjrI3uSWB2Rce1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شایع فازشو داره ها قشنگ.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/82553" target="_blank">📅 16:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82552">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApexNet Shop | اپکس نت شاپ</strong></div>
<div class="tg-text">🏳
سرور مولتی لوکیشن ویتوری موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر نامحدود 90 روزه - 45000 تومان
🟡
سرور 20g - کاربر نامحدود 90 روزه - 95000 تومان
🟡
سرور 30g - کاربر نامحدود 90 روزه - 135000 تومان
🟡
سرور 50g - کاربر نامحدود 90 روزه - 225000 تومان
🟡
سرور 80g - کاربر نامحدود 90 روزه - 360000 تومان
🟡
سرور 100g - کاربر نامحدود 90 روزه - 430000 تومان
🟣
همچنین سرور تست موجوده حتما قبل خرید از ربات سرور تست دریافت‌ کنید و بعد اگر راضی بودید خرید کنید
✅
🟣
برای خرید از ربات زیر استفاده کنید
⬇️
🤖
@ApexNetShop_bot
🟣
برای ارتباط با پشتیبانی و مشاوره با آیدی زیر در ارتباط باشید
✅
👨‍💻
@mehdi_splus</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/82552" target="_blank">📅 16:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82551">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mc-s40vpnwOhInR1biFpdw9frZxWlHBc9h7teX0rJIp1MPpvJkkhyWmS8WmMj_Zm2fY_-GQi5TRejBVk9-QAx1sroLKVOKoW-lRdsUqTeZCAQ5dzp3Ytjo-kELam3aAqr9kCJ7eC5JWGGSorkCsdrNxzkSCwpQaJv8GJcbdPhRW-5SZ7Il02SlPt7xouDUMMkwUxdFTD2EbayqifWLr7lIoQVqQT7bwIkf1dE880Tksdgys2uWnAiRjYgj7aiixHqJ0j15iQHwNxTdvhh0dzv9rUkQzpUqZjUzJoWQVfNnpBrtWTtJ7CVZwFtTAMP6VbNzx9IBG722exUTvsMplSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورمممم نمی‌شهههههههه
پسر ایران بالاخرههههه برگشتتتتتتتت
🥹
😍
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/82551" target="_blank">📅 16:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82550">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/adacd9a9d3.mp4?token=G_xXbCGkqPejh98ToF74KiZcujukbyYXJWWgwpdmylJV2sU1-lMV45ILiC1OTfRi4pzq1xfkLtqPiul0RJeichEF02bmPoHgW6p3-LXipyXjlbqhQiHxRRegUhZDNsOsGqC8JooHy5mSGoKWkCRWSek16_vIKWWLP-Dl5NNMSB4-4RWwu1OeNUPMQkzWe0x1PrMIWqXEy0p2b7jStgXraW2aOyCwLfwq7_8uOuo8kBJ3t-rvPw5Dz63iMg2d5ntKWHPtgXEMHucI-glz-sNtBMqYlCkS3gK6ny8wWwqlpg3zc_M6eBghg_K0r9lcxC4TtzaWzspfKUFyAM5pEEktJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/adacd9a9d3.mp4?token=G_xXbCGkqPejh98ToF74KiZcujukbyYXJWWgwpdmylJV2sU1-lMV45ILiC1OTfRi4pzq1xfkLtqPiul0RJeichEF02bmPoHgW6p3-LXipyXjlbqhQiHxRRegUhZDNsOsGqC8JooHy5mSGoKWkCRWSek16_vIKWWLP-Dl5NNMSB4-4RWwu1OeNUPMQkzWe0x1PrMIWqXEy0p2b7jStgXraW2aOyCwLfwq7_8uOuo8kBJ3t-rvPw5Dz63iMg2d5ntKWHPtgXEMHucI-glz-sNtBMqYlCkS3gK6ny8wWwqlpg3zc_M6eBghg_K0r9lcxC4TtzaWzspfKUFyAM5pEEktJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب این الان یعنی چی؟
😭
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/82550" target="_blank">📅 16:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82549">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqbWUL6UcMChlMIjbHZQNGfKyALMt7QffbQH8VJ1i8gn1JElEX4dvg6A_PqXwrbdsFZQZGZ-x9P5Wk4xRWIPYPFU_17SB37ERqO5qKxiTeCu7q4jFWSnnCMiu4SarPXPcpdkLou5GwKamisWqLXjSlXhboW9j0y7kNNbTgHGHky24Jw2TRol_mIJ8XoNoq795EQa7B_PB1xQlQvVYl14ASIwob_GzD4le3gMfXJb-4a3Dch2C0Ay4_nu7BMuNHx4hTS-aVQG3uL1WFYabsfmOySd_sOsBrKeE79hd5f8tKxoApAq3LKDXS-RWrJX0yUSeKsFG3F0PdBHBUfmm-TDAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۹  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/82549" target="_blank">📅 15:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82548">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5s9LVME8OiYW4teg4EYqPHVCLICf4fLXyqCfaoVq_QXsvH1CTdKLwojXru_RIMRu5riVy74qkKOfztEmtmi_EUp5htcSVCmfVt4O-a7G47Y9IKKfSosHDmCXpihs9KKCCnUCxHV3GJOFCDY75VN0Bi10dzx18RdT3RcMdNRqNkMGS-DN3KFGKvER4b1vGqHmD6hXdiUtPw0UZYmewH0eQJm1BoRERtUCRuRbtLGHYvAolB0b3ProHWyfWol-9Mxv8obymwJCffzda0Q9R9az2blIXaTfP-HKmIpvQ-rQcZgE74y5TEJ6mlPvaqUvdrHs9fsnlj1D-s-FEp8W60fSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یعنی دور جدید مذاکرات؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82548" target="_blank">📅 14:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82547">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کار کنید حال کنید حال کنید کار کنید و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82547" target="_blank">📅 14:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82546">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu2StN_WwLQ51-c22gI5-FBwM7Q4pu7vyaKbihHl56FzyNIaZVqCjJEbegdxO-zBUrzZtQgd-FCKviSSKS2tVezgu-gQ4FakpjdBiTzhAGBTmmRPEYT8xs5MvLrQSKMn_M9FOYRi0sHjjjtWLRMVxEM8G0yE55EqyK31e7WKF8ecyLJ8v_lrtn7bMZNTu_PM_Xeyg8zJuuj9xxIHGt6lFuOEqGU_T7C_us6bgL9nnj3_DaMMRidDL6w9bBm_qbHjv7Kuk5HjMxBdr_Mfz-bKOVrLFZwglbbp2rA-bN1pnN2fj1a8k332mJST_FPBnyBMWBq4IqjH3L_xlGiHrGiK3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عکس دیگه از مهدیار لیک شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82546" target="_blank">📅 13:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82545">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9968bc181d.mp4?token=VEX8AiT9-xTXdB9tDsBnQR8ktlo4hqy5yE8JBaKI1bim5BithH4ctFTP69ACIS6NCvdVuHbHYrM7AB7_Ssl2EbdusT8wV8S8jpcqq4Sm6eT-MleD9dBGAadix57XaKeIVCXWAMyyDKVjK_mZAsB6eOLRJcoQKqpEQkd2nk09Ve23atWjdj0iTwycJHHxAVWkzDkEekmJGhlKSL7aV0XzR2l0kJmvHETO07B8pfYOJUDBBRvfGM-XOaCpFwOuqdxMw2C4iGoq6Z5NRp-u4uxo6HZ8WdFpU39t3ocTFgWN-Ro4V30w0TPuFgcyL7iHW3SqW22AlI8LJGnSUmvrYbkOCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9968bc181d.mp4?token=VEX8AiT9-xTXdB9tDsBnQR8ktlo4hqy5yE8JBaKI1bim5BithH4ctFTP69ACIS6NCvdVuHbHYrM7AB7_Ssl2EbdusT8wV8S8jpcqq4Sm6eT-MleD9dBGAadix57XaKeIVCXWAMyyDKVjK_mZAsB6eOLRJcoQKqpEQkd2nk09Ve23atWjdj0iTwycJHHxAVWkzDkEekmJGhlKSL7aV0XzR2l0kJmvHETO07B8pfYOJUDBBRvfGM-XOaCpFwOuqdxMw2C4iGoq6Z5NRp-u4uxo6HZ8WdFpU39t3ocTFgWN-Ro4V30w0TPuFgcyL7iHW3SqW22AlI8LJGnSUmvrYbkOCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو عشق ابدی ورژن آمریکایی یه دختر ایرانی به نام پارمیدا شرکت کرده و اون ته مونده های آبرومون هم برده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82545" target="_blank">📅 13:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82544">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8056f1f9.mp4?token=hevPkGKshjhX90IBSSZ6c_x0j4aA9A_XE7SkL3sYDDxLEQQh67PlI2dH71I0ih9NoP7cSeOXt5XYt1fa_t9t1xubf6Qqqb1hdWMvB89DdhP7t8LPhlGNYmD3fHx3fm4fJgDP_SOsCt6Ebq6BtCfabjw0aUn4rvLD9hrmbed3CZc0XSzi2WRQOEOFi5IRF7L33yWXesGnkKA90SKm4689gvaxw_XKqe8uI3al39aLnBBleNSHc6dDIIbfjpobDWlM0sCE2_11BDIdn55re2jCLyCG29meCfYJYNpNOdaJnRk--PdbJffpsSQ5W5n-vBA9N7u0OUIP6hzTnZGu4eruIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8056f1f9.mp4?token=hevPkGKshjhX90IBSSZ6c_x0j4aA9A_XE7SkL3sYDDxLEQQh67PlI2dH71I0ih9NoP7cSeOXt5XYt1fa_t9t1xubf6Qqqb1hdWMvB89DdhP7t8LPhlGNYmD3fHx3fm4fJgDP_SOsCt6Ebq6BtCfabjw0aUn4rvLD9hrmbed3CZc0XSzi2WRQOEOFi5IRF7L33yWXesGnkKA90SKm4689gvaxw_XKqe8uI3al39aLnBBleNSHc6dDIIbfjpobDWlM0sCE2_11BDIdn55re2jCLyCG29meCfYJYNpNOdaJnRk--PdbJffpsSQ5W5n-vBA9N7u0OUIP6hzTnZGu4eruIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این روال عادی ایرانه، الان دو روز دیگه باز همه یادشون میره تا دلار ۲۵۰ تومن، اون موقع باز جعفرزاده میاد یه ادیت میزنه با آهنگا محسن چاووشی و شایع سلبریتی ها هم اونو اد استوری میکنن.
پ‌ن: البته خود این یارو تو ویدیو حرومزاده ایه که دومی نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82544" target="_blank">📅 12:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82543">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRQJTWMpnBJZcuVWfTD1fNLsWVnTifBexMQ75gxbE4LIWAcPfTXLfadZ1YXBaQ0RuT0WuqNmEBeNrGisBQ7uVTgLRj4KChgu7SUTUiT7GThWHOfUcjdcQYLirTxGgno3SKW0PIAtz0Zume91UtiEIJVhOOj50RWCeKjwtdaHlw4fEGeFngOI8uQKew5KvFjRrBzBwo7AqIRLEIStHb-jYKmnR4447dRReTwfF1HebdgJs8fn-mD9uf4YXsgmUbBtKm69mzF-tFZ6IH1csO-GCQT2dNqJ4jndYG4JJDZ9G6IHg5_zNKnJMYMafHwLM2sURCyTNiw41L69mNnQMo47cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی ویژه هفته نخست لالیگا اسپانیا
💯
⚽️
در روزهای سه‌شنبه سوم تا پنج‌شنبه پنجم شهریور ماه، با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های هفته نخست لالیگا اسپانیا، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/LA-100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r3
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82543" target="_blank">📅 12:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82542">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzKh-DiA0iroGyAac--Z813DrYSmWKE9uhzBnpxub_WupVa3p0d5MsdTuZIssCEaoUxuhIBrwJ0BLh6BssxeWlM4m5rPXlOA57wVe4wVvSfWbZw-aaHh86ENQRftxpI6XqqbWrWWESLnfTTh0JDV-URtdnolWDo5V4DBLXn2B99BHIq65lH_YMTPqY5Q0D_UQR2i8CQMpDEDJf-mODZZn1mXqx7wwfFAuCan_WtzPO-1LDsCLo-bHkVJNI--CSXPa17N3bsu-pg3FU0YIqHVYFO-_fT0HXRKEvSuJWGqqWscLRxAVA3clzjvi4Ah_tfTnmj-dgdSk7o94EEDOt2d1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری نیویورکر:
دولت ایران به گنگسترهای روسی و مهاجران آفریقایی در کشورهای اروپایی برای ترور، ایجاد ترس و آسیب رساندن به ایرانیان مخالف مقیم خارج پول زیادی می‌دهد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82542" target="_blank">📅 10:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82541">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC9U9DiLuemFDfCsxJcF-liiJPXM4LRnLTkPgJvk8buMQki0pszRH-MC7_KpxfDBedqMRz7JQNIgPPAyfuX11zSDILbt08nAGGHHq-hSHAr0RlWOYju9TJ2pG-1jrnfboMYGqYI8ulk4InqondRzuU93ZBczqcnQG8HYzvgOmqmTiIv31u30gfUyOScdHqDWE2sdXVgpV9Gzu_hgkpNLttnhaBl_qrc4mxPVPmvAORwQtOMI0CRmgmhy7wUH2lxUicpy5ir4xv-vq6mWm7KrIFZbS_SigYrr57viBWuF8z9c_qtkYXS9creCjXxHf-xzBBJumvdkmocAGDOtjah3Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82541" target="_blank">📅 00:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82540">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">همین فرمون پیش بریم مردم تا عید رفتنی ان</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82540" target="_blank">📅 00:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82539">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLKuZbUtGDZSMn0xYBhtT8JH-jTtVC2ZEDLucMTpu2IONmzJFFc0sVWbcHKd26c_gTtitxRytaKDqmedNhLP12RK8-PZ_DFWSFj1vTY_8ivvdk4aJ7OtBf0s5NUw1oef7GeYlJDzVNVdjnbhGnjzPwVJxcMXj1pLdnQE0SXF1px3qWDo7bFEjq-2qVpDGPj-hgmD25OXYqGSlP3oCt6SErYGfJgAKpuGfdpoMWDGdg8-6JOrHL4_DM1TXOSAyaBB7DwZmvBcnigwXKhmcjMh49ORvsjjHqNhMTE99zbk8wYiZmBPCOsz1LpLCUu8xPAZ7BQIiqRnyzsaCxTKDM9DGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکای جنایتکار شیطان صفت هم تا ده میلیون دلار جایزه برای ارائه‌ی اطلاعات از سرداران عزیز سپاه پاسداران انقلاب اسلامی گذاشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82539" target="_blank">📅 23:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82537">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">عاصم منیر حتی نذاشت حضور پر مهرش تو ایران یه نصف روز بشه و چند دقیقه پیش از این مرز و بوم خروج
(فرار)
کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82537" target="_blank">📅 23:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82535">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfAIFmcd1EKvRlcsMc0m0IvwOfzBpryP0KmWm_F6O9J0exeJbMk1NjD4Kr75PrArw_nj1kIJObyoI8SJuzvSHYlNvhZwMn3yUSGpxLdecbLzTn7luJFdonwE32yuRXk32PMsOTngVi2ZThmCA9JFC83YigOE6j3tyxgT69ujkJgs6JfUVOpqzQdnmByanMhbBS3wu2g5UYPWeLLRHdxTowdkVC7fsbk3byadL7IWGxcnT9kYkWdJf_ucfqV-qfJQZBWNpozmGu5D4puuo9ZpblOdDpQLshVug8YztEvnYfuwD_cpXT1hS8BY17wCY2ODADPyu-S_nATB2ymkhlLDBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nS8KUxmhXH3HIT_8ZRpEQaX4Fgi-RCkzgtFH9dgkyq_q_iNFD9sdwpwKqcgvSULtgORL-8Ovpf0VO-IeEZeK938sueAVotWZPZVfhRjunQiN7nOd0uvUi5ROq3H_jZuSCfstXH8fEuoz51gqml0lU5JalzQGTBBOUIv46tY8Atcqy17Sl9ZGx_UmaQRGPxWYXy_xcqnqBdONss46AdTykEYpiqzeGkA52JriprvP08paDrKVi7G8z6PrmkJnUohADe1DxWSUh6pbqW4LEZ6saMVDrmveoCuudd09Runu20qGIUrGHnMhwulYkfXmL_gNPC-Rx0gd9NFB031-WVi_Tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به این بنده خدا واجبی دادن گفتن رنگه مو هست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82535" target="_blank">📅 23:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82534">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41ff961f21.mp4?token=JrlfA4y0Ln7hk-51rZohEiPqhB20xMbFQQ1rF63UfuSSJmNN1unJKrp8P8RRoxptGNBuS53MubSi-AdKnUYs3IV-zzSgN1rTdOoNCYbvOpU3INaEp7XVpArtjOBFfuSDysd5gDY3xHaFQ_ewWv2eZd3HmYNIjvsmauLfk5Pi1DM0IOzbbxpVvU6LzERimm_-PWPkijYIn-zjsAov8E58dAL4BKpjCBJyZs8UDnc-NoazesQ3Tv6TNFlWONmLCCCBt-8qaUsH4YYdV-RwtXIxt60JzUQh97tKyQ7aBKlBBkonWYTpBWG5vKpgJsNg3uGn4EZOEcWdGunPQhXHsSlR6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41ff961f21.mp4?token=JrlfA4y0Ln7hk-51rZohEiPqhB20xMbFQQ1rF63UfuSSJmNN1unJKrp8P8RRoxptGNBuS53MubSi-AdKnUYs3IV-zzSgN1rTdOoNCYbvOpU3INaEp7XVpArtjOBFfuSDysd5gDY3xHaFQ_ewWv2eZd3HmYNIjvsmauLfk5Pi1DM0IOzbbxpVvU6LzERimm_-PWPkijYIn-zjsAov8E58dAL4BKpjCBJyZs8UDnc-NoazesQ3Tv6TNFlWONmLCCCBt-8qaUsH4YYdV-RwtXIxt60JzUQh97tKyQ7aBKlBBkonWYTpBWG5vKpgJsNg3uGn4EZOEcWdGunPQhXHsSlR6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این محتوا مربوط به رپفارسی هست
‼️
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82534" target="_blank">📅 23:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82533">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2adb2d63f7.mp4?token=P9sfUyTd-nRR_1erGkOwJL15QoAn2pa7sSEtMGItPtUKJmOkPlrhZ2gAR9_7TWwerl1tnso7CM6AEfsiA4cQiizU051L9ByYJ83SsxDnISQVMEY_aMxeEZ9rp7Zw0-8F-37ACFLt36Zfqrk8WxcN-0QeGr1jHOliOtO5zLFy-MNP6zOxpAJtsYlIYIn_mNuP0YeueuIr5-DEM5n7Vgb2ohsqKtXSpyZMCSPhsDLpoE2dZHDR2791D-o6x3CaX2rQqY815gz6wpsOYTH_l7byRhznCgwBMxhLgFs7FtW3htzvq0yY-NOWKGYnI_K3i5aCpRzCeofD_NZeaPPtpv-rYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2adb2d63f7.mp4?token=P9sfUyTd-nRR_1erGkOwJL15QoAn2pa7sSEtMGItPtUKJmOkPlrhZ2gAR9_7TWwerl1tnso7CM6AEfsiA4cQiizU051L9ByYJ83SsxDnISQVMEY_aMxeEZ9rp7Zw0-8F-37ACFLt36Zfqrk8WxcN-0QeGr1jHOliOtO5zLFy-MNP6zOxpAJtsYlIYIn_mNuP0YeueuIr5-DEM5n7Vgb2ohsqKtXSpyZMCSPhsDLpoE2dZHDR2791D-o6x3CaX2rQqY815gz6wpsOYTH_l7byRhznCgwBMxhLgFs7FtW3htzvq0yY-NOWKGYnI_K3i5aCpRzCeofD_NZeaPPtpv-rYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط باید پسوند اپیکور رو اسمت باشه با ۱۵۰۰ دلار فلکس کنی، خیلی پلشتی ایمان جان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82533" target="_blank">📅 22:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82532">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkavBDxt5S8KJJm0W4_8XlR8-389zRZPZwGThN7diOtNE756yIYJCnpXNx9fBF79q3K3JbwBPYuYfuh3PIeZZgOQ1TOMKxdpfM_Wyc_URBwuvgAxgM_cAt0-153Uqvg5eQTYC_DSi9QRgYSS0vAH9FFR1uVjCjL8gq4QzIvMkp1XbySpnQjVItMpZIfNYHtxHLn5M5R_JdZFrSEL39dx9Oerp8V2bX-O6oFwbFTKmY_kfq5S66rKT79whoiarb_qI0eAZBYCAs1dbm5rxacJ8HgyeuaVr-vCztNDnnxf3CE-xGKaRjuE-7bwjK5dfc3N53OelYYukriC0ByNqHgTvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکش چطوری از دهه ۶۰ فیلم گیر اوردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82532" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82531">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrHMJGNx32AYyTpKJZwpXyDum-9sVgk_fgMO6q9f1BdhxHpPPBuUelKF5XbaDqgy1vQ5UyjYfd_ve6iBhd_VZOZGthYeKwWfArOvQIV_IyP-eMQW4mmIL6gioktc4V6uCxGP02Ukat6cyPLl4TdDwLKP4J2G07dvRRsd7Jy5c0FZ6MgB21O1iyFvhqHl5Vpe9epEWPldADynTEaKxRCaQfRtarzZi4ZjohnCmvtTgCVxmaNmgwCxsrZz_u47FGjikX01yJ3008VS5p9lZbFfZ_ku27ZBsXTo7ZudSrwemYr8_NE_g3Bacae97qJLOIekuvUY0gcDLxxerI0U1l9uug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ با سران کشورهای جهان تماس تلفنی برقرار می‌کند و از آن‌ها درخواست می‌کند تا از هرگونه تعامل با رژیم ایران خودداری کنند.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82531" target="_blank">📅 21:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82530">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Titj8dEym-WJxVGsGSDKVyK-u6RgdwfnCcv-Y3tikEFBqBKqywKdqwQvo2lETq_VnwfV4sZJJSNQtQI8v3YvY-nusZk4Q6oOw8VnpFwG48Qwzz0otgsP2wqQQCYistpH2RpzDKaoycxHaQ_PJVo4D_huBAyZOxuwZUgA65rSZ_z_GM5VfLD2ugg9VL_a__oEM48yaHhLgKz46kW3oBgvz0QQ-j4kYIQxgZce3AotX0kpMSx2YAra_uQCIcUaW779gFCP7ZcFUCZlqh5adyIlkh3kkKH7CkGZHaDmen-wndrS50H79tHSqdjDkTF56Qwf0BlgjFrg3zJRiHW_vdHvpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا به دلار ۲۰۰ هزار تومنی هم واکنش نشون داد و پیشبینی کرد اگه وضع به همین منوال ادامه پیدا کنه، دلار ممکنه به زودی ۳۰۰ هزار تومان رو هم رد کنه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82530" target="_blank">📅 21:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82529">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تحریم‌های جدید و شدیدی که ترامپ می‌گفت توسط وزیر خزانه‌داری آمریکا به صورت رسمی اعلام و شروع شدن: امروز، وزارت خزانه‌داری ایالات متحده، عملیات "انزوای اقتصادی" را آغاز کرده است، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران. ما یک عملیات اقتصادی گسترده را علیه…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82529" target="_blank">📅 20:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82528">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3789f0e9a7.mp4?token=va8pin5QlVgViogxdnwm42ZaT9gvGW__ZOT5SK2kpPIRgH2k3UwM0-5Wt8o4-FjtbhaRCerauB44Za8KDpUzpP-GFKTNiY7tarCYORXWLMleGoL8RACvYZ3E5-_XoouiDULiFPfrTmj9ez0Dj56wyDtyzqXs4LnQ8vAllme5p7hmKvHPUB0IajluvFbBdDcXv2eyWlakUEAXT4IWGMqPjZcitNoTP64-5Mw-SUKv8uOTqq2rHdzROkEpjHC1VAXEkHxGAPmfYCLCl7Sqd1lb6oWPXkEK9mKX46kb4YmWHFuvHHgY64aYeMYQSewLiSXn6v-lLGd_WIQ9ucHnksnnozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3789f0e9a7.mp4?token=va8pin5QlVgViogxdnwm42ZaT9gvGW__ZOT5SK2kpPIRgH2k3UwM0-5Wt8o4-FjtbhaRCerauB44Za8KDpUzpP-GFKTNiY7tarCYORXWLMleGoL8RACvYZ3E5-_XoouiDULiFPfrTmj9ez0Dj56wyDtyzqXs4LnQ8vAllme5p7hmKvHPUB0IajluvFbBdDcXv2eyWlakUEAXT4IWGMqPjZcitNoTP64-5Mw-SUKv8uOTqq2rHdzROkEpjHC1VAXEkHxGAPmfYCLCl7Sqd1lb6oWPXkEK9mKX46kb4YmWHFuvHHgY64aYeMYQSewLiSXn6v-lLGd_WIQ9ucHnksnnozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحریم‌های جدید و شدیدی که ترامپ می‌گفت توسط وزیر خزانه‌داری آمریکا به صورت رسمی اعلام و شروع شدن:
امروز، وزارت خزانه‌داری ایالات متحده، عملیات "انزوای اقتصادی" را آغاز کرده است، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران.
ما یک عملیات اقتصادی گسترده را علیه ارتباطات مالی ایران در سراسر جهان آغاز می‌کنیم.
هدف ما این است که هرگونه ارتباط اقتصادی را که این رژیم مستبد را حفظ می‌کند، قطع کنیم، تا در نهایت تهران تنها بماند.
از امروز، ما فشار را بیشتر می‌کنیم و هر منبع بالقوه درآمدی را که به تامین مالی سپاه پاسداران انقلاب اسلامی و رژیم ایران کمک می‌کند، مسدود خواهیم کرد.
هر سازمانی که به هر نحوی، فعالیت‌های پولشویی را از طرف ایران تسهیل کند، از سیستم دلاری آمریکا حذف خواهد شد.
دونالد ترامپ با سران کشورهای جهان تماس تلفنی برقرار می‌کند و از آن‌ها درخواست می‌کند تا از هرگونه تعامل با رژیم ایران خودداری کنند.
ایران تنها دو مسیر پیش رو دارد: انزوا کامل در سطح جهانی یا ایجاد تغییر و بازگشت کامل به اقتصاد جهانی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82528" target="_blank">📅 20:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82527">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">قیمت روز گوشی   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/82527" target="_blank">📅 20:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82526">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJZq6eUvkitlQLz183nQzsdSgXR9TDNRUtHbFCdfUuM7uXolX1KUk0PRPVEG0Izf7ce_aRv7r_pg9iyFIBamgo6vlcy2TMi5qzNJbCk4qvXyIaLbbPb2FwuYaFVibhy87Z0J-mFPnRNxejLCSDGs8gmKnwBk8yYIWlGXdYDms0EmoeJj1Zmqvd47JkORBWqIxb9yL0iZ7kCWRoe8bhL6NoCdW79vZUf2YR1GcZlNSI3aYtv4Ed4T_0ILEsreo7iZu1JCJLeLxXmZ4nX3MUoyQhHh9Ail9UECBYBFUWLvbgzANH-6ViAxiK1elZlbCygOM_nVXiSar4PQ2Ht6xyjoDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت روز گوشی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82526" target="_blank">📅 20:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82525">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">از تهدید کردن فک و فامیل ترامپ با زبون فارسی تو صداو‌سیما منظور خاصی دارید عزیزان؟ زبونم لال دیگه اینجوریم نیستید که مثلا انتظار داشته باشید پسر ترامپ میان برنامه‌های ضلال احکام شبکه قرآن رو با دقت نگاه کنه و بترسه مگه نه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82525" target="_blank">📅 20:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82524">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b569772aa.mp4?token=jA3D-8xHNg2iZpDuYmM_VHZeaW8V241Ft1d4IAlFbsx_upys6utZuR8ncgCc0U21Mi-GayafoUPUuND9ZtSQsugB66kSHi2RRoOhndib-ebIovjtAEDnkAZADjO3GKNYE5I3kS6mBoou_6RsGOyU6LitK8EAARLzg78iBYq6-NWcTpaZ1t9lYK8jnSJAqj3dekhojKABL1TRKk3olcpImgnZZ1snOd3beAMwht_ooMCkxLHFeeY7YJzekXh_UM0-5xZApc71ZhvDkgBhDdB08pD1t8o5nuj7yKJ4oqsVcihrPdpfd3ElCJJqTaagxFEplYNwhRBhIOC63HzIEEmvqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b569772aa.mp4?token=jA3D-8xHNg2iZpDuYmM_VHZeaW8V241Ft1d4IAlFbsx_upys6utZuR8ncgCc0U21Mi-GayafoUPUuND9ZtSQsugB66kSHi2RRoOhndib-ebIovjtAEDnkAZADjO3GKNYE5I3kS6mBoou_6RsGOyU6LitK8EAARLzg78iBYq6-NWcTpaZ1t9lYK8jnSJAqj3dekhojKABL1TRKk3olcpImgnZZ1snOd3beAMwht_ooMCkxLHFeeY7YJzekXh_UM0-5xZApc71ZhvDkgBhDdB08pD1t8o5nuj7yKJ4oqsVcihrPdpfd3ElCJJqTaagxFEplYNwhRBhIOC63HzIEEmvqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از تهدید کردن فک و فامیل ترامپ با زبون فارسی تو صداو‌سیما منظور خاصی دارید عزیزان؟
زبونم لال دیگه اینجوریم نیستید که مثلا انتظار داشته باشید پسر ترامپ میان برنامه‌های ضلال احکام شبکه قرآن رو با دقت نگاه کنه و بترسه مگه نه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82524" target="_blank">📅 19:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82523">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9PTVcrh7F9b6XpbVwNtewpC7yB8Tyy89RyndAM92uRg12zAZXCsgZ_k_kAi4ic9SPqx_78T2M8eZXkSTd2RphV0KPuJwaUmlT333v9nQEhcpUpKcOmTo2O4ah6JNclQpE01s_1b02RY6uJgm1CTvMd63qbHcw2_GbYT-PiPTuo43OXToRWxnupCEeH8MGMEyqZ4_NYcJcH3XD1VhBZ_aI0QD7LOCqDC7eL818q9795od91sMcUFurBzgaCySxxtAkVbB9qxHCSx-m2__bN0PmpN3xx3tAwhuqT-Se-2CYtVcpsjbI4y-b2yWOnxBj1OknaVlZ_uaCzE8rk0x7pGVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم قیمت دلار رو می‌بینن، نادر قاضی‌پور از سیاستمدارهای تراز کشور هم چهره‌های جدید اینستاگرام رو.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82523" target="_blank">📅 19:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82522">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/482bcfbcff.mp4?token=bGBZFq6zman7eyA2lcay6vGube_oTRITRiDeFCOHAu_tUY7Aw8UD34WMJbO5kmNgqeEKtE4D--I4enjZFAeWFdw-VYnd9Np9OeOs0ZB87byOkR5g0GMjxx6FkjpfeFEOdDw4aUAQTjFgjXLHbxQWmdTRH77qIcyIsMyrt4HXSq9fF8uTUmNuOU8x4wgLGZqlLeDIXgU-disn8Z-yi5TlPkxF9ftogmPrEbk604IwGOam9unlXHlZr5cKWkL2zPAKrlAVAKRACvRsblU8lNthB8N_aY06w_bjR6Pzam6Qb2Fsh1_GqBjj6drat5-t2F5FEzUIojYTD9HeOjLYvHc_GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/482bcfbcff.mp4?token=bGBZFq6zman7eyA2lcay6vGube_oTRITRiDeFCOHAu_tUY7Aw8UD34WMJbO5kmNgqeEKtE4D--I4enjZFAeWFdw-VYnd9Np9OeOs0ZB87byOkR5g0GMjxx6FkjpfeFEOdDw4aUAQTjFgjXLHbxQWmdTRH77qIcyIsMyrt4HXSq9fF8uTUmNuOU8x4wgLGZqlLeDIXgU-disn8Z-yi5TlPkxF9ftogmPrEbk604IwGOam9unlXHlZr5cKWkL2zPAKrlAVAKRACvRsblU8lNthB8N_aY06w_bjR6Pzam6Qb2Fsh1_GqBjj6drat5-t2F5FEzUIojYTD9HeOjLYvHc_GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم قیمت دلار رو می‌بینن، نادر قاضی‌پور از سیاستمدارهای تراز کشور هم چهره‌های جدید اینستاگرام رو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82522" target="_blank">📅 19:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82520">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRJ4pDJU5DwgmI8hrjZBVACPl82LN86rT6isTw7PMq8kBkZM11dLK6RiOYCW7XqFET_7K7OxNOfIDBP4QICxpXtVwl_aLGBQzgVkd86m91sDtch3S6n0UmH1j1v-A9oIfzl68R_ygu5M5O7tDUBuXcdnRi406OPdQr3F59cCwQ8F7SFRvCXAHxCekIuWJCBRR4hWCsr9Jr2BgAIlsS7QRg1R4kocKx_imlOlTlGtOSYYvvTMBfQyqmlWEvnULWttMCNBwoUTybq-YislA9UEGBo1IsY0jtU2WPi6oNjO5QM3UIKFzF2mHpGsLOx70ooOeFM4VYJxvbJLuUrlQP_HNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ تا از پولدار ترین اشخاص دنیا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82520" target="_blank">📅 17:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82519">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAK3dL3io4ezNk6V0uqw56fe1MouCJo8HvIoeos0GR4fEkKX0sGP-KL4VR5XgtF2qtjRAw22zhrZul7x81F3W-9mHete95n8jh11eOYt-X6Ntnz9LMu_AjtG1bSnCsbBMBsH24lePa2fRoo7N2twSsNSwSpiiqBGCE54KmwPUgzflLsL3lwqTZDbqifyQ_KXXPft6i0xZaPq7OmH_XEHGfXvRKpRET49xZUht4NywehUPUjaKVOqiMrt7wgD8i6CtABaO19YgFOYFhKycle_zveKbD1_oPWRPaRR-HrUpjNARNgbGyTgdfMQr9C042IgMxJyfUxo88p9lRoHWZ9sxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82519" target="_blank">📅 17:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82518">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">این پولای عوارض تنگه هرمز رو کی نقد میکنید تزریق کنید به بازار یهو دلار ۱۰۰ هزار تومن بکشه پایین</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82518" target="_blank">📅 15:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82517">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlUimYsSG520WVYqxAJGVcLqHoeDisgGmj7nzMh0UTIC4IRjz-jzSHVAdwefr1eDEvEgrb8xBMN97GMwrgRvGyLrQa16AWrTwVLhNu7vMM-oAuv1wDWL5mzgAaoQr-1pCkY46KX-2SC3wj5CKXB8PrqIFV6pOalBuuXZ3Rb3mvndK0hlUElwGVq3hkpINpfFHLr8QLKWipyWT0cZXxH98_Mc9ydtLCreBrYM-MQBBoOlZM_luXZpMEe30J3YDftNvgDNtKRbuoxQ107_r9ofbTn7P6kSqShhrbzN7H7BSlH5xABy8kuL23bwEqwUFnd3ZaD-EeqhyWB5-UPfphkH1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی حرکت کن.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82517" target="_blank">📅 14:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82516">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">برای همینه نمیتونم از خنده بکشمتون.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82516" target="_blank">📅 14:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82515">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YddV1Bsi45jg5oA97Pnt2nvP9m109mjAscTIYBJPVg59Hw74agWfx54fPrS-ANA2yYD8uDmDfa2Hwow5Mqrlsq9pWeb4Bs6j594i7SvoLgJDpnGtwLgTyNEQPVnVita4b7RY2laNe7Kj11XqKCMDp0uc_t5RWeYzCYM9u_rRxpkqA7OEfYNNgbifegzfvSZ4jjqSpSwppNsdJAlWrsR5SJSLf4ZOomiWnuQmVUg46JlMQ_wzKjXL0TRGDgaz2iIVDWaIMcRmHmVkINrWPdiazV_bXrGwfKOH3XIw4OHGtAfb3UT56YaO1XJsYfmLOGLYdJOCfJVZou2st2Of6n5xzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همینه نمیتونم از خنده بکشمتون.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82515" target="_blank">📅 14:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82514">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b--pSU03Y3SwNLfqsDfCuMiQ0V3MJKtoXx7I90OiL4Pv30g1BsSmEl_Div-tg6yOa60zI2CVGlLZBVCLsnk40bV91iOzWx_YP-K2GGkUkykM7UYINKMKLx3cCSi7-03exCc8heBJ0XKf05GgcwCx0zjDybxnrP_jZXTPJMVa08vTOst45_5jZcLgnxFSEGx88kxcwd9liYcUJ2BixWUUE5xbsd3Uhi2xZ_4u3qsNots9WkAwFTVrIhH93qZluXIdLmwCOq9xg2eU7jPb5EUhyKktNc5XHJ9AvVxqa-T2P2g180lzDveDBfblwaAVFoCpwr4uWBF9ZKvlW1gI9lQfmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندروتیت دوباره به جرم تجاوز به کودکان، پورنوگرافی، قتل، قاچاق اعضای بدن در میامی دستگیر و راهی زندان شد تا بهش بگن کصمادرش چه رنگیه.  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82514" target="_blank">📅 12:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82513">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sl8jTX5wd9GSXIPtpTvjO51aFxoDGO82iX49yQhfax2abKA8bI8UCPo13L7u2vje110NCv3XhzpabGDVV0ik9F0HxBvkFIchaxwi0UO42SA5jbtfhfcXumkxu2sQ4DKRhIuW_AzHLXDtBBhdnWBRyvfemmTds7jbP9UHs4DGLB-1aGHopf5lJMg5jLHQ2jrnxRq04DOk9famrp_13zEFV4ZzjLwnK0Erv_Lm0rG4PXbhUWheIN0wCEQ5L9_pSNMJR0IpT2FIZP2DHjmZyqUhTm43Gl03yA00U91zxc7_h_4wqvLH6Y6lcRJ6sHcooSJfvwvsvFvvKnvFRjPy1JFBgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکسال پیش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82513" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82511">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OT8lF3CQ6eENHfY6DPEeHbGy95ft2F98CjNmbOxgUwv2DvuJ92QiZHB7ORMwzF5uTShrAh5Nr8GtzKXPrDktvWe5zvacIG7tZPJuj5oa2bMQrl3X456OqO5T77halIDO6WZ1ZLwf1QtU56CFhNtj4AIpwxK7lP9aOXnYldRaJM7VMjlyimt0VFFTfvYpcGIeHoPOHk85C0E7PqpeMyNGHKxu9cxFzsvsb7P4ETzpb48-kozUMB319-VRosgxDJWCt0dxrB3Grw9CWpHyx7CQclU8qjCp2F-pD5u2NPipq5--JgRy-My5O8p7OC2nPBj7CPRw-_cRV8FyYMqTgAM2-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطمعنم تو این ۲۵۰۰ ساله کلفت بودیم یا ما شانسمون تخمیه به این روزا افتادیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82511" target="_blank">📅 11:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82510">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCEBvMX66cC4aO6anUZKNkXjWHbCYZU6lrOLGDYG6Befycnl4mp_73Pcr8xqy9HlSj3MMrvCzQxWfs_gZQ4MuqBV3MwXnNLOSbKrdpP6vzDKC5A_sDo7asCwmMYWKimJcSIteIIm3JhqSq4y00SkoUiHmlx1s35WOyTN5uU89tuZqgYaG-V2jqLSWSnm1HP_2gnJ4oICRUajx0CPyYiB95W0hdLZJ_wjasMJFdDg6Th6xMx4Yo040siG_j9lofp7gc0H5RllnKxY5MGBb0Eky_Lec5Y0MnDk_dFwgQ7HEkgrJy7o7KdeS-0hnfZzxZuoDYGYPfGoVi1SqefKpbuKbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی حرکت کن.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82510" target="_blank">📅 09:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82509">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQeqKokFd4oVa7ugcJiq5JkbTlFohk_c-Dbl_OxiOFSMG7NffE64SIlUsIRChWgkZN2LMOjTf6ZhBgv5zZQOYJYrJ1rWthh7XmYjmWV-jcqFsxDSNjJR8cvtRbXRZTJtiVer8UOOjXKpvJ6toTmeNYP96gsnXgdUSWU4yEE0pV2WI55McE62VmFyMiODu6VTUNJD_crKAhV9DPl1A423UgvuIS2XNbmcB7DWbYFR-JdUtRCHk6hDzRCxiN5JO-1DGh7UwSlDbOGQqj0euFQSxmn2F86YzOQWuVYdDSgWRZO9OgN4LfWIAwsyhV2Ikv6uzEVpRwPhlqARzb0DZx9JtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قراره کلی فیلم سوپر دربیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82509" target="_blank">📅 08:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82508">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
آخجون میخوان پول پرت کنن تو صورتمون
وزیر خزانه‌داری آمریکا : از بامداد امروز، حمله مالی به ایران را آغاز خواهیم کرد؛ بزرگ‌ترین حمله از این نوع در تاریخ.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82508" target="_blank">📅 04:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82506">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYHEEUVt3BIZmY7OOdB2ecyATGN3qft9Jq1Wf646OYpSj7YPMZu9JmQEyHsRX_WujqTH3f1A9wTgg6I0w6viVkcaEyjmhROXoA6XFtkFszXI9U0q_QBAN-jRV81jUONv8-f2ogr_LnDTP9cZoDm0YD744sO7rQ-KyX3HcuMDJN-Mh_r4xnEXP7IUNfcI3Vbp45NLTWwZr6hFF2hhacQif402KRCbdEkM1XtjLH-aY1WtMPz1PVzTirPn-ZxxvG4i3mgu51RpooP8yM9YluHWZQU61486PXwvrokdH6uxbY7hL3V5JIw0zJtoEckleHLiD4ixPnkEGJBmbpxRxa7hEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری هیچکس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/82506" target="_blank">📅 01:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82505">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtd6QsFcVURq09CYorWthWTbNDHZvx9Kpe60smFB6nvC0CEucLPyoRtUfBVoWwf8XexpHAb-7B2APzgTBOmsFeCt1mt4YgjGkUclvR7SjDZAYjdR858o3l2-gudAC6W7URrX28DsqRP8hwZ0ahARTHVORMwv2-YpRgIDP_MjHuxnEsCfzsJ_znOhn40FLFUEeRQBTZGNMWCJdC9thGE0vbBMcSp-NyIBWzBP3iFg97Q9mcf8psxyXhcfQyuNkyfliya1lI2xWIPKEUVaW7E_eKme2zFB2FHQYYipnhO_AA8pni6B3zuv40gTOhnL_z7owFTkinjc8K5i4VM3eAo6Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بریم واس سی ال
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82505" target="_blank">📅 00:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82504">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBcRRldoCXa7Wr_09ZQC1hTI6LngSpccoSjQnpicLHgybV8cESVvbh2zTgjeYpTkcPRUA1ThwA6uEz0i64piiyqKfSVjjzJC-GtsshMPyc_u-yHAFtSRZrYrfEKRuxjQhdtlC4w7xMTT0BzXl0NV07-NhG4CiTWtRHpoci34bd9UY11m1HIuh1Atu389QHA7Mj-ryjj7XN1TTEi_MylNxCdmVRDEftKj_E2kR52MR71xy9EULLc0Ud_SXiS5O_plQE8lQvESqeKIonz1gf5yKlV2O53B6s2lRI8zz4FYPpNW8SkSe8DHy5zRusmoILt8hoZjF_ZcdCXWMGTfMuHd-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیر حوزه علمیه شیراز گفته زنان شوهر دار هم میتونن عقد موقت کنن و نیازی به اجازه شوهرشون ندارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/82504" target="_blank">📅 22:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82500">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6HMtsPr2U-8PISqpMLaNSvOi1tFmvzNr7eo7xH9wtLKx1iA_ZAOcqAk1RRDcFk9GOQ2fQgi1NVUmD2HQj5KoMNqdqf7R0oR4o5cewnO8njp_IpsEYFbyKt_63Voqhx7WXyZkGPrrKA8PRQBjmczy0gcSNzmLlZsiOcz9kIw_G6SKE4P4SKWUb_bt8bhgeyKZw1H7gdlk3C6Lx0Mc6KHd5AmomHit1JcrqxkegAYRFxVVH9SjEeaWzQZrCK18V0djYhqacpkqxLfzY6D6a3Vn6V5fUSPPsMS8t_CiKWQVR_RXLon_n4xNnQTD-7G4jtZm7qXLSldmRDMf2s19zyQ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الوارز بخاطر خستگی بازی واس اتلتیکو رو نیمکته امشب
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82500" target="_blank">📅 22:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82499">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">زن ستیزی تا کی چرا مجوز ندادید دختر بیرانوند کنسرت بزاره؟
شیما کاتوزیان لطفا ۱۰۰ تا استوری بزار رسیدگی بشه</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82499" target="_blank">📅 22:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82498">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6ODL0IVZ0vIeOow3iGVKjm8PU4BAF9TEHiwr6C4DLNVL65BGvEAzAa9UKfu-Eb7hKrW7N2za7Ks9BlG2E0jBdW_FcLptiQlV4eHqN7mg503E88yIA_yUBaSpr9PuVob1N2IFIle7IAQQIzjaGVViUnx6uqfESXz8JQB6jFAuLimmpgxKvSDzBtIJBf51nxWvhwMqgx3wmuXpFj41nNTEfa6kMISPlU7c6ZnA1XpcUpYroSQJEXX86ncfY3YkTVwf-2RMqT8RmDASqrS7C7QNUz1jqY153BQO415axpQTX3_TJXnaWhWq7z89cS3F7yhtlXJzq4QUS0jinulDejg2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجوز یعنی مخدر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82498" target="_blank">📅 21:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82497">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpGUM6Y2JyDosMjZ9ziV8nqtac58J9-Vzqm28CHlLEn-N8frsABi_c_z_9wIzczkrSyKbXhn2cJYdcQ56kyE3F5hNiaMx85hNJbSV06s0bM25BfcZ3BSLys9kgFiMB44V0AbN7AxZTAuymmHF60YgJTx1jiGi-ekKzAGTJgXJkMaHM3bOfUdRuPhoHNGmKOqYQyqzUdxPp8XDp-Z_DEEaEjhmbHYMJor__Q_9b_8akgmA24th4l6PeA6xvSSBbgASzh0xcxcRAJEIpRJ_zbOY6Y-6z54RjiXGJS9x7jb15v7F0hxnaD9MvuHZ5AuSgBs7gERKLkwwnofxpaJmA6cmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیر پسر یه چندتا گل به خودی بزن تا بزارن بری
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82497" target="_blank">📅 20:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82496">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">عجب تجاوزی داره میکنه استقلال کبیر به سپاهان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82496" target="_blank">📅 19:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82495">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NF_G5DuQlZGWLpUMFGgj-4I1dHb_7KUID6Gqx-AkpNLllRK8tW0KttjU1gceAqjtt65s6l8MRUKMpdZn_xXBkvevxc6nMQWbbpWW_jStwu9oPuL0zBm67-BdTrPAkeC1uAQhsBvBhty6_6cHjUOFghq_OnS_UUyjifl6zwxIHq3nRZDpFjYNei6XdbAgb_5oQ82_2XBNkK8dg4QXDUg8ZjlPoig611wnQOU78yZ7OsbABN8J0tcjb0ZF1G-U3wLP0F9CgDICwXk47kdCD5ZhgnzQa-Q-baKpunSwL0F3wAsPm7sV19OOrXc6lxdpL5WUqR_4fwrmT5S3G8jW1hcMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیپ‌هاپولوژیست چی می‌کشید بنده خدا.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82495" target="_blank">📅 19:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82494">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a34a3c950.mp4?token=ByiRhdKb7rZUp6JluOWxu90cCr0yuXOrgkG11dKiPzL39RE3QevyUYNMUBuTFG4yrEuvCnlALcIf3SZPwZ-pmJTIQ7w0eP_sVFrJSXHK03JOV7iGzcRVBAICyZW_gSHJfqJRf-75IOv2SfgRExOdMBvwrjA4B9-qz9IaxXZpz-u6zKyz3Imk-m-BFumjVQXqOqOg9MpCQcujdbFv97cAy-siWM6HF_7-IsleJqHA_dU-sluQQX0ts6lHUuQqxI5aVJoMibP_xjKkB6UyOTkMKEknBQ3j9SlQDwoXY3fbYSdB_wfYixR5fkNP4lKBUuHafjppnnrjx-0HxSoDh8QK4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a34a3c950.mp4?token=ByiRhdKb7rZUp6JluOWxu90cCr0yuXOrgkG11dKiPzL39RE3QevyUYNMUBuTFG4yrEuvCnlALcIf3SZPwZ-pmJTIQ7w0eP_sVFrJSXHK03JOV7iGzcRVBAICyZW_gSHJfqJRf-75IOv2SfgRExOdMBvwrjA4B9-qz9IaxXZpz-u6zKyz3Imk-m-BFumjVQXqOqOg9MpCQcujdbFv97cAy-siWM6HF_7-IsleJqHA_dU-sluQQX0ts6lHUuQqxI5aVJoMibP_xjKkB6UyOTkMKEknBQ3j9SlQDwoXY3fbYSdB_wfYixR5fkNP4lKBUuHafjppnnrjx-0HxSoDh8QK4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آفرین ایرانی باز افتخار آفریدی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82494" target="_blank">📅 19:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82492">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79c451060b.mp4?token=X6QB45n2YM6QCYA5uBV5QW9rubibUOzjIb1sg6S5ktvn1UHpxndXgdGKcrBgNW9eaiv_Jr_3TcWmHg_g6DSh_eJUplb3XrRmX78bPCfZVvRCmTi8yG4Hyg5PPYvzxC0gymC6qtUt1jp9mgQ4h4FB3tzAGihOkc0uUwMpfARulikHt6NAmG-CK9Kf-Rn3qi0J5qGjX7PeeTaBJkIBscbHt6auF2ojE9MqchSVCRGwhEbHoRoj8DD_BbSvocOXeaiV9Y5WO1-AzCA9dZoFlK6Skpi7iE_eqJ5rF553tmW2MbiHB7VU-Bn4ILsUQGnL2ACJxoowiRKOBCePWEe4WJsGCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79c451060b.mp4?token=X6QB45n2YM6QCYA5uBV5QW9rubibUOzjIb1sg6S5ktvn1UHpxndXgdGKcrBgNW9eaiv_Jr_3TcWmHg_g6DSh_eJUplb3XrRmX78bPCfZVvRCmTi8yG4Hyg5PPYvzxC0gymC6qtUt1jp9mgQ4h4FB3tzAGihOkc0uUwMpfARulikHt6NAmG-CK9Kf-Rn3qi0J5qGjX7PeeTaBJkIBscbHt6auF2ojE9MqchSVCRGwhEbHoRoj8DD_BbSvocOXeaiV9Y5WO1-AzCA9dZoFlK6Skpi7iE_eqJ5rF553tmW2MbiHB7VU-Bn4ILsUQGnL2ACJxoowiRKOBCePWEe4WJsGCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82492" target="_blank">📅 18:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82491">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خداروشکر جلیلی نیومد که دلار بشه ۲۰۰ تومن</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82491" target="_blank">📅 15:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82490">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دوستان به نظرتون اسکرین شات دلار ۲۰۰ هزار تومنی و ایموجی قلب سیاه شکسته رو با آهنگای محسن چاووشی ادیت بزنم استوری کنم بهتره یا آهنگای استاد محسن نامجو بهتر می‌تونه ناراحت و نگران بودنمو نشون بده؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82490" target="_blank">📅 14:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82489">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خب بگم دلتون برا همین 200 تومن هم تنگ میشه یا زوده؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82489" target="_blank">📅 14:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82488">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ویلسون ناموسا چرا به همه چیز هایی که تو مملکت اتفاق میوفته با ۶ ماه تاخیر واکنش نشون میدی</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82488" target="_blank">📅 14:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82487">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OP5zT1skTmYkkpspyodYN7hwRIR1Czz0pS62Wsi-OsK7aHq3VByX3hp6kQcJKMqcwmi6ITLSeM9VesVNMMaQTB2N8cPPuCQACqVAvMi_9ZJ81ZjwOfRnEYk564tcxOqreAdAcd0a637AaJ8WuC4QFw0BXtEu3biEvfPyys87A2CPU_X1Hp7zA0Z-eRe9_4H2tHgHCWSTPPjEN-MR4Z4Cf_qdAy41Bbn27CrOdCmNdAxqJohgltn9yajfH9ryVDESnM2zyqs3ywVvktnpzhpz9YPXfFWxIvHbHYgLuiycKh2WtdUOsTGfhqPIyjAQPvPUON-8iQCvFD1TDOpsxRrzCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار 200k شد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82487" target="_blank">📅 14:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82486">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دلار 200k شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82486" target="_blank">📅 14:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82484">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dw3TCeZE6QT0bDlLHrmN6QIwV0V85hYvQRUM4xnSJsYauRb7ReS2wXHnl1RcIUFYXpbTwwDawdrc51NT1Jz3oKAjIbC5EYilPvuqk2SVnpUyNkrKeUgT9dn5FzisglOgDE9Ow0nXIv6h8Qz-ndruDrW0WdmbMqHuNYr5t6XLAaOSE3InXclQuj-eg-4fc0awgVqEdAzInHw1B9buGhW-OjxthsuuVahhitzU3XuNa46KUeNw4Zc8llK47RqWgZNmL4gf3nQCPkEarYjANCRFV_SUEhXJKGbIr_qOPOMIawKP59Q6m4oSHUwCLNvb0BmSLYClXD8-bf3nyt4cW5b4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K9eh-7EzUxmc8qg_UVmD9mht4gm4XbiCuE6ESpN6mBqgOLJZVrwI3tQz5cUHdl8hNYRSJy9ZFq6Jj8OaZAPpshfo7iEREZIqCDFAa0M2JQ-Pply-mpJ8uFF3ibrPLNCWj1jreSAnW3CXbyPeUx2JmMK_gumHKSI2IRCBCTLhwhglBR1S15KxpdRQyFPsCSAA1NY56AxInYubGZmmmAROf4R4GJJ91JaQN7RWd3d6mnCl6fN5OV3fLebFkoFULS0fBndvvyMl1OeOX1BC7EpQrhldV-tIx9IEB8XQmtsvupElddG1ZhwwRhx9W8jLWlfyh4XKf56Pymy_U0SFha4mpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هالند کصخل موهاشو کوتاه کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82484" target="_blank">📅 13:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82483">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trTotJ277GKyPRZJWLz3Vz2z1fEbaNSnCd8xlKHLfBPt2fTdZBxg1PCypL5ScZo6pRTRDAdUz_c4kNhS315Zig6WyvoHfHOSuph4sFOQKNVv5a9GGLfY4CTOuw6W6749ZZsw32U7XSnuLHkSHnNQBihglCYwvet7q_VIt0DunykV7OqnV6Kn-ecZijBczyMn20K3SBzHSg9N5ZDEh3jcYR6MM9FAxperc4mdA9Ukx9n4IEVFQB2geJzjyhiJyt66x7C2f3uHebQGf_O_bm-qWcvlxqDIrTNSYuw5ZcWr9dvnnCi7NVI37EM9o6OaDeWfUo1oDn_F0jDD4eHo-AsFHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا ارومیه رو چطوری ربط بدیم به عربستان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82483" target="_blank">📅 12:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82482">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df1ed91c9.mp4?token=Dt-kbQYDsZ3KnF7TwJV0nwXN11H8qyP9cnFfCJrGC8sPE2laWGu6qg6InQlrNnTxd_zoNUwFwnpz5oAa1QxWRyFbSJdW8STGUyCCyxv6wkzXB_1wKe4bMpLFtPKsRLO6Ip3CdkLvJ6zaDD-ZpSNrgrkXQ5lClbypBE00NeEfh7HKVXgdk6NaMTcz-9PQWrI8VU9ugJvVybb05o6q3afWvymtOvpgRZbXGkCymJGmqqBeDivYAZLknDCgxOnHXc6p5n9LgJUkTV4IW8hPAaPd8M8pTZlSGFME6qf6k4DplbIM0CW1VJk-_Tauekn4919sLIfUtXbWmIFunpM9_6x8nFENsAq3Qs9-XtVRKoLOp9FVSVX_bVU3gQaZph-eApjWnUPtvweDMEApX-k2FF32kUtQ2fhTMQUpY8hqYI68E_5iPerVsLAbByXCj0eQtl5jAatOW36_dnfYBjJ56sBH_-ih5Fr-0EZX5Aw6QFDB8wp0eNJbIVxuSUIOkdmw3S5aoIf0QM5vGiXsF9cKrUD9lAxsA-txLVsB8sxqpCNkpIOIASySxigJwQWcQLT45hdGsdJM3mMPUgz4hpfuHbWVwqmX9zWT8ZXD4DN7rWWhGKH2nMTHPGFQmvLkM1ifm3x5GivUg0PGkpWHg_6_-O6_O4yJLXmTPsyc01myz-2fqvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df1ed91c9.mp4?token=Dt-kbQYDsZ3KnF7TwJV0nwXN11H8qyP9cnFfCJrGC8sPE2laWGu6qg6InQlrNnTxd_zoNUwFwnpz5oAa1QxWRyFbSJdW8STGUyCCyxv6wkzXB_1wKe4bMpLFtPKsRLO6Ip3CdkLvJ6zaDD-ZpSNrgrkXQ5lClbypBE00NeEfh7HKVXgdk6NaMTcz-9PQWrI8VU9ugJvVybb05o6q3afWvymtOvpgRZbXGkCymJGmqqBeDivYAZLknDCgxOnHXc6p5n9LgJUkTV4IW8hPAaPd8M8pTZlSGFME6qf6k4DplbIM0CW1VJk-_Tauekn4919sLIfUtXbWmIFunpM9_6x8nFENsAq3Qs9-XtVRKoLOp9FVSVX_bVU3gQaZph-eApjWnUPtvweDMEApX-k2FF32kUtQ2fhTMQUpY8hqYI68E_5iPerVsLAbByXCj0eQtl5jAatOW36_dnfYBjJ56sBH_-ih5Fr-0EZX5Aw6QFDB8wp0eNJbIVxuSUIOkdmw3S5aoIf0QM5vGiXsF9cKrUD9lAxsA-txLVsB8sxqpCNkpIOIASySxigJwQWcQLT45hdGsdJM3mMPUgz4hpfuHbWVwqmX9zWT8ZXD4DN7rWWhGKH2nMTHPGFQmvLkM1ifm3x5GivUg0PGkpWHg_6_-O6_O4yJLXmTPsyc01myz-2fqvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو تظاهرات با چادر تو ساحل دریای مازندران برای اعتراض به بی‌حجابی هایی که در سواحل رخ میده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82482" target="_blank">📅 11:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82481">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a208381aa.mp4?token=YKXh2n-XDRFHzOqS5D1UowxW2zrL3R2BoypK3Ilpehml9giThhgPXf10y_zRzQKI_SoA0gke3Yz9mZprfrxEi6gxIUuz610dlAq93bZiYdASOZLqZMhnRruTCFxDGElEb12_Fd7URVcF_jpF9k9xwSC41wrXw7bb1-lsnsflBIYap7lbbTFJclqSJHsqO-8TdpojFAq_u3fwS06CtDjo1I2Ky6yojGE7REGvCVOzanwaGGDDx4nzck7MmohfYvNfNTPfWgfTzh4FlURiVxYOslMsNRFO3j3edc_xSWjy-oJRugJ0N8j6CPj9K5QDGlmFQsHTgFx7tvEqYUIGhWG2LpMUcJmOmO3FSiCz634-JQl13gJJO2tE-2vzelQtPOlZtNWv4PMOaz-tOoXGqp07IwjdGVq1iSsJP-7zqmYif8vNDR65Y3bl2EGawefeWH9zEv53MKTlTVbofuQz60icmo57gddS1QUI4xCQJEqNJIJJDvfjzEpruX_VudqGcYvSfJ0BhZlpMR8tGDIvYL6-u_L2koODt0kFBXEjtZ8NPoYyoy_3Yt8nigKCVnuXGVtrz_9OfcSyc-l3gGnBD7k3p1_ofnMIhDvm1LzrldTZOS_20Pij_VIQwiSLpkbjefwNEfHofAaV7IqCSOSSBkM7LOOrEMSzK_PIKPM9YStLwuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a208381aa.mp4?token=YKXh2n-XDRFHzOqS5D1UowxW2zrL3R2BoypK3Ilpehml9giThhgPXf10y_zRzQKI_SoA0gke3Yz9mZprfrxEi6gxIUuz610dlAq93bZiYdASOZLqZMhnRruTCFxDGElEb12_Fd7URVcF_jpF9k9xwSC41wrXw7bb1-lsnsflBIYap7lbbTFJclqSJHsqO-8TdpojFAq_u3fwS06CtDjo1I2Ky6yojGE7REGvCVOzanwaGGDDx4nzck7MmohfYvNfNTPfWgfTzh4FlURiVxYOslMsNRFO3j3edc_xSWjy-oJRugJ0N8j6CPj9K5QDGlmFQsHTgFx7tvEqYUIGhWG2LpMUcJmOmO3FSiCz634-JQl13gJJO2tE-2vzelQtPOlZtNWv4PMOaz-tOoXGqp07IwjdGVq1iSsJP-7zqmYif8vNDR65Y3bl2EGawefeWH9zEv53MKTlTVbofuQz60icmo57gddS1QUI4xCQJEqNJIJJDvfjzEpruX_VudqGcYvSfJ0BhZlpMR8tGDIvYL6-u_L2koODt0kFBXEjtZ8NPoYyoy_3Yt8nigKCVnuXGVtrz_9OfcSyc-l3gGnBD7k3p1_ofnMIhDvm1LzrldTZOS_20Pij_VIQwiSLpkbjefwNEfHofAaV7IqCSOSSBkM7LOOrEMSzK_PIKPM9YStLwuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک خانواده تبریزی تو استانبول عروسی فوق لاکچری گرفتن
یه پولی‌هم جلوی اندی انداختن پاشده از لس آنجلس اومده استانبول براشون بخونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82481" target="_blank">📅 10:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82479">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">صبح بخیر
ترامپ: تنگه هرمز دیگه جزعی از کشور امریکاست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82479" target="_blank">📅 09:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82478">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsOaZExyH07KQT6KHjtvMqoObFTfMfZoJBwwzHrqugX7I5Z178IHIefYXsaLUlw3my3CaJLBd5BQrjed5CPm2SSZqmY1LjBtETtgz-MMVpyH0n3jV21C15iV1MVjckTGQ5PFEwMYqUTV-M34qJY1py0jCYTXojyC5NALTwvYCyjeaNca7rq3VNyQl8jaMmrGna5WwIfoceyQJCFIDMSSKKGamH7_CI6ej4TFzUgJAg-8ZNeRuv8rFORSnt68HHDUxmkjqvH4jxcUp1_UjnYTH1mG6qLUv9x36PdMkHQPNp5YjTqaX82hgtaPqERLUF91V_hshlACYI3ydUxdS042ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82478" target="_blank">📅 01:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82477">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کوروش چقد خشن شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82477" target="_blank">📅 01:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82476">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مورینیو یه خسرو حیدری و حنیف عمران زاده نیاز داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82476" target="_blank">📅 00:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82474">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝓔𝓻𝓯𝓪𝓷.</strong></div>
<div class="tg-text">میخواد یه ورژن ۲ بسازه باگای اولیو رفع کنه</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/82474" target="_blank">📅 00:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82473">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پدر آرات داره بچه جدید میسازه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82473" target="_blank">📅 00:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82472">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGGz6Ct36ROqojbYsfBWtgcxKYswmCSiVVi56HftJKfljshQTXWLSX01F-TBcWalzeRfy1GlR1XjnFEosWuwuamsRPpJ0W-0pszNWZigCdWLFT00zS3JkzF786IrNXqHDjwkOC61VJTfLmIMyfc4Bo9OVqPjrw0QWj1_GiZVkR_DGwGlaC6ckFkOphn0iBplZADxXIGCZlqZVtpxPg8Kk1wdTnMPVHkbSuG6wjpxSmISq8izmm6Z3B9zln-19mshOLVuRBrxp-ZtbcNj8sevtvNfirpon9ZmxtGFhY1WSokUp6gXZZB7B7BdGzv4lc6XOPsdaA9Mq3h7423JW5EXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر آرات داره بچه جدید میسازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82472" target="_blank">📅 23:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82471">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کیه این؟</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82471" target="_blank">📅 23:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82470">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSuSf6avCsCOcjm0gfr3xAa0EFLkpIwpj5xgLJw1-qqFbKt5PSoPJhWMs5TIJICCO34KhFfht1RlcjaAvWrAmLKo4VWjhGm4H5kqPAdr_U4A2DjLCw5Da-3zdROlQjDDjp0-LDDfY7gGq5J9jH3k0y8Li8wmd_t476r9OSp90qFWyucwuGc8fllz5xEfKaYjQjCoXfyCuruzggpFDNEsSdpd7hjTBx8gErEXX1wt42zw7pm8Ml4TMZ_VeH4_qn69rWjxiQGq8kKS1sfTjSHlFvWKAkNMQ2_T2jc1BOBqp5wKxuWtjoWKl0ATvAF2h384_e_O-E4F7cZsM040Eu-ZMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه برا خودت ارزش قائلی از تلگرام دور بمون دادا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82470" target="_blank">📅 22:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82469">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بهترین کیفیت کانفیگ V2RaY با تخفیف و قیمت استثنایی
☑️
فروش ویژه کانفیگ های تانل با کمترین قیمت تلگرام همراه با ارائه  نمایندگی ویژه جهت فروش
❤️‍🔥
🟢
گیگی 2200 تومان که با کد تخفیف (
bakei
) میتونید تا 20 درصد تخفیف بگیرید
🔖
جهت خرید و مشاهده محصولات:
@HyperPing_VPNBOT</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82469" target="_blank">📅 21:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82468">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3durHRg1_cgy74l3PpRP6kVTe6MC6HxpXcUZJewLdNJyiIyHBd6VyDozp6LHuezUlR3qFWFin8khOE3iM9R1e_yx-udH6B8Zv8_ik1Lqun1z1RbbHLZuhb-NZzYTXBvv-waPYLjoyr_LQ_-H9VS7xT2nXGZKbqqA17igd8tTdd6S97OXjMxJyAIeMcyAC5QWprtXqkCxyLqvvZQEqN_z8RmvV5mdPuZgLU6NI8bn_hJWjBKpvsWm_gAPIKmMrQnCJ1dO8ZZ_SBqI4tIBiDqK0eetjUxYUaEBwgjhb-aRuK3FmfLA8foAnIOoBC1AcURD5M3GoQ6f7OoxTSulT2i_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاتنهام چقد پلشته، با اینهمه خرج بازم گوهی نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82468" target="_blank">📅 21:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82467">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترک جدید حسین تی‌ام و TM Bax به اسم Shh! منتشر شد.   Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82467" target="_blank">📅 20:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82466">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترک جدید حسین تی‌ام و TM Bax به اسم Shh! منتشر شد.   Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82466" target="_blank">📅 20:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82465">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEnECDtqDmtFpL9El7buw-GhhkTG2DqAdCKFNet8we6SfKxNFgOIxkbUjnIfX0gz-rEKnq1vJxoLOvDGamv-OGkdDDruF8mK4KpJPbmuIOEj7oTGtJYukqJVdAPldelVjdCMa_HDDtwFXkVWHx-j8Fdyi_TbtOWMoMIvaWjhfyf2jWr_1e59_UBgNrjtmERn-pRZsKBCQM1yoI01RTLaRIz-hKREfxlgDeWd8DfBdtBdapjcqLBSA29EFm6fyBx-T_B5HwowJScYaafuxGDyEPqcJxmPp4gosqRkSOMqXuJECq2bq2ERS46o0M3bJ-R9-wBVDUaq4_qK12ZdahaZBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام و TM Bax به اسم Shh! منتشر شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82465" target="_blank">📅 20:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82464">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533cf854d8.mp4?token=uBzjH0X1PwJb9Inn_dKn1hlNrPr3602mdheZ0HwA7NgYUMyyo-UZifB5Eg6Z5pEIdbDD2Dgmu3Aab0u4xqbBARwbmo-BbkqSYHQoiu9bufjEf9JN9uJHK2matkQkPhgmEkEFkHd8-3advYlM46E214z563JT_Mo1m_xulvdOYnxvMXhrLHsT3Bl9uUMgXXjgO6kdjBjpda8l8CA7iR9nnggsryTKIZY8-o1Yjo1gsD02wdFf-dUixuHYsXw7nyr9SL1yWfUgBmdcFRonWt8o7Nyve1L3K2xGErEZA83ulFW5R0FSMNvAaPQ-drLXCI0eqPgDW_uJOIWWGrFY-YYvtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533cf854d8.mp4?token=uBzjH0X1PwJb9Inn_dKn1hlNrPr3602mdheZ0HwA7NgYUMyyo-UZifB5Eg6Z5pEIdbDD2Dgmu3Aab0u4xqbBARwbmo-BbkqSYHQoiu9bufjEf9JN9uJHK2matkQkPhgmEkEFkHd8-3advYlM46E214z563JT_Mo1m_xulvdOYnxvMXhrLHsT3Bl9uUMgXXjgO6kdjBjpda8l8CA7iR9nnggsryTKIZY8-o1Yjo1gsD02wdFf-dUixuHYsXw7nyr9SL1yWfUgBmdcFRonWt8o7Nyve1L3K2xGErEZA83ulFW5R0FSMNvAaPQ-drLXCI0eqPgDW_uJOIWWGrFY-YYvtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نرمال ترین حرکت پسرا تو جمع
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82464" target="_blank">📅 19:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82463">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVntlXQPpawBWUTG7FCwkoyIZKI7s3n1mjlD0l9RENjU-AUC0ZGk_c2aS09nVNkY-1PQe2EOhyvbPidIZONONtqBN2mXwYnlaXA6Htwm0hzqRVfouN8Ht0-pu0yflHfilvofh1sqGUUX238otPqLOAwf3J05gBGNNwTvgTocvKKXfXuegULO_lKB6ltIbOlq6c8ier86LhH0HXQRgfv2xAV59bZlPH8zff5xCGOUJ0WfAI_qLEPLdZDlgKjmtrh_UfeUhepNTeLGV6G1K9ednOjCWUkMM79j1FM7IP4B5f-GU1fDqDhvmdSYzE1PYwkMTvIjiHDsmU1bd7TE0upO3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاضرم برا گیر کردن سوزن حافظه‌ی تاریخی رو رضا پیشرو، دو تا کلیه‌هام رو بدم تا قبل از مرگ بهترین محتواهای تاریخ بشریت رو تجربه کرده باشم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82463" target="_blank">📅 19:21 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
