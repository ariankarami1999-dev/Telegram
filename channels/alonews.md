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
<img src="https://cdn4.telesco.pe/file/t-ntRuMLm1TDik2h166rImzeEhnqVseHb8kNpeQG2Tqsf22YWyOZhmSBGMzBoTRtTDMAE3nJY0uxRP2XctEDIO5MCrCiZEwK5vFLh4isulif_Hh_bh-tynZirV-RFhe8rKljUNi7yJgmTyrsCG0ruO4ImiSgB-zVUWrfCYu_5jmcdfHrZqPwKeU2OSVJ1_DVHR-ICDt9ROO56XVQr27h9haOAIhlt_5rU3v44OEXtSn7r5iLqgwfo58uJQiB9ywpEWFyjQQc_VFVRGqg472E6qnWMwVurAXsv_SeQiCK4g1nF_TOXs32gDpKS7eod2vsIj03qKJ1aiXs9JMTBAjcjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 922K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 03:21:07</div>
<hr>

<div class="tg-post" id="msg-133145">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سی‌ان‌ان: یک مقام آمریکایی اعلام کرد تا زمانی که ایران اجازه عبور آزادانه نفتکش‌ها از تنگه هرمز رو نده، واشینگتن وارد مذاکرات مربوط به تسلیحات هسته‌ای نمیشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/133145" target="_blank">📅 02:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133143">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dU1dhkIgpIERfMFJIAVy5zoVNWjEYwyG1dnr4ayuucTPOuo_LcEMHJnDOHV3PcTdRADxbz7JexI6aCb6mF3d39AbZ5Qfd3vgFItb-Vpipg4Talwddnj-heRwDNbOeBx7Atcwi2DYdhQt2jF1B_K6nvqEDzXI-WalJ7yK6B0sGM_P2rZs4_xrX907_xsLcGPb2zaAcH6XeIq2JeBsWHhcDsfT4lVzYAeVPBXtroi3_ZyAW1CMqr8HUKUs8lMykibjCZ-G5RxXqEPMdUAY-gfZ7RZPpwnzRRwwXiqSxNb2QiG4RjI5TMlBnr5MpcEaf1bOKrQAXVh08jCXVwbrMM-cPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l6ROVyL19MtEa60_oLmE9Du525GXLwL7ymeeUD7MSG_X6aHGU3WbenoaJyKnMc0U3pQ7ZuGgYlDtu6NfWZq54jZfh3Zon7km3tzSuwGCe3KgLW49bVAtkGOqrOZAQKSN5Ud_oyXy7vZujth4Vhsm26VHu-0X8p8LkepEQo9-r9odODz72fqnRfSpBM0K_STrMS836MkO93OnII7PFaeCjL1RwirmDv9n049Mo1TU_ZRo1zEj_HXNVVFV69e1mL6EJPLgHd2IVH0mJSWr4GM0FIBblFdOGDxAGP6WYB2ISSsAij1O7tw_UoAbZMqGiWhrmQ8Nx3o6CsLXWM6D8HTpPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دوستان به شدت دقت کنید این کانال و امثال این فرد کلاهبرداری محض هستند و کوچیک ترین سرمایه ایی وارد نکنید که سرتون کلاه می‌رود
🔴
هر کانالی بهتون گفت برید فلان ارز(لیست نشده تو صرافی‌های معتبر) رو بخرید قطعا کلاهبرداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/133143" target="_blank">📅 01:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133142">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q-v0sv8iQ3-Ps5ZvNlHtfv7g77HfykaiCBOCK46FScNICq5MF5F7dyjpfGXlQRQ5lzQvnVYPaebOiDLVV8vq5z1KnB1zDva7Gl_IkIbmw_QHXhxaOwWcUrAXrN2OFfquMmo89lDamCyP5zsMouStuSAVz--mM1SeitTHdqq2uf8DYK8qAJNSUypQxJZ-_omZrULgbc64WtOVOhLEkl-ao2ZWhjeV1ToZkBJFaYErJbg6hI14PzXGhoOgqD-WJeMecGqUUGRYNq0Hewp0eLOxZJmoJPV8cAf18YuzwC2gyHU30ZwhpSX-8KzykeXXW7-64nbKn2N9YAwx66FWIKLA_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الناز شاکردوست به دلیل استوری اعتراضی در دی ماه به دادگاه احظار شد!
🔴
جرم: امنیتی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/alonews/133142" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133141">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
باراک راوید، خبرنگار آکسیوس:
به گفته مقام‌های آمریکایی، آمریکا به ایران تا شنبه فرصت داده که رسماً حمله به کشتی‌ها و اتفاقات تنگه هرمز رو محکوم کنه و اعلام کنه که تنگه هرمز برای عبور کشتی‌ها باز و امنه؛ و اگه ایران این درخواست رو قبول نکنه، عواقب سختی درانتظارشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/133141" target="_blank">📅 01:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133140">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsDWieD_sMG-5h5_inS9pOV8yNvf5EaGge0F2kvcfjZ0qzC0NU6UhrbC6rOP_fHr3ATJFBi0UpYMIMuoGqU-tx2SSEyUG_IvVo-1ELkiSKrLVrCjqLA0YgYgGvk6mRScA_7BLKvvbhxJsuFMNHfUYbDJC2T9_nD73vBYnugcayoLamBFlVjna6g2PHYgQAMp_X3hIuWiINFfed1x7ez6rKsRmdlp6_Qs1aZVITF9_mZFJWUvV0MXyybp0pN4rTCrQ6S0VsY-vNrdcxGqcOx6j8omYWgff_Kt3kvv8F4hLYUtIqssoC75SHLcbP1BManSmchZtI1S_43vUvoJp7kzGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
اگه میشد خودم خرخره ترامپ رو میجوییدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/133140" target="_blank">📅 01:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133139">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">تیم ملی ایران هنوز شانس صعود داره
‼️
اگه سر تیم‌های بلژیک، مراکش ،سوئد ، ژاپن، آمریکا، کانادا، پرتغال، پاراگوئه، آلمان، برزیل، مکزیک، مصر، کلمبیا، آفریقای جنوبی، اتریش، کرواسی، بوسنی، سنگال، ساحل عاج، اکوادور، کنگو، الحزایر، استرالیا و غنا، بلایی بیاد یا هواپیماشون سقوط کنه
تیم ملی ایران صعود خواهد کرد
شانس: 0,0000000000000000001%
@AloSport</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/133139" target="_blank">📅 01:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133138">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/13ba9b7985.mp4?token=LXm6yooOqJFzimUdwfN2B3d2zZllv9c66QWf-OlzWbxUXtH1G9ioMx2cxMkOW7b14gTPtZmMTAvqSs7ELv8l8jeUyOxkgN_UFOd8wqfF7wFFU_LMHhaYN3M1gC0xiseDBvGBBS8KzhN-GDaRNsBRHUK7yhgwvHFl6-1lnwQ_vwGrEgLr_waZj-NEgKUIo6ygXtMVlOWOdWMWlTRVq-s8rEuIuklZO-zWeM6pDEpst5UvOPmiE5Z7jPVDdGPmNyFy4FTcwdpT2TiqPuvdbDgIHLgI5YX3ltwYe4bix7BAp4x7iKP6k9YPEZlEKUtvZNR6xvo4dEA_X55UPWwhTxC2yg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/13ba9b7985.mp4?token=LXm6yooOqJFzimUdwfN2B3d2zZllv9c66QWf-OlzWbxUXtH1G9ioMx2cxMkOW7b14gTPtZmMTAvqSs7ELv8l8jeUyOxkgN_UFOd8wqfF7wFFU_LMHhaYN3M1gC0xiseDBvGBBS8KzhN-GDaRNsBRHUK7yhgwvHFl6-1lnwQ_vwGrEgLr_waZj-NEgKUIo6ygXtMVlOWOdWMWlTRVq-s8rEuIuklZO-zWeM6pDEpst5UvOPmiE5Z7jPVDdGPmNyFy4FTcwdpT2TiqPuvdbDgIHLgI5YX3ltwYe4bix7BAp4x7iKP6k9YPEZlEKUtvZNR6xvo4dEA_X55UPWwhTxC2yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه دختر دهه هشتادی: من خودم جز جوونای معترض ۱۸ و ۱۹ دی بودم.
اما بعد از شهادت رهبر فهمیدم ایشون چه شخصیت بزرگی بودن، خاک تو سرم که دیر فهمیدم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/133138" target="_blank">📅 00:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133137">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
آکسیوس:
دولت ترامپ خواستار آن شده است که ایران طی بیانیه‌ای عمومی که قرار است روز شنبه منتشر شود، اعلام کند که تنگه هرمز برای تردد کشتی‌های بین‌المللی باز است و متعهد شود که حملات به کشتی‌های تجاری را متوقف کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/133137" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133136">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e875fd4fb2.mp4?token=gcgtoS14XPZMKk1WBzJ6PWQL1K_uP2iXlippep0fubfQS38pn-v3mn6pBDqfZYl_KIziaU5p5Xxrecw5U7eIYIz8z06nizfEtlhjoEOJHARtKpuYZ5CP0MGmLfE60FZcn2Fvpzum3QrRTgcLnqj9UmX6xgQ_jnT3fUmUybcC9WjhPyHbp8IKZJrFyZ7ePibBL1IlruWUWPpAvbD2E8Gwx97q7Ep8dxwToRxQFqPh88IkgPcpErXWsOckfr46V2hQob2AU2UXSFCdgUbbKD12ODsBjF0xspY5IP-ezZT72DoiAUCd-kPgROEI_Sr13N01T9_VyjgDfh5B2hann86Acg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e875fd4fb2.mp4?token=gcgtoS14XPZMKk1WBzJ6PWQL1K_uP2iXlippep0fubfQS38pn-v3mn6pBDqfZYl_KIziaU5p5Xxrecw5U7eIYIz8z06nizfEtlhjoEOJHARtKpuYZ5CP0MGmLfE60FZcn2Fvpzum3QrRTgcLnqj9UmX6xgQ_jnT3fUmUybcC9WjhPyHbp8IKZJrFyZ7ePibBL1IlruWUWPpAvbD2E8Gwx97q7Ep8dxwToRxQFqPh88IkgPcpErXWsOckfr46V2hQob2AU2UXSFCdgUbbKD12ODsBjF0xspY5IP-ezZT72DoiAUCd-kPgROEI_Sr13N01T9_VyjgDfh5B2hann86Acg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منوچهر متکی وزیر اسبق امور خارجه:
اسلام‌آباد یک پلن فریب بود، اگر تیم مذاکره‌کننده هنوز به این باور نرسیده، جلسه بگذارد تا برایشان توضیح بدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/133136" target="_blank">📅 00:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133135">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGpNa8KLJPja5d2WzgOu2y71x6GhGY-yaX7f72IvjLBvE1YdzjFmXB1eoVlkMYGuI3zXtXuwGGhq5oOz_undn3sSMFAIf63Rkygwv34gG24K9yjgfwhkx6q3Mzmg7DKG8SEq2ALNsBbcUYF5yGkFiLOa45wzFf8m8gVBvp0jVNEIcWVm4WU3YyfJHLEx9ocbxw8eDt0Xo67oOQFJcLL_iM7SKMA6EIl7CcHg7TDs9YCYXSlCkm-cmFhBH3eDAH8QobsPf31t_9UPEVtwfl0x-GSgZ2oUh5RTtxJnbXKUUIyNU0dQsX9yiKzNqVWxBvWK7PnaxvFClNhrGFxwshCrdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
تماشا برای زیر 18سال ممنوع
‼️
❌
ویدیویی منتشر شده از سواستفاده جنسی از کودکان در جزیره
اپستین
!
🚨
مشاهده برای افراد زیر ۱۸سال و افراد دارای مشکلات قلبی ممنوع است
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/133135" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133134">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
معاون اطلاع رسانه آموزش و پرورش:
شنبه جلسه‌ای در رابطه با تصمیم نهایی مربوط به امتحانات و تعویق یا عدم تعویق برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/133134" target="_blank">📅 00:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133133">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbP2K_dgIUvRPAq1X-ekG4JaahxrzAy6dhU9AP4ASOh5LEbP7cFzY9yYi23voYabmRIfPDphLPiSK92GrGfaSCp6Yf6yqSlpaiE099MdzeE2m-75z06NBO0Lv-i1hqhaVInMITXuojdz008IBLUQ6-y1s1mf5xl_z6nNna2rgdy4UXranap24YsOqn43qVPalpbmEZKHrPqF4VaNUA872FOqWeIDHRlsBZ1IvyqjLZ5LGC-EpVafjVLUM6YOY0xqw9-xjOIMMhWGoVnTv15q_MGGDAkcwGtRwFT1fiWLpMPpRf8MdX1K0GtsluQH7YcVEd9T0gS6JM82XmawqI_yDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هادی چوپان:
یه جون دارم اونم برای آقا مجتبی میدم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/133133" target="_blank">📅 00:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133132">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری / العربیه به نقل از یک منبع مطلع:
تیم‌های فنی آمریکایی و ایرانی در تاریخ ۱۲ جولای (۲۱ تیر ماه) در پاکستان با یکدیگر دیدار خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/133132" target="_blank">📅 23:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133131">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده: ما هیچ درخواستی برای مذاکره با آمریکا نداشتیم؛ اما درخواست یکی از میانجی‌گران منطقه‌ای برای سفر به ایران را رد نکردیم
🔴
این دیدار در مشهد انجام شد و دیدگاه‌هایمان را به طرف قطری اعلام کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/133131" target="_blank">📅 23:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133130">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
خبرنگار الجزیره: احتمال برگزاری دیداری بین ایران و آمریکا وجود دارد که مکان آن ممکن است ژنو، اسلام‌آباد یا دوحه باشد
🔴
برگزاری این دیدار منوط به موفقیت میانجی‌ها و توافق بر سر فعال‌سازی باقی‌ماندهٔ مفاد تفاهم‌نامه است؛ پروندهٔ تنگهٔ هرمز نیز ممکن است به این دیدار موکول شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/133130" target="_blank">📅 23:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133129">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHzE1bX0Z3j4AJvJ1pj13RpxFCVzgK8EQF0TEoTVQA14BCMOjtEThBeZBf2SLLKcIRRS1iFuaRrhLUwwg2y6_9tHtGnOUfd_gtJCiBtLnyDc7rHvQSi1L6gtBOqOIA87OMRWe6bLOViDJQGMZnNQyEkrAqcYyx_9mZSkp-B28-IVeicMHedjeg_xFrca30mwsSoNU1qMy5tt2DLAwRzn2DH-z0uxBWSj37CXTKJ2vwbVZPjTfxN2_AfcS-iEo9gT1WVbPDtF6kyJljAMEcL7XoGaKXXK7687ZyMcBsLImNAVpnb2LHaVxRNqxqjWsklWzs2ZiAY_wveuqavXEJVEeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکاردی در تجمعات شبانه: هرکس مانع قتل و قصاص بشود؛ خودش گزینه قصاص می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/133129" target="_blank">📅 23:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133128">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b106bf152e.mp4?token=ReMMUKdPERNIyr8U79W4_BP8wGO-TqU4v8zxjEdIovNyYp80gBJ7em4fn0rtnYHIKGJIlBnivrTZRfKsvntv6zQIsL6j6w-LzqwweB5jTRZlBF7USMSJEgSOShLHuOWYwgCfmzHNJZyRTOnEcCpJDHfeWERe-quiRY175Tc0IVqd_RB_yJWo0HSGYiMwfAHWgMrIATt4pEuAiFAor1duWOgdJycrZlcspsahV-J_CvpKwMd_pjXb7efl1FPvBCpoUk0Co9gyBFMRZsUuYsGBKZkko3y0PdI2IOwaC_71hJtzp_mk1qYlX7dXbcU_iz__oOBgPnkaaCsqWDrK-pR_OIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b106bf152e.mp4?token=ReMMUKdPERNIyr8U79W4_BP8wGO-TqU4v8zxjEdIovNyYp80gBJ7em4fn0rtnYHIKGJIlBnivrTZRfKsvntv6zQIsL6j6w-LzqwweB5jTRZlBF7USMSJEgSOShLHuOWYwgCfmzHNJZyRTOnEcCpJDHfeWERe-quiRY175Tc0IVqd_RB_yJWo0HSGYiMwfAHWgMrIATt4pEuAiFAor1duWOgdJycrZlcspsahV-J_CvpKwMd_pjXb7efl1FPvBCpoUk0Co9gyBFMRZsUuYsGBKZkko3y0PdI2IOwaC_71hJtzp_mk1qYlX7dXbcU_iz__oOBgPnkaaCsqWDrK-pR_OIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون کرمانشاه آتش سوزی کمربندی نزدیک به میدان شهدا
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/133128" target="_blank">📅 23:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133127">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
مدیریت بحران آذربایجان شرقی: آتش‌سوزی نیروگاه حرارتی تبریز ناشی از نقص فنی در نقطه اتصال به شبکه برق بوده و شایعات درباره حمله به این نیروگاه صحت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/133127" target="_blank">📅 23:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133126">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ایروانی: اگر آمریکا به نقض تعهداتش ادامه دهد، ایران دیگر ملزم به اجرای تعهداتش نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/133126" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133125">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ناسا به دنبال ۴ داوطلب برای گذراندن یک سال در یک مأموریت شبیه‌سازی‌شده به ماه/مریخ است.
🔴
شرکت‌کنندگان در زیستگاه‌های منزوی زندگی خواهند کرد، غذا کشت می‌کنند، سلامت خود را پایش می‌کنند، پیاده‌روی‌های فضایی شبیه‌سازی‌شده انجام می‌دهند و خود را با روز مریخی که ۴۰ دقیقه طولانی‌تر است، وفق می‌دهند.
🔴
هدف، مطالعه اثرات فیزیکی و روانی مأموریت‌های فضایی با مدت طولانی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/133125" target="_blank">📅 22:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133124">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
عباس عراقچی، وزیر امور خارجه فردا با یک هیئت دیپلماتیک به عمان سفر خواهد کرد تا در مورد روابط دوجانبه و تحولات منطقه‌ای گفتگوهایی برگزار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/133124" target="_blank">📅 22:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133123">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLEMGvVGpcWh76zu4YaIAJNLG5AzEnahb_SybVYD13EPRMtSnSVS0WY-r_wFD7tgHQbRU5W9WdrZYaUpmBaGJMlnTXj8WiZK7kJRx15pwzl9sf2y3Rm5w2OfPH3yW5AjpS1_PrPBuN0enhYrBpjX7-br7kb5vVOpmSl6TIVOlrqUP2umMMoEAdBYUjmlOb3IHKwInbCVrHWou6V-fK9HUchgo6bCLtZbc22pE8eQGlrJ09xVZEpAm7LOgrkeCkWiPOG1CPYvTv1jENprpzVwSwA67-ypsso6J0aeU3zTTvmGrYouAYZ-0f4qYGXnyCVb4IfFMv2tuJHJ-NefBrF9CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین یه حمله بزرگ با حداقل 270 پهپاد به سمت زیرساخت های غرب روسیه انجام داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/133123" target="_blank">📅 22:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133122">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وزارت بازرگانی آمریکا روز جمعه کنترل‌های واردات کالا به امارات را کاهش داد و صادرات اقلام نظامی، برخی ماهواره‌های تجاری و تراشه‌های هوش مصنوعی را تسهیل کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/133122" target="_blank">📅 22:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133121">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
العربیه:
وزیر کشور پاکستان احتمالاً به زودی از تهران بازدید خواهد کرد
🔴
العربیه از قول منابع خود از احتمال برگزاری یک تماس تلفنی چهارجانبه بین آمریکا، ایران، قطر و پاکستان خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/133121" target="_blank">📅 22:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133120">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری / وزارت خزانه‌داری آمریکا تحریم های جدیدی را علیه ایران اعمال کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/133120" target="_blank">📅 22:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133119">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ef9e8b4c7.mp4?token=UIUf8z3f8n9Uz6zfa6N8oc1PeKqt29ncA230FUYRciIh1yc67Brh3KY4B0G8NC913nrGrsPkl1h2r0kQ5iKq_BayrrLrY99yI14X3nqx3H_6zPVkWmajBW6232HHFcpnCSP1jE0TAT2jimlo-YYoGDPS_ubpAbG2vtLZs8kGybeMg8E4LOVIsAhTmeXN_TKFQgVzpVDfabx4TqhOljfvPSnLJeZNAxyJGUpXOqdFJWtedUfQMjWUcKmW5TvcKi2EBkqsnw1iDiHLMdhEuYZd6UQxSfIXRE2SC7zOWv1sg-gXxem9K4-3RXwYwLXts1HbhXk-eK3rCwu4GXZ4doqgkGEhyFgug8f5_1tk_sMnBi3erQJLDDLiqKhR9MkbkTKfN0F2FvxcDW085RZPlv53FpewfpLrp513FmbsZjQJkgYUrt0NjP-fs7GJAc6rXFpgWt3maPn2Xbg3OlCvys_D1SCLRwueyZf7sQdp0mul-afqOp3KXjZeNf62zwZ0m8aMpAdsDC0hRiW5QSb72xtEY2eKVTCYoCfIPstiYDXFHitAR0_KGWcF2fZhpdmE7d3PpuzPzDyWCkSSTlCXAm9jU3Cn_YnY_1O_y1h02H5hJEB1n-oVNhtoV6KVZcTwkYz6gBm1_T_JMx7mtxNbfPTaLfib_s2y6ZTHJx2aElgnNeY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ef9e8b4c7.mp4?token=UIUf8z3f8n9Uz6zfa6N8oc1PeKqt29ncA230FUYRciIh1yc67Brh3KY4B0G8NC913nrGrsPkl1h2r0kQ5iKq_BayrrLrY99yI14X3nqx3H_6zPVkWmajBW6232HHFcpnCSP1jE0TAT2jimlo-YYoGDPS_ubpAbG2vtLZs8kGybeMg8E4LOVIsAhTmeXN_TKFQgVzpVDfabx4TqhOljfvPSnLJeZNAxyJGUpXOqdFJWtedUfQMjWUcKmW5TvcKi2EBkqsnw1iDiHLMdhEuYZd6UQxSfIXRE2SC7zOWv1sg-gXxem9K4-3RXwYwLXts1HbhXk-eK3rCwu4GXZ4doqgkGEhyFgug8f5_1tk_sMnBi3erQJLDDLiqKhR9MkbkTKfN0F2FvxcDW085RZPlv53FpewfpLrp513FmbsZjQJkgYUrt0NjP-fs7GJAc6rXFpgWt3maPn2Xbg3OlCvys_D1SCLRwueyZf7sQdp0mul-afqOp3KXjZeNf62zwZ0m8aMpAdsDC0hRiW5QSb72xtEY2eKVTCYoCfIPstiYDXFHitAR0_KGWcF2fZhpdmE7d3PpuzPzDyWCkSSTlCXAm9jU3Cn_YnY_1O_y1h02H5hJEB1n-oVNhtoV6KVZcTwkYz6gBm1_T_JMx7mtxNbfPTaLfib_s2y6ZTHJx2aElgnNeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فحاشی های هانتر بایدن پسر بایدن به دونالد ترامپ: چطور ترامپ از این کارها جان سالم به در می‌برد؟
🔴
چرا هیچ‌کدام از همکاران سابق شما به او نگفتند: «برو در ماتحت رو بزار، آقای رئیس‌جمهور»؟
🔴
عذر میخواهم... پدرم واقعاً می‌گوید: «توهین نکنی ها، هانتی»
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/133119" target="_blank">📅 22:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133118">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری / وزارت خزانه‌داری آمریکا تحریم های جدیدی را علیه ایران اعمال کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/133118" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133117">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فایننشال تایمز: آمریکا یه هیئت فرستاده بیروت
🔴
تا به حفظ آتش‌بس بین اسرائیل و حزب‌الله کمک کنه و نذاره این آتش‌بس به هم بخوره
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/133117" target="_blank">📅 21:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133116">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سناتور ارشد جمهوری‌خواه لیندزی گراهام: ما با کاخ سفید بر سر نسخه‌ای از لایحه تحریم‌های روسیه که آن‌ها از آن حمایت خواهند کرد، به توافق رسیده‌ایم. این بدان معناست که این لایحه به قانون تبدیل خواهد شد.
🔴
من همراه با سناتور بلومنتال به نزد رهبران جمهوری‌خواه و دموکرات خواهم رفت تا ببینیم آیا می‌توانیم زمانی را برای پیشبرد این بسته تحریم‌های روسیه پیدا کنیم که ابزارهایی را به رئیس‌جمهور ترامپ بدهد تا به پایان دادن به این جنگ کمک کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/133116" target="_blank">📅 21:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133115">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
بزالل اسموتریچ، وزیر دارایی اسرائیل، اعلام کرد که طرح‌هایی را برای ساخت سه شهرک اسرائیلی در شمال نوار غزه آماده کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/133115" target="_blank">📅 21:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133114">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
صندوق بین المللی پول IMF پیش بینی کرد رشد اقتصادی ایران امسال منفی ۵.۴ درصد خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/133114" target="_blank">📅 21:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133113">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
پهپادهای اوکراینی شب گذشته به ۱۳ شناور در نزدیکی کریمه، از جمله ۱۰ تانکر، یک کشتی باری، یک کشتی مسافربری و یک یدک‌کش، حمله کردند.
🔴
در ۱۲۰ ساعت گذشته، به ۴۸ شناور حمله شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/133113" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133112">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oL0Froa6X-JiD5QVtT5Ex_Zai60TlN-uLOwESIUyXMm-hUQCHqRMt2jO20am4d6a73IQENpGdzoKxVqq75Q4DjOMFkHHLY8bbWDARdUa8LiKrAqjbdYosSitRc7SyvnYb-mXc38EM0VJHuIlPLhu8_WaM6cjXRPQRXKhEkVE4tzKOrJYwp3WHZqddndjcwzOqsv7G5RWuT9aaATScH9WwRVqDme-2gZ2EygWjUx62kmI461iJaN-Ru_-U5QkkHkavcb1piCAVDqlhpEvwkJ-mq1_8bON_WRQaaaK8D3UwG-6MEmFWvAE7b-gugIEKGTPTY8AHH14YqQr6BEpJPtR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار CBS: مقام‌های ایرانی روز شنبه برای گفت‌وگو درباره تنگه هرمز و اختلاف بر سر مسیرهای کشتیرانی که از آب‌های سرزمینی ایران عبور می‌کنند، به عمان سفر خواهند کرد.
🔴
میانجی‌های قطری به‌تازگی مشهدِ ایران را ترک کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/133112" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133111">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
شهباز شریف در تماس با پزشکیان: ایران و همه طرف‌ها خویشتن‌داری کنند.
🔴
بر ضرورت پایبندی به مفاد تفاهم تاکید می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/133111" target="_blank">📅 21:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133110">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
منابع خبری اسرائیلی از سقوط یک هواپیمای سبک در فرودگاه این ورد واقع در منطقه شارون خبر دادند.
🔴
بر اساس اعلام این منابع، در جریان این حادثه دو نفر مجروح شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/133110" target="_blank">📅 21:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133109">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d149dc62f3.mp4?token=H2ExFIBl8F7B2weNIVm7VMQmNKWLIBQKYInzBU7qvoE6UR0ec8l4Sv3AnldHiouYtbPkCjk2OlwGEk-tUCJjChXNXDibrALl8QLyryAN6cX5QhAz9l0bDQt605eAxAa1JACfmhZ7k_c8Xb4wjlZ3JZqaLHwh7rbqz4OdmxHm82B3jAfhG5NtTtsq31d48Yu21JlXHbBCvmUyiSj3NjdFs9hC3v2HQRUct2jM8_qbJlowqu5HLfFKeLmcFLeXvcG28Hf5Hf8kZJ_w3gGWWRiaOAIlv0giF3fqWmyR9PdqGWL9sI6izHu8Sh8NpbxndJAoHDMhhotjVV-y41-mcGK6BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d149dc62f3.mp4?token=H2ExFIBl8F7B2weNIVm7VMQmNKWLIBQKYInzBU7qvoE6UR0ec8l4Sv3AnldHiouYtbPkCjk2OlwGEk-tUCJjChXNXDibrALl8QLyryAN6cX5QhAz9l0bDQt605eAxAa1JACfmhZ7k_c8Xb4wjlZ3JZqaLHwh7rbqz4OdmxHm82B3jAfhG5NtTtsq31d48Yu21JlXHbBCvmUyiSj3NjdFs9hC3v2HQRUct2jM8_qbJlowqu5HLfFKeLmcFLeXvcG28Hf5Hf8kZJ_w3gGWWRiaOAIlv0giF3fqWmyR9PdqGWL9sI6izHu8Sh8NpbxndJAoHDMhhotjVV-y41-mcGK6BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
داده های ماهواره‌ای امروز دو اصابت آشکار در باند فرود در فرودگاه بوشهر در ایران را پس از حملات اخیر ایالات متحده نشان می‌دهد.آثار سوختگی نیز در اطراف باند قابل مشاهده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/133109" target="_blank">📅 21:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133108">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
تسنیم :  انفجار در قائمشهر را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/133108" target="_blank">📅 20:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133107">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
کان: ایالات متحده از اسرائیل خواسته است که از انجام هرگونه اقدام غیرمعمول در جنوب لبنان خودداری کند. بر این اساس، رده سیاسی به نیروهای دفاعی اسرائیل (IDF) دستور داده است که تمام عملیات حساس در جنوب لبنان را متوقف کنند. این دستورالعمل به IDF تا اطلاع ثانوی و تا زمانی که مشخص نشود تشدید فعلی تنش بین ایالات متحده و ایران و مذاکرات بین اسرائیل و لبنان به کجا منتهی می‌شود، معتبر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/133107" target="_blank">📅 20:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133106">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiSWS1InBAvwfbSb7cYdb9GedIfXBuQQz4H0sGRIS4_ac5eDPIJCKVfVXyl7pPh14UJrk4Gsc7q7ZhEJAXnhqb6o67CqocpufXIzVM5xkEa49GXthsPc3aR7Hsscvhh3358L6I71Ej3Mn6KhWyw9N-78labPZ7FFh50zEdzBbZwI3IJhCgwIxzD-wGeEMJdRDjL3DXxrAK55ps24N86EG2WakUQfzM4dnkIoZwm7fcVJGU5IV8aZWjAfBshWjGDD3nhKMeFdoRLVGUnE45O-TVNcvGHH7mfnYzX10NDqT8k34gKnBI0YIfPTug4EAVqHoolZXnRqOkC-crttDHnA1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شورای اجرایی «سازمان بین‌المللی دریانوردی» (IMO) در نشست روز جمعه ۱۹ تیر، با صدور تصمیمی، تلاش‌های ایران برای تحمیل حاکمیت بر تنگه هرمز و ایجاد نهادی جهت کنترل تردد در این آبراهه را به‌شدت محکوم کرد. این شورا از تمامی کشورهای عضو خواست تا حاکمیت جمهوری اسلامی ایران بر این تنگه و صلاحیت قضایی آن بر مناطق دریایی کشورهای ثالث را به رسمیت نشناسند.
🔴
این تصمیم در حالی اتخاذ شد که تنش‌های نظامی اخیر میان جمهوری اسلامی ایران و آمریکا و حملات متقابل دو طرف، نگرانی‌ها را درباره امنیت منابع جهانی انرژی و ایمنی کشتیرانی افزایش داده است. پیش‌تر، نهادی تحت عنوان «سازمان تنگه خلیج فارس» در ایران اعلام کرده بود که تردد کشتی‌ها منوط به دریافت مجوز از این نهاد است؛ اقدامی که از سوی شورای سازمان بین‌المللی دریانوردی «مداخله در ناوبری بین‌المللی» خوانده شد.
🔴
در مقابل، هیئت نمایندگی ایران در سازمان بین‌المللی دریانوردی، ضمن رد این اتهامات، آن‌ها را «سیاسی و فاقد مبنای قانونی» خواند و تاکید کرد که ایران به دلیل عضویت نداشتن در کنوانسیون حقوق دریایی سازمان ملل (UNCLOS)، خود را ملزم به رژیم حقوقی مبتنی بر این معاهده نمی‌داند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/133106" target="_blank">📅 20:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133105">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
قالیباف : تنها با کسانی می‌توان با آمریکا مذاکره کرد که برای جنگ آماده باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/133105" target="_blank">📅 20:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133104">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
قالیباف : این درگیری با تسلیم شدن ایران تموم نمی‌شه
🔴
اگه آمریکا به تفاهم‌نامه عمل نکنه، ایران برای دفاع کامل آماده‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/133104" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133103">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رویترز: کاهش فروش نفت ایران به دلیل تغییر رویکرد شرکت‌های چینی که به سمت خرید از بازارهای دیگر در منطقه گرایش پیدا کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/133103" target="_blank">📅 20:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133102">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: ترامپ مدیریت پرونده ایران را در دست دارد و اسرائیل در این معادله نقشی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/133102" target="_blank">📅 20:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133101">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e41Xk20WT-zVxmLf_i-tILz-mVLRN2IbZG91-skDhXxk1SC_-8MgetdACWqNZ9BcyRCMvb6eBI-Vl6coYj1sm27zp2nKtyhPeXNBd59aUz2iVfHroKgy711GyuuzsTwpE5jl4evSEWNPzs9le2Hw2glajcinxzvhmqgFHqv2sqovkNvh2KaKhR6Gq5RYZkbjK4opxlkqXKwnXWo3ylJHbMlxnmAl8pFuPoEft-lo2Sp-ADC6LH8Teeh_P6DPiD0WdU4cdizqz85MlK1cx4-BCGz-gkqpzHslYv1Pq5mTwNsbXdohbzgF5qEMXJLmE6CJOXqUwzNGI6xtQqghnpf4cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیلی : ترامپ بوزینه‌ای است که نام انسان را سرقت کرده و مانند یزید، به زباله‌دان تاریخ خواهد افتاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/133101" target="_blank">📅 20:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133100">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزارت بهداشت لبنان : بر اساس آخرین آمار، از آغاز حمله اسرائیل در دوم مارس، ۴۳۲۱ کشته و ۱۲۲۰۰ مجروح شده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/133100" target="_blank">📅 20:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133099">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
جوزف عون ، رئیس جمهور لبنان: مذاکرات مستقیم با اسرائیل ادامه خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/133099" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133098">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=clpxHV5l5a5ZnVvWmK5704QFABP1Juwm0KjJHtVZsqWTvYazeaRHiJ62Nw69gXihcSoEqzJ6WpN-46H0Zsnrl_mglt0Y94ybenoD7EEJzVoxWcO0NHwu83SMklZoNG1TXmeht0tGWmihRGPA_szXj0tjpRmSbl_btSXMngzpk6Uldv3Q6YWBkumRm8wQLJRnL8j0xQ4Yp4k7_JKfzw3aD9Ondk1DFZqF65yfLM_frapf6SWN9ieyWvrfXdtYr6WPj77K4YMiWfTPBuV8M-ZRCEXFVIUtFZt3Etxw4zFV9Ja_dSQgqDx0dxgi7Beu4KB7Ses-4KgKmOS4r6HEr3w1Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=clpxHV5l5a5ZnVvWmK5704QFABP1Juwm0KjJHtVZsqWTvYazeaRHiJ62Nw69gXihcSoEqzJ6WpN-46H0Zsnrl_mglt0Y94ybenoD7EEJzVoxWcO0NHwu83SMklZoNG1TXmeht0tGWmihRGPA_szXj0tjpRmSbl_btSXMngzpk6Uldv3Q6YWBkumRm8wQLJRnL8j0xQ4Yp4k7_JKfzw3aD9Ondk1DFZqF65yfLM_frapf6SWN9ieyWvrfXdtYr6WPj77K4YMiWfTPBuV8M-ZRCEXFVIUtFZt3Etxw4zFV9Ja_dSQgqDx0dxgi7Beu4KB7Ses-4KgKmOS4r6HEr3w1Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در شرکت اکسین پالایش پلدختر
🔴
فرماندار پلدختر از وقوع آتش‌سوزی در شرکت اکسین پالایش سراب حمام خبر داد و گفت نیروهای آتش‌نشانی و امدادی در حال مهار حریق هستند.
🔴
به گفته وی، آتش‌سوزی از انبار مواد دفعی آغاز شده و تاکنون هیچ تلفات یا مصدومیت جانی نداشته است. علت حادثه در دست بررسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/133098" target="_blank">📅 20:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133097">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نماینده آمریکا در سازمان ملل: در دیپلماسی با ایران همچنان باز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/133097" target="_blank">📅 20:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133096">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
الحدث: ‏تماس تلفنی نخست‌وزیر پاکستان با پزشکیان و بررسی تحولات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/133096" target="_blank">📅 20:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133095">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
نماینده روسیه در سازمان‌های بین‌المللی واقع در وین : روسیه خواستار تفاهم کامل ایران و آمریکا و حل‌وفصل جدی مسائل موجود است.
🔴
ایران و آمریکا باید راهی برای برون‌رفت از وضعیت کنونی پیدا کنند، در غیر این صورت وضعیت در منطقه خلیج فارس بسیار پرتنش، ناپایدار و خطرناک خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/133095" target="_blank">📅 20:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133094">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
فارس: درپی انتشار اخباری از سوی العربیه و فاکس‌نیوز درباره برگزاری دور جدید مذاکرات ایران و آمریکا در هفته آینده، پیگیری‌های خبرنگار فارس از یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایرانی بیانگر این است که این ادعاها صحت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/133094" target="_blank">📅 19:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133093">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
شورای شهر تهران: رایگان بودن مترو و بی‌آرتی در تهران تمام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/133093" target="_blank">📅 19:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133092">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
چین و روسیه قطعنامه شورای امنیت درباره برنامه‌ هسته‌ای ایران را مسدود کردند
🔴
روسیه و چین پیش‌نویس قطعنامه‌ای را که با هدف بحث درباره تحولات برنامه هسته‌ای ایران و اقدامات مرتبط با آن تهیه شده بود، مسدود کردند.
🔴
مسکو و پکن تأکید کردند هرگونه اقدامی در شورای امنیت باید با هدف حمایت از روند دیپلماتیک و تشویق گفت‌وگو باشد.
🔴
هر دو کشور معتقدند که رسیدگی به موضوع هسته‌ای ایران باید از طریق مذاکرات و آژانس بین‌المللی انرژی اتمی انجام شود، ضمن اینکه امکان احیای توافق هسته‌ای نیز حفظ شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/133092" target="_blank">📅 19:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133091">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xz_zjn6AqzquCoNLtrytKY4H3MNbGc25UfYVJ1tKK8ObJybnCU5t5HunIdrEwbXSfZmpittOplaNRGSDEwMHBoqTPXLUCwAS6_LQnJEWACDDu-b79RjvEmAvlYCCiSotJ7xKXgYP5OqHuwvA55jp17q4KL0R6YhIM3-mv0S-Z9bD-HmLbJ22yDcklbRyykmnNMyHA3TvcwtUppcXMC1-N3a6XVnzAcvodBrrma6jegU-kudlQ3odsDN9iIA4ylHzxx8B-vlPMcCOUBKwj5D9nBHzoxKeVchUm9bzhs5UjN3_2KE7fr2sOhekIWg4eopr6W3Axd5i_jVrqj_NbAP3Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی، نزدیک به تیم مذاکره : ترامپ و آکسیوس رو نادیده بگیرید
🔴
تا وقتی دولت ترامپ به تعهداتش عمل نکنه، هیچ مذاکره‌ای انجام نمی‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/133091" target="_blank">📅 19:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133090">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
اف‌بی‌آی جزئیات جدیدی درباره یک طرح تروریستی علیه رویداد یو‌اف‌سی در کاخ سفید فاش کرد:
🔴
«ما متوجه شدیم که این گروه به‌طور ادعایی قصد داشت حمله‌ای با تلفات انبوه را با استفاده از پهپادهای مسلح به مواد منفجره و سلاح‌های آتشین برای شلیک به مردمی که در میان جمعیت فرار می‌کردند، انجام دهد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/133090" target="_blank">📅 19:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133089">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ngPf_gq2HfzrQTiu4ClWlSy409MB7W6X9TNjCriweZBuNoyxgYXWnEPZ1MgHfYZvEYmAMpwWtsCt3nWlOWfurr9NGVZfGxYd1WqEonuwuhT_RkG988p9GkROdjNf41CYL-dBAj348tT0n3zJnoWZDIaeszJpf6RcHv-jw-AX0RJXi_9HpyUWyntK2kvNu5Vy1uC3FTcvixlzE-iunSUcyxfruifxPzmraicJzSc-0Gqg3s8YFOiEDeZdRhGAVAJsNMMWzlZtswWXzG-r-_I1pwqcrdcVlHloH3E8tHa1_HHm5vMajORiNtmnlZE7mYvWv0lTZn5-CXTHiVYzY0epiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: دور جدید مذاکرات ایران و آمریکا، هفته آینده توی سوئیس برگزار میشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/133089" target="_blank">📅 19:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133088">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
نماینده پاکستان در شورای امنیت: ما به دنبال دستیابی به توافقی جامع بین آمریکا و ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/133088" target="_blank">📅 18:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133087">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سی‌بی‌اس: ونس، ویتکاف و کوشنر در تماس با مقامات قطری در چارچوب تلاش‌ها برای تقویت دیپلماسی با ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/133087" target="_blank">📅 18:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133086">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ به نیویورک پست: من دستور دادم که در صورت موفقیت در ترور من، ایران را در سطح بی‌سابقه‌ای بمباران کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/133086" target="_blank">📅 18:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133085">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdB0ePw6FjYSVF2PV9-dNM7VffqhDEXs3DCZl7ugq5plhtIongHtwgm5P3hP3v0Z5Gg84Q2iLsOJ-5fpYt0WH79Gdx7ysBDg_74fgs6z3Ul7XMDZWuVmx_o0x_f7c5dYh629xYyLesc9usTdHNmEjtnYoLL9-s0OBG-3Oskur8rEEcUizCLPMLpZ6BF7HVLDhxC6M_ofgnHUdx3QeJIp1SuQG4yG84Gpxin5vzgfaNqMhIT5-znHIPGSZTa4WrMiGTtd2tNoicyWxVQY_7QRSDXGVsJcwbtXPr5g4vmnciich-q6fZG3ImLeFEzub2OjTMnU-BazU92tYF20U4ZiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری منتسب به کنارک
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/133085" target="_blank">📅 18:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133084">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری / ترامپ به نیویورک پست: در صورت موفقیت ایران در ترور من، دستورالعمل‌هایی برای اقدام صادر کرده‌ام!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/133084" target="_blank">📅 18:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133083">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
گزارش‌ها از انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/133083" target="_blank">📅 18:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133082">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/391b205ef7.mp4?token=kgw7vk0rMR1EBdos3ch0hpdA9JLk4AAdi0vW7eY2TQO9Qw3v_5F_GirqLCwIn0IJSKFc4m64i13w-r1qRyrt1uKUvX5NV2VllJvQjtDLd6kWfK4GmDt_ReiivAXCidpyRxDHgA4ZKNOoAPSK1aTfcOrp_2Fa6vZI4yjkRzACBcwJlPjvQ0UaCYQx-d-fpUzqlmxsZsOhjrlmjnJSevpS5R13lCn5WvoaAhNcHn0ILcliGe_8u3xdkipxe_50hgGS_5z1mfvvl8XGGZ5Y73uVj_yjq9g8oChY1Uu3Zl1j6L3Iq2gSsGpM8am-IYrRGbvdRTfqm0VbtkeBswqQz89kkw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/391b205ef7.mp4?token=kgw7vk0rMR1EBdos3ch0hpdA9JLk4AAdi0vW7eY2TQO9Qw3v_5F_GirqLCwIn0IJSKFc4m64i13w-r1qRyrt1uKUvX5NV2VllJvQjtDLd6kWfK4GmDt_ReiivAXCidpyRxDHgA4ZKNOoAPSK1aTfcOrp_2Fa6vZI4yjkRzACBcwJlPjvQ0UaCYQx-d-fpUzqlmxsZsOhjrlmjnJSevpS5R13lCn5WvoaAhNcHn0ILcliGe_8u3xdkipxe_50hgGS_5z1mfvvl8XGGZ5Y73uVj_yjq9g8oChY1Uu3Zl1j6L3Iq2gSsGpM8am-IYrRGbvdRTfqm0VbtkeBswqQz89kkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از بین ۱۲ فروند جنگنده رادارگریز F-22A Raptor نیروی هوایی ایالات متحده که در پایگاه هوایی اوودا در جنوب اسرائیل حضور داشتند، ۱۰ فروند در حال انتقال به ایالات متحده هستند. تصاویر نشان می‌دهند که هواپیماهای F-22A در پایگاه هوایی RAF فیرفیلد در بریتانیا فرود آمده‌اند، که احتمالاً یک توقف موقت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/133082" target="_blank">📅 18:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133081">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری / ۳ انفجار سنگین در کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/133081" target="_blank">📅 18:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133080">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری / ترامپ به نیویورک پست: در صورت موفقیت ایران در ترور من، دستورالعمل‌هایی برای اقدام صادر کرده‌ام!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/133080" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133079">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
براساس آخرین آمار پایگاه بین‌المللی هواشناسی «Ogimet» که وضعیت دمای ایستگاه‌های هواشناسی جهان را رصد می‌کند، بندر دَیّر در شبانه‌روز گذشته در صدر فهرست داغ‌ترین نقاط زمین قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/133079" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133078">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7c4e411a5.mp4?token=P9IK780tpNDmQQGV-3d1TtOGhGQ7-38W-UKs01E80P6I9Abq3VgOADWDWwwPQnYTseK-SUOV_4tIYsBKi50lBvGr1eykNw4IauBiGzaVYx0StYekd1WxjmfA-u9_bWk0ah6utg0tytsom8vPyehEKBxv2V316IND4v_SjMAkUrUh1bL9ui8Z0eLV8nBx3_yHeNmhzHUf4ReppMjkcf_LURxrtU15OA2Aix5Qsc5QHIPu8Q44170V5jMm3I0hxbC_ifBsJd1Qng5lxTG74PwhQOvYBQIXqx-biV7SMJ1SwkBu8iGoSWfVJqg8I28hOYS_lTmJ9Y8LXziMmjjPiWxQDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7c4e411a5.mp4?token=P9IK780tpNDmQQGV-3d1TtOGhGQ7-38W-UKs01E80P6I9Abq3VgOADWDWwwPQnYTseK-SUOV_4tIYsBKi50lBvGr1eykNw4IauBiGzaVYx0StYekd1WxjmfA-u9_bWk0ah6utg0tytsom8vPyehEKBxv2V316IND4v_SjMAkUrUh1bL9ui8Z0eLV8nBx3_yHeNmhzHUf4ReppMjkcf_LURxrtU15OA2Aix5Qsc5QHIPu8Q44170V5jMm3I0hxbC_ifBsJd1Qng5lxTG74PwhQOvYBQIXqx-biV7SMJ1SwkBu8iGoSWfVJqg8I28hOYS_lTmJ9Y8LXziMmjjPiWxQDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده چین در شورای امنیت: قطعنامه ۲۲۳۱ منقضی شده و بررسی پرونده هسته‌ای ایران پایان یافته است
🔴
قطعنامه ۲۲۳۱ در ۱۸ اکتبر ۲۰۲۵ منقضی شده و رسیدگی شورای امنیت به پرونده هسته‌ای ایران پایان یافته است.
🔴
اصرار برخی کشورها برای برگزاری نشست درباره موضوعی که از دستور کار شورای امنیت خارج شده، فضای مذاکرات را تضعیف می‌کند.
🔴
سیاسی‌کاری در شورای امنیت، اختلافات درون شورا را تشدید کرده و روند دستیابی به راه‌حل سیاسی را با مانع روبه‌رو می‌کند.
🔴
چین از کشورهای ذی‌ربط خواست با حسن نیت، مفاد قطعنامه ۲۲۳۱ را اجرا و از اعتبار شورای امنیت و دیپلماسی چندجانبه صیانت کنند.
🔴
نماینده چین با حمایت از موضع روسیه تأکید کرد که شورای امنیت دیگر مأموریتی برای بررسی موضوع هسته‌ای ایران ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/133078" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133077">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
نماینده فرانسه در سازمان ملل: ایران باید به طور کامل غنی‌سازی را کنار بگذارد و به آژانس اجازه بازدید از تاسیسات هسته‌ای را بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/133077" target="_blank">📅 18:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133076">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نماینده فرانسه در سازمان ملل: ایران باید به طور کامل غنی‌سازی را کنار بگذارد و به آژانس اجازه بازدید از تاسیسات هسته‌ای را بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/133076" target="_blank">📅 18:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133075">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری/ترامپ:  با ادامه مذاکرات با ایران موافقم اما آمریکا به ایران اعلام کرد بدون تردید آتش‌بس پایان یافته!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/133075" target="_blank">📅 18:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133074">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j79ni6O0ooJwQTd9qVpXv03f47yuCJW3XvGv_qe28SGk02ZpMo0fkgd_dkDLMWYXtmGeuLR9gk2N_2Xv7ikzYukjlVx80ztI_SZ3TKFe6MkpvsW--Jhdo-5-LfiCKrbFVWtG6QKYn0cKq9uCabC3brx_sVJo0j_lHGncGmMDY_nvCzPMWfOhJVnRv7nDgjIs92v5RF25o0bYg6oxQm5M7hXs1GduAs6yoUUflQDpzDyNMwnEQOZ3LszH1LsDcKNNXrEJPLNqF8uJq5U0xzKuZJPtIMuXjsgBGAV0NxWdfwqEOFyLlLsJrCSAVQmqXBOSEhacsRTr_BN9MA-cI7zgSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره‌ای به تاریخ امروز از ناوهواپیمابر ابراهام لینکلن در حوالی دریای عمان و ۵۰۰ کیلومتری تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/133074" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133073">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acmXvNVmEgz7OmY3D50XrZcTlquH4hoUsD2fWTCLt2DnChbB4aRYsaBaf_Vi-fwvQ7KXvo_CcWZQqfEkk2NWJZ6r0wCtZDXugg4xshe4OQ6NdLaGKsuxzLKDoiBwujNmdRvQIOMfdD4HkbqO23zpSobERR6WbM8K1usP_wrT2WnLL1mIbPntq7S19lyUY1bcQvYmCIJnAqSB5ZXEIoAu2uxH4eKfcPZlp5qEx3M2OLJYzMClE_w7qHiQWZWvIGCBgYq-UoxUzNSxDaJgoRL7Ua-TMA8-KEQNPoV6wAtdlAvg7uuwJMn6WGa7GqHq7vv3awhwoun7QZSF0agt6iMRyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور مجتبی خامنه‌ای در مراسم
‼️
🔴
امشب، موقع برگزاری نماز میت برای علی خامنه‌ای تو مشهد، یه فرد با صورت پوشیده و ماسک، سمت راست تصویر و بین جمعیت دیده شد
🔴
اطراف این شخص هم چندین محافظ ایستاده بودن و همین موضوع باعث شد توجه خیلی از کاربران فضای مجازی بهش جلب…</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/133073" target="_blank">📅 18:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133072">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnvPWGvieT6LpWwINzI-dcZHx1HvPXzJZO5AeBs8UfT_hspbCCDqDi9ymmXPi8wx9bRy7W12DR6GOwgp5x4aorUQ8oOAss-W2VAS3IG2C7NoBKpOIWsUZ4wtdjtxzgRNicTrJiMFjHKAV96-_MqHIxgfIHN7O_zSqEw_0V7t1V2gmk9VSMVZgGV_F1je1thqD35fpKDBYOzzp8X0DWk27HyThH_S0uTN6JX-65VOFD27aDjPVCy-Kk1TQmDmPRN4jN65F2CzHZVV4V82xpOTPKH846hufbOfsxiMIekV-QaCnBQqIdB2Ej9yzsSw4aH3tBskHaCerk_r23xBDBaYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره ای از پالایشگاه ساراتوف روسیه که واحد اصلی تولید بنزین آن تقریبا نابود شده است
🔴
این پالایشگاه تا اطلاع ثانوی فعالیت خود را متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/133072" target="_blank">📅 18:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133071">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
روس‌اتم: ۶ نفر از کارکنان ما بازگشت به نیروگاه بوشهر را آغاز کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/133071" target="_blank">📅 17:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133070">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAPNCglb8i0OQhhZSyI83VuAdTh4C0duGg-05idebvJcW_3DOHch6pC2OQwz4ATlajcwwoAcguKBj5FTTyOUXNcFwRHAqgTGGzQ7FQt9W3Klk50a2VQzh699P7dcMdLe7q7JeEMggOuTNup6DHWPiQ4auhXTMK8sU5uwRL7LW99QOqUmRoOdtKMD3wd1vFkQX2q5_xZpGW7C_g5Qyh0-9DJ0quRBWudt3arxeA_wnmbQjrzCIRD34DLsYQdc75uOML-stfz0HATGmXPFqnVe1L8TBFfCvK1FrVF8HsufJUmB9Gf_iG0DyMS4fgvp6dUo4a3T3TGM8tEWT0fkGAbTvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد هواپیماهای نیروی هوایی ایالات متحده که امروز در پایگاه هوایی شاهزاده سلطان در عربستان سعودی مستقر هستند، به کمترین میزان خود از زمان آغاز این استقرار در اوایل ماه فوریه رسیده است.
🔴
آخرین هواپیمای نظارتی E-3 در اوایل این هفته از آنجا خارج شد. در حال حاضر، یک فروند E-11 و ۹ فروند تانکر در آنجا باقی مانده‌اند.
🔴
به نظر می‌رسد که ارتش ایالات متحده بار دیگر فشار خود را بر ایران افزایش داده است، و به همین دلیل، بسیاری از تجهیزات حیاتی مورد نیاز برای انجام عملیات‌های بزرگ، از این منطقه خارج شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/133070" target="_blank">📅 17:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133069">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
طبق تصاویر ماهواره‌ای یک ناو هواپیمابر آمریکایی به همراه حداقل 3 ناو جنگی در اقدامی عجیب به فاصله کمتر از 300 کیلومتر از سواحل ایران رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/133069" target="_blank">📅 17:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133068">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رویترز به نقل از سه منبع نزدیک به کرملین : حملات اخیر پهپادی اوکراین به پالایشگاه‌ها و بنادر روسیه، عزم پوتین را برای ادامه جنگ بیشتر کرده
🔴
پوتین در زمینه تصرف باقیمانده منطقه دونباس اوکراین پایش را محکم کرده و مشاورانی را که پیشنهاد آتش‌بس در امتداد خطوط مقدم فعلی را داده بودند، توبیخ کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/133068" target="_blank">📅 17:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133067">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHXok4pYsHgrpxkgLj__6Z6akPw-M-Apb7aD2g1L7PcqBncTgY3PEB-Lu02vujFrtEduoym96yjhaI6x_e6Gk6hQvbTZlajOQv56AiEhPLLLgpdmhrq0QqtxzLUjayLKqqG6WC3_7zvA5is-_flaSFlHukq62BxI5lKf4WdknHRljlLupCFAwSgYJCLjpEdVUIWeRyOCwCuSFBezRDezl3cLV8Qy9lWUM9G7XMlCTUQh-TDWXfRlH4wF25AZamCeU3Js2UGVezkkAv7KtdSSxeVaR1lCkaMegp30z2QMw20JdMMWpbSNDJBAlCUim9BLMaEHLMGm9NaS3fuXlwz2OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق تصاویر ماهواره ای منتشر شده؛ ایران مسیر های منتهی به سایت هسته ای فردو با تپه های خاک مسدود کرده تا مانع حرکت سریع با خودرو به سمت این تاسیسات شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/133067" target="_blank">📅 17:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133066">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
شرکت ردیابی دریایی کپلر: فعالیت کشتیرانی در تنگه هرمز به شدت کاهش یافته و تنها ۲۲ تردد تأییدشده در روز پنج‌شنبه ثبت شده
🔴
تنها یک شناور از کانال متعلق به عمان استفاده کرده و مابقی از مسیر دریایی تعیین‌شده توسط ایران تردد کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/133066" target="_blank">📅 17:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133065">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuIre52i44Vtlob2Z71WnFWGqpbrB9q7EuTKiCDarPQVCuVxQMX7ensRwVQmdq3yyxa4IdnYeAh5ga5V0tFbFzCA4z7BJa2y-EYCzPZBOmoO_ynWqKhTkBuqQSEmzjvxD9MoY20ThXbz-AfDOTp7lPAWaj-5X6VVFfIBDBaX_3pVVTcsSXZAnDsCQK2CZu5HR8OORLgflT1VKOADz-xSdoswUsSXsRG2T9T09noCmpCK9Dr4ZXTxFwm9mWMr1ZDRSaTrgRCfQWiMMn8oVSU1uDjF0mK41vgbEDGY59U4XhSsaYWOEALJkd7hdlZB-0zOx-pr1KeI0J_FxV81Lbczdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لیویت، سخنگوی کاخ سفید:
جوون‌های نسل Z که از وضعیت اقتصادی و زندگی تو آمریکا گلایه دارن رو بفرستید ایران؛ خیلی زود قدر آمریکا رو می‌دونن و دلشون می‌خواد برگردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/133065" target="_blank">📅 17:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133064">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OD3CRE9T7yLETs2ku8IRfrVwoJScj2p7wxifKfyJKxbbYbGJLQToOirYQKYvtcKj4fVoNFn5Kmrkl_sQDil9CltjPuoVPXUhYRuVI8xjSBmtbsfh87OFdx6KYlBziqnOsXoPtYF-lwE-v6HqJ3szQKKQiQhLTfz95SzKgB4CByCLbTFoYbShv-lBNnuqpbfeglOqE6ZHGUH6YGMCaVpkwMOOWJYa3Wj4HlhFct2LUS21KkITKjc-9AL3PniLil4mqpb6zRjVv0V2GGyHhd8wkH1f2dcidmmjZlU4KL11uTI9CySWQybuSajqX6QDSR-6HNSh-ak9U8GNw9s-KqlXWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام جمعه اهواز(مگامن): هر کی موشک و پهپاد داره، ترامپ رو بکُشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/133064" target="_blank">📅 17:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133063">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پشمام
😐
بعد از برد دراماتیک آرژانتین گروهی از طرفداران زن این تیم در استادیوم لخت شدن
😐
⚠️
⚠️
مشاهده بدون سانسور فیلم</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/133063" target="_blank">📅 17:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133062">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری/ خبرگزاری CNN:
دولت ترامپ در حال بررسی آغاز مجدد محاصره دریایی علیه ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/133062" target="_blank">📅 17:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133061">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzOEdbkgzYNigmYz2097IwX4QsWaW0Z83lUaIpuOKsSya6caVZTGvCqLwzdBn_9xfQeFP7jjFS4OYEbGi3-TH_MRLOgrNeXXfp3A-zDaIo3S7b33NkJjHd6zlGdFvx8OAqO3fRErh2kgN2we17Nghiujsb_KAcAoZcS0J6Vcr9RKvjwfUx9npxhvKeRbPeoz4Prsn4nHODbwKFiLIImLl0i79q-MWVUpR1Eyien3HbgR4vI4bE8X1ssyfDACHnQi1BW3ZguT6c07zB7oXgPTCZ_SYRh7yJs6SvCbAppQmtAASQY8haoK3zx1CKrGhZVYsoFETHzIGjXiN4RutLCPEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله آشنا به جلیلی:
انتقام اول شد؛ نان و زندگی مردم چندم است؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/133061" target="_blank">📅 17:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133060">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7madSz3qL0PZCYTdUG5sUpwIlb7zCfcmJAqVhQnDrxy2HtXHDpcK_QWSskN0rmrHwpAqU84ablADOZ4J8N7GmvPNXVY839GMdTA76VWjSW9CXQ5GLX9Zjup5VnDHHbQB9tdhbe_y2ua4bVZ4SxFbTUWmAvmbKhrUpOcJficl8K6y5khlEdCmZQ-QkZkTm9iafzODLcAG6wbLniPArTodVtrVpJjvJFetXQKI9Y-_BQaZZYn720bze21JXitdzoujoCPxH9CycfcKVYty_BjWu04Xkdx82XPIhTk1JXR2XdkVDQzUlZcfe0Wnc_5uc8gWyfWW5BVJDkIDlO8g89vIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اولین تصویر از محل دفن علی خامنه‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/133060" target="_blank">📅 17:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133059">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc5b51f6d.mp4?token=LckmTRB2RVrgADChOSJrDMV9fFIclxvNp18yqMvzuw9Uo4arOdBJwgUa_6ixqNjeGZCRzusto13kEKMFzJQLn1hVaarvyi70UIhCB1oLbGEu773F161H_weZFMDYsvKovJo2fSzcCjaZFkITDGIgsiBj_YoLeeEVmwhwFPqJH0lMcat4thjflm0SiI6FLdUjq87IN0AzpMTh_t5QQJJDZuakns5JcQfMtxedTo7tR1fTpSEgSKzoxPu4fwzJgUeKBiV9JTh8CyN9wU4AbqlO2Nfnti0RNm1AEW4ZyJqRrxlveCFmlOd2wm7me_S1N4n_V6_sKXTavMWYWnQoowOkYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc5b51f6d.mp4?token=LckmTRB2RVrgADChOSJrDMV9fFIclxvNp18yqMvzuw9Uo4arOdBJwgUa_6ixqNjeGZCRzusto13kEKMFzJQLn1hVaarvyi70UIhCB1oLbGEu773F161H_weZFMDYsvKovJo2fSzcCjaZFkITDGIgsiBj_YoLeeEVmwhwFPqJH0lMcat4thjflm0SiI6FLdUjq87IN0AzpMTh_t5QQJJDZuakns5JcQfMtxedTo7tR1fTpSEgSKzoxPu4fwzJgUeKBiV9JTh8CyN9wU4AbqlO2Nfnti0RNm1AEW4ZyJqRrxlveCFmlOd2wm7me_S1N4n_V6_sKXTavMWYWnQoowOkYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
افشاگری رضا جاودانی از علت کناره گیری خودش از مردان آهنین :
🔴
درگیری بسیار شدیدی میان همراهان شرکت‌کنندگان رخ میداد، به طوری که یه روز نیروهای ویژه دور تا دور محل مسابقه مستقر شده بودن و تعداد زیادی سلاح سرد و شمشیر ، قمه و چاقو از همراهان شرکت کنندگان مردان آهنین کشف شد، منم ترسیدم از اینکه این فضای خشن و خطرناک تو مسابقه وجود داره و دیگه کناره‌گیری کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/133059" target="_blank">📅 16:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133058">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rm39_sONcWOyt7I7QWp_f3GI-5zvNAfFVxgODby-mWkTftyPbpyNSsc2l7HJ7-8S8Itl3avNURGz-03z65p-15TLUGikSvFowpQpC4JbP5LZNk8TxRJXNCDYlbalDgYL89zY5o1oWRdaOTQgb-kI1n4OcqOAiwd5HrLIqu8kkqs3ZGdbhpG5PpibMxcCtEbS6bEQG0JEmihCz7EohJYgmTALobf9fMc5Ual3VLd5QYJu54ujfP3x10clWRqzMxrlk19LyrFV_2zILr3P7ff6mx2x7rdr4Rvs6IN1IBbU8CCKHUBZwmXrSTT8YAmQLEHYmQ2_MrZl6Yso2ENf4rJe0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی ان ان: ترامپ نمی‌خواد اسرائیل تو حمله‌ها به ایران مشارکت کُنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/133058" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133057">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
تهدید آمریکا به انجام حملات احتمالی بیشتر علیه ایران
🔴
یک مقام آمریکایی امروز به سی‌ان‌ان گفت که واشنگتن فهرستی از اهداف در ایران را به عنوان اهرم فشار علیه تهران حفظ می‌کند.
🔴
وی در این‌باره مدعی شد: «وضعیت [با ایران] متغیر است و در صورت لزوم، حملات ممکن است از سر گرفته شوند».
🔴
این مقام آمریکایی ادعا کرد: «واشنگتن عمداً حملات را متناوب انجام می‌دهد و سپس برای جلوگیری از تشدید تنش و دادن فرصت به دیپلماسی، آنها را متوقف می‌کند»
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/133057" target="_blank">📅 16:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133056">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAb3jHQAjxFGQkus8-hiebmehdpbBLVTSJRykjDbUsWk6B1mfD8-nirjZj19Z5ZyJLk03h45sy66jYhHuygzIkV7qX7aVWhIqM7eHJ2VHkybxggIfcMsCn6XxiuI2M9IZqw1OS7x-wATy710aNfMoG8OgtmJgbwiOBRLuiVAdQnpF_JOd1a-curNfwowsUpGGkagVfLxweG1ljsBx28lL1osE6zbyOhxT8M-lpIUYevHoDb4bWeBeFBrlXHcqHCyw8gbhwr-67Bjdeb0su343hGvx9S4AoXxMnIZpvamgD5oXnzKcSH0EVdAFUmjvrr1E1kvc_fu4UzNxxhT_k5GxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
فهم امثال ما از زمان فعلی بیشتره
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/133056" target="_blank">📅 16:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133055">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
رویترز:
مذاکره‌کنندگان قطری برای کاهش تنش و تلاش برای ازسرگیری مذاکرات در ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/133055" target="_blank">📅 15:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133054">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
هواشناسی: تو روزای آینده دمای جنوب به ۵۰درجه و تهران به ۴۰درجه میرسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/133054" target="_blank">📅 15:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133053">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
زیدآبادی: قلاده تندروها رو باید مهار کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/133053" target="_blank">📅 15:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133052">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
معاون وزیر آموزش و پرورش: دانش آموزها بجای کافه گردی برن درس بخونن
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/133052" target="_blank">📅 15:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133051">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOwPpiHngV05BE0B_bKfzLExtjt6Fus9al2AQrdH0goRSJnIYBNzJ89-unHpePsw2lm7YKFKk26pr6mObWSlDunliz96QUcsxD-KMB7zfRo1G-PkilvgV0g-sHVk3NPxeJgbvInbEcYdksWGDhQkCb8lHLI6f165Muccn_CwL53y_-HinguZ329R0yf4QU61hq76pm5USdLqAJXuykY90UC02PwAbxANYfaxIv9v1noEpf_RFFtporq4eEHdDK9c-mTqCNPKLB5SCF6X_Ftq5-s0ScZLCbG3rAFzyLcqE7KQDKOg23oCRex3ae-DgnJImxI-U6dKP5v6_dxbub_K8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیلی:
برخی می‌گویند ما باید اموال ایران را آزاد کنیم؛ بزرگ‌ترین دارایی ملت ما رهبری عزیزش بود و باید انتقامش را بگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/133051" target="_blank">📅 15:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133050">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d5c47f340.mp4?token=VNpU9AiGYVn-Zm70sUbnfGavZZqcQPSULpvP6gQnrA9Jed3QVLy05JWZU8zEGbCRhVw96tv9xtV3irROc3Y8eI7LGj_roB6iyo_OLoOxkhrYun0u4_QGJEM6_VYR4pqHAFFdxOhsuWeDvc9dCEa_ap5pw4Rx_L_vz_hoX7WL72bghmJxWnQnHBSO-wrNOTunyvvEwJ7JPKVp0HlXuKJZZJefH8hYzXbaEgQd_fduTLzPtWcwDd2DfB7iMecT-v3Q4ATxXDq_ptTVXla2JYfa1Tr_XZIXwXYZQp9OkZo_fixgKJf4n-IcbGcF-gaqPOggEpBksFQ1FkTFkUPWZIhVaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d5c47f340.mp4?token=VNpU9AiGYVn-Zm70sUbnfGavZZqcQPSULpvP6gQnrA9Jed3QVLy05JWZU8zEGbCRhVw96tv9xtV3irROc3Y8eI7LGj_roB6iyo_OLoOxkhrYun0u4_QGJEM6_VYR4pqHAFFdxOhsuWeDvc9dCEa_ap5pw4Rx_L_vz_hoX7WL72bghmJxWnQnHBSO-wrNOTunyvvEwJ7JPKVp0HlXuKJZZJefH8hYzXbaEgQd_fduTLzPtWcwDd2DfB7iMecT-v3Q4ATxXDq_ptTVXla2JYfa1Tr_XZIXwXYZQp9OkZo_fixgKJf4n-IcbGcF-gaqPOggEpBksFQ1FkTFkUPWZIhVaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی مراسم تشییع آقای خامنه‌ای، یکی از حامیان حکومت سعی داشت مثل اسپایدرمن، جلوی ماشینی که تابوب خامنه‌ای رو حمل میکرد، بگیره اما موفق نشد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/133050" target="_blank">📅 15:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133049">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d349e1e2a.mp4?token=gwLulmG5XeuWe76x1auaaPALZ0RNr4ZKk1nHcR_HD9NHvFdt-E7xHYN6j34DoJbCoOb-xkujpEGg927R6RbssJ-I7ynUu41FqaV2SHyJqu7b0WKvnf2h5d5_7B19r3-pMh4B4IiBLj9KUQDDkjEV-YSOq-IArtFf8e-bwA_e31-56MlBv3AQEVW4CR-DGc6QchXACKpoGqj6OVf0VUh0st82T1_EzumJL836iMd6ZdNNufmhWtIXhdw9yruOJzztiu7DS3P_LK95gxDhb5yPFnIfIZl1qCkoX_6cu4Zzi9S9gqflq_aFHN3isGncSe84puI7GrJ0y8ax4h-CDomS4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d349e1e2a.mp4?token=gwLulmG5XeuWe76x1auaaPALZ0RNr4ZKk1nHcR_HD9NHvFdt-E7xHYN6j34DoJbCoOb-xkujpEGg927R6RbssJ-I7ynUu41FqaV2SHyJqu7b0WKvnf2h5d5_7B19r3-pMh4B4IiBLj9KUQDDkjEV-YSOq-IArtFf8e-bwA_e31-56MlBv3AQEVW4CR-DGc6QchXACKpoGqj6OVf0VUh0st82T1_EzumJL836iMd6ZdNNufmhWtIXhdw9yruOJzztiu7DS3P_LK95gxDhb5yPFnIfIZl1qCkoX_6cu4Zzi9S9gqflq_aFHN3isGncSe84puI7GrJ0y8ax4h-CDomS4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سید علی خامنه‌ای، ۲۲ مرداد ۱۳۹۷ :
به طور خلاصه در دو کلمه به ملت ایران بگم : جنگ نخواهد شد و مذاکره نخواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/133049" target="_blank">📅 15:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133048">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYr_1UrraErMVeaTO7PaEcLQugoaqGwA7xLWH6vrvrnyYVoWG0eRIRXGol76pF7mAUiVBTNAXjMDKG64XdNFxBcsChGNqlaWaLKC9ZUB8Lq8bhLcE3lxFXYr2urOQ-KoPhcQB35AcB2PbfZEGyoHCje0pxLODrtJPccgbv5QArBIdVBTONX2J6SgXRZDMVmxfqMc9gClK6heG3gY9V3zKXAOcnSutC1IIt1AI_7NuEojlwPbd94tX_GYNW4LMq6TJazyvYIzi0t_XCx7S8dQ_cO7PdwA5gwhSn7QnsSpJfuPtOHTP1HU5fT2K3Y7widHsUWMmeQYtVHhqvuo4RB-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیر شورای‌عالی امنیت ملی: با حمله به زیرساخت‌ها مقابله‌به‌مثل خواهد شد و رژیم تبهکار صهیونی هم از پاسخ رزمندگان در امان نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/133048" target="_blank">📅 15:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133047">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
به گزارش بلومبرگ، اتحادیه اروپا در آستانه توافقی است که به اوکراین اجازه می‌دهد از بخشی از وام ۶۰ میلیارد یورویی اتحادیه اروپا در زمینه دفاع، برای خرید سلاح از شرکت‌های بریتانیایی استفاده کند.
🔴
احتمالاً این خبر طی چند روز آینده، و احتمالاً از روز دوشنبه، در جریان جلسه ائتلاف کشورهای داوطلب به رهبری بریتانیا و فرانسه در پاریس اعلام خواهد شد.
🔴
بر اساس این طرح پیشنهادی، بریتانیا هیچ هزینه ثابتی را به عنوان حق دسترسی پرداخت نخواهد کرد. در عوض، لندن کمک‌های مالی را بر اساس ارزش قراردادهایی که به شرکت‌های دفاعی بریتانیایی از طریق این برنامه وام اعطا می‌شود، ارائه خواهد داد.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/133047" target="_blank">📅 14:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133046">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44c5dfe512.mp4?token=PYj4EaYmPxU1HRE2WrdGKHe1o6CgkAP7f5dsHezQYVvV6M7I09NrKjRRc1H_UPgNK1ICemFC0lsWdWPDCjK3d2Cb65QfXFfp0JivNLw8_mPYvgyZbreubFyNseLco1wbJc8DYkqDq5GtYQabfvk7k-Ql6qzzzoKsqpRfjgNUA1t23JwgRS5X6L1LS3xK1dFYOdQscKLhc7EyRe-Dk8AnCacBKVzl_wld1nWHL5oFCEwhXi7EKtTOVZeavphFNWJdjPg50nlZf2QkfEmmmpgemneN3ZGH1_yvAeRfYUbn9C2cJ9Gxt9vritI26n41ptjQFlFt-mbA5SUw9T_lc0SsCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44c5dfe512.mp4?token=PYj4EaYmPxU1HRE2WrdGKHe1o6CgkAP7f5dsHezQYVvV6M7I09NrKjRRc1H_UPgNK1ICemFC0lsWdWPDCjK3d2Cb65QfXFfp0JivNLw8_mPYvgyZbreubFyNseLco1wbJc8DYkqDq5GtYQabfvk7k-Ql6qzzzoKsqpRfjgNUA1t23JwgRS5X6L1LS3xK1dFYOdQscKLhc7EyRe-Dk8AnCacBKVzl_wld1nWHL5oFCEwhXi7EKtTOVZeavphFNWJdjPg50nlZf2QkfEmmmpgemneN3ZGH1_yvAeRfYUbn9C2cJ9Gxt9vritI26n41ptjQFlFt-mbA5SUw9T_lc0SsCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیروز تو پرواز یونان به آلمان، یکی از پنجره های هواپیما کنده شده و یکی از مسافرا تا ناحیه شانه از پنجره به بیرون کشیده شده!
🔴
همسرش حدود پنج دقیقه با گرفتن پاهای او مانع از بیرون افتادن کامل وی شد تا بالاخره نجاتش دادن و هواپیما هم فرود اومد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/133046" target="_blank">📅 14:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133045">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
به‌گزارش یسرائیل هیوم، دونالد ترامپ به‌دلیل نگرانی از کاهش شدید محبوبیت خود در آستانه انتخابات میان‌دوره‌ای، قصد ندارد جنگ با ایران را ازسر بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/133045" target="_blank">📅 14:50 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
