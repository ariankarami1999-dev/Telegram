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
<img src="https://cdn4.telesco.pe/file/ptBShGFRi0UIXwwbdd_hUY48Ph30WOmpWBSHiu3f4jxbcQLMH4DlLtYZKbpejm1Sk-5I6ZqbtCQ23reWQwAl3NOdR642i3VnDTfYOVryr5PYP1E130DitS6x7PjZMdlou_ySGJ-2QYAa3AKJxy6OmhUvhBsrUzbufTk70umJ9uDf-zIop-HwsvOu6iFMQEFutmWHcHbHEZu5del1bl2DG8qcsWl5dQr0q0r0wgWK_2DEL0kbXPZaFYd0SaBwod5HC0laoOZxhbsVFD9nORZ-Z2xciPFvnZYUgF2uRtttjyk4ibjBhlep4Fc67pQNdVv2aL5jxDrxpgTshHx4aCMGLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 525K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 03:06:01</div>
<hr>

<div class="tg-post" id="msg-29645">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLiqUl8e0VE7_meqnf-U0GO39UY8mmxe_n5o39gKyRkPUhCUO9fPfrLV-2HKgy92CeCxJQ49A22NaPOkRrP3LL_3RZ1xi5AZKPY6TK6eCPbbCXIdIvcUkWe2Ig5tN7zaBdy-i2TwQkm5K1r2kFexZ_mO10p_Sha-WmunAodeZUloH2Ru_eNJJ4ZTQ0DKwJdQlGeGdMP1ow2Y_FxGWk-hsvgKehIgki5Yi31XfaqRuVta9EHMcWZoPCkEwbeDvbVy4Vux-BjpPkp3LD2rlRMc6-iWPqFVdLOnpJmwSKy9HNyS5Gg8NyPUS9vnoQE3bWMTAWx14gtCMvSqSdPDRYATJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مصاحبه جالب و عجیب و غریب مایکل اولیسه ستاره فرانسوی بایرن مونیخ در پایان بازی دیشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/29645" target="_blank">📅 01:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29644">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔵
ستاره جدید الهلال افتضاح هفته‌قبل رو جبران کردند؛ الهلال امشب با درخشش ستاره‌های تازه وارد خود 6بر0 التعاون‌ رو شکست دادند. گابریل مارتینلی ستاره گرانقیمت و تازه‌واردآبی‌های ریاض دراین بازی موفق به کسب هتریک شد و واتکینز دیگر ستاره این تیم دو گل و یک پاس…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/29644" target="_blank">📅 01:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29642">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWR1ezl5azbA0IUEepBQbb5pc3OnilQYM6c0RS03QaOg73RwPGSUt04PJ4Hd7Rl23qVHWK2CMPR8hnQkzXM55qR_3MJ5Gt2Ac1X4Gqc76_uPIGQ21KRQMPNqJq7I5lMZvrS3j3l--GhycU0jPliMiX_6l4P8c8wtgi-4tJdEzGl5iZdWeLonHdP-MhP4Ifi-XmLpcl7jmislE-LfcNOVHVIzhxweoeCBR81lbRU0MiS5mHmvNArkY-XfiXfeys60k4onq4LrUznWXq2BuSFkVM_BXcn9EdCkga9urAlq2EqGOmub9CFDOCHu1w1CCS-5sVW6CghTrmWMjxkv2oFDHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛از دربی‌جذاب‌شهر منچستر تا بازی بارسا بالوانته‌برای‌تثبیت صدرنشینی در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/29642" target="_blank">📅 01:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29641">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROyy_grIL_iwd-ylw80wB4_JG9pyqu911iALxzTC7a5OhXrQ_VXCOGUuiofN77zBnwIX0h22Iz5lI0IhmagbBDw5zKJWrNLWdY7dnPmKG-RNAPYr-Q7mdoSSEPJHkwMdbpslrMaHXloA64okVOSLjW_ZWzZUpm-9oz1BDpFvHbztj63zMNCvmLrM9-jBzzJIPf1hRUvdddoRztd-P-bvuTymTwFQkUmGmMxicJhCe5YU7Y5djBNMqj3EG-bNKYcX1XwKYKd_8lNAPeaYgMhrdNdXaM8uXviCxvVzbQOJkWSSnFCgHzsmMj0EBPEod74I-uBKvqZm8a2AqOIPXGhNyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف همزمان لیورپول، چلسی و تاتنهام در لیگ‌جزیره تا برتری پرگل شاگردان خوزه مورینیو در شب درخشش کیلیان امباپه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/29641" target="_blank">📅 01:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29640">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAeVLoDSthGFKMUNI4dK2HoR7iHXg-6GoBQGU40hLYoR2LpzkZ3lORSda77_DBD4E-i9WLU172spDLAD-OyY7JTOAbxR2SDbvi5_zm2F4JPKT1pBYrloBrTFKGBKRDj4AJgMIm5lwlsedJQXIIZ_o9HIeBvG4lRJcRsmvHg0sjGPtK71bswZs6lO32PbXzfROcHnh_vnmD15SraJjCCq0EzgyqfHEgMwtYqSti4f4w9SO_kJH5LyaEoKWVz0PMUDS8tbUJBMQj7uo6yjpg5mcpPokgPXD7rjlHOIP2MwKNeQiKE4Vdt6sQmw4j2w-nxr6w1V42QPx-3vQNLRidI4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
دوستان خودرابه پین باهیس دعوت کنید
و
🤩
🤩
🤩
واریزی دوست دعوت شده را پاداش بگیرید
💥
برای دریافت این پاداش بعداز اولین واریز دوست خود به پشتیبانی سایت مراجعه کنیدوبراساس مبلغ واریزی
🤩
بونوس
🤩
فری اسپین
🤩
دریافت کنید
.
🎉
جوایز دعوت دوست
🤩
⭐️
🤩
🤩
🤩
هزار تومان به بالا 50% بونوس رایگان
🤩
30 عدد فری اسپین
⭐️
🤩
میلیون تومان به بالا 70% بونوس رایگان
🤩
45 عددفری اسپین
⭐️
🤩
میلیون تومان به بالا 80% بونوس رایگان
🤩
50 عددفری اسپین
💥
با پین باهیس همیشه راهی برای برد هست
🙂
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
p21
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/29640" target="_blank">📅 01:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29639">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJKc20Lx7O5GCX1PGycQoHHc7V0w7irI8H8zb-I6OCSAjy7GqZnXFIm0yTzJApMkoGMxIsrOv_qqxlci-yJB-qtDL14jU2bLSVoBp4H4p2bu0rzOBouzTvOZvxIruYBVjr7TJxVbT6C1p-eLcP3dds38AxdgXyZTY-OYHl7IXly5DcVfg1g4nPd0BK71m1CDv5MxTEad0mqkjKk-75h-fce-X4T8Lcn_wPH1QvX2CclvHSW-IvAyapVH7Q9mjnCo-BfDAgmavGtZMrHj6L9n3VqdRk2-Mpu9eryvprwYh8BCdWyd_6Bn3Z6rrPDYDR_rXwkPCuxaUHCWTYZHaA0t4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
تصویری‌زیبامریم‌میرزاخانی‌ریاضی‌دان ایرانی و استاد دانشگاه‌استنفورد روی‌جلدکتاب ریاضی دانش آموزان ایتالیایی؛ روحش شاد و یادش گرامی.
🖤
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/29639" target="_blank">📅 00:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29638">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02bd31b46f.mp4?token=YnnSDhRCydSfDv0QbA31wwyHgG-NKj2OZGSDl_AXDi5oV6-8Xn0v-Pc9OlLTykZKibbr0TTz3NhZUElFiXAKeM2QQK5k7-7nzjQbCamUrn5GDGWqolAzrmIsqAJYQ7sFPAFkaW_vSz7ZZo2Xb1Ft1t0ZaZvu7E12sQ2pHC-liNueu9nxMVMUZf1beeDmUYpiWq-Gnk53VV0DTWRUb5x2r1Z7izVf0eCAMxrp6UCgzgIhZ6WQP7mikSoi2WYmwI0UFJ2_eFdK0ZdsA736aNsA4VEl0X5y4K6Usly1SfSAY6k-ilHpKML3boALFwd6a9ftBUIs6CVDj7c7IPTEVvB-xLoTqTvl37svD3uR7VFAndKQuXCuGEptj3coXOoQ9xUhPkC76wc46lG28YyWMCZpa6eoPuZijZvJwlqA-brEBR3Hvny2vKydAAWLCV60UibQfDVl-wpDfPFrqvDG4ndDV5ZaydLvg6HzG-0mY70vpqVJNAAK136rQMIkEiYXrb3CEeSS89boTvwLh8Il3bzrp5xG7scvKEpCyL-Q8qafwOS2aUFTBc0bLr79lxBNJ4vhfST0AGm34hskPn5NrinhFNV_FknR1gTPMzVSda_RIvF9ZZB1aSDyoDrNsTCvILyUIJY9HYPmiLh1Ovr4SULdEc_wCGf9oHn9A2TE7zW4IxY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02bd31b46f.mp4?token=YnnSDhRCydSfDv0QbA31wwyHgG-NKj2OZGSDl_AXDi5oV6-8Xn0v-Pc9OlLTykZKibbr0TTz3NhZUElFiXAKeM2QQK5k7-7nzjQbCamUrn5GDGWqolAzrmIsqAJYQ7sFPAFkaW_vSz7ZZo2Xb1Ft1t0ZaZvu7E12sQ2pHC-liNueu9nxMVMUZf1beeDmUYpiWq-Gnk53VV0DTWRUb5x2r1Z7izVf0eCAMxrp6UCgzgIhZ6WQP7mikSoi2WYmwI0UFJ2_eFdK0ZdsA736aNsA4VEl0X5y4K6Usly1SfSAY6k-ilHpKML3boALFwd6a9ftBUIs6CVDj7c7IPTEVvB-xLoTqTvl37svD3uR7VFAndKQuXCuGEptj3coXOoQ9xUhPkC76wc46lG28YyWMCZpa6eoPuZijZvJwlqA-brEBR3Hvny2vKydAAWLCV60UibQfDVl-wpDfPFrqvDG4ndDV5ZaydLvg6HzG-0mY70vpqVJNAAK136rQMIkEiYXrb3CEeSS89boTvwLh8Il3bzrp5xG7scvKEpCyL-Q8qafwOS2aUFTBc0bLr79lxBNJ4vhfST0AGm34hskPn5NrinhFNV_FknR1gTPMzVSda_RIvF9ZZB1aSDyoDrNsTCvILyUIJY9HYPmiLh1Ovr4SULdEc_wCGf9oHn9A2TE7zW4IxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛ از جدال توپچی‌ها با یاران گرانیت‌ژاکا تانبرد رئال‌مادرید با رایو وایکانو در خانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/persiana_Soccer/29638" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29637">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TswQVneMtTudrcKXM5N9OVvXUoarEKFK2xPp44_dD3iVWPdY8-dVYtNj2foprWDSCnncrBHizUN8R84KNDbGHCEINosLpN2rNMd8xRoOgfLvjMxec3DM-c6r4NvGdPJlrwJmuDvvZ7rxNGLHuLA2LUhia5x-2m86jtvCBpNyJriMq0GBpMOphkF-mwk-t8BuVl7iNu_6qAsOycdBrBWz85j-z0sPlleRVJok4gvyU9Wt6R0Btqxpbm9_FP-QNBw6Jr7gDz4Z8oVo8skz06rL9xI8rDUVcj4QHgO3wavqRqPW2wUinOD19v9lCN2l6eLY_ukFDkpqV2rKWVclCMn_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/29637" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29636">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EliCtPb4gwaQAmxBRED7SGgit58NBu_41NYR7ylauDVWJ7cnwI4YFP-qaGU4jHNrFh83JXAWPRZc-sfZszDeCX5ks2gXdVpPiVyRgmC6qE0E0eKAzsAarGTvA-miolKpT8HxsdID_vnUksyp_54BpVj_0F-fBp9_HRrhVnw5QZoj9ymZHYD9Z73uhHXSsBCPldbGPNbIRWM7SDp-PX5p3pSL9OmcAz1FyAQQgAIUlT8OkTOyHnJq796hjeiDvlbNnqaKH5a2U9iHnvziQZ1jwZcc_DRnT8-YQG6I3sbWEfDf9MsRQncfT0uUP7d1YBFSfEFkwtETqFsyksMGXaKPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
حضورپارتنر وینیسیوس‌جونیور در ورزشگاه سانتیاگو برنابئو در بازی امشب رئال مادرید مقابل رایووایکانو؛ نیمه اول رئال سه هیچ بازی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/29636" target="_blank">📅 00:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29635">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCGr8jKIpBx575rtHIvYT9YQ1pgesv-UTJJeHkPk9upxmAkRvCT49n5t9wo67tbEcRS4S_tPf4VzYm8fGwQzqoHiSZqhQ-zU-t-mYFY-tZb-dPgcHp0SLzZNDDRRzjlHR9gXOWmVc7EARxVTcYM-dgS-8eH5aBDTNJfPuOqE5Cwl4ZbGlzKmFaPo9cuLMsN8ADPh3duVzQ4drcwfTDYSrTIbInZsvIe2S6rcOsxZsYHNI465rLeO0M48DHk3d019DU3Ljwi5bdQY7a9h87M44SdySWLyzEt3EHbbm_-1-O5HGGPn9yrMU_XL0OrWvFw6aFUVYQxkU6xokLapDOsetQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تایید شد؛ بااعلام‌رسمی باشگاه استقلال و با موافقت سهراب بختیتاری زاده صالح حردانی مدافع راست‌آبی‌ها به‌تمرینات‌ این‌تیم برگشت و در بازی روز دوشنبه با السد در لیست آبی‌‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/29635" target="_blank">📅 00:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29633">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjia5uq-MhhS4ftW87KkhZ74bMmfzDC_efNZtJ8U-NSodqyq7y3gVm2Wy-SCtdg3G0V9FJoDLJQjjDA38pdgpEp8XeFZZSBiW5n6zmX1jfNvXqKBg39anddg3UjKexgB5VslW-ANfxzmYT3JqRTjUFb18fk3X0-N_PCLXye7INkqvLCaLQ_nwBBGMmWEk63rNIxz7Yox5p8x1vXiHjagv_AmBsGz-cvMZ-PBfHeWin2ov0yQiMtPuB4VWq4IR91KSA4ovF3DhN8gDbt9Ccih_VFKUsOoHlHG6xuLGSZcoh56wffgZ96AAoQYvbEUzuFYE1huxUq8cnYvx4dgq6RxZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛قیمت‌پلی‌استیشن 5 پرو دربازار به 310 میلیون تومان رسید. بهمن ماه 45 میلیون تومان بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/29633" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29632">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdKM9QU9ZxmBA2W1dmAnFUwXYRlKK62vRPbZQH9y8zGG36_WYjvacURzJRJm-Kw-mhjgm9LRNo-UXIu8cQiXl6AIWECIqqcUPb4QuQuGv3aGloItjqx82TpHI4s6PvWNu0lmdboUaNuSXjOx-veyedDPWaWoRpvBnzn7VueU20oeL9ZuZgmAVCFiQBys_dylpirt_z3XPM2XzrMPtbfEiYXoeVBVuSwiukAsIqlnMz-HTUAAAftX2RCYWUXhD1KpUEZ67FsOOkpKOImyXNekkNvKaZFcbCilqYJrot7eaYDlDVnEkzJk3BGrY4lBe9cLWBe_B-m-IDxikdZRIeJaIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بااعلام فابریزیو رومانو؛ مارسلو بروزویچ ستاره کروات سابق النصر با عقدقراردادی دو ساله به ارزش 12 میلیون‌یورو دستمزدخالص به السد قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/29632" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29631">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKYotUMAuukXjsXYc0KcTIcodDMywiRbJ5DdsX9zgzf51v04vI8P4Xgb9PhI3N6Oiyrg40cJDcdLnTzKDibEc3AsvknNOyQ3ezyDj5l1WyOCAs23lkTQzhl-nfkRdIn8Gu05qZF5QnXPLaBNwgMOgYus5WPl0pwdzBknRHrJf5BzCYZVNdyTijv99rofZyj3s3aaGPiRHy-yNMU7AdBTZEplOmWhCAUbN4l7af9jZkU1otRS3ZYKiuksMyMmy0mW5s0CzB_uj4NOoUTEwWkDym6o1uyfIIpAs_GKA5FUkE1c_cIzcfvgrCvSDSWMvKi44_DY02jTVlEuAmUxLlWG2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زگیل و تبخال تناسلی درمان شد
‼️
ویروس‌خطرناک‌‌که اگر درمان نشه تا آخر عمر داخل بدن ماندگاره و عوارضی مثل سرطان ایجاد میکنه این ویروس
❌
HPV یا زگیل نامیده شده.
⭕
درمان کامل زگیل و تبخال تناسلی :
1️⃣
زگیل تناسلی
2️⃣
تبخال تناسلی
☑️
زیر نظر سازمان غذا و دارو
☑️
بیش از صدها رضایت درمان و آزمایش منفی
⚕️ آیدی  :
🆔
@hpv_help7
⚕️ لینک کانال کلینیک
🩺
@hpv_hsv_clinic
📞
09212046421</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/29631" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29630">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOe7GecJu46yKd0Uofh8kvtUuDRy7VerEZHYLdUq2yrbyYqbxJlqNnkcx2oRyn5aP_MFkk1OaGQ1095QXSnrEEDN2eDH8nbbd_HCjCQuT1CXoELyViPFx1eD1h8QsimZKnZ13zsiYkKXu_KOvF_-89P1y_4qkFEmLjMJHP3Ae-mtkH5T53MTbQXz3_iEPSY_km6WxUTXRziXvby3YEqXYYgT-feZD1ifl7UWAc9QcRdAJJi9uI5x6pQUfkKW9Js4giI_JyhKGff4xpxO7GqOu9KczmfqJ-z-ac4mzVlcdi8KQtBS4CSMYAeykFAG_ddtWfNEDBLYHkvFEiKqWgqsyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/29630" target="_blank">📅 23:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29629">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CC959Taa003IPFySKAz8BQRl0W3BZvvjrR_9R_-Oj0hBBtfTT9l8wp6MeyotBZBxcUzPCjUxM8B3OfMmP4Dz0IWnx_aVxQqYRtnU_F8gMqFCC0McW_e9qbSbV5QV2pGOg7s3fkVR1o7y4JDtMBwy-YweZ_Psoxv82T073sJW50ig7XhUy4q2h1tJWKRNX4kutgU9F9g3RanmUDB49ztSHcGVj3JlO5DvZs9CnKGDdvv_y6uNyWB102E8F7Xgvmu8oWCmGpGDGoD-XnLrALxArsgPnIGJcetEtLAO7u5XN8gSmj1KaVKyBvAVMALUJzU5N0CuFICALtHEVxc66nsv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌جدیدترین‌شنیده‌های پرشیانا؛ باشگاه‌پرسپولیس بامدیریت‌باشگاه فولاد برسر انتقال ابوالفضل‌رزاق‌پور به‌جمع شاگردان مهدی‌تارتار در نیم فصل به توافق رسیده‌اند و سرخ‌ها با پرداخت 150 میلیارد تومان رضایت نامه این بازیکن رو میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/29629" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29628">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8G7Qq5EhO_k3HE4pzsYikulMUivk39sS0T51vC0leg8N8kd-wqWyzdz_VcBOt4XFbUDoUE7Ro6fYAv7gUGrpWByaa6i9tx9Q7SUSm2EZX1G8d4UD9L23EJKgWIDsbzkT4AUeH8U5XKIwfFaOBvnYFj7b1MhOgH_iKxBNDO2C26a0fxqKeamzkBIZZ8O2_B25Nr3kkBfNiAis3NzlI9iofE1J-9PF2NrbGbDXSQ5_fSop_VlybCWlzSFQ49UDLif_91k0WV65FZOWQ7K0EFuY9sm2A4EpQzizBXoSlSDNE3hV6VW_hQPhmMAOLPCcs0mZMDWbzYNkbwsodmwB-U3Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌جدیدی‌ازبهترین‌برنامه‌های‌هوش مصنوعی برای تولیدمحتوای خفن در اینستاگرام؛ این پست رو یجایی ذخیره کنید به‌کارتون‌میاد و برای دوستانتون هم بفرستید که اونا هم ازش استفاده کنند. عالیه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/29628" target="_blank">📅 22:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29627">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ownGveQDic45xZKjX5sXRoLq_5slhIQZ02dcApUTwrtjzSOjzgUEYeYkL-ejUqo5phIoco7szlBZo6zB5MJRxkjc7FaUOhsWHbAdShijKf0E4RzwERF1R8BxyNGzaNAI0n59pkVaCZTcif8_zZkotKcrAQnPKMid6BOBI7XpwOmuLPQg2c3iT7dMejGprmZ0JIygK3aXquohNEiF79XcQGLVU_elWvhdd9G4Fu896vBfy0RlQPB_toO9WzziW6Bd9llW4NToSh5W4FJ6z7S8W_ywWsSfy6vHRMak5Oirm2FixrY0u5hs8yxU77bFmuio5bo3Nf1tayHC6zHAV25Epg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخبار دریافتی پرشیانا؛ باشگاه پرسپولیس بزودی با پرداخت 250 هزار دلار به دنیل گرا مدافع راست 33 ساله این تیم توافقی قراردادش رو فسخ خواهد کرد و گرا از جمع سرخپوشان جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/29627" target="_blank">📅 22:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29626">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZpOdX51eVwFa5pIyZEQ5zNPVqqONHPil7qcRzXL7bENx4r7YE4cXADlrOIPUjjy5HZrhaXbGix0iijkX89FgOZda8JJYy5Qw0w84PVz_Fy5kTGBTMPdrgcZ-Td1nhi1P_9rVqc5tusDMcQsM9Ozw1ZyKPvW4ZxKj9rU2bVV4kaWyLg_lIrQO8uKDlYc9ogp1GmoTjKiZlh8S5dbtsghL2oqGfYeIAKAZzMCU4sXGWHgr6Ygm9lEsw282Kv-antcVb3CXRfCtpkCLObUzmmooNXcCUt6PxQAOkI_SVByhSbrRgaJaOLhBvXaS6Fx2ErnUHvCWzmjuEnnpbzUApMUkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29626" target="_blank">📅 22:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29625">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2989e9b119.mp4?token=DyKnrB2gPhAmHjb0cKA-mj5IFlBtlVwkIXNsxtOK-L9ML_NlC1UGTdlkE1u98jsDQkMcRj5JHjhh0lu4BZwyo_7AyMjgZ2zTgHSqQmqpViNAGJSRcJhKHFK8MTOYW_BCZRoV0iSu93n-6BOp7116ExljQ9nRdDZZi9VInZLUwtn7rEWQ3M1miGZPqx_npO45eALV7e4OZMwHZsT13QItJtBEqJB_1pbNT6m7J3GCOsuR-jaIUyiOdyl5JJkp09jC9GeA_UxgyJF59Tj7ra5MYRsK43c0h70VPof3KF94Igk47fKuiTiA05gImMECXd473EvImS5X6CKfsrtd_OWnLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2989e9b119.mp4?token=DyKnrB2gPhAmHjb0cKA-mj5IFlBtlVwkIXNsxtOK-L9ML_NlC1UGTdlkE1u98jsDQkMcRj5JHjhh0lu4BZwyo_7AyMjgZ2zTgHSqQmqpViNAGJSRcJhKHFK8MTOYW_BCZRoV0iSu93n-6BOp7116ExljQ9nRdDZZi9VInZLUwtn7rEWQ3M1miGZPqx_npO45eALV7e4OZMwHZsT13QItJtBEqJB_1pbNT6m7J3GCOsuR-jaIUyiOdyl5JJkp09jC9GeA_UxgyJF59Tj7ra5MYRsK43c0h70VPof3KF94Igk47fKuiTiA05gImMECXd473EvImS5X6CKfsrtd_OWnLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد نوری استاد جملات قصار! شاهکار جدید ایشون درنشست‌خبری قبل از بازی فردا با سپاهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29625" target="_blank">📅 22:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29624">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKn08gmiGcQ6LEN1bIgIkBt60YVa4j-qEIUkceWJcgq6nN8r53RsYbT4Q34lrRQ3SfG1frV3RcRknZGCMEo_GlkVIh3snj671a_z2tvM5e0jdPGy_wnuJHeJKaW74oeB_mXnK1bUyTnRKibxnVnICAEjnFiRKVrrauIsF23oykWWtQTVHaExuYLXaIuGUn6SvzlB-R3hfY13SlidaoA9afl8cUkQciarZmsdVYc7tCl-FrfMSx3D0n1iEkMG68pvjA1BwosXknMIFbbMzoJsPyBlVkPXlDaEQH8cNidWUiTXwAfQAefHbTrxKS41BYvD--FFw8dwoGTtAyxIenFuyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛
بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد قرارداد با این ستاره 29 ساله تیم‌ملی‌عراقه و درصورت تاییدیه‌مهدی‌تارتار این هافبک تهاجمی خلاق به پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/29624" target="_blank">📅 21:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29623">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRyOx2-SG3aCMBdt9mAr-9y0fud04g7cZgSJJgoU-NvjIdPESviSyXs47-WEhCaNau_dxnbhQnlTTKKQ-S9arEfNxsUDGHBGlOzrfPBwCu_iHIxqovBEMupSjDkCoS1KAas0eDX51FYx6uuNk-TgddnF-7rsWSP8wsT6B2t5gucxc-LfIXyTXCdejiLpEHUUHVcgYfl9QQK-muZC7s8XPKqaWVtntjsipMzMfGYOOXRwB3m62ZHklGpuznhkfXnhAK5cawH8JnarZLfHsc_3NqYIQk_3G3beEdEQ4OiSsCg-Jc_bEcZt4WCIXU6xRKuqb-XCbf7hAyDTSNsQHKEh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
گواردیولاسرمربی‌سابق‌منچسترسیتی:
برای تموم تیم‌ ها در چمپیونزلیگ برنامه داشتم اما هرگز ندونستم چطور رئال رو مدیریت و کنترل کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/29623" target="_blank">📅 21:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29622">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
توهین به پزشکیان در پخش زنده صدا و سیما: شما خودتون لیاقت ندارید صدا و سیما ببینید
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29622" target="_blank">📅 21:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29621">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfLSkqqO6vMhemse6qGacwrN1bnEvXhXBt1RUkpCOs9KhImG1-_HXwF9C485yatBmxf-Ja5AsEoH5rhQxHlh5fAm1nCzT2oWzpYUAcTUGWlej3wnxoc4HEiwVUtCpleNk68lb8YN3PlZF9RI9RHJmCM9sdps0dzbBW6I-XFGgVuIAO3QlWuYmCeGFPb5RQYt9ialQvzh5D_21pwWAR9yVbW4CNoyHz1ej6835NagwpSyuPlLQiUmPwkxb8pgHDHYQsxOZJhWWmVFH52sNDMA_aTBCXBxz5A9uP5ijkJV35-gyIqObEJjK_4WtUzM8ijNta4q8RcCWCsB4FdORDwwqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت‌امروز انواع پلی‌استیشن 5 با دلار امروز که حدود 223هزارتومان‌بود؛همین کنسول یه هفته پیش 190 200 میلیون تومان بود! قیمت‌ها عالیه واقعا:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29621" target="_blank">📅 21:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29620">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzL-DnRkEooXNA4SGjrQE6Rc0mFx3jLGa3BF4IC8bymZ-1q8EvUQ67Y9OGemNZrA2fx1rOHT83-rnNfCjTYOejaA1HrIdI3FP4g0TqUh7l2oRP8dTBP9Dg5Oj7oaAmZfYLF75y3fEy9uIGIuofqKJC0ohRimfkXloG4X_m4alMaCGUFeEmr4i-OLMu2NaJG1D-sX_6A_jEQWN2wJ2_nGcPojAYNWuh7zl-narRiOUdNXpq-uuuSThVrz_mNkmACY5_qVc00cK8mg4vXWrHQ2IHpOMZRkSz4Lw_9-P4Lp2NVeDeh5_fdILS5AtZkfc89JpNeyFkaD6gc7_YiRe2Tbqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا
|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29620" target="_blank">📅 21:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29619">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHkN8c2jWx4QPEqtl-UBImkRRMmIScmEVq1GzB53WHzaSCKQ1wGpObfbsx2EnQDmEaX1m0IaCwa2C4T_g6aWdMgcTo0hXeqbTVEBIXD5OvO4fvgGrC5KNBRBjKLnjCTsKzG52VvgcXMek_nyaF_H473oOg8_VqrC4TeSgOwMTF580x2jL-S2natAeUznbQeOuwjKmBcLWdWH5L0xIcIAGk3U-yrCsxy6K4ydgPPiHEArG2ZEeztqkZZrug6sIj-rK8erqdD4YZjOCIruJkPmuy78l-ebHx7YGb3Fcv9zdJLKrOeW-nrkOWnDPxupYp_0AoMCni_QoIpuYS_zaSWJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌میگن‌فوتبال‌غیرقابل‌پیش‌بینیه یعنی این؛ الهلال اینزاگی امشب با تموم ستاره های گرانقیمتش همچون مارتینلی و واتکینز اونم در خونه دو بر صفر به‌تیم نئوم باخت. حتی نتونستن به‌این‌تیم گل بزنند. نئوم تا پایان هفته ششم  دومسابقه‌باخته‌بود و چهار گلم خورده بود…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/29619" target="_blank">📅 21:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29617">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWWmC_7JEIHb1Q1OWTG5ocfn7_RKOixI8ecIgGqb7wxE3D5xoZbuEqQcrltB605MnTJh_6TFbWUCjtjMW-yQonze0STQvN0Vzm1s_tmNoujzuLFhaFjbuwvkfDyyi4IKAKJ_g4avp5RGceqXSUv_ZCyWxiL84Sh2fIUU8dsZ0kcwMDn7qRgYPB4oD53HGFCf10Toeswo43F1cDgPNvCsA-l8C0ZEWeu6LlVPN8GLKGq-K7Jvj0-wWj8GM0nIk-cU7uqmUnaXOemeYiLbU9AdtX71NxqoD4xhvWThbeSozWcxymLxu20dcUQwhz5tLkg0a5RM7Q6smnB1xpTdD5y7aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/29617" target="_blank">📅 20:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29616">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuT2acNcIzHPgniOyVV6LtFjbPTn5U4Q6aNcfj0sJeKnCK855bdE5JEuQkw2CebGAUxMKXCwkA2KuNLYnL5-fZIzi6u0oR1fRIaal3YVFFkgtv__BfQPZalVOXrARUlGBrevPJ5k8VfDzL5S1s5ObushPNQnya1zCrlhQWGTkbosMPJDhcYlMe67qOT-ln4kR2hNlr4e_JPgOXetvLNrFxWyld3scMa881seVXZQEmypUQasz4y78x32EZnoaoX4SWlJtEM1s8SxtYyHXgdxPG-njmwu-TwK0e7THsfcZvHvvU_6svtA8hXNinmEnhavAbJgPWl7eig6QuJzPajWhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29616" target="_blank">📅 20:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29615">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6942e2257c.mp4?token=o_5ngxnpHMgxTiNddG-a1cwFVoXl2TXYgw_xvyk2JaE9ROBNgTrQNw_9nv78XbvQUqXvZPoI0-m8y9USrWMas7hOaiUjSoimqoeVZFQ_3Kb1IOJ003Ak3d47W0MqshPyyUF7KRN2W0qimkwX8ZdglWAuxymqqFXiz3pI9Lx_NR2UoUoP9uvoUOMmrPvUn0pNdm-7jv-MStG1zq_PutNg8MReyGfQ8csFXJ60SyqXz0QqrudfD85iHpHlhb6z3bI-t2YEXjAFtiEOOFEj3NwfGICkHkcPLNUWq8GVHTuYR-fOp4zTlNRT6na6w4-J9eGN7CTYLujOnRnInRNb38bzVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6942e2257c.mp4?token=o_5ngxnpHMgxTiNddG-a1cwFVoXl2TXYgw_xvyk2JaE9ROBNgTrQNw_9nv78XbvQUqXvZPoI0-m8y9USrWMas7hOaiUjSoimqoeVZFQ_3Kb1IOJ003Ak3d47W0MqshPyyUF7KRN2W0qimkwX8ZdglWAuxymqqFXiz3pI9Lx_NR2UoUoP9uvoUOMmrPvUn0pNdm-7jv-MStG1zq_PutNg8MReyGfQ8csFXJ60SyqXz0QqrudfD85iHpHlhb6z3bI-t2YEXjAFtiEOOFEj3NwfGICkHkcPLNUWq8GVHTuYR-fOp4zTlNRT6na6w4-J9eGN7CTYLujOnRnInRNb38bzVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گردوخاک اللهیار دراروپا؛ گلزنی دوباره اللهیار صیادمنش ستاره 24 ساله لخ پوزنان در بازی امشب.  عملکرد فوق‌العاده صیادمنش در فصل جدید برای لخ پوزنان لهستان: 6 مسابقه، 5 گل زده، 2 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29615" target="_blank">📅 20:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29613">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tT6havQfxjxr9tkuLTrmq2HtYjCAfSrHyPXYryhbDQqHmK9PENrI0QlEvkOTFgyJlDTXz_fqg0V8TMw0FnBe6Itq82EDrIY1FdKu6m57uW2kvR1lYqLZOEUmnloK591HPSCMyIgRQBeSiRr7XFyCnHhcIbF36TTwFSGRkpLemxPaGbWwnZQX59tJhj0lDoHNIvMU0Xe1E-82N2iuQNl2E9cWSbYvs5dwW_aWhz2AKvNUdJogGxO9tqhB6sZJo0bdLYanOIXRC6vOmMnk8uwXLNK-BEMKycyS0lMy58jxFSq-kxybaTuXX-WbcEoHvAR5uzbOoliy4_eqS41Rw96LKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLfdCT0u4dI8H738pjEK1jp17JpzB5Fb7L_e1PPmWLOxr28haozbwfJI2CIMCPqyn_QJxe6Eq1zOR1dTitu_HdyEIvc9jAOvYjNVfx0J60rvadLEl9HbD3TM8bLHpxuHgkHEik4wutc9yZ6AkSHNfKOm_LYsn9YyLU_BFFOOPbz5wvF69K9nGrlLA5qWy1V7ho6JewprsjllgfDoIMZClCOPxjm7a4caFyD6Hs-k2DPJzfQ9rix99nq8RlPVDHIdXaMz2m3CGiz9QMap5PvljX7qkeMaW6qbzrN4BNlvVe4u_tBP0z8kDPI_dWfr6tWzYiqqDFKoG9O7xQ0DDqNwtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29613" target="_blank">📅 19:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29612">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
سرگئی‌جاکیروویچ بوسنیایی رویادتونه‌که 3 سال پیش دریکقدمی‌عقدقرارداد بااستقلال قرار گرفته بود این‌فصل سرمربی هال‌سیتی شد و این ماه نیز بعنوان بهترین سرمربی ماه لیگ برتر انگلیس انتخاب شد.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد هال سیتی در فصل جدید: سه مسابقه، دو پیروزی، 1 مساوی،…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/29612" target="_blank">📅 19:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29611">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzI6MhehLPJJ2pvuJKhn98-WUM-7zrK_Ogr1hzJP5q1cb_NuXcqZRxrmi1mjGW5JqoOpUXeikq0rcT2GnAvhvX4TACeJZA_8Ja_wOi79K8pRv_bXoW8aoeLj2B9X87u3SSCf0ccF_AQmdC_sohvxyUFN2SWS7lRqLenR71N1XtSmDlhFU9XloaFFsBxgFdPTA_R1tW1M5H9TB2gFYOWYm3vYcTlUTa88J028Vb257mrwsWvbUOZdv6HEM9GOssPXER6UzYuvNPH7TxkOBGjNe4sLxomL2Qlg0c9CULb8SrUrYZkv81uvSGZpGhy52gns8qOowJPh3sdVxTLbatnVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرصت سوزی برگ ریزون لوئیس واسکز مهاجم بیرمنگام در بازی امروز این تیم در چمپیونشیب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/29611" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29610">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgIuZJZDsmdTPi_sUJQgpzeULMw4lRdxDyVMlsyGWWqvVvGBbPA6sT4T0I7X1HJWwVdSyuA9a0mgFVBh5P3nMz0cz5llFLfUlFXSD_qAp-syuT3U1523nIO1okwR3e77RSLfuWjAZbu6pZxFnG5njfQqiY5gLv1U6JwQ6kRCOYBbo-FPESqkofmhX6VGpHz-1LS1Vnq9t5DC5m8bF_G8scGYoFCjcFy9KuITTAfPTAk57nD7rufbo1-BzNhOaxNZMJR2Vx9EmCxoGcP-PdB4yUk0JUxIej23v3nK7QzfhYbxeE8cY5Ul29A6IkIAwlZGsz9pshdcp1mvl-aDtvdUqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🏆
لالیگا اسپانیا
⚽️
رئال مادرید
🆚
رایو وایه کانو
⚽️
💥
باپین باهیس؛ برای تو، پیروزی یک سرنوشته
🌐
سایت پین باهیس بابیش از400اپشن برای پیش بینی
🛍
پیش بینی باضرایب بالا
💎
🤩
🤩
🤩
🤩
بونوس خوشامدگویی
💎
🤩
🤩
🤩
فریبت ارزی ودلاری
💎
🤩
🤩
🤩
کش بک روزانه
💎
🤩
🤩
🤩
فریبت درگاه های ریالی
🤖
دانلود اپلکیشن حرفه ای
💵
درپین باهیس دلار با آربیتاژ 30 هزارتومن بیشتر ازقیمت بازارمحاسبه میشود
🌐
لینک بدون فیلتر
👇
👇
👇
g21
www.pinbahis.com</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29610" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29609">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdC85qbWZMQG1pJhLaJKHfimzxGMNG6s5UR3GocSKiACeo0xoC3PLGyyj4VA5xTNP8jcHM33sFyzAL8-8KRpx724FxNOp7nM-9flZGpX9MEwKeMEAGDK0uAnkhTbU6d3AUvm5qKKtI5sZwjv1nW97OB7e5RUgYm-9h8mwxFm8-Ap-t41fqR4f8lQIWg1xtmeXhnTR6TmiT5FqjZFDjXhhsWBFOXiIlVE9iEyQaUXY-2tBOozMhFrx-TjLpcTFddrcXTDZiu89H_IbTUKeV73mTG3J8sKPMvP7xDugCvQuq2xpw6JEWgxhVOPGMJW5WbHWP93JLflD2b2OML1dnedug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نگاهی به آمار خیره کننده مهدی طارمی ستاره 34 ساله الوصل امارات در دوران حضور در پورتو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29609" target="_blank">📅 18:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29608">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFLD-2trte8EFScTgX6vWJaDfI2JBOEILWHIjpSCVZEfIDZ8YkSgBl03AqJqQjfxdY1mFfJ7z6UE9fpirC3L8paG2KpPOasyobA0kDtVbiva3ylcrLIbHV1bj9FT5U8q-qyFTNQkfcctLoXdG67ZT1PB4uaXH2V1FhiLKSeMdmbvqCey0Og4j1CNQJEWxiHoZTtkpF6PrLvLK0bA5iNTRrAH7YIn02mDdFSCow8eQJBD_6BkREpKl8-frXIoQYg2HTwHtBS41WuEmDljweQhNAlNsDpah14ZXoPLfaEyvUevx7IutY_HQI17DMqP6AfZ9dnfe58yKylK-tN3UVqreQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ AS: میکل‌آرتتا اگه تصمیم گرفته باشه در آینده‌راهی بارسابشه فلورنتینو پرز سسک فابرگاس رو راضی خواهد کرد تا به‌‌تیم رئال مادرید بپیوندد اما اولویت اصلی پرز اوردن آرتتا به سانتیاگو برنابئوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29608" target="_blank">📅 18:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29607">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇦🇷
ویدیویی‌فوق‌العاده‌ازکاشته‌های لیونل مسی فوق ستاره سابق بارسلونا و تیم آرزانتین درمستطیل سبز
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29607" target="_blank">📅 17:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29606">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1Gbneqv_VbXrcwh9B4O0ax4MH628kR4JSOwRLyURks8FlcAFPfqIB4lKFd-cL9NElnQsk4e5wQKO7E1dhQTnGGnFg0RcQWIAfFwuSg_h84CTfiaSpy5_lIdOzuHKyYNHktMF_FEQ1XljwW3PmVYzzAq5zLBWIU8hh0UVtj8EFs8xgIHsdMYUf3PwyYU8WHX-9V7bzLxXrA8B-mBKm5JaWCznh5DUOY_CSybXHq3XkwnCD6E26rDxnJTFRN7loe2rilIB6hHqIqmPTNtGPGQkZ-rEHK0utd8g-lDq452Kpa3OW2k9ejEEHHP_-IgE6dqC2QklX-Y1Tm9LmBPcPOptw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
پرواز تماشایی برای گل شماره 979؛ گلزنی دیدنی کریس رونالدو 41 ساله در بازی امشب النصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29606" target="_blank">📅 17:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29605">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckQ_i44Cseb8uHwThRoWRXsGhBJdzIPcb9YxRNqUxNTybxGKvLVFoiNsCwxpKXzEFW7cTMkfdo6aws4irdLqYMYOWBKynwn_vdUwTAOLpWDbFqU9kLQzaJTpbs3x6y_EglLm3_lRBFYRhrpmPgPA0al8zfhk5gl3DfgJVPrsld1qXmKKiCpnZZvCfZZi_rfENsXailOKxjsif0Iegd6rpNzhKmBIqygPEeiJRGgXA-4ehJLNmtCMAp07ovTZJwp04G3zu0MASZCIjuSU85CHYpk3UloYfgFKZwFCdGNc3vpGMb3zV5ghFKe6sVrEEdtchhDKWAzoRwx5bJFoDKFlRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
برگاتون بریزه؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مدیران باشگاه سپاهان امروز صبح به‌مدیریت تراکتور گفته برای صادرکردن رضایت نامه آرش رضاوند علاوه‌بر تومیسلاو اشترکالی 50 میلیارد تومان هم بایدپرداخت‌کنند تا رضاوند تراکتوری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29605" target="_blank">📅 17:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29604">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Js4tgGy7pd_lyN7VIq1c5T7iAfqZVZB3wobrc1Yl7mI_83Ohw4Hov9-R1i_b42JTG1PYT5hois4W2EdFRCD7ZTLHsXZLMzkaPc4Shz2q9FSKjdmKXwKXMDsgU7xIqItiYQyNmw0NM7l5Qi5SlGLnQFMI-8hznqknzSfErYuld6DDBhkDaWK-IMeFTJuCA-vqAwCkiR_UtYcqgQKaSm8alIRiP-JVMkXNi28VwPljpGa5jv6kMq6l9VkR-dd6r0hBNnLF7oWcSSma_zvTPCnHLIDyPetHYUDzpL8ZVY7ZQiVcdaPTjnF8qt1g0ELjihv7UdSfyuA2yVcAcDqPYzvd1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
با برطرف شدن موانع موجود، کاروان تیم فوتبال استقلال تاساعاتی‌دیگربرای دیدار فوق العاده حساس مقابل السد در لیگ نخبگان آسیا، به طور مستقیم از فرودگاه مهرآباد تهران عازم بصره خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29604" target="_blank">📅 16:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29603">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pD67VcC34oZYj3UvqMeiTr_DW7PRWQeVahl25Z2CMjMoa-weTwAvO_sgcIH8U-e8YYeoFCFr9oHUh5woTVsdLqtOW8RdZtv8l-vlMQLnH5EMRQICtgGRPeHFxFLPHPvXbwZWYgb0p0zxzkq7lVA8AmzZwKat88VFm0ki8zN-6Qo4cc9RwQfytsOcbO6d0bLnko4G92hKbfMBmbUNdY90qVUdMBBEIT4wCjZJn_uF1TddT3hl0fZrmIGMRVXv-xxRuvMxvLftMsQlch9JXCFl617NGwn2fAxaiu2PRaynsYU6xVEqr1Lox6fFV_6A2UdVyAbGzHM_kc14D5e1IOT16A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه‌کامل‌ودقیق دو سری آیفون 17 پرومکس با آیفون 18 پرومکس که دیشب ازش رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29603" target="_blank">📅 16:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29602">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abe26c296f.mp4?token=FDWrkKHd9-ht3VsmHeTFjGfAIUkyhsuGlFFr_EvpT9nmHIIw4xz82HRx-3QnHsQ6NZrOwrWlZ2ZCvBSKktG-4KpwBPtfSn_2xEZiAbQZx8Lu8NQyV0A5hNtk7fFLqlqX0yunh1vOf0LZYCQRxt36G0JB_INccYog_sXSKIUC88P1ezy-O6HC0xJ7Ed8yhW9nKh103BbL80x95TNZ_4NPnlCOOEWL412_Egj49ggJ29domeYx7nEc6H0ULOiDfqRKau9xBQ55nyeISMYckvO3YnXOzwiJcUxl7vF-4w1nZWt50pa1JH4dU-a_e7UMPrwpDjd3ylKHxTjayZqAHQ_ANA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abe26c296f.mp4?token=FDWrkKHd9-ht3VsmHeTFjGfAIUkyhsuGlFFr_EvpT9nmHIIw4xz82HRx-3QnHsQ6NZrOwrWlZ2ZCvBSKktG-4KpwBPtfSn_2xEZiAbQZx8Lu8NQyV0A5hNtk7fFLqlqX0yunh1vOf0LZYCQRxt36G0JB_INccYog_sXSKIUC88P1ezy-O6HC0xJ7Ed8yhW9nKh103BbL80x95TNZ_4NPnlCOOEWL412_Egj49ggJ29domeYx7nEc6H0ULOiDfqRKau9xBQ55nyeISMYckvO3YnXOzwiJcUxl7vF-4w1nZWt50pa1JH4dU-a_e7UMPrwpDjd3ylKHxTjayZqAHQ_ANA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ویدیویی‌از اولین‌پنالتی تاریخ فوتبال که کلا 0.2 ثانیه توپ تو دروازه‌بود. دربازی این هفته لیگ MLS به این شکل که مشاهده میکنید بدون اینکه توپ به تور، تیرک یا دروازه‌بان برخوردی کنه گل میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29602" target="_blank">📅 16:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29601">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLFnfI9zvMwdyRfrEfjBP3rv4OzJt9wio0tYdmFXzBuoZxwtMHf4pNnGpw7UYuO6X_eGRh3smIbHx6Y1HcFdDuUsFhum6ZztLWJM0iImm4O1ZQlCy92FZR7hT2ynsrs4bHAqvPbfls_9dNyJ67gIZupU3qYiUIS2_pofFqBWIXEQza3c1DubJxjNtBiaKg5pqqeohLGVsAY2ns0isFARcoHb3g69PLFIqBJMqhC_jomHyCxjdmrt1zg8OZznK2eX7V2boR2gbmGSLDkVxtRLoYDcWk1joDj9zmuJNUqPuHKRAZd7sYCf-wyeHnEZ0ACx4XjMlBaeWqVJDzPmopPeSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یاسر آسانی ستاره‌آلبانیایی‌استقلال یک خونه 75 متری در غرب تهران برای تدارکاتچی آبی‌ها خرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29601" target="_blank">📅 15:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29600">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2KAxxQgbk9MWZQTcR5223bi3kInzi_Ngl3LrcPengMZe-Y7KJDXo6tOHsH-mhgbXsJcMNEjewKBDVOchQ1-Tn5UNjGT6-jR8GtcLdzroM2WIGRxswDgfLvQS_r4xRRRxt06h5yQ_NCipoZ0unvXVxn1qU-vM6ew1arX-dFdCPoYm79d4shIBWLTk_yDoBD_H_7qjL_0EBIQS4KO-ltv5VBy6LCaybTLOjSpKYuV-3yk0Z_gEJkACLfZDrl3KgiCvT1ZdlrHSXY_0h54y9kDPJF7iyvME2UKV4y8qJj-9VKD_I7zSsrKNuIvEbtVMvhkPa_t5OXqv5XPPAc2em-WbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/29600" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29599">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epWHa-_4Q1w1w5YXSJCrrVqW60B7PVKvo7c3Argnj5ZRjsL_ef6Zsf6W9up1BBdHI0wEoOe9z38Zkd9ZyT08E8NwyBbVZX_VsH6PuVX5A17BEYexMcizellvzLsOsCgs-RSyNWIBguIb9uCzw-nlEeQTwKk5MbwGiYqa5yK0-87s64DDMBhZgKnPwgiGJsViumn2Wjv0j4Zp0vH0R7KNA5NyByO0qsMvv9M0K1d62VUlIqOgl0kET4dxWvF-Y60H9VhQp4i1bMEb3Ea3Lgnx-Sglv2jhB5Aq8t_ilLnC2opewq2NvVhJErzuCMlYzit7qHhbfIDSvL-ce8_bHN76WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ بارسا در لیگ قهرمانان اروپا؛ رافینیا و فرصت تبدیل شدن به بهترین گلزن تاریخ بارسا در چمپیونزلیگ، بعد از لئو مسی افسانه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29599" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29597">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2a23445f.mp4?token=tx_cpQBtTCV4RWYZZ3xKf9vT8Ar5As6FUKN5BGDCLfeIoyjUQ2ZbkU21HuzPTmo0mlfR6I_ZHGWUwOAPnxoLhpwttrcOpj5up7sknYjaFwi174fB6bFTdddji2X7585OrgLbCQcgIUmaAA9X9vECbvpABuUvfkZYuj2lngy2Cl9wJIuV6ceJKlJ9lCH-T39fU4v7wBxgYb5Akfx41lu-_Q2h73n9N2VbvHpNBS_CPMhJl-CDmJWb8F2DlKRy4Xp91TWu3lIumETxYVB0NcIAsnGKx3A7aP20XcvUUKk38qOmFiFYz-m_xNY_xt8mAky4VbGxGjG4tOqPc9OkADDeNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2a23445f.mp4?token=tx_cpQBtTCV4RWYZZ3xKf9vT8Ar5As6FUKN5BGDCLfeIoyjUQ2ZbkU21HuzPTmo0mlfR6I_ZHGWUwOAPnxoLhpwttrcOpj5up7sknYjaFwi174fB6bFTdddji2X7585OrgLbCQcgIUmaAA9X9vECbvpABuUvfkZYuj2lngy2Cl9wJIuV6ceJKlJ9lCH-T39fU4v7wBxgYb5Akfx41lu-_Q2h73n9N2VbvHpNBS_CPMhJl-CDmJWb8F2DlKRy4Xp91TWu3lIumETxYVB0NcIAsnGKx3A7aP20XcvUUKk38qOmFiFYz-m_xNY_xt8mAky4VbGxGjG4tOqPc9OkADDeNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شاگردان پیاتزا بابرتری قاطع 3 بر 1 برابر استرالیا درنیمه‌نهایی جام ملت‌های آسیا به فینال این رقابت‌ها راه پیدا کرد و در فینال برای قهرمانی آسیا به مصاف برنده دیدار امروز ژاپن و کره جنوبی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29597" target="_blank">📅 15:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29596">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T55o4m2VPEQNYrUvLzFFfVMaZTpaK1-8bvgJOpsTLprY5a1GiVYmeUP-eNJW_WnqAEAMVl0pi6V8djBrDY_bZKnuUhgwPAKPs8AE_1r_g1RmhCBW56BaVEkWRewaSTYh8keHu-AEdaSdtz39WAReCJ6WLFHrOvtTJSuESZD1wKOAEtDlqIYrH8a411hwu-zOK6ViGCcbRILOTwLVnTvV2ZItBDqgwTfJO4289jGsJkkYnfO61EglBY3u-6JwsXBYHr1M181twOmlP-Q1IQ_jwjmAWwN-2KTHIXdwotEdMAaWBWiY6RVIs4X6_2uX2TBtSh9EnhKPeEW2Se0bT66XUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاریوس دروازه‌بان سابق باشگاه لیورپول در کنار همسرش دیلتا لئوتا گزارشگر شبکه ایتالیایی DAZN
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29596" target="_blank">📅 14:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29595">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wslx7AzbYttC3dSRHXvfdcnJ3MEMxHIzgcMdyA0utFHPS_T4EiG6J_jRrFJTFoOANjjVADS_xiTJYq9aq3RLiZnvGK8ko2eygSY1to6foiFE2ziy-c5gMPxJ4GsVjrr_CjIyDO4t3FehOOgcOpVH2f0sT5evy3uTg-wwkaGMYZr_03K4sJIEsG3mMoLLpXfHgxym8GCaQJepO7_MMr87qhiWVi8szMqcM8mmfopJjMZEht7jZgEznPix0VMsm4YqWchCNGEQBxrqFSaZWqZGR_TE0iAkzzza3Zi8CpvmFzTll80Eq8X4GEhtB8nd3N6B0kGP4FdGEFSCCW3F7jsYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌ویدیواز اول تاآخرش‌سم بود از دست ندید؛  مهدی توتونچی تو برنامه‌شبکه‌ورزش نادر محمدی رو اورده بود رو آنتن زنده بهش میگه شنیدم میکل آرتتا دنبالته که تو روبرای آرسنال بگیره نادر هم کلا ویدیو کال رو قطع میکنه. بعد توتونچی میگه آخیش! پست ریپلای شده رو هم…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29595" target="_blank">📅 14:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29594">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozhCqX3sUhxnPBG20FYBiYuZ1ebUdK6nIsSgseC378L3CyEmTkPyIF8I4Qw3LXO7X3Tfzn6jVig5CUL6KopqFx5_-kyE-CSlA0MPGabCYJJUY44xajgpXAJDXTseptzRZb3-eyc7TiSXG5bY1ezI7bG46YuYEr3uNjoaPeSWh0K1efYrne85YmAW21IOUvYizp6TZ-pE575zlE93601jRRyubL0Io5okIZDKPP1ipdqZWj6BuPtSGUPElJ12hfTDyGgC1CLJRNNd2xUuPZB8kQ3WN4KCnHpRWszyzqh6vNmaoRxELxpXOCDMH0tSY-eibsA1vv24sSJKl21huzPanw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟡
🇧🇷
طبق گفته رسانه‌های معتبر عربستانی؛ ریچارلیسون ستاره 29 ساله تیم ملی برزیل و سابق تاتنهام در دو راهی النصر و الاتحاد قرار گرفته و به احتمال‌زیاد راهی یکی‌از این‌دوتیم آسیایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29594" target="_blank">📅 13:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29593">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ro9Ddol6i9_wtX_6TXdieVrYSOeb9TtIJzlCtE-IFc5Zcro2N_yvf9GV_0ti-8qCmOK71uApI1DsWaLl6xQZ5AE7u2t7xN1D1tNkLLbtdZYNUyt9yav0zecDe7L-LOa9ZI5-JrRBCmhJ-pDA8TiPDhZ0lCGQquloeNqUUwh8B-dC1IprmiAFreqL5rTwmUwHfgkjCogc3cdTzuitRdpU5dvQQarlvUscjAl2pOcivgx_3rK-cNCHH9lI0YCC88DAdFMvclSktvgVQTn7sGv4XWIZimn6n3jsRyHabI5c817gXBwb1rKXUZBDd7P_8BaLxcW8dVeLRU4auf2j9cLkug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بااعلام‌پزشکان باشگاه تراکتور؛ پارگی رباط صلیبی مهدی ترابی تایید شد و این بازیکن 32 ساله رقابت‌های این فصل لیگ برتر رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29593" target="_blank">📅 13:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29591">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29591" target="_blank">📅 13:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29590">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tp6OZ-673UuICAPbrKiuyvp0hG_bSkjFTjdhMLI31fiSaIo4A0s96EIEssjzu4gurk6tdupFWqmdzl4qP-g7VeXOoqAdAnrLmlTMriG65Y-pP-gioWzqtOCqegBRg1dSidHmL2QSDo1lreuwHcMTJOt3bcMD2nRYfKWIsOr_6L1Y7kPv-9pfLA4MfRv0D-ylDWNmmvRoZZ-mExYASIv1nx9ThFYUJmck5iIknqVEkmToaXe6Og75QbRDkfwmJ03iQk5e_WjeejgpkU8Z0y99InduU1JGn7zUKJNm_dZ3bQNQ_wJLfPerrBpfvlJJUcvyUOhPwHn8XjhTrvd8VNYYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
باشگاه پیکان از باشگاه استقلال به خاطر استفاده کردن از جلال الدین ماشاریپوف در تقابل اخیر دو تیم به کمیته انضباطی فدراسیون فوتبال شکایت کرد.
‼️
باشگاه‌پیکان‌مدعیه‌نام‌ماشاریپوف فصل گذشته از لیست استقلال‌خارج‌شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان،…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29590" target="_blank">📅 13:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29588">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU4LJ3XxWVKRQs4DMGlWNRyQp6kN3BWG_dWNcMb2mps3_1YBP18x7pD373IQvwW6S7F_FpNq2My1XyEkg9wYin3CiXgYSMqeOLadT7St55zT0n8yF1bgeYJL-SGwdttafK4RmX_qa9MRXGmKWYONroum6dGkW5A4kMEU1ocLV3Rf1i_eeZECce0Cq5Opv_2d6mb7i95VqgizRBogoBINMRJ0GvVRlS2VYCYbnpNTzr32wFUA_hH6eK9Wdvyy2dTxAbiedhzE_GW-5kXxSTjK7-rwbqa5nQajOl4iOH39S6nVemJRoO1sjyB3igBOL-YteXm_XAyyeTnB6g6XLMlmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
معیارهای رای‌دهی به توپ طلا؛ عملکرد فردی؛ نمایش بازیکن در طول فصل و لحظات مهم و تاثیر گذار؛ موفقیت‌های تیمی؛ جام‌هایی که تیم به دست آورده و میزان تاثیرگذاری بازیکن درکسب آنها؛ بازی جوانمردانه؛ رفتار،احترام‌وشخصیت‌بازیکن درزمین‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29588" target="_blank">📅 12:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29587">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLWaTYQ_temNHsVC0XaxGGsnLgqeRlf9cKkJtLE1mNZXPya7WuRbEcolxtpaHmB_cNH1tUCcao0KYKUFz03xF0rkDHjCn5qaLd7mIRKx4klZCPKmI13aHofTR0a6Y-gUKu6DvYss1Ymg1lu-fV9MdshVirNY_Hfi4_8A510kMX-GpViUrGUZ45xWTcj4dAsv9uVfCCCE2qLnGnwaJ8dSJFILjnr7-dqomYlgh4MznoC7rTXcGgvvCZenUzNLmqUx788HvmouO7e7GdikGqrIjO0u7sQVk7IMTZgNQ-rI9wWSq1WJupAweFxKApjuAAiJZ9Ksl3LoIRiV1rgsZC-loA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
برگاتون بریزه؛ امیر قلعه نویی سرمربی تیم ملی که تاپایان جام‌ملت‌های‌آسیا در تیم ملی موندنی شد درخواست دستمزد ماهیانه 15 میلیارد تومان از فدراسیون‌فوتبال داشته و شرطش برای موندن روی نیمکت تیم ملی در جام ملت‌های آسیا این بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29587" target="_blank">📅 12:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29586">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3e03b999.mp4?token=CyGcEBUbhZ6VbY7GcAd4TQW8mHQMMcyBtvbccK5fsZFj9KGY3nz-oxEQKm_izEXJ_3xsVRhxDQM8LRQrwbxYPgXoLU_b7DHAZaWVTWQ67BAHlA5jYNoMaohQlZEQJjQfjJ_zvz6cXSAAo9TINBnm6wZcpXB8U3N8AK64LHvCmDMimnIkuXw9ffby7ATE7NI-LRU_zOSsdbc1Xj5ZAwNfHGrttoBpdDdeoh8EqL86TvfoLQs4aYRoFSWlEyzugANhOU6z3DFVJV4jqgsnJ_aYcJN0xZi4FAIQaHv0p1dq3EE0A5dpfBBnj83mfCCkLHnXIcAtYpTE6YzhB1NiyEO6sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3e03b999.mp4?token=CyGcEBUbhZ6VbY7GcAd4TQW8mHQMMcyBtvbccK5fsZFj9KGY3nz-oxEQKm_izEXJ_3xsVRhxDQM8LRQrwbxYPgXoLU_b7DHAZaWVTWQ67BAHlA5jYNoMaohQlZEQJjQfjJ_zvz6cXSAAo9TINBnm6wZcpXB8U3N8AK64LHvCmDMimnIkuXw9ffby7ATE7NI-LRU_zOSsdbc1Xj5ZAwNfHGrttoBpdDdeoh8EqL86TvfoLQs4aYRoFSWlEyzugANhOU6z3DFVJV4jqgsnJ_aYcJN0xZi4FAIQaHv0p1dq3EE0A5dpfBBnj83mfCCkLHnXIcAtYpTE6YzhB1NiyEO6sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تقویم
؛26سال از این‌خوشحالی عجیب و غریب محسن رسولی ستاره 19 ساله سایپا گذشت که با یک حرکتش روی آنتن زنده شبکه سه فوتبالش نابود. بعد چقدر بازیش خوب بود این پسر. یه لحظه نتونست خودش رو کنترل کنه شورت ورزشی رو آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29586" target="_blank">📅 12:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29585">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrQRO_gazYn-vkH540jSTgT6JiolnGh6d1q5XfJBQ4UuytgjskqsjkQwCOjzEY0KO4WA5zyv6E9Go2JgoO6tcPIeahH9yWyc_Y2xFSdYFjnM17h7TmamkbdYf8ij-VMCZkWK93VXMk_Vz_t6ipWLddw71uw8e4vJUcOaDWiXFYhxpAlMF-QPdUrhJF989DKGR6UZmtnjOkJ4ixZXYOELNX5NEUypOAN6T5x3f9bLjBnZ4kKUL-GcaGDgujMKsaSwZhvHZMqaZHGyq3IH8hOFVflk7Ci57VRAn7Y_YCPuYqiTO1ph-bc7QrhFgkq7ws_flvw7Jm6DNJ8sr0SzGayiiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در نیمه‌نهایی جام ملت‌های والیبال آسیا؛ فردا تیم ایران ساعت 10 صبح به‌مصاف استرالیا میره و ساعت 14 نیز ژاپن به‌مصاف کرهای‌ها خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29585" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29584">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkgeN6Tt0kVQbDGm2QjSgLP_63RwC7u26ce0yc72PzQwi5WeJwBcPOQQe91pA_tiJoLN94PlULhnUbJ2jh3x_zR_C-1hispNO_g8O2V32Dv7EcHZwHxFlGfrXQQBxivKLky8T9OxsAVNhH_L4JzTbkOi21X3M18sICKzzjxxa708Fi1eKLvd9FvqJtnXxUFTtTYhQa1NGkDk9y0xcNF9nYg1_D1QSid-ArhmLUF1nKGh3zICmrQVlKXFfjv68V-jpmBHfzeQZY0r6kT3yD8sUxNa8P3S9sblOLQaJI7i45tmgvHd7QMU73R9czvM2jdpvy0wy5YR2rZ9AVjQ6sdnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
باشگاه السد قطر حریف‌هفته‌اول استقلال اعلام کرد برای تمرکز رو لیگ ستارگان قطر و لیگ نخبگان آسیا از رقابت‌های جام حذفی قطر انصراف داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29584" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29583">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsSaVroKEIw1IRiaUpfA_SwEFbYhdygIfoocuT6K37AMa_LdBbJvMxjhDop_utRGvGtA3LBFbwInRzU5xDhc_yAchr_C9ikjDwSVgicYik32hbhTnKVqDka4e7zC9OhwOkCC7jLiFhV8v0KOqooiWoOhWYtpezlkMQdYt2f0sFzHueFJdHJB9WgUK5-PCDEWv2_LJ3lKfIY-pKQ4umZnbpA6CuSihJvc-CBO_NvYF2j6D9G5q2pe5yw8BR7mrhcX_NZ2vHJWVAKJihXgXeV4HKkegsnt_p2xKm8KmJ9EXnQmkabuvkPzxuJsyIgNTHEX8eK26EPjOkbIqA8YJ3g2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
‼️
از تحلیل و آنالیز تا پیشبینی رایگان
از مسابقه و چالش  تا همفکری و گفتگو در مورد رقابت های ورزشی
❤️
🪂
هیجان ولذت پیشبینی در کنار بت بازهای باتجربه و تیم حرفه ای پین بت
❤️
🤝
همین حالا در کانال پین بت عضو شو تا در مسیر موفقیت کنار یک تیم آنالیز حرفه ای به سود و موفقیت برسی
❤️
🤩
آنالیز دقیق رقابت های ورزشی
👟
چالش های نقدی
📝
گروه همفکری
🧤
ارائه فرم های  رایگان روزانه
🔗
https://t.me/+IxmGEx4ep9A0MzQ6
🔗
https://t.me/+IxmGEx4ep9A0MzQ6
🔗
https://t.me/+IxmGEx4ep9A0MzQ6</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/29583" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29582">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
فرانکو ماستانتونو ستاره آرژانتینی رئال مادرید که مورینیو به پرز گفته بود اعتقادی به سبک بازیش نداره و قرضی اون رو به‌فیورنتینا دادند امشب برای تیمش درسری‌آ هتریک کرده و نمره خارق العاده 9.8 از سایت فوتموب دریافت کرده است. ماستانتونو در پایان فصل به جمع کهکشانی‌ها…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29582" target="_blank">📅 11:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29581">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJ5ElgYlWErQ-FtbrSuG1Y2ktAzI2F3wLwTBM4wrAZ9SpkTIcKgyAapxCut6I1RDTfk0qzSA_JlQJnpiyxplO9Q-zQ_GtAEp89lmC9DDRYbqwR3RRU41QPFFsTMJO3oMTDhkCkNAUrPSVk059HKLSWOvWf6KzuckmGybYr0xDK9aALyCtmECw7uyjDDyWyNdPAqMUV0d8H6xXHbUQlQpMDE8djbvWYm5a8_rao9T3nDQt0VgJNfhuNL-DC1QWjs8KF6Jx_DVAcPTjOcbfkSZWgH-G8CukQQjOhpIixT8MA11eO02yhCbtvL_NOaInLCy2jgzLsz1GfC7U6L486sHRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
47 سال‌پیش درچنین روزی؛
اریک آبیدال ستاره سابق بارسلونا به دنیااومد و با این تیم به دو قهرمانی ارزشمندچمپیونزلیگ رسید. آبیدال سال 2011 هم به بیماری صعب العلاج خود غلبه کرد و بزرگان بارسا در شب قهرمانی این‌تیم در UCL بازوبند رو به‌بازوی این بازیکن بستن و آبیدال جام قهرمانی رو بالای سر برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29581" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29579">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af01699be1.mp4?token=nQ0mDapzBzeXpD4EiN6CBC2-n11NJ8GO49F8XXMAXyXU8ONRDz8EmcNwi0_RUvKcWqho0jeyT2fORD9yO6b1MzqngTjcAjEhhCqn66gLUWlYCcIIGrrXEOSKttXE3SwA2-Gu-aH2s-s8mCs0mSxmgnTB9VqjUD3gadbwErp2wZ6nR_Z4BzI8DJKqjLQx3uKxCBU_kfS7iCqFicSUriN9vXlX-Dmu08e-edqB6EdEvv09MBVQ6zz-P21g8GOXjJbHuvOHVDHbJHK_XSNSDF6es1SvG9ewxlBVgO63PiBkQQxFzio2KY5cpquBKfy7AGQGh_F6IF3A3urXhHsS1zZvn3PdStG8Fxdkt_mkaN8-FVeCUSXHAkxyUvYLQ5s8nTBqS9Ew6_d10MP7Ve2sW2KJnWK91P0fNSjQ9elZSSwjvikFSYghSsbc-j5IpSjad2Xjz0lrA0FMFIZ4K-Jjpb97eIGr6ogjKiwhX4IAdJUM5e8eey7Y6IywuqI6pz7EMl0RHVfXpRs0cWtIKehBn8xJrVfxakuWxC5fboOJJA1G-aXmhQRe9LbaRO-FCx-i92qQpx1jbGI82VTzHU6Feanh7v81u8ldaR8wBur5WX65ybe_V9YrLjSilZxYXsDWHya0Mq2iO1bWKwo5tuZbg9SGqd5pKiFoPShyUGoOg3mCvtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af01699be1.mp4?token=nQ0mDapzBzeXpD4EiN6CBC2-n11NJ8GO49F8XXMAXyXU8ONRDz8EmcNwi0_RUvKcWqho0jeyT2fORD9yO6b1MzqngTjcAjEhhCqn66gLUWlYCcIIGrrXEOSKttXE3SwA2-Gu-aH2s-s8mCs0mSxmgnTB9VqjUD3gadbwErp2wZ6nR_Z4BzI8DJKqjLQx3uKxCBU_kfS7iCqFicSUriN9vXlX-Dmu08e-edqB6EdEvv09MBVQ6zz-P21g8GOXjJbHuvOHVDHbJHK_XSNSDF6es1SvG9ewxlBVgO63PiBkQQxFzio2KY5cpquBKfy7AGQGh_F6IF3A3urXhHsS1zZvn3PdStG8Fxdkt_mkaN8-FVeCUSXHAkxyUvYLQ5s8nTBqS9Ew6_d10MP7Ve2sW2KJnWK91P0fNSjQ9elZSSwjvikFSYghSsbc-j5IpSjad2Xjz0lrA0FMFIZ4K-Jjpb97eIGr6ogjKiwhX4IAdJUM5e8eey7Y6IywuqI6pz7EMl0RHVfXpRs0cWtIKehBn8xJrVfxakuWxC5fboOJJA1G-aXmhQRe9LbaRO-FCx-i92qQpx1jbGI82VTzHU6Feanh7v81u8ldaR8wBur5WX65ybe_V9YrLjSilZxYXsDWHya0Mq2iO1bWKwo5tuZbg9SGqd5pKiFoPShyUGoOg3mCvtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما روز به روز داره خفن تر میشه! شبکه دو یه کارشناس اورده داره از خاطره قدیم میگه میگه کارتون میذاشتن زیر کونشون فیلم رو میدیدن.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29579" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29578">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRzSBBelcyInq5OiG7OxLv9nwaA8XNWaIPxjGEpFcCpOVChQcJNjP9vUU9-bfUHS0UhSo7xLr-45jpU0Wsj8GjkiyZ19-qMe25TJCbkxiT_doqpJ7JzkfBruRMljDMwkCDY0YAQhgcD63dpuH1NJYMWYyYAU9n_CYgySN2sPlr8VXeplkuGFicSooKldAM-T7H3xTEi48ZDJEp5KzI721e27VgKiGBPf77xFXfxtCblKGpNCTGNgRJjINjcdKbYx6HuqMEulwCgvIbpK4yBQ_JRWDa0rodRyb4l0NDz6emPT_nsD-MLwToSsxazW_xbQlJKMr78Txf48XdnoUlKcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌نویی‌قبل‌از دریافت‌پول‌های هنگفت
🆚
قلعه نویی بعد از دریافت پول‌های هنگفت از دولت! شاید شما فراموش‌کرده‌باشین ولی‌تاریخ که الزایمر نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29578" target="_blank">📅 10:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29577">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJl-Yx-w2lPAd4Qgl05V_2JzeMgwBcQ8TE2rXT2v1-s5lecKuLWWi8G7ROOBNo4VoDqA8vow-1rhX6BMeqUlLuWJY4noqNO-lqJG904u0GEvSoHWL15k2N0o2wCs2KHaNOZB1rdvBTbTCfb3TUoQ6cBhSqaNUKeRJdzJhXgDIK2UtLhq2KfT8ozejbSZqdghUL_nfbrLlBJw7XNUp33Qnx680dGsh9JoCvQhoPVeE9kiI3FPWkqxrx5zmefADrAk6v6nkehw8oHiMgnG_UdKw7JPJHUOrPejNIzRvxhWVgJ5GYgfFA_sBU4nJtjIdm8oBQq6857LK2KoOM7iVUA1AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
باشگاه پیکان از باشگاه استقلال به خاطر استفاده کردن از جلال الدین ماشاریپوف در تقابل اخیر دو تیم به کمیته انضباطی فدراسیون فوتبال شکایت کرد.
‼️
باشگاه‌پیکان‌مدعیه‌نام‌ماشاریپوف فصل گذشته از لیست استقلال‌خارج‌شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان، حضور مجدد این بازیکن در لیست بازی با این تیم غیر قانونی بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29577" target="_blank">📅 10:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29576">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6157fe5afb.mp4?token=TM7oyf3MnSBsQHpr6NyLdlEPC4jdW_W7RtR8EgoICjqwGjqZSqL3JAXFvtRsJgyqyO8keUGQyq7gReGb2EMBlKIIQ3bFt923CdnZt-xMFW73KJCTQUsAD0W6RPOAL8NtBHB-q1KfgLeypC7hfndbpqaxzrOGmAG1CX4k7R1gpzqmlYqxpP8VUvmSB9wtReTFnxlegMse8IA2eLj1b2EGADTTgBznYMb_LqCLIT-8o0g9GrUuq1zYHs-up52mAUiN3NeKh7rbJvgNiznMKm7WDBd1Jyn4vTZNWHvM6Tm9lREDyjfPNwtfAa9dFJZtxNLyioFcBCQnb4xbJNFyiArjgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6157fe5afb.mp4?token=TM7oyf3MnSBsQHpr6NyLdlEPC4jdW_W7RtR8EgoICjqwGjqZSqL3JAXFvtRsJgyqyO8keUGQyq7gReGb2EMBlKIIQ3bFt923CdnZt-xMFW73KJCTQUsAD0W6RPOAL8NtBHB-q1KfgLeypC7hfndbpqaxzrOGmAG1CX4k7R1gpzqmlYqxpP8VUvmSB9wtReTFnxlegMse8IA2eLj1b2EGADTTgBznYMb_LqCLIT-8o0g9GrUuq1zYHs-up52mAUiN3NeKh7rbJvgNiznMKm7WDBd1Jyn4vTZNWHvM6Tm9lREDyjfPNwtfAa9dFJZtxNLyioFcBCQnb4xbJNFyiArjgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
دوس‌دختراسپانیایی کیلیان‌امباپه ستاره رئال مادرید در فیلم جدیدش بنام "Drawn Together"
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/29576" target="_blank">📅 09:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29575">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2108b760c.mp4?token=M5OJaOGmbtw65_HthZpahDX85SNpvFCpf6Rpl36IFRIAKFoaK84AUVEyiKmNMUeUg_iVGzzInocW9ZF-u7J7r7jh81fwGotFmMNxYR6gJ0VtF7tKCzYH5sx7SA1Lp7tH3UGzA6O3I2mw4aX5mnHXNKpomsIAVKdky5cTLnb8eP9he7Uv9-ZCzlsdjHTLn41VzBC6BHOKE8jsyyW6fLVQ6z7eAlIGsmUEgsHMnmrhn02bm4fF8MtaFb8hgSMRD-i6N6FG0gx7QDQH5xLGdDPtJrgoFepyVpFPRofio9CPFj7TbXzRoixrhmgIL9_y2ukcjEraZiwHjouvmTTWwOLOORxwZ4ZHq5g11PmG9g-sbcc8c0CgdeNeN6G8gRcRsZhJAe0pjcbOYxIADet2AKDULBJdB5na3qDR3kJ7-cwKfw8tYm16I2-JEdyQvcUQ0aKdcYb6Al7tpwPU-XybyocwdoPjI3geZLcv_r3eKZH0EyQ5dJP0mPJmoY-ES1xfmxtZ5RPUxwd_i2_S3Sb4ASEfEyvPVsbXSI_iVgEJbERk4CsQihXmJwpAbnvXABQKJ-BbibFRvfQLVVkkkv5J1UAO9ep-Qe3lk8ubTphmqOmRJGcBkLDSISyxbJLCadZFyMXUa1iuGKBUjAvsQ6gOpWomFtA-rzr1eeIN_-OIYmqcxbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2108b760c.mp4?token=M5OJaOGmbtw65_HthZpahDX85SNpvFCpf6Rpl36IFRIAKFoaK84AUVEyiKmNMUeUg_iVGzzInocW9ZF-u7J7r7jh81fwGotFmMNxYR6gJ0VtF7tKCzYH5sx7SA1Lp7tH3UGzA6O3I2mw4aX5mnHXNKpomsIAVKdky5cTLnb8eP9he7Uv9-ZCzlsdjHTLn41VzBC6BHOKE8jsyyW6fLVQ6z7eAlIGsmUEgsHMnmrhn02bm4fF8MtaFb8hgSMRD-i6N6FG0gx7QDQH5xLGdDPtJrgoFepyVpFPRofio9CPFj7TbXzRoixrhmgIL9_y2ukcjEraZiwHjouvmTTWwOLOORxwZ4ZHq5g11PmG9g-sbcc8c0CgdeNeN6G8gRcRsZhJAe0pjcbOYxIADet2AKDULBJdB5na3qDR3kJ7-cwKfw8tYm16I2-JEdyQvcUQ0aKdcYb6Al7tpwPU-XybyocwdoPjI3geZLcv_r3eKZH0EyQ5dJP0mPJmoY-ES1xfmxtZ5RPUxwd_i2_S3Sb4ASEfEyvPVsbXSI_iVgEJbERk4CsQihXmJwpAbnvXABQKJ-BbibFRvfQLVVkkkv5J1UAO9ep-Qe3lk8ubTphmqOmRJGcBkLDSISyxbJLCadZFyMXUa1iuGKBUjAvsQ6gOpWomFtA-rzr1eeIN_-OIYmqcxbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌خاطره‌انگیز و دیدنی از عملکرد گرت بیل در تقابل با بارسا در فینال کوپا دل‌ری فصل 2014
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/29575" target="_blank">📅 09:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29574">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‼️
گئورگی گولسیانی مدافع میانی سابق پرسپولیس و سپاهان درسن 35 سالگی از دنیای فوتبال خدافظی کرد. او بزودی در لیگ برتر مربیگری میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/persiana_Soccer/29574" target="_blank">📅 01:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29573">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcHCj4Cwzo_8Z0HZjCFX8G0Spg3OpcyL6a6B3rTWRKHtv_tQuuaK74bT_Q-a9NKQd416a-lDKB1h3HYqOOTlYgW7rejLBLFCcG28iCb-doFUCUo-66R3KXGVA8QH4Rv-XtI8t1c6f03SIFqba8OSHNFMQxiCdJ1ofOazqEzjmA9PM1BalOptVBLNLz48aNpzU3pOJohgaYICsZrH7qY3yfDLfmKgB3bm83wlFOB2lWSpAxyt_MBAYdH8awtG1gp3_BEvYjadqE7Edg9Wkls3C8j0L18IZoN1fFDCWxpQEJ9ri_mR0E7BkAh4bqDMi2pl4240rfMD8MFPlwGI1PwsJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نادرمحمدی تو روسیه‌تبدیل‌به‌یک‌سوپراستار شده و هرکجا میبیننش دارن باهاس عکس میگیرند. همین روزاس رومانو بزنه: نادر جون به آرسنال هیر وی گو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/29573" target="_blank">📅 01:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29571">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsa8C0SR8Ank2MVE_C9J071HTTnGSA9ef9dgyLulpnix-bDGYMWWb36ErLrnyM05LGkH8eXINBUWcqhIrIGB7KWwNySSnvkEZTXdtd-4XAgF_rP-0ELxRUT6FbUJRayXuS3eJoQV5vuc3UxNz4bn9AkwB4R0-cCkLkXkGv1gqxDxOBnhZ6gYPMo0F6ot5fIHigEFWQ03e8wX3-3e6_MKEBVnjNQXZh2u5w9RCMagpiTRYe5irxbnCRuSWcD9NSLyOstiWCYiY72d2P7Nta5AP6flow4q0-oQ1LVYx5cFYfs6AfpALJJquzDnIQ-JTOPB726COJPZX6Y7FwYX1FIgYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین گلزنان ایرانی در تمامی مسابقات در سال 2026؛ سعید عزت‌اللهی با دوازده گل زده در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/29571" target="_blank">📅 01:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29570">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHgf8qUkumeJMI9pXebB8BObkRo3Z_7Q81ghIaZN4HpDliBWPG9xCWt70fv7BaEnezHtja_4HJ8DKxbMeK-hjFzb7BNpS7rLJFpJtQ_58FWFCYjkHpif1zR0TNKt6DnXYL9hBFQoHo_WI4FUSdlQyXzhLapRh6W68XZn5GLdkVDqm68s0hRap7boy8p2nQ4ZMIA2jfBfFBg8_DOOsBQTBNcKkNHraKPCns3qtvmrX9z0TWLRFPF7Pf_yZDk5vnyu30dYUAAopeJNS_A0oOqmb9teZKwrP3ryhAeQ7HmBs6jAOIbHcAk7-MaWl2ah9GYHr11Hf56rwhecZwX2p31a3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری زاده و نکونام سرمربیان استقلال و تراکتور به شدت علاقمند به جذب شهاب زاهدی در نیم فصل هستند و حتی صحبت‌هایی باخودِ این بازیکن داشته اند و به احتمال زیاد زاهدی در نیم فصل به لیگ برتر بازخواهد گشت و راهی یکی از…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/29570" target="_blank">📅 01:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29568">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDSNfzZN7M-VlpNidi4Q4DOEaeH6_-cPLeigcwpIWLMqQIrSOoPXR2UFPfBvN9Y5SoCMAzj8KFxuzwF8D7bjHiSjIkBkUNdJHQ8eIJsqwJmrR1zS7aIxH7h6dGknjzxEyqhV4NpSkfsXPG3fJLyZ4t25ABxF5loLoWL_prEEbSQxTN8P--SwO-X53dsfZFeGYqQDDTbcehPgjeqOdM6lFgny8nYsS3tZhIygR-hRHJ7gkXr2HokxMrNe2MubZhfcjoX2I6qgNSB63PqDxX25s6gBU_pS-WokNiXyhQD0ti7QZN6hohe4psuatKmFXCEvglYzIH4C7gVjXklKiEvftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ فرانکو ماستانتونو وینگر آرژانتینی ۱۸ ساله رئال مادرید، با قراردادی قرضی بدون بند خرید دائمی به تیم فوتبال فیورنتینا ایتالیا پیوست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/persiana_Soccer/29568" target="_blank">📅 00:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29567">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhgD47ytaH28wKUxX7h-ZoEGGefOgWA_803FvJz-3rWAfa7PjAmPE17VI6nvH-arFlai2xAwpNSCO9GtuFQIEACKxfISUbG1Vl6pzHOiauF02KHU5T2GU__XDJpM6wBBuC5bBMtPhZVQQSq5usnIyS8kUbQcmFdFR8KHDtKJmaJzwIO8fQkYNre4oimCO_RLYHj8MAF6ifbJPig9WibNuaXWusi7eoKm5HeGvbW2E6mV2u9XuBzphZE4DN3Hf9CCVHxA5AdupEyocOcK-tip1dNuIXn-PFPt-nqmd_uPVn3oJzyhUPn1-5PSRu2phAHLbW6e0oN1YAaET_VDa2KnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اوستون اورونوف در جدید ترین پیغام خود به مدیریت باشگاه‌پرسپولیس گفته اگه کادرفنی به سبک بازی او اعتقاد داشته‌باشد حاضره به‌زودی با حضور درساختمان‌باشگاه قراردادش‌رو تاسال 2030 با سرخ‌ها تمدید کنه اما اگه تارتار علاقه‌ای به ماندن اورونوف نداشته باشند…</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/persiana_Soccer/29567" target="_blank">📅 00:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29566">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a6b08f6a.mp4?token=jmNNwGYp01oGi7VB59r7FHo4qHbOnCbfJ_6Ymm6J2YocqBOt9V-qC9PIWKTqH0Mr01nL5oz_1sGrj0x_-Ocqa3Ix3hbRNxIv8A9ueCIPry9CRWQsNgBCzimLi9C9-lUhydf1LUq6f4eFWYAc_AhTe5yv82LMkFY0y2jiIGOhCPEJCrAJ-nxQf2-239VV36hes7j3QHqUJIN8KeV2oPfkzpRKHnbH7GGGraM3l2iwuqSroJfWFr4d_jzxK7-vmV6Lq6WWk8gGcOWqwQ9jHdO2qHqBHPG8rkqwYQBzLO9kXLS2QuHAolzBZkLpjKVQh5ymwn94Rf-Ef8JCmspwe9xbvYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a6b08f6a.mp4?token=jmNNwGYp01oGi7VB59r7FHo4qHbOnCbfJ_6Ymm6J2YocqBOt9V-qC9PIWKTqH0Mr01nL5oz_1sGrj0x_-Ocqa3Ix3hbRNxIv8A9ueCIPry9CRWQsNgBCzimLi9C9-lUhydf1LUq6f4eFWYAc_AhTe5yv82LMkFY0y2jiIGOhCPEJCrAJ-nxQf2-239VV36hes7j3QHqUJIN8KeV2oPfkzpRKHnbH7GGGraM3l2iwuqSroJfWFr4d_jzxK7-vmV6Lq6WWk8gGcOWqwQ9jHdO2qHqBHPG8rkqwYQBzLO9kXLS2QuHAolzBZkLpjKVQh5ymwn94Rf-Ef8JCmspwe9xbvYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌مهران‌مدیری‌به‌گرفتن وام‌های‌کلان در قسمت دوم جدید سریال جدیدش بنام «مرد سه‌هزارچهره»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/persiana_Soccer/29566" target="_blank">📅 00:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29565">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGfpPcuCSOAutCEltR_gzl2t4E2l3dfTD3wQSu0sAgwZ9EDTzgW0LHaaczQ1DbV9mqGblPyg8hAoZtFgkZ4GZ8Qtbo3S6gTB2I9_3gxkHAljb9aWSrBJNkKMxGWh6md7zhOVKsf33Ocb6qJneyeefyydoawaSPz4u33F-iSFNTmbr9Jc31hqjcQKRAVTfHSwoXdVXzUyCVt23mlnV36Rq-eLzVvQ1wD-MVePYzLlW4vOktbDI4BO1ocS8Gm2oh-C11Oqo6cEHVFN4R1Zglc_UJkgREoDrlONnADrpE_Xc4rU_Mrq5QfwKO0bMo1cNoBleRKU_ufpsQYGhZ6BRJdgjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛ از جدال توپچی‌ها با یاران گرانیت‌ژاکا تانبرد رئال‌مادرید با رایو وایکانو در خانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/29565" target="_blank">📅 00:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29564">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvuzBPgvhf6ddBlYPhvlwUHqqDd_llo7XyzAvXxYcvyA4yHTXjtLkQYCccr5jRjSM9NdNK3KT-340YHSNDp9L2vbFbA6VbJWf8bTp6GUGmm0Zsnw8Y0XhurdTEfszqJEFmCxTRCHRCYFjXTz5MBZ2OlT7ZLIsyCTRW81OJuqb22yo4KorBCPKzgqf0RMazDrrCtDQ3hXfHsG8XXIzqojr9-G9isyKOgqvWgU9Ke4SsgeGX5A2QIpr3V8WlUkp7Zo87YUDlp_KwNXeYXmdqn2SQ0Lm85udB07VJHpG1w4yGoFTD4aovMo_e0h1Aw1VOmq2A8Y80i90xzzlO35Huq60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
شکست شاگردان مورایس برابرالوحده‌وبرد اتحادکلبا با پاس‌گل سامان قدوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/29564" target="_blank">📅 00:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29563">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHevGKcTNgo92SPgVotS2zQbVJgET3R5b3hvaDMAH-49yZDFYeerZir4H4DwvPJ1JclDH6H5eA4kLcNTA04zSpcuEeNpssVu5RWSLrN9XPuaJXQ-7uNekRpGFTmWg8ItNCG8xQDlKgqiVdzf7s5-VGDFLNIGGZPbOdE3SznD-ZfkYVhw1HkdhuN24uST6hpZyoo2bANyYVL4bKZeN_qLiHgmpHyXSoRadgH9sOlLynodvVs0vbWGaxI3P6LTa_w7spbBC1wrxuGbZ183cDS9XrDpGewgXjjzLJaatQzHd-sbE_bxCnwsPVb-JNK3UrvU69zKdA4XX9SQox6jkP8yEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه بیرانوند بالاخره باز شد؛ گل اول استقلال خوزستان به تراکتور توسط رستمی در دقیقه 54
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/29563" target="_blank">📅 23:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29562">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITLOfimVa90MPOQN5Z1qwdikfSRYLYXmkrddNxcoRtxTRaxfs2RR0F8XTAJ3-UG1b67G94mZsjaErOq4cygkS1Qyg1mz9F6yvjCwI_-jIZB9LCQrcULhuVRDv_-7sMWKcZDhQ369urgsWjicn1WX5e4eJZsiJfijkEZP3En337zk898iQYJ2-X0BaZvhseMNuouferv8gmK01EBCdhggBjZt132s4ItM3YQPGSSlUTd9_9VJVZprLo1Nb_Z0TSPRN6-63nLmB_yO9G5k0CV4dig2nVJId_P2xbn8ESqdYulZQt4g3L-6wU4s7ZfRHD2ZktLFtjcbXp_0tuNpyKLgSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رقم دقیق قراردادی که نظری جویباری و محمود رضا بابایی با فابیو کاریله امضا کردند 1.2 میلیون دلار بود که بعدش یکطرفه فسخ کردند. حالا 40 روز فرصت دارند که با این سرمربی برزیلی برای پرداخت یه مبلغی توافق‌کنند درغیراینصورت کاریله به‌فیفا شکایت میکنه...…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/29562" target="_blank">📅 23:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29561">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5ms6kMe9vld3cQOCFzaKRVQ9Fcga2M0Bu86aXZ7wHcbGMnV6dQTqI2hnBEVhfNeHEXNvOCVKQnKBqQyDbGyqDhexv8SmiCbxCrIa-bmUzASrCA-XCG6dKE6G1lXkWYA5bR2ESx54q6tXzoKL_-W0TDHxwQNeR9z65TjOjiQPAGttfQEEC3laN2j_wtxVP5mhY3gXVJRek6owe9JdV6YRniV2tYZvG08zonsHNhq2RT6EXaSgqnLuWLQqKKKRhBF7Vbk237EDCPUKbuQt84gTWs5EWwMmErymoK9IPGbE3GIyBvI2tYNnklhiRwOGNX77N9Wsrt_UOi5c2IigmCnMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد فوق ستاره‌ های فوتبال جهان که اصلی ترین نامزدهای‌کسب‌جایزه‌ارزشمند توپ طلا 2026. امشب‌بایرن‌مونیخ بازی داره ببینیم کین چه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/29561" target="_blank">📅 23:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29560">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQsZfgkePYgSqrlxvApleD19AWA0PZ6GoWCto9GYrf--TKzaDz-v0QBnhweliCHu3nautS8AKcoYxkvrlnl88Y2d8nLo0KJ3KOEA2a39WwLTRIZ8kiHxQvXHMXoOuIMx2KWqXYfh5eBsY7maed-kazTz_P9lY_77MA61PReU_Jg_MWcTqUeFFnLZg7Zz1M-GOmF9QYsGcC3coygcpDVW2Iel5PWX1BKfIY2H1drnv7EhFlgl1Fv2tkoKqMw-JDpFarHT2LG9bVcovQg1NIxkg7364fsZh-A13D_AcOaButcJqlK4k477dm4FBK5Ii_g8yKGoLCVGhW6ynIVOUl-p4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/29560" target="_blank">📅 22:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29559">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzczJhdAJr7Ogamn1xniPc3mp0FAsuiiPR0uRL95a2ugqhTEU39bNZ9wj8R8cHdJ483Na98MAvyPPP8A1kgGMkW2kwXTc1lxyBadENivEyJV-1bJ1dQzGYJuTZV85Ed9IxVPrLKC8xifXlyS4pvDWbO_9G5T6jPoqUzxCwUjKM9VzHSSaMTSe-tQK6xd2Dq7-TzWsdn4nPpyx7JhUc6dfS81kGbnRFa4B08pKjFjsHdy7CkLkJ9fDPZ__-6td6MLJ-G3na_fDg6bBTJo2TN1DZR3HW-TLDIAup-UloQhooZIIhhbxVQzWgV4y13Z4pFj3NrqQJNmgdKr_-E8kWVCcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/29559" target="_blank">📅 22:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29558">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e36c4c43.mp4?token=NSJSiD-JeVJRG_yJSFHu-X2RhVXCGcYoSqkdb-w6RliMyVNh0OSsB0J5FGmqeOBIu1CV8kde-98zD6-4nWFHIZQTtXyvPtbcDiktzW3r8dF8l5WHtIUQ_vpy4rIHNiuQT6Y1cmGiHDjD6m7tVB3UUYcXkc1obV9RvUG4zgNKZ8BvTnVE3kS_ZqRH2sRt3hGVltCDPFtd_WtSpyTaeCJLCzrHFsDX2g-rl68c9I1gPSv7rBHiulY-DvFAJSiYnjsVUnhWd4ybM_wJGKo_W-0y0No827HbXD5Ly-9mkLQsRLkIlNx2Zihj0QEqxMcJsLWxKc_JSYSq6O_s70sN8aRZ-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e36c4c43.mp4?token=NSJSiD-JeVJRG_yJSFHu-X2RhVXCGcYoSqkdb-w6RliMyVNh0OSsB0J5FGmqeOBIu1CV8kde-98zD6-4nWFHIZQTtXyvPtbcDiktzW3r8dF8l5WHtIUQ_vpy4rIHNiuQT6Y1cmGiHDjD6m7tVB3UUYcXkc1obV9RvUG4zgNKZ8BvTnVE3kS_ZqRH2sRt3hGVltCDPFtd_WtSpyTaeCJLCzrHFsDX2g-rl68c9I1gPSv7rBHiulY-DvFAJSiYnjsVUnhWd4ybM_wJGKo_W-0y0No827HbXD5Ly-9mkLQsRLkIlNx2Zihj0QEqxMcJsLWxKc_JSYSq6O_s70sN8aRZ-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
صحبت‌های‌انگیزشی‌رونالدو دررختکن النصر دربازی این هفته این تیم؛ نمایش یک کاپیتان واقعی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/29558" target="_blank">📅 22:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29557">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpDIdtdM2wHnYllzLcmapCqkpD0dXFT99r790PqbnKubui9NWK1y9-UUZejFoaa_Z71Ew0nIZgw1Skr3l-94MVtsFUMyAQvfSCUqIk1Sxc7k9o0aaquwlZ1W4P5ca7azn2BoESgFOEcesbvKv5HpbyaC_OU-S8qVtjOCrlaTmONWKbA1__0OtGMhVSGkMp-9Pf5wxgjt24Xlg1AnEiR6Wr_hNNCpQ6INuZtL9ne0IsJqBpgnF4d1a1olU2SBvVNAehLbE91csyfMb4tWEFKHJ6_uBsyIg8_1r2FFgnBd2LyiNYeHPtSm4ka1QomnRJtDoM3OeQ1TD0CiQw-P9ghfjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/29557" target="_blank">📅 22:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29556">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSVepYkO9DFI7wV0QRGyJCM0UajwuGG9vxAib6RXiZdP9diEqmc5DPpQbzVN2vLLfh-mUthb63XgHLyjK1MfNBoYawauStdfFnYKu517glezqVAW7rzbGQIzdFsRYPAGYIiwkCjTLbGo07OAQydp_azFt3CuEXkaoRPZdLHO8UMBKDULBW5yzbgHsy79W4x-UoIWD8VLYFuARIPSOMrkjo3lCpdnRJVAdoSfCvigNq5q1QzBU7OMAC1Cq9yw9L7oDuEkec8Vc8iaVSmvKbdiSmO7Rzw7tdepD5QCbhzB9LJTLoRjKxD4VwQOAQxql3NILD63Xbfk_Pdm6rZbse8jxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/29556" target="_blank">📅 21:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29555">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IONScXsTiDtafldrta6aOz_IDhe9NdnOtf5KH4OHS8uGJHm0U-J5AkzUY_fAqj2IPvE0khvupwXLlG4wUnNdm48_gcwRPlDdoJEZl6I2YIRvpLyF5nYFaWIRQek4U1gpOoj62cgCh_oGsfvOD2sEsnNLQL5-NBbtty-O5tDsRStF0d2r-wjoEcfVm8o4__Q8eNT3XJPjQNkUch1mARkNkkBDs8uQR_vdtQuqMoVg2htBdBZn_MnDgoqupS_JE00HrvNvW3jWpniLRtVQ95BMfp7OB97EXnKB9iSnXF5Ufzk5if2gRVrzJqXHgdjPAhRP5sgx0FELyHjCtoPhb1Busg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص آخرین وضعیت اوستون اورونوف در پرسپولیس‌دیروزتوضیحات‌کامل رو دادیم. در این حد بمونید مهدی‌تارتارمیخواد اونقدر نیمکت‌نشینش بکنه که خودِ اوستون اورونوف درخواست جدایی بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/29555" target="_blank">📅 21:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29554">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e054a17dd3.mp4?token=YG5rpCMCCRTubl4bjqEtSd1RxLoK5ELMhM7YK-2QAmtKBo-iSOU9ifONT-b3sOlXi-8eTa5xjdIHlBE3Xg68OkcYG7hWL3jA-XQ1QCrVfG1njyDCIELltQ5-2EJEXp9y3j1i-poEsMS9if-0kbPcO7Ul921N5nr9G8Q3jYY5yI0MsYc9TpfJMBJ5atPMNSUYyXf3_KDzZK8k7drIF0rNnFgSaFyiD-bUri1Q5-pmRB4oeLdJK3oCuVxwq1B6pneZnl89HKPVKlc3zuMJjEXXG3bO3p2uYxdGb5RP4NUWmrtnyFxmG_uBpCh53IDxXQcAW5wqRxxcYB56eKxV_ZhEfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e054a17dd3.mp4?token=YG5rpCMCCRTubl4bjqEtSd1RxLoK5ELMhM7YK-2QAmtKBo-iSOU9ifONT-b3sOlXi-8eTa5xjdIHlBE3Xg68OkcYG7hWL3jA-XQ1QCrVfG1njyDCIELltQ5-2EJEXp9y3j1i-poEsMS9if-0kbPcO7Ul921N5nr9G8Q3jYY5yI0MsYc9TpfJMBJ5atPMNSUYyXf3_KDzZK8k7drIF0rNnFgSaFyiD-bUri1Q5-pmRB4oeLdJK3oCuVxwq1B6pneZnl89HKPVKlc3zuMJjEXXG3bO3p2uYxdGb5RP4NUWmrtnyFxmG_uBpCh53IDxXQcAW5wqRxxcYB56eKxV_ZhEfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمایت‌مجدد مورینیو از وینی با یک ضرب المثل جالب: "تو فقط به درخت‌هایی سنگ پرت می‌کنی که میوه دارن. به درختی که هیچی بهت نمیده که سنگ نمیزنی. به درختی سنگ میزنی که پر از میوه‌ست."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/29554" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29553">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac2a8bd0b.mp4?token=mgpFkqRYSJK1bNS_7eag9F6_2BQxCL9QZIkQZecqvphbFJY7FDPZYWgcPPVIYhn7DwBIAyZ_4pY1q7c9mvDKcDfaENvLMX9BlrwJ4weZ0KxTRBwQrpbbdI6nTHhFlSnS127HjJvyMWYkP6QkFWOTeYNWMVLOmx5Dtu4rpYB5xRJMYgt85uwDwBGzy4wpa5k3KCS_THUrJKyyYIcL9nMTvRU8iIA-jp3WBwBU9iiSS0cu4NlVVxTTJOt6HGANArvyWQI3QWOHwwrSTTtb25qmzHxu-PJlk0Dpe1Te8NiomXk3GK3XX4u2-VZBREgoUe2xRlGuu6VaZXcgX9wHnO_IUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac2a8bd0b.mp4?token=mgpFkqRYSJK1bNS_7eag9F6_2BQxCL9QZIkQZecqvphbFJY7FDPZYWgcPPVIYhn7DwBIAyZ_4pY1q7c9mvDKcDfaENvLMX9BlrwJ4weZ0KxTRBwQrpbbdI6nTHhFlSnS127HjJvyMWYkP6QkFWOTeYNWMVLOmx5Dtu4rpYB5xRJMYgt85uwDwBGzy4wpa5k3KCS_THUrJKyyYIcL9nMTvRU8iIA-jp3WBwBU9iiSS0cu4NlVVxTTJOt6HGANArvyWQI3QWOHwwrSTTtb25qmzHxu-PJlk0Dpe1Te8NiomXk3GK3XX4u2-VZBREgoUe2xRlGuu6VaZXcgX9wHnO_IUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌زیبا‌وتماشایی‌ازدفاع‌های‌جانانه مدافعان برای گل نخوردن تیم‌هاشون در مستطیل سبز
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29553" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29551">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4uPfS9GFZbQlJZxA24oBeRReS0sSzdj9AwMq0ejEiZItzZneZmSqX6zOgkT-WdsM95W4Hqz78r-32Pzzwy4RFvee3pJfHKb7AXzcwX7-PJtG2jcT5OXkT0a_NSTmG9aXoBor4ifSe_ajTXC0l-oXtEMg1VE71LTbGLGWK8RQ8DBOXogp6c-WJ9Nkw1kLhQcfblTKcwSkK_XqVlO2Jbdm5-mNBSV4BnqNZqkHReMPSdz96UCX-_XXrsct1EseLQN-VOOkCxXuGLeY40k82bSG5aRBtN9YKGj99ihsVrv8wedXk9VqMYKAn1-gA0XCOacgJZ1r3cvl6O1Sb6bhi5-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روشنک‌مسئول‌مسابقات‌لیگ‌برتر:
بعد از فیفادی و بازگشت تیم امید به ایران بین هفته هشتم و نهم بازی‌های معوقه هفته هفتم را برگزار خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29551" target="_blank">📅 20:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29550">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
کارشناسی داوری دیدار استقلال و پیکان و دیدار تراکتور و استقلال خوزستان با مارک کلاتنبرگ: بنظرم باید برای پیکان پنالتی اعلام میشد. هر دو گل تراکتور به درستی افساید گرفته شد و گل‌آبی‌ها هم سالم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29550" target="_blank">📅 20:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29549">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUQg6z5CpO4cXTltnU3u2qYTXnj8W_Ymgn-14XbeIEL-I0Pf6L7KEV8ih-lJlmfW2wjZXB2o7SKobQVo1uQbnbhd01rei-rhyv7baGH4JQ7iT17yHmZt0GcgItSp7IBrQtQ8Q3SknAk00WylYKni6zmynRlwpNfBdxwR2drT8FivWprHZM-RjP81-6LAtdTa4f3UBs1DlK1YE9StpyUK2txJGiewMApC8fDsbCHInkJozq-Pythcl3u3uXvxDJjmdwU-LMcZ3Pcf0HpsW6y4_ZzL3OHrjbixMUjA_bb3XRe28bvAOcksvWKlTNrJ8qG1UJpaWE_VQmd8TUl5ee5WTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نشریه‌فوربس‌گفته کریس رونالدو هر پستی که تو اینستاگرام میزاره3.3میلیون‌یورو که با پول خودمون میشه حدود  910 میلیارد تومان پول میگیره. در بین تمام کابران و سلبریتی‌ها اون بیشترین درآمد رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29549" target="_blank">📅 20:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29548">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1pidPXX8Cp0r9Gf3GlOsFkQ2EXpt7bsR8zghEj_FzM_t96PLUaT_UfLjWIqwtYoCWklE9a_XS9_vZ_AEDCWZtSMzoHFqjhYQO2tYmdu1ZvWXACx5Jd-1L0qJMVXOpxZC3EispZpKenyoMFRPn1UgiYjGNDtzUridazVXrXfgpdObd11IBi0M9A1D8rq-s9hO12LZV36X36-dxW6g64-f_7qOIZMfUDBDAs2wajckLzxZlho7u5y1JMQSRhjlyvWbWHJeT13_vo2l1KUbB7uoYpEC41xYxaRxeABV5rQPh4PFfOfi9bEm2eQd9Bq3D_yXuNJ2wwZTs4l02RLdJsJAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
#فوری؛ فابیو کاریله سرمربی برزیلی به فیفا نامه زده و اعلام کرده من پیش نویس قراردادی باشگاه استقلال رو امضا کرده‌ام و درخواست غرامت میلیون دلاری کرده! گویا پرونده استراماچونی دو به وسیله جویباری و محمود بابایی راه افتاده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29548" target="_blank">📅 20:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29547">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkmFDXkWElT69zUTZJEeDTrdPcs3mJDT7ft2gTm9YsduavPVjhxtV70Y1VMFsjJaxgaxn0vfEkyeypKggEc06R16fsU2XbQdIkwj_TdpTcO4rObVIsyDmq-hhELkweF3_b-mDzII1C-MMWrLYD9NngkZQ7U11m8bXUB8pGmZqVwxwi_J55n6Dt7HRkwAQ7Lf4CKoHZ9-A_O59jLGNAUF879ymgCDbi4j5J8EMraZ6xydbYRt1O5LeCCuUQAS6ksWqYFkFmKFuFPwSQgvceNekw9sgqimqD8cypdBJbEMq_fOmY1k9ooi0kGF61WYjnSNKypqpNqOw9ItYFWchqb17Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق‌ستاره 29 ساله بارسلونا با به ثمر رساندن شش گل و یک پاس گل در چهار مسابقه بعنوان بهترین‌ بازیکن‌ماه رقابتای لالیگا اننخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29547" target="_blank">📅 19:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29546">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlnm_lMZ5DfzVT-Te4DpfwW-ETkSWK7pvqGi_FLDcWcIwEd9ERnoC4kZCGqY5Bk55kxGZwtAg_tiUfdVr8eJF5xQj0cP2uGJY80pQmqklva9sbpnZFRXaCbJEl-wHWpxSbQnUs1_6oHKeSaZ21uUNd7i3ImVRw81x1SOGoBiBsy7L0HGe4kNXpbDHEBMhIoZWSthwwUHIavKiN_x657xlqVlQmmgXuGXS6_k4pNfBV76su6v2N7bnLXsZ-P8SYfl7c4L-46Q3A1jmz_1h_TU_Xf_C4NL7vThAKD57Wv2Easxk_PSEh4GA1fWa6-l6wYoX5KaAXQ8awUHu3U1x4pWIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
‼️
علی نظری جویباری مدیرعامل باشگاه استقلال: هیچ خطری باشگاه استقلال رو در پرونده کاریله تهدید نمیکنه، قراردادی که برای فابیو کاریله فرستادیم امضا نداشت و فقط سربرگ باشگاه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29546" target="_blank">📅 19:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29545">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkZXf6gmo66hgYujaz8DpCCUxSH9p12OhU4o6wpkA8gbiXyayotJ_Q_YNjFbXeRWdL3MVm_SpXZcn9I8g8-IrD5N_4AA23NpIobaLYvO1vbVBmCXkr5L85miycQvxUqEbyYkys4A8qdgwfDRF1Pzx2NzYsiv1bjv8kslYZNJhZp5NmeDDhztS1tDhX_UJRV8_lXkY579DRmUciWWLV1DgFicNmnt849XcR23GTW73T8jKFktWkb8ro6ANSfry7sJgfGAQleZ745biayeXmhOMBjejN9neiVnv77R3m3s0snWtJFOmARnM61nAO4Ms2Vz-Z7BTI0n5e6QRL1H3vtzrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
گئورگی گولسیانی مدافع گرجستانی سپاهان بزودی قرار دادش رو با طلایی‌پوشان فسخ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29545" target="_blank">📅 19:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29544">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1sMRHUfNCrYI9A3VeHx5Oei0TwjQ-7GulqZ8lqriC6ntNUf3-tjChtyYcQbvLn89aqqmsz-v7vuqZmZIQNb77Pi1fLkJfgenSdkOSHEp2BdC3Rkuy0_03kCe-eoMvl8uz4QjuQq1jOiblQPp-2-WlRx9mEkSGTDJOMunOea1YJsAizONJoUhngfaIuxHI1tZCg-1l1EY_hT-TYovU_mzLabbk5_6ORKiqWA_rm_yB4YKRTHrw8QdL6pW2ZNefYfp8ipa7j4I9grLz1WHoHD9uqBGCP02Wl-FtboOA7MQ1qZHIbesvgGcpUM2QDoWL5nGKaplAUduDJkeXKsOlx7FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریهESPN:سسک‌فابرگاس و میکل آرتتا دو گزینه‌نهایی‌فلورنتینو پرز برای‌فصل آینده رئال مادرید درصورت عدم قهرمانی در این فصل با مورینیو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29544" target="_blank">📅 19:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29542">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2yH0ag63bm7NHaZZb7xqCq_VGq8pxnJFDv_ksHMB_j8ihbgUmEnTYbeuXhFi0IcassXu91XzNLeN9JxLjT_q-cGgJZmz9_7sqxH-4QhwM_ThPer5q3HxQwXLQb6mfZBjt-nrLOWXCiGkFt4d2M3I7XtsvSLXZUxxvPrP4PEVtE7_xs-RdX4fY28GMUVpRptKCjpFczr1V_cr8sCQsdwu4GqchbsKqlju9IdUO7L9hxzIxczPgAfPz_Ufndm4cfCthya4tADpErfM_6Eorl-UhhXscdqZR0W76jjejvwNO9lDYwgpnkWw4Xrn2lhAY06_rO3uCJFR91VrNdA3ttunQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فکت برگ ریزون؛ تیم فوتبال بایرن مونیخ  12 سال و 9 ماه‌ست که در مرحله گروهی دور رفت لیگ قهرمانان اروپا در خانه شکست نخورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29542" target="_blank">📅 18:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29541">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDLdPmr0STzNNHr5jGdvNbcriL4rKUPOc8gBsqwIHE_NyV36XHeXeWscdyF9fFJYoMENzblPUb_iySYsENpRbgSWMTNqDOXITpzb3DF6_oGiKwJ7gM6w2_Nv6rXRdBWglrkybNvGD7UTcSYRji-7sEYVTTexzRtit4O0s3Ugpcozeij_jP6hU3DUywK1g5AvrlBSUaVt007rDihJxfzW2Y02ZjoZ0XXcRfO0tIfwXF_YjdNlzFfh_GW2-N0dMQDx5sUNYzPph6ZILT1Ffaji4sl1sCtVs_OajXGeP_ui_yIpaZx7S6xisQt61G_rIPHaJwu0eWJR4pUDGx7BidDvcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
#فکت؛ ازشروع‌فصل‌گذشته رقابت های لیگ قهرمانان اروپا تاکنون‌آرسنالِ‌مدل‌میکل آرتتا در وقت معمول "۹۰ دقیقه" متحمل شکست نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29541" target="_blank">📅 18:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29540">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pszf6bWzY-G0bdNKFQR_9KYBh6m8m8CzveDVFfxNzQ7Wp6UscvcQPlv8uORb7XrO3pcn1n_zA14-TGhVBQ_8gAu5g5gE_N5L9Z0FUbKqpmcwnsfK-3_JMsuXWj1Mn_8CQT3efLt3oa9AbmDIejN5PAgXaStMIwKCwAS8Aq3gEBxPFzOsYtj-yfWR5J9FiFWsBcJ-y98s466Yuj9TIZjCyZV7BMx8fFJZkWBRX7mp4wI2neSt0nuEeN9LnVd1t86DMokcP7gp6CFNKAm0Okd2Wya6_jUxM1CaOIkBnYhnZMih8HutpDqTfnDvgnzLzLyl_d2Q63zRgZXFcJy8NCACKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در نیمه‌نهایی جام ملت‌های والیبال آسیا؛
فردا تیم ایران ساعت 10 صبح به‌مصاف استرالیا میره و ساعت 14 نیز ژاپن به‌مصاف کرهای‌ها خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29540" target="_blank">📅 18:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29539">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57bb43418d.mp4?token=cE34AMB19qWIztXYHp3u_BxRSfg-eJXRNV0N9LNgX2fwdWyVy-7rprIgjejk7Yx9wbu4Ke1_zqlXwD2lieei2mU9-gVDedq879tzTevsdN_AI06xuIpJW_y-NL5fAMkUdixfetMFN0RtA9lABbvjMgBiJ-ff2f19ZlOJmjVbZhLVNU4JVZejtBIzy1pF1aSTDK9ikNSXztdUSEeGr6b5i-q4wL1U2ZpKJxwu5LRyNacXYP1QOn4VlZ8YEmnJY98-KGxxrwIargWlvaLIs2l4LwKOAPqwz0TFFs8pPjifFiDHjyTcGJLFrs2Xd8W_2VIp-J3AYbVmZzvO3jGTq4f3bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57bb43418d.mp4?token=cE34AMB19qWIztXYHp3u_BxRSfg-eJXRNV0N9LNgX2fwdWyVy-7rprIgjejk7Yx9wbu4Ke1_zqlXwD2lieei2mU9-gVDedq879tzTevsdN_AI06xuIpJW_y-NL5fAMkUdixfetMFN0RtA9lABbvjMgBiJ-ff2f19ZlOJmjVbZhLVNU4JVZejtBIzy1pF1aSTDK9ikNSXztdUSEeGr6b5i-q4wL1U2ZpKJxwu5LRyNacXYP1QOn4VlZ8YEmnJY98-KGxxrwIargWlvaLIs2l4LwKOAPqwz0TFFs8pPjifFiDHjyTcGJLFrs2Xd8W_2VIp-J3AYbVmZzvO3jGTq4f3bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌زیبا‌وتماشایی‌ازدفاع‌های‌جانانه مدافعان برای گل نخوردن تیم‌هاشون در مستطیل سبز
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29539" target="_blank">📅 17:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29538">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TydOmTZFVaqSYnD5SZ2W-WjR64R11oGiND4m59niKKG54KYu9HB4lANp1GLn7usqaakk0QKZSYCZyAyMbNzrg97XgftdlhG9rtpWwghL0wifTWzV7pw3X8TlbNxfs4besf-QJVQ0frqcy9LcFPxpUCiB_XsyaUvwHWw2SeMRIeuxnaVpbbNX6xESS5qA7DgcvoQIyuDZ4o_AK86Qpkt9LRsrk3V-gXSfhCEJIDFQ-WKpaidoOMNdxiTBlEKi-Wtc9ewjtqfdOcnBFNHt-vVdX07nl9ylZDFFu4B2PZWf3c3S-l536dYcNkHcOnW_RImroa_leFcmlPkWt7HQJoMxlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌مهره‌های‌هجومی‌استقلال
🆚
پرسپولیس؛ تیم مهدی تارتار تاپایان هفته‌ششم لیگ‌برتر با دوازده گل هجومی‌ترین تیم لیگ بوده اما استقلال سهراب بختیاری‌ زاده هم عناصر هجومی خوبی دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29538" target="_blank">📅 17:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29537">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8dddf4f36.mp4?token=TPkP6Bw5tBSL1p2ci85LtxQ1tIq8fBXhtIB5R3SOULUy7xlNgpOELvlO8erJHOPL1gwj_0zBsDxJMzkame5gXM6WBIZk-d8Z_6MJhcvMozfZ57Dlj2e4l7qdwdSaCXAzmcB-ta_7srDukpcgHGEV6PSt6-wm0TSZ3mwvS9LbKJaTMJMASDxriWZ-ZYXJaPiMc3xL8mvmoNVdDDlOUerpFZNcjBZkwUAqb10LMqg_6iUrzC76YxVPyhVlZtTN71d5Jv06ca5wMw1g20lLsFZKqrI1ZuQG48Hw_jbGxnbBZlKK8pImvmMW7YuqBsPWGYhDO9KvjJBIXD5PR1UrQ32uQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8dddf4f36.mp4?token=TPkP6Bw5tBSL1p2ci85LtxQ1tIq8fBXhtIB5R3SOULUy7xlNgpOELvlO8erJHOPL1gwj_0zBsDxJMzkame5gXM6WBIZk-d8Z_6MJhcvMozfZ57Dlj2e4l7qdwdSaCXAzmcB-ta_7srDukpcgHGEV6PSt6-wm0TSZ3mwvS9LbKJaTMJMASDxriWZ-ZYXJaPiMc3xL8mvmoNVdDDlOUerpFZNcjBZkwUAqb10LMqg_6iUrzC76YxVPyhVlZtTN71d5Jv06ca5wMw1g20lLsFZKqrI1ZuQG48Hw_jbGxnbBZlKK8pImvmMW7YuqBsPWGYhDO9KvjJBIXD5PR1UrQ32uQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلزنی دوباره شهاب زاهدی در بازی امروز جوهر داراتعظیم دررقابت‌های‌لیگ‌برتر مالزی؛ این نهمین گل زاهدی در تمام مسابقات برای این تیم مالزیایی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29537" target="_blank">📅 17:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29536">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwAATyFbBa4Vg50TXAR4hKfLN4pBGUz-_f-IKzKYE6CiBn2YlDg6eHLFhmah0W5-yivSF8rI4UqNpALLJxhf-gYBlCTld6J1VNJa1csZzqQqObnQFUauezy0Y7uDDIOZ76ms8hV4WI0mH6AMQiXmXNy2AAUDfBzIKRGCASvx90Kgqt9PaRM7CRyoJIyKuZliAwq36NpbfUSDT0BMtJo69_4rA-PRFDXxPtoHNkHIiaS_w94FoCYAnlVIwHm3yidqvKzYhXnH1jRS5ULCT59VvkMuInwN324BaS9o7zsWmpMg5wYuF3TPn1jhtXE3TZehCxy2_TAONeeQ49y0xOXuCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه کامل دیدار‌های امشب هفته نخست لیگ قهرمانان اروپا؛ از آتش‌بازی آبی‌اناری‌ها در نیوکمپ تا پیروزی ارزشمند آرسنال در ایتالیا وبرتری لیورپول و پاری‌سن ژرمن مقابل رقبای خود درگام‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29536" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29535">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeUjMqs-5Yon-adPjp4ZBYrVRwqKwpircvIz11ZN6xb_t45HdIK1m4k7yr3qvigUeW9xyuc1e3GIaTIIIZW-ckIXDU8UtR6-C7YBW2bpFFEgkNuBCdNJAsnB2-0a_MQS5KKjT2wzBcldc08O0iks392ENYp8cQ4MEbEbVUvg-nDupjw_Nbm_zOuj8PpAvQLg6gpKHyEY6BRZ2T13NUKvJBBmu5qikCmVd7v2fve4Zz9WZkQd3UtqgG3Zv36D-dkZcG59odrlw5vd814FZZ5yM-oqXUROJX49qecp_YTMWFnoOueA5hfNGLqFurobci-pRu9_hwYZahPCDFQZ19Xm8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کار انسان دوستانه یاسر آسانی با خرید یک خونه برای یکی از هواداران استقلال از زبان وریا غفوری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29535" target="_blank">📅 16:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29534">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CU7k6S52V1Ed1_NPANVGy3BVZLdgOz_-DMfvGcFvG5S1pfHTa7HRu3ZLBBL4eh8ivWb2qngwL4AQLueRBqPW0zDCyP3tOj509Wtc9s7qxb2An6QDyGA9xnKdpAFznzMqw05ExpCNGhwEnOhBv-z3SF46CXrXz2MhjEEe1QxCugtsEbSBA0i-NyP6mc1OlW6NjsLkW67thQvNO6cxLBvylMUMCaTdRCwmuzQk4wh7ChTzd_jxfrUtZKDSflV-JYb_XZEgmXjpLsCkbx4nxpHkOkNDCN_69AfEsN089LSARfI7wOcJQKn0PhaBLpMM6ObKXeufOxapDW95KLDs0LDp1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به گفته کارشناسان؛ علت اینکه فوتبال محبوب ترین ورزش‌جهانه‌اینه که شبیه‌ترین ورزش به زندگیه و دیشب یکی‌ دیگه از این اتفاقات افتاد. دیکتاتورها وقتی سقوط‌میکنن که خیال میکنن دراوج قدرتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29534" target="_blank">📅 16:11 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
