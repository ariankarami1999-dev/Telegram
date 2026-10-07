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
<img src="https://cdn4.telesco.pe/file/ur0iFb9FdUVLIqgztRjn6j5I5rKXgIlPryWKdml-VxE-9bmfza6QWIBPDdEjUjkpbxCmgxiRa9RxcYuwjy6zGAGMUmUvgWIw5kA91ZHebYArLOWUOlPVvfua2E8xopyXrBBB-vVeIC0FvnzeQQMDTfipAKCMrIRVi6NMG7R1cEb0X8rI3mMibFsQGn1IoQj_ojNJZwm5QHI7GhcpnjtMLNGKulszzq29qwBrS6tYYbOVSbbeJHz1FuOaDyIFQLshMLRubfPe--KU_mWLX7SpFRDr9rjL4fTbHRQY5jaCy5R7cqQdDLuE8xoVSbVSxhXyOS0sJpWbUP_frKtNC-gMow.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 262K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 13:03:45</div>
<hr>

<div class="tg-post" id="msg-84546">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=Y8YB6IoyXy9DSQSDxBbyswWBWK7p9dZAwSzxcQJmmgvMjKuNXcWcns8nJCYi-y2brt6OIPeag-lTMKwjEaQhTHadQ5nVLeOWL8h6X2kh5p9UICuUlQEqfWBAC9ZoLiPnyTsbp9OK8EbL1WvoW_9W7RIwNY_A31IClJCdAii8ijbYe4b0ilkd9vHuPW4b5a5hX_GNnOpsaCz90w4oJB6o2lvX-Hb3rR0gy399R49gLLEnfuhAMEg31-zqE5c9z0Wxje1Cli31cMFXGjU-yN_g_clHJ1Hgv66p-HckuFwt4WJ5GeqA614t8ljuFvSS3_qjSvZi0VDY5U09PXx73wgDfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=Y8YB6IoyXy9DSQSDxBbyswWBWK7p9dZAwSzxcQJmmgvMjKuNXcWcns8nJCYi-y2brt6OIPeag-lTMKwjEaQhTHadQ5nVLeOWL8h6X2kh5p9UICuUlQEqfWBAC9ZoLiPnyTsbp9OK8EbL1WvoW_9W7RIwNY_A31IClJCdAii8ijbYe4b0ilkd9vHuPW4b5a5hX_GNnOpsaCz90w4oJB6o2lvX-Hb3rR0gy399R49gLLEnfuhAMEg31-zqE5c9z0Wxje1Cli31cMFXGjU-yN_g_clHJ1Hgv66p-HckuFwt4WJ5GeqA614t8ljuFvSS3_qjSvZi0VDY5U09PXx73wgDfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خلاصه دستاوردهای همتی در بانک مرکزی.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/funhiphop/84546" target="_blank">📅 12:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84544">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiRYRrrU7vDOKxWu05T-DSzkxAR6G9bwNqhr9POqyLRgMVlb5TzOsukxiyNE9qqXGHbjxAKCJPle_PLi_KuSyNcQEepb_j9GixGhAtD1WDSAdt_qrZqOVN2Wje7w0OphFr6qT9oM3Euvc8rqfHIiC7-QYjgPwJParzEV1-UPpeXJ4atcp64z0Xpn-tSqPVKwUIMG_ntCFTEeaDdsnQDsgGMVY8GablAUrdY3JoXhRsxwXNGZi_MxnEfXzEDsdlfVQJhR4UDluP7ugiMYBQBBfigV8a_kBuAIrSXXrpz9HBoHzwi7-zu6fbRbPowUNASLCbY-mwVzLiSnj4EzqTi5uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86ab280716.mp4?token=ht0bScNTHclTppT4xwrGIEabYa43rjHI9AjoNZDx8j7FqV9T_uoIowUDS5svGTYvU62PtaHwA9g7BuIDnIYQatZtJkwHsiA9ErZr9l_7bc3f69-pdJOuHnTZ5TZD8oHbX2Otct_OKRxO0pteQX13CWDd8fI0MDE-7iwAfEEK3_HaseYCJUD2kibRJQvmfuzc7Bu_aDlRYoi-pUUBybm4F1QCkt7uQJs65L_8tQdL0MhSzkr0B7fgW9NYorWaYn0wdFQ3pTxnZaCn0V-AyRKl2ZuLJOlF7rOdBJDejVP38VkOGomF_V1C8nORlSdzA74FUyj4B8POZkWi7llvqkQlaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86ab280716.mp4?token=ht0bScNTHclTppT4xwrGIEabYa43rjHI9AjoNZDx8j7FqV9T_uoIowUDS5svGTYvU62PtaHwA9g7BuIDnIYQatZtJkwHsiA9ErZr9l_7bc3f69-pdJOuHnTZ5TZD8oHbX2Otct_OKRxO0pteQX13CWDd8fI0MDE-7iwAfEEK3_HaseYCJUD2kibRJQvmfuzc7Bu_aDlRYoi-pUUBybm4F1QCkt7uQJs65L_8tQdL0MhSzkr0B7fgW9NYorWaYn0wdFQ3pTxnZaCn0V-AyRKl2ZuLJOlF7rOdBJDejVP38VkOGomF_V1C8nORlSdzA74FUyj4B8POZkWi7llvqkQlaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نسیم مقصودلو؛ خواهر امیرتتلو :
خبرهایی که در مورد آزادی امیر پخش شده فیکه و هیچ تغییر در پروندش ایجاد نشده. اون فیلم هم که گفتم شرط عفو شدنش پاک کردن تتوهاشه مال پارساله که اونم دروغ بود.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/funhiphop/84544" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84543">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvAko_f_DlmfeagDW3XDz74VyX6qK4Cjy1NTDyXl9-HI_NCAXusCTmpCwdxH1ktsUSrBmTGuSm-vvKcsfjFb3Klo8xmW6-QpXexVJR2QdYpnNI3Y10WAyLVsOcQleA3JrJ_xJT0jrtzuPAC8RogiKTc8TkF1sNwCiVpW-VkZIFn6XPpigKyItAFGukXkvTAi-9tmjWLagaalxgtiN6BEj1GruiBVaq16Zu_-_1XxXbMVOpYZxCfTDMylg2ftdTVzqj3gYpCnNrXaiZtDUlHkAeaYLzmXTo70Y72oekleCqI1x2Y7OBNbqJFuK_Y-Fl-OcyLvzMK4fbGlb7Rc4q5tUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شوخی شوخی جدی شد، سفارت آمریکا تو مسکو درباره احتمال ابتلا به طاعون ریوی هشدار داد و همچنین
هشدار سطح چهارم «سفر نکنید»
رو صادر کرده و از شهروندان آمریکایی حاضر تو روسیه خواسته فوراً روسیه رو‌ ترک کنن.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/funhiphop/84543" target="_blank">📅 11:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84542">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/funhiphop/84542" target="_blank">📅 11:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84541">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAwV3_GBrujaSBzt81uVE4UpWg3HEgI--mYuFAZkyGJ0WjqFJIlV3sjEqZWIsoLDnj0Tl0uTLaqmh0gGJjahiTKTIiBSS0nZbTLXRx9DDxnCeAzGUPWfKlnb146BfcpYQECW5WHKiPvuXd-0Kqx4G_E5Rjsw7iymYxE807BR1dcPfDSmOcx5oLEoSNB9wGAuz-c7LJ1oXFXHu-rU6Fm0D5Uk0buYLWycNBYkomgS-DcU8ltmiuiYkTKTRMfAORT0J5IfDhbjhQZMSmD5T95YbCkpm7sx0pkA4soWpCLqC1IyWhiUo8fSnh6TR5sp3jvT-o97zPvUfDAhPRQQMvbbfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
آرژانتین  - بنین
🌎
ساعت ۲:۳۰
⚽️
کلمبیا  - پرو
🌎
ساعت ۳:۱۵
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:r15
🅰
🔗
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/funhiphop/84541" target="_blank">📅 11:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84537">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tq1KF2O2Nz2B353j0N4q8p0XFfLQbeQurfBue9es0PYOrPguTFUuaJ1QUuDEjdKM4Lokb1KwWuuZVfSl6xKprm2KUDYiq_hohA2yiAWA8AyDMQSm7mV69ouZ3FK1UBYlyFJmY5-awaV5gku7Rg-h61HPx8yyEbRP8efXjV5fSf1ObGlxq_oJ45B05laLUq5gCQL9ww1k2isEtt4dsQjpWIwskFwZ5cvej4ZKMUgS0g09kBEoQrlDKoQDecZMBtgcad1GIcMaoOE3aknOld3Eh56eSQq0WzN4jBR0te6PIPH_9AlmM_aVbAmV5-gXQRvv_7qLkxKBwghSZ-jdiVSzhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدجور دارید تو طبقات بالا ویولن می‌زنید ها
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/funhiphop/84537" target="_blank">📅 11:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84536">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmAusNHwDf-JZraifWBLVaa1MDr0s1DOyg7toQ2ACsl2wTLz6_inYjTE0RJqmEXxaIv2PJYEYhG5F-ZoPaGKOYvANbhH8Ptnauy9NPS_afBa25eNSrQw6aXUqNRU17FFkGCfGnh1jduN6FtEzPPEBDGZ2QIz6eH1SZtnDB_0WmxqRPTX83WbHgKXxHUB1bG2ny8KBlevHuFV5rfZJjEjXLdWamJ3SqvF7pgyjTji7Aja7jyhdAkKktmPQlFbtSAKZ5iQlPqzv5nBPqDMKnZWtvF_ZfWFUP7Cv25VsVZov6WWXXWAdymmx0ILLj8L41XAQmvTQCBu9YMTfBnX0_5Upw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام امروز هفتم اکتبره.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/funhiphop/84536" target="_blank">📅 10:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84535">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d26406817b.mp4?token=MAA1ShIXpRQkSNyDKx4R02LMCFS-5imsUlOAqJ5GQhn3V2WzmHTyuEBFmx_XVf8klrN9khz5S5rMBXc0Wyi_8BAxyu1p6hvMlbUeAFdYbaLiodcH4Okxg8uqEbo9v1BXz6itkC-w0Z5VV8qYjO_AASsLIs8PzqHMEMHfUPkXAnMJW7UlzY5-78a-4h06svGPs7MdL7HSjsDmmtH07HZV_xXquqAHhARf67vmLbSgGzb8KCU5xF7q8PK9mMRjghOChJzy6uHTANALpbxijVBN-l27YtcmcEBRRfhNNyGTbSUEicbUlnUl_MLJR68OKe7iOVMool0ymJnHXVCvaDE_kA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d26406817b.mp4?token=MAA1ShIXpRQkSNyDKx4R02LMCFS-5imsUlOAqJ5GQhn3V2WzmHTyuEBFmx_XVf8klrN9khz5S5rMBXc0Wyi_8BAxyu1p6hvMlbUeAFdYbaLiodcH4Okxg8uqEbo9v1BXz6itkC-w0Z5VV8qYjO_AASsLIs8PzqHMEMHfUPkXAnMJW7UlzY5-78a-4h06svGPs7MdL7HSjsDmmtH07HZV_xXquqAHhARf67vmLbSgGzb8KCU5xF7q8PK9mMRjghOChJzy6uHTANALpbxijVBN-l27YtcmcEBRRfhNNyGTbSUEicbUlnUl_MLJR68OKe7iOVMool0ymJnHXVCvaDE_kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام من از آینده میام
حدس بزن چی شد؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/funhiphop/84535" target="_blank">📅 09:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84534">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Msb9yg5irxbuppXkElMM32cwd_SwW7KVoCEmyak9fImCS8RROrQnOkTHrHHSHcxRH7gGWvT68KyVBIs2oXDOyxtb5u5CJvo8sA08Fk8FGoBJ09zg30qJRg8B9U3WMoINdPElXFebTvvSeZGtuFyDCfBFlZq85du3axx-NDNOA43boWrht1sQm_ZObBvaEI9ITWAXHYDKJNhVQ6sFTahnu7BctXgiYUlrQ3ffExv3R5RG4wEISAelM4CfdHboeSqujbQhz0oZKiH_LSwc842fcZBIcIPOg086eDb5Y5oteA7v1BATg2feqgt_5vRiZsbD9PpJLBaW0s1nBau9_4ay0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی بنین در بازی امشب.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/84534" target="_blank">📅 03:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84533">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یکی بره اینارو بین نیمه توجیه کنه بازی اخره یه ۱۰ تایی بخورید</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84533" target="_blank">📅 03:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84532">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کسکشا این دیگ چیه اوردین جلو ارژانتین بازی کنه</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84532" target="_blank">📅 03:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84530">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONfD5aN9u7I9r_o_GhOgvOH8NcRVxNNGlZTb8VnCgvq-_GJ7Dykfab6zWvITlUtLbCFkEoNUlr0a7Am1nAWvukAkkbHJUjcSHo-0f8tfiDe6y7tMioAFEhm07mcoAk__JRpS_HngTYdFtrXTPrS9X3dhnRv3rufqQFTxAjop-gJNXa5KaxiXoKNe73dMJf6gLwliKowlkbr9Ldu1dt8gnOixd8ViWj_o5busggisyc1HUDZh-Cn5k-MMvAqdj-9x52LsJTiFbvypOXSRwx66mvbimGSt6-ip4bhRroxi6RM8mFe7L0UXqb8T49OPz2gv4yg2AfyyI2j8rsVPemOM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیرون ورزشگاه به بز واقعی شماره ده چسبوندن اوردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84530" target="_blank">📅 02:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84529">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUoCuc0orFzzmkW6pAunWvkiHpURuHLkMd_dZ4IoR4XcIUrPtURdN-R2xP_1wiBvSdCtMglZVCaECxlWf-tZ9R5jIBboBv645-rZe4NIWWXKo-x1jngkpBDR7vr9M5j_fHVe4kPCV-Zy1eWXdZ9kPxgJl28uSZxfAYpX_VMlJ3kYBtagMOpI-snEiXKMUAgWHU0iiypbWoxiIjrLXSiMx31cw8TK4zDx6wzJgN4WJuLgG2VVB4_IAwweNUiI1Yq4hnvie2mC7AeT5YsjMFx7G0eZwnMeRQ4uFggCOZDxR0amJ9DyrUJyufqATuDWs9FfvihHJqplTOLkETTswM8anQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی تو دشمنی هواداری چی ای</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/84529" target="_blank">📅 02:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84528">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تمها دقیقه‌ای از ۹۰ دقیقه که مسی گل نزده دقیقه یکه، شل کن بنین بیناموس</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84528" target="_blank">📅 02:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84527">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9mj-EaGoXN6P7BuInaeCBaTvtjYVn3K6cn7Uwx1ndEIPY9XG6sSMZ5zfIlWFrrgWCNbiOLBIo-GciwmTebTSgJboq2pkyH_ysLcMXk3jpy3TJ8o5oqfNCavyVgPIQ65wvF7pwdDaC3pfdlc2emcLZpi0qBuN6RvUm9ZVacrcYWSefwCndwHO5Ra8EMj-eAjrQ2SQZ-ahod1Qwss3b8QPYnXoO2C15nWE3cPjkl00rbyj2iB25IU0akJDEJfsotJ3bpiOk9YOed3yD1Ts_w28aGlNk7G_3r3bFTqqAtouVmgikzsEcBanGH-UH-lzIOfQk8C8wsMGOFym52uvrmgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحنه رو پسر</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/84527" target="_blank">📅 02:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84526">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اگه خداحافظی مسی هم مثل آخرین کنسرت ابی بشه چی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/84526" target="_blank">📅 02:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84525">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شوخی بسه دیگه حاجی، وقتشه بیایید بگید مسی تازه ۲۵ سالش شده و نیم فصل برمیگرده بارسا</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/84525" target="_blank">📅 01:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84524">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vn7fkpUzzmXbBx-W-8JDArEuJoLr2QUMNHqpZHCYpc7fMXMAFsEIRtwax9O7I-CkYbt1CutE_Xm0eEsqudWNBtoFQPeV-6N0GufmiVPpvx6CXN2VRTfbNAe6TMW7eUtwtg3kaUjiCBMMbUjyZtRGOZAqNM55gS1In2mqTMi7Xqt3nkg7XmukaAKS26jUwo6C1YIVqlWUfkV4cxcMEXQAeN9It_6hxBcZCVNy2HV5VCH0E6QMmrwGg_lTumG7BA2R4MlpBtz96TKiFgCgLsLFKF_3AYcyYwm7xmXTo0DqsIX34S3VR_OlVZvLHFj5Fhm6bT6kzh9-JbXZjMlpYaUspQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاهی که امشب آرژانتین توش بازی میکنه یک ساعد قبل بازی:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/84524" target="_blank">📅 01:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84522">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شما براتون مهمه که تتلو عفو خورده و برای ازادیش باید تتو هاشو پاک کنه؟  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84522" target="_blank">📅 00:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84521">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHedWoL9-WjW4YbJO1CMFpAM_Fgk2cYxZ3_ojsHKCDkORlS_rU8_-xZ_pzfemVljmWu--5pNwQT9mgEsxY5TX_pIRBBL8SyJs_2AHoGNEH6UL5tYl2xze3ikjXJLH7_jljdtJOOApgeoLfYwnQUDyg98Sv5OLFCVNLSoUYyD8aICDHu7BCyGfmfQBfYTzKi314TzJXxvCVvqcD2wR-oeWF3_egW3PGSw-csGG2blsHa4Nrl-L1gXYlKb6EptNKkRH3vTcImhGOSgUamdGhhn7nP2ky4dbgxQ4xUWACjWab2nkWztzI4yWDSdqai6nh8jcEILv249M45hV8as_RJZNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر این یارو خداست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84521" target="_blank">📅 00:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84520">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شما براتون مهمه که تتلو عفو خورده و برای ازادیش باید تتو هاشو پاک کنه؟
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84520" target="_blank">📅 23:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84519">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ قاتل :
باید کار را تمام کنیم و تنها مسئله این است که تصمیم بگیریم با روش خوب این کار را انجام دهیم یا روش نه‌چندان خوب. به‌زودی متوجه خواهید شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84519" target="_blank">📅 23:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84518">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وال استریت‌‌ ژورنال: ⁦CIA⁩ یک لیست از ۵ الی ۱٠ نفری مسئولان ایرانی رو به اسرائیل داده گفته اینارو نباید ترور کرد چون بعدا قراره حکومت رو به دست بگیرن تا ایران کشوری نرمال بشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84518" target="_blank">📅 23:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84517">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">همتی: بسنت گفت تا دو هفته دیگه ایران فروپاشی اقتصادی می شود‌. ده روز گذشت و چیزی نشد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84517" target="_blank">📅 22:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84516">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHd63QHJ6FFpFmMy5XxnutNKCNgAA1R80-xiuu4QqLtsEzMQxeJ7dXtqNvmiha8Aso4AptP3RhwYhHE9-8R2cJ6KaDw90NjzZVpx1VWPKaONMwicRkstw7J_dtQcTusWdoPBA8b6RhkfFhisqdAa1e_fAdHp7mhPPtek2bbE2e0vE7Avs-C8kw-WoQRziWcYkBu9mcLZyDko4iw09b0SuFS7jnDIxTmxacp8H5jd8pN9wQsg1QGV9m1DQY9AeZLFB8nlZZFxRXUaf8_bVaPUMmgtyoDiICdbO3zjVNv2CBG2Ox_FxMlpPPuRR5aeQXqEZYdFY8mngQnupY8UOSXxqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلثوم اکبری که 11 شوهرش رو به قتل رسونده بود، به 10 بار اعدام محکوم شد و این حکم به زودی اجرا میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84516" target="_blank">📅 21:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84515">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpExLJ3PiCVhZOR_2q4zmwbcOKP0CvyZHVHeOetfVenv0v3uwNICAtFkMWMClx9wDAK5SNy4DEmnAq1zOo93Fs_3fci_vs5am8yaXKqkWtWREZHU3UMvC0H4THD9wy72G04BJlNLuqwimX-0kgER7iP4qReCm5nETRwRMjDMhKE2MEaOipcVdfdUotZ4XFHwFwf8U_1Jm160-Q-7AJPpoABH06QY3hWjdi8G8pRlc1qbGdNNrcoKpSXOFG7wW5179Py-KG4gcKrKlEEX0dqxYEBlHgl894jLwB0AATtM3t40rKCV87aRuXOo4CFptFt1wHUz0_yxY8siSgTboeiv3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته نشدی انقد پول فیلترشکن کند دادی؟
🤨
سرویس مولتی سرور با بیش از ۵ کشور مختلف و آیپی ثابت
👌
💎
سرویس های پر طرفدار :
💫
1 کاربره 1 ماهه با حجم نامحدود : 148T
💫
10  گیگابایت 1 ماهه : 45T
◽️
-همراه با تست رایگان
🫰
جهت دریافت تست رایگان و سفارش :
👨‍💻
@storkvpnsupport
🌐
Channel:
@StorkVpn</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84515" target="_blank">📅 21:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84514">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پوتین و پزشکیان جمعه با هم دیدار میکنن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84514" target="_blank">📅 21:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84513">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Waiting</div>
  <div class="tg-doc-extra">The Creator</div>
