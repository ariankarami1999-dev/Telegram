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
<img src="https://cdn4.telesco.pe/file/JkcmrJKE4WdavYJdmHBxrv6Bp0Ih1wPm_zhMBBiRFxmXFdPqKrI9Hs0LCRTbuq8jmWGp22wmfaoB3QSUCokxRQ07kOUj-ewfSbbRmZsDtXP6cX3ZPndaEVi3mPtQ2XCPq5AXkNs7uewLNks24EURkn-RKCAmVHsbaxrkp52rAQqFyZeyI-WXCASKY5_pR8nTMfK86EAWJM6ROudzAKsJbDONWA8CVQ_N0GEF_S4x-iMUEzMSgfjhBT0FO7rsKRfYXtcxYqh9CCHPAw2i9cax9DT-HpWaLWevug27rAtM_IeKlzX042F87o2dKfrZlkTmbsm1GEl7YxRJKGEpGif-rw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 197K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 11:29:05</div>
<hr>

<div class="tg-post" id="msg-67412">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIA5PEyeosPnqgWlH5qmCrtBek7hBza7JBiTAu4_GyrZwrBXTUaSKOfmJUiBeeHXBW6Mca9trsyQL4uSSHUEsI8bxSU2oEgIT6MVf1ceBJwmiXrds0844OfRqLH9ee67hGmUtsq9vIhJWPWEYHkYOls4ZAHD_u2iAptwaQFuQKSDlqtriyE3CskKEq92-ot68rQfbJnacXD7RUmrlCNntpNr92Wq4zeWrFXTT4VXa7cN6ah0byNsiTzW7WQR_0iYI6QfMVcDMlINUF6BocIm3x8oqhRtYhBoVHht6r1dwmI-gCV1G-Xpa6SgeMl-h21kt9O9jB7EdzCv6X-tiZPKUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس:
دو مقام آمریکایی به «اکسیوس» گفتند که ارتش ایران دوشنبه‌شب دست‌کم دو موشک به سمت کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده است و دو کشتی مورد اصابت قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/news_hut/67412" target="_blank">📅 11:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67411">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
احتمالاً نباید این را فاش کنم، اما ما دو تا از بهترین نیروهایمان را برای محافظت از قاآنی در مراسم خاکسپاری فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/news_hut/67411" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67410">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64666ae825.mp4?token=InoN07M2isUWRtnChPAxmn_FaS2se88-MnBwMqg2x9gSDgxksSuSymrt4SQMkNK4plajGqwkhg3wzS7ku4yNBwO-uqwNgY9Ms4i0yuQ1Rw1nhMDk1Yfn6oKB_Jh7vT6xqQVvzaLShVLCPaqaG2XmAkW3ULZ5bk0vU2w83bTUgjmaDpYhyN5QGU83QiZnUi1PORmFNzE0P11JKoJUtrSC5fHMC8d85fXfczures1k-hRvtrq6ZDjfBAoJUYxDl-bTajCI0Ow_pNiwP4upztD6Jmi9wtpABWT3Rc5Fjg73zMZy61zLlFsR2lMjjqhodB78xEyVuhqlQyT8nvYhZgWUYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64666ae825.mp4?token=InoN07M2isUWRtnChPAxmn_FaS2se88-MnBwMqg2x9gSDgxksSuSymrt4SQMkNK4plajGqwkhg3wzS7ku4yNBwO-uqwNgY9Ms4i0yuQ1Rw1nhMDk1Yfn6oKB_Jh7vT6xqQVvzaLShVLCPaqaG2XmAkW3ULZ5bk0vU2w83bTUgjmaDpYhyN5QGU83QiZnUi1PORmFNzE0P11JKoJUtrSC5fHMC8d85fXfczures1k-hRvtrq6ZDjfBAoJUYxDl-bTajCI0Ow_pNiwP4upztD6Jmi9wtpABWT3Rc5Fjg73zMZy61zLlFsR2lMjjqhodB78xEyVuhqlQyT8nvYhZgWUYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته میشه این شعارها علیه عباس عراقچی توسط تندرو ها داده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/news_hut/67410" target="_blank">📅 10:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67409">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=J1uE3oupNr9E0v4jfY_casFy3B9zoCrjxbV6gSFOmNuCtT8c4kgvlbAWTMrTpTbr4amGYz8H0ih12U4gyEGyQ8gQpv5vhv7CC9pwoiS7688E77IrTgZsWF8MjE0n-PH4rQtftEF7YEOp9bdD-C4dmi6P7C2O0cdv6hn2OHg7HeiFMv5zQsEFg0RmiSgLneEXcMbUbQAz5r2UbI2oliTrwXtsvOyhG4_JBUaOJ0WnRu5mf8SPXJku-4bDUi_iWn3IMEzy3jl_LmP8_rkdZwWXgDcCsHt55bjtEwLzGW5NyUO3oyMlrgwc0A3tQ1fgU6aBYE5kinrDttyJ21aio6-yTiMJaINge3LIK7J5R97eOPcXrxscUc1HlVWYYDFPYDlOqNGxiu_ndic6X4h1b3ycEtN0cie_1XqL-4Ssp4KxUZlX1iDRAlQiTCyvFJ3i9-0R0kzkKG4nj4iAo9xXhLV6YUUbUm8zXesRa2Z384b6swuprWlM8dmdaQ8sqd_mh1O70gS0epLqhSdoSxlroZqFLAVmhA6fyg7B3XvSM0NGUf4EcbyIEu1h-pfKUU1fm7GgpsTZUwhpZZayulbl_ZkuB3kl3O72L0yz76lHkGlittYJNH4pUazo_2RdHXO4rR1mGru19XEVn5CPWN8FY2MS6ifaB8WbnIm3DlpVzkbqE1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=J1uE3oupNr9E0v4jfY_casFy3B9zoCrjxbV6gSFOmNuCtT8c4kgvlbAWTMrTpTbr4amGYz8H0ih12U4gyEGyQ8gQpv5vhv7CC9pwoiS7688E77IrTgZsWF8MjE0n-PH4rQtftEF7YEOp9bdD-C4dmi6P7C2O0cdv6hn2OHg7HeiFMv5zQsEFg0RmiSgLneEXcMbUbQAz5r2UbI2oliTrwXtsvOyhG4_JBUaOJ0WnRu5mf8SPXJku-4bDUi_iWn3IMEzy3jl_LmP8_rkdZwWXgDcCsHt55bjtEwLzGW5NyUO3oyMlrgwc0A3tQ1fgU6aBYE5kinrDttyJ21aio6-yTiMJaINge3LIK7J5R97eOPcXrxscUc1HlVWYYDFPYDlOqNGxiu_ndic6X4h1b3ycEtN0cie_1XqL-4Ssp4KxUZlX1iDRAlQiTCyvFJ3i9-0R0kzkKG4nj4iAo9xXhLV6YUUbUm8zXesRa2Z384b6swuprWlM8dmdaQ8sqd_mh1O70gS0epLqhSdoSxlroZqFLAVmhA6fyg7B3XvSM0NGUf4EcbyIEu1h-pfKUU1fm7GgpsTZUwhpZZayulbl_ZkuB3kl3O72L0yz76lHkGlittYJNH4pUazo_2RdHXO4rR1mGru19XEVn5CPWN8FY2MS6ifaB8WbnIm3DlpVzkbqE1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، کارشناس مسائل فوق استراتژیک:
باید هزینه بالایی برای خون خواهی امام شهید ایجاد کنیم. کانال ۱۴ اسرائیل می‌گوید رهبرشان را شهید کردیم و هزینه‌اش فقط ۴۰ روز جنگ بود و دوباره می‌توانیم این کار را کنیم. این بار آقا مجتبی توانستند جایگزین پدر شوند، اگر باز رهبر ما را شهید کنند چه کار کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/news_hut/67409" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67408">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=qF05nh8tcTnLZwYpjmWt_twS5nYNN5d8Is59v0wffqp7vA9OkadxxSo-5-_dFBhSdX3QFEVo-EV4oVjSivyYB2Hl7Sa03m7sniiQq9rItnZuw51NezcOieTQz2z3vB_O16p2_GqevFL4O1KmbMYJ24IfJrXWWT9Gwz86OsdxCJjaOYUJvHqc6KdBcY5D4Tjocce2fRgRDNz8NNto1HEVhugehwJ1fM3AUU9DtEmkISGUrwgGr8gnGeC2_j0JZBSIHXJxmqFRzp3XdCc4_fBy29jWe0t7rLVxHo52GrTfNLOovtVobPDZIu61jBMDyNH68k0NhTd0QEnbkpL3aH31Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=qF05nh8tcTnLZwYpjmWt_twS5nYNN5d8Is59v0wffqp7vA9OkadxxSo-5-_dFBhSdX3QFEVo-EV4oVjSivyYB2Hl7Sa03m7sniiQq9rItnZuw51NezcOieTQz2z3vB_O16p2_GqevFL4O1KmbMYJ24IfJrXWWT9Gwz86OsdxCJjaOYUJvHqc6KdBcY5D4Tjocce2fRgRDNz8NNto1HEVhugehwJ1fM3AUU9DtEmkISGUrwgGr8gnGeC2_j0JZBSIHXJxmqFRzp3XdCc4_fBy29jWe0t7rLVxHo52GrTfNLOovtVobPDZIu61jBMDyNH68k0NhTd0QEnbkpL3aH31Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش جالب یک مازندرانی به حضور سعید جلیلی در مراسم تشییع علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/67408" target="_blank">📅 09:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67407">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcgPScQ9Kw0-gIVNE0tm2LQs_1-3T2ZSsW5JvC3lBLcvPUTnyI8EY-8LJ1Mbtqaq7UuW-yl74brixxvknrqxvdUPSa3-VnsdsBmiiDMDiDZliSOaVPubSkt1ixBfOQnqqcm1GwlaA3BeIveiVZM0uiDoo8DP9hqT75sRoy8ruMLxw6WxDbhazdZTCcNT4WxndWpHwgT2omrsdWaBpu2jqdwDGwydKyNdgEOZuZjeDF14NHQvzALVgpPSMppdKfTwVMiWFeR_7bxP4RBQsLGq5aEq6-WfX5ORbY8YM3G3LDMzWeF9wEDp8pkCqsZc1E4kETav_AXGAB-8mpQZWULBxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
مرکز عملیات تجاری دریایی بریتانیا:
یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
بنا بر اعلام UKMTO، این حمله باعث آتش‌سوزی در سمت چپ کشتی (port side) شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/67407" target="_blank">📅 09:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67406">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67406" target="_blank">📅 03:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67404">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cBtE8Oq7qdCNA_z8-N74SdgSUpYRZaWHJ9U89xZhuS2Qn-J8KLKKiF6sXB387TtRi9no_g-rLioy5yHRlgEWd3jeQPEDL0jgYW5CqF4sgP82OFkTPVRhM826m-KAZmbIRW2ZKoI2Tc-rcsy5CAkGehLi8aMiiRN5vSAg3dmKxwlHLzmcifLHoLIzslUVGMSmwBqV7QFJ-onD_tFvfUtyTl8b9N5ZVp6vaYuVX8dy9h-paasujLfrclUyzCpahmz2EwlHti9zntRha2ATLMACUcm414eiP_iyvwpd4lwNprss1Bwsc7Afh-EOE1kdxYz1_6-dh87x8fllmc75hkcfFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67404" target="_blank">📅 01:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67403">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmeGBYTX-1t_vob9flAPg1dBIEIxR5Wncg1UU5XfqBgXKr6CE9Y4NpCX88a0aKpIdf_52PO45-w1uPTkw5VxuilUXpwyDy72Tjg_1ZuOYbqE-XRv6M9iwjBekDa3U3exwdCfYyqsjz21yPcV6DkQJQmohrkF51N0_xmhzGyV_KyEBWc7jPX7YxUoOVDw7uQznYlZtyWBUWOWddt16JulzHVVdWLL62B7NU60LVFjNeZnhkrp4tu86KjeX7PccXP-R7fNlOw7AzqaxpO3oKQ6mrlhzKSrBW6MTwQM6SIDU7aZoLdyd40fVbrJ2RXOE8h98Ros2uHiMUtdP8-6OouSLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026
| حذف کریستیانو رونالدو و یاران با شکست مقابل اسپانیا در دقایق پایانی
💔
🇵🇹
پرتغال 0-1 اسپانیا
🇪🇸
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67403" target="_blank">📅 00:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67402">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9EPOMo_EwGK5TWXy-w27uzWFe30iPPNfNcZmXyKj7oWeXNgMaTfH1i2faLYmketlENwqqYYsPzpFfQOrutPzZhxTnWwRnU8zNeDWyZl1Vk7mTbeivjxelxmytsZFjAxZhzLNwXQX0VK9PZ3VX_4F35GuJdCDHcc5ePoJDBeUreNNqM5BWLgPpxiMNMANnZMNy02pxlAic90AgYlMo946Sol-qHfOWcbo98VlDkiv-hMBg9IlRzd7ZG4CO43BhcK4bWIatHeDUq_4FET2l94bDF9aBvZ1c8QqrEtlnNKMX9lQFEMsGrGs-j-txxdIQ5R4QOLOD3LrXdTHWA1f9fH8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ادعای کانال 14 اسرائیل:مجتبی خامنه‌ای در مراسم پدرش حاضر بوده.
🔴
حضور مجتبی در مراسم تشییع تأیید شد
🔴
مأموران اطلاعاتی خارجی، مجتبی خامنه‌ای را در جریان مراسم تشییع امروز در نزدیکی میدان آزادی شناسایی کردند.
🔴
گزارش‌ها حاکی از آن است که وی با پنهان شدن در میان گروهی از دانش‌آموزانِ حاضر در جمعیت، تلاش کرد از ردیابی بیومتریک بگریزد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67402" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67401">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=gv7vtphSTaY52hmHj5eFLxwd5MwEwdaBvoiq38fxkdmzB4LG5URQpHGo4x5qJH-butoo_MTM30QwyaFNryf55-2H7Ifi6XPxtc5-_WyPtTFIuajXIrNpc1YCxQthYiugBTmNxtrbw7xdeXfjgACJAiZH5BF3lH2Ef5oWIr6qPySaZhS40T-z8jOLBcQMK9qN_TAXSz8cFCp8xtYwBDSUpZCvH8nTJahvAfXnR8jSVaDju3Z6YW1tIxOG-KCZLiD6gdlbrD8xLE1o9ixaWKlxomRUUWFk9Ovm1siHGXdVY8VF80AxqlbEGwQsLeB4huSBplORKDqN_UGBD5YMco8Tjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=gv7vtphSTaY52hmHj5eFLxwd5MwEwdaBvoiq38fxkdmzB4LG5URQpHGo4x5qJH-butoo_MTM30QwyaFNryf55-2H7Ifi6XPxtc5-_WyPtTFIuajXIrNpc1YCxQthYiugBTmNxtrbw7xdeXfjgACJAiZH5BF3lH2Ef5oWIr6qPySaZhS40T-z8jOLBcQMK9qN_TAXSz8cFCp8xtYwBDSUpZCvH8nTJahvAfXnR8jSVaDju3Z6YW1tIxOG-KCZLiD6gdlbrD8xLE1o9ixaWKlxomRUUWFk9Ovm1siHGXdVY8VF80AxqlbEGwQsLeB4huSBplORKDqN_UGBD5YMco8Tjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارها برعلیه پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67401" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67400">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتلوبیون اسپرت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT0SrnmGJJrvFyDQk04ksgojZ-BWkm1irBlfzd3gzz5vbtOPkpxo8i6ZeZ0dHaQSpxJILhTl4KpEtMdY-ftcpL6c1YtAOslnx_7UEvWKhYokxiXitCmkpPeVRxFSCJ0M8MB3XCRNZBx2KRInKtgDxgifVRBtN193l6abmgSACLxIODzUuaSNqTr9iCrkh7EgHETQzfEe9Ap2-EKTK1j-sfRw3rngsB_syO2JUd-gopaXjMqaVXELLYOnv31xjgT7DVynTNcTjDiaH9gF5-W-GpfvoCaiW85tAdso59mtFP71ELXze7nWFnw21QSN6sJJmPtNnvj2T7TIS-WHMhfQRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
اسپانیا یا پرتغال؟ انتخاب با توئه؛ تا از رقیب عقب نیافتادی از تیمت حمایت کن و پلی‌استیشن ببر!
🏆
👇
👇
👇
👇
🔗
همین حالا حمایتت رو از رونالدو یا یامال در لینک زیر اعلام کن و با بازی کردن پلی استیشن برنده شو!
👉
Https://tcup26.com
👉
Https://tcup26.com
📢
این پیام رو برای دوستات بفرست و به این چالش بزرگ دعوتشون کن!
🤩
@telewebionsport</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67400" target="_blank">📅 00:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67399">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733e727650.mp4?token=crH_ZBmmMjbHk6ZeCPhCAVAj0P3giHM01Y2jQnF6xWYi8CDvBhFBYBDgR-bOuEUTsg0u2Al9JEkweu58QD-mUsN2xjOB6gHoneZfrMzySJcUYgT-UWWx8YWNsceNBdk-MfHpMum003qDqaxhso9vahPkISSmdEzz99bk736ect0cCpPsSW-uCZjLNlrfOESbkbrVL7KHhz9eG-NJGOup7my2J0ppm9SMI94ry2oe8pYZaUqAkmF1VWvJbUbJXNJPq1EpZ7adXY17ID4mdNneA68JdFGnep0IM_GVJTF9P2JGbAS2mv2cY_FhSK-IR6-elSmy7zHKF4eqbCUi_EvXEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733e727650.mp4?token=crH_ZBmmMjbHk6ZeCPhCAVAj0P3giHM01Y2jQnF6xWYi8CDvBhFBYBDgR-bOuEUTsg0u2Al9JEkweu58QD-mUsN2xjOB6gHoneZfrMzySJcUYgT-UWWx8YWNsceNBdk-MfHpMum003qDqaxhso9vahPkISSmdEzz99bk736ect0cCpPsSW-uCZjLNlrfOESbkbrVL7KHhz9eG-NJGOup7my2J0ppm9SMI94ry2oe8pYZaUqAkmF1VWvJbUbJXNJPq1EpZ7adXY17ID4mdNneA68JdFGnep0IM_GVJTF9P2JGbAS2mv2cY_FhSK-IR6-elSmy7zHKF4eqbCUi_EvXEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
عجیب‌ترین چیزی که امروز میتونید ببینید:
نیسانی که با یک چرخ جلو بدون مشکل داره حرکت می‌کنه و سگی که داره راننده رو قانع می‌کنه تا دست از رفتار‌های کصخلانه خودش برداره
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67399" target="_blank">📅 23:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67398">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad6611348.mp4?token=Jdgotm308lj4ID9_cegzyhOhu0DVrefvROUXOI9edm2mZeN4QRcsTp6CiZKoM5Nt6uVL-hRw6Eu55yfXYgCziBQMWhhcTq8oDHkD30ELYEhpb2UEW5NdfiJqviZq921Hx6zGsfrdbF-4j4wtSzZDLw5wv-staOz3tNR5hKhfDQTsP67Euq-u2Xh94GFp7DbzSBs-vhIRPksAecCzscq8qk_jYyL1X2WXwKw-XsrRnJmmoElYgidR2bClIllCI5uAjAdfphmI7p3DqZX1iVK2m2DuVKNeGhEGh5zjRlTxhStwrKO_0UH5bZgrjUV7q9AXtro0X_RS8_xk2qdcpKIGJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad6611348.mp4?token=Jdgotm308lj4ID9_cegzyhOhu0DVrefvROUXOI9edm2mZeN4QRcsTp6CiZKoM5Nt6uVL-hRw6Eu55yfXYgCziBQMWhhcTq8oDHkD30ELYEhpb2UEW5NdfiJqviZq921Hx6zGsfrdbF-4j4wtSzZDLw5wv-staOz3tNR5hKhfDQTsP67Euq-u2Xh94GFp7DbzSBs-vhIRPksAecCzscq8qk_jYyL1X2WXwKw-XsrRnJmmoElYgidR2bClIllCI5uAjAdfphmI7p3DqZX1iVK2m2DuVKNeGhEGh5zjRlTxhStwrKO_0UH5bZgrjUV7q9AXtro0X_RS8_xk2qdcpKIGJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فحاشی وحید خزایی به خامنه ای
رادان کلاهتو بزار بالاتر!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67398" target="_blank">📅 22:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67395">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSY-X2EF8UTgN2_qkAK5hkqTY1VT82FDalU-AxPj5CKPQ95ZqDw85BKrx_brpZgfr7s0moL3kzDKI-ZNYcXloSdit3RvOnin_epxTEhWeJUiTPf2rjXk0OTqcTRNunEAQts2ubQHGiz3DKYPG1qQPMzVaJhECCX4NwKCAX17hY4Mh1Dh7bygAnBJjeR-hQ_u09wBz0UdIZW3HLCrQkoZm3-feJxMRodpePw6pBbV2zwzTy5EN7SQ9yc36JWZMhx_e0bOlt0HkJk8PFKIixa7fvoG6y8smoCCVmhyp0qzCk4ANEntk01TgOqK-6IbLeorO8uBChJEIENZSC-fQSz8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DkvG6CuaqMHkUuzoApGzAhyZe0ehRo-rJRT4lu59bjh-7IOG5aK2LzRlo0GZp0dWLwFtzEjNR7Oh4DHZ5v2ga8gJeY3GmusHjdbut81O6UfJGUlXOfR6Rb4gkAcHLcMxK06mzh3RjQYbDkrDWZfE_5z5ZQtx9VmZ4TcCRVBwYi9I8lp-BY1CZNO2mVlvtGYETtlh6hsoxebZ5X64D8p0cF74HIR0qSx71qImMQUlvndPbyLl9fkP7ixn2K2LLBKBT7NvShX-UXw1SGUVHtV5eGjy4XKSWqiKNiW_W2pAzJ-l-j-2vXtiGrkmnNP5xtj1fOopbD3Rbhs4lvZ-9LawUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=HKYqC08KFpd6BiaF__GgTOZ8KbQR-6QVOB-7d11QJZjZVTowNYHFP9TP5jDsiobF_z-3_cT0RgFnlYB64dOaGqrTU2JzcDx1sAE9-iPcJuyBuEDjO653HMstyvji3Yv6VUjeCKVeb-Xphs4n44V4oNeogq6uojSe0QjR1kmsP0RaiJBRh1fKtLgWeGlRXonHdC1HyKpKur-81JgucINBxAIsXZSh5dPUAKmaYn83bpmFj-1TsoEyuFNXGkmiEjg4x8n6cIAyYKMtLw2zkulTUqFoWP_5vCx03KWHFgxAluTJYmtiNK21pBEjravXDTzp4ia9v_sk5bJlxvoGzRHmcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=HKYqC08KFpd6BiaF__GgTOZ8KbQR-6QVOB-7d11QJZjZVTowNYHFP9TP5jDsiobF_z-3_cT0RgFnlYB64dOaGqrTU2JzcDx1sAE9-iPcJuyBuEDjO653HMstyvji3Yv6VUjeCKVeb-Xphs4n44V4oNeogq6uojSe0QjR1kmsP0RaiJBRh1fKtLgWeGlRXonHdC1HyKpKur-81JgucINBxAIsXZSh5dPUAKmaYn83bpmFj-1TsoEyuFNXGkmiEjg4x8n6cIAyYKMtLw2zkulTUqFoWP_5vCx03KWHFgxAluTJYmtiNK21pBEjravXDTzp4ia9v_sk5bJlxvoGzRHmcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلم اول تصویر کوچکی از جمعیت یک میلیون و هفتصدهزار حجاج است که امسال برای حج به مکه رفته بودند
مقایسه کنید با:
🔴
فیلم دوم جمعیتی که روز شنبه ۱۳ تیرماه، با وجود واردات عوامل جیره‌خور نظام از ده‌ها کشور در مصلی جمع کرده‌اند
آن هم در تهران با جمعیت ۱۵ میلیون نفری!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67395" target="_blank">📅 21:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67394">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=cp1KQvesViQCLMXLLWAcoxleH0MWuYBIhp_3_gmWSUi5r_drGhdcWBjV0Q-qE-xNXwqNqJzC_DJKPhCW3BwAhtXBCFaTB1pygSjJWzOltnM8VnF-jcVERT6YZ1SIcJvv5kbcOOWDZceBlwQW98bocFL2o22hPmD9MmbkhJByS9lS0kIESOa8jqktmOWXjPx-pMMwQ4W4ZiiHVQxHJ3Ey4-K1mOlOPvqJbTXeNJopdOX3zyNBGxIlRlypHCgaVS40wumSJS2L-ykUJG5EGAyZSaG0OjpVnpAu1SMBXtXo2vvEblpL6vPBPMzJpixA324usA-3NFMCzRervjsSR0rcxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=cp1KQvesViQCLMXLLWAcoxleH0MWuYBIhp_3_gmWSUi5r_drGhdcWBjV0Q-qE-xNXwqNqJzC_DJKPhCW3BwAhtXBCFaTB1pygSjJWzOltnM8VnF-jcVERT6YZ1SIcJvv5kbcOOWDZceBlwQW98bocFL2o22hPmD9MmbkhJByS9lS0kIESOa8jqktmOWXjPx-pMMwQ4W4ZiiHVQxHJ3Ey4-K1mOlOPvqJbTXeNJopdOX3zyNBGxIlRlypHCgaVS40wumSJS2L-ykUJG5EGAyZSaG0OjpVnpAu1SMBXtXo2vvEblpL6vPBPMzJpixA324usA-3NFMCzRervjsSR0rcxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره مقامات تهران:
ما بسیار خوب پیش می‌رویم.
می‌شنوم آنها میگویند که«بسیار خوب پیش می‌روند.» آن‌ها اصلاً خوب پیش نمی‌روند.
آن‌ها آن‌قدر شدیداً می‌خواهند که یک توافق انجام دهند. آن‌ها باید توافق درست را انجام دهند.
آن‌ها با بسیاری از چیزهایی که بسیاری از افراد گفتند با آن‌ها توافق نخواهند کرد، توافق کرده‌اند.
ما به یک روش یا روش دیگر پیروز می‌شویم: روش مهربانانه یا روش غیرمهربانانه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67394" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67393">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=pzxj6cPgT2GTuQiy-cF7gTrZqFwcgf_JpaaQ1QyU5KvDSPFxHj_PhIGgrxTGU8GcZSBlfop3Xi9EyI21AxfSWXbZWmJBJCPg197pzl2443l5Oy6rGG8Lbv5-VCMpMTZTBVx69QJ09G0kymKneY1_ZcqZ0bnDKl_QzhbbgEaS6sAAqsBQ_b50cm6GnowNAQLKmtxWG_tycmktLnivQZlIVhEDZ54bgE_xdJiOmQ37-63-0JF2KmlAHzmGxo1Qi_hPeFTK_ubwexKm0GfeeHZ5eyExgGBmmw0wmW1Snorh1SgVmaeQnRPRZa8G_5ofBVPxGZLE0nXfGzf8WlNucyNWbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=pzxj6cPgT2GTuQiy-cF7gTrZqFwcgf_JpaaQ1QyU5KvDSPFxHj_PhIGgrxTGU8GcZSBlfop3Xi9EyI21AxfSWXbZWmJBJCPg197pzl2443l5Oy6rGG8Lbv5-VCMpMTZTBVx69QJ09G0kymKneY1_ZcqZ0bnDKl_QzhbbgEaS6sAAqsBQ_b50cm6GnowNAQLKmtxWG_tycmktLnivQZlIVhEDZ54bgE_xdJiOmQ37-63-0JF2KmlAHzmGxo1Qi_hPeFTK_ubwexKm0GfeeHZ5eyExgGBmmw0wmW1Snorh1SgVmaeQnRPRZa8G_5ofBVPxGZLE0nXfGzf8WlNucyNWbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح عقل عرزشی رو ببین
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67393" target="_blank">📅 20:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67390">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QL0_JW9igrdy62CoMf5qgwoZwos7uiOE7waADHhyAoF-8_LhlysGAEpnxL57YKxpbfuoSYkFUDGuJp_6fu_TYss1CEB7DYkQMy1KoDa8ExK2ruIdAmTUCDlTZQQOgoCvWcw4ys7HzL7FAnceNVtthOfuYcIPMQD9HoKv35IoNEnYSENnKfsUzt0IhG1NW_-2besoe6vR5GMKLk6E5Bah5neOxXVhfHMuox9XJqO3OuCVpdJmXDVtqNCyK2NzJr_3qQheArKDi21R7KcNfUe04QRO5zzdaEvMyEsKTQjbvpPOmznOy-8geMWFIpxxck36rvut8gy236KQaNQg5apYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GhX6TvNKLyvH68G6xCUJKV8wslMf2C9eDldLCg1EzNM7p7zPpS6Bv8Ynk6enW_mIVBqvqMfOVNduH1QS-byDUh4c05kQ9Xzn1SjK3hoES6Fshw7Bj3sJ4yQvoMttEbsjWI2KqoRfXoyCMcNBolFqf2cRWStLV0Y6-8junPQqF93tCS9t8JEMqcgqDKYVh-b-iIQ-lNDcF4bE5x3KzTElpq8pUrkyva5gT0DFF2K_tOHC15pM2PDnwf7wF8cHbd2TCmSjiOVmagF9mF0wBeEBQXqFDZNdhOUeo2Bqlgn2EPyMD5xS6yGeTYHtuq2mUhJuPedXrW5k33rFHraRbz-MCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=fyyacducrAVsvgaBoqBJRUBqqv4oA5mF1goYXd42SCcKo8tSoQ5QOINjXEtFYPD-4B2D6Pc2aDNMp8cPFXxtjuuiHAQSQ9WSrGQhdltw5sRN6KsyzZdyskCTvTnsuAlR1T7pZVwS91cogYaQUgY8oUBRqbM9_KE9fHm_c2H0RSBMSgWK32BeJTvgsK5NmAZoZwhazU3moL-DEN_lXETl6TvaADIF_PmSIM4X0MF5eIO9e02deBvF7q3BixW7VtEmEs0s9Z2mq1S3dwcEFg1WqJ7GJMBargmx1gHCorRNz4ciN8BYG3ERYKAGyzrfmrqMDDVMpL-BKb8ZOzETe8Ms6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=fyyacducrAVsvgaBoqBJRUBqqv4oA5mF1goYXd42SCcKo8tSoQ5QOINjXEtFYPD-4B2D6Pc2aDNMp8cPFXxtjuuiHAQSQ9WSrGQhdltw5sRN6KsyzZdyskCTvTnsuAlR1T7pZVwS91cogYaQUgY8oUBRqbM9_KE9fHm_c2H0RSBMSgWK32BeJTvgsK5NmAZoZwhazU3moL-DEN_lXETl6TvaADIF_PmSIM4X0MF5eIO9e02deBvF7q3BixW7VtEmEs0s9Z2mq1S3dwcEFg1WqJ7GJMBargmx1gHCorRNz4ciN8BYG3ERYKAGyzrfmrqMDDVMpL-BKb8ZOzETe8Ms6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
پهپادهای اوکراینی اوایل امروز به پالایشگاه نفت اومسک، بزرگترین پالایشگاه روسیه، حمله کردند.
این پالایشگاه در فاصله ۲۷۰۰ کیلومتری از خاک اوکراین واقع شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67390" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67389">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=bCx5QDu9oKEGm-MJoinJvu0kK5oKfu6wHKCrKnXwEY1oWR7PG8rhTe_bHeAl4nB4gKkbWgzREIoSw-dTb7N7QlbWXwmKOIhImwB1r8xnxRX9qqAM8MTezSSCZL7OFlI13NV2FbsUKiZbOFvm84JyYQkmCIkWytB6M7tgs6Oyv-MHKeLmxQUPLKms8bfEyKJW4ml82ZIf6mFM-eFfWGLpDzjaFjLc5YNcR4GCQ_4kqThozTM00k7qVHEzkUM88zuXzVOUrr9geCeHNzWTGt6iG12od088M7nuXoWFAB77WPYLSQ7lBE5H7dmhukQW_cJNffKZMMrKNh463enQXpJ41Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=bCx5QDu9oKEGm-MJoinJvu0kK5oKfu6wHKCrKnXwEY1oWR7PG8rhTe_bHeAl4nB4gKkbWgzREIoSw-dTb7N7QlbWXwmKOIhImwB1r8xnxRX9qqAM8MTezSSCZL7OFlI13NV2FbsUKiZbOFvm84JyYQkmCIkWytB6M7tgs6Oyv-MHKeLmxQUPLKms8bfEyKJW4ml82ZIf6mFM-eFfWGLpDzjaFjLc5YNcR4GCQ_4kqThozTM00k7qVHEzkUM88zuXzVOUrr9geCeHNzWTGt6iG12od088M7nuXoWFAB77WPYLSQ7lBE5H7dmhukQW_cJNffKZMMrKNh463enQXpJ41Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد جنگ پهپادی:
چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند. شگفت‌انگیز است. شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد. و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67389" target="_blank">📅 18:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67388">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=qbaoIW3536WIEQ9v1zVKjtlmXLOOUkbks-TVidZ6DNCMUaEbEJC3a-6T0NW_jwKD7UBzCAQz2dc2V9E-gqtwssxS3jZ8-07XfBp4CpMU4P2plzGd6_jRK-kUhj6Tz82x3VlNiGghDABw60iEgEzGX1vpJXGUlyZU6INlTjjr6DPToNhqLCL-SgxuYMpprUJszXtwvUDKysUuXC44pVwYiT9iSe_JR4bKHc0aAbablQZKsTBTPixTSd5rQWnQwREx9OSh1kqjviyJbBCL5ccybO12CUstVlQbZAceiKUJLdy-KDYgUK0EhSJHI9hL3b17zfPNwYQb4ac-PUlXKwjltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=qbaoIW3536WIEQ9v1zVKjtlmXLOOUkbks-TVidZ6DNCMUaEbEJC3a-6T0NW_jwKD7UBzCAQz2dc2V9E-gqtwssxS3jZ8-07XfBp4CpMU4P2plzGd6_jRK-kUhj6Tz82x3VlNiGghDABw60iEgEzGX1vpJXGUlyZU6INlTjjr6DPToNhqLCL-SgxuYMpprUJszXtwvUDKysUuXC44pVwYiT9iSe_JR4bKHc0aAbablQZKsTBTPixTSd5rQWnQwREx9OSh1kqjviyJbBCL5ccybO12CUstVlQbZAceiKUJLdy-KDYgUK0EhSJHI9hL3b17zfPNwYQb4ac-PUlXKwjltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره کارت قرمز بالوگان:
من درخواست بازبینی کردم چون فکر نمی‌کردم این یک خطا باشد.
این یک نفر نبود که به صورت کسی مشت بزند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67388" target="_blank">📅 18:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67387">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=pjC_DEJEPCMHqnfRvewQGpYGYFsIz95PFIVTSfFUR8btOGsP7oodDUfblt1c1b1Dtf5hGIj9ev_wESn3ZQC3LIS0MzMdPnq3Buz1piRhIGBVyoHp5bDCZbTahYGjc8te4uK9xmc4I5LjTp8SIm6sNcA7F9MyoFLqTuqbyqWjOjbIjpy4cGrsCelvI4kyGohSiZVlGNFTDJV0hf3B32jZBGZXW9tlwSHMlqS6N30SNFfVGYLO8Z-PsmPC1AmvoODvG8TfIFy8PlwlwTxeAqPV47vNYq6qs6XgvcbQ6Ni3zlFtyeV_N8L7anTiAbLP-dsF8qdf4zQmoHnjCFTdUVqpkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=pjC_DEJEPCMHqnfRvewQGpYGYFsIz95PFIVTSfFUR8btOGsP7oodDUfblt1c1b1Dtf5hGIj9ev_wESn3ZQC3LIS0MzMdPnq3Buz1piRhIGBVyoHp5bDCZbTahYGjc8te4uK9xmc4I5LjTp8SIm6sNcA7F9MyoFLqTuqbyqWjOjbIjpy4cGrsCelvI4kyGohSiZVlGNFTDJV0hf3B32jZBGZXW9tlwSHMlqS6N30SNFfVGYLO8Z-PsmPC1AmvoODvG8TfIFy8PlwlwTxeAqPV47vNYq6qs6XgvcbQ6Ni3zlFtyeV_N8L7anTiAbLP-dsF8qdf4zQmoHnjCFTdUVqpkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره بالوگان بازیکن تیم فوتبال آمریکا:
بالوگان بهترین بازیکن ماست. او کارت قرمز گرفت. من نمی‌دانستم این چه معنایی دارد، اما بعد شنیدم که به این معنی است که شما نمی‌توانید در بازی بعدی بازی کنید. این بسیار ناعادلانه است. چگونه او را برای بازی‌ای که هنوز بازی نشده است جریمه می‌کنید؟ من درخواست بازبینی توسط فیفا را دادم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67387" target="_blank">📅 18:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67386">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=VlmayypIcIKJpM_Q8MdwUyYzoz6xEc3RsOfDGeW1LwwsyfcTTjwUqWaU-2sdzwTj_B_47nyRsxdtIByTrZfP0xsKOfGEImWud5sUshbBPGuDcKx12msUmMPkuh_1Hu9yztCaOywDiqHxZ7c5KbL38SjYeDN7SHcVTh08KraVU_MIy_tLWtFDczuJ22L8Zd8AVYbhIkmgueLr1_OItV3RcdZnYHRbS6NLPNAy7XTzQ3NVolr_-frDzfDgmkqvQHEjUIzitclSV1hO-YJ06f6SjFZblLlMf5f8SZUlKVl7RgSIyv5CtkCOwLcIb-njVpxB8-Lqw66W40sOOXsSScUtnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=VlmayypIcIKJpM_Q8MdwUyYzoz6xEc3RsOfDGeW1LwwsyfcTTjwUqWaU-2sdzwTj_B_47nyRsxdtIByTrZfP0xsKOfGEImWud5sUshbBPGuDcKx12msUmMPkuh_1Hu9yztCaOywDiqHxZ7c5KbL38SjYeDN7SHcVTh08KraVU_MIy_tLWtFDczuJ22L8Zd8AVYbhIkmgueLr1_OItV3RcdZnYHRbS6NLPNAy7XTzQ3NVolr_-frDzfDgmkqvQHEjUIzitclSV1hO-YJ06f6SjFZblLlMf5f8SZUlKVl7RgSIyv5CtkCOwLcIb-njVpxB8-Lqw66W40sOOXsSScUtnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
یا قرار است توافق کنیم، یا قرار است کار را تمام کنیم، باشه؟ و تمام کردن کار سخت نخواهد بود. ترجیح می‌دهم توافق کنم چون نمی‌خواهم به ۹۱ میلیون نفر آسیب بزنم. می‌توانیم پل‌هایشان را در یک ساعت خراب کنیم. می‌توانیم تأمین انرژی آن‌ها را قطع کنیم، تمام آن کارخانه‌های بزرگ که ساخته‌اند، بزرگ، زیبا و مدرن. آن‌ها اکنون هیچ پولی ندارند. ما به آن‌ها پولی نداده‌ایم. می‌توانیم کارخانه‌های تولید برق آن‌ها را، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر کارخانه‌ای از بین خواهد رفت و آن‌ها این را می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67386" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67385">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f387513a36.mp4?token=MWPi6f1dieF6Mxft7ppZjdcwqwG6whkQMbD4CXRMwdCCJqVck5GcQXg5zbXXtrBx67juQyTyvHLWMRtJxM6cRk_BBMc8rc6avHyrzhUY0LeTHt0f8S5BGnjOB3v0xWEq2SqEsplLimRysicV53Lza2R4QV_tfhI5sEwriyQx-mGf2dKsEb74M0rKqpkgwx8U4aBmzGmI0U_6c_CitwCp2zUEogPBBrc7WU7m1OQNU5_hDJVBK7lbdtAZaZ6tWLjUqApJtiy1kyttNqIqE5LHqmbdL0b1kmODR39L10IzKa_kKrUmXwvbQt7dbHYX25do_72iBb4MIolrsl_y_YD3ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f387513a36.mp4?token=MWPi6f1dieF6Mxft7ppZjdcwqwG6whkQMbD4CXRMwdCCJqVck5GcQXg5zbXXtrBx67juQyTyvHLWMRtJxM6cRk_BBMc8rc6avHyrzhUY0LeTHt0f8S5BGnjOB3v0xWEq2SqEsplLimRysicV53Lza2R4QV_tfhI5sEwriyQx-mGf2dKsEb74M0rKqpkgwx8U4aBmzGmI0U_6c_CitwCp2zUEogPBBrc7WU7m1OQNU5_hDJVBK7lbdtAZaZ6tWLjUqApJtiy1kyttNqIqE5LHqmbdL0b1kmODR39L10IzKa_kKrUmXwvbQt7dbHYX25do_72iBb4MIolrsl_y_YD3ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
تنگه هرمزِ معروف؛ هیچ‌کس تا حالا اسمش را نشنیده بود، اما عجب ماشین پول‌سازی است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67385" target="_blank">📅 18:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67384">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=DGfm8AuMlSxU-zVI8ftoIWkfIBAL8KbOaks0PHs5MrubQGMKaVuSKNCAK9oIwoFu9NUwDkHWQA6sd-vQCViBXwSPuse7Od22KksLd1i8JwDLv9Es9YgvLwhC2pMxeBRRxt36zuCVU1O4j3CDtmUBCT9wA0lspD9DuyGn8OFs9ViuIPJjby0LTSiXP5jgoO8Wd7hCXE6ue-r1scGtptFjTkVFd1bNrFYt0WWGyxUKI-krrVqaTVGT7U5PjjUEDMribwPdM6VYOimfv_scYZ1Lam0WOsxrp80nlgtFop7AedW0BzB6LXFlmgvW7UVf5aJAKlmPV7OUHGcNg2sbix0ZXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=DGfm8AuMlSxU-zVI8ftoIWkfIBAL8KbOaks0PHs5MrubQGMKaVuSKNCAK9oIwoFu9NUwDkHWQA6sd-vQCViBXwSPuse7Od22KksLd1i8JwDLv9Es9YgvLwhC2pMxeBRRxt36zuCVU1O4j3CDtmUBCT9wA0lspD9DuyGn8OFs9ViuIPJjby0LTSiXP5jgoO8Wd7hCXE6ue-r1scGtptFjTkVFd1bNrFYt0WWGyxUKI-krrVqaTVGT7U5PjjUEDMribwPdM6VYOimfv_scYZ1Lam0WOsxrp80nlgtFop7AedW0BzB6LXFlmgvW7UVf5aJAKlmPV7OUHGcNg2sbix0ZXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
به یک دلیل وارد شدم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
من به دنبال تغییر رژیم نیستم، اگرچه این تغییر رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67384" target="_blank">📅 18:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67383">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=hZq1KGW0DRg1Cr67bd24K9ZNHzY1a_LTAubyTuIDVhFHsa7exKsPG9KjDw1Mayzk0yO3HD-84HTFeZaLSZkKcYhm6TUzAlZeBIHHRHAE141mwkDkmEMSrs_JZa4P7VFj5NvK0cNsWfc6GCly9iss2C3qi8mJAGDRWwcTQU4hgYGuZubiq3HPI-rNLFjmxL9gdDwo4wIUh2noy-6vkagGCaTgg5D2sDq_X4m-9B7Dby2JKIRAAJ3qaQPeSLUCfZdASuxrugW7oSNK4NZ0wOksIdJgrI5HcpvxjgI7yzu8ar6uIA18X1-yNkaSPlVIo2hDD9Jk7PDZVrsgKpCoBVbf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=hZq1KGW0DRg1Cr67bd24K9ZNHzY1a_LTAubyTuIDVhFHsa7exKsPG9KjDw1Mayzk0yO3HD-84HTFeZaLSZkKcYhm6TUzAlZeBIHHRHAE141mwkDkmEMSrs_JZa4P7VFj5NvK0cNsWfc6GCly9iss2C3qi8mJAGDRWwcTQU4hgYGuZubiq3HPI-rNLFjmxL9gdDwo4wIUh2noy-6vkagGCaTgg5D2sDq_X4m-9B7Dby2JKIRAAJ3qaQPeSLUCfZdASuxrugW7oSNK4NZ0wOksIdJgrI5HcpvxjgI7yzu8ar6uIA18X1-yNkaSPlVIo2hDD9Jk7PDZVrsgKpCoBVbf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
مقایسه اجرای سحر امامی، مجری تلویزیون جمهوری اسلامی، بعد از مرگ علی خامنه‌ای (10 تیر 1405)
و اجرای ری چون‌هی، مجری تلویزیون کره شمالی، بعد از مرگ کیم جونگ ایل (28 آذر1390)
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67383" target="_blank">📅 17:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67382">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237168e66.mp4?token=klCqk6OD-l4Tp0fl8hjD6jH8n-MKsksh5LxOAb2G5okC5Vyn7yPm-hZiOwHSiyTW6lmzthehaSNwPYDqWL8fItW4Kib4WPmUhzGZfDHqKpz2hH15HZcKDtQuZksRhRwK4W1bmcpgaWRQr12AAR74UqSJUcBz2RfY7BNhuRV8iLz-CxyfIcHJliEAE3AfYjIVNc6ero3oF1NV9GFMvq9d5jdELncnEaV_FqFrkMfGM7j0X8tB8KkAfTNaI0Cf2CGBfqaFU3HUEIUMRYd6OKcCJHqooNe2Rzy2tC9aEcB5XYDJEyLMjxqmtpdl9dObg3Wwaloj41wdr1r16FzdRSPP6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237168e66.mp4?token=klCqk6OD-l4Tp0fl8hjD6jH8n-MKsksh5LxOAb2G5okC5Vyn7yPm-hZiOwHSiyTW6lmzthehaSNwPYDqWL8fItW4Kib4WPmUhzGZfDHqKpz2hH15HZcKDtQuZksRhRwK4W1bmcpgaWRQr12AAR74UqSJUcBz2RfY7BNhuRV8iLz-CxyfIcHJliEAE3AfYjIVNc6ero3oF1NV9GFMvq9d5jdELncnEaV_FqFrkMfGM7j0X8tB8KkAfTNaI0Cf2CGBfqaFU3HUEIUMRYd6OKcCJHqooNe2Rzy2tC9aEcB5XYDJEyLMjxqmtpdl9dObg3Wwaloj41wdr1r16FzdRSPP6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مارکو روبیو: سوسیال دموکراسی همان کمونیسم با ظاهری آراسته است.
مارکو روبیو، وزیر خارجه آمریکا، با انتقاد از سوسیالیسم و کمونیسم گفت تنها کسانی که کمونیسم را از نزدیک تجربه کرده‌اند، درک می‌کنند که سوسیال دموکراسی در واقع همان کمونیسم با ظاهری آراسته است و پشت این ظاهر، همان ایدئولوژی خطرناک و ویرانگر کمونیسم قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67382" target="_blank">📅 17:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67381">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=O0RI5UjuBwGZ3cQkODBRXUlEF9xzRtslHq1Pzw9Ny3bdjerxQuEIvnWxfb-NMss2O2IuP0aw74dnHAv7yWS6BCEK9DevFlSeyXEFo3hmebAvRQInKtlpDHxRNf_0Q-tIYJMOv4nYAO1QNzLeqhhb1DWuoUwPx31iNAd9TmNyz1qy3py_1ehZkaPlHNl9-QvaJZ45AG6wiPlhxhopG7l5r7BDL2N5Ztf2pVARU0kj9yUJUdTlLQtTFnWsmETYa9oxDv5EW9s95vVwYMbo5sFtm2zATZJRCYDTzBPrTfAmd3gdKMKxQE97QDRroq3mRyaSre0DLd5R366hdFDr-LGvGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=O0RI5UjuBwGZ3cQkODBRXUlEF9xzRtslHq1Pzw9Ny3bdjerxQuEIvnWxfb-NMss2O2IuP0aw74dnHAv7yWS6BCEK9DevFlSeyXEFo3hmebAvRQInKtlpDHxRNf_0Q-tIYJMOv4nYAO1QNzLeqhhb1DWuoUwPx31iNAd9TmNyz1qy3py_1ehZkaPlHNl9-QvaJZ45AG6wiPlhxhopG7l5r7BDL2N5Ztf2pVARU0kj9yUJUdTlLQtTFnWsmETYa9oxDv5EW9s95vVwYMbo5sFtm2zATZJRCYDTzBPrTfAmd3gdKMKxQE97QDRroq3mRyaSre0DLd5R366hdFDr-LGvGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در برنامه ای در صداوسیما حدود بیست دقیقه کارشناس برنامه اسامی سران و مقامات جمهوری اسلامی که توسط آمریکا و اسرائیل ترور شدن رو خوند
بعدش مجری به کارشناس گیر داد که الان بیست دقیقه وقت برنامه رو گرفتی که اینها رو لیست کنید و در ادامه میگه به جای اینکه به مسولان و مردم دلگرمی بدی داری دلشون رو خالی می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67381" target="_blank">📅 16:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67380">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=EdVhtrH86cYFIcb6zSIheIsI3nUyK7DEPkEbctaSdVzde16-GzP6IPrZBeJyTebZ-nM0eurCbDti_yi-k50p9Ag_fH5F7NSwXYGIwE8ejsyYmCnNckGGsulAI3xGnnrJZ4Hurs_o3EMGodpchfQxf6HnxH7HPzRjDDWYVT4LR56lbKyJXHD3fPecl6A0A_bOYZwc0j6pT8cPxdehbMnb3m8wZRMt61qVp-UZpQGV8-E_SfjWKON3KMmIenHufqHvogX1gebalRS3QjM2WwcWPJ4IKnBNiA0DBCJpS7zgzgtPcAh4r_egcUDJqBQJlgn-K_HnTsDqaNWcDU4o8HI9pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=EdVhtrH86cYFIcb6zSIheIsI3nUyK7DEPkEbctaSdVzde16-GzP6IPrZBeJyTebZ-nM0eurCbDti_yi-k50p9Ag_fH5F7NSwXYGIwE8ejsyYmCnNckGGsulAI3xGnnrJZ4Hurs_o3EMGodpchfQxf6HnxH7HPzRjDDWYVT4LR56lbKyJXHD3fPecl6A0A_bOYZwc0j6pT8cPxdehbMnb3m8wZRMt61qVp-UZpQGV8-E_SfjWKON3KMmIenHufqHvogX1gebalRS3QjM2WwcWPJ4IKnBNiA0DBCJpS7zgzgtPcAh4r_egcUDJqBQJlgn-K_HnTsDqaNWcDU4o8HI9pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو در گفتگو با فاکس نیوز:
ایران کشوری با حدود ۹۰ میلیون نفر جمعیت است و حدود ۸۰ درصد مردم آن از این رژیم متنفرند. اقلیتی که شعار «مرگ بر ترامپ» و البته «مرگ بر من» سر می‌دهند نماینده مردم ایران نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67380" target="_blank">📅 16:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67379">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=nPE6bDupT4GIP-xGdrtBMU7EMchQrHS8xgd4MoN4dmOh1hfor14wDVluvHbZoY7OZmzF1weyYUDfX1etbJblXHnZK46tH2OBgczqn0L6NOMulC9n7mwFCLtwyW7sxNYYHogtyJGYCyVKIANQTpLZSet8rtsXNN8n-j2-HGttjWQleGYzihGGo5zYxi0QBi-ZFXYosoWFFNRxelbR6xw-hAYiLU57lRcus2xUEmBd4XW9--DPM1PwdAr8CvxqHZs5DH2RTlRG584ZY0a4TP7RqIgTDGU6HXEOSG6d8_pxARZdxhATKMBVYmjJKUIV3-uFTCyepB7Yxk4rI1fmtTaBUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=nPE6bDupT4GIP-xGdrtBMU7EMchQrHS8xgd4MoN4dmOh1hfor14wDVluvHbZoY7OZmzF1weyYUDfX1etbJblXHnZK46tH2OBgczqn0L6NOMulC9n7mwFCLtwyW7sxNYYHogtyJGYCyVKIANQTpLZSet8rtsXNN8n-j2-HGttjWQleGYzihGGo5zYxi0QBi-ZFXYosoWFFNRxelbR6xw-hAYiLU57lRcus2xUEmBd4XW9--DPM1PwdAr8CvxqHZs5DH2RTlRG584ZY0a4TP7RqIgTDGU6HXEOSG6d8_pxARZdxhATKMBVYmjJKUIV3-uFTCyepB7Yxk4rI1fmtTaBUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری:چرا آن دولت هنوز در ایران پابرجاست؟
🔴
نتانیاهو: زیرا چند صد هزار مزدور دارد که در روشنایی روز می‌کشند و قتل‌عام می‌کنند و در شب مردم خودشان را می‌کشند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67379" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67378">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCR70sBKizt4YglVMh3lmIlMzdE8dtlY5RsVCVvSdHd1fnc71zWiI6jPiRZ45z1lIJPPWDqZ5mhWwYR8WNKzVuTM9uFVMSqbLZPfPZ6Kc3c-xuIQgZMW6Is2wZ5--rJ9BpZ_4WlIjQ3TFuSb_pJ-C9P8a2PaCC2988jvsoRnjQYnr8NFfDUav-RnHjl0BACyWhu9_8P9BBXEhhhmopjuS4xTzb45cbL7fe0ui9wyMhI7pwiuk6lz6bJKygKrJPIIVwr0ZtYGiF5Z_P_3qDbeF0k7t25tKm-TZwpffMlmd6LL0XStp3BqpqGR6xQpCxpAPEtGJV8_ymjkqPCJ4wN6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
واسه کشتن نتانیاهو وترامپ 100 قطعه زمین 2000 متری جایزه گذاشتن،آیدی رو هم زدن اون پایین و گفتن انجام دادید پیام بدید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67378" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67377">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHPK3gCcrt5q1zv4zqayexWNEBiCLoLq5htV9IugQihHjBteUExkF76zUpwuVss1TGO2QCKnRYOApZMYrh5pBm0jM-r2_HBPuPUtsThiPPyiphEPqUbC0aqXWRvOB_DrZBGGeUCoek61SApFhg6HJ5T-rvFx_mdpiZMG4BwRO4i9yUtPaXXzMXkHTYS02zlEIymX0AehFMksKIJQ2DsQVoaKbUGynxoOxMRiE2gW8_xu9bUS6J9Cx1bmkeJy2xdiEt4rm1QJdcRaraiFjOyeCcAtHhKY1nF7C7l7jclPSectIycmWC9217k57anjFHDNpM5kcjomS224BVspu9fvJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67377" target="_blank">📅 14:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67376">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NH5QX5AiQhcF4AxPhGxADPBZLRNRgkCTAHlq1LaF9h-wjyMChhCvQTStm1DTpz5wTB2udpIa9HfkIxFnwoe2RV1G3EYN-iHEl46W4f0BpjJwETAqhFcJJuFKgZCD_yEf8KMSG_DaDShxa6Amvf1V8x3wqDitt030eRuEuPQJWZGKsFWIYgMUb7fnUAvBptMaDVlY5wrmHjDiqU3nbT2AWg1hBASF9__x7uBeQz74jEt39i2GsqT8tYtgMumaV9snugk1TVCFcuIhmxcs1abm-DpDBiflaFZrjGBYBcZBXnkesnXyWIvD0V4TkPBvwkpeIcSp3MJK99MBL1PqcYiu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏شبکه ۱۴ اسرائیل :
سپاه قدس واحد جدیدی به نام « یگان مختار» تشکیل داده است که با کارتل های مواد مخدر مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67376" target="_blank">📅 14:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67375">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8dkeoMt1dN3m8IM7GE1bNQ7w5N4PnxGkBe0V6E9k-ewAQGCVZi9X5zL6BFhux7TqGpVeE1zlmjWbyKmtbAcY0ZjtV2UfoMw7ckbpq-GCsvcDrxiltb9DyElxY9feTDyIRSmpan0Or7zjoxHF-N3JxM5vWyPXuxAnhRhmzJWseh2d1ADqEqhA24H7g_SasrT2f3WGIsW2TbxFPWCiTcitIXBAo4OMSmzQYZYeeX7xjwBsK2zx3EFA_0vP2njW5fUNuR8WkJEX8zAODPI0sQL3OyR2p20yTR0Z-Ds4vWcSUEE_KjbQDJa5kfNG4FdTfbb4Pcri99K0O982_NKQ7LTIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یک بنر در مراسم:
دونالد، نابودت می‌کنیم! از توجه شما به این موضوع سپاسگزاریم!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67375" target="_blank">📅 13:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67374">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjSIh5MDBSTY5LaJwBnRqe55HxgYx32iQUoJW1Ldxn75QpwGD9aqg3z-NzVt2Wl2rHYvxc9WryEItnKkYXWg4DJdwjiE0yQ0eMYY2qLLWdQkt_VLDeaNgCVY0iDZGvw62HIll3qOhCdxAqXo6mvk7ieQIbSjYDV-08EdMERRwNuwXyPz2Q6c2buEsKKHFpUD8AzKTUKRU9myMS2khDYWRYwY4vhatMqG1mhD3l8apzCwK_OmiZ8N6VmzABjKHB68CIUUOocdct0Ccf5opdla99t-k9owloXFHqbtPZWzmbRH9grAHe1bRyH4kFnYHWeIN_ZMWH1pjD1-glsP3domBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ادعای
نجاح محمد علی کارشناس عراقی مسائل خاورمیانه و از حامیان نظام جمهوری اسلامی:
در مراسم تشییع امام سید خامنه‌ای رضوان‌الله‌علیه در تهران، فرزند ایشان، بقیةُالسَّیف، آیت‌الله سید مجتبی نیز حضور داشت. او پنهان نشده بود، بلکه در جایگاهی قرار گرفته بود که کمتر به چشم می‌آمد.
هماهنگی بسیار خوبی با نیروهای ویژهٔ امنیتی و فرماندهان ارشد سپاه پاسداران انجام شده بود…
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67374" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67373">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4acsZ0MfuVjjL8R0NvzhCcsMnSL8Wq5t1XRedr5_8Hj6DoDXgWr8zqgV7emA7HTf9dQRORnpvNh3oQ57uRu2xBuTn_IZGPpP8Vajh2kfkPyGzBtlaBLrQK2qkquQnF7s5G7gBa0nRg1VXZhqY_dpMYaSlFCdr80KPFhCxLMP0_AmT7RgF20gwZm52graYlXcmuN4Gq-G8NMf1hpSPKVmstgB_N-TU1YACNFVe_SpeVUwVnjGmKoYQHlswazKdv4sgu02OjX5xUx4nzULLAYrNBnqydJsst38uia6pTb0_fFYuk9mvm2t71NhCu9qLgJY_UeWH_y8vLTvmQKgCcHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
«آیت‌الله خامنه‌ای که مراسم خاکسپاری‌اش هم‌اکنون در حال برگزاری است، توسط اسرائیل حذف شد. هر رهبر ایرانی دیگری که برای پیشبرد طرح‌های نابودی اسرائیل تلاش کند و اسرائیل را تهدید کند نیز حذف خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67373" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67372">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=AbmDqQiBkUzRwYs3MPnEFjxdvqimvcDUkSYdE6scGeccL4dKO4OYx5ZVkIsa2y8acAM9BxiZ0_hSHVEEqSoSiqCVJBP7oJN1PVl3ogkn7BslU4al3R9KN_TQFKKoywhl_ZPmEDsZfLOm6eJOqFc0gQ158U5YWR2h4yamo975uuTl02i6aGFRwZ8ipL0x6PRWc2chLVQcRzrGCNC-ew43ETNnaWZ20vUh9_TrP9Ihq_NShn9YP_URNnP2RHOvk6fuyZMEwvp6ddzC3nWgyGF2E1GBR34e5o2EUhxS_ygoYtj9-RuZk1PVztHAk8-1yNfsziam241ZMZsMhTcEHZq-dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=AbmDqQiBkUzRwYs3MPnEFjxdvqimvcDUkSYdE6scGeccL4dKO4OYx5ZVkIsa2y8acAM9BxiZ0_hSHVEEqSoSiqCVJBP7oJN1PVl3ogkn7BslU4al3R9KN_TQFKKoywhl_ZPmEDsZfLOm6eJOqFc0gQ158U5YWR2h4yamo975uuTl02i6aGFRwZ8ipL0x6PRWc2chLVQcRzrGCNC-ew43ETNnaWZ20vUh9_TrP9Ihq_NShn9YP_URNnP2RHOvk6fuyZMEwvp6ddzC3nWgyGF2E1GBR34e5o2EUhxS_ygoYtj9-RuZk1PVztHAk8-1yNfsziam241ZMZsMhTcEHZq-dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور احمد جنتی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67372" target="_blank">📅 12:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67371">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=FzyNmCCjBJWKONfiw-BQTSqI3CIIAZ3ir76_cNu9-VRJYli0EC59yCVM_jE-aUU_l1VijTiYm5F7ERgdhgg-reSDFJUV9Zz2FwzT3jxVO9ejQRWMV-021F1WJD0TyPg-mdrtvOln84wgu5eXKhKNIX2Bz-5m5HklgKJkMQKEyrThhszY5z6brl1q4P1BRA_-D_MnlRYe5U91LhAMYW56Wno_-i9D4MFJhRZCe6uXQoj7yQ4DUH6nkpNVmNhGPrVpUEn36Ud9tmf-bXVZlRI7SUE5ERZmswInfOamgMQl2Q35OsF8Qg5Qk3tba3IBeUxtC2G8RyzVqxC2Gy9bxLw_wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=FzyNmCCjBJWKONfiw-BQTSqI3CIIAZ3ir76_cNu9-VRJYli0EC59yCVM_jE-aUU_l1VijTiYm5F7ERgdhgg-reSDFJUV9Zz2FwzT3jxVO9ejQRWMV-021F1WJD0TyPg-mdrtvOln84wgu5eXKhKNIX2Bz-5m5HklgKJkMQKEyrThhszY5z6brl1q4P1BRA_-D_MnlRYe5U91LhAMYW56Wno_-i9D4MFJhRZCe6uXQoj7yQ4DUH6nkpNVmNhGPrVpUEn36Ud9tmf-bXVZlRI7SUE5ERZmswInfOamgMQl2Q35OsF8Qg5Qk3tba3IBeUxtC2G8RyzVqxC2Gy9bxLw_wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی عجیب منتشر شده از وحید خزایی شاخ اینستاگرام با سردار رادان که میگه کار دارم با وطن فروشای لاشی،ترامپ گفته گوه خوردم
من سلطان دختربازی ایرانم ،حتی سردارچندبارمچ منو روی کار بادخترخالم گرفت ! اماخداشاهده آنقدرمهربونه،هیچ کاری باهام نداشت و ولم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67371" target="_blank">📅 12:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67370">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=FMBo3_GlL7bFubvH6AfTd1xbtrvx1vzsZ4n3TRZgGlNZKiMHQ78hQraWKm9kOieA3Ib1TWfeudjC2P85cP8Dq2JfEAKlov-UyQ9ERHx3CpGZg33abreELGdTz0Ngvpsk7wX0H5I4P-vVT-yV8pwTZrSQ4NuFqgzMe-m4ZALjt01fFb0TTKae9hrbkKeT22utzMgfqYNzb7a009JlovbA3GYkDgQ5naZGPFhTIf4OrrJVqlh2mE37LLo2uXCQ9zHMp4zl_NILqeixdHfACCS7SBKWHdi3WkQvlIU9cSj6fzj1iySeOJgS9DV9cMGR3PGkas0at6XUQ-UjXZbjkBqcWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=FMBo3_GlL7bFubvH6AfTd1xbtrvx1vzsZ4n3TRZgGlNZKiMHQ78hQraWKm9kOieA3Ib1TWfeudjC2P85cP8Dq2JfEAKlov-UyQ9ERHx3CpGZg33abreELGdTz0Ngvpsk7wX0H5I4P-vVT-yV8pwTZrSQ4NuFqgzMe-m4ZALjt01fFb0TTKae9hrbkKeT22utzMgfqYNzb7a009JlovbA3GYkDgQ5naZGPFhTIf4OrrJVqlh2mE37LLo2uXCQ9zHMp4zl_NILqeixdHfACCS7SBKWHdi3WkQvlIU9cSj6fzj1iySeOJgS9DV9cMGR3PGkas0at6XUQ-UjXZbjkBqcWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وحیدی فرمانده کل سپاه با موتور اومده مراسم
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67370" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67369">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=UyeCSE5PF-pmyM6BgQgO582vSn6-GO7mjPEC1dO5yx8lF4w9lEt7VOoSbVt3mZ-sTJHhquK6txY3NPGaaNtaiSI7njJpuOZwcLAG9USE_6ZfZnYf0LIQDInJtL6SD3DPv2XLtp-fd75QJaKZMT5DuT5sZ1nsQfMQwHMF8y4DPUQxj4lskOd1tVs320eKgSGABNcyXZf1FXY5ZGdZXSoiEakWX6CUgTc2UjU7FNeeyxrWkVWsqENIwvvSrRq-NvHlcQJPG99IuGjBWQwNkuw1HVFHhKXoYZuaSwHVKCCZvO81WS4chZMgm-PN0yf9YjYgxpJFkTKOo2o8p7OucIE0qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=UyeCSE5PF-pmyM6BgQgO582vSn6-GO7mjPEC1dO5yx8lF4w9lEt7VOoSbVt3mZ-sTJHhquK6txY3NPGaaNtaiSI7njJpuOZwcLAG9USE_6ZfZnYf0LIQDInJtL6SD3DPv2XLtp-fd75QJaKZMT5DuT5sZ1nsQfMQwHMF8y4DPUQxj4lskOd1tVs320eKgSGABNcyXZf1FXY5ZGdZXSoiEakWX6CUgTc2UjU7FNeeyxrWkVWsqENIwvvSrRq-NvHlcQJPG99IuGjBWQwNkuw1HVFHhKXoYZuaSwHVKCCZvO81WS4chZMgm-PN0yf9YjYgxpJFkTKOo2o8p7OucIE0qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عباس موزون، مجری صداوسیما:
چند بار [روح علی خامنه‌ای] از بدنش جدا شده بود و تا ارتفاعی بالا رفته بود.
«اصلا بعید نیست آنهایی که علیه بشریت عمل می‌کنند، از نیروهای شیطانی کمک گرفته باشند.»
چی میگه این
😢
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67369" target="_blank">📅 11:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67368">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vhu6cw8or-f0gNtm_9yV9_RGpudgnchBKO4H7vvKMOdM07GUZ606je5H5X3tcSxE5sy7V8UwvoCEZeiKDAUJNcSF_317yWyxfmA0inpWuWnnL649EWVfnbQi2FwstHIIh4OR9EKnrMB4Se1lQdumraSgBR1Hlj-JTWEH_fsCkUbLcAcDJXtm2hmX3NkswmGQfuM5C9s0QkAYmn4A8a_TWTUoic_lwSFbcBkeJ1hGtozDLBGI7g_Z-76vSa-wof0pWKTIoA3hb9UmQzfQVKqn7OxjhldiowjO6VGuvRvcLC1fdetPxQy82b9qL9a4QYXCRO_L_FX8VzGExO9rDgeWxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکبر هاشمی رفسنجانی،24 اردیبهشت 1370:
سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67368" target="_blank">📅 10:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67367">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=K2GVljxiTwbJvTTsZrARCsU37vySvtiGHi4757iVEzElcLi68TcVgFnwrfxnGWiVVIvzmwqqbv0wQzQ-bpYsteNEASffIfmHt2BuE0l_oOLxod17VCA3kIBny9rvqSWCQ5btV4lJ44on45ZjSACA4XssqX7n9GtOSbc_7uPWQ1St37kbOLht7BmndYtdHFBO1guVsR8SiWCBE6xmIs-bZRwCxS4U_feWBGkOGB8MgjfJRdZ29KvXwO3EuZ8dnuC2jmrRaRcoJWlnlU_z10VUfpJNgp8txbqOygpskvOrd3X-hA8GL34wIeZTef8LF7liL36WkCcwWh-Oewe5qLklMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=K2GVljxiTwbJvTTsZrARCsU37vySvtiGHi4757iVEzElcLi68TcVgFnwrfxnGWiVVIvzmwqqbv0wQzQ-bpYsteNEASffIfmHt2BuE0l_oOLxod17VCA3kIBny9rvqSWCQ5btV4lJ44on45ZjSACA4XssqX7n9GtOSbc_7uPWQ1St37kbOLht7BmndYtdHFBO1guVsR8SiWCBE6xmIs-bZRwCxS4U_feWBGkOGB8MgjfJRdZ29KvXwO3EuZ8dnuC2jmrRaRcoJWlnlU_z10VUfpJNgp8txbqOygpskvOrd3X-hA8GL34wIeZTef8LF7liL36WkCcwWh-Oewe5qLklMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
خرافات پدر ایران رو در آورده.
آینده ایران در یک جمله است؛رنسانس.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67367" target="_blank">📅 10:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67366">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=XWvUHE9YN9sDCyFpBpR0qcMapdNcHxhfiPFXZIt1tBgtlG-D1X-hr9HgASYCLju5kAOmF8Ozt2qk6vtx3eV2vZkQq1GxDDHpIK434POmRETzCW1gxYyGvMLyx_i27WiBmo2FGyVdW5dZrMHRKgSsVj9BhZ7j5Tx7bjRh2VwLfUWUDyex-I5dTX_LxObjINir_saW37XHAx2M-_qtUIwic0KQXxgHCEpCOcqhxuLf7i8kMiLWOkuHamsQuAZUBFI-gQcorIBTfKhnblPswpVmOktygB5W_1fD0GR5tNsayCdY1GxuYTFwiG4N9aCA2Wh48W2LxRH3yGEm8UGIZqM-Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=XWvUHE9YN9sDCyFpBpR0qcMapdNcHxhfiPFXZIt1tBgtlG-D1X-hr9HgASYCLju5kAOmF8Ozt2qk6vtx3eV2vZkQq1GxDDHpIK434POmRETzCW1gxYyGvMLyx_i27WiBmo2FGyVdW5dZrMHRKgSsVj9BhZ7j5Tx7bjRh2VwLfUWUDyex-I5dTX_LxObjINir_saW37XHAx2M-_qtUIwic0KQXxgHCEpCOcqhxuLf7i8kMiLWOkuHamsQuAZUBFI-gQcorIBTfKhnblPswpVmOktygB5W_1fD0GR5tNsayCdY1GxuYTFwiG4N9aCA2Wh48W2LxRH3yGEm8UGIZqM-Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم وداع با جنازه علی خامنه‌ای، وقتی نوه‌های خمینی میرن جلوی تابوت سید علی خامنه ای، قاری این آیه از سوره نساء رو به کنایه می‌خونه:
آن گروه از مؤمنانی که بدون بیماری جسمی در خانه نشسته‌ان، با مجاهدانی که در راه خدا با اموال و جان‌هایشان جهاد کردند، برابر نیستند.
اونا هم برمی‌خوره بهشون وسط آیه ول میکنن میرن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67366" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67365">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnjK-2DWSNY5qpbvzLyfy55Ix02nqjw3zlnQqag3JQB_tMQ7ODWB63buRPY-pCFm1DaEqnM-0-3ld_ptgEnTjQNexYgrsjpR-bj0uRzzxqckv5r8WX5QltEFbj_i1p6MTMGw120InuCCvXYCA10Do28nBkBME_Ebkmhro871OlyNz6X1Zr5KdP6yvLNUeKE-O1d9kUtZm1mLk-JUhauewolXe8gVjTTeNp0YDqeLAMqfgcE0-ebQM9nq44HA0rFTr3alrO29KSX8-TNrsRm5fOgWW3hQM_cLe_zeIF_ZjJkv9PPMY50VagMLlQL1i-zyMAdbSwnEdIw7hV-PrWOO3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
قالیباف در گفتگو با محمد درویش، رئیس شورای حماس:صلحی با آمریکا وجود ندارد و اسرائیل را به رسمیت نمی‌شناسیم!
🔴
دیپلماسی باید در خدمت حفظ و تثبیت دستاوردهای نظامی باشد.
🔴
مذاکره زمانی موفق خواهد بود که کشور همزمان آمادگی دفاعی خود را حفظ کند.
🔴
ایران بر حفظ تمامیت ارضی کشورهای منطقه و پایان جنگ علیه متحدان خود در محور مقاومت تأکید کرده است.
🔴
جمهوری اسلامی صلحی با آمریکا ندارد و اسرائیل را به رسمیت نمی‌شناسد و حمایت از جبهه مقاومت را در قالب‌های مختلف ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67365" target="_blank">📅 09:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67364">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67364" target="_blank">📅 03:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67362">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fkqf7_BGgRWQ9AC36ZmPxttaamjQ7x8gJUb9eFAa8LpAluAqXZjl1Gj0rExNyMdhPAovuDM_ihnhgrmKUR_pB_FEbp_UrsHtqVduri1KeDNxpYtzMeazjwoLea7t8bCNCIc6XL9NbLlOLTadE3690Mz7fL7u7HJE7IEU8iy-evAdBSAPBt4mKbG66AG6ZYSe1Oe_AzNbAd8mDMaeuDmky7-RNTrSIBdcCT7RZJqz6SGdLLV5rlV6LgZQPxgU9YlyX0pj3Lq059aCZr8x1fp36xEE4qRWWvMeC4q84UyS28O5LrdQYUXYwRLdZsKImYr4L76TYxw7y_7a3OidQosJgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67362" target="_blank">📅 02:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67361">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=opccwdwsi2RmXdG_mwg2P8zX7T_pEQkKmMF59KNv5QrZiU3REfVREJZFUShgXCyWRM-cfm_7yHPjPf_CEBc60QeyXAzqqCmDRPZz1-5KQwK_XwA9baa1pt95kiQTXIXCVA70inz2H-v1lTZrqJL6-wCVUgwco_R9f16FG2NVqnHGYu9XqMZFhhwIEmcxQ6qz9r-_1hUe5TEfJzSC_GOTYJgdXDODmOxl4pI3ILUBDBTXKezCor4mJF1nnV7TB7M4bkpgiS3WD0hz8uqLT2AKHVlSx5l62Hb5Z0IIAi-V3EgV3FYxbX6xm2MCOJvEGM7kp5HwDsXbpypuuxpCt-qozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=opccwdwsi2RmXdG_mwg2P8zX7T_pEQkKmMF59KNv5QrZiU3REfVREJZFUShgXCyWRM-cfm_7yHPjPf_CEBc60QeyXAzqqCmDRPZz1-5KQwK_XwA9baa1pt95kiQTXIXCVA70inz2H-v1lTZrqJL6-wCVUgwco_R9f16FG2NVqnHGYu9XqMZFhhwIEmcxQ6qz9r-_1hUe5TEfJzSC_GOTYJgdXDODmOxl4pI3ILUBDBTXKezCor4mJF1nnV7TB7M4bkpgiS3WD0hz8uqLT2AKHVlSx5l62Hb5Z0IIAi-V3EgV3FYxbX6xm2MCOJvEGM7kp5HwDsXbpypuuxpCt-qozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
ارتش دفاعی اسرائیل:
پس از فعالیت در نزدیکی نیروها: ارتش اسرائیل یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را در منطقه العقیده هدف حمله قرار داد
امروز (یکشنبه)، نیروهای تیپ کماندو یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را که با موتورسیکلت در منطقه العقیده، در نزدیکی منطقه امنیتی محل فعالیت نیروهای ارتش اسرائیل، در حال فعالیت بود شناسایی کردند.
فعالیت این تروریست‌ها تهدیدی برای نیروهای ما محسوب می‌شد.
پس از شناسایی، ارتش اسرائیل در یک حمله دقیق، این تروریست‌ها را با هدف رفع تهدید هدف قرار داد.
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود ادامه خواهد داد و به سازمان تروریستی حزب‌الله اجازه نخواهد داد به شهروندان اسرائیل و نیروهای ارتش اسرائیل آسیب برساند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67361" target="_blank">📅 01:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67359">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ck2fmDUos9lpdOEaa2aS-xWlUqDT9vVeON6oVCG96o25InsQ2FLNxQU6awQP1HYnKJt2Zm9GJsOIIisokoKS1jpe4CdFyvpPU0-4EYg-s62l-o-EK3EI9jOf427iJ_CmDcOvYKnwLOEYUG20-rUbvE6vkvbR9_C_tzlizLvmvimY9HSbM5NjjoyReb7ao1EVY8n-hN0bKNVsmIcWvISwm-dGxI-FyJsOhQHuQWEccKRnvKhVjB1-GjAfJ_cJfaYBqk5xd7z9QDsOCwxj6lfH3HgyCInGIS0bhh_KYNmSOL-NpIxOz8VdjUSKJdyF5FCvi0qtJZRNb1d1zkEvVbJVlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کانال ۱۴ اسرائیل:
انتظار می‌رود نخست‌وزیر اسرائیل(نتانیاهو)هفته آینده برای دیدار با رئیس‌جمهور ترامپ — که هشتمین دیدار آن‌ها از زمان بازگشت وی به قدرت خواهد بود — راهی واشنگتن شود؛ دیداری که در آن برنامه هسته‌ای ایران و خرید احتمالی جنگنده‌های اف-۳۵ توسط ترکیه در صدر دستور کار قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67359" target="_blank">📅 01:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67358">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=CLnr9YTpbOLo9fLbXQd17WoKCaEuNB_oNQRy8zwrUY6CtU0dPNrkJzH72w3hZE7j4JOSdkx0-UyTRXXd_iCN3Dr3PnlkoXrIekcTG7hlAl-BwTRJaEg3UjHfLExUhcX4YjVCG0UOkTLMzDDQDZbkFS7pydNEWDKgv7YnwNNRSzBN6-S6igW82ogztn8fIAVdoP6cDxY5aKH9fwmXliHUl9ZtUqx5tLEgkgKe8dR-51WWjB5onvJz8JUxbenrc0RVitO0fLf14oEaj8vrQKsib-pUdbr8VGHwnRy2gIKt4ZU_s5Edlwfqjhnt43FMiW8V19gIZoWZWfxmJaXg_Dd4gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=CLnr9YTpbOLo9fLbXQd17WoKCaEuNB_oNQRy8zwrUY6CtU0dPNrkJzH72w3hZE7j4JOSdkx0-UyTRXXd_iCN3Dr3PnlkoXrIekcTG7hlAl-BwTRJaEg3UjHfLExUhcX4YjVCG0UOkTLMzDDQDZbkFS7pydNEWDKgv7YnwNNRSzBN6-S6igW82ogztn8fIAVdoP6cDxY5aKH9fwmXliHUl9ZtUqx5tLEgkgKe8dR-51WWjB5onvJz8JUxbenrc0RVitO0fLf14oEaj8vrQKsib-pUdbr8VGHwnRy2gIKt4ZU_s5Edlwfqjhnt43FMiW8V19gIZoWZWfxmJaXg_Dd4gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ای که فرستادن به صداوسیما از لحظه حمله به خونه نتانیاهو و ترامپ و گرفتن انتقام علی خامنه‌ای
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67358" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67357">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237c10defa.mp4?token=Xi9VO_3b--09fuUHfUbg-Jn58WFDBp9wftiLte_JFx3h2rvqPmwFvGgH90vV4v-TdOnWF8zPao4LLhDdDMMsGii7fHdU7cAeay3MVqF3bHdhjKKheR5lO0SVPFVcUjFyzZH6r0CXXzpax0qI9roM0H6IVsCDZXGDKWEhL394QEJqXyWxPowWB_kKV1BBFnEyBZrBWrMyveDzY2TUbi2-qWri5_thzHBcHPO8G3uv02v4Kg_2JnyiAuBcw3qM_ph1GcvyJDdfR715R6NgptB5_ULnSbYVMG5Gp4_H0PrRjVf_skyN2z0gypnG375GDte9vDkQtVL7ZcZ1nf2d0qtqJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237c10defa.mp4?token=Xi9VO_3b--09fuUHfUbg-Jn58WFDBp9wftiLte_JFx3h2rvqPmwFvGgH90vV4v-TdOnWF8zPao4LLhDdDMMsGii7fHdU7cAeay3MVqF3bHdhjKKheR5lO0SVPFVcUjFyzZH6r0CXXzpax0qI9roM0H6IVsCDZXGDKWEhL394QEJqXyWxPowWB_kKV1BBFnEyBZrBWrMyveDzY2TUbi2-qWri5_thzHBcHPO8G3uv02v4Kg_2JnyiAuBcw3qM_ph1GcvyJDdfR715R6NgptB5_ULnSbYVMG5Gp4_H0PrRjVf_skyN2z0gypnG375GDte9vDkQtVL7ZcZ1nf2d0qtqJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پهپاد اوکراینی یه سرباز روس ـ افریقایی رو تو یه مزرعه تو شرق اوکراین بدون شلوار حین دسشویی کردن گیر اورده و افتاده دنبالش
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67357" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67356">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhdENt9UrwmLOLGKRIBWS4BNzxtKuep0XuDAPXSTF8osh-XMUIsnkuLw2uhL1UOqi0f38xPA1p6YhCd_M1B5rJgbnwRgOP94BHYgaoH2UdkNpH2I3UoKdQuAycRFXW221ZFguQgwYS5exM3S_eDgX3_Xp0qzDauJN895ntGJdnFFo4dsPqhzGX0urjuQXjtwlV758Pr7Y-oOYuTzaH7IGfZJhsBcdWrGwqS_81miu2HxIgqNijs23dE2nI2kT5BoZA9nBil55minlpE1ubVDonuWOxnouBT3BmELKV00ItXLvRN6CN-Py1Oturmn0MtUCvHuYs8YAnRR5hvXdgtQOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سنتکام:
یک چترباز ارتش ایالات متحده اعزام به خاورمیانه، آموزش تیراندازی انجام می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67356" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67355">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=kbUzHK2sVFyl3a39CDb_hR0m62OZ6bjFczu8By30LrQoBNTsF65zVX5RLa1GJB9a6GT2Foy2heVXJPPVpUXhuvwlV-35dPNQg-smMVBxIKp2Ignyg-5U9irVag3VMw8P5wtl80wpc79bBSCzLJNaluqx9tQXp0QFSA8eWya2Z9lcTWXOvZVI903AlHK_aI6jhJEOehFPU2RU_pmel_q_B9IOrdkMLgn-N9187DVLbQTOT-YCzxMkWAak224DaU1FR2IZiMkmG7bjGrSbIsxTov6WotC0bXv71jDoZAVmJvXW-udvRsEt4n89wiEShQWOSpsCgfX0A9Z9LKo0CoKr-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=kbUzHK2sVFyl3a39CDb_hR0m62OZ6bjFczu8By30LrQoBNTsF65zVX5RLa1GJB9a6GT2Foy2heVXJPPVpUXhuvwlV-35dPNQg-smMVBxIKp2Ignyg-5U9irVag3VMw8P5wtl80wpc79bBSCzLJNaluqx9tQXp0QFSA8eWya2Z9lcTWXOvZVI903AlHK_aI6jhJEOehFPU2RU_pmel_q_B9IOrdkMLgn-N9187DVLbQTOT-YCzxMkWAak224DaU1FR2IZiMkmG7bjGrSbIsxTov6WotC0bXv71jDoZAVmJvXW-udvRsEt4n89wiEShQWOSpsCgfX0A9Z9LKo0CoKr-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه کنین؛ توی اردبیل چند تا آقا نشستن با یه خرس نون و پنیر میخورن
🗿
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67355" target="_blank">📅 22:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67353">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXgrD4yLLFL6xzmSxxvB0fHtG_dHI-x5W-uRj1KjLDBRP0_n3CIAbf66rDOSmLDLgNVo_InzeedSh9RNjp4nlBDAQZ3G3QnNwRRWOHeShcIf1adQbJh7K6978hvqRu69hTUdPalfAuWxwAz5vhRRZsRBXueSWIz6dygi8n-h1NZ-i0gNcCSaTk2HWcZfJC_hCsc81KS9t5mO-mR9Dhsa6KWgZzXUCmJ2NvFw4O8KHpUwikg6Z6gZl56tsWHEOu-qpo4kjlZiizEx2xBH-3DAg2lLfrIVpzaAbOPq7nEG1ys6_wce5gDPkjqecc1XAMz5dy-suVo6nMyDKyHsUpjjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
مثل اینکه مجتبی هم بوده
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67353" target="_blank">📅 22:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67352">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=m5ewB6gM1wQCT3DCLlVAHIo-HLnZc4697vthSLiHoGw4pxpATIrwGHx9_BcVfIKFN4jEmYKFPwj3bMojLNVP7PCE65CvdRhIXrecNZ_i7cuPu11YJeEd9Do-n39DuestPo2Sqp3EE91N5If67bvstQz9AgezDyJNvKceVi3Y4f-ylTitA_nKAYsJxr3hzOFIzFY7nYl-31lDuX_JS1h6CfOMhrWo1gbZgXhPQWmCrARlPSZhtTvUWsVVMdnaeKK85uNjJkDCJpHCg81bDle4JFmqMAAyJ_KjYZv9UDNvxlAS6oD6XkxgBUHPT_LRk7pqDkWkvytIW5gSEAECbTB5ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=m5ewB6gM1wQCT3DCLlVAHIo-HLnZc4697vthSLiHoGw4pxpATIrwGHx9_BcVfIKFN4jEmYKFPwj3bMojLNVP7PCE65CvdRhIXrecNZ_i7cuPu11YJeEd9Do-n39DuestPo2Sqp3EE91N5If67bvstQz9AgezDyJNvKceVi3Y4f-ylTitA_nKAYsJxr3hzOFIzFY7nYl-31lDuX_JS1h6CfOMhrWo1gbZgXhPQWmCrARlPSZhtTvUWsVVMdnaeKK85uNjJkDCJpHCg81bDle4JFmqMAAyJ_KjYZv9UDNvxlAS6oD6XkxgBUHPT_LRk7pqDkWkvytIW5gSEAECbTB5ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی :
یکی از گرون‌ترین سیستم‌های حفاظت در بین رهبران جهان مربوط به علی خامنه‌ای بود، اما نتونستیم اونو حفاظت و پنهان کنیم و از دستش دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67352" target="_blank">📅 21:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67351">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
ترامپ:  از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!  @News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67351" target="_blank">📅 21:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67350">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FENiGPLMoec5zkg-s5cy-mMeudsTRtI6FzEh-HznPcMlFJ-VtvQkRjPMxxiSqYLAwWGVAqvu15gtAD1nPTRgbrQqTzy4VlawexZzRITNPkoqOESeYAW7-uXzs2XYScuiYswxJcJIPkso4PE4lSuoorL5WmCMDAp9iO3WRH8ZsxSx4Eee1exp0F6acU2uTYgnGGJSaYH5veFtJv5-ezYEv5ILjjLsm0tNsE3RKpnNjrMIrikeY64W3GORuo-KW1kqKYIJo4l5hk7JnUWThBESSle21FhH9ch6AcDCzfTEGnj5l9I3I2oIHi3D_PsPZhwWbhnm3n3lI0dDgo42MXazTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67350" target="_blank">📅 21:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67349">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=Qi62q07BDtRrREN0dTZkJ9JtjC2UiBb7J-aemF46JL611LUC7UsRMNA9DR6ySAULDDeaCoYZIjtG6D5hHe52znNZmXgyK43mtKaEqxB8c5vB9aFwkbdZLXcl1ePQ2_H3TDDIQ7f9nYxXzb4bXP024l25qMoBoz8881JM0cGtpO2jXo2WQQERx_LOFpaNmU08bnCSQ8QBK7qyQ9lD1lL_csBCEqsg9fiIopbjq-1eK3scCg6sJTz7_vBve70QCFzswcHnYq53N9fSjs2UvLRNKMTpodpmVHv-V-e6YOxTqEHuyPXuq3f-wmr_cUDcrkqBfqT0QBARUct8rMLtpnCzJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=Qi62q07BDtRrREN0dTZkJ9JtjC2UiBb7J-aemF46JL611LUC7UsRMNA9DR6ySAULDDeaCoYZIjtG6D5hHe52znNZmXgyK43mtKaEqxB8c5vB9aFwkbdZLXcl1ePQ2_H3TDDIQ7f9nYxXzb4bXP024l25qMoBoz8881JM0cGtpO2jXo2WQQERx_LOFpaNmU08bnCSQ8QBK7qyQ9lD1lL_csBCEqsg9fiIopbjq-1eK3scCg6sJTz7_vBve70QCFzswcHnYq53N9fSjs2UvLRNKMTpodpmVHv-V-e6YOxTqEHuyPXuq3f-wmr_cUDcrkqBfqT0QBARUct8rMLtpnCzJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد مخبر مشاور علی خامنه‌ای:
قاتلان امام شهید به مرگ طبیعی نخواهند مرد و نظام آنها را به قتل خواهد رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67349" target="_blank">📅 20:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67348">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=GRBIav8Dh-_b_cJ6ahdkm1c-DUd_ov1K1YAyQGMRQjhga5Q2yEMuCfnAXk5wFh9t26lpBugUVn3uBjHYUFMgBewmIVGX_KmXGIFLdnRwyq-AAH9K_UpVB4JAspFJGMwgUETyD5nq9B6V4MRm8p-OZEP5vFlvcf2kXMgbSpx1HmyPBPs-Wk5qw0GvwldCKhtCLAXA1QBT4Aeeld3iq84Cjc4FMr71I9hSNeCC7tSVFARktBQUi-mfhgDT3KX53myVEfbbdobrCdzLkdbh-CRIczkibMAt6MNnPQqZukDaTAogqRxNe72sl_5qXjoNJI8ndiQTNMv9eUisK1ouxfdo1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=GRBIav8Dh-_b_cJ6ahdkm1c-DUd_ov1K1YAyQGMRQjhga5Q2yEMuCfnAXk5wFh9t26lpBugUVn3uBjHYUFMgBewmIVGX_KmXGIFLdnRwyq-AAH9K_UpVB4JAspFJGMwgUETyD5nq9B6V4MRm8p-OZEP5vFlvcf2kXMgbSpx1HmyPBPs-Wk5qw0GvwldCKhtCLAXA1QBT4Aeeld3iq84Cjc4FMr71I9hSNeCC7tSVFARktBQUi-mfhgDT3KX53myVEfbbdobrCdzLkdbh-CRIczkibMAt6MNnPQqZukDaTAogqRxNe72sl_5qXjoNJI8ndiQTNMv9eUisK1ouxfdo1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
قول میدم راه امام شهید رو ادامه بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67348" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67345">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gZXEx3zQZD47EtVJPFPvw_Ra9H957gvbPoOmgD9QJlbli-etyJB6fglxEySqKXVOIzqiuac4-KfMmQ6tWDh6-wn1xxKcGF7dVxJD4PpWO-cdVbcxhQEuOamqGSfdildZ114Hz7D6crKEFKNeT9fSAaFWc_OeakkyNtL_3i4vFSIJpLZszuh9Amu8PAtbDkAwb1gfbzKjNeaYQ5TeIcXx0Vjg0q8BQZ3FrDE5dQ4etgH6v8Llz7d5PHuLDe4oLCAb31T3kHUo0kvd56TY_OunziO6IKAK7nTqST89m2ZHXvVR_MP3D0J8x3J9JJ0D1s5bdVYE-2fPmUqtAjPIfw7DFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcLka_1OkqWfaP7Dwc-WNEL1Q99KbsJWwUWC8mls24WiPOJjxYp5DD2CpVt1VY5Kf7VPZub-VOtWrPJGEQGrVmXXBFYohxYreOYjvWdzVYqkEf59TWWr1XTOLNhh8iE2ALB2NIi2GDxaHEi6EkZnxN4CxqE9zhSnOOak0Ct7KLFtWAjmmC0cihH67TWWNoVsSEgQ8Kr-VPtgszOHlEtuu8MDHxOeURxx9YEN2WdwHwTKDn2ErQbutwI1kSal3FYIvM2XDtmFX4O05MVoH1nGpRQ6EnBu2_exbCOFwS_W0CuOW6hGa5nHOF-KE0q4ZPP3Ij9-wwjXXuZC5K2EIm2mKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a975887416.mp4?token=q5fubZlMrEjnGtBBqWjhJbWmCZaVa1cH5SBeMReAGUJBnEcJMNAE0asp1BUiPLJxc4dmcAPormALTbUIfObqYeg06Yohk2mFPBRR9oO5Gz2kORzmueoVdDWmrtyB_vah09lA2DqfMApee-o59vhio8xEY6NGJiL3VnWnFLq0RFiRBIyok49BgA4A8g0uqPplRaQM6G2fvs9FDDKypctVxJLeZKm7xUpPRV-Dlg61UlQf3OmCQD0a0ix78SBHwR_nwCYaHT8AhOU4-lLxQPYTi2Zpf1Wg77uX5u3JbUBtSc06Pg7yinimkVhqvg7cgm0R2mV0iKX1-P2gQXeFTnFD7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a975887416.mp4?token=q5fubZlMrEjnGtBBqWjhJbWmCZaVa1cH5SBeMReAGUJBnEcJMNAE0asp1BUiPLJxc4dmcAPormALTbUIfObqYeg06Yohk2mFPBRR9oO5Gz2kORzmueoVdDWmrtyB_vah09lA2DqfMApee-o59vhio8xEY6NGJiL3VnWnFLq0RFiRBIyok49BgA4A8g0uqPplRaQM6G2fvs9FDDKypctVxJLeZKm7xUpPRV-Dlg61UlQf3OmCQD0a0ix78SBHwR_nwCYaHT8AhOU4-lLxQPYTi2Zpf1Wg77uX5u3JbUBtSc06Pg7yinimkVhqvg7cgm0R2mV0iKX1-P2gQXeFTnFD7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
حملات ارتش اسرائیل به نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67345" target="_blank">📅 19:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67344">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=Tqqybg7wZFniC5CxexO11V5KpvuE2QQckqrbH5N7QqqEemORTLna2aFK8QQV-ktNg9Qx_kXJcmZZBwXJmZ3bGbGM-pmP6UjVUAEz1XOZvUMd3jcyWc53nLwG5DhQFROCLWBXH_pF68DiQ-zBW6GNY0EQsJ0EFCh8nhJCdGxCib6P18iv89pb_aGNG476JoY0uKJDQF7IEOGJOtLJ2Cm2Q_XFoHvb6KIRkdpMj4CzCG8E6uo6cNof1K8qAgdj5PLlo2cqkOCa587KcL5vuorhzwbO9xe_srSSjV2sbVMa1jy_fEXtqj0khq0rirNVM7O2NKQm34KUY5XahVRsJW1AdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=Tqqybg7wZFniC5CxexO11V5KpvuE2QQckqrbH5N7QqqEemORTLna2aFK8QQV-ktNg9Qx_kXJcmZZBwXJmZ3bGbGM-pmP6UjVUAEz1XOZvUMd3jcyWc53nLwG5DhQFROCLWBXH_pF68DiQ-zBW6GNY0EQsJ0EFCh8nhJCdGxCib6P18iv89pb_aGNG476JoY0uKJDQF7IEOGJOtLJ2Cm2Q_XFoHvb6KIRkdpMj4CzCG8E6uo6cNof1K8qAgdj5PLlo2cqkOCa587KcL5vuorhzwbO9xe_srSSjV2sbVMa1jy_fEXtqj0khq0rirNVM7O2NKQm34KUY5XahVRsJW1AdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما در وضعیت دائمی جنگ نیستیم.
من خودم، به همراه رئیس‌جمهور ترامپ، چهار توافق صلح را به پیش بردیم.
تنها مسیحیان لبنان نیستند که از ما درخواست حفاظت می‌کنند.
دروزی‌ها هستند، مسلمانان هستند، مسلمانان سنی هستند و حتی تعدادی از مسلمانان شیعه نیز همین‌طور.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67344" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67343">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=avo13aIkpeb6mkLOj84neTKfXb1Fqdgt_7bez_hGguELTI1W__9VhRDKXvPXGICTVnK42_IZJ0qx4njm3fVQMTftQKny-8zrO0O-awZiA11BZjCz7E01dmlomE6tR-ZzEOiIKhrNqnHxgCqwXFiA2NXGZB8ls5uonkE5nJyvqZ46GAhj3qYPnKLxJXmI2-jmYzAKwo_uv73yw0wssDrH8zMMLTzXVmbFT3zCaLJW3oM_5i3KqCaBmG5Rsti6966_aLpNu-MiHEO_TzXprbctJm743yRWPPhzuhZ1iF8ow5TM0lnYYU-saBm23K_V_C2UTN6eOPX9NG8Dcgyzy7JdTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=avo13aIkpeb6mkLOj84neTKfXb1Fqdgt_7bez_hGguELTI1W__9VhRDKXvPXGICTVnK42_IZJ0qx4njm3fVQMTftQKny-8zrO0O-awZiA11BZjCz7E01dmlomE6tR-ZzEOiIKhrNqnHxgCqwXFiA2NXGZB8ls5uonkE5nJyvqZ46GAhj3qYPnKLxJXmI2-jmYzAKwo_uv73yw0wssDrH8zMMLTzXVmbFT3zCaLJW3oM_5i3KqCaBmG5Rsti6966_aLpNu-MiHEO_TzXprbctJm743yRWPPhzuhZ1iF8ow5TM0lnYYU-saBm23K_V_C2UTN6eOPX9NG8Dcgyzy7JdTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
روستاهای مسیحی در لبنان...
برخی از آن‌ها در واقع درخواست الحاق به اسرائیل را داده‌اند زیرا ما آن‌ها را در برابر حزب‌الله محافظت می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67343" target="_blank">📅 19:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67341">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=LkrUe3ddnrb8Sc6QIwEkhK5vpBMF9fm244z0E3oYnVOhIY6NDYaW9MdCGPzfbn6B2KYU_8lZz7L0CaD8C-u3woccDFyjMsJMj6CDQkm1EA6__X4vYkUnP30DG3QzUkiJLnq7ilwAxyVyaHgC8sZ2hLKHK11Rtq0HGnmTXS26-d9Vxts5y60q3zLL4J9VEQq78FA1HImagCOPH31G5Zq-o_zqCXk3ho4nfnRs1kKOAsVZbzXWz9TSuN_ryuoBes5TDvcFPB6Yty-etF1v5_hUceRVGUFuUS2GM7mDjvtziac3attpjEp8kKoNfMFg2CA9nnCersjgedrmACyJKrDDng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=LkrUe3ddnrb8Sc6QIwEkhK5vpBMF9fm244z0E3oYnVOhIY6NDYaW9MdCGPzfbn6B2KYU_8lZz7L0CaD8C-u3woccDFyjMsJMj6CDQkm1EA6__X4vYkUnP30DG3QzUkiJLnq7ilwAxyVyaHgC8sZ2hLKHK11Rtq0HGnmTXS26-d9Vxts5y60q3zLL4J9VEQq78FA1HImagCOPH31G5Zq-o_zqCXk3ho4nfnRs1kKOAsVZbzXWz9TSuN_ryuoBes5TDvcFPB6Yty-etF1v5_hUceRVGUFuUS2GM7mDjvtziac3attpjEp8kKoNfMFg2CA9nnCersjgedrmACyJKrDDng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار تسنیم : نظرتون درباره رهبری مجتبی چیه؟
🔴
زن عرزشی : چی بگم؟! نمی‌دونم ما که همه منتظر بودیم مجتبی حداقل برای تشییع جنازه پدرش بیاد و حضوری باهامون صحبت کنه، ولی بازم نیومد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67341" target="_blank">📅 18:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67340">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c05464482.mp4?token=XZ43aSbgb0Pa6esPBYjuzx53Hs8SdmvcoDcQO6LMRrRTrl3dM3ZCtM1624-RxA_Hj2eOeEoW3DpwvSQeJiShFaR3oVTNYRQVtOkQwzVlv7DmeJB_k10QFgjO45GWkKN3T7KaCyCIlYqiafv-abOcE7_jhL4lt8jxIN-A-D8BvCSSYuAm92Xp4JuWNJCBobfFPkw4Oja7ocFAkS7T5CTF7XdGe_7JO7KWgWCUVN_gf6mdpA7jkruXblxQYiu9GpNKXofZuUaI9tw1p9mV41fOP-sY_WbYKgh_4vOiTIIF87fnLNeNkxbV17Hm-03G8xXC23z1gjM6X7ZTrDhViS6wgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c05464482.mp4?token=XZ43aSbgb0Pa6esPBYjuzx53Hs8SdmvcoDcQO6LMRrRTrl3dM3ZCtM1624-RxA_Hj2eOeEoW3DpwvSQeJiShFaR3oVTNYRQVtOkQwzVlv7DmeJB_k10QFgjO45GWkKN3T7KaCyCIlYqiafv-abOcE7_jhL4lt8jxIN-A-D8BvCSSYuAm92Xp4JuWNJCBobfFPkw4Oja7ocFAkS7T5CTF7XdGe_7JO7KWgWCUVN_gf6mdpA7jkruXblxQYiu9GpNKXofZuUaI9tw1p9mV41fOP-sY_WbYKgh_4vOiTIIF87fnLNeNkxbV17Hm-03G8xXC23z1gjM6X7ZTrDhViS6wgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زینب سلیمانی:
شهادت آقا برای ما سنگین‌تر از شهادت حاج قاسم بود
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67340" target="_blank">📅 18:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67339">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDTeNy_-CDY1xAcdFVOXG0z4PXpO088OeVa8sXS7wuBio2TCCHak7EJXG6X2kbBMCGz67zI0gygRw1CGFT-FhJyhmabXJexraTJo41TWx62vFW5O53zxnVzLSlzDNz4N9kgOJJqe02-HVNulQiAsB1OnHo6q0XQRpKtRgZKDV-JODa8Z03YiS5P3c_Xp1pYs6BcoTn9aY4nDG4qGmgHu5-D-3QExDBJvEPfgQ9yHNN7XacuM5z4dzVFZ0oAWL65h1sCz-VVot2GLXEGUIz5mBvJGQxEoXK90mnezmOluOnlqsaAcTN78G6acIa2Id7EwiEneakl48xhjoMYu0Ku8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دفتر شاهزاده رضا پهلوی:
🔴
‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی شاهزاده رضا پهلوی، تصویری نادرست و گمراه‌کننده از اظهارات ایشان ارائه کرده است. تیتر و متن این پست، با اتکا به نقل‌قول‌هایی ناقص که پیش‌تر نیز توسط رسانه‌ها و حساب‌های وابسته به جمهوری اسلامی برای تحریف سخنان ایشان بازنشر شده بود، به‌گونه‌ای تنظیم شده که به مخاطب این برداشت نادرست را القا می‌کند که شاهزاده رضا پهلوی آغاز جنگ یا تصمیم به حمله را به سفر خود به اسرائیل نسبت داده‌اند. برداشتی که هیچ نسبتی با محتوای کامل گفت‌وگو ندارد.
🔴
آنچه شاهزاده رضا پهلوی تصریح کرده‌اند، این است که سفر ایشان به اسرائیل، در کنار تلاش‌های گسترده میلیون‌ها ایرانی، به روشن‌تر شدن این واقعیت برای افکار عمومی جهان کمک کرد که مردم ایران دشمن جهان آزاد نیستند، و از این رو دنیا در برخورد با جمهوری اسلامی باید حساب مردم ایران را از این رژیم جدا کند. اینکه مسئول اصلی بحران، جنگ و بی‌ثباتی در ایران و منطقه، جمهوری اسلامی است. ایشان همچنین بارها تأکید کرده‌اند که هدفشان پیروزی مبارزه ملت ایران با کمترین هزینه انسانی ممکن است. چنان‌که در همین گفت‌وگو نیز تصریح کردند: «تمام هدف من این است که این مبارزه با کمترین تلفات جانی به نتیجه برسد… هر انسانی که جانش را از دست بدهد برای من واقعاً دردناک است.»
🔴
این‌گونه رفتارهای غیرحرفه‌ای و تحریف‌های آشکار از سوی بی‌بی‌سی فارسی در حالی صورت می‌گیرد که چندی پیش، مدیرعامل کل بنگاه رسانه‌ای بی‌بی‌سی و رئیس بخش خبر این سازمان به دلیل رسواییِ دستکاری، جرح‌وتعدیل و ادیت مغرضانه سخنان و مصاحبه‌ها ناچار به استعفا شدند. از رسانه‌ای که هزینه آن از مالیات شهروندان بریتانیایی تأمین می‌شود و با وجود ادعای راستی‌آزمایی، به دلیل نقض مکرر استانداردهای بی‌طرفی با بحران جدی اعتبار مواجه است، انتظار می‌رود فوراً نسبت به اصلاح این گزارش مغرضانه اقدام کرده و سخنان شاهزاده رضا پهلوی را به طور دقیق و امانت‌دارانه منعکس نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67339" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67338">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=OJEdFXMwlOSCdgDYH2mvqqM418D4WUs8YstXSjri2A9kycgkYgHHmcUtHsYcYKUtRGKuYraQcVLwIapX7pIdro2JsGx33ZZlzsbXqb3wxVd_YiV0lUlYJavt5focXmKZNAGfNJq7LsC-hH6Ii7liXxgdl36JBterh-OxYXIHyh99dwEegy8xgPU-DVlf-TkuBfaZIJedJGcHtj6XdTsbdWeCeOFvNyhREwwrkw_DJA4WOwe5EvJPNoxVGSp4vIcCPxWw0cOh53-nwExohN3cOa6f4e8kUnWe7XcMc-PV3wG2zyLVoTTS6KIhvcm-IJYQVWNU2sc0JiTf9nE1AKfsng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=OJEdFXMwlOSCdgDYH2mvqqM418D4WUs8YstXSjri2A9kycgkYgHHmcUtHsYcYKUtRGKuYraQcVLwIapX7pIdro2JsGx33ZZlzsbXqb3wxVd_YiV0lUlYJavt5focXmKZNAGfNJq7LsC-hH6Ii7liXxgdl36JBterh-OxYXIHyh99dwEegy8xgPU-DVlf-TkuBfaZIJedJGcHtj6XdTsbdWeCeOFvNyhREwwrkw_DJA4WOwe5EvJPNoxVGSp4vIcCPxWw0cOh53-nwExohN3cOa6f4e8kUnWe7XcMc-PV3wG2zyLVoTTS6KIhvcm-IJYQVWNU2sc0JiTf9nE1AKfsng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزرگترین آتش بازی تاریخ آمریکا در واشنگتن دی سی به مناسبت ۴ جولای روز استقلال آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67338" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67337">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JL2Lozg2P8U5q0SmdXoICm9DNwJKW8cyaLkogJtOl1kUpyz_s2Kqttae0jCdycOafCoNfldEnuYK6yr26YTKX5_QaEKbDNgZMUIsYjja9LXiWJInQYiswyaP-XJ3aUy83JO8F4ptOV6t98M3aKiUNNaP-seFD8dRF2gZupR-RXo-mGPt2hrzIo_3vgtDqVLqH3QaroMIJvho4LURQZLBL6KT6qe_z2hxg6Qe4HKDPCSG-RSxTiuCTMHBBesf1nQ1CrxhuYILFOwnCJ4rEKfzKNthELZswTl13RnrOWHtmGPxAdM8Xkkb7Q_PXSbQsr5bWcgR73hvLF-bFNtew7-I2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67337" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67336">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=QDWo4S-NynOM96S2z0pPMpZlcQPb-pSh_zLYqjoW9UKn4NpOQ8Hb8quNZGsMBgF6AbqCLCsReRTcoaKuydizHZ7uavgrEA6-RFtfkyww5Ak7RUTBNrKsjWr7o5bKAgb-GA7AWTvOfqZjAMZP-QVs0diWcaFqxzMIGtG3xWbxUmpmXHI97tLBrw2YuxGc3i_Gl9Gi0DPG-oPcntHPQzZD9RlCDKcO7JMTM1TnlKCHqwxB6BwR-uVnz55a4n1v34j7Bk_6kePhQfEtXxcrETaoiNYJDLV5he7oW_nRgaGK5uBQ8aaOnt7xkNhAiDe6JPAUI4FV6_ifCgoIBSnpisXssA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=QDWo4S-NynOM96S2z0pPMpZlcQPb-pSh_zLYqjoW9UKn4NpOQ8Hb8quNZGsMBgF6AbqCLCsReRTcoaKuydizHZ7uavgrEA6-RFtfkyww5Ak7RUTBNrKsjWr7o5bKAgb-GA7AWTvOfqZjAMZP-QVs0diWcaFqxzMIGtG3xWbxUmpmXHI97tLBrw2YuxGc3i_Gl9Gi0DPG-oPcntHPQzZD9RlCDKcO7JMTM1TnlKCHqwxB6BwR-uVnz55a4n1v34j7Bk_6kePhQfEtXxcrETaoiNYJDLV5he7oW_nRgaGK5uBQ8aaOnt7xkNhAiDe6JPAUI4FV6_ifCgoIBSnpisXssA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اگه اهل دعواهای خیابونی هستی، این ویدیو از استاد طِقه زنی رو تا آخر ببین تا به امید خدا پیروز میدان نبرد بشی؛
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67336" target="_blank">📅 16:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67335">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67335" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67335" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67334">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67334" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67333">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsVBX5-Ut2klaweo-9msgjC_F66qm2INrHtDK4fDDStskiRcNWltTZb3NR0ZgxL3fQY0FcRk18F4WUNprqjexUVgcQ_8nuGA67G4gHJEcjLPILnrzM2obVqIa0JI3x1KTEePd_ct26oOrto-QeFMd-svnBRWjJEVclQj52iT01RwnP2kkVC329WnZzvZo-lIUhsCP8Ah-_UJKxvbMsfdVoLgLyqtN26Tjg1WRV8QbtLOeoeCzgVne4Esaqax28b2kBw5ACvXveDCbdbNMt0ku9iFaRsHy0SkBjLMw3nVc7R5DbDRDfiT-aHXDyvZcmaRfKJm8hCvG5U0EJra2PFGmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا کامیون حمل جنازه علی خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67333" target="_blank">📅 16:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67332">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJKg09tW8cYW7DACISvidq6Rkc119MCST-KGFjk9YRZdvw7PFmmqM-e8IFjd-ZdFTB9iVRoEk0Nmae00nVcKwnZcLoGwecHZOQw64usMWRt2YaPRmb5vlLA-Q3tSfvgVwd3ChfKlnUULk8exxYid5IY5v6UMLI8DB-pw1NrpJBgms-kf7S3JVP1ybwiNyLqYRjIsYatK44e66BN4m4jiWjbFuOnikANOkogVbqhtDljwYbIQ1AqqQPioiLXRbJBRccKNXH-i8H-O3NuQaWErT4fEv3pziu00TRX-Rcl1xr6_bk8LKTT7kdRMXJQoLaZczjH7kmB9D5kX8f0yzNCUsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد اکرمی‌نیا سخنگوی ارتش:
«هرگونه اشتباهی از سوی دشمن، با پاسخ قاطع نیروهای مسلح ایران مواجه خواهد شد. ما بارها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توانمندی‌های رزمی خود بهره می‌بریم. ما حتی یک لحظه را هم هدر نمی‌دهیم و تمرکز خود را از این مأموریت برنمی‌داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67332" target="_blank">📅 15:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67331">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو در جلسه دولت:
شنیدم در رسانه‌ها گفته شده که رئیس‌جمهور ترامپ خواسته علیه تونل‌های تروریستی در لبنان اقدامی انجام نشود. این یک افسانه و خبر جعلی است.
او حتی یک کلمه هم در این باره به من نگفت و من هم از او چیزی نپرسیدم. ما بر اساس ملاحظات و تصمیمات خودمان عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67331" target="_blank">📅 15:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67330">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_tt0aENCyXi9x1sWGmEYwqqwDuhFxcxUEVWGObrOW_ycckfNt_WMm-xyx4xMZDXHiBK6KBtrthS_WFZmRqS3vvg2jBnciMK22xnMyADkW2UAQRn1siePmX6jYcmxT2Nte9HFDHZ8G48ib5Wl2lAns1Eh6RZPWFGY27-zFbMlS8X6ib5D081PnILduz8pSiuYrrbvO8lSBYeNcpO0WaIN7gopwKgiHyq3OoCV_v4GP1-yoUvEjEr0EReolOM-R-aqXisSEMySNfgMtmSX6gQ8JmghVoPKeUWJLlx3ibtHB2nn5bmjoSuri37a6Ag8xuBIK3lfB4cTGWT2IbUXdDf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویر ترامپ در مراسم وداع با جنازه علی خامنه‌ای که روش نوشته شده:
خواهیم دید چه می شود
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67330" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67329">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTRcTGjzIuLMAywKdccx6v9e_o8DXNnUNIaF4ctpc-ukXWt4ltnhMBUw0_OWf-SqTUWpNJYtz0PaiLVEJkCTLI-rLThnYt0EKXjUoOfVOkr-5ZKZI4UmWYgtsGd6ZjC9JIm6O98pKheif-zfFj0hPZY63XfQ8daAkUB2JGqUR-H4RRLIb6HusZcVw5DGaSFzqm3ih1ytcu6251xhoKgLHHopavYDfqT-ZrJJW4xuWA_pUysq2FnA4DGJOnUmITDP-r4dYeOt-MUpULUG4ZM5LfHZ4Mm-5Rz2Sl4GsOz5iEh0wTlsI86FyGIl4w8LHfQE5brBMmOjh0NdTP53KpfauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
بهرام که گور میگرفتی همه عمر
دیدی که چگونه گور بهرام گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67329" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67328">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=cUAX-tu1KxoTJDXhSPFdz9DsEYI8JNvRGlfN5BCkI5FgELt-bBRyh-irABP-ndso2Fc042UMrBeraAJOxxR121OvIxeoZnD_J5YF1FRuDJZ3h4XeXkIOblu5CDJ5-zspqBeBls4S2kBIK2nFafurKblCd3vO-W-rTGhmRP6dXx3DYx2nnkO8ISxhTXeYvBPfEJZhKdndjcW4pQLTnvCZIPQ2wCoEfSpybqS3-9K7hxme-Dk7NytO2EDtiGR7xEvDMKoqbP8SXlAT7cOifiGTfLBapIZHJY47r0R5_DzV19wV84fwpD2q7CQKygUMJp4u335Vuj4etzFVwb9mjXi-Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=cUAX-tu1KxoTJDXhSPFdz9DsEYI8JNvRGlfN5BCkI5FgELt-bBRyh-irABP-ndso2Fc042UMrBeraAJOxxR121OvIxeoZnD_J5YF1FRuDJZ3h4XeXkIOblu5CDJ5-zspqBeBls4S2kBIK2nFafurKblCd3vO-W-rTGhmRP6dXx3DYx2nnkO8ISxhTXeYvBPfEJZhKdndjcW4pQLTnvCZIPQ2wCoEfSpybqS3-9K7hxme-Dk7NytO2EDtiGR7xEvDMKoqbP8SXlAT7cOifiGTfLBapIZHJY47r0R5_DzV19wV84fwpD2q7CQKygUMJp4u335Vuj4etzFVwb9mjXi-Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این بزرگوار که قبلا گفته بود بخاطر یه تیکه نون به سگ دادم اومده داره ترامپو تهدید میکنه میگه بیا کوت عبدالله ببین چیکارت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67328" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67327">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67327" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67326">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=pkmUfszdaEGTXhZZTQrc6qlRpp03X4wHjCdEJEDtExCO2jvWh4MGqezLo4At6zcag6PxMDFqtkpQYbFO3HzmWYvObvin75zullg4i-eiY1vzCx_l7j2Iz9Ijl-vZFJtqsa8XxmVmlyZFspq3MYcfruBOwrF5p-3DNj_N2hKHTifHmBMMSIs7n696l64AB2nD5wT-uJfCVS6PTGYkmNr93sQWeMnPtxA_iixSyaaop0FBo529CZ66zaw7QaCusPzs_zwVQiBEZ3plfgvDfo0sAZrnwKk5T5wKKzC9Cy37LLynnggNx7--HaBJJGWSLxrxQ8zLeG102YQLiE58RDqJxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=pkmUfszdaEGTXhZZTQrc6qlRpp03X4wHjCdEJEDtExCO2jvWh4MGqezLo4At6zcag6PxMDFqtkpQYbFO3HzmWYvObvin75zullg4i-eiY1vzCx_l7j2Iz9Ijl-vZFJtqsa8XxmVmlyZFspq3MYcfruBOwrF5p-3DNj_N2hKHTifHmBMMSIs7n696l64AB2nD5wT-uJfCVS6PTGYkmNr93sQWeMnPtxA_iixSyaaop0FBo529CZ66zaw7QaCusPzs_zwVQiBEZ3plfgvDfo0sAZrnwKk5T5wKKzC9Cy37LLynnggNx7--HaBJJGWSLxrxQ8zLeG102YQLiE58RDqJxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمهوری اسلامی پس از ۴۷ سال در مهم‌ترین رژه‌ی خود حتی به‌اندازه‌ی بند پوتین‌های ارتش شاهنشاهی هم نظم نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67326" target="_blank">📅 12:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67325">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6amnGzsMRlFNFLh6m88hKl_8GNGxQimNqJuOU-FJdSYSG1_LdpPgUORoEov46RoCJC9roKrVSmxlRNOLYsqJtxwactkkATx4U5v6xP4ME668Q8CjeoAkenlNhGwBytCYsvVldvw0hpFeD7ZcaR1m_rD6sjj4hBNTkT3Q69YGzod37lk1cD_rpc4O-XKk5YO72h7-Ai7bQ8EzLE30y8KtIsGfJBhKbT61sS0ojN0tpLI8gCuEb3jq-TF8fNcNBsHDT2W3zFNAFtLeP6Qwjapt4YC_OA3vLM6NlA1EiQS19yY6QO0wMeEHEPChZSaNFFY6mLnCtd5lph8HfEYiviOIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هرمزلتر:
🔴
نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67325" target="_blank">📅 12:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67323">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnT24ydqRdOpbk8YI1naX02n5RipSmDuDPHYzlqWzSKwzuIcckQriZUZ4IGiYapbIMc8LMSPH2NHYxKDzM5s8LR5KgNc8WQ0uWHGxHcRGiYC5d_xrkQNFAlR9bLa6wyck_fbtEAfa8XDhYbn1onauvWZEVxGzvqKRn_kMdm5-vFvYgZ7UmtDmbQXg93z_T-AxJBNiDoKvaXPa2DOWnDm741Nxqh-o8SuRGnK1uaD1yAkz021qKtNRrmWbRncGyOQKFMZJ0RraMJ5otqLL20q_ukcltxpzUrqpuFfFRVFoQgKOTnWhDIjiwHrWKwpgun4WTdKLw9alSsIMHFg_0DtPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=mhxUQZYeVMF5YtUSchgpzb_n-RA4hgFg5wvgsyUr2AnReiJneIHaI9UgN-afv86i8x6PedwyOqAW-wqDL3Du2Do-K5ymKmtGNgpVFBQkrRV-1O_sikEZupZY9RuvS8XHPzfmkP83Hj2tmCmjzEVnyEQqOTnMyine8lvVcTQy0OZFuh0nfLQfQ5X9RhRObSK6hEiH9GdWvQrBDeNRAybsW92HQIcTjV0BL1MAbkicUXhHV199mW6IRZdneElUjIEqXX5CGjxYOAfdoNedIiLdgPE6NszSQ6tS1lG7iRa_ZO0aaqvbsnVMwbQRkSG3xAFIQ1hzhF1yc61YUbbx8VGjRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=mhxUQZYeVMF5YtUSchgpzb_n-RA4hgFg5wvgsyUr2AnReiJneIHaI9UgN-afv86i8x6PedwyOqAW-wqDL3Du2Do-K5ymKmtGNgpVFBQkrRV-1O_sikEZupZY9RuvS8XHPzfmkP83Hj2tmCmjzEVnyEQqOTnMyine8lvVcTQy0OZFuh0nfLQfQ5X9RhRObSK6hEiH9GdWvQrBDeNRAybsW92HQIcTjV0BL1MAbkicUXhHV199mW6IRZdneElUjIEqXX5CGjxYOAfdoNedIiLdgPE6NszSQ6tS1lG7iRa_ZO0aaqvbsnVMwbQRkSG3xAFIQ1hzhF1yc61YUbbx8VGjRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بعد از چهار ماه همچنان عامل این جنایت و قاتل فرزندان ایران چال نشده و اجازه چال کردنش رو از قاتلش گرفتن!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=Rzsux5EjXCEaeO6bjNYEaS-m0UQG_QwWLOYwRR3_91pfRpaQl-1iqb4lkrG1Z-D1xvxEa0DlQW1h88BAsR8RMhMjpZk3BnwTDXIt8xGPXSKlzG6N23GCSx1FzBhkeEi5OZHoUaEtV5d_i4nmS8FPF13MyrdSzV4LfFhPZY75wS5vpfMR8miVVq8HoI-sL828PKGZXy0vx-z7xLekDerSr2IPHy9IR7MrzpyWHFvi3Yyhiife-gxL76KeIAYxmP3uaFuuoAR9Az-vMct9Wwp5E8x-QMAO4Tbb5x4boZ1lJnb9mkRyoQN3Hsdo757nmMnSAAXzSrZR_CpN8zQ3iOth0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=Rzsux5EjXCEaeO6bjNYEaS-m0UQG_QwWLOYwRR3_91pfRpaQl-1iqb4lkrG1Z-D1xvxEa0DlQW1h88BAsR8RMhMjpZk3BnwTDXIt8xGPXSKlzG6N23GCSx1FzBhkeEi5OZHoUaEtV5d_i4nmS8FPF13MyrdSzV4LfFhPZY75wS5vpfMR8miVVq8HoI-sL828PKGZXy0vx-z7xLekDerSr2IPHy9IR7MrzpyWHFvi3Yyhiife-gxL76KeIAYxmP3uaFuuoAR9Az-vMct9Wwp5E8x-QMAO4Tbb5x4boZ1lJnb9mkRyoQN3Hsdo757nmMnSAAXzSrZR_CpN8zQ3iOth0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رسولی  مداح بیت رهبری میگه برای خون‌خواهی اومدیم؛
شما هنوز خونخواهی سلیمانی و... رو نگرفتید بعد میخواید اینو بگیرید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=gRgdB3NaaCdRVZMWYPqf5PMscIOI57EET8soxZJeMbzieGPLaJFgYWRYGtZHrYFIhIefj5meF0ACVMtoirlnHGTF8DkLtOiaSQjsCKNBHBJ-N-z3Gyav21O45kgkmUskHbbOGOOWSeZDNG6WbbQfUxKhaQbLd_ptyFC5FMHdvFKL3EVk79EPmcldmjAIE7I_Fe-sHMsVsViV4b6c2JjkTCX77QZeb5-uOqEKyMmshM9s5owXaGAHPLNoABTXqLNfMq7iawyKFrXAL1_S8RuN_d31G9eB9k__6Rndjurh9WxEDAKJoyyeZn3VNJKJTRlp9R1h32PWtg0QmGEpHdnEfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=gRgdB3NaaCdRVZMWYPqf5PMscIOI57EET8soxZJeMbzieGPLaJFgYWRYGtZHrYFIhIefj5meF0ACVMtoirlnHGTF8DkLtOiaSQjsCKNBHBJ-N-z3Gyav21O45kgkmUskHbbOGOOWSeZDNG6WbbQfUxKhaQbLd_ptyFC5FMHdvFKL3EVk79EPmcldmjAIE7I_Fe-sHMsVsViV4b6c2JjkTCX77QZeb5-uOqEKyMmshM9s5owXaGAHPLNoABTXqLNfMq7iawyKFrXAL1_S8RuN_d31G9eB9k__6Rndjurh9WxEDAKJoyyeZn3VNJKJTRlp9R1h32PWtg0QmGEpHdnEfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف یه 20-30 سالی هست درحال گریه کردنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67320">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=TTK8sBi43cTUWSGDFhieoFQhlLnrXT0H57gSU5atWFmQiFy5YH1x4ygNgU-GjSOifAXjU0cNcvWdDsY2h9uDudcKh372eU9MbGsdq4hhGW09gb_q-AsX7E-GeziSL8Orn9DrxHKlG_BNFYp8zQW7pkga1V9xsjuTRJag2dVKY3ZUX_60k2mmLjAqoCVcupgFH298IxvRxlReTVfAwAuMMHzlY2IEgSsyO8w4DHyO1-nfIUzwPvl0tuAnI-bGzwleksifaTGDz74GwEU_jSLVi9FGEMgRgyknvYJxLcLNzPU926F81kjmjgkaD5bg6DYN4DXz0DmqbTO4EuTLRFvk9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=TTK8sBi43cTUWSGDFhieoFQhlLnrXT0H57gSU5atWFmQiFy5YH1x4ygNgU-GjSOifAXjU0cNcvWdDsY2h9uDudcKh372eU9MbGsdq4hhGW09gb_q-AsX7E-GeziSL8Orn9DrxHKlG_BNFYp8zQW7pkga1V9xsjuTRJag2dVKY3ZUX_60k2mmLjAqoCVcupgFH298IxvRxlReTVfAwAuMMHzlY2IEgSsyO8w4DHyO1-nfIUzwPvl0tuAnI-bGzwleksifaTGDz74GwEU_jSLVi9FGEMgRgyknvYJxLcLNzPU926F81kjmjgkaD5bg6DYN4DXz0DmqbTO4EuTLRFvk9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان مراسم افتتاحیه مسابقات «فولسوم پرو رودئو» در ایالت کالیفرنیای آمریکا، یک چترباز پس از آنکه پرچم همراهش به درختی گیر کرد، تعادل خود را از دست داد و به شکل خطرناکی روی یک چادر سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67320" target="_blank">📅 10:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67319">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=KyGyTdQc_8pk5tVGOH607Azp0t7m6l2KhOrSarhaGcLWF0dSJqMM7K29Zw9bD_C9XrtGGWeFAU2lb9wEAL5_AOdnW0TzDF88sSRllIWGSaofv8nAk4zOvX_T1mtdp7-X2ckdkZx3AfNsaU4HdZL7RvQAIbMnoZa__WyJVNwSP0aDV2F_NnvuXnj6la3Eo7FcTMIoxxy4TAvjZDRtXE-oTcwIdxofqAZRqIr2xHgl45U6VQFvJxmNwdBhX3lDr3pqN_TsYGrHBZFt3l5EC_809tgNO_t1xnlspJQyJ9HLvNr01CW-oDEaeFYrP0hNPiZt8KQWPJ6JBBQHH4rqkAKdsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=KyGyTdQc_8pk5tVGOH607Azp0t7m6l2KhOrSarhaGcLWF0dSJqMM7K29Zw9bD_C9XrtGGWeFAU2lb9wEAL5_AOdnW0TzDF88sSRllIWGSaofv8nAk4zOvX_T1mtdp7-X2ckdkZx3AfNsaU4HdZL7RvQAIbMnoZa__WyJVNwSP0aDV2F_NnvuXnj6la3Eo7FcTMIoxxy4TAvjZDRtXE-oTcwIdxofqAZRqIr2xHgl45U6VQFvJxmNwdBhX3lDr3pqN_TsYGrHBZFt3l5EC_809tgNO_t1xnlspJQyJ9HLvNr01CW-oDEaeFYrP0hNPiZt8KQWPJ6JBBQHH4rqkAKdsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین حضور عمومی مصطفی، میثم و مسعود، سه پسر علی خامنه‌ای، در مراسم تشییع او در مصلای تهران.
مجتبی خامنه‌ای، جانشین علی خامنه‌ای، اما همچنان در انظار عمومی ظاهر نشده و در این مراسم غایب بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67319" target="_blank">📅 09:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67318">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=E5KYX8RBnNTeZyh2d-1nK0_ZU5lkjlU8pqXt-8emFpihm8ZYIbA1U_qbpySdM-SKVR3K8GZzJZMFgfYx8meyOw2OUqqo5gMPQGQ9-VmUin6DwJSwV8w7_jlO7SB9GRGbcyx7kd63yc1hkfxL2CjHLJ9aJ9RE9qQ3FmbcGdHvl_Fn4bRze1l7qVPWl38B2xPqPAXfIL_CAnWvWBQ48VNV68SgVrOa9EgpGpMnPkdxrj2dnr8VlnZ5YNZJNxFMCsJ_pu9mxoxhEMh8cK8Aid96_dTt0atVegQtM4xQkOVYw98HE3WwZfT4Dw8dBOYhGY9hyXi9E61UbUyWFn2N0KFeAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=E5KYX8RBnNTeZyh2d-1nK0_ZU5lkjlU8pqXt-8emFpihm8ZYIbA1U_qbpySdM-SKVR3K8GZzJZMFgfYx8meyOw2OUqqo5gMPQGQ9-VmUin6DwJSwV8w7_jlO7SB9GRGbcyx7kd63yc1hkfxL2CjHLJ9aJ9RE9qQ3FmbcGdHvl_Fn4bRze1l7qVPWl38B2xPqPAXfIL_CAnWvWBQ48VNV68SgVrOa9EgpGpMnPkdxrj2dnr8VlnZ5YNZJNxFMCsJ_pu9mxoxhEMh8cK8Aid96_dTt0atVegQtM4xQkOVYw98HE3WwZfT4Dw8dBOYhGY9hyXi9E61UbUyWFn2N0KFeAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زاکانی و برخی از مسئولین تو حاشیه مراسم رفتن چلوکباب خوردن، عرزشیا هم اون بیرون زیر آفتاب، صف وایسادن تا تخم مرغ آب پز بخورن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67318" target="_blank">📅 09:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67317">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Womj5L2z4y-5a4KioKuLQKZvSQyXObJEVgxf8k5MrxVatwLHVyGQI4w_ecFrOsBYaOXuDwM9ASB-WQwHfScV9tZeOdbhwxzYX9b3114Rv1O11HZt8vdla5-9Ibm-vu3QlFACABkJ-j1Gkl1wdKtvYnos6BcNAEqEik-oC4v8Gy6S5IVHUYDjnXfmKLDsAfzJMgk5ImGFytynqVU2RdTcliz9Kj8VG4tJSA0ElH5YpyAZPpGrdORUQn7Wy_Vw8rHUVgQ9JBGMCKlt3_OUnOaBMr_TFmUoodeALh2RCls1TniDqSYobvceUYBjU_HGkMM_jbiUQgIzGfjrni-KMrS4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
8فروند جنگنده A-10 Warthog در پایگاه هوایی موفق سلطی اردن مستقر شده‌اند.
🔴
این جنگنده ها برای پشتیبانی عملیات زمینی استفاده میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67317" target="_blank">📅 09:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67316">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67316" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67315">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YlVQ5oIIHBN3Y11mdO-nfBybPf4fpXUBfw6UBUr6FN9SPF8nRamOHgzI0kQ7ANYiK-pmsEn2LLyXjTY8iBwVGHIKxIBQt_8_HTM--jRl47mSCdfJXLRr3SOYMQIR7i-7HVFkWyav4wAKF2Mk6RIX0gm9u-EYciAGGw9IFTxtg7Zy1brAIkt54dF6lFk9dHT45toYEVj60O2JwAe3acGNaIVDBVmDh-GIesP_dkImbLknMRK2hpLsIUa5r6pZywFA1LCJRbPYMcruNQKrFHEVgJPTv5hBdUNh5xmtYhk9Xp32ceiTSYXJB-7Nv3_TPGZ14d1MruKGKiPSkCGujI7LOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67315" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67314">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV2Jjw-oWhh54tABLKUOnCcHDmJvncu6WhQGDz2l-arAWQQFL1SBeKd7kgx6rnWCgAAEOcuY2aN4w2lri-kafgKfwnp0I-B01e5cR1Oj2zgHkZO0MvTwDf_rVlZgJy45SA1CK0JKpiZgC9c3XBN7sZfjtfSF39i79uVHdHSWbyL0EzcdkSQ4YZtHHPSg41CujW0Gpd3R7JklIEDIfCRetEI0_w8ERHuMEsBeg1zAXndoCtH6hKUtr4wM7Fhc8DYVQtHILI7t_Zkt9O9TJ60T8-r9YsyCM-Xd9YPDHN-E0V-25-iQVdxJDbtjRGswCCJFD2WT9HX4Me8AHWxRzl1o4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
ولادیمیر پوتین، رئیس‌جمهور روسیه، با دونالد ترامپ تماس گرفت و دویست و پنجاهمین سالگرد استقلال ایالات متحده را به او تبریک گفت. کرملین اعلام کرد که این گفتگو یک ساعت و نیم به طول انجامید. پوتین از ترامپ برای سفر به روسیه دعوت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67314" target="_blank">📅 02:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67313">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=YFy3WdF1T_o74G1Ytj9UAT6V-3AfKo1dVdA2FhemCT8fxkreApQkQA8hxFHOnmTyLHE82KO04jJh5h7577Sd8lrJDjYPCwRkPXjOimnChJlnSBqTf5nJM3qKNYuzngBY8vGJcZpkk6b7q5Jj3WB7g1xOON0qtZSmlDzWhQBAiTr-1RE8nf4jJk2coRnn9e5TMCKU6osBzKVA3yrhCEgwM7H1P_mCKIbVkXgx2lBqEmrIiV3XsnFcn1Pa4OGhKyXfqkM3uJHMthRSDltkp4nlyGsMqXLIQw9efzgOO2r6KXRPfzBhh2fTxIqdvKE5vrj-qDUFtD4GJVKOHaLq8xWs4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=YFy3WdF1T_o74G1Ytj9UAT6V-3AfKo1dVdA2FhemCT8fxkreApQkQA8hxFHOnmTyLHE82KO04jJh5h7577Sd8lrJDjYPCwRkPXjOimnChJlnSBqTf5nJM3qKNYuzngBY8vGJcZpkk6b7q5Jj3WB7g1xOON0qtZSmlDzWhQBAiTr-1RE8nf4jJk2coRnn9e5TMCKU6osBzKVA3yrhCEgwM7H1P_mCKIbVkXgx2lBqEmrIiV3XsnFcn1Pa4OGhKyXfqkM3uJHMthRSDltkp4nlyGsMqXLIQw9efzgOO2r6KXRPfzBhh2fTxIqdvKE5vrj-qDUFtD4GJVKOHaLq8xWs4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمعیت هموطنانمون در تجمع چند ماه پیش تورنتو رو ببینید و با جمعیتی که در مراسم تشییع جنازه علی خامنه‌ای اومدن مقایسه کنید
🔴
فرقش میدونید چیه؟ ۸۰ درصد جمعیت در مراسم خامنه ای اصلا ایرانی نیستند. کلی لبنانی عراقی یمنی و فاطمیون افغانی گرسنه رو با پول و... آوردن بازهم نتونستن مصلی رو پر کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67313" target="_blank">📅 01:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67312">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0psLmz7uTAFI98_7nu88KNvviM9L8hiF4XOmYf4gJLC2hTLLn7D9QlM84jiJCxYZjE3HrbnWYNzvBpm2Gg_ZXemr2nsEup8GIp6kRogqkouVg_I_PiV2Ms3T4JT6PIh-tDpSj-C3RoYJ0_riusjCY3WMmS7QbMjiPPaxCYXa_90QKD5SEovUboeDMGqF0E_4NGMsoN0SUZ_d4LjKAHj4R-2BSvg0VZZPdluubwCQjvqV-_encoHqwEUVwVIlSaVARRDwk5iBjt8vMH2yGH-yXMUWtPY7CuLfbu_YPoS8XqlTkTjaKhbS8w17g_ocL1DVLf77aox7nuyuPyui3g9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروهای ارتش اسرائیل در حال عملیات در منطقه حداتا در جنوب لبنان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67312" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67311">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=hHArChNnggQ7aj1V2YmQLvWh2aBtWDlhv6YdmaPwTCE15PPEveSL1NBuC1Vi9pn3wpS28ZOIg4KZ69c1ecIxydfXg3ooruMOVz77YO1s9fX7GRJOOoJHxywHvgz1aheVWzHLaphuPNydmV3572Jv7-uN1zraax-qqq5VmvYtgDzngbhYtDtrm6FGBiYFXUo0PoMIl6Nj04oFrsmB6_OhQCz-smmg4gaYpYuiN0y8YzTnlAfRflsMk-z7Zwgk3F1MCsemFptSyzvLchlIFcJKqGfVyADVHez_WSammSyxzW4OR_EZA8I_q8E65MNb375qIXHDwtWNT1Ciim7ZI3CVTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=hHArChNnggQ7aj1V2YmQLvWh2aBtWDlhv6YdmaPwTCE15PPEveSL1NBuC1Vi9pn3wpS28ZOIg4KZ69c1ecIxydfXg3ooruMOVz77YO1s9fX7GRJOOoJHxywHvgz1aheVWzHLaphuPNydmV3572Jv7-uN1zraax-qqq5VmvYtgDzngbhYtDtrm6FGBiYFXUo0PoMIl6Nj04oFrsmB6_OhQCz-smmg4gaYpYuiN0y8YzTnlAfRflsMk-z7Zwgk3F1MCsemFptSyzvLchlIFcJKqGfVyADVHez_WSammSyxzW4OR_EZA8I_q8E65MNb375qIXHDwtWNT1Ciim7ZI3CVTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای،‌ 3 بهمن 1403:
ده‌ها متوهم به درک واصل شده‌اند. من به شما عرض می‌کنم به فضل الهی این تجربه تکرار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67311" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67310">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67310" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67309">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c6-MBAVwIGCEDYO9CggULmy9VhtOehM0Bbg3SewZ4LNLvS-E7rJnZfEUL3vmYFZ80ng2WkO9bqcBzeC97LS1O5bFb1iF61IsekB9OFKw-KNLiYAYMJiTVDOZHUzYknEzIP0yTZaaeY8WEjPkjvIa2QwIUfqY36Z6qzNEsZoYjrhdcIrEwOgkPBR4o3CM_ObN_S-DNtwKxNT0oWvRhVqOUuSzpHCIFDGEXSrTIrzC44t_W7CK5qrgsxzhfQieANQ1xuJesEWMirD9QwkPmxtPz_ZHxe8ATCls7Sp-Cf8C1pLUQzodnKPBEc2l7XJQprcpFjpba2uScGakygT5dGVl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67309" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67308">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=hB3eu8xueYeIuWYKlN1mt-fbgteolcVTLu29qxGBSROM-CRmRiItw6XQ-rGLuI5qscQq-5gK9DYnSbrTQLXJGebzQBfsM6HX5VpzpvzzWhfD8jZPmG-sPQGTjadq1culHuEOUb19gWa81gKUqj6eVPpIqHn2AAZxGrrQhB0jzgowVCZzxm6pKZ74wDY8rnqBjDXhPVzJ9EDtkPLwWgTBN-z0EpTc_SyvIMWOwqcGUcEGTCr8ZOie_SaPPHPjSu8XlFDBO6z74Z_x9mc_r9gF1KIkx4wYQBPXXXkEwWHItoib71vy4h0Z3_g-F6lm7XbCjQ3NZ8kxi9yXCJhDY2M7HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=hB3eu8xueYeIuWYKlN1mt-fbgteolcVTLu29qxGBSROM-CRmRiItw6XQ-rGLuI5qscQq-5gK9DYnSbrTQLXJGebzQBfsM6HX5VpzpvzzWhfD8jZPmG-sPQGTjadq1culHuEOUb19gWa81gKUqj6eVPpIqHn2AAZxGrrQhB0jzgowVCZzxm6pKZ74wDY8rnqBjDXhPVzJ9EDtkPLwWgTBN-z0EpTc_SyvIMWOwqcGUcEGTCr8ZOie_SaPPHPjSu8XlFDBO6z74Z_x9mc_r9gF1KIkx4wYQBPXXXkEwWHItoib71vy4h0Z3_g-F6lm7XbCjQ3NZ8kxi9yXCJhDY2M7HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌هایی لو رفته از ابویسانی، معاون وزیر اموزش پرورش حین گفت‌وگو با دانش‌اموزان معترض ؛
دانش آموز:
نه اجازه میدین تشییع رهبرمون شرکت کنیم ، نه اجازه می‌دین پیاده‌روی اربعین شرکت کنیم، چه کار مهمی الان دارین؟
+ ابویسانی :
اربعین بخوره کمرتون!
دانش آموز:
ما می‌خوایم تشییع آقا رو شرکت کنیم.
ابویسانی:
برو بابا تشییع تشییع..
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67308" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67306">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcQ2HyOMqegRpFYUfGtwUvBgIRlbqi-qE16ZgiLB13Aafddh7ne3o9yfU0czE37NY-cqXC0zzamppVNJ5kDJQ0PioZVjgYNEfyUaWr3_nVrD9lgnv-EdOIcQhXSr5s8wWvVyH8defgc0TQnoV0-OcgdIE2WnPqNaV4W0TOhsbkPWjs6m1V5AjJ5Sa0nBD0towwP-521y5_BlEOaxnpzaQrF6QqpS96sPf_HEtTeZJEQSiBAAx2wCHBvvrp49ZANNBi8-bfZoT482K1AcwuJ3h1k6AuQv5PatjmybZ_JJrkCxXaF_Xyy8jnjvpCaSd69QJi5wnyJCCKCEbMCFBa03yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=RngGPwrWQouRjZCe7JdEpgemoT98LRpGHI8IwElzrAyxEWIxKx6MSI1zfu6JYDISuIjcm24_nKa1wy2nwHjTGe_VAb2rYOzCLzrufdXmOqlR1c_CE8Uz-EjGmXBIXxqnADttPxRPMHvox3FcYrvI_WS8fVWiMU474EUzMwQLc_yEuckwSFkY4uSsNhRk8kIN0AVXxJn6WGPJPagE8ecxc5SiW3MTzxgTt4yMcYEQmpUKLTIlo3POodNrDXNCa3j8R-Al5Yquqqj9pZH4gNkYwmgn8yGlK1aWHYJf4VobjNdguRM-hTBPUekNMKy1eXpayJm0E32E2NRGghhxl5QsQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=RngGPwrWQouRjZCe7JdEpgemoT98LRpGHI8IwElzrAyxEWIxKx6MSI1zfu6JYDISuIjcm24_nKa1wy2nwHjTGe_VAb2rYOzCLzrufdXmOqlR1c_CE8Uz-EjGmXBIXxqnADttPxRPMHvox3FcYrvI_WS8fVWiMU474EUzMwQLc_yEuckwSFkY4uSsNhRk8kIN0AVXxJn6WGPJPagE8ecxc5SiW3MTzxgTt4yMcYEQmpUKLTIlo3POodNrDXNCa3j8R-Al5Yquqqj9pZH4gNkYwmgn8yGlK1aWHYJf4VobjNdguRM-hTBPUekNMKy1eXpayJm0E32E2NRGghhxl5QsQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از مزدوران نیجریه‌ای حالا یک فاطی کماندو از بوسنی و هرزگوین ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67306" target="_blank">📅 23:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67305">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=H8fxMqj2MKRhO_Ccg20J-3xobEuZX9diDjBAWlkm-O3NI0S8r2UadRbQ7cFbe8Q3ztMiWmrejO847lNIgXYQfbCSkBZRwRP8N7FQeQBnvDUgGFYBBMvhJql7kYm7j4Z-qQg2DuLBUxnO5epxWBRqvn5-0dxDeu0qShkF3gbbjre4BaExkVquu0apDZM1NQbRJro-vx3LzSzmc9aw2I3-oqwlK3D363wFefl2mVEKjWL-8fg7Z_hIQuxcxa3Ms6BB5tLZT2t2CzUE2j2RNpsVcZjt76c7khbn2uvAkOyaWeG92b2BBqNIsswoVRMgzlAp0TnVku8b-7VD5sqKHgUTmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=H8fxMqj2MKRhO_Ccg20J-3xobEuZX9diDjBAWlkm-O3NI0S8r2UadRbQ7cFbe8Q3ztMiWmrejO847lNIgXYQfbCSkBZRwRP8N7FQeQBnvDUgGFYBBMvhJql7kYm7j4Z-qQg2DuLBUxnO5epxWBRqvn5-0dxDeu0qShkF3gbbjre4BaExkVquu0apDZM1NQbRJro-vx3LzSzmc9aw2I3-oqwlK3D363wFefl2mVEKjWL-8fg7Z_hIQuxcxa3Ms6BB5tLZT2t2CzUE2j2RNpsVcZjt76c7khbn2uvAkOyaWeG92b2BBqNIsswoVRMgzlAp0TnVku8b-7VD5sqKHgUTmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم خاکسپاری رضاشاه بزرگ در تهران، زمانی که جمعیت تهران فقط ۹۰۰ هزار نفر بود و بیش از ۲۰۰ هزار نفر در مراسم شرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67305" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67303">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j51rehvx5be0gLHwgFc127HNuobQ5zqqrywls_Y9TW0VX5kcb60VSu7gcgbS8q3Qb7xH7ni7CnP1MDb9DnLIDhrNfSqzi8MuOtfc4VW7p5_JNePVP1FMXOJtCRpfpVNAkdvi1KIr25vuiwyagQeMUyuNghJ6OvKhtxZt07xiZQf2wsHTUZFalCtxvSW9qUZi702DXcMMh0Vxfa-WeSSGNakfrLVSWDE98vFdPSGjI6DqCJ5gEdX5JUgZ958qK73JkLE_RkONzRyUZH447MptxLCJziJVA1U93Ov_hhVjZibw5X7QWkMOY1kXCVoiC4ltmfRYktCNGQP3Uz-ViRkrTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqJSkTy9Ot1rEevwwUo_FVKJEofmChMsMg2A5FdT76pKklPSD0gDnsoK7QbI0d4s6tdgweWXg05T46Utn9C5FA_JNfO2fC51zrKt-v7wP7UBE5fzNR45i6HWCHnJabGr3s5JgXEQUL-vuhBY6flqZo93nKRPRjFeYl2ZrueGmfZ6MIHYgInz5izV1bqhahqtg19wTilmXEXKfMYrANMxsxWaHcxc-0kSHJKAvFscRLIsnom0ePa0J0_PrGM-iHP6zP-HbApXHNdB_iXeSvSJ8S2dzlCC1QZe5aDCaK5aPD5RFLczV_iAaT1yL-u4kyjW2TCfbaPVXHE2hGAOMLjmAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زمین گرده...
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67303" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67302">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pf4xJgsoFo7ubqMwtnIQtF0PuwKdce_rSEPBf_thcjwl8VMEPKok9-S1g6bXt7HDyGOdHo7fzptHpBsCvL7iG1lTREFrsg3cbCWmrCE6Y_NB3BwHNx-Gfve-BcK1Rx8s9OGWgMhtPRfsnTS63NYmT7JzQRXTXGFeuzL9U-X3rw6maPOWJaRyJxHCHoB1KPd9l5Ubm-Ceg5SCbdSfA1uNIAwRk0q7jr4_4HK4_DUKZja6zbqqLpGKANvGPMqCE8wyH5FytiDAJDzkhGsKvLuw6bM0pJV4Ds7QE86XCENMiRkz-zaCjm8whMJe9nBOPclMNWyNkTRH1GuMRO7yJrNHnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
دو مقام آمریکایی به من گفتند که مسیر جنوبی در تنگه هرمز همچنان فعال است.
یک مقام آمریکایی مدعی شد که اکثر کشتی‌ها با سامانه شناسایی الکترونیکی خاموش تردد می‌کنند تا توسط پلتفرم‌های اطلاعاتیِ «منبع‌باز» (Open-source) رصد نشوند.
این مقام تأیید کرد که ایرانی‌ها تلاش می‌کنند از طریق رادیو VHF برای کشتی‌ها ایجاد ارعاب کنند.
مقام دوم آمریکایی اظهار داشت که سرعت تردد در مسیر جنوبی طی روزهای اخیر افزایش یافته است (حدود ۵۰ کشتی عبور کرده‌اند) و این مسیر همچنان باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67302" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67301">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=Ohgi-mXAEnPpseHgkNy6Q05xIrlYHAJh_YtmC1Wxmm1qRLOMFc1E-084QuqJZl5xLHKj8qjZNKZ2SbN8f7EEOIDeSA2uhAKePG3iwTfbstChZV30CsATY1Hwwpc-HNwwuizIEXK1wMTNRQufnC0IgPZxOeMXOsMqmYuE7nxVQrhKuKVgi_YAu1gf36dr2ezvqwtPNA2AViScQMasMn14aMc1-DiHWNABICUUPjUrtXCVuJ0QxPXuGSHzYzZbGky7Hc3C6ZXLXamlHZij5kxycuwv6Y66zQZKh8sc3kCO1qptanlgYMWt_Gorebwwy-UhpGXPJ77nTLlvdhWMLsyZSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=Ohgi-mXAEnPpseHgkNy6Q05xIrlYHAJh_YtmC1Wxmm1qRLOMFc1E-084QuqJZl5xLHKj8qjZNKZ2SbN8f7EEOIDeSA2uhAKePG3iwTfbstChZV30CsATY1Hwwpc-HNwwuizIEXK1wMTNRQufnC0IgPZxOeMXOsMqmYuE7nxVQrhKuKVgi_YAu1gf36dr2ezvqwtPNA2AViScQMasMn14aMc1-DiHWNABICUUPjUrtXCVuJ0QxPXuGSHzYzZbGky7Hc3C6ZXLXamlHZij5kxycuwv6Y66zQZKh8sc3kCO1qptanlgYMWt_Gorebwwy-UhpGXPJ77nTLlvdhWMLsyZSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم اروپا با دمای نهایت ۳۶ درجه
🆚
مردم خاورمیانه با دمای حداقل ۵۰ درجه
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67301" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67300">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=BbddGt4POUPsSYfxyV_lBhJKndfszHKIYNrZm-7_mbWvE06ykD9SDQDAezhlAuvH8PVWDCVhgUbd22OWFXvLhkQlt3Ikx_ad-nurV7izXAiBeQReoPm4i9eTeDqZmsmXz4dGqRmcPzCp9cRQH3D8HqzkLmQKDvRnmCtGduvNr31x9lVQR8LRJEa-RZrGshCxCoBjLjSilukoEYfRCoqULivB3pOEE015yVvTPd47Qo6RM6t-y8-RSLg2UCWoxcLx89747EM8-A_xMtyHvKvRmlE8ln9JdtfN0HaMorJPOjP9MjqI39qn8zLxLFt5oAwCmPEa8W-dOFHFaVNbq-j_qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=BbddGt4POUPsSYfxyV_lBhJKndfszHKIYNrZm-7_mbWvE06ykD9SDQDAezhlAuvH8PVWDCVhgUbd22OWFXvLhkQlt3Ikx_ad-nurV7izXAiBeQReoPm4i9eTeDqZmsmXz4dGqRmcPzCp9cRQH3D8HqzkLmQKDvRnmCtGduvNr31x9lVQR8LRJEa-RZrGshCxCoBjLjSilukoEYfRCoqULivB3pOEE015yVvTPd47Qo6RM6t-y8-RSLg2UCWoxcLx89747EM8-A_xMtyHvKvRmlE8ln9JdtfN0HaMorJPOjP9MjqI39qn8zLxLFt5oAwCmPEa8W-dOFHFaVNbq-j_qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام نتانیاهو به آمریکا به مناسبت دویست و پنجاهمین سالگرد استقلال:
🔴
«۲۵۰ سال آزادی. ۲۵۰ سال دفاع از آزادی.» او این مناسبت را به عملیات «انتبه» در ۵۰ سال پیش (که در آن برادرش «یونی» حین نجات گروگان‌ها جان باخت) پیوند داد و اظهار داشت که آمریکا و اسرائیل در ارزش‌ها، سرنوشت و مبارزه با مستبدانی که شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» سر می‌دهند، اشتراک دارند. یادآوریِ یک اتحاد مستحکم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67300" target="_blank">📅 22:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uq2kuonqutxjYm7ny0WMbeLWCyabUMvnv7FKi4KcajyjfOj5h9FAafqdh61wj2RPgq9o3Pm0W8HSt650vxwLqKaXR2LHX68TYK_IM94h2WaePPGfvRP28U9MBW7HW0orW3FmYHxOmitWlW8FLdodLwM0BZFOutsskygV3DEkK6vdkvWiqrzdmBYElqQ1qrWfE8HjE5-Axc0SQ0lVh4aCfNxQjGWdmrhraGc4kdf7Y9SUQNRGGhBHuvo0MGpnUpkdxzWwN0AZQaXXqTztpLRtwOq3vnNVm_xhFM2iK9xwVWhZfIDgj_pWi26JBHpwMihyE9d1Bgon6s90UlTM0OxjOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
