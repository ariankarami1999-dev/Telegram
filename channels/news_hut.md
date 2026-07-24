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
<img src="https://cdn4.telesco.pe/file/A2kF9hvfSXZqGgwrgH2TS0L56pP-y0zKMLjrP3hhl4goqUmxHot539CVnglkH-ym1oTteANtC6OyLXvQ8O3DGW8i6o1rU_LohdKMdEmc4FIgWxEb3KiHQFtVcuUtD5mZ0IcDW-3BHopAUaGqTrCURybNAozAJLwQBVYqEkz4Sy4Fl1wmA8mQ_ermW2C-QNFz66gJZnN5ufHUq6qaWtNzvn_NY8GL_KdtRFT2mnW5G_3mDXMrYJQf2TQ9ZOaWjdgFPKrsAGT-MwRnH81aWP1RzoPXBo1OXdjGlJUy0vVRa7RCUto_M6Z1ZkRHn3XWSZWrN8Hj0jOQzn6WIbZLVMje0Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 151K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 15:28:59</div>
<hr>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8y8dSOFhGftEFtB2GkYZJSkSMbSOoffc1yMeKnwrZVB4YC-zx9S6kY4kd48NALGw_ZP4t561nDZeJcBt8kduQ2zt_L5a3DGp8k72cgQ-jjJ_lFLz4-2hpeTXjnONWXxICQiQsdvRLRZrLQ9b9f2w0KHSr6MFfxn5lQb8HeRAIwgZJSAtzAIn--Go-LJjkwOmtCna5gzgt5YDOYx5TW_UfuIeDeHr5TnCPj719EoYmhrCb4wi0sLFngfgSP1Woye5Hz4o7IFjVd1SKStUQLtjQSJ3-pMGHUKQ_YF2qN9gh5U5FOxUVLF_JjKryok0-lukT7uQV9wf-UFaLE-KpHoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HALS0fGIfVd9PhNCGqVVmTXLUQgF3X62dxWrhnLZMq8hM3nWUjPezmmOm775PCof3EYdgt5YbZCzUnzPlajb5pjzBMGf_OYppsZ81yoBvGgqOagrKgf156ZSi100wLnmfSHHGsHRw23TyVm6rtF9ZauHdCTZnKNI6GirJduOVrXwnwcNgEqkcE3AvtHqnSbghQMHSGjOro2Ina88QjaPTpW4hdvqgBXwLYF81tc08bCZ_mBWKKaB6d-u9ptDYevCv9Lp_fppJf9--wSiIIqBPUiDpWd2_KrdoNhIbG9y-QMPunZX48d51S1ieFFD_I-tKeOvnkfu5UCvkS0iAw-E2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRJ7TTGs2Ofl8jong2j-sno1zEHUBkmLj_Gl2EPO-WxYj9RrPG9LOR5ewe0cepztxxUHGHwf-QG0Ba6a329KNdVOkcUMnEGYJhNZnktH5usS7NmgMpJRfSJRkJEw5xY0AXkThUCDk4xSQ0sJZmmBLcW0Dmm7SsB9_9C8ABIjXtyyHjWLtEj1lL1TenIaefrqC4juhpTeAT7URNk8ZqsTqjk4zrh8HFcT-yjzDw61Q_GlJmznveAi6GhtC8EtBLOClaVrmaqFCU1A1YXtn4elZSQMv_ravXg3jDCU5u-I2YIGgqDtPpBsQFWiYurVzbSlxhfyHQX-nr5fHW1vTuY7eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=PoMfqO5j-3kzg8TyBBSTL2kwQ4e5X-v1Du48cFatYAU5__MJ3zPuixctrQlcbLjo01h9F_4Y2DPnRyFfQa4zEl2-ou8e5XiMjnXIo8vppQObRTXC-C5SJhNDex9dqpETmpKceY1N87UudMUT1iT_IOVePJbzTVS4V3O2CHAnz10y332_9RuMLCuXoT275kWAQGSPEagiZZpnjbyPx8taw2NmO7B7pcsIz_u5S2iFyGVGqd2uCZP3ZA3e7v60vgcxMn8xhFbCRmVzOyOQ5FrgdA8Vcl7baU-BHHijK9icMw2xcIe0_fdcvtUNOX8T97buz_nbPvSV9CervjB1NI18vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=PoMfqO5j-3kzg8TyBBSTL2kwQ4e5X-v1Du48cFatYAU5__MJ3zPuixctrQlcbLjo01h9F_4Y2DPnRyFfQa4zEl2-ou8e5XiMjnXIo8vppQObRTXC-C5SJhNDex9dqpETmpKceY1N87UudMUT1iT_IOVePJbzTVS4V3O2CHAnz10y332_9RuMLCuXoT275kWAQGSPEagiZZpnjbyPx8taw2NmO7B7pcsIz_u5S2iFyGVGqd2uCZP3ZA3e7v60vgcxMn8xhFbCRmVzOyOQ5FrgdA8Vcl7baU-BHHijK9icMw2xcIe0_fdcvtUNOX8T97buz_nbPvSV9CervjB1NI18vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1iLxnnGDs6ZsKIbz_j_9RNFnuCt4XLZpfguYvHGiZ248i6qZU_0BonnNqQbMeUiBJYsqpgO5bIzZvTVCnBwlMxXPn_56ogkq2-b8HEvbc0kpOhNsxFtKNohShV5NnRbjVShJASEWE2CnlhldfWBQN26M4AF64mHVaj3dXdz1mXsBkeHwS8bh1GrFMAwiGeFROGSnEarMW_IWTkwcD7Jtkz3gUzSjXiCeVkF-btcXVHZyHgP3DTly7N6lsebQdQcZzLCSm1MCyfkRSBfrN6uiHDrDhXD_GESD2meq8ewDYwBpBHuRmvXprakjsOZVuqQORGLFCrbqlbzAtm9Ldkmlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu2hOnPx64uZ14BlnG_XdAIq6OuRaiFLMJeGDch5BhSLWaEfOfpfQBbmI1tdOiSCXOYWtmOMymi1gYCIEd040oT_XSlRgAnH35tquTTwk3tE7y4dfxiYo__Ff28b7hCyVNjeb_a8EkeB14sRc1euE73lEOX3Lzw_6wZgoc1HTfsyxChWEN_eX7Tp34h1sI_B8BbB7O7d1J2d3NDiVVaI4o3JNUqiTR0l-w6NZ3_bvWOjZL_SEW9s5r-l-RRlr0pimuvY-vBLMEAAzDQtqV3l6UEyBXViiZDw6mZzQeIpbKaOsLyUBfY3gkt5V8I1TFGGkADN1ztD7mai_sJJA58Fxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=c7eBmwzvpDuuvFDzT3GZZ6T9hhmc6aMaBKM_vRQzSpf6GY1fpS50B10v1nieLL1RFPNY7kKxR0fBnB-9A6LqBtK-f3NWzrFlcGXEvn_ZKgLHJ2yEfR_qe5OWRZOrLLFqKI_hfJzgl_Wvcfkl-YQ8_RzyEIno2U-0ZlbezQIG-IlA9gqGy1tJ888r5RXi2p_FOMfBfsXADEBmsJ2xn_GSFdMYDkBxRJbeNU1NBU1gRXD8FlnhD7JM9Aqt3qeNoiiJoL7QmoPOAn6ZFPLydBU76Ouu7Cx_nO0c5VoNJdmID_UmctvdoIo4elUOsRthY9XyvdsCjxKxx96aDGymIW2Mhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=c7eBmwzvpDuuvFDzT3GZZ6T9hhmc6aMaBKM_vRQzSpf6GY1fpS50B10v1nieLL1RFPNY7kKxR0fBnB-9A6LqBtK-f3NWzrFlcGXEvn_ZKgLHJ2yEfR_qe5OWRZOrLLFqKI_hfJzgl_Wvcfkl-YQ8_RzyEIno2U-0ZlbezQIG-IlA9gqGy1tJ888r5RXi2p_FOMfBfsXADEBmsJ2xn_GSFdMYDkBxRJbeNU1NBU1gRXD8FlnhD7JM9Aqt3qeNoiiJoL7QmoPOAn6ZFPLydBU76Ouu7Cx_nO0c5VoNJdmID_UmctvdoIo4elUOsRthY9XyvdsCjxKxx96aDGymIW2Mhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=Tep3cdORHfOmIemKo27RtHosPdO2z_QAlNQpE6yUZZI1day7xfTitXmtp6U-PNm4k9C8eOJuv_WzhCO6LNutE_lHRZZAKNvGSu_0xxDuJ64b4DCiLf-MkzWhpch-T3oN_iusw6wSqlMcS83_BUcRWEN2NazPQ7M_BWsqZWCwO45XBLRtTRAbmLhZW2sc3y63TsfxBf9Qp99kjm0_e45XrV3z7axcZvHiaPU93IPuzQnPPxI0Xr7g8e3cgnZxWu-Ez1b6SUvwHnJUM6lI49rzMdNq544Tsi4yWA5MoJ8y2gipr1l_RoziHqYr4f1AEqMxZJ099FCshSrNYZdKBqljIA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=Tep3cdORHfOmIemKo27RtHosPdO2z_QAlNQpE6yUZZI1day7xfTitXmtp6U-PNm4k9C8eOJuv_WzhCO6LNutE_lHRZZAKNvGSu_0xxDuJ64b4DCiLf-MkzWhpch-T3oN_iusw6wSqlMcS83_BUcRWEN2NazPQ7M_BWsqZWCwO45XBLRtTRAbmLhZW2sc3y63TsfxBf9Qp99kjm0_e45XrV3z7axcZvHiaPU93IPuzQnPPxI0Xr7g8e3cgnZxWu-Ez1b6SUvwHnJUM6lI49rzMdNq544Tsi4yWA5MoJ8y2gipr1l_RoziHqYr4f1AEqMxZJ099FCshSrNYZdKBqljIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=PTXTzR2oYV_n6E6SYA5dPjd1gH6ujbNyHWNlq1SRwUu6Yh2tbAcA7Mlx5fqrQmVR6_UqMcfBbndhRJPwe0s0Y90MVKSAv9zZX1XT6lb4KNOLXEmsvLdN4OOc44UijwhredT9SvGCrV_D97blCQYqOtuwkvTk3TCUBWhLg4bTazsdihJVAFuTR9I2iGQN7XBSwSwHjXpCFShMdT8tJJhoSrwxmMQGxJDxbl6-B17D7d2zZ35Oq3O8O667NLCupyM3OQm881GjTNct3E_A2twRvcjbUY-iMBSdMuppKwoX0j_BGICpEXWrEcLCs58DWBqai38pTd_tOsa4NhFzhUto3Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=PTXTzR2oYV_n6E6SYA5dPjd1gH6ujbNyHWNlq1SRwUu6Yh2tbAcA7Mlx5fqrQmVR6_UqMcfBbndhRJPwe0s0Y90MVKSAv9zZX1XT6lb4KNOLXEmsvLdN4OOc44UijwhredT9SvGCrV_D97blCQYqOtuwkvTk3TCUBWhLg4bTazsdihJVAFuTR9I2iGQN7XBSwSwHjXpCFShMdT8tJJhoSrwxmMQGxJDxbl6-B17D7d2zZ35Oq3O8O667NLCupyM3OQm881GjTNct3E_A2twRvcjbUY-iMBSdMuppKwoX0j_BGICpEXWrEcLCs58DWBqai38pTd_tOsa4NhFzhUto3Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=Z1XXXZjt-PuZePR8Rr3hrWUWMROS80zzdlIcYQrGnv8eNa7H-39YPVFZwRDkU2CINy9ozcx5cCmcA5oc81Lxmj_LHluWjrIM9dbygsbSyfS4aS_f0R4SWacndyrtYqzI0LJZ2NK3FpXWOsOJIaF43nTB0zWspnoq917acOBiuUB5_-jAhM5dMWJeJQv_Sa4s-hpF5Ybx1Dj6GYycBD1_0az0uIPW1FRi_zLHLVmXhQiSh_JXLwWxnr-H89M0N9u867rhq8HPBgvqaH2Tz1dzR2zh0W7vHGDLO0_E-FzW-QK7TNxykn5dMAyPzDP75qtexrP6KVgyqiOFYhy6fP-bGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=Z1XXXZjt-PuZePR8Rr3hrWUWMROS80zzdlIcYQrGnv8eNa7H-39YPVFZwRDkU2CINy9ozcx5cCmcA5oc81Lxmj_LHluWjrIM9dbygsbSyfS4aS_f0R4SWacndyrtYqzI0LJZ2NK3FpXWOsOJIaF43nTB0zWspnoq917acOBiuUB5_-jAhM5dMWJeJQv_Sa4s-hpF5Ybx1Dj6GYycBD1_0az0uIPW1FRi_zLHLVmXhQiSh_JXLwWxnr-H89M0N9u867rhq8HPBgvqaH2Tz1dzR2zh0W7vHGDLO0_E-FzW-QK7TNxykn5dMAyPzDP75qtexrP6KVgyqiOFYhy6fP-bGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=XQAjOCsgE0DNOX4Dpi2HcuCoujXLPdGdnzjaVDGeLH7zFuUsz9G5r1NS62u2N59nwkoBITnjPbk8TSVXlEJc4NfR3mNN1C6s4fwbSiCgFDCRkxfHBjaWtzmjIOgrKC6yeBgt1XZmRsRUEr97t2Y194756SbQamveBt1V36eI7l4ZLqrPJIeLd24-jt55QGZltazAJl0Q2EJF7Q7e0_n0f5cZMjjDvkXXrJmn7rtrq2YhzvG7BBUAAaLZ-p_uJ2w9-bUtoceDAHkeezYPDwDhxifZn6siqqKNdaYl3ZEOjS7l78dXyaW8RaL8_0UBzoPm0lZWB2euxVooMxHwiIG17A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=XQAjOCsgE0DNOX4Dpi2HcuCoujXLPdGdnzjaVDGeLH7zFuUsz9G5r1NS62u2N59nwkoBITnjPbk8TSVXlEJc4NfR3mNN1C6s4fwbSiCgFDCRkxfHBjaWtzmjIOgrKC6yeBgt1XZmRsRUEr97t2Y194756SbQamveBt1V36eI7l4ZLqrPJIeLd24-jt55QGZltazAJl0Q2EJF7Q7e0_n0f5cZMjjDvkXXrJmn7rtrq2YhzvG7BBUAAaLZ-p_uJ2w9-bUtoceDAHkeezYPDwDhxifZn6siqqKNdaYl3ZEOjS7l78dXyaW8RaL8_0UBzoPm0lZWB2euxVooMxHwiIG17A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=Lsc9MWoDa44i69UpHfuyvBSMr4s8oekG8p6ILo3q5h61HdnrtE0of9HgK7LrCzhOko-2Q1INF_azVnciriuNYylbPs7aTEpBX9t1nqtBsZl_3YZE7sFax9QEvyZxbdjjYB0uU7j3BfrylB_uvML6thm0nQ2Fkvx7s7WmIwHEg2z2kWIe4WiFEGfWMX8mYiEvys6w3fN3Mh1JjfvlVg6lptflgFdofg4ZdIVcF0eeDd5472OhodCHNNYqp0sTQq3RA_H46roxkRAtmT8IGWezG93pKcqR2gRUH-LVg3a5vvlcDFQuiGFV6XEW9i5wYy68P6l_vhfU_JMqrHDshdEi0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=Lsc9MWoDa44i69UpHfuyvBSMr4s8oekG8p6ILo3q5h61HdnrtE0of9HgK7LrCzhOko-2Q1INF_azVnciriuNYylbPs7aTEpBX9t1nqtBsZl_3YZE7sFax9QEvyZxbdjjYB0uU7j3BfrylB_uvML6thm0nQ2Fkvx7s7WmIwHEg2z2kWIe4WiFEGfWMX8mYiEvys6w3fN3Mh1JjfvlVg6lptflgFdofg4ZdIVcF0eeDd5472OhodCHNNYqp0sTQq3RA_H46roxkRAtmT8IGWezG93pKcqR2gRUH-LVg3a5vvlcDFQuiGFV6XEW9i5wYy68P6l_vhfU_JMqrHDshdEi0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA1Ac1AYbaYlS-WlEXOiVNCiGZKoduUSbPo5Lu7h0xVYwreC6PspjyxI-E_An5mWwtyevvzeM9EWIbd6sdBVF3G34rqCexmSubMaDEDPMRQI7jU1fLgheECieyW634iImlsJGPWsd7ZFTDHtaawXVCdFOYT9UFbSyM8CI_tRVBlorZkp3lhWqrQtFS_RtTNS2LlrYCN6oYhuhrw3oY9f3AoX9-cJsy0fxqyzgptTHTnVOaIf4ZegBsPgu4ifWzbESdsR8CU0HQBgPA1NBYUhJpxJbAjo3a7sI1VXVBvepYPJqWgM0OZfzbLaN0ociDKgoPCG_C3B9jyFpKQCHkOxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7CjlSYwTdkwTxOJR4OYQO3tYfU6Zz-eHjrKVbokmsgrvmWcoVNbsUDN-LLWV08NCiAEXDOncszhB6bhcs2FpOBMUNud87f2wW3NHk6AjPNeAsPj5XhMxAI-3zXJ_MDjE8bupXO7tYh5_JB8tH0rwLdCgVqWkSar_SR2jGPCtBX-Bg-hR8EJ_lHbcK8V07Wpz9a3a1K83ENjIzt-9b1fxzTb1bnUFjf6D9jWjKyepPnsW5dJtXVmlOtueJFuPfGpQP02IYJwKca48FT-1zVOemOm3IjCEgxltyJByAHnF0lvYx-jcfKS8yP24V0pRthPm10_D9LRk6jxxfkywUPjTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_hVGC5bIO86xm2pt9LTQ2bupRJ_M38j9RWcGmxUkScQOiBWxxG-X0eOlGyfKzPSchljkI4B91FNZIB4SZ-7j0FVyi9FJQDXmhkkqkvSXSZIUsiYba1chrWAO_Yjmr1i13DLQHEmqUIGE00avT8vedWQOr67jxEzRWBP51et4FiNdK_vGez5bH28-_57EBOMfPT7350xR5rQsbKtn2-6zbr9iCrfwhCG7-xNraG7a3ebrBu9MxkPOwD_R47G_dpMYl1qMzIYRkTGEDWsmBiSubHAmx3LC3JRjiEOC3GUvGloltQKhunMPLdOMSQqv2QPNbxRb7GjWnT4lWRTCJv7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=tnSkWIVbOVMvzKuKgsHh1E_Ve2tAGxCsTlf6bCplHgXzhOUnwYwivhSVW6gZbI6UxCPe-MK7_p_LrwDe7IdnhjPQknwxDfGLVvz-QGlTsRPhrspzvQ6BbAggj-yKXttekiOmsiSE_aP_N-iOglANzQE_u-S_P_cUeVsK3S1MoN5FFFCMvkngQcgpvtUMtyP9nq50Fu80Xs29ENgbNFi9d4X9Kwo6aNdFyhfBGN9n2MnUKEA4bTD9vihLCHN99M92f1vtkkdtkwu6C6SGqVN1HRVlhU32XKWiOR4oTHN5hwtmFmKInCArmUkO48MD21pV8YXN-ZtKX08GCLRNoJhmhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=tnSkWIVbOVMvzKuKgsHh1E_Ve2tAGxCsTlf6bCplHgXzhOUnwYwivhSVW6gZbI6UxCPe-MK7_p_LrwDe7IdnhjPQknwxDfGLVvz-QGlTsRPhrspzvQ6BbAggj-yKXttekiOmsiSE_aP_N-iOglANzQE_u-S_P_cUeVsK3S1MoN5FFFCMvkngQcgpvtUMtyP9nq50Fu80Xs29ENgbNFi9d4X9Kwo6aNdFyhfBGN9n2MnUKEA4bTD9vihLCHN99M92f1vtkkdtkwu6C6SGqVN1HRVlhU32XKWiOR4oTHN5hwtmFmKInCArmUkO48MD21pV8YXN-ZtKX08GCLRNoJhmhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=W8TK39E-zbdApsg9JznX8AdJTkg8xwdAi_p4G3At1O7oqyvoy4mKd-Hr-Wi8tGsloGnExwHHd_b91lI-CBNsg3VSfOgcuck2DYWdp0N-buq2GFTBawb9l99HaUnl411Yye-wtCjBQ3J7xI5N0S0GFE8SNqroW52W7lJ5Yt7mYy7JHn1utK-shTKQHn6TItsf9R5Vl1a8GbkwISzQFxV2u_FUOGB8e4iYFWCUTWEzY1HLj-2KwP6m5wcHyTT_xt8OcZvRN4ufmm5dyb45sxvYK5-a2FjeqkVLEa8FF0BLpF367oNRSUPHFg0m_RuRH6HAHZ6V_vA-68uFNyYa43C1LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=W8TK39E-zbdApsg9JznX8AdJTkg8xwdAi_p4G3At1O7oqyvoy4mKd-Hr-Wi8tGsloGnExwHHd_b91lI-CBNsg3VSfOgcuck2DYWdp0N-buq2GFTBawb9l99HaUnl411Yye-wtCjBQ3J7xI5N0S0GFE8SNqroW52W7lJ5Yt7mYy7JHn1utK-shTKQHn6TItsf9R5Vl1a8GbkwISzQFxV2u_FUOGB8e4iYFWCUTWEzY1HLj-2KwP6m5wcHyTT_xt8OcZvRN4ufmm5dyb45sxvYK5-a2FjeqkVLEa8FF0BLpF367oNRSUPHFg0m_RuRH6HAHZ6V_vA-68uFNyYa43C1LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=A1-z9982EshWRxdeUSjduzRThd4KWa-FK7jyNpA547HCkLQsZLOk_ykmQXr1Ak4vjt0BOnlbs0HM5P4NLglV9iaogPA47HOQiALsetTFoY_3Tdu_WLD6TUuPLCuB5R5W6WBeF0xCciuUTpSaTDHu1is-6EBOgHm9rplPOvuZGdFNVilHyWHQslL7EiJUJ1PtEdHreJmZbffYkzK2ZL4XB68dNtjm2MkLDOZqhCdJ-fUu-Vl3RCXAHw_PgSCkZmK8IGx5zoq-ainOA7NRCLUC-xjKF1ie79XHXQ9d372uakKp4S9Qs6zzTlQaS5iDJ2VvEJpx-1K1abSyCT0KTKYK_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=A1-z9982EshWRxdeUSjduzRThd4KWa-FK7jyNpA547HCkLQsZLOk_ykmQXr1Ak4vjt0BOnlbs0HM5P4NLglV9iaogPA47HOQiALsetTFoY_3Tdu_WLD6TUuPLCuB5R5W6WBeF0xCciuUTpSaTDHu1is-6EBOgHm9rplPOvuZGdFNVilHyWHQslL7EiJUJ1PtEdHreJmZbffYkzK2ZL4XB68dNtjm2MkLDOZqhCdJ-fUu-Vl3RCXAHw_PgSCkZmK8IGx5zoq-ainOA7NRCLUC-xjKF1ie79XHXQ9d372uakKp4S9Qs6zzTlQaS5iDJ2VvEJpx-1K1abSyCT0KTKYK_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qc7lqXncz6Jg9_JLmK6z66mqMyuw6Fvl3JUQL7PgK-Rrz71_HNVplJSYkX78j_rPCYUNjbTodSw43mfU0cl7ApabXiYPZqU-e7owpz_DEMc5bVZURXvIlWhqseKX5lu9jleaEAoY8pSoSR_3vcjTaZT6Vm0wxgIpFz4AuHRoYbc2hr9fb52DPRy-uU4KVp4kZx6RH4wWsbFJt1w_nGOVJ3V0T8P1BwIivrw2SnclZPD8kqoLvx72jlkysvwm5mL7ROdfNyetdw7HWifnnonIc7ia_Y7yHMWPk8uvy6fFAbjkiiUOzCjNTXmtOkcn12Dk8tPmxrmCw3L2sDVd7_31IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=Xe1kEsS6kK4ZT7JwTpovEIT56WgellakCaj0yRtk9tTogVv7KSAO09ndOd2usitbCxh25kfq3XZYImbFkM5JnJ2zJCBBDxSl7ogKWzpaMd4zZ1bj4J6a12rzv5xm7o-ltAHV-u05TPPJEhRFvJkICjISTMz1dxLp-pwrPWIF2atFVVYFuxxnN8WS_BHpibarVR9vadRktSFuHsT4Mk_1p1IkmhevddqQZWHV7HGZcaZ64aTvW_WBAaIUfC9ZhKeuCrFSl_bKUlslkfC34-mW6f8hCZqcWPG29M1XQ1wLDjX5Iase_IQHkD2TjX58Jk9NeF6cYxcHl6bHalY-3I-HLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=Xe1kEsS6kK4ZT7JwTpovEIT56WgellakCaj0yRtk9tTogVv7KSAO09ndOd2usitbCxh25kfq3XZYImbFkM5JnJ2zJCBBDxSl7ogKWzpaMd4zZ1bj4J6a12rzv5xm7o-ltAHV-u05TPPJEhRFvJkICjISTMz1dxLp-pwrPWIF2atFVVYFuxxnN8WS_BHpibarVR9vadRktSFuHsT4Mk_1p1IkmhevddqQZWHV7HGZcaZ64aTvW_WBAaIUfC9ZhKeuCrFSl_bKUlslkfC34-mW6f8hCZqcWPG29M1XQ1wLDjX5Iase_IQHkD2TjX58Jk9NeF6cYxcHl6bHalY-3I-HLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=O96kyaFe2LWHwqjG-eyh_f6fgcMEuxXk1aNWR0mnrWc9W4l7-L14Cl2l_SaFGjkrhpmnP5Aj7mvvRTrQmjIb-Vtxg5B_RpwOUZ_BCLHopgGNlVX-dt9kbgC35WsCzEaE6w1yYxo5b2weQHFWFUeh30__S26f0Y3MGPdItQ1hJCa4c4PUaSJEK_kyJWg9xDnWCy_7j_ou8ri-vj6ZzHWuNxcemEzmon9IujPMpzH_J9K-_gnTQf32fqk7pls59UGgAXw5sU7Xf23B1bBl4h7fWpI0ggxrPzo0QD-cpVB0yIs_VC2yk1dhRFBuBdhAl4kHZ_4_C5wMS09IbUAPqLFMhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=O96kyaFe2LWHwqjG-eyh_f6fgcMEuxXk1aNWR0mnrWc9W4l7-L14Cl2l_SaFGjkrhpmnP5Aj7mvvRTrQmjIb-Vtxg5B_RpwOUZ_BCLHopgGNlVX-dt9kbgC35WsCzEaE6w1yYxo5b2weQHFWFUeh30__S26f0Y3MGPdItQ1hJCa4c4PUaSJEK_kyJWg9xDnWCy_7j_ou8ri-vj6ZzHWuNxcemEzmon9IujPMpzH_J9K-_gnTQf32fqk7pls59UGgAXw5sU7Xf23B1bBl4h7fWpI0ggxrPzo0QD-cpVB0yIs_VC2yk1dhRFBuBdhAl4kHZ_4_C5wMS09IbUAPqLFMhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBXx1nuEfVJ6vBG8bdfNYkgwho5tdyWDZTwwpS-l2p-CyHlMjBTQk8rCYvwtRGD8DHwOoIc_3gGPiov3sSBxd0WQV9jCV6razk-ILg_Sy7VNAAIIQLlsrrAP_1yLv9sgmTKyWHW8j7su2w1IcdumQsrLaeAIhIOD_6YXGtBgQ_w32uZunC9e5iwr3FZ-9W5VWkzSYDqbY8wivX7AeUExNcDRLyCyHbfw-xX_aZoQ__ZthGXvWv26Z0SaGbUbm0POgCqdjX4NbphmzmVFBiKmZPGUDsUKiqRSSb1o5VN5o4o_7NVHMxSNGkUYoiPIfiukx6DT6HB7CEG6QX3FrDkY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=Quq9fglWHzY3ajmvmD7oQ-sunr25Lq-p6Zsgf35XxgMnYgx4Xw4oJYuzHBh8DeTGbI2CspPmS2AbuB-xzZc_CeLUA83Qo91p3W5Ymmv7waDnzA4LFOOAY3177MzgrT1vyopQbhc97a8vfRKdGcI4d1iODw7fW0oURLt7e1daSgyY1XArYjejfxsAssA0hzD9piLXI1GlQc7ViIoXeae3dES7mSVJfkgxP7RvCl2UB9ZNsNCsMY7VXbPlzWCN_5O89Ut6J7y42lvPQeYp-dSbMaA2uXx1OJ8neXtVgfjZ8NhoTEB4Cp_rjZ1PRbD2RHZFZ1E2CP9ViAuDkXGmYOJ0mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=Quq9fglWHzY3ajmvmD7oQ-sunr25Lq-p6Zsgf35XxgMnYgx4Xw4oJYuzHBh8DeTGbI2CspPmS2AbuB-xzZc_CeLUA83Qo91p3W5Ymmv7waDnzA4LFOOAY3177MzgrT1vyopQbhc97a8vfRKdGcI4d1iODw7fW0oURLt7e1daSgyY1XArYjejfxsAssA0hzD9piLXI1GlQc7ViIoXeae3dES7mSVJfkgxP7RvCl2UB9ZNsNCsMY7VXbPlzWCN_5O89Ut6J7y42lvPQeYp-dSbMaA2uXx1OJ8neXtVgfjZ8NhoTEB4Cp_rjZ1PRbD2RHZFZ1E2CP9ViAuDkXGmYOJ0mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران اهداف توسط ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=LVFkDaDRULutP6oYuBGh6fImnWXdlzARqiWE0cuFRaui_gC5jEkKRvMNjlKzJlwsLxcbS1PQ3S7Y9wbXsVPWUB5Q7YdBPiyH2fbeiOMYEtj5qyVqZSE68inrPcFW431cWlQnruy2xbD4SIaJbNUJBZmk-qGprI8MtkX6r_P1QnOO0O_RHYENfEUNUZaxeFgT0-ddILh22QMZgM7K1RUvpNrdukLzulJpf4i8nDh3b66hmzd66LG2jS0185l05r1I2oH9GEpha8kYhZHHCxJpkSmIEg2N_piSJWGxqxiLhUFbv6FH1Kc3e6iVMnqs5vJWTiOdZnLR_K7HxJb1mbqubg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=LVFkDaDRULutP6oYuBGh6fImnWXdlzARqiWE0cuFRaui_gC5jEkKRvMNjlKzJlwsLxcbS1PQ3S7Y9wbXsVPWUB5Q7YdBPiyH2fbeiOMYEtj5qyVqZSE68inrPcFW431cWlQnruy2xbD4SIaJbNUJBZmk-qGprI8MtkX6r_P1QnOO0O_RHYENfEUNUZaxeFgT0-ddILh22QMZgM7K1RUvpNrdukLzulJpf4i8nDh3b66hmzd66LG2jS0185l05r1I2oH9GEpha8kYhZHHCxJpkSmIEg2N_piSJWGxqxiLhUFbv6FH1Kc3e6iVMnqs5vJWTiOdZnLR_K7HxJb1mbqubg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266056eac.mp4?token=C9y5KV7veaXazb6oK6JiacBT_ynupXSZnYizJ6h_Bf_FshUZt0eNV1wwS_pSjJm08ahLWRqxI1KfUgOITCL6Ml92iN3iyQmy0V3CUiSSQJl2bSZ_0pDqoogzA6aafPN1pnlfiiMeGBMfIEfmTtIYziHXCXhrayYkHfzMd3N4DPWVaS9KKIGHAz_ueiwbdkILLgx7XyK7g85rLQ72shZQLBo7fyFG2MYh8hMba1J6teCxqivBZV8DZCZpdvuT2aRtQC-P8ZSip_pk0aIWTURuSys4bVhiB6X2zx82wU8UFQUxbFiDRkEV25T4ciAVzn_nsrqnmD3Q6GOs-ieZfR-6rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266056eac.mp4?token=C9y5KV7veaXazb6oK6JiacBT_ynupXSZnYizJ6h_Bf_FshUZt0eNV1wwS_pSjJm08ahLWRqxI1KfUgOITCL6Ml92iN3iyQmy0V3CUiSSQJl2bSZ_0pDqoogzA6aafPN1pnlfiiMeGBMfIEfmTtIYziHXCXhrayYkHfzMd3N4DPWVaS9KKIGHAz_ueiwbdkILLgx7XyK7g85rLQ72shZQLBo7fyFG2MYh8hMba1J6teCxqivBZV8DZCZpdvuT2aRtQC-P8ZSip_pk0aIWTURuSys4bVhiB6X2zx82wU8UFQUxbFiDRkEV25T4ciAVzn_nsrqnmD3Q6GOs-ieZfR-6rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران سنگین اهداف نظامی در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68891">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68891" target="_blank">📅 01:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68890">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2lJSI6dvP-24kvbhCFWDMPLP0tYnXtrFCxYoXPezBSzDc74qX8HzrBuNIfr-dJL84safBIWc1tjbXPlq0Ok9rGaT0pgk6UA6uHGIkVNXAp6-BfRkHF1XNINqvdb-mgcMz3l-WC3bPVBHRj0PVmQ510HidSafPom0YlG65H9C3v4kkYL3xOmh80JGsCjOSdpnILq_hTaY3T-z21Y4EhWw5_pkU3bT4OZ1uVHVBsBpCT8ycC7cESUFwv1i07WQcSjXfbm0uuXY6Tbe7djAQAZ7SlWUM4H76aegg57Tnh1t6Ehe8y0wBqoVYT-70WHSDU1sGXt_CF5PAVb01OeHo3kKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:
لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
اگرچه ممکن است این خسارات بسیار سنگین باشد، اما با این حال، این اقدامی عادلانه و منصفانه است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68890" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68889">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=RjdGM0kgeNYaKv21u8tR1exfMegHk2wkAyM-xgWIiAXkLC5t16g0qKLxsBxywh8yXecFaliKF2TMvKBaDDxwf9nAINe91Gkpi8Bc93FlB56l6cDVopfUzMiu9kSFq0pCrQdRKGGP6dF1oZHejD__zKG8MVs-5Be3l4XxjlTTy4q6hx7WgG1G91Xol8XmwchHPFSRnPP5Cf0TRu5LFHKfbJOyWfglJdgEJQDqICQnIQUjEQYzLY_ifpv0c8bJQOpF71anqg8_7EpIrLWK_MlB-AkjJtB0ea6OrJ_mB1VQu137vVLglrCzWIl8RVsQRUMAobkKjaGbIXGmZiPT3hFw1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=RjdGM0kgeNYaKv21u8tR1exfMegHk2wkAyM-xgWIiAXkLC5t16g0qKLxsBxywh8yXecFaliKF2TMvKBaDDxwf9nAINe91Gkpi8Bc93FlB56l6cDVopfUzMiu9kSFq0pCrQdRKGGP6dF1oZHejD__zKG8MVs-5Be3l4XxjlTTy4q6hx7WgG1G91Xol8XmwchHPFSRnPP5Cf0TRu5LFHKfbJOyWfglJdgEJQDqICQnIQUjEQYzLY_ifpv0c8bJQOpF71anqg8_7EpIrLWK_MlB-AkjJtB0ea6OrJ_mB1VQu137vVLglrCzWIl8RVsQRUMAobkKjaGbIXGmZiPT3hFw1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
مقدار قابل توجهی از هواپیماهای باری نیروی هوایی ایالات متحده (مدل‌های C-17 و سایر هواپیماهای سنگین‌بار) امروز از اروپا به سمت خاورمیانه در حال پرواز هستند.
برای توافق دارن میان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68889" target="_blank">📅 00:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68888">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
دقایقی قبل دو فروند موشک در جریان حمله  آمریکا به محدوده روستای مسن در جزیره قشم اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68888" target="_blank">📅 00:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68887">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b133a06016.mp4?token=lk4y38sSuYKazGbc4Hu06qnXpdCDYPkAQDr8mbalo7c1GbXVYWyDsp4pNFQYHT3kW7Msfxx2hSSjr20UQGRWAdzBRyC3aT3tYa3Tjm9exUuN4-ho60TQMTiE3IKm1s5VnA9K3rYUqDB570WWKhg80SpsA4L27xJL3HfyN1YPkhgUPUr5CSpiP_mDogpY7ubtwYUub0LCgw37KUcc28alS4pfmKr_S4kx3KDw59TgTHbLWjDJtqc0bjTGhZ9MYT_JEVx3XWNHpYDpBntmDjjuaYI-gixA9U58liCuEFuk__SjTwyPIIn38N7C9gO_9fxatb3-x2WS-Stt6EdNUkoO2oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b133a06016.mp4?token=lk4y38sSuYKazGbc4Hu06qnXpdCDYPkAQDr8mbalo7c1GbXVYWyDsp4pNFQYHT3kW7Msfxx2hSSjr20UQGRWAdzBRyC3aT3tYa3Tjm9exUuN4-ho60TQMTiE3IKm1s5VnA9K3rYUqDB570WWKhg80SpsA4L27xJL3HfyN1YPkhgUPUr5CSpiP_mDogpY7ubtwYUub0LCgw37KUcc28alS4pfmKr_S4kx3KDw59TgTHbLWjDJtqc0bjTGhZ9MYT_JEVx3XWNHpYDpBntmDjjuaYI-gixA9U58liCuEFuk__SjTwyPIIn38N7C9gO_9fxatb3-x2WS-Stt6EdNUkoO2oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امشب تو میدان ازادی تهران
زیردریایی سپاه و سامانه‌ موشکی ذوالفقار بسیج
به نمایش گذاشتن
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68887" target="_blank">📅 23:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68886">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlexratLHQdKxjhp0TiZMRi7PjATR-QupqOGeNyQfq9ZAt7GZj1gRLMg_nOzWxZCzFq9PJyfdo03M7kSDTAuMf9WUglCSa_q-jJE5hcaJtWIiPSy91IOwpV03uC7xhkV7dtsVfqkh3NzZlRB0T6NNGSNg4x6ow_nnzunhbz3WB2bG2LlGK-VytBfRMkMIi6fepQ0WVg4azbGx9vYJg1V-ejDTJNxK_U1b3sjouIJPuMyYwtgkmHupnFTV0G9Cy5ljpQunMrW7Vl0-AgDeX4uPWV6zIovQDqo9yusGagWywzI5uQpW_E4x-P28NSh3_DStSgf_O8YqFwU8POqtfQ_Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک دیپلمات آلمانی در گفتگو با شبکه «فایتوکس» (Faytuks) می‌گوید کارکنان سفارت این کشور در ایران خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68886" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68885">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن  @News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68885" target="_blank">📅 22:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68884">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68884" target="_blank">📅 22:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68880">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HQzSGtLWF81aiXCoJAp4j5xWagFhBNHCkp-gDZXvihV-VAB2OzyOtLvz9rKB-JIjCXMYJSAw-Fa_Jlvk8oPX_kXIbL3LEFs-GjjFCmTaLbnssuO4D2Nf-S7GjgRgqp-WqSs8a4uyQ6uRJ1BK0amy80W6N1AAeEIURQ-KcDkD_Dv4yRU0aDa3joF_T5g30gwoqzeO2PfzqX2Qb4x3taC3ePzRz1akXN1lGGmO6Sh8-78so6jZbcw138-l4Y7vFeCdFSfIKUxzONC7b1nmvkyaivEhXC8W8lk61BYlfNTZeeQ8dfDxjGslQWHNKWUW2LbyMYraps_oPQTqoQdGPTAFzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zjo4MieI-SsquTK59NEebRy8MSGtSzP-WVO8Eoflv9660sxvFQRCUlWSMqV6sesrT8cpFWDzbtbh8ldJjAvn4rcwct_WzhKwQCY-L5X2WGOMvF0tynZHvfZydaDxJw5qDAhcSvc-cFG_q5qI2zPyWhQ8-ApyxO8S86pz4E8cjzHrzXzcfBtgfjvF33gG5VjXJf5GIz__n5Er0WuwqMioQWUFQW88BsbbWtiCIrYl-eWtAVCca3Wu5olun1lUt1YCpr_Rp1-fI1HWrwLJSscpwt7UlgG0aYabuZiDTZw0ZVL3Wj3zIEBrKdG8dhZB7s864RTylYiFWz6r6hUi2truCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=BEG-2j1qLSNC3RH1kzHmc0z3Y-Fay6pX4X2QKd8JxeEMdPAwZXdWr1NJInl1pvikBUkmiy46Im9LDoWG0rMvIgAK537_a7ym3OXkvq8Aspo9y_mUlBW4rOxrMc0JYhyS4DxHX_UZl1gKMqehbAY5RRvBNFrkdOz6F1AwkC5utzCfd__AtwhK81fE-UwLIMLftqTsyyUB1Iib1mUc719PMkdQfpxCHAzzr_680bNBpa4X3xUJDYK0d6pRRMpgbkMtL05mMrSpb7cdYTvox-MPzhaKbMz1kVgs4czT16lcj495r_CGVxCq3zyPaoouAQkByaSBp8Mc6APHN0xkMZIo5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=BEG-2j1qLSNC3RH1kzHmc0z3Y-Fay6pX4X2QKd8JxeEMdPAwZXdWr1NJInl1pvikBUkmiy46Im9LDoWG0rMvIgAK537_a7ym3OXkvq8Aspo9y_mUlBW4rOxrMc0JYhyS4DxHX_UZl1gKMqehbAY5RRvBNFrkdOz6F1AwkC5utzCfd__AtwhK81fE-UwLIMLftqTsyyUB1Iib1mUc719PMkdQfpxCHAzzr_680bNBpa4X3xUJDYK0d6pRRMpgbkMtL05mMrSpb7cdYTvox-MPzhaKbMz1kVgs4czT16lcj495r_CGVxCq3zyPaoouAQkByaSBp8Mc6APHN0xkMZIo5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای تهاجمی اوکراین در یکی از بزرگترین حملات از لحاظ حجم آتش شرکت بزرگ تجارت الکترونیک روسیه، Wildberries، را هدف قرار دادند.
این تأسیسات که در شهر کراسنودار واقع شده، به‌طور کامل در آتش فرو رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68880" target="_blank">📅 22:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68879">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
ترامپ:
کیرم
تو هرچی کمونیسته
#hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68879" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68878">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند  @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68878" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68877">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68877" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68876">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">همین الانم ترامپ داره حرف می‌زنه
#hjAly‌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68876" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68875">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اگه امروز این قطعنامه رای میاورد، ترامپ مجبور بود جنگ رو تموم کنه، یا اینکه قطعنامه رو وتو کنه! #hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68875" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68874">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.  اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68874" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68873">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=dRkDIvp3xYLDDa9d2Pl_E-atJjVV_ooDULcRM0UO6gpDg2mV_EDmRYfN6sDx6BiTfwI_Ew0GlZIbULUhokumfZ_jS1B2Sb-Hkv6PiC2vgycWvCNa7Q8befTS50lGpVgeA_cxnD2JGDcE7P7upim5aqMb2wEsILsIGNzAl9oXwXBErMISrtYB948SrAHXb7jkrWcwNQpfVs3rWvoxyqjkbPB5vv6Cj6jig4q5cbheyokJaWvUN6tpnr_USKhyJmJOQAYHEy3Igvx0z-LvhI9s2q6LUbodM9trtowxw9Fjhso3jlS5Zr4EBWDJHrC7L16mE86OddV9aT-wU5keXkLJ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=dRkDIvp3xYLDDa9d2Pl_E-atJjVV_ooDULcRM0UO6gpDg2mV_EDmRYfN6sDx6BiTfwI_Ew0GlZIbULUhokumfZ_jS1B2Sb-Hkv6PiC2vgycWvCNa7Q8befTS50lGpVgeA_cxnD2JGDcE7P7upim5aqMb2wEsILsIGNzAl9oXwXBErMISrtYB948SrAHXb7jkrWcwNQpfVs3rWvoxyqjkbPB5vv6Cj6jig4q5cbheyokJaWvUN6tpnr_USKhyJmJOQAYHEy3Igvx0z-LvhI9s2q6LUbodM9trtowxw9Fjhso3jlS5Zr4EBWDJHrC7L16mE86OddV9aT-wU5keXkLJ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.
اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول از کنگره مجوز می‌گرفت. اما با رد شدنش، چنین محدودیتی اعمال نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68873" target="_blank">📅 22:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68871">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0_boY8j4X8wXUzsxRsu5P2Qo7sR6UPvWZBG5_8e7mzVW8qkrPFCksnv-4PqmoEbqgTM9nMBbVQC5NjDc4dTEmxLoErBKz2oWfKuI0JOY8OdgHmYhEBa94MnZ5B4PFQOIWKnsxZcjvvLRWf_QKFYz-XIDg_Ecoa4cl__e6LJeZLgltJ-qpIBF5_X6s948j7bglmIv0Mv2R3Z56w3lCfABRb27nA51O1c7tOStULg9-FKVtOOdbBK7YwO_yRlSOX1Q9RSCpiV0DbzicJbRSECZTjOetf_DaWiYI7UySkdldUIfykQ3cwa6pckuo1VT-j2Nr0GaOZiLK9aRXJJVIbRdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=U428DGlUuCaXp6air9qtxEYobBvzHtlr-Xyaa73xogwBCx1yDLzdy3aRm1s-jsMX5Eqe4c7mJh5XnAPN42qJS5lvfWgZwS_eWnniFwJIOKWFDTfbeZ7ZAsP0JKhYZwnPQ74wQo7WXv4S1izsIZx3DleqGQMs0x7G9zbdZEO43raC7wEdZD_WuFTILZ-gRDqDixbyvym63sM89kspVzgoNk2pdbzOn09892SjQIPBd0NpCMB4CMwLqTeFdAH9_oQv8hEBFi24hcFdcmQyqSOZl0387iIMEzmR7cwAKi3uS3QcYDtJiCxfbwhQmAeJsT3wA-PT_CVKTikjD6dfgc-a_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=U428DGlUuCaXp6air9qtxEYobBvzHtlr-Xyaa73xogwBCx1yDLzdy3aRm1s-jsMX5Eqe4c7mJh5XnAPN42qJS5lvfWgZwS_eWnniFwJIOKWFDTfbeZ7ZAsP0JKhYZwnPQ74wQo7WXv4S1izsIZx3DleqGQMs0x7G9zbdZEO43raC7wEdZD_WuFTILZ-gRDqDixbyvym63sM89kspVzgoNk2pdbzOn09892SjQIPBd0NpCMB4CMwLqTeFdAH9_oQv8hEBFi24hcFdcmQyqSOZl0387iIMEzmR7cwAKi3uS3QcYDtJiCxfbwhQmAeJsT3wA-PT_CVKTikjD6dfgc-a_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ساعاتی قبل سپاه پاسداران یک نیروگاه برق در کویت را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68871" target="_blank">📅 21:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68870">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=MWI9Ac7Q06jwtC3Vs4Tvq1ab3C4kKUcbDfFMm6j4e0v4H_KobNDTsfWc0g84i02L3vaJFyp9yHSo38RBMNHkVCfWtaEoGS3dMbPDogFIFhHBRbROOJCAYE8L3FD7bD9IZLwj5SE2EN6V342g_bpg1btospbm8jZ-iFR8yFS1YzYxLZZnkyeGoYj6HORPyJwiJBvJhybIs1dOCCvPqDszC_55dlw9Xuhk1-3gINei4um3ydyDv1xyFrssP3d7jisW9I2SAxn7HhNN-Vr-5LiVwm5OKo5VWo7E93lS59jtMZ3YWYnkfM3o4eZlk9Cy6joYd5QaY6fj0Q74v0JBkDUBWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=MWI9Ac7Q06jwtC3Vs4Tvq1ab3C4kKUcbDfFMm6j4e0v4H_KobNDTsfWc0g84i02L3vaJFyp9yHSo38RBMNHkVCfWtaEoGS3dMbPDogFIFhHBRbROOJCAYE8L3FD7bD9IZLwj5SE2EN6V342g_bpg1btospbm8jZ-iFR8yFS1YzYxLZZnkyeGoYj6HORPyJwiJBvJhybIs1dOCCvPqDszC_55dlw9Xuhk1-3gINei4um3ydyDv1xyFrssP3d7jisW9I2SAxn7HhNN-Vr-5LiVwm5OKo5VWo7E93lS59jtMZ3YWYnkfM3o4eZlk9Cy6joYd5QaY6fj0Q74v0JBkDUBWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب یه دلقکی اینجوری پشت ترامپ اداشو درمیاورد که حسابی وایرال شده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68870" target="_blank">📅 20:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=YmQiEMn9nj-X2AOAahnoBRPzCtV6lBVA5xa727PY8N5ghM709Kr6_vFXdsqYyBI9_1h0tJQ5iztdv20-rGhUIOPedX3nNCOBK6Jz5OdL6LofQKXonNzTLRzLEJoVrElsjZTEupKOiuJOVdGpR0M_VSA97t-gPD8e7ICEjbJ0ZiIqOMXPb7ZC_doaNCDw7or-KXMAzH3j9Jch2sPkuuQkQXoVoHX5HnahBn6EJGoOiH6vbRYECPnKpVCMDTy52Ws3e9ZfM9GigsRm0B_hwBjjkGEzkUuLUGp3lvRsiXtdaEBXO8a7MRYWPQ9GqyRnsFiRWQpnp2TwwIRMdkN6Fbs__GxKQZLJuzgqGzZJa5LSzksDdGtVYinaYXvsoxMaeJTIctDfFxULKC0Ml9x530TOYjNGLWakQXJYVo9XhK1wLJv1_OGXTfcoW-PJ_JpJ4-knHMEUF9XgYDhVcmZuifqG144Auc6ov61XXE4yM2S_MX1BwdRN-TrkxFc-PDV8vIgw_JPXP5iCkZhjtqHCai7K6o4ir6GkVOKLbDxMb3aBrpUHhpUMhy0qRl6UqyYcGaxDE6AHRwkoBEm3iD7gez_9At2s7Y46IAIkc7o1szRQ_pwFZVxpYr25A7ZSlDic1-rqeHVjxSWArhWUqWyc8vzvNJx2XXNVq7DBh74WKXljaQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=YmQiEMn9nj-X2AOAahnoBRPzCtV6lBVA5xa727PY8N5ghM709Kr6_vFXdsqYyBI9_1h0tJQ5iztdv20-rGhUIOPedX3nNCOBK6Jz5OdL6LofQKXonNzTLRzLEJoVrElsjZTEupKOiuJOVdGpR0M_VSA97t-gPD8e7ICEjbJ0ZiIqOMXPb7ZC_doaNCDw7or-KXMAzH3j9Jch2sPkuuQkQXoVoHX5HnahBn6EJGoOiH6vbRYECPnKpVCMDTy52Ws3e9ZfM9GigsRm0B_hwBjjkGEzkUuLUGp3lvRsiXtdaEBXO8a7MRYWPQ9GqyRnsFiRWQpnp2TwwIRMdkN6Fbs__GxKQZLJuzgqGzZJa5LSzksDdGtVYinaYXvsoxMaeJTIctDfFxULKC0Ml9x530TOYjNGLWakQXJYVo9XhK1wLJv1_OGXTfcoW-PJ_JpJ4-knHMEUF9XgYDhVcmZuifqG144Auc6ov61XXE4yM2S_MX1BwdRN-TrkxFc-PDV8vIgw_JPXP5iCkZhjtqHCai7K6o4ir6GkVOKLbDxMb3aBrpUHhpUMhy0qRl6UqyYcGaxDE6AHRwkoBEm3iD7gez_9At2s7Y46IAIkc7o1szRQ_pwFZVxpYr25A7ZSlDic1-rqeHVjxSWArhWUqWyc8vzvNJx2XXNVq7DBh74WKXljaQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فاکس‌نیوز در حال بررسی فهرستی از اهداف زیرساختی احتمالی در ایران است که ممکن است مورد حمله ایالات متحده قرار گیرند؛ اینکه کدام نیروگاه‌ها ممکن است هدف قرار داده شوند؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68869" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68868">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcQS7hgCVZSwgCgGV4_rGK31Znk6Z-u7xlBts-qyefCF62_ClVYj_kiqtUVoQWEr0XrlbCXRvrg4Hal5Wn6t2axcTh_3ayjglGbndqBH7Qku7YYfb1qd6oqx3t7TxzCAesFd6x71M0ZCx64H6TWkyB5Ao3ien95W4TDeC9POMuV87w1wfwYbDQspol6mX-wWrdwRXjgYFpYM-nufKKBpuMyuTHYBhjSKN40B2iZwuGbHdOBjjsMSI2nLv85mSNjQQppmLyDlm05H4HkkkPQvy6LIxWTbscF_CNb4kfstQ-ugbFOGPGwlZ5gmWoJx2L24UpDnZcRz742AojIKIQqE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68868" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3Es5IVwrDiA6uZdIZ4_0-v0w_wm-0Ras96asuqRt0wyWFEcmkfMRw2ok0kIbsKVXjKpliOWHd3963zK7BeswLXlB-hXy8krlGcbNjlgsRpYiMVX9jyFm4vgwSbtQ7U9o-g8tGN82gy6xOxHIZpYYDIUKjmSHF2GH2uI6LLeN1jVXCVdZQ-QRg_E41LsFM2cgoME9L3XjMDCN-ovfQWzdEDPWXzW3-ki3Kih7WW6lxcuKz7Par5cQ_n9i_SG_OHR9hakW6vxFRehjVtI30TcOZrEO1ky_GO2QaHAjoCKIeFh9ASW1e1khqxqNdDubFxzsT8PQOIAZ_CEhfLyw9g67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
آنها می‌خواستند ایران را تنبیه کنند. در عوض، خودشان را با نفت سه رقمی تنبیه کردند.
استراتژی ۱۰/۱۰
👏
👏
👏
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68867" target="_blank">📅 19:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68866">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=JwMwhP0Sg7FZV5gghGZjS-Sawf5Snek_QdfIf7HRTACZ6J1WXAkOj2ApjH3COAUkfbZjClAbxrJFdu9J4va8GSFsHOygmtRCbvUsn6vGozV8fDCt4xQIhTuCIpFSDzcAkJmG4qpS9SfUcfwXaDOoI01zHO2n0wuJeALOhuywSpaMlatfHdQ-SCfacPZ1EorzNIpbz1urc-DGuiTX7Mw1oalt59xZ9P4wWPP_HMYvkIus6WVKp5MpQL1OZdPD3BbUrBghd9iZ5uMBCzrKYpl4uxdqhN4HIqqmG5z0mx12oacHtWwAllNG7FLD_cJVFGTbfEfL_9Xq7UAk9XWYKyoyfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=JwMwhP0Sg7FZV5gghGZjS-Sawf5Snek_QdfIf7HRTACZ6J1WXAkOj2ApjH3COAUkfbZjClAbxrJFdu9J4va8GSFsHOygmtRCbvUsn6vGozV8fDCt4xQIhTuCIpFSDzcAkJmG4qpS9SfUcfwXaDOoI01zHO2n0wuJeALOhuywSpaMlatfHdQ-SCfacPZ1EorzNIpbz1urc-DGuiTX7Mw1oalt59xZ9P4wWPP_HMYvkIus6WVKp5MpQL1OZdPD3BbUrBghd9iZ5uMBCzrKYpl4uxdqhN4HIqqmG5z0mx12oacHtWwAllNG7FLD_cJVFGTbfEfL_9Xq7UAk9XWYKyoyfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العدید هم که تخلیه شده، بنظرم خودمون رو آماده کنیم... #hjAly‌</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68866" target="_blank">📅 19:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68865">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNq7x54sYxIeNwlz-tcyNnDKwCFsdeeXM84tGVL9wDcRYL4GvxOonVigG47AFwG_DhSDKTQEgyvbACLxVs6nh8eYFcYuHvu9LKWCT_0CZ6PtzKBmwXgjlrFhOJSvoJXGnMOx2B2YRyfRQEyqUueVPldnZm64WzcjvrCl6Fps6TgbbB8ThiNnSWRJuaSDHjgW0yLeUleBtL96RagIKwuY6yKFOSh5kguLHOwek6MRPeTb5UKQnxt7yq0KgD09QXmK40aOGUbc_w5f8gUZNoFhhAp5ggmQVwgjcc4i2pvKCTW7fuQ-GdiBn4kG3CXCqI8MCvEi3_BdwcImas6zXFbapA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین نشونه های نزدیک بودن حمله، تخلیه پایگاه هاست</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68865" target="_blank">📅 19:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68864">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ همچنین گفت:  همه چیز برای این حمله آماده است. اگر از اسرائیل بخواهم ظرف دو دقیقه به ما ملحق میشود اما ما به هیچکس نیاز نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68864" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68863">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری؛پرزیدنت ترامپ به کانال 12 اسرائیل:   من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.   @News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68863" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68862">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X34TwXdQm7XjKzzsThq0Iied6sWDrS5iFq7Ki-pnUbnOoVQ-M8awsfPjmsTBeLtmPfuYTxlDlA2Gy4nkm4On2FO7SIGQ6tDdRDDwRrVnYpbr_FpEa81GaeYRozo316Zf9Z0gl2FEKwjxUCb3i339IPJgg_I0xBV0WiBtQ_YC_az1nS94FOX-jI6mak1gE6cA8Fc-VXhtNFM1lcaB1pJ2CqvYtW7pvixxmr-hj9JbCEqgzSuH4t5r2M9bDt55sq5SvqgQI4fXeSn89ghVwMpK470N91eYvctGDUat2mopIflcq4C-NpciAcPomWpY80sh03KhZv1YUCSMEy6MCp53qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛پرزیدنت ترامپ به کانال 12 اسرائیل:
من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68862" target="_blank">📅 19:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68861">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=UyLUAK-5TiVDu_MCUZlwOMxoRK1Kw_JERVZtxoJCPT3iMvP2Qen5Tt4IEdWuNLa759e0f6YHutQ42-7GsTsP3gfq2PwT5sAMc1f36zi_JXUmNwFIUj3ZT-WapDvIVkx-9-YLQbVwouzVYI2RwKDNvp1vpX0uix05LBolCRkXOGf1XCmfukJVW3qIxo207K7vOAFtbe786R7NJzS1YBQecLfmypB1ilcnj4359LxJV5HecyZDUp4vzf59C9taQl2zcxq_9m7A-e0p1VIzfTMZY9feacl45mR016XeyzfJS4xqkDYZuianbpupF0QznjPhwnTdJEtiaqfnBAn9hR0I0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=UyLUAK-5TiVDu_MCUZlwOMxoRK1Kw_JERVZtxoJCPT3iMvP2Qen5Tt4IEdWuNLa759e0f6YHutQ42-7GsTsP3gfq2PwT5sAMc1f36zi_JXUmNwFIUj3ZT-WapDvIVkx-9-YLQbVwouzVYI2RwKDNvp1vpX0uix05LBolCRkXOGf1XCmfukJVW3qIxo207K7vOAFtbe786R7NJzS1YBQecLfmypB1ilcnj4359LxJV5HecyZDUp4vzf59C9taQl2zcxq_9m7A-e0p1VIzfTMZY9feacl45mR016XeyzfJS4xqkDYZuianbpupF0QznjPhwnTdJEtiaqfnBAn9hR0I0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من بلافاصله پس از انتخابات به دیدار ترامپ رفتم و با هفت اسلاید بزرگ به آنجا رفتم.
اسلاید اول، اسلاید دوم، اسلاید سوم، اسلاید چهارم. "این کاری است که ما انجام خواهیم داد."
نه اینکه بپرسیم "آیا به ما اجازه می‌دهید یا نه؟" بلکه من به او گفتم: "این کاری است که ما انجام خواهیم داد." و ما به اسلاید آخر رسیدیم و من گفتم: "این پیشنهادی است که به شما ارائه می‌دهم."
شما بمب‌افکن‌های B-2 دارید – این بمب‌افکن‌های بسیار بزرگ. یک مکان به نام فوردو وجود دارد. اگر لازم باشد، ما خودمان نیز علیه آن اقدام خواهیم کرد. اما بسیار موثرتر است اگر شما بیایید و به سادگی بمب‌های سنگین خود را آنجا بیندازید.
او گوش داد و در نهایت موافقت کرد. من بسیار خوشحال بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68861" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68860">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3008b12665.mp4?token=Av9soF7WGIo0TyNH8TB2YrXLJbqjMC5Aa8ACVrutkVlYsw8N-jzoy3Sh5FvDXbwyXJ-SxT8AS06zjAPVbzpyu2YOCZJKtQHL4O7RpkWgkm_0A8R4Rpve2393N3MW9AR5lkVglAvM31qlmTrabDOzuAz1wpS3k50omTMeypqgM6fR6bcEBG-Ra7JldfPqa_hffOsj48mcYEGSpPlxqc98F7VUnQUNRe6LyNOFlzSoKQfYjUmYGux6YyjKKrnoYNLz4qBEdPtfDAdYv4RBlVjA37KJq56lP8oQVpvTyhwSzKYI-E5W44fZDTAU-OgGP-sr0I4EvOfANXwgmvWDjX8Lbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3008b12665.mp4?token=Av9soF7WGIo0TyNH8TB2YrXLJbqjMC5Aa8ACVrutkVlYsw8N-jzoy3Sh5FvDXbwyXJ-SxT8AS06zjAPVbzpyu2YOCZJKtQHL4O7RpkWgkm_0A8R4Rpve2393N3MW9AR5lkVglAvM31qlmTrabDOzuAz1wpS3k50omTMeypqgM6fR6bcEBG-Ra7JldfPqa_hffOsj48mcYEGSpPlxqc98F7VUnQUNRe6LyNOFlzSoKQfYjUmYGux6YyjKKrnoYNLz4qBEdPtfDAdYv4RBlVjA37KJq56lP8oQVpvTyhwSzKYI-E5W44fZDTAU-OgGP-sr0I4EvOfANXwgmvWDjX8Lbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری:
الان تو دنیا کدوم کشور با ما دوسته کدومشون دوسته بجز مردمشون؟
⏺
ثابتی:
اونام دولت هاشون مثل حسن روحانی تفکراتشون امریکاییه
⏺
شهریاری:
توهین نکن حسن روحانی امریکایی نیست بعدم تو در حدی نیستی بخواد بخاطر این حرفت ازت شکایت کنه اگه تفکرات روحانی رو امریکایی میدونی یعنی تفکرات 80 درصد مردم امریکاییه..
⏺
ثابتی:
کی گفته؟
⏺
شهریاری:
کی گفته؟ اگه جرات دارین رفراندوم برگزار کنین تا مردم بگن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68860" target="_blank">📅 18:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68859">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🇮🇷
هشدار سپاه پاسداران به انگلیس: بیش از این پروندهٔ خود را سنگین نکنید!
به رژیم پادشاهی انگلیس که عامل اصلی بدبختی‌های مردم منطقهٔ ما بوده و سوابق سیاه تجزیهٔ کشورهای اسلامی، کشتارهای گسترده در این کشورها، تحمیل دولت‌های استبدادی و بدتر از همه سازماندهی هدایت عملیات اشغال فلسطین و تشکیل نکبت اسرائیل را در پرونده خود دارد و بیشترین مشارکت را در تجاوزات آمریکا و رژیم صهیونیستی علیه ایران داشته، هشدار می‌دهیم که بیش از این پروندهٔ خود را سنگین نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68859" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68858">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avMtQTRI5RJ-phcVS3ffH39t4xPih0s5l2iaCzwmOHLqLz6KaeJCNfFleU6sP7cLSZL6o_CAb8WupjBunqY_-DaxyJxgLZlJfWxhddMMbMtKVpyTwGokh4ixe9JEJlsUJewq4kABfrUTBdB_kQDNa9lf8yb_n_kMSibWqNeXdbiPm0r75fG8uSoGbjvl-_UZauF5rrhgPU0nqXORZoODBqG2YzsKYrx292KIZ7Vshs6A4qVAleFbR8bjbemM_YZFbnX46jSSj3Y2sL07qcWOzhOSzy9LRCWwqOo2LeQzZxKpj_zP7ICGr7n9K8lYilxFqK4gfq0KuZuR-cTbKSvb-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
نفت برنت بعد از تقريبا دو ماه، مجددا 100$ رو رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68858" target="_blank">📅 17:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68857">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R264jZjoefMWbaCOf3NBsu7przNz289SZDgpKp1tF7kw77uX0iO9gII8lwtCmRO2pts99xOxNQY5JxuxofiY19peFqfXFdjEPv1cXGVoe2KwE9dOrYKGxxiRPtwWL5c9fM3NZqEbPiuc8TNJNw3EGJeMx2N3JwOe0IAJgN23xob674afLFdun74hqVImdDtcizhUOubPJsro8-0-R6qLfc59RieTuKs8DLOzFizdrNm0wwqV1skDqsmeI4fHNpYyFN-wiUv7N-giDu6z8nR_uGwIxb3PXOEODzHmQJOSP45WlMA8dUBt-8HA4ZjA16qeU931Q9pgv6tjxnfm9Ue1Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس:آمریکا هم‌زمان با تشدید حملات علیه ایران، بمب‌افکن B-1 را مستقر می‌کند.
مقامات آمریکایی اعلام کردند که ارتش ایالات متحده روز سه‌شنبه از یک بمب‌افکن دوربرد «بی-۱» برای حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران استفاده کرد.این نخستین باری بود که ایالات متحده از زمان ازسرگیری درگیری‌ها با ایران در ۱۲ روز پیش، مأموریتی با استفاده از بمب‌افکن «بی-۱» (B-1) انجام می‌داد.
استفاده از بمب‌افکن‌های «بی-۱» — که قادر به حمل ۲۴ بمب ۲۰۰۰ پوندی یا ده‌ها موشک کروز هستند — نشان‌دهنده تشدید و گسترش قابل‌توجه عملیات نظامی ایالات متحده بود.
هواپیمای «بی-۱» (B-1) می‌تواند در ارتفاع پایین با سرعتی فراتر از سرعت صوت پرواز کند و در عین حال، سنگین‌ترین محموله بمب را در میان انواع هواپیماهای بمب‌افکن حمل نماید.
در بحبوحه تداوم تقویت قوای نظامی آمریکا در منطقه، رئیس‌جمهور ترامپ همچنان بازگشت به عملیات‌های رزمی گسترده علیه ایران را مد نظر دارد. مقامات آمریکایی و اسرائیلی می‌گویند این اتفاق ممکن است ظرف چند روز رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68857" target="_blank">📅 17:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68856">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=b5f2SiNeFEX6YEQvVYblH8KZQzg_yMuBzuF_-2twqOUDeN3Wmjnoaa4ICZrHR3jWry1tXcQFcDNWEh1SBTnosBcaUAuOq32TJGr5Z3hprcuQox-LIBkmWwP5M2MVgKzqNohgd5DUCS7pJsdMk_tfjGu_h-xvwkXk9zaLC2ynpSxmQ29Gu23BiX_xfQj0lQKv6WRCtQmKt977eaO0vdjjjQrUt5BAQbM3Ug-QOV7bmvqUHxmBdFJEFHHA0DKTpBhH5nkE0TA0TbgHADPmV4xyaNtOPEJ7-YtYvrvMS52I18cbvhaPZKXIs5nAADvJ4ySs03U6jbr7qgyLK2_GFrYZdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=b5f2SiNeFEX6YEQvVYblH8KZQzg_yMuBzuF_-2twqOUDeN3Wmjnoaa4ICZrHR3jWry1tXcQFcDNWEh1SBTnosBcaUAuOq32TJGr5Z3hprcuQox-LIBkmWwP5M2MVgKzqNohgd5DUCS7pJsdMk_tfjGu_h-xvwkXk9zaLC2ynpSxmQ29Gu23BiX_xfQj0lQKv6WRCtQmKt977eaO0vdjjjQrUt5BAQbM3Ug-QOV7bmvqUHxmBdFJEFHHA0DKTpBhH5nkE0TA0TbgHADPmV4xyaNtOPEJ7-YtYvrvMS52I18cbvhaPZKXIs5nAADvJ4ySs03U6jbr7qgyLK2_GFrYZdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاره کردن امضای ترامپ هنگام شلیک پهپاد به سمت پایگاه های امریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68856" target="_blank">📅 16:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68855">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:  یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد. از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه،…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68855" target="_blank">📅 16:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68854">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noDG4kFUPg4dFBn9bkalNZmulPeJ-6awPfQIJGMPv2O71rrJIYrfHnS_KfYZZqG-ujSmoZhFkIkGowuheQQW4m0OCrYOJQK-F-XoQVM91KXUfZ9rhFpdI9eVquD-f_0A0sSQfZIkMSZJFdkld3bXvedP7hk4SNuYPg2hpq38SByiSalsM1ec1wdJYdo3taoRp-EbtxQgfGXdBDkBznWYN07rHjKFYP8T6KPsUTOjc4c6hONLsE9B5R8urdGUk92vQExvGEzDbWDiv9sXLVXoaAPuGUbfQCp-uNlyrUAdYSw8uq58xkiKm88jc1erbkpvbYZSCKtNtL0LM96kWdYOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛فرانسه در حال تخلیه کردن کارکنان سفارت خود در تهران است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68854" target="_blank">📅 16:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68853">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K54d5ux2AQFLYExDG_0Rx73q5O1E4plElybIu33HI13lnM9Vt236C_40cnMT79LWuyJjHl681QrMCjhfO_jbjJJkIEpbUuvZvtAAXp3Cr0J7ZrD-DubOFilmqxCAP1SGdaGWctj0v9nY77XP3HbmHn2mK8c6DD299WHikdmmYr2lIUXfyp26wdxdyecRGYXAffczAGjS8KvMC5PwSG2E428kMd6ob3ihyd6-U2ulfqf5mV661Q4x0iZFhVkHxd60DyXl6Q7qrr3y0jN_Uq01IkDBPstUPRHAuSzsU5sruychX6z2-wMFFlwDp6QqMku6-BGi6d8TwhKqY1bPkCSgGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد.
از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه، اکنون آن‌ها دوباره فعالیت‌های خود را از سر گرفته و دیشب به دو کشتی عربستان سعودی شلیک کرده‌اند.
لطفاً این واقعیت را مد نظر داشته باشید که اگر آن‌ها دوباره دست به چنین کاری بزنند، ایالات متحده ایران را مسئول خواهد دانست؛ چرا که حوثی‌ها نیروی نیابتی ایران محسوب می‌شوند.
در آن صورت، تنبیه نظامی سنگینی علیه ایران و البته خودِ حوثی‌ها اعمال خواهد شد؛ گروهی که عملکردشان تا پیش از این بسیار حرفه‌ای و هوشمندانه بود و اکنون موجب ناامیدی شدید من شده‌اند.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68853" target="_blank">📅 15:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68852">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wjna60TtPR7qvVOU6wqgvRZILpGfYMgpjwjV-yFiWb-c3vTe4hHKihvfy2nvwG0KUOM-wiytxxXuzz5TIHC-LeRBGoOd2jifhf4wfp86qr_d0CJHCbXjq07bUtgxDYV0l6PgfF79qiuhCA-exLjVd2A6ddpeC_aSADKCQlZPn7ktxIggk2wjbfqUnxz9NUPykQI_yrBqE0qg2xpuLmdHKGzn64pHO2ZRMkg2rzXb_BK8IfsLtfzlARqEG0T4avT1o7WwsHhcohZvgxFquEsFalhj13VRaQJGwZurekt7luIjbpw-tFcrFRJyIVcKGxqua5BumS2254TjQCB-rek96Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توافق هسته‌ای غیرنظامی (که شامل هیچ‌گونه غنی‌سازی مواد نخواهد بود!) میان وزارت انرژی ایالات متحده و عربستان سعودی — که صرفاً به مصارف غیرنظامی، مشابه آنچه ایران و امارات (و دیگران) در اختیار دارند، مربوط می‌شود — تصویب خواهد شد؛
اما این امر کاملاً مشروط به پیوستن عربستان سعودی به «پیمان‌های ابراهیم» است که بسیار محترم و موفق هستند.
ایالات متحده با تأسیسات هسته‌ای غیرنظامی (بدون غنی‌سازی) مخالف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68852" target="_blank">📅 15:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68851">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=JGmNLZ-n3JmH4pTXrQ0Tn5VOr8VHmVXmrhvDLcoAcEDkHPd3weEIIAJ7ij_YYy2eiCg7DhiU81khYvaMtJeUaUbV6ynmVq3M_Ya0w47z1BdUAYPOP0phRKMhx4Nl8KicS1YvOaRafs3B4tO0Gj_HRDlfqdbO6JUgZRTwhWMwHi4hhSi8JPtOJMrpqqhNmRH6ZYeodiWEjqJdSE2Rrk-aLXcFvC0NWttTPXkavZ5JmlDBcNT9rIjit_3sLKzSM0KHC4ohkGkdnLeb7RZqGKaaZ1hT17Mwe3nrzXlRFIebzpcTEycRUKFgUFs8P15T7Til13ZEvS7yDCnoo6mf6CJYbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=JGmNLZ-n3JmH4pTXrQ0Tn5VOr8VHmVXmrhvDLcoAcEDkHPd3weEIIAJ7ij_YYy2eiCg7DhiU81khYvaMtJeUaUbV6ynmVq3M_Ya0w47z1BdUAYPOP0phRKMhx4Nl8KicS1YvOaRafs3B4tO0Gj_HRDlfqdbO6JUgZRTwhWMwHi4hhSi8JPtOJMrpqqhNmRH6ZYeodiWEjqJdSE2Rrk-aLXcFvC0NWttTPXkavZ5JmlDBcNT9rIjit_3sLKzSM0KHC4ohkGkdnLeb7RZqGKaaZ1hT17Mwe3nrzXlRFIebzpcTEycRUKFgUFs8P15T7Til13ZEvS7yDCnoo6mf6CJYbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو فروند هواپیمای «EA-37B Compass Call» صبح امروز وارد پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) شدند.
این هواپیماها که بر پایه بدنه «گلف‌استریم G550» ساخته شده‌اند، جدیدترین هواپیماهای جنگ الکترونیک نیروی هوایی ایالات متحده محسوب می‌شوند و مأموریت اصلی آن‌ها مختل کردن شبکه‌ها، رادارها و سامانه‌های فرماندهی و کنترل دشمن است.
در حال حاضر تنها
پنج فروند
از این هواپیماها در خدمت عملیاتی قرار دارند و قیمت هر یک از آن‌ها بیش از ۳۰۰ میلیون دلار است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68851" target="_blank">📅 15:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68849">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gy1hiwulv8pUoOzhfIPaTuLo8LtyV9vaCZLifMOisavUDHSnd1W0xjEx6VeXvMXZa_Upk4NrnlBkG-1PFYCFu4fUGroz27ppgALGJ_T5f0WcchKMKrtXPUz8voJvikv3wh0RffCJ5EsZiXOXUoULwIOkC1PTYHwL4F0bPnhpS_gF024cH8DU4mTVQWLPPhuAL4euskcC422n9bcK3eaSkhaNz0uV1G3JryTfUcV_TzuwXR2MqkJCWEv7jcfv41PnrDw71L4wnb3DPucbT_lRZq01YoSaRKLFjfRRMMIQGdZcInrpOzOpj-jDEZt_uQB8kSpoM6_zic-FOiohTwavJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=JPj3p_Y7a_EqrWCTzMDBry5oGBCpWPUrhLaFedsGywBa6CS1T-DBSDPBFwjto_JorSmJpS0EJszEzbhZ2DchdmRtfyy6EKafINS_52bAeWjwpShxi3sSPX9o5ohnPfqVZFoYe4xIM2gLL2sStNwDqxR6l1Aaus_3wGymDBpAJiNErL3tSX1FH9EJcINzWFOy-__-ruYs2Qzlu5-wHAGtAtG3ULxQWmnD5SFDwgR9JHJ8jh266udTZFzMlKK6VKpuf2V7MeFBiZwE4WD2JUIQycj_YXxLOd7umylNO2sVofxq3sP4oDFsSnmyqoND-PsrB6OopTIPaCucUOzbfpVGWrn7vKttlAK7orJC8IItQICTsROwGR5hPOovbVx9yAzlh7rVs2zU0N3tSqwepJN874DSb870ztDhb93PAHRZ7-EIRa-0kh8tE_DtxABYtKE1HquZoegKrbWmm6c6GaaBjnO4OyHKR1nRS1F4PuI_VNFCPW0Zi1DLSBrN5Ak_jhu5PBNnZ1650rqNIJAvQjbur6Zfr5aGxRFB2CdLrAJQcd0f_a7u8dVotgEdRAp-JRNH70Fw8aFxAeHTASRhh_XcUJ9_D9JttBEi15yrGbTXtdldHsMSRpMpwmuPif7PFnw9bAXyicben8VjcrO59Arjw0kfPDebT-wHok3H6jBsbak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=JPj3p_Y7a_EqrWCTzMDBry5oGBCpWPUrhLaFedsGywBa6CS1T-DBSDPBFwjto_JorSmJpS0EJszEzbhZ2DchdmRtfyy6EKafINS_52bAeWjwpShxi3sSPX9o5ohnPfqVZFoYe4xIM2gLL2sStNwDqxR6l1Aaus_3wGymDBpAJiNErL3tSX1FH9EJcINzWFOy-__-ruYs2Qzlu5-wHAGtAtG3ULxQWmnD5SFDwgR9JHJ8jh266udTZFzMlKK6VKpuf2V7MeFBiZwE4WD2JUIQycj_YXxLOd7umylNO2sVofxq3sP4oDFsSnmyqoND-PsrB6OopTIPaCucUOzbfpVGWrn7vKttlAK7orJC8IItQICTsROwGR5hPOovbVx9yAzlh7rVs2zU0N3tSqwepJN874DSb870ztDhb93PAHRZ7-EIRa-0kh8tE_DtxABYtKE1HquZoegKrbWmm6c6GaaBjnO4OyHKR1nRS1F4PuI_VNFCPW0Zi1DLSBrN5Ak_jhu5PBNnZ1650rqNIJAvQjbur6Zfr5aGxRFB2CdLrAJQcd0f_a7u8dVotgEdRAp-JRNH70Fw8aFxAeHTASRhh_XcUJ9_D9JttBEi15yrGbTXtdldHsMSRpMpwmuPif7PFnw9bAXyicben8VjcrO59Arjw0kfPDebT-wHok3H6jBsbak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقوع انفجارها در گذرگاه مرزی «عبدلی» میان عراق و کویت، در سمتِ بصره (عراق)
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68849" target="_blank">📅 14:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68848">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ja150UJY7xQ7st3tpDL17Tzh1d_CsTJZEQEd1j1tEJK3g-F_c1GxPzhtMg-nA6sSRI3Q7i6H_E6yGP68BG9s3UF0eDJ6G5kgRqtPggpnnC7cloxsieYQiEIGIcvsCNeO5apLCma0jwEkUv2GUXs8U0pemfttBy5geVBhCEKdkoloKHVjVxS8TTPVUKwvp6pEroNXckFj9W_AMj6_PzI5JsqahEN1AF_EiiOCplhWLJPH_c3IHW01T6rx2zmBuPAkCNkyMAaml4wfpHwlrLPGRLX83gOT_4g3ggSeB4VpHkaF-fwUiRhuXP3I3wuq0LF6tldG7EN9Ipoq65TYuanbXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابوالفضل ابوترابی، نماینده مجلس:
دولت مسعود پزشکیان با ارسال ۲۸ نامه به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، برای مذاکره اصرار کرده و او را «تهدید» کرده است.
قالیباف و پزشکیان در «تله مذاکره» افتادند و «باید به عقل هر کسی که الان حرف از مذاکره می‌زند، شک کرد.»
اگر جمهوری اسلامی «دو هفته دیگر جنگ را تحمل می‌کرد»، آمریکا و دونالد ترامپ، رییس‌جمهوری آمریکا، پیش از آغاز مذاکرات «همه خواسته‌های» جمهوری اسلامی را می‌پذیرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68848" target="_blank">📅 13:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68847">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=LNA25nSFJpF7vA3qUoXqaKLerVXp0jK3qaKTOzKSNxYphdPqipCuD4wNn2xqDHHBv5oumXaQ8ZqSyvCRpuO4bfV8ju8CLEeglt4u_nLucLm_417qxoPyOufrXL7TH7Hfn6da5Xu8-xuDgbCZZ2SHiTfBKIlr7J6grLZZvLxyAz2smnYQuZPYUv5IJnZ2Bwfq4No9AkAWW0rxL8N8ajK-e61wUTpNVxDCz13wX76ZeXUQpaQmCcsYc9q_QvICzJymP1CYj9APfS224ltDk-_FqcZ76mD3C7erso15SF0UnK7YRL28Px5V-TPkCTNMUV5c-CcNqsrIgDmC8f469BTFHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=LNA25nSFJpF7vA3qUoXqaKLerVXp0jK3qaKTOzKSNxYphdPqipCuD4wNn2xqDHHBv5oumXaQ8ZqSyvCRpuO4bfV8ju8CLEeglt4u_nLucLm_417qxoPyOufrXL7TH7Hfn6da5Xu8-xuDgbCZZ2SHiTfBKIlr7J6grLZZvLxyAz2smnYQuZPYUv5IJnZ2Bwfq4No9AkAWW0rxL8N8ajK-e61wUTpNVxDCz13wX76ZeXUQpaQmCcsYc9q_QvICzJymP1CYj9APfS224ltDk-_FqcZ76mD3C7erso15SF0UnK7YRL28Px5V-TPkCTNMUV5c-CcNqsrIgDmC8f469BTFHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه حمله آمریکا به حوالی بهبهان
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68847" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68846">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXhXKBZ9JT5NIn8JoZVMxnl5-exqxkonvRl5NMSFs4flOfZjbQaVXUGCu8N1aCxT-qkW64d2BP1CDMFrvsrKfwXVx6v-6ldlgTwxX1TyFmrOOf-mx--M9uJr3rNDoxMfJ0yT7o0eNhoaXllY8FJerMI86tdXkholmPDCpzuzOkulx2OE7xcsrYhrwie8oz-F9nAn7Am9n5lg5uQYlKxA2WkjQzkdNMvZYQnvMghQBS6bqv1q14BB-t8JUtSkG3KG5LR8a-oQe4h9l1ZYBLgsElMDy2CRgktosErFzzNeiRCK-EqWpyMQo6Q21WN7AYwJVA20Nr-dOymF4ya4tcTGtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68846" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68845">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇱
شهردار «رامات گان» در اسرائیل:
«ما تصمیم گرفته‌ایم تمام پناهگاه‌های شهر را باز کنیم. ارزیابی وضعیت نشان می‌دهد که خطر حملات موشکی از سوی ایران در تعطیلات آخر هفته افزایش یافته و دیگر ناچیز نیست؛
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68845" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68844">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=hXrEJTcgv839LvixtYJLgo-kGATBeRf208bq3ZfzSOlRcjS5Dc165zIN81vlNCIS0Ax8gzznWISh0wQggBBFUMNLUUPEwWP-PxPYhPF4E-lJVibWu1pOaY7sSnn-oc5ExzFNd70qOYS1qHRXPTOHd9RMclShxYVehDzpIBIf7fah3YugCiJpzuyJl6YQ3JwZWnsvtRlZbPInwX5IDHOpCe5_LdWG3R8vb41hkk5ISsvYPEnrruiusjHGCrlYucbjW-UH3_Lw5QszlRUo-w_jTn74_nqRZfe6RSvxf4PDD0PNRLnt66iKe457JLBFmUlSQ4SkaO4WD7wU3QhHuZNmoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=hXrEJTcgv839LvixtYJLgo-kGATBeRf208bq3ZfzSOlRcjS5Dc165zIN81vlNCIS0Ax8gzznWISh0wQggBBFUMNLUUPEwWP-PxPYhPF4E-lJVibWu1pOaY7sSnn-oc5ExzFNd70qOYS1qHRXPTOHd9RMclShxYVehDzpIBIf7fah3YugCiJpzuyJl6YQ3JwZWnsvtRlZbPInwX5IDHOpCe5_LdWG3R8vb41hkk5ISsvYPEnrruiusjHGCrlYucbjW-UH3_Lw5QszlRUo-w_jTn74_nqRZfe6RSvxf4PDD0PNRLnt66iKe457JLBFmUlSQ4SkaO4WD7wU3QhHuZNmoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
عراقچی می‌گوید سیاست آن‌ها "چشم در برابر چشم" است.
سیاست ترامپ "سر در برابر چشم" است.
آن‌ها بهای بسیار سنگینی خواهند پرداخت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68844" target="_blank">📅 12:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68843">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoDE07Uy95WF1zu7SJtJTnIfxLBMIJxzv8X9N6Q2pXHSLwn6gy2Lm3HmyYw30vsydJN3zmbObLzL4KGiznxB8e6q5uVRdtV6MTYbd6PtspRpy3-cO0Lk4ZbTqlcWT7QLn5c_6Vx5BT_jXq1fwjugBs_4Drd8Z12XNfpYVtfjEsw3r6O0roba20Gn7tuBF1IsW0JzfAOQ5zyHMOkXHDTp5te7ti_UZc6LtBag3b0Wr58aqYSj09HPuttbTSYEOyyHgyaXJ5p-qvpcimWGcLFxQmDp3eBx73KIH_YXvFgD6Vw3mA_LYQFy55hnnUdfGYbNqQ-m3z-v7gfpELuG94t0-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پایگاه دریایی ارتش جاسک که صبح امروز مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68843" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68842">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=v4___NQz1_L7QO504f67inq-HdjfOoSqyJQtZYpw_pz1VRr6NvJL1xKADlfDjq3pcdfAfSX47GTa3IFzLQ4IBuqtNO1z98vTPOwBKmZQ3Vt2d47OI-avpe-7FTCUXCUzrQZVziBLm8cLhBKw_RqgH0_h0ATex4sVNVNt6QxqMkPHRG8Q6trRn4T_7M98WYckBqPQEpTC7WvfsC0FfqZUSEGd8p9o4IWpThjfGamna72P4OOyJuujY4KfWbm147EgCbI7Ka-qjAUWAEGy53z3VPet6g2TySw1rSB1MHrLxkIC3Ryfs5YmhZdRJZ4hzXemk-z-oa3UdKkvUMHht-c9pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=v4___NQz1_L7QO504f67inq-HdjfOoSqyJQtZYpw_pz1VRr6NvJL1xKADlfDjq3pcdfAfSX47GTa3IFzLQ4IBuqtNO1z98vTPOwBKmZQ3Vt2d47OI-avpe-7FTCUXCUzrQZVziBLm8cLhBKw_RqgH0_h0ATex4sVNVNt6QxqMkPHRG8Q6trRn4T_7M98WYckBqPQEpTC7WvfsC0FfqZUSEGd8p9o4IWpThjfGamna72P4OOyJuujY4KfWbm147EgCbI7Ka-qjAUWAEGy53z3VPet6g2TySw1rSB1MHrLxkIC3Ryfs5YmhZdRJZ4hzXemk-z-oa3UdKkvUMHht-c9pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای ناموسی در پخش زنده
😃
⏺
امیرحسین ثابتی:
نباید تنگه رو از دست بدیم، نباید تنگه رو بدیم بره. شما می‌ گید تنگه رو باز کنیم، مفت بدیم بره.
⏺
شهریاری، عضو کمیسیون امنیت ملی مجلس وسط پخش زنده :
بدید برررره، تنگه مال ننت بوده که بدید بره؟
مال عمه‌تونه؟ مال کیه؟ ارث باباته؟
⏺
امیرحسین ثابتی :
آقای شهریاری ادب داشته باش چرا وارد بحث ناموسی میشی تو پخش زنده...
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68842" target="_blank">📅 11:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68841">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=E-V6V6TXnKbmTmATZcx07DOsIk0tM2V37j87OQYj2RIXicmNi0oMvQYOn8LyMslDh91OOxcHBGgpfHSSlWIvFEBgttUNfdWIZx7u2jSEnjdodHJG3An7f2F08XLq19tadhWP2BPwyVUlqANx7ReWNp7eUyDTkFwPR4pYmZedlsGvM4weqmLAn78hdmKMOt0nj0480OZaCqCgFtRZEYAF4uhU84YKBOyHdongQAZLLLpANZPwotQpjGDituLRO3nfd4kjvaFKcy08TAyfX-HAP_KMhEP_cZ8CONyfL9LrHblzs7s2CpDVPsSKjJcElgfNH8XIUrhCYFZ6HkGioxst3oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=E-V6V6TXnKbmTmATZcx07DOsIk0tM2V37j87OQYj2RIXicmNi0oMvQYOn8LyMslDh91OOxcHBGgpfHSSlWIvFEBgttUNfdWIZx7u2jSEnjdodHJG3An7f2F08XLq19tadhWP2BPwyVUlqANx7ReWNp7eUyDTkFwPR4pYmZedlsGvM4weqmLAn78hdmKMOt0nj0480OZaCqCgFtRZEYAF4uhU84YKBOyHdongQAZLLLpANZPwotQpjGDituLRO3nfd4kjvaFKcy08TAyfX-HAP_KMhEP_cZ8CONyfL9LrHblzs7s2CpDVPsSKjJcElgfNH8XIUrhCYFZ6HkGioxst3oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دعوا بالا گرفته بین قالیباف و افراد افراطی!
🟡
الله کرم رئیس گروه فشار:
بهتون اصلا اجازه نمیدیم به هیچ وجه اورانیوم بدید بره.
🇮🇷
مشاور قالیباف:
به عنوان کی داری اینو میگی؟ نماینده مردمی؟ اندازه حزبت حرفت بزن زیادی نگو.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68841" target="_blank">📅 10:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68839">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=mV4uuo_JrZo3DQt0NWHm9b0VSd5VirVhp4QwSBpLztsjGeRj3r82Ji690gR9bYAQbZ6wSYXm7_AXGMMufriVKR-YQgH4AH1U-QmHMnstC7pbKRJT79zENIkm81b3Ye9bz4jsnGdudYKuXNC2TvNs_y7TZsMsaGzBaXzmXdszyB-8GBeMJcSr4k0_Q1CIKTDLKNuexmeljYin48evz69fFaexwOzP5nPQnHbN_X4To06OlT9nI5H5W7hqqJAt-MBXTF0b2BpQp5QzEUhxyAgeJBt1MVgWgeYbw1YhLc2tD6zy_kvqi5v3ymixGrJ2XBQZ1Ylub0D1jc15VbDzUVpNew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=mV4uuo_JrZo3DQt0NWHm9b0VSd5VirVhp4QwSBpLztsjGeRj3r82Ji690gR9bYAQbZ6wSYXm7_AXGMMufriVKR-YQgH4AH1U-QmHMnstC7pbKRJT79zENIkm81b3Ye9bz4jsnGdudYKuXNC2TvNs_y7TZsMsaGzBaXzmXdszyB-8GBeMJcSr4k0_Q1CIKTDLKNuexmeljYin48evz69fFaexwOzP5nPQnHbN_X4To06OlT9nI5H5W7hqqJAt-MBXTF0b2BpQp5QzEUhxyAgeJBt1MVgWgeYbw1YhLc2tD6zy_kvqi5v3ymixGrJ2XBQZ1Ylub0D1jc15VbDzUVpNew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حمله دیشب آمریکا به پاسگاه مرزی شلمچه
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68839" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68838">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tvGOwIsY3YJ2sjiy_b8JVbDtXkbi974e1pjqyCTHdj-LTO57fiN5Uu3LpYQFvc5uR8GNbbG6FoovY3PROrj9W_FqfwpURx7jnbGVuOJbRt6qpz5JWxwkuRr-sW53RVL0geqAjJi3boNr4T9LNbylNqQJpQSo-G7urBGpTBWDpNgUfNFKsCtCn5OIZkNyWiEAnBYuokOf-WC-2hcPe4yewT-_sVbzMAZZ3Kr-Vo4NmUiqJ_Z4IM8F5nZi5YwS13YER1C2avoQnC39ue2Dz_8CI8NkE1r1Yyg5BoXGLfOmIcsixo7aK4sdqfsLNMTxWWLu18-9bR14gLSIzAIuNW1C5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس برگه صحیح شده یکی از دانش آموزا که امتحان نهاییش رو 0.25 شده!
در جواب تمام سوالات نوشته:
با این مملکت درس خوندن جواب نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68838" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68837">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYvJ3Zn-7dYUzwnuZ390YESEHW8ZowdUq6mmmz9qWdHdBKbCFc_z5bTxGoSc0B1oiyi3hcOv8EGMgJZJ11eOziMbynCTn-hfyEJxt_5lYw8bfoNISwv8Z8AyIpfSUGFr5APm2s38gnK0aGsPEDR_GAEHThlqzZu84GloNbkfB7tfeZX0o2j8gMR2avJGqWIXA65w5OA4dwax8RqWuaIN3uMFfGpWDk_6fGJuvS02Z8L_5_lLEwjFP1Uu63sgCxXC_7i6zRvvgF7K24RCAJesQZPZt9DsZ4A0fFHI0d1PB3avhOA0NY2Rd746P-03nlJ7nAkyCcrdyCWNQMAjCfWdpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👌
وال‌استریت ژورنال: ایالات متحده در حال اعزام گسترده نیروها، کادر درمانی و تسلیحات به خاورمیانه است تا در شرایطی که رئیس‌جمهور ترامپ احتمال گسترش درگیری با ایران را بررسی می‌کند، گزینه‌های نظامی قدرتمندتری در اختیار داشته باشد.
به گفته مقامات، ایالات متحده طی روزهای اخیر پروازهای باری را از پایگاه‌های محل استقرار نیروهای عملیات ویژه به مقصد خاورمیانه انجام داده است. نیروهای عملیات ویژه در مرحله نخست جنگ موسوم به «خشم حماسی» (Epic Fury) در عملیات‌های رزمی جست‌وجو و نجات به کار گرفته شدند، هرچند توانایی اجرای طیف وسیعی از مأموریت‌های دیگر را نیز دارند.
به گفته برخی از این مقامات، بمب‌افکن‌های دوربرد نیز در حال آماده‌سازی برای انجام عملیات‌های رزمی بزرگ هستند؛ از جمله بمب‌افکن‌های «بی-۱» (B-1) که هم‌اکنون در بریتانیا مستقرند.
وال‌استریت ژورنال پیش‌تر گزارش داده بود که ارتش همچنین هواپیماهای سوخت‌رسان، جنگنده‌های «اف-۱۶» (F-16) از پایگاه هوایی «اسپانگ‌دالِم» در آلمان و جنگنده‌های رادارگریز «اف-۳۵» (F-35) از پایگاه هوایی «لیکنهیث» در انگلستان را به منطقه اعزام کرده است. اردن و اسرائیل به عنوان میزبانان احتمالی این هواپیماها در نظر گرفته می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68837" target="_blank">📅 09:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68836">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⏺
فرماندار بوشهر:
روز چهارشنبه، یک نیروگاه در مجاورت نیروگاه هسته‌ای بوشهر در جنوب ایران هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68836" target="_blank">📅 02:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68835">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=F8v70G9d56cMsaAILNTYcBrItwxzhasnKWUYb_BhrqdkTeYnPUiNm1b7GQD39amRqHyLn0nkDxAB2PzGkZ17mkrVZebGR3vsQx79kEkm_y_eI2KDjOtkZoAx8-1GxqC8dBeRvAAO2x80y8GASMrGMEFUCuo-qRLpa0zEj6dtPzoSNxmCFjnA4waS7HgqyTvUXAWI2F6zv_aqp3t1vFO6iwpoVlmXkHGKevM2uOaSgTJ7pkN90CNHCDyBHMCthoFS2zCituHCmmreMCNQ-JkW5wgy8PsZg5lznobG7vdmU58cTno7f-0NY2tKqFhD3mtJ7R6Fmn42h87yQmSdHoOaBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=F8v70G9d56cMsaAILNTYcBrItwxzhasnKWUYb_BhrqdkTeYnPUiNm1b7GQD39amRqHyLn0nkDxAB2PzGkZ17mkrVZebGR3vsQx79kEkm_y_eI2KDjOtkZoAx8-1GxqC8dBeRvAAO2x80y8GASMrGMEFUCuo-qRLpa0zEj6dtPzoSNxmCFjnA4waS7HgqyTvUXAWI2F6zv_aqp3t1vFO6iwpoVlmXkHGKevM2uOaSgTJ7pkN90CNHCDyBHMCthoFS2zCituHCmmreMCNQ-JkW5wgy8PsZg5lznobG7vdmU58cTno7f-0NY2tKqFhD3mtJ7R6Fmn42h87yQmSdHoOaBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛مجلس نمایندگان آمریکا لایحه سیاست دفاعی ۱.۱۵ تریلیون دلاری را با اختلاف آرای اندک (۲۱۶ رأی موافق در برابر ۲۱۲ رأی مخالف) تصویب کرد.
این طرح شامل 95 میلیارد دلار بودجه نظامی اضافی است که عمدتاً برای تأمین هزینه‌های مرتبط با جنگ علیه ایران در نظر گرفته شده است.
این لایحه اکنون برای بررسی به مجلس سنا ارجاع خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/68835" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68834">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2tNQXdsJl_BCbeBiC32rulRrVU8ZHM4whObkqHdekJ6VXvxXm5JfvcfRrBXv1_k0pjfgi9ov-b9y_cbBDDGD9O-9e8OPUZFTwRHmSo0c3m0o5L1jDZVgCZHBvOuY_hHzPknyxjWUlc0-k4XX88rAYgVra0G_so7FQnZE8xI8bzll6aM8vDxKbbZUmdpBCGCSRh_idyzRUQCm1HP3O2j20DzAC-6BYQFzSdx7I1fomngpHq4TAzAX0VtIJhTsHCdBd9p262ctK5Ftpx3NKfJJqjxyeJhEvYblJzw2vBH1UJLbwGfpitNUqVL_Cnf4nNVTisMRCIqMBjQvMNXCJLbaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ستاد فرماندهی مرکزی ایالات متحده (سنتکام): امروز ساعت ۵:۳۰ بعدازظهر به وقت شرقی، نیروهای آمریکایی به دستور فرمانده کل، حملات بیشتری را علیه اهداف نظامی ایران آغاز کردند.
این مأموریت با هدف تضعیف هرچه بیشتر توانایی ایران در تهدید دریانوردان غیرنظامی و کشتی‌های تجاریِ در حال تردد در آب‌های منطقه، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68834" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68833">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدید حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68833" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68832">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🇮🇷
هم‌اکنون حملات سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68832" target="_blank">📅 01:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68831">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hy_MUwna_C4ZoRghF-GbSwekWSuwXpHCYDX9Awn-otcKQqcOpmunjWGqHuAxNZckowMDlPCOkn2GBB_cyRQuB7YDOB0z2FmiDXhypHecOZ7EepwwDyadRB8B4f_BgPszxPqbdKtWVhQpA6QUpTbqhaVWkAN0Avf2dLctj6cT1uCX82qk0frL9XCZ842s3DJbPWxdjjRTrFLgoMDPwdeMECMUH_kT-J467WQ5vtFEGlbADHSQVJ5BIIM7eeU3hnqKBXIbr2kPox5HLFNYz_zKucMvnAcO93M3VTuF8Jv1kJVPDCKwDkT_m-I1cY2tK5qPhaQkXqneqZmJxO-EFzipnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نقاطی که امشب تا این لحظه هدف حمله قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68831" target="_blank">📅 01:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68830">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk6_DbWoVBzgG8-IsnISwMIL7n6jKc3PnSyZhoeCueRjl1nzrwqj9wp0zaMByrD1hIW5shECnStXyGVMkTOhnIK30KZkVCcMmTJoNZ_YQi5UCUe2XDa4qazTEKJzDSlTjveg5PQculCV1Y5raqznwhafLkFCShO3dW3RTWcv_7uhWAvvp7wPgZ_TonvBnPmuFbnq3MI-qqm8baiuV4fYYbQwaBVzHZEXAz_DIOEoW_aGh3ItvB9a8qh-PYdAP1O4UM1ZAS9KwXxIgiVQMwXr9MXpFvEFwjkJNZ8ZTCYVDeYwPuh2nXHDbrE7v6QvYRoe3vE1iVcaU39y910MuEpScw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.  @News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68830" target="_blank">📅 01:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68829">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30afc95033.mp4?token=YHzUUeHs6RotJhHnlFNNwkzbj0Saod_VNwGOCLQWiD6FMy9Z8NRhkHU15IDwXQb8j_rjLsn2GaTMJsYt_5LPMGo7PrJwyA6oOS_OI7-4jgbkC7IYVk8wuFByrx8Zufe4X5HBiCLofI0st1_ByB7c8XnBaM1GW697Nw7usYKe0iLnqk2g9LNox9x8Kq0FMDtVMBsu_8B1b9RZh_8NK_eOHvzCFo6lB7bWkpNJYonrwHocNhHLxcZIXX3ynHmru6RwLXX6o_0eLmbf16H8KfbUL5nH-W1ueQGQwZFPBcbBbPBgdWFhZ8T1LrJmjdNY-yjamMlV04rJQihEFkRuqfvZIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30afc95033.mp4?token=YHzUUeHs6RotJhHnlFNNwkzbj0Saod_VNwGOCLQWiD6FMy9Z8NRhkHU15IDwXQb8j_rjLsn2GaTMJsYt_5LPMGo7PrJwyA6oOS_OI7-4jgbkC7IYVk8wuFByrx8Zufe4X5HBiCLofI0st1_ByB7c8XnBaM1GW697Nw7usYKe0iLnqk2g9LNox9x8Kq0FMDtVMBsu_8B1b9RZh_8NK_eOHvzCFo6lB7bWkpNJYonrwHocNhHLxcZIXX3ynHmru6RwLXX6o_0eLmbf16H8KfbUL5nH-W1ueQGQwZFPBcbBbPBgdWFhZ8T1LrJmjdNY-yjamMlV04rJQihEFkRuqfvZIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68829" target="_blank">📅 00:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68828">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
صدای دو انفجار در بوشهر شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68828" target="_blank">📅 00:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68827">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
فارس:
حملۀ موشکی دشمن آمریکایی به یک سولۀ انبار آسفالت در اطراف رامشیر استان خوزستان.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68827" target="_blank">📅 00:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68826">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZ7bw7L8DEa2DBhBs03f5qmKwf-Mb3OkWqDOQcs7wwNiMcRE7-bbRh1nlonpnXO3seavlTQYeNwRRAqx9h6HjFDyjaGJQLr1F8o4qDHKBwBMi-btcNiR16EqURrf8Rr5r5VYZGACkrA2gBNLv8ub-lsFl8KK9ENWa3SRyl3V_NlDQI6jxAAPECW7VYKCvOG--qG_sNQcdGeh7oKYaNUSw8j3ak_IicHtq3P5V0-GMBYBVDV85P5-q9vJeaDPnj-rWmJfHasDRfEtM0XxRt2D7d0F_T11WZOtJCqPmoiW1zQiXo3_g3zUPMr_jigxhoecqAF-66inoAX0GZYmESG15Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
یک جریان مداوم از تجهیزات هوایی آمریکایی به سمت خاورمیانه در حال انجام است، که احتمالاً شامل هواپیماهای تانکر سوخت‌رسان نیز می‌شود، در چارچوب آمادگی‌ها برای تشدید عملیات نظامی علیه ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68826" target="_blank">📅 00:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68825">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
پاسگاه دریایی زیارت در سیریک هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68825" target="_blank">📅 00:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68824">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
دقایقی قبل صدای چندین انفجار در اهواز و ماهشهر نیز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68824" target="_blank">📅 00:30 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