</div>
<a href="https://t.me/funhiphop/84513" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید Creator بنام ویتینگ منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84513" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84512">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiH5F-5u0O_AWUJOQDJoo1JgrF2c4-n6ylP9MueMXaWhkzGYliGSPa6llID8HEx6cGlJK9lyDIn0UTXCn2u0iK5cBcyUDar_FtkTQiN8_nxGBIc_Wd0Z7At6OD-rOTnXTEhtEN9_-3SMoQDUeypXAtBalzs9bolxkGyX0qp9HNWXTNPA2pawt6bAmWVIqh8ndV-yZx37TFYrnnelxINk1pwgkQ0bYNC8WAs3HNRJs4J-fyzvmf5FVY9L45xLHxMIohZmk56VaY0_M3GOzN4fvHGbM-PD7C5j3jfI1kvN_D-n9vll_9nf_Ou6rUCNRBQ0hHiKUMYc33oe2XOYO2RZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید Creator بنام ویتینگ منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84512" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84511">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حمایت از آرتیست:  Download  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84511" target="_blank">📅 20:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84510">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ملت ویو هاشون میریزه میرن با یه رپر هایپ فیت میدن، دکی هم رفته با کسی که مخاطبای رپفارس با اون فهمیدن معنی فید بودن چیه فیت میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84510" target="_blank">📅 20:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84509">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترک جدید عرفان پایدار و هیپهاپولوژیست به نام "بچه مردم" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84509" target="_blank">📅 20:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84508">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9LrdOAbVveXxhhbmzGOArAXW9DXI2cwtVtQjqdhURWFMtk4dOSoqU6ElpbPBhMP-bWz5vAw_u5igxQYkufPs8DFonrwCtk-DqEeULSjzU4rsqVsiMyWrD45lF1D-CD95ltB-c1gje81WS89VQ41ZmHByQoVmzU_iek2B-N-XB3BfKnuR2d9woIA35mfppij9JSFSrf_7UOZvdj1gpFs0p5hNLJMfTd_thaCialzilGgM-fIN49v_Kx678f51RK9sKtezuUTkC9butWm9TrpbtPr7tZ1BvLdoKJ50rf5yAFjuIH4PZkENYjZ2nFG1XQyZhLuUCZT-aZ3KzBaknwADg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید عرفان پایدار و هیپهاپولوژیست به نام "بچه مردم" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84508" target="_blank">📅 20:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84505">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab91fa8060.mp4?token=qzCGuBWecQi5Qb3BRZnYka5zU18tO39-Wgiq4SHvwmUp9cayur-mm332qeToVV43MnUH7pv5LjS6eYcwuOO04vTwJiKmBVnG1G2Ip3dscITFSQFa-_AeO52SvxT9A4uiMTwZXBpkJpq2hyGhPM6R2Y6ZvTCjq1pmidz1p_VTEi2WeBWTd9EQW8F8d_-j6n8dSKqrjFEcp9h5FS-NJCtNFQ7kbwY8JklqUt0A4Q5xxma3N8b57qT1tRZEFyz3zch7w5F6RuI85xBff71i9olh8AmQdR_wfYppZRColbPrRrMG0lmcVS7wMw1GPPPEqLn0-L55Wek1xO1eDjUFEhdAIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab91fa8060.mp4?token=qzCGuBWecQi5Qb3BRZnYka5zU18tO39-Wgiq4SHvwmUp9cayur-mm332qeToVV43MnUH7pv5LjS6eYcwuOO04vTwJiKmBVnG1G2Ip3dscITFSQFa-_AeO52SvxT9A4uiMTwZXBpkJpq2hyGhPM6R2Y6ZvTCjq1pmidz1p_VTEi2WeBWTd9EQW8F8d_-j6n8dSKqrjFEcp9h5FS-NJCtNFQ7kbwY8JklqUt0A4Q5xxma3N8b57qT1tRZEFyz3zch7w5F6RuI85xBff71i9olh8AmQdR_wfYppZRColbPrRrMG0lmcVS7wMw1GPPPEqLn0-L55Wek1xO1eDjUFEhdAIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشق امشب آخرین بازی ملیشو میکنه و همچیز بعد ۲۰ سال تموم میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/84505" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84503">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=HK1NIB95Tbf4sd8o1MiL41-op1CGn2zlLAEAk7meE8AvMgr86Vxd5cDiNQIB1Q118zKwwmHodbAaAs0SYxU-7gLhw8hS5cgVz5Co4-RqAFI76ZMT2SI3hXzteqmkR-PjqHqN5pUrU9jFa349Tk1Mzsamw5dkxJrL-dFTIP73eS0yOWnvQnfl0jYiScTJwJwDfTlo84K8Pd5pSk_rI6rDjulCSQN8a_ExzCVqtEjYaWMXwAyAc_HrS5FneeVjrnn34b_V-PpOZcGfOEuD67IEw3nN3d0SNbssG5qo5_Cg0wPYSwaRrgG3DX0PvDJqizPN10Y2ZfKgKwceKoWiR47w7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=HK1NIB95Tbf4sd8o1MiL41-op1CGn2zlLAEAk7meE8AvMgr86Vxd5cDiNQIB1Q118zKwwmHodbAaAs0SYxU-7gLhw8hS5cgVz5Co4-RqAFI76ZMT2SI3hXzteqmkR-PjqHqN5pUrU9jFa349Tk1Mzsamw5dkxJrL-dFTIP73eS0yOWnvQnfl0jYiScTJwJwDfTlo84K8Pd5pSk_rI6rDjulCSQN8a_ExzCVqtEjYaWMXwAyAc_HrS5FneeVjrnn34b_V-PpOZcGfOEuD67IEw3nN3d0SNbssG5qo5_Cg0wPYSwaRrgG3DX0PvDJqizPN10Y2ZfKgKwceKoWiR47w7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکارترین پرونده فساد توی تاریخ ورزش کشور
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84503" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84502">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رایتل ورشکست شد به مزایده گذاشته شد
شستا آگهی مزایده عمومی دو مرحله‌ای فروش نقدی 100 درصد سهام شرکت خدمات ارتباطی رایتل را روی سامانه کدال منتشر کرد. ارزش پایه‌ این واگذاری 130 همت تعیین شده است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84502" target="_blank">📅 19:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84501">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf8c96111.mp4?token=nDXyCiChzwMv3aWixe1lUHZMrQ28cUWL_c7IsaybfsTMfb_WGUKSVKue5D7hsWDu0B_8wHlfd6wnSrgcYFcfzO5suNzEERS9Kpy_Vo6QT7KyQssezmV7PgemMUiKQkil_ubVsYwcYCkUtPQ5fHIZMP8GZCKdquKvSFyL_B92gF1AbFzamr0ASQp6Z1FEQkO3DWUrac6LWmVwZnYxRgRmge9AbMgPyfd9L2HxwSWhm5N5BXW7L7Z_qs2VLMIhbtHgrBT-I_kNhXqFvavLmTqWbHyRyNngH4NR7JjYDH3bnZYqgERPgBTO-FnVfh3W3WbDuEEJE40SIZyMwyvTWqSxWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf8c96111.mp4?token=nDXyCiChzwMv3aWixe1lUHZMrQ28cUWL_c7IsaybfsTMfb_WGUKSVKue5D7hsWDu0B_8wHlfd6wnSrgcYFcfzO5suNzEERS9Kpy_Vo6QT7KyQssezmV7PgemMUiKQkil_ubVsYwcYCkUtPQ5fHIZMP8GZCKdquKvSFyL_B92gF1AbFzamr0ASQp6Z1FEQkO3DWUrac6LWmVwZnYxRgRmge9AbMgPyfd9L2HxwSWhm5N5BXW7L7Z_qs2VLMIhbtHgrBT-I_kNhXqFvavLmTqWbHyRyNngH4NR7JjYDH3bnZYqgERPgBTO-FnVfh3W3WbDuEEJE40SIZyMwyvTWqSxWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسره جلو چندتا دختر جوگیر میشه می خواست از تو یه ماشین بپره تو ی ماشین دیگه که بگا میره
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84501" target="_blank">📅 19:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84500">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ea14d958.mp4?token=hWdDFZKptQ0JzM7JJ8-Ic7VzRm31CLaw1Z9vtQbM_iX2SWA9vUgn0tEm5OKgSgQVM3vJvTsy1OkukooV_M6_dQR6gTwYVZgAaTdqH7il7IWgeQ8DaYvLqfGc8iuNVxgkQPsGHri2TZKYa8PcGxf5ALhPQSRGfw1ifmdX-HymevUPEj_g68hLKdHw46oD1fp1BM6fvUFRTNzvYidZ8JPtD76824KFeD-8d2eI0UT-t4KdUs_ngdrVGNWny-w9Dx1_hJ8sLv0yU-oLE_ehnb4_715p5kbmMO3Pnt1bBjgM5sx_wNUdZc8nnSRsQksc3Zjx9iuBvRA9_j_hF_fPQ20JMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ea14d958.mp4?token=hWdDFZKptQ0JzM7JJ8-Ic7VzRm31CLaw1Z9vtQbM_iX2SWA9vUgn0tEm5OKgSgQVM3vJvTsy1OkukooV_M6_dQR6gTwYVZgAaTdqH7il7IWgeQ8DaYvLqfGc8iuNVxgkQPsGHri2TZKYa8PcGxf5ALhPQSRGfw1ifmdX-HymevUPEj_g68hLKdHw46oD1fp1BM6fvUFRTNzvYidZ8JPtD76824KFeD-8d2eI0UT-t4KdUs_ngdrVGNWny-w9Dx1_hJ8sLv0yU-oLE_ehnb4_715p5kbmMO3Pnt1bBjgM5sx_wNUdZc8nnSRsQksc3Zjx9iuBvRA9_j_hF_fPQ20JMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اونایی که تو سال ۲۰۲۶ ایرانی ان:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84500" target="_blank">📅 19:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84499">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mumy8u7XGNtJe03wH5pCVNUmAP93l8YKoxIKRKC6S3vLb59GIsKd0eo4OnrN0ZWqln3rdVlD4gvlQGA5-iiVGNVhXXfuwi4lMe1dcljgT3aI1y0FKQOQMCiRcxMvJUb6PHSVzE8FdfJAL9ls6Jx5DBsegeEBgAFFQhQ5TogccAKScbnz8aifd2cqh0z7DWGT-Pi6isfu1hBzg5y5pqzpWuI1xllUabCEs4tMjBm8kHyvAT1sHmSirduTTdnmHYhQ3nV0T9gAgK8P9pHuA2sLzX_fnrUk42bCUswTi8PS3GKL3hqQ1CqsJgxgFtU1Pwq7bNtS9S7DuLQLNzwLZujybA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا نامزدش چطوری دلش اومد دل این بچه رو بشکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84499" target="_blank">📅 18:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84497">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb27cdfea1.mp4?token=M9d-cLUSql3zE8RDqBkhq3rBByI7IjdIiXxspsMnX9c6n9XsLZr-nttnWiAq4w-uZ87xW1SuBz_a9ovHC6juORcZqTQg4Z0CsNPO5r5cWY5kh33wyl___qOpiAU8v_fTqeCL21KDP3cuk7TEPsyqOz3X1dDQxLgGafIz7-kOz7IlegzOiCNQ5-1KXaeeE1MMc-dE6tLIf5-xKmdadW3kpuAkZk_YJIiXN_G3Lu-HV_Na1nGkRguaMOupGPk9D28dvkts3WovnjdEPqIrtmrkhveFoNsZsLB0kixR8ALRYY7Typkof2rK5tS_GpGll0u_TojyHlK2Njtl5lK8oSXCMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb27cdfea1.mp4?token=M9d-cLUSql3zE8RDqBkhq3rBByI7IjdIiXxspsMnX9c6n9XsLZr-nttnWiAq4w-uZ87xW1SuBz_a9ovHC6juORcZqTQg4Z0CsNPO5r5cWY5kh33wyl___qOpiAU8v_fTqeCL21KDP3cuk7TEPsyqOz3X1dDQxLgGafIz7-kOz7IlegzOiCNQ5-1KXaeeE1MMc-dE6tLIf5-xKmdadW3kpuAkZk_YJIiXN_G3Lu-HV_Na1nGkRguaMOupGPk9D28dvkts3WovnjdEPqIrtmrkhveFoNsZsLB0kixR8ALRYY7Typkof2rK5tS_GpGll0u_TojyHlK2Njtl5lK8oSXCMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بری‌بت
✔️
دو شرط رایگان در روز
⭐️
🇪🇺
برای پیشبینی بسکتبال، تنیس و والیبال
⭐️
🥳
بر روی بازی‌های ورزش مورد علاقه خود به صورت زنده شرط بندی کنید.
🤩
۳۰٪ از میانگین هر پنج شرط خود را در قالب شرط رایگان دریافت کنید.
💱
0️⃣
1️⃣
🔣
شارژ بیشتر برای شارژ با روش رمزارز
⭐
مجهز به سیستم پی اس ووچر
👑
😀
ورود به سایت:
😀
g14
🅰
📎
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106
❤️
کانال تلگرام
😀
📎
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/84497" target="_blank">📅 18:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84496">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جوک برتر قرن
احضار سفیر فرانسه به وزارت خارجه ایران
در پی برخورد خشونت‌آمیز دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گسترده حقوق بشر، امروز سفیر فرانسه در تهران به وزارت امور خارجه احضار شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84496" target="_blank">📅 18:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84495">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بزار باهات رو راست باشم عرفان، همون قبلی ام به ورس تو میرسه میزنم آهنگ بعدی  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84495" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84494">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دیدین گفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84494" target="_blank">📅 17:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84493">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHsX4Iv5C_vRo_vH_XOOq0cGCQqDPcKJ3aFAjjSvZlNPwS2d-SAPBubl3F8H4gUuCvUbQeJoS1Gl7o1eXDSj0vOyjIKcGktmQ_ItHfL2ftOdcnrlTAd0qgmqU6N88pXAmga6-VDmuw5Z3iBKymuP71Q4v8y1Z0RmUBdreI-qxsXLMhztkGKtK538xQz5CO6X-3aJRcVI_7Bni0WyzC_3qFT7z7KSssp1K7p_8I-VkNx4aJitIfDcahUUN8KUntANJZz7r-92p0iaI0O_ZRiCMCTPT4ZrsS8Oxb4y-kHfJKldj0OWF-uGwbO3U_N0YJCGEs8YNNTr94ga2Ry34-obMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا شکرت
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84493" target="_blank">📅 15:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84492">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qd6HUzTr0_Q4WJC2rVcVxQB2PaqSLWqiauWgaf4lXo7pKeHkZSn0ZilVbOPN_kZGNK-vLnmh60M2jO5xVILOSYcZ5HBnqV1bBBJ4ABgYYu_8rhhBGqybJFE4pXHy8efnRpJ1QIuj7uvf9OyUblnZazs3oB8NRSo7N6FLQZoL6SyVMI7UTJUAXhyu1VgxsDdSuGEUsbzMUa_df3dKQFNZAD8ah2-BdwH5zIwIy51PxWsa0EaU14d6cVZXrCNoW0wns_maguGbGmNTHWu4HZLBPpRA5BdBHsj9iuOPy2sHhL6-YwamFCffdIPwYTeUDDdyB2gFP6wvTCGW9_Tzpv5o_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی فلج های مغزیه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84492" target="_blank">📅 14:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84491">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دولت فرانسه اجازه ازدواج مرد با مرد رو صادر کرد
👨‍❤️‍👨
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84491" target="_blank">📅 12:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84490">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">من دقت کردم ویلسون هر وقت با ودکا مست میکنه ویس میگیره، انگلیسی صحبت میکنه خطاب به ایمانمون و عرفان و هیچکس، هروقت عرق سگی میخوره فارسی ویس میگیره خطاب به فدایی و پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84490" target="_blank">📅 12:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84489">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaGizlxg788ZL3rgni1SXM7VH-FIh80wovOwhM2WtJ50IL9q54HC-5UJvK_65xhFwC3WxYyc2TACE8M8ys_RaFYprr04wBQi_NE1Z7LmcwXU5LDvtX7L7S7280KSNXEG1NSTmqKc28-S4T1dEUUfp8y_8IneL9UotWf60qQTvkA6V1OJUisj7ZdHF0N0Ui8JTf1L9YXL8l5R69yoXekDlyq5vxLjSniGUkhgTIeyIuVigB8F_BjFL4vDBUsNz9IUgOEK90bNMpIIb9T9w8OE79j9DVM0qMSM2gP0k7_f4GoROwCdxrhA8qIXaBCRk-jh1AGyKjkoGE2bOTKd-pkbng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزار باهات رو راست باشم عرفان، همون قبلی ام به ورس تو میرسه میزنم آهنگ بعدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84489" target="_blank">📅 11:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84488">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هرچقدرم از خطرناک بودن طاعون تو اینستا کصشر تفت بدید من یکی این سری ماسک نمیزنم، کیرم تو این دنیاتون</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84488" target="_blank">📅 11:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84487">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2951b20357.mp4?token=hRy5uT0CYQHFwaGjwtgA0-8WoQ-uJykN0SHKqQNNYbD41T0Y7pwXGVSyNY8iz-TI1cxpsdC_Un4f4WgwVinGPFjDftayRWc5geCrW9IZ_WLIHQfv1i13d_1nSoe-kEUqhNQaGzrxElGGK43Vsk4EDz07oN1xSWFOD_nlcIMCR9UDCTI8-atvFJBXE2MsDQq3uPuzs9-Em6vA_T0P2B4QethfjZtunXtgducucC-57x88tD6KflZLPkXCSpV39S9tbRWCEBNCbL701AtVgk47E5hdwa8YKoyry_RUtGwdaKiWGD9KGduXrXAK8wyd8Vj3zlnmFPwehLJGe23cvo74Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2951b20357.mp4?token=hRy5uT0CYQHFwaGjwtgA0-8WoQ-uJykN0SHKqQNNYbD41T0Y7pwXGVSyNY8iz-TI1cxpsdC_Un4f4WgwVinGPFjDftayRWc5geCrW9IZ_WLIHQfv1i13d_1nSoe-kEUqhNQaGzrxElGGK43Vsk4EDz07oN1xSWFOD_nlcIMCR9UDCTI8-atvFJBXE2MsDQq3uPuzs9-Em6vA_T0P2B4QethfjZtunXtgducucC-57x88tD6KflZLPkXCSpV39S9tbRWCEBNCbL701AtVgk47E5hdwa8YKoyry_RUtGwdaKiWGD9KGduXrXAK8wyd8Vj3zlnmFPwehLJGe23cvo74Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمو بخدا من نبودم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84487" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84486">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84486" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84485">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUrYFXHnPSft5fo-CDT8eCcP9mnLengvLFwEm_sMHZ0nsXrcykPIp-T10oLfBiN8URCpmCpLIfg3lDGwVpcfcammRPbCC88O3q89KNSjWhSms27n1XFxYnLDxXwc0gzDAk7omjCKuIN5vIUWb03abL7u6SvQKj3b4akB-G7L2ED7KVuZmZWemcPQEQ2I4qr0GadfdUvQKHWOINZ35hpKSuK5lZlR7rzClpZ78yXb7z4PLz4jYPq6fc5-6UvynsOalaJhFnJUuDIAP9IQ0om4CTD99ppj867sahIhok4Lk6yduc741iDI8EDcmu-qeh6IcKAinHEZfnReqQRfjVGCug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
کرواسی - اسپانیا
⏰
ساعت ۲۲:۱۵
🌎
📲
مقدونیه شمالی - سوئیس
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R14
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84485" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84484">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رئیس پلیس تهران بزرگ: از این پس قلیان و موسیقی زنده در کافه‌های تهران ممنوع است و با ارائه دهندگان برخورد میشود
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84484" target="_blank">📅 09:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84483">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سلام، پاشید برید مدرسه+دانشگاه بدبختا</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84483" target="_blank">📅 06:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84482">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سلام، پاشید برید مدرسه+دانشگاه بدبختا</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84482" target="_blank">📅 06:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84481">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlhX9UPLioCDkCbDwNUlmyYqZdSIQ1ZJ_nuBJwY1lNepFJZqrOcdwteh3z7eJb7oVnikFmCW-D2nGuP3HSOBgv82kUsdipXKbeh_fsG932xt-NitQKX7OgHD1cp9YAWBzr0pG6twMaENb0kcaMCTsgzfL-LxuUQUzN_4Z0AZQfpvwxG7J-KkxsPh4fdPvSY5lBnMUFebn1mjL8q9MDiL0TcmDiVhpcGqLO3eMc5BtaUcZp8Im0OdyRCSYWVxuwtdpV-6ATEfzVVAh9s5X9sJztpzFTUfZhs3Sf67d4-GDJ6NJ4ncj4-bX321ZllS4UPSi1pjK30tHXsnNh1H3SNZsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حوثیا که نیروهوایی ندارن بالگرد آمریکایی چطور در نزدیکی های دریای سرخ بعد از کد اضطراری ۷۷۰۰ سقوط کرده؟
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84481" target="_blank">📅 01:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84479">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJ0CRqrAwKGhSEwvE0bDcMfvlvIuxZCkdgqfivkTr85tccZTF902kyM1fdOspQFzs8_2gyND7dxQdaSrslJxZ6i-FX3a4C9Lrp0nzPQ-frsOXDHk5LzbqsbrBSoHKD8R8kyg0JQjthD1ptMqwPpP0oYQaARjqIvHp7poyAd01dZ1LhwYBaEel8q7n_6bkxlBQhJmIQusFyM4mGpZdXQHJDpH610iHDf-UWan98ecYjuJ-1oQdsdOdItESYSxXCOb2qXgREepgnMc_QuQuTspIyI_EajRAteQ7XfzFXRA-EnwBKCDhtn82ZI-3dy_zyhwGJR57S8-mIzXSpjxGGWp1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LR5MET5GqdUfwaEMnBrPxlIsGdIyeND8Z6BB9OQODY6PSvuoyiSM43tlRl7N6lr2TI5Z3xyULO0zkxkstKvMt4mjSHnhni1zaQ6n6wiGHVwmdogv86OgUEObOB6mDFQNRH_ZdDzekt8YXclwtvi_aKkKZXBG5U2UwsJHf_xb1MLAmiwGQWIgu4ddBOLttWF2A6wbUMeDTA-jjP6GroR3xFGxLtgc9-9QITkHayzM8YuereuQBwx-GS6mLh0BPKyPMZHbtIwyEt-gYPzmnR6AWsCPewqClh07bXTDVwECNxqjoKDoijCxJqnZYjT-NwL6gwbemVLTH2PqUJ81T454fA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بهترین وینگرای جهان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84479" target="_blank">📅 00:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84478">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اولیسه واقعا خداست، دلیل این که فنای بارسا ازش بدشون میادو نمیفهمم، بازیکن رئالم نیست بگی از رو تعصبه</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84478" target="_blank">📅 00:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84475">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اولیسه واقعا خداست، دلیل این که فنای بارسا ازش بدشون میادو نمیفهمم، بازیکن رئالم نیست بگی از رو تعصبه</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84475" target="_blank">📅 00:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84474">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjehHj9xyYx45b7xxpJygub1rbcq2MiODSYS8WR1wi9R9RcQMGA9IAidvQB3KclfqFeCpdwc1IwaFUiXK4MQ8cVifxtFPPhNQVdZX5OdmfWHlX90LZ3JVM-QW8pM2VYUaeTZ6we5PG1TDDXQ4XN3dwkFkyAPIFF1fZMs_ExlfNStGYZJFXiHNWsbIcqi-8jjAnIhA0ssFVAyHW4eRyK54wGphqXSY5NDIWLvf_-h0wUpz3CWTlOPwK2Eja6vng4EaUzUlwllGX_coxCvhsdT4MG3KAEi6daQzkWmG43Xlz2e3C4MGE0eGKqLOrXq8k-p37dOnCbFUAokC7j9h1XUPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر تنها کسی که شبیه آدمیزاده بنیامینه که اونم فعال رپفارسی نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84474" target="_blank">📅 23:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84473">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ:
معتقدم ایران در تلاش برای ربودن هواپیمای «فلای‌دبی» که عازم دبی بود، نقش دارد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84473" target="_blank">📅 23:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84472">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ویدیوی وایرال شده از شهر شلخوفِ روسیه مبتلا به طاعون تو سیبری که نشون میده چندین نفر با لباس‌های محافظ و مخصوص، تو شهر درحال رفت‌و‌آمد هستن؛ اینطور که میگن در حال حاضر بیمارستان قرنطینه شده و داروخانه‌ها هم آنتی بیوتیک‌هاشون تمام شده. @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84472" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84471">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b249c59827.mp4?token=eCoyyaVg7fPR2V9JWHw6o6ABo5brlm-hpq7Q9zzbkn8S9tPCMrHjz2ePaYicMojnlTD-BXnb58IszcCdAqrPNy1knXdVVfQRoEGuuXjpeN47fZ9L0wbcX1xwuTXhZ1kY9ncsgYtRG267Rtdit_xNJmocZiHk_CDCH2z20dCuSLestW7nMLcWecTmp7bFyPqS2O-1B4nHTfYjSxb2c88fN4culrrE0Jx4AIXtevF5t0lSDQoVErLz4uJ_eRpkGFUeAxHg_AvmLv4w11SU7kL3T2qClvpzGhypPJHcRHq5PqBeg1n18mVWSl7l9PH5jguIjlwm1p9elKaAVSyiTblwNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b249c59827.mp4?token=eCoyyaVg7fPR2V9JWHw6o6ABo5brlm-hpq7Q9zzbkn8S9tPCMrHjz2ePaYicMojnlTD-BXnb58IszcCdAqrPNy1knXdVVfQRoEGuuXjpeN47fZ9L0wbcX1xwuTXhZ1kY9ncsgYtRG267Rtdit_xNJmocZiHk_CDCH2z20dCuSLestW7nMLcWecTmp7bFyPqS2O-1B4nHTfYjSxb2c88fN4culrrE0Jx4AIXtevF5t0lSDQoVErLz4uJ_eRpkGFUeAxHg_AvmLv4w11SU7kL3T2qClvpzGhypPJHcRHq5PqBeg1n18mVWSl7l9PH5jguIjlwm1p9elKaAVSyiTblwNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این‌سری دیگه ماسک نمیزنم یه ویروس ناشناخته از آزمایشگاه طاعونِ روسیه پخش شده، چند صد نفر قرنطینه شدن و چند بیمارستان هم بسته شده هاگوپیان: طاعونی که تو روسیه پخش شده، حدود ۱۰۰ برابر کشنده‌تر از کروناس  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84471" target="_blank">📅 22:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84470">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این لوکاکو چرا نمیمیره</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84470" target="_blank">📅 22:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84469">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbed26b887.mp4?token=ppQvZalSojva9nOZiU2omEj3s__EXwZABvybYXz3LuIMWKIzxU_Lqr4jAY1V3GQNKuw9MGjg13obnCWXk509fPRKneY2ZPtash87Ie6h0knOnH0jfhuERedREEguVTJMWt9TizjMxPcdCB7JIdfOeJnMDYsDRiyihW2w4a0QnNn2zjkdPNC67R1FoLgxuln5nOUiVDAojbKtqr5uVHpKg6YkOJmSLtQFul3WpQI_SZ5WfhW2lZP9yeB2V7Ft7veqdQAA1QjtP-LaSEGF3428JktI-Cnj6q0S2VBnUJpJjP7RNeOk81uIswd6CEHb0GJ28anGIYejRm92rQLb50ZM9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbed26b887.mp4?token=ppQvZalSojva9nOZiU2omEj3s__EXwZABvybYXz3LuIMWKIzxU_Lqr4jAY1V3GQNKuw9MGjg13obnCWXk509fPRKneY2ZPtash87Ie6h0knOnH0jfhuERedREEguVTJMWt9TizjMxPcdCB7JIdfOeJnMDYsDRiyihW2w4a0QnNn2zjkdPNC67R1FoLgxuln5nOUiVDAojbKtqr5uVHpKg6YkOJmSLtQFul3WpQI_SZ5WfhW2lZP9yeB2V7Ft7veqdQAA1QjtP-LaSEGF3428JktI-Cnj6q0S2VBnUJpJjP7RNeOk81uIswd6CEHb0GJ28anGIYejRm92rQLb50ZM9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با یه پست رپی ناب روزمون رو شروع کنیم  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84469" target="_blank">📅 21:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84468">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خیلی دوس دارم بدونم اینایی که از رپ دنبال محتوا ان تو باشگاه چی گوش میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84468" target="_blank">📅 21:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84467">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">منو برگردونین به اونزمان که تنها دغدغمون این بود که حصین زد یا فدایی
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84467" target="_blank">📅 21:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84466">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">LCPV</div>
  <div class="tg-doc-extra">Creator (ft sahar)</div>
