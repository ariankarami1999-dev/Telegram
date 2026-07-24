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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 13:38:17</div>
<hr>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1iLxnnGDs6ZsKIbz_j_9RNFnuCt4XLZpfguYvHGiZ248i6qZU_0BonnNqQbMeUiBJYsqpgO5bIzZvTVCnBwlMxXPn_56ogkq2-b8HEvbc0kpOhNsxFtKNohShV5NnRbjVShJASEWE2CnlhldfWBQN26M4AF64mHVaj3dXdz1mXsBkeHwS8bh1GrFMAwiGeFROGSnEarMW_IWTkwcD7Jtkz3gUzSjXiCeVkF-btcXVHZyHgP3DTly7N6lsebQdQcZzLCSm1MCyfkRSBfrN6uiHDrDhXD_GESD2meq8ewDYwBpBHuRmvXprakjsOZVuqQORGLFCrbqlbzAtm9Ldkmlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu2hOnPx64uZ14BlnG_XdAIq6OuRaiFLMJeGDch5BhSLWaEfOfpfQBbmI1tdOiSCXOYWtmOMymi1gYCIEd040oT_XSlRgAnH35tquTTwk3tE7y4dfxiYo__Ff28b7hCyVNjeb_a8EkeB14sRc1euE73lEOX3Lzw_6wZgoc1HTfsyxChWEN_eX7Tp34h1sI_B8BbB7O7d1J2d3NDiVVaI4o3JNUqiTR0l-w6NZ3_bvWOjZL_SEW9s5r-l-RRlr0pimuvY-vBLMEAAzDQtqV3l6UEyBXViiZDw6mZzQeIpbKaOsLyUBfY3gkt5V8I1TFGGkADN1ztD7mai_sJJA58Fxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA1Ac1AYbaYlS-WlEXOiVNCiGZKoduUSbPo5Lu7h0xVYwreC6PspjyxI-E_An5mWwtyevvzeM9EWIbd6sdBVF3G34rqCexmSubMaDEDPMRQI7jU1fLgheECieyW634iImlsJGPWsd7ZFTDHtaawXVCdFOYT9UFbSyM8CI_tRVBlorZkp3lhWqrQtFS_RtTNS2LlrYCN6oYhuhrw3oY9f3AoX9-cJsy0fxqyzgptTHTnVOaIf4ZegBsPgu4ifWzbESdsR8CU0HQBgPA1NBYUhJpxJbAjo3a7sI1VXVBvepYPJqWgM0OZfzbLaN0ociDKgoPCG_C3B9jyFpKQCHkOxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_hVGC5bIO86xm2pt9LTQ2bupRJ_M38j9RWcGmxUkScQOiBWxxG-X0eOlGyfKzPSchljkI4B91FNZIB4SZ-7j0FVyi9FJQDXmhkkqkvSXSZIUsiYba1chrWAO_Yjmr1i13DLQHEmqUIGE00avT8vedWQOr67jxEzRWBP51et4FiNdK_vGez5bH28-_57EBOMfPT7350xR5rQsbKtn2-6zbr9iCrfwhCG7-xNraG7a3ebrBu9MxkPOwD_R47G_dpMYl1qMzIYRkTGEDWsmBiSubHAmx3LC3JRjiEOC3GUvGloltQKhunMPLdOMSQqv2QPNbxRb7GjWnT4lWRTCJv7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFKj8yn8H362oVB1V9haClQU8BpbLbRpoEon8R-XjTop2mRFc8bwKBFNSBEnI_2noGJ3EPfLwoKalJo_3FCXRbHcTLzuaqfNNsnfxVyw_3DAPS-nPhCQhm96R7A2PKdez5710xRO3-UHTLsPasjYsAFldb4TSxrYX9iilRMNJ2qUGPkHHBYgG-Vn6FWN2SyApUpGf4tt4XQQtBhmNZkl_LTRmPpjM8-4O8ye_aqx71i13-IFYVlVzZtMYAcMWgUJXyiJlpUreoB5UAhaHV0E-OigIrtgwTMgkQLb1iY4KyUuFOXRUoLYO0RlQ8QIexpjO2DdMEPB5QTtK6m_jPSrJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBXx1nuEfVJ6vBG8bdfNYkgwho5tdyWDZTwwpS-l2p-CyHlMjBTQk8rCYvwtRGD8DHwOoIc_3gGPiov3sSBxd0WQV9jCV6razk-ILg_Sy7VNAAIIQLlsrrAP_1yLv9sgmTKyWHW8j7su2w1IcdumQsrLaeAIhIOD_6YXGtBgQ_w32uZunC9e5iwr3FZ-9W5VWkzSYDqbY8wivX7AeUExNcDRLyCyHbfw-xX_aZoQ__ZthGXvWv26Z0SaGbUbm0POgCqdjX4NbphmzmVFBiKmZPGUDsUKiqRSSb1o5VN5o4o_7NVHMxSNGkUYoiPIfiukx6DT6HB7CEG6QX3FrDkY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=sbCbwbj4S4WvIlKu-J-0Ly_bapPIH8lG-rnrFobH4wtAxtZRLvdmckTikoRCJ2Huzy-jQq08k9z7zrs3Po71gC46DLnPmimeL4iSRfKoH5kTg0mxCM8bMQWei-pTv8O4EWkWT8P4_QLOtcdKxxc7U4jao-fdt0WgW6sDfz2ZN4aUUXFV58E0IWCZL3konUFwNZApc9NtYJToQgMK8eJZK5BxI8Lf5tHGuYwkfttIsdleOtozBuD8x5w6kxqT2hi7Toyz5J6qITTsWWjF1IrpnFLBuJKVr-T25WGOhBmA_qNjsVCzRyZ_IPmtEF0Vg2Mrb--fmVAoLcDx4zI5hHfl6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=sbCbwbj4S4WvIlKu-J-0Ly_bapPIH8lG-rnrFobH4wtAxtZRLvdmckTikoRCJ2Huzy-jQq08k9z7zrs3Po71gC46DLnPmimeL4iSRfKoH5kTg0mxCM8bMQWei-pTv8O4EWkWT8P4_QLOtcdKxxc7U4jao-fdt0WgW6sDfz2ZN4aUUXFV58E0IWCZL3konUFwNZApc9NtYJToQgMK8eJZK5BxI8Lf5tHGuYwkfttIsdleOtozBuD8x5w6kxqT2hi7Toyz5J6qITTsWWjF1IrpnFLBuJKVr-T25WGOhBmA_qNjsVCzRyZ_IPmtEF0Vg2Mrb--fmVAoLcDx4zI5hHfl6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68891">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68891" target="_blank">📅 01:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68890">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2lJSI6dvP-24kvbhCFWDMPLP0tYnXtrFCxYoXPezBSzDc74qX8HzrBuNIfr-dJL84safBIWc1tjbXPlq0Ok9rGaT0pgk6UA6uHGIkVNXAp6-BfRkHF1XNINqvdb-mgcMz3l-WC3bPVBHRj0PVmQ510HidSafPom0YlG65H9C3v4kkYL3xOmh80JGsCjOSdpnILq_hTaY3T-z21Y4EhWw5_pkU3bT4OZ1uVHVBsBpCT8ycC7cESUFwv1i07WQcSjXfbm0uuXY6Tbe7djAQAZ7SlWUM4H76aegg57Tnh1t6Ehe8y0wBqoVYT-70WHSDU1sGXt_CF5PAVb01OeHo3kKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:
لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
اگرچه ممکن است این خسارات بسیار سنگین باشد، اما با این حال، این اقدامی عادلانه و منصفانه است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68890" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68889">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68889" target="_blank">📅 00:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68888">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
دقایقی قبل دو فروند موشک در جریان حمله  آمریکا به محدوده روستای مسن در جزیره قشم اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68888" target="_blank">📅 00:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68887">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68887" target="_blank">📅 23:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68886">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlexratLHQdKxjhp0TiZMRi7PjATR-QupqOGeNyQfq9ZAt7GZj1gRLMg_nOzWxZCzFq9PJyfdo03M7kSDTAuMf9WUglCSa_q-jJE5hcaJtWIiPSy91IOwpV03uC7xhkV7dtsVfqkh3NzZlRB0T6NNGSNg4x6ow_nnzunhbz3WB2bG2LlGK-VytBfRMkMIi6fepQ0WVg4azbGx9vYJg1V-ejDTJNxK_U1b3sjouIJPuMyYwtgkmHupnFTV0G9Cy5ljpQunMrW7Vl0-AgDeX4uPWV6zIovQDqo9yusGagWywzI5uQpW_E4x-P28NSh3_DStSgf_O8YqFwU8POqtfQ_Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک دیپلمات آلمانی در گفتگو با شبکه «فایتوکس» (Faytuks) می‌گوید کارکنان سفارت این کشور در ایران خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68886" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68885">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن  @News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68885" target="_blank">📅 22:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68884">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68884" target="_blank">📅 22:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68880">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68880" target="_blank">📅 22:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68879">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇸
ترامپ:
کیرم
تو هرچی کمونیسته
#hjAly‌</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68879" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68878">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند  @News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68878" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68877">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68877" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68876">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">همین الانم ترامپ داره حرف می‌زنه
#hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68876" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68875">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اگه امروز این قطعنامه رای میاورد، ترامپ مجبور بود جنگ رو تموم کنه، یا اینکه قطعنامه رو وتو کنه! #hjAly‌</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68875" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68874">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.  اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68874" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68873">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68873" target="_blank">📅 22:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68871">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68871" target="_blank">📅 21:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68870">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68870" target="_blank">📅 20:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68869">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=YmQiEMn9nj-X2AOAahnoBRPzCtV6lBVA5xa727PY8N5ghM709Kr6_vFXdsqYyBI9_1h0tJQ5iztdv20-rGhUIOPedX3nNCOBK6Jz5OdL6LofQKXonNzTLRzLEJoVrElsjZTEupKOiuJOVdGpR0M_VSA97t-gPD8e7ICEjbJ0ZiIqOMXPb7ZC_doaNCDw7or-KXMAzH3j9Jch2sPkuuQkQXoVoHX5HnahBn6EJGoOiH6vbRYECPnKpVCMDTy52Ws3e9ZfM9GigsRm0B_hwBjjkGEzkUuLUGp3lvRsiXtdaEBXO8a7MRYWPQ9GqyRnsFiRWQpnp2TwwIRMdkN6Fbs__HVvzXQs1QEGevQgWPbSfe1Sb5A10utvuVd-IJinWQZqb5uXZ3j_9u1wBoi-2MEtberBGTW4aL8E0DmQGLVz4Iga6tj-XE17RkDGbpq6MjvcZYDa8ImQDhkTKDQ8ueHWSU2FmTvSaEYTl0Ji_cKw7dKNCbwBJ3spmQadvmdX6dsF8OjSriKlCJqEKsATpTngMkEACQIuqtRzY5GDQiw0eFPtFRD1TDz2L2cDbtCOf7B7WSpW5t6cC6Q7X0DJa6Nx1qKZeQRXhqQtUzolGEi6C3G1O0AZGArGlOkxxma9bPEVwqUP27jOrRt2-jNKE3GAFJqr4ZvCcJVAiOx1EYPQ8yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=YmQiEMn9nj-X2AOAahnoBRPzCtV6lBVA5xa727PY8N5ghM709Kr6_vFXdsqYyBI9_1h0tJQ5iztdv20-rGhUIOPedX3nNCOBK6Jz5OdL6LofQKXonNzTLRzLEJoVrElsjZTEupKOiuJOVdGpR0M_VSA97t-gPD8e7ICEjbJ0ZiIqOMXPb7ZC_doaNCDw7or-KXMAzH3j9Jch2sPkuuQkQXoVoHX5HnahBn6EJGoOiH6vbRYECPnKpVCMDTy52Ws3e9ZfM9GigsRm0B_hwBjjkGEzkUuLUGp3lvRsiXtdaEBXO8a7MRYWPQ9GqyRnsFiRWQpnp2TwwIRMdkN6Fbs__HVvzXQs1QEGevQgWPbSfe1Sb5A10utvuVd-IJinWQZqb5uXZ3j_9u1wBoi-2MEtberBGTW4aL8E0DmQGLVz4Iga6tj-XE17RkDGbpq6MjvcZYDa8ImQDhkTKDQ8ueHWSU2FmTvSaEYTl0Ji_cKw7dKNCbwBJ3spmQadvmdX6dsF8OjSriKlCJqEKsATpTngMkEACQIuqtRzY5GDQiw0eFPtFRD1TDz2L2cDbtCOf7B7WSpW5t6cC6Q7X0DJa6Nx1qKZeQRXhqQtUzolGEi6C3G1O0AZGArGlOkxxma9bPEVwqUP27jOrRt2-jNKE3GAFJqr4ZvCcJVAiOx1EYPQ8yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فاکس‌نیوز در حال بررسی فهرستی از اهداف زیرساختی احتمالی در ایران است که ممکن است مورد حمله ایالات متحده قرار گیرند؛ اینکه کدام نیروگاه‌ها ممکن است هدف قرار داده شوند؟
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68869" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68868">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDcVQSefpQZkDjcPpcJZtcstnUnOwaVitfZ9cW26C7NFTAsJYcjJHo4oVMH0s4xCEPBz-pi08TxaBL2jTMNjK9G3dBXefBIH2wuZjGtHqcxfPDgSTQJbcgyRTCuBWvuReXL7rAvm_BqSk5IQbaQeKGp70xbfTyn2SuDGa85gRuR3VuD5o-lpZKw6o42eGS-GbvwgQqX26JbyLe7BL7P0TXzct9Qj2kR09PRNh9XiLvF2mdNi8FRlLjV8cJyRr6_pCQq0cWCUPFk9Y2rL5xu1CdhiSQnnLMYcp6qJtlI-_abofCwvN8Mo4jYZ_GK5tTQKs7wyZPljrEvIheK9JI3MMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68868" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68867">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IirWxmcJZqX9bW0GoAkmO4mvb58vqGHFNegcMT_ctnpqDy4dUy0Z5STPKm9xjA3dOTgnNR-oz-kz6p1YzdNTwozHc2ivkPhAWxkyurWNH-roQomrIvMWdS4X2tfL-6V8ynOkOXkkDdViPnPd5bUQYvskv0wAsWJcfH71u9h6f1WjmQtGlMvTppoxOS7meqm8_O4_niyzIGYEKdQUE9qirLm08zJ9Pt8Xm3wPNiFRX5EfgRsqW--ZrgauAV6Za7jyy8Cc8_YaWWM_BuVWds1p8FJdfkPU0o3ZkKgDPjm6Ze20cJnpxAg5lHOmnFKhDF-Jp5r7i_sTUsqUihJy-bme8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
آنها می‌خواستند ایران را تنبیه کنند. در عوض، خودشان را با نفت سه رقمی تنبیه کردند.
استراتژی ۱۰/۱۰
👏
👏
👏
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68867" target="_blank">📅 19:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68866">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=v0M5Pbzcm75zedJ-k20nZpWC2SFxDMSD7DpYG79jokAm2IqBQFa4N9qNilbovJ9N1lzxh9XiD0_BAdfiSxbQDF1DsAh28ysOGraUzzBwgryPEdXRL3gbSMzyX7QWE7Zdzwl0AL1DbMsnk-4hBT4wSbAutppkKNhjy8nnKVgNazo5quz6NVXRuRzth5bJ4Z4TgLi93omkYtDELv4BHoFflgQggSLF0_HaRyEx-bNIvdeRt0KdyqJk3_8OiOs7Nci4QT8vqz_EE-wmTvQgFGxBYCmXeAcSYD9LB0wDkc7_YweCb56aC71kZXhU22UHCLc5iFtWHS63wtMhbJs_4_Xjzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=v0M5Pbzcm75zedJ-k20nZpWC2SFxDMSD7DpYG79jokAm2IqBQFa4N9qNilbovJ9N1lzxh9XiD0_BAdfiSxbQDF1DsAh28ysOGraUzzBwgryPEdXRL3gbSMzyX7QWE7Zdzwl0AL1DbMsnk-4hBT4wSbAutppkKNhjy8nnKVgNazo5quz6NVXRuRzth5bJ4Z4TgLi93omkYtDELv4BHoFflgQggSLF0_HaRyEx-bNIvdeRt0KdyqJk3_8OiOs7Nci4QT8vqz_EE-wmTvQgFGxBYCmXeAcSYD9LB0wDkc7_YweCb56aC71kZXhU22UHCLc5iFtWHS63wtMhbJs_4_Xjzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العدید هم که تخلیه شده، بنظرم خودمون رو آماده کنیم... #hjAly‌</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68866" target="_blank">📅 19:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68865">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzzqNZSsDemk4P17C7VKXuwC-ZG9Mr2QcWG-HXOnKy_724mECpWWg_qwAYCn0K1R0aeJ-Qg_vFuQvgho5x7fbyz80u4oo8jbi-MjuhmPnew0oMv1qPQkqljvCOpldVIfCqSZNAUWOXJyqjlD1rB9LnNW--yOFokk6xDwiSMAjYN0DAm6bg0zM9F8MbMFzzfoE6zLgcIkLVQUy1pUl9ADIKnLddwSWEHWZKCSL14r_-O8c89VIOOQSw92UQj1kPs5FmDS7ljFgd7xebfxXe3_fRmNgKZZGdJXNkvMUAa00wXu1pOz2w98jZh2VC79lG1UH8895BbUmwI48vM8s44YxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین نشونه های نزدیک بودن حمله، تخلیه پایگاه هاست</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68865" target="_blank">📅 19:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68864">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ همچنین گفت:  همه چیز برای این حمله آماده است. اگر از اسرائیل بخواهم ظرف دو دقیقه به ما ملحق میشود اما ما به هیچکس نیاز نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68864" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68863">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری؛پرزیدنت ترامپ به کانال 12 اسرائیل:   من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.   @News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68863" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68862">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDS6Tz6e9sWwttYn0ufWZnuCkokxMAETbx1zN5oN_SDXRTyF2E3cE8XVDQuObUD9P6gdAjlqNqLUIyX49_RU-hrpnyLy3DYsSmhBsZyUIKuVegIAKrD32zmxsQas6hesTArtLQhnjTsflM5l-zXvAmjwlVqpBqJ5TxLpXJT57tbSgwqXJ2eQrPlPaC6qf7jm31XnUEpcUB46-YVt_ddRNPEuo5DVvJg-Y39fo6IomBBPOzdTT9YhAvLmaFcn4kEsOmFpwYSLBhfseniyBMUBV1hm89AWcSsQnozZCjKSxkOKEduUEvsFXgOjYc5R1HH1mfL0uSPyZXVrPECs03fsCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛پرزیدنت ترامپ به کانال 12 اسرائیل:
من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68862" target="_blank">📅 19:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68861">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=UMkcPPx5NRUz4Lpy1KRbUidTLBGT1S5uA_rqB8rpaX0-vkK4NKHgtSMLQp5aez5fI6xyGXjZOV9474m0k7vnMTrWl3aJMjFwaYdFeN8-VBEcEgqLGxZADAlbnzCXJeh-dWG7bWrxcIpfewtrW-TPTXcebmROO0J2Es8bsTkMWj3I3w3qJ6X_e3ueQdpVlbWXorkL7JenHv1v5Tv2PLAkB5XnhxRHkzKNyESetjlWBmTYCMefwuTmw8U0bDbDbmN5kIggEYSmH0_DaNRZD9CbIyf-J8-egYFAl9NUb0WgvapdWv1xkAupsWZy8IAN7_PWtqpfsMzs7yHIUWg9FMMYpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=UMkcPPx5NRUz4Lpy1KRbUidTLBGT1S5uA_rqB8rpaX0-vkK4NKHgtSMLQp5aez5fI6xyGXjZOV9474m0k7vnMTrWl3aJMjFwaYdFeN8-VBEcEgqLGxZADAlbnzCXJeh-dWG7bWrxcIpfewtrW-TPTXcebmROO0J2Es8bsTkMWj3I3w3qJ6X_e3ueQdpVlbWXorkL7JenHv1v5Tv2PLAkB5XnhxRHkzKNyESetjlWBmTYCMefwuTmw8U0bDbDbmN5kIggEYSmH0_DaNRZD9CbIyf-J8-egYFAl9NUb0WgvapdWv1xkAupsWZy8IAN7_PWtqpfsMzs7yHIUWg9FMMYpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68861" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68860">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3008b12665.mp4?token=N5_KFTE7OuARNsR-xNA6QgawdjTjN61CW3ag-xSqnLGrNVBK4tVXZRJNIJ1Leb2PWOjw9pGbFfAaBy157EfMXU8eJHaDqY8otTNQOiKwkTNPk8yXafR3ZQSryJd2dZ3xUycQigDTMIiOaCEQ40bHs2wuSn3AsvxM-WQZ5je1t0e6hWJbU6zQ3u3-TdsekjZC2dg6YU4FM0G-3cAbngtnq6vwokiwiQv9pt5MwqesDSOmtdNQp5p3lwxw-ku9khmoBL40POvYjFFkgfN4Atgox6I3khUiPcMaDeOmMu4BA1mjAALek21-fXxDvmu-4VCxEv9DjMCr9vpWC8NfCZuXOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3008b12665.mp4?token=N5_KFTE7OuARNsR-xNA6QgawdjTjN61CW3ag-xSqnLGrNVBK4tVXZRJNIJ1Leb2PWOjw9pGbFfAaBy157EfMXU8eJHaDqY8otTNQOiKwkTNPk8yXafR3ZQSryJd2dZ3xUycQigDTMIiOaCEQ40bHs2wuSn3AsvxM-WQZ5je1t0e6hWJbU6zQ3u3-TdsekjZC2dg6YU4FM0G-3cAbngtnq6vwokiwiQv9pt5MwqesDSOmtdNQp5p3lwxw-ku9khmoBL40POvYjFFkgfN4Atgox6I3khUiPcMaDeOmMu4BA1mjAALek21-fXxDvmu-4VCxEv9DjMCr9vpWC8NfCZuXOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68860" target="_blank">📅 18:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68859">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🇮🇷
هشدار سپاه پاسداران به انگلیس: بیش از این پروندهٔ خود را سنگین نکنید!
به رژیم پادشاهی انگلیس که عامل اصلی بدبختی‌های مردم منطقهٔ ما بوده و سوابق سیاه تجزیهٔ کشورهای اسلامی، کشتارهای گسترده در این کشورها، تحمیل دولت‌های استبدادی و بدتر از همه سازماندهی هدایت عملیات اشغال فلسطین و تشکیل نکبت اسرائیل را در پرونده خود دارد و بیشترین مشارکت را در تجاوزات آمریکا و رژیم صهیونیستی علیه ایران داشته، هشدار می‌دهیم که بیش از این پروندهٔ خود را سنگین نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68859" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68858">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tS2wai8eTaHDh9QWtKq3f9C33yLYYZmFJn7hxWFC6TbI_PwoW4xiGURcdTJnanewToiD6R2h942Cdx-N_mmI1wOgsovbiCEV1ucNNoAFm71q2V4v8STB1rv07H0r2-gTCsnKpSmlVxYA2ZC5a8AWfwBCsuE75siZ2KKRXWDFeQV6JlcAAfoMWIg-wLGSEGBjMzbuT3Q3LlRwVuTgLhxwjHW_iNyILAQknvVMPW4j35S45lkTsoLUJt_JZVmMHrcUEeAo6Gct8u5ql-rg9ow-J1zv9HEjqU9boosZ4IkrViVnI-jlO04RUbqESKSmrMBjEfUCcovofr_cDnddkkFF0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
نفت برنت بعد از تقريبا دو ماه، مجددا 100$ رو رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68858" target="_blank">📅 17:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68857">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJFbJkRczdQ3d3wMp_fZyC0yhXnjwp7RzkkPszlARwREXkO0KDw5GithnPUiDoT-6yjJ8DL3NUuEwO3PUP-mM5-gIi3d8txj7vBNqdNF1GtOWtlcKNWCMKwHa5S-ZPChR-MP6V3KbahPtceSZBuWdfhZaQb9gOCBxcUlMsDwhNjwSfSLArYo3rEqODXdjw9eZlkgwTih2IC4959QFtwbALiysksdW2tDthxAnnpsCZi6DhP4zQibSxE9fMSFXbvWA3LsGHOFy-rqmjYBitCLx9oPbgAdTUFL73rh_8ECtScoIdlrrH6V06AfN9YDna-grOWW93FVnjUjH-XAbp5kQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس:آمریکا هم‌زمان با تشدید حملات علیه ایران، بمب‌افکن B-1 را مستقر می‌کند.
مقامات آمریکایی اعلام کردند که ارتش ایالات متحده روز سه‌شنبه از یک بمب‌افکن دوربرد «بی-۱» برای حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران استفاده کرد.این نخستین باری بود که ایالات متحده از زمان ازسرگیری درگیری‌ها با ایران در ۱۲ روز پیش، مأموریتی با استفاده از بمب‌افکن «بی-۱» (B-1) انجام می‌داد.
استفاده از بمب‌افکن‌های «بی-۱» — که قادر به حمل ۲۴ بمب ۲۰۰۰ پوندی یا ده‌ها موشک کروز هستند — نشان‌دهنده تشدید و گسترش قابل‌توجه عملیات نظامی ایالات متحده بود.
هواپیمای «بی-۱» (B-1) می‌تواند در ارتفاع پایین با سرعتی فراتر از سرعت صوت پرواز کند و در عین حال، سنگین‌ترین محموله بمب را در میان انواع هواپیماهای بمب‌افکن حمل نماید.
در بحبوحه تداوم تقویت قوای نظامی آمریکا در منطقه، رئیس‌جمهور ترامپ همچنان بازگشت به عملیات‌های رزمی گسترده علیه ایران را مد نظر دارد. مقامات آمریکایی و اسرائیلی می‌گویند این اتفاق ممکن است ظرف چند روز رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68857" target="_blank">📅 17:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68856">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=r6hN0bd3VP3w2Yhw2-B76yZ5xTjdj8e30kpO_r2oYsTYbB7iRqQvII67LKx_Zhf2WaZuhyleaYKJ5kvKgJ5-LxIusZTsrLZ4K0IgJcxAdIVnG8eBgLBz-FzVGspFPSKvfciRN7WqhHhZKURjlkx32nXfu1TMP5jUsdy2-YdnEmgBdyW5CP-PUzW6zic8dhUdWuApl4x9KpYpLXOq_5C5UscBx8V1XH-D-2RiaL5jBccT7yuqLFtenmwiy9MEkS7w8UQ5IvzDq7j4_ZMycSeXW3KTemDvv8zr1vcgKedgJjpIf04GiTq2noiVYmkEf2FFPoOfyGeGq4iXcyttaYsr7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=r6hN0bd3VP3w2Yhw2-B76yZ5xTjdj8e30kpO_r2oYsTYbB7iRqQvII67LKx_Zhf2WaZuhyleaYKJ5kvKgJ5-LxIusZTsrLZ4K0IgJcxAdIVnG8eBgLBz-FzVGspFPSKvfciRN7WqhHhZKURjlkx32nXfu1TMP5jUsdy2-YdnEmgBdyW5CP-PUzW6zic8dhUdWuApl4x9KpYpLXOq_5C5UscBx8V1XH-D-2RiaL5jBccT7yuqLFtenmwiy9MEkS7w8UQ5IvzDq7j4_ZMycSeXW3KTemDvv8zr1vcgKedgJjpIf04GiTq2noiVYmkEf2FFPoOfyGeGq4iXcyttaYsr7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاره کردن امضای ترامپ هنگام شلیک پهپاد به سمت پایگاه های امریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68856" target="_blank">📅 16:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68855">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:  یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد. از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه،…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68855" target="_blank">📅 16:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68854">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHMGPViKE-8zr0Fnw2lzckHWS6MjKkaDfKZpwbI1hd14TZI00I2U8WMtLHjUS7cbxh23qO4YhLZH4XsRRbOetbykRWBUXqk6KTNxzb0mdmITu8gAO75b14yR2eG72neEXB60I-vSkNc2U_kxyuA70fWBBddkIkQe4S8FAt08nndlAj5J3SvpbFHYsvEeUfsoVSYL9VYBVKtOpGrc11ckBgL8dnUTPHCyEI5WuI7shU5O2rn7cud4PEBogWaCXBet8qm4ioybbMC-YVlvXd2DFcNRGUHDuwnH29xUa4xKnPpSyQATZaB6Hg3JQChC8y8NYFDarf8Ekbi1z3UIl1lMmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛فرانسه در حال تخلیه کردن کارکنان سفارت خود در تهران است.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68854" target="_blank">📅 16:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68853">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBdHVPlOAvcIdLHpy1puO0RUeoWv6TRagsaFBvbHGGyxeKtwmoeCufG3JtwMDF-DN1FgEq9qpJ4D5fH4AhFqtvA4PwnPQT-6jfQR-XX7dYjTY3T1Z2bgknGExM5ZoJHLtROHu9C28D5_F_lHpJOUuKZE9qDFmgI-cIxA1cGl2Qo2UeZi95IwGCbk6cnmFfce4VRPP_ZLgvh3FUVF7-lGeMJqSVElgprlydgvTdyYfKX3OWHS4mcVdiQy7CA_W9pWVBX-LijrGleGd6010hOpCKU3nytFqUiUcJqOpsVrd4uvHVrbyefHFSFciA7WtPHkhZM1wYSTAq00QDhg_2H06g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68853" target="_blank">📅 15:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68852">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYQH17Wbi39rUt2hx2_-Dldv9LPG1Z8ltiiyFMusIa-QCZqty1HEhgUvxXT_BwAD8vizfg3Tq_pPBPIwdVVGSxTsvq-cEgD8wk_QsyCCacGXcE1elE17Zsp8ZjEDQdxtmza9ZPl7eIUAk7-bsyX_hyp-Dkhbh2v_zh10O27qj-xcQmEWxdVZ_jrvmp4GraHHXgl5KuRR-GXn0bzYS5zocE7cItxesoWb8B_s9GjuoWY0Hh3oK2oYSplxZZ10o0Y65kFUpDPLEMImHMRi7YydltYlRtZXAzldI9tkyBsfbSqJyMlyKfpdt85dWPxle-HwBacnZsQZJrf80SOd91gkqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توافق هسته‌ای غیرنظامی (که شامل هیچ‌گونه غنی‌سازی مواد نخواهد بود!) میان وزارت انرژی ایالات متحده و عربستان سعودی — که صرفاً به مصارف غیرنظامی، مشابه آنچه ایران و امارات (و دیگران) در اختیار دارند، مربوط می‌شود — تصویب خواهد شد؛
اما این امر کاملاً مشروط به پیوستن عربستان سعودی به «پیمان‌های ابراهیم» است که بسیار محترم و موفق هستند.
ایالات متحده با تأسیسات هسته‌ای غیرنظامی (بدون غنی‌سازی) مخالف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68852" target="_blank">📅 15:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68851">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=qRLnSp5cQOO0qrRlif-pGjPsJGuxgulnBC7ciHChABSD4yT83fdjiQo8oop84OhT9SWBG0SRT8-fCgskG6CPk5Kp_8RtE024u5hPye63ruZGF6xonBepMvXgJJ_LkCmk7SbxTRGVpdD_IaSKlXIOQSe02mTeFxcJv7nFb8FnJIpmGMkEmnobKstulRo3r8d5Iz1hX8H251LNSpJTJCpA6LE0L5o1pXi_AB9BJeTNdqIXxzg7eLmw20HYWW3mWalJlixk4rDoWgQKTtT21DLICRTcwcfbwX4RYCeTdB8SVTy7tgEmCChf-8DjMnfSNNvuBfKBZP5dJqFx68UlHY0JjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=qRLnSp5cQOO0qrRlif-pGjPsJGuxgulnBC7ciHChABSD4yT83fdjiQo8oop84OhT9SWBG0SRT8-fCgskG6CPk5Kp_8RtE024u5hPye63ruZGF6xonBepMvXgJJ_LkCmk7SbxTRGVpdD_IaSKlXIOQSe02mTeFxcJv7nFb8FnJIpmGMkEmnobKstulRo3r8d5Iz1hX8H251LNSpJTJCpA6LE0L5o1pXi_AB9BJeTNdqIXxzg7eLmw20HYWW3mWalJlixk4rDoWgQKTtT21DLICRTcwcfbwX4RYCeTdB8SVTy7tgEmCChf-8DjMnfSNNvuBfKBZP5dJqFx68UlHY0JjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو فروند هواپیمای «EA-37B Compass Call» صبح امروز وارد پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) شدند.
این هواپیماها که بر پایه بدنه «گلف‌استریم G550» ساخته شده‌اند، جدیدترین هواپیماهای جنگ الکترونیک نیروی هوایی ایالات متحده محسوب می‌شوند و مأموریت اصلی آن‌ها مختل کردن شبکه‌ها، رادارها و سامانه‌های فرماندهی و کنترل دشمن است.
در حال حاضر تنها
پنج فروند
از این هواپیماها در خدمت عملیاتی قرار دارند و قیمت هر یک از آن‌ها بیش از ۳۰۰ میلیون دلار است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68851" target="_blank">📅 15:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68849">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWUvXnkv70Dr79o5qEMYsK-PFn3J-NwMfVD7urcdjhwxkUIvzWb7qah5MhY7Hqn7EgUWX_uY_dVMm51GwfPNR5ju5Z45c4iqfelLFOYO-FkNitGATaitskqM79OeeMcIix_UUphwgdBooRBpGf0k-jdZzqXt8-Sp2kAZfjmyUZKXm_HzhjsTLtst9xZH19vhY6i1w4cbyvbiNBIX2hxbP8w7IYQmWJo-Wqbw_7iyr7VESZW9svDbptYhDvEBQUJJ1mlD-iX7_yTEOB596W4e9Rzhyathl4lW0QfBasNQZfCuA4enPMski0qR6szB1NE0gW7vpcrogrqKv97blSN3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=YsPOdgcdGhwwBAQ8PeN8uXlWSfoZ2CF6Tc-gJFnQZ31Mmmxvyz4qEZLOwHU3X9_0cVoSyEOEfMqA6SuV8Bc9bThzFgETl9xVwtE_fzO4P4cua3vdaLHOLiiC66MeaTU_De8zZs7PHkIjX5M2kF5c6e0Tr9t4hhJXxI_2FZ7whk7eDK3U0a1G-e_wiWa0qGY-nwiSZNkx8DwWnSkImSZJJOu0IXjbYg5ejMbCoDlLoUTASRWjeD0tmebxcRT415IaxpwvwBXnwWoRqfCGK7psWuiNho5ZiUFcuX8adQIVM9chrewt1-51U4a4fh9PQl3KImHmE4AoAvx8gYHBZk-uWrTbS9ZUfnRbZiw36OJ7stWr7yGiljv9E2AwM4gUY5jzIj6Co-8TMYjv6wXyvTZCz3TpN0iNHmKVXtgQ0UHBRyiTnGvgs8wHJJvjTgmOQTU8k1yX-gOepcIKZveLjEQG1UJp4bQgD7L0ap6nO2qDmNrR-LMteAP7rCS7GrOQr1WT2WeK6qVY-kXlwSPWyiCy8Fn6-zaiUStI_x2RQQO8MQtlkv9q22Vz9cMJVpw_k_WjiyPlO_VlPPRsPJWHhgGUiauBTF0ii_FYRh-bb6o4FCtzz0wMgYmPSApPPGcbYtiCeWVsy6i5V8rQS3HAfHIxUOO_iKQGoiLgjwq3C6CiAuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=YsPOdgcdGhwwBAQ8PeN8uXlWSfoZ2CF6Tc-gJFnQZ31Mmmxvyz4qEZLOwHU3X9_0cVoSyEOEfMqA6SuV8Bc9bThzFgETl9xVwtE_fzO4P4cua3vdaLHOLiiC66MeaTU_De8zZs7PHkIjX5M2kF5c6e0Tr9t4hhJXxI_2FZ7whk7eDK3U0a1G-e_wiWa0qGY-nwiSZNkx8DwWnSkImSZJJOu0IXjbYg5ejMbCoDlLoUTASRWjeD0tmebxcRT415IaxpwvwBXnwWoRqfCGK7psWuiNho5ZiUFcuX8adQIVM9chrewt1-51U4a4fh9PQl3KImHmE4AoAvx8gYHBZk-uWrTbS9ZUfnRbZiw36OJ7stWr7yGiljv9E2AwM4gUY5jzIj6Co-8TMYjv6wXyvTZCz3TpN0iNHmKVXtgQ0UHBRyiTnGvgs8wHJJvjTgmOQTU8k1yX-gOepcIKZveLjEQG1UJp4bQgD7L0ap6nO2qDmNrR-LMteAP7rCS7GrOQr1WT2WeK6qVY-kXlwSPWyiCy8Fn6-zaiUStI_x2RQQO8MQtlkv9q22Vz9cMJVpw_k_WjiyPlO_VlPPRsPJWHhgGUiauBTF0ii_FYRh-bb6o4FCtzz0wMgYmPSApPPGcbYtiCeWVsy6i5V8rQS3HAfHIxUOO_iKQGoiLgjwq3C6CiAuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقوع انفجارها در گذرگاه مرزی «عبدلی» میان عراق و کویت، در سمتِ بصره (عراق)
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68849" target="_blank">📅 14:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68848">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alElQv2BA82d5Nd7-Ta7RyK7GbwJ_9Co4ixi0xAOChdWZC3m7Q2CkqkcjEw6OvX-jWeKrORII6zyMTAmbOs3SRBFK0GDW_5e7l91tJeQbyKOTaaCQUl62Fyzu3hVd8FhaIWv_i2cbGfz-TFxnT4lgHTIiOUJbuYX0Qi3QH9GWLfU-L-fiEIDsqPKISaWWCJDlsvTVMRQ4imUzd9dEdfjoU_TkZykdOkkYkYl5wy0Qz1sw4FOMYUmIsHf5VaAcS6H_s9sGeMkaS8nYYor2lVvTSq6KAi4lX-zneZZTp23SbfMewei-NqG41sAFfv49z2vIrCsPxL6VcCwY13MLQcuNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابوالفضل ابوترابی، نماینده مجلس:
دولت مسعود پزشکیان با ارسال ۲۸ نامه به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، برای مذاکره اصرار کرده و او را «تهدید» کرده است.
قالیباف و پزشکیان در «تله مذاکره» افتادند و «باید به عقل هر کسی که الان حرف از مذاکره می‌زند، شک کرد.»
اگر جمهوری اسلامی «دو هفته دیگر جنگ را تحمل می‌کرد»، آمریکا و دونالد ترامپ، رییس‌جمهوری آمریکا، پیش از آغاز مذاکرات «همه خواسته‌های» جمهوری اسلامی را می‌پذیرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68848" target="_blank">📅 13:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68847">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=BRP14RAMnf_nM07u8hVeDoIbMOZmhKwuR8h6hpSQ1uoZvzJRv9N6Li5i7F9WzqtzP-XdX2RIoIXwSt-MG77kka7KQjSuE4pQdA9z7nB2I9f2-ji4gHpmJ97Ps52QQUD2BUaxzQY09apgM3i5JJVOZQRsPXfpeG6AepOqAqA7L1H2RIBKg4PJ5K2oQAHEHCsXDW4iG0kIqTJAnzp9OOP75UxKyfQqNsw0kQpcmahQ6iShS7QpBSk0Dtc7GX0zN18b9xhLmaFrB_ji9TIOdgbGpsF5vtqVFwJw4WR5DM836bier4ujYYY3Jh6NTIvTkyXM2LMndJpGNOBB7m2bAtL6BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=BRP14RAMnf_nM07u8hVeDoIbMOZmhKwuR8h6hpSQ1uoZvzJRv9N6Li5i7F9WzqtzP-XdX2RIoIXwSt-MG77kka7KQjSuE4pQdA9z7nB2I9f2-ji4gHpmJ97Ps52QQUD2BUaxzQY09apgM3i5JJVOZQRsPXfpeG6AepOqAqA7L1H2RIBKg4PJ5K2oQAHEHCsXDW4iG0kIqTJAnzp9OOP75UxKyfQqNsw0kQpcmahQ6iShS7QpBSk0Dtc7GX0zN18b9xhLmaFrB_ji9TIOdgbGpsF5vtqVFwJw4WR5DM836bier4ujYYY3Jh6NTIvTkyXM2LMndJpGNOBB7m2bAtL6BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه حمله آمریکا به حوالی بهبهان
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68847" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68846">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOE4ndx8ohgUFFEvjOw4l9BeMQnrbZk4bxpPANHUAg4niIWnDJpKNx10C0RnPJ1uCR4jgykgJrFm7piTQX8z-uKWyJMZ8TCpd_D5Bp6mQ13-KkWYBEpDmu8h3k4s7XLkEz7yRiSqAj2y-XNC3rt43qkG6EXlVO3G70aIpds3P5qABrUSYncqLdlCX1G9zeOJ20i_vUndbd5hTodK83KUfZWo6p8FpMNdCybgu_KkammyyOrZc4Q2_9WcWvuTDDd620TUWycFcd0pFlkPB7cGnQzZ5CkepB1R9nAqjlfX15oVU95iGm-6tcL8wUSTy3CvaKY0tZkDsmtE7mV-lzGmlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68846" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68845">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇱
شهردار «رامات گان» در اسرائیل:
«ما تصمیم گرفته‌ایم تمام پناهگاه‌های شهر را باز کنیم. ارزیابی وضعیت نشان می‌دهد که خطر حملات موشکی از سوی ایران در تعطیلات آخر هفته افزایش یافته و دیگر ناچیز نیست؛
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68845" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68844">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=T8bsfA8iK4ERGHph8qxG7xlDK3cZihHWetgTnSrar1CinnHGfZ5rDP5Um8waiau1NqJuxC2UASQvJp_fLt-FJ_dlPm1_MqLc3ELmix_I_Uh8SU-sXzrmYOvl8KHae3KzAeE0IQR1JSvO1GUncr0MS2UAW5OhDlDXfhLCbc-T44in1D_VIZ3sO9ToGpYO6MZjB6F4bjwotVDqqAL4I51vkuKFWBPUgmF9eZ9Qq4WA5-mbSMNppLHHXmlbvfPb2QT96IkVy-3UZ8RAbXFBNn0L_E4fTuByAWz3HajqaSErHiqMgN_dq7RRQ7Ih9NhRSqwDSBWRT7GD0UGGRxYlYRxPZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=T8bsfA8iK4ERGHph8qxG7xlDK3cZihHWetgTnSrar1CinnHGfZ5rDP5Um8waiau1NqJuxC2UASQvJp_fLt-FJ_dlPm1_MqLc3ELmix_I_Uh8SU-sXzrmYOvl8KHae3KzAeE0IQR1JSvO1GUncr0MS2UAW5OhDlDXfhLCbc-T44in1D_VIZ3sO9ToGpYO6MZjB6F4bjwotVDqqAL4I51vkuKFWBPUgmF9eZ9Qq4WA5-mbSMNppLHHXmlbvfPb2QT96IkVy-3UZ8RAbXFBNn0L_E4fTuByAWz3HajqaSErHiqMgN_dq7RRQ7Ih9NhRSqwDSBWRT7GD0UGGRxYlYRxPZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
عراقچی می‌گوید سیاست آن‌ها "چشم در برابر چشم" است.
سیاست ترامپ "سر در برابر چشم" است.
آن‌ها بهای بسیار سنگینی خواهند پرداخت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68844" target="_blank">📅 12:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68843">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjVB2NaU3__pMmUlbcx2xJn--HkawX79fQ8FnOqMvOsBLQTXFqHoqOiqXzx6f4ojo3D3ZLPPw26G3hC3fhr_xL_hIdjOtNXXoa4qJcsRDWD4ZECohTTgXBI-WiYZ-HkB66UMYqf6_fB9YkMZA3rdLtIBSfZIuRBv6AgRbjoPOxlBW72dR6XwBFfoe0a4N3NRK0Bk3mE-cDfjMxCnCzuq1HaRGBLHoU2jqYOTJj5b3SxlxH81cVKZHpY92D3y2soPAo_48RigP9kjQWoZf5ayOBjiS-Hg_A0AQKD7cxn2ZUVXp7Ygsq8bzOSEpAjbVKRyOXb1fTE2XM_dGREe8fA--g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پایگاه دریایی ارتش جاسک که صبح امروز مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68843" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68842">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=hogqdfQxM_EEthGbHMaRCsGxN5K2NQVT5r058vwlCfCaDiiBsA7GayEwEeZfa1jehc9LYjxyNZ_0NrTIp-yJV-PCXcD2DWR-B7dqd_yNoRIQCGfkZfW0-hIjzsqbUKh2Q9pI31tA8qCjvLQL9pb9XzHNm2OO-D25pj1em1OJGUNwePwQlR-LO3rJK-rVO2H8w0zwSjC7Q1MncQYdi8Y__3Buep4dSqMEhifiVRlaTnXhZhPipv_DAAOuSPuFZX6q0rfYizVXTE8JNiUiZG47YsswtCscY65IjeJQ8XNImsHo1V6owjV5Z24aIaUIjMH3JIpXmddmLB2wFVLy6DCsYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=hogqdfQxM_EEthGbHMaRCsGxN5K2NQVT5r058vwlCfCaDiiBsA7GayEwEeZfa1jehc9LYjxyNZ_0NrTIp-yJV-PCXcD2DWR-B7dqd_yNoRIQCGfkZfW0-hIjzsqbUKh2Q9pI31tA8qCjvLQL9pb9XzHNm2OO-D25pj1em1OJGUNwePwQlR-LO3rJK-rVO2H8w0zwSjC7Q1MncQYdi8Y__3Buep4dSqMEhifiVRlaTnXhZhPipv_DAAOuSPuFZX6q0rfYizVXTE8JNiUiZG47YsswtCscY65IjeJQ8XNImsHo1V6owjV5Z24aIaUIjMH3JIpXmddmLB2wFVLy6DCsYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68842" target="_blank">📅 11:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68841">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=h2FOZ89ZouO2ctRcJp5sXrI7iIR1GS1vCpJr740qNzAuydN0a_QrzTzJDTAz_Tjh9jTpqCtIMBJlVqCaDodIQ7JFJu4MIVgDUibRJhPSstIzFpJUzwpiKz_w2eVovkNRd_Ek0DDl1ePi34S6XZhHO9Z_3kpFSNX66LcVvSOneLFfozrASdG3P2FQOGlTg15GtZ30fXe9t5wpP3oLhXwybvOY9ixUwSdTS_2qLzZ6ZR_wxYXMn44ssQkJr4kk5zAd5yDwiJo1_qv2wQlIolj8eU4zkDYYu8dVEh12c-xIW8gOqxDtAzavAX227UeftHUgCzzu-soQ_COpkeb0X2gpTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=h2FOZ89ZouO2ctRcJp5sXrI7iIR1GS1vCpJr740qNzAuydN0a_QrzTzJDTAz_Tjh9jTpqCtIMBJlVqCaDodIQ7JFJu4MIVgDUibRJhPSstIzFpJUzwpiKz_w2eVovkNRd_Ek0DDl1ePi34S6XZhHO9Z_3kpFSNX66LcVvSOneLFfozrASdG3P2FQOGlTg15GtZ30fXe9t5wpP3oLhXwybvOY9ixUwSdTS_2qLzZ6ZR_wxYXMn44ssQkJr4kk5zAd5yDwiJo1_qv2wQlIolj8eU4zkDYYu8dVEh12c-xIW8gOqxDtAzavAX227UeftHUgCzzu-soQ_COpkeb0X2gpTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=DSEp2cg6nafxyuKTS0DOZRuWkKl0b_O9ATVs6pqNkl5t1xot1Zbw9G_q_WS4LM0PVFTf8muymYfWO2rsewdsM3zvGd9cPCIuMFQXj3giezIha2ynUJFj38oXN_JePoyns0Cb6Ckxg1aOfvgUWOLMMnxSqHOhHyE66Vb1a6oiw8GfJq2INJVzMlQyKbpTBrBqOTtkVPIatzzrr4gMqWM0lPsROu4DFXrtLxDgueEFIDaMr6REfFfG8tjggb0XFDwPq-jJ6FErpd6DPq9j06YZYx1V-i0VBhSssqUNtg8da09m1PAtkP9vpNx01l8czSEolW5cFmiax6a62Ojm4myrgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=DSEp2cg6nafxyuKTS0DOZRuWkKl0b_O9ATVs6pqNkl5t1xot1Zbw9G_q_WS4LM0PVFTf8muymYfWO2rsewdsM3zvGd9cPCIuMFQXj3giezIha2ynUJFj38oXN_JePoyns0Cb6Ckxg1aOfvgUWOLMMnxSqHOhHyE66Vb1a6oiw8GfJq2INJVzMlQyKbpTBrBqOTtkVPIatzzrr4gMqWM0lPsROu4DFXrtLxDgueEFIDaMr6REfFfG8tjggb0XFDwPq-jJ6FErpd6DPq9j06YZYx1V-i0VBhSssqUNtg8da09m1PAtkP9vpNx01l8czSEolW5cFmiax6a62Ojm4myrgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حمله دیشب آمریکا به پاسگاه مرزی شلمچه
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68839" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68838">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gOFPfeutgHxYfgxiljdw56_a8HiOE6CYZWjs_owxW7T1Xns59iKPlNwbCiMB4BbhAYPxos83PMVFR6UuTZ703UR8aRrHLZoXxh_WIuHRM_NHq_YwffdBfRPHJvYgiDiUGSOIIzf9xDcc-VWZhQ4HrHgjTaTom-PPF8u8f5VjR4kG8f4WUzaC4fB4M934eqoTqnuI0g2wTll8Qk4xSyfflXcVMPhlsqX7hm8gHQn5NOcEYoatvt62VEyQopqM0Cj24RKjyXP0EJaF5JI853sZOrF-6_tIvD6t-LBsHF5LsxPsugFCDhyfDnlXz1c3pIEcXiNntmZDa9bAQLOa2UqQ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس برگه صحیح شده یکی از دانش آموزا که امتحان نهاییش رو 0.25 شده!
در جواب تمام سوالات نوشته:
با این مملکت درس خوندن جواب نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68838" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68837">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYvJ3Zn-7dYUzwnuZ390YESEHW8ZowdUq6mmmz9qWdHdBKbCFc_z5bTxGoSc0B1oiyi3hcOv8EGMgJZJ11eOziMbynCTn-hfyEJxt_5lYw8bfoNISwv8Z8AyIpfSUGFr5APm2s38gnK0aGsPEDR_GAEHThlqzZu84GloNbkfB7tfeZX0o2j8gMR2avJGqWIXA65w5OA4dwax8RqWuaIN3uMFfGpWDk_6fGJuvS02Z8L_5_lLEwjFP1Uu63sgCxXC_7i6zRvvgF7K24RCAJesQZPZt9DsZ4A0fFHI0d1PB3avhOA0NY2Rd746P-03nlJ7nAkyCcrdyCWNQMAjCfWdpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👌
وال‌استریت ژورنال: ایالات متحده در حال اعزام گسترده نیروها، کادر درمانی و تسلیحات به خاورمیانه است تا در شرایطی که رئیس‌جمهور ترامپ احتمال گسترش درگیری با ایران را بررسی می‌کند، گزینه‌های نظامی قدرتمندتری در اختیار داشته باشد.
به گفته مقامات، ایالات متحده طی روزهای اخیر پروازهای باری را از پایگاه‌های محل استقرار نیروهای عملیات ویژه به مقصد خاورمیانه انجام داده است. نیروهای عملیات ویژه در مرحله نخست جنگ موسوم به «خشم حماسی» (Epic Fury) در عملیات‌های رزمی جست‌وجو و نجات به کار گرفته شدند، هرچند توانایی اجرای طیف وسیعی از مأموریت‌های دیگر را نیز دارند.
به گفته برخی از این مقامات، بمب‌افکن‌های دوربرد نیز در حال آماده‌سازی برای انجام عملیات‌های رزمی بزرگ هستند؛ از جمله بمب‌افکن‌های «بی-۱» (B-1) که هم‌اکنون در بریتانیا مستقرند.
وال‌استریت ژورنال پیش‌تر گزارش داده بود که ارتش همچنین هواپیماهای سوخت‌رسان، جنگنده‌های «اف-۱۶» (F-16) از پایگاه هوایی «اسپانگ‌دالِم» در آلمان و جنگنده‌های رادارگریز «اف-۳۵» (F-35) از پایگاه هوایی «لیکنهیث» در انگلستان را به منطقه اعزام کرده است. اردن و اسرائیل به عنوان میزبانان احتمالی این هواپیماها در نظر گرفته می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68837" target="_blank">📅 09:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68836">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⏺
فرماندار بوشهر:
روز چهارشنبه، یک نیروگاه در مجاورت نیروگاه هسته‌ای بوشهر در جنوب ایران هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68836" target="_blank">📅 02:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68835">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=P5Fg_psPAlq5e3e7E1iRf1sti5MLJM15uNGmfxrI9D43z1mslHzEMBYCJQMq4h27pLUf6x2fWUbeTJTOPgBIUgKFpDUddhypfeR-3N-4Quje9X-tEhympLiudc4kndTygt_IhzIFno9s99-FfYjQKzg29eCSH0NZmNSlFd-fYc5ty_zSaBAHJPCCcvaPIoWXx0JepI9HNqxLK9a7kok9TK9vd_bMAaSF35Rr5L8F98tBinXHOAISgX5QMG6saNIulG4kzo10I2cSeB9nRCu5FxwtCRSyjP9CYZEhoqbO3OrZlSzxw6khoZsFad2iGPzibRHGs3nI5C1bGkMqbdiXmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=P5Fg_psPAlq5e3e7E1iRf1sti5MLJM15uNGmfxrI9D43z1mslHzEMBYCJQMq4h27pLUf6x2fWUbeTJTOPgBIUgKFpDUddhypfeR-3N-4Quje9X-tEhympLiudc4kndTygt_IhzIFno9s99-FfYjQKzg29eCSH0NZmNSlFd-fYc5ty_zSaBAHJPCCcvaPIoWXx0JepI9HNqxLK9a7kok9TK9vd_bMAaSF35Rr5L8F98tBinXHOAISgX5QMG6saNIulG4kzo10I2cSeB9nRCu5FxwtCRSyjP9CYZEhoqbO3OrZlSzxw6khoZsFad2iGPzibRHGs3nI5C1bGkMqbdiXmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛مجلس نمایندگان آمریکا لایحه سیاست دفاعی ۱.۱۵ تریلیون دلاری را با اختلاف آرای اندک (۲۱۶ رأی موافق در برابر ۲۱۲ رأی مخالف) تصویب کرد.
این طرح شامل 95 میلیارد دلار بودجه نظامی اضافی است که عمدتاً برای تأمین هزینه‌های مرتبط با جنگ علیه ایران در نظر گرفته شده است.
این لایحه اکنون برای بررسی به مجلس سنا ارجاع خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/68835" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68834">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMyZ5kMFfGyONZUxMdF43-8RYMgJQXdLE8LWIPrrrrpQZ99jgMY3wsjBAJm77ksDLAb9hYgMHHwx-eWwYZdrPpoY2OnRaFFfP9AeAyZArwaCELObWLAdW2iNW2wGxvNX9-Xg8COBP192ebzkx84Zr_cKDr4riDxiTIFwaoi80DYSNqsG750fyITGy6TB6ggxQzMJrDZT6KRzWGnPV9KcQ9QRCq9DRqh4KX2F7PJN1y3K59TaOcfRR3Q9tkSIrUxCPo4IzhdnYeF3Lh31bRt2tRUxZgtI1nyqunQ7UJZAhnO2m8m48hqShTrsb6ffa5FUf26r927WNw5lgwE18PmfOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ستاد فرماندهی مرکزی ایالات متحده (سنتکام): امروز ساعت ۵:۳۰ بعدازظهر به وقت شرقی، نیروهای آمریکایی به دستور فرمانده کل، حملات بیشتری را علیه اهداف نظامی ایران آغاز کردند.
این مأموریت با هدف تضعیف هرچه بیشتر توانایی ایران در تهدید دریانوردان غیرنظامی و کشتی‌های تجاریِ در حال تردد در آب‌های منطقه، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68834" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68833">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدید حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68833" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68832">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇮🇷
هم‌اکنون حملات سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68832" target="_blank">📅 01:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68831">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMv7h1sbmu8BxzW4IVO-PhqyoCz3_EtkD0EJ2-ukjzGe0kGOH5Y-c03BkrElm-7l4sJEoWnpdqWGypxiqNrP0r8eWG6l69axI13yEACY0-ydyl1ku6m6k40SqeA4gK95jxNShIpB_EM8Y5Gg9-f6MVi12ySReOoxPENi_KY-dtcUolEhRoJQQmHqThT5-6fAGMkgzpvxnOokST2buatsdd2OVS9S7h5aU99TZBqYceQP3hUUirf0rKLNvC827qkEoyrqWKrL9QEp4ZjeOiPLHNFTEK6_GGr5bKhOvwyNpdOtgZL-pgyhzg_C_AagIi1op412YafXUMmW5upfCOTGMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نقاطی که امشب تا این لحظه هدف حمله قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68831" target="_blank">📅 01:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68830">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg2E9Z0kbtjOM8H204qQNF2pcG6CvvhL6GauT0NndOqlmOF45_TjNRqQ6z1oRoG_lPIPZtNstRdq5_-MO61Vo1vlg1Ew363jlLNcegrgEaUCiFxfYCvkOPSdalo1iC90YPXvGVoNHfvuqyWecVU8v7sIso_BI7nvDV8FWo4BIw1znwAvrnZJpcg-6Q70NMUUYsMZbeWD6z5WFTpQNuFJkNFKFetbBLUBnubGEAT-_qelqgD9UaaFGr-kWN9_iiwrW_IbyM_KebZCkMcTHVWtB7psaE5_Afs4PshsE_mT6idNbvoOfLNnyPhUlaywb2gi1mfXlObhdm27iXX7-ziKtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.  @News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68830" target="_blank">📅 01:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68829">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30afc95033.mp4?token=ec_j0vTNkjGSo-0Gbqvrk5YkWlD94Gf0tpSn4DXiZsxhi-sq1i6xzGhVV1Xw3g7hevuTy71v3kWRwUsfW7MiA4NSkCR9hW1FXKnduZ0BgjUhsByHjaRbvUgIl728Hm2BNWOkq5haBnFBYMDmPOKKlw5HDfbu8DhJ_sP8nfnVsLyITgtWsZ9DpcSDYY29Tm4R2S3wsckSz2N6rAm-NExQ4lRVRv6LxP8_njpZBsl8SlP5hvxq5lWSl8FkfBCAjZM_2hdvdOFHYKNzk7vpR4tYWcTXdGC-lnG70IugsRoZViL5qzbMida7HjDsCaOjC0c0jkwEhavO4Gb_r6dFg0X5CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30afc95033.mp4?token=ec_j0vTNkjGSo-0Gbqvrk5YkWlD94Gf0tpSn4DXiZsxhi-sq1i6xzGhVV1Xw3g7hevuTy71v3kWRwUsfW7MiA4NSkCR9hW1FXKnduZ0BgjUhsByHjaRbvUgIl728Hm2BNWOkq5haBnFBYMDmPOKKlw5HDfbu8DhJ_sP8nfnVsLyITgtWsZ9DpcSDYY29Tm4R2S3wsckSz2N6rAm-NExQ4lRVRv6LxP8_njpZBsl8SlP5hvxq5lWSl8FkfBCAjZM_2hdvdOFHYKNzk7vpR4tYWcTXdGC-lnG70IugsRoZViL5qzbMida7HjDsCaOjC0c0jkwEhavO4Gb_r6dFg0X5CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68829" target="_blank">📅 00:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68828">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
صدای دو انفجار در بوشهر شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68828" target="_blank">📅 00:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68827">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
فارس:
حملۀ موشکی دشمن آمریکایی به یک سولۀ انبار آسفالت در اطراف رامشیر استان خوزستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68827" target="_blank">📅 00:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68826">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmEo3I39Lz5-pbVIKfvBs6aAuHMUrjZ-vBRSJP50EVE5_DkL0LpWYL42LXTyNtXIgZy52vadEtc1aIF_2SvG51VGu0bfznnCGU4zPRDmiIWi3Ufk_6QMBYxOT99Ks-BQr54i-MVcZK8p-Mm875_VwJdlsb89TG_Jz8Ks2AMVPcTnXgPhB75we4uvxqCpVm-R-zBXg0KypfH0qcCeS0Av-opgfJ7VHuNth5ljFyw9FB5wxXobztaysekTq3-YzP8e37wSHcSglzDgECPBtQ5OpQoIQCzVjnzzxJa8HdrphsbkiMMEjZf7xBmW0hNWfxf-RUewcI7EOVuFZkByre-fhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
یک جریان مداوم از تجهیزات هوایی آمریکایی به سمت خاورمیانه در حال انجام است، که احتمالاً شامل هواپیماهای تانکر سوخت‌رسان نیز می‌شود، در چارچوب آمادگی‌ها برای تشدید عملیات نظامی علیه ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68826" target="_blank">📅 00:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68825">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
پاسگاه دریایی زیارت در سیریک هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68825" target="_blank">📅 00:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68824">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
دقایقی قبل صدای چندین انفجار در اهواز و ماهشهر نیز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68824" target="_blank">📅 00:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68823">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
صداوسیما:
چند دقیقه پیش، صدای انفجاری در منطقه بمانی، واقع در شهرستان سیریک، شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68823" target="_blank">📅 00:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68822">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/030860acf9.mp4?token=TXD4Er2WWt7kItFUdT3ombRBhTpjn3ItvKdlRvYI6TZCCXTWaZ3kg_Q4tDHUbLkD768H7wALLgLr8u-Z8W0slw_8Jd2azD4WrEXEUSV7v_rKo7pmkljdYvka8I74vWiIUsbK8RZ06fhbZZyAA_2-cqkNSiHbD6PomITwkgM__fH40Krx9Fwt-skalYrwaU9HOvBttG0UjFCs_pSfmEITUyYvNP9bGBjuWIfANwuEb37FQkaSsVbdxjT_RvwZyLqJE6RxqEqu2Q7rolqNVizFoSg7ON_58RDECRaIH25PxKgGoaIOk19knGUJ_JZ-raqWQlbJmcIVSQjuXYurR9SfJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/030860acf9.mp4?token=TXD4Er2WWt7kItFUdT3ombRBhTpjn3ItvKdlRvYI6TZCCXTWaZ3kg_Q4tDHUbLkD768H7wALLgLr8u-Z8W0slw_8Jd2azD4WrEXEUSV7v_rKo7pmkljdYvka8I74vWiIUsbK8RZ06fhbZZyAA_2-cqkNSiHbD6PomITwkgM__fH40Krx9Fwt-skalYrwaU9HOvBttG0UjFCs_pSfmEITUyYvNP9bGBjuWIfANwuEb37FQkaSsVbdxjT_RvwZyLqJE6RxqEqu2Q7rolqNVizFoSg7ON_58RDECRaIH25PxKgGoaIOk19knGUJ_JZ-raqWQlbJmcIVSQjuXYurR9SfJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه روز پیش که پل کهورستان رو زدن ، سریع اومدن یه جاده آسفالت از رودخونه خشک شده اونجا کشیدن که رفت‌وآمد متوقف نشه.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68822" target="_blank">📅 23:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68821">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b162fcc101.mp4?token=DNE_Z-HxzLX46-qBaifHRoBr3wK4IU6g6yjCkanqUuS6wWbH4CC3THwZPRccCf6HcC3WC5xQQwZ3g_03i0plhnaj6ATk4k8StVudVtx6zIwfrvs_AF7JbwCLPmXM-Bw3Iivu0FsTcHP5bK0V4ZZEWXqpH-Wg72HaDle_NvsIynFRXzn0WtO2NmrBqQcesS8AXS90eD-7-pFh58wSnck0QCbSTnos-aCA9C6iVzkJLjW960Y0B_qbVuXKnN2XGehwgiyy8Ca5kTYQ6YY1F5c5wYsT27_z5_s0N2JXPt25Ui0o4XaXLkv24ZEh9x3GKdMvRs4_VL7v6wD7fsmYNbPrloi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b162fcc101.mp4?token=DNE_Z-HxzLX46-qBaifHRoBr3wK4IU6g6yjCkanqUuS6wWbH4CC3THwZPRccCf6HcC3WC5xQQwZ3g_03i0plhnaj6ATk4k8StVudVtx6zIwfrvs_AF7JbwCLPmXM-Bw3Iivu0FsTcHP5bK0V4ZZEWXqpH-Wg72HaDle_NvsIynFRXzn0WtO2NmrBqQcesS8AXS90eD-7-pFh58wSnck0QCbSTnos-aCA9C6iVzkJLjW960Y0B_qbVuXKnN2XGehwgiyy8Ca5kTYQ6YY1F5c5wYsT27_z5_s0N2JXPt25Ui0o4XaXLkv24ZEh9x3GKdMvRs4_VL7v6wD7fsmYNbPrloi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ما به تنگه‌ها احتیاجی نداریم؛ اصلاً به هیچ‌کدومشون نیاز نداریم.
ما نیازی به تنگه هرمز نداریم، اما مجبوریم این کار رو انجام بدیم، چون نمی‌تونیم اجازه بدیم ایران به سلاح هسته‌ای دست پیدا کنه.
من اسمش رو جنگ نمی‌ذارم؛ یه درگیری محدود بین ما و جمهوری اسلامی ایران.
اون‌ها اون‌قدر تحت فشار و ضربه هستن که می‌خوان توافق کنن، ولی به نظر من هنوز آماده توافق نیستن.
الان هنوز آماده توافق نیستن.
ولی خیلی زود آماده می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68821" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
