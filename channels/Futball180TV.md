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
<img src="https://cdn5.telesco.pe/file/XlSyKenPPXmNxR2dMCPJzt-Efpbs88W-pHjrRzoHx7BHOklkPwBAwUzYcfW5OiUHuOa_ELyxHzadS94V3TbB9VQZV761JlUaXZqUSWXqtAR72rCIpBkfLQoFVTr_a_uB3d9wrZYz-VpT2OMrtsvLYnTphAAj0-fPHKJ_QOublKqsL3vvhjKnTp9K08u0ACbPhXVS5CLNkxlh8FT2wenB1JV3cr2K3uV0uqv5SFsaCEchBVMnV2HoB5MDFTOu1B7_XeXWlFAUCFinVwQrSVgM6UJpbq9dslaZPaDCrajWIzNyUejQmg_gyeI9yKroKSEp9lA4CdewoP7iYo0GPCXKXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 670K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 21:11:13</div>
<hr>

<div class="tg-post" id="msg-94246">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kazfHTtuQnMrGtO729QglGAk-bLbVMWjIn6Xzt8OKPFnWsOLSmW9Z1kTU5WhIBkzbL-RgZ1y15eG_bmCPloAlujZp3hcXK0nAh77Kk9OvyXdvVzPAz_htMgXSvD9GU7nddBS-RVCROR__0oGHCzSSnZgDeC2NSoV3XIPdDeLMAFm88s6Ia5YNkXOpr1hnUmBb-pDnXTSqexDdhlER4W9rHZkguRaBZPHkSFoxPy-vQnh6AwB-35hAq_hMFmTVL03uR3nrhtdZJQMQZC663fsD3wXT_k-GJgx0pqY3SBR95PVfRU14egucdhmPciIRJEMzpOzKdZTATo4d8BocSKOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇦
🇨🇭
ترکیب رسمی بوسنی و سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 631 · <a href="https://t.me/Futball180TV/94246" target="_blank">📅 21:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94245">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZl4pZF_grmQ6_08AZ4n_WRsc53hJ5bsg3dkv620rnNr7mntSNE2Fho5aG3Abr12iT0LW4I2g76GDVqMxzuG6zrIhe5I2Pv0Od6E53HDcOcEqNOz77_1MUENSh3sLKfDO591aog0vfGtttzAemNCwqSWqHMgBGW3AWvlMbiWERM4oYPGYIOmTxS0gUJJhWSjBlZ5fha3qJ8QDl1LFFzXGmj1CDx-BzpdZDBNQSMdtxARvI8DbzAmhAYdTyvymNKVUmQ6ZeIhtWIOylUMKzzAu17VAH38CdGV0Qz0RHhLBtJkRIGl6kYlyOz65l2XsD3mAqpLZ59SMQcZ7a2oY9Oi-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مارک کوکوریا درباره انتقال به رئال‌مادرید:
فکر می‌کنم هم من و هم اطرافیانم، خانواده‌ام، واضح بود که این فرصتی است که نمی‌توانستیم رد کنیم و من از تصمیمی که گرفتیم خیلی خوشحالم.من مجبور شدم تصمیم مهمی بگیرم و هیچ شکی ندارم؛ فکر می‌کنم این یک قدم بزرگ برای من است. وقتی بچه بودی، رویای بازی برای تیم‌های بزرگ را داشتی و فکر می‌کنم رئال مادرید یکی از آن‌هاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/Futball180TV/94245" target="_blank">📅 21:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94244">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0717ffb37.mp4?token=dWjOXzdecUPiF75d8y40TdeFWlbsu8EC3MPP4JL5B-cFeQ4blRGIns28I4EDB8RMKNd7-q3in4ajABWDs5oD5THP-udHfk5gVoqCE5WfvYomBaGBvquqbkvp_XYiHZmtGR4CkmTLekZrBtL9-notDU16aL33j8Sg_9i7VX0OmbEYA6UQUrOTu2QAi6b_2pojoYJLc3b07HZTi4Drnf1rme_PBxoQfGVzdKBF_QzCJd-Hp-ZOAsHZ8XvUs2Pp9z6QpW8ziUKiVHSqZak9UYJnI5B8MfRGKikOM2FaZ-mL1473QZq37d1fnEjIXxKnDOEnhWeD3zqhdigKHaKFTZeFlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0717ffb37.mp4?token=dWjOXzdecUPiF75d8y40TdeFWlbsu8EC3MPP4JL5B-cFeQ4blRGIns28I4EDB8RMKNd7-q3in4ajABWDs5oD5THP-udHfk5gVoqCE5WfvYomBaGBvquqbkvp_XYiHZmtGR4CkmTLekZrBtL9-notDU16aL33j8Sg_9i7VX0OmbEYA6UQUrOTu2QAi6b_2pojoYJLc3b07HZTi4Drnf1rme_PBxoQfGVzdKBF_QzCJd-Hp-ZOAsHZ8XvUs2Pp9z6QpW8ziUKiVHSqZak9UYJnI5B8MfRGKikOM2FaZ-mL1473QZq37d1fnEjIXxKnDOEnhWeD3zqhdigKHaKFTZeFlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رونالدو نازاریو: به نظرم اگه یه نفر باشه که لیاقت اینو داشته باشه که جلو بزنه و عنوان بهترین گلزن تاریخ جام جهانی رو مال خود کنه، اون آدم کسی نیست جز مسی؛ مسی بهترین گزینه برای داشتن این جایگاهه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/94244" target="_blank">📅 20:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94243">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeuYPrgNbTTld4qmiXTn5TKaHrANGHVBwIDV5uIxdmQqzdIuZ7kRBuExeJdYlOHBraDA-qmQW284oFRqSOcj05IE_GhXK_oXzxNCbILplUWIcfHBfqnD4_09x0M1PdkGsxngT_RIRDYnAMoVGBgFl3QFHO2Qgops3aEA5ojwMcGfrffcvL58Uo-KRBE6Dv9CVMxxZsRsV2EofhyF8G6nWHGfxhLUXF1xVkG18ffleFVsY-vOcCrJUCOiEOflLacFpUo7trOVPI9hfX5CCjldjM6VQVeFMkoU-f7NG_2IGeqLMWNulBuV8aXqUevInUGHW_LfUEAAIXUp63D1OkD4mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
بلینگهام : مودریچ بی نظیره، اون بهترینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/Futball180TV/94243" target="_blank">📅 20:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94242">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPUqdMn2xY5p3KivYf6kKQ-jfN4stZ4MWYFw33c9ehAdEN8j47l8poz4AvI1a8O8f_xDaZotKtA5A38DhPQC_6CX5GTYX89gGr_8ztVzeOM1Tb-FunqeXeO6uD1FrnRBTUyxz4PnPidN7kJ439yRAyG59qNmUWNCY_mqeHqL3zfA4q8HHRRwTLpyzk41ge1GwO50jj4VGgr27zkGe1bYSxQMBC17Q3s25F_ZemjebVz9gzLWcOIc-OzrGjnfDe9SFQNJjF5_vnZrPTlZusml9JVk7wM9cSZN5Dlhe_BwKZ41GxxdyME3LbA-HDZ1H7xyLNpwQwgFYG3dY1MbPlbvKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇰🇷
بازیکنان کره جنوبی امروز دو پهباد رو تو تمرین سرنگون کردن، فدراسیون فوتبال کره جنوبی رسماً فیفا را از این حادثه مطلع کرد و خواستار تحقیقات فوری و اقدامات امنیتی سختگیرانه‌تر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/Futball180TV/94242" target="_blank">📅 20:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94241">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/Futball180TV/94241" target="_blank">📅 20:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94240">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bbFniDHZHGSvG0htsn1VdOGtZyffcUH3Zg3SP85wH_w0CQf0bwoqmZB2PdwehlZc4yPzYFoIQYJs34my_r9OzNFMXSYxDtxUDSFvoe6ssVg82HNbK-mMXRQsJ4Fgf81UfW56Fxqgv1hMLNr9C5CuPwEkTcHLRABMs8friSw6buE_7UJlgILnHCIO5C8IuxkFkNCjwvjQbHojoG466Hzd-MsSpdqAxJvM_28QXtczslbQpjuEOs3c6jbicETRwTxzRbdlGVDz-NltSS2vDUvWsjw4NVv0AF9AzVGHRwWWiaLjPd-izs9ejOew0jYHHyR51LwzDiPC0JygTJVwlWmsFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/Futball180TV/94240" target="_blank">📅 20:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94239">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پایان نیمه اول
😀
جمهوری چک 1 -
🇿🇦
آفریقای جنوبی 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/Futball180TV/94239" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94233">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZywLXbY1fQ_Zjf2wfXCPqWGYnl_sv74U1Zn5aEdIz5sqJ0k0TYelRPx59z7z_3_thf-NfwsYTcwOFW8BLmSWM4LrM-_-qQyTrE2eoQlb-dRvK47J-kQIZ6gcArhc10ro3NeZgE_VQ3W5VkzXxOu00bFEX5jazXVlEKtJXJk3hUsIx0PEofYlY5TIHpGY8TU6uTpNPyuEiEOaBtRP-90vFbdVChL9wn0beYg_9Yjpm-3F2l_hrXeGrSLvTe9LJNR4pNRVQEKbv8QNa52dw7GuIjAP1gBEzflqPba3zzCtB0pNeTq8yNdfhMbXaiQssbi6KIltJNIjM7MqT_b8cobiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVK7SXyY8a5YvRd3iTtEB7sO-nJCRRedDYb-YPYGf1RVfC4bEJfJ9RhMlTYz1F0I-P4VXI1U6FNhDww8GDywVUleSMBhujtSA0Wo37GrEZ5KJVkKSJAqX4rhqmmhPYL2ClaxEalBb7JK-9KCE4nVuAuhF5V1M6jYFPZke9AYZs-fLHKpeG8krf4bK8VFetu6R5nBbaPgyfHcHqD7NkZINgHbtb6NmLaRcR_g_r23Ey9rQ1xCySihsWGVz1W8HKzy3k0bxj3Avs9FBP1hMUUJwV9-Ph4rXY1dMr6W_CeWhQb6dOemCcwrKeNFzdRA_qBP9jn1BIO_Za-VcRFmoiv8rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNM6GN57c1KGMAMsoW1pihCbxqla_Ys-AGTkqVmr5eBz3xWRGLEeO0DCxdpmNVpvy6LKPFjKhFoHbwOA76_CJnmWrvbzjLT1rPhHn3ibDLxa67434zFPSWzcCOKQvIG9KU4_kggIkx0MSmk_XIDsOjGcUYxONOXF9pZUptxX8fnSTDzFLTjaahol5tOVtqOzUV_tNfCYDwdWnska7lSWaYgJWJAs7YsERYkPGRnexHixmewHhJGX3OX_BTYnWJzpWV7s2OF_F2kgRhNb_lQcZQmP-j07C6DG-RcYrdTLBZwp33DJ5GiDGil-hIxUr0zXtGF3-9zS2MfikQRav1bBxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uijAKwamhwVPFmajJlDHLvJPYgACKAFQabvuoHVQM7E4RzQACsOYMBboC3ymI3ERD7ktAyeO9X8fA4YE8Dyx1X49ah6j0VH2r3zFyG2sGCIYSUuP4IkepGPwhxdqSzcDjBXdo-kdvglzGWfBvTQx2f2CqHCCaT9oEgLQ-Mn-8H475ho0m-JOt8EDvXl6RVgfWgSmvdlooCzx76OU37TFoJs8gVhlvJ062ZtdbJ7cA0us3XGHphMX-duK67rLtr9qgA-V9UFPqhSLtSp4ALtBqa-DubV3to4cVHP7-oAXv_12Ww9kKxeRCe33kvdFtHqTuVwQeT4E91_82vBymp6Cdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iqZLbaXTKH9SU7DmbgRadJQ0qeTiQ6Ncnf94O2LNad5AcQIYa3XKwidKuHrGcYcbuicpO1xXM8CvvBKc809Q0tZyq3YTOhKQTc2gPCgAe2dJYpFpV3EY06dlMR47Wd06rGT1ha3Ow5JLPilIbQeQXD5_Igs5zSE1vLbygC937HoYqlpt6ICk-IGzpIFF8_orlbnzOOTjPLPoyGAcqT2hrpZLNrtGUdfqdDGHN4mmRnqBtM_VVopbnkwujB1c_r_kqBkxMdWUbbz_CD4f6xLtQIRpznq6To93jbOg642h5iv_KDKj2POJeqadlVwZ2n2v4NkQpnm-9FSFIqYhmXMS4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i91slw946d26Ji0vNF-6mJOlMxXq79Ts9i9UV5Pho0Qq9AlbZRi68sc-TrH5KnscB3WYquHR88sXxsBUPR8Y9pTSTNt1egDPWN6xVXhiTzWIsp9oeo5yiW3PKL7FjrgaTWJAk4_sPP-TeK9qnBlVL7DHwD0_o6amVt7TQ_EGwvloTT_SMy9j7wJsxHyuEB3oReGI-opXikTc0VfVwO1k1pMA-tCOiAaikUt1xptcONVJMVm0kqY3ulSZ0HFpknGeOXhWuBbpe_7Z1ZzyeEWKDcSMLwqhE15mMJOufz3Xo1yWNrBXVengqyRghHUk8PjUJwwrO5VLnfbpAg3jrND9aQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای اسپانیا و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/Futball180TV/94233" target="_blank">📅 20:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94232">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiWw9IAzbclTc4MOyCMcRorN4n2W9KLAdiTBp1p3o94CEKdAU_WvBBmY2TF_AZXB0IESqDPOO5pGb0kYPhfZAsWTAK4SqhxDrZaCA7UD8d6vmGJkHY16WBl8cdYlX5F4cPIJvORIruR0WGW07SiX4DvIxF0XNFgcjVciT-zaWWmOdNQPlBCpfBbqVrH10hCoVu-Fxk9_kmjLbUhwfxUNARqy0JxZps_8RmR3KEegQRbhgBs0a7q-t9VL6nhqYS19L9rtnuwHR5KBVKPigN47DUgkXUHdNHnYAmN99B3Hd5952BQjBqIKFcPPKbCEmy8BEpOhmbgRxlxndG9gImJg7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
3 گل در جام جهانی 2026 پس از پرتاب اوت به ثمر رسید که چک 2 گل آن را به ثمر رساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/94232" target="_blank">📅 19:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94231">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/562bcb149d.mp4?token=qZ7CkEHCza7hCUvPPPwIH4X00bmdcZjfIWFwAi-ZjTPqGvo0UknMlzekJD0uMItp6W1aFPqHuJ9gUExQQVu1y5v2K-zcflRe94aKmLnjt95Zv53Mcta0U9EjHxnUcenM9Tj_vpujyARwKTJaJYro2FfTWA2lLQgAudepk9N2FeRcaOtZrKbEyj6I4QcTSq2wbFEpOKtsqQX8hHsODNlsfNe9oMtUwyVkQJqtaHbh7o-f_d--mAGfV9nK05yqd7rjIPIaUm6bl2SdK0vZe09si5pQQEMLBDcfiomx7s_p36owXorUfXv9pM8YXo5aFkj9QGfMj0mpfq9gnHA6LYfZkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/562bcb149d.mp4?token=qZ7CkEHCza7hCUvPPPwIH4X00bmdcZjfIWFwAi-ZjTPqGvo0UknMlzekJD0uMItp6W1aFPqHuJ9gUExQQVu1y5v2K-zcflRe94aKmLnjt95Zv53Mcta0U9EjHxnUcenM9Tj_vpujyARwKTJaJYro2FfTWA2lLQgAudepk9N2FeRcaOtZrKbEyj6I4QcTSq2wbFEpOKtsqQX8hHsODNlsfNe9oMtUwyVkQJqtaHbh7o-f_d--mAGfV9nK05yqd7rjIPIaUm6bl2SdK0vZe09si5pQQEMLBDcfiomx7s_p36owXorUfXv9pM8YXo5aFkj9QGfMj0mpfq9gnHA6LYfZkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رفیقم: داداش قمارباز اگه برد و باخت به تخمشم نباشه قمارباز میشه.
همچنین رفیقم بعد شروع بازی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/94231" target="_blank">📅 19:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94230">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
❌
🤩
#فوری
#اختصاصی_فوتبال‌180
🔻
اگر اتفاق خاصی رخ‌ندهد، اوسمار ویرا سرمربی پرسپولیس طی یک‌هفته تا ده روز آینده از هدایت سرخپوشان جدا خواهد شد. اوسمار بدلیل مشکلات خانوادگی و البته درخواست حقوق بیشتر نسبت به فصل‌قبل، موانع مهمی در مسیر تمدید قراردادش گذاشته که بانک‌شهر مخالفت جدی خود را با افزایش رقم دستمزدش اعلام کرده
🔻
دراگان اسکوچیچ درحال حاضر جدی ترین گزینه هدایت پرسپولیس شده که البته فعلا بابت مسائل کشور دچار تردید شده. از مهدی مهدوی‌کیا و علی‌دایی نیز گزینه‌های بعدی سرخپوشان هستند که بعید است این دو در شرایط فعلی قصد حضور در ایران و فعالیت را داشته باشند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/94230" target="_blank">📅 19:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94229">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9605daa245.mp4?token=q60429f_1q_uhvRhSzkFkMyP-3tFrF8UcLoW_om2BmCOJNKcypB6mUANQyzpwJ7C-pE-17IChoPZ83snFaaslpL1gUKlTvhxLpjAHURLWosABBUXw572mzIfhEic7tR_-55jmd0xengOYWCGImM7Bav6c8PiEepVzAEH3figC7Y03AMfrY3lXia7dQseZE6ONpCGuNuqrkQq14vEGTEMDmpUK9Hh-ToR5voho53O7YjXHovQancwHkr-yKQrDY3fZsGL7r7emhGHE7IjeD4VwOScwDCpAforjrI1BkYU5g9NyM8-GSJW2UU4n4SpfoDyytnlcwNriC9bYXrM2Wf18Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9605daa245.mp4?token=q60429f_1q_uhvRhSzkFkMyP-3tFrF8UcLoW_om2BmCOJNKcypB6mUANQyzpwJ7C-pE-17IChoPZ83snFaaslpL1gUKlTvhxLpjAHURLWosABBUXw572mzIfhEic7tR_-55jmd0xengOYWCGImM7Bav6c8PiEepVzAEH3figC7Y03AMfrY3lXia7dQseZE6ONpCGuNuqrkQq14vEGTEMDmpUK9Hh-ToR5voho53O7YjXHovQancwHkr-yKQrDY3fZsGL7r7emhGHE7IjeD4VwOScwDCpAforjrI1BkYU5g9NyM8-GSJW2UU4n4SpfoDyytnlcwNriC9bYXrM2Wf18Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش های مربی ژاپن تو بازی با هلند که به شدت وایرال شده و به انیمه ها تشبیه شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/94229" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94228">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0LKlcZyJs9fzzjRQ11irbEXfywasHeFy0q-Fjxq4R6hV-0gyhi9bXGx2R0qFd3Y9vBTEFq0NvDJuFe4Y_7Qm5bbn9GFFRrigZbt3TWvr3sqwYup4rQOfeDvU2j9Mzxc0g6V-GdeY7MTuL8xI5cJEgvJQ-72F2LEGMvvOjD27XNs7jBGt9mCJZ1acv4WYt4l_4Ob8gQFPT1KFuqvmX0H0PuQkjWUAN8RDi2E9DvRcnneNlxfPJ6oVjZtqpn8zAL9IJa52MQlkgtUt7SSo78UCH0lkhqZsJYau5C5MkHrj4KvdbRjXKnOyKT8ik3mNCap2lTUvrQejX_OIWrdDNnOiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پیش فروش GTA VI از هفته بعد شروع میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/94228" target="_blank">📅 19:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94227">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLai6v-1SHgITncts2CjdLs08Mx5ZmIn9NHRt8-vmf_QmM2LqCI23aG2Qc0SCGryRBIZU0OghrOUjvYDgOG4lJuzAPVJANCeKiwJFhOCuqHJ8aVLGGXrxvuCES7UOFP9AAiBbJdIWRvI8GSHIDWRUrXKCcD9roKwaWSDQWuwE8eXBpu0Wqduf8n8w9NqeJ0cgChX-SPPD2CmdVPuc0pOn8m5ksSf-4J0qE8v0rs7MGN9qHuKWIcENjB-7WVEOeUCAl8AqgtFFGxUq3QhDoKtA8h7mN5sOb7OCPoimblZiqbsGEDpW5B2P9KNFcXfLshgCnb-TWlPQXwXuvNYxThVdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آماد دیالو بیش از هر بازیکن دیگری در هفته اول دریبل های موفق ثبت کرد
🔹
او فقط 34 دقیقه بازی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/94227" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94226">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2opAb0x44Xf1FyCWdrkfyNApL92GjkDoyTdGiLVJ4nU4MHBqKLqctKV4G8v4faOxULL05QhhCplV_fCmvLoDDCaOz_bzV2aJ2hOHoP9GoTXTvIm3j-qt4LBgpjy5vTsuPSdrBHVPUYJLfdbBwMMuqeC8xMsXQdg95kIgpgQLLXME1okfu2mWNW6BbGk5t-loagu7HwE8Vod0RDIikCOrbFpwXL7_Am9auX_VN8r1kj2_RuSE5RRQuxhDlG8AaalYIm4UJOrtqjGFjD7ADYaJW8lD4VRtmDvxzj7UJbXsMz-K5F-7G0DNlG-GoK_U0bhzxP4deeFajG1QB2x5C_j4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇿🇦
🆚
🇨🇿
۲۸ خرداد
🗓️
۱۹:۳۰
⏰
چک
🆚
آفریقای جنوبی
📌
📌
تقابل یکی از نمایندگان فوتبال آفریقا با تیمی منسجم و ساختارمند از اروپا
؛
جایی که قدرت فیزیکی و انگیزه در برابر نظم تاکتیکی و فوتبال تیمی قرار می‌گیرد.
⚽
🔥
جمهوری چک، تیمی منسجم و یکدست از قاره اروپا با ساختار دفاعی منظم و بازی گروهی حساب‌شده که همیشه حریفی سخت برای رقباست
در مقابل
آفریقای جنوبی، یکی از نمایندگان فوتبال آفریقا با بازیکنانی پرانرژی، سرعتی و جنگنده که به دنبال اثبات توانایی خود در سطح جهانی است.
🚀
⚡️
آیا جمهوری چک می‌تواند با نظم و تجربه خود بازی را کنترل کند؟
یا آفریقای جنوبی با انرژی و انگیزه بالا، شگفتی‌ساز خواهد شد؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/Futball180TV/94226" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94224">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffc86a865e.mp4?token=J7sYhyHDgloaxP9bkPWMMoSa-HacNFDU-kxOPW9ah25RO2tsppFMujFiOitEQ2w2bxuCVT_Ubz9ZiQXt1Z0HJnQjFVFs7msy7hLBKbZ-mYjWl6uNaUJCNao3loks1yxYkKxb6_LLUGk0I6nKNizr79Tp0RIDf5fH75GZgmjhgm4TQycDaxIXZwx5gHKCIfLEYpGbpyj_MjLRrfb7KPwaXnvQqpmzVmyAJmeW2-s_zs2zFvx1T0yzdyrhqCdJwxidutpAWUaCh8WnXKHHedcgm1lLgZLQjgTVEh8P5FqSnRTo8GTclKR34vzjBdSF5H1JXsm0WmyGVTfmsOkpbx6cOw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffc86a865e.mp4?token=J7sYhyHDgloaxP9bkPWMMoSa-HacNFDU-kxOPW9ah25RO2tsppFMujFiOitEQ2w2bxuCVT_Ubz9ZiQXt1Z0HJnQjFVFs7msy7hLBKbZ-mYjWl6uNaUJCNao3loks1yxYkKxb6_LLUGk0I6nKNizr79Tp0RIDf5fH75GZgmjhgm4TQycDaxIXZwx5gHKCIfLEYpGbpyj_MjLRrfb7KPwaXnvQqpmzVmyAJmeW2-s_zs2zFvx1T0yzdyrhqCdJwxidutpAWUaCh8WnXKHHedcgm1lLgZLQjgTVEh8P5FqSnRTo8GTclKR34vzjBdSF5H1JXsm0WmyGVTfmsOkpbx6cOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول چک به آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/Futball180TV/94224" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94223">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چک گل اول رو زددددد</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/94223" target="_blank">📅 19:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94222">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
ترامپ:
اینکه کشورای همسایه ایران اورانیوم داشته باشن و غنی سازی کنن ولی به ایران اجازه داده نشه بی انصافیه! ایران باید برای تولید برق و مسائل مسالمت آمیز اورانیوم داشته باشه. ترامپ دیروز هم گفته بود همه موشک بالستیک دارن ایرانم داشته باشه چیزی نمیشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/94222" target="_blank">📅 19:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94221">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eL-9lZTsTgUiFiRc_lbk-2jnGfdy7JU6AS1i-nwREtRKMpSTXVLKE19rEu_91TAY-DIKunUfHn7pfCF0gNF048qCDu6OQ32deYf-FS8YCRtTRfIxB1mbZVMmxWwyO80T-0p13FdVpMqwfG7Ia9C-mIFTDAg4qo1tnEwb00zk_MRDTuEywErvBqsMf9x_th7m9dgN91bhQkslo32StwNjscnwC23wTkey-mJSMNUPhmrOwiwYTrR2hu0DtH_146p8IkF6cCuWMqxsTu_PQ3CDIp1XOGABCKiCOKWwpUDuW90kEay3ot3eK6oZ4pwNn8k1X04yJdn6KUAjkeqkosUPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
مسابقه جمهوری چک و آفریقای جنوبی اولین مسابقه در تاریخ جام جهانی خواهد بود که توسط دو مربی بالای ۷۰ سال هدایت می‌شود.
🇨🇿
• میروسلاو کوبیک (۷۴ سال و ۲۹۰ روز)
🇿🇦
• هوگو بروس (۷۴ سال و ۶۹ روز)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/94221" target="_blank">📅 19:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94220">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b4f88afb.mp4?token=K_ppf5lLMZnu61k3dGeDEl0pWQ8WjJfsbdUbJWMcBfe1K-3w9C_UdLZ1mDvF3AVypv485WgnlmuL6usebOjlU4QwkWBVAsnRwt-rLW4IxljFeTv3hxrWr1SSu-ZNp7KsVgzM23YaSYnmLFN5L6ll2nWHhFHtKzW5fhHnrJjxYDf2G9o5E2xol2J9_x1AMVs5zG-Lk0mm1Abo20oLj5TZ3OdL7co_ACnc_oXd5nAbE86K0dO_aRXxVWpKJlx8TfuvMtm4pWgMAQaLXVHXqC5SAWEJxzMhzHoQj3L3VZQN44DIh4YyJ88o8YrQioqtZ42LbysNUuvpVEQJcQib0-b81w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b4f88afb.mp4?token=K_ppf5lLMZnu61k3dGeDEl0pWQ8WjJfsbdUbJWMcBfe1K-3w9C_UdLZ1mDvF3AVypv485WgnlmuL6usebOjlU4QwkWBVAsnRwt-rLW4IxljFeTv3hxrWr1SSu-ZNp7KsVgzM23YaSYnmLFN5L6ll2nWHhFHtKzW5fhHnrJjxYDf2G9o5E2xol2J9_x1AMVs5zG-Lk0mm1Abo20oLj5TZ3OdL7co_ACnc_oXd5nAbE86K0dO_aRXxVWpKJlx8TfuvMtm4pWgMAQaLXVHXqC5SAWEJxzMhzHoQj3L3VZQN44DIh4YyJ88o8YrQioqtZ42LbysNUuvpVEQJcQib0-b81w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
وضعیت فیلمبردار بازی امروز صبح کلمبیا که بعد تکل خشن خوسانوف اینجوری مصدوم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/94220" target="_blank">📅 19:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94219">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4N_UhXUNI72ahrNjTQWrJVMP7BGoAM3bZHBVxAouL3VOSYTzwi7WqpcuVXNE4ApDmNGb8RF9POTKTiGHh_COZqSukgS_xE33GjCuUNB1zKDUIwHl_icBLWiJG9WgxjMydQG6-C26bUMRNLg2NvJs0ygEtDTWva-45pAjV7GwyqYAIGqvLvxE8GQJnCiqOgbGHwYbZ6BaDXLZhdNotaj7D9Nc4qYtIOpZGRo3KqoFw2HAqpdDumCv6deO4y1tEe4lkwMgDQ-KyLu4Dpysb90UjC0arrYu3A8nToMMY9v_bKepfPsCDgGcXLpzHxPTyhmZWwe_kc-zO21t15pAALBSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار معماری ورزشگاه آتلانتا آماده بازی
🇿🇦
🆚
🇨🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94219" target="_blank">📅 18:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94218">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462604bf.mp4?token=soRxlamw9GTngkFach18Q5Z3qylXCikdgFTUNMXBHtvv75kQz1EvLY73SvAosw0uCrkJcvY-GT2MxGQwO6j6x5du7xwuk0V9tw9IjJtUgtEiUxLk9xBn9gu-6GBYtCBSi_LtDRkXb-pK6tPDv-NPmpPLGYz10DjklMyVXf53we5AphchwFseZ5VZWLPXiFWBQvSkAix_tWcEJEE-noSB4l738JhOwGa8SR9iK32bMM92xYwqoO7XYZXnl4L8XVaQ3uj9THluXaXUPo922Q8lEU6dirZjNxj9ju0mvTmeUAEEVcQRmNVXDwH2HnwDVWU4oKd1i9YwIB1Wbaw_diq8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462604bf.mp4?token=soRxlamw9GTngkFach18Q5Z3qylXCikdgFTUNMXBHtvv75kQz1EvLY73SvAosw0uCrkJcvY-GT2MxGQwO6j6x5du7xwuk0V9tw9IjJtUgtEiUxLk9xBn9gu-6GBYtCBSi_LtDRkXb-pK6tPDv-NPmpPLGYz10DjklMyVXf53we5AphchwFseZ5VZWLPXiFWBQvSkAix_tWcEJEE-noSB4l738JhOwGa8SR9iK32bMM92xYwqoO7XYZXnl4L8XVaQ3uj9THluXaXUPo922Q8lEU6dirZjNxj9ju0mvTmeUAEEVcQRmNVXDwH2HnwDVWU4oKd1i9YwIB1Wbaw_diq8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
برزیل از نمای نزدیک چقدر زیباست. بیخود نیست دوست دارم این تیم قهرمان بشه.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/94218" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94217">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gg8rHqVoe4d8TnrHQWl0mdy2NhcPS4fJmtTVbvS6E30KuM-Oyyp17LokVYq-QkyJLYq7D3aCqWynMpGOP2E8b5vUheXqRa2W9KkJUNFf6habqf5OaSbhAOpyYsquI8_FRLNGPF_B1Dsr1qPzk8EnmDgB-M-I7r10IBwrLyE2cBZj_Zl5eQ_FEcOE7Pjvz1Le4X9V0fDk8TkRWbLJnOZ-6hp5ELCyEYCrvASGTWsYs1IO034UDIcmO0LB-lfpJ28034mBO4mbGiNEijF_ScB3aew7MhyQLPaWfV3zhEN_IiyU16CmeIPboOi5Z3ac_IEM5gZdOB2JkUqa2PxzrijWEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیمار به همراه اعضای تیم برزیل برای رویارویی با هائیتی به فیلادلفیا نمی رود.
او در کمپ برزیل در نیوجرسی خواهد ماند تا مرحله نهایی برنامه ریکاوری خود را تکمیل کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/94217" target="_blank">📅 18:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94215">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LfagJDu820A3SLg9JesQlJyq7AZRsWSJUpzaYxp8uBynxGL2nm1xFzpwq0_v5B6OFgw8tgQm2MDYdN6yVuXS7KoXMT8jCIX33cOs5w8W9hVknM_BBX-lhdH8tn5IkngTTnrSmUTujz7WCibkE7YwqQz3dlnyFFI8XfCjUWMtt_cKzkuJixdTKjAJl_LEIGPs_OyVMJ7s4KFDUFRp1_zmsYts7TI_xrJGh5U68FPvTvsapdnLEMrHz_9c7F5q7yUgVoO1vwpKhISLfA-Uueuean5FP64zNyxu34dy9-mR6B_dj1KpVfoFeFS05zUqe4ny_B7W0qnp1vwY6Dj1QIDxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYrdPPb7Qnk2CKEZvEWTS4DAWk5lpBPoO0UjFc7OgBsYJ0OGyuXJjkYLNdjZUOsORRukCwrcwxa23-jeHWB5q_hSGQmLtTQkEpcG5SMjFbJWF9dTa90hCSo1Qsj1C79aoaGme6de_KBkm3WZTqih5QvuxCcMPLqrIYHlCmpIKC5_yIystTNVDEY2L3kMdyNNZ-T3TiI9Az0-nPuFa6IEm5PvES53lA22NelY4wkp3DXOG0pzOZ73MMSmn1Wnbb9nZHFBttFM8rl834yuGMnTkVzeCk8yJuZvzZGbkqpxeEBDcP1iw8Pn7Y5zdpMczoUx6x_7dTJ0-lJbX2ahEdKxeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇿🇦
🇨🇿
ترکیب رسمی آفریقای‌جنوبی
⚽️
جمهوری‌چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/94215" target="_blank">📅 18:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94214">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723f2bef75.mp4?token=aREAajqpciB2jLKIKMNGAeHjRuWTf4gUZRojuAhdLQHsG7uyh_BdixX2rHHhT2sIetLUKOgeJL_zIaGOwDJBJv2MFZuprlBYl1wK2dtFATvrKDpEBvL7InotC2KXbSBP-hJIHBLk7-v7gzXEHOiew6vJ7cNEcKG0vkzb_swp4Jm9jeCC45r0mwel5DQVPVAYS-64Z0BdVjEWcXgC3E_OzRynJexKDcdEgjuy6-WC3PGZry0cv_B9sGl70TPVwjzTB8gDczY6X6YUs1zxpWpHqiaBTFCyeYlnOH_zX4oF2puqTbJlSnjCYD9VfI_utjz0cjv3LDvsn-40wjeaYDlnKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723f2bef75.mp4?token=aREAajqpciB2jLKIKMNGAeHjRuWTf4gUZRojuAhdLQHsG7uyh_BdixX2rHHhT2sIetLUKOgeJL_zIaGOwDJBJv2MFZuprlBYl1wK2dtFATvrKDpEBvL7InotC2KXbSBP-hJIHBLk7-v7gzXEHOiew6vJ7cNEcKG0vkzb_swp4Jm9jeCC45r0mwel5DQVPVAYS-64Z0BdVjEWcXgC3E_OzRynJexKDcdEgjuy6-WC3PGZry0cv_B9sGl70TPVwjzTB8gDczY6X6YUs1zxpWpHqiaBTFCyeYlnOH_zX4oF2puqTbJlSnjCYD9VfI_utjz0cjv3LDvsn-40wjeaYDlnKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تیکه سنگین امروز فتح‌الله زاده به میثاقی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/94214" target="_blank">📅 18:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94213">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔥
💥
🏆
آفریقایی‌های خلاق این‌شکلی با موزیک رسمی جام‌جهانی ویدیو گرفتن. انصافا‌ خیلی خوشکل بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/94213" target="_blank">📅 18:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94212">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80aa310d96.mp4?token=fgNxCpClDgPOVM_rkhyCE27PlneXjCoPTxWGGacHr5LtzZnka0H9nV1yBrfWW2qNAIdDoCWZePPMtS5z_Yrz3muWuAICC6rpKJ3gPQZTWibbn5dumC-NS5qEWVuthcpqJOHcZ7ulP0NGl2U4Go5MGHW_o_mwsE9I8BPLFqCBbk2mkjy989ee4TfxjZrm9bNeuFYJkcBw3sOWbAJ5T75vBA88glB19h4Kzs2yGcfxK4FD9sz8JgfNCPzP32LyneZWOqWLXuuJHtIGhWzTdIui4wytTxvLXU8XQC9D56RSmf1rmbtL3WkW7GioedoXEOJ9JxoPuMbdYt48H1cqBnAnhF3r0WbgJqz00ul24krPbEN0-R9dJAV7vlIm4INcqDIr_x-l0mlcXX8ZyZmxUhjJwS5FWMzhxOCoAyLmI3hXcftlzr14qB6zgpGC7xxs77U9IU-K6Fm2dGJEbNCJXcpjdyq7nr6a7GoQJWvPv2X4aPnVkhMkw6j1AsWQ2EzjbohyowqL6Y2epz5ET63ocjRMHcNxdXccvoGe95vi6bbtXMNXNditGOar32pvgblquDrM9WM8vCcQg3REzkNvAValuIYT2QKNaR-OcoT46kuiSGZ_35NeumkQZinqoGPFIHQwiBc0qThmHyo2bA3x_57Jv7OfAw4EWYgOVXTOWpTzJ28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80aa310d96.mp4?token=fgNxCpClDgPOVM_rkhyCE27PlneXjCoPTxWGGacHr5LtzZnka0H9nV1yBrfWW2qNAIdDoCWZePPMtS5z_Yrz3muWuAICC6rpKJ3gPQZTWibbn5dumC-NS5qEWVuthcpqJOHcZ7ulP0NGl2U4Go5MGHW_o_mwsE9I8BPLFqCBbk2mkjy989ee4TfxjZrm9bNeuFYJkcBw3sOWbAJ5T75vBA88glB19h4Kzs2yGcfxK4FD9sz8JgfNCPzP32LyneZWOqWLXuuJHtIGhWzTdIui4wytTxvLXU8XQC9D56RSmf1rmbtL3WkW7GioedoXEOJ9JxoPuMbdYt48H1cqBnAnhF3r0WbgJqz00ul24krPbEN0-R9dJAV7vlIm4INcqDIr_x-l0mlcXX8ZyZmxUhjJwS5FWMzhxOCoAyLmI3hXcftlzr14qB6zgpGC7xxs77U9IU-K6Fm2dGJEbNCJXcpjdyq7nr6a7GoQJWvPv2X4aPnVkhMkw6j1AsWQ2EzjbohyowqL6Y2epz5ET63ocjRMHcNxdXccvoGe95vi6bbtXMNXNditGOar32pvgblquDrM9WM8vCcQg3REzkNvAValuIYT2QKNaR-OcoT46kuiSGZ_35NeumkQZinqoGPFIHQwiBc0qThmHyo2bA3x_57Jv7OfAw4EWYgOVXTOWpTzJ28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇩🇿
🇦🇷
مراسم خواستگاری وسط بازی آرژانتین و الجزایر. داماد چه ذوقی داره
😍
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94212" target="_blank">📅 18:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94210">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FccbTx7bfMXcnIuE_38POxPCKhgA2nknpxwEIvcDD8Zk-chzEF6XrZVm0cNVcykmOizOpcV9ilxKfZ0UVb00TmQBAUhVKSI8c2rPQXf5o4MaQgY0dGlmJBfeWXRkJyyEuaITLGRZ3wTPzsmGp9DMICWYs5xaZF-3Jq_O38xDVxW5ccwP5_OA_LcdsDVylQe-l-R9-OnnFwjpC9iw5SyepDj7EY3jZ6yZo9gREEEUKpIpkCUDuKfpgOUm-Mg4lzn73ou49kuh4IINGdDdYDE5LHFs10h-5lcn3Fz8sVYnOTBb7qsmv4awC4bIYo2ZZaq1hT-SlYQ9GnOwYr91HdR2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B38LmOjwomvgBl88-Fv9cCF80OSXqrHBsaMVRdUvwr7zH2-93vM6cy2jdgkzYjKsNElDKQRUYSYhiHx_if1pVyp9tTSl4MDL6iLxmksblM-PFTfM1w7PvJQgChie3q5Y-u3SjtTVe2dU45vVbiTjh7Z32Iu37chCJEWETfW95g8QtFeyRRg4CN4159now6CIl7kwZYdQ5KA1Ohpo1hyodrSkx0vfRXUZFY1xvIDf4JHwKCDr0JuwwrPlbvPBK43q92u2eOxkc4qQt1LYMjUhqjhHMe_LqSvS0R0NIpksuqtt9QyMnDeo8HNf_pOzieDIrxpi3EkcBWu-0tJVE4pNfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚪️
#فووووووری
از مارکا:
رئال مادرید در حال بررسی ارسال پیشنهادی رسمی به مبلغ ۲۲۰ میلیون یورو برای جذب مایکل اولیسه است. رئال مادرید همچنین میخواهد این تابستان هر دو بازیکن انزو فرناندز و مایکل اولیسه را جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/94210" target="_blank">📅 17:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94209">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/916898ff1e.mp4?token=n6YILFhyUhlnECE0sAKiz598Uk92QqWfH4vRNSdukF7YpFhRBW09BwMy0Ln010USehkD_YyODI5xZAh9TIW2JT_g4XmkyF5Yt5ArFiQD3WRQ5m-CaGzWDe3w-Whu1KhJixqgQLnH5AB9xaN4wEqoJM_LZzD9a65SnYqBCdZQmMnJ9I5PaGLDfLGxXSWKEUE3wrjhy3Jz6zQePZ8JSlY9Ti968kJnOM8J4OweivqGakL4sPMneHuBfGiyChb7hMhIPz2kcFRCeX8s1ZYSxB0ia6Y2YlWQZ__ZrKnNkp0YGCXOQajbzSUMI8ppGG-tP67RSvBYkcJatVg5b_WJp-NSow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/916898ff1e.mp4?token=n6YILFhyUhlnECE0sAKiz598Uk92QqWfH4vRNSdukF7YpFhRBW09BwMy0Ln010USehkD_YyODI5xZAh9TIW2JT_g4XmkyF5Yt5ArFiQD3WRQ5m-CaGzWDe3w-Whu1KhJixqgQLnH5AB9xaN4wEqoJM_LZzD9a65SnYqBCdZQmMnJ9I5PaGLDfLGxXSWKEUE3wrjhy3Jz6zQePZ8JSlY9Ti968kJnOM8J4OweivqGakL4sPMneHuBfGiyChb7hMhIPz2kcFRCeX8s1ZYSxB0ia6Y2YlWQZ__ZrKnNkp0YGCXOQajbzSUMI8ppGG-tP67RSvBYkcJatVg5b_WJp-NSow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🏆
خلاصه هفته‌اول مرحله‌گروهی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/94209" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94208">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37dc9fa1fc.mp4?token=K6c3WpMtJqtXgjI6lqOd-lG_NPb_PkscUnXXY7EpMgPg-IPF2IICJ7Bmt4WfAYnjui9P0jMVQX1PUp-pl6TlkvapI9XHRRJXj9stUxsxiHgDydAjAkqYbnSafrZReJlYCS8JcdfK-DETgDhYnPXO_91UEB-RpEoJQ158qkVE0CIKt1FoGd13mFoqJwexnFbU3_scrGjiEd9QQvVcEt2k54cybr1izQqmAasCYAxA2v3miRhLaQqSNbEX0DOT7VNHq8s8NC6INES5qPjyoWDtjklkHJITsMSDTq4Iv8S4ghzdpXW_rC4m4LEMNeuplYvsUthNz6hHdDgQB7ITLa0YZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37dc9fa1fc.mp4?token=K6c3WpMtJqtXgjI6lqOd-lG_NPb_PkscUnXXY7EpMgPg-IPF2IICJ7Bmt4WfAYnjui9P0jMVQX1PUp-pl6TlkvapI9XHRRJXj9stUxsxiHgDydAjAkqYbnSafrZReJlYCS8JcdfK-DETgDhYnPXO_91UEB-RpEoJQ158qkVE0CIKt1FoGd13mFoqJwexnFbU3_scrGjiEd9QQvVcEt2k54cybr1izQqmAasCYAxA2v3miRhLaQqSNbEX0DOT7VNHq8s8NC6INES5qPjyoWDtjklkHJITsMSDTq4Iv8S4ghzdpXW_rC4m4LEMNeuplYvsUthNz6hHdDgQB7ITLa0YZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🎙
روایت مرتضی پورعلی‌گنجی از مرام و خاکی بودن ژاوی هرناندز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/94208" target="_blank">📅 17:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94207">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/182af5a6db.mp4?token=i_kDuL2vTmT4ZKJxymFttjubani8-hMU3VBqmtAfA_p1iD72msvLGuGWZbUdyyrLZC9D0orKY4RuhDl4R7FjdMtm06of6b2ed4lEvFiYTuyEg9LG-MBbv76rtn0Uuc3nPP0808AI1qNJVRI6MW95lnB7geL64jPlRzmJ7jFHlK_fLsCzE6ZQjj7Cdf45R86mqRfwOJ2QglMl8pgneIy-FGCIR2AzcAKd2dh9gVawBxNYw9e2X5A-cMv0GjLJ1cUZUEYJMo7rrpLxLGWpg4GTnaHT5wPFgzPokcV4pLcCjckb0plKaQbsMadXB9WxYAmKChgUb2MplcsHeUgZCBbZ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/182af5a6db.mp4?token=i_kDuL2vTmT4ZKJxymFttjubani8-hMU3VBqmtAfA_p1iD72msvLGuGWZbUdyyrLZC9D0orKY4RuhDl4R7FjdMtm06of6b2ed4lEvFiYTuyEg9LG-MBbv76rtn0Uuc3nPP0808AI1qNJVRI6MW95lnB7geL64jPlRzmJ7jFHlK_fLsCzE6ZQjj7Cdf45R86mqRfwOJ2QglMl8pgneIy-FGCIR2AzcAKd2dh9gVawBxNYw9e2X5A-cMv0GjLJ1cUZUEYJMo7rrpLxLGWpg4GTnaHT5wPFgzPokcV4pLcCjckb0plKaQbsMadXB9WxYAmKChgUb2MplcsHeUgZCBbZ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رونالدو نازاریو:
به نظرم اگه یه نفر باشه که لیاقت اینو داشته باشه که جلو بزنه و عنوان بهترین گلزن تاریخ جام جهانی رو مال خود کند، اون آدم کسی نیست جز مسی؛ مسی بهترین گزینه برای داشتن این جایگاهه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/94207" target="_blank">📅 17:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94206">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c565269871.mp4?token=rh6XiEIZWljBCu4ljfezMAfVqQFTcJCI0IAeal4hMar4jYqqvR6mL4ppQ15OZsMlJ-_8slxbYflKHDocQfw9hc3mH3WG1QZRzJg8TwkMKgxJcd9yyiLpGuhIHYlAYeOeJXATY3vXBAlO0KMpAljdTTbQNyDFFe_2My2wrALZVicAVg_hWcqr4oEhcbs2T7d-P4IyLI3WLL_TvI_cqEY9jRNqdcISMk2jK9HAAaMxfet_J9cdj1CmDNs0ubXWZN1L2EK8gaW96oF9tMWKZHb5Df28VfwNjHXXCveEW2OljttBR7bpCzcmsLPh9ZY5ybK2yM4MUwxsc2VLgbMloS9vYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c565269871.mp4?token=rh6XiEIZWljBCu4ljfezMAfVqQFTcJCI0IAeal4hMar4jYqqvR6mL4ppQ15OZsMlJ-_8slxbYflKHDocQfw9hc3mH3WG1QZRzJg8TwkMKgxJcd9yyiLpGuhIHYlAYeOeJXATY3vXBAlO0KMpAljdTTbQNyDFFe_2My2wrALZVicAVg_hWcqr4oEhcbs2T7d-P4IyLI3WLL_TvI_cqEY9jRNqdcISMk2jK9HAAaMxfet_J9cdj1CmDNs0ubXWZN1L2EK8gaW96oF9tMWKZHb5Df28VfwNjHXXCveEW2OljttBR7bpCzcmsLPh9ZY5ybK2yM4MUwxsc2VLgbMloS9vYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
حسرت یه موتور روندن اینجوری کف خیابونای ایران رو دلمون مونده
😢
👅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94206" target="_blank">📅 17:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94205">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tvnw5eyJ1pRGKqDkwllOMNLJIettzcBnoEfSfqoUIWFCEHe78clMdxn647U5rKs3VzVCfvapQL4q1HImA_Bx994k7KL8JaocjXAXAK9LBTeCUqNSip2_EY67ZK60oFiunp8_ZmFxcqaD-dhHfNuXStnQ3kqQzvyrTHuT6y7kj1pOVchAsj-BrfqLLjibjNn9zPrQj8mRF1UEvZLBTDJFRRsRYXDbwXILsUPl25U5S9WKVVHR_AV-3ptmflnyRN_ZZ_M2KY41VZQ_2iuozE5vz_2chzfC8i-oHDkO3nz5ZWVq7F-mBbr9FOYmWSyPSeHwFhWzPBl9B4146cl0GcDVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پیتر اشمایکل:
روبرتو مارتینز، بدترین مربی تاریخ جام جهانی، نسل طلایی بلژیک را نابود کرد و این برای او کافی نبود. حالا او میخواهد این کار را با پرتغال انجام دهد. آنها نباید اجازه دهند او حتی یک بازی بیشتر روی نیمکت پرتغال بنشیند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/94205" target="_blank">📅 17:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94204">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUeSnnMeWOyrHtPXjcMTus8yqPYN8Bh4KP2wxk5RE0VTemXdxURcYhm2ZPM7oykfQqJ1g8rL7sk4QfHCRzlluyjJNOJXt7fDX59j3dv9CzXlp4kTG7dwvCbNLBksAF5vrq0iEf3PUjA_-e3cvf0FQ0RNNUQKBBd_8tolfP-q6-arCwF_TlUI2qzf3onY-XyA6_pBYaPqfJ5Jb6AMrHRj2XcA52u2rkt2XRG5kNPk1YO034ERdRIUfWu0F9NeL4N2CNYDeInv41drIq9IEARov1gAbsZY4TdJ9k98PNawttLKDMmqETO-BxMmtP85B7UYItocAAtAIEh9QYH5RqGxZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
فابیو کاناوارو چهارمین بازیکن تاریخ است که برنده توپ طلا شده و به عنوان بازیکن و مربی در جام جهانی شرکت می کند.
فابیو کاناوارو
فرانتس بکن باوئر
اولگ بلوخین
مارکو فن باستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/94204" target="_blank">📅 16:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94203">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7bc36d5.mp4?token=mRXtv-BoidrqaP0Mx6HrsmbnzXkNwvdC2tNxObjPc-oElPerE7AVBeOrSCQWHrJSowTUXvmW9OblsIqmY6FMo_A2Cwf3z0TkdoddreCV3A8QY8okXdRUvxQzIyfU78ktG268oIB5A5GzlzgJWNHM6feuFOqY9_ik7rkECGt0--8AgRR_g5-FFo8qt1eRb6OkglWkL6gErGPYHL9T0gdKChypi5gWfY7Y8TAONZcEOEcBDMrKKx_bK1qPzmAstDbLA_xfFt-TryhSPNxqgKVX18dzSI_ZxADQGmCc61NI-wkd_HVXeWYPNZaZYLxOX6YgEw1Dq307D_IJT37W_MG8Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7bc36d5.mp4?token=mRXtv-BoidrqaP0Mx6HrsmbnzXkNwvdC2tNxObjPc-oElPerE7AVBeOrSCQWHrJSowTUXvmW9OblsIqmY6FMo_A2Cwf3z0TkdoddreCV3A8QY8okXdRUvxQzIyfU78ktG268oIB5A5GzlzgJWNHM6feuFOqY9_ik7rkECGt0--8AgRR_g5-FFo8qt1eRb6OkglWkL6gErGPYHL9T0gdKChypi5gWfY7Y8TAONZcEOEcBDMrKKx_bK1qPzmAstDbLA_xfFt-TryhSPNxqgKVX18dzSI_ZxADQGmCc61NI-wkd_HVXeWYPNZaZYLxOX6YgEw1Dq307D_IJT37W_MG8Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
یه ماه دیگه میفهمی به بختت لگد زدی مردد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/94203" target="_blank">📅 16:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94202">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vi-gbulRr-J65gd8Jr5FM321N9_-vkTL-x8u_uQguSlF7i6Yuvg4MBdyYBJVFhmGNbuyBKetDSiRaiO40MgphFNgNdq5ESbVSb5qo7qnKdYMPrUwdbmvD5vLrM1zwNWBuHiGQNnIznWf9liQj4YCYwBEPTqCd7ieBA1KOIH1gZ-huTbt6-6FNj6X8Zu5QeyMcv6ub4y4vqWXF53rNNB1IQ7mJahHm8sCOTq4Qm7XsuP-mGY-RbHMbk0UPUYUqGC1L5dw5kUTSWte6Ez2__1yiczeC4xYVp2kgdfsngZixU696wNEaNv3NbCcNzYI1uUc_CqONCrB_LUXliBOuuzNkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل تو رختکن خطاب به بازیکنای انگلیس:
دلیل اینکه این پست رو قبول کردم خود شما هستید. هدف کاملا مشخصه: قهرمان شدن در جام جهانی. باید از همون اول درباره‌اش حرف بزنیم. میخوام به جایی برسیم که قوی‌ترین تیم دنیا باشیم؛ تیمی که هیچ‌کس دلش نخواد مقابلش قرار بگیره.
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/94202" target="_blank">📅 16:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94201">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxEUbJGjxkEf7F40QVvcV70OT19wqLtaytFALEjc3HCgQ6BkIcRnJ4U_R0rgkuB7MnIs7bEY7Zitvkhhl1c3hDfudbgv88-mtNePK8zBJiqo2KbVnzlULKPOsRjjdCRsnm4C7XjWsDF354uMNWOrkTMsYPnaklD_0j07qh0UGe70h92rKFbmPwqw_8UutouMtO4_VT68A-wRfcRJgv8kX2vCv9Im_4NtXtWDrKcqM8ZqKXcEwfvYEqXdw1HkfiGHiaG3bgHeqp4IDBFQDWotR26qNa8YHW-XhfdF0brG-NMvvyU79Tgu23jDaeFsPSed9seSHSVpO8wK1CegSC_nEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خواهر کریستیانو رونالدو:
بازیکنا انگار یه‌دفعه یادشون رفت چطور باید پاس بدن، توپ‌گیری کنن و حمله بسازن! تمام بازی رو به عقب و کناره‌ها پاس میدادن، ولی اشکالی نداره؛ شروع بدی داشتیم، امیدوارم آخرش خوب تموم بشه.
🙏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/94201" target="_blank">📅 16:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94200">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTQaSUaSR-XPYofidNaVmZ02O1by8surcdsii_dfVsjDOGeMahXkBS5Rfd9A1IrvlhAohoGjCEFCUCgjbSxHuMbpeCZnjYeN1-MgkyVWSXYUPz4P96YpmvP6J64lKcMc_yEhzkvs2oLBoS5jZpPdcRBCQY253xtpe9OjvLnQwc9Jy6giUeKMfz7BmGADvQR6fkoMjlaKHAZsTRbMmHgUKRWotmWM91LmY4tov7vfZTp1asG3_gt-Sv_4b4xM958NuJW5cpHUjh61NnESy--HPwVDez9aJIsrt0HyYDiKY9uM3ruTb7n7VoVxWEyXVi69VjU3__iLkrFQVciIWOy6VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله
جیمی کراگر به رونالدو:
مسی مشکلات تیم رو حل میکنه، اما رونالدو ممکنه گاهی خودش تبدیل به بخشی از مشکل بشه! مسی سطح بازیکن‌های اطرافش رو بالا میبره، ولی رونالدو دیگه اون تأثیر رو مثل قبل نداره. بازیکن‌ها رو باید بر اساس چیزی که الان ارائه میدن قضاوت کرد، نه افتخارات ۱۰ سال پیش! فوتبال بعد از سوت پایان، به گذشته کاری نداره؛ فقط عملکرد امروز مهمه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/94200" target="_blank">📅 16:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94199">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b65f43b16.mp4?token=us_RapEE4cYsU0szxaGyrrtEhjzfJ1HpjLO5_nCQmpm3z8LAATNlWHC9WqLjqB_4DDKvGggEuJ2G15vXP6CzojGdFgYSjlwWj4MufEB0dTptZRuqY8XhS2G3vABN_8kTU79WWNj5FKfQvr9UGrGqpy9ivQd1cQ2oVCwKTcVMJWyYuR3xe3eGDAHgVlZOViBK6xLdnLnZ3y89Y6DxaNRlZUVNzV4iShwFeOBYhjHx1K1dCzimo5Zat1PtqktgftyY99c-1sib4Z5NZNY6jaT3LQtN6YK_FkhuJhb8n6M98vQswEjkbAWLqatMSeIvGxuXnGS9FU_MKNGrVan4hT78hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b65f43b16.mp4?token=us_RapEE4cYsU0szxaGyrrtEhjzfJ1HpjLO5_nCQmpm3z8LAATNlWHC9WqLjqB_4DDKvGggEuJ2G15vXP6CzojGdFgYSjlwWj4MufEB0dTptZRuqY8XhS2G3vABN_8kTU79WWNj5FKfQvr9UGrGqpy9ivQd1cQ2oVCwKTcVMJWyYuR3xe3eGDAHgVlZOViBK6xLdnLnZ3y89Y6DxaNRlZUVNzV4iShwFeOBYhjHx1K1dCzimo5Zat1PtqktgftyY99c-1sib4Z5NZNY6jaT3LQtN6YK_FkhuJhb8n6M98vQswEjkbAWLqatMSeIvGxuXnGS9FU_MKNGrVan4hT78hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🏆
خبرنگار: «ولی تو در کنار کلوزه، بیشترین گل رو تو تاریخ جام‌های جهانی زدی؛ این عدد و رقم‌ها برات مهم هستن؟»
🇦🇷
🎙
لیونل مسی: «نه، راستش نه. واقعیتش اینه که خب باعث افتخاره که اونجا باشی، چون نشون‌دهنده ارزش کاره؛ اینکه اسمم کنار کلوزه باشه یا اون بالاها باشم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94199" target="_blank">📅 16:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94198">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2d6b9ef8.mp4?token=aDW4qf-euuz9llkwIFwB0ep0HZ3zPqnJyFs27NIL5cBAcFmMtFhwOwcqEQx8gRIysW81usrpjBy5lkrXa-Mh_IxJOo57IL1snCriLSgSePceiPtoSisG8IHndKxD_5YLqS_K8y_YFr93jbkbQJmWUVB49fc65ciWKMbTy0kr-uR_S1geeQFeKqhQ_2FyhTMUv9LH_JZszhjflFzUCtddtxCEvwm_UrFy3NHvUfNfz9A36g11oYNNJH3evLuw5_nju7wD5E6gotOXvTYXaUiYsxpC5z7gQLqRfy4FgvIMUO4TqL-B_KC5H_qUgSu2ZyclUAMkDoze9UfYdpD1q33uL2yrrW8E_AVmDuiJqYXNJKiYZ6vKM1Zmk6VJl8zAAoBKNX1N2dWPEVp_MeqWOIseEYOwEXcC7hhjOJi_HWyCMWbrkD0yeJxALDEaGN-FInw5cft0boAAD_L1ztUpciti3OVnryYKgW6m1AEjSWcpJmD3JqneVxUyuL92csBYgET5-hVF-b8iGl05NKmZt2Q76Y5_Ib6XMuXbJv_zzSL9MtrGFTOrJjnelO-TlYW9Ay6xgnUKoD47xgZ9_EInMePXHmNEBczeXGKV4qOOVDl6nbsKjuqoY-LE1ZzLVZAC78Ow-C_BnCMif17wk20TeLkrcEDWQ1m8bAzsh5VwksUMD9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2d6b9ef8.mp4?token=aDW4qf-euuz9llkwIFwB0ep0HZ3zPqnJyFs27NIL5cBAcFmMtFhwOwcqEQx8gRIysW81usrpjBy5lkrXa-Mh_IxJOo57IL1snCriLSgSePceiPtoSisG8IHndKxD_5YLqS_K8y_YFr93jbkbQJmWUVB49fc65ciWKMbTy0kr-uR_S1geeQFeKqhQ_2FyhTMUv9LH_JZszhjflFzUCtddtxCEvwm_UrFy3NHvUfNfz9A36g11oYNNJH3evLuw5_nju7wD5E6gotOXvTYXaUiYsxpC5z7gQLqRfy4FgvIMUO4TqL-B_KC5H_qUgSu2ZyclUAMkDoze9UfYdpD1q33uL2yrrW8E_AVmDuiJqYXNJKiYZ6vKM1Zmk6VJl8zAAoBKNX1N2dWPEVp_MeqWOIseEYOwEXcC7hhjOJi_HWyCMWbrkD0yeJxALDEaGN-FInw5cft0boAAD_L1ztUpciti3OVnryYKgW6m1AEjSWcpJmD3JqneVxUyuL92csBYgET5-hVF-b8iGl05NKmZt2Q76Y5_Ib6XMuXbJv_zzSL9MtrGFTOrJjnelO-TlYW9Ay6xgnUKoD47xgZ9_EInMePXHmNEBczeXGKV4qOOVDl6nbsKjuqoY-LE1ZzLVZAC78Ow-C_BnCMif17wk20TeLkrcEDWQ1m8bAzsh5VwksUMD9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🏆
🇦🇷
حاجی جو ورزشگاه بازی آرژانتین رو‌ ببینید. ناموسا چه‌حالی میکردن با لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/94198" target="_blank">📅 16:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94197">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb2cdbc7c6.mp4?token=UVEhOSlevnIYxKozqRpexFc3V2wzMwFq0zl0BEaUPBZyr5tXAkRzAzttTqQJ9ou875ac2mGPOgSHZCWAvvXOkCD2wQVDAz8Zw9NRyyTjwqdgfv4PE1K1vW775F0qMOXVSEvBU_agp6-1JyhGPIi_nC-s0cdgiEIBrFr2cdgw_VpC1TKr8LJBRm_zmjPrRhLyt4cgHxGrezD2hTMneY2dOT94H84Tu5PlAI7evfiv3Y9hMqnQo0b5LQSaVJNp53s323el84oLmnayxLVc19fBxx4hguezEdLLF4dHo_JgBO04df-8u9gI3FycFxfJRFQXSFGLl0ryxM4H9HE_vjbEKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb2cdbc7c6.mp4?token=UVEhOSlevnIYxKozqRpexFc3V2wzMwFq0zl0BEaUPBZyr5tXAkRzAzttTqQJ9ou875ac2mGPOgSHZCWAvvXOkCD2wQVDAz8Zw9NRyyTjwqdgfv4PE1K1vW775F0qMOXVSEvBU_agp6-1JyhGPIi_nC-s0cdgiEIBrFr2cdgw_VpC1TKr8LJBRm_zmjPrRhLyt4cgHxGrezD2hTMneY2dOT94H84Tu5PlAI7evfiv3Y9hMqnQo0b5LQSaVJNp53s323el84oLmnayxLVc19fBxx4hguezEdLLF4dHo_JgBO04df-8u9gI3FycFxfJRFQXSFGLl0ryxM4H9HE_vjbEKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلمبیا با این هواداراش واقعا شایسته برد و درخشش بود و هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94197" target="_blank">📅 15:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94196">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7zzqnUQ_Lah1IH9dsFfXvBx_iidVZtFvrle-ZIqx5B5lY39ur5ccgNXdjM8b78srptD9y42-07FoqnEwvT7N0JSgbXgVlGgjOk32I0ulImojmzdRZZ6j90xmCNE0jaHVQxdJlYKqyNDcWjNpGiy0_b_culWBgmz381RLEOMpeg3lyQvz3Et5Ci8zuuCIlRN1gaNvjuKvHfi2m9d-kmgE5yooXCOUyrOhpfEmF57gjiAhhgPC0ymfJ2B0RFBAdNBP5NY4HpAUQc-ks_EfY00nwW4GIE_AhtOzNuHE838FJCG1l2GYCLJSlYTgpJBUKJpgHh5aQfBDeTjfU1P_xHS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
به گزارش موندو دپورتیوو، مارک آندره ترشتگن و ایناکی پنیا جایی در برنامه‌های هانسی فلیک برای فصل آینده ندارند.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94196" target="_blank">📅 15:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94195">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65efc6e80c.mp4?token=NQ2DaTHsuSLyKAYIUQJ6bvIjxvYaVHqyQdeiIGuwgAmIBPkV-GFTUMKDUJREMKCKCn4A5fBHC7OkMmzGOjPlezp7z0_tEtkBxE3LV6lqqeLd1eyVTko5RupD1P5w_RiAhnyIZEzs-5-FnycWZVeHe6IgY4D5v6SxdEV2UuVHk3ALFjADrDW1YGrYQQMPHTrfQY2_XKf2OZCKWMnfzzc-3tpFyjuAGE2fLtsfvJmLds1vMcUA3XcrcCmTKFx9fR3uCpUJMZYz92Dwr2ZVi3Awkoh6nglKvza74bDN_PlQdw5xpyP00I7htR0mqk19-BWiIi-Xzqk-uIPMdQWPLtEomQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65efc6e80c.mp4?token=NQ2DaTHsuSLyKAYIUQJ6bvIjxvYaVHqyQdeiIGuwgAmIBPkV-GFTUMKDUJREMKCKCn4A5fBHC7OkMmzGOjPlezp7z0_tEtkBxE3LV6lqqeLd1eyVTko5RupD1P5w_RiAhnyIZEzs-5-FnycWZVeHe6IgY4D5v6SxdEV2UuVHk3ALFjADrDW1YGrYQQMPHTrfQY2_XKf2OZCKWMnfzzc-3tpFyjuAGE2fLtsfvJmLds1vMcUA3XcrcCmTKFx9fR3uCpUJMZYz92Dwr2ZVi3Awkoh6nglKvza74bDN_PlQdw5xpyP00I7htR0mqk19-BWiIi-Xzqk-uIPMdQWPLtEomQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
کف خیابونای بوئنوس‌آیرس این نقاشی و بنر درخشان از لیونل‌مسی رو نصب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94195" target="_blank">📅 15:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94194">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuzXgoPGwWq17PTyZV56_csMUTWYJX1OWhM7s4_iLmQNk6jCv9RpsCvN3oc8frNosVwQq7GDrw3r882bvnvYpnd7RfPV9qfV4A8vX1cB6t9b6g1QvLWJ84arOPzKSWKqhAZOp-t0Ebryq-FX9W1NWb8QncZAK5VRKkMMcTiKt6tqdOf_CnfPsuxjvzsHqqKtKa2ECFRm0KuA0kzVpDt1Eb2bWhPkcMDrTY-zqc2QTf1EtqbuXCmIquWmDSm11NFSKqOKLACk-PTkw89Zt-OTQ8kxTYjI35jNympmpHoT-kwaInL54sspGV36RXVX3L2tq3UgTIGKJNk_RO-q4_Hfpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
خوزه فلیکس دیاز: ادواردو کاماوینگا اصلی‌ترین گزینه خروج از رئال مادریده؛ هافبک فرانسوی مورد توجه چند باشگاه پریمیرلیگ و همچنین پاری‌سن‌ژرمن قرار گرفته. البته خود کاماوینگا به هیچ وجه حاضر به جدایی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94194" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94193">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/94193" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/94193" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94192">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jinlcn4xetDLA6nEkKH8Ssr95CpnUjZ3A66Y_OdTHUBUumfw54R-Yp-wjLpYfEdnpvAkK8LXySlGAl4UQ3C2WWTEZc5wthCSY3r1QJk1PjtMZJofaKF43mxuOpICr1baS354PhmsAxo--6hNj0E25coJinPuzKhxbLsfWkVHxjnpVzma7SV0uNu0AGmkI4TYngbsLkakiQkPL3v7gNp9z7p6cIegTokr8oGCHAtzgZNndijRMkECYFvvZ0TT2TfkPfqx2KdWECKzP1rva6Vks16lk6_KAvj-OcI7NSm1LYFPVej-umNFrZ5v27ogcwuDSxpW7yp7SN1C_vHJbOcP7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94192" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94191">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BY_NMAnjVLKnuqTBcnFBc1fnc8ld8E9Bz_nphrwPf90-T8GEy0s2zfOoi0Jhut7OQFJ7pbtBcgIyr54bMubljvmLZCjfDsnojlaYyNUL-WI0kOBb1_x_r1rXDxB4nvNZFFH1sAeTmsriNzpB-nZWiEbZyaihnubfziw9Du9Nren5ZjNRuKkZ1sKYd-WAR8W5pEJJTyVutkRXemiiB0w4gDES8vEfYlGJdSaHpXdTNYXrp7dy4eVopOP12574I4TYnmhNHSPwYkpE4PKiH1d-WCU2R8PEADuc9qqjbmSxrbvOTvOOrJmCI1qL8PpiAEhjFmrI8eZaYPj015F56-MEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
خوزه فلیکس دیاز:
ادواردو کاماوینگا اصلی‌ترین گزینه خروج از رئال مادریده؛ هافبک فرانسوی مورد توجه چند باشگاه پریمیرلیگ و همچنین پاری‌سن‌ژرمن قرار گرفته. البته خود کاماوینگا به هیچ وجه حاضر به جدایی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/94191" target="_blank">📅 15:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94190">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozncJUc5-kN25-n1CFxaJtaZVDGgzRfTMcskAeNWmQnQzglDpj_MLw8tTmjUYOakaFmtsmL5vQ0iV8pz8Lvspr_3TWS_v4Hh_Z0b8blD-Gu1Rz1Xha_y0JUhKRyvCuzYXx6DKlXtEa2535Wo8erWv_RMYJvA_nxeoekwFn_d0R91jx8K83etaIWhwDWT9kJWqRhuSwnGnJ9HQWVbSXF-A3kzs388iwCHpD3c4UGOGgf5ver9H7XOhhjt9K1BGO0X2SknW89EFG0YTB6kGlmf_5AgVZcm_546T-kVwHuEsiQea4A7hE3NkgCFI6Bn8BLlfyoFi6eRjXQaRGFjqbInQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🚨
#فوووووری
از رادیو مارکا:
فلورنتینو پرز در حال آماده‌سازی یک حرکت بزرگ در بازار نقل‌وانتقالات است. گفته میشود رئیس رئال مادرید روی یک انتقال بسیار بزرگ و جنجالی کار میکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94190" target="_blank">📅 15:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94189">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFG4dJi8Bns8mP204Ea8Cbj86H418txq9YC_5L4LRj6KSclnDX7vT6uqk3tQrqzZLz1yTbwm2nvrIw1V3nHXoGOjdiXPl15xp6r8xLlgwS4kCzaxqti4G0RxJYf1eKA3ksywceJXsWKJ7VXZIAgP3BDz-RXDE8v_olOOfQR-qxnV3tS8x2Kl9MhUB8XluFRygXXa4n1Dd8HBpMSHy2Pd2LMPaMV_37D5Q2tBxacoqeVHwY5X4LvvIYNhHSMnlzIxqChtqI2IupIApsdZ9ImkRSFKni5ZK8x2TQvw1kJ8wiqS3VRa51uoiPkaHaEcYBSbQlcqRqqzLO2C15K3ENHCHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🔵
بارسلونا از ادکلن 75 دلاری خودش رونمایی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94189" target="_blank">📅 15:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94188">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC7PckTcle9HeNbDUm4Hh8O5jDZUfIhdgZux-N1bmyokEq7qFfr4zQmhX_HDEnNOtz2NHO5TPTGB6-tesOsUYrWJ0fUWOKDPhdDXfkhWL1Tw0KvZaAMuNHZ1lBi_1LvQTTpzPUHiORttbdWtYbSOzvNw80V89enqTrD2AM7ZbFQ6-L9Yo4uGyvgFJfDcpYPRHxyR6MDMd0kCcy0ez9KXsdc9M_ftCtQKufxBdRJxgAu0hnqDuFRuCUEEVjmozOMXAxeaK_Qpm6Yfb2fYU0vyOSsSeJk3V5JDti5yFaHDxzuZSM0U_YAEGwYmYjZkYPnay11O9Jg6cUP1r0K_MXkGuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🇦🇷
زوج آرژانتینی بعد برد فوق‌العاده کشورشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94188" target="_blank">📅 15:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94187">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrRmT66duP24SULRwmDIZzij14DbOfzEfKnXLCg6dMh-J3EBbTkVTxNZHuqdh4S0YTw-KjsMfazIOrM1o9lH2pLRK_OwsFCV-onIbOhHnoEdpFg3eRvJKx1-Ashia9cRhDh8mRDZeYw1e-8IwMlo2ZrhhkxPcUO8n8AyP3y8dey_mK3rb491BW2sZqbRkMvZMkUn3XKvvGzQqVST9FHL1_-BxOGzaNJ4O4kq-xuY_YrywzpuFgcEZ_irvDpmncaWFSI49y8vktG0rbOtuZDU61kBPGmDRgKAXWwHZ0UCUeDVpPdXO1cuzmL-__lffzTVtIyAb-PrA8qfIrIoO01Oyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
آاس
: رئال مادرید استعداد مراکشی ایوب بوادی را زیر نظر دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/94187" target="_blank">📅 14:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94185">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kh_U0yr5koEZBryI6QwJV9KTjs703UQAxkQvHWHijV55TZGMkR99x5aNA1gFWQN91ooh3jd5N8cxlgkOMowfvcyIyaRemtBoMwgg8rx85yRQ_jvFfuYR4PNw6wqri_5JIzQOzAhEq9sBc7dE1sNPMUTx6_TW8Eq-IU8iLjPtrQuYYKDTLSUdkn0yd7lMWR-BBNh_5R6dQTs_MNp8ISjnuTeAzMvzeW7NPjAXzrt2Qrt6303KOvdqpRpMN3qHmnoJDlv_44w6EgsolnBdvA3JQoqOthY_czKwpayFUwC32q-HSEiHx2Hd_BLdZqRStlGZ1tNHLJHBhLi4EbMkHOmq6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rch99HdHllO3dsx81m_Cl9OKHTyUn365ZoLBCO6xt5WM2Dr9gJ588hBlJ-ewdg09wNLvB1vPzX5E-TCts1CTR9tMk_2epv5lESGtYMVFeu746QaKBdfIkWfHcfM1xvRsgYns4Ly87p6fYTI88bBCnirERlKvdIIGAaOmd-SXwElSk34UvF19mb-PgnIWWfievDt7Bqaw9YMJtneb4FRb4q0mEDWL1-T-dbaWzYs7RuXLzsJyfWKGdrVp2V2lY3xXobi_L0G3nk5PvI-hxZ6-IVTMvDxpcsex-2_mG5yub9IKAURQKXnlHgT_B-h9mTjzK1WjlYPq5epEG3717pRo_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🚨
فوووووری از آبولا پرتغال:
⚽️
روبرتو مارتینز رسماً سرمربی باشگاه النصر شد.
🇵🇹
ژرژ ژسوس رسماً سرمربی تیم ملی پرتغال شد. اعلام رسمی از سوی النصر و پرتغال پس از جام جهانی
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94185" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94184">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54bbd91a7.mp4?token=SV74HpkFrHAgy2QP-X29frnKLn99DKark5LuhkyCqWujyXxw85syz7nTiqAytIgkw1LlMjg26Q4reFoxbTN8VZlGFWdZBpQkVkzA3pv2tIp6V9lnw3FkU5aMMuB08JB6MnybU5c-S81-tfSwugaylnFfl8m0tzbp8C7ICUtzG-N2m46h8QJLCy7qdaoetv1z2nGRUnbBWv4vR1tQ5yQpyTDrzhDPwWUwQx_rc1JpnPBH_PrH2M7RZfBOyjQtLlZfYYx7E6Bh1eDvp4jJA62NSOxD2bbP0IY63vXBtnx2mRRiRaKeOxLdYHquLTjRfTDRZSuvUsADFBfWQBSw7oTQzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54bbd91a7.mp4?token=SV74HpkFrHAgy2QP-X29frnKLn99DKark5LuhkyCqWujyXxw85syz7nTiqAytIgkw1LlMjg26Q4reFoxbTN8VZlGFWdZBpQkVkzA3pv2tIp6V9lnw3FkU5aMMuB08JB6MnybU5c-S81-tfSwugaylnFfl8m0tzbp8C7ICUtzG-N2m46h8QJLCy7qdaoetv1z2nGRUnbBWv4vR1tQ5yQpyTDrzhDPwWUwQx_rc1JpnPBH_PrH2M7RZfBOyjQtLlZfYYx7E6Bh1eDvp4jJA62NSOxD2bbP0IY63vXBtnx2mRRiRaKeOxLdYHquLTjRfTDRZSuvUsADFBfWQBSw7oTQzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سباستین ورون، اسطوره فوتبال آرژانتین: تیم ملی ایران خیلی متحول شده است/ فوتبال ایران ظرفیت پیشرفت زیادی دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/94184" target="_blank">📅 14:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94183">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f86cfb3e2d.mp4?token=iGpIdNH6aX0mF2wZ2pXpvEZ71iGub54P_DFQN9Y6WgFpF8eXeB4DtChUT_A3JBn40gCbm4tBimA3a9cJlXxDLr2rh485daotPrxfN1sdJDXA0VY7GkYftcA5Y2E0d0utDgs56dDsqHgzvey4R2-rozYZ5lDOKLwcuirqe9FTsgHAjUo0ePGbjvSr1XscF0Meuz0CshWkHuedpjTibzv4fkjOUhg-6r1AffqIeDwfsmK1GApjhH5EUBkpH6n13H6k4tGNjIZwTzh7JLR6sGN2WwCmKn_phuxPeZ_lmJDo-MeNQgleG3seokopYN4fnGRRc6QTDJhEBVYZdf9Siwyr6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f86cfb3e2d.mp4?token=iGpIdNH6aX0mF2wZ2pXpvEZ71iGub54P_DFQN9Y6WgFpF8eXeB4DtChUT_A3JBn40gCbm4tBimA3a9cJlXxDLr2rh485daotPrxfN1sdJDXA0VY7GkYftcA5Y2E0d0utDgs56dDsqHgzvey4R2-rozYZ5lDOKLwcuirqe9FTsgHAjUo0ePGbjvSr1XscF0Meuz0CshWkHuedpjTibzv4fkjOUhg-6r1AffqIeDwfsmK1GApjhH5EUBkpH6n13H6k4tGNjIZwTzh7JLR6sGN2WwCmKn_phuxPeZ_lmJDo-MeNQgleG3seokopYN4fnGRRc6QTDJhEBVYZdf9Siwyr6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
⚠️
پیروز‌قربانی: با تیم خودم فجرسپاسی از این تیم داغون نیوزیلند می‌بردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94183" target="_blank">📅 14:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94182">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtXBiJSo4BcB7O-B-unKMgbrDcnzdgo7i01JJoqbTpbKpi5hCWTlBZf-P2DIhg-Cip7Qq2QVPAwOESV0kWabjBE1AE5aKrFf4NgKyoecBnWYHcuoVAy2LRFKXRp0EmHhRVSJ_wtPd_7yhIHgYHeWgMSW9VGs2dd0QtQydJ0bH-3xfepVV0QYvWh8R5zJaeH2uldqtQlrXYxehJk7FhMC27qZDkE__iynlph-S_wLYb8YwrtNamgTy7RNlx-kBIBA4Zkop2i00Zcc7sH4hYnQeUvj8un673zoSCl7AK7B83BSCoaA8-4kSqgX5rndoX2xPThQdB2mwcTOOdCibeyj4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری نیکولو شیرا:
رئال مادرید آماده‌ست یک پیشنهاد بزرگ به چلسی برای جذب انزو فرناندز ارائه کنه. بازیکن موردنظر هم علاقه‌منده چلسی رو ترک کنه و به رئال مادرید بپیونده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/94182" target="_blank">📅 14:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94181">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQ2ETHyJ9cJzKS1u885inKwxRI5jpjvahtymfU6xi6Jbdcsa1PFEtWZlmZbMwjX338RNMhNXfSNTlFVTn9yhlVlaFvrKXFXpMLZNANMt6ZCqUAJxFQJCjbzRsn7PI3x_4j87JCpSsBSCCY913zU_q5Axd94_XY0s-61-SrEYeGLjdMyCVslXs95e-crHjvFdfrxAO7svSgbtzctLd0T_lvKmRIqp6lgYvHwPhuKnkXYxcTjWEwPHOWwaWX753qNDkKY1WJJgpsp5v1vNs1pjBhrD8-5HOspjehchi8p5_E2xnTLRV_HQD79zAx9f7wGapJJvLIHJZxTtzBoDKEMaWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇳🇴
📊
عملکرد ارلینگ‌هالند در کریر فوتبالی خودش بعد درخشش در اولین‌بازی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/94181" target="_blank">📅 14:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94180">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9087c58782.mp4?token=j8JW_zqVasM0anb_bhPYbmRmH8zKLsayOlk4_4Al08VXX5fVYn7vJaDUdRNqkQaaOJ9PIs6dnnBBHgfe3GvMO39QDVnTVE_EgxbJ-LeAZZ30oEib53BPhLHc-8xl8QgOlx3U_9tq_xWtoeEy5pzdALnquEFPQlqY77l9VJ-usjubSJUBIpCTjnhBNVs6GlgxT59bejzxcSOGZVw4ZJqpoihcX5XR9e9PLzDnZQh0e9v-wZba0goF0cxab005MJGz2P6_1FDl6yz9g8pu_VI1seZm6IIoSZbmeahQGt8SFAVyN3H57_b92aHz7v3pD5kG0z9wRoOhfDmwtU1VZ-4X7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9087c58782.mp4?token=j8JW_zqVasM0anb_bhPYbmRmH8zKLsayOlk4_4Al08VXX5fVYn7vJaDUdRNqkQaaOJ9PIs6dnnBBHgfe3GvMO39QDVnTVE_EgxbJ-LeAZZ30oEib53BPhLHc-8xl8QgOlx3U_9tq_xWtoeEy5pzdALnquEFPQlqY77l9VJ-usjubSJUBIpCTjnhBNVs6GlgxT59bejzxcSOGZVw4ZJqpoihcX5XR9e9PLzDnZQh0e9v-wZba0goF0cxab005MJGz2P6_1FDl6yz9g8pu_VI1seZm6IIoSZbmeahQGt8SFAVyN3H57_b92aHz7v3pD5kG0z9wRoOhfDmwtU1VZ-4X7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های زیبای دکتر انوشه: فوتبال و زندگی مثل هم هستن و شاید دلیلش همین باشه که ما اینقدر فوتبال رو دوست داریم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/94180" target="_blank">📅 14:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94179">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oayXOoN7gb6xAzWp2F_fC9dGntvcBgkxGC7dDLVdvzimlCVVgq7jtYUGvK0mHLpYhxgAwUizZUnwAZs1CBA3Z58epH6KLcSvDKaguQN1-GUlz5TSSohRlDcIrXTEDDFPKR-PCKkQp4Kw6GECQ54WovhzSyzsDzbsgfLGbQbhLhBzXURMuBXHKHryuo9nW-fTHgmZOB5aar6D0pA4w9MH6YCri0E_8e8KrEcOGkoNDVmXE3TLctUDAzPconp7WiU7wYeN7MRp7bm8ztFRr5AbqDqPKiS3SJpy82yGhDeFswTYMhxkfNiHi_75tNEI2BXbNg3jnjKvaazMj8kQ4ykATw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پستی که رونالدو تو اینستاگرام لایک کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/94179" target="_blank">📅 14:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94178">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39843c046d.mp4?token=dw0c9S9I0sxpCfejJLnm47_yBNKqt4bwgX5JqZseWuUs3rJixGvUGW4l8qlV2MJRtSei8SCNEeYw4vJrz9JAVUnRkGaMA4S1v8HIQuRmNstWuYJ06qhLe56dE20ASTY0kotjiMSVJjD2tgfLcuph7m444P1jj_fz6VwDYqMvYsL1bBrca0Z96kTY9fCglwI2lWpeAVM0uQbn6vHc4-_KpMn95EjNCrWHDQhRWdohPngLeisk-CrM4Gcf6Aq1iWA8zGw39eUZ2lSSDG84MdteHiCXiytvJAu3QtcyzEOAqqF47JnL8nDVHNnggCOfVjeIFGr-_nb_V-yJIC9tgysuQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39843c046d.mp4?token=dw0c9S9I0sxpCfejJLnm47_yBNKqt4bwgX5JqZseWuUs3rJixGvUGW4l8qlV2MJRtSei8SCNEeYw4vJrz9JAVUnRkGaMA4S1v8HIQuRmNstWuYJ06qhLe56dE20ASTY0kotjiMSVJjD2tgfLcuph7m444P1jj_fz6VwDYqMvYsL1bBrca0Z96kTY9fCglwI2lWpeAVM0uQbn6vHc4-_KpMn95EjNCrWHDQhRWdohPngLeisk-CrM4Gcf6Aq1iWA8zGw39eUZ2lSSDG84MdteHiCXiytvJAu3QtcyzEOAqqF47JnL8nDVHNnggCOfVjeIFGr-_nb_V-yJIC9tgysuQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇨🇻
خیابونای کیپ‌ورد بعد درخشش گلرشون جلو اسپانیا یه نقاشی غول‌پیکر ازش ساختن و فوق‌العاده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/94178" target="_blank">📅 14:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94177">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">امضای پزشکیان از نزدیک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94177" target="_blank">📅 13:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94176">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnfP0laITKTpVjDO_3Dve7OkJ3g4df20eXs3wklvQXDsThri7hByY9ZpKEk47oM-pQkW5UaOEvjTUfmtRWyXFntrgF3FIfPhzn1ebBn-E1StVDwr7-BcCO5RaI_7iCKc-DcttQUwDyAzcpEPPSyhLo42pGeF6uDoBQ9VpqhfB4KV6VaQ9fwL7tzVfL4NotNjzFmbknMs3g3_QENThGKamKJd_JsK9NjtRxzif6V6hPxrmsAQtsEfyx7HBxUyalSWLwJC86e08IA2H2kU91-gJ7ErAX7NAMTFuYQk-UBwspfeZwJK5GknD2bC69s5WutqZXG5Q5dh0JCE_trV6Q_-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
سه‌گانه ترسناک بایرن‌مونیخ:
🔺
‏اولیسه: پاس گل
➕
بهترین بازیکن زمین
🔺
‏هری کین: 2 گل
➕
بهترین بازیکن زمین
🔺
لوئیز دیاز: گل و پاس گل
➕
بهترین بازیکن زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/94176" target="_blank">📅 13:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94175">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6df6576c1.mp4?token=mFEIBvT06bGoFgqNs7Swpu3cUBKdZUZWxJ7VYIWFIA2MzuJcGJI1OF9zr4aXIl3Xvjir6fdqElZPrSBNQZPaxRXwd7lWkZVE07s5ul9n2it_Mmk7-b5AoXr7Yqc7bXNg8r74WuawiA0NjQ6IqdQRpktSg2qrH08rl28TuF9_1qcsbskug10N52vEHnq9LGgY2iYexOML-7eM_jx64l9Tdg03mhg94ARrjaxVXP4tjX1UntI57K9r82VU71mR3gitE-EbL_oZzxreW3G-xqTdm4r9ThiEyQgdQRjVRNT6x4yyDWKSxFfUINftPdnGd5CN1S2OhV9Kpo70g7HKynyrWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6df6576c1.mp4?token=mFEIBvT06bGoFgqNs7Swpu3cUBKdZUZWxJ7VYIWFIA2MzuJcGJI1OF9zr4aXIl3Xvjir6fdqElZPrSBNQZPaxRXwd7lWkZVE07s5ul9n2it_Mmk7-b5AoXr7Yqc7bXNg8r74WuawiA0NjQ6IqdQRpktSg2qrH08rl28TuF9_1qcsbskug10N52vEHnq9LGgY2iYexOML-7eM_jx64l9Tdg03mhg94ARrjaxVXP4tjX1UntI57K9r82VU71mR3gitE-EbL_oZzxreW3G-xqTdm4r9ThiEyQgdQRjVRNT6x4yyDWKSxFfUINftPdnGd5CN1S2OhV9Kpo70g7HKynyrWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سباستین ورون، اسطوره فوتبال آرژانتین: اگر مسی مصدوم شود، آرژانتین با چالش‌های زیادی برای ادامه جام جهانی مواجه می‌شود/ در ۲۰ سال گذشته مسی نماد آرژانتین بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/94175" target="_blank">📅 13:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94173">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33819b4cf6.mp4?token=My8eORNCwS4hBL0TmibUmTo82CATIfAbX-dv9Cjr_iC1QbMC-E3-vTmJtE-3xO5O4p0t0ejRBRLGtt3XbFc5WH6KcAyD9eru-BmkmHqph00BiaMGnF_Ah_aSLobYgB1qlk8NrGSM-OzKpkYTvfDl-aQvifrW69XbZHWPME-9VDhaI15n0OYyd5kQ8qbzyk3DQQY_E4SgFKfokLZfLrtIwB53G48hIw3LDbfWcOUc_ju4dEmETpD31fAd7Rp6UoTE1rArH7uxScHrlgF9QfvbRql9TDhSoWp6LCHBtH6Tvfmah0a0XKZeEm9Zra7m2YE86lNX_peC0G3ShmTkiWbmVol1sdWj8kuhIWvmBpdAN0yol_3z4V-1bJ7v7iUOq4x0idjjkDdJLCq66Mo24p1EIpxB-Yzurkwz18-17i4nyN0fLOCZ8Ptyo8Mh084yfK-fzxfSCl7m1do5Ey2-ZzrgvUHS1ob-WvTGvYzYy0HTAssCBWe09PKWrSIFVO4aUakFEVud5tOPwUDKl-vA__iCbrLp7dua87VJIg45C2UetvARIhT8PshCtBal-rF71uFMlVqqr6ikC-LfwN8BZUOsmYOnA8w5QCjZzZ6VzUUx85puGQOJXvrDjIMr8vTRg-IvAkRUZYZ-urPuOjthQGBFqhVp2tDme8AZ8n6DBEIS-Ak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33819b4cf6.mp4?token=My8eORNCwS4hBL0TmibUmTo82CATIfAbX-dv9Cjr_iC1QbMC-E3-vTmJtE-3xO5O4p0t0ejRBRLGtt3XbFc5WH6KcAyD9eru-BmkmHqph00BiaMGnF_Ah_aSLobYgB1qlk8NrGSM-OzKpkYTvfDl-aQvifrW69XbZHWPME-9VDhaI15n0OYyd5kQ8qbzyk3DQQY_E4SgFKfokLZfLrtIwB53G48hIw3LDbfWcOUc_ju4dEmETpD31fAd7Rp6UoTE1rArH7uxScHrlgF9QfvbRql9TDhSoWp6LCHBtH6Tvfmah0a0XKZeEm9Zra7m2YE86lNX_peC0G3ShmTkiWbmVol1sdWj8kuhIWvmBpdAN0yol_3z4V-1bJ7v7iUOq4x0idjjkDdJLCq66Mo24p1EIpxB-Yzurkwz18-17i4nyN0fLOCZ8Ptyo8Mh084yfK-fzxfSCl7m1do5Ey2-ZzrgvUHS1ob-WvTGvYzYy0HTAssCBWe09PKWrSIFVO4aUakFEVud5tOPwUDKl-vA__iCbrLp7dua87VJIg45C2UetvARIhT8PshCtBal-rF71uFMlVqqr6ikC-LfwN8BZUOsmYOnA8w5QCjZzZ6VzUUx85puGQOJXvrDjIMr8vTRg-IvAkRUZYZ-urPuOjthQGBFqhVp2tDme8AZ8n6DBEIS-Ak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
انتقادات تند پیروز قربانی به امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94173" target="_blank">📅 13:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94172">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX-VUAPysH_Wv-E4VrgBSj9IivQxFv-iIjmsRS_j-F8ofR57_uxxyW1w89OOyv99kL_we5Gp098Y3GC6RvwI5iEIqJbuu_cEZq8_zyPUoy3CrFfhVyzY37RiEHPIiivvJHIyAkywwuEuIFJelOJzp_3zd_6MN_bzqWj12HfrSHqu49lRUmDXtSCNBeaIOsql6a-nu6qyy-R6LYIDJeNYmNqz6v_8fgF_LACQjG1si-hZAfTI_MqmS87qucK4EcstV7TyIvZr6bPgwHOTbDW-5E1XYnMuWAvdfUmnH8srCZwrArd6-wv9ssNJ5olMLKkfKyYE_INyTDfMJjpaDE9ASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
خانواده لیونل‌مسی WC2022
🆚
WC 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/94172" target="_blank">📅 13:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94171">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb6168a2a.mp4?token=mmrdywWREGIWovblj1s9eQTR76tmuFJylE9R0MPwua302hGmfprAA3c1mWUWlBBsxJqxwa-4UFmwr4z_OO1LzkZGQqZDKBaMDUoUW7kv8e9I44TMh0PCI1u1MLOcI5ulCZbyCD_PgHLC4UL0Et0BHbVDBWSnlcb0jWAfPetunVFmmYFAtC5tQPPXlPnnTnCW5ZPrWygczl6VCkS8TujpS_rstpbuwMeYX655aseVAJ04Bq8_9ckp1jX_47JSb58qukJpR_UGsDAgIaS4nlcVasumszCfqRmNcCFhpgZ4yMhfLrnvZPZyBmhoedL_1Rh90rbRb3FrUqBoR4HTFtQuwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb6168a2a.mp4?token=mmrdywWREGIWovblj1s9eQTR76tmuFJylE9R0MPwua302hGmfprAA3c1mWUWlBBsxJqxwa-4UFmwr4z_OO1LzkZGQqZDKBaMDUoUW7kv8e9I44TMh0PCI1u1MLOcI5ulCZbyCD_PgHLC4UL0Et0BHbVDBWSnlcb0jWAfPetunVFmmYFAtC5tQPPXlPnnTnCW5ZPrWygczl6VCkS8TujpS_rstpbuwMeYX655aseVAJ04Bq8_9ckp1jX_47JSb58qukJpR_UGsDAgIaS4nlcVasumszCfqRmNcCFhpgZ4yMhfLrnvZPZyBmhoedL_1Rh90rbRb3FrUqBoR4HTFtQuwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇦🇷
🇵🇹
صحبت‌های محرم‌نویدکیا درباره تفاوت حضور لیونل‌مسی و‌ رونالدو در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94171" target="_blank">📅 13:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94170">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720508738.mp4?token=mUe5qOTki_PVLcEgokDunMNHAjE4mGv_XAws6Vium4qCaWrDSms21eI0XPk7nyVdPCBzm08Gbs-t46oCJjOkA6KvNvZX2RvGK5dftLFYWBbyGsJtMnqJqYZXNcj1Lq5E5_9z4Jkc53w9CEv-Zr_lc0pwWen-GFz5uH-LZ-IQuD263ok0Bhw5X2Nau-7CxnScCWV3LlVEKwz9vUgugShPLqeQ0oSutuFAnzAFbZ1s_cttA3jGOc2JocdBcZZPnwGajPa-pLeRvGXuKN5vrL1ALb5w6aqdfytVaFYMf5rpQdHvnN-HxBXk8JmntYqjgt_WF6MnTdvYYKNp14sm9EcKuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720508738.mp4?token=mUe5qOTki_PVLcEgokDunMNHAjE4mGv_XAws6Vium4qCaWrDSms21eI0XPk7nyVdPCBzm08Gbs-t46oCJjOkA6KvNvZX2RvGK5dftLFYWBbyGsJtMnqJqYZXNcj1Lq5E5_9z4Jkc53w9CEv-Zr_lc0pwWen-GFz5uH-LZ-IQuD263ok0Bhw5X2Nau-7CxnScCWV3LlVEKwz9vUgugShPLqeQ0oSutuFAnzAFbZ1s_cttA3jGOc2JocdBcZZPnwGajPa-pLeRvGXuKN5vrL1ALb5w6aqdfytVaFYMf5rpQdHvnN-HxBXk8JmntYqjgt_WF6MnTdvYYKNp14sm9EcKuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهار نظر جنجالی سباستین ورون, اسطوره فوتبال آرژانتین: مارادونا از لیونل مسی بازیکن بهتری بود/ او در زمانه‌ای فوتبال بازی می‌کرد که حتی زمین‌ها صاف نبودند ولی او رویایی بازی می‌کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/94170" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94169">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAjMnFsVtQhqYLC06alzJIprxdcRzb97gceSPm0jK2W_E_qgQWow3wPCgyC76kSfevhKaR2qGtLAQzGwCRwzaYzpEcu4c7JoX24vKMwS-3Q-0wCSG2RevH2uL0Pu8MFdqmRsvIvuP_9gx2W1WjtMkcIYvuRYNNwZp7cx9MHdW4ZpCZFKxBoe-NXgXIBBLxeOztqOnT_1mwUfZ2knUjTTZZvi0muhjzqbB36A2QCkbmH8sJaPhY8fKO08vtY4cYunI5nYa2FDYd5dVaMO_cj7L1ERSkii6ix0vrCaKRN7hY-bGYdQFDNXg8K9il-3kykahTODl-Cu_b9RStIHAGy6xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بیشترین پاس‌گل تا پایان هفته‌اول مرحله گروهی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/94169" target="_blank">📅 12:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94168">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8bc47b42.mp4?token=ifcB9PStvS0ERjq2t0_UTEtv2z-LfIgp8LdLejyHLixUYxN-4x9grlpnQkd-nqCiVKuCcoZOFsXefLhPiaJ8eWzhsLGHTUNq9gMwAuriPTnGyROhTW44MGJFBXoi0m7qXDapHSfy1zler_XZ6qHFyvgce4B6voKoxV-hORkRmjcL9d9ajKDpeJVmXNSyYMqwKfBE5oOyGc8HZYqyCk07eXUXxhZktC6AjulTemv0CmlLnd6ocNBCW9dnkQ1b3ZbopQcOICw6s1dO_ONx6JGqsxjndY4ywT_ImxOhRjUd0KeEbZ4UlgqeUZ4Oxc-c-1-ooDTyOHiE307FP6tyxZM9Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8bc47b42.mp4?token=ifcB9PStvS0ERjq2t0_UTEtv2z-LfIgp8LdLejyHLixUYxN-4x9grlpnQkd-nqCiVKuCcoZOFsXefLhPiaJ8eWzhsLGHTUNq9gMwAuriPTnGyROhTW44MGJFBXoi0m7qXDapHSfy1zler_XZ6qHFyvgce4B6voKoxV-hORkRmjcL9d9ajKDpeJVmXNSyYMqwKfBE5oOyGc8HZYqyCk07eXUXxhZktC6AjulTemv0CmlLnd6ocNBCW9dnkQ1b3ZbopQcOICw6s1dO_ONx6JGqsxjndY4ywT_ImxOhRjUd0KeEbZ4UlgqeUZ4Oxc-c-1-ooDTyOHiE307FP6tyxZM9Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراتر از سم
😂
؛
🤣
چالش بازخوانی نام بازیکنان تیم ملی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94168" target="_blank">📅 12:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94167">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb354f20c.mp4?token=KCNZugjec_dQ0NzGd9aiz13jAGk4u5Wj5D-l81INh_nBrQjprs5b78zzp2NIRfhiEO00nmNHXOiL5v-mHh_3vdr8Tux5-CNRWgjmCwTGpr0WEfx804YLc8d9BKCSLRwNGFa1oLr4t3VOGWxXVaIwdFqy9EQODVNLJ1owg8H8cRY-EF_ByVQNL5URt6DjOVbdmyfU188CY7-mudZ7tKpXXksexiDRUXXr8WyDbfMegXBXIHfL1dqcC8icBgGZgbgZKA67eRvbBrRjEz9JF4oN4mAayEmHOXRBRgqbhnZJKYAWAWA4KtmR0sEeBz-8o0kp0kWbZxieNm0bwKa8fRpeMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb354f20c.mp4?token=KCNZugjec_dQ0NzGd9aiz13jAGk4u5Wj5D-l81INh_nBrQjprs5b78zzp2NIRfhiEO00nmNHXOiL5v-mHh_3vdr8Tux5-CNRWgjmCwTGpr0WEfx804YLc8d9BKCSLRwNGFa1oLr4t3VOGWxXVaIwdFqy9EQODVNLJ1owg8H8cRY-EF_ByVQNL5URt6DjOVbdmyfU188CY7-mudZ7tKpXXksexiDRUXXr8WyDbfMegXBXIHfL1dqcC8icBgGZgbgZKA67eRvbBrRjEz9JF4oN4mAayEmHOXRBRgqbhnZJKYAWAWA4KtmR0sEeBz-8o0kp0kWbZxieNm0bwKa8fRpeMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهار نظر جنجالی سباستین ورون, اسطوره فوتبال آرژانتین: مارادونا از لیونل مسی بازیکن بهتری بود/ او در زمانه‌ای فوتبال بازی می‌کرد که حتی زمین‌ها صاف نبودند ولی او رویایی بازی می‌کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94167" target="_blank">📅 12:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94165">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWD8vJeG6hqRyyeIB8u2_YhjdRQiMGVAQGehLp4Y9WWi7Z70VhJoL3ar2iCbtM-MfKStS7aghjGcXxtN3xYfzslTe5jsxhWWcAWgLqZIpRxj70FcGhTgJMvLlqSsfz6gVV0bsYlaE3kMktl_gvtQLjLMgcI5_8jb-rox5OQHabKum96WPlDBFITvxdFpdQt6LVvcP7QjF683YBPel_YfKRT-VgdzOrAlGn8Ugu16yIsF9tp6tDv1qJHqTSSc6q9YD023SIxuxe0CFU_1YCRskIcZM-1VdfUciiUZCyaP5rvdgkue5mYRuyiJFVCpREauNo3wmUUgKM4VJsEvtTB69w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🤣
تو ورزشگاه‌های مکزیک یه پیرمرد فوت‌فتیش بجای تماشای بازی درحال عکس گرفتن از پاهای خانوما بوده که توسط تیم امنیتی و اخلاقی فیفا از حضور در مابقی مسابقات محروم شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/94165" target="_blank">📅 12:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94164">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFVcfWZCoprSfrjOdjwNENoVQ7_F-U8234m24-TikXsIBNo1K8HW8WAlZb7X0FG5nbk5Y46gd6o5WGygPTehiuvtoO-OyOdjHHCt-EiPKc2d15nKfFYabacInojVStg00AXR_VB9iJrK0KVaQcunwRYTB3gJOrkxA-9cK2ugh5eG4orlCeBUYMtdtTOJycgztxNrIKmkBohjjUcCJcTbbhcmtfH7zgwrd2lRagFkWFttFp7PU_6OTIcwHZVONIWCq6Z_VjLtTFrBfEK2QSW8xxcRZ0IcD29V4R1kV1643Sn5G33ZedFQEA3ImvEb48JwfNlIoGSs-dWUpEpDkoXDrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فوووووری و رسمی ابراهیما کوناته با قراردادی تا سال 2030 به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94164" target="_blank">📅 12:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94162">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biSiyZWTGxUKQaxw0hA9CXePd26lNhJWNyqbLjfuxZE7qhdXKZjnY6SRiQvax4-g3EHdBWN2c85JmFHXq5eRTQRBrvHLuNYkGvJzUDc4bHwyfL3FS4tLBTf_eGSD4Mn10Aep6LjlZ7oMWNPZKK7RURBBuncvGRPHJGi-fIkPLH_N-Yjw1EiL8DVVaJs5-DyRBgZrsRoW8QuAusynBYth9Efj_tUWItv2DYmFZxcORmP4HMZIn-LoeKrE-YBJiS7wQeC8f_ArMhMGrxgsU5kJYyvlFS3GWePqFPDdNpOPByIe1sYt7gtqQ-eaEZ6y3s6zPhha8_tb1TAF0pB85J28yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🎙
مارک کوکوریا:
رئال مادرید یه ابهت خاصی داره، واقعا سخته توضیحش بدی. هیچ‌وقت نمیدونی چی قراره اتفاق بیفته. خیلی کم پیش میاد کسی بتونه درک کنه چطور رئال درست وقتی همه فکر میکنن کارش تموم شده، برمیگرده و بازی رو میبره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94162" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94161">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5767fe2278.mp4?token=hl27Oe-c2uob3fkKhd4-TEvfBXVgM-G_tZU1N3E6J3jsEONRPkDQ0-ywy19lUPnYZPoPN3O3F2jNKQbh7e47Q2YMARKWqy_ZRrUHGXCw0pZm9zOtboFhmrncnRQPCGys-0iKb8BDFBhbHFK4xBJpA_vCIg460fu7lndHcDJci3FQ-jiRs26QQsCwFXU8uA8SQJUZj-xJJsP1mZGiam2uHXayS-bZu5W1w4HazSz12qxs4u5DVcXdSc1Hhft3TsWSgB_BIkj4X1rmDzt47JPsThnZ1wdfm_9ufjC8Mo2g38yUXpDVmDvvFHTmWA2EewOVj5txI4F1No49JISjpkp-tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5767fe2278.mp4?token=hl27Oe-c2uob3fkKhd4-TEvfBXVgM-G_tZU1N3E6J3jsEONRPkDQ0-ywy19lUPnYZPoPN3O3F2jNKQbh7e47Q2YMARKWqy_ZRrUHGXCw0pZm9zOtboFhmrncnRQPCGys-0iKb8BDFBhbHFK4xBJpA_vCIg460fu7lndHcDJci3FQ-jiRs26QQsCwFXU8uA8SQJUZj-xJJsP1mZGiam2uHXayS-bZu5W1w4HazSz12qxs4u5DVcXdSc1Hhft3TsWSgB_BIkj4X1rmDzt47JPsThnZ1wdfm_9ufjC8Mo2g38yUXpDVmDvvFHTmWA2EewOVj5txI4F1No49JISjpkp-tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🏆
🇬🇭
رسانه‌های خارجی با انتشار این ویدیو نوشتن که غنا دیشب به کمک سحر و جادو هواداراش تونسته دقیقه آخر پاناما رو ببره
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94161" target="_blank">📅 12:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94160">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5190506dcf.mp4?token=jSIdnZw8n0oIuBlrtyu7rUZ8w2wa2U0qREHMP7lFy-djEScxTQDb7UsiQl06wT_7yB8-8wsSPkn8YhKYh0DnAjlX1FO_wm_wxhMo9jxqsgEmv1V1iq420KAGQbLRBHdNk6UwQ688UAOYsu-7AIvtkw-XQLUYMogNW6KKJ4Ok0ZgcKBIFTDe7qdoEGRTpUaDflc9dVN7Po9f7D1pYN1G0xVbEQ9-yD0RP895h4N1VcHlEaVbI-paazS7H9tH8ghaNtMq1EdJHcPA_YZwiVNINyFBfTyO8HgVJTJFzjJp8CS_uWUOy8rcWONeB5cjXXKSCFKOIhsauSPvcmlfW5a0L5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5190506dcf.mp4?token=jSIdnZw8n0oIuBlrtyu7rUZ8w2wa2U0qREHMP7lFy-djEScxTQDb7UsiQl06wT_7yB8-8wsSPkn8YhKYh0DnAjlX1FO_wm_wxhMo9jxqsgEmv1V1iq420KAGQbLRBHdNk6UwQ688UAOYsu-7AIvtkw-XQLUYMogNW6KKJ4Ok0ZgcKBIFTDe7qdoEGRTpUaDflc9dVN7Po9f7D1pYN1G0xVbEQ9-yD0RP895h4N1VcHlEaVbI-paazS7H9tH8ghaNtMq1EdJHcPA_YZwiVNINyFBfTyO8HgVJTJFzjJp8CS_uWUOy8rcWONeB5cjXXKSCFKOIhsauSPvcmlfW5a0L5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔺
حمله نویدکیا به قلعه نویی: وقتی حسین‌نژاد رو دعوت نمیکنی حتما باید از لحاظ ذهنی به خودت سر بزنی
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94160" target="_blank">📅 12:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94159">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMSYvN43NX0lj5dDTvA3ebJDxhN9SlF0mDRjkEc5LLLO8k98FpICCMd-5daDd_pNMABlpmugyjQAHo8Gkg46wQGGsTvkhczxsqR6CMdVT-Gj_HtVCthiaaS-AYnixaDSPo-XDg0mA1g4sNm4AZEimbTU0dJtUlKmynMuRjsV57ZgJPam6WylllX3ebpW1-p1pv_LDsggNSdhoTRXivppRY7eHrbqtbwRvYC1Swj3fP2Nf5c_wwxy6W6HxaE8CxLxTvM652ww77Nm_Ct5y-t1oLKLoOwadVf18iy53kzOKPwmG_8erdBEfSqPevKLojZqqrThlw0sk1ugdgnTOPnipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جام جهانی ۲۰۲۶ در پایان هفته اول به میانگین ۳.۱۳ گل در هر بازی رسیده؛ آماری که از شروعی پرگل و جذاب در این تورنمنت خبر میده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94159" target="_blank">📅 12:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94158">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BGUI4q7QatIJwal3_ZXXUZXwXU3HX550MTJLKmG7fWfdJJkK9Zo-7TZS0tE7xedqOXd02Bz0_S7_x6i7K3Dy452dTA9hcjFiryOaE4OwL5_xbOodHqpatDRePPpvTpPlWAlRk6QDkJmV3AysHBFr51oA0_7hJ5MTikPdpR8t6tCFHVqblDoP2YnVP461-lHVRw3XJTJXY32vDNBT4uCVSaaX49C7OfE5QoaFsScp2TXdczI8uOFXUoXF-TKwmumXBjXAlK5PMU4kqkjG-1vaBDGkTrNy7GKKEDekNbhoknApbb1cdeJKcDHHbOdVVWsdgKaBl3tLVryznX1_l5xy-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نابغه خودتی پسر بقیه اداتو درمیارن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94158" target="_blank">📅 12:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94157">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOXBiy0SEsaIgtzshFRzlFCo--O0WY3H50BBXbjLqwNSr3xtjoCeSwHifTy8JOBoc3_hiP1k1VLr5p2YjMLJ0PBVTlor-5skKPk6EE4PMeoGsB6LkHZHV03AC6JSmJ-riJii8j52yLQN_t7I5e63ehSV_STsxUyvmfbn7KRPHooKzn3RZjsfVBKA7zeW7kTo00XVcajtdFjOslGBnH62l6SBTLRTgIeHfZ1_lIwzkts90MOTMHakbud4L_TfP-pW5PCPCDBTv0X2ZlpFh4hpurniypheg8ScIYGsFuy6xJEwn9-VxSnrqay0k7SfCK_Me__dRPoIwwM1ewx7WRSfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
رامین‌رضاییان در تیم‌منتخب هفته‌اول مرحله گروهی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94157" target="_blank">📅 12:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94156">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIWlbUR_lTSKmiYWLrfCTvSsSxdOFc3KzfQKA3NN6BmOv3FHrDg4VvrWJqnZCZ0q8gB1oB87ms1_yg6h1Lqf8iQpiuAOul1uDSWGyhXZA4I6F9b3hGhzPI61wwtg-Q8AP01aN1Gmwt50v7bnW9eySpjv_xeBHQNPMF1RnbuzdFF9FMc_ZX7wYPt65746zyAgX_JAqLfckUSMXP-Cwt0hnHhy6mcWjSVq7vvUZi_-cXWvFocYcor1npEpzSgJN7CjQkH_LZFXN9asM35rOsSOXeYKbZC665s3xsfEiNMO2Ld3CmYhlcqOaYPuwvjV-FpdXXCiAKy-n8VI-ItanEojAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود‌بلینگهام ستاره تیم‌ملی انگلیس بعد درخشش دیشب مقابل کرواسی با دوس‌دخترش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/94156" target="_blank">📅 12:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94155">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7db6ffd41.mp4?token=AlUKFOZkSTCqhS7dZ2Ur7yIUWQI-s27cL6bILx2rvGwE0twc1RlUlkQLzeA-NFcucy5BRwkffG3hmsj1ffj_brqjbbjRSveeh7IU4Y_Z44hzSm689XAwdsUHaIR5tQvGZsDmLQF15jPwDEe5xFEdlBCpWBpMgGyCr18OAALH-mce1UxzY0uq_RC11IANAMEvt-01ClkV6y5Y2myM-SaRusZnsEUZ10a7vNxDEtRHkFOgG-vNcTiT2xZh431NoB1sea5Z-yGx6YyinV5FeugEvl38NeT2x24huwvYYWJRxl3456LziAfVZnykh4RKCEsRwa7sqjnEnnIuWT965oVUyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7db6ffd41.mp4?token=AlUKFOZkSTCqhS7dZ2Ur7yIUWQI-s27cL6bILx2rvGwE0twc1RlUlkQLzeA-NFcucy5BRwkffG3hmsj1ffj_brqjbbjRSveeh7IU4Y_Z44hzSm689XAwdsUHaIR5tQvGZsDmLQF15jPwDEe5xFEdlBCpWBpMgGyCr18OAALH-mce1UxzY0uq_RC11IANAMEvt-01ClkV6y5Y2myM-SaRusZnsEUZ10a7vNxDEtRHkFOgG-vNcTiT2xZh431NoB1sea5Z-yGx6YyinV5FeugEvl38NeT2x24huwvYYWJRxl3456LziAfVZnykh4RKCEsRwa7sqjnEnnIuWT965oVUyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
بدل لوئیز سوارز یه جمله گفت که باید رو تمام درهای توالت‌عمومی و کوچه و خیابون بنویسیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94155" target="_blank">📅 12:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94154">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0I30MU1VeRWiPTKzoksVKjg-tPy_ew76MPnx2rfmFzdNkikm5cI4n0Wjn5oXDV4CrqiltmLUXBiubn3rBHqAcsRXMk8054x-0C6lrxEK4qOFz0v9e-igy2XjORwpzLM8LB75BgERGrIN5R_JwcKllRcaWgyIIUgKZOwz72BUh2oDFToA35PSzeijFcR91iyLaZXVNHaRtmkR1TlGW00wjISFUvGBDwWcTkNYInWe7hw-6ccdxTEYCGvkwL7itWuw-5eyMDOq4YQhqiqmT6LKyxLMR-R4U5dpWM5ZTxb6bcXeYM5Ltqr6KC2ADYyX7u80Gepl59wY0gVj9r-zcpmzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🏆
میزان حضور تماشاگران در ۲۴ بازی ابتدایی جام‌جهانی؛ تقریبا همه بازی‌ها ظرفیت استادیوم تکمیل شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94154" target="_blank">📅 11:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94153">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2491447567.mp4?token=EMQwPe9b3o2X_ccWYJ8omdqXJZO5oTlnZueB0TZbdR7vEt2ojHpdrrJRbbhWkAPZVDTUOJF9hdFaHMSTYTgzoIg42MdbuytQzoQBRuPU6ANRCBXitK-pmi0X3PqWnnAJAqz_zstgPeH9IrrLw4lvmL7bLGgmCjCKFpTbPoSpvPGeRqM3sBU7xDNkRf0li4alfDK-GRqKLOUDFiP6KdwUXlxvGmspeRPCY7TAIAwPclYgmerIQhjF-RUUoz48ob2_EvfGClQKEyjKpu8ChS50cBVS9V9BHHnqC0lsCZqelcRSEn0GwbwZT97fcAINn2v4URUszuV9Kxuhejau2nMbM0Pq0_v1Le5jeivAZYGaIPtsqGav7RsXnKDNQ7X7crHi4H4sHX58IwPVi7AWyu-cbNVNk-xUmT4udq8YB3EGtMl9JqUoF8PpGC-DUHhZTBvRDGF3H-LzkBz489TscnNCP9VerDTncsYhlnrelOymlNzbzxBPfiOlEaeUTNl-aP94JUzP_xdOItUm2K8BFxMLfmLMg-uUgzVtzO0M5ixFttPHzBoYdDwfyRkGD4uQEzddIP8Z7Dv6oPKYkLyLpA-beljGohLbOGy9K_j3u2Fl0vCj32xFRLq8LghfpPrXKg_3B5d6qVy2mIkDxTaYJQ4xTY3mFA628Ejf_-RVPBeh53Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2491447567.mp4?token=EMQwPe9b3o2X_ccWYJ8omdqXJZO5oTlnZueB0TZbdR7vEt2ojHpdrrJRbbhWkAPZVDTUOJF9hdFaHMSTYTgzoIg42MdbuytQzoQBRuPU6ANRCBXitK-pmi0X3PqWnnAJAqz_zstgPeH9IrrLw4lvmL7bLGgmCjCKFpTbPoSpvPGeRqM3sBU7xDNkRf0li4alfDK-GRqKLOUDFiP6KdwUXlxvGmspeRPCY7TAIAwPclYgmerIQhjF-RUUoz48ob2_EvfGClQKEyjKpu8ChS50cBVS9V9BHHnqC0lsCZqelcRSEn0GwbwZT97fcAINn2v4URUszuV9Kxuhejau2nMbM0Pq0_v1Le5jeivAZYGaIPtsqGav7RsXnKDNQ7X7crHi4H4sHX58IwPVi7AWyu-cbNVNk-xUmT4udq8YB3EGtMl9JqUoF8PpGC-DUHhZTBvRDGF3H-LzkBz489TscnNCP9VerDTncsYhlnrelOymlNzbzxBPfiOlEaeUTNl-aP94JUzP_xdOItUm2K8BFxMLfmLMg-uUgzVtzO0M5ixFttPHzBoYdDwfyRkGD4uQEzddIP8Z7Dv6oPKYkLyLpA-beljGohLbOGy9K_j3u2Fl0vCj32xFRLq8LghfpPrXKg_3B5d6qVy2mIkDxTaYJQ4xTY3mFA628Ejf_-RVPBeh53Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
💎
🏆
تعریف و تمجید فوق‌العاده محرم‌نویدکیا از قضاوت علیرضا فغانی در بازی فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/94153" target="_blank">📅 11:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94152">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H43xgeS7RZfCeFCDzjs47Yp_JD70uyiYmT_ebeKsaX3ptNTlGsCrflYZOsKszAeY8x5wRDexoPtvmntnzNY4bBsHVE6tDeo8QQpV3az3UowKFp4triIOBxMRvZjy1B3YudhDsepWZ-g6KjM6qvsZcUGJkrOkupMvvE6wGY1DKn49ft4yns3a5SOcpWinoYykMTBykfgP26eZlz6l7lmtbtJl3sS2w2G8H00maDztGlf5FHBWlTChAqLRQt4c1TJFzDW7VyX2eSaDwYq405j2UqnGu8TjQV-7ZusFlogAyE3_COxurC6GjlpW--bnZA7oVqJmQPuGAuaxFN2yRK1aaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
زرگر سرویس سپرده‌گذاری طلای ملّی‌گلده.
شما طلای خودتون رو برای یک دوره مشخص سپرده‌گذاری می‌کنین و در پایان دوره، سودتون رو هم از جنس طلا دریافت می‌کنین.
یعنی بدون اینکه طلایی بفروشی یا از داراییت خارج بشی، طلات می‌تونه برای خودش طلا بسازه.
✅
۱ ماهه: ۰.۵٪ افزایش وزن طلا
✅
۳ ماهه: ۱.۷۵٪ افزایش وزن طلا
✅
۶ ماهه: ۴.۵٪ افزایش وزن طلا
✅
۹ ماهه: ۷.۵٪ افزایش وزن طلا
✅
۱۲ ماهه: ۱۲٪ افزایش وزن طلا
طلا برای خیلی‌ها فقط یک داراییه.
برای کاربران زرگر، یک داراییِ در حال رشد.
🏆
و یادت نره؛ تا پایان خرداد هر هفته به قید قرعه یک شمش طلای ۵ گرمی هم به یکی از کاربران زرگر هدیه می‌دیم.
🔗
زرگر؛ به طلات وزن می‌ده.
🟢
ملّی‌گلد؛ پلتفرم امن خرید و فروش آنلاین طلا</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/94152" target="_blank">📅 11:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94150">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14ca557dd.mp4?token=Q7YyKO0KKCnnGGCFSjO50iUqTZdMwdxTAlQUw6LxGtpYWf999IaMd-PRfYBj80ZnYZbTU6uPYCslxHxNqV4_fufbVLgyw9glYeqGuRBrgDYRzu83ufHA3lzQbPkVztFPbx7WElyYJjp3MKbIycwo-Oa9DSwusx9mwKSYXMpuH3G1N7ALUdyj3lfrmVNFZc0s3uEWgSskvxuWTbAKKBU2JyeFekMgbE-_t_0Exsfw-al6Sb0vUiLRVyG5yZAzZFzkzZBGbtKtLQgS-0YMMECJTZY4SV9BkW1nb6-V1bo8BeQo3WXz1N3yFOxvep_NuoNdpAuaXIXjcwI0LPIN1Ht7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14ca557dd.mp4?token=Q7YyKO0KKCnnGGCFSjO50iUqTZdMwdxTAlQUw6LxGtpYWf999IaMd-PRfYBj80ZnYZbTU6uPYCslxHxNqV4_fufbVLgyw9glYeqGuRBrgDYRzu83ufHA3lzQbPkVztFPbx7WElyYJjp3MKbIycwo-Oa9DSwusx9mwKSYXMpuH3G1N7ALUdyj3lfrmVNFZc0s3uEWgSskvxuWTbAKKBU2JyeFekMgbE-_t_0Exsfw-al6Sb0vUiLRVyG5yZAzZFzkzZBGbtKtLQgS-0YMMECJTZY4SV9BkW1nb6-V1bo8BeQo3WXz1N3yFOxvep_NuoNdpAuaXIXjcwI0LPIN1Ht7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⁉️
تفاوت هواداران فوتبال اروپا و آمریکا از زبون زلاتان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94150" target="_blank">📅 11:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94149">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab0ef7f628.mp4?token=Hd1k4UwzUbtR1e9sQ61IrgBY6dLnqF4S4X8BlYFfMRaa_Gy7HcGnHK2IzPqu58JJVrdoUXdi9G7i34_TRG0j-3PUyRnFDIp3ZiKTVJeebM_Wy_mMxVthA3vClqrY33QLH0mkr3E_In9DXdO4NeXmeyKErjdm08BVZCrqXdWI4EwOenq3OMjMBBh3UzBJo_FQTH5QEHuV1tXf4VDjPhPl9bQ9tVZh0GMS2z2FxGcY3XvlS9Uz2m8sb7q5Mtw-sYg8pnqaRBO851vkWV_PjEp4ZZ6zY3StmolRXqDUrv7C2s843Ok7Jhpx7NHo-JARxox4NEU7V2w78Ub3AWgQKS3Bpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab0ef7f628.mp4?token=Hd1k4UwzUbtR1e9sQ61IrgBY6dLnqF4S4X8BlYFfMRaa_Gy7HcGnHK2IzPqu58JJVrdoUXdi9G7i34_TRG0j-3PUyRnFDIp3ZiKTVJeebM_Wy_mMxVthA3vClqrY33QLH0mkr3E_In9DXdO4NeXmeyKErjdm08BVZCrqXdWI4EwOenq3OMjMBBh3UzBJo_FQTH5QEHuV1tXf4VDjPhPl9bQ9tVZh0GMS2z2FxGcY3XvlS9Uz2m8sb7q5Mtw-sYg8pnqaRBO851vkWV_PjEp4ZZ6zY3StmolRXqDUrv7C2s843Ok7Jhpx7NHo-JARxox4NEU7V2w78Ub3AWgQKS3Bpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
دیس پیروز قربانی به میثاقی: با تتلو اون جای خالی رو پر میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94149" target="_blank">📅 11:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94144">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdW93GTRTpvnJKSKU3Wcsm-TTAzh-fJXd1hQASKoTluhUgtAnGTzNJP4h8__dnYk3Fxp_bWUcqRAixD30A95FEwkEZnRLMpaLZc1K4uEnhTh373dGINr8CpAJVAiQnaQ-QI4rlxx66IfUv-pODrWabVXRZpxpyQ69JROkVwASwPc4cZRHU2X4bAit-izejYDrwwGp-CNhQzjbaVDg4KlOD6T6iek7Ub2XfNi0t5sKNTs614loEcgGE5nXH3M8QJ0P3q-XytJTqNx52AbkEucT4T6AaexPkbNwhU5akFw35wQiFbXYLS8aqUZx6t7Y-NKLFWG8F5NslW6w1A_iQ-SXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/McWsFBNCCf-Z81ga3nAXii-iJKm29mALBsylJE_okfQ614ONKGhR4KkgZpYU92akzSX1U6lVB04FbWyBN9oWDrAS9tcnotUNvJfH9cKz2qHawCWUOTC4eP_lyM9dU8cu7Q0-vzgQPQFux7YFQhOCye3vyn2zCjnS33upEqobSubBRE9QLIoDFVm5jECxVp_8nBB3dwwVOQh8yS6fiKfYRqQxLDIWuBt5tbP10kj9aqpaC6q0dzVTQrRPZZnlVBeyswISOdb5WBnzR9pP3tn7u5ylKgauql7gz5X9Nbj76gQVR_XzfXS_cybI7bAjc5QWPsP_hJWMjQEj8BN8SPNylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kllsLHArOCtBUvANx9iw03bXHIGeRBr42YbZiHuzjfKPxTxPer8xfD7Dvaeu0V7ITOg5aEAeQxZCiAb9zAFzRRFlCHLbTh1ljq6L1u1CmYeH6pF3xpp1HS39blrEVHG8BwgaQOTvQJ3M5eWIq418qpC3qaWwwyaqBLygvu4NDMhEdCxdXYI3azjgVYxH-G_JiqLlUnG0cEbsO3f93PSrOI2S5ftsF0Cezn88rIO3A567L5_kDAq7sVfwSxkk5mgnlaL-_yyqJ7Z43NN9eAGGhTvODhc1Zysv4h3IhpY49x_Eh51-xQUmGsu9ijUHgb8feFUE46Y0BvdZevr6IUbmXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LbYmoIpkYC8_fQNs7NsQ-DyJ0MyYWSMgV-HAFQEltzFqElM9hlBO1FbjCVhLdbkoRFIzf5_Q1IdFl7I5sCaCQXyJ__HpzQrQTqpmblawVTlSWWZMvf8LSgLW6BG-NJf3GfRNs1WPoZIqJ-I_-cCt9Fc1YgzoAZ6A7aJKp1gJ7UxSGorrUUR-oDfnLsg-zKvihbl63tPGey82-KHzTq9UPhlArsPdoErVyUAgPQPgO-wmw32PhPWKARZFWzra_l6XliNcpziZbJ-pu7NjWXZHBsY7iWlVZISPqBdg4EePP-0ixYFxYbouQII1r6pbPu7ugJQtT0hNYK6DTI-7V9lFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGAskMmYLMqZjYJJhvUM_Vw-o90DajdqSt9O3vDyEWLNHfj0k8taPCtDaWrduDyICcZNg0yowPANIC4mZVMe6MLgrqkeFBRxpAAVLnZbCi_sQZQdEPz3SpKCHYMoQuZ6h7WP4v9RU-YpPMFJPJ65GfUs1wYqvLjmR3BJKDRWw0RgjurYLP8RZSXRtdUISAGl6UNMJ0S00v37rUP6HBjwq0fbJK_ImQRoul_gYB1cOuklsptnlKxpdc3xFkDx2Yax4sg5tmK_v4jziueUS4a_7X2536N-wdIsoEmsjnQRd3Rbx-KXlnrdLJYGS3Uw4L6JlLR_Tbmf-UNyWTF6GwTbRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای کلمبیا و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94144" target="_blank">📅 10:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94143">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQFO4aEDOfWIzYs2-xWbilAnjDo5Y6abWzAdlcKnJbnBov6PACKvUxWomQN9vOW-bUhrSqMM_3Z3vvF8BRUAbNTW4fBsHT4zq6T_mJQe_b_YG1J1nROQgcqMA_5ihu-gMGMvkMOW9itBcoumgFDoT47BIdt-5Lk262c9llyEujH77FOD6Fwp8ezd6dfJxgdj5bfN69LQP_p5QdkSd1oc2yXD3Xn9euPzKFbHAdorKJUDpAvJ2gyShy5rBOMQq9U6oAkAT6A11qg4RFTn82hJfxynQK9zBtLvYWfcyr3YRjB7pct-yLpJHSt7kP-T0PbaERG-HQP7Sy15heq3dmWFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
رفتن دیدن رنگ صورتی به بازیکنا اعتماد به نفس می‌ده و بابت خاص بودن رنگش، تلاش‌شون بیشتر می‌شه.(روانشناسی)
🔻
از طرفی هیچ تیمی صورتی نمی‌پوشه و این رنگ به دلیل تفاوت با رنگ لباس‌ها بیشتر تو چشمه. (اقتصادی)
🔺
اینجوری شد که امسال یه بخش زیادی از بازیکنای جام جهانی استوک صورتی شدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/94143" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94138">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RbODhOg-7YNJfvSi7usT_9PgMj_HLrgl3LZGUoBvXPIBX-5Ow6GF_zSI8my_sRho4xxurpLJixXsNJCFnsygQYLfLsDGaR42K95xMujQpTWQSk18HKaMqqpVStrRUFl4yaYK1ALsfFNVxllJAlW-Bqnw_QjTyYKiOl5t2m8wfsxpVIFa8YVCJRN2xcz5TzqFSaGa4BHUWUzFetAWGYmkmGhhHirZx-sKwClGs6xlU0oMNskMN0ufbIbAvLaNIXKRRGKMte-lolPfFrHimU7dAGZ098ywpo2kjoH89uAUbeMb6v0jDkbBKgVmR8o-aeNWcKzPHpb2LikfBwz5tctS3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdzTYFDcDxrS0yZuPvMwJw48OZ-b31BARkLNavXoHz6bU9Z1dWEUpaTDwp-2z4NnSReKhBxmLS-dcKeGxuTESyt9iTIMF5WjRebJJWhr4bCjdK4kb_GE3kajNwUeMOmAUVBex5LdkV_jH1hLe5LADplAkldjtDlcna3BefRhykqSr19iGzp9dASmODJroOPzLh-rrQEo7QJ5x3pvZYJVkb7jG7afWT1idzg0FtobUxTLYxT8Y5E-5noMB1l_RObHNbZrS5BQ5X194IVGBio2BGw3F80aV6BBrBYYPITmZdj97xI9gUrPE-Wx26V9n2fN0sRqQPdUfqSjYown6yq-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4rCxQWdDoql95bIjIHWojNDILbMhVniVNNbUF0idtplUqkQbDd72VJCoeVBtH-QCZg0T5F8J5Tb4Y3GjEhjbJVrLmJSH45S_9ASt8p5ZK6eQ_ocLgXl44h4942uOi8auA5XbGY-God3eA0_no6Gg-M6srO4-_19a9EpTTAG61y3oKVrsTicW6aoevz432zHUDnmHoz5vrpAl-OVFC-eaY2F6PFpI_bekXfzs6L3SuRHs3OPka9WkHc_NqZRcufqPVemW-l96fipYs4Jc3h6UvlgXe-OJTrv1JNfTE_FUq86LXUs8V_kZhx8Xmywczt5CiqDRD0horUjfIfZpISR6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rty5KDiVqbpfgkoQhCkwSG0xAouUM9LwXgCCnUMJXKECwyBCyZzCFz7x3i1aXcyzhdq-L-hDgKaV48odel-1lDtpfXT1fXUA6X49lQNz1F2EE3e5FQsyziCJdw86nUwz5rNJXrEX9zIwTHnSlWLrPBKyuDXnfhp7oCd88ZUH6BCuDRqdpTbEANvaARyTRyGmRwFE9iuhPa6gZo5yK4XkKCM9iiA-3qFbOj7HBOpmutoDXVyqFVf_SP4NxHGDdDqietCTI69YydNE-8yC1JKpby5XTXSmUaGJPg5TVSCrT2k56e86o38jsiGNA12jIy80ivQX3lbf8IPsSmzOkIHJGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
حق برزیل واقعا قهرمانی جام جهانیه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/94138" target="_blank">📅 10:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94137">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a99ba4fd6f.mp4?token=iIm5My_l_UO1ox-ueA3Mh5xI7RMBvjGgBiX_BhUkGOpQk4EDfGAGfucKVqd5xUE-uykAl58TJK5ceBshwnySwbOvgB4LJh38_3YrEBI3BZyV5JfJB6ZkcfB5Rnx_MvbE4Cz0p_AxvWeXWfqToHaeUS-BApYl-62ZONW0kEBid8TiDhlZw6RYqa9HuMHTRqy-Bbnb3RKpTbANOGfXfXfWP_6-2lwz3p-PtSeLMjqJK1ILUeK5Z0Lq5WPwBFzrTsfAduh0xklvIvM45eYWa9foneO8ZOZZkzrRuJ3z6VRLhaBTOhPQvUNtrpkufsgzd_m_m2pghjOmis8XUaCrOUKdhoStj7eBt9Z4EWJQdAynhGJMy3D_FnJu8ejKZ4TU3EFYcDGicl0QYcEtymIUBBTRpvt74_Q4LVDrs-SN7YSHeOBzUw4wPXoeSZkLVkg-tGnoD3t--J0mUy6rKGnf_71s32bBDPBc_GzvoGEk0UIsj5eLWmbJdQQFPU06dXBU5IS_4kPy-ga5jzg7TXUEyYM45zUkRTB_jHFQNkBjjKooDabdnMW1mFCduKKAZCpwYn_dYT5oVDK0in0HL34_QV9uFt5zcEqYbbrphqiiQxH9-asmOOSNwg71VfzCeDcERlA3XvYLJbvmYZocsCHpy4H7PpqBjhvOK1RDnvh4TYKZbcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a99ba4fd6f.mp4?token=iIm5My_l_UO1ox-ueA3Mh5xI7RMBvjGgBiX_BhUkGOpQk4EDfGAGfucKVqd5xUE-uykAl58TJK5ceBshwnySwbOvgB4LJh38_3YrEBI3BZyV5JfJB6ZkcfB5Rnx_MvbE4Cz0p_AxvWeXWfqToHaeUS-BApYl-62ZONW0kEBid8TiDhlZw6RYqa9HuMHTRqy-Bbnb3RKpTbANOGfXfXfWP_6-2lwz3p-PtSeLMjqJK1ILUeK5Z0Lq5WPwBFzrTsfAduh0xklvIvM45eYWa9foneO8ZOZZkzrRuJ3z6VRLhaBTOhPQvUNtrpkufsgzd_m_m2pghjOmis8XUaCrOUKdhoStj7eBt9Z4EWJQdAynhGJMy3D_FnJu8ejKZ4TU3EFYcDGicl0QYcEtymIUBBTRpvt74_Q4LVDrs-SN7YSHeOBzUw4wPXoeSZkLVkg-tGnoD3t--J0mUy6rKGnf_71s32bBDPBc_GzvoGEk0UIsj5eLWmbJdQQFPU06dXBU5IS_4kPy-ga5jzg7TXUEyYM45zUkRTB_jHFQNkBjjKooDabdnMW1mFCduKKAZCpwYn_dYT5oVDK0in0HL34_QV9uFt5zcEqYbbrphqiiQxH9-asmOOSNwg71VfzCeDcERlA3XvYLJbvmYZocsCHpy4H7PpqBjhvOK1RDnvh4TYKZbcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
💥
وایکینگ‌های دیوانه درحال دلبری تو جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/94137" target="_blank">📅 09:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94136">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1df67b89f.mp4?token=e6XxkyHPg-HJtuOcYSP_Ov3ACf6XgQgVdbFuJ5_YjrHnju0FgA875ktuIPdyHy_vi2i9uNu5hMHo8bzGDMuojgb4G50ThMD0z2qd-1VXm9Xo-DZc52NNiSRmH8v2nLXtmKiv9S98sAn4najP_Ly5wVJy96dKYyjW11drzvYRankX-K-wsLdHFwr2Vp8t5bs7cLN6RgDFrOj4w1atrO0HcrLd6ctnT10cGXJytbiRquoItQInrTH5rtAVZb5AW1fDaL3lah6slr9_DxMgqzzbihsUscbjCM8iliqcLlxx8iS7m_t_uqnH3CX3yUblHAdx2K5cAyffR-B_gDnesJKnfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1df67b89f.mp4?token=e6XxkyHPg-HJtuOcYSP_Ov3ACf6XgQgVdbFuJ5_YjrHnju0FgA875ktuIPdyHy_vi2i9uNu5hMHo8bzGDMuojgb4G50ThMD0z2qd-1VXm9Xo-DZc52NNiSRmH8v2nLXtmKiv9S98sAn4najP_Ly5wVJy96dKYyjW11drzvYRankX-K-wsLdHFwr2Vp8t5bs7cLN6RgDFrOj4w1atrO0HcrLd6ctnT10cGXJytbiRquoItQInrTH5rtAVZb5AW1fDaL3lah6slr9_DxMgqzzbihsUscbjCM8iliqcLlxx8iS7m_t_uqnH3CX3yUblHAdx2K5cAyffR-B_gDnesJKnfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
دیشب وسط برنامه زنده عادل فردوسی‌پور پاش گرفت و اینجوری داشت بگا میرفت هرچند طبیعی جلوه داد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/94136" target="_blank">📅 09:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94135">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d434481e09.mp4?token=rTgvIFURhDAFict3Ki8fvdEu3T4AvmfyKfTGfzvL9dOm_ACybunWeBzn8l3JCBkn1p3AQPezWsLeuHYzmeLp_r_xDRFb_BhwXS_24hhfz29k9yf8Fia5l9aaXC7oHgzb1GlrTH-Df4UdnWk3yUtLr93Z5FksAEegLVvbiDYwKJujZgjIzc6EMPQAVIXJjF8F0CjrQ39j44-UaaxgDt2M8CONkf7dC8laeuQ6dJXhY0PCv8kjupO79M58AjLohOrJp1cLhky7ozF4gm3Sz9l5lDcOIpJqiGddADXPGPz8t7OykDau4wOEtKxWUye5nFdmiQNNRJlCsuVscTV1GWO7Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d434481e09.mp4?token=rTgvIFURhDAFict3Ki8fvdEu3T4AvmfyKfTGfzvL9dOm_ACybunWeBzn8l3JCBkn1p3AQPezWsLeuHYzmeLp_r_xDRFb_BhwXS_24hhfz29k9yf8Fia5l9aaXC7oHgzb1GlrTH-Df4UdnWk3yUtLr93Z5FksAEegLVvbiDYwKJujZgjIzc6EMPQAVIXJjF8F0CjrQ39j44-UaaxgDt2M8CONkf7dC8laeuQ6dJXhY0PCv8kjupO79M58AjLohOrJp1cLhky7ozF4gm3Sz9l5lDcOIpJqiGddADXPGPz8t7OykDau4wOEtKxWUye5nFdmiQNNRJlCsuVscTV1GWO7Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
👀
منتخب ایران باید این‌شکلی باشه تازه مورد قبول مردم قرار میگیره :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/94135" target="_blank">📅 09:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94134">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yqm-i0zhD9As2ej8o6tUNEFhQAFzfbuQ_dvExN0yQPJdZLtPFMkYY0IbTQFwnHZXGSGWLO6lAqljRS2y3UlpDGZnGnJw_LZwiAWSsOGr0sGRPrKxjO0H3Oc6n2y7G_NWngpIHZ5iGa4-NQnN1fEeaDT1WEht3sVyXPBTxf-0Em454P09YTC5X20tAoW_TNG5Q8Cg0KVD_R6jA49zk3dwCDlBcrx7-iAxeKbscEcJ48xMywtc9VGnCDHaIFjCEHaKD96Qgg_MNrh8QQ1a14Dg5FmHUBnTl4La9P0iLXGHkYqZjDaQOzEdQUcuUyokAHNDmm5Zzwo8dKygAA-67CTWWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
نتایج دور اول جام جهانی:
‏
🔥
۲۴ بازی
⚽️
۷۵ گل
⚽️
یک هت‌تریک
⚽️
۷ دبل
⚽️
۳ گل به خودی
🟥
۳ کارت قرمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/94134" target="_blank">📅 08:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94133">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICMJ3M178jS4-myrbKLqxTC4EPusqrPL0XWyglrFDzuE0VPiGTD2ZuwSa5k40q9vyK_KByNbKF7tDqYvA-u64v-g-cDbFDSiHpQJCnEnVUIgr2CBFwUIUkC87wlUc31jCcsA77CRVpBr4WcXAUEma4Fpp4IZGPPDyyWUa0CmA5V90_bddHVgyV3GdEudmR3v8ilfpNfClS6rm_hG-DMYuClOTpTTi0bZAgoCiDbuYmN7f-FzYmWWfzSoO1m9sk0kO6dvSXrfEJPCfVIi5y6fdu5Gd3tgdWI7FBhu76QelyoMt9Bu2-Okzu0V6W_49Xb1NYQkPi6e5RxP9Nm87l7wcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
🇩🇪
مثلث خط‌حمله بایرن‌مونیخ تو دور اول مرحله گروهی بهترین بازیکن زمین شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/94133" target="_blank">📅 08:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94132">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIeNbZtyCwwGKrxC28HWeal1SXPpu7kUkgCWfMTOn4s18XelHhF5Bfn4GqQ6TrGvmwjgohXlvcIqayqjbfr8uPHcRl_cbR9OOjyFqvykHZHH1XBbvfuSs61ThkD5wbcmOxyneI-d2G3LJuCrj2-b2oOFVRU6phKkVX18hB_1HTbPTUzpcRQHO_GMDDL08bUxyLfEU-5hbtmtaFVWN9vFcTfJghdfKc1daSvlXSpkfdU8NhDXnWuqtQg5pW40xpa20qPIC3ZQEdkA0NjlcfW0w-IHT8YGdoBD6WNi2gGfAlZXDO9qL7R-Sex0XMh6MdUNvRmCnhz-N8W8oYBeQN0_rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
رده‌بندی بهترین‌گلزنان هفته‌اول‌ مرحله‌ گروهی‌ جام‌جهانی با صدرنشینی مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/94132" target="_blank">📅 07:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94131">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Goo-cURipwU3aTGzA_1St9NXdYf0CJ-qBzNlBNfgn3WViaGDMzqPXR5u5gq8TvuaVbG_HhSiwWsP9GL3u9FEVGk4HTogFeY-aYeOwn4h0XvEf25idKsPI2xjt0l_t_WOq_0qccSn3M_NYMqKVEVtiQkLG17wZ_MJ47MqyLQJH6Hy50OMISPMfLQYB9kX9Zh47XZaQ39Gaw1Va99szgHeT4jIQ8vwcwRR1JlC_8ypw1z9dCs6DvLJrmvZt2NBFuYqP_I9OFX0IgjwK91aLfqNcjuQE6KWkj8WdzQcjbD0eHJMgHOhp0DKIOVG4ou7SVYXNpyrSKzETAE05FxATVSaUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
رده‌بندی برترین تیم‌های سوم جام‌جهانی تا پایان هفته‌اول؛ هشت تیم از دوازده تیم سوم مرحله گروهی، به مرحله حذفی صعود خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/94131" target="_blank">📅 07:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94130">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roPdL2z8fwNE9i_3fFeQEZDamouu1LxswQhyo38bTbWNNYuToEJnmbZVQt8waJzPaLoB5qlARg3SYFinikZindl8DdebxL0zQ41pZOQcZN6KaJhY1xsawcEWtyWfc_qIh7H-fwoAVEEVPnTv-Mnp8lLwiF2qzU5AExFUAgWkuvHNMGMi3g_0gHI-L75PQAwYvNNwyIL0giQvR1wBePlkmWg60qagDHS-tWdopxOMKc0a2CsBIbfErhNb2SKgyGHe2pDDHZIoRPRxw9ImKIi3xnjYdBvXTJG3khd_7PmUJFqVo5z7oi3tyRnxwI4XFswMkD7IZff87iCSj5bK-7LU5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
جدول‌نهایی ۱۲ گروه‌ جام‌جهانی پس از پایان هفته‌اول مرحله‌گروهی مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/94130" target="_blank">📅 07:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94129">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RABoHWqLllrCLE766AgxnOI4F7jjGDykp2O6iB_fV1n_LL-4JFjqFhChaf6oG8pm12jIA8oxLzD8SU0N5RsvzNd3YitYmVCgbBZ0NULy9-XZsZhIuHblX0AeNRFlshYShBFVH-gJsN7Z-Y8h02ZrZLgvKpOf3tJmb3xozz8FvxiFSXWm1zvySVASPZ9aZhm_2GGQSwfWtHFPUyMTDgqYUReYXyhuZ-CXGpd1bhG-6Fa0-9Ux7V_XtxuGJDSTdZRwfNDAJuenJChyPpv2BnUOPaYxCOancLah4mpXZQRhDDgqAa9kpVwLqrb6osmLTX5PzdH4TQA-1mX4yi3dhF0GnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
لوئیز دیاز بهترین بازیکن دیدار کلمبیا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/94129" target="_blank">📅 07:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94128">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEmhXadcxHxLXRiodio1NXBL8IGq6imclcXvu409w17U_XxdyqcQzlI6tzH38aUsazVeRu7TnRGet0Fmad8CYrzP7klCVz_R6uPILNN5fSpBfcOa6lcWRFQOCfVerQf8-UFlarTRhkolZrDRi1f0Ivj19hP3mcKAzLcCiuISN58cA-u6ITMRZxjXGospYPWxKTfyapWIcVCUElxe63ULjMuMAGQ_7HRL-RbiY4V1p8YHrsrKn3I8YOw3b6Q7VQ5noLVVDjQ35gxR2RJIPXSQQewwDw-tTFqCpuvDz0vsSBdvc8vXDcDEfIINS6oPVO44K89ZXi76DyO38_3qp_mJCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
جدول گروه K جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/94128" target="_blank">📅 07:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94127">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی رسما به پایان رسید و بازی‌ها در هفته‌دوم از امشب آغاز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94127" target="_blank">📅 07:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94126">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🏆
پایان‌بازی|کلمبیا
😆
😃
ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94126" target="_blank">📅 07:28 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
