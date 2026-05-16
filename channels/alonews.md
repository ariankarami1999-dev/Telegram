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
<img src="https://cdn4.telesco.pe/file/KtAzV1Pmir1gkKl-4ODKdWdhVbBys6Zs0Fa6yJjg1Q8I8_DPN_DckRlefO0UVj8OC2Rvg6A-jvr72vxqLaADOFrL983gXtm4_IjZNpAATG5gaTNaTHWgmUN21zwxMKLOh8AAUWnXHBE9bBm-UdPgqg5PEEhOCIFRcg8iqFhgP0J2Kpm-_1dQ9rjEmw4_Rfyw2wlweQLPIq-dYVRxu_0AOxxj0dwq56WVIvz2QqtgcaUW5Ug0sOS5C73qgq2QKsyOuUJZYAg73KbQZ8wVDqhNm9bPJF-m1YsYuSw_rcbhUCusZurhd9lRv_B_8ISBc-hTnlzGpd1WQXOcH4w17tZrmA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 955K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 05:37:54</div>
<hr>

<div class="tg-post" id="msg-120300">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a9d3010c.mp4?token=SDLgv5badNwpR6Z4nMlLddsXbk_DNdj0uYNroYQ6ld26pxfJNEkRi2lNxcIZ1q_pU75WBw6nLVilNZzxxhKv6RwuZgbqjn-KegVCIu1AYn1gcEEsasY6yU9KaopxKYdFcB8eTljAowcKJNuzTaEKGSriHlYlW38GGLGOuS7O5kgRk6hg6uJXkSrw6CIPthLq3PW3UpKM1YrGljqebiuVPwTCBXEpqpsMAx0dM2ErL9d7-hjSt9z5zHpoIcutxqd5eu27SoYRy24RTEDE3bXKRuZnRFHAkVtGcwxA7M3XzmLnIJEKu01ipkmd8Uw9Roa64Ukt9fwMFZtvmTHEWid9Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a9d3010c.mp4?token=SDLgv5badNwpR6Z4nMlLddsXbk_DNdj0uYNroYQ6ld26pxfJNEkRi2lNxcIZ1q_pU75WBw6nLVilNZzxxhKv6RwuZgbqjn-KegVCIu1AYn1gcEEsasY6yU9KaopxKYdFcB8eTljAowcKJNuzTaEKGSriHlYlW38GGLGOuS7O5kgRk6hg6uJXkSrw6CIPthLq3PW3UpKM1YrGljqebiuVPwTCBXEpqpsMAx0dM2ErL9d7-hjSt9z5zHpoIcutxqd5eu27SoYRy24RTEDE3bXKRuZnRFHAkVtGcwxA7M3XzmLnIJEKu01ipkmd8Uw9Roa64Ukt9fwMFZtvmTHEWid9Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ در مورد ایران:
ما نه تا دوربین مختلف توی اون سایت داریم و دقت به قدری بالاست که ما می توانیم نام یک شخص را هم بخوانیم.
🔴
اگر اسمش محمد است ، بیشترشان محمد هستند ؛ شما می توانید حدود 50 درصد درست حدس بزنید.
🔴
هر کسي که به اون فضا نزديک بشه ، ما میفهمیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/alonews/120300" target="_blank">📅 02:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120299">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8501d1acc2.mp4?token=uMd3aK_eQcn6Vd89DtQ_ZKRC8rZ6d9mSXd9WiEvcQQBm7i1Fuk8j5u_Bu1xs6Zyp_U77yDLfmmrkQB7uBfOt6EWww9GNpxyaNmvYp6NIQptQS2vmxx9Ngst_MAjM6p8Vb5AqOsxKfjZMhwTCkSPyURIvw0CPkRd70RgapCiPA8XFC-WXM51WThn2p_Y1Or8oVT8Z_pBlLj7pmAx-h1lnPZus1hOJfqEqGP-nGYcouT_S9bp33p2v1UHEVJgIRltBz21_nzuVFuxF-WwObkG83U23npPjKIrZdipjDe9w91IeigQwRUbCENrFew1xVluh_2BUdEhlLjq6BXl3QWQ-lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8501d1acc2.mp4?token=uMd3aK_eQcn6Vd89DtQ_ZKRC8rZ6d9mSXd9WiEvcQQBm7i1Fuk8j5u_Bu1xs6Zyp_U77yDLfmmrkQB7uBfOt6EWww9GNpxyaNmvYp6NIQptQS2vmxx9Ngst_MAjM6p8Vb5AqOsxKfjZMhwTCkSPyURIvw0CPkRd70RgapCiPA8XFC-WXM51WThn2p_Y1Or8oVT8Z_pBlLj7pmAx-h1lnPZus1hOJfqEqGP-nGYcouT_S9bp33p2v1UHEVJgIRltBz21_nzuVFuxF-WwObkG83U23npPjKIrZdipjDe9w91IeigQwRUbCENrFew1xVluh_2BUdEhlLjq6BXl3QWQ-lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: گفتم گرد و غبار هسته ای را می گیریم ایران گفت: "شما می توانید آن را داشته باشید. اونا گفتن ، " ما نمیتونیم تحملش کنیم. ما توانایی مصرف آن را نداریم. گفتم: "چرا؟ اونا گفتن چون خيلي ضربه خورده"
🔴
برت بایر فاکس: چرا این کافی نیست اگر هدف شما این بود که آنها را عقب بیندازید ؟
🔴
ترامپ: از نظر روابط عمومی به اندازه کافی خوب نیست‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/alonews/120299" target="_blank">📅 02:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120298">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/013d87334a.mp4?token=r88osW5Qlyx2uVNmKgSv_BBihPx9JAPu5Uel-2wJKk2yGnYSPefwz3vhE1yo6RZlj6Hm6Mty2keT-ZdDsVKmw8dZ9Zj9mZ5a9tPJL9wSklQLdygISm90KLC8_EwSsTE6iW1k-9skMXNn7425LXOl0XG2dEsGYLI01AJ6ltrBriMZ2icIHvdigBlsJ4Ubtv6xCmQV_lxqvIsWm70E8xHg_KjhqDp9Yn8NWyLU9lXy2R-J3qTZlMnAl0S4luA5EsXLjAbQVq0pyBpG5yuE01qD8FBfSw_R7uNPce8_tlLPbxHWK3G0mUQh8nz0bi19j5HYgUHLY8MbQsAqkLcO705RGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/013d87334a.mp4?token=r88osW5Qlyx2uVNmKgSv_BBihPx9JAPu5Uel-2wJKk2yGnYSPefwz3vhE1yo6RZlj6Hm6Mty2keT-ZdDsVKmw8dZ9Zj9mZ5a9tPJL9wSklQLdygISm90KLC8_EwSsTE6iW1k-9skMXNn7425LXOl0XG2dEsGYLI01AJ6ltrBriMZ2icIHvdigBlsJ4Ubtv6xCmQV_lxqvIsWm70E8xHg_KjhqDp9Yn8NWyLU9lXy2R-J3qTZlMnAl0S4luA5EsXLjAbQVq0pyBpG5yuE01qD8FBfSw_R7uNPce8_tlLPbxHWK3G0mUQh8nz0bi19j5HYgUHLY8MbQsAqkLcO705RGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برت بایر از فاکس: فکر می کنید ایران به زودی تسلیم خواهد شد ؟
🔴
ترامپ: بله ، من هیچ شکی ندارم.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/alonews/120298" target="_blank">📅 02:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120297">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/057506e9d2.mp4?token=i11YOhqw32iBGkfQ14mdlfhLipa8vSU4GRqlG029Qj8Y4GfzhTcSd40oGT8CKZTbl0dHv0bRFQ29QGx9FBUimsdxT9v9Ke8BrKu6Z60UrB-sm_e3IlnBndaiVSKx-nVJsh2HdAVP2xcMt8ZBdWg7VuIL7uqB06ywdfdrlNpv0h21oOL-MsMg2iwZiqP04D2EBJpLiFYXNXyJvkho5FQjl2bJpY9ATWoBMWPFpzuq0u3hjCd5w9h_LtDIggdHJiqIbeHqY-YVGc4VtmXPNUN1EwbvEqgOD2atfizgjrUerQ_LyyK0ohwRj7KZH5fofZSZEVOYehsKCYwLBDcl_OBa0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/057506e9d2.mp4?token=i11YOhqw32iBGkfQ14mdlfhLipa8vSU4GRqlG029Qj8Y4GfzhTcSd40oGT8CKZTbl0dHv0bRFQ29QGx9FBUimsdxT9v9Ke8BrKu6Z60UrB-sm_e3IlnBndaiVSKx-nVJsh2HdAVP2xcMt8ZBdWg7VuIL7uqB06ywdfdrlNpv0h21oOL-MsMg2iwZiqP04D2EBJpLiFYXNXyJvkho5FQjl2bJpY9ATWoBMWPFpzuq0u3hjCd5w9h_LtDIggdHJiqIbeHqY-YVGc4VtmXPNUN1EwbvEqgOD2atfizgjrUerQ_LyyK0ohwRj7KZH5fofZSZEVOYehsKCYwLBDcl_OBa0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ در مورد ایران:
ایران سالهاست که جهان را با تنگه هرمز نگه داشته است. اونا در گذشته تنگه رو بسته بودن اونا ازش به عنوان سلاح استفاده ميکنن اونا ازش به عنوان سلاح با من استفاده نميکنن
🔴
رئیس جمهور شی دیشب با لبخند گفت: "خب ، آنها تنگه را می بندند ، و بعد شما آنها را می بندید."‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/alonews/120297" target="_blank">📅 02:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120296">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d4e78216.mp4?token=tE-tCVklohY7KeJlzkGcR53NeXlBkNQrBQpRzp1cHjOqVipZTov6c-SFyKtmkIpZ2gB0L4IIYaw6WlNXsHWncKm8x8G0V0_n4g8l-3683XFx1STjqTq7VS-FWTwRR_iwrjmWjma8PNXC8ZD7qrnvgVQDrZVM1AbeVNq9YphF8h4q_Tl4XN8PNewVJZwODQp54hI-pHJpGY0h3Hv0G6pDGybE_titM8TZ2Zv1LVIIaPZOHuBPfgGu7Twcb34lNwJk2g9JSUbSieHpaN8vAqVk6SHO59tt_fSGL_Qr3Y-U56bvdRcx0lMrJ_qzlQ9im8SVn6pRGAbDjqSlovfXYM7zBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d4e78216.mp4?token=tE-tCVklohY7KeJlzkGcR53NeXlBkNQrBQpRzp1cHjOqVipZTov6c-SFyKtmkIpZ2gB0L4IIYaw6WlNXsHWncKm8x8G0V0_n4g8l-3683XFx1STjqTq7VS-FWTwRR_iwrjmWjma8PNXC8ZD7qrnvgVQDrZVM1AbeVNq9YphF8h4q_Tl4XN8PNewVJZwODQp54hI-pHJpGY0h3Hv0G6pDGybE_titM8TZ2Zv1LVIIaPZOHuBPfgGu7Twcb34lNwJk2g9JSUbSieHpaN8vAqVk6SHO59tt_fSGL_Qr3Y-U56bvdRcx0lMrJ_qzlQ9im8SVn6pRGAbDjqSlovfXYM7zBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برت بایر از فاکس: آیا تاب آوری ایران را دست کم گرفتید ؟
🔴
ترامپ: چیزی را دست کم نگرفتم ما می توانیم پل ها و ظرفیت برق آنها را در دو روز از بین ببریم.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/alonews/120296" target="_blank">📅 02:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120295">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7b5ca6f24.mp4?token=eMgdtdRtc7aVWHG4kj5Jo_47kVcP16E9a38XpXMw8zFZQmzKLJj_DLvLx05UYFlShRriU7JZQ7FZdf1kDgr9CvyPMa8VRgOXumk6ODrT2Wu92koL61fyPVK3nZDI1l1V-65_dJRfjk8SH4Y-R44hFW-KhobGf79_fQ_rjU_GKKBlwBadHSvbqchk92gdVYnhlTOZoP8yWinJsMRLymgm09BPc6P4wAQW9S_DK_MrajnWzDJVdICKcc2ZVwwuDNWFXR6CsXxqrHla69dFNEDnTxJsd1l8hUs7HX0KM_QlfjAQacCwfh-UB3wQC70JohXuJFeQj_bOy0YiMx4hHRxk2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7b5ca6f24.mp4?token=eMgdtdRtc7aVWHG4kj5Jo_47kVcP16E9a38XpXMw8zFZQmzKLJj_DLvLx05UYFlShRriU7JZQ7FZdf1kDgr9CvyPMa8VRgOXumk6ODrT2Wu92koL61fyPVK3nZDI1l1V-65_dJRfjk8SH4Y-R44hFW-KhobGf79_fQ_rjU_GKKBlwBadHSvbqchk92gdVYnhlTOZoP8yWinJsMRLymgm09BPc6P4wAQW9S_DK_MrajnWzDJVdICKcc2ZVwwuDNWFXR6CsXxqrHla69dFNEDnTxJsd1l8hUs7HX0KM_QlfjAQacCwfh-UB3wQC70JohXuJFeQj_bOy0YiMx4hHRxk2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ویتنام ۱۹ سال طول کشید، عراق حدود ۱۰ سال، کره ۷ سال، یکی دیگه ۱۴ سال، یکی ۱۲ سال، یکی هم ۹ سال
- ما فقط دو ماه و نیم اونجا بودیم
- چین هم این هفته سه تا نفتکش پر از نفت ایران رو برد، چون ما اجازه دادیم این اتفاق بیفته،شما اجازه دادید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/alonews/120295" target="_blank">📅 02:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120294">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: چین جرات اقدام علیه تایوان را در دوران قدرت من نخواهد داشت‌‌
🔴
پکن از عدم نیاز واشنگتن به هیچ کمکی در پرونده ایران یا ایمن سازی ناوبری در تنگه هرمز خبر داد‌‌
🔴
چین برای تامین 40 درصد منابع نفتی خود به تنگه هرمز تکیه می کند‌‌
🔴
خب، به هر حال ما به یک راه‌حل خواهیم رسید. بنابراین یا این مسئله به‌صورت خشونت‌آمیز حل می‌شود یا بدون خشونت. و من خیلی ترجیح می‌دهم که بدون خشونت باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/alonews/120294" target="_blank">📅 01:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120293">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtJilXCWqskyisHWOCDL8nRodaZLLwmowQEyfSrU6_1yp2zAjKCPPnCQNuyJLV42hDOValHkgIKcvgtYqfFmz8DXNV_90zxS5vuAf5NwuuH515L6XHE9r9WdXeHNYFTfPjPE4GfesW4-Xbwwo8YF42bH7DXw6m5EcvklTY1qj3xiUtHHSU2GKlaixK7jnpU_2xN6bNuFZ1o3tVMrfpanK6ufV6MfsUpxY9Qe-X8SJnsuVdYvINECnykPjCi3AUOdWlPnY0K5PVmc3G3x4vncrN2td9pT5ULMf8SBZtHrdXNwDZZ7eolELIWQWLY_AjQvrH1k0oxtFAl3hX0ClUP-6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پک ۱۰عددی کاندوم با افزایش قیمت به ۴۸۰هزار تومان رسیده!
🔴
دولت باید به اینجور چیزا سوبسید بده تا همه بتونن استفاده کنن اما.....
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/alonews/120293" target="_blank">📅 01:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120290">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee9cf6e98.mp4?token=mybfeosUrxXC6T54etAfnhA-VdrD4_tlDY4sjph1VVQwjxIaEMRhhEqueh5iwIehLMG343yNlLQhGGJ53OV2Nh1oZUwHUxWGI1TU1ewqIkgU9G-HYzGgIxRH-s_w3yippVmxXhYgl6ZCNzEKSpkEgexL-3dkkJYixE3nAhAzW1BzukXI39aeYEOZfW9D9PpYZwhl_Dgu1WFmiANPcuhGynzuKZ-cKfvKX5EV3cbamKgcgZZ-W-gmG7nHQWmR9MLav5VceAP8BPYnvQ-mdIv6bBCMtXqfghiSxVBUsuKlkhuIMz06nnsZTw-aHOPkuZN8r0FuBcMHpGHJYgY1L0qvkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee9cf6e98.mp4?token=mybfeosUrxXC6T54etAfnhA-VdrD4_tlDY4sjph1VVQwjxIaEMRhhEqueh5iwIehLMG343yNlLQhGGJ53OV2Nh1oZUwHUxWGI1TU1ewqIkgU9G-HYzGgIxRH-s_w3yippVmxXhYgl6ZCNzEKSpkEgexL-3dkkJYixE3nAhAzW1BzukXI39aeYEOZfW9D9PpYZwhl_Dgu1WFmiANPcuhGynzuKZ-cKfvKX5EV3cbamKgcgZZ-W-gmG7nHQWmR9MLav5VceAP8BPYnvQ-mdIv6bBCMtXqfghiSxVBUsuKlkhuIMz06nnsZTw-aHOPkuZN8r0FuBcMHpGHJYgY1L0qvkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجریان بیسواد صدا و سیما برداشتن یه تصویر هوش مصنوعی رو گذاشتن و دارن تحلیلش میکنن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/120290" target="_blank">📅 00:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120289">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/444d83ba6e.mp4?token=cRlz6M1ADneTrHR1PqN7Z7L5wU6dTr69zMyHbdjz90DXFjm00nK7Q3uRRuhmOM-YjDxXZ2-KuLtgqgwMZSRkmTmo6Y9UBDcWDzJyYAdO7RuEKvnQd83Uqh-WSHPnGGAb8Mp6fZwuoHPkwLT4SwMFyx2bHYjCiNJziC89eVhLt3Ez2c14oeda82APO-adT82murt4r3DisVgWJBqWumcF7EEdutnaApNsRgJCwBuDlR1eVK9VLM5wSNGJanpdJqA937aBuOcDlxNctRlyrw4cuV5q9FtKY9_84FOmFue9a48T3H1MdkHMjszD0BE4z21fVvOkDhyrFnMB66P8zDX2RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/444d83ba6e.mp4?token=cRlz6M1ADneTrHR1PqN7Z7L5wU6dTr69zMyHbdjz90DXFjm00nK7Q3uRRuhmOM-YjDxXZ2-KuLtgqgwMZSRkmTmo6Y9UBDcWDzJyYAdO7RuEKvnQd83Uqh-WSHPnGGAb8Mp6fZwuoHPkwLT4SwMFyx2bHYjCiNJziC89eVhLt3Ez2c14oeda82APO-adT82murt4r3DisVgWJBqWumcF7EEdutnaApNsRgJCwBuDlR1eVK9VLM5wSNGJanpdJqA937aBuOcDlxNctRlyrw4cuV5q9FtKY9_84FOmFue9a48T3H1MdkHMjszD0BE4z21fVvOkDhyrFnMB66P8zDX2RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مصاحبه‌گر : قبول دارید عامل گرانی‌ها محاصره آمریکا علیه ماست؟
🔴
حامی حکومت : نه، قبول ندارم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/120289" target="_blank">📅 00:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120288">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نیویورک تایمز: گزینه‌های ترامپ در ایران شامل نیروهای ویژه زمینی برای کنترل اورانیوم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120288" target="_blank">📅 00:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120287">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e3b53b1a.mp4?token=sunbuM-6fQ3pNkPCIh5hkaBZnpZ__FvaYgwXIdyNHo0Op_Pct0XuTNZaurgRof2hf3hWn8ov92ZQ0iGnL-dIpYF-m5rCdUWMhnqovqR3Xo0fk7Cbr586dqLs8mfyk_0Idr5YACuLx59H2df3k8QscPcxaiHW7GqxvrE_4SsjJ3sDmaTIe7-reMYAN6j37JUu5qqkn3vXIkxYYrBe3p0sWsHbgJ13-9B78BirVrV_kCSesWfKBAYs_aOlP0LDUPDw_1QymERnWgTZdn5cN0l_sclZH7CagicWD9y9i3oI1_GLCIk1xQHOv38unvtGDjEP9tUBAQNw6-n53cyapDuTqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e3b53b1a.mp4?token=sunbuM-6fQ3pNkPCIh5hkaBZnpZ__FvaYgwXIdyNHo0Op_Pct0XuTNZaurgRof2hf3hWn8ov92ZQ0iGnL-dIpYF-m5rCdUWMhnqovqR3Xo0fk7Cbr586dqLs8mfyk_0Idr5YACuLx59H2df3k8QscPcxaiHW7GqxvrE_4SsjJ3sDmaTIe7-reMYAN6j37JUu5qqkn3vXIkxYYrBe3p0sWsHbgJ13-9B78BirVrV_kCSesWfKBAYs_aOlP0LDUPDw_1QymERnWgTZdn5cN0l_sclZH7CagicWD9y9i3oI1_GLCIk1xQHOv38unvtGDjEP9tUBAQNw6-n53cyapDuTqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گلایه مخاطب ایران اینترنشنال از قیمت نجومی عرق سگی
🔴
قبل جنگ لیتری ۲۵۰بود و با دوستام میخوردم اما الان لیتری ۱۵۰۰ و تنها میخورم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/120287" target="_blank">📅 00:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120286">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ادعای نیویورک‌تایمز: دو مقام خاورمیانه‌ای ادعا کردند که آمریکا و اسرائیل در حال آماده‌سازی گسترده برای احتمال ازسرگیری حملات علیه ایران هستند؛
آماده‌سازی‌ای که بزرگ‌ترین سطح از زمان آتش‌بس محسوب می‌شود
؛ این حمله ممکن است از هفته آینده آغاز شود
🔴
مقام‌های نظامی آمریکا به‌طور غیررسمی می‌گویند پیروزی در حملات جدید بسیار دشوار است، زیرا ایران بخش زیادی از توان موشکی و زیرزمینی خود را بازیابی کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/120286" target="_blank">📅 00:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120285">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
نیویورک‌تایمز: ترامپ روز جمعه پس از بازگشت از چین، با تصمیم‌های مهمی درباره ایران مواجه شد؛ در حالی که نزدیک‌ترین مشاورانش طرح‌هایی برای ازسرگیری حملات نظامی در صورت تصمیم او برای شکستن بن‌بست از طریق فشار نظامی تهیه کرده‌اند
🔴
مشاوران رئیس جمهور آمریکا می‌گویند ترامپ هنوز درباره گام بعدی درباره ایران تصمیم نگرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/120285" target="_blank">📅 00:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120284">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
فارس: نمایندگان مجلس پیشنهاد افزایش ۵۰۰ هزار تا ۱ میلیون‌تومانی رقم کالابرگ را داده‌اند اما دولت گفته که تنها منابع افزایش ۲۵۰ هزارتومانی رقم کالابرگ را در اختیار دارد و سازمان برنامه هم اعلام کرده که پول نداریم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/120284" target="_blank">📅 23:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120283">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ رسید آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/120283" target="_blank">📅 23:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120282">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHitin_D1tV6B6BVGQkhjajQ1OfX-yahDB0s-BhXlC2DrvpYPB4Wa5hC7anWtjng7kuGFDuVGjDNAwUcGplfpKzDeL0aWEEtX6Zsep4Sa_TMmkt6w9T4sVBnjp1L6N2uAsBgAOk1ZePIf1_JvBAe0ZsqqT4R8gC8wv3wpWzUJe0JompIBSRcyaGUTDq4brTlkkMcveuRocoPs8ECDqWeb2oHq-HHSXQqZUE_GoaqULPxpQR5Wdk3OXU4nTIXRZYm8pGHDw1_MtnrwfSmcYOkVIcXCKUwiO5UqXxG-dl_-MboybpwjkphJonkYizdxl6n8AOdbicBhYPe192LEye3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقامات آمریکایی مشکوک هستند که هکرهای مرتبط با ایران ممکن است پشت یک سری نفوذهای سایبری باشند که سیستم‌های نظارت بر سوخت در پمپ‌بنزین‌ها در چندین ایالت را هدف قرار داده‌اند، طبق گزارش CNN
🔴
هکرها از سیستم‌های اندازه‌گیری خودکار مخازن که به اینترنت متصل بودند بدون حفاظت رمز عبور سوء استفاده کردند و این امکان را برایشان فراهم کرد تا خوانش‌های نمایش داده شده سوخت را دستکاری کنند — هرچند نه سطح واقعی سوخت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/120282" target="_blank">📅 23:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120281">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ژان-لوک ملانشون، نامزد ریاست‌جمهوری فرانسه، درباره ایران و تنگه هرمز: «وقتی کشوری از خود دفاع می‌کند، از تمام ابزارهای دفاعی خود استفاده می‌کند.
🔴
ما هم همین کار را میکردیم.
🔴
ما تمام کانال مانش را مین‌گذاری می‌کردیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/120281" target="_blank">📅 23:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120280">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
منابع عراقی از حملۀ پهپادی به مقر گروهک‌های تجزیه‌طلب در کردستان عراق خبر می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/120280" target="_blank">📅 23:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120279">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی: قواعد نظم جدید جهان دیگه آمریکا محور نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120279" target="_blank">📅 23:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120277">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b1bc7ef.mp4?token=TNkqwX8EdVvjSAlCEQN4zktzEfp6rLxdrZC_0HQmkrpLotpmFUjq2N8WKDajA5mwhaKOZkX5jGb5urvPX_23gUAoWszQn2BDj6x4d-N4Vs5wFjmYgWNnVr7BZSZkdZWsht4Ks2G12XdQVad3cnP4Is9yldjmsYkOWqyknLspZhmmtW9zP1gSh_9UQRJaWS3TcsA2rvvKSLOVHGrnM_pi1B6XFMEQsIYb_4xnvM8JOZSs94KLqy7gWPtCEV5CAIDXMvII8InUPgk9piuKsr_Q-pdMBjFk_pD2rbsR3WzC9X6i2hZM4Y-6SexIksqQDmOHnRRKbz_actSyW0nQ3eDVsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b1bc7ef.mp4?token=TNkqwX8EdVvjSAlCEQN4zktzEfp6rLxdrZC_0HQmkrpLotpmFUjq2N8WKDajA5mwhaKOZkX5jGb5urvPX_23gUAoWszQn2BDj6x4d-N4Vs5wFjmYgWNnVr7BZSZkdZWsht4Ks2G12XdQVad3cnP4Is9yldjmsYkOWqyknLspZhmmtW9zP1gSh_9UQRJaWS3TcsA2rvvKSLOVHGrnM_pi1B6XFMEQsIYb_4xnvM8JOZSs94KLqy7gWPtCEV5CAIDXMvII8InUPgk9piuKsr_Q-pdMBjFk_pD2rbsR3WzC9X6i2hZM4Y-6SexIksqQDmOHnRRKbz_actSyW0nQ3eDVsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهر صور تو "جنوب لبنان" بعد از حمله‌ی سنگین ارتش اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/120277" target="_blank">📅 23:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120276">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
واشنگتن پست : ایران واضح‌ترین بازنده دیدار ترامپ از پکن است، با مخالفت علنی پکن با اختلال در هرمز، تعهد به عدم ارسال تجهیزات نظامی به تهران و توافق بر اینکه تنگه «باید باز بماند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/120276" target="_blank">📅 23:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120275">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/195d80b28e.mp4?token=d46ht0c6MGlAJk7SPhPfMQ6FcDXgV644l9GL4V2oa3qHS28FTxr7PgEg56ER002SfVCGCCcyM0VUS8Fhh2jc2IfUEQ-fjvb3Ty2W5vUfKx4x4RIQoeiBdxQqm6O7jOVKdf3mQ8Usdz2eeaeuLSWMoJ9cMFK4g4-66Xsis_e-_maecOL4hQ7WTlZyXBxxCYwQ10YDri4UzGwVsyzJZEswFJiYshq8PDIT1kegIu4i9lY9m6tBdK2ma1EfQ_P_4Clisov7TBpl-8y31bg2Xp9SIrXkEQD2D4ND-1GkEhbQlLeGiy4cp-VkcanOuSPFM6Bei5TpW1G3C_bk7WBHLnANCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/195d80b28e.mp4?token=d46ht0c6MGlAJk7SPhPfMQ6FcDXgV644l9GL4V2oa3qHS28FTxr7PgEg56ER002SfVCGCCcyM0VUS8Fhh2jc2IfUEQ-fjvb3Ty2W5vUfKx4x4RIQoeiBdxQqm6O7jOVKdf3mQ8Usdz2eeaeuLSWMoJ9cMFK4g4-66Xsis_e-_maecOL4hQ7WTlZyXBxxCYwQ10YDri4UzGwVsyzJZEswFJiYshq8PDIT1kegIu4i9lY9m6tBdK2ma1EfQ_P_4Clisov7TBpl-8y31bg2Xp9SIrXkEQD2D4ND-1GkEhbQlLeGiy4cp-VkcanOuSPFM6Bei5TpW1G3C_bk7WBHLnANCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره تایوان: من به دنبال این نیستم که کسی مستقل شود. و می‌دانید، ما قرار است ۹۵۰۰ مایل سفر کنیم تا جنگی را انجام دهیم. من به دنبال آن نیستم.
🔴
می‌خواهم تایوان آرام شود؛ می‌خواهم چین آرام شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/120275" target="_blank">📅 23:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120274">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1806e8ed23.mp4?token=tDCOsuf-PV8tPDQVPa9AGAYE90vwD_aHfAMw9eOvaJI33TWxoh34Arry5O6fhcnEBnbf1dO1SBVnSq_AVKdr05W8eY3BH9rdJEH2e88Sp8SGJokRt-xOutj8uoBWbyxpoLkvKKXW98Ke1BcGvkJa8divSuPwEyfIst040o4-lwiP2ogVRsFpU4DMcX9xdh2QSeZl1v_2aRp319aaLVgSQMZeG_jOdREA9FvCpQHrwBGODpYrVG1dO11HybZm09IJCdEf6zvTZdBpxLcfXFv-jDtBopr0t0Hzlfr9XMeLSl-JB3FUuRRintaFXQShK73OU7c6Z-pS32V4UGjQvsTHTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1806e8ed23.mp4?token=tDCOsuf-PV8tPDQVPa9AGAYE90vwD_aHfAMw9eOvaJI33TWxoh34Arry5O6fhcnEBnbf1dO1SBVnSq_AVKdr05W8eY3BH9rdJEH2e88Sp8SGJokRt-xOutj8uoBWbyxpoLkvKKXW98Ke1BcGvkJa8divSuPwEyfIst040o4-lwiP2ogVRsFpU4DMcX9xdh2QSeZl1v_2aRp319aaLVgSQMZeG_jOdREA9FvCpQHrwBGODpYrVG1dO11HybZm09IJCdEf6zvTZdBpxLcfXFv-jDtBopr0t0Hzlfr9XMeLSl-JB3FUuRRintaFXQShK73OU7c6Z-pS32V4UGjQvsTHTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برت بایر از فاکس: شما در حال انتظار برای تصویب میلیاردها دلار سلاح برای تایوان هستید. آیا این روند پیش می‌رود؟
🔴
ترامپ: خوب، هنوز آن را تصویب نکرده‌ام. خواهیم دید چه اتفاقی می‌افتد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/120274" target="_blank">📅 23:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120273">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4f5115bb.mp4?token=rgA_tSTAuUj5fXHSts5tvJTvzqWs8pvYdTQbeflOkfx1owenV6PGF8g9DMDHyEwbn3e_eFkGnTowLyRxyq9GN6MC3Iwf1_XRdbI23VkjLnCKbaZJK9JoIPjJsm_lqtPLrAyg160VpgjTZL1Oihy3U_poa49HlBpZ8-JqxZ8w2bKrGLEfPYWaEkdJerBP07WNphU9NqLdoJ2TT2SVUeml4WaWAhboy-U-35Dt01XEHhrEUwF1eRN5b6sr-FcQ8-xjonRxQ9clYrjant7YeU281bLYhh8L5rOAhgHR4YrYhDEoAzsmYWzy3VbBUxgsJ8mn-6kblfOnd4MVX3s9PEt66w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4f5115bb.mp4?token=rgA_tSTAuUj5fXHSts5tvJTvzqWs8pvYdTQbeflOkfx1owenV6PGF8g9DMDHyEwbn3e_eFkGnTowLyRxyq9GN6MC3Iwf1_XRdbI23VkjLnCKbaZJK9JoIPjJsm_lqtPLrAyg160VpgjTZL1Oihy3U_poa49HlBpZ8-JqxZ8w2bKrGLEfPYWaEkdJerBP07WNphU9NqLdoJ2TT2SVUeml4WaWAhboy-U-35Dt01XEHhrEUwF1eRN5b6sr-FcQ8-xjonRxQ9clYrjant7YeU281bLYhh8L5rOAhgHR4YrYhDEoAzsmYWzy3VbBUxgsJ8mn-6kblfOnd4MVX3s9PEt66w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سفیر ایالات متحده مایک والتز ادعا می‌کند که «نتیجه بزرگ» سفر ترامپ به چین، موافقت چین با عقب‌نشینی از ایران بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/120273" target="_blank">📅 23:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120272">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
امیر قطر و محمد بن سلمان، ولیعهد عربستان سعودی در یک گفت وگوی تلفنی درباره آخرین تحولات منطقه با یکدیگر گفتگو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/120272" target="_blank">📅 22:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120271">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de25f2d379.mp4?token=KA3Ak0UPOpbBEpYuYqjaiehl-_cI-3de0SvZcxI68KDLqyy3E3i6IJPXM_B95n_oM-MW-YtUDMUQWkWUZhpZII4qqADdOeoEPsT7PulwuJzuv1R06wtf1g6_EhCUUxfjogFBBNELSKsaHLJA5-I5ViC4QY98xIYYPw_Xu6d9jkBnUthURkRqwSxLW6OMwqaulX2p4FJI469QKQFxI1JSZ0Fe-QXAh6XM1AOfg5PkRfceMCx8v-I5SoLRdlHToUttOH83g8N-PYptECirFI_2qpjlfpTBBKLxV8sS-ca0Lj2AXBoyk1-A3QGSXw8L6vvdT5NRNZ7UfYXLF3cQB7NogA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de25f2d379.mp4?token=KA3Ak0UPOpbBEpYuYqjaiehl-_cI-3de0SvZcxI68KDLqyy3E3i6IJPXM_B95n_oM-MW-YtUDMUQWkWUZhpZII4qqADdOeoEPsT7PulwuJzuv1R06wtf1g6_EhCUUxfjogFBBNELSKsaHLJA5-I5ViC4QY98xIYYPw_Xu6d9jkBnUthURkRqwSxLW6OMwqaulX2p4FJI469QKQFxI1JSZ0Fe-QXAh6XM1AOfg5PkRfceMCx8v-I5SoLRdlHToUttOH83g8N-PYptECirFI_2qpjlfpTBBKLxV8sS-ca0Lj2AXBoyk1-A3QGSXw8L6vvdT5NRNZ7UfYXLF3cQB7NogA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
۳۰ روز طول کشید تا جنازه عبدالرحیم موسوی، رئیس سابق ستاد کل نیروهای مسلح ایران، رو پیدا کنن
🔴
پسرش اینو به صداوسیما گفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/alonews/120271" target="_blank">📅 22:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120270">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEd1cD8BBNb_NxyDnmM8GKkjnr1Xfarn7rHMzF2nBwKx5Q5mP1EdEIYMHsDlty9N7tpLeZh0dKof2TErQ2Es70-78RN4OQY59CtPAWOeXMA8caRY0fih1RotkS1MsgT2ip6CUeZeZoJbQibHuK3QYfSIxH-auqC4a8ZbTw4HN2YWSI6SEiAMZuCax-XWvAqUyuEe3F9V7pxI4qCRLCyeE9hago6yaY_zmqCP3ZoyyIHCC3trUjJMZylztJqrcERtx-dzVXjHKU_8Tuyb3jSJmxXAqEZcnTFfoZH_l4dR3cQ21oiH9p7Ns2b9pLh-Y7LZ_nvgjgAkqc_wnFMVvLntUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید و عجیب ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/120270" target="_blank">📅 22:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120269">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRg4rFjrpc_e6YEUkQsiwASWtDAr9LqiN-UL90urkVMrlEa3N2XM4_qCQfKCodaaMahxLpyXWzLV4-3cNHiqWb5AEAbVMtdkl8hIVvDeC855wcB-_aGqR9bxhVnaUl9YK8f9SRGbpjFfM_0JlTvFYw5DpiZRrHYcpzOtbs-Rkvz5lwx6bdD5a_-ytypJ57J6eGdvm6q0Hir1_JK4N_FDr0kaPP9v79VZ3tgT1S95Fx1Aaw7_lNmImlm9SpqU_mnrf66XFVfDNyzoIPQwuc4bEV9_twQ8WBfbY54_xj9uKfFapNGFe-4PKkTLpS-l7SmviZXGYFHLE1en_kr-VHnSvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دنا پلاس؛ ۳ میلیارد تومن ناقابل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/120269" target="_blank">📅 22:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120268">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMiRFLrTkWzABJ8PQULn9CxQ63PUSBDozbZUyUPSYqL9GCXIrnpTCn5T2lKCoUiWrEQ-S_wl7JIKRj3QkiH6jwoEPjOLof9Oi63AJggy4dkxvtHqMHVS6cPVW2dzn0KP7EqwjBJGVI0Yxg-c9AWeY1GWnVTnq5e3THTP9iVWpCXOIwuwYUSkOcJlEx8vL-7QvjlY8bMXljwBHdRl6MVU-u25jzmfBxXbr2tsO0KY1e-Q95DRGFGYO5bg8imgkCgl5cj89aYcDF0FYKv0BSLXpVi_lgCjPFd9AgXWESnvTSNbIT_zu5qyYvrjUNoTMpZKLenUV4u5WGv0bQIZFOGauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۹.۴۳ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/120268" target="_blank">📅 22:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120267">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foS5ZIy8riCGyf1Yr4CDc1VCN-lM5COi0uYzi5XIRNmTT5sJvRHaJq4-i6iMnmedZRZAmKgNuKAh5UrZB7FQDEWiYYR3HQhLwant_NElzzhdCW9-lUegiWamGN96bnwKkHpQw4HzRAlDoeeyiPcgOP4nKewf9FJ0am_8PnEB-RqEB7QKhRkvH0bqMOoci7OL5nBCJyIcTxy3wnDcvbegNxjTpeZSGRKro6dk7mPhd2wTliFgKGLHyRbWOJsPcGOb0yarsnhL723u5ZZP0sCCfs-qm4w2SQRWbJuY0Q1WCa58DBRkhEY-KyXIyH2MDQLiOqZMUOpdvd45MVpCfxs5iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار مرندی: حمله ایالات متحده به زیرساخت‌های ایران به قیمت نابودی نیروهای نیابتی آمریکا در منطقه تمام خواهد شد!
🔴
اگر ترامپ به نیروگاه‌ها و پل‌های ایران حمله کند، جمهوری اسلامی برای همیشه نیروهای نیابتی او را در خلیج فارس نابود کرده و زیرساخت‌های حیاتی رژیم صهیونیستی را فوراً در هم خواهد شکست. رکود اقتصادی فاجعه‌بار جهانی تضمین خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/120267" target="_blank">📅 22:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120266">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhU_pFOO30wixtdX7p_PSw4xAp7_IdYPsn_aVklIFifValYWd9WRifZdT3Udxwfh5cc9YXit3lXaVNPWe6c8bqYKRiCSBqeUoFLqaze0SW6c_kYRTgMfDmFkJp_YZjH430VuQneNFJWhdGD8Us0uS9kCWQ6w5D3v7rO_Piteb_mszD45PAeLp_nTWo3kh6qOEAJqHAFJ5ZNu944nEvfaPg-t8LcBFVPthfxtGx_11w5NUzyyQVJgKAN2zwv-HiZ1uTYrHFnrtXkyMms10npVHpo2Dns9rMv19lVLfVxqNmsulTkBlh5MyOaXOb_VNPL5A9j4pLyt6pMK7ivuuzRWPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعیین جایزه ۲۰۰ هزار دلاری توسط FBI برای کسب اطلاع از افسر سابق نیروی هوایی آمریکا که به ایران پیوسته و اطلاعات نظامی حیاتی را لو داده است
🔴
شبکه فاکس‌نیوز گزارش داده است:
«مونیکا ویت» متخصص سابق نیروی هوایی ظاهراً از سال ۲۰۱۳ فرار کرده و اطلاعات طبقه‌بندی شده دفاع ملی را در اختیار تهران قرار داده است.
🔴
او متهم است با استفاده از دسترسی‌های امنیتی خود، هویت همکاران سابق و جزئیات پروژه‌های حساس اطلاعاتی آمریکا را به مأموران ایرانی لو داده است.
🔴
مقامات امنیتی آمریکا معتقدند ویت پس از خروج از کشور، همکاری نزدیکی با نهادهای اطلاعاتی ایران آغاز کرده و در عملیات‌های سایبری علیه پرسنل نظامی آمریکا نقش داشته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/alonews/120266" target="_blank">📅 22:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120265">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
الجزیره: هند پس از افزایش قیمت سوخت، عوارض صادراتی بنزین و گازوئیل را افزایش داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/120265" target="_blank">📅 22:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120264">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cf44I_S0nVBflzA74K7G22khL61Deyyks7UADwDrG3pVyV6_CTIg_mImaNet-SoDUjBhNBCIB3H4qyZONjCZgEICmBI7USyFCYMw2qrilYiSimQYvby8TPmnoUHULqaVCRyuAKX7Pj9QOpOwhhVX9mwROAOhLNz4O2vNRHsOJdvzH5pQQzHI6S5pO89H51nxhU3jdG8dON5ksWxWevVfGEd8lID2kZ9RerkLciTsHxraPpXGx6Hch8xAS5jdj4s-Os9UxQgXFHMS7MtJYC7o4tFXCofYfdxL3U2CSXgQCJSntOjJK_clyQXoR1gtCYHz2FppWZwA5-ZRG56a6EJMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امور خارجه پاکستان، اسحاق دار:
خوشحالم که اعلام کنم ما در بازگرداندن ۱۱ شهروند پاکستانی به کشورمان موفق بوده‌ایم، همراه با ۲۰ شهروند از کشور برادرمان ایران، از طریق سنگاپور، که در کشتی‌هایی که توسط ایالات متحده در آب‌های آزاد توقیف شده بودند، حضور داشتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/120264" target="_blank">📅 22:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120263">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26232c3807.mp4?token=A--mIMy9dz70Cg8GZx7pJUuJnw-utqruA4YcXMA7x7FechtDmqWWaQwpcxXpcLQPk7x45XrbJ6VxE92xlKpWezfbzHbfQPwjPd5F3czdRgTVhp2KK7I5KO3IE2MHqNXlfqMKb81BOtCDXBakaYXsWYvv8ELNicawe6e2m-lz9GFCuwtM-rO1geumQAo9GcgInKaHnkmhMc4yl_3hHPaL4ASfC-ihMSQDbqifiVzbs9lvAnefAeMLnXiedGFswbV6Dfw5FfuhkLa5Sj6pXyHbffP_L5JfARk00ox37-mYjbpZ0s_kmirOZUvI7e6h7h4dL4QAzkpKku6Z-6QRr58DeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26232c3807.mp4?token=A--mIMy9dz70Cg8GZx7pJUuJnw-utqruA4YcXMA7x7FechtDmqWWaQwpcxXpcLQPk7x45XrbJ6VxE92xlKpWezfbzHbfQPwjPd5F3czdRgTVhp2KK7I5KO3IE2MHqNXlfqMKb81BOtCDXBakaYXsWYvv8ELNicawe6e2m-lz9GFCuwtM-rO1geumQAo9GcgInKaHnkmhMc4yl_3hHPaL4ASfC-ihMSQDbqifiVzbs9lvAnefAeMLnXiedGFswbV6Dfw5FfuhkLa5Sj6pXyHbffP_L5JfARk00ox37-mYjbpZ0s_kmirOZUvI7e6h7h4dL4QAzkpKku6Z-6QRr58DeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
یکی از صدها موشکی که برگشتن رو سر مردم و جمهوری اسلامی طبق روال همیشه با مظلوم نمایی انداختن گردن امریکا و اسرائیل
🤔
مدرسه میناب جای تحقیق و بررسی زیادی داره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/120263" target="_blank">📅 22:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120262">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k59dvWYQywRvYT4aW3Nvi4h8CVURbVhRvB5niOo7vm4OpTbTUddnXaKBhydhsMRVvi7dhxFtUhhgnGAb1rFoGftBrAVsnBZVN-IM_e-u2Z_Ayde7FB0kiAGE58V2MmUiiw3Z8BI5DNeg2zhBCokysrgnlp1jrPGpA4QphjmmXpwyc66eDNKaZp9RP5VQQ6rNbqUPuBn-PHoy4A6raz8RUlEYadXi908UIeT1ALOfwQJPfA1dWwKRYZydDq3fCba2rxsnixe3Eqyjukuvx_fhvThq5EZI0gvRq03kfIhromLx-72KrUOUsGLSX1jDueQE3cfvwC1hSO5FS96b06doKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید و عجیب دونالد ترامپ:
کشور ایران ایالت ۲۴۳اُم آمریکا است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120262" target="_blank">📅 22:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120261">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
اوگاندا و جمهوری دموکراتیک کنگو هر دو اعلام کردند که شیوع جدید ابولا در کشورهایشان در جریان است.
🔴
۶۶ مورد مرگ ثبت شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/120261" target="_blank">📅 22:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120260">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا: آتش‌بس بین اسرائیل و لبنان به مدت ۴۵ روز تمدید می‌شود تا امکان ادامه روند مذاکرات فراهم شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/120260" target="_blank">📅 21:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120259">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/120259" target="_blank">📅 21:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120258">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hyRlVB-em-c0kvfXEE9vwrGqYkTdNWmOoKVKdMPrgYat-gP3E6XNAK5x3akJP3PB9cphDNl2EPbc_mC5rAaz57mUFTYy8w5r6igtyX7Z7WfrE-TG7k1fRdzNxJl29-FtXNbJ44RTAo4tEbgd__sAjmEJ543Dd6l6obMVd_uOuo_QnJY_22jFGWUKzhbck3nZ0eiQq-a5BIUhv9qX5dePfNzFg7K_LWw4OFtOiHORDqpmbKaK7L_viN5DSiHkHzX6uXRYqY5BQ6uTuHLxnMECBXc3tQo5Gm6KWPPfGnp-ocJyHDJOpsgftBYMsQMZc6jprSGeRIOnsZpScT1rSxLPvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه آمریکا : ونزوئلا 7340 کیلوگرم اورانیوم غنی‌شده‌‌‌ش رو به آمریکا منتقل کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/120258" target="_blank">📅 21:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120257">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KmTOFU02dYI3CaAC1-xSdriP0TUhPFr02zywZnbKaRSVbGxdfnRmsd3-l1FXylnHF6szCfYcoFF3HKzQu-QTv0bRs5GHIL4IHODdPfW8tCJc1e0_jBr-cR5QySm4pi8fWxKcHfG1JpQJyicUDt4zbaK1iQ0l0ODteFq99xTALUPeESYXohGiiUPyLlAWujxl_zrlZYv3ms6K9sUo5vKiLiY3jQFxWQDwyGI2bDxDMauqD34ujIzBcSwXJn77IfP4ZAPTyis_EX9__ZAIOh8E_vs7733XStjDCvLsqAbctOhsigxz-wBblzRSs6VtlmG6bUDUVyxjT4V7iGk0CU2R2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش وی پی ان
👑
ارائه بهترین کانفینگ های ایران
👑
👑
👑
بدون ضریب
🤴
👑
👑
👑
همراه با لینک ساب
🤴
👑
👑
👑
پرسرعت
🤴
👑
👑
👑
همراه با لینک ساب
🤴
👑
👑
👑
۵ سرور متفاوت
🤴
👑
👑
👑
همیشه در حال اپدیت
🤴
👑
👑
👑
کانفینگ های رایگان
🤴
🦁
توجه کنید شاید یکی قیمتش ۱۵۰ ۲۰۰ باشه ولی هر قیمتی دلیل بر خوب بودن نیست بلکه ضریب دارن و یا سرور های کند دارن!
🦁
تنها چنلی که کانفینگ رایگان میزاره  :
👑
https://t.me/+nVsNnhQep1s5YTA0
👑
👑
https://t.me/+nVsNnhQep1s5YTA0
👑
👑
👑
👑
خرید از طریق ربات :
👑
@CyrusV2ray_bot
👑
@CyrusV2ray_bot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120257" target="_blank">📅 21:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120256">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/575f6be6da.mp4?token=FL_zxyeEpLoT17tF-6r4S7l225pUsnmDCP6eKaottRk0SIbhvHWojhfyKNVuupZIj-Q1GK5XcdG1t5lfXCB8Q3aWDxgQ7vQypWrVAzCNLNLfX27qX6QBK_mhk9LzjuF0Q1NMPmCj1_U-XB2RNznITMJkJE8_KVnRiF9z5LoU74b44-hm2PjZ0hI9b3tiizSbDlhnzW7bDnzi7pG8R77XQGJBiOKKBooCanP3Xl3f5Pm1T5jTEs-aWBZdZHSs9Tzjk-ojKFrVMLq3nMefn-kpJp4mU6U5fu4vVvQBviP2BFPymuD2L6uIFoLEChuifocuLnwt1WYtK7MBqS9WDlXo_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/575f6be6da.mp4?token=FL_zxyeEpLoT17tF-6r4S7l225pUsnmDCP6eKaottRk0SIbhvHWojhfyKNVuupZIj-Q1GK5XcdG1t5lfXCB8Q3aWDxgQ7vQypWrVAzCNLNLfX27qX6QBK_mhk9LzjuF0Q1NMPmCj1_U-XB2RNznITMJkJE8_KVnRiF9z5LoU74b44-hm2PjZ0hI9b3tiizSbDlhnzW7bDnzi7pG8R77XQGJBiOKKBooCanP3Xl3f5Pm1T5jTEs-aWBZdZHSs9Tzjk-ojKFrVMLq3nMefn-kpJp4mU6U5fu4vVvQBviP2BFPymuD2L6uIFoLEChuifocuLnwt1WYtK7MBqS9WDlXo_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاوه مدنی: وضعیت دردآور جزیره مارو (شیدور) ملقب به «مالدیو ایران»
🔴
نشت نفت به خلیج فارس پس از حمله به تأسیسات نفتی جزیره لاوان در فروردین ماه عامل این فاجعه بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/120256" target="_blank">📅 21:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120255">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ایلان ماسک : برنامه "اینستاگرام" برای دختراست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/120255" target="_blank">📅 21:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120254">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2c4db2b5.mp4?token=Qp5YACgnCmZn7PyahcbwlyBsS9lTN8oH-nsK_m5G6kigsYXAl4TzVTS-nO6ce8oniNnT-_fszk_ynqzhcsJJVHxlYs2Jqb29EjCGGU_D2bXHH4CchsaoZvhvY1EEmtXYbdm7bNyO1_RjOB0L272UifPsMktFO0p5z6mGGwGgHBIglSrIRu9q_uwoC7s_6s6Cy5fYbl51Mm_5mCEPypPEMZb6k9bJtW36cpAGbweL-z5p4nVYQ_NQkaW6cOXW-3tx9M0TcDmOfdyGptHBzFX988U4_M-VQqVsbi-iCYqRC1okuNobDJlFVGwwRbWkG2rO0dFdTJF08YSDA8HeKVdmBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2c4db2b5.mp4?token=Qp5YACgnCmZn7PyahcbwlyBsS9lTN8oH-nsK_m5G6kigsYXAl4TzVTS-nO6ce8oniNnT-_fszk_ynqzhcsJJVHxlYs2Jqb29EjCGGU_D2bXHH4CchsaoZvhvY1EEmtXYbdm7bNyO1_RjOB0L272UifPsMktFO0p5z6mGGwGgHBIglSrIRu9q_uwoC7s_6s6Cy5fYbl51Mm_5mCEPypPEMZb6k9bJtW36cpAGbweL-z5p4nVYQ_NQkaW6cOXW-3tx9M0TcDmOfdyGptHBzFX988U4_M-VQqVsbi-iCYqRC1okuNobDJlFVGwwRbWkG2rO0dFdTJF08YSDA8HeKVdmBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو کمیسیون انرژی مجلس: دولت به دنبال افزایش قیمت بنزین است؛ مجلس مخالف است و اجازه نخواهد داد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/120254" target="_blank">📅 21:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120253">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
رضا پهلوی: هرکسی که در ایست بازرسی کمک کند و یا برای نهادهای امنیتی خبرچینی کند و یا اموال مصادره شده معترضان را خرید و فروش کند؛ در فردای آزادی مجازات می شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120253" target="_blank">📅 21:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120252">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
عراقچی وارد تهران شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120252" target="_blank">📅 21:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120251">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
رزماری کلانیک عضو ارشد موسسه Defense Priorities: به نظر می‌رسد ادعای مخالفت چین با دریافت عوارض در تنگه هرمز فقط از سوی منابع آمریکایی مطرح شده.
🔴
خود چین چنین چیزی را نگفته است.
🔴
تفاوت بزرگی وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/120251" target="_blank">📅 21:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120250">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJFC4McTt_IDFD31ncEXxO0dYb9KvUOqY8bma0YRgwIUvKAg6mZrxcvkn8CrYrxjx1SpOOaiXtRHYx1wTF9RU1xUAzslAgz1RO7j1-9pSpKQ9orLJ-xOnfM7I73wdRUI0UpO7dL1zb-WST9fys2igCCrUiXUEUuCrWhTsFjdK-454v62kytjaST6WxsCcyMN0oeikkmAhqTLwylxkXJXVDzBhB8bf8fL0TGAAVw8OsKjDAwtkBQKd5GO0TiLRqVaiZelTD_2_7BnwQ25rh5FTtfgRQmLsc5sPwEoRgBZiYlGWzaVOEnTNp9_QqAZLmueK7_u-OZTIdTujRIpvDlK0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چادی هوپان : ما با زحمت و هزار دردسر به قله رسیدیم، نباید بازیچه دلقکان مجازی شویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/120250" target="_blank">📅 21:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120249">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
امارات متحده عربی روز جمعه آنچه را «تلاش برای توجیه حملات  ایران» خواند را غیر قابل قبول دانست. این واکنش پس از آن مطرح شد که تهران این کشور حاشیه خلیج فارس را به ایفای نقشی فعال در جنگ خاورمیانه متهم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/120249" target="_blank">📅 21:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120248">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رئیس جمهوری‌خواه مجلس نمایندگان آمریکا: عملیات «خشم حماسی» آمریکا علیه ایران به پایان رسیده و ایالات متحده هم‌اکنون به دنبال بازگشایی تنگه هرمز است.
🔴
دولت آمریکا در حال حاضر به جای اقدام نظامی، در حال مذاکره با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/120248" target="_blank">📅 21:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120247">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d07cbc7e.mp4?token=bf7o4-lTDk2hi-lJJUZslArbx0VAT3PMME6O64JN3Z-9xvAwk43dhAaDrROvu4jKn8USEmwdQFeaTyPs-fEaPGqzyWOkZM5OEK2ApDgFiB0HtKKPTCR9ifye6KdqG-_oRVaCESsWCFk05vQJL-ZB1JItlCvuccks7FMcarT6nZ3SzrBwwSyR7XqpkKdv73opsIgyt6EEThND5QzR0rqz88jNfpGSaBB4GPaRT7W9rdEVPk_6tsRZsPbtP-ZXvt1ite3odWLrWTGiwtWcjf9Ze5u9GNzqT1LQEj1ke1PPRx0S2gR-yfnl7chB5LEch-vrKk_gKRGH1pczX2Q6HmtAlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d07cbc7e.mp4?token=bf7o4-lTDk2hi-lJJUZslArbx0VAT3PMME6O64JN3Z-9xvAwk43dhAaDrROvu4jKn8USEmwdQFeaTyPs-fEaPGqzyWOkZM5OEK2ApDgFiB0HtKKPTCR9ifye6KdqG-_oRVaCESsWCFk05vQJL-ZB1JItlCvuccks7FMcarT6nZ3SzrBwwSyR7XqpkKdv73opsIgyt6EEThND5QzR0rqz88jNfpGSaBB4GPaRT7W9rdEVPk_6tsRZsPbtP-ZXvt1ite3odWLrWTGiwtWcjf9Ze5u9GNzqT1LQEj1ke1PPRx0S2gR-yfnl7chB5LEch-vrKk_gKRGH1pczX2Q6HmtAlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات به یکی از پایگاه هوای ایران طی جنگ که نشان دهنده انهدام تعدادی از هواگردها درون آشیانه و همچنین هواپیماهای فوکر نیروی دریایی بر روی زمین است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/120247" target="_blank">📅 21:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120245">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsV2oJoPueg0VgyF9VkhBXuwjD9I1mgzeGl6MHx9XAq3OEAhI6UbXqAzEoALuMq-m2FCxIQmtRxHMH0C3KBN_S2nJMPfSVoR6XNpKUY3qsv4hrY5vr6kkUjY3ogDmNVqO0D4TnoMciy8_5e_b3rNwxz4u7E2dA8-SyQnRNtgBQGmzhCGmbOr8KQ7NYiGIPPvVEoK72t_TiA8_MLc9GfLqR8sU7IhQTcDh1DWxh1YbPLlsIZoTT1Z31WyMuoGl2dzKnXp-p9SLwiJ9UDQsqQ3lPD35PwtN4jFUX7RTK1PdTX6tLtlPvM0_yY4THUCFxelciOA4ca68ezEsT_hTRyTjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ab41979c.mp4?token=ntWigK-VJOcs9fWHcCl0RN45uqR1xx_kL-ivMqpLOXBDam3felhruXt5jZqUzcSppFZQeK1Oke43Pl69OFcEjkJMTQRV-FgT1gARUJYp-bcSjF2T39IUCLdMh0eJwdZeKHnGJ70nSgqkaMqlB9CHPsP9rTHlfM7GLqYZ48HnINXT-49VTD1rlKXLDUR5AxDzmtYwTqhgEona1s0CEu1Y2XQYEy_70qhoPIijQMRMO0c-nkLx-BrjayXogcDobjg0x2NO9ll50gjBzCLDJjbf0OojU82bQgTDMVQ9PwvE5FHp5Bv5vCWCnjfQ5LVW3tLHhWQHLg-Eayk2UFnJtY6Vpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ab41979c.mp4?token=ntWigK-VJOcs9fWHcCl0RN45uqR1xx_kL-ivMqpLOXBDam3felhruXt5jZqUzcSppFZQeK1Oke43Pl69OFcEjkJMTQRV-FgT1gARUJYp-bcSjF2T39IUCLdMh0eJwdZeKHnGJ70nSgqkaMqlB9CHPsP9rTHlfM7GLqYZ48HnINXT-49VTD1rlKXLDUR5AxDzmtYwTqhgEona1s0CEu1Y2XQYEy_70qhoPIijQMRMO0c-nkLx-BrjayXogcDobjg0x2NO9ll50gjBzCLDJjbf0OojU82bQgTDMVQ9PwvE5FHp5Bv5vCWCnjfQ5LVW3tLHhWQHLg-Eayk2UFnJtY6Vpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محل ترور عزالدین حداد فرمانده گردان های القسام در شهر غزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/120245" target="_blank">📅 21:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120244">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رضا سپهوند، عضو کمیسیون انرژی مجلس: یه دلیل بمباران جنگ، روزانه ۳۰ میلیون لیتر کمبود بنزین داریم و در کوتاه‌مدت هم امکان افزایش تولید وجود ندارد، راهی جز صرفه جویی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/120244" target="_blank">📅 20:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120243">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFeip4HpWu_4Zot3f6C8jTGHgnyE3BV3tojhcO5TP1BHNsIhg2iFPQ4fjT-yLaPgd9-NeS6CGZ1gEtHgepKUDGaDU0z04kmRiW9UJzQHwkJ3lvrXshI3wK8_qh091ZMbYCRZa71qJeEos-lasiem3FszjXAhYhErVrhWrlXMRL3Mk6_LfyuT3U6YOuqly1eeu5vgT3Bt2rY4KQX8Eafim5Ap0__EUd-fhEWf7soBNJTKyqb5wJ7AUaa85lY8INghAEO6CQ8IEBkKY_etp_-9yvrvDKZRSpYVkKSbSB7zbNDOP64Ursi71J965Wx7vq26vSJ6uEjt6Fy6yah5vI7iPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل : عزالدین الحداد فرمانده گردان‌های القسام، همراه با محافظ‌هاش ترور شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/120243" target="_blank">📅 20:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120242">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
رسانه پخش اسرائیل: تصمیم از سرگیری جنگ در ایران هنوز به رئیس‌جمهور ترامپ بستگی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/120242" target="_blank">📅 20:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120241">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: سیستم امنیتی معتقد است که ترامپ با حمله‌ای محدود به ایران موافقت خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/120241" target="_blank">📅 20:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120240">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
آتش سوزی در تاسیسات گازی در ونزوئلا
🔴
رویترز از آتش‌سوزی در تاسیسات گازی تحت مدیریت شرکت PDVSA در دریاچه «ماراکایبو» در ونزوئلا خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120240" target="_blank">📅 20:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120236">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5Qgrt4nqoe700bm1lQ8vkS-H2HJmU8c_YtUYDMs0r6n1YXDChMtyTlPunB_LCIvMS9IS0i_XVCWc0ycLOfz36-JQe7SQpJc6f-ima4b_Kq8oTuVNA345kiYfmf7mhq8_zn9H3eU9n3-M7BfOIwjNc69fTCe6r7Sc2XO0G1OK8Lp9xLAwQn5pJX7g5UlWgom0-kZfIO_GPJP5ayVg_R_vTKf2Seuh3eSofEA0KAgAWB_YVHFSuIMAGcn7zIGqiySMpS1uCL8lKUD-AJm5zpWZjrl05W2tkgnfI7LXIGJ_dni3lBF656rdf7ZGRnqohqKIakyqsTuThstjwb6Od3RpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5424fe043f.mp4?token=KdBpsx8OQwg6k5tTsL4Iv-0o1mQvwDWSmOgUF2X6X6BszrjGfjUS1OCyCHjeFUXMNw-Wm2mtizBJS_ERA7E8kLd7VbhEsPIbwbQO0XruLBarXWhs18vsUQSZ-1x9_o0w1OSWLTyk4x-OW33f1_6yY33a4yViJBrccPVYdWQ-GL0XMhKfdUWzgtRZ8IpAJTVTnIJ95Bw7JaqkpGyxQT9NGAX2-scd4UP9wb4v5e5syrIB-Hksn_WlRc_DGfng2P5KtqLI25LTQ8cE72N2bFjEe5KsSnmeCvfWvB5FtOLE3LJv7pNIHVl2MGlCQBf1LBLhxTkY7QYWZxJhkMOIp6iKnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5424fe043f.mp4?token=KdBpsx8OQwg6k5tTsL4Iv-0o1mQvwDWSmOgUF2X6X6BszrjGfjUS1OCyCHjeFUXMNw-Wm2mtizBJS_ERA7E8kLd7VbhEsPIbwbQO0XruLBarXWhs18vsUQSZ-1x9_o0w1OSWLTyk4x-OW33f1_6yY33a4yViJBrccPVYdWQ-GL0XMhKfdUWzgtRZ8IpAJTVTnIJ95Bw7JaqkpGyxQT9NGAX2-scd4UP9wb4v5e5syrIB-Hksn_WlRc_DGfng2P5KtqLI25LTQ8cE72N2bFjEe5KsSnmeCvfWvB5FtOLE3LJv7pNIHVl2MGlCQBf1LBLhxTkY7QYWZxJhkMOIp6iKnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چندین حمله هوایی اسرائیل چند لحظه پیش یک آپارتمان در محله ریمال شهر غزه را هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/120236" target="_blank">📅 20:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120235">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
مرکل صدراعظم سابق آلمان: خروج آمریکا از ناتو به ضرر خود آمریکا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/120235" target="_blank">📅 20:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120234">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NatvjDglYvMmArWMLa_Fzae-52Ms3lB_R8TRwcV11bWYMUjraYUCp06QTylnI6wvlU5zltjw_MBVK74ybb_Lwj7-cq-QHcSRN1pnMMy7Q1XrM8j6sjrWlbwknm1CFOqPTmxUDX4KvfGfQ8tcMRSImjhgLbhLtHVjUO18km1cZVq4LH5dcXxIhKBESI1Tp0w0_AdwesACZ26T2lgTVtnZCzO8A4zMhUDV1O_68bNNlwxwQfHNDjX4hqO1zwFItTSs8w1z_TecN4r2o90KyG16mnTLuDCiYeY53F8uPWRdcnBnAVC2nucalokPxqQyyxTzqieueCBah8J_vK0T-KnwwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ چند دقیقه پیش از آلاسکا به سمت واشنگتن پرواز کرد. پس از توقف برای سوخت‌ گیری در انکوریج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/120234" target="_blank">📅 20:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120233">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlJUzKpslg-UyiwPsE2O0eJpDchzhfRLYoyfRfsvnU8lQUJuQH_0eu9EUzMMUfcR1KHSkI5RZ0C_UX5Je3SQIPEKNoA044qS9GTLGVYTGa67QEeLPVBwbiRo1v9dRFOI2y2GVrC3wEhAMR062wDxNCdXZtDpFL_YbP7DxRgl1gJ2e0LI8OeF9rKfxyPqdyjWstdGynnG9OU3AdesOe9xxfyK2ore9V8ceAWj95BYOEzFQQAkw0p1E4nxjLpw6k2DFJ92Itrknq6WlP2cK0-Pm5R7FHEUB4vkG-PgFlUTIJLyTBTFQNF4dJS-nRcEklwhzK0uFFkh54Rt55sxmtCWQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش چشمگیر تولید نفت کشورهای حاشیه خلیج فارس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/120233" target="_blank">📅 20:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120232">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
کانال ۱۲ عبری: حزب‌الله در عرض یک ساعت و نیم، ۱۰ پهپاد به سمت اسرائیل پرتاب کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/120232" target="_blank">📅 20:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120231">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
قیمت جهانی نفت به ۱۰۹ دلار برای هر بشکه رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120231" target="_blank">📅 20:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120230">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
علی واعظ عضو ارشد گروه بین‌المللی بحران به نشریه فایننشال تایمز: ایران با موافقت برای عبور نفتکش‌های چینی، به صورت پیش‌دستانه توانایی ترامپ برای چانه‌زنی با چین بر سر باز کردن تنگه را خنثی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/120230" target="_blank">📅 20:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120229">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
منابع اسرائیلی و آمریکایی به کانال ۱۱ اسرائیل گفته‌اند این کشور در پیامی روشن به واشینگتن خواستار از سرگیری جنگ با تهران شده است.
🔴
براساس این گزارش، یکی از گزینه‌ها انجام حملات محدود و هدفمند علیه تاسیسات سوخت و انرژی ایران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/120229" target="_blank">📅 20:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120228">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سفارت آمریکا در اسرائیل در حال بررسی صدور دستورالعمل برای خروج فوری شهروندان آمریکایی از تل‌آویو است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/120228" target="_blank">📅 20:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120227">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
کی‌سی.سینگ سفیر اسبق هند در امارات، درمورد افشای سفر نتانیاهو به ابوظبی:
🔴
«دولت اسرائیل می‌خواهد مطمئن شود که رئیس‌ امارات، محمد بن زاید (MbZ)، آن‌قدر از نزدیکی و تعامل صمیمانه‌اش با اسرائیل آسیب ببیند که دیگر نتواند با ایران به توافق برسد یا هیچ نقش مستقلی در شورای همکاری خلیج فارس (GCC) ـ جدا از اسرائیل ـ ایفا کند.
🔴
با توجه به اینکه من بن زاید را می‌شناسم، این موضوع برایم ناراحت‌کننده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/120227" target="_blank">📅 20:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120226">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: من تاب‌آوری ایران را دست کم نگرفتم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/120226" target="_blank">📅 19:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120225">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ai5RrcHUGlkkkA_SLAH1zh_wwVUk108NZkIqYF1_7Zh6bVlKk8XnI-NV2Hi6FDf5xN5svCQzPVvp58d4MDZMHg4sPy-9cT7R2kZyPNmmAHBe_2TDPzZpVRZMS690DihOSJ-f5Ke1pEjIVs2_2LdQ7SnNQ8lMIz9PUnNsmydWKEySrOhZ2KNH-gVWbAH-mSsBtW-cZoVcl27Uz3DAoIVGIl1tbhgdCdG03hOi9eT2nuW0TtJptQjI_y4QVE1TQz3_mdx99OQZgB68KInggl54TpQAl0b_Mfb2uWFFLrsVz8YBq3eWep51G6DvfH_6UB1MZjyawduXYaI0dcvqXmf19A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرانسه حضور ناو هواپیمابر شارل دوگل در تنگه هرمز را تکذیب کرد
وزارت نیروهای مسلح فرانسه:
🔴
تحرکات این نا‌و بخشی از یک مأموریت دریایی گسترده‌تر در دریای سرخ و منطقه خلیج عدن است.
🔴
گروه ضربت این ناو به انجام مأموریت‌های مربوط به تضمین آزادی ناوبری در آبراه‌های بین‌المللی، در چارچوب همکاری‌های چندملیتی در منطقه، بدون ورود مستقیم به تنگه هرمز ادامه می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/120225" target="_blank">📅 19:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120224">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سواحل شمال‌غربی زیبای دریاچه ارومیه، امروز ۲۵ اردیبهشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/120224" target="_blank">📅 19:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120223">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
فرمانده سنتکام گزارش‌ها درباره باقی ماندن توان موشکی جمهوری اسلامی را رد کرد
وال استریت ژورنال گزارش داد فرمانده سنتکام ادعاهای منتشرشده درباره باقی ماندن بخش بزرگی از موشک‌ها و پرتابگرهای جمهوری اسلامی را رد کرده است.
پیشتر واشنگتن پست نوشته بود ایران هنوز حدود ۷۵ درصد پرتابگرهای متحرک و حدود ۷۰ درصد ذخایر موشکی پیش از جنگ را در اختیار دارد، اما فرمانده سنتکام این روایت را زیر سوال برده است.
این تناقض مهم است، چون جنگ فقط با موشک و پهپاد ادامه ندارد، با عددسازی و تصویرسازی هم ادامه پیدا میکند. جمهوری اسلامی میخواهد نشان دهد هنوز دست بالا را دارد، اما واشنگتن تلاش میکند بگوید ستون تهدید موشکی تهران ضربه جدی خورده و دیگر مثل قبل قابل اتکا نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/120223" target="_blank">📅 19:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120221">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYtrJoctdIqzETaRWH8BXYpVAvE8u0hJsX15Kku4oQJff9zKVmry7WLfAi2zF6-8gn-_7XhpJvIVB84jrJYtFXBJYC2yqvo3qKixGjwLNUZunZ5PScbRC_BpBjWlW1N4c6lzxONFfXC3aYqLfuMwZewV-kB22rFjNLYoa5bcpgPgz7IVVnMJwfdWGoP7jlLUGVZ8p8-CeIW1kUJCaT03oiRzv1-937uu717IVblBbXzjhXpGTRK9OivFwxIUBMjTGztZAjX34NKPR_207TZroBAVomlv5ryTz_dC_OfHNkB7NjXHS11xRAwFBiZmQT8vQFhi2j2yGuO1v5kCkwAAoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6NyelBWCvvzKW-vMPqLfiGYz69F-xLdnZEU4xTdeSIWOjEXoP0IVcbxi46mGHI93l-uPvQd1vZ0Tl2mwOhhGl9NOls1sgAukHnkK8Z2f6cSncNs787Sai45BjF2ftYYngoS_rkXVeT0Wtk4ZUR3B3Pse7boxnyf9Ybm-aINjdWvoq77uFU6tp4D4UqaTrqW1iwgaGPh8CpBSYEOMLGOqqZyiBfoP8oF4akqFiOr-P_CPCzFXUJK0b4SUybeii_dD3iveI-xzUf7E5QaI26Gbov0ditSUuU7dWrUyuXgbHQK9V1XH6uhBdh1BCU7UBum-y3W44BYHFAEh8577wpmww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله‌های امروزِ ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/120221" target="_blank">📅 18:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120220">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رئیس ستاد کل ارتش اسرائیل هم به امارات سفر مخفیانه داشته
🔴
به گزارش خبرگزاری کان اسرائیل، ایال زمیر، رئیس ستاد کل ارتش اسرائیل، در طول جنگ ایران سفری مخفیانه به امارات متحده عربی داشت و در آنجا با محمد بن زاید آل نهیان، رئیس امارات متحده عربی، گفتگو کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/120220" target="_blank">📅 18:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120219">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
چین از پذیرش دعوت سفر شی به آمریکا خبر داد
🔴
وانگ یی، وزیر خارجه چین اعلام کرد که شی جین‌پینگ رئیس جمهوری چین، دعوت ترامپ برای دیدار از آمریکا را پذیرفته است.
🔴
این دیدار پاییز سال جاری انجام خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/120219" target="_blank">📅 18:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120218">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhCrp38iLpJc_Wygn1mZSk8q7HilgslpFBAOEzDvsIRtg2pn2_qaxhUxEozBk48F5OBY1kFDRcV2hkNQZY2WPSt1Sq1TifnQHTzOuDAwtaQFLpCAP5tnsiqeq9PvgRPjW-uXTfZ2cz4Bz_QQ0oaNgVYlm8fRVPdKHzd_KP29AUBh8EzrCdHhvxPKaTo5ElYWU-xkm8qG9zwPfonYNv4KVo6RuE9BkjRZ9TRntXx3p5kS-p3_e4FVla3y7vSqzeye0mVa0RC3ZR4wc_UZq3cWv_UWZ2KDFx6o9FbR8t70jocXXknUE32ixintImszN8e6DHDKfZj3jVz45JzY8xkXUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
هر صحبت یا مذاکره‌ای باید با اجازه مجلس باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/120218" target="_blank">📅 18:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120217">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
فروش کانفیگ متصل پایدار با ساب و مورد تایید مجموعه الونیوز
⬇️
🔔
@FastProxyMakerBot
🔔
@FastProxyMakerBot
✔️
با خیال راحت و بدون دغدغه خرید کنید</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/120217" target="_blank">📅 18:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120216">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
بلومبرگ: امارات به دنبال پاسخ هماهنگ به ایران بود، اما عربستان و قطر با آن همراهی نکردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/120216" target="_blank">📅 18:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120215">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزیر امور خارجه پاکستان: یازده پاکستانی و ۲۰ ایرانی که در کشتی‌های توقیف شده توسط نیروهای آمریکایی بودند، آزاد شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/120215" target="_blank">📅 18:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120214">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزیر امور خارجه چین: ما خواستار بازگشایی هرچه سریع‌تر تنگه هرمز هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/120214" target="_blank">📅 18:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120213">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزیر خارجه چین : شی جین پینگ پاییز آینده به آمریکا سفر میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/120213" target="_blank">📅 17:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120212">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
وزارت نیروهای مسلح فرانسه: ناو هواپیمابر شارل دوگل در دریای عرب در ماموریتی احتمالی برای بازگرداندن ناوبری در تنگه هرمز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/120212" target="_blank">📅 17:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120211">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزیر امور خارجه چین: ما ایالات متحده و ایران را تشویق می‌کنیم که به حل اختلافات و مناقشات خود از طریق گفتگو ادامه دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/120211" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120210">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
شرکت‌های نفت دولتی هند قیمت بنزین و گازوئیل را بیش از ۳ درصد افزایش دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/120210" target="_blank">📅 17:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120209">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c642ffed33.mp4?token=C3gkCu2vzTs6lW9yaIVOfJiexfxf7_KaQY7RDgdM0gcbakQ1J6f5vYUDhqdUjtIz9j6yM26GD0uOkIMzhlitDX4DmDjRL2omoAAl-Dj8SJAuyto-UFGiMTBdfRkKiOCU1w-HxTz8NJC93Qxs0wwlVzTbGeP9Fo_V01sdTYaJl5lnSyANwFrcM3bNoad0rtPH_Y-rQWmS26w4lbEP9jS85yaRjmlE0rS4PoFqyjGP9DODdn1BfEESlbl8xhp2X86rJrpWE9XIZCoc9cI3PSui2K7swRVnowQjyL3MzEYxGCd1QNCiZkIpMR5X6xHxJ96zNDLj6IOU1GyIaZc6O9wjxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c642ffed33.mp4?token=C3gkCu2vzTs6lW9yaIVOfJiexfxf7_KaQY7RDgdM0gcbakQ1J6f5vYUDhqdUjtIz9j6yM26GD0uOkIMzhlitDX4DmDjRL2omoAAl-Dj8SJAuyto-UFGiMTBdfRkKiOCU1w-HxTz8NJC93Qxs0wwlVzTbGeP9Fo_V01sdTYaJl5lnSyANwFrcM3bNoad0rtPH_Y-rQWmS26w4lbEP9jS85yaRjmlE0rS4PoFqyjGP9DODdn1BfEESlbl8xhp2X86rJrpWE9XIZCoc9cI3PSui2K7swRVnowQjyL3MzEYxGCd1QNCiZkIpMR5X6xHxJ96zNDLj6IOU1GyIaZc6O9wjxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر انرژی آمریکا : قبل از اینکه تصمیم بگیریم برنامه هسته‌ای ایران رو خلع سلاح کنیم، قیمت نفت و گازوئیل تو کالیفرنیا رسماً ترکونده بود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120209" target="_blank">📅 17:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120208">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bea015880.mp4?token=q3QvSsHkf4am2Al49lThT4vbnX55YjlboknFcZvQNmQ3Hn54rshit2ZohoMw01l46r47y4iAecYswJ_W_7dHV_6_4pi4845mnHVqDrsZ7O_u6KMzqZIyNlvwVYwHeQdfsBNZwozRZ8n2UxvV2HQikfDIT4mpt4Vx5OBTzc3cY169tbACYSZmCBgmo15LRhnpbahyvKND-8XdFlTtQjL9Ti4AqI26ckgX1zcg8PFqVSCbboekBifvFnazcAEAaWp1E591M464Q1h5XsJQDlghn2AYEeKfOgKANJPsVbcAZD7K65ywhbGgpTr9Y4LCUofD43nPbXE7HUO8KJahI0zTeQOXfx2dbR8jnIEb81os_56V1AYlXfzwg-6pCuE4dA2KVu33MIZ8x0lajf_a3ZF-DfI1rjVGDkc1UCBLPlsSXp56hDUnyKZelcK0djgjmbEWL9XqhlHgBP3HXZBOffHZBzSelfsIdrchXlCydIwnADqxODFXVKzl0ShdCv75y0xLA8uDjaR-WYSvOH17086ZETF7oMhKXdeuSsrxae-SbwCV_XAP4mo0grHohCtsFXKn7VhqK6qLJicB_cND-5arx4qzZ08PZ35dL85youPaVzW5AjjZdRzC7Vq24M48zkVBP4W-e-bP_4RLgyvXQx65nlchvyiZq3F-HqF61dpr1w0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bea015880.mp4?token=q3QvSsHkf4am2Al49lThT4vbnX55YjlboknFcZvQNmQ3Hn54rshit2ZohoMw01l46r47y4iAecYswJ_W_7dHV_6_4pi4845mnHVqDrsZ7O_u6KMzqZIyNlvwVYwHeQdfsBNZwozRZ8n2UxvV2HQikfDIT4mpt4Vx5OBTzc3cY169tbACYSZmCBgmo15LRhnpbahyvKND-8XdFlTtQjL9Ti4AqI26ckgX1zcg8PFqVSCbboekBifvFnazcAEAaWp1E591M464Q1h5XsJQDlghn2AYEeKfOgKANJPsVbcAZD7K65ywhbGgpTr9Y4LCUofD43nPbXE7HUO8KJahI0zTeQOXfx2dbR8jnIEb81os_56V1AYlXfzwg-6pCuE4dA2KVu33MIZ8x0lajf_a3ZF-DfI1rjVGDkc1UCBLPlsSXp56hDUnyKZelcK0djgjmbEWL9XqhlHgBP3HXZBOffHZBzSelfsIdrchXlCydIwnADqxODFXVKzl0ShdCv75y0xLA8uDjaR-WYSvOH17086ZETF7oMhKXdeuSsrxae-SbwCV_XAP4mo0grHohCtsFXKn7VhqK6qLJicB_cND-5arx4qzZ08PZ35dL85youPaVzW5AjjZdRzC7Vq24M48zkVBP4W-e-bP_4RLgyvXQx65nlchvyiZq3F-HqF61dpr1w0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه حمله هدفمند با پهپاد FPV به خودروی سازمان ملل تو اوکراین رو منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/120208" target="_blank">📅 17:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120207">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrmeUgwNbhcYZiHCHh5EW2_Mb5yPZFogWq4-p8ZlRRqjbqXjPuVF8B811W-zEJftvctcZC1wZEpVSMQOQ-OatlpbpxATRcL27-7_nI7oWCEJTLKp16Q_S8A_vsfRhQfq0DnL9bncROmqXPJjOGkkV1S17ElHhvoDyejX4Qr3ssAYDSwYKibWYFmzdKkJmg13SQhyGbAXXZ4tQ8QFI24W0KOootNqX-4Dcw4t1PXEbeyiLfaP2zBWiTf9UKbn3lBOofDYErkjMlnDTxWPBu7W2BDkAOluKxg99Z1l7uYmAO6m_BKo6ZHYR7C1sFAmOMgUIrdMRBb_xC3--FGrxt0DXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میدل‌ایست‌ای: ایران دنبال دور زدن مسیر محاصره شده تنگه هرمز با کریدور زمینی پاکستان است
🔴
در پی محاصره دریایی ایران توسط آمریکا که وارد پنجمین هفته خود شده است، ایران و پاکستان اعلام کردند که به دنبال احیای پروژه‌ اتصال چندین کریدور هستند که بنادر کراچی، بندر قاسم و گوادر پاکستان را از طریق بلوچستان به گذرگاه‌های مرزی گبد و تفتان ایران متصل می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/120207" target="_blank">📅 17:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120206">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40a2b1c26e.mp4?token=B8eWY_gWvOLMLwMZlBoZrAgtYutgI886znlCciNfjUKMjI482tRn9irfuCNLAikuU70xaL6pDLDmtRuuTgQk6WjdY-pyhDT8VM8mVTV4wtMD30jrggHAu7EOwbMwtdBXfVggYJxvUjTD0deaDEgGTXVrTcRMcIsMP0vK0tpuuf_EWFqGCWf6dElkOFbHWmZb1yeo4yiQsKfWe9wHMvB4XCEdOglIyjKUXozZh1TvBAszkxwpWSAlFmoooAr1r8aINBf26M7OFN370aqC27ZJ4LmePbV6i5qdi40VqUmx0lRT5qf-MyzaRCVUNKTg5dEn8Fsce_o9I3Iko2rwEJCg3DquDybdE3F_hYV6EydTCysOs8d-84dQGPtsOicS6001gcqFwW1VAe1ahCVZdZtocTkIJwCRKYSluL1yNUXId4l7X6kUIiJNoms44yfTkSVVZ4FnzUNPgQWAA_Tnp3mqioFb4bfK7uO0cEGEG0PLrKLumSQF6X4vQWgzxpo8DKGMwXDLIqlHCO-2mfwghVRlStVEb_nqzEMg8TkT2LLqLcQSNpJ8XTStYo4Pj_dnr7NMgyMtZeRY98HTwQ0b3SuzI0lR8o3YmAkIy3Hx4SoxkOS6fZvp9dHPKUJvBZGncCEhq7Y7HKEyItw6_gHoY-deB5SJbqIeSDXpSzmoyj46AaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40a2b1c26e.mp4?token=B8eWY_gWvOLMLwMZlBoZrAgtYutgI886znlCciNfjUKMjI482tRn9irfuCNLAikuU70xaL6pDLDmtRuuTgQk6WjdY-pyhDT8VM8mVTV4wtMD30jrggHAu7EOwbMwtdBXfVggYJxvUjTD0deaDEgGTXVrTcRMcIsMP0vK0tpuuf_EWFqGCWf6dElkOFbHWmZb1yeo4yiQsKfWe9wHMvB4XCEdOglIyjKUXozZh1TvBAszkxwpWSAlFmoooAr1r8aINBf26M7OFN370aqC27ZJ4LmePbV6i5qdi40VqUmx0lRT5qf-MyzaRCVUNKTg5dEn8Fsce_o9I3Iko2rwEJCg3DquDybdE3F_hYV6EydTCysOs8d-84dQGPtsOicS6001gcqFwW1VAe1ahCVZdZtocTkIJwCRKYSluL1yNUXId4l7X6kUIiJNoms44yfTkSVVZ4FnzUNPgQWAA_Tnp3mqioFb4bfK7uO0cEGEG0PLrKLumSQF6X4vQWgzxpo8DKGMwXDLIqlHCO-2mfwghVRlStVEb_nqzEMg8TkT2LLqLcQSNpJ8XTStYo4Pj_dnr7NMgyMtZeRY98HTwQ0b3SuzI0lR8o3YmAkIy3Hx4SoxkOS6fZvp9dHPKUJvBZGncCEhq7Y7HKEyItw6_gHoY-deB5SJbqIeSDXpSzmoyj46AaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل یک تمرین نظامی غافلگیرکننده در امتداد مرز اردن انجام دادند که هدف آن آزمایش آمادگی برای تهدیدات ناگهانی امنیتی بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/120206" target="_blank">📅 17:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120205">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyjhJiWR1suPzOM84fi8CYjSIrKtF7SJ_NqIymjep2p0jDyA7dSNJ3XXur4ee6Xk9mCk84Cxt9Zwaa70IP_FDTN0jJbJXU18pXBWHK4Mhk7UZaWTvYja7oIX7cBR8K3x1jIEEACM2Lnj-95QWJHYHk3Hl6jyndSAW98FpQtIQ-1XgHh_IGowE3nLyLYzkJMd4tg243PSBz1DGN7qZ2ngdJoz8KdmV1ViCbdUcnGPGJzF33V4BTN_ZJiYWGtAHVM4AlAVgiCAKb0gVkfIG33Nhtju6UsIndX9A7ouyHmQsJmGfDLgq-gd1NXCuaJ4NSnL8yxCKzMuUS-7YGlEr5XHBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدر اعظم آلمان: تماس خوبی با ترامپ داشتم!
🔴
ایران باید پای میز مذاکره بیاید و تنگه را باز کند، باید از دستیابی ایران به سلاح هسته‌ای جلوگیری شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/120205" target="_blank">📅 17:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120204">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رویترز: امارات هم مانند عربستان به دنبال احداث مسیر دور زدن تنگه هرمز است
🔴
امارات ساخت یک خط لوله نفت جدید را برای دو برابر کردن ظرفیت صادرات خود از طریق فجیره تسریع خواهد کرد تا توانایی‌اش را برای دور زدن تنگه هرمز به طور قابل توجهی گسترش دهد.
🔴
ولیعهد ابوظبی اعلام کرده که این خط لوله در حال ساخت است و انتظار می‌رود در سال ۲۰۲۷ عملیاتی شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/120204" target="_blank">📅 17:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120203">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نیویورک تایمز: سفر ترامپ به چین در ظاهر دوستانه بود، اما پشت پرده تنش‌های شدیدی بین واشنگتن و پکن جریان داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/120203" target="_blank">📅 17:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120202">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: تا امروز، ۷۵ کشتی تجاری تغییر مسیر داده‌اند و ۴ کشتی غیرفعال شده‌اند تا اطمینان حاصل شود که قوانین رعایت می‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120202" target="_blank">📅 17:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120200">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd1a2c0e0.mp4?token=KUWORDbwYLIyiBQIlPehOnm7FJ6sRaVPeoc4sLvMpBMKcI8TDoIFhrYpCFmk5lkhxjVzbBELF3Rq7qt21Ob87HH7A6ySZwnhsfAZo7VuMLnU0E5KUI9UWSQJq1U1VDR-YWrKmSPIkTeDsN93TC5OOsUgWcupglHZybZCi14xnvi92fniECkK0gn4SEv86RkmPPo7YDN62eOky_S41WUPlzSNu9n0KtLEam8x4Rt5eamWJPsixiGixQ0t9JGRX4XwYhCWcuP8_hepJ6XlGchkaqrM3ckKscdQZKb_4xeQrtdANvpuaxpCe14u6hNlrcwWjp6SRvauQm5sxIRwGNcerA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd1a2c0e0.mp4?token=KUWORDbwYLIyiBQIlPehOnm7FJ6sRaVPeoc4sLvMpBMKcI8TDoIFhrYpCFmk5lkhxjVzbBELF3Rq7qt21Ob87HH7A6ySZwnhsfAZo7VuMLnU0E5KUI9UWSQJq1U1VDR-YWrKmSPIkTeDsN93TC5OOsUgWcupglHZybZCi14xnvi92fniECkK0gn4SEv86RkmPPo7YDN62eOky_S41WUPlzSNu9n0KtLEam8x4Rt5eamWJPsixiGixQ0t9JGRX4XwYhCWcuP8_hepJ6XlGchkaqrM3ckKscdQZKb_4xeQrtdANvpuaxpCe14u6hNlrcwWjp6SRvauQm5sxIRwGNcerA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حداقل سه پهپاد شاهد-۱۳۶ ایرانی امروز اوایل روز به سایت‌های متعلق به گروه مخالف حزب دموکرات کردستان ایران در شمال اربیل در کردستان عراق حمله کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/120200" target="_blank">📅 17:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120199">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: در صورت حصول توافق با ایران، آزادی دریانوردی می‌تواند با سرعت نسبی به تنگه هرمز بازگردد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/120199" target="_blank">📅 16:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120198">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c1130ab0.mp4?token=TWAy6rkGV9_TvpN11P-q_QPe8IPZ1_O9pemTF4ccFm_kpQBgbKXBLoPVyVCUUtj0yxFiQ7bFhN3Gnd4hFx995mmZaxiCoOw9hWyYRUJKngUtU3_bCypE0ZXCBKB5OvVy0ibAANYg3HlW7SMXSgemU29_uaWzbQNFwi5tY2jurGeaB3J_hNcNcennu1UgDRIhIIV0HObYNtDlzAgW9esv13lHj1lq0XCCyvYissZbzbAsuWxw97n5RuWIK0H-_YbH8A7qFI0Jl11YieVSNWusbTYWTH5xK1-L5MTR5mGT_bJQ4cIiN4D0NtoVkyO8rcuWJbf34tn3m67TnrHOQXZ12w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c1130ab0.mp4?token=TWAy6rkGV9_TvpN11P-q_QPe8IPZ1_O9pemTF4ccFm_kpQBgbKXBLoPVyVCUUtj0yxFiQ7bFhN3Gnd4hFx995mmZaxiCoOw9hWyYRUJKngUtU3_bCypE0ZXCBKB5OvVy0ibAANYg3HlW7SMXSgemU29_uaWzbQNFwi5tY2jurGeaB3J_hNcNcennu1UgDRIhIIV0HObYNtDlzAgW9esv13lHj1lq0XCCyvYissZbzbAsuWxw97n5RuWIK0H-_YbH8A7qFI0Jl11YieVSNWusbTYWTH5xK1-L5MTR5mGT_bJQ4cIiN4D0NtoVkyO8rcuWJbf34tn3m67TnrHOQXZ12w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بازید رئیس ستاد کل ارتش اسرائیل ایال‌ ضمیر از مرز "اردن"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120198" target="_blank">📅 16:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120197">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
العربی الجدید: ایالات متحده شرایط سختی را بر نخست‌وزیر منتخب عراق، علی الزیدی، تحمیل می‌کند و خواستار خلع سلاح گروه‌های مسلح، انحلال شبه‌نظامیان مرتبط با ایران و پیگرد قانونی افراد دخیل در حملات به سفارت آمریکا است.
🔴
واشنگتن تهدید به تحریم کرده است اگر خواسته‌هایش برآورده نشود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120197" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120196">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
الجزیره: هیئت‌های لبنان و اسرائیل به مقر وزارت امور خارجه آمریکا رسیدند
🔴
هیئت‌های لبنان و اسرائیل برای شرکت در دومین روز از مذاکرات بین خود، به مقر وزارت امور خارجه آمریکا رسیدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/120196" target="_blank">📅 16:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120195">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزیر انرژی آمریکا، کریس رایت : تصمیم درباره تنگه هرمز تو دستِ ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120195" target="_blank">📅 16:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120194">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
تصمیم ناگهانی وزیر جنگ، پیت هگستث، برای لغو استقرار برنامه‌ریزی‌شده ۴۰۰۰ سرباز آمریکایی در لهستان، مقامات پنتاگون و متحدان ناتو را غافلگیر کرد و باعث سردرگمی و مشورت‌های فوری بین مقامات آمریکایی و اروپایی شد، طبق گزارش POLITICO.
🔴
«ما هیچ اطلاعی از این تصمیم نداشتیم»، یک مقام آمریکایی گفت، در حالی که مقامات در هر دو سوی اقیانوس اطلس تلاش می‌کردند ارزیابی کنند آیا تغییرات نظامی غیرمنتظره دیگری ممکن است دنبال شود یا خیر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/120194" target="_blank">📅 16:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120193">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
رویترز: قیمت نفت روز جمعه با افزایش رو‌به رو شد و شاخص‌های سهام در اروپا و ژاپن کاهش یافت.
🔴
تا ساعت 09:25 به وقت گرینویچ، قیمت نفت خام برنت با 3.47 دلار یا 3.3 درصد افزایش به 109.19 دلار در هر بشکه رسید
🔴
قیمت نفت خام وست تگزاس اینترمدیت آمریکا با 3.72 دلار یا 3.7 درصد افزایش به 104.89 دلار در هر بشکه رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/120193" target="_blank">📅 16:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120192">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وزیر قطع ارتباطات: بسته حمایتی برای کمک به شرکت‌های آسیب دیده از محدودیت اینترنت طراحی می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/120192" target="_blank">📅 16:28 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
