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
<img src="https://cdn4.telesco.pe/file/iPWQWdF9gImhvKyPevOeSYFxGjGXXb8G2mt_6z_dmyFC7IMMvvMn1qNI9PZjSgFQtCiv51QvB5T_lLVM21t65zCVIdqan2xapyWaMUqnnOVtSkPZx4p1Owt5x1XCN98EIb2rsZY-x2XwTjpttgWT-ozqJsJQtI_YWFiWAwMMZR4Q7jNgezdlpeo7XbrjcXSyRfQMVQ9aLOr801a8eUR-DhG90hYBRjtph643B84UVHJGG_BlkSSo7ahjLQ3W9wtXBOhmitCdwIBrDgy3pJW_m_IVTwqoNnrGqimLPLhAei9h4gqzZxKHgI4nCi4QFw0jKdtfGThsBTaNRloS7QRJhw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 07:34:31</div>
<hr>

<div class="tg-post" id="msg-457153">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دریای مازندران تا شنبه تعطیل شد
🔹
مدیریت بحران استان مازندران با پیش‌بینی وزش‌باد و مواج شدن دریا، شنا و تمامی فعالیت‌های تفریحی، صیادی و قایقرانی را از عصر پنج‌شنبه امروز تا صبح شنبه ۳۱ مردادماه ممنوع اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 492 · <a href="https://t.me/farsna/457153" target="_blank">📅 07:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457147">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tWe5RPVQdL9Gsek9mC7Er8_xS0NKiPPifXQahsfcJ4pXyUqniJNsyc8bVGJ_8pq89jHNZaIJEft929SeLUf_epn6Mp2l6CoCOBVf3qENYKlmVKxbJi_Zel8UE_9ZU0UMHaarf2tKAF4Kn7gMB5wV8yaF5xMCMXtIOr4-IAXZBBHpFH1e3pKC58eowCn90WpeT43RbebQzMgJ1u3o5tnxJCLuxGwpQ0jLxx8jeTzIgGww9DmWa3hwR-7bRsjsoyfO1jeZQgAGiMOync1Yn--7lI4YgozqiyI8grsKH1awFCcSDt-INFKzoGzr6v4quThAXJDruz-fedPrL9a8DhIulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZRjGHliU3NFuhJdS5-fEfLezMqGbv-7R32a8mulBRbpfsZwmc-oR612Rf2j1d9KvALvZs9lqWLsi_bqQPHd643RrFO6EWLCsIRedvWa6YT_k7m1my2jDb8uxvdvyOrloT6yl21e4Lhga8Cve9_Xw2oymyK0HlE9OlH3CVEAWpklSRvMk-X7SLouBwdZwUPYQPWPYzdTK1G82qCA1mWUjvEOGDBoqOm48dIL7ko9HlWSspGrUHpSjIFJhbTJxmM9k2SHCMFLZ-cRjOMLyOfIL4pzTbc4HuzrFXECy8ciy1HePu-6Hyz_0qpqyGGJg4SZ-S7Bg9QODKoqmlzrXns47A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_gpDsLEhwAl6-vyrCOjYWg7boZkTLqpfbGa5ZpcQ3xheeySc5G37NBrQyYjcRoVeu9vVALYwkjwfruBPfl5Is_sUxgcsnEGRrohPKIg-bbhwVXgfFBVgmM8SRHZ2bUeCuTdK56o1QWxmKvsGfBOjKbPCidCGIiZbb4z0Ny5fwfixI9o2ulJghfE8BvNaDbvGIh-1gXSlGbdWB7yFswemkbOv4CWt7pwJFoW67i4Ski_6yLiE4W-f3zuDoPaK50572jrsMW9uYGF8YtJvSLvM-i2_22nYThkjFzwIlkdnbFNUO2TP9i1M7VmdXWeY8wWuWhGcLg4OokFK_nQrlFxkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X2-x5_kUWqqlV631sruH_KxIdcdNwqZP18ZBUKWZMUUjktkbxk27FRdPOTOj8lvHbqkV4houUG5QvaCkzeRtACMZMg5GTOjzaIZtIHCf-Sp8s-SYSmKNehN1hozNXHhaNaYrWggt2tnEU7EWhHGshjMflr-mMDqw2tf8XwTp07_GTwW4BkmRX0Xywc_PY8tVNzBXN025Nlfz4jNO-D5u-HLPJrhshmJJMUMt95uljQn9OXSURFp-ANj2fxo1FLj4FMQkPNEjQgXAoeD8y0iuwX9iml3TjMm1OQz5Y5YDyQbedFB906YPCBPKBUz6fxN2nBDrEM3Vk1KqPn7jO5BWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3SxvzhTGJZ_dlO8J3ZOVro0J8-IPpT7E5ED1BgFKw7PMQmJKu6ff2_O153AFd9EGQSat57gHr8G2rO9ZfqsVY7b8fc7n3MTJPt0t9mZqNDfAk--qLhiCg7N36DjfMxSv6PA4KUhqyz3TsaoxSEGizyt4kikyeXHtpbBU_U8UkCcqV5QvXRPkW_S0fhqyr43i3eEsdft_ZpfaoDUWB5KEN8WiO6xIsk-yTl6fBX99lvbK_Y6Mi81X121xwGdWcVYSUGv3xUQCiCwD8zsm6Y9rRCG_0ppzKe_ASZzpeKDHxJ19pCWwbiD5ZM4m6ZJTZKcpg_KQ1cgT_bzIdtMbkyAHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbXnH0Oc0WYrMpun-OfGC413ga6LeXIvMTqHadWWFRwtPk0M7nq3o4YDsVQW4gOLGuQNPC9vMwefGJo1imWPhR18HNDtrlU8QYVpcNWxDTcQcQOV48LILxuoLO45uv_rzNUhbrAjNvohNOr08UUEwLtvWxSsWiBGojkrYNM9_iygxiXxq2G2_u-2nGeq7GnRDUdY_9Z6QiD0PZfutYuPaX6TnOpxsGolTpeq0GWouvqH1zsY1A1eOoy_g2nhM5aEuElM7L8fmATlGB0UYIUE8jaH_CSy0sAifAuD9XKG8VQnko5OfCRtyBcH-ycYNzEMUnDdzzgKLG7b9cPdAsXXsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای بازار سنتی تجریش
عکاس:
فاطمه جاوید
@Farsna</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/farsna/457147" target="_blank">📅 05:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457146">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/035dc36b79.mp4?token=Ctkq3TYukVMpgJjdv1ozOynrH51RwN9bgz8PC_0HllnM3XGE212v3whw-dIQknzYtV1AxiDl9ASihKLHfBmBS-VIyS7C9EhQl2D1HB-cmB38EY-GGDI3mOT-wLbkd_66xKDa8ghiluTEXBADccQRSaEga9qqtxo6hRko4UlcqixBNLLikHrp6OcQZjI_X5KjnDk_bvukSlWMi5k197MqbxrPqN05Ps7GZUQwOqWVs4bIeMEkkyI3HV0_nBiGcKsc2_biXa8SIrrV15R6a3UNnQj4TtCDZgWtQWZHf7jMHq8BfNPJ1MdophpZCyJP04GybXcTvtZLYP7n7zKGMr4lQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/035dc36b79.mp4?token=Ctkq3TYukVMpgJjdv1ozOynrH51RwN9bgz8PC_0HllnM3XGE212v3whw-dIQknzYtV1AxiDl9ASihKLHfBmBS-VIyS7C9EhQl2D1HB-cmB38EY-GGDI3mOT-wLbkd_66xKDa8ghiluTEXBADccQRSaEga9qqtxo6hRko4UlcqixBNLLikHrp6OcQZjI_X5KjnDk_bvukSlWMi5k197MqbxrPqN05Ps7GZUQwOqWVs4bIeMEkkyI3HV0_nBiGcKsc2_biXa8SIrrV15R6a3UNnQj4TtCDZgWtQWZHf7jMHq8BfNPJ1MdophpZCyJP04GybXcTvtZLYP7n7zKGMr4lQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرالمومنین(ع): روزی شما ضمانت شده و شما مأمور عمل به احکام هستید
🔹
مبادا خواستن چیزی که ضمانت شده برایتان برتر از عملی باشد که انجام آن بر شما واجب است!
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/farsna/457146" target="_blank">📅 05:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457144">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65aef8733d.mp4?token=gYao5GPbDaUuqDdFvSztG51DObcZessBZBk6PxsmeZ5I9TsxF1dEbFd_aGSKDPCfguiYPgDAwTh7x0C_kR3CZoT1h2k58b0q0U_03Za-nPh8aZkksXHXW4s-pxBpaKhOun4fimgqFVxSmaS2AWvXweTNXH29_ila_Jhhvi5YQheTPnaMLSYJkkt4Bu-SKw_aPZ2GqWTygfXNn1HXKkQ_0A7mTyBdG_mRWCoqiUJdDG9VM7eU1_yDP5WB7fR3t2YlyzAay2XotIy3JSq-Nv9thswSudspBt3hYun46huFRvJmu3XEru-AGET6nyeEjkc2BmRcJx11LoX21cjaP-Gs7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65aef8733d.mp4?token=gYao5GPbDaUuqDdFvSztG51DObcZessBZBk6PxsmeZ5I9TsxF1dEbFd_aGSKDPCfguiYPgDAwTh7x0C_kR3CZoT1h2k58b0q0U_03Za-nPh8aZkksXHXW4s-pxBpaKhOun4fimgqFVxSmaS2AWvXweTNXH29_ila_Jhhvi5YQheTPnaMLSYJkkt4Bu-SKw_aPZ2GqWTygfXNn1HXKkQ_0A7mTyBdG_mRWCoqiUJdDG9VM7eU1_yDP5WB7fR3t2YlyzAay2XotIy3JSq-Nv9thswSudspBt3hYun46huFRvJmu3XEru-AGET6nyeEjkc2BmRcJx11LoX21cjaP-Gs7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موشک چینی بعد از پرتاب دوباره روی زمین نشست
🔹
چین با موفقیت مرحلۀ اول موشک قابل‌استفاده مجدد «ژوچو-۳» را پس از پرتاب روی زمین فرود آورد؛ دستاوردی که می‌تواند رقابت این کشور با فناوری موشک‌های قابل‌بازیابی و کاهش هزینه‌های پرتاب‌های فضایی را وارد مرحله تازه‌ای کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/457144" target="_blank">📅 04:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457143">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSTQt232J1zHGuOh6bQaJiel1RU6j8CP36fHG9_exulHFI6d1T9dk0cF5Dks9TN5HJfRgXeQg0pJD7xIlOj4Uh6IRyhTexuWTifHQ12YxBjo6Yqis6c7B7vQ-6hscdbbCaJnXHuDYWlHxqk6R9-USzQ4Zts-t_z555IFMOE_LlFFF8rp_6MBq2tzWyEA3NDNR3ihQJgji-1_m10ac09jX-PDKmjg-IImQd-ey_eyHFAwCwoyf-lzyaEFRZOWe0yH2sHv9nswlULTewK0LP-7fA-OTlvnyNURJOMvPBGywDTO2IlWKrqcyoaJI3vrblfTZFeTYIVNAvapVw_2rt4Psw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراض نمایشی انگلیس به شروع پروژۀ جدید شهرک‌سازی صهیونیست‌ها
🔹
وزارت خارجۀ انگلیس از احضار کاردار سفارت رژیم صهیونیستی در لندن خبر داد.
🔹
این وزارتخانه در بیانیه‌ای مدعی شد ما کاردار سفارت اسرائیل را برای اعتراض به مناقصۀ پروژۀ شهرک‌سازی ای۱ در کرانۀ باختری احضار کردیم و از او خواستیم که اصرار کند کابینۀ نتانیاهو فوراً پروژۀ شهرک‌سازی ای۱ را لغو کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/457143" target="_blank">📅 04:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457140">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/062190fde9.mp4?token=vN4TIFr1W1hSfw5ZIHau7z0IpgaIsZn-IaCkqX58uqarttgxT5gv8v1jOAvXDOjGlj2sE1HuAY7vLnFIoghl42dlazRG1x91erziNo4oE89e_LAX87NBo2HcFHK01Pi3HgtkuSgeApic2PhR11goDBoR-WXgC_htvRJUiSWFsczlpJmJja1EwHVsozqEGA1eYWbYN7ILL6P7kQw2AHjs3CV406PA8qVeTyjM6_CeLq9LNy_ki5S5Z5SAsmLtM56RwcO5JI04pPTOI9z3v9vO4LRlRWLOIrqcXV9asfWdbU3xYmX8fXDeWBpww0P2CYMfQVLfMlOCUP4_1EM5WBgmjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/062190fde9.mp4?token=vN4TIFr1W1hSfw5ZIHau7z0IpgaIsZn-IaCkqX58uqarttgxT5gv8v1jOAvXDOjGlj2sE1HuAY7vLnFIoghl42dlazRG1x91erziNo4oE89e_LAX87NBo2HcFHK01Pi3HgtkuSgeApic2PhR11goDBoR-WXgC_htvRJUiSWFsczlpJmJja1EwHVsozqEGA1eYWbYN7ILL6P7kQw2AHjs3CV406PA8qVeTyjM6_CeLq9LNy_ki5S5Z5SAsmLtM56RwcO5JI04pPTOI9z3v9vO4LRlRWLOIrqcXV9asfWdbU3xYmX8fXDeWBpww0P2CYMfQVLfMlOCUP4_1EM5WBgmjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجاوزات متعدد صهیونیست‌ها به جنوب لبنان
🔹
شبکۀ «المیادین» بامداد پنجشنبه گزارش داد که جنگنده‌ها و توپخانۀ رژیم صهیونیستی مناطق «کفررمان»، «تلة الدبشة» و ارتفاعات «علی الطاهر» را هدف قرار دادند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/457140" target="_blank">📅 03:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457139">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534dbabd1d.mp4?token=GGQpxo2bko2uyjc63O7ukMM595ELud0bfUFkhlisfsItYBGSrkzEkkUXIosoYts42lxxGIRhGL3etRiWp3BDKa-OhVjseyvHfaRC5mlJi7GfGd8DzyfaLpQa6DbhE3IKnV7ilTNZFSHnO6vBxnhS1hcZjv98C6P7LgTqi6wL5qEGv8Uy7IRbyPPU-f1LxBSY3s4npaB-8K5jnZ2mEAVT30Djti6IejTqPxBuHqIFO3tyVs3N0e7CVt65RuABpLv7VPODS_BF9PQErmHwotmDKtC0dc0-QWG9LvQoAJ5lrdRyEHP1dVONjgBF8w-ehqaiQFj04cCdij53AG-wbHGyv2VOd_wkf0cViCzTQsVtC8W3K_BzRvfw-VT0IKCLY0wSQDF4gTjKEFQw2fslguhmHqtmGM3BDQr80maHsgMRLSPmhyD-LHCMcbDxMtPxKqK9Qf-119vR1m1pSt9qHn6wQwRsiGX_XXTK1-IAt505tq5x_IV1M9OcSpDeMtdhes8wue0PQtBvqHDH9gnknU0xHL6_dzOtdvoYRebFSjTbd6e2JGZ8Gd4qrAmV-dcl2gSQ97WAtvJ4KgQV6uFbtt-ZtfW7Hg5C-aEN1pIuHE24BzM-XImWZcmqUZToHrYrfnmQs-TahUGI2uwMr2sBuX8QffCTNPS6Yhst7M7J7mX9iGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534dbabd1d.mp4?token=GGQpxo2bko2uyjc63O7ukMM595ELud0bfUFkhlisfsItYBGSrkzEkkUXIosoYts42lxxGIRhGL3etRiWp3BDKa-OhVjseyvHfaRC5mlJi7GfGd8DzyfaLpQa6DbhE3IKnV7ilTNZFSHnO6vBxnhS1hcZjv98C6P7LgTqi6wL5qEGv8Uy7IRbyPPU-f1LxBSY3s4npaB-8K5jnZ2mEAVT30Djti6IejTqPxBuHqIFO3tyVs3N0e7CVt65RuABpLv7VPODS_BF9PQErmHwotmDKtC0dc0-QWG9LvQoAJ5lrdRyEHP1dVONjgBF8w-ehqaiQFj04cCdij53AG-wbHGyv2VOd_wkf0cViCzTQsVtC8W3K_BzRvfw-VT0IKCLY0wSQDF4gTjKEFQw2fslguhmHqtmGM3BDQr80maHsgMRLSPmhyD-LHCMcbDxMtPxKqK9Qf-119vR1m1pSt9qHn6wQwRsiGX_XXTK1-IAt505tq5x_IV1M9OcSpDeMtdhes8wue0PQtBvqHDH9gnknU0xHL6_dzOtdvoYRebFSjTbd6e2JGZ8Gd4qrAmV-dcl2gSQ97WAtvJ4KgQV6uFbtt-ZtfW7Hg5C-aEN1pIuHE24BzM-XImWZcmqUZToHrYrfnmQs-TahUGI2uwMr2sBuX8QffCTNPS6Yhst7M7J7mX9iGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
الیوم یوم الانتقام
◾️
مداحی محمدرضا بذری در مراسم چهلم تدفین آقای شهید ایران در حرم حضرت معصومه(س)</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/457139" target="_blank">📅 03:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457138">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU32m3JlPq64oNiHd5j0IvNg0n1cjrk1xyDpbC8n9u--RnvzwfsFUD9_yhN3xSQ60o4fIyP4UziymUe82Yq278kQan5xPP9BokQ0HYKerWu_Swa8QUE9Nm8WtAyjIgg9OKyCGmGULX4TlvLuwjJdZ9zKokGEzxxCqLp3gzCN4nUg4Qsfy1Cf2onLHV50pl3iHTuS-4S1EgY2f0Sc0KreBnzknXc9AXJ8mkpCcrz-h6qCOGeYD8bEOeMF7v5nWdlnT4vEssK7qSS7QvLfCYmwEPO3yynBVnPFYpzCUA9SxQ12BtXnXu7Ixyuf6miGAJbrjVIFT016fSva3Wb5TaXL1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعاهای تکراری رئیس‌جمهور متوهم آمریکا؛ ترامپ مدعی آغاز جنگ اقتصادی علیه ایران شد
🔹
رئیس‌جمهور آمریکا ادعا کرد واشنگتن «خردکننده‌ترین عملیات اقتصادی تاریخ» را علیه ایران آغاز کرده است.
🔹
ترامپ با تکرار ادعاهای همیشگی خود، مدعی شد نیروی دریایی و هوایی ایران «نابود شده»، صنایع نظامی به «ویرانه» تبدیل شده و کشور در آستانۀ فروپاشی قرار دارد.
🔸
این ادعاها درحالی مطرح می‌شود که ترامپ پیش‌تر نیز بارها از «فروپاشی قریب‌الوقوع» ایران و وارد کردن «ضربه‌های تاریخی» سخن گفته بود؛ ادعاهایی که تکرار مداوم آنها، بیش از آنکه نشانۀ یک دستاورد جدید باشد، به تکرار همان جنگ روانی و تبلیغاتی علیه ایران شباهت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/457138" target="_blank">📅 02:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457137">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfpkAq3LPaqtpeLExMGpNPWqqCmWb6yxyCQhY_Nd-hnWvXPd-uK9mdy3mI0V-wQqbWQc5CJZOfWpzAk8Q0NikYotW3Ydr-WSS00esCtKdAyosw2uqLt6rAWZjghoQbhWOX48qmmXka1Dhe1Jytho6JZAAjNLVacEXEPR2ObD14a8XIKHpyRxJihl_07z1KQJ0zVJeK0DLfm9hgIVzRANP7lO698uYuN23ZtK_4DKIE1btekHnFH5q6LG-RkiV9Q1TulaHNpm55KLZR9NQEsLDc3gh2kjrQY1DI4LPLDlZMLmwUMilnh_33uvKgFZbeWlunpDsui4R9sQtpwgc-HymQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک فالکون ۹ اسپیس‌ایکس پس از ماه‌ها سرگردانی در فضا، امروز به سطح ماه برخورد می‌کند.</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/457137" target="_blank">📅 02:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457136">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQeZD2cg73u6e1ZT0NBGwIubP4w2MyZ4OXY-Nw9hs3NLSVyMj3KP6Aka8NEqS_oYHinukYss37XhkcHaEyXtm6xvimYLtU1t7sy5-rtpL0Z7JQnitWRgFRtJ9JtrotxTF4vzEFKTp28W54Po8m_GCSNicDvN9HZK_DnJhDcJ3koHwLgoBLn3SAV9Uq9rak7hCQMSxBIEpiV0wkKfpZG6OR8kKD9y6XjfmvpfZADLlTnSvtWt4XzX_g-5q1P-pQaRjUIppg59hHwLcarbagzaq7NNdF8SBDkogV-_89odwcaQZS0qixbodyW6qFNQ-Gd_6LXwo-FgDCZLdyUtHsaTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه غول زیرآبی حمل‌کنندۀ سلاح‌ هسته‌ای آزمایش می‌کند
🔹
روسیه آزمایش‌های دریایی نخستین زیردریایی هسته‌ای «خاباروفسک» را آغاز کرده است. اما اهمیت اصلی خاباروفسک به محموله‌ای برمی‌گردد که برای حمل آن طراحی شده است: شش سامانۀ پوزیدون.
🔹
پوزیدون یک وسیلۀ نقلیۀ زیرآبی بدون‌سرنشین و مجهز به پیشران هسته‌ای است که روسیه آن را برای حمل کلاهک هسته‌ای در بردهای بسیار طولانی توسعه داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/457136" target="_blank">📅 01:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457135">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cefc2913b.mp4?token=Qdd03q9AiRJwh72hNPFVvfrUW3rdUntpMks2pfACUxrSbcero9sOCKLiL1C4eH-IlLHHkGtuH6AiwmAwAHe4J0V7oElv6EI44NdB1gFh0xXgISQJTOAsDFNVrz8iJLzXpf3bQNd5fgglqWGwswfI3ofe9L8JLNjti_uKlhf_IhCOCgYshFlc592vDxHcNzmpGq81KILhWgciSaxDSZVdP_ZaWnhaIhy_K6tsbHBn_me4KXpqpzbzMsV4X5SJtv06EjP-SMAzNoCF2A1cnWAcUhU2xiQfDQHMLd22Dd1TdQPeI1XEVz34LBgglvKVpmb3PM0ZO7cExIKzNkTXZxt6CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cefc2913b.mp4?token=Qdd03q9AiRJwh72hNPFVvfrUW3rdUntpMks2pfACUxrSbcero9sOCKLiL1C4eH-IlLHHkGtuH6AiwmAwAHe4J0V7oElv6EI44NdB1gFh0xXgISQJTOAsDFNVrz8iJLzXpf3bQNd5fgglqWGwswfI3ofe9L8JLNjti_uKlhf_IhCOCgYshFlc592vDxHcNzmpGq81KILhWgciSaxDSZVdP_ZaWnhaIhy_K6tsbHBn_me4KXpqpzbzMsV4X5SJtv06EjP-SMAzNoCF2A1cnWAcUhU2xiQfDQHMLd22Dd1TdQPeI1XEVz34LBgglvKVpmb3PM0ZO7cExIKzNkTXZxt6CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر تازه منتشرشده از توله‌های «هلیا» یوزپلنگ آسیایی، که آن‌ها را در سلامت و آرامش نشان می‌دهد   @Farsna - Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/457135" target="_blank">📅 01:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457134">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRqahySUDoZngEwrCOMoyjyQqb4f8XfCH-JBD1XQErDR2g1DSz10kQluHzK0nlgJYmooPhIBkbv-Xsv9bmqHE2iAE89YHwWK6t-lBgx-lTcK56xlEXQXZBCqAgzpUulm0eeVfKHuxJOMb8aCOF-Mt0kQvD7jMKNRJw9wTVMLy9ScPtNmvJAlK4ImqmlHvMQTOw6QjzdELtXqS7lC6Y6b8TqaT9_PjxB7wPvjRSVx3fS3k229KIhY5ThgCEwJ-gvl5wIUbKoIpLcLZHt582NoiES9rg1U0_jT3_7dHeZEzbsnBT9cvZIcMj4jqDdiDKhy0jlEcLJrPX2wjjBDk_noxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ: هنوز می‌توانیم ایران را تحریم کنیم
🔹
رئیس‌جمهور تروریست آمریکا مدعی شد ما چیزهایی داریم که می‌توانیم علیه ایران تحریم کنیم.
🔹
وی با تکرار توهمات مضحک خود ادعا کرد هم‌اکنون تنگۀ هرمز باز است و قایق‌های زیادی از آن عبور می‌کنند. البته ممکن است این ترددها در مقطعی آهسته شود.
🔹
رئیس‌جمهور کودک‌کش آمریکا همچنین دربارۀ افزایش بهای جهانی نفت و قیمت سوخت در ایالات متحده ادعا کرد: خطوط لولۀ زیادی برای انتقال نفت و گاز در حال ساخت است. من فکر می‌کنم تنگۀ هرمز به اندازۀ گذشته مهم نخواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/457134" target="_blank">📅 01:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457133">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حملات موشکی روسیه به پایتخت اوکراین
🔹
رسانه‌های اوکراینی از وقوع چندین انفجار مهیب در پایتخت این کشور گزارش دادند.
🔹
شهردار کی‌یف با تایید این خبر اعلام کرد که پایتخت اوکراین هدف حملۀ موشکی بالستیک روسیه قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/457133" target="_blank">📅 00:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457129">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMe2CGZ6I6LVsJg9BtnnFavNDNLMcPpQBS7YrGPrhWJ-T13dFx2ktn-ZuYlrnZZdJHVhq6vNprZ0kQabG-PPgWSEO1XnF86DjElrAikqMfHjTXq4tf-ChMb2wuwXmFTI-6-VMUa1vnk-Wp8tqumrgdiwsyId5aemmwFmI988U9HIGLV_0Li5F8HTakxpvldZTIV_SwhrWGdX__avmesY9j7nG7zvI7bY7tpIo4WdO-UQeMb2fGFC66SvvxWXXn-PU34aSRK3dWip2wqDnsiPBsNV8Mh-oLuSywFZ4hbTu1xXgJlo6wJbHGRQ1eOOPrj21DMvQPgKCHrkABdASNP5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s8NayPsirXxwag6PJbuusmRZuW7VMxMDqmxGEizHDsdBSf3vND8-dBdEwtIOdDD98iEbTCOKoX7Cs_22Vg3Txn-cc1vpSWnN-GNoRzPZ2By29N9VCOu6KH3bFzzV899OyYEZWG8IbycfcWi-1loR0x_PZWxTVZcJT_LaHn_1jui2ph4Pab2JPnnplKW6BwoMOv3Fbc_zOarlxsDQ1qbvfc_SwxL2VsM7c09zKZNF6RrL6PNosNwwWdCxDQe_2HMyHzXEdBL4E5jj9YOFDQ8h73Ria2m_BWJyefS4Xxn7FHcIw6ws6LVRFPvr3XyMTnDty5-Ff_XCpBxjaXWh0nN5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btlYpJM3_QY3kDjSV_yaWBGXHgjcVNBOhn2sQrI3zhJpm5Kw7fzcygFJNmC2_m2bD9NSjBFbABKl0zGbsLs2LSq6yYcfJ_7MSSyk_I1E0I1JjuLzicazjQVoCZtWB2uVJ0ZoDWpYPh16vlsxyj8aUrgKeP2PtLmdrCCzmH-2i7dUClGBrAJmsIgfR9WN7GMufmKP7d_YbPSojg4bA3zxm0xNFpeG6lMyPxHCmhhl8qr9_n3uu1eAJDKr9Bb0i4ky6KthhydPU4Z_BX-nDLHhKtBogXocX4qsLuySTVv9HAjLtYWhAoMIYpxqIZfpdhrhuFUem1rWp0IRDHQgoxt7Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZcmJkhZ3p7S6OVZWJN3kIZpGI6vOFzMY595jUjIW9y5SQGClm45PzZIQwgqgK-foipSU69P0m5Y2s3dkqvuhB2c0BkBHh-i99GePomWf66qSZgDq_a-AB2TNpxTkdQOKzZB3HsgV2YlKrSuAWnaQw_aqsCAEgzfs1-syUY6jE-upHx2VcoG7-7iOs7oJq-jXWhPHXBQ1MverG4udK8S3sgacqD6t24IxBiI9HdvzD-DdatGnZcX2dsBQRoghrok4k1OfESEFq8uKfC9XwIMaLZAVvAQsMtWLvyEt9dGOSVNjIJxl_jt6hByhnEWNyNr7HidPxogwDTCSHK8hjiMnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۲۹ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/457129" target="_blank">📅 00:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457119">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsy2M61tAK2kTtkd1kVEmwyIihG_6rwcMbLu-VfmSGFEgXCrX_nk5qT28GQKOq3Yvzk915mGT0IOTOSmrlsZL3iG2APtmryEAS3o0-536LpSp5h64LZ1EXDZEnNd3EbHPDpjjPwnXnFRN7Ii2VJUTypPriLoff3JHmg15GOvuxgGUQyajiQyTZCDVpD5OOXoBDN-aIojCRfC8XNZ25_mVK0RJPCrtLEkNsHmUxOYcPik9pB40ABWsUicHzKz1fOdf3jZvfSef1vGNPkSVR59WggLns-T3erWpVElq6YXSyog-YXeZbj3Z4yJGkXPBRsTmViQgMTjbKzu5kWMq5Wg4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZzpKgiiYmTUQ5NcZrh0ydpB0nwTBODX2eJ0oBHt0ISnmHl7TXbCtP1q9GTdSy4iyyoEgpcSAtFBDqGuMu3WI89SoanweCeqSaKRm-aB2oiQ3wKiblmkilO6wVAgY7T30yHku9fGtLJutAGC9UyjVEh3pkIlWjnZs5s79TclSXOJ-C8CNPRleOAgdoGn9Z-zMBgX_SbvKE3TXgsbOeKpuAGvZ2pOLqG4nzd5LsBcG6HMv8URZDd4X5LX_M6A1Pi_33YDgenqf0rY1H0C7eIjXFvHSwJGM84yo9wx-P60VCjAbbeTz2TYOt6xopVodIqBdslj_YaWrGNxdVX_E3jdzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fvOrsCvxBQf6-w7wXFKjhthPSHtijHRLjpsIkPo-jAlrJQR6XOB022Txaqoi3k7-k65chUOMZcA99BzQdDcbHBXSEju78jpqTSfS594A61bNlZBXmzDMm_uQ5RcStSqSsUeOdYOLhWZrx4q9QHMfG_H5Bpl5k43Cq8cXjxxdfeEiHumbwNHYr-5Nmvmx0azVQA-DqmJLaYCfsPqE_Ihr2jm8YfdK5TK408efxyBtLruP3r-JiJDT2e4hDZo0nmHfnjksSw9JDPMpPFW3c6GHlBkrZpGKQYLNYY1tsTzK9STW0UUXf1-CkIIQjblSBVA_ovfBZoJTWzoc3Tkh7oqc3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VR3ZdrODYlvE5zzb8X7W-srRN_dySAcrFf-ENP3xbAgBuIONQk1hL9w1NC460kgyUvkHTDUaUthYoPExAcxFEQqis7vxtLiPqU6mYaQgsxFVxca0BTPLRccSbKIAIbwB-KNRCqn0x9kIKdIBfrzNoHpCqL_ef-o4YqwHqh0f9CRjSU_jK4b6Bad6RjXdDa6H03Lw7oGEh5njSAjp69QcFv930YiUbbHqC3h4Hiy2eab564Zj-8a5sAuyWeCa8NdCOfY5pkVcwAB5Ffsr5ivSZiqIogt34UoVvWzX8Y5glM8jS0uuuNpY5e1EPf567WKd01IJFy2ETezS8Qmz9LPT3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pCprFdTq20ZnCwSQVmlRDNXuhs2V9yBW_cLj3JLCF_FLdA0SpcCke7x_ljvhDPJRSVeohrxuYVstAJ4Dzn4_0tvdlJtj4DzTBc0NO2mvktYAC3bE2_kvT4ech77qrWup6OLNbizGBJpOXm5oWNPJNn6J7NbT-uUW-oO3a5T5wzYfiEGqyWshnY6poZDi1tuxzhyaodiJkHPVfoJWDrEoHjihTzMVogTd4GKIKOWq-Z1rQWCNh__N2Kw9iTtk8mgIJJNfAs_b2KAqYX9dpozKEaNjgbW-O0ZFwYa-_OetIW7KvvdK4wHQKqRCpVyouiFANa7WGsdSNdiDjzgeriO5Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLGc4w_3mk9iPrR1WQN9OpKP775dMmPzd-wQb2Nz2NScDzSW3YkxFef8XF2rwUu9ul4aMaaFSuKtBrXUzdUS72NN_BpN85EOEeASYKAefGAlUlkh5WnxUTxkfha2LjBOt_l5YTKOTsizCA8gsuIl6kVkMPePgZp2oyI7Bi5KvBa5PokUWE1mb-ax6FiIzg_bMDQq9ykBTfsw6oE3kIS95HdUakmw-bkVj8k464ak6tqQSqBhlsTsJFWXf47xGI-m3pb6ODqrqn3mK3K9SXYiCDWHyP_ArfxusBnYw0RMGbW5GTPTDxKLEOtc9zuePvt5lTwS_pDwoqmBzR8kzfD_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKlHGvl_iZCTZjjmL6iHrEMINEy-4DzmPc2ELG0G4juX0oCiD1EwQ_3Gd9II09M-X2Mlg8Ce3qYGuMKO3RXE5vXJOEIy4oM3S24ngpdK0WtTbOurczlohabOIY9m-f8QciPhe11NCa5FjuoWHxGXuvO-XZOPUc7f-ACG-vPOtqMCnGN5Jpq5S1FiwBdnPXyTLqdZ_-mSnjGtPlEitvdSK03FhRmpqyCaDJxfSZjbHunt43_vPxilRASLG37CI8YE39J8U8e5IZFZ1vVEyeh0Ic5O-rupWF7fyqyX2-bId16lTHWSiiaNNkAUNO7pAAd4MjRoOMYV89mnkuRRKSFoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oV5Lwupi7bqtSdr-NNNcw1Qqgv9FIDJsoSnyFG1kG5BcbVCOEtOPtmVj1voTbhMGbZnvtVgqqngM4KPiQ-Q1Ak8gP1sCrtnqyiGleQ-BMXK4MwuiTBy9DKBLS6Dz1PCOp86taaOR-p3CeRepyAZ5FyJ6HHhIkv1BTMXA_aTiZgU1Jh53YmFWc_GKA57ksiD4U1uLvZb07XdJKp9rqxG8Jlud66qO_b0FS1Kc8czVYqJdIvSHToO23Okw31TT2vUCyBqPn2IQq1G5GrCWVfvhioLg7484rNGAer_CMueWctaz91Zicf86MDL6s7mLIlSWyPfzt5SNH_g5phJPwKA1wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vMRWJ15QdYr1-abl0fBL9Bo_3xl4lU92xfmK-FQSIl4DOh9mYQlYc9bw96Hq13XMuIY-k6TWuwo03jRc8rT9-9UQ_zCrP7BUZLFlktAB71OSh6YdW6W1B2Pr43KbmxbjWf597gHEL-ETQF5N7V4zj_PBHL67h_uJHlRFuAT0e1Wo5CcMkJCWWcKLIhzXyhQ9FpVwI-qxDBAc87sslutihzwKmKBIr056dfZtQK1YQGQmapbN2f9999frj5kTlNdaljuemWJO7G5gZ62toyoLsrt-D4D1xLgio2qkiNT4AD8Wo7Cm5HZccL31c160mqeuTWfWUYZki1-JvY0HcILR6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdxgpJVkNEPjgOK3FgfjQQlTojHlv68ehMpxdZ9NJG3mrBN636zt1OqoRtEcIW4tSDGPZnFQ1O3uqn3d_Bn6Dx0GS-DbTBOqyfvlsgWDW831zpGTLLUWzadkLzHYMaUD_1koYwwmix4hJOYWkQ1IBrl4wzaCv8AW8gMBY9yAZv6JL1UUwxZTZmekznkWwSnYWrS8sHtpzGKh6Dd8h7qdeemwq2_Y2Zs24oyUDRK4w6sWcyDsA6leldr3dPxBYrx0JzRXb18XZAlKVl7aAFIcmRVyeL9ZLT2kvmzb9uKqP5x6aVXwynfVIyvQVP_ynnM3Z3A_mBpciWv2SlcxMqN3Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/457119" target="_blank">📅 00:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457118">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPJQtmuHyEWdrqzeC-PaPcTNZ7F6sV46vaK1IT60_nV_gcvLvQBq28UwJDCJN-RC6aGbGpXSSWUa_qkFR7ho4uXhEw0__FZL_iZJv-P5shOiTeT8zeuoL4V88x0anYMRizlFpgfdgLV0CD0ubqzvzwyPLIPtTOCskMVExD-OvAtGaw-SG86ftXKvQ-irXz0z2_sbZTTMawDP3nwf5WZvKxlQ3uxgvcQJsb7rK8ACOuj9pZtCUtUKhHa8cx-X-DESyHFPz6LJJ2SzT-qDH2g-uBDZH85tGPKl1-wIm6MI4YS56rSFq-ANOG1IXYo0RATVkRXdG3GX5DTXHt6Y0R854w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام اینفلوئنسر اجیر می‌کند!
🔹
مرکز پژوهشTTP در گزارش جدید خود نوشت: متا صاحب اینستاگرام، برای مقابله با موج ممنوعیت شبکه‌های اجتماعی برای افراد زیر ۱۶ سال، به اینفلوئنسرها پول می‌دهد تا از حضور نوجوانان در پلتفرم‌هایش و ابزارهای ایمنی حساب‌های نوجوانان دفاع کنند.
🔹
این مرکز در مطلبی عنوان کرد که متا در کشورها، از آسیا و خاورمیانه گرفته تا اروپا، به بازیگران، روان‌شناسان و اینفلوئنسرهای حوزۀ فرزندپروری پول پرداخته تا در برابر ممنوعیت‌های فراگیر حساب کاربری نوجوانان موضع بگیرند.
🔸
این کارزار از زمانی شتاب گرفت که استرالیا نخستین قانون ممنوعیت شبکه‌های اجتماعی برای زیر ۱۶ سال را در جهان تصویب کرد؛ اقدامی که دسترسی متا به یکی از سودآورترین گروه‌های سنی کاربران را تهدید می‌کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/457118" target="_blank">📅 00:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457111">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vjeFr5wjdMpqcsR6RHmyJ6JV109Y--C9jqngJCnqefH5vkbkR_-h9GuEA9brWSOsNf58s2TsaO0rgsuYWWL4xVRhUOpdc8qaFIRAEabIvsemuX2ztRfdPYOxbKAgnpLwG8Ygig7l7w8qAZG1VV5BLxiaLSuH1YdeUFDKfI0mqiMe-AFjO2FDeN5ZDclfBaeBDQD6u2_P006662uiY7nI1Tau2O1MiCTDOQOrKCbO2mLFTf_BjkZldueptu9OiysDcwSGhTujMpNOfeBARSomFd9L98TOMLzMDCiJ5FwdYHHvEdypSC0uDHELj424FkUNsAiiqAwmRoCRLTnxgBEygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnwGsDmdm-0yeIEnRHQE_fDdBzfrl3FcHtqFiWGZbxIupSE471CPaQwKRFX15HxN3bwCnenq7MCah_tLWKw6FXJUiA1BAnhpoy69DPmctFQk5MOOaPE1A-MK5XyFCqv5Wy1skd5lVYvhbJEeUbkqd9C8BGyN7A2njrjGIiU1KZIlYQ8JHl6xxb0ShdrtH_esjR0HWlhsERrTPxr5IzIY0y6ulCVejTq8oAHVrQHDcN-_WW13wCHnz7lP3uqcHEMiIy0uYEHLtNbMRkMQCqSNirZnS7ObvxYamhs11oDi4nRXqdPy65c9fiylelTaib3ICMEmD1xu1NrDPXrtYrQaGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtiQVgs-rYBYFsphOEnahwjeAt2i1dV7riygBUGYOIzeFZOFfDmydErNidWRCB6KG0TsM5__SDr2scw2rAX8t-naximOufZ7LYmilYlnUx-xtGGNw8vuTLXSTJ2fQmvSHqziiVtn3GKDnH3y1oeeIgtNTtGU_OuykbrgF1FeAPyghzzuPOnNcu0uUXL-wemVnGSDN-ayLnYmN17j_vz1Ng7bR9-fyvfcAwlTHGvEsy6QmYaDi0QmHzu5mJOqXhp2GirLaXwfLFKTaCs7LkO7UXTkL2i6G4cQkx-zN6UFOqSszlHS_wqzGD5EQg2zn55cVFNlwECag1xZcebu9FAs6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XoXxpIPrZq6mmT7SiVEu0WzO3HN_SVEHOu4xWBD7WwusLJqa0K_BN2tZUOCq9CQtl7sjgupjSvAOx0roVqJMF-rERw8S1_4hoI7yd5_iJ3RrqQSkKP-ytqY5gclAP4BdAX5KOyuOMDlzybtlngFDhlvBWZezIOdX0F5V-UdCF5tv-EcZxA3SI1CaDcI0d-DFxeX40Gw6X6IO_hlleFfRHUG4YlBxhuWj3vZUVqVp7mlYfOMM6Gehu4mHZcJhWwyCs6pKsC8niKKwneE7-BHTI17YfSDdDcYE8j7JBrAOPkAGOL7KGroHpo_7erWK1I8N8RVHZK19O1rDxEGQxFWlJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HblBN2A9DOVJA8IGh-rEle1f4ZeSjK9RIS1VK3jcP9PZvqx9R1YrSr2ZerP9OrK2d5enXwB4oyp72UXqrh68qebwp2bgCqdFmYQf1dYQ-Rade-KvxbXzOhhyYLD0NSX80VONoHhAThAUPglRZW9qWGRMk78lhJrB9zDEwQGf8Gg3jGb3tSUt1DO_Mofi_VEYAor3t4TO-6POCV8vlqvEneMEFCprICIAPyDxN3RUsGu_RNwRA1jJ6BmsjSqQhOxGzRlPKCqCzRxHUugHKM59tJPxIEyQTxPfIT-Aj0kE7-PEO4bLdKFeMCFTu0YoSnr3w45y4NT2OYS2YbZNCx4KyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jv04V6QltzCtcxr2tdbe0pGWCqgitrOzWUF2-1p3fZ3epK2TiwLOmaTsaS9UxqzS94eCUF5tIZ8qCepPeQ9ehCUsVv_CWhfaYchHnpwke9KBU1J3vqRMdGUfpqOU4IGRasl9Q4NKTVSU8X2j2TWwq_G2Nh-3F8lpKNnoaxGkITznlfsJuX0pyAE-ke8CBOXbG9NsmitCkNOAEUxl3A_lj094MOSgXhf4XBWZ_JIi789bLJ5F7tTsLdshX5DXb1jXjY-htVcskLuifPe2yOUeZAhyG-jpzOVjcBhv6txLH8MtBdVYkcrmMBHl2A6SgZBKErDW6dXKK5aZeyxIBejhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qV1x5zDEkEtwbuv1LaqWqgI4xM9iIWCk7j7f47hstb4k9-xsHZ0izWzfMRAjzezJpSvz65cnVBBGi8vK8BPSCkyB6aVchrvNaBRw54BewN3rRQEFxzYlEnqX_14fbuo7mW7fMvyseyjhG7Sxo-xwGDKHoeTlW4wdGLMY3a1Dl3hJBclxLStSF7f0_WwA9Zi0vl90k2kKFhICqiqW0aR6pYx7NXA-6FNXtoFGZiv2V2bxxJQ1eRCEyj_lSTn8LZpWhfossoQXXr6cSYirTcs5-4qEafXsxGcZjbCfbbSUG_qpUQjJcPJT5fqp6f8Qfgza0oPYahgmQid6j3kufV2ihw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اربعین خاک‌سپاری رهبر شهید انقلاب در اراک
عکس:
عادل عزیزی
@Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/457111" target="_blank">📅 23:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457110">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc99cb7a6.mp4?token=Ff97HdwAEv9om62trISBsVO372rohkU7pCv1DgFbcfPRaorAseWoFGFuGQzzmyABkCaJRWF6DB65OpUTXwummPYHiJmyIgherYLb3ug1zGPApJ59SxeIjUjwGkzcIs2Y137iTG9ejhugY23vfFPNVzkXI4xOFy8XDMoFxj_FV7Rm559MN6gHbOgeyAAQDdRNeqcWTN3s7BQ3pkqMArdGAtfNhxQJdXZ0s7GQYEcqejKGi3waKzqVaUm_DAgR_gVo5LPLwxtUpMj3dAF71WtkvNjIdPMtw-P2qRxBSvPEFogSIY1T4tuzYxrvawKzfYD5wdbajG_GplWYNBgiubYkvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc99cb7a6.mp4?token=Ff97HdwAEv9om62trISBsVO372rohkU7pCv1DgFbcfPRaorAseWoFGFuGQzzmyABkCaJRWF6DB65OpUTXwummPYHiJmyIgherYLb3ug1zGPApJ59SxeIjUjwGkzcIs2Y137iTG9ejhugY23vfFPNVzkXI4xOFy8XDMoFxj_FV7Rm559MN6gHbOgeyAAQDdRNeqcWTN3s7BQ3pkqMArdGAtfNhxQJdXZ0s7GQYEcqejKGi3waKzqVaUm_DAgR_gVo5LPLwxtUpMj3dAF71WtkvNjIdPMtw-P2qRxBSvPEFogSIY1T4tuzYxrvawKzfYD5wdbajG_GplWYNBgiubYkvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مادر شهید پاکپور: بعد از جنگ ۱۲ روزه فقط ۳ بار فرزندم را دیدم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/457110" target="_blank">📅 23:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457109">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تکمیلی/
مرگ رئیس دستگاه اطلاعاتی اکوادور و پنج آمریکایی در سقوط بالگرد
🔹
در حالی‌که رسانه‌ها اعلام کرده بودند که در پی سقوط بالگرد در کنیا شش گردشگر کشته شده‌اند، گزارش‌ها از مرگ رئیس کل مرکز ملی اطلاعات اکوادور به همراه پنج تبعه آمریکا در این حادثه خبر می‌دهند.
🔹
به گزارش دویچه وله، میشل سنسی-کونتوجی در این حادثه جان خود را از دست داد. وی در ژانویهٔ ۲۰۲۴ به سمت ریاست اطلاعات اکوادور منصوب شد و همچنین، مدتی وزیر کشور اکوادور بود.
🔹
علاوه بر این، ان‌بی‌سی یونیورسال اعلام کرده است که خوزه آلبرتو سوارس، رئیس و مدیرکل در شبکه‌های مختلف تلموندو، از جمله کشته‌شدگان این سانحه است.
🔸
تلموندو یک شبکه تلویزیونی آمریکایی است که برنامه‌هایی به زبان اسپانیایی تولید می‌کند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/457109" target="_blank">📅 23:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457108">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در لردگان
🔹
سپاه ناحیۀ لردگان: فردا از ساعت ۸ صبح تا ۱۲ ظهر احتمال شنیده‌شدن صدای انفجار کنترل‌شده در شهرستان لردگان و حومۀ آن وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/457108" target="_blank">📅 23:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457107">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d50b79f5c0.mp4?token=cbnH80xASgsqxYjNk05q1F9PdwjhNLR2GjUBywgYu6OuOBaFtWIAhGW4-eEeiyE4GmJ0O85EzYOw3J4Nm0C5-BRuskySaOuFZQuDBkqOFNjfsSgT8ShsjKpmbMyh6aQGWDyWDdW-oa8GEGkqj_wwk5g2OXbfEtP97wPF6xMQGhfcJac4KpWTv9QhrJnwE7jevzjEf3nN0Wb6egLPeQ4c3bkctP2qIfmEi069BpyziNkHmoKC5OAfduUMP-Y34ejgABRaZhG7ke562oHshPY6USpwqbr08hhCJ_2c2EL4Gb_6tO2jGzOGC5e4pxu3TtZsw1dVrsQGTPgdmW8mVB_Zog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d50b79f5c0.mp4?token=cbnH80xASgsqxYjNk05q1F9PdwjhNLR2GjUBywgYu6OuOBaFtWIAhGW4-eEeiyE4GmJ0O85EzYOw3J4Nm0C5-BRuskySaOuFZQuDBkqOFNjfsSgT8ShsjKpmbMyh6aQGWDyWDdW-oa8GEGkqj_wwk5g2OXbfEtP97wPF6xMQGhfcJac4KpWTv9QhrJnwE7jevzjEf3nN0Wb6egLPeQ4c3bkctP2qIfmEi069BpyziNkHmoKC5OAfduUMP-Y34ejgABRaZhG7ke562oHshPY6USpwqbr08hhCJ_2c2EL4Gb_6tO2jGzOGC5e4pxu3TtZsw1dVrsQGTPgdmW8mVB_Zog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: ۷۵ همت از اموال بانک ایران‌زمین به نفع بانک مرکزی مصادره شد
🔹
این بانک ۱۱۴ همت اضافه‌برداشت داشت که با کمک قوه‌قضائیه با آن برخورد شد. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/457107" target="_blank">📅 23:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457106">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e19cea5db.mp4?token=mfHBxqSgjD1d0C0q4Daw0Vo3WIbUFmlbk3r9nuwDrBCuKPSISqKoy1J4ZChkQqeE48NJVJQKy332XWClI4BZ55H1YX3UWAnbnGSNvjYG8hauy7PsQ7y7AXH7igRtG4hDGOX0gyMMDWmmdULczQrLqAF_8B9JFcBnVhBvEHhT_lKlVtAHXBTXG8zPwSrk7bMaWFyNEvwQNpY1gR08tb7tAOcKSn-ij65WTZbeVNqdB5ZeA-zJtsulE1-UMewA6sxwveJq_4Oeo1rBnWLZXuKSDQcSym2T9Tmp-mxwWz-AzafQfMK3XKCO8KKjH-QTQ8Xweh-hpC-uzoYCZqAYeqeiwGZzvlSid0u6qEMP-ChRvykBIF7eg0Z0EIvVO3yuld_UqhAS5ox3trx30S2-OlXF8Oleenji_QCG1Qk8DnJWVxGTeFp1jsB5oOE2crlb91gqHfm2BZ7hffm6r5z_OzSwkBChonrkW4ceYt1YzAlqHrtfnSmnfhAa-_GxFhC8n55F3bi1tXzdLL9W5Cl-RCChBmw0ZrHHrd15mPQSaWz40KSppOHXjuLTcgMUyqSW47w-drjXdlMbZ9UaGcEwe77mjyzuvQNSc-ZMDUu_ZLkDILDFLWRqg-HrEkfmaVQu_20MJEsQIEwCPK7LiJxUGGW401FQWRcjPLW24_17mL4XU4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e19cea5db.mp4?token=mfHBxqSgjD1d0C0q4Daw0Vo3WIbUFmlbk3r9nuwDrBCuKPSISqKoy1J4ZChkQqeE48NJVJQKy332XWClI4BZ55H1YX3UWAnbnGSNvjYG8hauy7PsQ7y7AXH7igRtG4hDGOX0gyMMDWmmdULczQrLqAF_8B9JFcBnVhBvEHhT_lKlVtAHXBTXG8zPwSrk7bMaWFyNEvwQNpY1gR08tb7tAOcKSn-ij65WTZbeVNqdB5ZeA-zJtsulE1-UMewA6sxwveJq_4Oeo1rBnWLZXuKSDQcSym2T9Tmp-mxwWz-AzafQfMK3XKCO8KKjH-QTQ8Xweh-hpC-uzoYCZqAYeqeiwGZzvlSid0u6qEMP-ChRvykBIF7eg0Z0EIvVO3yuld_UqhAS5ox3trx30S2-OlXF8Oleenji_QCG1Qk8DnJWVxGTeFp1jsB5oOE2crlb91gqHfm2BZ7hffm6r5z_OzSwkBChonrkW4ceYt1YzAlqHrtfnSmnfhAa-_GxFhC8n55F3bi1tXzdLL9W5Cl-RCChBmw0ZrHHrd15mPQSaWz40KSppOHXjuLTcgMUyqSW47w-drjXdlMbZ9UaGcEwe77mjyzuvQNSc-ZMDUu_ZLkDILDFLWRqg-HrEkfmaVQu_20MJEsQIEwCPK7LiJxUGGW401FQWRcjPLW24_17mL4XU4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریادهای مردم کرمان در شب ۱۷۲ خون‌خواهی
@Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/457106" target="_blank">📅 22:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457105">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a78829c1f.mp4?token=Ch-RNzzBStYu3End7F2fUxdI1bV8WlVwYIxBx-CGE-Oe7mcog0HFMhCnDjLwVOGnmy6dA4rBTGQj4S0pEbwSVh7THxnuWASzTiriJZl1rXSB06akvgOXCRJ65lD8FTr-7I0czxy2ms4LUN3080W59hTS1iXegnO1_u2JJp7nlTwBQhKwcCgy9SRbunoEhuQ78bmElAs2FEpdeUwYfGujeJmKYwxSg7qDfTNX5L2F5yo8BIrQABHnb3EodXrTDsCke_V0j4A2SMbsz1mugle2tKybOx7i0CP0ttu5qyS8zSEWpG4v4_Qsp5AwVGgWWbX7Yycjl_tZPriCTq6C6eo_3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a78829c1f.mp4?token=Ch-RNzzBStYu3End7F2fUxdI1bV8WlVwYIxBx-CGE-Oe7mcog0HFMhCnDjLwVOGnmy6dA4rBTGQj4S0pEbwSVh7THxnuWASzTiriJZl1rXSB06akvgOXCRJ65lD8FTr-7I0czxy2ms4LUN3080W59hTS1iXegnO1_u2JJp7nlTwBQhKwcCgy9SRbunoEhuQ78bmElAs2FEpdeUwYfGujeJmKYwxSg7qDfTNX5L2F5yo8BIrQABHnb3EodXrTDsCke_V0j4A2SMbsz1mugle2tKybOx7i0CP0ttu5qyS8zSEWpG4v4_Qsp5AwVGgWWbX7Yycjl_tZPriCTq6C6eo_3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: باتوجه به رشد نرخ ارز، رشد ۲۳ درصدی برای کالابرگ منطقی است  @Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/457105" target="_blank">📅 22:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457104">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e7b14962.mp4?token=lMrG8EpsZQmPTUpgZ4wzsfRQJqdufhpUJTBUfTAEID6sm30KMKE1mAKvdgH-cxmmI3wB0fjODOCKTvWTtjK85E4sQFPDBCV05L4PtSCl5iIIsjuQu9nV7h5rrKE94-3gnbX_sDkblOWbroyVSDMT3Ng4mXh9XziLNfhpgvQrbWMJaXY_GwMrhULRN7bbcyp4ck5N1hrC3Q0kK4JCGobVKegSkd02zhOBQaUFFKnQ0o46eBohlh8VV-MoSZAOcB84mgPHVGQlLpdGK20JbilekvaHWlNP9y9wuwiCurDC9TcQGr247yqHrz5tONXldGOSElI2lG9RhvlUJXfVioJ8BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e7b14962.mp4?token=lMrG8EpsZQmPTUpgZ4wzsfRQJqdufhpUJTBUfTAEID6sm30KMKE1mAKvdgH-cxmmI3wB0fjODOCKTvWTtjK85E4sQFPDBCV05L4PtSCl5iIIsjuQu9nV7h5rrKE94-3gnbX_sDkblOWbroyVSDMT3Ng4mXh9XziLNfhpgvQrbWMJaXY_GwMrhULRN7bbcyp4ck5N1hrC3Q0kK4JCGobVKegSkd02zhOBQaUFFKnQ0o46eBohlh8VV-MoSZAOcB84mgPHVGQlLpdGK20JbilekvaHWlNP9y9wuwiCurDC9TcQGr247yqHrz5tONXldGOSElI2lG9RhvlUJXfVioJ8BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فتح عظیم در راه است
🔸
سخنرانی حسین یکتا در موکب امام شهید ایران شهر لامِرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/457104" target="_blank">📅 22:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457103">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noAcn8SjWpeJIaFOWM0ArjOqZZWvEsHHgGw14Z9vuXTbKk912QchXBvjiANKYOV9WS7zkzTEwKivJ-y8tbqiTa7PquWsklkXX6c1WmsDCnjRFPoEJxPWZ3pxOIgEllOs_ho6EF-EpVH5y6bI1roaw3Zs0WAdZ9i1q_ki3IT8l3EfZJz5hI8jK3blX-F1bbqQHyN1I8yO8YqrxIcYjKUxDFGDW4r2a0AKehDLZTxA_cDMiztWvnvjCPmJHmK18glxZRm5jfrSX3Qpek7Myku0QORLhGKdzM9wQUJkRboRXPz7mycngA6CWSDaQ5w6T-jQkYwVioxuxmDJg75iqdaw1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاگردان تارتار گام دوم را هم محکم برداشتند
⚽️
پرسپولیس ۴ - ۱ استقلال خوزستان @Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/457103" target="_blank">📅 22:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457102">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4808bb6f76.mp4?token=kN_WiElumAE3MSglhAcoC641TjvBnCa5vVth30Jq-k_DlRbWMTw2CBmUXYFXE52BzUhwqkoGsAvMXZgZwK6LUw6XqSSDbAmvK7tlW490VC6WtR1PvcPQRJv7dR9ABnLuiS03yKtdfeG0Ks4-46vMGwj1Uv4ljqP-tV3H0Q-LYXxnHmHf2pDpdYCxsXhzHbx2R0yTtwe9fYazKCjef0gscGEo5CHWDve3YYQolObJ9HUZbRgK7zXaWW8nhUAkqXpgIPVX_wtpyb0F2P_bCtEpcFW_-zVB1y5h7qkSs7NxJjVInTWbyuVoS3yHFhdLyqRG1KLNY2knVPBPoFFSJtQcIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4808bb6f76.mp4?token=kN_WiElumAE3MSglhAcoC641TjvBnCa5vVth30Jq-k_DlRbWMTw2CBmUXYFXE52BzUhwqkoGsAvMXZgZwK6LUw6XqSSDbAmvK7tlW490VC6WtR1PvcPQRJv7dR9ABnLuiS03yKtdfeG0Ks4-46vMGwj1Uv4ljqP-tV3H0Q-LYXxnHmHf2pDpdYCxsXhzHbx2R0yTtwe9fYazKCjef0gscGEo5CHWDve3YYQolObJ9HUZbRgK7zXaWW8nhUAkqXpgIPVX_wtpyb0F2P_bCtEpcFW_-zVB1y5h7qkSs7NxJjVInTWbyuVoS3yHFhdLyqRG1KLNY2knVPBPoFFSJtQcIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زمزمهٔ دعای توسل در جوار مزار نورانی رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/457102" target="_blank">📅 22:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457101">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b984e842d.mp4?token=anJTfaWrK2y5wkzWNhkh-SdSGbtnkx-a-oV7A1fcEkllmgwLmm5FywrqDjPacnJ_ejBOw7v1EgQgk-xScx3384aAUi5pGnMdEc0lHcKPz8npiX5hZDL6XefjMDE3iGaUjpZOpBSo1DZG5zQsicV-vM9p2_g8k5Zdo-RrkjlH2OFqJ84MN51JnA-x0PSzXS_Csqqb4Q0Bd9bTl6nr-G0HwiqezqNICDEXyMVRzJKUYgBJ8M_I--uCubPBWfVgshQQ1UwSHbl6KgDxhR4nLhQ0uDeoRqaozxAZhkEhFvYboR04kAPuYcyW30Xtc2EEfUsRgWmHIYWYLA3wT_j5-Pcjbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b984e842d.mp4?token=anJTfaWrK2y5wkzWNhkh-SdSGbtnkx-a-oV7A1fcEkllmgwLmm5FywrqDjPacnJ_ejBOw7v1EgQgk-xScx3384aAUi5pGnMdEc0lHcKPz8npiX5hZDL6XefjMDE3iGaUjpZOpBSo1DZG5zQsicV-vM9p2_g8k5Zdo-RrkjlH2OFqJ84MN51JnA-x0PSzXS_Csqqb4Q0Bd9bTl6nr-G0HwiqezqNICDEXyMVRzJKUYgBJ8M_I--uCubPBWfVgshQQ1UwSHbl6KgDxhR4nLhQ0uDeoRqaozxAZhkEhFvYboR04kAPuYcyW30Xtc2EEfUsRgWmHIYWYLA3wT_j5-Pcjbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بانک مرکزی: ان‌شاءالله مبلغ کالابرگ را افزایش می‌دهیم
🔹
نظر مجلس این است که کالابرگ برای دهک‌های پایین افزایش پیدا کند و دراین‌باره درحال تصمیم‌گیری هستیم. @Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/457101" target="_blank">📅 22:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457100">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a70545bc.mp4?token=bmZxs0FqCRdL4xOMUpEHaUEhCTdAEtOhPAsGI2XKBpISGKbWhg4LgnVLdOzDbnxZASJDE-HbnnvKZb3rJecyIFD-b-MJVU3jGWsfrXEbQ6qAZT6pah-0KOxolhJId7vz19AW6xWkMpAsqUTLPeLYFOsa2C2BDCXwJRutgGRyDPjg1h4UndfEu36_R2G1jWjIAt4KVrATEvSjwis-lsqtqwFx-JogBLM88KjwOttw5amhmcLoKf4n0PRCvu_AyzOh8ePEFH6P7VpC1YbIX2MyQszhjzRvg2it8uwchKaTBAEspfZsi4gDrGSvkjhluOnQmCqPoS2kJ21B0v3jIKdmPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a70545bc.mp4?token=bmZxs0FqCRdL4xOMUpEHaUEhCTdAEtOhPAsGI2XKBpISGKbWhg4LgnVLdOzDbnxZASJDE-HbnnvKZb3rJecyIFD-b-MJVU3jGWsfrXEbQ6qAZT6pah-0KOxolhJId7vz19AW6xWkMpAsqUTLPeLYFOsa2C2BDCXwJRutgGRyDPjg1h4UndfEu36_R2G1jWjIAt4KVrATEvSjwis-lsqtqwFx-JogBLM88KjwOttw5amhmcLoKf4n0PRCvu_AyzOh8ePEFH6P7VpC1YbIX2MyQszhjzRvg2it8uwchKaTBAEspfZsi4gDrGSvkjhluOnQmCqPoS2kJ21B0v3jIKdmPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: ماه گذشته شتاب تورم را نصف کردیم
🔹
البته این به معنای کاهش تورم نیست بلکه شتاب رشد تورم گرفته شده است؛ یعنی احتمال می‌دهیم تورم این ماه با ماه گذشته خیلی تفاوت نکند.
🔹
تورم در کالاهای اساسی هم مربوط به حذف ارز ترجیحی بود و طبیعی بود. @Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/457100" target="_blank">📅 22:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457093">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iBoPNUUwkMFmUZhczZYK_FR_eXDSqT7NJSLv796DPBYOeQh3BZ3F28zBSpWBg-TDnQYCPGYrdCGcMi-fgAhLjeCcIYyTFieu1JLnSh41MlbCJWy0sp7dMdxLcjJaH8dcoTcBgmQH3jHW9sfI02ZanbDv6pXpyT5TGTsjx2iQtlnQlYXL2POwy9Wk8SDhhIIOVBhaC8ISGT1sj1eOlfRMjPXS6HBCCNFcnBkyzCVPFQY_Rrar3LtTSccgjJK1Y5e9DWXwrukfh5ijTekpvc8HJC3Mo1keCGCsv6v9hmUQlx-cDFTWd2IeNG5VZHx8iQhXkpSOaINcqvtnGatLipkwvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RD73j2cpEpCNtIw5KylRlnikMqxAtrAnXwJ4zf5ETAvbgJ67P8Fbh9hDwScp3SdpRBA9h6jHucaTvyT8pH2Cxsa7YQvHyFDE1BgK1tUWntLuk-k9n1eXq4PkAOA18FhKwz56Ql1pxthmuwMNbGJ0EMM6Y66onOF1QZ5ecHKVFE794JATspYS-ncSqaL9t1jXoWkfuJgPG1a87r1dATMcf7sDvLYjVSJ2WTevq_sOajchliz8mGg0TzqXukQs_ltBLGmqUFPZDgMmnLutKVLoQ2Yj8kJa1mY2ho7cNPv8DlgtXAWgjyxUV7XrfbQgNubrE76lMl7jcxgJXrV4DeMD4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZiGe2IrbwDyTSyHWG3ab9LzJPoPivlG3C1pYW4uPJ8WzoHWz4CKQOmAdXQ9yEZQ6g_rNbeHdII27NNkHkVNIZltTjxHVQo8UOMw30xGmsVG22MJTxA80HbddVHv0t9zgMyTPIyJxRWW7BvF2MIBikf5AWnRyW3pRBAKgwk5qiY8O_AG0G2_NGUM3MKunwwoyrd_4cMrXhH6IG0jJgq_yLKz-wnH-X7YRXChf1LGLk6vUk9IufT_CI67zmMJpjMMz9CTs1UmSUSw30D2uR1xkVibvSnzgS4l_GhZtUDpOSVze-nPtqe_3GaxqTrk3DfaYoey0BYKkuuTniY4mcyc8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fca1k4X088f2OpkxjrP19g84lEqiYfXPcQOb5HhFiXK65iZBCCPba3h-FecevF4ftVhJf4FNj2gOpZPG2rbFAwEkNNWHeVigXLka51iCpEKdbkexe1tVnD7ct4knmQG951CSINOQPqK-EK4avU8D_wBDpeUlWY7ZZkU08GhP8d-dw_YIERjy7IC65F9JuaEmWoDpfa4oPXSg-Rl5TT84NS73x0no3v_U0jO-z0cQqGrD9sZtXOO9klwSwzCBcJ1P1ttS_O8QkWPHAK30q1Hq36V5-BB9NH80LZSfVt30o78ZM_GXsuCmBt3cGDTG0fPskWrW8I8esUsF3w96EkHrSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdR68_bubjHUR-SkyiWhxdbLws7kQ2T6wkNZU1e5MX4dt4zkx5mVrBWYCCpYxHC2eQBO6UvI51tzPWZJajwjra20750_iP5K4sQAkizlQkSp07R0eRNCRAlIcMcDBmKEvwazLMhs9SgJb4eJo9bJ_ecW2q-QW5ojJ-z_iWhNVIE7mXdmb3VVSFZDdssxJ9RhbO9dX1YlNS6-foDZIs26gR47HBNyl_OI9XfbV6dWF4Bln2iYaxZlZzSGdFKNSNp26vHjczcZBGg0EzxtACoNjnH7JMNuFW2QGGrJ8EBp-eDawnnSRZw3HIIEZFMYU7IrqCdyBZOraAdg_kLyWWD3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GF9m6-PRgO2opEt8eoLMEwvfQJ1sysTFDtcmSGxBEyolezhOGzJsg1mDxU9wEUwvv5_EnmmJRui7DwxLSDNzpsTNTHT-mOq_whc5Pct8YOTs2QtJUPyEmM4A1UiXzY-D2ETaFXwkUGyxRIioZ_OVWQioX9BdtgHhblw5HLcA7eWTvDcfQUhWoPYk36HtCRRsvlQTwTXJ4LngmjmSuHT87A9oHG7lXewSUZ-h9WGekKMWG5_t8Gh8D0AIqcCGgEav5K-C7zBub-UUMVZqIvyIadEvKQL60PYiVid24hosJ-DWyyD-F0ISPm7QjmDvQUDDFxNG6xa5cTUui9H_87fetw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PK3FZkBDC2XKI__TvL0QtstIsV1uAzniPjnay3ur8MO9Oi2_pXbr9FBalHAeM4pMjYsVZxgAZoeyXtJwFS5bE_HusXCFSamrA299bFEyhlzTketwre5NwGI9LyUx45yzJbJj_diMq5az9ONlPun_mZ5BIlE84LaQonw5jbjoFRc23nJVmNwMyUlp9jWwxUS59p1DUMVFDf8jkevK9o1JKlferVRMdLwOxb0pMpKy892v9ftMksQXfd1exyuQNk9CvXN3GJJwA_dM42znpb53h2YM2igyfML9G7ZGL7nVUOQJ9HQeZ4-WsQaV-XhLS3NiHRFxmB0bRXuZePJZJADBLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت چهلم رهبر شهید در قم
عکس:
حسین شاه بداغی
@Farsna</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/457093" target="_blank">📅 22:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457092">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf0c47651.mp4?token=ZT0wKivQvoIwVE7Kl4u6PqrX1mdTZjhW9ssC5gJF3rwq2MX5xGS048BwYSXU1jaiMs5iRY9IakxbIE04ZJ2PIbpiNddFAxt0lrB3Aww4SggJu3bU3k-_z1EfqEVOdmlwLc6SITsW8muT2s3IDZKqXgWfXVhu3YJgWQDpLVz1uwMG-hM37pz6tg7i4IdkInJtTCklRJfz-yfI9KrS-7mFCarHcP-5he9sfUrq0FtLWj4rhLF55CjBFiCnc_os9yY4NXMJBSrpvlpjpoD2AS6lIYlt4cldjhCCEEXOenvfO9oK72tJLJ9yo92AWRu1ERvwu11qXf2Qi7ujVkr_vnh4jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf0c47651.mp4?token=ZT0wKivQvoIwVE7Kl4u6PqrX1mdTZjhW9ssC5gJF3rwq2MX5xGS048BwYSXU1jaiMs5iRY9IakxbIE04ZJ2PIbpiNddFAxt0lrB3Aww4SggJu3bU3k-_z1EfqEVOdmlwLc6SITsW8muT2s3IDZKqXgWfXVhu3YJgWQDpLVz1uwMG-hM37pz6tg7i4IdkInJtTCklRJfz-yfI9KrS-7mFCarHcP-5he9sfUrq0FtLWj4rhLF55CjBFiCnc_os9yY4NXMJBSrpvlpjpoD2AS6lIYlt4cldjhCCEEXOenvfO9oK72tJLJ9yo92AWRu1ERvwu11qXf2Qi7ujVkr_vnh4jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: تاکنون چیزی از پول‌های بلوکه‌شده در راستای تفاهم‌نامه آزاد نشده است  @Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/457092" target="_blank">📅 22:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457091">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eab130c1.mp4?token=tnFY_fT0jNkjfJkjY_Bj5YNP40um6qKSv4CQwYGvng-SVY8jt2uhBMtDEeMLE1Y27kfnNu8_-onnhHYaPXirNsfo_AnSjyGG7HWNLZKFs619nHTJOC6pTcO-dm7C7PlcyXYZNQ3foZkZl9kBCHx66uRfd6eUO44jQ8XG4F_91DaFNl3h1FX2T_vMKLbrK7lQjpevPPrccQSjlfvpTrs15KvbjTl1gnREN0WU-OS2lSgES-HmftPj2P9n2U8x1SUhisrdS7vTA6ZEajO2iW22a8jYBAgLRRVFvSvCBkIR9vzZz9c-BtgWNop2FI0M4gVlMDIn5l9KOokIfxdm2iyZNzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eab130c1.mp4?token=tnFY_fT0jNkjfJkjY_Bj5YNP40um6qKSv4CQwYGvng-SVY8jt2uhBMtDEeMLE1Y27kfnNu8_-onnhHYaPXirNsfo_AnSjyGG7HWNLZKFs619nHTJOC6pTcO-dm7C7PlcyXYZNQ3foZkZl9kBCHx66uRfd6eUO44jQ8XG4F_91DaFNl3h1FX2T_vMKLbrK7lQjpevPPrccQSjlfvpTrs15KvbjTl1gnREN0WU-OS2lSgES-HmftPj2P9n2U8x1SUhisrdS7vTA6ZEajO2iW22a8jYBAgLRRVFvSvCBkIR9vzZz9c-BtgWNop2FI0M4gVlMDIn5l9KOokIfxdm2iyZNzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/457091" target="_blank">📅 22:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457090">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7e60144ae.mp4?token=KyuODHTtjcWrq-5iTyxXkntEti9J8A20zb35iAkLlPpadTRbmQ63qkJVUkzNBv49WG-HVlc-BS96JSWX4UaIrFGFny-RlJt5EL_-rtRZmSV4l-FDgxGOpT285pDU-BJEVvbCjw61L8DJHW8HCVaIXLX0NfmrGN8hZT5a3GKcQo3htcPOvCShBlB5vykty_K3NeHoloCT3O4rIsVyxPpubESGJApilwI4yQAmL_1JtVPmUnRnGnEHMX_P31kVSv0H4ayBdD3rtuC-nRrgGIh4hHp2jKDLtr520hvR_y_RE45KQXNhRMJ5fbYh6lwFd8Vnlh259E7YTzMx1dqfOLug3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7e60144ae.mp4?token=KyuODHTtjcWrq-5iTyxXkntEti9J8A20zb35iAkLlPpadTRbmQ63qkJVUkzNBv49WG-HVlc-BS96JSWX4UaIrFGFny-RlJt5EL_-rtRZmSV4l-FDgxGOpT285pDU-BJEVvbCjw61L8DJHW8HCVaIXLX0NfmrGN8hZT5a3GKcQo3htcPOvCShBlB5vykty_K3NeHoloCT3O4rIsVyxPpubESGJApilwI4yQAmL_1JtVPmUnRnGnEHMX_P31kVSv0H4ayBdD3rtuC-nRrgGIh4hHp2jKDLtr520hvR_y_RE45KQXNhRMJ5fbYh6lwFd8Vnlh259E7YTzMx1dqfOLug3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ولایتمدار شهرستان زرند در خون‌خواهی رهبر شهید به پا خاستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/457090" target="_blank">📅 22:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457083">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N1bJBBFPktehP1hMTQ7GiW62vw25Y5fREQShTYEuzn9081EUZrLG5Xw-fMUOvDH264W5iMi3GgfNLz9MpizV7G8eDQ1API4Y-dx7ZN84kizBiAoIVuhCo-DoglCose1qehKwk1-IcsGAyXtwiRqdUY3qS_w9yevkqI2nN3MRXA6oUdNxkq0wZ649q5SBBWTaauvHd9aLgBPUyYNsKBpSTjC3N8Hcr557VcGvHkyAMc99NbvsnHAH2L6uN6i8LyQ_95hcW6HCKGn1J_i8rsTYeimNH-K6d2cqu77br9bwbRsEIf_fYA4-qrZee74bA5x6kj6kNO7XCD7hrl78svnC-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4XEmdW3MY5S5VZGdSYqSRDQB4_hx0EVbraXZ1aCSgWGQ5DaYwpwxc1yJDcY5LIWKQoPf2ByS39D5Qf2Ostiz7N8bTJS3TU8ZHKpGjUL03x5bBozlKYBL17R1TfAdT_sxeBS5LpPy26_LmkEqJpZV8KDbGd9kZ86UZKssuQ5BDg0nQrcfFxShcJUwnZ5iLxKou7RrsSGiInomCMMibFPV5iNC0HUCbBw4aLfVptZrH16kERF-_40BraymoF2HLBNMOWm4fkddd-zOkemnu0DBZlj2F9Q10WnyZ7sl1gO-nEPssXkKEyQgupRJ9_2-DXEswy9jLxTrHnmQEpnYmaoFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aXALpNDvb4lktJWnOkPoYqN1Aetb6WpKnq1BEZPwljFIs1RqaWOZ0H_Gll6uPsDWw3kzH7U3dE6LjXJFAsG17InhRGV54KA11RpPgKzg7vNe-wsidzBej1BIabDKiDG14tyNipQAmwrl3SVh1fcKbCar4zVTd-1O_Of95TEDutItejBdb99pYg4POPJKzgxGD7tuOnG-dhezE-5ZFoGYtD7SB19NTO3tybYXgX9gKZgvC4wyVkdSBiMExAtHF2No1yqWytp69_2s63r4ADeVnlCNbgN_zuEP2tXHcU_6mOodrBoSKgf_TpF-4Z5KjSJerShyWVr7q0jYkSJ2pwy8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QfhFC9r8RvNnMV-gaofYpji5ewNqhK600NJ_3x4Ngrw6a522fXVrvJkd83Sbn2l0bMo5rjVKqqiHTgpXow7dVpzWxzIu_qaFeG46iqEb1WHGR1kIoq3qsGhO8rgQwptyxlVrSnmbsLC5ZcbLthpJyjYZhEA88H2eaGr5mAW_J6R_AaISs1If4mOFFAdH8Xvo7LgNfyIn9Dzxogeuojma9rktrxVagxPCbmn_K1Ut7gdsj6ItYLnbwnWfUvBeJ_8qE7ElzgqHeFvt1mZovWVQ0JqwtBCGlCX3CpbO7rjiMHAt8FgIMwJjdCUDqYUYP5ONcE5860Wg_tc7C6SFayM9Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mRvZuxs55Fn1bPgg03hpb56VibpWomM_jbncpIYZPSVOwDaMmx77cut72tSnSpiEWkTTn3mOr0tfeWhgDptlag8LPyBnlpBsZxSirhzQ3OCFhKkmBiZM_9Xul4oGuDVGKBZIbrtMhztJajA0nYKGHuB__I45Mau-UNuXK2Jfid0gw9TImja9CKHQwwbztW6_EGidDJEMEgklBTCbRcHZXxNGJkXCFu8-ZGLEvYTP9mXIMIVRwYaLFX7T8zMPlcu4x6k8-8dYKAFiuLVRipHGc_6YyS8I04JsXgINlClV1t-D1L5Gz1tkUzfCmFUi-7NR9v4OUdka2Ll-_N8IWAf35Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kehagCyE11LK_7VucJEjRbITC_Hcuof-9oOXOu8IBsNVCXCbjXshRqC0yi8UDxacolYl8HAoNI2yrxpPGq0q8vAXvLItYzacVDVJz45HmISY1UyRB4ypNhrV0lIwddLhaHQshkBn6G9idHRMfBjPwRsxv2LyO7DdpJzcL2i-M_JOWBg4mKh_kgQfEB0Wle3eWKkCkjx0myAwumT-0kyhqoqEG0eRciVAVFrb_VUZlH4nh8RiJ32Jv38MUt2zRxITZ8uRh5lfM8_H2CQ1D9Qep9C_Y0EHjy376s5yy7qEVDiLap_zbN4pwAT5pRPp-0XVj66BzEBEz86FdNBBN5l52A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Apb7zXl3Yh8-275ORAaWLthyGGu523PHbNoMfkEhSJ09aPncSafA5m8-YoGlNVaxpHoLXXbHNMIw3lS-UMhT5DoMj2qad5dK9R3WmYN8G9oLz_1VLVfKBLC8fRXda0vSLoW_wpsN9K3mc64aT5TdRfy3rAqdBs1N8h5eZ5ghIBK2GJzoKKC5W7nnJR-bppVu3wBzegsjW0kQEsU84L-Epv5glTkv1Jjisk13nqDCGOSDxiRR6qnjnigovt4B4iVku0fSY1bEfqpKcLpo5L9tb7o9LRlWWRGPUiZg-6o4Eh3oOjAjE3fEWvIAIjHER2RDdfz_fbG_aVZjltXSDddy0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشنواره «ائل سَسی، کتاب نغمه‌سی» در ییلاقات اهر
عکس:
مهدی ایمانی
@Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/457083" target="_blank">📅 22:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457082">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80b6cefd1.mp4?token=YLtp_xh8YiRfdvdMGSyehRwjlg253uUZhgHBnvk63hwl_X8xkRNyNLZshNrpC3-tv3TWT_AM0SL5LVsTts41kzMAht5tBvXcAF6UbFlTpUpkDuCGUjfFa9_Kzjliy7fIecuoZvFXQarOuFkFMatBGw3WKUMqeAoj1t0piIcSJMmzjamRhjS3BtDX0oFaOcSg2SBNybZ3mkvZNhN4Or5fq1cMaMzAtpDuzUB9uwr7KUQHVjcfEM97IL5FVC78gDftNMHd4JqMNsLZF9sbE0c1-CRaWCBvr_xuedj1XHXatyGxrGbu9qd0FsA_eQXeasCcGMZ80dO4-KI-UbL-PUrIZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80b6cefd1.mp4?token=YLtp_xh8YiRfdvdMGSyehRwjlg253uUZhgHBnvk63hwl_X8xkRNyNLZshNrpC3-tv3TWT_AM0SL5LVsTts41kzMAht5tBvXcAF6UbFlTpUpkDuCGUjfFa9_Kzjliy7fIecuoZvFXQarOuFkFMatBGw3WKUMqeAoj1t0piIcSJMmzjamRhjS3BtDX0oFaOcSg2SBNybZ3mkvZNhN4Or5fq1cMaMzAtpDuzUB9uwr7KUQHVjcfEM97IL5FVC78gDftNMHd4JqMNsLZF9sbE0c1-CRaWCBvr_xuedj1XHXatyGxrGbu9qd0FsA_eQXeasCcGMZ80dO4-KI-UbL-PUrIZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: تاکنون چیزی از پول‌های بلوکه‌شده در راستای تفاهم‌نامه آزاد نشده است  @Farsna</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/457082" target="_blank">📅 22:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457080">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">پاکستان کاردار آمریکا در اسلام‌آباد را احضار کرد
🔹
وزارت امور خارجه پاکستان روز چهارشنبه کاردار آمریکا در اسلام‌آباد را احضار نموده و به دلیل «اظهارات نادرست» سفیر آمریکا در هند درباره وضعیت جامو و کشمیر، «اعتراض رسمی شدید» خود را ابلاغ نمود.
🔸
طبق بیانیه وزارت خارجه پاکستان، اسلام‌آباد توصیف جامو و کشمیر به عنوان «بخشی از هند» را به شدت محکوم و قاطعانه رد کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/457080" target="_blank">📅 22:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457079">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751a5db559.mp4?token=JvTQ8RWZ_RvmBoKKEXvNHObC9llB86K6LvpvRDVqGXFDjMdG9WBf-8smWh_5hg7knVv6FCeuWT127-kY4vcZl5Do8J1OQehSOdNz_-UFDiQbs1Q1dv6vrhXATsKJ5rcZtA6FaCZDNHTbKzrBSjuy5YT9eNshyecuJFA4zcp_GiAwI-iqZEH_dpszXdMLHKYlbxxLqjNi4lfHEr0M0KSf91F74heC8p_uu2VZqJW4gRk8r6GbdiiIpyqiPKsph_A6j7MMQjFIbAqHiiGPvtemIpyusitA1epqTkd7htlA-GpeWU5oKFcTVr7gQ6isco9kQNmPPnEcyw9xPQ8IUurVbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751a5db559.mp4?token=JvTQ8RWZ_RvmBoKKEXvNHObC9llB86K6LvpvRDVqGXFDjMdG9WBf-8smWh_5hg7knVv6FCeuWT127-kY4vcZl5Do8J1OQehSOdNz_-UFDiQbs1Q1dv6vrhXATsKJ5rcZtA6FaCZDNHTbKzrBSjuy5YT9eNshyecuJFA4zcp_GiAwI-iqZEH_dpszXdMLHKYlbxxLqjNi4lfHEr0M0KSf91F74heC8p_uu2VZqJW4gRk8r6GbdiiIpyqiPKsph_A6j7MMQjFIbAqHiiGPvtemIpyusitA1epqTkd7htlA-GpeWU5oKFcTVr7gQ6isco9kQNmPPnEcyw9xPQ8IUurVbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: تاکنون چیزی از پول‌های بلوکه‌شده در راستای تفاهم‌نامه آزاد نشده است
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/457079" target="_blank">📅 22:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457078">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXBUZASa1NV556BtfKJ5d5o-7bZ_-A64oBAkRSC__g4EOVJwThgtzUH7knxILGmjOyhna-FDYa_py3F9uY_8fA69t3zRZRXl3BMTK59DuwQ1KHU-2ZBJzSCTZ0BJ_aH2dv2Focyf-meEEBs0q9c8Ou38Wh_1t8bFKfArJrlLa-LTR7xlqI8Y1ewDMgZMFI-_FLNjYGgPdvCMgDh40qzEGA8_fNpK8kFJwb3-bOs8Cmg3juv21rBAUptf69r8uGfbhgQKqBvIYgLs3-xKTX7r0JjENtuq98KsHtJlP_GLBuVDiEW5C6KiiWfxVvp_HKrEXzEHobmhCUa4DWF14vQpYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی با عاصم منیر
🔹
وزیر خارجۀ ایران و فرماندۀ ارتش پاکستان در تماسی تلفنی، دربارۀ آخرین تحولات منطقه و روندهای دیپلماتیک تبادل‌نظر کردند.
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/457078" target="_blank">📅 22:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457077">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjM3Xkce5qhp9-6yfCjEFrmTRgUGfEs-3fkR20-lRKUEWsKiEAdkOHDhehln2MHsvGXsSwj8T9gRM8lPpfI695xg_qq66MVZXkWFrPmionl34_ePlsZJNxrsEos9mVLcSzEOjujfHSPDwlijAsxY0GV9VQ2fs6BMD-XPfZZqQCdJQZLpbPYiLjTdFkeCyWQ-7pcy_cEzfD_49Tte1CseAXbyzi_jjxSqmN_aZKUFlFEeb-aSBvn8135vTcQp5aJjrw4tRslQhbZaZMHKzRtfmEhfWxFVirIUtw1zAU8gVYWwT0yWI5ffRXs6rpbWAIUj6408d5haAO_uU1usSJug-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: ایران و عراق دشمنان مشترکی دارند
🔹
رئیس مجلس در دیدار با نخست‌وزیر عراق: ملت ایران و عراق هم دارای اشتراکات جغرافیایی، تاریخی، دینی و مذهبی هستند و هم به عنوان دوستان و دشمنان مشترکی دارند.
🔹
ایران و عراق با نقش‌آفرینی منطقه‌ای در بین کشورهای اسلامی…</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/457077" target="_blank">📅 21:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457076">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvmWdO2fOay2TOn6zVG5Xvv_U-ztHsPbTaZUnd-vtK1ZLOlOQCLOSIbXP8y1QWSTd9hqxDHEkiK-wRV7Ap3fOf9fjHh2ctu7qYHhstd8ZKqGbI9K-ZQybkkQovDqk04yw_sAJs9S5dGEK3vF8kcCcnAW5HcrOupEjeQ7UnO5KLARqJ-ao6w1sqR-pso6lbcdl9r2MublcDQo1HGhApUmBwsG8PqTfOJZ2tRCMz_16bwuIXB-2ZcequeweM4mlxrGN04qTsfXHgQiCI7H8LjzGwSjv2jdvPrsyPu_aU2cywuaMtu2Zmyp2Zr_QTnzHV-HnOvE4K2UH6PFViMCu7xqSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرخ‌ها با پیروزی استارت زدند
⚽️
شمس‌آذر ۰ - ۲ پرسپولیس @Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/457076" target="_blank">📅 21:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457075">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/495a4bf5de.mp4?token=i_YxV5q_M3zqfdhU72B-Ioozgs1TGHAjJByLHkDPbEYNfkP5szb63DeFyx4MxhMLgwZM6oCmwCvdrINHcpeDqvBemGrOpuB6z463u2wm8vA2B-NOxPsXsrrR-Nsl31OIrH7gFdozQsl5L2UfSYCoSgKGJJm8xm3965aLp1vtBH2f6cKQasFkDEH0Lq9WkR42yRrOFSJEIVbUlWQjDQT1Pi4g7ohK8Yv81VGvBfXF36P6fm2umB18P6I8SEBTs6xIz41OXmbUNhcbC_0SF3clKadpQuKAY9bR9b9yylXUHnGd7WC-_thTgpqeHFt4X4tJzP0Yj6mhS9Gj6v_V8QX7wbjtgZO2ktO66q5caBia5SqLPf5qaqJmq-24ka9odl1_G6cZ9VueehShUCVkFAerlX7L2PuqPY3FW-t_Grf1O7v3Jmh5ABC78-RzL5HDfR8opBUx0LJO8klI_cb98KNuUryqSrzNgBNGU7j3serMWzkxtkFA4iSQLfu7e8AmRqYCvtWODlgJ9pWWBa2HSln_EraouoQkuf8k9cMVIa1oaxBTHlqAxRe_jTNhwwbRfFy94tdXWgKMJLVxxOgAD1o1nk0tBLbQNF2f9Pu_8IiLltdQO64_HR7qblAsg97Jugmzt56EtwDUnkW561guHA7Xr31dbcGfXO9wyomxzNnp1Dc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/495a4bf5de.mp4?token=i_YxV5q_M3zqfdhU72B-Ioozgs1TGHAjJByLHkDPbEYNfkP5szb63DeFyx4MxhMLgwZM6oCmwCvdrINHcpeDqvBemGrOpuB6z463u2wm8vA2B-NOxPsXsrrR-Nsl31OIrH7gFdozQsl5L2UfSYCoSgKGJJm8xm3965aLp1vtBH2f6cKQasFkDEH0Lq9WkR42yRrOFSJEIVbUlWQjDQT1Pi4g7ohK8Yv81VGvBfXF36P6fm2umB18P6I8SEBTs6xIz41OXmbUNhcbC_0SF3clKadpQuKAY9bR9b9yylXUHnGd7WC-_thTgpqeHFt4X4tJzP0Yj6mhS9Gj6v_V8QX7wbjtgZO2ktO66q5caBia5SqLPf5qaqJmq-24ka9odl1_G6cZ9VueehShUCVkFAerlX7L2PuqPY3FW-t_Grf1O7v3Jmh5ABC78-RzL5HDfR8opBUx0LJO8klI_cb98KNuUryqSrzNgBNGU7j3serMWzkxtkFA4iSQLfu7e8AmRqYCvtWODlgJ9pWWBa2HSln_EraouoQkuf8k9cMVIa1oaxBTHlqAxRe_jTNhwwbRfFy94tdXWgKMJLVxxOgAD1o1nk0tBLbQNF2f9Pu_8IiLltdQO64_HR7qblAsg97Jugmzt56EtwDUnkW561guHA7Xr31dbcGfXO9wyomxzNnp1Dc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این هم جواب مردم به گزافه‌گویی ترامپ
@Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/457075" target="_blank">📅 21:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457074">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrigciQk8VZCQQ6RIKSFFLyofJyDNbrtGqhg3avSxRW_XNoMrHOma-epTRnAPi2uQpMPKiDtld8jvV5_fuBqPleeBs2ELag6dcSd0DjSENPic-o3kLiLDT2JBgapyi5Tcyh6anROnWewaIsu4swvJPzT8CnrkGThY8rz2OE40YHIOpyZQ-bUW1eQOUKRIJnctY3aTqveqXS8U8bdB0uQyFfXFar9ikzi1R_aGXwp9nSyzgSLWCksS2xqPUUUiCLMeAq8jgaKX4MgpdMVTiKGuVzpBAzxiaylrkAn-R4eNcMQ4mE1mQkhrimGNdN163jT8eC9R9Cs2YQhhTOAU9DBGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نمای ویژه از مزار نورانی «آقای شهید ایران» در رواق دارالذکر حرم مطهر رضوی
@Farsna</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/457074" target="_blank">📅 21:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457073">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">زمین لرزه‌ای ۴.۲ ریشتری حوالی گیلان‌غرب را لرزاند
🔹
زمین‌لرزه‌ای به بزرگی ۴.۲ ریشتر، شامگاه امروز حوالی شهرستان گیلان‌غرب در مرز استان‌های کرمانشاه و ایلام را لرزاند.
🔸
تاکنون گزارشی از خسارت‌های احتمالی این زمین‌لرزه اعلام نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/457073" target="_blank">📅 21:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457072">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Od5NGV7XBoN9Bp5y54yJuWW7vZM7KWz91n_OooyNNS5ze6hmkS784VBWk1I3U0cb2Llw4zKfW08YlAWr5-ZpGN2tEICMrxI8ZxrZ4WqnP6rJmqNHcU4dUi9cRK9BF7swTj7vsLy9ruZPnyJT1beY0MjRdo2cRMD_fnvF3FguIrkvVH-aK34HFmtkHk5SUj5Mvb0bEtpWLqMtmmq7GQ95VU0Np7f0_2jhmN68_XO1sz_8TcUfRdSrMZjgXi1987Te9os5o3WCsDjCMt7CjDopZuDAcKu95lB8VTvMo172mwA5IUmtfProQy987CrFQgG_DNMofiqd8GCsm27va8Ling.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قالیباف با نخست‌وزیر عراق هم دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/457072" target="_blank">📅 21:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457071">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d316473ded.mp4?token=f7ydUtKiGm81diCNDdYxh0pfA9zSJawH8oWuQKXIcneoHaTCnz3F4srrGYQmITpfofsd3cKmbRq08-aM4VuXwzh84o_2LnfUqzkmJ7gTtKKCPc5w5PZGTC-R6U55oPYp7kFiQjT5Mde7C4QWr6e8kDafYEAkY5FefE0zJrOerJT38iDArVmgrZTG3X9K6t5QXa2N9ahN1cBmLrjQb9DWoG00w2C2nSEMA7wgVtMgwFZ33Re1lEIVy2a_xlWxgf1ggwYGWtZxA22YwskyuaWuU7Xk1LcgdHYiSiewY3X0iKMLHVGS_xT8slUqTj2xUbOstEK4lM-4pP5S1oBVq06t-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d316473ded.mp4?token=f7ydUtKiGm81diCNDdYxh0pfA9zSJawH8oWuQKXIcneoHaTCnz3F4srrGYQmITpfofsd3cKmbRq08-aM4VuXwzh84o_2LnfUqzkmJ7gTtKKCPc5w5PZGTC-R6U55oPYp7kFiQjT5Mde7C4QWr6e8kDafYEAkY5FefE0zJrOerJT38iDArVmgrZTG3X9K6t5QXa2N9ahN1cBmLrjQb9DWoG00w2C2nSEMA7wgVtMgwFZ33Re1lEIVy2a_xlWxgf1ggwYGWtZxA22YwskyuaWuU7Xk1LcgdHYiSiewY3X0iKMLHVGS_xT8slUqTj2xUbOstEK4lM-4pP5S1oBVq06t-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال خوزستان به پرسپولیس در دقیقۀ ۶۴
⚽️
پرسپولیس ۳ - ۱ استقلال خوزستان @Farsna</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/457071" target="_blank">📅 21:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457070">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eeadc87d4.mp4?token=UB-l1XzmMmVCirEEfFtamvhE2k9LmYImsXceljUSPgdKxje4-UM5hWxzB9vjOiyTYPBnkRcKAPjrLSMUBP3gnrz1WOy8zyLn-BOyZNp2LPT-r-ruF1rUzJsvu1cRVviqIJbOmBJ0z8HCGxRBhQzTkgE1cE3lKmTVkZrKvh9OHFz2ZRv6-tw4sdwuZLufsdWS2GQGS_MtJPvVzixWDVuYHCfOcxtxjCMmzc8etbr1t03Lcq8JOVa09io4CxwEWL7bSgzJcLPwPA8YoBxkiQIJ3mLT3_WKdK9nYzJ37EdvUKh_FejqeW6morjrw8FOcA1-s0tUS7ooPMDUGl7LQcdzIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eeadc87d4.mp4?token=UB-l1XzmMmVCirEEfFtamvhE2k9LmYImsXceljUSPgdKxje4-UM5hWxzB9vjOiyTYPBnkRcKAPjrLSMUBP3gnrz1WOy8zyLn-BOyZNp2LPT-r-ruF1rUzJsvu1cRVviqIJbOmBJ0z8HCGxRBhQzTkgE1cE3lKmTVkZrKvh9OHFz2ZRv6-tw4sdwuZLufsdWS2GQGS_MtJPvVzixWDVuYHCfOcxtxjCMmzc8etbr1t03Lcq8JOVa09io4CxwEWL7bSgzJcLPwPA8YoBxkiQIJ3mLT3_WKdK9nYzJ37EdvUKh_FejqeW6morjrw8FOcA1-s0tUS7ooPMDUGl7LQcdzIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین شعار «الله اکبر» و «مرگ بر آمریکا» در مراسم بزرگداشت چهلم «آقای شهید ایران» در حرم حضرت معصومه(س)  @Farsna</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/457070" target="_blank">📅 21:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457069">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acaf501b28.mp4?token=tpuw9Q2I572IOsiqBkc64KKhamXddg84Cv_Cctt6fYCF4tQqWNLKgqn10KqL8joyQTrdDi9Qhi6eSoEhkkwlCxnCmf5mOUXYjxKhyglexqvB4-4aM6g6GpnBnAkTecKXRBryGAzl9cL_PDPtSNZQY82nt1f7TUofY27-jFp9OuDrtq3zLaHXnXhUqnxdXt9p-0EVIkbAuK2MjoF601BHZaQBv8-O5GBZsHl8bu6hukoL99y2to2xKb-f032fgWSC4KR6ICrmTtP8yKEjgyHSZPan_D5S8m5ex83OhBDbRG7mW6EtqZd4UirRDIAiqFREfcgqqOGefh2G_xr5AjlOoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acaf501b28.mp4?token=tpuw9Q2I572IOsiqBkc64KKhamXddg84Cv_Cctt6fYCF4tQqWNLKgqn10KqL8joyQTrdDi9Qhi6eSoEhkkwlCxnCmf5mOUXYjxKhyglexqvB4-4aM6g6GpnBnAkTecKXRBryGAzl9cL_PDPtSNZQY82nt1f7TUofY27-jFp9OuDrtq3zLaHXnXhUqnxdXt9p-0EVIkbAuK2MjoF601BHZaQBv8-O5GBZsHl8bu6hukoL99y2to2xKb-f032fgWSC4KR6ICrmTtP8yKEjgyHSZPan_D5S8m5ex83OhBDbRG7mW6EtqZd4UirRDIAiqFREfcgqqOGefh2G_xr5AjlOoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله اعرافی: با رهبر معظم انقلاب پیمان می‌بندیم بر سر راه امام راحل و امام شهید و آرمانهای انقلاب اسلامی تا پای جان خواهیم ایستاد  @Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/457069" target="_blank">📅 21:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457068">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c017da3af3.mp4?token=J5F372fLo5a4lq85FmgeusXqnkJbirzzVLtnefnfeIRqMMuHtjqo8VgeZsd36EBPkVN5dBzT0Yi5TRMCKUU9SDW2qaU2cem-sq4aeECHvFZ4hwpiyf9RIs1mZx_yYvECEQFQdl0x-vbcoNui7CN_Ku6W2UiNutfQaGDJIJ5mQEWl8n_eX2vMMv-DObCafaR1mb1QT44tyncR924PQOOQA9MfVkb1YT_u26ilnIRDy8Z99VMqjS58567Nl_O8pW5fL1DtG_dG3pGUZzJjMiko6qIXlUy9abeA4O9qGIcT_kIjge7l4sIHfu2c4-wDK6viz_Kjs85Ibyz-RmzfA_vXhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c017da3af3.mp4?token=J5F372fLo5a4lq85FmgeusXqnkJbirzzVLtnefnfeIRqMMuHtjqo8VgeZsd36EBPkVN5dBzT0Yi5TRMCKUU9SDW2qaU2cem-sq4aeECHvFZ4hwpiyf9RIs1mZx_yYvECEQFQdl0x-vbcoNui7CN_Ku6W2UiNutfQaGDJIJ5mQEWl8n_eX2vMMv-DObCafaR1mb1QT44tyncR924PQOOQA9MfVkb1YT_u26ilnIRDy8Z99VMqjS58567Nl_O8pW5fL1DtG_dG3pGUZzJjMiko6qIXlUy9abeA4O9qGIcT_kIjge7l4sIHfu2c4-wDK6viz_Kjs85Ibyz-RmzfA_vXhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس کمیسیون عمران مجلس: بانک‌ها تمایلی به پرداخت تسهیلات مسکن ندارند
🔹
آن‌ها ترجیح می‌دهند منابع خود را در جای دیگری هزینه کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/457068" target="_blank">📅 21:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457067">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFDlbfKoNoNzejgLHSP5Ew8bJG7pNWK4I3Dm0DNcvr46G_UnpsmjS66WUvnbXTU97zPgdSEeF937J9w0w6DxuWbq6bPmHwQ9CTy-D0MFw137xBHXXYueJjy9dBfwi8SQXu57vd2z8kxsgSTMuH51hXNC4NHdTiiF-Pv7NBaaow0bKz_ozsinbOvFvsGuZIWB-Y1_IBRo26WDuv-i-eBoCK8oiMM4giIfz6l2bRebg15e7lmG-AH2iix_BTjl0nKJMDhOcxa926aoDqa0hreXkUdaeG3QyOEWasWdiB8IzneZZvGxZcVZUlHGWxVsFAlJi-J_VukFp6Xq5MQ-az3m_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس معناداری که قاليباف منتشر کرد
🔹
رئیس مجلس با انتشار تصویری در اکانت خود به زیاده‌خواهی آمریکایی‌ها در خلیج فارس واکنش نشان داد.
🔸
این تصویر که قابی از نقشه خلیج‌فارس و تنگه هرمز را نشان می‌دهد، به‌نوعی بیانگر تسلط ایرانی‌ها بر تنگۀ هرمز و خلیج‌فارس است.
@Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/457067" target="_blank">📅 21:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457066">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4612523b.mp4?token=r_uomK86Zi0deK7VBWdKlQVLM8Gu3j-Ys-JfkJg9uKBKYUKjzfY4N9LT-4CWhwzphJzpQNSlxk3xnZmVrMJRFldVo5xP_-1-meNykRdLQiajMyFBeijDTuL9Z1dm-vA-thByY6Yav3NjKb_-oDFSM4pG5f2IO6UtCiaCGD_WXHiJECJNxktJj6GnZ-H6fc-aqR-sqKEJMpiy12TOEm-iYUALSTlSqfDg8sod_cOp6vZOpJfe96r3WZiVtbf6fmWATUcKVeOffzE8015AdfSFHRSKgKvL4OL7igPdaVGSIFYvZVQ32zhniKBhiRNAHXK82E9Ui7a7hK51z9hQjQiC9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4612523b.mp4?token=r_uomK86Zi0deK7VBWdKlQVLM8Gu3j-Ys-JfkJg9uKBKYUKjzfY4N9LT-4CWhwzphJzpQNSlxk3xnZmVrMJRFldVo5xP_-1-meNykRdLQiajMyFBeijDTuL9Z1dm-vA-thByY6Yav3NjKb_-oDFSM4pG5f2IO6UtCiaCGD_WXHiJECJNxktJj6GnZ-H6fc-aqR-sqKEJMpiy12TOEm-iYUALSTlSqfDg8sod_cOp6vZOpJfe96r3WZiVtbf6fmWATUcKVeOffzE8015AdfSFHRSKgKvL4OL7igPdaVGSIFYvZVQ32zhniKBhiRNAHXK82E9Ui7a7hK51z9hQjQiC9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله اعرافی: ملت ما پای انتقام خون امام شهید ایستاده‌اند  @Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/457066" target="_blank">📅 21:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457065">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb83c53a3.mp4?token=HJOLfYcSOfMDsuAx7Na_2yDqPbFUoPpdlUzTtImqdb4SyfDjGX97ugPRuCE60DGNIszD2F_qJLJnSrnWSdd1eVDJAlohaDyAbxs9oe9A5qE9H8Io2HhcVq3MUA4izI-TZp34L5RPPQTyTF9DeMwLl2Q04_xtcOe6uWQN4GqZtKyeZNKJduunQUSvju556keB0j1rHkH50N22IuBejZlNYcPOTnLtAsXvfDaFdQE0MOVi7aXD1TCmnk3RKUKpcuVa9dyAbQXINq3F1MV9bLV8HkhBHfLHEWRRMgPpmWFDYDboPqZJejTuUJoBo5q-wLePVBBVOO3DWrJ8geTDj6cXGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb83c53a3.mp4?token=HJOLfYcSOfMDsuAx7Na_2yDqPbFUoPpdlUzTtImqdb4SyfDjGX97ugPRuCE60DGNIszD2F_qJLJnSrnWSdd1eVDJAlohaDyAbxs9oe9A5qE9H8Io2HhcVq3MUA4izI-TZp34L5RPPQTyTF9DeMwLl2Q04_xtcOe6uWQN4GqZtKyeZNKJduunQUSvju556keB0j1rHkH50N22IuBejZlNYcPOTnLtAsXvfDaFdQE0MOVi7aXD1TCmnk3RKUKpcuVa9dyAbQXINq3F1MV9bLV8HkhBHfLHEWRRMgPpmWFDYDboPqZJejTuUJoBo5q-wLePVBBVOO3DWrJ8geTDj6cXGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل سوم پرسپولیس به استقلال خوزستان توسط سرگیف در دقیقۀ ۴۸
⚽️
پرسپولیس ۳ - ۰ استقلال خوزستان @Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/457065" target="_blank">📅 21:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457064">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/780459cb40.mp4?token=qOPAuv0XyUZyWY4_WH22gKngAAHC5XRf7_ZTQM1OkIKc18oYsczqWY-FMLWgBytDyeH1rLJINgYk_zC8QYKvXTSO3voVQDXixQ1D-bzJTTZ49y1CK8G8auMmXhhQC_ivNU0iWRonfFE0j8HDrZYydWK9qVyBHEqO9W4IlxP-uIDKwzGDacdCtrBZSo4fib1HKNbr0rYpAm-Xk-rBD9IwARCIIAPeanByOD-VUeqRw5zFO6mNt66P2iD1cPMpXDYPC4RqXgjt9wXURhmj9qfj73jJh9Bt7BFdP3wOcoxJwV--jBVHx08QAsDnpKTA-LfetsMaunjouZvEwYLiS8yJ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/780459cb40.mp4?token=qOPAuv0XyUZyWY4_WH22gKngAAHC5XRf7_ZTQM1OkIKc18oYsczqWY-FMLWgBytDyeH1rLJINgYk_zC8QYKvXTSO3voVQDXixQ1D-bzJTTZ49y1CK8G8auMmXhhQC_ivNU0iWRonfFE0j8HDrZYydWK9qVyBHEqO9W4IlxP-uIDKwzGDacdCtrBZSo4fib1HKNbr0rYpAm-Xk-rBD9IwARCIIAPeanByOD-VUeqRw5zFO6mNt66P2iD1cPMpXDYPC4RqXgjt9wXURhmj9qfj73jJh9Bt7BFdP3wOcoxJwV--jBVHx08QAsDnpKTA-LfetsMaunjouZvEwYLiS8yJ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در نشست پزشکیان با زنان فعال و صاحب‌نظر چه گذشت؟
@Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/457064" target="_blank">📅 20:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457063">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9565c277.mp4?token=XC5BUpfS2f0PI7x3i1Vqg0jXQ8mB0vRt9IiX3-nwBv94CmXqlsWC_2y9E2j-xClCBVGaMP7GxnhlpoDWI9uaY60Ys7YwJ3o54nUOSD_hb1N0x61neCFFKbEC2z3RENYdBVN82NbooR8ckEQS52r9GVrzWf9Ji-dztw95c6-t4ewcmZLMUhtg7npatpFkF3OkUEZRmMcb3C1PaoEk6xisx5ivbo26TT4Uj0CosTl7dNp1-ZxgoOkjviiXcFZLhTkFvMkLEWRNCPM_aU40Qt4_ViZtPjcnd0MtNlT6WW7H1qGrOK3FdJm3Nw-EG1Mzc0reyC4BLHBfwi3IXbV7R3nG5r4um9oOfocWfUuEqoUuHB20oeMjz08yxIw9YaqMnFnWdHyO_4e8NXaj6dN5jJWjc6x66DHhBUg9FDIcwm7MuK4oVDm88D33CPdExwcQPLWK4gE9IaycRnsJGdoC0jY_v-Fx--kS2bq8O771MxXdUFqlXPkrZv6lbz0eXxTrd6W5xWS0EeBrpGhlyL2FMEaORwEKUi4t6nPwBrtwvfEMUi9P5cycWPaMGLY5Dej72mWCJWOVmV9dbWiYaJUqig1GhX0ggkL63yhhXS8UGFzNLxZWoiFeOwRXUI_CYSR8rJOaK9YnIbhH04ENgGcboW_VhhLw_2ZRCm-GjGfZJZKXmKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9565c277.mp4?token=XC5BUpfS2f0PI7x3i1Vqg0jXQ8mB0vRt9IiX3-nwBv94CmXqlsWC_2y9E2j-xClCBVGaMP7GxnhlpoDWI9uaY60Ys7YwJ3o54nUOSD_hb1N0x61neCFFKbEC2z3RENYdBVN82NbooR8ckEQS52r9GVrzWf9Ji-dztw95c6-t4ewcmZLMUhtg7npatpFkF3OkUEZRmMcb3C1PaoEk6xisx5ivbo26TT4Uj0CosTl7dNp1-ZxgoOkjviiXcFZLhTkFvMkLEWRNCPM_aU40Qt4_ViZtPjcnd0MtNlT6WW7H1qGrOK3FdJm3Nw-EG1Mzc0reyC4BLHBfwi3IXbV7R3nG5r4um9oOfocWfUuEqoUuHB20oeMjz08yxIw9YaqMnFnWdHyO_4e8NXaj6dN5jJWjc6x66DHhBUg9FDIcwm7MuK4oVDm88D33CPdExwcQPLWK4gE9IaycRnsJGdoC0jY_v-Fx--kS2bq8O771MxXdUFqlXPkrZv6lbz0eXxTrd6W5xWS0EeBrpGhlyL2FMEaORwEKUi4t6nPwBrtwvfEMUi9P5cycWPaMGLY5Dej72mWCJWOVmV9dbWiYaJUqig1GhX0ggkL63yhhXS8UGFzNLxZWoiFeOwRXUI_CYSR8rJOaK9YnIbhH04ENgGcboW_VhhLw_2ZRCm-GjGfZJZKXmKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲ کودتا با یک الگوی آمریکایی
@Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/457063" target="_blank">📅 20:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457062">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJkjaTCIU_G8q8J4zWFzfsZblCcCdsIRGv8HXfxr06XxEpOv2k2CCb8ws9LyB9zhsEp8ecaWcPBhknwrF3qGjZpiMvv97RAZFYuElu9Rpa1iMzDjWLQK5CGeIAjADJGeXIKFRS9b1rvFZ1qWO58mbRWjb-lCJMpKzpsuJDMkuaTI8MbGQbNsmJ7kbvNKau_hRNE6LfRAPaBybsuu6VKxFOdy3YHAtObQ_MPLwxT83fFVLf7jRUXxGwh3Q8aOrT2FY0pP4SaVOXsteHtt375z03bm8xuudWamtMRtjaxD5LEve9Q4igov0_xsmamS0wxs3XQvvfhQBWVMNMrdiBPgEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود ۲ دیپلمات فرانسوی به ایران ممنوع شد
🔹
وزارت امورخارجه: با توجه به فعالیت‌های خلاف حقوق بین‌الملل ازسوی ۲ مامور شاغل در سفارت فرانسه در تهران، وزارت خارجه این ۲ مأمور را به‌عنوان عنصر نامطلوب می‌شناسد و ورود آن‌ها به ایران ممنوع خواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/457062" target="_blank">📅 20:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457061">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f9c60ed1.mp4?token=ScsJGXbru1oFBTHZVvmCUaPyBSeXRx4iTZAQ3CoKwmkfNlVlBxXKJTLMKj2MITLzZLI2lsrae1YvIqToW5Vwof8GT_a0u8c0PGmXB24u4KZFWqepUErbhEGnXy92hiysjJKHKX8B0zdJWVAvZpkkcQNpLi996KBe1t8fFAmpmW7fO7aNGzHDdIB-WVQ9rZbgvB5RIBdyWwVgsnPXRpKWLjYoftSAOoxaFG_KctweKO_2lCH1-OygbKFxwXmxHTXb4G_zDuR8euEBdcFkKK30GE0OnZ5xdBUwOA0BV3bkhGptgYg_m_A2DRHHBZQ0odSc_0cBizjhxbwGBKMkwA6LnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f9c60ed1.mp4?token=ScsJGXbru1oFBTHZVvmCUaPyBSeXRx4iTZAQ3CoKwmkfNlVlBxXKJTLMKj2MITLzZLI2lsrae1YvIqToW5Vwof8GT_a0u8c0PGmXB24u4KZFWqepUErbhEGnXy92hiysjJKHKX8B0zdJWVAvZpkkcQNpLi996KBe1t8fFAmpmW7fO7aNGzHDdIB-WVQ9rZbgvB5RIBdyWwVgsnPXRpKWLjYoftSAOoxaFG_KctweKO_2lCH1-OygbKFxwXmxHTXb4G_zDuR8euEBdcFkKK30GE0OnZ5xdBUwOA0BV3bkhGptgYg_m_A2DRHHBZQ0odSc_0cBizjhxbwGBKMkwA6LnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این بازی‌ها یعنی کودک‌تان اضطراب دارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/457061" target="_blank">📅 20:46 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457060">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57af079833.mp4?token=B5Re-esZuMdYcZy6p6PEA4nUSouRLjdjUCivtfnnaIBDM_4fH08ygSVv14Mf6j7JJZ0w1Sk4n5-rwvCxlnLtt82n1-0xovKYBgkopdUe6e5GIJq36K9Gxii-WSchjI4Ndviqr5mSZcqyNymRdxmi3lm9ITgrwlsfPKd65nyCXSi8x58GTYCRJfk8ZS3YzBzupItGh89uU_kfJ8yhd1b4alKbMpOMqQ1AASxZWnNOhKx8RNk25PPXCpIYFYzXkQIx8jVzc_9KagFpRCgMdW8AyPyN8Cmw7sDJz3UQtsAUPl5AkzT6btXRnd4ORJKik_haYz19UeN0MG8yr7VyjPUcFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57af079833.mp4?token=B5Re-esZuMdYcZy6p6PEA4nUSouRLjdjUCivtfnnaIBDM_4fH08ygSVv14Mf6j7JJZ0w1Sk4n5-rwvCxlnLtt82n1-0xovKYBgkopdUe6e5GIJq36K9Gxii-WSchjI4Ndviqr5mSZcqyNymRdxmi3lm9ITgrwlsfPKd65nyCXSi8x58GTYCRJfk8ZS3YzBzupItGh89uU_kfJ8yhd1b4alKbMpOMqQ1AASxZWnNOhKx8RNk25PPXCpIYFYzXkQIx8jVzc_9KagFpRCgMdW8AyPyN8Cmw7sDJz3UQtsAUPl5AkzT6btXRnd4ORJKik_haYz19UeN0MG8yr7VyjPUcFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم پرسپولیس به استقلال خوزستان توسط علیپور در دقیقۀ ۲۰
⚽️
پرسپولیس ۲ - ۰ استقلال خوزستان @Farsna</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/457060" target="_blank">📅 20:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457059">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8c87ecb9d.mp4?token=gkjguMHsoqc-D9brl7pcc2eCwKo_NSI4c_1uq2BN0MpcbAKqqer0C7XBDYFTZTBe6B0wnH5q1LbOQi8ah8n4qewxbk9tKCd1xTZCik-VFlVqJ1rYJgKgdPe68RMzoM17n5YSTMILPuN7efDqRWJtXPOTEcopVIzq2oz930sX1bDETNFoDiuEQKmRULUir6a_QYXAJfNBwAmIuRycAKNxfG0TobIPbsR6cdaXBikkemRC0-jp7VXrBBzAHp22rARJXCw5bj8HAjhSMIV9rXdMkm4-Ux2GgBwAuzMgQgzJSi_gfiSr8r-HZOMtrYpH3e9h6HN9NLlmkRHXt5-SX7rwnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8c87ecb9d.mp4?token=gkjguMHsoqc-D9brl7pcc2eCwKo_NSI4c_1uq2BN0MpcbAKqqer0C7XBDYFTZTBe6B0wnH5q1LbOQi8ah8n4qewxbk9tKCd1xTZCik-VFlVqJ1rYJgKgdPe68RMzoM17n5YSTMILPuN7efDqRWJtXPOTEcopVIzq2oz930sX1bDETNFoDiuEQKmRULUir6a_QYXAJfNBwAmIuRycAKNxfG0TobIPbsR6cdaXBikkemRC0-jp7VXrBBzAHp22rARJXCw5bj8HAjhSMIV9rXdMkm4-Ux2GgBwAuzMgQgzJSi_gfiSr8r-HZOMtrYpH3e9h6HN9NLlmkRHXt5-SX7rwnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت‌هایی شنیدنی از زمان‌هایی که دعا به استجابت می‌رسد
برشی از سخنان حجت‌الاسلام میرهاشم حسینی در برنامۀ سمت خدا
@Farsna</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/457059" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457058">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyzgooHbNgOpPCXqQTTtYcH6om2tUDJE90Z-htzY8zTCVtHYxEE3IKeGkasBk0p3T-cqL5kTiQruldBRYO0KkBLfptpgcrr3tXztvX7ds3t2ui3vcIMiZN22vKskChmxSBRKhu04oNzLfBaT6qBKLrOGJzG6Dux8AUQEAe_C_WdfN7fI1XutrlQUbuQCyQdINTjvqiJcR9a9ZX_k9KO6JEVjBaitrp6vVlNBBQ9q2Y0-rJMBtePze_XNTHa-5kA9n5E8K9rgLrFVAI_AeyOjld3CBWP90W6M2KDAQHPYUiOKO974D2Zq9Bo5If7y4lXKIUyimE4oBE13G_-ziPMeRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد قیمت سوخت پیشران اقتصاد آمریکا شکست
🔹
فایننشال تایمز: قیمت گازوئیل که مانند خون در رگ‌های اقتصاد آمریکاست در جایگاه‌های سوخت این کشور رکورد شکسته و به ۵.۴۷ دلار به ازای هر گالن رسیده است.
🔹
آمارهای جدید نشان می‌دهد که «کرک اسپرد» یعنی فاصله قیمتی گازوئیل و نفت خام در آمریکا هم برای اولین‌بار در تاریخ به ۱۰۲.۲۰ دلار رسیده است.
🔹
افزایش قیمت گازوئیل در آمریکا پس از جنگ علیه ایران شروع شد و ادامه دارد؛ متوسط قیمت این سوخت موتور محرک اقتصاد آمریکا در سال گذشته ۳.۶۹ دلار در هر گالن بوده و حالا ۴۹ درصد گران‌تر شده است.
🔹
۸ ایالت آمریکا بزرگ آمریکا که قطب کشاورزی و صنعت هستند وابستگی شدیدی به حمل‌ونقل دارند؛ این جهش قیمت، هزینه‌های کامیون‌داران و کشاورزان را بالا می‌برد و دوباره تورم را شعله‌ور می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/457058" target="_blank">📅 20:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457057">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40204522b.mp4?token=dgGOEB5rsRvAM2lYBKlKbhhdeBOiEd0RTXPMuAlQ9ovSkaI-ul2cFEwoAdj_ivZSjpidPkBdf1APJybvO_xhRKAHE2B2IryJSky7CEIXexlSRrJiSEeVBKk1jjsqPPPG8wATQqXY4c8ivXzhaS3iDl9Lszd2PoWUxlo_xtsDWY0dv0by1Z2qUmbwPM_L124RDCD8I_cbKYLqL-92mcP9m1T5Z_insnDpSsm_Qm6OSi84sqCkRLGDmC6gQyyaVcRqMlrO_4Exdt9yPCzcku2w4RFEmyd76TpMpWDnMI6Z6D7ijQlcfi83i7T7qmW1s8eSm9FtIPyYw89UQ3LsND1JpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40204522b.mp4?token=dgGOEB5rsRvAM2lYBKlKbhhdeBOiEd0RTXPMuAlQ9ovSkaI-ul2cFEwoAdj_ivZSjpidPkBdf1APJybvO_xhRKAHE2B2IryJSky7CEIXexlSRrJiSEeVBKk1jjsqPPPG8wATQqXY4c8ivXzhaS3iDl9Lszd2PoWUxlo_xtsDWY0dv0by1Z2qUmbwPM_L124RDCD8I_cbKYLqL-92mcP9m1T5Z_insnDpSsm_Qm6OSi84sqCkRLGDmC6gQyyaVcRqMlrO_4Exdt9yPCzcku2w4RFEmyd76TpMpWDnMI6Z6D7ijQlcfi83i7T7qmW1s8eSm9FtIPyYw89UQ3LsND1JpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سیدهاشم حیدری دبیرکل جنبش عهدالله عراق در مراسم چهلمین روز تشییع رهبر شهید در حرم حضرت معصومه(س)
@Farsna</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/457057" target="_blank">📅 20:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457056">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df2fc0de27.mp4?token=OJ5cYBGHGv7ndA792njjcOEuTsSgXtWSVk8G7Qu95Zi9HfKyHKLeM-zqWEYdtxZm7QenI0aQTPWmXi4o-IJWdCBqVbfrLJG2Yu1aWMuEUrJP1b70tuoBK-Ka7kiYXLVqZXF4C_Y2uYDj2wI7mx5J5TeDG5RsA5OPhba9421KSov9YNem3ETXFsE84I4UJWZ_kBI82xtfwgGqRNa-opyKNKa3AF_E8TQxXn1b5pLfyQAeeyNZ1F12rVqa4-nLGqjtVUapHKOO_Bq06Dg9J-_EN_EYyw5szNF6OF6hb37jhWo3C_qVnngluHaQF16UVvv_BssD8Tmdl6t5JDC39g5NGiWSTDgkd_0wqEy_DxQbWnxMSGrgRQFKRrSIjKmeVPLThSDVvE1psiWB3MxbXXkULuu52Yao0fEx6MO5qB-rTvw-Xs9Ck5wGW8ePIV-fv20ZamX7u1SOhhMraC5z8-8oPBsEUNsSTcP0GoUrPasMrMV-OEIuvNTQWHYR1cGBUAJ2EbX7JM5DEDzDAAMEf5KKSenBGaGJDor6peR30h5iyra7KA0pVvgLX1L4QAWoR-Z8_DELfcQP-7GKsvl4fY8b89eQNJSxrewPQq-bB09zSYVZD2RGtQ3wamPdxumt901_go2NW8npdaAwBTEfjm61tPcrtIg5gTg9HJsJ6s0A5WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df2fc0de27.mp4?token=OJ5cYBGHGv7ndA792njjcOEuTsSgXtWSVk8G7Qu95Zi9HfKyHKLeM-zqWEYdtxZm7QenI0aQTPWmXi4o-IJWdCBqVbfrLJG2Yu1aWMuEUrJP1b70tuoBK-Ka7kiYXLVqZXF4C_Y2uYDj2wI7mx5J5TeDG5RsA5OPhba9421KSov9YNem3ETXFsE84I4UJWZ_kBI82xtfwgGqRNa-opyKNKa3AF_E8TQxXn1b5pLfyQAeeyNZ1F12rVqa4-nLGqjtVUapHKOO_Bq06Dg9J-_EN_EYyw5szNF6OF6hb37jhWo3C_qVnngluHaQF16UVvv_BssD8Tmdl6t5JDC39g5NGiWSTDgkd_0wqEy_DxQbWnxMSGrgRQFKRrSIjKmeVPLThSDVvE1psiWB3MxbXXkULuu52Yao0fEx6MO5qB-rTvw-Xs9Ck5wGW8ePIV-fv20ZamX7u1SOhhMraC5z8-8oPBsEUNsSTcP0GoUrPasMrMV-OEIuvNTQWHYR1cGBUAJ2EbX7JM5DEDzDAAMEf5KKSenBGaGJDor6peR30h5iyra7KA0pVvgLX1L4QAWoR-Z8_DELfcQP-7GKsvl4fY8b89eQNJSxrewPQq-bB09zSYVZD2RGtQ3wamPdxumt901_go2NW8npdaAwBTEfjm61tPcrtIg5gTg9HJsJ6s0A5WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین شعار «الله اکبر» و «مرگ بر آمریکا» در مراسم بزرگداشت چهلم «آقای شهید ایران» در حرم حضرت معصومه(س)  @Farsna</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/457056" target="_blank">📅 20:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457055">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c4502fdbd.mp4?token=C9womxQCnemCrR6q3SklvUiWnlaJhh4XQMwoDA1La-YPyAlD0cSl1P5w20mZPVoVCwab7PB28ojXx2BLIlJkkM58esyvMT1tEeL05eyI21bcnS3Klf5y0fYyRwmNTpqpolKvSXivHb7wSYVsKB4khjHeqIgWLzQQ4xG6QL4dBhMILtf3dWtxsE8nArPmbBFxHlAhBxCvpwjPc605xD42Sa12pqnvlQ9_VRFUnj_fh9E40w4lDvJM9hIRQ_TYEzsBy6a5_cejnuGJKnnmbsnb6wySf_Y2kHSFGBnzTB7GJensTJcgj9MXbX6O50HWYoi5D5CpVXFH9X3tM9oSuHVtOYz0SpYDnP9OGa3Qs_0hUC_JDe-3wBwc9EDPaPWIXzNzOIORm8L6Aa6-R1PAbpMqgLB_cI4sKdVD2rHzphxAY7pysVpkhImBYefC9MtCQTZ2m0Hy9R81W354wErHoUG5a7Yk_MFWfF2wpqPgMdYy0hDtECyj_sBzZqFDYd9MyKI2szdCaOXecJB291kEzgAOHpXE8D53cBFttgZhFpfP7CeMjEqyI-3XN09-tgIhouPVBoqqpFdfPeZ9hbm7Cy5PWJFFNNHA76LG30Xrn3GBiBebVGQUyrgqgWAoGldezKsHBCniAw7eyJuqEKi9mBCEXa4x2g8tjt10BVOT_b9fizM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c4502fdbd.mp4?token=C9womxQCnemCrR6q3SklvUiWnlaJhh4XQMwoDA1La-YPyAlD0cSl1P5w20mZPVoVCwab7PB28ojXx2BLIlJkkM58esyvMT1tEeL05eyI21bcnS3Klf5y0fYyRwmNTpqpolKvSXivHb7wSYVsKB4khjHeqIgWLzQQ4xG6QL4dBhMILtf3dWtxsE8nArPmbBFxHlAhBxCvpwjPc605xD42Sa12pqnvlQ9_VRFUnj_fh9E40w4lDvJM9hIRQ_TYEzsBy6a5_cejnuGJKnnmbsnb6wySf_Y2kHSFGBnzTB7GJensTJcgj9MXbX6O50HWYoi5D5CpVXFH9X3tM9oSuHVtOYz0SpYDnP9OGa3Qs_0hUC_JDe-3wBwc9EDPaPWIXzNzOIORm8L6Aa6-R1PAbpMqgLB_cI4sKdVD2rHzphxAY7pysVpkhImBYefC9MtCQTZ2m0Hy9R81W354wErHoUG5a7Yk_MFWfF2wpqPgMdYy0hDtECyj_sBzZqFDYd9MyKI2szdCaOXecJB291kEzgAOHpXE8D53cBFttgZhFpfP7CeMjEqyI-3XN09-tgIhouPVBoqqpFdfPeZ9hbm7Cy5PWJFFNNHA76LG30Xrn3GBiBebVGQUyrgqgWAoGldezKsHBCniAw7eyJuqEKi9mBCEXa4x2g8tjt10BVOT_b9fizM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گردن‌کشی یک مونتاژکار مقابل دستور قضایی
🔹
پس از انجام برخی اقدامات و تغییر کاربری غیرمجاز از سوی گروه صنعتی بهمن در یک محدوده ۱۲۰ هکتاری کشاورزی در منطقه روستای دانش شهرستان قدس و حریم منطقه ۱۸ شهرداری تهران، با دستور دادستان شهرستان قدس عوامل جهاد کشاورزی…</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/457055" target="_blank">📅 20:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457054">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8df437fbc7.mp4?token=rZWM7JRtlGJnxwIs14a1ejugOM_3iG6GQprWebyfcfDXunZpbHcN28IsHcOjtmpOZuJfkS3v7esV0IrfI9e4S8EqjRcM-3lzJ52eY3i0AdfYC3w_58rrddCI_udbu3niDIQMEmKnEXMivpj0mNobKpbMmIG9-Zc47gE1mBnV7NKleZdnU9nJROQ5i2wAeh_jRIeueuwuo5J8gqOyjdSA648n8Tda0PPb37IHeiy2joJwmgHAAa_pL1P3QBCONFQxm-i1_qKyyFZyfgNh-gGTGReLwGc8rd-goUjwG9f1QYnqfV5v1Qicl3QMEoSNp42fLR4HSw3x8GuIHEren_GvBD2ytKIb29St0NPVEqPrcenZyEYYmIWv2UQBKlbFjHHRd2JzxrjNU08LwMjZLGd8CnPSFOXTucwk8wDZ8d2Ix8pknkKFiqMVocOdVtlnFjCr_nxyZFgGW7EuC1c6NHF9g5Hx0SBWqBNBQ9ui298rPLr4WduH2Pvc8lWjYZCNDABNwL2bu9xFXm6j8rQ8zPqfY0wJxfTZS7d9ZQ71EeFUppfm-skoeoxp_fbgjhXlEesS6ynb_WJkZQHBb69AjX_ZjboDj9KA0XL4yF0IJWihrQACFXr5MZeGeH5j-2pSw7znH-lDXbTu5nVt_cS0n8qug_ELlta2AaPvKoeenGux1xY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8df437fbc7.mp4?token=rZWM7JRtlGJnxwIs14a1ejugOM_3iG6GQprWebyfcfDXunZpbHcN28IsHcOjtmpOZuJfkS3v7esV0IrfI9e4S8EqjRcM-3lzJ52eY3i0AdfYC3w_58rrddCI_udbu3niDIQMEmKnEXMivpj0mNobKpbMmIG9-Zc47gE1mBnV7NKleZdnU9nJROQ5i2wAeh_jRIeueuwuo5J8gqOyjdSA648n8Tda0PPb37IHeiy2joJwmgHAAa_pL1P3QBCONFQxm-i1_qKyyFZyfgNh-gGTGReLwGc8rd-goUjwG9f1QYnqfV5v1Qicl3QMEoSNp42fLR4HSw3x8GuIHEren_GvBD2ytKIb29St0NPVEqPrcenZyEYYmIWv2UQBKlbFjHHRd2JzxrjNU08LwMjZLGd8CnPSFOXTucwk8wDZ8d2Ix8pknkKFiqMVocOdVtlnFjCr_nxyZFgGW7EuC1c6NHF9g5Hx0SBWqBNBQ9ui298rPLr4WduH2Pvc8lWjYZCNDABNwL2bu9xFXm6j8rQ8zPqfY0wJxfTZS7d9ZQ71EeFUppfm-skoeoxp_fbgjhXlEesS6ynb_WJkZQHBb69AjX_ZjboDj9KA0XL4yF0IJWihrQACFXr5MZeGeH5j-2pSw7znH-lDXbTu5nVt_cS0n8qug_ELlta2AaPvKoeenGux1xY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین شعار «الله اکبر» و «مرگ بر آمریکا» در مراسم بزرگداشت چهلم «آقای شهید ایران» در حرم حضرت معصومه(س)
@Farsna</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/457054" target="_blank">📅 20:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457053">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43389d44f7.mp4?token=eL4Q5-LDWhri3GpONdrVpnAZJfM6gt33cIz61By5cycSonAh0In7N3tsNF6dUUwA0Ku91b8Q7T8p5uC1hXu88MSI0lXVlF5Qy0_lioi6HxDLNE_dwlozKgq3r8M-ThrhrM6H5K6rddDsDOhH9QPtuevHEM_U1yrbEY3nGjJK0bhowp0ouROy9DvSdVf2pKjJxC9eE7jSTIhF_DOxmaJvjhU6x4VZnUqTE6JDYDFQSk2lfBEs-OeK-cymN9EqL-uCcwcr5wz7PrnbqDpVvmDW2gnPkoD9HYrg43PvN7jO8oN7_Hz92mHKBODJWcpVvUzUcfb9hICZTp7DgTzHKc6BxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43389d44f7.mp4?token=eL4Q5-LDWhri3GpONdrVpnAZJfM6gt33cIz61By5cycSonAh0In7N3tsNF6dUUwA0Ku91b8Q7T8p5uC1hXu88MSI0lXVlF5Qy0_lioi6HxDLNE_dwlozKgq3r8M-ThrhrM6H5K6rddDsDOhH9QPtuevHEM_U1yrbEY3nGjJK0bhowp0ouROy9DvSdVf2pKjJxC9eE7jSTIhF_DOxmaJvjhU6x4VZnUqTE6JDYDFQSk2lfBEs-OeK-cymN9EqL-uCcwcr5wz7PrnbqDpVvmDW2gnPkoD9HYrg43PvN7jO8oN7_Hz92mHKBODJWcpVvUzUcfb9hICZTp7DgTzHKc6BxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صمت: رئیس‌جمهور تکلیف کردند که برق صنایع قطع نشود  @Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/457053" target="_blank">📅 20:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457052">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfffd7c1ce.mp4?token=aPkvSR1LRrs9Q2Sk-T5rroUbs-NE03t-AImvVDWI7izOnQQNLLuCIlJVQOjrK2Clug6YA6eAkzdvDMW1yas503oFdE53EiNqPHFvdRCe7ffs0UNG6x6sf0dGLpPkJO6zkn3XQt2Nwj3InMC84uXswcsufSM7m3_3P_J-w9nrtM7lMwFZRhHVFgTfW77VUr_ypkDxyDH_RPzBrVdo_YE0qkYSya__IIbhY0DSMPvlUjSTV-kYu7SStE22TQLkeue0ZRUjWzmT4rR-r3D0U4lTjOVAzIFAv3-IYmZE--6zJXZNYk_E2f5-YhN0H2_1bz58lj-DMJ4UNRQSIlEqnHPJiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfffd7c1ce.mp4?token=aPkvSR1LRrs9Q2Sk-T5rroUbs-NE03t-AImvVDWI7izOnQQNLLuCIlJVQOjrK2Clug6YA6eAkzdvDMW1yas503oFdE53EiNqPHFvdRCe7ffs0UNG6x6sf0dGLpPkJO6zkn3XQt2Nwj3InMC84uXswcsufSM7m3_3P_J-w9nrtM7lMwFZRhHVFgTfW77VUr_ypkDxyDH_RPzBrVdo_YE0qkYSya__IIbhY0DSMPvlUjSTV-kYu7SStE22TQLkeue0ZRUjWzmT4rR-r3D0U4lTjOVAzIFAv3-IYmZE--6zJXZNYk_E2f5-YhN0H2_1bz58lj-DMJ4UNRQSIlEqnHPJiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس به استقلال خوزستان توسط خدابنده‌لو در دقیقۀ ۶
⚽️
پرسپولیس ۱ - ۰ استقلال خوزستان @Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/457052" target="_blank">📅 19:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457051">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4f517fbb.mp4?token=vNP1RAZX1x0lNd-6HcYKJXSauRXaJ0K_kJg7twTDDS2pR17rMwYDbLRdz1rYmfKxsiGRhZ2n5WiLc1a2dtkoxQ7HDwicAikkSk3cMjb3cKGP69JKvXOe7cMBDgoA259oACYog0EV2d3LM-3TGoaoaPNYzuLWHX1rXw_uCqohMdLz6_ebyyNPlNdHJ13RqKiBVTQS5FQw_qVyghHbVUVORSI4TjJcSdTdKt6vvj3jX8KXlzD3yVFgyzBHXsLjceW4QkGJRCA-qbtAPAjj9-a3ys0xA0f2LY6Cg91Kq5XXLvHsOY2UlBxIjO7kMOpTUMl9ia90EiwKcKcLyU5iUjop2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4f517fbb.mp4?token=vNP1RAZX1x0lNd-6HcYKJXSauRXaJ0K_kJg7twTDDS2pR17rMwYDbLRdz1rYmfKxsiGRhZ2n5WiLc1a2dtkoxQ7HDwicAikkSk3cMjb3cKGP69JKvXOe7cMBDgoA259oACYog0EV2d3LM-3TGoaoaPNYzuLWHX1rXw_uCqohMdLz6_ebyyNPlNdHJ13RqKiBVTQS5FQw_qVyghHbVUVORSI4TjJcSdTdKt6vvj3jX8KXlzD3yVFgyzBHXsLjceW4QkGJRCA-qbtAPAjj9-a3ys0xA0f2LY6Cg91Kq5XXLvHsOY2UlBxIjO7kMOpTUMl9ia90EiwKcKcLyU5iUjop2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صمت: سند آیین‌نامهٔ ساماندهی خودرو در دولت چهاردهم تصویب شد  @Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/457051" target="_blank">📅 19:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457049">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ebe804d25.mp4?token=tmAUme6FpFETl5ZeJr3wopMT8CV_aH0-DwWubounSfYYXb4zgW5bMKI7cxpng02wKD1RqGqZjO6tnhvTvNSOL5Mz6UX8Dp6aAHYD3tMIBMKDl5FErqtGUr7heKf1m-6Y818uStNIkja5hx_xFSqUBrLjBWjNu9in5T1AeRpEnjli6t722JyRr2duEp1Ib5YBLtDhkOy0nvl8v_HB5zwLVu6bEKGhOhnTAbjzTS-jc-HQZc1juKC6D8IMhHN_uzU3iqZv3sYYjb3zKkpxCaY-OFN6gXraR4Cg0z2fSOL_4W5UfkiOMCCGx8Dj-cr_m1HmQMXxGpmI-HidpoH47ZcDHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ebe804d25.mp4?token=tmAUme6FpFETl5ZeJr3wopMT8CV_aH0-DwWubounSfYYXb4zgW5bMKI7cxpng02wKD1RqGqZjO6tnhvTvNSOL5Mz6UX8Dp6aAHYD3tMIBMKDl5FErqtGUr7heKf1m-6Y818uStNIkja5hx_xFSqUBrLjBWjNu9in5T1AeRpEnjli6t722JyRr2duEp1Ib5YBLtDhkOy0nvl8v_HB5zwLVu6bEKGhOhnTAbjzTS-jc-HQZc1juKC6D8IMhHN_uzU3iqZv3sYYjb3zKkpxCaY-OFN6gXraR4Cg0z2fSOL_4W5UfkiOMCCGx8Dj-cr_m1HmQMXxGpmI-HidpoH47ZcDHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس به استقلال خوزستان توسط خدابنده‌لو در دقیقۀ ۶
⚽️
پرسپولیس ۱ - ۰ استقلال خوزستان
@Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/457049" target="_blank">📅 19:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457042">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RrrFouGc0tTRgGGqKSXD-4GdALtrjS9xLE1NHCk9sPCP5XM2essUdGUgpI-22rb-lQIx2IFZx_dxOz_TiyZ6KRcMetTp68LZX_9DZGl0rnLGnuZYWMOQDQDZ6pIbrn3mLP581yPGycqXOELsPyyvA6TdmRnwfDcI3isC63-TKYe9e0Crv_bzQsqR4gfBX9pvw6uALrWo8BQU4oK60z6ISWQkZrsXuvYnKC7k4MLJeGLeTpzRC9M0Qq4-QpfHbC_QTZ6YIGFJQ67dOPiM-FL2AC8-WYOT-OrFz9R30DOpM8tRSuHo6E3FtY35jQdD4C7Z2FDISVefC6kOhoNQeHzjHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/geX15_yNpVgt7TfY0BeJxg5-bLB3ckeIsFdCd7QtVTRZjA9D7ktLF6ZDi_zfekO-Gd65l9kF_XYo7TUbZOWFLkoAJdfIJs9cGzMYPeS_9ihlODt-C278f7sWpmJQI7fZLmxvkQJBpDN0um6AG_Fegeh84Iob3SNNXCoF-RgUP-TEhGkZg5oSSnM4SWwzFdnZFsjAaXG4I--5PZhlKCLVS29q85NwjqG_XSPSuS4gbKuF4cdamDvAJByOBqsSHwnfqZSRRXCzvfSkGCWNMUn-1LfYAsac3nEpYVUOTcIwlFMd6hbwaAWAshFM8z-iosxr0lF3JJWllTu1YeZ6ISseQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1zasdxm7JEKUAIGdwEnMvu7cFYsD6OS5gviDjQgGWVzpBw416JVm7XO8qSsghYkg0f7RkZfaGl30xxc7krRUnM1u-5bAjCxgsNHKNJkzptXvp8SAE5ZtZM3nktaz-LZF2cHm-esxj1Xn7PiCHh9fLyVG1xeRazWdAbZu-qWdCeN1i-Mq7VcpOhTPMDBTMYB1GxNGRgZfqLgy-Okud34Dm77g3nkXuj94aTyvF3fSFBXfi0pIgN9uGeIkVyE8VfMGM3qq_hnbb_UJLm3uu0thIWgOeb0HxAc05Y2jgZ2EXCZOOlzUyZhG3BgQiLmgFVyYEbVWvGwOHtSNQLidwZ9SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RVnugvAfH_B2fi_3nyxI0CjJ423uiOUaLGEdG8_gJHQYXLl9G34voxvMtIc7dekRSEtrmmO675RnBH8QV-NnpmwXjgTGmx-s_RCsvnuc5SDZcLAXXD65c-bhwUxdJTwIN9E0MLYiVrM0szrDBif8-pIMh5XpS2MvZ7EEaE4XuRZaDHZUUpfKAmtZvkk9qHCdFpKqrru7dq2R3B1A1GAbJvaRbzFp0dnhcSQcui_2bw5Yb9SKqzjqCE9qaCuR-HnCddR3l7SIXrWhfHiY-bRBN6a6W9q7nXwmqD91rh-m1jLBzkMCvQIU0Qk98VC3k6tvWfhXiTp-zOd1jhGUpXIp1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfFEAQIeiEeAC1x4HYDxn8kS2JREbq26tQwjlnGMDETBI6E-AMXivLGp5ugUFhUdffet0sRMAHaOysu-rQmTnNDtEtEdhMJw8hT302Ws5D3J3CPqC0vwL3ZodaiEjFNAJ-bKon_wn6n_aryyjWFDhzwavbv3PHGKeurf4tZ_aaWH4XeJ11AmRqQGhLjkPtRXrmFTsXCX4C0Ea5Ts46MsMfu-qupbLHDgS380eeOk0sQn6iMcFx_6juXVSx56vl7YnwkzLcAJVzQZBZLHKncAFMhfUXI48sxJifRdJQ7XJS88xZRaSdiL4xsfqH-tzw06EXkvHOj8RNSwWQCR858zhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjVryOV9qqKbJ8bCqGkvy_jzKsKHr0jERvBZOq622yQSlfKvhpu7Yma60L0pbMYdGXBH0YHEbURxLXJJBMrss8PILl6WUKP20tZ3OjZsiu3NedTAe_3fuhoPOgddhHvSb-XEBdkDs-hLSLTEWL-1SvaBi-A5sCdjL-x6UHfSL-seC4SXLngS2BXv2edslhsYKQazDpGReVLQdJ3oG-pQEVF5FuQ10WkDXVDoK_c25nuEITebKdtXms8O0zbsxtu7uui39bYDmPxSo3jOwjfNmPMcoh71Ztkv2oJeFfZYQZiY_wBi57QCXH6txQwGYGGp2tfE41Oj54y98zgE3FPIcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tTm7lpmqfCBbtsU1eglrSvxOVHeeE0aJF-KANwSGwPpfbfeJ342DnvsK3_0_ocLXcinwcn8cS-HfUJdMXp_2Zj2Y4Ycb83pjLNl8OwLvxcHpiZZXwpXDk_HLly7X8WtTchxvujL3TolHDnD_hxRppG7uZpZaqbochA5EhcbPen6cGd0O4ZyAWG6ErfALKN7j64_TPqVCckg3fxjSxU_-xQ3nBmaezbnNt9QEAKoV198EOSp-fGoZaHGlfP7gr8imZP7H_qVhge381gNfHtSgLoANFK4K3q5agAhM223VeSouthq2-GjRoAmYGr7Xw2p9OF_FNFbo6I95iIzNjOLQ8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زنان امدادگر در میدان تمرین
🔹
۱۲۰ امدادگر زن از سراسر کشور در یک تمرین عملیاتی در فارسانِ چهارمحال‌وبختیاری، مهارت‌های خود را برای روزهای بحرانی محک زدند.
عکس:
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/457042" target="_blank">📅 19:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457041">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d110f4cc.mp4?token=VxgmP784NrRMN66E6WI0K7sAZzOOYF1MqW7NPycHgR55Trj_wd7X2Z43rLr3NGsD8pn69p3zl2lEx59-EKpkZznHXl-Itoi3cPQqEXrnflCsoW5bW1_QMkGRuym-5t28TJXQ09wQnhTbhVY3HNE7elA9XKpwbOpTXuvze6v5OxRadv5EqDooTd9H34_qOk_dXNCEqUXpwRaW8mE2USUm6mX7HDTuuk6c0jQpe3r3xZjOogdEl0-PkDzxqrwmo10x9dZYsBIQ64Z680tI41pD5oeAEqIFu6tPuzOa8oynYXMMMbwijaJ01HotSzj9yYRFqauJ4V3DNLx-J28FeWa85A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d110f4cc.mp4?token=VxgmP784NrRMN66E6WI0K7sAZzOOYF1MqW7NPycHgR55Trj_wd7X2Z43rLr3NGsD8pn69p3zl2lEx59-EKpkZznHXl-Itoi3cPQqEXrnflCsoW5bW1_QMkGRuym-5t28TJXQ09wQnhTbhVY3HNE7elA9XKpwbOpTXuvze6v5OxRadv5EqDooTd9H34_qOk_dXNCEqUXpwRaW8mE2USUm6mX7HDTuuk6c0jQpe3r3xZjOogdEl0-PkDzxqrwmo10x9dZYsBIQ64Z680tI41pD5oeAEqIFu6tPuzOa8oynYXMMMbwijaJ01HotSzj9yYRFqauJ4V3DNLx-J28FeWa85A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صمت: سند آیین‌نامهٔ ساماندهی خودرو در دولت چهاردهم تصویب شد
@Farsna</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/457041" target="_blank">📅 19:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457040">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎥
روایتی از ساعت اول جنگ رمضان
🔹
گفت‌وگو با یکی از همسایگان بیت رهبری و روایت او از ساعت‌های اولیه حمله آمریکا به تهران را در مستند «همسایۀ رهبر» ببینید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/457040" target="_blank">📅 19:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457039">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkBwM3loZzy7c_2JkK0XhZvHB6ZcLpplxi5fc0HjIeHjF9ccmVcAu7ZqtzrVng-ae1F5VyBtb5pnq1Nv_VXOo1Sl4ex-WV1wy2v0yY9zLrA6uFqpZFT6Bqa_QXz5GQ1IddZoVvvux0x6z9GM40c63XgpFay2BpWWrkBcrBZBoVKSEKgTQ_XfvpCoCvsRWXXvD5SGYP9bA2mzYbmOkbGE7T3-HBa8wgsyv6pWjjV2f0VJrbBqpUnZYqK9-6MexRKAbOxkEGcIldYmBa20IAp1bvyOHeqOWrAZUMcG4AAQUr1uXPd0hGcC04u2sKPNAdKVCC_OAW_8Gft9ECmHhe9qNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلمان طرح شهرک‌سازی رژیم اسرائیل در کرانه باختری را محکوم کرد
🔹
معاون سخنگوی وزارت خارجه آلمان: اجرای پروژهٔ E۱ عملاً کرانه باختری را به ۲ نیم تقسیم کرده و آن را از بیت‌المقدس شرقی جدا می‌کند و راه‌حل ۲ دولتی را غیرقابل اجرا می‌سازد.
🔹
آلمان هیچ تغییری در مرزهای ۱۹۶۷ را که مورد توافق طرف‌های درگیر نبوده باشد، به رسمیت نخواهد شناخت.
🔹
ما بار دیگر از اسرائیل می‌خواهیم که برنامه‌های شهرک‌سازی E۱ را متوقف کرده و ساخت شهرک‌ها در کرانه باختری را متوقف کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/457039" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457038">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laEVYOLrenkOEvng5DDvkX0awgbR7vffNkSOUKpw3AKSc95kUdqGx9d2o5QKTbdF22ktRSlOXyadbJqMgIInfk2GjweKE2gWJ6WsQ_5GL84SHruu7XVlIxvKh1ovAFwcYvUfyA9BVfPIm48pcJj3QZ48oDYDDuP4IROMOv2uSjxDlCQbs0nmfMmwh9ZnyaUUIwovIeOSkbWqcbeltCiM3T-v_amOC5hktGM3pjK0AzAx-Xffi6ootIyRfgK6IznyGuLqJKKMR9cmHESN_BxdQ6tH3akfqQIq2Kz5NMs_PrvJmSPoAYjXDrOsuujPcRC-igbbyw0WjlPvY_EkH4koRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبور نفتکش تحت تحریم آمریکا از محاصره
🔹
پایش‌های ماهواره‌ای نشان می‌دهد که نفتکش چینی «مایتی نویگیتور» حامل ال‌پی‌جی که تحت تحریم آمریکاست، از سنگاپور بازگشته و امروز از تنگه هرمز عبور کرده است.
🔹
ترامپ یک هفته پیش در تروث سوشال نوشت، همه می‌گویند محاصره ما دیوار آهنین است و ایران هیچ کاری از دستش برنمی‌آید؛ او روز گذشته هم گفت، تنگه هرمز باز است و محاصره به قوت خود باقی‌ست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/457038" target="_blank">📅 19:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457037">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e41c1593.mp4?token=GiHc2LdHByc5WguKugocqFNez-wRRlTSRykfhl8URe60TpbSnJo-bC4_9Yrw2px2GbX2gp2oxVGmNSIHETxoPzUyQWfMjXhSJxPfqDDhVkakWMcGz_RmI53ZcapyadcrvjkdKq1W6JxtsSzi97qcUw4RUarFMS3qfde6SeW-zYGHESgDj3G5bnsG4SxxuwKiEVdA5zrDCSadTD6rr5nAXthf7RcwLt0JX-COlx7x38u089hPRmKTkRpDO-W1OC6Pwir0LDqfAH8h7ZdsQ6O3KH27bisbO9SBMlgrPNZormoWQvBFX8FujRXHfkv9DD2ta3UgAYd-qmI8_GFvPSGfEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e41c1593.mp4?token=GiHc2LdHByc5WguKugocqFNez-wRRlTSRykfhl8URe60TpbSnJo-bC4_9Yrw2px2GbX2gp2oxVGmNSIHETxoPzUyQWfMjXhSJxPfqDDhVkakWMcGz_RmI53ZcapyadcrvjkdKq1W6JxtsSzi97qcUw4RUarFMS3qfde6SeW-zYGHESgDj3G5bnsG4SxxuwKiEVdA5zrDCSadTD6rr5nAXthf7RcwLt0JX-COlx7x38u089hPRmKTkRpDO-W1OC6Pwir0LDqfAH8h7ZdsQ6O3KH27bisbO9SBMlgrPNZormoWQvBFX8FujRXHfkv9DD2ta3UgAYd-qmI8_GFvPSGfEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تودهنی رضا پهلوی به اینترنشنال و خودش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/457037" target="_blank">📅 19:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457036">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6x5tg4TGLNdgbOGketGenNlT6LA6r3nVkGKJ7NXqzFidi9QLicIFHsSmuMCEGK8xgDmQcietF36dLq3TZUZ8H7moOwbEG1ImoRcCfAFmQ2qGY2JPi8UTUcqry1f_-rx7CsBydXLMPImfQydUTsuQ9i4WWnBUHPHkTzSllihXBFR4eoExU4rIv-uRZGRK_5u4eUcqUV59HcjN6GXifOR7gvPufh4_v8IFuhMgagd4suL_0MaRLS5rjnlYuaGIA7PnK_QHyOwv2WSFWY3nJYlEUBJZ5dLLp9yonfVfkZ0rATfjQCX8MnCTspQ6oIVCsjwlGcTnIJY_HcIoLs1osNbbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: هدف آمریکا چپاول کشورهای منطقه است
🔹
رئیس مجلس در دیدار با رئیس‌جمهور عراق: آمریکا به کشورهای خلیج فارس و منطقه نزدیک شده تا منابع آنها را چپاول و غارت کند.
🔹
ایران و عراق و ملت بزرگ آنها دریافته‌اند که بزرگترین مشکل و عامل اصلی تمامی اشکالات منطقه،…</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/457036" target="_blank">📅 18:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457035">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDtCEK_06STlXFDyIj31mpCQShu2w4qkNHPCc_LUl0m7lyLuPKgSuNnH3CJkG4mZ56dRVsVBgX_We07AuUgaeT5t6D_oGEycVUtw-XcCVTafg2G7t_sdooOsHls--Fnwpwp5mD_tWwL05yHV6clEacpPO-62vcp0dGsLhgtNowJY2RZyL3texfveBaLztbZ4usV5v8gfTFFWOemd9gWTU1pacteOuEmlbAzK5EEDR6KgxxhfFKuOvknvpSXe-W7U_XhzWzQWHz2kTpZ-8M_maxV0cDAmE3hsgvS6ZU326eXwT8v7cqyDJElEVaqzYzn1qx7IkzIUUHedYjQJp4lO_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قالیباف با رئیس‌جمهور عراق دیدار و گفت‌وگو کرد.  @Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/457035" target="_blank">📅 18:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457034">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyocFn8MQeCLgPx3NdL4zqst3ft-bbOQsdYySl60BkVdY3tf6UPpPaI2voDRx4dpC4lTO-befYFNEbWzyBwv8Vke1fsT6izAJZhM1X45pb-cyTYgd7qoCK9o9fu5tGgM5Nm6tYAEVY9P8qwPEpSqiY8-Qi8ZTKiYf976DDiNAKVq9wRPDWlleEnxaVdjg2iWHz6O7MCeNOaHQSD1mDNvlubMsKsstVGRS2-VXs0JGK7RHG5hd8IeFHMUE0oLgZ4HKC9vkq6I702ECajdZnoCRtfqxVIcJN_IAqIblyxZkxyAf4KChXaE5l736tWSWt77wLoY2OPYET0QH1Vj9gs1vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصف دلار پتروشیمی‌ها باز نمی‌گردد
🔹
روند بازگشت ارز صادرکنندگان از سال ۱۳۹۷ تا ۱۴۰۵ نشان می‌دهد درصد بازگشت ارز به چرخه رسمی کشور در این سال‌ها از ۸۳ درصد به ۵۲ درصد کاهش پیدا کرده است.
🔹
دستیار ارزی رئیس بانک مرکزی می‌گوید که صادرکننده صادرات انجام داده و ارز برای خودش است و امکان دارد بخواهد با آن «در خارج کشور سرمایه‌گذاری کند یا در بازار آزاد بفروشد.»
🔹
اکثر ارز صادرات غیرنفتی مربوط به صادرات پتروشیمی و محصولات فلزی است که یارانه انرژی و خوراک ارزان از دولت دریافت کرده است.
🔹
میزان تخلف در بازگشت ارز صادرات غیرنفتی در سال گذشته ۲۰ میلیارد دلار بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/457034" target="_blank">📅 18:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457033">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G28Qn4ZAdUlGehAW2PRGXXVs8w46RwY3csok7KnSUt0vPkvKAGTPCiIs3oyJbhHiBeI6hB2F7X-KLhul1EHowM1tAHIG8pBqF55hNAUuNb9IyxwarjcBGi4ryqUcAKQTNz-VuG6dLx1HZAznochEGXaFPKMQh7LmT6A96vc_6OqpqeZZsV9vw3xkKKmKQZLJhZMm786bXccE1H1EHxo-mtpIjfSOGigxSbV9h5AUxr-MlADN2-Rom23oHAUFXVFMurmA6-8SjuAvY1ilZv01t43FaStt3j414pJ0hLwxnl3xVWCjrdQXoL5lGCbWfR3Z7Qlt2q4a0UWGuM0Md-yRqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیمیل بخشی از کارهایش را به کلاود می‌سپارد
🔹
دیجیتال‌ترندز: کلاود با دریافت قابلیت جدیدی در اتصال به جیمیل، دیگر فقط دستیار شما برای خواندن و خلاصه‌کردن ایمیل‌ها نیست.
🔹
این هوش مصنوعی حالا می‌تواند بر اساس محتوای مکالمات، پاسخ مناسب تهیه کند و پس از تأیید کاربر، آن را از حساب جیمیل او ارسال کند.
🔹
کاربران می‌توانند از کلاود بخواهند صندوق ورودی را جست‌وجو کند، مکالمات طولانی را خلاصه کند، ایمیل‌های بی‌پاسخ را پیدا کند و اطلاعات موردنیاز را از چند پیام مختلف کنار هم قرار دهد.
🔹
قابلیت جدید نشان می‌دهد نقش دستیارهای هوش مصنوعی در حال تغییر است. کلاود دیگر صرفاً ابزاری برای پاسخ‌دادن به پرسش‌ها نیست و به سمت انجام مستقیم وظایف روزمره حرکت می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/457033" target="_blank">📅 18:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457032">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/531e74ff2c.mp4?token=INGMXS7ZO_u1VooLT3UHO0pn15toQqp_sWJwA5FMtcVVSKQMoPZcbAcqhhGXFz4T-UQmiTxKXW-ffsW121n1mUcld7XcfSziurf6i8VTTl3n9k9pZcQqhkfvher5lGi3nw1SmVmXElLtelJx0bzuq1ITIEBmQ-EQ6F_VSxOse_Thb8oLWGidEl4tWGbr4h4PP-LExRgyUVK4hZyt0ol0MP5VjiVAufGyI9zRrtuZ7me2GQ7q2soIynwHCEBysG0IVh8RsvahqVkkS97sVkYJJSzKHMOrZ5pYiwz0nI0dApxnElfaPT_Fjo-PJS55J2Rz23GMa9393dxSerdFufBOgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/531e74ff2c.mp4?token=INGMXS7ZO_u1VooLT3UHO0pn15toQqp_sWJwA5FMtcVVSKQMoPZcbAcqhhGXFz4T-UQmiTxKXW-ffsW121n1mUcld7XcfSziurf6i8VTTl3n9k9pZcQqhkfvher5lGi3nw1SmVmXElLtelJx0bzuq1ITIEBmQ-EQ6F_VSxOse_Thb8oLWGidEl4tWGbr4h4PP-LExRgyUVK4hZyt0ol0MP5VjiVAufGyI9zRrtuZ7me2GQ7q2soIynwHCEBysG0IVh8RsvahqVkkS97sVkYJJSzKHMOrZ5pYiwz0nI0dApxnElfaPT_Fjo-PJS55J2Rz23GMa9393dxSerdFufBOgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرگ ۶ توریست در پی سقوط بالگرد در کنیا
🔸
آناتولی: درپی سقوط یک فروند بالگرد در شهرستان سامبورو، در فاصلهٔ حدود ۲۷۰ کیلومتری شمال نایروبی، ۶ گردشگر و یک خلبان جان باختند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/457032" target="_blank">📅 18:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457031">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf0435e5e9.mp4?token=v4k8OvtMuzuEbzVWK2EBqVRH0G0dgli4_q_6HdXGU8v8MwooiCqHpjZooZkNOP3Fg3VNshGAhnPqzHvJDtxFtdt8hI833lPq-PsJrDlnTItkCkPmBkFtzEPS0zdlTM8WOTJtvDOIQrl7iWWprGJXprkN8pTqAUdB-YsSgaYLcvfEH6m5kOjvsqaI7ovfPJVJfguiOsOBlQV0kUOM2svHHqvAsJk8rWuHUaPyJXiyYOhjvsMVF0pLhzMgoAMnFnmJTBgj0l6huoYIAWvqJe9CR4xB0i7fUqfYYfFg42Y4Gt9nl4WDILjcmGcgbth7k2eb8djQNtxV40pS9qZrekuxng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf0435e5e9.mp4?token=v4k8OvtMuzuEbzVWK2EBqVRH0G0dgli4_q_6HdXGU8v8MwooiCqHpjZooZkNOP3Fg3VNshGAhnPqzHvJDtxFtdt8hI833lPq-PsJrDlnTItkCkPmBkFtzEPS0zdlTM8WOTJtvDOIQrl7iWWprGJXprkN8pTqAUdB-YsSgaYLcvfEH6m5kOjvsqaI7ovfPJVJfguiOsOBlQV0kUOM2svHHqvAsJk8rWuHUaPyJXiyYOhjvsMVF0pLhzMgoAMnFnmJTBgj0l6huoYIAWvqJe9CR4xB0i7fUqfYYfFg42Y4Gt9nl4WDILjcmGcgbth7k2eb8djQNtxV40pS9qZrekuxng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هرکسی به شیوهٔ خودش برای رهبر شهید نذر کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/457031" target="_blank">📅 18:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457024">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSjgZg5gnFgI78YzVEpp1XXbS-GH9SjFT05Ze6eIxCvHX9Z7LBL-3DBYq4Q9RS5OzpNX4sM-hLAB1LEQx95Jg-Wdkrcgj7vSET6P0n51mwb8ate4l0X-ehodP60oW-VYGFgfQDrBA1dx6kZQ_lTkgE4lHVJjYYv_4hK3a-hmxDgXlnNERsF3f1UQ7YyiAEwu85sv-5T6pSyts0Zt_skCCQ4cG4hbl9q20toLmlXN-YZhhpBQnYOQzJKuvmCRNJ4VoPjuqatYuUcGNDVrVb_a-6owcyASVfKiOYsjMbU8asGwv2Cd4SgMl9RPpeMyGI-OUdI-ROBvmowl4vAFYKghWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nMaVmMT8YlKOHZtUAgdWYniapLuA7l6EYfNPqbUwy7Zfny43tcVOmuqBPZhMCrvaBNlLxVMC79uq0PXgwgsm0L_OX4RaKfyyjvBml0UeozHhOGw2uX-2AO2JuROtjsdj6zdy0eJs-uTnkNSQo4-SunmP8lGpKoHUk5UC4bEoZ-dUfazx6pevpNijY_wjex1r-mSjNoWg7_8mwzZGqXpbqq-2yWCOLMqld2TcFlXggPMHm_apc6O-Wx7zKUK4DX-6YVgkB9hTiMFn1J4YkLojhurZbl0cCQOYOvJFlmswoLiRu9xNH-FaFmDJCPT0t6VKNHVx1r6oO_3zi-77kWlGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLqKXhFXQlzqy_xLIlBOwY_ImwKzzHSdIg1i9I26oebKEic6Bf5DV3UsxnIMpA_zqhJD9gVM9w6NNJ-wzCSuKEkOjRP7sh1kH17TMvYigtGnw9uz9pY84ZyIyWMCB6Lvs-nr0ewC4kmN9osGxghSc1dVrs-K7iToqJaSoEP5mc-60dBJq1-veFUU00Eu0QwwZm6fYt12EbplgtzqWDH6ZrqN4NTH34JuFMQWEuEI06NzURr2iCUoZf4VnjNSE62vylKrXsYmsxi_1FXYf-7EKF0rEogPJJ7KNv_ASCCwLkZ9mVbmWj-UONBdQ3E_VwL--DLHCoJZh4RdR3tSPNsCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kOlxdwXh_DZ3R8syjcBuSHJR6H0pCNbroI4K_zp-_mgoxpbVay3oEEcIgaXNw9qqi-7xUYBVeIu7XSKfxXw-Mv4TA1CYFna1TtK-c0uWQWAUeibweRROgBZgNUbP3B651cBJSx6F-ACGW5MNw7k6OCkH9VB2e93RTiOUr_xLSR-WPerhUWLkr6BSxqUcPi4KSg2DwwXiNgIeR8LvcivK9CcoJIx3SynfiXWOIYtkOXFydJvZoT-62bVnac5WGq4hCofk_s_5EeNZiDnaTx_2dY_SrzWaQGVkHhZTNppw0cxU6sy5WzhiSXNHJX_IkmqV1zNtbrn9vv3GUvLm__Xf2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzlyIsAAfMs028wG5lLm6sH8JZ7xU1lhky8QtkZjGtbIVQo8o3vzKs2Vg_RxDp7_oK_HVjrA611Pui5q94k4aC8lizslnWzxvpuFl7nMC-p8rdMHipWD2thuard4vm0fjKaIx3AnyuAqdNmFukOmbWXdO5Y8InL9ju8cBgQlAaAI9LYl8aa_SFP8Sfg48oll-phZ692YaK9qn5IFhMMjMwV5C0FGZbxH_7QgP9za-82i3P22pVZ4rXSU2i77FwALx7MtyaKgAtX14V0Xa0wMkLbUGtA8NRIbW9FkSBXMKobsc9ZRlePT5mbfzBCjBdLilcin1BWrxsNUDyNFVmZVZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/in7Au6_2NhQ32Kd8Hj1cqo4zXQYD2Fqt_PbcvxQrU_tgcit7UVe3aJkCC_qbBNbugzEZnHltjW2gFr7YkqeW9gtIW0DwaP20anyL-XR30ucnq1wPNTCo5Ry7JyE-kIS4cQgX3-fb5Oc1kkg0TbGqFn2AiFERcgOVRnG3STcxA7UO9TAr30LNCfJFlchcCosHHEbcNFIV1qKLqRs7527YVxFyjGj5aZlWV5WBTIq2c8FWC8pUl-ojKCtAFYzD6TcKiRu22kHSE8t2irg-qzLEdxOMWp8Z9fRD5-edHBSfobWqk4pZ0KaJJe7sBhhhBucoU5BXA_3Ejm_-dqTRYCyzNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d6g4lCvQpok4jcU8d2jFWBNwNfqRzHDzUsHwWTA3tyRR7DjdXxNyxq6_ZsoD847jEPD4Ra71z3DMf6kHSBAUyAMD8OlvZS2l_Z_E5uZHEthRbnjPN9YA1WhPHl0AK-8rmbYoBpU6StmqYubLI0j1hOXqOhzE5aNJs1rzIncpdhUGo1JIdw_fx6wEFOKbpb5Ng63ptGDHsC9xY8lfiXggSh02jL45A3bCYSN5hbzgbuoM2tar2lfh6gXeHLkYGViDOtlxrZGxUiw3pfxn_oa20J_VibnXdj-quZS13N5Qj1oJPtujEDEDdAQlX5lTGtLJjXZodNmwC9uONRAxSTEaJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تقدیر از فعالان مراسم اربعین
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/457024" target="_blank">📅 18:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457023">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc8a8e3503.mp4?token=X5sjlUKfQMc2fQ8GkVwCjAaBTWDX-RWQfsuNSLB7s12-rs1djfn4L1Qsh8FYVltZwTE1f5V8BlyFoskOQfHyuaycPZ5FjNrrXiDrhd15ZkgGIW_S8cYFukFc0pHEn33_RT1aO7nFdKw2dsn7w3ZA23wLcwr-70nUKPolvQUaLxt8DdGoocsmAqtHbysJ2HZgaYtCppjDoEqv5u68nmDZt7UNfHVLgTkxNJk5Q23LW-d0iIVisrZx1wclT6iyFz8Z1nSOSJ8SC0cVYoZDlPGdXHn8kfVqokN1mDLpSbIPD3eR7XQWj2XgPeWK0fwHMUSwCIRoO9gfiyA--3NpXATsrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc8a8e3503.mp4?token=X5sjlUKfQMc2fQ8GkVwCjAaBTWDX-RWQfsuNSLB7s12-rs1djfn4L1Qsh8FYVltZwTE1f5V8BlyFoskOQfHyuaycPZ5FjNrrXiDrhd15ZkgGIW_S8cYFukFc0pHEn33_RT1aO7nFdKw2dsn7w3ZA23wLcwr-70nUKPolvQUaLxt8DdGoocsmAqtHbysJ2HZgaYtCppjDoEqv5u68nmDZt7UNfHVLgTkxNJk5Q23LW-d0iIVisrZx1wclT6iyFz8Z1nSOSJ8SC0cVYoZDlPGdXHn8kfVqokN1mDLpSbIPD3eR7XQWj2XgPeWK0fwHMUSwCIRoO9gfiyA--3NpXATsrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک شادی گل با ۹ کارت قرمز!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/457023" target="_blank">📅 18:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457019">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L0aB7FqKOibeGU1WjIKaNUmJKu5tnAEPx_iDoliJ6j3crNXWQe5MXXQc-Ovn6k-d7vgyPJcvT1JKMPIoUkCVOW6UXHZfJRd1gbi_v4B8R1e5NvJ4MTilfw_FxeHMDWlrmx_2O3rd8QL3ybIYScrKUh9dY7BG8DNb9TOQMRp_h9y1zhR6q26f-iGWrNVQA8GVCQ0JKf4XR9vLxb0OeEzn9KV-qbYyr_L4wVZC2XEd_hie2X2AVSFTB6mYeN_rZeNDMT7n8OQYUp7RuMQZDfRrT8PLtBmvZ9S7r0bmOZB7oRuFKyVGNejGnyjC9tKt0yeNPtmUfazzE2jXAbjYLiyGlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Una6Q-CKBzDgSWAp2nJWfZjjfzXMnUALhz7CfOJvlWZOAWy7GKVp6b5IpUakY7wocXry_b12oTzmmW-8zVVjJh_ik0U58qr6VIvQCaj8RtEf8f04hq528rnl1-IgO8hM6_T7k9AY4qJO0AeRPy-1Qt0JLJakfsvChjLu5WI4U4b1Lw5By2-ADgIH8dVyiu9LdT7dRse2QeGBS6LGqVOa49s-rwqqve_VFPEjW3tfEvuJtKTdzoADh6gS--9ky1HqOn54XSwQLIIe8CnAELlGao2XCO7-XB_g5T93aSJ9P-IJu7OSxGWbc1eYqd9OsKOGlzAYVYBSZ5X85vDdZPJj6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PM4AND01LUNeDk_SMhDTj4A3rcskGzPsGy9o7nYF01gxlbUk7C29g66cu-XZvz14YZ7t4rIPoqj6Ou8RpLXXbDyTcQCoahhbteefqqgrrwV2npyWvnM6qn23Rf1Oc1_U9NDaaZcNHBzbXyB4eQWlC_RJ8vzKbvYpyjob1INWH0aUhkJZi9mB-HqevEZEGhzGqpKJyaFz-Qh__1eAdQN1YyIzpY7OVYQWESDbXD6MWuqBi3EvtHLabWYTQiQcbshKwXPAe8KsghXpnSwsq6E9Tgr3VPOiuvZ6_zAN2HWpnf09WlfsqF-OkMLBW5jnkqGR_y2LX6Ckn42--QwceDBLZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تداوم عملیات تخریب ساختمان‌های مسکونی در جنوب لبنان به دست صهیونیست‌ها
🔹
رسانه‌های لبنانی از وقوع انفجارها و عملیات تخریب منازل مردم در شهرک حولا و المنصوری به دست ارتش رژیم صهیونیستی خبر دادند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/457019" target="_blank">📅 18:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457018">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1645b5f818.mp4?token=DTaDbk_Jy8gLw3ttTCIzXD7HKS4iVC9p8rsodTNNjYvos81MENX3Ighs3yFOC9TFRhvVLq9owao1dhy4bO7wOIqvsAsEJe8XJ_1aWIvEjcmsA5e5NQ45b7SrTPFlAE0TQKqeSeiOGZAnYmDV5zXiHlHf8ZePC_NzVCquIx9XIXN1ph5zRFVu_sZrLYFWUI-rO4dqGoYM0Pwlye_uy7fvbeQsgHbCMa3ixOk9OXiwPsy7J0Kz0mpwBQ0kPsZLkpAtPTQ-A0xbkJYRDndz0Irt5Eoimg_s4N4bAtEi2wvJzs1ccdUuPY4oeyHOTRjtxETClaC82m8bf9NVlj4HxISiJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1645b5f818.mp4?token=DTaDbk_Jy8gLw3ttTCIzXD7HKS4iVC9p8rsodTNNjYvos81MENX3Ighs3yFOC9TFRhvVLq9owao1dhy4bO7wOIqvsAsEJe8XJ_1aWIvEjcmsA5e5NQ45b7SrTPFlAE0TQKqeSeiOGZAnYmDV5zXiHlHf8ZePC_NzVCquIx9XIXN1ph5zRFVu_sZrLYFWUI-rO4dqGoYM0Pwlye_uy7fvbeQsgHbCMa3ixOk9OXiwPsy7J0Kz0mpwBQ0kPsZLkpAtPTQ-A0xbkJYRDndz0Irt5Eoimg_s4N4bAtEi2wvJzs1ccdUuPY4oeyHOTRjtxETClaC82m8bf9NVlj4HxISiJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روسیه و اوکراین ۱۰۳ اسیر جنگی طرف مقابل را آزاد کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/457018" target="_blank">📅 17:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457017">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2694417128.mp4?token=q2CLH4gs1245DaC0C5h9j2XfH3UYtllU_5rQkRejBQSWFXBplRGueqws9EPNygJIs-8vB1rpaXPTNSBhJgC41Ys9oV0fUgqIsQpYvbAmtM8cdtRoAHmF0t6yc-I2x4V3_Sqt4Te_5p95NGP6mrvQLQQNTP7go0MURF0Qz3oFovbip58g4Ak9pqetK3DeKZ9Gx6_qex3j83f3jkvLro-vJb8WXBePB2Rq7df574XpCv3X4AHXGKTqhKlvwAr8SwrwWHSPkit2xfre-brY6LX4uBj5fDyzdFkmsB9A_5aqdCRZoiOIC1INpDoe35t78Yu_PkenSpgvGk3w55y2EgGUdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2694417128.mp4?token=q2CLH4gs1245DaC0C5h9j2XfH3UYtllU_5rQkRejBQSWFXBplRGueqws9EPNygJIs-8vB1rpaXPTNSBhJgC41Ys9oV0fUgqIsQpYvbAmtM8cdtRoAHmF0t6yc-I2x4V3_Sqt4Te_5p95NGP6mrvQLQQNTP7go0MURF0Qz3oFovbip58g4Ak9pqetK3DeKZ9Gx6_qex3j83f3jkvLro-vJb8WXBePB2Rq7df574XpCv3X4AHXGKTqhKlvwAr8SwrwWHSPkit2xfre-brY6LX4uBj5fDyzdFkmsB9A_5aqdCRZoiOIC1INpDoe35t78Yu_PkenSpgvGk3w55y2EgGUdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از صحن پیامبر اعظم(ص) تا مزار نورانی «آقای شهید ایران»
@Farsna</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/457017" target="_blank">📅 17:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457016">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEX5WU5f5eVEFWGskfspavIBzGu3GsYwCKypy4kfFW1FSooVtnrRKs9IVCt_SOnK2Ak_7u31N80C-2pyYoS_TFyUFINXStlGdaIFnTM9xi68JI74xWiZQldS8ISXI1mlPjc-B2-_Fk3F_UGhCghuIjYUpbDwnr__Tw8ln5U2dLxv8zYKmFHhtN1FNi7z1oxAx4i3NK4-Xh04m7up8TMD-uhSbfLwhzQM6sc1tZFWCbAVbKCX1eIAsCmJdRECXFQ54lj1veDJlzQ4MtlveNXwe9f89g3oTvv6AiLw80uIC15sGCEXKKthaHsNT-GWoz06NV_CT8DbOi58o23Q_X97Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رقیب انتخاباتی نتانیاهو حرف‌های او را تکرار کرد
🔹
نفتالی بنت: حملات نیروهای نیابتی ایران باید به‌گونه‌ای تلقی شود که گویی مستقیماً از سوی ایران انجام شده‌اند.
🔹
اگر حزب‌الله به ما شلیک کند، ما به ایران حمله می‌کنیم و چنین حملاتی باید هزینه‌ای در داخل مرزهای ایران داشته باشد.
🔹
اسرائیل نباید تا زمان خلع سلاح حماس از غزه عقب‌نشینی کند و اجازه نخواهیم داد که قطر یا ترکیه نقشی در غزه پس از جنگ داشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/457016" target="_blank">📅 17:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457015">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9775b0679.mp4?token=ogq4o-kI-p8CnChTDRRw5epD7yZo6j17EIR-J0Bn0SBLlfIVbqFEHOX9Apv3GGyeDo0AJAxVc_B9zcCKkU00HnE99Z0l-isfogkAcpGWgMFWC_UuS_mhvQ0rT3RB2n79cCRv4UdpjnegNWgkn2msfvBzxHKvxZ9FJa7RGn7MVDZWz1YOhsM0BnKHO9RbmJmzshpMyF0VKaTJQ8i4elaowXnu1nqc_u7Ej-K_av_rXRkFp9b1208zSzRi1Ox7V_ZmvdiMFmZCsXnagQV6v5yeHh6k5pYFIpoUi0VfJvM9lDwHj3dXsFd87cNduTVQn948DNHcXPqlwvdVUWnktCMJhV4956HQviV2sx0i43blss0N2WEiztEbMOv7WG-kmC9AI1fAfgl6hq5n6yBQgRRgSsBLTodAbdEM4lB4Hozy6oZjGz8uJhmeOpnD0cLxlkOZUHYUMksbDOmcmUNn4RMBV5saW2j6vjtMpwMQ0z_YF0G4M1f4D_U8PshEDbC75-jCTxQIcMhuf1s_68rX1cCLyF8yJOis5oFFWqmrOpGR1ruT3TvNT9--Ptwh1RrKabBoVMc9ciCk3afwYd2NQY9kxBFTpjZL7o0sy8u1zK8vVnmVBIWwilws6KN_jI_HXGUSsl5Ajh9NC4IZEmc0kXoNMUAsu3SVR-ZXfH0p_haFx_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9775b0679.mp4?token=ogq4o-kI-p8CnChTDRRw5epD7yZo6j17EIR-J0Bn0SBLlfIVbqFEHOX9Apv3GGyeDo0AJAxVc_B9zcCKkU00HnE99Z0l-isfogkAcpGWgMFWC_UuS_mhvQ0rT3RB2n79cCRv4UdpjnegNWgkn2msfvBzxHKvxZ9FJa7RGn7MVDZWz1YOhsM0BnKHO9RbmJmzshpMyF0VKaTJQ8i4elaowXnu1nqc_u7Ej-K_av_rXRkFp9b1208zSzRi1Ox7V_ZmvdiMFmZCsXnagQV6v5yeHh6k5pYFIpoUi0VfJvM9lDwHj3dXsFd87cNduTVQn948DNHcXPqlwvdVUWnktCMJhV4956HQviV2sx0i43blss0N2WEiztEbMOv7WG-kmC9AI1fAfgl6hq5n6yBQgRRgSsBLTodAbdEM4lB4Hozy6oZjGz8uJhmeOpnD0cLxlkOZUHYUMksbDOmcmUNn4RMBV5saW2j6vjtMpwMQ0z_YF0G4M1f4D_U8PshEDbC75-jCTxQIcMhuf1s_68rX1cCLyF8yJOis5oFFWqmrOpGR1ruT3TvNT9--Ptwh1RrKabBoVMc9ciCk3afwYd2NQY9kxBFTpjZL7o0sy8u1zK8vVnmVBIWwilws6KN_jI_HXGUSsl5Ajh9NC4IZEmc0kXoNMUAsu3SVR-ZXfH0p_haFx_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت انیمیشن لگویی از حملهٔ آمریکا به دادگستری لارستان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/457015" target="_blank">📅 17:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457013">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHyiOo21elfP0OTWjj1d7CZGPBtVruo7e0bJlfryfZXIYIWUwzhpbTMyg164T04NbGBwgEdGAMUTlOMVcituehWZ01WrAiqb5e94cF3hyorp1ZKClmvaJAo-E-Stzc8ffhbceDLMY9IqeaM4I1mq-_6mNsExL4bSteF_UsHXeDvabq6LoF72Kgix6VspPDzMWtd33y9ZG90_P2L4tOvjeLk8WLEfny9tySYLZIixkw-leYrE0Z_WdSWg-YoMBAvdkqUKmJTBKeW-cu5C7pxWLS3ltEg-lMEi6tYjxSU3fIHAYqYnSmBm5u_F4OX-ceP4LfkiYsRkU0s0wcdjNfNHkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار قاآنی: غاصبان فلسطین در سرزمین‌های اشغالی دچار «سرطان اجتماعی» شده‌اند
🔹
غاصبان فلسطین در سرزمین‌های اشغالی دچار «سرطان اجتماعی» شده‌اند؛ فروپاشی از درون، سرنوشت محتوم آنان است.
🔹
تروریست‌های وحشی و رهاشده در کرانه باختری نیز نمی‌توانند آرمان جهانی فلسطین را به حاشیه برانند. الحاق منتفی است و فروپاشی، قطعی است.
@Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/457013" target="_blank">📅 17:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457012">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce2f0bcf33.mp4?token=E44by_9_m6hTsXdiNyTWYVZqxa12TdtjVKXB3w5Ssivtvo45Hndm50ZySpys9ZfB31uDPGhV1bnty_Fd-hTZ6UUp6IXfUIqyBsbenqGMCq9zoVXiYYS7dHfQJGtQurhGPl0Xhey2ApvZZbW2qOd0t1rEhaEsNcwPL2alxtoE5jeKct1-BbGyPUqz5seQ7X50UGRi03TMw4t4TQ80i2pFjwqImIgoOJGzQewptju3U9eh2OtpG5l8kFMck5Sdxk_T05cVlQHjlfHCH7EN2t0vwUOv9iQIQRCg2m86bgO6XqPhsOMit5Y3EUPJidJQ60BMHZ-p6Vt5VqWEzblwh19Ssg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce2f0bcf33.mp4?token=E44by_9_m6hTsXdiNyTWYVZqxa12TdtjVKXB3w5Ssivtvo45Hndm50ZySpys9ZfB31uDPGhV1bnty_Fd-hTZ6UUp6IXfUIqyBsbenqGMCq9zoVXiYYS7dHfQJGtQurhGPl0Xhey2ApvZZbW2qOd0t1rEhaEsNcwPL2alxtoE5jeKct1-BbGyPUqz5seQ7X50UGRi03TMw4t4TQ80i2pFjwqImIgoOJGzQewptju3U9eh2OtpG5l8kFMck5Sdxk_T05cVlQHjlfHCH7EN2t0vwUOv9iQIQRCg2m86bgO6XqPhsOMit5Y3EUPJidJQ60BMHZ-p6Vt5VqWEzblwh19Ssg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خطر سرطان بیخ‌گوش چه کسانی است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/457012" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457011">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3L23sFa6lz7YrNQ6ApklnG-r8CGk8oXwJfnk0asrDJ-gkrsCwBI4BClseFJJbnO-Mq1t7MENy_cbLgutIZ1wB00jFjF8Ss6Z_YThVVD06asKxtYih4bvf6rq0eWLxCn-Yh-iwLzroGj2OFsD3siXUGsVlNo9ha69h8Eo328HDn1_LdSo857NjE36UZVt3lWRE1EurFbFYy7X1kK0UAkG13voJdIMtn9thpWD1wE4R4IxvfvbKi_jiCIj7a-3TQREigiTGMkJri2keVbE-6k4Ffvq1DRUDkcm1asP0MCouWIHiCij4AlcXNMQ9iC31A_Ui3vccjJKXGQc1v-3l8Rzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: مقاومت تنها راه پیروزی است و اگر آمادۀ جنگ نباشیم مذاکره هم ثمری نخواهد داشت
🔹
رئیس مجلس در دیدار با همتای عراقی: از دولت و ملت عراق برای تشییع میلیونی رهبر شهید انقلاب کمال قدردانی را دارم همچنین از میزبانی شایسته ملت و دولت عراق از زائران اربعین حسینی تشکر می‌کنم.
🔹
مقصر تمامی مسائل و بحران‌های منطقه آمریکای جنایتکار و دخالت های آنهاست. همچنین غده سرطانی اسرائیل که توسط انگلیس در منطقه ما نهاده شد این خسارت‌ها را به بار آورد.
🔹
ملت ایران با مقاومت و وفاداری، با نیروهای نظامی و درایت فرماندهی کل قوا هیمنۀ آمریکا را شکسته و آنها را پشیمان کردند تا جایی که امروز آمریکا که در استیصال به سر می برد، هم با خروج از جنگ دچار بی اعتباری می‌شود و هم با ادامۀ آن ده‌ها مشکل برای خود ایجاد می کند.
@Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/457011" target="_blank">📅 17:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457010">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFmkYsOuRFMMflIkfn81dQuHkmUeEOz8J0iaTgHzNMHp6iZwynyrr8xagTzGAB2O7jRF5aKL6hI0-e3m6oPz7b2HxvwObFPbJYqw8syFvhJUKuAOWJHliu8kd5GHH_fA1h8nESEzyL4CZp-XwJUqZKXzqj0gjYy2PxOC6e2AcfKXjpv3MXCWI6Dx9-sfEweZA8urXKv4o8Kz_ML_5_h_gsv17vCFCmNI6hDg1osXSmaY1GP_hXWBQPUzkOwPxB8Rxf8oFIBw2aTUdn1pLLvm77DuuWjh9FMV8roBatKLHhK0xE1qE2JiJEQrkkaMaB6iJ_lriMQ-RhUtqe3suNiRJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت صمت: محدودیت برق صنایع به یک روز کاهش یافت
🔹
معاون توسعۀ محیط کسب‌وکار وزارت صمت: با پیگیری‌های وزارتخانه، محدودیت برق در اکثر شهرک‌های صنعتی به حداکثر یک روز کاهش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/457010" target="_blank">📅 17:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457009">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITj_ifw8_K7XaUXP8xMcJEiUpssOxp6WjZRlCwfqorTJZibfKQZ9BFz-nQ5JtFWFcEe7u89m_pwNDKXfBFKDNC0IfSaw9ixxYU2KggFfyzVVuJeTc_FEOKhNsaN7Clx3IqJinLAudb65tqkE0oehkzyGbOibc8OXHTFwhhW9441NzpNrN9IVutK8av1FyUjRws9WprkobiXJTwqokkPVQxjO2YPpQb5Zn-4DKVNSzIGsOHmZoRU-zu6Lpx24_aUGBwc36jyfiRuXSWWcbTQZgp75Ueg1r5nSLEbCPXl5pjP8v1GptVP5pPEdZbSVU_vXqOeiHMGhkqu0mZHw7Y9cPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قالیباف با رئیس‌جمهور عراق دیدار و گفت‌وگو کرد.  @Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/457009" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457008">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bffa382ff7.mp4?token=Lm0TpfxCkX_raFUNM6zvwqn_mDWtofMdqtZn9mt3EQwCBfgW9QqCwDFx5YAslHfKPLRIphTsIbDWp2j-KOwBPqHTA18W6279WAA1BeqFBrC9DUey084TGULClfmEL1wBjzOSmaMyL1fiMPRPJyfEnX1kJpY_u7GLBcfQLzllRRSDoKnqCLmLniOkz4mZWSvNLH1J9gkI6vslXh4YhRqXRVI254FfQvq4J6AmWdYyRbTpHG5nszhWcWtAmUiSTVjThjn58j5R8I2oKcsyPkX48GHWDaQkUfzp3y6wESkBpzfv-uL5cjsAMf1krYl4b-indFAEeLXxNNoLI8TxB1p8kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bffa382ff7.mp4?token=Lm0TpfxCkX_raFUNM6zvwqn_mDWtofMdqtZn9mt3EQwCBfgW9QqCwDFx5YAslHfKPLRIphTsIbDWp2j-KOwBPqHTA18W6279WAA1BeqFBrC9DUey084TGULClfmEL1wBjzOSmaMyL1fiMPRPJyfEnX1kJpY_u7GLBcfQLzllRRSDoKnqCLmLniOkz4mZWSvNLH1J9gkI6vslXh4YhRqXRVI254FfQvq4J6AmWdYyRbTpHG5nszhWcWtAmUiSTVjThjn58j5R8I2oKcsyPkX48GHWDaQkUfzp3y6wESkBpzfv-uL5cjsAMf1krYl4b-indFAEeLXxNNoLI8TxB1p8kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طرح سقاب برای بنزین چه باگ‌هایی دارد؟  @Farsna</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/457008" target="_blank">📅 17:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457007">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46d12cc487.mp4?token=qGK_cKygWZzOgwFh-yowmUvaE14fGfii9MB0VrlKhoHcEs7CRXgu-5qnI-1tCAvAYPZFlwaQm8IWcJt8HnCEt29TGOdy4hDRrKaZVepOC6Nx9gvlX9F-214P_AdoR7V4rtlE2urkR9BmTh1b-rrYAElpW2RfXxV2hb0F5Mp26gcrvjBJ0jtAZli9_FzjJSKxI4BB4nSVnlQVT9OFhtEtwW5I9GE9h6qKg2dShek-ZIvMtgQNDROxMf89YW3XIaiDzsOxKDgX7uIqs09VlhDc0qn3cImCw-AbIt1bZ9IKLqkb2xZp45NytIFJD0k85ZZb82Kk6zcnQh4hotPpNoXqNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46d12cc487.mp4?token=qGK_cKygWZzOgwFh-yowmUvaE14fGfii9MB0VrlKhoHcEs7CRXgu-5qnI-1tCAvAYPZFlwaQm8IWcJt8HnCEt29TGOdy4hDRrKaZVepOC6Nx9gvlX9F-214P_AdoR7V4rtlE2urkR9BmTh1b-rrYAElpW2RfXxV2hb0F5Mp26gcrvjBJ0jtAZli9_FzjJSKxI4BB4nSVnlQVT9OFhtEtwW5I9GE9h6qKg2dShek-ZIvMtgQNDROxMf89YW3XIaiDzsOxKDgX7uIqs09VlhDc0qn3cImCw-AbIt1bZ9IKLqkb2xZp45NytIFJD0k85ZZb82Kk6zcnQh4hotPpNoXqNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زنان «توانا» برای روزهای سخت آماده شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/457007" target="_blank">📅 16:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457006">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQce106Q99fB25jZMaO6Ry-fWjiLAoHH7kHwpjqGreZoxyh0u5lnpg5Vhop4NCnGKEoHq63eg346PYOIVcwta8ZCfDuU32SlCqVxq4tqPwE1qv8biZmG6VijtFEf5ehX5F3YOey_Fdm2fnJojm2onrece6JveBh_kwfvhN9v7lWU-Csg_jEUNoYmaLKq63O4ROTPPYga8YmIk1JjRS9U3NC3pDOHe-9rZ-Lq5hWXe4bhM72uDVHdCw-XOJr-B2ohWjotpJ3C72T7VLhSLSiwZWH_OY5jSM4_TjDpVJkZLFwOw9xSnDEJ1Mk0nWwWgpN5j5wS5rH86lrqbEAcdTyMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تشکیل کارگروه ویژۀ بنزین در مجلس
🔹
رئیس کمیسیون انرژی مجلس: کارگروه ویژۀ بنزین و سوخت زمستانی نیروگاه‌ها که از شنبۀ آینده آغاز به‌کار می‌کند، برای رفع ناترازی انرژی راهکار عقلایی با در نظر گرفتن منافع مردم اقدام خواهد کرد.
🔹
از هیئت‌رئیسۀ مجلس، دولت، سازمان بهینه‌سازی مصرف و شرکت پالایش و پخش در این کارگروه حضور خواهند داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/457006" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457005">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df7fbcfee5.mp4?token=qFU5oiqPG-LVUa8Z3DDS7tJ3AqUeTkpkfQSKY9BITQW5xNz1uV3ZMyNeD2piWWogWXqty0K1tKtgj4D1gLT9LNL5cz7U8xRTCHBF1JMctfIkoqkQd-Quzs2e0O1BrmWwdhlYQfQRADONoFvEUkIrxbNqv806Sxyr3WDfqlU6szWWuZLuIa2BZMJsgNbhSkgZrZ1ESYLwItvi0LfEbaZ7-T9goDXPYKGPScgflke3FRiZM8qGJ5v_1YHaq7gkmYFhyyNXusbr6J6C7rYZ1jSORVvTmqEZDy24pyHpoC0s_ZplcCisF1JYzAwtUdXRAwoiwbR35FLF0GfokMJJf08ukQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df7fbcfee5.mp4?token=qFU5oiqPG-LVUa8Z3DDS7tJ3AqUeTkpkfQSKY9BITQW5xNz1uV3ZMyNeD2piWWogWXqty0K1tKtgj4D1gLT9LNL5cz7U8xRTCHBF1JMctfIkoqkQd-Quzs2e0O1BrmWwdhlYQfQRADONoFvEUkIrxbNqv806Sxyr3WDfqlU6szWWuZLuIa2BZMJsgNbhSkgZrZ1ESYLwItvi0LfEbaZ7-T9goDXPYKGPScgflke3FRiZM8qGJ5v_1YHaq7gkmYFhyyNXusbr6J6C7rYZ1jSORVvTmqEZDy24pyHpoC0s_ZplcCisF1JYzAwtUdXRAwoiwbR35FLF0GfokMJJf08ukQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزدان‌پناه، استاد دانشگاه: یکی از کارشناسان طرح سهمیهٔ بنزین می‌گفت اگر تا پایان مرداد این طرح تصویب نشود در پمپ بنزین‌ها خون‌ریزی می‌شود.
🔹
همچنین پارسال می‌گفتند که اگر برای برق فلان تصمیم را نگیریم مقدار خاموشی‌ها به‌طور فزاینده‌ای زیاد می‌شود؛ نه‌تنها…</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/457005" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457004">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77e86f339a.mp4?token=Dtv68c7rzMyW8p3rqeZ6mO6-QSLccsOmveVvzxQcr9fT1yos6Cgx157wudjuSXqop94jkJyTtsAJavj1FRRB5mLyiQR6NoUSbOFMPjU9Xg72GQ9i63hnzjx7rwhspBwHJYck3cmUJ6AmyxRJburDgzXiEksng78sZlkaO7uUWNcqGjD9awfltTXDWkjYQ7VQ6b1hPdZ0ojLznxXje18ztHLGuCb8KEpVi_d0duUXbkqGdQofuoOdvaFgVgh5X7VAlV3o7QkzVs_M69mOiGjdzDDPjOqy5c6aYGQlnsCPHSx-Y-DP9a6rLGOt4HbQgXEqjONYJ7u8yQq6jNfOGjcQ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77e86f339a.mp4?token=Dtv68c7rzMyW8p3rqeZ6mO6-QSLccsOmveVvzxQcr9fT1yos6Cgx157wudjuSXqop94jkJyTtsAJavj1FRRB5mLyiQR6NoUSbOFMPjU9Xg72GQ9i63hnzjx7rwhspBwHJYck3cmUJ6AmyxRJburDgzXiEksng78sZlkaO7uUWNcqGjD9awfltTXDWkjYQ7VQ6b1hPdZ0ojLznxXje18ztHLGuCb8KEpVi_d0duUXbkqGdQofuoOdvaFgVgh5X7VAlV3o7QkzVs_M69mOiGjdzDDPjOqy5c6aYGQlnsCPHSx-Y-DP9a6rLGOt4HbQgXEqjONYJ7u8yQq6jNfOGjcQ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ظفریان، معاون مرکز پژوهش‌ها: باید تبعات اجرای طرح سهمیهٔ بنزین پیش‌بینی شود.
🔹
حداقل کلیات این طرح مطرح شود تا با شوک‌های اجتماعی روبه‌رو نشویم. @Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/457004" target="_blank">📅 16:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457003">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b67b986b0.mp4?token=Wk8B7j622ppsyZNwTsfWZ1c6sYVUDIo197Vde3WC79WAcOoZwbFmG0nIOWgnXiaxqNsWFIXpbjTshXh1m9EGPvu3RxZjHFqukRMVBj-k54R6WJ2N_eUIONTNhpOtfDjU05ZWBWQmmvH8fCst_iU47xH8rNOcgXihihH-khqui7AcupNTBtElFBU-esEDLeDPy3AMV2M8cyTQ347VtJPGJiH2KX0xRohblSZPuQPhW-CMgYoZoeiS5hihOvUKcojzvCA0SEfzgWikp5vE1K9GXQ3ESR8sIOJ4OiWyHFd15VkpfSY3Fb_CzDUjmYti2V-CklMol56e5vwXbYIznx5Peg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b67b986b0.mp4?token=Wk8B7j622ppsyZNwTsfWZ1c6sYVUDIo197Vde3WC79WAcOoZwbFmG0nIOWgnXiaxqNsWFIXpbjTshXh1m9EGPvu3RxZjHFqukRMVBj-k54R6WJ2N_eUIONTNhpOtfDjU05ZWBWQmmvH8fCst_iU47xH8rNOcgXihihH-khqui7AcupNTBtElFBU-esEDLeDPy3AMV2M8cyTQ347VtJPGJiH2KX0xRohblSZPuQPhW-CMgYoZoeiS5hihOvUKcojzvCA0SEfzgWikp5vE1K9GXQ3ESR8sIOJ4OiWyHFd15VkpfSY3Fb_CzDUjmYti2V-CklMol56e5vwXbYIznx5Peg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ظهوریان، نمایندهٔ مجلس: در طراحی سیاست‌ها باید جزئیات آن روشن شود تا زمینهٔ بروز خشونت جدید نشود.
🔹
باید مشخص شود که آیا توانمندی برای اجرای طرح سهمیهٔ بنزین وجود دارد؟! @Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/457003" target="_blank">📅 16:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457001">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJ5ti7nq0ZO73IxPGlb1yOgWiXsdXj0BAhZl1ev6cz1SmKtoOm_yfkEZ91zDngYqppdeaq0NKJtjpdC9AV01bHtLP1cbf9u-NCzB77rO8VqtFuy484RwQ3N_WsEnmKMMlcMiT191d5jyRhbJKCyjXbzLZ0RNnTuVbwK_QL-e7GHxUMIe-yKwVCmZzvr7_CiDeDEBrV96FVVbUb5KFcS1RFR69JLvQ-t3qZFQ2O-UwwUBCzza1o1FWhRm8plzlbhQpRPxvMa0AyjP4zoDe8fmPfR_SI1GFOTUmVubF8eM98sHGQ7plpkrf9C3-7URw7jRjMoKU7GNfVGI_r6hG9RtWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: ما به قدرتی رسیده‌ایم که معادلات را تعیین می‌کنیم و با کمک خداوند موفق به تحمیل ۳ معادله به دشمن سعودی شده‌ایم
🔹
معادلهٔ اول: محاصره؛ به این معنا که ما دشمن را در محاصره‌ای محکم قرار داده‌ایم که هیچ کشتی‌ای نمی‌تواند از آن عبور کند.
🔹
معادلهٔ دوم: هدف‌قراردادن هرگونه تجمع نیروهای سعودی، در هر مکانی که باشند.
🔹
معادلهٔ سوم: حفظ حاکمیت یمن و مقابله با هرگونه نفوذ دشمن.
@Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/457001" target="_blank">📅 16:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457000">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37f8e3bd1a.mp4?token=OUJ4ARVUdUwdCC1JnOQzxK_IpS-odHWIAJYw5l9Bavjg15u_t6J2jYUAFcgaNF2fX4gqHhxUHJksHWBhnKEBB-EksCWBZTGMGJIcBaXAV-1TZAV3-y4sbtTG9mOz9bND6TaIazePljnO3R9b0veK0p2e5mYWSgLy17FQxPl3shpvGBGZjRDxnN7gxX15xo6mZhN9MzYiKZ-qwWLRD7uGqEGGBn_K5fV1gQb34NWMPiYnrDpZpIcX80Vr_gEDhDdN96Seu-JSbiw0r6XpoMHsId8jFjNFlBq1WaaTYgugltio0K_PXLv5wW2Gi_bhmKWM2xB2X4OH7X4okfwGEo3dZIUsO_r2yBrHpN-Xgn91wAKxLAmFJ6GV-nkcRr-pDDmJul8LZFThNyaEv9y5CFdB_gc-8NvtG4ygWypnYKAtBT08nz6Icig7dtg62M914nFRhbiaOSJGO3F-ImTDXTplMKIEDhCBdY3DplSC-AcqiBIZxdDqn42o0GCTuVVzCdIovs68Pvee999RM4oM4wGYn_gTvA1cYHwxmUVv7E1kE7TAhmzhj3EJ9eXlkCN65-cvX9KMBn3zVapKBEv_X-I5OqMY-O_r-k9uTtgtr5GPTRiqJ9pKwZdVmvHZPT3CuB-5vOITCKsbrYWZBSVvQyURpRN6KnZFldamaS2xHzJ6m08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37f8e3bd1a.mp4?token=OUJ4ARVUdUwdCC1JnOQzxK_IpS-odHWIAJYw5l9Bavjg15u_t6J2jYUAFcgaNF2fX4gqHhxUHJksHWBhnKEBB-EksCWBZTGMGJIcBaXAV-1TZAV3-y4sbtTG9mOz9bND6TaIazePljnO3R9b0veK0p2e5mYWSgLy17FQxPl3shpvGBGZjRDxnN7gxX15xo6mZhN9MzYiKZ-qwWLRD7uGqEGGBn_K5fV1gQb34NWMPiYnrDpZpIcX80Vr_gEDhDdN96Seu-JSbiw0r6XpoMHsId8jFjNFlBq1WaaTYgugltio0K_PXLv5wW2Gi_bhmKWM2xB2X4OH7X4okfwGEo3dZIUsO_r2yBrHpN-Xgn91wAKxLAmFJ6GV-nkcRr-pDDmJul8LZFThNyaEv9y5CFdB_gc-8NvtG4ygWypnYKAtBT08nz6Icig7dtg62M914nFRhbiaOSJGO3F-ImTDXTplMKIEDhCBdY3DplSC-AcqiBIZxdDqn42o0GCTuVVzCdIovs68Pvee999RM4oM4wGYn_gTvA1cYHwxmUVv7E1kE7TAhmzhj3EJ9eXlkCN65-cvX9KMBn3zVapKBEv_X-I5OqMY-O_r-k9uTtgtr5GPTRiqJ9pKwZdVmvHZPT3CuB-5vOITCKsbrYWZBSVvQyURpRN6KnZFldamaS2xHzJ6m08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از دل‌باختگی عمیق و دیرینهٔ مردم افغانستان به امام شهید انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/457000" target="_blank">📅 16:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456999">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc421912e.mp4?token=RFYVsRGFnJiw3KcunRn5QYrQChhG0TQ8KzI3ogrQaXW6avae1xd7B4tgo2VAJDVdfw8ofZ2kSZr7zBF8K3kpUMVCEQD-qSr_vZ4VnP_IxM7-xtVloCi-QRa5ulO66HelOooLW73PLNcauVPlTOeIWCYiTYdWK7p3oClBi1MiVQbrCpMyA1IqTfMpObK1I_rEcfd0hc1UM_PJ3hBzncawbIzHhnrKi8Kdq165IPhAZ_oGAt49alJip_lY4lCgqKMWSZAKbcWy4BmrMEph_UL6rJMCbwSZyTK0ZAs0L_ke1AtG5rsn1bNK87hurtLVRyconmWbTZJ4FJikG7CEO41nrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc421912e.mp4?token=RFYVsRGFnJiw3KcunRn5QYrQChhG0TQ8KzI3ogrQaXW6avae1xd7B4tgo2VAJDVdfw8ofZ2kSZr7zBF8K3kpUMVCEQD-qSr_vZ4VnP_IxM7-xtVloCi-QRa5ulO66HelOooLW73PLNcauVPlTOeIWCYiTYdWK7p3oClBi1MiVQbrCpMyA1IqTfMpObK1I_rEcfd0hc1UM_PJ3hBzncawbIzHhnrKi8Kdq165IPhAZ_oGAt49alJip_lY4lCgqKMWSZAKbcWy4BmrMEph_UL6rJMCbwSZyTK0ZAs0L_ke1AtG5rsn1bNK87hurtLVRyconmWbTZJ4FJikG7CEO41nrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ظهوریان، نمایندهٔ مجلس: طرح آقای سقاب برای سال ۱۴۰۳ است و مختص ایشان نیست.
🔹
تنها تجربهٔ مشابه این طرح در ایران اتفاق افتاد که با شکست مواجه شد؛ این طرح در دنیا تجربهٔ موفقی نداشته است. @Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/456999" target="_blank">📅 15:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456998">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_EEE2j5eTXS4-JxN6-jl28PtzCfl8jNJReX21LGB4VIN8ZXwYi8G2azVrGLeeiIYUMRIOQN8OoxC7UJZF4L_pmJcr6T14r_-6TmO4P7CzPIvcDKR_6kNZT2lgWhvoOSmlZB2IQSUQVCh0s2_IXGE91NCDvwmVOPNaht5ssQOt6TDmTixcEczJkJq-ARuO_qMz0FIBGMae5d445BJtkri4IyfhtWAAc9_Vz_EjTPtWoTxjv0Ahj6FFynWDDY04JjiIVt7jZOYw66YL4dCdp-9qAlo3CyjRWwIFNQbBMSnU6XgnX8LvL4oCLpp-5yGG6wcX90jckQZzY1u1ny2_HrkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصوبه ۴۷۳ چیست؟</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/456998" target="_blank">📅 15:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456997">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3f8c2df6c.mp4?token=HrrywQPZSVXNKATM_-BpXXcJ9tKxobe9SY2_uzNrHL7p9lMq4EDuKz21Lumz5qd577Gv1fgmGMsGCpCYINH6m5jwgxpBlbMzWdievHhgyU59xi15zc3ZivlwzMM97v444zXcIUtnc3iMI3jq0ouanOf8Ve-rX9wSJ5iUn5FDg7JjjTzsu3TNBA2xWiSorgeS1VtMKv-xml8VtScZUOrxBft05uOhnCaWe92tPgAVglaqTNPUrLydv5vPeMdRTuwYDdeoyLr2fCXOGZ4MeEo2ANkXNaOSbcdmzwMMGBOHJZz8qUlhmRzuQz3TTQcwRNZFXArCZlQajzxPaxPtU13KCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3f8c2df6c.mp4?token=HrrywQPZSVXNKATM_-BpXXcJ9tKxobe9SY2_uzNrHL7p9lMq4EDuKz21Lumz5qd577Gv1fgmGMsGCpCYINH6m5jwgxpBlbMzWdievHhgyU59xi15zc3ZivlwzMM97v444zXcIUtnc3iMI3jq0ouanOf8Ve-rX9wSJ5iUn5FDg7JjjTzsu3TNBA2xWiSorgeS1VtMKv-xml8VtScZUOrxBft05uOhnCaWe92tPgAVglaqTNPUrLydv5vPeMdRTuwYDdeoyLr2fCXOGZ4MeEo2ANkXNaOSbcdmzwMMGBOHJZz8qUlhmRzuQz3TTQcwRNZFXArCZlQajzxPaxPtU13KCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ظفریان، معاون مرکز پژوهش‌ها: ادعای کسری روزانه ۱۵ تا ۲۰ میلیون لیتر بنزین غلط است.
🔹
با افزایش تولید بنزین از ابتدای سال تقریبا در مرداد ۲ تا ۳ میلیون لیتر در روز کسری داشته‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/456997" target="_blank">📅 15:39 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