</div>
<a href="https://t.me/funhiphop/84466" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید Creator بنام "ال سی پیوی" منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84466" target="_blank">📅 21:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84465">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3jrLnfApb9KjTxnPOI93DpMOzJPSUZxTuOPxZk-8BgzcUwJlW_3hzCzxi5zjzToTIpC50eD0VfkWE1GgeANMxFD1ZfICf-wvITvNnAEppMC6SnHIQNfJOWfSuLJwIQMVkoF7nkRG6x7jfnsyEjh07Dn91VTSttEEfGgeFemE5wjJFwR1ok7WJd0W_DWiKIVVoBAMQLsQWLi3N5ptVLTQGv7AtNlBKohcAt3TjkZmH1FHhsnLNY1yyBe1r9kMKR9bo7BStctK7twdT8LLPXMcJtMkgClJBm4GYYeoZkr2ShucjJ6_wFkKn0P6GWSM-GUllJUpk_f2bjN5vTQMuBdow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید Creator بنام "ال سی پیوی" منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84465" target="_blank">📅 21:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84461">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GY-vfxk035fD3lmIKEe_HRovWaEXzUCQQoNyhp0NQuLzIi28AgwEZIn3W92T6jbtnNgDqD7Y0QHyjCyUAKe87uZUH3BayxsmuuJ9FWcbbPHw_JLAbBbB4bYu1l09jMNaIlp7U_4PpfZ8UaJQD5d0Io8fBu7Zz9toOeYsM3eGGrKleylD0AbEm5SngCNrfyd9XNrW4oT3O7xyiVYdTykV5N3vsWDjNj-7a-XvHd9C8yg7j0KndNwpxpXYb30szbpjwbNzziwiv-MlC-Fp-T_v8FvYi1OBkVG0ToI290P3yNdLAKhUCIUw8vJ1ix_aF67OVYJFDw6HjnlJxJz5BM-_mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6KfOApMRASxrAaeLMRyr3ZpTcuuPN-XY6Z6eQOGissYU6xhQX2rlAfSBbhS-b6P8RXZ7t7pEeXJ3xoil7rZjkRmy0DIDF49zU2i6aNfS0ylh56xyeDBuR_bbqSENOdrML1qChqRNWRU--v7webMoYl3Bpzd3a_1Ox_Q2eEGdHQd5kpHhyaICrwpZkmWwqX8yBP99c9XQ3ZZqxdBqLfRe-YCx7tAO_2lvKXaybGA7l40Hbgp6y6DWLpArHkmCL0shindTQ6cA1H4a3be_P7sLG7fXzoWQyCt7rgN2qHXe5m61o53iAbPSK_DVb8bQRHqtnkJc16wEEXeVL3DgRZFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVOm3uyGQxeOtCR0I9FWHkdVGvPKhHIbkJBtH6-KNfbLEdeElGcBZ3RjSCZyqSvcjPRIcoA4eboc27QByWJRVf-KZ9TRwQBo9-G9ONMwV7vfa0fjooKWsmDZXo2EM8UVXCcoRy5eEsh3-fjqvwWFiTe4FRc5jyZD69QXU_ICFkzoTi5bnuXdd9xshR59p0shfaLlS02-dKovm1ROkAZo5cFOX1IFCFtp0zEupJGSqJJHHxuhV_xrRq9dz9xDZXQwjUI-bkLHtDvi_OIuMByDRfzGob5uOG6-g_FvGblE3I9epNdMveNodk_dgHvkHKIEHAznOv4uicGff6WJa9PYdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ef8uXIQBOuHOkTX4GAeLGuXFqJM2qUZtOe4tJbC7x0NUwqdDuESoe6eZlCx3ZqwR-SCNxxqF0lfNw_psopciIfwMopAuGrtL3bA-82oZOpTdYBOl-47F4J3eNjCRz8lZqdZ6SYP2pNgbIjfyheJ_26pkoh-v5kANjzi5CF8FVqs7hCA4dC_hBCgi0iVLapcS7KP18b_m63iqe-Bnqva0VV5eHT8G0soGmIgXuaVd_Qoxs_aCrIXRXb3-ojm9KeAipqUrr4dB0FKUu81RaMUT2lUxnPBic0AUKTLxwF-IYsHf0-4jsPOl7gCbxCR5YMc90Q0UVPxUQg7szZ6lSDumeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلیشه برعکس و اینجور پستا تو اینستا زیاد شده و دخترا با این ترند حال میکنن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84461" target="_blank">📅 20:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84460">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دکتر مسعود پزشکیان:
تاکنون، آمریکایی‌ها سه بار پس از مذاکرات به ما حمله کرده‌اند و این نشان می‌دهد که آنها به دنبال گفتگو نیستند؛ بلکه هدفشان سرنگونی نظام جمهوری اسلامی ایران است.
حمله آمریکا به ایران، که با هدف سرنگونی نظام صورت گرفته، فقط باعث اتحاد بیشتر در میان مردم شده است و ان‌شاءالله، این ماییم که از این دوره سر بلند بیرون خواهیم آمد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84460" target="_blank">📅 20:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84457">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ارتش یمن داره حوثی هارو با ماشین زیر میکنه و میندازه تو دریا:  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84457" target="_blank">📅 20:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84453">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e122cdcfbe.mp4?token=p4lGuVJQQpG47VYSvvCAwuN8lBN9qPbjsmEJcwpOnBaScQmSIjByVS6pFwo3yFwsMVaphnI-DhwtxHcMq1z66JuSXgnyMRAmUPWjK2XfKE0AB7OWHM9ljrtmladIlaRWWYSbNOayflr0XhpVHZc2V-5gR0ilpBBE7KOlgGEgwqJyfL-gz6cS-wIT-v6QD-F62m9zApmLZMpSI_rJxCP3jn2J7r3fp9oHL1-PXGu1In4PodepgEcL8dKwYaCDAC1mwLl1ZvRcz2mpb3hXwUNYr4NVCRlH0RVMPEs1wZBn8_MmHVaZXL1gw0JEkJPaTg-6tGelFzBbdfPJrTyAYeN46Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e122cdcfbe.mp4?token=p4lGuVJQQpG47VYSvvCAwuN8lBN9qPbjsmEJcwpOnBaScQmSIjByVS6pFwo3yFwsMVaphnI-DhwtxHcMq1z66JuSXgnyMRAmUPWjK2XfKE0AB7OWHM9ljrtmladIlaRWWYSbNOayflr0XhpVHZc2V-5gR0ilpBBE7KOlgGEgwqJyfL-gz6cS-wIT-v6QD-F62m9zApmLZMpSI_rJxCP3jn2J7r3fp9oHL1-PXGu1In4PodepgEcL8dKwYaCDAC1mwLl1ZvRcz2mpb3hXwUNYr4NVCRlH0RVMPEs1wZBn8_MmHVaZXL1gw0JEkJPaTg-6tGelFzBbdfPJrTyAYeN46Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش یمن داره حوثی هارو با ماشین زیر میکنه و میندازه تو دریا:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84453" target="_blank">📅 19:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84452">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84452" target="_blank">📅 19:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84451">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaXpxFZ-5kPPj3JgTVbCLZ3XyGkRDDg7k-0jkxNvhg7CGKnEBdYJ8zFg4fs5bExtNe7Z9EU_8yZs2LMm13PmrjtZ4Va3U2Uy5o3UXGeu36dwB4S3Vmdi49Q2dBar2JSC4XFkwZRo7K7RIEIJt9_0_yNePm6LauppOZGc6Pfq1VFLAHHuCIwSoKxPOLTZwmjaSn3lmy-XsIAvflZl0GJ63ZytjWOPsWeDOWNVSaMFeUthacL0rRK8u4C8BTA_tYi2Ih4PpE8rJ5hWxHhghi4CBIsTmhcPLwOchMA9WBdJY7aRAJQwWq4lkaa-yP_8Ee949Dc8EkflRcxhLgSFP931Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G13
🅰
🛒
ورود به سایت
👇
✅
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84451" target="_blank">📅 19:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84450">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پسر خاورمیانه به روزی افتاده که تو نسخه بدون جنگش روزی ۸۰تا نقطه مورد اصابت موشک و پهپاد قرار میگیرن، وای به روزی که جنگ دوباره شروع شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84450" target="_blank">📅 18:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84449">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKUcQb_mMeB5Xi5GDNiIrH0JXO4U6_PkGoO3yBb0jJkk2aRFDkHo5nWrYa-EvDgwtzGEBFojBbZDtaGKbOigLQtttMQUwCX8YE8NJhLwTDw2mwZJsVSoOp7M4sMdJT50aW73n9ajWtzQ5WW6wn4xi_eb3ORXbVi2Kwlj_gd7366lXljv5IJuT0KzTexUC6ezGGzcFsM5uTrxW1qBmoTtjKR1w9CaRWbAb9IWaob12ctpTBjjRYqbkdb_H6_F_uRKzoDa9WubkgpzjWp8LtFFARIWS_VPcReypN4nW6ZR0kvZVpqutTmlpOquGIUHmm8QL-bZxMQC4jjEnnwY3y1Xiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منوچهر عاقل ترین فردیه که تو توییتر دیدم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84449" target="_blank">📅 18:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84448">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCr_XI69qBfFs6nhwpcqbmr6HQ-n1SVyQtiRIQyhszlvtU52i_4rn-qTE0Bv6XPnAh-dP4njL6yD7CMD3pJDx0bicxYGTG496NT9FMxrMCXhg4JSjlhUjmL7YNv7S5dpH7Lq4DgVplfBYlUuVlMOBqvPSV1nL3a-WYHqwvIuLSaVQWQfKHe8pYUfSUbsOdNdNYlRvRQs0Fh-I5SWIScnKN1uLp_yxGIxBSym1ZRSFjLlgdZIFB5vikA-IZ1KmFh_ZKA0YMWM8b0M3RR7tl4JHs8TkItSiL3iAK65M5pU3IRztIaF9cY-OMCvBfHAIkqiFr8Owo74FmLGdXFPCDo83g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این شاهکاره ولی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84448" target="_blank">📅 18:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84447">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آلبوم جدید امین تیجی به اسم «پله اضطراری» منتشر شد. Spotify  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84447" target="_blank">📅 17:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84446">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مغازه دارا واقعا بدبختن، با یه کیر دومتری تو کونشون دارن کار میکنن درحالی که ملت فک میکنن اون دومتر کیر برا خودشونه و میکنن تو مشتری
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84446" target="_blank">📅 17:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84445">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyZClVb-j40bZlMSMxYc4LtvRx7Yh36BB0H688Ud0_VyHYN_E-Q-WxI-Nb2ZS1YgCONHy3nK-OmpMz-3kkyg0MB201EnIDlZEg0UYohRDPS22j4NHKsGWF3sIeVz-N6VTTi6lXeyBE1_3RE81h5bgEvXBF861hJSYjz4RbsogUov7N42OGtzp3OvDphUx4skR54bV2ri3UVlKdaxTkHlM-I8Q9IqN5YtUd9lfB7wLNIlZRPO55T0L7OPsPVW5efouKgRAH2WECw1qFXxu-26lP-x5niIJ9r648frEWX9DSrunsybtKwZWKsAFaBOY_Kf9bsr4Chf6z2Vc12Qsv8cqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84445" target="_blank">📅 17:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84444">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmNaOc_sIlsB-tifodbvZL9UlMHgN6_0HDK_2EvgThmMHd-ohJPJ9jOuRCqrSqnVea0QcO4iEHKZG59n55diKtqQETIvUQsyh-juBks5BmQXPR403cS6t_kbb-GZVDFdFLCT9JdAv3WRMC0QgbSyQPbby9cULr16YCAJQ8CLsGj_KufSITO9A_z0a0htLq2jX4bpvC8O_dCQFbRhrOeGZ_o13u_AW8Ef1ZaD8BVgjQe8LeFBlnyucilPez6RuBhS6yHx2DfYL8p9xWvN7b80A-pxqYySCb9oG66T1diR7kBTEM6brGbvTqCFfgfcgOpbhzNLXR-3mhnBlHe0d48WHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چارت؟ کدوم چارت؟ چارت یوتیوب با آیپی زیمباوه یا تاپ۱۰ ساندکلاد با آیپی هلند؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84444" target="_blank">📅 17:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84443">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/269eed4b24.mp4?token=lnx8lMd670vsIgoilmdzt6ZNj8E_Y5OAMvKh7r-pQ7GjB-y3Pb5c0282tUWDOCVUzicjmPeMYYgrh9otjFYko_pS6p23ATNaBizzh9H4MT4CtL-Zq68hyFz2Zwt06x51g1e0lQrTrzXdjDKBaBehqgaMPop3enH-jEqt1jj2625twZ03UKj-HJUFJXW1rTnLEGw4dm9UXoV_YaNox2xsBfaQigS4W85zkzPaqYr1Kdvlibzz2XrgfFAM089OBGfQj0UfQdfQ3uJz10rVl9zJOazaqCQqy8ZpjCHInyNaIr5xOUgGwViuTCxGF_6cvMyJIrTAncwnmz4hcQkmGPVivg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/269eed4b24.mp4?token=lnx8lMd670vsIgoilmdzt6ZNj8E_Y5OAMvKh7r-pQ7GjB-y3Pb5c0282tUWDOCVUzicjmPeMYYgrh9otjFYko_pS6p23ATNaBizzh9H4MT4CtL-Zq68hyFz2Zwt06x51g1e0lQrTrzXdjDKBaBehqgaMPop3enH-jEqt1jj2625twZ03UKj-HJUFJXW1rTnLEGw4dm9UXoV_YaNox2xsBfaQigS4W85zkzPaqYr1Kdvlibzz2XrgfFAM089OBGfQj0UfQdfQ3uJz10rVl9zJOazaqCQqy8ZpjCHInyNaIr5xOUgGwViuTCxGF_6cvMyJIrTAncwnmz4hcQkmGPVivg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تورو خدا بسه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84443" target="_blank">📅 17:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84442">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کیفیت اصلی فیلم اسپایدرمن اومد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84442" target="_blank">📅 16:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84441">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJLf2nm7Xjdh6aBmOda0A4uyv2l9rEJQRq5YZ8jCpOl8Bir7NbBCP0k_BAtGHV_V7NPzZmRq7EOJRv00VE08F9iLppJw4NI_bd40a_wtrw36xvO98wDoR7FhOjsSg4i6n0W3d1N1QNY9ocyv2GJvvhXJ3WMuRdQorOScf-uwr6sq38CVv-N9Vqr62u5Rs-tYELC3YslS1Mux-bs1XtksaWxcnFsG7UFhP4KtzpROUavmP1qKyT2Zo4Nr5Jpx0PwZj6sl9r3XK_hRtkrG60Vlvb-7FiKyZ4xPoTjsgZTeDQ0vc8vyQAuplKXOGmqdHFB6PYdExJP9OaypsXsP6Kz_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاگان همچنان درگیر مهدیار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84441" target="_blank">📅 16:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84440">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijBv2kroTTfgvceaXzgluHmkIG1jcvWVRaULmzNtP71uv0RWga1G_zBgwwU3-rbQ9w8L0DOTABPvkQ32DeX72zyLjo2leM1A9N63oxSEu5O3FIdDEzLNml31z5ulWc0ciddqDHUTr2_kKc3tRRyMt4HVpMJjy6KcwgWdNuYxhogJ3YaLeGvQvJ_qNZMCIV67dZlfvvtR-4MffMkeC0KOy-FCa2-RwL0zJuu5A_A2KepOrq6SQl6IEpmm9LkXauOuy5_2cf75Ll1_tmKz79GoWS01DLJ3opqjlKmOxryXCQYRXSvq2CBSt5qDU3Xuhud3Cs3nWMtcJjv3MBCN5JenOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زود قضاوت کردیم
میلی پول ملتو تسویه کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84440" target="_blank">📅 15:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84438">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تیجی داداش هرچی نسخه کنسل شده دادی بیرون از نسخه اصلیش بهتره که
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84438" target="_blank">📅 15:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84437">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وکیل تتلو گفته که تتلو شاید امروز آزاد بشه.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84437" target="_blank">📅 15:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84436">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np-mCQiBGWV6_jr4XZl4hmucuUgrnHcqDCVrfbeGgUk0KrcDwj-hZP0xoaisic1PxHH4zt8bGWZQhpHpTp3nHHAoHer9yVQBKq_UnNKErhpWkYn_oKDc4wISz1sXqoYhKuCJDkHGKvkG0OIpfaGRCrV3E3hV5QeOJKJ8frhK-ye5KzYAURydj4Pmgdh-jGNr24GosXhodq4aM11BOEdVvfDJWtYQSdyizEW1x4Gvtn9E0uzgbV2pY17ifQMRzPHByDwOyUnD91Dvf0VCp15e1repLpLhugaU_zkl7mpkSmjHAsfGxlh5tzAjWI9GgguhbfRC9LAH1AMkhV24n_ZS6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ورشم؛ خبرنگار نزدیک به ترامپ :
آمریکا در حال آماده سازی حمله هسته ای به ایرانه.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84436" target="_blank">📅 14:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84435">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84435" target="_blank">📅 14:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84434">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMH_TmUS61gGDZq3XOqdMf18kY9Jxf-4o7mq8KjeiSZ07V7BmpGOYj2-R_bM0HC-E8rapLu1FB1uOoPj1QwCsECEzbVXBuBWMYeKlfcQYkHovTnczX4OztJqKmOxcArE9Bmfc_bOlPS33rhEQjpPC9zyYqAAuXxU6AzasZrBmWYWY9A-ygWMugxj7ILC0Abg8jmAzvBV_x2MqonauEkwmKykAmJ9VbOtlPhH5mTYoqiERG-nU7B0HsnWYH3BzrS9AQrWi_V9x-WTMtcH6GbYCWwwTI1dqfbgI3zo3dt5mEo71VdKRsZWxuVgZqox5g-zqUatR78QUFAXKDu82HhEGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
فرانسه - بلژیک
⏰
ساعت ۲۲:۱۵
🌎
📲
رومانی - سوئد
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R13
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84434" target="_blank">📅 14:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84433">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آلبوم جدید امین تیجی به اسم «پله اضطراری» منتشر شد. Spotify  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84433" target="_blank">📅 14:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84432">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3008a810e4.mp4?token=aYt9C273SJ_-4rgrIYbI2_rmE6oSr9UZ7K3voi8lIt2U5HWZgGFJj-SffuK2q-fHMNiIYrM22U_jvJ5Bxk5URamyNUOE-MltBh9B6FOHAYDu6rPWAdd3sDjuTwx0FQQvPQyqA6N4NRJdupNW_aIlkcBUl7SrGt_K_ifWe4vcYWs295p5bVY98CnOE0JMAdHBaqOTFbPZDPBqh95ztvu0nl0XeYInKfoSad7Hgh8LYvKM7GHQSQzhay0Yf8BD0XeIukVVaZ97M_rwSkJOAFsW7tfSns7xAEgeXxJQsdQbM5DVOBKVA8bM6RG4P-pPDlancmmuouWqTVdSZEX1UtZliw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3008a810e4.mp4?token=aYt9C273SJ_-4rgrIYbI2_rmE6oSr9UZ7K3voi8lIt2U5HWZgGFJj-SffuK2q-fHMNiIYrM22U_jvJ5Bxk5URamyNUOE-MltBh9B6FOHAYDu6rPWAdd3sDjuTwx0FQQvPQyqA6N4NRJdupNW_aIlkcBUl7SrGt_K_ifWe4vcYWs295p5bVY98CnOE0JMAdHBaqOTFbPZDPBqh95ztvu0nl0XeYInKfoSad7Hgh8LYvKM7GHQSQzhay0Yf8BD0XeIukVVaZ97M_rwSkJOAFsW7tfSns7xAEgeXxJQsdQbM5DVOBKVA8bM6RG4P-pPDlancmmuouWqTVdSZEX1UtZliw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این‌سری دیگه ماسک نمیزنم یه ویروس ناشناخته از آزمایشگاه طاعونِ روسیه پخش شده، چند صد نفر قرنطینه شدن و چند بیمارستان هم بسته شده هاگوپیان: طاعونی که تو روسیه پخش شده، حدود ۱۰۰ برابر کشنده‌تر از کروناس  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84432" target="_blank">📅 14:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84431">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این‌سری دیگه ماسک نمیزنم
یه ویروس ناشناخته از آزمایشگاه طاعونِ روسیه پخش شده، چند صد نفر قرنطینه شدن و چند بیمارستان هم بسته شده
هاگوپیان: طاعونی که تو روسیه پخش شده، حدود ۱۰۰ برابر کشنده‌تر از کروناس
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84431" target="_blank">📅 14:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84430">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آلبوم جدید امین تیجی به اسم «پله اضطراری» منتشر شد. Spotify  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84430" target="_blank">📅 14:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84429">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j17VR8Rrc1Bn347qgPUKf_gLqJJtX29bGOZVtR40P2aXbrU8r65qmj7zO8oRgRjeLzzTmz3qgDtEuyTAULXZU79SeZitFwq1c1CVLA3KQOTYDiMcbhowR4lq8JDXmWhN-j_86y0L70GEY8rBqIHIJUqR6v78chXXPAIIIAt-8LDQQOSBZ3bM3xyVJZ8s33mcOxVUfjeNPpEuXOGLsHSXr2QxdTGcfYx1hCg9OpLygSrmL8LLTrhOkGswqfGX74ZMdzgenCx4qVw_AHbRHK2diUqgVMq2ad1exs5-Gg_2mKXpmmdGQWTD0HCMPx7Tu9wPaZj9RNpEjR4IjClAQ0OGkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید امین تیجی به اسم «پله اضطراری» منتشر شد.
Spotify
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84429" target="_blank">📅 13:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84427">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BKcJ7VXUue8P4kpPC5ODiRwlF3JtrZOse2dow_Y-PrlrljmnqIR3Wl9iZtXWllijhhn660VxXI0qst3YIOFKetvJ32NNsea-mLq4LtfLIXTmBDCFmQWD4wR7wme-LIrrDYlI-3QTxzqVjbjX20Vv2Vo1UAijsShIJwOqO71S4nF_3FFssW7beQg6HCwxkQdAWMoXgsJGqV2wTOVhTggw7QlzMc5RESMCGJ_VCjXV22nzcRzgCk2EcJxeOW_Jvu3lHrTm-zXS00Qt4czT4K6_EkujmIqm2u82tsuhlaxIbdEV2ecAt21yNs_G6th_tJ2r0yxQKWE2sIY7QU6xlsWnuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Fd9g8_Ex5BptodtVVTrQ-wbrxZB-E7_s0kTzurNBYQ63MvkvdOO1cjf2F0Svx_0iytQhJTvNLObqBd1MV4hXhRAGuJ83x0UWIA9qMOW1Yhag7TySFoEDiU2LdU_fax9nkpLVDojiWwFTETItC4q8zI7UUgonc24dDKA3xIG-kqG-QpNQtIXnyowFOPhJhV_1VGoONUuRoD11aXcnVtnbf0hJ-kusjoOLM03EukiDwup5kOusGyRmW71WgpZlt8Evc6IA_S0WsJwSUAibKudDXpBQGoBoYB2-hAA4sVLUQVIA-QMgHY6SzCQ1E31KY14JaHNoHyxZQBDi-vi2Bj2IlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صرافی ایرانی omp finix که امتیاز رسمی و تایید شده ای داره، پول مردم رو بالا کشیده و ۳ ماهه درخواست تسویه حساب مردم رو پرداخت نکرده و مردم رفتن جلو قوه قضائیه دست به اعتراض زدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84427" target="_blank">📅 12:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84426">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">علیرضا رئیسی ۲۱ ساله و علیرضا سپاهی، امروز همزمان با اذان صبح اعدام شدند.
قبلا علیرضا سپاهی بخاطر از حال رفتن موقع اجرای حکم اعدامش راهی بیمارستان شد که متاسفانه خوب میشه و حکمش مجدد اجرا میشه.
علیرضا سپاهی با دختری که دوسش داشته شب قبل اجرای حکم باهاش ازدواج میکنه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84426" target="_blank">📅 11:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84425">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MclghU6g8atZnJHWRAqzuJmmv779NuqM1huTyKllxAikDtAk93KzMuXnGJyBQkSyC1LMUFRuHWK2OfEKw6YZRWiWv6_nAglEIvXcYK1Q02twm6RU0QbdvD4XVSOrqt-95jVog1HBJ_WzZAby8pqF2LEuWakYwlRtNX_yYARqkeIsBduN4CoEN8tJxPygWdy1sXomPP5m8fR77qZH9GKJ6gpJl906eikH_ljqc0YMrF9c4AqPpJzG4V9kul53nSbXfmZfW8bGig-Cbo2wczYxDO14A-u0oUvRUyN4RfmmVE4-MYCECJX7GjgDFAtXPrIhQUS9uRiFQq1bM2up728h_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/84425" target="_blank">📅 03:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84424">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فدوی: قیمت گازوئیل تو اروپا 2 یورو شده که یعنی 700هزار تومن
ما اینجا 10 هزار تومن پول بنزین میدیم که حتی یک دلار هم نمیشه و اصلا متوجه نمیشیم گازوئیل لیتری 2 یورویی یعنی چی
حتی با اینکه قیمت ما سه نرخی هست بازم کمتره به یه دلار هم نمیرسه
این شرایط قیمت ها بخاطر ابهت نیرو های نظامی جمهوری اسلامیه که بوجود اومده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84424" target="_blank">📅 00:38 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
