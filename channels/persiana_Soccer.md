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
<img src="https://cdn4.telesco.pe/file/Wa72znTc0EAiX1Q8iXwNxy3w_zHlndu3ObAUQKA4MG-C1kxsL0LOidTFuojE5rkx4eoK5p-4radGtz0bUugbut2t5ZPdac8MCaaEXdcrcscvfq5g6x12FMhYrMwru0mYBSbTqCH0GRK773fCkTAlOCeeZr8eSkgYa7zPUD0JbN8fJu-PJSEemJW0YuI45VJhEI6g8774upu0m_4n_AjoMxwmF2MzDBbnATW-2h0bFMv8gljjuT_G4ndRzirxT23jrijHlsyGsxfhaBpoKRjzKyV5MYg0bHvt6yz3AECC994SLXAam39sHucohv69tNOHkzqSK0Wo5oL2u5ziTEMm7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 519K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 22:38:00</div>
<hr>

<div class="tg-post" id="msg-29701">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqlx8WEzMrxAl3cwk5pzxsDI9J88JaznMhnr5YqcQsfmVc4OvYjehRouqxe5V5tKIPqTW5_Ek1fjKxw36oOVxZw4iVUgffANYNGj60rVH58AlUIYnShyH0KT4J-sZaWl_HumuzU_qa0ZgHK7rZJ-ud_OYSYto5U5tCcy3K4mD-d6hSQrWBBVB0sN1nLTAv_vpVzgWL7V9gMXqHlW_GcavwjiHj_TwGPFF8dK-JKyc099p4G-HboVIkIN8W7PJOuonC4wu8rPw514QQsAAYlzoD-lT7OfP9rEabflAgwuSXBya5wUiZ7raz8jvoUz8HAef_WJFIBjIXO-ODgw6XGTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امروز عکاس‌ها دوتا شات جنجالی از لئونور ملکه آینده کشور اسپانیا درکنار شش پسر منتشر کردند که جنجال‌زیادی دررسانه‌های اسپانیایی به‌پا کرده است. عکسا یخورده مثبت 18 بودن تو کانال دو گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/persiana_Soccer/29701" target="_blank">📅 22:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29700">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eb0365ee.mp4?token=E89YPrksJ-aw1UIEmK_lGQ0SUO0Ltpc6mQp2wyhWMn1JDra46-Pl2lXBTZ9Q-tg9IS4qudfBANzEbzZFLPhKjFh7MP4IVLXNJA4Ahv6YH3Os9bvCJ_wGOtF_Ke_80Q8xrphXusiQbsUBm7mX1PRe79GqecRYPJuDzPMhAFx7mIbg0oi9XQiGTpMF7LOiwdJS2vpXYh3ji1DWoao5_oRqbTWuxnUOnRCYAqkFMHohMDLNU5efjNONc3kB1SkFlpN8HWOwya3Rqg8L8qGwgopGUIprdUC-Tjx6gDMgA_S0iqBzcgVxXpqwz5aAT8OYhFR23b-FV-GLkzDS0JApw8B3MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eb0365ee.mp4?token=E89YPrksJ-aw1UIEmK_lGQ0SUO0Ltpc6mQp2wyhWMn1JDra46-Pl2lXBTZ9Q-tg9IS4qudfBANzEbzZFLPhKjFh7MP4IVLXNJA4Ahv6YH3Os9bvCJ_wGOtF_Ke_80Q8xrphXusiQbsUBm7mX1PRe79GqecRYPJuDzPMhAFx7mIbg0oi9XQiGTpMF7LOiwdJS2vpXYh3ji1DWoao5_oRqbTWuxnUOnRCYAqkFMHohMDLNU5efjNONc3kB1SkFlpN8HWOwya3Rqg8L8qGwgopGUIprdUC-Tjx6gDMgA_S0iqBzcgVxXpqwz5aAT8OYhFR23b-FV-GLkzDS0JApw8B3MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/29700" target="_blank">📅 21:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29699">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKAFajkbwLw15KmioZJMysYoPIcMgTODvQSWaTdJ1z_2N9s3TwR6lXZhEBo-XnSbV0HcyvUdjjGZQMaeg0UTn2K_gWjwtMH71iv0gaxjlCFh15da0rUIUh1Lyyf7ZzJJi9q-cSj5BpluAAkeNftWRMslWi7nnUACmGPAbzyjGMgOBSYvergVB964wAmUawKhCGUdyARySJHgIFP6PrdyF7FFojkjImlxOGs4K7xj6RdQ8LFUfNwt081l_sn3omJYyXIimWpZQDk8VEXROBCVDHukLWTXl8cMya-0oWq9PJr_W-fGP3n9KmM9WEVc1kJ2GdrUYhcTF2ZaAqjtkPHL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت بازی فردا استقلال مقابل السد؛ نگاهی به تقابل‌های آبی‌های پایتخت مقابل نمایندگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/29699" target="_blank">📅 21:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29698">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4GkSKrjJp9_V13opeTTJPV5viJDQFcn8KtxbNQ6mvrayt6EEhxy3aTWt59DydbTTbaOCsHGXHW3axoYVuXfapsLM1j-vH7L_rXDN2S0r0IOWcHQbIjDq723lpxBaW2K8_iU5FUSDwWkr88KeQltyiGjOFqPmwqA4OwLofJCsAqu5ohryT1lAawlsQRHcBlRpnhfelEEWowKg8OmVF1QdQ9CQn8MGukzB4K7aNLsNQV6kJPs9xySBOEWno3hg_v97CkDApS_JlTKjT4Q0NEBL9_Q99QSC0m7-ZMciHQoFvwTQI4oi80Hv0vB5EtzkTgzYD0PJ6tcrzmyYwdnOr9F4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی به توپ طلا نزدیک شده.
📊
عملکرد پشم ریزون هری کین در بایرن مونیخ:
98 مسابقه، 100 گل‌زده، 22 پاس گل، نمره 9.5.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/29698" target="_blank">📅 21:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29696">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrvYLYGZicYmBODzD-XRCvPZb_Ek2vO5Nns_nJv8K0l2B_DPL9kCo43h-gumixdPnaH3COgRtsNvgbZP1_CXt4vESeZchidRlYn6yNzhaKhlD_5Z3tTd9SXh284GS0dnF0Myf3ysYx4SpqTPvWg4PPAI1f55bwxRxlsnzSanDg5H23p20MbtwN9q3XSkjbnCf3XxJq3J-SicAc_81Q04AcDY3cIoMJ-GyWJ3eMC7ZhUg_XAPqe_FOzInW8MRAlOIiTs0s2vU37pT-2zg5aDh-dOk0if_S0iWFPgGo3PWTw8kt9GVsya4LCngv5S3CZZV6d5g7BewDive0FKIL76P2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/29696" target="_blank">📅 21:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29695">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f40791fb.mp4?token=OipcAdeYpyie4UeH7Lo3oXYrmc_czspluF4GMyFdy_gshGS0bp9YcuYeJOkdp5swdi7XSFu2e_rsjb9leEzYS2bKDHmrw5oMM1wmk6mS8HTF6RdRbJpjlJ-yxah4xTQHifJssNWO0pxLqnJagADW6W3QVn2HnYekxsdf9faJphjRd7U6FA1-VgAEETa6WhIX9FdMwKgWkmmHqr5n8Mof4dABQlA9Xop27hIprkreYVpDgIXtGK-L2_OCTaT_THDzZcFqWmD7rcLfW0dMzHh0p4iTKFS2aTHGFCGqHjC7fTdTY4kRIlmLRLe6CZXdw3XFD1WVDOMj6STZzZCqmK8dox67q473OKQ-hxTfxB63hA7FL85MoYd8b7X67ZbIFQVqu8RQ1hvV5d3fdN-PXZskmSzaRkOWB2EmcFR0eKSoTlkqYhIoB0_L44IdcH2vDTaAwb6VGFHD90vZzQ7HtbuA-InueGyH7ZF5I5mT5wKzfmxtLuWHEU9MfU9xneQnQcmBNe4pZBcWB8noXw1ZP8Jj4tcUAIsttksphk-DB7UAgmWxGfLz7WVCshgCqzucHrVo16yKaScgjby9G-d7w6Rnixt6IdNq5xplHuFlHMarS2plrhxXdVsLdoBpNRhJt8ooH-832JuOo01gKJHPvCjHaC58U0PcL1NrU29n9DBRDdE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f40791fb.mp4?token=OipcAdeYpyie4UeH7Lo3oXYrmc_czspluF4GMyFdy_gshGS0bp9YcuYeJOkdp5swdi7XSFu2e_rsjb9leEzYS2bKDHmrw5oMM1wmk6mS8HTF6RdRbJpjlJ-yxah4xTQHifJssNWO0pxLqnJagADW6W3QVn2HnYekxsdf9faJphjRd7U6FA1-VgAEETa6WhIX9FdMwKgWkmmHqr5n8Mof4dABQlA9Xop27hIprkreYVpDgIXtGK-L2_OCTaT_THDzZcFqWmD7rcLfW0dMzHh0p4iTKFS2aTHGFCGqHjC7fTdTY4kRIlmLRLe6CZXdw3XFD1WVDOMj6STZzZCqmK8dox67q473OKQ-hxTfxB63hA7FL85MoYd8b7X67ZbIFQVqu8RQ1hvV5d3fdN-PXZskmSzaRkOWB2EmcFR0eKSoTlkqYhIoB0_L44IdcH2vDTaAwb6VGFHD90vZzQ7HtbuA-InueGyH7ZF5I5mT5wKzfmxtLuWHEU9MfU9xneQnQcmBNe4pZBcWB8noXw1ZP8Jj4tcUAIsttksphk-DB7UAgmWxGfLz7WVCshgCqzucHrVo16yKaScgjby9G-d7w6Rnixt6IdNq5xplHuFlHMarS2plrhxXdVsLdoBpNRhJt8ooH-832JuOo01gKJHPvCjHaC58U0PcL1NrU29n9DBRDdE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
هفته چهارم لیگ جزیزه؛ شماتیک ترکیب دو تیم منچستریونایتد
🆚
منچسترسیتی؛ 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/29695" target="_blank">📅 20:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29694">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkVJ--5FbPp8gqvG0lYuT9eKk7eawAgehHQJQKfQKQVktlnkBa_rAqZsaQ6fOQ2tdC45aaS_PpGpKGQ1hkEujOjL_YVPLMg0P80dUOPLKQLLc3sZv4i56chK84GLPOs6j1BD4IOeeEgpxaW-Jbfrqg-FGJR0bfzLSbRzN2KRt0dq6k7N7JQFzGulEEV_856M-l7fvTJdbbY4REJ67dcIhZJDhecWcq0pwgvsHpG3Pk-SyNFHkaJ4SKulsGjtOOozwMTSIivguj4VnTmpadN6tRgLOZZOHqTDYcs-RgS5jz39dg-nkWUNJsWau3gfPL40GvEZM3aYXrnVJB0PqqT4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب گویا صداوسیما بهش برخورده که مسعود پزشکیان گفته بود تلویزیون دیگه ارزش نگاه کردن نداره و قراره‌که‌از فرداشب‌مجموعه جدید و جذاب امپراطور دریا هرشب‌ساعت 19:00 از شبکه تماشا پخش کنه. بعدش هم قراره جومونگ پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/29694" target="_blank">📅 20:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29693">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HugoVNK-GMNk2wFnmSmXinAcQY6MeECPEjK8IgsMjVzxXkr4sCml0HCzD46lLJLGNMtkffmZfsxtGpJD-FjSV9g3r0zlBBAo5EB6mTHJqmHzo5M4zXNkQzYSMnnKu8_oVfO89NSZ_3by-4LdoNZy21ow7yeVSFS6VTG6ieD8gME4J6UjUuvycWfWXrhCkjKN5e4nhyJj7XJVOTNp4vViTp1musQ3gqAMcfSZFfWtEelQpV-iLyiI5iSkst0sIl5WRdYEtG8O2yII6MXwLYggQYzS42Owy0yldbhpnH7SmV55enqlgvH46GtGkzFINRTz7nFe_oJdK3z9HakfcDNRXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی و عجیب اتحادیه موبایل ایران: مردم به‌هیچ‌عنوان‌برای‌خریدموبایل عجله نکنن چون قراره خیلی قیمت موبایل بیاد پایین. صبوری کنید!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/29693" target="_blank">📅 20:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29692">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ad168b5f.mp4?token=GxQTBfmUXOmkSzB85mpWDKb9gmFTlt4f2-tdk4VL36L0dBMS-oRjd-YW_xnkU9sF4f3cZC3MKzsnlYw6CkRIGKdXc23x5Wx_c8qXSxk1ewQkaR8PP3D9ytQYKpgIUV0usp4hBhUNQVq7OIoXg6SVXRmuxAJH-zyzZ_lbITjesC8JryWU1B-HkCqbWkv5LDiNwd5Gkx0zVJ9jFU3QX57sU5LNVLKX5x-XSYZ85l2dGADmss1Z_-FbUpyBVHlIHwhdeS3KhsYJsNhdTG6jieeyZxc4t8N4AM0jv6-PFTWbSzy6SEFey9pD-5wXI60uMAZqX7YcgpA6U2rQDJ2h6OvTfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ad168b5f.mp4?token=GxQTBfmUXOmkSzB85mpWDKb9gmFTlt4f2-tdk4VL36L0dBMS-oRjd-YW_xnkU9sF4f3cZC3MKzsnlYw6CkRIGKdXc23x5Wx_c8qXSxk1ewQkaR8PP3D9ytQYKpgIUV0usp4hBhUNQVq7OIoXg6SVXRmuxAJH-zyzZ_lbITjesC8JryWU1B-HkCqbWkv5LDiNwd5Gkx0zVJ9jFU3QX57sU5LNVLKX5x-XSYZ85l2dGADmss1Z_-FbUpyBVHlIHwhdeS3KhsYJsNhdTG6jieeyZxc4t8N4AM0jv6-PFTWbSzy6SEFey9pD-5wXI60uMAZqX7YcgpA6U2rQDJ2h6OvTfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
دیدار گرم امروز زین الدین زیدان و سرخیو راموس دو اسطوره تاریخی باشگاه رئال مادرید بعد از سال‌ها در حاشیه مسابقات جذاب فرمول یک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/29692" target="_blank">📅 20:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29691">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OA1yYCurRrAcRdaK855BBk3ukgone0HCbrJ54xG9mAU9f93ruYKqfU3PjMnoWWQ3-pz1xHyll5QmZwG7p_pRZ4QLSnvx0qoqc4fQEvc2-dcKkRX7xEGoq5bi8MxY-D4jHaS62O_Wwk8MMTmS7bzvxh0alaWWDGxF3RC4OUmgMkTZN0rdF8KXcB8o1BKZKFTLde4Zj-VjUxZmoC-6ttL3s7h-5_gaQg4JLOCM4T1sXYeFTDi_aAYALjUWDKYytX9VEq6gh9tr7Oagj8c8NpLQM4lOGbcrIt6Hn05q94h0lgtsIGV12ooqXqJc2yFSm6sfWaQmU9MaIG2VM4FC2LMhMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
اگه تو این اوضاع اقتصادی بد دنبال یه راه مطمعن واسه کسب درامد میگردی زود جوین شو
💵
💵
💵
🤩
تحلیل آمار و شرایط بازی
🤩
بررسی آپشن‌های مهم
🤩
چالشهای متنوع همراه با جوایز نقدی
💎
کانال دارکبت محیطی امن برای کسانی که به فوتبال با چشم تماشاگر نگاه نمیکنند بلکه دنبال یه درآمد مطمئن از این راه هستند
🔥
💵
g22
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/29691" target="_blank">📅 20:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29690">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwmTWrFhk2xqem0xwMasBHQueI7RMsK73fI35AVz2h57AYELVGHNWxT3XmsixNVgaC2-aBf6KWGBYdw1WpkA_pRTpvzOTY_R6EccZ_RqP-2xaS51y1xGYK8Fk9bmswdPGiTkwT32xEKe7HynxZEfKoiBjNk3hnNeCkxdlk1tdX1hccr0zth4dGmHZ049OsVLLecvapUVHEkw9OoEUmX4XmRGcqbp6sEMkKI8oK5JB9DIA1VJfmANhcCb91-V1mrP3qk3j4LA4yFsF7Yics51jT93icAHiCrN_AoCc7mZINhqvz8QfxbX3IBTeBXm6c_GQ68HdM1VAO7Squ_XIfhUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
🇪🇸
نشریه ال‌ناسیونال:
فابیان رویز ستاره اسپانیایی30ساله پاریسن‌ژرمن درخط هافبک تبدیل به اصلی ترین و مهم ترین هدف سران تیم بارسلونا در پنجره بعدی‌شده. رویز از یونایتد و چلسی‌نیز افر دریافت‌کرده اماباتوجه به‌رفاقت‌نزدیکی‌که با پدری و رودری داره به احتمال زیاد بارسا رو انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/29690" target="_blank">📅 20:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29689">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQjt6KEobYuw6lQQ17Y3eP9WIhcfXknBjQ-y5VxCJes5cvmv1Wz3CYKDRT_vEHPFLUKEmxArmUvQLbrbOu0tvu7WAv-lwllnBe8EPfziel9D4UmfvHNDb_zdF_YY-EHV8otnu7nEgK9W1l8YOcqc5m0FKMO0r1nZsAng5gbzunE1IGTEbcjC_jZcQFSH2iqClnoNJoVhEoZKaBH4JTYcYSYmiOgE4rqJRZGhGOyQPxjTHaCMx5fVfgTpvK13H1tZWAKyw4bajwMmfQWRdiM8DMdJEOp5nYCvl2cUy9hjVINdpdn63a1iOMxDomKm70_JH5y6TD8MQfjwkQO38WMNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
در هفته پنجم لالیگا؛ شاگردان فلیک در دیداری خارج از خانه به‌پیروزی‌مهم‌چهار بر دو مقابل لوانته رسید و باپنج‌پیروزی پیاپی در صدر جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/29689" target="_blank">📅 19:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29688">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB0sMx9Svj14pS459iZOLnTiKk2wbuQAzF0B1vLgVYQtRfdDs1nGLNzQl8rEygP_SnwVJK1mjDklKqtnvlVqcRAA8-Tgrzpi8zkza-dFsEfBHrFDrfmj1G1GReKWKhuNZdIb7qmzK27NmHaskkef64ZyTA-dNrYJFWexhTRWNtGbwYMmm9SyUJLe-pmN6pYmI_dzkroa0XPJdBqtbCa_2P9jOaqCnRF4J8fPqKwp6N8qsCe_STwTIBFz97V0RzQMULpO2hdAFyevUOOW79U4xsdQcPxaB5_AlvWIOpGptYmrwAEGg4K1WSfAnftgogsxZwzmBP6B2O1DzRVeTWD5Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب بارسلونا برای دیدار مقابل لوانته؛ ساعت 17:45 از شبکه پرشیانا.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/29688" target="_blank">📅 19:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29687">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wB2CZ72VmkV4o3KqI1KlNNPxlP4wbbHhwxRtiFhAa1ntbw9hfE-hwuUIZcQeKVChCEBrrMHmZIWV0RfaowrenHUR0ubUBE0D74YHs2NbeZCmx0APdbdVLFkiKaZdCRgx9NPjKi6hYjecyl1fRh0J7AJ9QsnhED5tRKkDFJHGA2l2tx2PNbmOOMMIEJOwFdhRdSPwLDhvA6AZFOugSn3nNcPV74TUnh9dvJ5yi9DdgQsP1wmQJCynA1yaBzSQrvgbm8UZ3cVW6FcrYoRC6QTHMO1UuXt8SlhE3JU7PFLONmi54OCGNcmNe1We_eMYU907iAOku4xksgE50MJPI288Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/29687" target="_blank">📅 19:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29686">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4a-hSRkT5236Cfk7MpvK38KESMfMHRn76DyIIVxWgSAltHwkM3JEPg4wZKdJC_6SIXkFF4JrZXZnnOAddWXhIaDS2BPZvu8oAghwdeqVG3nP2jHUIrguNqR9Ggl-umavrxBmve0XVGWeA4aqJMPEbi-PQFkYgCzDJ0iNQXN873eTVsNUGVG-93et1m3cnClKK90wPGlKZ8hJP4-yfsOfPSRx4aKHqh0Mi7dsEEsQM1e6wQqFD_ETBUVtBEHs-AlKSfIDtN43nI3MsYFCSbWSNZOU5x3NAPApDT8JHcWDJnKl1Q9OKjs9qL5kMdx9r4hadisA4DLtOmZbOsFmqrs8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رونمایی از کیت استقلال برای رقابت‌های آسیایی و دیدار فرداشب‌برابر السد در هفته اول لیگ نخبگان؛ این‌مسابقه راس ساعت 21:45 برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/29686" target="_blank">📅 19:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29685">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUSdllg7et3FOMNT1j3bEAjqKX3lsUptkGGoe8yrgQYtm2gt-i7RVsebRyHtAEvg_vgIHZqOuitklO4Jt_urXfA8lkMcYc2fWJAmK4AYuJpWjZH3UKGk6netmx7W6jza8LHzsmQVqav4sFt2ytXZKO2WQvFy_odSgAs0FOWZ8gpU3vV5JavSVm3y1PIzuZz7z-RlGqzZMjNNRYEIDq0GV9tB6iXrUklAD5pgECdsX-Rdax3IhD75NOWEkqc3EUsS__8zCiL2Kq9V9Z7iDiVOreBwAaUJY42d_sAu_esiqXrXYT_fu7kUsW850r_dj-1MvImI3d1Zc9SxFUoee4zKxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اوستون اورونوف در جدید ترین پیغام خود به مدیریت باشگاه‌پرسپولیس گفته اگه کادرفنی به سبک بازی او اعتقاد داشته‌باشد حاضره به‌زودی با حضور درساختمان‌باشگاه قراردادش‌رو تاسال 2030 با سرخ‌ها تمدید کنه اما اگه تارتار علاقه‌ای به ماندن اورونوف نداشته باشند…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/29685" target="_blank">📅 19:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29684">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f29263824.mp4?token=ZODIJNPF1IZ_Am6rhMIzQ9Za41fJIFX8X_2rHcReO6L6ytuekdPmQOhN_L5M1KFC3vyuzxeyfhHBPu97FyZZ-oapEDrZpe_pL2C787P3q3M_p2gn9gtDK_b6c6vPxVE0pJiBLf2WyUCrUfVrJr41krF_Y1sGkcTuZv70oE8ocg3m-a4KgCzpkBQrwXpbP2VUy_ewkFaA36QJwWwqV8RWgi0KvFmKDapDFF-bu7X0fUdcVNf6mN27C0-u1SaIdGoGZWETBK1e0QcPci1un4G6wUVirKOjv2ywb7GZ_ybxRTuTLEy_z8KFg6RRkxpuzNZZA3TRzlSSMUR5ZoXdUT7m2i89N1KaJzXE7SuR9WDd4_UG9QQGUeYfSWTeLUXiwXwI48vhU_XmCi30PMdhlkexlK6J5hzA7owTLz7wHhacF7I7vlNr0vvT9OKU84OdBpS_QeWz6T2kODlVitueT96LkDuWztQpqZe0qFjFR1Rpa9NsNGaVA8pXOBqMXHC1yNPsyO29bC_6_27eFIghxGgpk4AEhT86tmq86rw1_eqKhgMZBoAzjvYl-FN1nMLvuDXYCZxx1nmlfWVqGY0W9s_awPtFKJwyzDtqHwXNgzyQFBMzVejR3OVksGHFHi5my_ti6oS_7m3H6XzsOh6jdKp60pRUfftN0P51WBhlticvZks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f29263824.mp4?token=ZODIJNPF1IZ_Am6rhMIzQ9Za41fJIFX8X_2rHcReO6L6ytuekdPmQOhN_L5M1KFC3vyuzxeyfhHBPu97FyZZ-oapEDrZpe_pL2C787P3q3M_p2gn9gtDK_b6c6vPxVE0pJiBLf2WyUCrUfVrJr41krF_Y1sGkcTuZv70oE8ocg3m-a4KgCzpkBQrwXpbP2VUy_ewkFaA36QJwWwqV8RWgi0KvFmKDapDFF-bu7X0fUdcVNf6mN27C0-u1SaIdGoGZWETBK1e0QcPci1un4G6wUVirKOjv2ywb7GZ_ybxRTuTLEy_z8KFg6RRkxpuzNZZA3TRzlSSMUR5ZoXdUT7m2i89N1KaJzXE7SuR9WDd4_UG9QQGUeYfSWTeLUXiwXwI48vhU_XmCi30PMdhlkexlK6J5hzA7owTLz7wHhacF7I7vlNr0vvT9OKU84OdBpS_QeWz6T2kODlVitueT96LkDuWztQpqZe0qFjFR1Rpa9NsNGaVA8pXOBqMXHC1yNPsyO29bC_6_27eFIghxGgpk4AEhT86tmq86rw1_eqKhgMZBoAzjvYl-FN1nMLvuDXYCZxx1nmlfWVqGY0W9s_awPtFKJwyzDtqHwXNgzyQFBMzVejR3OVksGHFHi5my_ti6oS_7m3H6XzsOh6jdKp60pRUfftN0P51WBhlticvZks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ویدیو آنالیز دقیق عملکرد شاگردان سهراب بختیاری زاده دربازی هفته اخیر آبی‌ها مقابل پیکان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/29684" target="_blank">📅 18:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29683">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961ce8dd07.mp4?token=vBo-D4Xj0G9XSqVWo1Karh6U8B-IY_e9EZq_LRNsJ-oX9YB92lheS8WBSUST3CJpFMGjVL9Vhxjy0RyWLcTM_xFGpcx8xWrBfwfl3HlKtDDluEQRFiCnZzSXrSQ6LrCOjhyyDDFCM193zdwBVA2fqLoaJN1FxE_ymPlhmJIcq5Zp_8bKQ-lNLjT3DagueQuaunMXunMk7QR_h97GOOXLMNNuU-K6jy0Y5-ZsoIiBC68wiAeG5katpHvI59JxiKUiF7mGdPeSsoAzk9v02lQpQxSNiBdLI5HsLJ02_9XZrUQ5VXwkk4tCNbor-lsdK3hj06hT4MD3ilVpbGSWroX17Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961ce8dd07.mp4?token=vBo-D4Xj0G9XSqVWo1Karh6U8B-IY_e9EZq_LRNsJ-oX9YB92lheS8WBSUST3CJpFMGjVL9Vhxjy0RyWLcTM_xFGpcx8xWrBfwfl3HlKtDDluEQRFiCnZzSXrSQ6LrCOjhyyDDFCM193zdwBVA2fqLoaJN1FxE_ymPlhmJIcq5Zp_8bKQ-lNLjT3DagueQuaunMXunMk7QR_h97GOOXLMNNuU-K6jy0Y5-ZsoIiBC68wiAeG5katpHvI59JxiKUiF7mGdPeSsoAzk9v02lQpQxSNiBdLI5HsLJ02_9XZrUQ5VXwkk4tCNbor-lsdK3hj06hT4MD3ilVpbGSWroX17Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
هفته چهارم لیگ جزیزه؛ شماتیک ترکیب دو تیم منچستریونایتد
🆚
منچسترسیتی؛ 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/29683" target="_blank">📅 18:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29682">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtnfJlKORJslbYurrVMMT2sZsk0Wy8097D1C1X7lYtSmfvUzyJ-KY8Xth1SbgsxRyQfd1SqCgaQ7il-x5YlqOUrQdblZE1qxGgNkzwNCpJnOMrNNGEI7BUL1pJcXLAqE63xiTHmithknN4Ap1btxknDG2N8lgFPXm6oZLxx2CCxadcPoFtYX5qjnLjk3aLd64BG92YHQX7NcyEz8zjnQ_I0t5VCioTd0BD1Emg7fLhyTzthcxkjFiDAYnT9AIYOGSEKcBURE1f27KWH3kVKVix_cWs1ysEEHYhI6s9sCtWiW9bqGGdcyv8GldD7qb94yBLu5xl4Kth9c6lPttARuXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم
؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/29682" target="_blank">📅 18:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29680">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flAmA2d4bqVOABfKQFLYocyR2m27199gPE5Wx7RxC0AfrXiUfQKcpJTxpiNehvSnD8NM5g2j0O0A51fC8AgsPUugVJKLjt5_cpr4tiFyNVZk7dMaitv7HLuf5SrjIeENooM7chUCPQCm_kt645epWByIr9b6fSZCDLHZOCk1uKkAxdXI38el0nMhy2adkmXYB4LDcId5eoqMWdM3Q8HdShKlwekCbdPdoUO4n9kWR2k1ChE7YEBslDtk9-29Fwgski135f68HvXK_xfJ135qV0eHAYeS4UkLTTEx6y8StBjfKSDKr8sU2IBm25cu0ez-pTRkA_6HtqHtRJPHdD9-Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/frlAAcxteDmU96_DzqQCGFwvTRdi7aS3HJOrWjJOv9fQBHPuPR4B9EF4FMASfGw5XYDl8ykU6MWEnzjzJDjQPyB6oe6H3Zb3m1bo1TZT5r_gRjU8gu6X79eRTWMh85QEMaI6KYsia3IT2eBErHbjOHe6Bl6Zga5QXodaXl21jCZm_JZrKCNk6uzVjooqt5iPJfDs4YyhLa6PZfXpBQ-qpc9mOiXz8YCY0IYTBnL8lyPSGy9SIVH9_USGDLsNT8WgslfhH4pIBKnIol9WVTCkMpqKs8oWrVvD9RZFXkwNPSTG8WwTPjmlin5iL2AUMUPaJe35LYWnum47nRTWacWP9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
به بهانه بازی حساس امشب دربی شهر منچستر؛ نگاهی بیندازیم‌به‌افتخارات من یونایتد و من سیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/29680" target="_blank">📅 17:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29679">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE3eoS1_oql3rbYMWyqrqOoehfi23gxbEJgT-2-k6e3KM0XqJ0XQ8pTHUmJdSCczl3HO3r1kA867VWhb8Z1h-Xfikx1QmVk_L8agR7uelRdRL24UOeY1KBS8UXnvpt2s4pdox0LoE1_jOlMUMbQ6BDTrfoajBDNfmRu7qObo_OjOUZnynvxoM41oqNPtQWcLh7r3o7dWmRkHDtZ1nEW_dgPhSDe4NoJ-dkNfWZRgtsOC4tRQE-8JdmDkpAhc4J9OBB3flKZTvRcEkujWWgtAALZDjOqunDHxm2Bq4Aj_clt7jRSaooPS68WSPHd4eVKSeHPjEcYgn-Vg-9bTPbtrkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رادان: بیرانوند شامل‌قانون‌سربازقهرمان نمیشود. دروازه‌بان‌تراکتور ازاول‌مهر سرباز است و باید یکی از تیمای ملوان یا فجرسپاسی را برای بازی انتخاب کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/29679" target="_blank">📅 17:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29678">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=GQWV5zOr9ODkhh82F6H3OD_Ayowl_rQ1Svu6h6NIohspcfrXL15qfteyo51hg7zNoRcjhy0YyUYfmD8Ty25sjZUC1rtORbcta9du2bkJUFHzsRYm897sN_qqBuoppJKftZadprBvs_8Dsc3zw-x5LKGNQ4weqGP_FKGs7UPR_1jUL8JMi2uc6JRkTUtTW3BHHZV9QliJROo6zR26Y_miru4JpV5RxwhWyNcML_sA4wjUX28pcjqj6uTOUEz3SGMOLApKrHFFMnMXKDJjvGYKfxcme5qoSl5ULSTU1yjjWwA4fbh4r8fwPJ3XE_CA4QqvudPH9ikohmvpn3hhsKJQETzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=GQWV5zOr9ODkhh82F6H3OD_Ayowl_rQ1Svu6h6NIohspcfrXL15qfteyo51hg7zNoRcjhy0YyUYfmD8Ty25sjZUC1rtORbcta9du2bkJUFHzsRYm897sN_qqBuoppJKftZadprBvs_8Dsc3zw-x5LKGNQ4weqGP_FKGs7UPR_1jUL8JMi2uc6JRkTUtTW3BHHZV9QliJROo6zR26Y_miru4JpV5RxwhWyNcML_sA4wjUX28pcjqj6uTOUEz3SGMOLApKrHFFMnMXKDJjvGYKfxcme5qoSl5ULSTU1yjjWwA4fbh4r8fwPJ3XE_CA4QqvudPH9ikohmvpn3hhsKJQETzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رادان
: بیرانوند شامل‌قانون‌سربازقهرمان نمیشود. دروازه‌بان‌تراکتور ازاول‌مهر سرباز است و باید یکی از تیمای ملوان یا فجرسپاسی را برای بازی انتخاب کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/29678" target="_blank">📅 17:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29677">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7865bde240.mp4?token=Zv4i1SKdjbaewOOqkelgkeyMyco1YouSuTcrkIdb6m6UvtGY3yat8lYb_9YIv1JVHHj-U1Ri1SG-j3z8I6qrLqnYipZYLGejOeA9NQavEiYlhQywvCVaZxKIgu5c31C5Bx-TgafIdZsvgqr2x6ctgph5yGn2mQHxRX9LKZLKvo_31u3ieDwp_JYP5Bcr0pkKFbX_atI_HH9ujMMcQM4cIX1B12CSUm6FeY0duJgnKO0br3RSx7z9X1sESHWz9iBjHnqPsrGWQF6KpswOHu3_oAqG08neCrNVyPFkF6CtfqxS6POGHreMeOfW9LKNpGjwgjGl0WZ1p2VTs8Eo3qko5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7865bde240.mp4?token=Zv4i1SKdjbaewOOqkelgkeyMyco1YouSuTcrkIdb6m6UvtGY3yat8lYb_9YIv1JVHHj-U1Ri1SG-j3z8I6qrLqnYipZYLGejOeA9NQavEiYlhQywvCVaZxKIgu5c31C5Bx-TgafIdZsvgqr2x6ctgph5yGn2mQHxRX9LKZLKvo_31u3ieDwp_JYP5Bcr0pkKFbX_atI_HH9ujMMcQM4cIX1B12CSUm6FeY0duJgnKO0br3RSx7z9X1sESHWz9iBjHnqPsrGWQF6KpswOHu3_oAqG08neCrNVyPFkF6CtfqxS6POGHreMeOfW9LKNpGjwgjGl0WZ1p2VTs8Eo3qko5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/29677" target="_blank">📅 17:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29676">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6h9itWlcCeR9lIMxuwHVWqo51vbTKTbNevPAa-ws-qNKPBhXhBVTN_XRKs8FMlU5Getuj5pdMh4vGJKiVpemcW2BmMOueR-QJjTFNvrqx5wXzCXLaUSPw69CdURXGosm8_X3lplUltCRNQk8rqHqovLtRIQv-hyiLzM5gTuI1kLh0p8HWyxrhDN0376zxqc9XrJZHzmHF5m4WGn1CC7VHJLREpNZQ3m-mJaSeFQNwYw8kcs4IRZVqUzpNKjHPm1C98Tdj-SwNKs37b9i7Nrp7dqtc0x7PO9hgWCFZ_Xagtb4oR9tL0z3kp35C6wpcoG-FiYeON9sqYADQC5XEk3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/29676" target="_blank">📅 17:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29675">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‼️
برنده شدن جایزه 15 هزار دلاری یک مسابقه در امریکا توسط این دخترورزشگاه؛ یه مدت صداوسیما هم کپی همین برنامه ساخته بود که بازخورد نگرفت. هیجان مسابقه بالا بود حتما ببینید از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/29675" target="_blank">📅 17:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29674">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhWn8FBMHtztjhnwoW5kSMOrs14i-OC_nh9ohRLWAwrtdAS7xkiSs6g20gRdsF0-TBthxCgh6Xqn4LfXY9pm3NUraoqVltXfTe1mfEj2YYrPFqMJrTmwy3ntUJrnAXQFdrs8GG-phCU7tRfWU9P9jlNu95-0tVAn9fqolwYerI8ZHZCVGnwP_--V6lPc0J8Re4X4M63dL4sUy0hKWELEw9lQaXuhHGeNRfEbsyv7a_9jffpGt89cqotsyVmJq2w_efVS5qfpvAoXO7gR2N3q0TPInvFfewjgQly_K9FThA-wpBdvJMwuA9oD-SomEprw4moYTmYjmfyLIItvkXJ5Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته چهارم سری آ ایتالیا
🇮🇹
ساسولو
🆚
یوونتوس
🇮🇹
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/29674" target="_blank">📅 17:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29673">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnIh-tPYn8zeGy1RXYUpwAwEBoQkVHLybsIH6pWWZ5VOZj9EsVlDuUn2_-KfzSVHN6AJ1XjsoVgFm2qfHbSjbm7O2ntAleng6EI6J6zeaSB13MD0R_WF4Zi04nkdGFm3MbK6mVN47Y6GrE3zE-vmw_MRxDKmol3VeGWD0JHlTu8-wgzqI_SAVWYb8fGtZRmKK1P42cxfbcgAYqlQ7QSBg3YCDsu1W9WnIwuZSaAw6kLG667iKrytVn7Bs-O9yM4zXkrXCAkMzk-qVhuO1vQAI2srDf3UVetPtNGhI6LG5qoV_DE9Ot_RVcYhOc47W0xfSFpeK67ZLQMhAr6qR8akYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا
|شماتیک ترکیب بارسلونا برای دیدار مقابل لوانته؛ ساعت 17:45 از شبکه پرشیانا.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/29673" target="_blank">📅 16:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29672">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0d75NvDJ3clA3UjlyA6gWkhLo1FOXMmPcurtSwtOTERFFXmWMocOsf_PsCXqrgdmZ_NjaFbAHli-d1hXOXOi5_9zbT_jjmGoCE5c6AY7RkMaNHQvug4GyqwZjNi9gWtkrIft3iXHDMKTkGspmfwrAnGKMbUrptftrwiYFHC_0xOYhF0oyclRrtcuv6l3k_dHeMUv8zz-egg6K551srZIEFKjyEJkZ17P6gkfJRltVV1H0CGL85Atxcp5sKG-ZWa95REWE6IFbKFws4tUncR7JR3VDhB_D5uI7JjeB1OANKZxy76pFSfppEcKVoKM_LJ-YdjSBlCCyg4O-dZ5b_MyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت بازی فردا استقلال مقابل السد؛ نگاهی به تقابل‌های آبی‌های پایتخت مقابل نمایندگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/29672" target="_blank">📅 16:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29671">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/570942af95.mp4?token=MoYbjX8At1cX3BV45POOdZRvfb9gQv5dEDAiYI7l0BJbUdRPGNIFvkoy9Iend2p17DqAGLWtQB7SG2E3tC_QQwcPS55MmB21DEj2inIoO4jKvEEJHJ6RcX1rDih9MDOjVPpZ_uzGZBIAVE8qGvvES_KXQpYnochpkaM8Fzlk7IBOG6MUxCS-D0AL8-AtSiuB0qbVgF8x4hzZzvzIK-8bXQoqFlul3gSny-2BZRmLAbAqmAgOkgw3-KTdP3laH3Vpx2qEjP3ud5Hj9plFy7CEZeYMrL7TpLEPFWW8EX9JWzEcaXKn2spgKaP9azFLOEgaA7ApcmoRCPD6cEe3DgaJlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/570942af95.mp4?token=MoYbjX8At1cX3BV45POOdZRvfb9gQv5dEDAiYI7l0BJbUdRPGNIFvkoy9Iend2p17DqAGLWtQB7SG2E3tC_QQwcPS55MmB21DEj2inIoO4jKvEEJHJ6RcX1rDih9MDOjVPpZ_uzGZBIAVE8qGvvES_KXQpYnochpkaM8Fzlk7IBOG6MUxCS-D0AL8-AtSiuB0qbVgF8x4hzZzvzIK-8bXQoqFlul3gSny-2BZRmLAbAqmAgOkgw3-KTdP3laH3Vpx2qEjP3ud5Hj9plFy7CEZeYMrL7TpLEPFWW8EX9JWzEcaXKn2spgKaP9azFLOEgaA7ApcmoRCPD6cEe3DgaJlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ گفته میشود قیمت پلی استیشن شش که درابتدای‌سال2027میلادی رونمایی خواهدشد یه چیزی بین 1400 الی 1600 هزار دلار خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/29671" target="_blank">📅 16:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29670">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rj5nrCvw74If24WdgY8P2FqiUH0nzTazRZZedD9R1zH72XP6VLIy7oONH9qwYWyh6rze4f58qpTpFnj1I0trEQP-f3821qN6mve4OmFc0bKh8a3QuCnNwDIbMy71Bbd38IcEkBZeeaNi9gxj28kmL1DlGCoo6CXcZDMoCsbQKKkjG3EA6FaYMEW9sKu72Des67Ha-0lvh2lzWieQ40hI-sWuWS4uhzuewnApsvrU_vbF-BvSoUj_wCXpK0vDXH-NwMFC2NMUaGJppxQygyPIRTZ5gvDtaS9pBhypJPuX6hGzIwSohoXGKFCuOKi4-Dfy1qL8BcfxWyVoEiu6_EC-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فینال‌قهرمانی‌آسیا؛ شاگردان روبرتو پیاتزا سه بر صفر از ژاپن شکست خوردند و قهرمانی ارزشمند این رقابت‌هارو و کسب سهمیه المپیک رو از دست دادند. یه زمانی همین ژاپن آرزوش بود یه ست از ما ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/29670" target="_blank">📅 15:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29669">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7GnrkmbTVmZyRyukfsC1NcO9OePbo9IhUXv8M2UsSFp5NRq46Cr917wLEXiLP9Z9hB7W82JZeBmpTILkcJLXFjcrwuPRUoAsBlnfN-WUZBARrsJno3DqWBftMFlpbVGbs-Ls5qj2F4SIqOoQAOu81hJEaHPNg7myqx8nXwMfBpg6Anb5GzESUQXi350mg5YRBKaxp3Qu6-RB2GHiVdw5lPFfAjKYAsVeo1uiSHVQ4X6GLdGRInS4YCZDc9XbYPaidbKqC2x5yrrEgCZPq_1SyaKEZrhZYzfSCk7eRO_d3ehQhopfB3f2huPu6wYq9rtZuQ4duF_AHdL6jIF72AhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های منچستر یونایتد
🆚
منچستر سیتی درلیگ‌جزیره؛ شیاطین سرخ با اختلاف برترند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/29669" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29668">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXKT2DUY36eebBDQMFrKSdDLtbRTsJJyD2VFeeG_r2ohy8M_A97J_bTfA-P66jdP1hDEoyOE3G6KNYKODd32egFOUKBrMTcTa2CUCdJmGy6NnsbmR0xng9P6lukxBnREOUo8lORqE_SOop8BSkjpOMmP934CsHb4AMQx5mJkTT6PnhwgxrLFrywhOA1mXKuPx_-HTkNhPg55yR1_XWcmiHcCVKj8LnY15X1QWXA2hi7iieCpaz_U7AJOUsT_G3aglVy2yvuxw-27UOxKEgkPacg2P4-lcQNyaw7zpkWJ9Maj076eIXFW5sX_jdfyNXQixT6ipBwuIkDwV9j8HmM-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمتراز یساعت‌تاشروع دیدار فوق‌العاده حساس دو تیم ملی والیبال ایران و ژاپن در فینال جام‌ ملت های آسیا 2027؛ نتایج تقابل‌های دو تیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/29668" target="_blank">📅 15:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29667">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f478bf5a4.mp4?token=AqNP0U726F1c6tJ3juMH3yXCMYcvbzNTL0n4nOUYaNDIIi3rU2Eit-1fLxDPBgtYoMrErOLleazT2tU7w30ztzYYceWGfQVL9gLmVoKbQ0Q6OudPVGQuvIEHt26h-m5bbm9h_i89WQcvuzYv0alQ7YCUVuG7mdJ7rz7t0ZoOBFSFWgUoqlo9yt3y65agEiJ5l-D0H_LU3CPZ357doKNcZpeFTPLGRSv-dIIwyXnM7JQRijB7iKX2OLMtmkpjhdlzKPgl5mizjKipXahrJH7oXF-ZojOd9AWZvIpjKLPOiTwYndd8Qa999V8X7gunnPvMPWVk8ZiiWyAyEBIRNT_NiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f478bf5a4.mp4?token=AqNP0U726F1c6tJ3juMH3yXCMYcvbzNTL0n4nOUYaNDIIi3rU2Eit-1fLxDPBgtYoMrErOLleazT2tU7w30ztzYYceWGfQVL9gLmVoKbQ0Q6OudPVGQuvIEHt26h-m5bbm9h_i89WQcvuzYv0alQ7YCUVuG7mdJ7rz7t0ZoOBFSFWgUoqlo9yt3y65agEiJ5l-D0H_LU3CPZ357doKNcZpeFTPLGRSv-dIIwyXnM7JQRijB7iKX2OLMtmkpjhdlzKPgl5mizjKipXahrJH7oXF-ZojOd9AWZvIpjKLPOiTwYndd8Qa999V8X7gunnPvMPWVk8ZiiWyAyEBIRNT_NiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز کامنت‌های‌پرشماری‌که زیر پیج السد درباره غیرقانونی‌بودن یاسر آسانی در ترکیب استقلال زدند این باشگاه کامنت‌های اکثر پست‌هاش رو بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/29667" target="_blank">📅 15:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29665">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2b549c3d.mp4?token=nBDwUtyy9EuNlegMqmLirK-J4GShBNnTN6LC9AFHjF3vyJNFAoEOTagHypWj1OXHCSQQUHfUf1dydKlBXjjY9v4t74NRQH2JfLuVxEi2WDpHJc2jqYnEuHjh0qbKnY-jJKP2EfSSx_GLJDoLEHdnkeRq6X6AKD14g68s4xENmmGXgKeOxNWgMGwSnsXtTNK0fpapWiDiUmWyd_bAwZsQhybA5I10hRcXALxrSr60iKdzngXLsHHCgFcMxvDS8MYwvHVyTFMH0_S0ORqBuMFBxZaDNrvAzx7DOjyTXoATalR5Z-0aBeWzWTdzNYWSuIS9REf7coUmeVlmyyJpMrxA6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2b549c3d.mp4?token=nBDwUtyy9EuNlegMqmLirK-J4GShBNnTN6LC9AFHjF3vyJNFAoEOTagHypWj1OXHCSQQUHfUf1dydKlBXjjY9v4t74NRQH2JfLuVxEi2WDpHJc2jqYnEuHjh0qbKnY-jJKP2EfSSx_GLJDoLEHdnkeRq6X6AKD14g68s4xENmmGXgKeOxNWgMGwSnsXtTNK0fpapWiDiUmWyd_bAwZsQhybA5I10hRcXALxrSr60iKdzngXLsHHCgFcMxvDS8MYwvHVyTFMH0_S0ORqBuMFBxZaDNrvAzx7DOjyTXoATalR5Z-0aBeWzWTdzNYWSuIS9REf7coUmeVlmyyJpMrxA6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو با این حرکت که میبینید داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/29665" target="_blank">📅 14:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29664">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mupLnvTcGPwuDir8228zC9bqfjEQ7HpBp6fDZjFMSRwJ7rU147H9ATvCv2vL1R-KY8zF8gZxEOWLnobaBeM0mixMbqXDwXT2G4k1XjejxpYN9U5DmixMmvkXKDGqe8cNQzfjrXpaQ5ECDgIsMFzpIbVsnV6AKSNM876K09QDd-wBjB_BRSwvrm4wMYkwP1-gSKaqb0-2wV5xji3-vaqwghb8bI3s222Ix1qrnmp5x-sFGwe5l3MGgA7RCjUz0YEz-fCNE6gVYrIDynGnO7NxgDnnLShFWgR3WvW_Ve56vy_p8r9Oc9krbi9i2njRPhmMmPyMma8AUrGdn8XhiENWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب گویا صداوسیما بهش برخورده که مسعود پزشکیان گفته بود تلویزیون دیگه ارزش نگاه کردن نداره و قراره‌که‌از فرداشب‌مجموعه جدید و جذاب امپراطور دریا هرشب‌ساعت 19:00 از شبکه تماشا پخش کنه. بعدش هم قراره جومونگ پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/29664" target="_blank">📅 14:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29663">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltXbbVS0Fp4Q8IEK0Tcubte5uoBdT-BodLu4Ov15dk5wem79YDhpzJUlaLc1psUHdx9Mf-68LDVAgyL7-KGxV3-QqTEIR-ulGt61n-mUMrn02FyZmgiS9fk2JLOeo6UM2ued4GdJoxk95ATrlzl_g1d7S5nIaf82_IR9jz0W-htWw_52lKW5ugCHLwmgYZe8F-vmJShf1uqIX0jOjPiImSSFWgB8BIUSUf7F1os0GVjI3vaIlh34ihH8xzqC4wuHSxcuRV4VzqyZm_VUURmSvd3Md3yMUrXUkFZc3eircfV5duwSl8zt_dFB4fQ4sPpvlkHwyx8f8hZ7bE9K2Xz2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برای خرید آیفون 18 پرومکس در هر کشور چند ساعت کار لازمه؟! خودتون لیست‌رو میتونید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29663" target="_blank">📅 13:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29662">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mm50EgbCqreBxax3o2HlHkVX3T99xrzZKWzeZ4cPVm64Z431lRArKfkGiiASjqOByY4H3ZoERi8RTXD9zfUuAs1anNKABxfqTVQsQKIg8SU6S7y_B1MulxJE3cYBn6Ci8GHqma3EF2fq0xApvI3sD3YFT8T3cfCrVak7F6CbVMX0aSa8GflFNUQssJaDLY2T114Tg-WUG7bkgH5S0sQZo8x7tudPwsYMGZblNc0iPA7laqpnTBRqWNEc5sivHgkHHf-tBjpR5c4z_8wlFrpl99vOyhsgHHjxqx_kR4JDUL9esLSKjxdvIGeacVKKb-ZKHL2flu0EHlRuOo-NsrlC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از توافق برای تمدید قرارداد آردا گولر؛ باشگاه رئال طی‌روزهای‌آینده‌برای تمدید قرارداد جود بلینگهام تاسال 2032 با او و نماینده‌اش جلسه برگزار میکنه و به‌احتمال‌زیاد توافق نهایی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/29662" target="_blank">📅 13:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29661">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TizcT9Yen1h6mdaOvErsq2vf91gA4MYVUpxcMXQklVX1bL6SrEm22khapTJ-dDtcJVHiWd_s0AAOFY4sVuKaGZscGHienieu4wPWN78le5hoQllzYnC832GWXhmoyXczZDdJNyRLBv1kYv3Gns_fMH0qhXWnaIwuXwnXk2VGQllnJBgPZtEQQ18gtnIY-u1J9GP-y2Vlc6L1a_0UKM0F3PIIX-lXQLhOGsUPCB98RJkGZXHw_s4KZHzLfxqX7-5wG5tx-IAX_i2nfJD1dgUwCX_o23BUAk714Q2OjlqMO2PeWpJZkGVvg81qbal2RC31droZKbQTiux-WyCzar_GkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخورد ناخواسته و عجبب و غریب علی حاجی‌ پور بایکی‌از تماشاگران ژاپنی حاضر در سالن در بازی امروز ایران با استرالیا که بعدش‌ فدراسیون والیبال بیانیه داد و از هوادار ژاپنی عذر خواهی کرد.
🇯🇵
ضمن اینکه تیم‌ملی‌والیبال ژاپن دقایقی قبل سه بر صفر کره‌جنوبی رو شکست…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29661" target="_blank">📅 13:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29660">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeWMmqHfHQcHiL2AJndUit_-kPF6bXFPStmoTw_CqG3imNgbtEaVAWduPR9Y07lvwf-jjVcLzrOW8Lpjq9O3ZcrTa4XR0BEImdWP8vU4ovdpJemzk_1VtGk7IgP2UuKTIS3UA_1kQssdO8I-Xgym4CosYiElJGSt2RezoFT_lH8GXn3ym9ipeh0_TWp5NZpPnctF2sJzEuesvy92T99QYi4p-P_55lRQcidJZtFqc-kggPWRnOi1vrJg6kGD5dhn96RP43IM1YDQ-u6VJmuCJ1mmn0CvBq3qBH1lERst2U6WIBJ8Ewu15J9flJRT4J_6WpXZUGD_yKshDLLN6CDJ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/29660" target="_blank">📅 13:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29659">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eab57eaae.mp4?token=NK_jffZK3JaTHBHQLQJePF-mOau9pePIxkLi0f5oVWNufQPpgEFO9YX1F-DAfPuWvjKGV4E0f_VnViUEorprHvfX0ilOL8PpWDouvJL051CLceG1daYI2S4BximN60Gb3PE3GjEk3gQ2ACZM_o9rhq4bvZGdYrm9qMGlK7Z-0i1VijLHkgLBm1D42Ov2v92zv2FMGluCpdtRgo5x54vKwSv4cZiZ6EKPbBWhkelZa9qibr7uSOgEx0kkMyOyZr6ZIlD1t-9if2GXbuIh9dmOv6Xe1MDho6z9X9rLBH2xX3lEAb0C_Xb8-SJa9ZSHAOl8n5hvEtC_xr5UhuoLT6wDBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eab57eaae.mp4?token=NK_jffZK3JaTHBHQLQJePF-mOau9pePIxkLi0f5oVWNufQPpgEFO9YX1F-DAfPuWvjKGV4E0f_VnViUEorprHvfX0ilOL8PpWDouvJL051CLceG1daYI2S4BximN60Gb3PE3GjEk3gQ2ACZM_o9rhq4bvZGdYrm9qMGlK7Z-0i1VijLHkgLBm1D42Ov2v92zv2FMGluCpdtRgo5x54vKwSv4cZiZ6EKPbBWhkelZa9qibr7uSOgEx0kkMyOyZr6ZIlD1t-9if2GXbuIh9dmOv6Xe1MDho6z9X9rLBH2xX3lEAb0C_Xb8-SJa9ZSHAOl8n5hvEtC_xr5UhuoLT6wDBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
هایلایتی‌از عملکرد درخشان عارف آقاسی مدافع 29 ساله استقلال در بازی هفته اخیر آبی‌ها با پیکان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29659" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29658">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHLXi7UKAlQq955pLEKT1107jbIMSX2JCSGpQFU8PmIlHWL4KEM1e0Zgx8hTHssXjwK3VRaSEHcc5A3pxbLusyjNvxF91uoI8615efjaNbqiJpW7IqIsGrM1qluOne_lRNph0mgwhD2o8tUAbwnDKaY8cDnuAP1B5UUNy6E8KfYqlvT25ltzqA9X3snq7OXFU9TyMbAjja5t-tOHzGcAGjcfIloKjflnpGMAQ76Md6q29CTTFMaypZnAmeQBrvkxMQMPqlymA4fjj7aU91yYUsUT7zgV12PnFfcQ-HAkzCDSdyFg8lEOyFaLKVn5WvYhj5hdt-kzD2DwV-aGAA74tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛از دربی‌جذاب‌شهر منچستر تا بازی بارسا بالوانته‌برای‌تثبیت صدرنشینی در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/29658" target="_blank">📅 12:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29657">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9b08e88d1.mp4?token=rvIzBdqmnURk_WCodABMRIQcdZgFRb4belj7iui-IPw-B92J2zSQE9EDZaDscEiTtaJx98duj6um14RtSgQUQXqLFYqyUHqtEA-D1ncpx0j5chnhtQHTLOWyW13CrZEFs21aybTWqBYA49Ji1CEeQKZnh9efcnkXGvbq_-yNj3J0pnvGd3jVwNQBPBKiy7oHoWvQ59Ju5-Dvw14TPbYm5IabOUnuiF36LvFfaE2gS9_a-DOsDadmUIOgdP2N_VcV_DYqJyM_gxWlpz9Y5nS-reK22JdRCfRL8UvvUttqXw55POVE81D65Ny87CekcNXExllwQqN1jts9chIbL2sb1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9b08e88d1.mp4?token=rvIzBdqmnURk_WCodABMRIQcdZgFRb4belj7iui-IPw-B92J2zSQE9EDZaDscEiTtaJx98duj6um14RtSgQUQXqLFYqyUHqtEA-D1ncpx0j5chnhtQHTLOWyW13CrZEFs21aybTWqBYA49Ji1CEeQKZnh9efcnkXGvbq_-yNj3J0pnvGd3jVwNQBPBKiy7oHoWvQ59Ju5-Dvw14TPbYm5IabOUnuiF36LvFfaE2gS9_a-DOsDadmUIOgdP2N_VcV_DYqJyM_gxWlpz9Y5nS-reK22JdRCfRL8UvvUttqXw55POVE81D65Ny87CekcNXExllwQqN1jts9chIbL2sb1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2018 در چنین روزی؛
ممفیس دپای ستاره هلندی لیون این سوپرگل تماشایی رو به PSG زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/29657" target="_blank">📅 12:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29656">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAG8Kf6o5A5Wq1ewDjB6AaXdpnVfdSl-_pJdz8jOs99W8OS8ZVRbQiciaOncmHCo_LJo3r4IcWQ-cFf7w4EEI0T3YsNaWSL9_RAPWPA3cx_FTDo0EhHGysmIjf3-T4QzWiUSNNGfyAW6wHcnNYX57fKmdXQfDuZ7Z6WZtiLfcLUesMQrPovYKJ_olDB5i5fU9bD_hnpjkEkBc0ETeDf5K27nye59brFhB15DBaL5vS2_RCouFLSvLW81P-L47DMMq6KtJTs6t4qK0pvhUnOMM5mLsXCYv4sCTP0zshUd4-lzhz25sZ5GM8Q_4xsoIWdRlr3Kr4mdKeDCnIEUGgytKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
هفته چهارم لیگ انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر یونایتد
🆚
منچستر سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⏰
ساعت ۱۹:۰۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/29656" target="_blank">📅 12:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29655">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uw6dCRyN5VP8GgVzQaHO_0CRTbMeWTAqfnwHZy-uaqca35163K3YyvyhSrmZcqFlGfPjlPjiEiyI5XQ2zuSAvCR0izvnH2OtR-sAnJoHi94Qe1HyoF0vUdLpzptbGVMPIxq-jHDUGHO9_aDE5TeVtmVDBcDwylSQAC1JnsB7UJj0Qfei0D-wnOctQ4NYP2SOeiz43kCEv8-eLidv3o487HE7-Qb5--WdGPbjFV99qvXwYr6U2aBS5qgdgv-Jlq5wAIkYm5rPZ5rOrdx7W-Z6JJ2UOSugBUngmXzEr1H6dNRs3b-kjvL-m_BGhjAnmPs2kNR1xqJxrIPYlnJXBSR9rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/29655" target="_blank">📅 12:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29654">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6HYrI1vxSeQkKwfkJaC2Pa3fJRgDT3CMyVUUtn82NgN-gqxlU5uw2tP-K0hBm706cnICX2zlNZK3YcAtpGf_vWQK-bgT2uSzevmg0zogLyftR-WkV8CNF4rjdJK1uB_gEzpRSLnmNW7ibc11POM3sroWBixnZg-9k_s6yWfVyxFJZdVjnP-uwQjHMr5osB7uE8EfbkESMikjggW5h0B-D9U9lTQ5rKAsODTh7i4Zm3pEB_lFmAecV-atj-lPeBfcHl-zRb94OLJ1AzgX8MvOJ0OYRxwRKjhdlxMbBrq3ZpU99LH0WUvl5HJepxV1lbW-ZfVs08nf1nh_M4Kfgl6mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29654" target="_blank">📅 11:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29653">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFxDrCes9JP5OrK7P9ocBUNuuF_8sf9N0fHcbmo0KEXfcbAuDOG9iB9VLWOpDPpqiAL4W3VFZdmkL4AN_y1jD4sSMoI0hOW0kKsO6UiwX59FVyTY-CwGYAoWJNYiNCR5f63x0GXIPGYeWRHKv5jRpbhHpeVuBl2i-98Qlp5Kqbj7XRDUEq-qHPzNCr2GYjoSeDWbUOUNmb1-rRoNkakngSdWFejO8a24yNmVR4TV1XSyXnavZXWXu74BeVfrzWTPUSInyy_M42zLF1ZheGKCXXwVD1CRGEaLtiTkhtosPy_aNvgOvbCPk3gEhsPK0ZW055JrPQuhOvuTsfz-09a0zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
#تقویم
؛ 138 سال پیش همچین روزایی اولین فصل لیگ فوتبال انگلیسی شروع شد که به عنوان اولین لیگ فوتبال در جهان شناخته می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/29653" target="_blank">📅 11:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29652">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال در روزهای‌اخیرمذاکرات مثبتی و فشرده ای با مسعود محبی مدافع میانی22ساله خیبر خرم آباد انجام داده و قصد داره با او قراردادی بلند مدت امضا کنه و نیم فصل به جمع آبی پوشان پایتخت اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29652" target="_blank">📅 10:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29651">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">▶️
صحبت‌های‌احساسی‌لاله‌مرزبان‌درباره مردم ایران پس از اعلام نام او بعنوان بهترین بازیگر فیلم ونیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29651" target="_blank">📅 10:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29650">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjPHgmB8mJmC4c6swpo8YZM0O0L0euMmYiSxekcgiDu160798EL4xgEDENOex_suv2bpgsD-QwhA8KnKGxU7_pUCwAZ8-jrNu-mexh5YpIaaOZjEZ8a7mrbG6xbbUuAAor9rkmbk-eIMM2hKG3VmpBpHGt13MH9YA6O7OuvzFgcqGIaolPzwQJIFBy7QLDoglJdSM9ADLY5DvhzdD8OYZw_jfmLSrE5bwXsBSKzmWAM4crpHoRyCh1NDRFbp7v8YhUIaqXvzsknL5ic7z6sQMj_cpuy4N_YNWDE3OmWfy3fb9UfCIVlG00CSKzpcelOuKVVg85pF93vFw6lfAtqSsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌اسپورت:
یاسر زبیری مهاجم 21 ساله رن فرانسه‌ که‌این‌فصل‌قرضی سانتاندر بازی‌میکنه که در این 5 مسابقه پنج‌گل برای تیمش به ثمررسانده گفته رویایش پیوستن به بارسلونا درتابستان‌سال بعدست. بارسلونا از علاقه یاسرِ مراکشی به این تیم آگاه‌ست و به احتمال بسیار زیاد برای جذبش اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29650" target="_blank">📅 10:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29648">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
#تکمیلی؛ محمد قربانی، محمدجواد حسین نژاد و مهدی قایدی سه ستاره ملی پوش لژیونر هستن که در در حال حاضر در تیم هاشون شرایطی خوبی ندارند و باشگاه‌هاشون هم درنیم‌فصل علاقمند به فروش آن‌ها هستند. به احتمال زیاد هر سه به لیگ برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/29648" target="_blank">📅 10:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29647">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379e42f937.mp4?token=GptfafHSfCbwOQgMXvlj5zAI9ZrKJkYkL72rTa7wcpXQ0zkck3iPc4W1ZeOud70mJWET30CuwYrW9XUUk2fw91H1stOEdaFghm0_4SDgNnQjs1UOh7bJ8K77888dJ1TMO7OJ81HG4LG_xr97X14sLIo9VOmZCJGmgUfUXpiEyFcKJRlnfFAwKbuCSOLDoE9vO8SdulocHhS0IRHUv4azRQEyNCp0P6RyQ_Ru9LE4YoH7-W30UQXzqxlISw0YdeWACEeURepro6r4iiJ3tWSbeof21AZ28V4L-K76CIttfBAWluDuPKZkgSwKHjESYkp6MH-g8PhRb6yEhrWw9fPJnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379e42f937.mp4?token=GptfafHSfCbwOQgMXvlj5zAI9ZrKJkYkL72rTa7wcpXQ0zkck3iPc4W1ZeOud70mJWET30CuwYrW9XUUk2fw91H1stOEdaFghm0_4SDgNnQjs1UOh7bJ8K77888dJ1TMO7OJ81HG4LG_xr97X14sLIo9VOmZCJGmgUfUXpiEyFcKJRlnfFAwKbuCSOLDoE9vO8SdulocHhS0IRHUv4azRQEyNCp0P6RyQ_Ru9LE4YoH7-W30UQXzqxlISw0YdeWACEeURepro6r4iiJ3tWSbeof21AZ28V4L-K76CIttfBAWluDuPKZkgSwKHjESYkp6MH-g8PhRb6yEhrWw9fPJnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمار آپدیت‌شده‌از عملکرد کریس رونالدو و لیونل مسی در کل دوران حرفه‌ایشون در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29647" target="_blank">📅 09:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29646">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a250924c.mp4?token=KAysH6f00GWyxBk3Md6Nc8F_p5l4RVNLhwhIW-w3VxTKivjBJhnLYMqAtyAbt1eXCRTvftRt_NMooOg7TMSVwvU0ZTt0zgWEF7q-phP45T_MD9-bKNxn1HXvwV8pJ1GXa1Dj1Ig4lrRyg_jCMHndf_rLyz7LyXAZ2lRBiGKIi31ew_0I5R7mNqs2iQRF9hZvXQow3KEaPY0w7zF-4pwwZJ7YP4ct1ZWZ-WrDiI-IUFq-Qs_0QuxMLVml7_ztt19JiDM7I1PirhRPiINPnHkvpv9E28c32upsDWSN0kxKEVAT84s5oRib3lBMPEM82WtCVmbwqVqALzBLBPM7bOUO1IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a250924c.mp4?token=KAysH6f00GWyxBk3Md6Nc8F_p5l4RVNLhwhIW-w3VxTKivjBJhnLYMqAtyAbt1eXCRTvftRt_NMooOg7TMSVwvU0ZTt0zgWEF7q-phP45T_MD9-bKNxn1HXvwV8pJ1GXa1Dj1Ig4lrRyg_jCMHndf_rLyz7LyXAZ2lRBiGKIi31ew_0I5R7mNqs2iQRF9hZvXQow3KEaPY0w7zF-4pwwZJ7YP4ct1ZWZ-WrDiI-IUFq-Qs_0QuxMLVml7_ztt19JiDM7I1PirhRPiINPnHkvpv9E28c32upsDWSN0kxKEVAT84s5oRib3lBMPEM82WtCVmbwqVqALzBLBPM7bOUO1IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌احساسی‌لاله‌مرزبان‌درباره مردم ایران پس از اعلام نام او بعنوان بهترین بازیگر فیلم ونیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29646" target="_blank">📅 09:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29645">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrbaR7b6mC64SWtuO-HxVrdfleSBAOhAwZcOZoIxYaG6AKqbk3-sAOykNa5mauPHRP9IkMI0JXHVibrRwnCx_uh6NyoGuoBtbjseTP7m7gZZQC-JUxVcHrnWT-cVCIbu13EQOJ-n7jlHjw2ayYzDjO0Zc0WJvZo6fjhDPrRTPhtChA2K8FQhTxK9aq4DXQwsifufcpJXMBnMP0liSXmGtu-rHgRkXu88VoFbJHQTNDX7k_z7ALIWQR1c3V5uDb27PJRJ9gGQr5OnfM6RXzkAV21pPN0cwr0ZOOgBmrwOnm2loqIQBWGQyWiQM8oGBgm4lv_UmjzrNDVaeugAr1bkuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مصاحبه جالب و عجیب و غریب مایکل اولیسه ستاره فرانسوی بایرن مونیخ در پایان بازی دیشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29645" target="_blank">📅 01:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29644">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔵
ستاره جدید الهلال افتضاح هفته‌قبل رو جبران کردند؛ الهلال امشب با درخشش ستاره‌های تازه وارد خود 6بر0 التعاون‌ رو شکست دادند. گابریل مارتینلی ستاره گرانقیمت و تازه‌واردآبی‌های ریاض دراین بازی موفق به کسب هتریک شد و واتکینز دیگر ستاره این تیم دو گل و یک پاس…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29644" target="_blank">📅 01:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29642">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWR1ezl5azbA0IUEepBQbb5pc3OnilQYM6c0RS03QaOg73RwPGSUt04PJ4Hd7Rl23qVHWK2CMPR8hnQkzXM55qR_3MJ5Gt2Ac1X4Gqc76_uPIGQ21KRQMPNqJq7I5lMZvrS3j3l--GhycU0jPliMiX_6l4P8c8wtgi-4tJdEzGl5iZdWeLonHdP-MhP4Ifi-XmLpcl7jmislE-LfcNOVHVIzhxweoeCBR81lbRU0MiS5mHmvNArkY-XfiXfeys60k4onq4LrUznWXq2BuSFkVM_BXcn9EdCkga9urAlq2EqGOmub9CFDOCHu1w1CCS-5sVW6CghTrmWMjxkv2oFDHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛از دربی‌جذاب‌شهر منچستر تا بازی بارسا بالوانته‌برای‌تثبیت صدرنشینی در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29642" target="_blank">📅 01:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29641">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROyy_grIL_iwd-ylw80wB4_JG9pyqu911iALxzTC7a5OhXrQ_VXCOGUuiofN77zBnwIX0h22Iz5lI0IhmagbBDw5zKJWrNLWdY7dnPmKG-RNAPYr-Q7mdoSSEPJHkwMdbpslrMaHXloA64okVOSLjW_ZWzZUpm-9oz1BDpFvHbztj63zMNCvmLrM9-jBzzJIPf1hRUvdddoRztd-P-bvuTymTwFQkUmGmMxicJhCe5YU7Y5djBNMqj3EG-bNKYcX1XwKYKd_8lNAPeaYgMhrdNdXaM8uXviCxvVzbQOJkWSSnFCgHzsmMj0EBPEod74I-uBKvqZm8a2AqOIPXGhNyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف همزمان لیورپول، چلسی و تاتنهام در لیگ‌جزیره تا برتری پرگل شاگردان خوزه مورینیو در شب درخشش کیلیان امباپه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29641" target="_blank">📅 01:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29639">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJ9o6g2bvjsrgkcb52iS-I3ESNY-4ns6A-Koii0im2KSwe4lHGDGp_Zs_RdEs6AmKlA5ptnlJ_p89_xSoF_T66NICZC9Wj1nrhlBWM2GLq3GIrRq7KD8cO6vLoYwRO0wnSd18EyN3EZZuHEUlxAG4XV7262c029ZNESBsEzY5saGPHnx9zk5Gq-oJIzkJmqeg9xID2pkWdDSzyaAr0-4ytcThNBGQ2qHK_LeMqnwUMn-njhkxr2G_bKvmC1mhXo7wWbA5QEBSYLzu7bwnJLe0vwhqBSSDxlkc2T6mHCdaBp9sGQHy1dCqCkKkghqvXUWOwa8SANn8S456-zJaIAS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
تصویری‌زیبامریم‌میرزاخانی‌ریاضی‌دان ایرانی و استاد دانشگاه‌استنفورد روی‌جلدکتاب ریاضی دانش آموزان ایتالیایی؛ روحش شاد و یادش گرامی.
🖤
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29639" target="_blank">📅 00:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29638">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02bd31b46f.mp4?token=FVkF-LLLT76HVjDpXhqXHeSYWdtkJfpmGrZ0BhSkOrp22ko8foH_NLMRg1eGj0r4G1oeIkuaPQ3a4FE4qwUdffBgCzAnphOd6dS10xQRDzkt4iJA3LxSvSCspqndUZLoLtDs7nzSdxx4MXeqMa22Ct1wbxnD_Hd2z8WhLV3usZWDklY8EO6jkYeaUNXA4WeViDD9U8P5iP2WbtZJDhwv8miiqfdYP1QwuEUO601WQCdOnQcOXUJLgC3YczGypj0CZ8Ne_9b8eP8E_pGdHeGP6xNmPe2gSOZihKrjLqLU6HhLEEQnobWmXYe-U3z7jQ_OOA7xNiKEp7y-QOgWvSh35FkHecmJVEi4i18XHYcoTana78Waxey7ShEFM1ixpMbd_wxVj8jsDRmv2phuxkw94CJt57hweZqRbJjQv5wHqWq4TxQH7PjJpB7tik3etR-KHe1v898xMI_sByv8zUmKwrmA4GTZwlMcsNyCIXie5fNK-w6JiB2YgGlK_KOobLrtY2SIVNOrgoPFNLOZ4a1EZ8fXYERfzoBuIB_956NSCjPZOIs-dgyHU23vjJJ2UgbUA2r9pqKuw5pvDTW5OnyL1PmHRIrFy2UkcFcVFAy4DSBZD0HYV7aPq1M9BIBaBL1C3_apSkimAxTcwImN_ySOwa3v1bhFC2nKWV38481eq7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02bd31b46f.mp4?token=FVkF-LLLT76HVjDpXhqXHeSYWdtkJfpmGrZ0BhSkOrp22ko8foH_NLMRg1eGj0r4G1oeIkuaPQ3a4FE4qwUdffBgCzAnphOd6dS10xQRDzkt4iJA3LxSvSCspqndUZLoLtDs7nzSdxx4MXeqMa22Ct1wbxnD_Hd2z8WhLV3usZWDklY8EO6jkYeaUNXA4WeViDD9U8P5iP2WbtZJDhwv8miiqfdYP1QwuEUO601WQCdOnQcOXUJLgC3YczGypj0CZ8Ne_9b8eP8E_pGdHeGP6xNmPe2gSOZihKrjLqLU6HhLEEQnobWmXYe-U3z7jQ_OOA7xNiKEp7y-QOgWvSh35FkHecmJVEi4i18XHYcoTana78Waxey7ShEFM1ixpMbd_wxVj8jsDRmv2phuxkw94CJt57hweZqRbJjQv5wHqWq4TxQH7PjJpB7tik3etR-KHe1v898xMI_sByv8zUmKwrmA4GTZwlMcsNyCIXie5fNK-w6JiB2YgGlK_KOobLrtY2SIVNOrgoPFNLOZ4a1EZ8fXYERfzoBuIB_956NSCjPZOIs-dgyHU23vjJJ2UgbUA2r9pqKuw5pvDTW5OnyL1PmHRIrFy2UkcFcVFAy4DSBZD0HYV7aPq1M9BIBaBL1C3_apSkimAxTcwImN_ySOwa3v1bhFC2nKWV38481eq7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛ از جدال توپچی‌ها با یاران گرانیت‌ژاکا تانبرد رئال‌مادرید با رایو وایکانو در خانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29638" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29637">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iH_u05ZrZ2_iaCz8YXrcC3SULSHJSihtdnRcQFpFkzph1zs-T2rXNLHdpfKLMin4_YV2IOG7KjYM7b02fdWSTfqEn-QKJRHxOL5kU4F9tVZ6uTAJIDXwcsR5GH2TzrNoWvUXDS2TelYsnx4DUjZajh7Yu4vWgHh2NxVhyE8RwNxsmiC9jPUoY91q-AgrEmF1P27qj85TcR5ADov297tkDlsqlhW3uzK8kikRxkxHhLELTUqoOjpowCcyBm7-Eui_UP2vnihqdJr-bXS4bDJeNJjLpo1eAC4e3KhG3XtwJ6BT2uLxZGs5T2wc0TP6h-s3dk5vOQsdr9bfHFttJ1x20g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29637" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29636">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzVKWCSvqQGlgRoiaBnr4UwSdEHR4MVDaE75yzgUAUh3aJgcDG55PwOWSIAsCiH4v1KGrZ1ungYZuzqdy_N0bqN2D2sa_y0z42wsAE2g4lKptZSrShAZtZMYWInWldJJqkPp3igiqF8ZzgOQ8xJl3BmxDzPKOsq8RWtLfm9lqor3sVf3MuGZi3dUM2Bs7ahu9ePka8YBTXqszti7XI_VnbYtAiDGkfmh5nnkfzNWe6Hfsoh9WkBIgFPnIqXndMTdHMK_l_2CRnPm0d2Ph1LF9lm9uIAjC5ini5TiFToIDxltCc4U4yiu5dv6qS-GBxh04HIXAxSI5WyNoCcFfkFR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
حضورپارتنر وینیسیوس‌جونیور در ورزشگاه سانتیاگو برنابئو در بازی امشب رئال مادرید مقابل رایووایکانو؛ نیمه اول رئال سه هیچ بازی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29636" target="_blank">📅 00:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29635">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-SzIjUrJOW5NxosxVG1mgOBkN31bWq_IZRfbVXwRpCxf3Pt1G55kHXJ8MRGZCDZL6_d7eUtVDmcbqMRRi9EvaLXp20kkRj1ZcXmK6-nS4Y-P7CngRmZ2xOEj2FkMCNKIaDrfTfh1lfnzyYs1t4hDBNdwS68zLpSQHAaas23OfW1VoqVsgMISkOG1l5kvHGE3kke271Ax2SLp3e57lfi-u5zU2KwQaspH069iBXqUEpPUPI79AoLR5M0APAfqZkO7lTfBZkYvdFkQip6z17DDZJk9GppqwUabVR6ouDGRmIkAeEoygHyx46SZLUymkpc5amrlivgZnWGhYpnWdm8ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تایید شد؛ بااعلام‌رسمی باشگاه استقلال و با موافقت سهراب بختیتاری زاده صالح حردانی مدافع راست‌آبی‌ها به‌تمرینات‌ این‌تیم برگشت و در بازی روز دوشنبه با السد در لیست آبی‌‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29635" target="_blank">📅 00:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29633">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBm2ceiO2yzW3TE5K_ciymF_cyj0ts0vXKMhNVBJ-szGGgtGoyPuJCONRduVpwLoQ4HjUHs9cR4fp8aTDVedIu5_ypIorlP7eX1X80BShvBaLuC-zdsd3hUwArkLUePr-zjpeela5F_DS0qsxwL1hWBwkjAhEHIZAQCDfm3hFMwlpnVwEFoL8krnevcO9yPDZsBirJzVHX5GHGIL7KwCPaHan2RJ5hki2wH2cMr0U5QV3wkcwUpHEREDZiGtcDZpx9V4gM5jeB0r4OPJEselE-8bmOs1dCPf_3tgBJBSPkH0gHgy0Jzl86hbAcWcgcjQSZlPa2rKugxXa6YtZxb7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛قیمت‌پلی‌استیشن 5 پرو دربازار به 310 میلیون تومان رسید. بهمن ماه 45 میلیون تومان بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29633" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29632">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuwBw4JM9095kL70efQZQotMtnKi7-5CJHVZVZvvKB9WqLQ5uGsha_x1DcBFtxwOmZZrz_t6VqUmXopSxRQJlgMElHzfLZTQ4buo3qrWpAbCYsXtJ_MaPwT8mmEQILgBX577cIUitgSGoCwIO9HvBYQyr6sAHlUNCpvcPOK-hxQzpBpYuL7nN3773V-gTUjarUdz253expztR3dInoyUx6x83z4ElRq4WXcuaneV_V8In3yY2Qnsi8OzsjwdQFL4A5o9Hpbm4y-SKu8NN_KSguOdGqed2S0V5Z-VVDMzTe2o9mkP808f97TM0u7P1GUy13tfDLVuFp9AlXJxe1MB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بااعلام فابریزیو رومانو؛ مارسلو بروزویچ ستاره کروات سابق النصر با عقدقراردادی دو ساله به ارزش 12 میلیون‌یورو دستمزدخالص به السد قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29632" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29631">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuXDoCeDouS0wkkAY2BqFftbFJgDBD_YjzOAPVlYf-XFwYx6-NOZqGZlbC_qsyG5Wq1N4ZhRN2PZgPVXWkK2XjuQh6_8hvvjn26a1A9m_yv1MwpHvy9gFASAX-EQn35zNC030OSUX_Gxc4Tts_AplfyFrfLNuDXt0IdFfr9IvKla05Rk7mOMrEBHoqMw1aOy8nZfF1nj4XR6XOWAz4HvyDgxwuIvA8q3uEXtrQiaBsqbpscKErSU1gewoxJscdyJ4R34akSKUfpO_q0HAehAyXaOYfYijiNDO3LkRE2sqTfKBuH8rFf0x3UvSQmGYeGbDmCfal3KL6qjYM3VMC1ngg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/29631" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29630">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scvt89eUKa-59DY5KH18627A4lI3lTv52Bs7FD31y06B7w6r7aHHEGRc3cZvXXRdGj1pOLG2rfqc0WxSo9CjQri1hZjLnCJyWG9jJakxMMUXghZ-r73jN8Jf37d35N5xo0vcsu-tO2tpT6yhxt_ADJWmkLjxnc84pVCRtWdcIdiWHzB-0TaOvdjneIhamA7QSuk3UvngKVDioACZRJnKrD7ySPpHBwDo8FSZRKNoYDRaJP2x5m6MAuYU8PfwBcp01F_FANm0tu1KKMqHvCcES5pZwaFSuboFJHxXljrfoMXXVvTn5gPI-kqhxPTIXdGK5OGgPphlqu8hnQpLW8-QAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/29630" target="_blank">📅 23:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29629">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSlYr8E7DPndUnSww1fttYjyKLXDAHL2uXEuaWTqedD0GSBALiuJFghjkqkbw_AiE2XsBsr8ARStZLKrKx1YOj8hqz-T_vQqH7EAqLypB_6wp5JBfYd1CUsR-GrRkHTuZdGtAlFOUzI-ElepCvnH4tmp7-xbBi1hdP03vbku-s7aiye_bwSDUuNSBrDYnvL1TR8wHQJ6Yo47lZ0CiGNa4MaS-RyAVl_3Mgn7YnnMJR5CbOJnqU2x58G5RLzntUuIqZUp45kOxzZo0FJUgOwd5LR7NBcHWcQzAmXvsuYvQ2Xrf05um_xY6KZ-9kkEwmx0FQ8EKcfzod0iPPFQM11fmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌جدیدترین‌شنیده‌های پرشیانا؛ باشگاه‌پرسپولیس بامدیریت‌باشگاه فولاد برسر انتقال ابوالفضل‌رزاق‌پور به‌جمع شاگردان مهدی‌تارتار در نیم فصل به توافق رسیده‌اند و سرخ‌ها با پرداخت 150 میلیارد تومان رضایت نامه این بازیکن رو میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29629" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29628">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcfRc9QGithZHydifivUAIq1r13lBLY9dSt-SE4ehtSuBrhgy3A4f5Ju5joNaxCt_DmcabHO3tqZhJ7aj2qT06tWROELzekuF7XdQ0-kbr8md-PhXcSnSQd0x0becvMa7IkxEfkG8JeXR8AqXwOTU6HjYM8W6V4RDpn50MeBQ7YptlxNiUvcc2NZafFu4sOptuOkfAg3-o65yUOY14L-91UtA0sN0BCCRcYwYh0KevmHMjuFaxf2oeJp9siuop9xiz8n_7ulw0pq4kC3OyTF-udodNFLc_UEUUbr8_9G4sXHNgz0LF7N5ZOGCoy8SSNyCud9GiWdC1DV-rwrTg669w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌جدیدی‌ازبهترین‌برنامه‌های‌هوش مصنوعی برای تولیدمحتوای خفن در اینستاگرام؛ این پست رو یجایی ذخیره کنید به‌کارتون‌میاد و برای دوستانتون هم بفرستید که اونا هم ازش استفاده کنند. عالیه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29628" target="_blank">📅 22:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29627">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVzucelUkhHQXXHsUwbG6t_b06_NLm1s3ImJRjT4uz9_zGq_6KkFG9ZvocmrI0WXh1PAOBrWTAE5vhf1nZNOoVtJbqCrbrfhj7s0zkQSWWaMnuiqm3q7v_rAs_i60wiCGJDg0p0AGpPxbr8T5k4swdfyXPcEOxf8iYNMJcvB5GifGzh_vWEhS8kZWW-4_FjEVV9zW_0RTQhom_6LnbyHAfcqwWaBWo1Fup6OUOr6a3ivOdQw4oZ8OIEE7sLnYlMn5GRHirnGLlrRb4gE2RSRIwTv74AbOr8DKZWyYxTicEfYnvkP1nllZIZEbArB97nwaQWVj3WVEOBWGcPi92_2kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخبار دریافتی پرشیانا؛ باشگاه پرسپولیس بزودی با پرداخت 250 هزار دلار به دنیل گرا مدافع راست 33 ساله این تیم توافقی قراردادش رو فسخ خواهد کرد و گرا از جمع سرخپوشان جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/29627" target="_blank">📅 22:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29626">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKedVzbIUMFatDeA2wGmBoLPhDmCkbWeyeLOI2BQRMbDbddvMREj4pg6pp7zGUB8TumSf8YtZLduS_Z3xZUJEurQ-x18WCvcED6QtuAw05iSS-HW65f460ycRtYJ3Xjx4R9l8fzcAwRJ29l6WbhW_V1IgsSqMzuGKAz9vsJufyXjTuVT9sUHBu1MBp-C8aBwlpMAM-rKl40WLAW8I0SlkHr-mqVfgmeaZ7lyXOcVthzu5VagIxfFskZTPfbR8v5B5QuTrINvdKh6DZPULMdC38YLSLMX5cuRPqVMoW7Xyk2Ea-C_6Q36yCg1WHRfy8NCkYqpF9aKO66h8P-I-82rZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/29626" target="_blank">📅 22:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29625">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2989e9b119.mp4?token=qfT9draJMYHKWc6Tf9xJ-ud0Nx-UNuZ1Q8DSCruKJhJrpcctjVKJdvyaHwWwRfhbqMTyEDjjeWKqxVK2QYRhFpQyP3-Ypb4fdQCSP3EV6K4SSS9pqARvRZh5xSaDEKiFUx0In3M_swPCZbK91kLCdlx1hycZcrjH5G1GEBMkj2jbluruTzqmN8ZMOrvwcy2B-0I0j3PnL4m8ENYJMuDQ5ACYPSqnoJgI_76SsxA36zZokm-PPd5p0wR7_5Ek_KHAy4S4Kfljy4KLKXfd02zk4ORW7CnMMs-b3_azuiEZWrF7lbcGWatn_Nsg04bm4blVMsJ-5ZeGyb59BBTnvAdrRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2989e9b119.mp4?token=qfT9draJMYHKWc6Tf9xJ-ud0Nx-UNuZ1Q8DSCruKJhJrpcctjVKJdvyaHwWwRfhbqMTyEDjjeWKqxVK2QYRhFpQyP3-Ypb4fdQCSP3EV6K4SSS9pqARvRZh5xSaDEKiFUx0In3M_swPCZbK91kLCdlx1hycZcrjH5G1GEBMkj2jbluruTzqmN8ZMOrvwcy2B-0I0j3PnL4m8ENYJMuDQ5ACYPSqnoJgI_76SsxA36zZokm-PPd5p0wR7_5Ek_KHAy4S4Kfljy4KLKXfd02zk4ORW7CnMMs-b3_azuiEZWrF7lbcGWatn_Nsg04bm4blVMsJ-5ZeGyb59BBTnvAdrRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد نوری استاد جملات قصار! شاهکار جدید ایشون درنشست‌خبری قبل از بازی فردا با سپاهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/persiana_Soccer/29625" target="_blank">📅 22:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29624">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeujUlFtdnOxAi4h3tAtLcE1VrhDmyCP-WjdduPoQSYQqFFC_PEuj2_3EbLN3v_hQdbNJPutXdS6GxNWug-6QlFYItVZdaivn7jG70Lc3fNXZcm0LBxnih8y9eoOFQt8oe3xHWfyh7QIdCQ2VP_YxckAcbTvSWQiruqGBgojJ93CZkoiBLT_UREBuL-GcJYI5WIwWCnIefEjtS88Zm-4wuWQPIF_oJCQiP3fnSiztH82sYjngNsrYZF2NSq2WuOkkoa2klbOLtfwSgn3uk4cbT7F8Ox-ZTh75Mc0s0u0l2a_HjFNOyo-laAtF3ZoAVMFkgHiOlYv3RqGbAoKXJwH4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛
بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد قرارداد با این ستاره 29 ساله تیم‌ملی‌عراقه و درصورت تاییدیه‌مهدی‌تارتار این هافبک تهاجمی خلاق به پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/persiana_Soccer/29624" target="_blank">📅 21:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29623">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJqdUn8-CDHgPWUvrenM5Vo9T_SNozxqHa1bf-3DlRXCdtHv3tGjEW1r4SpF5fjp4M1_KRLXoM6WeEOXswngJKm3jKxnEDif6viTPrmHj-1MMdD2JUwEEc4FdesinHT1JwOYigZ9C8YHjvGJinO2tzm5ipjmfi6In6T0r8v7XKx6uRLejVFK7FOApDVM4AkOgxv-GkCjE72K4lnv_hAXx3D0qN4kZJxEHvXDUUk9-vnTb9eqM1-38O8Ipkfosr3MepO3aXKAHMz3tJmPfzjbo7wKyPeblCMg8BlvKJW2btHXbDUjbVP6uDvvxgaO7ARu2e_JAMCEVBVaoFKGu5Y2Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
گواردیولاسرمربی‌سابق‌منچسترسیتی:
برای تموم تیم‌ ها در چمپیونزلیگ برنامه داشتم اما هرگز ندونستم چطور رئال رو مدیریت و کنترل کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/persiana_Soccer/29623" target="_blank">📅 21:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29621">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZdYbFPHcDymBAXT4ImXgFWXzU_kWjmYHWodsebNzr6tvk3ulOco0OqvxpyKBSnQfaMEOlLe2EXW2pnWzCAbk9GXN1Uz-PM6UOckFwE4UrASs4DtusLACqo496TJ2zqY-ah-UC2_vZRsswV4UIS2fzsGiGTNCIyE57TtlaJf_49uAKOvsirbIPy8M0wE99zGI9bsmhR38QoCOz9yvaof43wUKxGaiqxKwlLnSniRv6_krefeYiXtteXoQhcHEWtGNI40-aWhcEqzfYV-wenZ85ntE-gPqOb3mm_hb6lGoVwjAy6fobo-CyVqJACyofyVEM_JjhgZ9otqe3OWUrnMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت‌امروز انواع پلی‌استیشن 5 با دلار امروز که حدود 223هزارتومان‌بود؛همین کنسول یه هفته پیش 190 200 میلیون تومان بود! قیمت‌ها عالیه واقعا:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/29621" target="_blank">📅 21:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29620">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnNYlmYKrb_NACuT3EWxzYiBDx3Lr7PDVcw2vwYCJdJL8OID7qbCvt8g7dWBPkP82IWL5Hn6Kr9vx8Zv9norg2sjkL-2g3wgYEb2Um6G5ilSYtEvBQ5riTi5rd32NixvFwjAbrqlUT4v_JhqluQ0B0Ah432CGbD_Ew5vSbFOCMz29PTyWH4f-PiE7YyR2_DdQoH1Wyf3GgQdgvx4cvxPX51kb6FhGTIT7n0w6DNVRikgfESUe7N_aNr_A7svi1PcUaUTb9qy-EJllWbsvGqazAIMEdZXAyOB1UuxbUUbbAT98y9uqoY7Ubfvn73wDAJv-IxUKDqW4ek9C4goJOHtuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا
|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/29620" target="_blank">📅 21:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29619">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4VcACAeifbBzqi8lbe5VP5sgL_RCaHTT0cRj--EJuDdY4kyKcxKyh04IeTSObeARZbhMkrcF-KS4WMeyPj06-0MUEcvAmsc69T98CaKsZ0zwj_vVrEMj-nYdD8gLMyjGbooAeFTmpKg5V_SQx9rFBYtW5TVtypnEsNl8akeuhtRVIb7e8-I-89-q2EqicwGfXXD1Jp9eFngtI5I2efh7bY7r4gd6kOpQ9INkrjf0fMpP0dGvM6g53mADYjzoZKqcTUISiCJVbz3ONE8aNmw7bS6gi3tGKEPr7lelO_hwH8dR20HLpoXiYyGVpHBWK8v9toxoCUIj-HYQqo8V7eBSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌میگن‌فوتبال‌غیرقابل‌پیش‌بینیه یعنی این؛ الهلال اینزاگی امشب با تموم ستاره های گرانقیمتش همچون مارتینلی و واتکینز اونم در خونه دو بر صفر به‌تیم نئوم باخت. حتی نتونستن به‌این‌تیم گل بزنند. نئوم تا پایان هفته ششم  دومسابقه‌باخته‌بود و چهار گلم خورده بود…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29619" target="_blank">📅 21:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29617">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcGkBK87aBgv7GIkyoeXYmiOsNQ8RegqCpIDVoTXpzH9ithPSbzEnE3xMuAYuTWExV5tfxiBAXtPMl9380mH8vSr9Nd9eB63bIXu9GYb2tsHX_5Oug6_ZQZxDB1gtf8tqWuNViqsCaHu0HrED7Bjpitua18vegvDnBcwp7sGN2onRAweZev28xkkbIkr7jBeSsbNOAFspsY-DfUhZ_RcQgnSPwwnkXLEyXvBR9rUPHcEF0uHLXXPvVli8rKt7h5yYyyPBEfT1ntHIo2ptwGCaD_fQksnxgHEIDYTzM4E5PUmDIMhLG769xOBkVJO486LdHyuCrnvSzwGf2GWIv3fyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29617" target="_blank">📅 20:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29616">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6t2H1m1_BTMYyOlodyJQRxrFIJZRmk6OCC-XKS54oXMaOZVcjFIB1s6qlhd4oWbNf1hxU-IDYT3dCa47MJLIlgF4Sp3_5kSDkGsb7etU2bKt3diqwO8uOKmQ4eLnwnDkLWvJNWif6Y2TX83WugouaByRVpjqkXFKk3UAb45FzERyl4lN3XyvI4V1vsqu2kIBLSGhsx8R2MNuIR3fhK0XYVZEykGd7p8a5ugLKMFnSEJKOeWhJ99-deyCV4WLcm-BUzQA4nzhuC9VAYLKeNZy8-zNh-Ddgg3wxHheYi2HkjWmhySeVsr0MB3CwzlTNsdXJRPXak_EH7JJb8Pk6InSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/29616" target="_blank">📅 20:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29615">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6942e2257c.mp4?token=B_GF4QT2GzRNWTZNdDeu8hq9qFJAhEIb-3rbZKShntHc7GXGbkNuXk09NwXzc0kli0ltrVPVaVviUfEcWd3bXRiq27CWVlwjVe2dschoPTP2ZJCrhFSMSDmN1lif-PPf9mNuC0S_n7yp_HNcDyT89W20dX59DAd9qNhDxazuOzBzItOxLAtjzyfoYGDrBGsr_hHdxMUog9TCowvK0bNEbGDSRJhb2PVDuWfZGMcNJj5801pYVs5mXNC5-HLXdQbX9XqBow7VS7dL6IsU6nFH4bVYgtKL0RXTHW28P_aRUOUs-cyFiNOT6-jlenayy4Q3JYOsWrL595kFpNBPdJjgSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6942e2257c.mp4?token=B_GF4QT2GzRNWTZNdDeu8hq9qFJAhEIb-3rbZKShntHc7GXGbkNuXk09NwXzc0kli0ltrVPVaVviUfEcWd3bXRiq27CWVlwjVe2dschoPTP2ZJCrhFSMSDmN1lif-PPf9mNuC0S_n7yp_HNcDyT89W20dX59DAd9qNhDxazuOzBzItOxLAtjzyfoYGDrBGsr_hHdxMUog9TCowvK0bNEbGDSRJhb2PVDuWfZGMcNJj5801pYVs5mXNC5-HLXdQbX9XqBow7VS7dL6IsU6nFH4bVYgtKL0RXTHW28P_aRUOUs-cyFiNOT6-jlenayy4Q3JYOsWrL595kFpNBPdJjgSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گردوخاک اللهیار دراروپا؛ گلزنی دوباره اللهیار صیادمنش ستاره 24 ساله لخ پوزنان در بازی امشب.  عملکرد فوق‌العاده صیادمنش در فصل جدید برای لخ پوزنان لهستان: 6 مسابقه، 5 گل زده، 2 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29615" target="_blank">📅 20:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29613">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2nZbwHM6slq496ODLnRtC1i6kn2oltBypKGU_ojJZBTVk7zVQ7A0U1gFtBdxMkRGfkZjq-5uHMBuZUAeYgSLNL0_OGEzD3BGwlRvVVd8WnyIU_TEpJpCy8f2wxg06ssBt668v0LaAMr4lde0W2ST5V932I8LKbuU9IgHyHMTJcY90hi4obpkEpeQNTPJVqherq53UHtrETWUMIEsL0i7zBuQg8e9GCk17XJcXlQFoB8V3yehNF_FHqUTruQybOUIT8Wo30FYFZBesRV1Sgex9p7VgmeKd05YR41qY7zHts6J71u8sDUUZnnFmGXz1zJ3aSUdZLmHwqMXDCF5fuhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wif0XUvaO3ZbErBC-bXzEmrmg5ZEGxcmn-SEiz3lt_sOIpE2G4fP9Dh-0ymzEG5aGxHc6BFn-h-YiVLR3J1vYCgztV_AlTjQ0YAYJHUQi1pp3FftqdyTPG8crDVXgXN_9Y-_LyOqDGrf2ZrSwdxaP6GRj2eW8aX5fg2GUrWLvnmULHdCCxZjkAyr6IwYgf0iAvU8iFpCfUC1uwiz3QvOxFhzewtYx6TaJL3EshlUh63zCtfblbU1wgO2ekFwfvGDMeXVRYCR5MhuGig3JBGCqDzT47db6PCn3f6bWWYaKm-or9c3ArxqtbNVvnKQ45HdEBLUeTmUwvH4Gx3Sw0lWMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29613" target="_blank">📅 19:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29612">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‼️
سرگئی‌جاکیروویچ بوسنیایی رویادتونه‌که 3 سال پیش دریکقدمی‌عقدقرارداد بااستقلال قرار گرفته بود این‌فصل سرمربی هال‌سیتی شد و این ماه نیز بعنوان بهترین سرمربی ماه لیگ برتر انگلیس انتخاب شد.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد هال سیتی در فصل جدید: سه مسابقه، دو پیروزی، 1 مساوی،…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29612" target="_blank">📅 19:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29611">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkAJy-OvfgbczS3DsQt7DNYhNMn8PUmg7Jm91vSBn-lViCJO3YnSpd_Pc6H1xTBxlclqWfiobKh40kSxsdbpxuz4p0QrJeeP26FPz7T4lvQTECaJrbkggVTxtpYg_1HB3vhLB0KDTT81XmB0mYaAJlmHEFdeWuZQvXplKRSFACfGe-NuRJ8zLzwvjDiVQ1SzNIUogCQzh_IPOIGOLmpVfxvpfoK44ZfFLYUa0oUTzLb8Yh_0_7IG_m7jnIl4Al0S_pFCwhT_4-Uw2zD2SLTlahOpEUFyMNlkZovIkEmfAvgw1d6TDU9D9KlgA4AqpB7gqsNiv5sNDzKLLTHFlhCydQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرصت سوزی برگ ریزون لوئیس واسکز مهاجم بیرمنگام در بازی امروز این تیم در چمپیونشیب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29611" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29609">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEdReCFmQGzVB0GlenVP6-yHpkfPbfBGPFmhdPbZD9sGKC-WjBVaBJvJNJooDQFeVIyi1XvuR2FO7-jMmjLAt6p_yKJ_M5824M8gSvE6QWSm2TdIuIInN9drB-xL1JwACqpYQk310chT8RH0q0wPrzX0g7OsqY_fdz0wbiSUu00Sw8HVZYIHVC1WjMLC-9n4vWyIl2IUUjb5oJNZy0UUQ1hCkEGMxqXgRKaQ9Blf5a-15y_a_QgI8Ns6F9Up_Affnkf98CbBW51-rEPA_PSQiFB-mhqJI2nkwTE9nqsqXKpl0iV904xAvFoVMN81ylWFMBPZsFg_kDdJj1A_DRs0KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نگاهی به آمار خیره کننده مهدی طارمی ستاره 34 ساله الوصل امارات در دوران حضور در پورتو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29609" target="_blank">📅 18:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29608">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDIBe6ahQ60D3N3XknQtcJH6v45f9EmyB0sTxWd0GV0buryHlekZ6LqADxRV_8K-DTg6laJ4OEccSomGBzFcL9wH4X22BIIQFcN1HU0jh3HJ2PWddv6zhsYOTY6AecRqU8wXROZD4g7xFaaLLwffTW60AWvZwajOzPYde8ZbuCp2bIKhCsmZjQ4CXQNBTWjRcah-r6vZR16tUnH6BAOi6ijvOBSBy1ILsq-fbL4G8UW-uwOFKg1b8x9ZLMVduqxmEPI9i7t_M3tqdMWZzubldVb5cUkHvA3xmTjajnDIjG9qHKhTj6MtLMcKkRKwx0NhYOu9HH6RX_3HHFDyIi0bBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ AS: میکل‌آرتتا اگه تصمیم گرفته باشه در آینده‌راهی بارسابشه فلورنتینو پرز سسک فابرگاس رو راضی خواهد کرد تا به‌‌تیم رئال مادرید بپیوندد اما اولویت اصلی پرز اوردن آرتتا به سانتیاگو برنابئوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29608" target="_blank">📅 18:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29607">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇦🇷
ویدیویی‌فوق‌العاده‌ازکاشته‌های لیونل مسی فوق ستاره سابق بارسلونا و تیم آرزانتین درمستطیل سبز
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29607" target="_blank">📅 17:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29606">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUZO4Mxr4F9xoCB5vks37_vfVrLZuRIMItKDtw-P7KqdFTtmEFgLpZk7NRYGj23qWnoD2wxWhyxGsyZziOJe5IYRxoEsMSNqJXCruXUoMpyoDWWmI3ZrHvT8OzhlLthfWb3NLnIzfqNlXp0KdrbdPGzn8k9kVwOjtHncS7RYlXt3fKkQHxUSYm7wtFMAQKCSKrCkLNMhAxyQ32WW9XrDUNdAUZOAFD2BiseXLtcWIN2bVb0plXwSEnJaZwwl1Pedt8YMigQrcv0SCWp-o33ASqL5eL--T6O58E2ozk0Dl4eg2LZcv_VC3ln-RXBT82Sg39LuYOQwO3UR9i15qhyNng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
پرواز تماشایی برای گل شماره 979؛ گلزنی دیدنی کریس رونالدو 41 ساله در بازی امشب النصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29606" target="_blank">📅 17:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29605">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGwSVW8t9YumPG3KUv7a3Nb-l3WfQUiN5PcLyGg1CARqVetGnAalG-RpwxrXYiHn4JIfr4OfE3fcFUmtC22TO-UCB67SWbL-0-Xrm6TpSVzMpSFgvG3OjD0rYJHbtZCDCOzAAHcdHp5uaxFPDYyIBfgZbRNjYbwcZDGkyMMHeUJ4rZWf4qxk2hhwVlfI787w1reczJqVpQL15ExebSWJ2ifMN1j2zqNo6GXS-hmODipYAMfQpZACOY1esHgFSl_-rAKhFhfCWxaPrx6gKFIWTK-QpDZwE1HuOk5vSkL6cNH2Qp7L8symOgxxkjcA7-l6Ozs7kVDHqPrJU5W9PKjDBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
برگاتون بریزه؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مدیران باشگاه سپاهان امروز صبح به‌مدیریت تراکتور گفته برای صادرکردن رضایت نامه آرش رضاوند علاوه‌بر تومیسلاو اشترکالی 50 میلیارد تومان هم بایدپرداخت‌کنند تا رضاوند تراکتوری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29605" target="_blank">📅 17:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29604">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czIKo0rEW8Q43V2aJo22fFEfv63sDlVnJmKkVQ9uwJ3kl3Es_jiIAbMLTq9cecRSCZgYrIHlGKV5B9oxh5obNmCt5Uk08h1txx8vguKG-afZE_5W7D-1ZiZ3NVuSv8SVr5p1moU15Cb2k26dp-55TC8eT_FoJfvO1imwosIub0pslP2yVzK52yvc6kEh7Xu16tm56hVinAFyxAppjcwsY_rqNbC6uSbMgZzDxddh7OOiW-stKdsIali_9M2gke0UWj5uvKWgvlj9iEbj1LNkkIZB2V3ddrIfAYRnEjulqs_D5sNbrQd0-YY9Ei8v1oo7HRB-26PJObIJozBNvFABig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
با برطرف شدن موانع موجود، کاروان تیم فوتبال استقلال تاساعاتی‌دیگربرای دیدار فوق العاده حساس مقابل السد در لیگ نخبگان آسیا، به طور مستقیم از فرودگاه مهرآباد تهران عازم بصره خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29604" target="_blank">📅 16:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29603">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0evLXSm-w6xsDDoyKRS11POjoKHbfIoBEKIYApXYZiWCHeURQfVELIwRJwbZk5zMww71y0dQUVa_xz7YH4dDO8KWz6CMUGtbj7GrmO6hR5WlbxeRP9J6YpuAiyTq2EvR7z0Ug0midpDAm8Z_6u5r9_CGl91SYNK4Rf716KLjdcTzOg4MRyh6WliXWWT6HvK5gkNmAbubA-JAIYXjL6fZaze3Dt4Z0dU-LyX-7KMCrDd1f16-UwI86Dk2Cya4KXkKaOHunO1lwUGlfhiH11V6WK8xvpbRyxDZ4yNuvI2DeWhPVeIrFTXL3eoSyT5fPeTukezpj45ZsEF16HxSDKiDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه‌کامل‌ودقیق دو سری آیفون 17 پرومکس با آیفون 18 پرومکس که دیشب ازش رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29603" target="_blank">📅 16:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29602">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abe26c296f.mp4?token=JfYKWxTHy2zCJq4WdNPOqMFexo2Sd91GyEvSYpTo57aiXwyhUFm9jEHPesW63YgvSslojd_NFOcX2H2fJmEyc2iviu-MixqwdNA7PO3MysfbiQHwFAfAYsWZC_0k7IQ8OIMU0DRmRozGVWB9IWg-bt-b2OywsPQWymyCjTKjQgnzZj2LOOFBa1NAaUhGFdlBM2i6maPiF2xWiDP6GD-J3pQ2TMJxTErQ7ck232WJAVJFD4-m08eYZK8BUxGVNva73KXMdun0GzDCHs6-W-kYy50o9vyp2su_ZZH4dTGrLijKHJfCRxP2-lXRKQS8IdVyNW7rNiAWQN4FI5bmyzSxHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abe26c296f.mp4?token=JfYKWxTHy2zCJq4WdNPOqMFexo2Sd91GyEvSYpTo57aiXwyhUFm9jEHPesW63YgvSslojd_NFOcX2H2fJmEyc2iviu-MixqwdNA7PO3MysfbiQHwFAfAYsWZC_0k7IQ8OIMU0DRmRozGVWB9IWg-bt-b2OywsPQWymyCjTKjQgnzZj2LOOFBa1NAaUhGFdlBM2i6maPiF2xWiDP6GD-J3pQ2TMJxTErQ7ck232WJAVJFD4-m08eYZK8BUxGVNva73KXMdun0GzDCHs6-W-kYy50o9vyp2su_ZZH4dTGrLijKHJfCRxP2-lXRKQS8IdVyNW7rNiAWQN4FI5bmyzSxHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ویدیویی‌از اولین‌پنالتی تاریخ فوتبال که کلا 0.2 ثانیه توپ تو دروازه‌بود. دربازی این هفته لیگ MLS به این شکل که مشاهده میکنید بدون اینکه توپ به تور، تیرک یا دروازه‌بان برخوردی کنه گل میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29602" target="_blank">📅 16:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29601">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_k8c2tSGIwy3mD0GKPPALJ6s8LHb80k-jswfmxEe8BeGiyXYaGmg2Lj8XiKgjKZxrhMeA6ngrT_aQKoBJjkI9pYkapzm_uTw0a0x0weMxiLD2XrpmlAnqgznkUqdYFV-Hw6pIKyr9VJx_1FuVsJ32X7DfSfbwmrtGAo9662kOr2jgPtCAQfF-g9Et48TIacZeoMyzhR6Huo4Ps8XRgchPxuFYYlzDyFI1i2BBmQX-1cGNEw42ddAGHoED9AUXefIHQZx40Mah32iSVh54H88TLPh41_AQV9zfzDeRshzYQbWOKSZll_MLkOVKyCZivZ_m_5r3-AT2DW1Yu-LXVbCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یاسر آسانی ستاره‌آلبانیایی‌استقلال یک خونه 75 متری در غرب تهران برای تدارکاتچی آبی‌ها خرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29601" target="_blank">📅 15:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29600">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zvp_katzxCibRtNsjJxn75zw7elGDxzD2GV7mDtv5LQqYZwXgzZtHLfA4O0zBaw0YRFRRvawbdOGcDCzaU54srtcbCsjUdWGaLjorgDhuZ1YuMHr7p_d-UoQsrnqs-hm8oMX6sWOMzYANNvwmLCVe-rAv-t77ycRPCZ47yyj6PXOH1gE7oaWs8t9gOP6d8tpd8xQEEAx-D_4CpSnUbaLw81LcSlWlRA2OnTQ-f8CDUd1ju3AQJsHHURV0d13jZVyLHUvSuwyNLrZO6rBgOsvxG1Mxrn-aHI86kLZa9RJOZE9Ox5u2DnJeECgJbAIhLtELzoiRHco6oe5QzIPE0Feyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29600" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29599">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_rvDPUrs1buLFgPLritmJqis2UIZZpSkknWdgHP-vCKjT9AQElEB54k1Qb4iAhbImPX42fVE7VNF4vmcpqli8fhRWcBbjpR_4rWEtw2BZaVDUzpnT2aL63Kc-zpI2ONEbyXYkOb98X3bOD9wkI4NKG3LGEFT8OK-zXaeU0EKEx6cvsHXcDPqVbOkebjiGACaQfWHe2HI8npH207uC_NHEURqrHYX0-q9mDnWkSNrcjaE-dUUAy6gB_d_nhSOUA5-8MfBTS7mD2nuBCyB6K64Ub2ke_Sz5vxU-QoNlA0_xjaxcvoHrqQo3u4VYEvj97mcsWcyrxK75qT48z8i74HtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ بارسا در لیگ قهرمانان اروپا؛ رافینیا و فرصت تبدیل شدن به بهترین گلزن تاریخ بارسا در چمپیونزلیگ، بعد از لئو مسی افسانه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29599" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29597">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2a23445f.mp4?token=Jgyh2Gmcw0ozc1pF6reYUd5kql4iBdun7INDUbNvkJsUrd1qwEq_IJWQQY3aOXK50ZsTgsz5idiDDveXHbAIKPTwSJHXhi6yCAhcO_lB97tUBIqmmGq9rRaHRLQ3sdB7-5D2P9oFOzaqL2vCMQ6ScUpz0Fh3VZ1DfgZB3uYMOEaeChA7CMVcXFX0ytK_WaxOTu_DNqUZdufohYMUrIxAHxmbnn6O6Mc0O4m-kprLSvRp6UPlSftlLVa1yEjiet1_AlYMYLLDlCFvolWhDJTlgtYrGks_mUAeRtfzo05a-NpvPwf5Mr6Vy6Whkb3wMm-9Ku-i7SzjK9Jdo2cVPkahIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2a23445f.mp4?token=Jgyh2Gmcw0ozc1pF6reYUd5kql4iBdun7INDUbNvkJsUrd1qwEq_IJWQQY3aOXK50ZsTgsz5idiDDveXHbAIKPTwSJHXhi6yCAhcO_lB97tUBIqmmGq9rRaHRLQ3sdB7-5D2P9oFOzaqL2vCMQ6ScUpz0Fh3VZ1DfgZB3uYMOEaeChA7CMVcXFX0ytK_WaxOTu_DNqUZdufohYMUrIxAHxmbnn6O6Mc0O4m-kprLSvRp6UPlSftlLVa1yEjiet1_AlYMYLLDlCFvolWhDJTlgtYrGks_mUAeRtfzo05a-NpvPwf5Mr6Vy6Whkb3wMm-9Ku-i7SzjK9Jdo2cVPkahIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شاگردان پیاتزا بابرتری قاطع 3 بر 1 برابر استرالیا درنیمه‌نهایی جام ملت‌های آسیا به فینال این رقابت‌ها راه پیدا کرد و در فینال برای قهرمانی آسیا به مصاف برنده دیدار امروز ژاپن و کره جنوبی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29597" target="_blank">📅 15:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29596">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiNmDCtDno9ZaY8u0yODmAMeR_C9aARXWSyXNHprZBbbbaT2TCzCk3FsN6ulhzSsOACRs4awYytY7fRqN6l0mJHTq3HRGoocgJKxsDu3hi1MMTNEIkWyhSk_ds4V-7ChRd2_fOXxFWt-RsrsINpRCwGwNZOPHdN44x1LWoBi5Dy2-7US_cEAuSXQVGNy4HSNio3FDPtQNFJ1jbP161_fV4FdVrtEsKyaHHMVptRrt5PQ_jJffA7aHWL6LRm4S_jw0u4ksNw6IoIJtBYGi2V1zBMZVJpmHtqmbqvljrUMHBhFya-ita4d89_uNjYP6hXRSDT4mpYlz4O-IiekCOrJag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاریوس دروازه‌بان سابق باشگاه لیورپول در کنار همسرش دیلتا لئوتا گزارشگر شبکه ایتالیایی DAZN
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29596" target="_blank">📅 14:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29595">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDWjAzpVA8zT7xR5nyUmY8c5vyzvoEvr0uXWZeZoYsLNkXSa64hp2ouxRuj4YrcCF1KnzzdWtXeKkgXncyfVBxm-bWYYgBk_Dj6MhPOv-NjJBKzxV-krKoVVcqf7DxuyPM_c5mDZjZzmnK5XPGo0May9oUynFcBLveN2bujfxcF_GA4TBZFiXtQoDSfl-yk505PGyYGVTUMw_Zw3Ht3_MMxH2Lcfu9IVfs5nZeqJoez9RjfiATerGEtJ-E27klMranjkqPxJrS-Od-H84gWDvGlZ0NZEMizPUMDHW2kdBWqc3KgZw2KUlnDRtoaS5Y2z2OGUG7RfL7dcfLr_G1ntBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌ویدیواز اول تاآخرش‌سم بود از دست ندید؛  مهدی توتونچی تو برنامه‌شبکه‌ورزش نادر محمدی رو اورده بود رو آنتن زنده بهش میگه شنیدم میکل آرتتا دنبالته که تو روبرای آرسنال بگیره نادر هم کلا ویدیو کال رو قطع میکنه. بعد توتونچی میگه آخیش! پست ریپلای شده رو هم…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29595" target="_blank">📅 14:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29594">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVjKt-vmxCZ0FIluOH590eGThKYnfKc_6N0DeFadD1hfqVvzfEc1KpzToQys77QEgtQ1eCnz7-7B1i3MST3OCj6EnGdavcSdeMnlNzGkjR0GTO-rfoTGAcM7bQjbn6GSh3ftn6HAf4Z_7USeuw2Bh2-qShpi6NOGKTDe1pG1E9jpTJwe9FbcMi3QGBq1SMS1rSLxH-_KD3zmK0UnRdMUaOLjy0AbV1LDF1A6jQTNKmATdH5-SOLPl9e8QO5qPSCVGqYw15NCZWacMFIDUNR4OFOZV_7isGfAw-xrisdycdyiAGMSk456mmI0AxS3HvqiJWYzd58ysIgXNQFoqOqL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟡
🇧🇷
طبق گفته رسانه‌های معتبر عربستانی؛ ریچارلیسون ستاره 29 ساله تیم ملی برزیل و سابق تاتنهام در دو راهی النصر و الاتحاد قرار گرفته و به احتمال‌زیاد راهی یکی‌از این‌دوتیم آسیایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29594" target="_blank">📅 13:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29593">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY00_J3_6cdJLkux6051321TTeuMI0XNNpwODgSRuI3aL4lAi9xRl7iiwpHbvhLuefMVeZjdLBCb_wcfgQK-4eSYcIUDdIf1Qu5p8VtFXxfPa31CKNKnOHh0zEbgQ34U07r2UhqwE5aRnkqtzyAv4TACd8nYYxv217GIHaJQGLytw3DzBLJ__x4AYxLcS7R6Po6cwwEYcWUfY0xB_DANOnC9yue4lCdwDr8uHbTdzntl0xp1tymUbNmg5hgvMwZ7Z-_QGJQFxALvCYB4g3VV2RMyXun1ADN-Dv1x29Y4HUO8Yu5vfWSoXGFeob61LzDLU5LaPUps7SaEx9-JhwIHjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بااعلام‌پزشکان باشگاه تراکتور؛ پارگی رباط صلیبی مهدی ترابی تایید شد و این بازیکن 32 ساله رقابت‌های این فصل لیگ برتر رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29593" target="_blank">📅 13:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29591">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29591" target="_blank">📅 13:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29590">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGjK0H5xGdY6co21-CnzVfSC6PbKQXLC91W2mHkHcenT9m7ctiEghKbOUvaXFg9uJx3Poe9S0uqW2Fpa_8JxBbnzrqs1O5CDvnY0LN0A3tspVurIrjXYOUPxyy9FJ7ViJexVoDlNnIAK3mRlm8G3xsMapoBVSqxFPdnnpDsNHbDYQzpozMAQ22PcFHPbNcVAsLZLm4R6r2ho-C-SsXOZSNJnFYOyonzMO_jzB-swMNfzHPEGCv4VgCTS3GzMBbZfrgtgRc0ZPFvoJ8aDYWOU3r5Lyrrv2qy_nHFA7xYwrTISy7SGRjBbOYIXSiX--4LAVQntL-fswdM_JkdqhMTAtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
باشگاه پیکان از باشگاه استقلال به خاطر استفاده کردن از جلال الدین ماشاریپوف در تقابل اخیر دو تیم به کمیته انضباطی فدراسیون فوتبال شکایت کرد.
‼️
باشگاه‌پیکان‌مدعیه‌نام‌ماشاریپوف فصل گذشته از لیست استقلال‌خارج‌شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان،…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29590" target="_blank">📅 13:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29588">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlnwzBRan8ciFXaYJCZyn2yB7-cbtxjt8I6PKS-nE6zputVCRY4HBLZvIZeQpLxjfrgrWhZKpNNRSSZ_v_01FRYrA3GmvpujTZXcwY8ndUS_oBjkfbTE0mODUu6s-Hkk3_w15Q0-1XiJ7yGAwXqSR2oiNhv9KX5bQ71HDhHnygySuRh46y0Asvjxc4vparjUMwhmoVx7vxKllMtZrX7NuJ5KbbyvHuIlbx7ou--U3NJzOYbkCr0pfaCXRhaBR0iJEW70G2B_Nlg-wYrNhhh3tchInOGA2HKbzFKEqYj7LNWQsNBL_kLnzDuAFtVqbzw5otSQRjVfw0e84jYkn-x1Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
معیارهای رای‌دهی به توپ طلا؛ عملکرد فردی؛ نمایش بازیکن در طول فصل و لحظات مهم و تاثیر گذار؛ موفقیت‌های تیمی؛ جام‌هایی که تیم به دست آورده و میزان تاثیرگذاری بازیکن درکسب آنها؛ بازی جوانمردانه؛ رفتار،احترام‌وشخصیت‌بازیکن درزمین‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29588" target="_blank">📅 12:43 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
