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
<img src="https://cdn4.telesco.pe/file/t_lD_O9vtDOjG8xFisZ-Zi4gbfTCblaJ6Fi9AnO-jDVbp41P-ahX7ZFCsWHxa6SPcq5eFQ0FIuoMfQ_9okzyTw0KdM6NLJvLNExhWVmVR-wFeEg1bqiQoy8FlkQTFFnvDTJZs5tcJeGY8VRQ3w2g06yJ0N52qeukL4eUXIZhTD6XoawNCGJKfxPPt6cY3ipeGSn_2QOCVeXUbTSWWVv9TmfD7l5MueIsGGt2AFoGHN0M_c2Pf4s8kBVU9aXRGVqBMlEp0u7jrycyDhrkDP74WtsSSbZAD3Y2_PFnub2SneWrvF3Eu1XgURznkpVByGaP8RCnF6D6tgDVW_AivWz5QA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 975K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 14:56:10</div>
<hr>

<div class="tg-post" id="msg-126253">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cd2922db.mp4?token=rA2r-Lk7Ipj5x1WudWBESK00_t901LlcypgARSIHT2pTsA3Rdtz2bCVVssuh9KdYBntMyQiIY2f7kTjtlKB4K3GpkYmo2Y0KOmr9b_e0gonjhFo57TjBlmYM_vCqJZps6jJVaUMCRYg1-S_jktc6_JS5cmPGNPZb4YhB8SsaoGV1HsGdM7-O4kU3r0AUyOsO6wJR_MzfLQr7eSbnW4HZeW6X1RnsZJPwue71_PMzMHw6BPBlAl8TECZpyx4j09vXDMD_-crYBI5RmqGwTzz364D1-Cdkq2yyzpOnVG2QVyk_UbHXN2hLUdUPWH6xNKBVN_Z4hU7048jXb76Amgig0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cd2922db.mp4?token=rA2r-Lk7Ipj5x1WudWBESK00_t901LlcypgARSIHT2pTsA3Rdtz2bCVVssuh9KdYBntMyQiIY2f7kTjtlKB4K3GpkYmo2Y0KOmr9b_e0gonjhFo57TjBlmYM_vCqJZps6jJVaUMCRYg1-S_jktc6_JS5cmPGNPZb4YhB8SsaoGV1HsGdM7-O4kU3r0AUyOsO6wJR_MzfLQr7eSbnW4HZeW6X1RnsZJPwue71_PMzMHw6BPBlAl8TECZpyx4j09vXDMD_-crYBI5RmqGwTzz364D1-Cdkq2yyzpOnVG2QVyk_UbHXN2hLUdUPWH6xNKBVN_Z4hU7048jXb76Amgig0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت دفاع اسرائیل این ویدیو از حمله به سیستم‌های دفاعی هوایی ایران رو منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/126253" target="_blank">📅 14:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126252">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayRfs5DJBL5syxrG91ngq8a4DnqQQQGfTDpYZnYMmFjiOPSirLwOuGXTRHTyCc9WSWb1p6aKyNqNbuedUPwGHQxRVsSjKkQN1CkQ_y8wZCnYg9A0CTT0pwKLT2DlPA5E2w_sUPczevLrUBepWnvud41lhMoWJS72as60o6rId_bh4J-xMyZdGBZY1w80v1ujtDL8UaS-e3Iv8M1D5flbaBJEjOAnilTqPr4hw5Zy2-H2cGNtdV-ReiB9wSR1me2c3jzkzBQ25TMDhsMWLWWJtIJu5Gtw9W1DGgyDFBbvbwBmCUolHNy9KDF1VQUaaCIFfTlOkfpxq5VFdLQ3Jbqc1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: جنگ ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/126252" target="_blank">📅 14:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126251">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiK3m-dLfOthp1T6_yl9-WZRfM-BaRzybjb50pWr2XkDCjGerBUyPiZkVlgMqaSOwIAh8-ZlGhR-e3UJIzdq0IDot_Qw1tnVxp9_rttnNVxbn6k6sC8yPw0XHR0vhPY7thGzAlX0c35byUga56FDWEQzRlAsXD79RCBCRyKxQnZ5JLwUOQPQ5tepwyEf_XzUUv72xY3jR82n-kIi8bmpHAANQVi9fAjATHX5bUPgkZj5VPAey0Qk3lcZn7SwGpTbrdww8JMrEcn3_Q1VR75Kv5DzUcbe13fvppgOy-1ldGzNFLgwx9gHaKyKaQiAH2cqSjZ02u-QHpeToRlkqWBFlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/alonews/126251" target="_blank">📅 14:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126250">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
قرارگاه مرکزی خاتم‌: توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما در صورت تداوم حملات، از جمله در جنوب لبنان، اقدامات شدیدتر در راه خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/126250" target="_blank">📅 14:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126249">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
اکسیوس: یک مقام آمریکایی گفت که تماس ترامپ و نتانیاهو «مودبانه» بود، اما نتانیاهو در برابر درخواست ترامپ مقاومت کرده است.
🔴
این مقام آمریکایی گفت: «به صراحت به نتانیاهو گفته شد که این چرخه باید پایان یابد. آمریکا با این حملات موافقت یا از آنها حمایت نکرد.»
🔴
در حالی که دو مقام آمریکایی گفتند نیروهای نظامی ایالات متحده در حملات اسرائیل به ایران نقشی نداشته اند، یک مقام اسرائیلی گفت که آمریکا در رهگیری حملات ایران به اسرائیل کمک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/126249" target="_blank">📅 14:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126248">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوری / اسرائیل هیوم: اسرائیل و ایالات متحده پیامی به ایران ارسال کردن که اگه تهران حمله دیگری انجام نده، هیچ حمله‌ای علیش نمیشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/126248" target="_blank">📅 14:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126247">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سفیر آمریکا در لبنان: اگر حزب‌الله حملات خود علیه اسرائیل را متوقف کند، اسرائیل نیز ضاحیه (حومه جنوبی بیروت) را هدف قرار نخواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/126247" target="_blank">📅 14:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126243">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v4rgDGhWTsiptVu8w_dDugCqKyfCNpS9nU-JuDKLYr76Q-mnp8TjoFd5bc0qV4ckEtzywdHXzWBOpAkayyifrJfVNbLk82H4SMuxGmQv6qO7r-yTtXXB0H6FtgcAWFFs1PYWp7B4kPj4KstSEw6DmR_zNsuuEDOw6B4hy4LpfjCnlXLZ8ahq_eLlmSMz6kJAtJlpLFMv7BA3ewXrAgUuDAlXol74ozZn1oZdS5B0bUayoxHK4mlMposvUC9FlWGp7ooZqUSTKUU02xCxied3xIJ4OvGIqLadOHY1BWDAZTErk4sKuGq0bLpf8QQm_ao-xdwMcTiu0XiKRsrazGek5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhuWd1UGvWEmpz-DRytpMChFS-shsshaliUZeT4lYMK4lWtCOQJBpJ3AgUCayxMWL3sp3B9mI2_JGl2oQRp-FLdA3VJD_2-PeV6YcEbko1L4x6KcN8yTt9wlzPmMIxYs_0Tpru7H5Ni6ibsnmvitT_YJ0j2lOPP58UCX5DF8Bxo8-iUvaWYUelNodYoyGOFwL5hYgy1vkqvW0Wqgbzk1mBiUgPa9CkoVnsRXJAkx85xDrGCAR_IpkGr5DNvvgHT9CT6v-J1sV5WoGK50WyTUS_pqfqBKXQtDm3d15YIqApFLNpSMpARRjyUiY_dwGb7w7KgSyIPmzfpWMDOlGkZWTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gqIVD6F-FR2pLoGaj3E85FTjwESSxoslAPyFvXbb04gKQ_aRiC329XnYoPCK956Gr8u5J2oo8M7H9y6ySzXnn9X6k1_2ccxKYD1H1fdtAwV1ISOV0mR0LCpVmSvbLbukYRi41hJchjX5T2S2evIwOhKjY5hE_LZy3usd54MUGSSvXX3uqDgReiPOzGM8HpnN_T8iEBsBX_jt5IJWP9sIQh1HIjmLGlwHMCKZXzKT9NN9f5IpdX9OmKScmos2_dOh4QP6fIcuR9pRWLi7gOrjlwUfXVieu8uakCeJmZB2qJQfe-_U1OpxR6cNEtsSwMmCS5Ksfgaatd8bDPP87svZaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DW1dW9Lv_-WTP5dtBrGTDAsCGCbJh3w1TFb24UORzRxMd2WInOHbCd9C2gAcXRNfxTEMziz8B0PK9k3U2v6o7E6WlD5qoENNp8GxLQd9KUHfP6CzJ9zDXB_Elw8aoCJ03YINRp7sVXYT_BGJmPt53kbIHbxTePJGiHbPClLBipKsZobg9eKXvkYU7-9Ff19nPSesnvtcZA0LHov7JOXrWG4xSka65QDamL7jrsh6TOsW08JDR7Ml6aZZYpN6dDT6M_ogoYoz13KmsuaKhTIilgS8xrrwniwsOqAkpAAJgH_MMwraQ8iBkAuEF1-YcIYJ0DhD56I4iAThMQLAUbkejw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عکاس
اسرائیلی
؛ رفته کنار یه پوستر موشک ایرانی که تو اریحا فرو رفته، وایساده و عکس گرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/126243" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126242">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
فرماندهی سپاه تو خلیج فارس : هر شناور رزمی متعلق به کشورهای دشمن حق ورود به خلیج فارس رو نداره و در صورت ورود، هدف قرار می‌گیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/126242" target="_blank">📅 14:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126241">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کیر استارمر ، نخست وزیر بریتانیا: مذاکرات جدی برای صلح پایدار در جریان است و مهم است که به آنها هر فرصتی برای موفقیت داده شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/126241" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126240">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی: ایران باید به تعهدات خود عمل کند و از فعالیت‌های غیرقانونی خودداری کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/126240" target="_blank">📅 14:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126239">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
اگه آمریکا، اسرائیل رو بمبارون کرد تعجب نکنید چون ترامپ رئیس جمهوره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/126239" target="_blank">📅 14:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126238">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ترامپ: به اسرائیل میگم بس کنید تا برخورد نکردیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/126238" target="_blank">📅 14:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126237">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
🔴
نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/126237" target="_blank">📅 14:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126236">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترامپ: هر دو طرف، اسرائیل و ایران، به دنبال برقراری آتش‌بس فوری هستند!
🔴
مذاکرات نهایی درباره «صلح» در حال پیشرفت است، مشروط بر اینکه جهل یا حماقت مانع آن نشود.
🔴
محاصره به قوت خود باقی خواهد ماند و با قدرت کامل اجرا می‌شود، تا زمانی که «توافق نهایی» حاصل شود.
🔴
اوضاع باید سریع پیش برود. از توجه شما به این موضوع سپاسگزارم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126236" target="_blank">📅 14:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126235">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvV_1ex6NxWl1ZsExuyR2Nlvc2Fe46pzPwC-MJrHE34FNlLwJwCkIk06Cycdz_GVUXLzfy6yJfgHaNWiQUFyYoZLqhbeTZYTgsmSTbuQqlXVQrRDnHfavFcWncmZ5rKeedP-4-zK6YuGIwn1_2HzbGL_S5Z_OAmhXEiec0YskZWY0uBmoZ2nuEVviugmUBqb0GCRoGxjZlYGB2mwkpF5gsYHBK_bBhkxPjRFdRf-olyk6HLQFlF7LwSr1rDzr-tywUKCy4mR4VZDoCVI2vLB_FjFsVuvbNax3txQLUxWzflXnlmdC66BFaOt2v7n7PHWkJWXOuZpUCaeDcONhhRbQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / یه جت خصوصی از امارات ،با وجود لغو تمام پرواز ها داره میاد تو کشور  و نزدیک تهرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/126235" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126234">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
زلزله‌ای به قدرت ۴ ریشتر ظهر امروز حوالی مهران در استان ایلام را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/126234" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126233">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه چین : پکن به‌شدت نگران وضعیت فعلی و از سر گرفته شدن درگیری‌ها بین اسرائیل و ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/126233" target="_blank">📅 13:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126232">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری/یک کشتی هندی در دریای عمان هدف قرار گرفت و دچار آتش‌سوزی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/126232" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126231">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
انهدام یک پهپاد اسرائیلی در غرب تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/126231" target="_blank">📅 13:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126230">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
یک منبع نظامی به تسنیم: ایران برای جنگ طولانی مدت آماده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/126230" target="_blank">📅 13:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126229">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
فارس: تو غرب تهران پهپاد زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/126229" target="_blank">📅 13:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126228">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdqowOAE_eFfnvg_LiLDNsm2lVTcciXVxO_M-V4TPVllSfStW9AsRWTh4V5ULMQ68Xw_RKeeG-ZR1_aoQEHEbkrO5A1_cqPcwg4cypczfbmHtR-vzMnvPPZ_5bwR7C1v7HCL9tdX1irsaJ5Y1ZDnD1zfDxqDM7xCnz2AucqlSWsisjMrGosfCT3p92_s55iCaKF7SkG-4ISvIKuljbYVVBXT1gWj-pfhCJcLVk4cQCSAUlb2kqofVF6qAMdguwV_fWpoBfh6QH7wkzV4XXuSsI7K0PNDjcZI5ojlMHHgQa6Loe7IroPea6R5-tH6u3ZkPzpHsyCTS-gzj-oRGTYOig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۲ گزارش می‌دهد که ارتش اسرائیل برای احتمال یک جنگ طولانی با ایران آماده می‌شود، در حالی که «عملیات شیر غرش‌کننده» ادامه دارد و اهداف جدید در حال حاضر تعیین می‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/126228" target="_blank">📅 13:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126227">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
نفت: ۹۷ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/126227" target="_blank">📅 13:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126226">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
آسوشیتدپرس: سوریه فرودگاه دمشق را به دلیل درگیری ایران و اسرائیل موقتاً تعطیل کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/126226" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126225">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
لغو پرواز‌های مشهد به تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/126225" target="_blank">📅 13:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126224">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ: اسرائیل و ایران باید فوراً تیراندازی را متوقف کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/126224" target="_blank">📅 13:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126223">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: اگر فرصتی برای ترور رهبران حزب‌الله در حومه بیروت پیش آید، در انجام حمله هرگز تردید نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/126223" target="_blank">📅 13:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126222">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
اورژانس تهران: هیچ مصدومی در تهران تا به الان نداشتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/126222" target="_blank">📅 13:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126221">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
سازمان ملل ابراز نگرانی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/126221" target="_blank">📅 12:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126220">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YV7hUSa2cRP2ZfTs6JlTB9znhZTbqlofy-lrydta6cU1hi6oqBaHqZEU6cZo6cGliDw1O4w-vER24PplqMaGkEsbxo_lV-3010xMcmY63VruuefmOIzAt2Q8eH_WPba5HnqK4wrxPJCHxQMmhGqBPe87fUR9tnoPOBQMaKS-i09JHw-HuRIbeY2BTm1iaOtLSSLC2jvfI7wur7ta6n0XPomTWMwhl2D3MqPUDvNsY12yqF16GEL7znjYCBcBSGb1wxc6VoqJyiYuNWbRFB1U3vRuZx_QCLcyFmWhqfzd5aWSXb52L1sp8XOKwHlJ5e92C_zL4B6s4j0eUPRo-w-krg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمان منطقه ؛ هم اکنون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/126220" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126219">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
منبع ارشد امنیتی ایران به المیادین:
ما قاطعانه تأیید می کنیم که معادله قبلی  «زیرساخت در مقابل زیرساخت»، همچنان معتبر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/126219" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126218">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل:
تاکنون، ایران بین ۲۲ تا ۲۴ موشک به سمت اسرائیل شلیک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/126218" target="_blank">📅 12:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126217">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12238f728b.mp4?token=RkUeBlKeXorn1UlRIYqANagou4EjkPKm1JQJX0G-7h-He4DR0fCR_s8JGmJrqPbGjQCuvD9z8Z_eZ-HNhz4LvJWPw6YV6jwmt15qRI5FkmR0hRdCt1mxivn88OaIZcYJq9GyQnk2r7hVcoL3wmRpTA3Wx4kYhA4sUfGCjN0eu8ZVUxEU80Hbgb4G1Q-_83Uk6QrItVrk6T4SxtRkkFPnl_aglFDKrFAo5YNqMd5fXW2GoRCPzh6X39bo-fZZ_pomC0b-BGtlCOMvfj_C5-jZiiQZS4HLXlAIdGl2HLpbYx67X8nDr-BMzvfL7fUsamsanvRMUxosa24Tm4Khgdg09g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12238f728b.mp4?token=RkUeBlKeXorn1UlRIYqANagou4EjkPKm1JQJX0G-7h-He4DR0fCR_s8JGmJrqPbGjQCuvD9z8Z_eZ-HNhz4LvJWPw6YV6jwmt15qRI5FkmR0hRdCt1mxivn88OaIZcYJq9GyQnk2r7hVcoL3wmRpTA3Wx4kYhA4sUfGCjN0eu8ZVUxEU80Hbgb4G1Q-_83Uk6QrItVrk6T4SxtRkkFPnl_aglFDKrFAo5YNqMd5fXW2GoRCPzh6X39bo-fZZ_pomC0b-BGtlCOMvfj_C5-jZiiQZS4HLXlAIdGl2HLpbYx67X8nDr-BMzvfL7fUsamsanvRMUxosa24Tm4Khgdg09g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا: «فقط کشورهای احمق وقتی به آنها شلیک می‌شود، پاسخ نمی‌دهند»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/126217" target="_blank">📅 12:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126216">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
هشدار دادستانی کل کشور درباره انتشار تصاویر محل اصابت پرتابه‌های دشمن: با متخلفان برخورد قاطع قانونی صورت می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/126216" target="_blank">📅 12:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126215">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6yV5s0_MWPVJ12r8rp9iuSvAEvYeEqXa7mw3TzUiMw6-yQAp6dz5MZt25YlkhSOOehLhSVM-Dzx_osaeGW96Ln8FfxUNODknsVLzm3ezkytmtQVW_30I0EwoTOBhEWMjDao7_Mi_01LlEhQaIj3CGdaNhJllKUo-wKZL2TDf63POgyN2w8NG9TsfMSDwltKOw-HZ4nA8xEppbMuKI27C1DIuT4LEfIAYjvaZleBXnymMc9VUoZECerXfiWYSTQdNq4C966MKEGh95749PsCSlMPejdb3WVNpFjEwKkIQDudrwtYUkbZrN_GVOfPEA7BUacYR_Sdz5P6HAZpkxFclw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره: اوری گلدبرگ، مفسر سیاسی، به الجزیره گفت که پس از تشدید تنش‌های نظامی اخیر اسرائیل در ایران و لبنان، روابط بین ایالات متحده و اسرائیل در معرض خطر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/126215" target="_blank">📅 12:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126214">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
رسانه‌های عبری: شرکت هواپیمایی ویز ایر پروازهای خود به «اسرائیل» را تا روز چهارشنبه تعلیق کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/126214" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126213">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5391f1a037.mp4?token=NLljvNTnva16ezdnAmTQGeH9qQCr4mAITJdEN5fGhElEI85TNf5tHz2BBB7pUlODUh9kUrUGRKNemdj48UtRIBxasTuXkZRxn8b568ZKPdKQye1oibWaWiwoM-YK3OlHAdMdbjNWfwgYCsEJwqip8he8Oa_iNOuhBSbCd6loiKyBz6GMY8Byq_zA5hX5yu_ELN4bOWz9Yy3WBGyKiCSOwvZaaVYdVZrbU_PykzK-Gp1ZvFSYHNX7WX_Dta35wa5ZNRl6sD6KriTdtwHt6U1froNYuzuAHYTzmojQp_4rY2jZ9SZoIDopTTFwnqz-qnqkeByz2tbTk6oNd3sfrmtKGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5391f1a037.mp4?token=NLljvNTnva16ezdnAmTQGeH9qQCr4mAITJdEN5fGhElEI85TNf5tHz2BBB7pUlODUh9kUrUGRKNemdj48UtRIBxasTuXkZRxn8b568ZKPdKQye1oibWaWiwoM-YK3OlHAdMdbjNWfwgYCsEJwqip8he8Oa_iNOuhBSbCd6loiKyBz6GMY8Byq_zA5hX5yu_ELN4bOWz9Yy3WBGyKiCSOwvZaaVYdVZrbU_PykzK-Gp1ZvFSYHNX7WX_Dta35wa5ZNRl6sD6KriTdtwHt6U1froNYuzuAHYTzmojQp_4rY2jZ9SZoIDopTTFwnqz-qnqkeByz2tbTk6oNd3sfrmtKGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من تازه آنلاین شدم، آتش بس نقض شده؟</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/126213" target="_blank">📅 12:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126212">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">من تازه آنلاین شدم، آتش بس نقض شده؟</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/126212" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126211">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rktq-1pvZ2fIgTPFWlxk3UuQmK0C-Rc_buNmK-DjdYEo4FaU8Hnim5jQBj9ukm2QUgLoxmPIBv-gYsfIASiku8cLuaQJxIDTzqqq7OebL6DffJhYN7di5NQguvzbSrSPtxvpYK0njpWO7iwa1W0rcdQ1xlj9WwofUiWyQ2cPRLye8W5K6TR45JurfZAESQ-CHklr9y0jv0-gbAdLOzyzbVoGUJlVM8ZtHjVVUzPx6IgAN5Dah84YKhsaiJ8f1KhJJ2Sl-OGyrsvdiqiz4BT3iXg9SXSbxEzDVDjb0DGmyOqGyi63g_x1cYTWnxZbf8fO-j7_WNIWxRQNRbiJrdDuzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در حال حاضر جنگ ایران و اسرائیل را رها کرده و پست های مربوط به انتخابات منتشر می کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/126211" target="_blank">📅 12:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126210">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
آکسیوس به نقل از رادیو ارتش اسرائیل اعلام کرد که ارتش خود را برای چندین روز درگیری در ایران و احتمال بازگشت به یک نبرد طولانی‌مدت آماده می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/126210" target="_blank">📅 12:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126209">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ارتش اسرائیل گزارش می‌دهد که حملات به ایران تنها توسط اسرائیل انجام شده است و هیچ مشارکتی از سوی آمریکا نبوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/126209" target="_blank">📅 12:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126208">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
الحدث به نقل از سفیر آمریکا در بیروت:
قرار است مذاکرات لبنان و اسرائیل در واشنگتن از سر گرفته شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/126208" target="_blank">📅 12:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126207">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
قیمت دلار آزاد به ۱۷۸ هزار تومان رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/126207" target="_blank">📅 12:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126206">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری / روسیا الیوم نوشت: ترامپ به پیاده کردن نیروهای ویژه در ایران تهدید کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/126206" target="_blank">📅 12:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126205">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل: حملات به سامانه‌های دفاعی استراتژیک در ‌ایران را تکمیل کرده‌ایم
🔴
نیروی هوایی به حملات خود در عمق خاک ایران ادامه می‌دهد و این حملات شامل فرودگاه شیراز در جنوب ایران نیز می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/126205" target="_blank">📅 12:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126204">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
مهر: هیچ اصابت یا برخوردی در فرودگاه شیراز رخ نداده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/126204" target="_blank">📅 12:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126203">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فوری/نائب ریس کمیسیون صنایع: امکان قطع اینترنت بین‌الملل وجود دارد
🔴
بالاخره شرایط جنگی است و مصلحت ایران اولویت دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/126203" target="_blank">📅 12:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126202">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
دقایقی قبل، تهران
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/126202" target="_blank">📅 12:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126201">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e7a96493f.mp4?token=M1I4GdxYs3PlfCSQhIC-9-eslSA1mJsMjhq5LqIIYyX_dfCRBKFDbfeqJBgy9mUhZQipGv96oAIa4wwJQPHakpFQZRvKmgEGdwl5fao11kbZ3tTlaoIkEwCNPUtDUaaiA-DwK36k3SN69OfeJqvu_1zRY86igfjaf2AT9fUGlxKOSPHmMIqXzXpZEsumTOkRU04KpJVXLneT8d3H5XC9d5Iu16XHDewaQNMQ6FDaEg47mPbaq2je-Vm4LkKowVCAV8E7tI_m9_3EKxibnh4D5j5rQJh1a0nHYU7sFINzMqKM23WkJjRU56nEVG2-iXsEHERFq2SomLRArORSFElIoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e7a96493f.mp4?token=M1I4GdxYs3PlfCSQhIC-9-eslSA1mJsMjhq5LqIIYyX_dfCRBKFDbfeqJBgy9mUhZQipGv96oAIa4wwJQPHakpFQZRvKmgEGdwl5fao11kbZ3tTlaoIkEwCNPUtDUaaiA-DwK36k3SN69OfeJqvu_1zRY86igfjaf2AT9fUGlxKOSPHmMIqXzXpZEsumTOkRU04KpJVXLneT8d3H5XC9d5Iu16XHDewaQNMQ6FDaEg47mPbaq2je-Vm4LkKowVCAV8E7tI_m9_3EKxibnh4D5j5rQJh1a0nHYU7sFINzMqKM23WkJjRU56nEVG2-iXsEHERFq2SomLRArORSFElIoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آسمان یزد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/126201" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126200">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سخنگوی شهرداری تهران: پارکینگ‌های زیرسطحی برای استفاده به عنوان پناهگاه آماده می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/126200" target="_blank">📅 12:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126199">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
برخی منابع از شنیده شدن صدای انفجار در کرج خبر داده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/126199" target="_blank">📅 12:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126198">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
خبرگزاری مهر خبر خود را تکذیب کرد!
🔴
بر اساس پیگیری‌های خبرنگار مهر هیچگونه انفجاری طی ساعت اخیر در اصفهان رخ نداده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/126198" target="_blank">📅 12:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126197">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcDmW5tBIerXk1yjz3_qTEuqN_P2_cHfgjPFS0wBGGo0Fo4sqIzUTAYL7M3PzGONRq7d1HZxOm4knXMgF-u1O3YfXWY2engzV-tVLS5GwHc3ZW9gBga2NKdyWUpgDXoLVkuk2FhWPPKO3WS6NKIcA3-RmEJhYD7TmXuTN00LMmY1zVKKVEYMF07DpUM3cwcQru2ZQBkkc8KF3hAx_8qnVKi3ctyZ410r7tenYee_fpaHmT2BPWh9FYU0G1sBXYnnmn8N_q6sMJ52YC2ZZdxLggLVb_OLpPUcCH_PZD27er_WqCqYxzojCLyqP4wYmKbsw_k65L0gVh5wNewnF4coPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاهده دود از شرق تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/126197" target="_blank">📅 12:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126196">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
صدای انفجار و فعالیت پدافند در جنوب تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/126196" target="_blank">📅 12:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126195">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
کان نیوز عبری: نیروی هوایی درحال انجام عملیات در ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/126195" target="_blank">📅 12:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126194">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در جنوب تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/126194" target="_blank">📅 12:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126193">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnPSR1KAkqJ3dwI2T-Ec3X7xoURvuPaLDZo_Dqw_smolWeJoys_fVSMWpLEcdlmCzOEjaRr7iN3A1s1HosaThpI6GJxbyIUUa87aGcHLcGYgN5VH8_dgbNQio86QFVSGcQw30DyeKak8D21jMoYmrH-Eb6lonVyJP9nfspZ_1x3xuYrX6a6Uulg8tmz6tnOjOxO5gzDjhVJ8peczYfwkczhKOGLKgG95YDeC5TwVEPl2IE7RHYR_eHtnbJY4jDCdepc6awit87Z2E-fmWOf66P4bRm0d67gtrm6IxGj71H2VKeoMq5qcBQDOfSLC2jvPcjpI0_zL-vuKBjMvJApspA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری از تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/126193" target="_blank">📅 12:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126192">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
دفتر نتانیاهو: به حملات موشکی ایران پاسخ دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/126192" target="_blank">📅 12:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126191">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
حمله به شهر ری هم اکنون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/126191" target="_blank">📅 12:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126190">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سخنگوی شهرداری تهران: با توجه به شرایط موجود در کشور، استفاده از مترو و اتوبوس در هماهنگی با شورای شهر تهران همچنان رایگان خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/126190" target="_blank">📅 12:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126189">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
پرتاب دوباره موشک بالستیک از یمن به اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/126189" target="_blank">📅 12:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126188">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpOoirYmIzo61ZHnFrZAJXqQG0b3djRYILW42LrLRH0urOi_bXsjXtDX194Cm3k09n3sESXb_kMxdDqDLC05oAqpGorbK6ymkERwDb7UA6gDsr7V3-f7bk2-hrpFfvPQpNT5J1lwRB2asWnufaf0m1R2d5xcTKxUYqlUzywUWxxNM1yjR8B6GcHxCTv25xEcJhZYoww6t7MZcbRYgcp-yktjQL9kOe9FgNHDKxRBVqHqdR4hwH8AGeKLaHD5OFp0l8A7KU3MAqQJXc2ecQ-JUBo5Eq7kT6YWsOAzYKllJe3mmuDaKsaHs-A6AB2OdywA9PoK-3On6A3GrQk7tyo-ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دقایقی قبل، تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/126188" target="_blank">📅 11:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126187">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
صدای انفجار در شمال کرج گزارش شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/126187" target="_blank">📅 11:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126186">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
صدای انفجار مهیب در غرب تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/126186" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126185">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل : دانشگاه هوافضای تهران هدف حمله قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/126185" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126184">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
منابع داخلی: تو تهران پهپاد زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/126184" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126183">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
دوستان از محل‌های نظامی و پایگاه‌های بسیج فاصله بگیرید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/126183" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126182">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
فعالیت پدافند در کرمانشاه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/126182" target="_blank">📅 11:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126181">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری / هشدار سفارت هند؛ فوراً ایران را ترک کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/126181" target="_blank">📅 11:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126180">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
فعالیت پدافند در شرق تهران ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/126180" target="_blank">📅 11:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126179">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbmUQaEBhfHbky7ra7mQZlYFwM3m9d99cbiy02fFbP8hpwMInPkzxpkKW_zshrfP6rgG5q3yY88M3bzezx_YQYS75t-Ab5niNJEuVD2ppsFiNV2gLJYdtAgdC_q-c18QhjLZXxDIoNW9EKBCuC-Hq7Pk45rwHRokHiT3hl5_ny_sgQIM6KihDCc_RaDLUH9lh_W53wSiUuF8-LojEETp8N4ubyXi3b1OYS1cD0zda1wUTU8tGlByWzmGOkF-uNQSwPdBlbLKSUmalaBB7jkY54W8IlHqVDDAGJ2s4JKO7k9gw6B4vIrRqlHco6c3TdJakK0vfX6wGSvbJQfSoZL8Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم‌اکنون شهر ری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/126179" target="_blank">📅 11:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126178">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
صدای انفجار در اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/126178" target="_blank">📅 11:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126177">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
معاون سیاسی استانداری همدان : ساعتی قبل نقطه‌ای در شهرستان کبودرآهنگ مورد حمله دشمن قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/126177" target="_blank">📅 11:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126176">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
صدای انفجار در غرب تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/126176" target="_blank">📅 11:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126175">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⭕️
الونیوز فقط در تلگرام
💬
و توییتر
❌
فعال هستش
🔴
سایر شبکه های اجتماعی چه داخلی چه خارجی که با نام الونیوز فعالیت می‌کنند مرتبط به ما نیست و پیشنهاد میکنم که لفت بدید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/126175" target="_blank">📅 11:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126174">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
یک منبع آگاه نظامی به فارس اعلام کرد، در صورت ادامهٔ حملات به زیرساخت‌های انرژی، کلیه تاسیسات نفت و گاز مرتبط اسرائیل، آمریکا و هم‌پیمانانشان از جمله تاسیسات انرژی منطقه‌ای هدف نیروهای مسلح ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/126174" target="_blank">📅 11:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126173">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
چین: دعوت از ایران و اسرائیل به پایبندی به آتش بس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/126173" target="_blank">📅 11:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126172">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1486cb80a0.mp4?token=AHVeKTyIYKLDfvVp7psdJw1mSU3D2ictpHlEKEq7f67Lm6uyeFwmmKeNbGvyVbcMw9plaTpmzIQ-sf-fiGE6LnvBDD_3Znw9rEv2feg0vYH6A_r9DAb1LGvvtBSUId0v__85tlozN28z_GOoZDz6PqLML6V5hApHezGzOaypv7bbJ0cNa-4edY_YjZLmGy9iPaDhBQqZ6arMF8FTJbdxu-JgAEavvKYVG8PbUKRGxLMGyBTV8ngjkJW8r4kkrh026fFNVk004FmwWmudf5Rp9jVhkwtPwiF2-eyFr-CCIE8RbALdl47ak2WhFqSb-E8oJm-we0MlwPxs3tn37G--xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1486cb80a0.mp4?token=AHVeKTyIYKLDfvVp7psdJw1mSU3D2ictpHlEKEq7f67Lm6uyeFwmmKeNbGvyVbcMw9plaTpmzIQ-sf-fiGE6LnvBDD_3Znw9rEv2feg0vYH6A_r9DAb1LGvvtBSUId0v__85tlozN28z_GOoZDz6PqLML6V5hApHezGzOaypv7bbJ0cNa-4edY_YjZLmGy9iPaDhBQqZ6arMF8FTJbdxu-JgAEavvKYVG8PbUKRGxLMGyBTV8ngjkJW8r4kkrh026fFNVk004FmwWmudf5Rp9jVhkwtPwiF2-eyFr-CCIE8RbALdl47ak2WhFqSb-E8oJm-we0MlwPxs3tn37G--xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت
خارجه
: حمله‌ِای به عربستان انجام ندادیم، اگه بزنیم میگیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/126172" target="_blank">📅 11:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126171">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8f71707a.mp4?token=kqzi7-gBmbvIJ56nSKcuvEMGPIQ-9SMwOUjzHHIEdAelONXbscdI5u3_SqQTRFG-YSc-9wlpF1NHYizUSv295tYjlGi5U-w8yOlkXOS-vA16ozfMyfrdHj_VlVsuErtBjUdCnkLhceXuim4IF14bHtnMroXqf4XX-iZ1srAoGWvX5iT-lHjI50_Z_c_iMQbWDo4__h4tScWn6QL9MkePKi2_cZgYMmkpQXL4vZJIhzBtcCZT90-W1mztjse1J6aNP5zuDfBc92XFWf12ME0OxEzh1jhiUPBtXrRDaux3pUnyFLjzruaYuepv1K19xfi8rKVIV6gF8qZVoY0pXETiXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8f71707a.mp4?token=kqzi7-gBmbvIJ56nSKcuvEMGPIQ-9SMwOUjzHHIEdAelONXbscdI5u3_SqQTRFG-YSc-9wlpF1NHYizUSv295tYjlGi5U-w8yOlkXOS-vA16ozfMyfrdHj_VlVsuErtBjUdCnkLhceXuim4IF14bHtnMroXqf4XX-iZ1srAoGWvX5iT-lHjI50_Z_c_iMQbWDo4__h4tScWn6QL9MkePKi2_cZgYMmkpQXL4vZJIhzBtcCZT90-W1mztjse1J6aNP5zuDfBc92XFWf12ME0OxEzh1jhiUPBtXrRDaux3pUnyFLjzruaYuepv1K19xfi8rKVIV6gF8qZVoY0pXETiXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی گرافیکی از نقاط مورد حمله قرار گرفته توسط نیروی هوایی اسرائیل از جمله ادعای هدف قرار دادن سامانه های پدافندی سوم خرداد (یا نمونه های مشابه) در اصفهان و خوزستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/126171" target="_blank">📅 11:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126170">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
عوستاد خوش چشم:  اسرائیل و آمریکا جرات حمله رو ندارن
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/126170" target="_blank">📅 11:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126169">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: تردید نکنید هماهنگی در همه سطوح به بهترین وجه وجود دارد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/126169" target="_blank">📅 11:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126168">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
حریم هوایی عراق برای ۷۲ ساعت بسته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/126168" target="_blank">📅 11:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126167">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5d255059.mp4?token=JN_ZLWWPdWvATVwduMrBzjGStR3FVhYQvXl_p4CtFIa0TdxqNgH27Ut3tUDqr1mPcnCX77-UMkMuyPbg3QEuDvQIGaE3Fjiem3K1JDjXs_nZeDjXn7T1uHOiNmBk1gb8tI41Zpy95IgLoI4e-2cIkA1Upi-ymK2p59Ji_UrlG9IMOnWoFfqIE23cCS8EYnkHrnH4ZdK4RrlGnlvqrmfpT1EP5Vg7vTHXRN8X-ScISNCa-GuCQDn6aWNI0FcGdzgGMrspo1V0mpa2yu1CqqIdje8Vw5RdPS0aqfBppvT61mJYHbtuwN63InO8lk6105bsMr_NhELAZqUP2HmD7Nj_q1OAdcLh_0LxgA6F9isQ0h2IIpUiu4mnI72JXLhXUKrmWKj__5YOIrSwgEHVk7gmQ58bpjbWjCfKRngIG2bPo8wmSKWDKr1uiEpV-ZMUcfXTQkDznYSI0fflARFn0LBx44hr8Gwse9CufdZ6LlXAh7FGaa8Mzm_IWjRvR-94udE84-IL1QowyKDS07p7mlrRIlOmLSp3zwwTQvsNT4UScf59mTBfUX_eAj0oC--qrYd0szVlq7e0zt01LPYIBwxUmCBi6xN4p_XVgF_RJmiPwKZ_zDVYjoFeeylbUOcmf3Qfp6IY-5iNgC-S4MzywdV8YJExUx9DJGVp9w0y3N5jtdM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5d255059.mp4?token=JN_ZLWWPdWvATVwduMrBzjGStR3FVhYQvXl_p4CtFIa0TdxqNgH27Ut3tUDqr1mPcnCX77-UMkMuyPbg3QEuDvQIGaE3Fjiem3K1JDjXs_nZeDjXn7T1uHOiNmBk1gb8tI41Zpy95IgLoI4e-2cIkA1Upi-ymK2p59Ji_UrlG9IMOnWoFfqIE23cCS8EYnkHrnH4ZdK4RrlGnlvqrmfpT1EP5Vg7vTHXRN8X-ScISNCa-GuCQDn6aWNI0FcGdzgGMrspo1V0mpa2yu1CqqIdje8Vw5RdPS0aqfBppvT61mJYHbtuwN63InO8lk6105bsMr_NhELAZqUP2HmD7Nj_q1OAdcLh_0LxgA6F9isQ0h2IIpUiu4mnI72JXLhXUKrmWKj__5YOIrSwgEHVk7gmQ58bpjbWjCfKRngIG2bPo8wmSKWDKr1uiEpV-ZMUcfXTQkDznYSI0fflARFn0LBx44hr8Gwse9CufdZ6LlXAh7FGaa8Mzm_IWjRvR-94udE84-IL1QowyKDS07p7mlrRIlOmLSp3zwwTQvsNT4UScf59mTBfUX_eAj0oC--qrYd0szVlq7e0zt01LPYIBwxUmCBi6xN4p_XVgF_RJmiPwKZ_zDVYjoFeeylbUOcmf3Qfp6IY-5iNgC-S4MzywdV8YJExUx9DJGVp9w0y3N5jtdM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: ادعای مصادره دارایی‌های مسدود شده ایران به نفع کشورهای منطقه مضحک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/126167" target="_blank">📅 11:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126166">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: تردید نکنید هماهنگی در همه سطوح به بهترین وجه وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/126166" target="_blank">📅 11:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126165">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
تقریباً ۳۱ موشک از دیشب به سمت اسرائیل شلیک شده است، ۳۰ موشک از ایران و یک موشک از یمن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/126165" target="_blank">📅 11:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126164">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM5dSv--GVLxtDlV5EmkhqIczHraG7ES2onRZt0hFCJBNWlf2tIfyOV22ywAAOOWOzDXOjgAOClDlvSZrNBLVjqOL51j9LE9Ha8-aqqiClIFGCiByRe38054saiND2AZoyfwMLMRK-KoQc6jJvbOJd8VxQFZT8K_YkhRb6CuAfdMhZunroDmXGUuZRsCpzgBy7tVdaAMPr_7dVpoL6okelfgqR2mq9Rjy953DVzXSKMW-mkXch3AzgQY_JO__r2mllv-J0Ey26c_P5klJv1O3OfE00QXvYvAjpiRC_fF4nm97CeO-hGyfNk_BaROYlncnXoTTF0qj5Et6ecnYZ8olw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اصابت دقیق موشک در حیفا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/126164" target="_blank">📅 11:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126163">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سپاه :  اسرائیل با هدف قرار دادن صنعت نفت و مراکز غیرنظامی ایران، وارد یک «بازی خطرناک» شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/126163" target="_blank">📅 11:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126162">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه ایران: هیچ کس باور ندارد که آمریکا بتواند بدون هماهنگی کامل با آمریکا در منطقه اقدام کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/126162" target="_blank">📅 11:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126161">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
کانال 12 اسرائیل: انتظار می‌رود وزیر دارایی اسرائیل، سموتریچ، استدلال کند که اسرائیل باید به جای حمله مستقیم به ایران، در لبنان در پاسخ به هر حمله ایرانی واکنش نشان دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/126161" target="_blank">📅 11:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126160">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89e8f3ab93.mp4?token=BATL3vb8_aM2QxP7FzNAU_BUnaPSJnF7sm6fiCaiDhgs-ZjwIFg0sfFajgf6lD-E91W3INGxv41yC6Dz-2GzsppHqX4_t6ZYs8YTxLHFiff-1EGpA4lUCm60v6VFsxupNBom_AhEX9_1O_QxRoxev55VtOazb3ubbb8Pvrf9hXQ2-CNhHqWaUHbzUXk-KLqqRHQv36_IRCXwlx7kiO5vilnh8b1nq0uO2KMjtKgI7RyHEHrUCbqBa2vPutm3dLcFHATAoIz6VSEd6ObS8T7MeMcXPdNtQFlvjhOXMWftO_Mt1tC4qoG4eiSBnpuk6vs1z9MeEAJxmBXyggflHCTZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89e8f3ab93.mp4?token=BATL3vb8_aM2QxP7FzNAU_BUnaPSJnF7sm6fiCaiDhgs-ZjwIFg0sfFajgf6lD-E91W3INGxv41yC6Dz-2GzsppHqX4_t6ZYs8YTxLHFiff-1EGpA4lUCm60v6VFsxupNBom_AhEX9_1O_QxRoxev55VtOazb3ubbb8Pvrf9hXQ2-CNhHqWaUHbzUXk-KLqqRHQv36_IRCXwlx7kiO5vilnh8b1nq0uO2KMjtKgI7RyHEHrUCbqBa2vPutm3dLcFHATAoIz6VSEd6ObS8T7MeMcXPdNtQFlvjhOXMWftO_Mt1tC4qoG4eiSBnpuk6vs1z9MeEAJxmBXyggflHCTZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/126160" target="_blank">📅 11:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126159">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taK1PObKka1bB1Pm8lB0UaI0sqR1q72g3wKPEpDfSHSmhLLmZYtBH_ulwOzKIw0Vo6xvDPc5Immh_iozbt9bjPZFFbqiSOUEgcvdVb3V-qemv-8XoSbV0o7AL6Q3tyHu-JxIZ-5RV2SVMgRgVkFaJTA-SFyNuEOsa30jqCs4_sPVB1r0t8XwiTjVHtbmo_eIvAj6oo6h0j36avdV-48YT31LP_JgpDLmSKmbS4Ynp90FB65yLQzX2aN6FZJ1o_bIT04KJP9VF6DyOj6HbIZ6cE-F3f5zOZGtWfPQ8EDJAeDdEp3k_z25nIhqDDEbWc9mFUol_RtOUvS_SgZUyD1LeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
این اینترنت بی صاحاب رو چرا نمیبندید؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/126159" target="_blank">📅 11:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126158">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
مسئول سیاست خارجی اتحادیه اروپا امروز از اعمال تحریم‌های بیشتر بر ایران به بهانه بسته‌بودن تنگه هرمز خبر داد.
🔴
کالاس در گفتگو با خبرنگاران پیش از ورود به نشست غیررسمی وزیران دفاع کشورهای عضو اتحادیه اروپا در قبرس، گفت: «امروز اولین باری خواهد بود که تحریم‌های مربوط به آزادی ناوبری علیه ایران اعمال می‌شود».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/126158" target="_blank">📅 11:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126157">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: آتش‌بس به‌طور مستمر و مکرر توسط طرف‌های مقابل نقض شده است.
🔴
ما هر وقت لازم بدانیم برای دفاع از امنیت کشور اقدام خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/126157" target="_blank">📅 11:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126156">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزارت امورخارجه ایران: ایالات متحده مسئولیت مستقیم نقض آتش‌بس کنونی را بر عهده دارد و اقدامات اسرائیل را به واشنگتن مرتبط می‌داند.
🔴
اقدامات اسرائیل در منطقه را نمی‌توان جدا از ایالات متحده بررسی کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/126156" target="_blank">📅 10:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126155">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c18b980c12.mp4?token=uIgAi7tsPBB41LDhy9NAmlzyslmHfSTPHwNAoUMh85ngLJQdXFrefTmV0ArYydE6FvITRCg7H8yWUnmOfhSXrQIK8K0HUdSAwxF_IAQnmJ-9pewskTy-ijhY26gj5DSfjEilK5eaUVIQy4fyjsssBALGMz2v1bxm6bDn-AuyCghUBQdNW1g5WOzW5qug7SOtGRgbM6bxUllzU0k9jSMICM6-pbLoptKuPvf3oKB23WIkYfzDg1O9VfCOF4IbBFV3mu7T1iLQOAWBWfUNPomBNA1Ttw7OC_SITiX6QXkQU7zh_WlC6_scJOmRhsG0L96rnIUBd4AsRBSJM67ZPIjH_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c18b980c12.mp4?token=uIgAi7tsPBB41LDhy9NAmlzyslmHfSTPHwNAoUMh85ngLJQdXFrefTmV0ArYydE6FvITRCg7H8yWUnmOfhSXrQIK8K0HUdSAwxF_IAQnmJ-9pewskTy-ijhY26gj5DSfjEilK5eaUVIQy4fyjsssBALGMz2v1bxm6bDn-AuyCghUBQdNW1g5WOzW5qug7SOtGRgbM6bxUllzU0k9jSMICM6-pbLoptKuPvf3oKB23WIkYfzDg1O9VfCOF4IbBFV3mu7T1iLQOAWBWfUNPomBNA1Ttw7OC_SITiX6QXkQU7zh_WlC6_scJOmRhsG0L96rnIUBd4AsRBSJM67ZPIjH_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت کانفیگ فروشا
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/126155" target="_blank">📅 10:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126154">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">💢
فوووووووری/موج بعدی حملات اسرائیل آغاز شد
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/126154" target="_blank">📅 10:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126153">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0VTuHsZexWLEMzzRcGXbN2iMGkWoR5g_iOgLSKMGl-Q-PIg3Z71ew64QzJFckHhnnFQlj9mSbvyOLUgwd4JeiExUpwrNMbDnms0DoBgYraGC0dbb2GDB9OKgS5QveoZ5VstzW2Ix9TxrG1igaKduQ1ry-ndChPM6qtO8zS9c6We9VBAPbe2Qga-oGpa-xrCN5eKegHWgWmBL8mLhVxu9a_RRuoFVmGN9OvUGolQzFehg5Lbi07gJ4YNjFk3ebEUZTymHwv-8GX0wufehpmZQ5rsTeeNeEZ_iVKpIRjsLfxdTgVv4ZowS-MrOT6CsL_e1Aa7Vwgy9XZGrpfORLFBPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس: نباید دچار خطای محاسباتی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/126153" target="_blank">📅 10:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126152">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
بقائی سخنگوی وزارت امور خارجه: مسئولیت هر اتفاقی که در منطقه ما میفتد چه آمریکا عامل باشد چه نه، با خود آمریکاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/126152" target="_blank">📅 10:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126151">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
برخی منابع از شنیده شدن انفجارهای قوی در پایگاه هوایی ریاض پایتخت عربستان خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/126151" target="_blank">📅 10:45 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
