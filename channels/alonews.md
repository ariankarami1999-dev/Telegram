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
<img src="https://cdn4.telesco.pe/file/SAD2gRopAA04krslXDmRC2q2P7Njjv-B7xhn9_Gt6r8BhppH_VbnYRRMURnUWrxBzHbOlUE9Z6IX_N4VHIF8BP-ZsOh5njNZ3FlsBsjghsswC3RI_WUO4KkVYarF7-MGjx_flhitWnbeDx6993UlNojhYgh5AohVmw4EJxKlo8T8pgn2_8N2npGnIbLUhJ09IhK7vjertztabP1W7_bfYnAhl2_HoZeY2Qt7qf_Ro8hwjbQsKcmYcPn6f03dlKMn6l2EXP_3LyfbScqEWhjTtgb9csW8q3uN9JL7eB4WdwKRdmkPk7L8lU6gR9VgKf_KS9czwOEDyZHRxhnblaMHvA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 929K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 18:01:45</div>
<hr>

<div class="tg-post" id="msg-130913">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB4sF7yFDP4O6H308mei4v9iQMJiCgTYrftcU7J6MykiVP7HnKee-9xWYXYrHTVceYRIpivBWXjObdiTraGzdGU_S0zMqz2a9-QD_KQ_SEntctUqm5mYmtYBdcbV2bowjS0LUQLP3gN3B0sXZ9CvT1i7HjZ_LaO940lOatP9lChzxNK7uzvp74_-v0Up8uBcw0GAjEXzjHgpzwxYVNxLmjKC3rgRSaddF7d4zArp-0FpdDJZH_NCQ0Y4GI7ob7KGENGQqc5OwZQxj63ntyRn7TiJaEoT0gPK9M0JvW6i3_jR2n0te1GrdQDmDJdZtBuchTXb1s2gS6VKofQ7H1zEJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار فرمانده سنتکام با رئیس‌جمهور لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/alonews/130913" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130912">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e26cc6d01b.mp4?token=fHlI_iGKBY6JkGHqtWFbWD4HLmAZH1QH8G-JP7g6m6zGC_658Ko0rhGWW3iVD1fYb0s0nhye8aNWjYTQ389GGuYpypLgzIBBFh39yIkrYR_SxNEay1KnGvK4HhcQLv3oZ7ZPZj7n9Mlm2ZRjxS2xhlEWK-WhO-8R-mo2V2QRiXCQq6SVZPslUlC2fTHfb_FN4JsDEtjfBeIPgQzLjclq-OHEtdSLIxVxqODyRUOO514We_y1TCXdlKuQaCBwv1NJVfHzxIyQ6l_yCPeD239JLxm8PZ_VVB8kc3DCo8FfjqpGKjeSNCPW6kGqlOkNsqeN-twdISKdBarjG2nSc5eYCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e26cc6d01b.mp4?token=fHlI_iGKBY6JkGHqtWFbWD4HLmAZH1QH8G-JP7g6m6zGC_658Ko0rhGWW3iVD1fYb0s0nhye8aNWjYTQ389GGuYpypLgzIBBFh39yIkrYR_SxNEay1KnGvK4HhcQLv3oZ7ZPZj7n9Mlm2ZRjxS2xhlEWK-WhO-8R-mo2V2QRiXCQq6SVZPslUlC2fTHfb_FN4JsDEtjfBeIPgQzLjclq-OHEtdSLIxVxqODyRUOO514We_y1TCXdlKuQaCBwv1NJVfHzxIyQ6l_yCPeD239JLxm8PZ_VVB8kc3DCo8FfjqpGKjeSNCPW6kGqlOkNsqeN-twdISKdBarjG2nSc5eYCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله خوارج با شعار مرگ بر سازشگر به عراقچی در کربلا
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/alonews/130912" target="_blank">📅 17:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130911">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
دولت عراق تا پایان شهریور به مقاومت عراق مهلت داده است تا سلاح خود را تحویل دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/130911" target="_blank">📅 17:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130910">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
غریب‌آبادی، ادعای ترامپ درباره جلسات فنی برنامه‌ریزی‌شده آمریکا در این هفته را رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/130910" target="_blank">📅 17:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130906">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXmd4adKIJh9QGCmjQkwug3GA6AFjNGggOdic-wHmLoVbPAC8XR_LubdmYONbdA7aYc7KAkwWbDVgjiv6CrlGZD2xtKMN0uuyZ3O4z_y3Q_4t9B4PJLTIFf2kGsB5hCm2TtkJUelxBm45Ebrw_17jSBtKm_O68YEo4Vm_I9S1Q55PJc7Q0IJLjeev79i9cjIa4Ax4OxcKA2zmVS9fTeHjZbg8vWEIl0BqlTOSSGUEy0hno46puRu_cVCosg6ntjM-W0CMwjx2Jp5edFlYSBGZ4tMGdwHUrmb0NZaVadRqJTjXzd1W--FNt8rvc9bWT6MDGGAXL6qmFi_WT5D33pnCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39e76a3148.mp4?token=U3YBVPlHfPchfJecVSxa1c-iXTDWZoR7IV53YZ-yRqEKkisund8mzWG1oyzuqqp3-E_Sl0_JUI3ubUeG4XzFdPMbRTz0U1loNce1j0DNSf8FC6yaurH8i7aIFOBpmWiWDtShq3H75I18MwoE-PZfHGwO_PQeBIyIzp2k2FnXfCi0T201EWq3ce31YcVc3YwUYCFkoyDtf8q3Y4viz3izaw4ARBk4_QWf9U-OhpGQ2_GMqlHd5nCpK1kNHuxTnPgW_Nl6950InrCFamPYHyBrfjxgGMhkmthBxmbONV0Wra36jBtq3_sPojHbBUSvbmdor_Ow00nadu-IGSuYvmLlig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39e76a3148.mp4?token=U3YBVPlHfPchfJecVSxa1c-iXTDWZoR7IV53YZ-yRqEKkisund8mzWG1oyzuqqp3-E_Sl0_JUI3ubUeG4XzFdPMbRTz0U1loNce1j0DNSf8FC6yaurH8i7aIFOBpmWiWDtShq3H75I18MwoE-PZfHGwO_PQeBIyIzp2k2FnXfCi0T201EWq3ce31YcVc3YwUYCFkoyDtf8q3Y4viz3izaw4ARBk4_QWf9U-OhpGQ2_GMqlHd5nCpK1kNHuxTnPgW_Nl6950InrCFamPYHyBrfjxgGMhkmthBxmbONV0Wra36jBtq3_sPojHbBUSvbmdor_Ow00nadu-IGSuYvmLlig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پس از ورود دکتر عراقچی به خاک عراق، از دیروز تاحالا تو این کشور داره کودتا میشه
🔴
بنا به دستور الزیدی، نخست‌وزیر عراق، عملیاتی برای بازداشت تعدادی از مقام‌ها و چهره‌های سیاسی این کشور که متهم به فساد بودن صادر شده.
این عملیات با کمک نیروهای ویژه عراق و سرویس مبارزه با تروریسم (CTS)، خودروهای زرهی، تانک، سلاح‌های سبک و سنگین انجام شده.
تا الان 47 نفر تو این عملیات دستگیر شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/130906" target="_blank">📅 17:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130905">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPSnGfEFXRHBkoBe9IIWg8VH7NgqLsE9AY932GdlmJEps_bWOr7gcL3zGhg-ZKQU3N8bvrQoylseLHB5lMdi31YcNHtzOiU2SrcelFMPXY6T_wwFx0UEtLP0j9d502Dn5YmqvXLJmrmJtTbWkq5DDTcuav5Xq61DMlLe74GYh6XFXfXT2JZxJfgtHRWxoikaqtK9-CfVJs2g0NxyX4nYKSdHiEeCeFkXc0elozWhYQ0qTe50G7JU5MpAuHLYXs31c0dw8b7Dt4fRdvwDv0deXp0U5OWz6OK-0wSxzORtYa_FEt4nQntKUO5kdrcMNBG-aNUEMlk5BwTzxvTFlQ2daw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده سنتکام، دریادار براد کوپر، برای دیدار با فرمانده ارتش لبنان، رودولف هیکل، به بیروت رسید — هدف اعلام‌شده، نظارت بر آغاز اجرای فاز آزمایشی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/130905" target="_blank">📅 17:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130904">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
کاخ سفید: کوشنر و ویتکاف به دوحه می‌روند
🔴
سخنگوی کاخ سفید اعلام کرد که فرستادگان آمریکا به منطقه و مذاکره کنندگان آمریکایی، قرار است برای رایزنی با مقامات ایرانی راهی دوحه شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/130904" target="_blank">📅 17:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130903">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری / ترامپ: ایران درخواست جلسه داده است. این جلسه فردا در دوحه برگزار خواهد شد!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/130903" target="_blank">📅 17:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130902">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سپاه : انهدام مهمات عمل‌نکردهٔ دشمن در بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/130902" target="_blank">📅 17:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130900">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nyakWpzqya0NsYhDj9n8QpS0Dm4Oa-g2pNX-Iqc9-snliP7gXGIA_WczWBIRyNZVQzrg7BnVWDyu5AjKjkBQ7mZOP8FCCGcCjrAmfu81ZscW0Grl1zo393K71C_ewKEx2aOq30aIruVd1DNM38Qlulo-hjXwOu0iRbsRACbucArW8zqIM-IY4yQhMQs5rGsfVwtxgzvN4NcGM7C801NYFeMSo8b1urcvndZoXdsfRf6esgv5daa0UudTka30l-d8xhvSmDhzsq_htfWplcLjLxUbDBYp_JZLDw2LdPg9T2Z7yCaUc8DCp5iiLvljY1A4XsmXKOYS00e1JsHUmwcRCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bOg2bAugkvNkdKe4RS-aZ_q_UGWd47rHqRw7xqzRZnFSPt9JopTV43tFVEOftcDjtcfdGeJ7I_6ai8dGetpxHfYYKMixCAJyCgb3jkZwkv1444TgBhDuryTRpLj2Z_sOhNmeiDEGGugutoy9PKApv3K80OWNsyDURck4zVs9mhcqgNJqmNZQRdBQB8ar7ghUgb98UnRD32IYx83dtXFPM_hPsEaF8CaUmEtxHLeXrnbtHpdp6lLSCaSgJuYD-pEHLxmBGHMmeVQo7_G_W_cKkj_PvoxukhzIKTJoSgYSEEG6Bg1kkRiYJWP4ZT2mUK2W_ofVANeDyGkYfTcN6aWnRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
رئیس‌جمهور سوریه، احمد الشعارا، با وزیر امور خارجه عراق، فؤاد حسین، در دمشق دیدار کرد تا درباره روابط دوجانبه و راه‌های گسترش همکاری در چندین بخش کلیدی گفتگو کنند.
🔴
دو طرف همچنین تحولات منطقه‌ای و بین‌المللی را بررسی کردند و بر ضرورت هماهنگی نزدیک‌تر در مواجهه با چالش‌های مشترک تأکید کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/130900" target="_blank">📅 16:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130899">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
هشدار نیروی دریایی سپاه به شناورها: تنها مسیر عبور از تنگه هرمز، جنوب جزیره لارک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/130899" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130898">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwjQyd1873wd88BTxHfQ9Yy3XMR5dQIcS2HAUB3HrzUDWjK3_np3EfbYwraNQrhNQ-trBiDbv0oOII_lCfO1YBpKDzQfw_pJ4mhd9yo9l4AwMlTil6dH9GItcHZLIMbTFWNS8K2EpbFKQSxbIcH8p-3rlMGf-1rsLzsKz3tdXpedX9U2V-R0u-tqPYN8fBYAtODKjUqXyHMJcQs6j0cjcySNqthfEVAG7fSwP92A0oE4AQJf6fkGAVvBo9NGrInWO2qkj-A-N5bmWYM-HdGkurAbHrVx07jTl2PMHtaSMQTCJ6_u7JyJjpSllvja1m0HWTfz-H-yssPT-iPuhqD0UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: کودتا در راه است؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/130898" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130897">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0oWYsq6N_Y1QC2VgRE_5ayklCTakl_ysHZtOhyNMIVPXAXdOoRWUJSbyM4zl3CjC1UQI6dZhUF-yj89WVziUwe3wwlnuVXIxh1jzH7Dg9OlhPArLld0t05J6Gy5qief2tE30fWjfSR0vYxdGZcQKTo3bBr4ss5ELv27i03k9rDA9rqMKQj83BFvM8EVO0C_qtnK5vw92Xf08t8h2RdestRbK5Idpzdsq8_wZ4c9XLFmLFUkuQAbYJtl9h35NkdKcVuvgPRnXavsTUYeNN4cmzgiEzODR8VyPxLaTNSkpdNHvchxow4XlopdVGGTAMDAZXRUHK2Ep_lVN22F5yd49g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یکی از کارشناسان صداسیما : تورم تو امریکا داره بیداد میکنه و کمر مردم رو شکونده، مسئولاشون بی عرضه ان
تورم امریکا تو 1 سال : 4.2%
تورم ایران تو خرداد ماه : 89%
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/130897" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130896">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزیر کشاورزی آمریکا: محصولات ما آماده ارسال به ایران هستند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/130896" target="_blank">📅 16:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130895">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
دلارهای کشف شده از منزل حسین منیسِ!
🔴
ذات سیاست مدارهای اسلامی شیعه انگار دزدیه
🤔
به عکس های دیوار توجه کنید، برا اینه کشورهای منطقه دارن جون میدن تا جمهوری اسلامی سقوط نکنه. ولی میکنه.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/130895" target="_blank">📅 16:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130894">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل و شین بت اعلام کردند که اسماعیل مصری، رئیس امنیت نظامی حماس در گردان رفح، در حمله‌ای اسرائیلی در نوار غزه در روز سه‌شنبه کشته شده است.
🔴
طبق اعلام ارتش اسرائیل، مصری یک شخصیت ارشد در گردان رفح بود که مسئول هماهنگی فعالیت‌های امنیتی و ضدجاسوسی این واحد، تلاش برای بازسازی توانمندی‌های امنیت نظامی حماس و پیشبرد تلاش‌ها برای «آسیب رساندن به آزادی عمل نیروهای دفاعی اسرائیل» در غزه بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/130894" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130892">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUmFJS8ynDAZQ-7DBMsbgMj_wgzkKXlvZ6M_nJgSo0-XCUNvhm4PWbxRf4a3hdCgr8RsFfCPfiR80mGL-rjSqA4DPobgomyUo7AFZ5mg2Y5gXbIy1yFMQ_PuDNEJ_okRgri2ZArkzbMOSACTBsEtpkbG1aF-cCen5kamiL1FBmU5UtARfe_kptg14UxrW32RomN8tfW1wh4HSbK9BwftSlzQ1NVipXQe2sd60itU2Ic_HjRbEYJkYcUGo9La9s0jDpeX4RYmKafZlae0xwpaJKCaF6R96YLm6vB79cZ9XyFxIvsTH2AphJ0zC8ye3KWh52vFzj_ZeADpg4HGZHW-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BArh2YFJWA6ifEAReQO4fYpyV29wgYZ4R5w3BW_fOPFctLg8Rc87xyRRGmIXvThlQCnnXo_5I-O7895NPWrWSzVP97jUDV2ezLlx2BsdBh5OAen63kEQbOdwkZ_5aIGm9BcOonwsaKt3aCkLpYakF4IeY8Su41Gfsy8UcgVBAfAtwzyLbRa5vT8GQIybAqu1i2t2kpP82C9dUw-zxX4XLpyelyUEnt8kGpm2m1aBxiVIU1S65iQ5DA4K91kmYLujZG_yODY7cAynPgaw27D5PDws60F_-vCwy3Qv69r1s1-RU6nW3FDiX9KY4oifdnaLN05fgvrArBeumsCPEUhRlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک تانکر ال‌ان‌جی روسی مجهز به توپ‌های دوربرد نصب‌شده برای محافظت در برابر پهپادها و تلاش‌های احتمالی برای سوار شدن شده است، گزارش تایمز.
🔴
تصاویر مارشال واسیلوسکی، یک کشتی کلیدی تامین ال‌ان‌جی به کالینینگراد، دو سلاح ثابت نصب‌شده روی پل را نشان می‌دهد که برد تخمینی آن حدود ۱ کیلومتر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/130892" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130890">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W1Qe7PpOIRMnI6qcxjzVEWYHuITuannfvSCKwUHdvYePm-iyGs6HoxWqBFqIT4oNV1SmxY0nTa40Wvsg27wH2pDWu-dkYqQsSKRN7Pad_85L-vj2Op1mYF_fjUF1HOwzEl844JHiIFhZqQ16wvDSBnIzb8JhH-4N7weSs3W0tkQrPlFprhzzXBakd5OqTovbIw5kat1FjmnQ7zQZyVZn9G0Kc2TX3HhTuhNQnfxp2KEO70PVBHTdV7JHPHb4RXD8OMoSW8xx52RuFwCSSKr3fVpnNvmHj3lZ047zX7iMc-hS_lPvJOiLKtg4BChF3EplNHzbqs7REwya74rPXzglGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/roXAD0redwXETZjz7deglHn5MMeQDeAUD8mXyZSGGgm5AVjLdE2wQosUMwEfaINkNtBRScAgrpxtqSPkn1WCBeL1m8CvvFtyXM3YmPweKpzHw16IMQ1N0Ov0yzAOlcPvXZaWVUcPl8wPIBO3_hszfLB7wE02DHhBz_pWsL2bat-jMyGAEvSaYwwjob1AWq1Rv0UuvTK3-z8AQG6aa38KY_JHMNhG-lcxemeEMAf54uZbGwNH0M7t8wLXiVygwMDrijol-KSD0fqbBU794M6CEFNbnOmmA2--1v8lchmQw2sD5tNd0gv3ZK9L9fwwgreVwswiPV2ZKOMDRa2eV25IfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله هوایی آمریکا به یک ریل پرتاب موشک S-200 (SA-5) ایرانی به همراه موشک متصل به آن
🔴
سامانه S-200 یک سیستم دفاع هوایی ساخت روسیه است که در دهه 1990 به ایران تحویل داده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/130890" target="_blank">📅 16:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130889">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزارت خارجه عمان: کمیتهٔ مشترک عمانی–ایرانی در مسقط، نخستین نشست خود را دربارهٔ تنگهٔ هرمز برگزار کرد
🔴
دو طرف دربارهٔ راه‌های تقویت هماهنگی در زمینهٔ مسائل مرتبط با تنگهٔ هرمز و همچنین تأکید بر پایبندی خود به حقوق بین‌الملل گفت‌وگو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/130889" target="_blank">📅 16:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130888">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyMxmpwfIDXxgf7qgOiKb4TpzPnaPhAfxro9KqcEtHmuo8wpJELff9LNYoXdaqHpErZ_kZpm67lDaZsM6ia5xzBpWQKk5vjBd9q1gISBmzp3kSZqNXrcFo1F6JOK7K4X5COzbqU0Oa6BwiMLqKusqH-BhwRVR9iV4729Cg35xyECR2-tfBWeHO39arrIBjSoZtTNxZ3EYbje6aXGxN4l5pap0V58VmpQFomWQp8NMmSrrHM9fI_VXfx1dVymDy3BWtFk3VT0ZD5hWq1C1VSnIRUKvZKDfcOJDai-xjU2BWdCLtEwq1I6a7DJrOY_DdopUoBEr3l11fF8muNLxpZCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای اینکه خودمون بریم تحویل بگیریم باید پول بدیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/130888" target="_blank">📅 16:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130886">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnXNbJegqcvhoCbRWQFmCHWInHiRSWG1AEykR20Ilp9w7QIac-XAzRwn0lk5JNcp3QeJtu9usJHOoXNc_VKAgQ-zUq1NolOXHWNqwtL0cacT1WI3rinxXBrWNRNekdHOPME7Nnuybl8-DFhLuzD77IctxzwR5hduSEJlykU_W0HKoqqd4sBE2hQzU63A5jze0hqWTQO38bor_bhDBrt4SnEMaIlmvzf4RfgRO0nRYnMwm7HCWFweGDoMoTJRTXQvwT6LDwIfJHBXkhTqQlzRSxOe02rwH9_aD08RBp_bh_oByT_vgq1VpLLP3VScSH8WX7odZoQHH-_uujyGXZtyeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E7eHwmNw4O3ReuTTvOBdCgh-9DO3GofTMFsyTWmqcNWCYz6BB28CUAhsHuPBz4G8hbbqLLFU_nvrYkLG4zc4csJfu53sDdQFINlSGU17gVMv2nHidwt_D3YvoNb6g-e6SbMIRqlgido-Fm7l2bggz16Crn7VXxB2QAoEeLolxb3Iia4vXhfGgs5lmRWXQ5q28FsIM42T0ocmXt3poxY3jTGnT8DenrXMNiX9bRFRjQBVkXuYiU65hXSJ-vBOPkXLRTa2s7kk76Y9ksYVz0-o3uXt562XWNZZ1pZ0kjZWpn2VCEw640lPQxjDPU0uxw1azDnvS5McFMJFLIhEV97HrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
دلارهای کشف شده از منزل حسین منیسِ!
🔴
ذات سیاست مدارهای اسلامی شیعه انگار دزدیه
🤔
به عکس های دیوار توجه کنید، برا اینه کشورهای منطقه دارن جون میدن تا جمهوری اسلامی سقوط نکنه. ولی میکنه.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/130886" target="_blank">📅 16:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130885">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
لاپید، نخست وزیر سابق اسرائیل :  نتانیاهو دیگه تو اسرائیل نمی‌تونه دولت تشکیل بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/130885" target="_blank">📅 16:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130884">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
دقایقی پیش فرمانده سنتکام وارد لبنان، بیروت شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/130884" target="_blank">📅 16:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130883">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135ed4036e.mp4?token=VgVOZz7EieqwWEeGQWBoxVc_D1R8_LSC-Dum_McTTW33l7Lwx1MEFIiMTjsm3_wwPdrGuEdKjhEFK84Tf3_hZcunxImh8Hp8McrCVJQA7HA6mskRAyHydmWm9hVQ4shbknYSknTegCSdAXyDK3y-PFZE651ZmKT8PGTpH7X0uUq6SESZoeqkQYxHiUM4Tlh-_PRevv7egcTgz-feosH-iLSMoD4Atq7slfTBUEWR7r6CNQ5f-ZVB5zJXKZkeu5ToZQWWKLuUeQCSa0m883h6ath-jmLiQ3QkgH9YJ3NhYtM7ye5p7qJ_ffeC9iY1u_9hfgQnp_30CpXL-7ae2avdxlZYYOg0RSE6u5mo5TEAvfOEqNv4tO-wNp5hw0ceuH1CFVGvmZaQ42JFPGGYCkKw6pMvCMoGNtfxiw0aPx_6BxgL7M8PcLV5M-Xmlbq7WH5q--QszdRUg-3Vj9SJH2G0_KqgnpVS-qFaSZRM608jyIiwx748UO6Wu8umIpN4t55oxPLsBZA4foDaQcn3OgSney9_naNFYzn2Npn-mp5Akapme1RiJ-bfNIdLypVhNsnc-Kdm4jYYEdzcv8Yqtj7Op6AbMdSxqfFuWj1nAqWqyby2W9bjrN3UOd7L6LdAeBJrGbLFCv8W9WPZfEzx7qE5xTvluncWnPzBBDNjH6MRSKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135ed4036e.mp4?token=VgVOZz7EieqwWEeGQWBoxVc_D1R8_LSC-Dum_McTTW33l7Lwx1MEFIiMTjsm3_wwPdrGuEdKjhEFK84Tf3_hZcunxImh8Hp8McrCVJQA7HA6mskRAyHydmWm9hVQ4shbknYSknTegCSdAXyDK3y-PFZE651ZmKT8PGTpH7X0uUq6SESZoeqkQYxHiUM4Tlh-_PRevv7egcTgz-feosH-iLSMoD4Atq7slfTBUEWR7r6CNQ5f-ZVB5zJXKZkeu5ToZQWWKLuUeQCSa0m883h6ath-jmLiQ3QkgH9YJ3NhYtM7ye5p7qJ_ffeC9iY1u_9hfgQnp_30CpXL-7ae2avdxlZYYOg0RSE6u5mo5TEAvfOEqNv4tO-wNp5hw0ceuH1CFVGvmZaQ42JFPGGYCkKw6pMvCMoGNtfxiw0aPx_6BxgL7M8PcLV5M-Xmlbq7WH5q--QszdRUg-3Vj9SJH2G0_KqgnpVS-qFaSZRM608jyIiwx748UO6Wu8umIpN4t55oxPLsBZA4foDaQcn3OgSney9_naNFYzn2Npn-mp5Akapme1RiJ-bfNIdLypVhNsnc-Kdm4jYYEdzcv8Yqtj7Op6AbMdSxqfFuWj1nAqWqyby2W9bjrN3UOd7L6LdAeBJrGbLFCv8W9WPZfEzx7qE5xTvluncWnPzBBDNjH6MRSKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاخ سفید: بسیاری از آمریکایی‌ها نگران هستند که حزب دموکرات تا چه حد به سمت چپ می‌رود.
🔴
شما این نامزدها را می‌بینید—این حزب دموکرت پدربزرگ شما نیست. این‌ها کمونیست هستند. رئیس‌جمهور حق دارد آن‌ها را این‌گونه بنامد.
🔴
آن‌ها می‌خواهند پلیس را منحل کنند و می‌خواهند مالکیت خصوصی را منحل کنند.
🔴
این‌ها ایده‌های مارکسیستی رادیکالی هستند که در تاریخ جهان هرگز کارساز نبوده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130883" target="_blank">📅 16:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130882">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
منبع ارشد ایرانی گفت که دوحه و تهران در مراحل پایانی توافق بر سر جزئیات فنی برای آزادسازی اولین 6 میلیارد دلار از دارایی‌های مسدودشده هستند که به گفته وی در دو مرحله پرداخت خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130882" target="_blank">📅 16:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130881">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikg-wNq-yPcz2PFcXxhQJMrCbaYCo31OT3HNPW9rUu-WsRL6bbOXfwMIyvA5aCWwMW6jS75QmShZHp2d773sVbuGkn3qQsXCV_r4jn2xBdOo5yeqSlqyKN6Cdi27v2TZKS5Oeh_4Q21dyZXoolCi_bXsCJKt67rTkAqctAbJlViyuqEG90LjZJ4r3X9BmuHXyC_iPgmK0XboTwKH1MBTkaBNEopL-BTmdTISp1dNEuF8rUppvsXiZ6EiNGmi5Y9XU5yDVy9LkymfIxh44F2uh4j7ZUK5DlcWIAQHlWCKMmu0eFTD6t3LeKsy7AS2YNAYPPdIX0PvY5BoGSXyWmcpZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسن ازغدی: ایران باید با کوبا و کلمبیا که آمریکا آنها را تهدید کرده ائتلاف ایجاد کند و علیه ناوهای آمریکا عملیات کند مثلاً با قایق‌های کوچک آنجا عملیات انتحاری کنند یا در آبهای اطراف آنها مین پخش کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130881" target="_blank">📅 16:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130880">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
فاکس نیوز به نقل از کاخ سفید: گفت‌وگوهای فنی با ایران در حاشیهٔ گفت‌وگوهای سطح‌بالا برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/130880" target="_blank">📅 16:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130879">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
عراقچی عراق را ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/130879" target="_blank">📅 16:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130878">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
رویترز: توافق بر سر آزادسازی ۶میلیارد دلار از دارایی ایران در مراحل پایانی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130878" target="_blank">📅 15:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130877">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8f6c51391.mp4?token=ltYh4wMqW6oyR3XlCGpIMYGuwuvwQ3cs7ndpTdNZOq7SX_MTd8ZOnGESUaJsgFK4ADzDyjgbWDd9d1PdY_-d_R0ElXxUvLnOdbM4wbAPZ6T_b8ynAuL5LMvvL1uiSjHo9UA5KotxKcHLjc-CqBl-M2jN8OFdCAwEOt8AJzN8oCZmn4ylBO4Wv94NqBbB-LH0Pe-7uN9OfPP8h5LnKal6na4H5gFIDSGJ3GdUS0DTRRhvUIC_-QgOCcOWY-Yhpu3t_W3_3vHWylT1TZZW3safs3fCyVK9uVYkX6A5atafLc_NsmhgT6nrH4w6fWwPq6txNFArdGoRHnNEuerhYGGjDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8f6c51391.mp4?token=ltYh4wMqW6oyR3XlCGpIMYGuwuvwQ3cs7ndpTdNZOq7SX_MTd8ZOnGESUaJsgFK4ADzDyjgbWDd9d1PdY_-d_R0ElXxUvLnOdbM4wbAPZ6T_b8ynAuL5LMvvL1uiSjHo9UA5KotxKcHLjc-CqBl-M2jN8OFdCAwEOt8AJzN8oCZmn4ylBO4Wv94NqBbB-LH0Pe-7uN9OfPP8h5LnKal6na4H5gFIDSGJ3GdUS0DTRRhvUIC_-QgOCcOWY-Yhpu3t_W3_3vHWylT1TZZW3safs3fCyVK9uVYkX6A5atafLc_NsmhgT6nrH4w6fWwPq6txNFArdGoRHnNEuerhYGGjDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاخ سفید درباره ایران: ما به تعهدات خود در آتش‌بس پایبندیم.
🔴
حملاتی به کشتی‌های تجاری صورت گرفت و ما پاسخ دادیم.
🔴
خشونت با خشونت پاسخ داده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130877" target="_blank">📅 15:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130876">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869b87835f.mp4?token=BT_i-N_GLOt1jgCjCQVRGqqXbg3QE01KyeIrcxry1yGnqDJQID_YTsN1iWl55fcl0QAhA6XXGHIMziiT4RVhsa-oWZkEsT0Qs9G5SQevtq16bMR_iZHGpL8ELbLYzwXBLfcw_tMbTrD5d3lT4ROKQh2sNUEXXWK6hkoAAQ0h_2MOLnGeqtnxOjVlIWCRN3arTir3XPX3gY0ko2Ptzq60Vn6cOpMV-Amn8ClJ_WL-gj2SvB0PPLtpiKeM5oKk2IiiFX9tFhqpo569ryGIIC21oQjz6Sd2ZxK-we8sJBpLLwlguNrMpPpZ8pks3E-YNW4wpuUUeqhYSvtugxF_E674Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869b87835f.mp4?token=BT_i-N_GLOt1jgCjCQVRGqqXbg3QE01KyeIrcxry1yGnqDJQID_YTsN1iWl55fcl0QAhA6XXGHIMziiT4RVhsa-oWZkEsT0Qs9G5SQevtq16bMR_iZHGpL8ELbLYzwXBLfcw_tMbTrD5d3lT4ROKQh2sNUEXXWK6hkoAAQ0h_2MOLnGeqtnxOjVlIWCRN3arTir3XPX3gY0ko2Ptzq60Vn6cOpMV-Amn8ClJ_WL-gj2SvB0PPLtpiKeM5oKk2IiiFX9tFhqpo569ryGIIC21oQjz6Sd2ZxK-we8sJBpLLwlguNrMpPpZ8pks3E-YNW4wpuUUeqhYSvtugxF_E674Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاخ سفید: ایران درخواست جلسه‌ای در این هفته داده است.
🔴
ویتکاف و کوشنر برای جلسات سطح بالا به دوحه پرواز خواهند کرد.
🔴
در حاشیه این مذاکرات سطح بالا، مذاکرات فنی نیز برگزار خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/130876" target="_blank">📅 15:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130875">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
‏این تنها بخش کوچکی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراق است.
🔴
‏اگر روزی خانه برخی مسئولان جمهوری اسلامی هم به همین شکل بازرسی شود، چه چیزهایی پیدا خواهد شد؟!
🔴
امروز در عراق بیش از ۱۲۰ نفر به اتهام فساد بازداشت شدند...
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/130875" target="_blank">📅 15:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130874">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سرکنسولگری ایران در دبی: نخستین پرواز تهران به دبی پس از جنگ در فرودگاه دبی امروز به زمین نشست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130874" target="_blank">📅 15:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130873">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PXTRZ9ASfvDxSqCXXO1XjZHog2Ey-ZSEmYdlMe2QGB9OHe9PAMq31vGN2wUJ0hx5j5mEZ3j_P3GL94XJ20FqzUktCK_UPjzxQU07M-ICsQ6XCaUw3PIf3wyXSF4SSzLIDdWtMVuiMMJuBpe7avKdWEB0NC7FHM2gQgC4oxlvZzwMfPaOmwSqWLFveHJgn6PIMWIOp8DVqvFuZfKUHmh5sETdlSiVGCtswoYGfb5KCTK7gfMVGREwF8IvrXsDOmuDkt5dkL6ieE8qW5w0s2E6CGl1YC8l0bVGF1_6r7R6j5lEepY3OePOHAbQemr0ViRcKqd3GtvaCD0Gi1uT2hkPoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوستر برزیل برای بازی امروز مقابل ژاپن
عمو و مادر سوباسا
@AloSport</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130873" target="_blank">📅 15:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130872">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0906a59cec.mp4?token=i239j68kFNTfiQpYabLkL6S7TAxIfilyAEuJV-egQM4KQPwN-Gc0tEXRAgvB8rNrcTn64Nf_SatMmAggiVVpoaYyKtt-5c0CYgAEdBCur1-6FCcmWdxXIeKHe1H80QLX8LLGhlj1IOggPDpdNG5L-SD0reSrFdWMTbmAucHUSQnr4qDV0ovUSLOF5g6b6LimPC-IG9PpQNiZsHFOWAu8flVqwzDw0h0EF-el02w2I3qom5nOPVostbwdZGfhpBLc6jbIQEu99bO64U5_3bdzr1Kkza01nzWUXaMMk1sr7X1mwQ3D3_gveJnhw95bWO1LjATd_wrWFqnoCDc6JGnVYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0906a59cec.mp4?token=i239j68kFNTfiQpYabLkL6S7TAxIfilyAEuJV-egQM4KQPwN-Gc0tEXRAgvB8rNrcTn64Nf_SatMmAggiVVpoaYyKtt-5c0CYgAEdBCur1-6FCcmWdxXIeKHe1H80QLX8LLGhlj1IOggPDpdNG5L-SD0reSrFdWMTbmAucHUSQnr4qDV0ovUSLOF5g6b6LimPC-IG9PpQNiZsHFOWAu8flVqwzDw0h0EF-el02w2I3qom5nOPVostbwdZGfhpBLc6jbIQEu99bO64U5_3bdzr1Kkza01nzWUXaMMk1sr7X1mwQ3D3_gveJnhw95bWO1LjATd_wrWFqnoCDc6JGnVYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اقدام عجیب تلویزیون کره جنوبی در اعتراض به حذف از جام جهانی
🔴
شبکه KBS کره جنوبی، پس از حذف کشورشان از مرحله گروهی جام جهانی ۲۰۲۶، تصویر هونگ میونگ‌بو، سرمربی تیم ملی را به‌صورت تار (محو) پخش کرد.
🔴
این اقدام معمولاً برای پنهان کردن هویت مجرمان استفاده می‌شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/130872" target="_blank">📅 15:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130871">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
پلیس آلمان: پنج نفر در پی تیراندازی در شهر شتاده در شمال آلمان کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130871" target="_blank">📅 15:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130870">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ: تهران هرگز سلاح هسته‌ای نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/130870" target="_blank">📅 15:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130869">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d4a95a20.mp4?token=a4hCm5JKj2amhMoJB4Xm012iCaaK1VKMBcy9AqeDHWxcuSVF9364o3CDW41YxRCiGjxDPbpVojBpmBz62I7mH1SfPgz2Hi9fFsisIOsKJUzGt2EhezBZnREqyGK9JvC4M_znkG3QB_rlgM3W4og_EcUj6s1_EdXwZUVI5oTfHEN9cEuIeew_oKUX0nKquFrrpsZvLCr4BgtVKCIFzABzpnOjqqjr5MJm_zNF0l-DRgOj97AhY7QKn6CnmITWK4wRzoA_U7_Yl4RamgNMoGq_UoCyeKb6KEPHxAilQnLNfxwhEdv6XScgvYu1n9H2VgdHkqy3gmfHNDQGWFKHms5USQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d4a95a20.mp4?token=a4hCm5JKj2amhMoJB4Xm012iCaaK1VKMBcy9AqeDHWxcuSVF9364o3CDW41YxRCiGjxDPbpVojBpmBz62I7mH1SfPgz2Hi9fFsisIOsKJUzGt2EhezBZnREqyGK9JvC4M_znkG3QB_rlgM3W4og_EcUj6s1_EdXwZUVI5oTfHEN9cEuIeew_oKUX0nKquFrrpsZvLCr4BgtVKCIFzABzpnOjqqjr5MJm_zNF0l-DRgOj97AhY7QKn6CnmITWK4wRzoA_U7_Yl4RamgNMoGq_UoCyeKb6KEPHxAilQnLNfxwhEdv6XScgvYu1n9H2VgdHkqy3gmfHNDQGWFKHms5USQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زنگنه : فرق این تفاهم‌نامه با برجام اینه که تو برجام امتیازهایی دادیم که پس گرفتنشون راحت نبود، اما تو این توافق هر وقت بخوایم، می‌تونیم بریم به همون شرایط قبل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130869" target="_blank">📅 15:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130868">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550d1e43a6.mp4?token=V9zHFslZRPPEwgFpc6DF8HHphgYYXZoVC-r6PEn_kbhMVmR22tIisoLRT9YLIsrFafh0Zb7elStOkYHGCvxbpUGdZEYlpzeysQRFI6X4ydRYXWz2RoffQQtAk8MiL29K8qMczJTnzFe2PM3xMcKWryLh_ywagEfwqTFWTrIDRCwpyDGZpGXGgrNEuJK1mOitPSLeOtb9sMoWzCp43DVkRHsf48u6tHzk6GdAzgJy33mhzwhPm8shnVNs_dm771-4SLIwLsMy262JLkF8vwhr3Ip8GCInbxH64YXE1BYwM-mOwW6DLWXKYyHZsH3dhgyzfb1zqDtT0eok0oEHGcEGHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550d1e43a6.mp4?token=V9zHFslZRPPEwgFpc6DF8HHphgYYXZoVC-r6PEn_kbhMVmR22tIisoLRT9YLIsrFafh0Zb7elStOkYHGCvxbpUGdZEYlpzeysQRFI6X4ydRYXWz2RoffQQtAk8MiL29K8qMczJTnzFe2PM3xMcKWryLh_ywagEfwqTFWTrIDRCwpyDGZpGXGgrNEuJK1mOitPSLeOtb9sMoWzCp43DVkRHsf48u6tHzk6GdAzgJy33mhzwhPm8shnVNs_dm771-4SLIwLsMy262JLkF8vwhr3Ip8GCInbxH64YXE1BYwM-mOwW6DLWXKYyHZsH3dhgyzfb1zqDtT0eok0oEHGcEGHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زنگنه اگه لازم باشه، ایران هنوزم می‌تونه تنگه هرمز رو ببنده
🔴
طبق توافقات موجود، ناوهای جنگی حق عبور از تنگه هرمز رو ندارن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130868" target="_blank">📅 15:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130867">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029bbf8e06.mp4?token=Hje-a-1DnVczoV0rOcHV0IPWU4pRoiacpDvAmvqT8tEUFBvGSjE8gzCo40SuzZjarterIVxHEL7Y8CzfBJeJVup-nHu-M9hIBzUbQZyebV1WpjQUnCrZDSKuhpSHAw2jU7kCcks0rDpbKnw9D8WVkhkhgYxm4_EVjQNlVHXCFY0yeAoaGoRcLDOA7q6w7ufHLRZK0skOXJBi6rOTwQuXqUkBxLcmmOONCxQ5FnU4R1OTemotBKbRB28MphdUeIxinjuvA-ZH5wWnqe3-vno-V1CN9tH71YOjOqTJHueZ8qFJw44rLOCB7EFc89Ynk_TULdVp3eioYplVwMkNen0vHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029bbf8e06.mp4?token=Hje-a-1DnVczoV0rOcHV0IPWU4pRoiacpDvAmvqT8tEUFBvGSjE8gzCo40SuzZjarterIVxHEL7Y8CzfBJeJVup-nHu-M9hIBzUbQZyebV1WpjQUnCrZDSKuhpSHAw2jU7kCcks0rDpbKnw9D8WVkhkhgYxm4_EVjQNlVHXCFY0yeAoaGoRcLDOA7q6w7ufHLRZK0skOXJBi6rOTwQuXqUkBxLcmmOONCxQ5FnU4R1OTemotBKbRB28MphdUeIxinjuvA-ZH5wWnqe3-vno-V1CN9tH71YOjOqTJHueZ8qFJw44rLOCB7EFc89Ynk_TULdVp3eioYplVwMkNen0vHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زنگنه، عضو کمیسیون برنامه و بودجه مجلس : برخلاف چیزی که دشمن تبلیغ می‌کنه، کنترل تنگه هرمز دست ایرانه و حتی برای این موضوع هم قانون تصویب شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130867" target="_blank">📅 15:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130866">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
دو زمین‌لرزه جدید صبح دوشنبه ونزوئلا را لرزاند.
🔴
اولی با بزرگی ۵.۱ در ساعت ۷:۰۰ صبح نزدیک ساحل آراگوآ رخ داد، و یک دقیقه بعد پس‌لرزه‌ای با بزرگی ۴.۲ در حدود ۱۰ کیلومتری شرق لا گوایرا ثبت شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130866" target="_blank">📅 15:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130865">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رسانه اسرائیلی: ایرانی‌ها دارند آمریکا را مسخره می‌کنند و اظهارات یک مقام آمریکایی مبنی بر اینکه مذاکرات طبق معمول ادامه دارد را رد می‌کنند.
🔴
تلاش آمریکا برای نشان دادن اینکه «هیچ اتفاقی نیفتاده و همه چیز خوب پیش می‌رود» فقط باعث می‌شود رفتارهای بد بیشتری از خود نشان دهد. این یک نقطه قوت نیست؛ این یک نقطه ضعف است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130865" target="_blank">📅 15:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130864">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
العربی الجدید به نقل از یک منبع در ارتش لبنان: ارتش اسرائیل در شهرک‌های فرون، زوطر الغربیه و الغندوریه که به عنوان مناطق آزمایشی تعیین شده‌اند، حضور ندارد
🔴
در انتظار سفر فرمانده سنتکام طی دو روز آینده هستیم تا موضوع مناطق آزمایشی‌ را پیگیری کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130864" target="_blank">📅 15:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130863">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLJ7HV7AXDy0IOzyUracJN13PjTniZjjkDcO804O90AovPYfsIIBLS79GVtXKsKpg9DTHnxbUjzkihctsA8WwAMyfucm4uwKtV8Wb2Ou6_vzbBLU4MNiFYaAtif-Uoa-U6QkSYFvlHoK9lnO0PTAJC0UXe4SQCWeVY6-b5YM92mXYQPuPahV-kkSsna745GwrgPqmyiHab0jukOeVVyNyNWSShF-R4CQw5hjR-I6M94UdU3CuAAQkZ4qArR9lVK7ClUYH3wIELXxQ5TJjwzL9ajdl_d4XhUxfDWPPwr9QmyZbI_r6t5yNyN4bWlRujFtVeiPnEfnkKbVfSTr7P9ADg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:نفت خام وست تگزاس اینترمدیت - ۶۹ دلار، و رو به کاهش است
🔴
این کمتر از قیمت قبل از شروع خلع سلاح هسته‌ای ایران است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130863" target="_blank">📅 15:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130862">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00245d127.mp4?token=NLnyMynKUVEn6xrYLYMa-o8spO4nbrGH8aUXYJ928BJEhD1WgFnahFOFaBlaEZYaWAzSf6TNSrQpdqRGp_Vs-zQCm58EHYvkF9cKXm2pKzr8jJ5CoHlMKwRqE5dFNK1F1-DymaqCggYeXD20adML3U-5qIdnMQFbhdv-_medn1GTR2DYbpsXbGJExta1x7lLiLng0-VYJWV9UDhLrSkpRMX8Z920yYkiD-rP8IiPFrrIHSzLco4EBwLgaom4il2bzLi7C_PXHTNgYg2bZcP__2YDKLaMFpu1T-t2AyjeFUx5erHfeMiP31-Zgzm0Gnye-sf7xPPSLQUXdCE2E78W4ldtknu8ipvlMNZBc7DPR5ufwD6ziCNNtbm_MFr36axgI55fC7u-BcP0XzKKpPjDq7ZZIcu5QwyIl7yyFyXEoIIAb0xlik821ThHWQ7D4GW5TR5T0w4NNnKMYj4Q6_u-1N7bBS69-7Zz1dni6TMLcFi3bSWJtz9yRRRQoRgH4gj021p3JqlLQDUsGRyEAvD7rBYHonZmZwajwV1ViVgmtwW-59V1XmxvepDrP37t6d8VNOfirI0K9uF78P7rDFGb9ENOynFk0GwWGxrv-947Wdjy3iM6c_JbQ94lzz1urAHWZmGMGEvbsyrxoMiJ8Vbt25BGXRbBCp1rxYuNTB8vDmM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00245d127.mp4?token=NLnyMynKUVEn6xrYLYMa-o8spO4nbrGH8aUXYJ928BJEhD1WgFnahFOFaBlaEZYaWAzSf6TNSrQpdqRGp_Vs-zQCm58EHYvkF9cKXm2pKzr8jJ5CoHlMKwRqE5dFNK1F1-DymaqCggYeXD20adML3U-5qIdnMQFbhdv-_medn1GTR2DYbpsXbGJExta1x7lLiLng0-VYJWV9UDhLrSkpRMX8Z920yYkiD-rP8IiPFrrIHSzLco4EBwLgaom4il2bzLi7C_PXHTNgYg2bZcP__2YDKLaMFpu1T-t2AyjeFUx5erHfeMiP31-Zgzm0Gnye-sf7xPPSLQUXdCE2E78W4ldtknu8ipvlMNZBc7DPR5ufwD6ziCNNtbm_MFr36axgI55fC7u-BcP0XzKKpPjDq7ZZIcu5QwyIl7yyFyXEoIIAb0xlik821ThHWQ7D4GW5TR5T0w4NNnKMYj4Q6_u-1N7bBS69-7Zz1dni6TMLcFi3bSWJtz9yRRRQoRgH4gj021p3JqlLQDUsGRyEAvD7rBYHonZmZwajwV1ViVgmtwW-59V1XmxvepDrP37t6d8VNOfirI0K9uF78P7rDFGb9ENOynFk0GwWGxrv-947Wdjy3iM6c_JbQ94lzz1urAHWZmGMGEvbsyrxoMiJ8Vbt25BGXRbBCp1rxYuNTB8vDmM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس دفتر نخست‌وزیر اسرائیل، ایدو نوردن: در جامعه اسرائیل اجماعی وجود دارد که بین رود اردن و دریای مدیترانه باید یک دولت وجود داشته باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/130862" target="_blank">📅 15:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130861">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usXR4Yk_pnuVn9o77Vz0Ax4ku0sA3Pry9VcyOjgSQLFTg-tLNT4KZEKTA8l8KOd0JdSc3KDXPZwOIQ3_ovFaz3Cr29NOZjrBpt8R_fzidO4E1xOvkJ5IXbags5IZ_VJ55Dvm6CAMDPo3Dq204g0az0g4F82WO697ZGc1eqfCtqsdMvlHmtYzXw3w61-ktlNFZyXGBCOxAe8YwR1-AOBHi0uUXU7kRyHubyc6m5qCX6CP6jbL1U6N0cYiLQc6IshzO8wxnyCTJBgl7hZwP9KibNG197jaX79-TzVpnbs_6MXPeSEtXqU7uki9960bioMt2D-k884zysIGVdP5EYnvnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین تصویری از یک فروند پهپاد مهاجر-۶ و ایستگاه کنترل ساخت ایران در کریمه روسیه منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130861" target="_blank">📅 15:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130860">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
کسانی که در خیابان فرزندان ایران را به گلوله بستند و شکنجه کردند، مولایشان حسین بود.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/130860" target="_blank">📅 15:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130859">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dyzT1CMIxbWiq3xf0XTY3zC9_oKAL1JDFixsEFpIPmOOmf_Uef4iqKyUYOfTiAiB_ZSrQCZETk0hmexA9jBmzEZ9j_7ZgNSnFIm5rEvudVlcACmp2k_HhDt30d5RSDeBR0DLLBtoK68G32TDvonOo5ZOUWoxFxFLUGPAT5FU1v7NQ8NQ69qsXrbuQFPslRu00zGxRSQpNIgksBRh6H1iMk_RN8JIG1AgcREAhwzq8i5D4LaXI9oQ1INXtlT8nZr8ggU9YxDjbWHtoebGyW8wKjy4WVcY4a0zGuITv3c7Lp5ifxdZbSI_fUKlISDRKSP9ZGYKy2WV_o9T1AXvAyBa1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ: ایران درخواست جلسه داده است. این جلسه فردا در دوحه برگزار خواهد شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/130859" target="_blank">📅 15:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130858">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
عراقچی به نجف رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130858" target="_blank">📅 15:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130857">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
بانک مرکزی: نرخ تورم نقطه به نقطه در خرداد ماه به ۸۳ درصد رسید
🔴
تورم سالانه ۵۷.۷ درصد ثبت شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130857" target="_blank">📅 14:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130856">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
آتش توپخانه ای اسرائیل، جنوب لبنان رو هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130856" target="_blank">📅 14:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130854">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fb964ef3.mp4?token=Jo4TT1rYLorb6w9xLwu8GdHfau7ZrxI_QVT0kPT0pBJ2gbUtrm_epfikWsVVSef9hPaiU216riLSb4YGJXbwxV3ICEThhVhVxnljxP0VkU0qs-snC1n0YcBUc7BTdZr3BfPKTEbV6kw1TpAD_NVxtK6UCiXyGLlPPSTf0xqIzwMXQB2HiioJeUD-g1uKUUtl9XZvtYzwriJSz95ElNCn9A25t8wMcTB8SnmMVYcj_igLiC-KHYqNOif51eaesnkYqKKbPiqHHEAznuh3Ese_8sfgEWGuU1EW2gudsggSiKvArxAGn1e3h7Deud_tA6MVcZfdU916x_jDLbdyJjNtLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fb964ef3.mp4?token=Jo4TT1rYLorb6w9xLwu8GdHfau7ZrxI_QVT0kPT0pBJ2gbUtrm_epfikWsVVSef9hPaiU216riLSb4YGJXbwxV3ICEThhVhVxnljxP0VkU0qs-snC1n0YcBUc7BTdZr3BfPKTEbV6kw1TpAD_NVxtK6UCiXyGLlPPSTf0xqIzwMXQB2HiioJeUD-g1uKUUtl9XZvtYzwriJSz95ElNCn9A25t8wMcTB8SnmMVYcj_igLiC-KHYqNOif51eaesnkYqKKbPiqHHEAznuh3Ese_8sfgEWGuU1EW2gudsggSiKvArxAGn1e3h7Deud_tA6MVcZfdU916x_jDLbdyJjNtLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیوسدادو کابلو، وزیر کشور ونزوئلا، در لا گوایرا دیده شد که با تیم‌های نجات آمریکایی بحث می‌کرد و آنها را هنگام حرکت به سمت کمک به قربانیان زلزله‌ها متوقف می‌کرد.
🔴
یک آمریکایی شنیده می‌شود که می‌گوید: «این خوب نیست؛ من خوشحال نیستم»، پس از اینکه کابلو همچنان برخوردی خصمانه داشت و به آنها گفت عقب بروند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130854" target="_blank">📅 14:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130853">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
فایننشال اکسپرس: تولید نفت خام در خاورمیانه در اوایل ژوئن در بحبوحه آتش‌بس میان ایران و آمریکا، به ۱۴.۶ تا ۱۵ میلیون بشکه در روز افزایش یافت.
🔴
تولید تا پایان سال، به طور کامل به سطح قبل از جنگ تحمیلی علیه ایران باز خواهد گشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/130853" target="_blank">📅 14:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130852">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
خبرنگار صدا و سیما: نیروی دریایی امروز هم به شناورها هشدار داد فقط از جنوب جزیره لارک بگذرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/130852" target="_blank">📅 14:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130851">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pngv7azciMNH83fbGLe0oiQ6LM7df1cSxV3h4VZ2T08mNbWy9vUEmANbj40UQLOkGXsFSiiv4TlbGlkNOqYcSX6rqjUCesABrKo5UzZk-qt6i5kBbQv8OOmhJ2LylSzTrYozc4byEVGnFMUp0yAmLfdY0JsFp4jqFR0YvPDtZ9c3Lsa-y1on14F6za6ioF_uOnd40U4zzMJMolQ0gCpicKNNePwBN23T6N9mwePoaxlpdDd4DgsuM-qvN9U-8uM-g2c-YqPofQsh67MsMYY9CvEknlRTraWmVLnUblRyN9VMq0vY-K531lr1LHKzq08sOQGxIIFvnE9N9wk4187vWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : محبوبیتم تو نظرسنجی‌ها از همیشه بالاتره
🔴
حتی از روز انتخابات ۵ نوامبر هم بیشتره؛ با این حال ایران نباید سلاح هسته‌ای داشته باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130851" target="_blank">📅 14:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130850">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee2c04f620.mp4?token=oHFkZO-2g4NXQmmBLNB-HmAHKxHNZiorr3H7vFtTpUAGYNLvdkzN_nhvu7r8y24OJDpfBfDPt3jvh7D8-Rrj-8efiGwtjbMKvT_Au-EKEt0hgtvckI8vvIQXJs4u_brEyrtNSiEcxOLMlhPZAdgPaV8m50rskoim4S1hhuIQ0Efn-NcxjSENtE_HP2-Dg21K1XRoTd3WVs1FaL_lgIjC3WNBCX3yKCdl1u5ZgCv0iJnABP4zzuEgn-RPvewptc5AnE_brWeZoyolsQW16dQ2E_6REiA6BiTw8blYnARFhL3Qu9LkhMKoL3gocadJKML15dyUMUCaXSc4aVDulkMGKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee2c04f620.mp4?token=oHFkZO-2g4NXQmmBLNB-HmAHKxHNZiorr3H7vFtTpUAGYNLvdkzN_nhvu7r8y24OJDpfBfDPt3jvh7D8-Rrj-8efiGwtjbMKvT_Au-EKEt0hgtvckI8vvIQXJs4u_brEyrtNSiEcxOLMlhPZAdgPaV8m50rskoim4S1hhuIQ0Efn-NcxjSENtE_HP2-Dg21K1XRoTd3WVs1FaL_lgIjC3WNBCX3yKCdl1u5ZgCv0iJnABP4zzuEgn-RPvewptc5AnE_brWeZoyolsQW16dQ2E_6REiA6BiTw8blYnARFhL3Qu9LkhMKoL3gocadJKML15dyUMUCaXSc4aVDulkMGKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جان کری وزیر خارجه دولت اوباما: نتانیاهو به اجبار از اوباما می‌خواست که به بمباران ایران بپیوندد
🔴
او از اوباما اجازه خواست تا این کار را انجام دهد.
🔴
اوباما نه گفت و از شرکت در آن خودداری کرد، زیرا فکر می‌کرد این یک اشتباه بزرگ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/130850" target="_blank">📅 14:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130849">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGxN-hx79Q2WAGEi9dBJ0tqa70F_WFpo5M2OnYebSZ2DOL2qzGedVxkeZZMKSx2NVe-PNoHtNrCVO9JZ_qzFpZPdIh13vTvA84ed4NobkrMA0bBfENHidaymh60LebwQ48LiX0PeRDvOVF63pTYdNBUYQsawKihwNzo2Uv-ry3YYJLZuLkrxZiWh7uGzJ4lFdIx22Lh-Nu5kOkiamfn-IsVX0EeIXqbuqcSUfTrhgf_a_D0yO764H2Gyg-LaO3l5rTyqCLfAK0zFoJwMr99OV1Ff9OzwTEhq8Y6z1PGLHpyVg05tR_qOyn-uu_xxxRKZ9qVVD73709K-Xtp8pFgUlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
آیا فکر می‌کنید مردم قدردان کاری فوق‌العاده‌ای که ما در ساخت و اداره نمایشگاه بزرگ ایالتی آمریکا در ملی مال انجام دادیم، پر از مردم خوشحال و همه عاشق آن بودند، هستند؟
🔴
از خودتان این سؤال ساده را بپرسید، «آیا فکر می‌کنید اوباما یا جو بایدن خواب‌آلود می‌توانستند این کار را انجام دهند؟»
🔴
پاسخ خیر است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130849" target="_blank">📅 14:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130848">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d3b8ad0e.mp4?token=SgY8wgb48CuGNXriFZyn4_xMseTIb-3r7dNzUKlK1pADrjNmxNAKOz3pO0lEU-fzx2xg3aSg_Nwb24DuuE2WDmPF032nzansQD-IuqyTTzlJO-n_KGtJ6MPiq5yTzuerri39YiF8mSxn7zoztxG3ELXzAUn4k1BBTj8-HlEhlHq84XbMDtBGweSnMvHwDRsaUI-BfdnURm8kvQYka3Opwoxw_WNx3E5jvbiVH61f-isfZO2_T10A5Aop-jKO3d_hL9CnBVj9ezo8-ho8VDLQpKlJKocVPeioxuzeB7DbsBLTyn2dkbxOLqgW_S36R08KcnMDm0P5m_P3FFHU39uEPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d3b8ad0e.mp4?token=SgY8wgb48CuGNXriFZyn4_xMseTIb-3r7dNzUKlK1pADrjNmxNAKOz3pO0lEU-fzx2xg3aSg_Nwb24DuuE2WDmPF032nzansQD-IuqyTTzlJO-n_KGtJ6MPiq5yTzuerri39YiF8mSxn7zoztxG3ELXzAUn4k1BBTj8-HlEhlHq84XbMDtBGweSnMvHwDRsaUI-BfdnURm8kvQYka3Opwoxw_WNx3E5jvbiVH61f-isfZO2_T10A5Aop-jKO3d_hL9CnBVj9ezo8-ho8VDLQpKlJKocVPeioxuzeB7DbsBLTyn2dkbxOLqgW_S36R08KcnMDm0P5m_P3FFHU39uEPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این ویدیو از اعتراضات دی ماه به شدت در رسانه‌های دنیا درحال وایرال شدن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130848" target="_blank">📅 14:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130847">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v20NvEanMmM9Juj7rNuF_nuHGus1KU0IoPG-Bt9apSA1ACD_RD0pz8CqdgITQOc__CVbuaWfiu3yF3DqPa8AuH93bPO3vvPrboTIIWcP_T593i8DqoivnyirDefmAPmMieu35nLrGq7NP-LOzkZpqa-4WzcwlJK4ii5al0GtsWlb18MzsyPUiZ15QOQ7R-dZOidux-0_hjwgkTKUMk3vmF6JdpIzFfY-Z1xGB8no5M_ITOpPreOMwULZJSCrb7XF9pQmUWxDEee5l4LGyh8S0e94_sEfnEfKuPHECW2NHR_cD04DksbLyy6_VjudhWzFg-XUvIQYfdRIy-2ibnzqEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / رویترز: ایران شرکت در مذاکرات فنی را لغو کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130847" target="_blank">📅 14:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130846">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GS540mSkOsyQZLzqt5VTiR3jv2PUO4tCc6e8dEXf_GWcu88aafEAbIMDFQiiRbXz97cqQcYQkv31SOTGOLaii75OKBaCZbXLawStG8BchLwHVVaoobKH1R56ako2J5sdCQq3hDtigFVC9qLAOoMSW-eo5EKwXxwio9dXmbKBflGTanylY4CLRtZS-bYyKGaSVe0-rum3m3F-ZXu0ymstU0E9OzNWW8FqJbxPUJFEWfIzZSBqTNRhtNkjnGMBggqYiobBiHEgZgZmgN8gg4dgJ5rG4p_EGdwMOIMMeHHnPssbyF1Ikp_ji-oqqQrES3317hCiob_Ch56gSOn_7Wu4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیت‌الله مکارم: اگر بدخواهان مانع‌تراشی نکنند، توافق می‌تواند آثار مثبتی برای کشور داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130846" target="_blank">📅 14:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130845">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxA7rAj-A61vwhma-eUtUvyceIbMp2GcMee1CcX-K6ZJpwCqy-d7MilHwfRspOm1SENi448x0F6MPKrGcrk3InGFMDxj7w8ltPmsCtRtVK1TraJUJocYND9cMVZC1AjY33GWfVJT9OslcYb9NKxZ7f8ufMWsYb1UC1awxZgpRvkCwv0jwUGyLzAU3mOOGTi83VPZsHKbZKLEfTTtadQMFtQleue-ryflutshusDr-Ji0801NQItX1bKUfrG7BtUf4YIj0ncJtve58ftqqvAH-8clwF-ev8DWXLJFzVj7ZcR8qNON2pBE5ZyBi9PJjuGW1sOHOqkDGUJobpxp7tAgMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار ان بی سی:
یک منبع آگاه به من می‌گوید گزارش‌ها مبنی بر اینکه ایران در مذاکرات این هفته در دوحه شرکت نخواهد کرد، نادرست است.
🔴
او به من گفت: «تیم‌های فنی که روی اجرای تفاهم‌نامه کار می‌کنند، قرار است در روزهای آینده در دوحه دیدار کنند. کانال‌های ارتباطی ایجاد شده برای کاهش هرگونه حادثه‌ای برقرار است و مذاکرات فنی قرار است ادامه یابد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130845" target="_blank">📅 14:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130844">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
رجا نیوز : پزشکیان عدم دسترسی ایران به پول‌های بلوکه تا کنون را تأیید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130844" target="_blank">📅 13:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130843">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PM3Cu6EqK87hIoWt5sHNCy1vuMWPwAluipARSmrR3qSAQmMyyhTV2MJ8jgVYpXDkBkReKC3kSmS-MIjQ4TExSUp_XRXUGzvzdC4AwvqSS6zozqOFCkSen3Lm3AC0NL-fkC-47gAyqOpqyBj54y4H_PVstKJEdfyCHCzcrjHHVYjhcYtcovZrwxyZtlak7D1PKMSBMLJCHK-lnCeJZRmPzc9tWqCLpcsjnjJQbPpvAmSV1XANpDjjJelLb6YuLo5UjURKMemjcWYX7tf-WtRGfXsnRyq0TIZv6LAwe1nWUpIDgvdgaS3RGfzpGaz-8HFGK76EKQac80WjQjVtoepU1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت یک وکیل دادگستری درخصوص پرونده عجیب پرداخت مهریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130843" target="_blank">📅 13:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130842">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚀
سرویس Vpn(v2ray) تیم اکسپرس
✅
اتصال پایدار و پرسرعت
✅
دارای ساب برای اطلاع لحظه ای از باقیمانده
✅
متصل در تمامی دستگاه ها و اینترنت ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 50,000 تومان…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130842" target="_blank">📅 13:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130841">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚀
سرویس Vpn(v2ray) تیم اکسپرس
✅
اتصال پایدار و پرسرعت
✅
دارای ساب برای اطلاع لحظه ای از باقیمانده
✅
متصل در تمامی دستگاه ها و اینترنت ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 50,000 تومان
▫️
۴۰ گیگابایت — 95,000 تومان
▫️
۶۰ گیگابایت — 140,000 تومان
▫️
۸۰ گیگابایت — 185,000 تومان
▫️
۱۰۰ گیگابایت — 230,000 تومان
▫️
۱۵۰ گیگابایت — 340,000 تومان
▫️
۲۰۰ گیگابایت — 450,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 560,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 95,000 تومان
♦️
۵۰ گیگابایت — 140,000 تومان
♦️
۷۰ گیگابایت — 185,000 تومان
♦️
۱۰۰ گیگابایت — 250,000 تومان
♦️
۱۵۰ گیگابایت — 365,000 تومان
♦️
۲۰۰ گیگابایت — 475,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 675,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 240,000 تومان
▫️
۱۰۰ گیگابایت — 275,000 تومان
▫️
۱۵۰ گیگابایت — 390,000 تومان
▫️
۲۰۰ گیگابایت — 500,000 تومان
▫️
۳۰۰ گیگابایت — 720,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 820,000 تومان
خرید:
🤖
@Team_express_bot
🤝
فروش عمده و پنل نمایندگی:
📩
@expressuport
📢
کانال اطلاع‌رسانی:
🌱
@vpn_express_sup</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130841" target="_blank">📅 13:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130840">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ارتش: انفجارهای کنترل شده در شیراز به دلیل خنثی‌سازی مهمات است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/130840" target="_blank">📅 13:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130839">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9ce41f48.mp4?token=AxwWIy_aQiPDATkv9-xFa9RPVzhteIHPn3zZylgsj5Es06ot6jzeZ0EOWHc-wyeSi8wTLQtgyaq6uQwDIQSCUf2laWHlQ2STVepwaOIH0_R8Mg3A6HPV3I3YvpXDxp8Yn0JZfh2ZnC5PaFCw8gdbi_6kQzwwX36_0dfbcJburD1D3_5_dN8VqAlGngUi_PiG3r2ABShES7ixw5IS9m5bEMicdTZBKidFyzCOFSlY2Md34xiB774olSAEU8Xc_iaiLC7P37Rc6mSXiaaJZE744eU2Eh2Hv1SRb_FKF7IIwtKvzUG_8ZbJEhhPEKmXBjPRXx8uMaRkPuDdvTCBuqg2sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9ce41f48.mp4?token=AxwWIy_aQiPDATkv9-xFa9RPVzhteIHPn3zZylgsj5Es06ot6jzeZ0EOWHc-wyeSi8wTLQtgyaq6uQwDIQSCUf2laWHlQ2STVepwaOIH0_R8Mg3A6HPV3I3YvpXDxp8Yn0JZfh2ZnC5PaFCw8gdbi_6kQzwwX36_0dfbcJburD1D3_5_dN8VqAlGngUi_PiG3r2ABShES7ixw5IS9m5bEMicdTZBKidFyzCOFSlY2Md34xiB774olSAEU8Xc_iaiLC7P37Rc6mSXiaaJZE744eU2Eh2Hv1SRb_FKF7IIwtKvzUG_8ZbJEhhPEKmXBjPRXx8uMaRkPuDdvTCBuqg2sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش پاکستان : تو عملیات «غضب‌الحق» به اردوگاهای گروه‌‌های مسلح داخل خاک افغانستان حمله کردیم
🔴
آدم‌های داخلش کشته شدن و انبارهای اسلحه‌شون هم نابود شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130839" target="_blank">📅 13:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130838">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erR0f_mPbSbUgq-ZweslZKGJWE7NIAvQNtxQa0PSVrflhHrx8uYkUoettYFhKyMcEBNqpsxmMcTmibO8mJ3zAAclzKtAWjWs3945Pr13WLQ77GtoOEj7bTOyD3gxND1PsAcjq3yhH7xaCKOwk7RYbjnRcY6iS3y1RhxLcaley9s7fxA3SEY7e5o-eS376r5yZJWFxwTVO4D8XEM25NvVys3dOPwzjlLovCBK_M8m_jXdIbd4T6XK1rlU41dxJ4Z0dfsywdVwhfqwpcn9XySSTbHrTbF-NVR3Gfiufgp3V5UCI9te7T2fzA2nfMbsG0YEQ8MrTjsw93DTBLruAEr9AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان حقوق بشری
هه‌نگاو
:
روز جمعه 6 تیر،
امیرمحمد کاظمی
، سرباز 19 ساله اهل نگارِ کرمان، که برای مرخصی اومده بود خونه، به همراه چندتا از دوستاش رفته بود بیرون که یه دوری بزنه؛
🔴
بعدش به خاطر اینکه صدایِ آهنگ ماشینشون تو ایام محرم زیاد بوده با نیروهای بسیج درگیر میشن و تو این درگیری به امیرمحمد شلیک میشه که گلوله دقیقاً به سرش می‌خوره و همون‌جا جونش رو از دست میده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130838" target="_blank">📅 13:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130837">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: جی دی ونس و افرادش کسانی بودند که طرح مخفی موساد برای تغییر حکومت در ایران با کمک کردها را به اردوغان، لو دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130837" target="_blank">📅 13:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130836">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
المیادین: محل مذاکرات فنی ایران و آمریکا از سوئیس به قطر تغییر کرد و به گفته یک مقام آمریکایی، این مذاکرات همچنان طبق برنامه در روزهای آینده برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130836" target="_blank">📅 13:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130835">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
گزارش اختلال شدید در همراه اول؛ تماس‌ ها قطع می‌ شود، پیامک‌ ها با تاخیر می‌ رسد و اینترنت کند شده است
🔴
از دیشب شماری از مشترکان همراه اول از بروز اختلال گسترده در خدمات این اپراتور خبر می‌ دهند. کاربران می‌ گویند ارسال پیامک با تأخیر انجام می‌ شود، تماس‌ های تلفنی مکرراً قطع می‌ شود و سرعت اینترنت نیز به شکل محسوسی کاهش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130835" target="_blank">📅 13:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130834">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7rC7OwJyqBRNwTaEWumVRd6urzqdH5i610J8swD3Sf6Zw6EPEFhWzqFhs2ORgmkbYVp73P23DIpVeXtKL8WLbzQUtWiyh8BRyfP78twsfOzTAMNTMXmnSDmSHzFHJWoay-pFEqBu2EsovDub5QqO2TUivZDjZitfMUuDfycxcONpmG2m2s4ZAuCNXC8kMO4Ruwn5D3gQkgX5B0lT0c3kVnB-vg1V1XBYYWpajI_31Ib7XphpRIw03sG7A316M8cB1glVLF_OX50vnk1hH6fCKdE9qJhhJBbP67qug4ihiNe3Oa7pyGgThJpNf4zAXBPE9Z0WnvN3zLioEjobghHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با کاهش ۱۶ هزار واحدی به ۵ میلیون و ۵۹ هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130834" target="_blank">📅 12:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130833">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
آزمون وکالت ۱۴۰۵ در نیمه دوم پاییز برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/130833" target="_blank">📅 12:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130832">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رئیس ستاد کل اسرائیل، ایال زمیر : الان جنگ به یه مرحله حساس رسیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130832" target="_blank">📅 12:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130831">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ایندیپندنت: تابستان امسال تو بریتانیا با یه موج گرمای بی‌سابقه آغاز شده که دمای هوا رو در سراسر این کشور به سطحی فوق‌العاده بالا رسونده و اگه وضعیت ادامه پیدا کنه کشته های زیادی میدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130831" target="_blank">📅 12:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130830">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516d2a369b.mp4?token=VYyyuhN2wcBCJKPVTP9rM8INKvseZNIN_K5TgNQxgxgyO_FS2SFnMRPy0zHjvqt2Ffn7mO9-8xyz9IWUuw3NvY6nFW9Ein0fZfPDCidZ0Jr2ZKw8xcU3k6t9wU30YfYayKk-Mwlbwe-SsnbqFiOdUpAblQhH1zLOv67aC84EVIxZWvXQ_uloi_Z3gyACokCaQASH39WuTsBj_gMhvROHXd_xJGyyuQBiKO7WZRrM4vAIvOX0fr0t0-WBxI9-HCi-6l18Qlh9GI02j-zK1Vgahs8tqA35obV4XnXGSJdoz3SUobneC4Qw0GXHaeDkjzfpYDjSHS4DuhLcZXfeJuPamw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516d2a369b.mp4?token=VYyyuhN2wcBCJKPVTP9rM8INKvseZNIN_K5TgNQxgxgyO_FS2SFnMRPy0zHjvqt2Ffn7mO9-8xyz9IWUuw3NvY6nFW9Ein0fZfPDCidZ0Jr2ZKw8xcU3k6t9wU30YfYayKk-Mwlbwe-SsnbqFiOdUpAblQhH1zLOv67aC84EVIxZWvXQ_uloi_Z3gyACokCaQASH39WuTsBj_gMhvROHXd_xJGyyuQBiKO7WZRrM4vAIvOX0fr0t0-WBxI9-HCi-6l18Qlh9GI02j-zK1Vgahs8tqA35obV4XnXGSJdoz3SUobneC4Qw0GXHaeDkjzfpYDjSHS4DuhLcZXfeJuPamw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سود سپرده بانکی افزایش می‌یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130830" target="_blank">📅 12:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130829">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
نبیه بری: تنها راه اخراج اسرائیل اجرای تفاهم‌نامه ایران و آمریکا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130829" target="_blank">📅 12:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130822">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iM0MZDxlZl3_vI0gDDC08nnIYSHMche_Rsc9W4IwG7tfwuRE7Rth0EAfdPbZNCl3y3dlOYRBdIe3Y4OSqlk1cjBuMfzWiNQZFEpcj2am0YQAidx1GbFCQvepGOmZG0jyB4_SkmL67TGiOHux5g_aQvIfaF0UE_qZK1HlSD2dSYlfOFElGjMjLatmHfOld0YWlYKG71VR85Cpdvvt845ZshycFzUiYiAa04OVl4ymcUxYM1bDoTcx3F1aANq7AZSTCbCvU8JOtLX2xV5Vq7_8jdh7XJcZVEJl8fiYM9ULM0CwOkVHWY9E5VK0l61OBrs3bueIpZ9ckyAxBzbPgIeQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYWM0ZTnRSK8j3zlnAU91USETWRbu4ZRBtpPGJp7UgDKfNBcb7pt60IZzTSjjUdJ402xbQX5G7C010kntioXB4YNBN8xBxSWL6rkYPeqOccCHIl3PhPA4TbOaROpzD7qPi1SBw7LAcxDQ8gLcIL7oK-F5Csa-C_npoAmIw-H84TjsHBfXYvHboW7yL4w8kuup5Q0bNiobDE24LLh14UvwnqXw7r6HubkBRoJ1-kmqfk8EJ_0hXJABxDPM_8WMGZ5qXzBjijhEqbQdtdfVYHU016m1TuKZgU2VBHP8bHdeulGKdbAsOe_vfCmUEfjeB2C3jLUGyFZBQpJFqU9ILFSQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQzG4o6hdVAtx_Hlk5kNe2qaQxQLVSDhsIFFbJGON3nWMJR6o6L9E5-cnaq8nbxPupQEooo-TznMHD3_lFLFxlL7SI-LbX3c1FpEQWqucK1AXWoQxTfLC0FgU2fjJkQHJoZvPOk43pn0oLHJdLRAL9QfpCfxXdYw_CChbbWoPPKtKbXlHGeZTREzHRcHtO56TSq65wDN2pL0BccWNcLdE5oNFdLjy5Y0cJEM-a12qkEhF3sgoIb4KbaP763_0TbER68ueKb_ZHoLQZXpnck0vUXPm0Mk4o_9UgC5SjFP3YmnApk9FruMOBIjrHPh8af1Quhax7N9TFJY2EqVtSRBfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDVIjj_yk2pjyU8yeqTwkcr_M8cg6PbvysRYluh-ZOpKMtc2KZ8BEMc-1uooxfS8ltMoHUvH6PK6rJD9IxkEtGF_Y4VpJmjMKtXf5_HCUFx2clyKp2RtIGisLHJZEMucbk2q343u5eexwj7CisOCWbQJx6HNDRt-F-jEYrE8TFmYPMb1ny0VCDVRRPdY7ZVN_MFsAdswzrzd3ZW-eiqLIuxOOfp31MhKOvdT8dNXPCNbhzCz3052Qpdta2k6SgoveXLgD6c_-e0oPHScw-BBu87l1uXrvypzX5SEeKRbGobh3lBwTTDtZ57uheRUtbtrtXjqqQw2hC4DvVfh8nHCDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgkgkWBGeyyyw-WLxUW7UACEtCMgqML2cdUN5iIYMMozix-d4m8BeW2c-VM8_8U_-TrU9i6Ejmhy6YF-YrhV4vx8yfnZs56JCMIrZIOMjCAslb7w6ZWnyWqQ_vx6GhPNMQVeBIQ4Nf5Xl0giBlQSQ2pskKxgEvSbDcz_gzJyoNQlefGxzzqd63KuOUh3B_N2cn7i-1Uc07lGVQ454m2vIbQnkEsZ3dGYYFtp6LToT8ExjgmHrelKWKOtKiyE1z-mPUoX2Bz0lZ64mOqhJYPzHJGw0psDaJ18KBZOlmr_-i9qjZLjvDV346nv7_bNZ_CEWa_6WuBZRQGuURkmMZ7BOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ui2difXNBqDItjed0NL7LvS-7ZS3E2w2PlSLZ5xT52euB5Gx0FYayUZpNng-hHn4Z9PCrKG8XVVzMT216y81ujfG2bYASDNDlxzK95jlaSh6PqRtp5v05VBHCjrlNh_xS5LZfMPld_8U0AsBBGw5ipi_NZmUZ2_c1SwTJVG51uVtDwy3gDWgV-cjAd6NcvtyqE1wLmRTFr_tV8i8hCalaBo9A26J0DOgrA1nEoDVJIvWN8fDBW_fv7l-HAFhBgr0JDR94UiMbGqjiIn1yz5tsx_EODN_utcMLxFOhAtG-4rAThAGBUimrDIlxnuz3O3LeeH8IvEvt_BjklthZTtYUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i-WVhrO6zLX6RZQDcJMyqzYskHh0oVzBhyIh3D8PYW9oIOul8kNug92FTLEbT2RFG0YccOmokKKChRBupArx4442GCBqmgI0niIiV3CO80sU35Ia2ILRc03ZkBAX1TBq9u_1YlTZ1qlavQsiGnl9TBEIbplQdO-Phx6V7Fxg-1JwDKBH-krGqJDAX8VhUJ8MbiK5Wreg6VJBf14Adg8gqRPedgsCMYLlddcGxVV0e_3louzk4I_y-9AfPrPcFzZb0SiJiNg82virCihq2XDEF9oL5EDXhfBskBy3PrREYqsrlyfZMw2aw2VRUTojbU1Hg5ht1aZLq9IF23Em3KnqwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر خبرگزاری فارس از تردد کاروان کشتی‌ها در تنگهٔ هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/130822" target="_blank">📅 12:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130821">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سازمان جهانی بهداشت (WHO) با هشدار نسبت به پیامدهای مرگبار موج بی‌سابقه گرما در اروپا، اعلام کرد که «تنش گرمایی» به عنوان یک «قاتل خاموش» طی هفته گذشته جان بیش از یک‌هزار و ۳۰۰ نفر را گرفته و علاوه بر تلفات انسانی، زیرساخت‌های انرژی، حمل‌ونقل، بهداشت و محیط‌زیست کشورهای اروپایی را با بحران کم‌سابقه‌ای مواجه کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/130821" target="_blank">📅 12:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130820">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ارتش اسرائیل: در پاسخ به نقض توافق آتش‌بس توسط حزب‌الله، از طریق حملات مداوم به سربازان ارتش اسرائیل در منطقه امنیتی، ارتش به سه مرکز فرماندهی حزب‌الله در مناطق نبطیه و مفدون در جنوب لبنان حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130820" target="_blank">📅 12:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130819">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
استاندار تهران: روزهای ۱۳ و ۱۴ تیر در تهران و ۱۵ تیر در سراسر کشور تعطیل است؛ با این حال، مراکز درمانی، بهداشتی، انتظامی و بخشی از شعب بانک‌ها برای ارائه خدمات فعال می‌مانند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130819" target="_blank">📅 12:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130818">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2301d6d68.mp4?token=UyGMTOL3CEwxRfluDHaJYumKulnLkTrHm9HWMkDlHZDzaQSvoKI43ed63hg80i0k2laVFJljRWGh8nJMvfIl62pkSLsAhIDm3t6qrBoPL2wPxSEL0yMXsvjvmLFSbl920PbermPCBrvXJMhaYyWu23cJlmdHzO0Y-6_DFm6lKL_dJfpQ4rmjlGHqX_u4r2T1d17OW7HuD4c7tqWvgTFdSvstFO2klXWgioO2fwa8DD07KoyS9E2MOeea35xVT-eggLuEF9Tw-h6nGmMsyuqFv3wwaNYNTfiRcMUSdvDcdPYtcYyDLi8XD3m2J4RGbOGfR3sTx9OmJZMlL8-c1p4WGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2301d6d68.mp4?token=UyGMTOL3CEwxRfluDHaJYumKulnLkTrHm9HWMkDlHZDzaQSvoKI43ed63hg80i0k2laVFJljRWGh8nJMvfIl62pkSLsAhIDm3t6qrBoPL2wPxSEL0yMXsvjvmLFSbl920PbermPCBrvXJMhaYyWu23cJlmdHzO0Y-6_DFm6lKL_dJfpQ4rmjlGHqX_u4r2T1d17OW7HuD4c7tqWvgTFdSvstFO2klXWgioO2fwa8DD07KoyS9E2MOeea35xVT-eggLuEF9Tw-h6nGmMsyuqFv3wwaNYNTfiRcMUSdvDcdPYtcYyDLi8XD3m2J4RGbOGfR3sTx9OmJZMlL8-c1p4WGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تسلیحاتی که در این تونل زیرزمینی حزب‌الله توسط ارتش اسرائیل کشف شد ، از جمله راکت و قطعات ساخت پهپاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130818" target="_blank">📅 12:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130817">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eeb8978e0.mp4?token=O6JYrH-PBfcy-NSZZh8T0WRDw7H9BZr3b8LNsLEXR0wRclF_GDmConB4GW6GdO2JZ8eu-s3l0vIKtFAlQn_HWOR6eEPKssx6mGnJrkZdD763asBSVECY5PW4h2qGM60H_CsaJpEhymy8X-MDxOnly-rLEHd9ujaoCqDFmgb7c7OmOh40RC_L3SDcWMRhcJqcAo1nWmb0VYpM5b2HdFiozRojyuVuHoyV2s3G6D19veqALxL0rCJ3B9_fVactXH8eJX2D2jf4pyvyHDwVf-MgHWAFfF4eIELeGeCd9zQiHOCXtxqYQQp5X7f5FJQ5WnYlvvn1b4ojxLiaRRtV1BdpIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eeb8978e0.mp4?token=O6JYrH-PBfcy-NSZZh8T0WRDw7H9BZr3b8LNsLEXR0wRclF_GDmConB4GW6GdO2JZ8eu-s3l0vIKtFAlQn_HWOR6eEPKssx6mGnJrkZdD763asBSVECY5PW4h2qGM60H_CsaJpEhymy8X-MDxOnly-rLEHd9ujaoCqDFmgb7c7OmOh40RC_L3SDcWMRhcJqcAo1nWmb0VYpM5b2HdFiozRojyuVuHoyV2s3G6D19veqALxL0rCJ3B9_fVactXH8eJX2D2jf4pyvyHDwVf-MgHWAFfF4eIELeGeCd9zQiHOCXtxqYQQp5X7f5FJQ5WnYlvvn1b4ojxLiaRRtV1BdpIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل ویدئویی منتشر کرد که دیشب تخریب یک «تونل بزرگ حزب‌الله» زیر روستای در مجدل زون در جنوب لبنان  نشان می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/130817" target="_blank">📅 12:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130816">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
پزشکیان : از اون ۱۲ میلیارد دلار پول ایران که توی قطر هست
🔴
قراره ۶ میلیارد دلارش آزاد بشه و برگرده ایران
🔴
برای برگردوندن ۶ میلیارد دلار باقی‌مونده هم داریم پیگیری می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130816" target="_blank">📅 12:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130815">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
جان حداقل ۱۴۵۰ نفر را در ونزوئلا گرفت
🔴
برخی شاهدان می‌گویند هنوز صدای افراد را از زیر آوار می‌شنوند، اما نمی‌توانند صفحه‌های سنگین بتنی را جابه‌جا کنند...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130815" target="_blank">📅 11:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130814">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
واکنش بانک مرکزی به حواشی اختلال ۴ بانک: انتخاب شرکت‌های فناوری ارتباطی با ما ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130814" target="_blank">📅 11:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130813">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
مرکز مدیریت بدهی‌های عمومی و روابط مالی دولت اعلام کرد: میزان بدهی‌های دولت ۲۴۹۷ هزار همت و مطالبات دولت ۲۰۳۳ هزار همت است.
🔴
آنگونه که مرکز مدیریت بدهی‌های وزارت اقتصاد اعلام کرده، نسبت بدهی دولت به تولید ناخالص داخلی تا پایان سال گذشته (۲۹ اسفند ۱۴۰۴) ۶ درصد بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130813" target="_blank">📅 11:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130812">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHNQqw16dfb2CkkKvmlkJ9bf7Y0ya9MddMj_GYz77FlIA-84eT9y0SAoWSfTpWKB5XMQhvyG_zWvWar-6cOiVikvjmBhDRep_pLpJcF7-Oz39dSUCXPmJuOr3-g7cnrNRN_2t1W0HSEo8KRAmA6VPKZCNatZd_aOUJwuAD_IkqxDXWi50Iitc1gzhJXt6wW-GxnpF4xXebVjbP1k-_yaBGAxN5kaUWU7q7eAu_Jqpf3PYfTIQXQvgDwBRS2SATs7jCYzCt0Myi9-HkhGHq7uS9JWJpBzIyhZ1w1269HAHT_Q5EEIV6i9vx41NT7fRRUT_-coDNFK2d8pPQs0uDfLIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باز شدن نفت بالای ۷۰ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130812" target="_blank">📅 11:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130811">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
قیمت دلار ۱۷۲ هزار و ۵۰۰ تومان شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130811" target="_blank">📅 11:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130810">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ce213c07.mp4?token=rjDZpFxB40UplYCEZNc67Zu2qJemXLr1YhTMLata8EXUl-uq1r40jn2ssU_XZt2JXykLPMBlAUqPRDzOEymgZfapX3kHgr0MMxxeYxJSGWOB-VssnlnJztVNngfudUpajoRBDClhCe6PlvGopzMs5u_tKkwr6NgiTv3apIb6R1b4XX_kkuenLGtEOEbEQ2K6Io_uBXXYLvw61HCHVyljyK_b7E9WhLYB2ubVxxSm8EW3OvixqSxHKhO-H0-d_zquD2mdOS6oFr9PEvkJVmCQ8qFMuR7GepIDf8-eiID43vY7Owrtl9Y1UOaZA4tmzqq-ZeFw95PSBRdHr3rj5SHA0LDpPolFHuJgEPNEAa6lGV5Zw-uPN8-O8xzz8uruVV4v_MREQ6ts4fT4u3-R90Pa5Oc2ijAveMW-RKy7JcVGPcY8Ss4CxzxiqRui7HqjIB3yvn4Lxlp2icHLCaUdElJTISdZOhRi-cd4q0GT0g38zZlE3Q0jtJnCDHTQzWuV_qWbtIDuUO9uHzKT7dAHp9g9M-PqPXcerBoz9f-OHOB_aIEvfUHHgMTI19gBYx4iMiq6zrWCl5XFWMEtJEe9JgyZqCg8ZrAXCmekFEZU_JLJDDcqxQGupd6mYXbzOxB_TcK_zLqQkKpa7Qj2TGW4pRSEN70ycBYXn_CHwK9nEF6iwE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ce213c07.mp4?token=rjDZpFxB40UplYCEZNc67Zu2qJemXLr1YhTMLata8EXUl-uq1r40jn2ssU_XZt2JXykLPMBlAUqPRDzOEymgZfapX3kHgr0MMxxeYxJSGWOB-VssnlnJztVNngfudUpajoRBDClhCe6PlvGopzMs5u_tKkwr6NgiTv3apIb6R1b4XX_kkuenLGtEOEbEQ2K6Io_uBXXYLvw61HCHVyljyK_b7E9WhLYB2ubVxxSm8EW3OvixqSxHKhO-H0-d_zquD2mdOS6oFr9PEvkJVmCQ8qFMuR7GepIDf8-eiID43vY7Owrtl9Y1UOaZA4tmzqq-ZeFw95PSBRdHr3rj5SHA0LDpPolFHuJgEPNEAa6lGV5Zw-uPN8-O8xzz8uruVV4v_MREQ6ts4fT4u3-R90Pa5Oc2ijAveMW-RKy7JcVGPcY8Ss4CxzxiqRui7HqjIB3yvn4Lxlp2icHLCaUdElJTISdZOhRi-cd4q0GT0g38zZlE3Q0jtJnCDHTQzWuV_qWbtIDuUO9uHzKT7dAHp9g9M-PqPXcerBoz9f-OHOB_aIEvfUHHgMTI19gBYx4iMiq6zrWCl5XFWMEtJEe9JgyZqCg8ZrAXCmekFEZU_JLJDDcqxQGupd6mYXbzOxB_TcK_zLqQkKpa7Qj2TGW4pRSEN70ycBYXn_CHwK9nEF6iwE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از آخرین وضعیت میزان آب در سد کرج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130810" target="_blank">📅 11:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130809">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری / پزشکیان، رئیس‌جمهور: ۶ میلیارد دلار از منابع مسدود شده ایران در قطر آزاد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/130809" target="_blank">📅 11:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130808">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار در اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130808" target="_blank">📅 11:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130807">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
غریب‌آبادی: اولین نشست کمیته مشترک هرمز در عمان برگزار شد. درباره مدیریت آینده تنگه هرمز تبادل نظر کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130807" target="_blank">📅 11:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130806">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otjG6dGhn0i4aL2AJfTF8yMmObGlcFUzm_mfVrJffYxgzhCbNgVUH00nWsXS-85eQGGmCgRc4fNi7JFhbhv5hJnbcDLtGrdle8yx3dA1tKqCdz3f-aKIbHaXetIu1k2I-V0wMX6svtjSX9DvJjRSWaXkHaZMt6tkLiSUl6Sme6BqlKAWQFXVd-RFDk2ePlAqtPNXcfmFaFRf2pmqPEoIRy65Hv5473SgyW2ZYfNG3z_D5aGt68QNPRDC0bc4IkGZ-gFZWcgqu9Xzil833asbuJhgPbrbO8EAmD7qcKWs4hJexzWIYFA6IHI4xx4-8LeJY26Sht9QF_rv9HLYarGROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثروت بنیان‌گذار بایننس از بیل گیتس فراتر رفت
🔴
براساس جدیدترین فهرست میلیاردرهای فوربس، ثروت چانگ‌پنگ ژائو (CZ)، بنیان‌گذار بایننس، به ۱۰۷.۷ میلیارد دلار رسیده و از بیل گیتس با ۱۰۵.۹ میلیارد دلار عبور کرده است.
🔴
بخش عمده دارایی ژائو به سهام او در بایننس، بزرگ‌ترین صرافی رمزارز جهان، نسبت داده می‌شود. البته خود ژائو پیش‌تر اعلام کرده بود برآورد فوربس از ثروتش را دقیق نمی‌داند و معتقد است ارزش واقعی دارایی‌هایش کمتر از این رقم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130806" target="_blank">📅 11:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130805">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nhSWzDiiPWLH6e6_QhVd6zEJnPvBTNmvelEkliG0osZqhQuas_-jze-kFamPCVJizO_ljHNu_uPALUUwwE7AspkN1Orp30mV51Ixhag_luzPDsJGjyhdJ_QSa5kAuXOAgDhnfNX7uUgfUUGqbXGzdwx5dFlONkRcMB9tU3S-KI6Wm8TdpaBznP7TmTxYhiZUBbn_gR6rD5c-4yUg1Uf-m1IdgFmQTWSkf3bYcWfv-gV70X9ljxLbL__X1PfpV16xFQYunjBKDo0ZUxWKZXeudPSZWYyrgvn8tdQ_fjeuhXW5vxOR9bUhNplqR0S2FGevOZVG20PMhz_KISqdR-dbfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ذخایر گاز اروپا در مسیر رسیدن به پایین‌ترین سطح خود در حداقل 15 سال گذشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/130805" target="_blank">📅 11:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130804">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35ef3b087.mp4?token=KvW3gML2swm-r9fzJLOwhFFVnozFmrcl30Qd71Q8HhM5KE5BtvwBgNssGPH4NrZGCp5f7npONG56z-dpLC1DfZO_0RMg4wIh9i4NqJudsdv1MxDnL_Cv9lcKmjO95YkBXVbZ9-Td-8ENq1ScviKUARq06LgKR0Pvx98U7f3SWSPyBdEr249QZEgKe1ZB3fJY5vfvPxzdlqQi1l7G5vUa4Sf2419W8TcISsGFbrkTVT9UNwyvCdsE2k0fU1bBFCUuFScBqNKhbg9Y14TGkaVUa8YcqrdfgWQ2bgJcIaerR_0KiD5y3zgI_qoLtmRMfoxNN6eN8HRzqqDbEtkdarsG8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35ef3b087.mp4?token=KvW3gML2swm-r9fzJLOwhFFVnozFmrcl30Qd71Q8HhM5KE5BtvwBgNssGPH4NrZGCp5f7npONG56z-dpLC1DfZO_0RMg4wIh9i4NqJudsdv1MxDnL_Cv9lcKmjO95YkBXVbZ9-Td-8ENq1ScviKUARq06LgKR0Pvx98U7f3SWSPyBdEr249QZEgKe1ZB3fJY5vfvPxzdlqQi1l7G5vUa4Sf2419W8TcISsGFbrkTVT9UNwyvCdsE2k0fU1bBFCUuFScBqNKhbg9Y14TGkaVUa8YcqrdfgWQ2bgJcIaerR_0KiD5y3zgI_qoLtmRMfoxNN6eN8HRzqqDbEtkdarsG8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این ویدیو نشون می‌ده آمریکا طی ۷ روز گذشته فعالیت ترابری نظامی سنگینی داشته و حجم زیادی از مهمات و تجهیزات نظامی جابه‌جا شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/130804" target="_blank">📅 10:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130803">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5532f056.mp4?token=A7GHbZgVENXOs3uM1bNNNQniyj-LveCf1UlUszk4sdl6PYarnS2YPozcu7cLHWb552_A9NlJywLdz1lzNX0-gq0GMCkyXevHu4RD9rq1HmQq6UVZOadeeDPFNoRpok3Nwpm4f_fSN69SKSfPRkzAmeUa7TvTH8rcN70xFOXQFjZ8NAVC0MCMAJgGYu8YtndsCqqjb4QGO-VJ_tOPhfsDfTBRhDAfyklf0LrBk1r4GHMK-9d3fX-vdUz1fTcEqiR8tmWOyfWDdRw5MFLAkxkU4yEZLs69ZyAcdDH_rIYTjakC_3aKN2RU1TvaTA1IU0suza2migJI4O9M_foVlubBog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5532f056.mp4?token=A7GHbZgVENXOs3uM1bNNNQniyj-LveCf1UlUszk4sdl6PYarnS2YPozcu7cLHWb552_A9NlJywLdz1lzNX0-gq0GMCkyXevHu4RD9rq1HmQq6UVZOadeeDPFNoRpok3Nwpm4f_fSN69SKSfPRkzAmeUa7TvTH8rcN70xFOXQFjZ8NAVC0MCMAJgGYu8YtndsCqqjb4QGO-VJ_tOPhfsDfTBRhDAfyklf0LrBk1r4GHMK-9d3fX-vdUz1fTcEqiR8tmWOyfWDdRw5MFLAkxkU4yEZLs69ZyAcdDH_rIYTjakC_3aKN2RU1TvaTA1IU0suza2migJI4O9M_foVlubBog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور جان کندی درباره ایران: ایران الان مثل یک مرد خیلی پیر است که توانایی خوب شدن از سرماخوردگی را هم ندارد. ما آنها را به شدت تضعیف کرده‌ایم، نباید تسلیم شویم.
🔴
برای من عدم توافق یا توافق بد قابل قبول نیست ، در پایان یک دوره زمانی معقول ۶۰ روز یا هر چه که باشد، فکر می‌کنم باید دوباره وارد شویم و با قدرت با آنها برخورد کنیم ،باید آنها را بخوریم و استخوان‌ های آنها را روی زمین تف کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130803" target="_blank">📅 10:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130802">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
رویترز به نقل از مقام آمریکایی: مذاکرات فنی ایران و آمریکا درباره تمامی بند‌های یادداشت تفاهم، از سر گرفته می‌شود
🔴
دو طرف حملات را متوقف و کشتی‌ها آزادانه تردد می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130802" target="_blank">📅 10:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130801">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/229c290e15.mp4?token=JhvGwxqOjx3MY1EDJd_3NCVdMxCq15mJadlQWogKPoT-zLTY2FE_M9VLrMTs84nZmBmikj3w6wDb_14x-VbDpk9LW0vR6WYMGdVdH-gSYykYLfbZJ1KckDSmFB5b2dlrWECwrxKH4rj7Wr56kLcAokaY6tJ1kCSz1x_ZCz-9YMJABFV9lL6JFbUaju5oB55vSh-W4f_SUgglmv220W1FHUxn6R5tew8QpckW1TTsWVUJdZfVC4SlxjWCJ8VYa9l3yZqFg6zDj04YqMMIfVPHcrUScjEknpzejZIZNvsp0MG0oPbOlzW9QMRKdrJH2ItUDr4RuuTUpmAE0HqPiF6JXDCB1ISf7gmJ2v_jh03tkkAdg67_tyN0xFedsLV6iR9xoF6OubUfNol_Kmqocixuc0hQFgs20BSig1b3OHOlyjbUczMjPs5UZ1FCfG-_sVn8zVvQnz_BKbykqqcMgk-e3FYdW-0JaaQL-J2ifGA9pooX3W0Dz8qZkc1FktziYCDGUg7c2LZZNBmQNCd06C6KepYIW64K3g_7h6vszrsqVXqM80eU6WUliT2Qq18gaSlXUTXrLcs24hDGBClKPtomfXFHFpBZjX4GbEn3zkoWmlCriCyHSDgIR82jMwD9xC-k2y0sw2o_5qyRxFhoIr7AefCO5q_l5uDorudcoXX5CuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/229c290e15.mp4?token=JhvGwxqOjx3MY1EDJd_3NCVdMxCq15mJadlQWogKPoT-zLTY2FE_M9VLrMTs84nZmBmikj3w6wDb_14x-VbDpk9LW0vR6WYMGdVdH-gSYykYLfbZJ1KckDSmFB5b2dlrWECwrxKH4rj7Wr56kLcAokaY6tJ1kCSz1x_ZCz-9YMJABFV9lL6JFbUaju5oB55vSh-W4f_SUgglmv220W1FHUxn6R5tew8QpckW1TTsWVUJdZfVC4SlxjWCJ8VYa9l3yZqFg6zDj04YqMMIfVPHcrUScjEknpzejZIZNvsp0MG0oPbOlzW9QMRKdrJH2ItUDr4RuuTUpmAE0HqPiF6JXDCB1ISf7gmJ2v_jh03tkkAdg67_tyN0xFedsLV6iR9xoF6OubUfNol_Kmqocixuc0hQFgs20BSig1b3OHOlyjbUczMjPs5UZ1FCfG-_sVn8zVvQnz_BKbykqqcMgk-e3FYdW-0JaaQL-J2ifGA9pooX3W0Dz8qZkc1FktziYCDGUg7c2LZZNBmQNCd06C6KepYIW64K3g_7h6vszrsqVXqM80eU6WUliT2Qq18gaSlXUTXrLcs24hDGBClKPtomfXFHFpBZjX4GbEn3zkoWmlCriCyHSDgIR82jMwD9xC-k2y0sw2o_5qyRxFhoIr7AefCO5q_l5uDorudcoXX5CuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رانش عجیب زمین در هند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130801" target="_blank">📅 10:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130800">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
تحلیل جدید خوش چشم، کارشناس صداوسیما: ترامپ تنها به دنبال باز کردن تنگه هرمز است
🔴
من ندیدم کسی به این موضوع اشاره کند؛ مذاکره‌کنندگان هم به این موضوع توجه ندارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130800" target="_blank">📅 10:37 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
