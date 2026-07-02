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
<img src="https://cdn4.telesco.pe/file/TOn3M6IjdpmkKHQ0QjtKns5ZMTMuCx2PponC68cHUk_vsqGpCYCiHB5BMvpH7pWxysMaHCbybOfYYK5yFBUSogP8-LoeUIuH_nxYdUvZfW3yg7x_IMowagBGDHqP2FnQ2Od5RE5wxObDOSdalcyCarG-xsh7J1iCBmhYoH5lMqXLJdGTKNGTZm8D68YUAHTrKoNC-RyyURgXIoRB-YiCpWYRhktO4DWRqOWujyYuwK1QF_Z3ZxUcCXeoOp5LLBuZoJkpccDcL8XOS89XsendHetu3OftIeeBigA20WfhgvHz-DyHs7MqfXDvFjaT_F3r61Vea7QPiCFVlcZbkDUYLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.12M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 15:33:43</div>
<hr>

<div class="tg-post" id="msg-665616">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZWhvECcYJQc9pKpizEiapKueOf3f0LBUYAbAkX4LMi-UxEtU-pjR8Sa80EwXNHJCchlTXQfOGOXY3ziLExgHrJs1lyTiw7lVtvaBgKJisAiq63tbrFw2TkGKm5l6-z_W3xVPLJ2c_Sl2_CCJZYlbcWRLB1a8I2zINoqybzYBoA_xWIxrmJUvb4urhPpiO8wDEhqWWeUJbcavuxQ4XqkYdoWnrtE3V0YodMqg59iIKZiy-TXjzlvDk68tWKB159EpxTv-7h355HZbE0bRDckeWQAMVUKLff7CMMovcprn0jKRhgQ2FuniN6FUB73ve29MOqOy9kPjHt-B9EDnwtlSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم ملی کشتی فرنگی جوانان ایران قهرمان اسیا شد
🔹
تیم ملی کشتی فرنگی جوانان ایران عنوان قهرمانی زودهنگام رقابت های آسیایی تایلند را از آن خود کرد. در جریان رقابت‌های ۵ وزن نخست کشتی فرنگی قهرمانی آسیا در تایلند، نمایندگان ایران صاحب ۳ مدال طلا و ۲ برنز شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24 · <a href="https://t.me/akhbarefori/665616" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665615">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
اطلاعیه شماره ۲ قرارگاه برگزاری آیین وداع و تشکیل قاعده عظیم شان شهید امت( تهران )
🔹
هموطنان عزیز تا حد امکان برنامه سفر خود به تهران را به گونه‌ای مدیریت کنند که از حداکثر ظرفیت اسکان و ارائه خدمات به زائرین در تهران استفاده شود به عنوان مثال سفر را کوتاه کنند تا تعداد بیشتری از مشتاقان شرکت در مراسم بتوانند حضور پیدا کنند
🔹
مبادی و جاده‌های ورودی به پایتخت همواره باز است و هیچگونه منعی برای ورود وجود ندارد
🔹
زائران گرامی اخبار و اطلاعیه‌ها را از مراجع رسمی پیگیری کنند و به ویژه مراقب شایعات و اخبار جعلی باشند.
🔹
پیش‌بینی و توجه به محدودیت‌های ترافیکی در سطح شهر تهران و حفظ آرامش در هنگام حرکت همواره توصیه می‌شود تا برنامه‌ریزی حضور هم وطنان دچار اختلال نگردد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/akhbarefori/665615" target="_blank">📅 15:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665614">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3ClRF-hEi_gt82dWu7KZ8ESRszrR7eNInkmfTwkLe1gFJa6J5TwBjYgUfUNGvk3idkwJKPpvOv0bOZutpvC8bAiY2JecfY6mhAkM3LTOwCTx_Y6LLwWfvPVfEJb9QYYhA091eToDkAXFeSBvZprM-GfVe1GteKO7F5eNkWXavZP4WjCtJFG4KO4Wfl57ZCaSSTWBg83F93Uy0MG2tk-VmyWloC1OFhYj5kCOLoELGrB1j0KCVhvI6gDN6lf0gq4w5_OhhSOEF1dxgtZNM34rsJgG-48gxRTeeqgaZzh0pby9139OMfhebsvp-t80X3zpqsxMiB88EsejO5WKtziHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبور نفتکش‌ها از کریدور عمانی- آمریکایی با سامانه شناسایی روشن
موسسه تحقیقاتی HFI:
🔹
اسکورت آشکار کشتی‌ها تحت حفاظت آمریکا در حال انجام است. در این مدت، ۴ نفتکش غول‌پیکر (VLCC) با سامانه شناسایی خودکار روشن وارد تنگه شدند.
🔹
در سمت ایران، ورود نفتکش‌ها به مقصد بنادر ایران همچنان محدود است. تاکنون هیچ‌گونه تشدید تنشی از سوی سپاه پاسداران انقلاب اسلامی رخ نداده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/akhbarefori/665614" target="_blank">📅 15:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665613">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت
وزارت امور خارجه پاکستان:
🔹
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند. زمان برگزاری نشست بعدی در اولین فرصت پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/akhbarefori/665613" target="_blank">📅 15:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665611">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d3ad0855.mp4?token=Da0UkATK1mkhZ-SxsYmZ7igrrEJTJmKWo4z7auuzP2Qn5UFzfLmw_MicO-hy4-9hZj_CM1iRRXoQBHLDrTh_M1ykJ8Huz62V3TeDWwwTuW80RDNzTWoX-0DH9cu2dhVrXZzLPeprk0WX3y9N2xl9syaVpPWn-Qs7A37DsdanVY1b6R4iPURYq0sP03WjPhDljymk_0fCeYU2RukdbdE_Dc-Ai3R7H3yjaqG5smd9huoXBqI7VEsMURg5IiCmfj9Yn5_uuJ2JgCXNvN5EoxgKmtVaI0tFDSdJAZYyQlu3rN8GEcXdzEuR_LjO9qFrt6m90qmU3A_TRqc4FYMS4TonV3QYfQbz9c3oFBglIVhcT1yJsdJWzV1wYJbbzA_CuWwaIUMOqpm5DKDZ5KZSW7I5nQ4FuUekGkIWJVWXUfIz2CAtUi5fgfn5aT0D2Az5aK2RfPA-c3emN33mqg_Z377rtr-SchZfcq4CDZ91dd7eq8jnaA0DNxdLUnAuH-dp21dWx39YxvDeYY1WiK7M1AU8Iof9DaFfG4l663D0_gV3GGIhhNSEmHjI6hX5rNZT-RW57cD2vOSz-6fE7o_bPPHnRUO-_57GSdVgT149tt2uA3JUg5cSM0kvVm1i_uUNzGNhGV-Gz7dmfjDDe23Ai5be6s5Dv9FqTPmQxFI4K-csoRU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d3ad0855.mp4?token=Da0UkATK1mkhZ-SxsYmZ7igrrEJTJmKWo4z7auuzP2Qn5UFzfLmw_MicO-hy4-9hZj_CM1iRRXoQBHLDrTh_M1ykJ8Huz62V3TeDWwwTuW80RDNzTWoX-0DH9cu2dhVrXZzLPeprk0WX3y9N2xl9syaVpPWn-Qs7A37DsdanVY1b6R4iPURYq0sP03WjPhDljymk_0fCeYU2RukdbdE_Dc-Ai3R7H3yjaqG5smd9huoXBqI7VEsMURg5IiCmfj9Yn5_uuJ2JgCXNvN5EoxgKmtVaI0tFDSdJAZYyQlu3rN8GEcXdzEuR_LjO9qFrt6m90qmU3A_TRqc4FYMS4TonV3QYfQbz9c3oFBglIVhcT1yJsdJWzV1wYJbbzA_CuWwaIUMOqpm5DKDZ5KZSW7I5nQ4FuUekGkIWJVWXUfIz2CAtUi5fgfn5aT0D2Az5aK2RfPA-c3emN33mqg_Z377rtr-SchZfcq4CDZ91dd7eq8jnaA0DNxdLUnAuH-dp21dWx39YxvDeYY1WiK7M1AU8Iof9DaFfG4l663D0_gV3GGIhhNSEmHjI6hX5rNZT-RW57cD2vOSz-6fE7o_bPPHnRUO-_57GSdVgT149tt2uA3JUg5cSM0kvVm1i_uUNzGNhGV-Gz7dmfjDDe23Ai5be6s5Dv9FqTPmQxFI4K-csoRU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هجوم فرانسوی‌ها بر تهیه پنکه و دستگاه‌های تهویه
🔹
مردم فرانسه به دلیل گرمای شدید برای خرید پنکه و دستگاه‌های تهویه مطبوع به فروشگاه‌ها هجوم بردند. فروشگاه لیدل پاریس به میدان نبردی بر سر پنکه و دستگاه‌های تهویه مطبوع تبدیل شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/akhbarefori/665611" target="_blank">📅 15:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665610">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dl7JhEYsXGedy1mKQkD6MC_sm2tvYwdgFuWCt_6azQxgy1SOGmvmpi4HkQQK3_PV18IPrS3VxRhur4kGImlzjgzW7Jx3YPNw5_6F-ITZsPk5qbG-ooPdlaxYelhYMdwkVgt73siHRykUuQRWTu1DGOo0ANPkiP-CIRDASbN_CBCWDRlaHoeDpvN95oLh1FCWOtrO01qlQn71fnpa8br8VRVNrk8b8HUDSMkiNfpp8D1fprFa91d_s5aJcXtHdQB4Bvg0QBRjpUvQrOaB-xhZvG1PEB5S3Chvm3YH0qI-0Z32jNlajCOyB2_kvdX9LEF-RNQkQDZ7khgUwsYbGxqG1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تفکیک زباله از مبدأ؛ اولین گام برای ساختن شهری پاک  شما هم به این پویش بپیوندید
👇
#نه_به_پلاستیک @Ertebat_baforii</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/akhbarefori/665610" target="_blank">📅 15:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665609">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfpH6oy_dHKcZuis4vjyXVvctfGNNJxp2CtIEc-RvxmJdVzI0hWaoYo7_rcEBFVowx9I463jOstPGsBqBjpv5zXU4-NydKP6Lk2b3J4-U42JP1Mm640XnzYMlZ7HCJaLeU8WQAVqs9myFDh3SujArRWmf--f0IgkEc0Dql54bgilKoqE2CehbK_7yKJ8ZYy0Bd_MRi9AJ0S8LKT5zK1Q3xo_mBf4wv7y_foaWyvbgLl5NJDi9S1VA8LekAvQQ-mzIVVnbXa71GvJpwlLmDqRxrv6zZrWmchgCjpU-XCe532PZYzQgJ2bW3YpYIVcqfo-VRa6P1Bs40_rFZi_oP04Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پست مهدی طارمی در واکنش به حذف ایران از جام جهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/665609" target="_blank">📅 14:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665608">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بانک قرض الحسنه مهر ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONagQjOwUWsd_rd5gKS2wFnmgvp5mZK1unyWu-VJ9hKJS2GBfD_ob0tJlJRxvQjbSZOq2Je4XJ7cJAN4kSxowXozuJlCU1uKQWe0KHIiKUvVdGeasfU48TZJ4_mjNqtkYMKgLIIiVrdMHHomhWzvktrngvl7Nuz2bAZn9dGsbBNosqUmdUyiCIPpBkLmEp6dk1-jM4nrwQnXSwYFCh5tANZdR2A3sNU1fyDVVBDtPuitq4n0xdRP68rRbNZplvQ_wsa-rdsMtz7vYeKjGLxdZ3jt-OokV0EzRDrDrWe2Q73YJyjlXhDL3EBYpu3VZpmPryUmRAOZ3m5GtiTx4VbXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔹
🔸
🔹
🔸
با حضور متخصصان اکوسیستم نوآوری و به همت بانک مهر ایران
🔰
نخستین رویداد کیوتاک با موضوع تجارت اجتماعی برگزار می‌شود
🔸
سلسله نشست‌های کیوتاک به همت بانک قرض‌الحسنه مهر ایران آغاز شد و نخستین رویداد، روز پنجشنبه ۲۵ تیر ماه از ساعت ۹ تا ۱۵ با حضور متخصصان اکوسیستم نوآوری و بانکی برگزار می‌شود.
🔸
موضوع نشست نخست، تجارت اجتماعی و شبکه بانکی است و در این نشست راهکارهای نوین بانکی در توسعه اکوسیستم تجارت اجتماعی بررسی می‌شود.
🔸
بررسی وضعیت تجارت اجتماعی در ایران، ابزارهای پرداخت نوین در تجارت اجتماعی، تجربیات جهانی و مطالعات موردی و چالش‌های پذیرش ابزارهای پرداخت از جمله محورهای این رویداد است.
جزئیات خبر...
🔸
🔹
🔸
🔹
🔸
🆔
@mehreiran_bank</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/665608" target="_blank">📅 14:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665607">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
خون شهدا با پول شسته نمی‌شود/ ایستاده‌ایم هم برای قصاص، هم برای انتقام
دکتر محسن خاکی، استاد حوزه و دانشگاه:
🔹
ایرانی شیعه‌ قدرتمند امروز خون رهبر شهید را فراموش نخواهد کرد. خون ماکان نصیری و سعید زارعی افسر ناو گروه دنا و خون رهبر قیمت ندارد.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/665607" target="_blank">📅 14:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665606">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdtQnjoq--7nPbyZ9j42XAiwkQf1mdOr8HCmecOawe8oAXFU4UaSasTOHOACupl2tF7P00sPWYZzC_TU6ImCjg6oR14ksLmfB7tMkri82_fileHq7RcV0SQx3g9mlkxUPfqWAkL0v5fTCMLUXdU7nvsxQFjB2tjaa8ouNQMHT5WVIK0PP7Wzb5TUiQIn-QbSGljjNRiVlPcn2FOMr9Zog8_FU285EDCGqHkWLhgVSFIIh0VrfegJKo74OL4r_uk22iIKmoJI2KqgWHzGCamdvfkLX3TB9-zZiCDtHQnaWs51N8qls9dVWyKzKzQe42G1Jm6OP5Dx6K-6W9IGPzrqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
سوگواره بدرقه یار
▪️
علاقه‌مندان به بخش
عکس
سوگواره «بدرقه یار» می‌توانند پس از مطالعه آیین‌نامه، آثار خود را از طریق لینک زیر ثبت و ارسال کنند. در صورت عدم امکان ثبت از طریق سامانه، ارسال آثار به شناسه رسمی دبیرخانه نیز امکان‌پذیر است.
#بدرقه_یار
▪️
لینک ثبت آثار:
https://survey.porsline.ir/s/aU5VZuaW
▪️
شناسه دبیرخانه:
@Badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/665606" target="_blank">📅 14:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665605">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDuvOJsjiZMa2RUtkN9h4BWHpID8zl4wkMpwUpSFcIJWTOWkb2Udm17W7iWbUiN7CiTdOy7LEShgBRFkyMUz9KnGtZP0HTmeEkcfAaO2kZEgkvaO8alohPS8UXiGXDgDG5nCP1NebBPCq0VKqPOURlflKs4fqMTrO7114qsjFUz2LapXW0xuq9k9JIaSDz3KAOoYLZBEcTyOceWfopFzeZ1Y81A6id5ecRl0rHRRC9VnOaGK3-kl6dNvBUszeutsT74LscOaENQs_uFGIEJ1Pnrk3_oU6l6B8Y-fMwCMBhi6TByN0LbJAI-G6b3Y8BWPJny_6p4u7qXH6w9t1eIMYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
واکنش بلاگر معروف کره‌ای به مراسم بدرقه رهبر شهید انقلاب
قهرمان هرگز نمی‌میرد
🔹
«داود کیم» (جیهان)، بلاگر شناخته‌ شده کره‌ای، استوری ادیورز ویژه‌ای را به مناسبت مراسم تشییع رهبر انقلاب منتشر کرد.
🔹
این چهره بین‌المللی که سال گذشته با انتشار ادیورز پربازدید «قهرمان» (HERO) در ایام عاشورا توجه جهانیان را جلب کرده بود، حالا در جریان این مراسم تاریخی، بار دیگر با اقدامی رسانه‌ای ادای احترام خود را به نمایش گذاشت.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/665605" target="_blank">📅 14:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665604">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
جزئیات تشییع پیکر رهبر شهید در نجف و کربلا
اباذری ، رایزن فرهنگی ایران در عراق:
🔹
پیکر مطهر رهبر شهید شامگاه سه‌شنبه ۱۶ تیر وارد فرودگاه نجف خواهد شد و پس از مراسم استقبال رسمی با حضور مقامات عراق، صبح چهارشنبه ۱۷ تیر از ساعت ۶ صبح در نجف (از مسیر کوفه به‌سمت میدان ثورة‌العشرین) و عصر همان‌روز از ساعت ۱۶ در کربلا (از خیابان ابومهدی المهندس به‌سمت بین‌الحرمین) تشییع می‌شود.
🔹
طواف پیکر مطهر در حرم‌های امیرالمؤمنین(ع)، امام حسین(ع) و حضرت عباس(ع) و برگزاری آیین‌های معنوی نیز پیش‌بینی‌شده است.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/665604" target="_blank">📅 14:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665603">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه نیکوکاری مهرآفرین پناه عصر</strong></div>
<div class="tg-text">📹
محمدمتین تنها ۱۸ ماه دارد.
خشونت، سلامتی او را گرفت و امروز برای ادامه درمان و توانبخشی، به همراهی ما نیاز دارد. مهرآفرین تاکنون در کنار او بوده، اما مسیر درمانش هنوز ادامه دارد.
❤️
پنجشنبه مهرورزی این هفته، برای درمان کودکانی است که قربانی خشونت و کودک‌آزاری شده‌اند.
🌿
نگذاریم فقر، فرصت درمانشان را هم بگیرد.
💳
6104337737614782
💳
6037707000289144
💳
6037707000426027
🔖
IR 180120000000001264298063
📞
*780*35260#
🔻
پرداخت مستقیم
Mehrafarincharity.com
🤍
عزیزانی که مایل‌اند به‌صورت مستقیم به محمدمتین کمک کنند، در واتساپ یا تلگرام به شماره زیر پیام بگذارند:
📲
+989101785282
⭐️
مهرآفرین باشیم
|
اینستاگرام
|
وب سایت
|
پرداخت آنلاین
|
❤️
@mehrafarincharity</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/665603" target="_blank">📅 14:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665602">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
کارت امید مادر از فردا شارژ می شود
معاون رفاه و امور اقتصادی وزارت تعاون، کار و رفاه اجتماعی:
🔹
مادرانی که در فروردین و اردیبهشت‌ماه صاحب فرزند شده، اما اعتباری دریافت نکرده بودند، از فردا اعتبار معوقه آنها به صورت یکجا قابل برداشت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/665602" target="_blank">📅 14:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665601">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iURQGwXXqTxYguNTkJX27bkB-RMTlTG6iq2Tx6-RGYRvySH5EwP0XL_xFxGZUp2gNi-PM0fdjgwp08N3QHDjvJqP31ZIELPkFViqdxi-lRpw3FHFLCdL94R9mkPs1X1E9JLvwxaDs3LDUVofMdJuwk0bUDjIvpjI049F2hwuAwk-Dq3IaW1A1JHV_OHfEW13FLQN7mPx8El7HjJLHsmOS9-tygDijHfhXXPlZIKAZGvLOyKDQAhc9YU1duujTlS9qLWt_7eyBFb4muq5PWV2rlTDdH3QNFWYvM2fCEQt_-9t3b3IcgOdm08GmZIRKwyN0nCYNMU7y7_vMUbpcz6P9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای جامع مسیرهای ورودی، پارکینگ‌ها و دسترسی به مراسم وداع در مصلای تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/665601" target="_blank">📅 14:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665600">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
استاندار تهران: کودکان، سالمندان و افراد دارای بیماری زمینه‌ای در روزهای وداع و تشییع در کانون‌های فشرده جمعیتی حضور پیدا نکنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/665600" target="_blank">📅 14:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665599">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/28f1f15dd1.mp4?token=N3GbpLq9R3EbY7HcYFfcAfY_zHnKkOAiq5VdJbi-0lpdBA44MN-0L2D6PZBv9bWmmegPNx3DE5HX-IwSzWr0iEsgXcQ_Qm_L48F9H1IoPmcJRX5lWUkzsx5p4aLlO4HbMexIurgsYpBTZTx-YFFqboN8GNQbG1RDgNzMIEm0S0mpQPy4tojWMNhG3Gkg9zcgVMf9M65Ncw9cYOEBxy3lBn1x9x1TGoGs7BAKYlPc-r2hvc9RzwfeUDAGORwxrTpwhedcHdV251eG7AeTelMJ0PrVaTFWk08MfDxKU5eGbuI2wRk-vPBrUvDxI-NIlW-sbCJHiyr0dLNUxFVmhrxP4oaFGZuADQtPO1J16fz4Vhv5vzAsZGRwOvRB986R5eznIrBT69dGyaZdMKOhNuwgjG0nUm-L_iCzaJdjoDd1beTLxCAOnU4RKyNlWuNGQZ-fvaPx3NwconMjdJg6o4lW_BCWXrq14GFg3q0WNfAZP5Q8e6-PVv3fNDzEf0cjAnAYxv5jxRV_Qlacpk0-px3RxXs56qGueA63C5qe2fo5zZVHbuMAmcBvXh9YyNwv4l-3jk92mtyMHwfGGCOgZ_UUOk381BWw8p8CUwinH8hT__32REBRrGPf8nYq6HcTcvNeqDH73mkGr8qCtQ0OedaKnifPT6njnwTs8Uf2bT4_o1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/28f1f15dd1.mp4?token=N3GbpLq9R3EbY7HcYFfcAfY_zHnKkOAiq5VdJbi-0lpdBA44MN-0L2D6PZBv9bWmmegPNx3DE5HX-IwSzWr0iEsgXcQ_Qm_L48F9H1IoPmcJRX5lWUkzsx5p4aLlO4HbMexIurgsYpBTZTx-YFFqboN8GNQbG1RDgNzMIEm0S0mpQPy4tojWMNhG3Gkg9zcgVMf9M65Ncw9cYOEBxy3lBn1x9x1TGoGs7BAKYlPc-r2hvc9RzwfeUDAGORwxrTpwhedcHdV251eG7AeTelMJ0PrVaTFWk08MfDxKU5eGbuI2wRk-vPBrUvDxI-NIlW-sbCJHiyr0dLNUxFVmhrxP4oaFGZuADQtPO1J16fz4Vhv5vzAsZGRwOvRB986R5eznIrBT69dGyaZdMKOhNuwgjG0nUm-L_iCzaJdjoDd1beTLxCAOnU4RKyNlWuNGQZ-fvaPx3NwconMjdJg6o4lW_BCWXrq14GFg3q0WNfAZP5Q8e6-PVv3fNDzEf0cjAnAYxv5jxRV_Qlacpk0-px3RxXs56qGueA63C5qe2fo5zZVHbuMAmcBvXh9YyNwv4l-3jk92mtyMHwfGGCOgZ_UUOk381BWw8p8CUwinH8hT__32REBRrGPf8nYq6HcTcvNeqDH73mkGr8qCtQ0OedaKnifPT6njnwTs8Uf2bT4_o1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به ما اطلاع دادند که شهید کمال خرازی ترور بیولوژیک شده بود
صادق خرازی برادرزاده شهید کمال خرازی:
🔹
دکتر خرازی دو بار شهید شد!
🔹
من منکر تلاش‌های برادرمان آقای ظفرقندی نیستم، چند بار بالای سر شهید خرازی حاضر شد، آقای پزشکیان دستور مستقیم می‌داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/665599" target="_blank">📅 14:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665598">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyDd61n3oNWC3fYvD3_W-xUx691slzmPXm2BxO9nq5oKko8rJWEEc4A84PQp7OuSD2H13F7hUzS_scYw0r8B73vitwJ6eLmkB0wCyWUInIUEAmZdKOgXQfqg6yxoOzZDPu2fi_9-rldYjzXTm2BflvhL70zFTiiIjvzjjaGb5GxbM5KpCLalSB9iQ33QgnBK-os4ZgYOricesNILI1fL7042qiGU0M9SDnbsfwgClrzNxuEhlazI-91rkfZU48Pm734WJFONrQv2WcM-dteBkwacHN0msfkHGU1Vo0KcZKSG0pfBkEQb6BScwUkJF1QeR4USV4imNuziHBzgv_LSZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطعی برق؛ هزینه ای که مردم می‌پردازند  #برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/665598" target="_blank">📅 14:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665597">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGWAJKVFCIW1RopgjHOWCvxhiB2eb1Hm6KO61kWzLKGSbPzTem2FNQZzUjipIhEqqZ3w8TIPalX_JLCkQQlPHBAxQaATZ9z9J4R0woKeXuxmR6lhycWpKL0iVtI3VPpYT8Sx3c1N4LfwTRXzgnlCuP6Dzq5O7BCqn_qSGvJFR9PBtP-ah6Rk3rbhtfsRxRL1rbWUrJsc_46_5rAdr3bD-E5_oM4S-KSYyCR0U3ZUN95dgy5T1COKgWJhNa8BHHQp6bOrRGYIFrTkOowL4G9GocdSK8jwN8JUbE3SiBdrQJqU_5rlNKS_YQX1soUf6HSN8493ZHSfN_PURwBfzed8xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | کمپین «جامانده»
🔹
اگر به هر دلیل امکان حضور در مراسم تشییع را ندارید و میخواهید در این مراسم حضور داشته باشید، یک فایل صوتی حداکثر ۱۵ ثانیه‌ای برای خبرفوری ارسال کنید تا یک همراهِ قلبی به نیابت از شما در مراسم شرکت کند.
🔹
در پیام صوتی، فقط نام خود، نام شهر محل سکونت و جمله‌ای کوتاه درباره همراهی و ادای احترام خود را بیان کنید.
🔹
منتخبی از پیام‌های صوتی ارسالی با عنوان «جامانده» در خبرفوری منتشر خواهد شد.
#بدرقه_یار
🔸
ویس خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/665597" target="_blank">📅 14:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665596">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAQ56V3znDLlP2yrHqn1zQCqf0AAWW8eGX9flGhWoQlwDB_m3He4ldV__y-9YTgn5F3kjt4eUYpsvA7wDp2JV_FXLKC6fnYRVPCKqerpk8jZzUqxqd864Tk2wLdC_CwB7G-7LBkjyZfwW0Xf_1KdFLag2z5aarAPIGvXYq9aUeuWn1s2HWDcw3nE4agUvxHGjjC82uexXceaFvrsZYcxNsk5SyUi2lwpTkwK1JRi-MkD21gLNM9Xl1cliEvCG1efjAn50B-OUO4VBdgGeyXKjYEPX3FZFA72qqnAA36MqGAjuxDYfOJo3YAXt2M4FZZ0z-pJDQ_RWIlMQvq2CkpDQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهترین گزینه‌ها برای یک سفر ۳ روزه در ایران
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/665596" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665595">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وهفتم از فصل چهارم
🔹
در این قسمت ادامه روایت تجربه‌ نزدیک به مرگ خانم زهره ابراهیمی را که بعد از ورود به برزخ و دیدار و درک جایگاه خویشاوندان و حتی جنینی که خواهر ایشان محسوب می‌شد؛ به دلیل داشتن فرزند از خداوند بازگشت به دنیا را طلب می‌کنند و با عبور از میان اجرام آسمانی و درک زیبایی‌های بی‌نظیر آنها به جسم باز می‌گردد ولی از بازگشت پشیمان و دلگیر می‌شوند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: زهره ابراهیمی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/665595" target="_blank">📅 14:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665594">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXVE49f5lmNiL2MbGzoeWt8R6myWq4g3a0zfz6DZ2A877sh5-JzCvg2xmdEPxAOKtRiiStOQBOJwVUCw0Qj_8GiwlMOgVTCDk8PZlf2aEqGrS5lg-PWwkDIYY8wP0h7EIQQcCQIATfAUrKhtwV575lJUWdeo6Ln6n8y1Lz6AwbjTokcHMuRJi9-HLRS9LPa6FUEvI0pmkBTdChcMmKjsA9eNEh3iDxxKurpAni_HQNhY82ypRk0tLdCIZ-SrxVmyRk1i3FQKxgcr6W-h2FqUkpJB1Qpm1WAg2X47Od1JRIAZffl1X-cWT0Rf6k0oV2QJ4d7V3ekaJxtShUq3XOwZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسارت ۳۰۰ میلیون دلاری به شرکت‌های دانش‌بنیان
🔹
برآورد اولیه خسارت واردشده به شرکت‌های دانش‌بنیان حدود ۳۰۰ میلیون دلار اعلام شد.
🔹
بازسازی شرکت‌های آسیب‌دیده در ۳ مرحله و با تأمین تسهیلات دولتی انجام خواهد شد.
@amarfact</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/665594" target="_blank">📅 13:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665593">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
استاندار تهران: کودکان، سالمندان و افراد دارای بیماری زمینه‌ای در روزهای وداع و تشییع در کانون‌های فشرده جمعیتی حضور پیدا نکنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/665593" target="_blank">📅 13:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665592">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
الحدث به نقل از منبع آگاه از مذاکرات دوحه: آمریکا به ایران گفته که پیشرفت در پرونده دارایی‌های مسدود شده، منوط به پایبندی کامل تهران به یادداشت تفاهم است و تغییر در وضعیت تنگه هرمز، نقض تفاهمات تلقی می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/665592" target="_blank">📅 13:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665591">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e472a6477.mp4?token=DCu-ZEaw9U3ZskN0Wp4dNa97XuRHcmH6lcHJXEP-hnx0NHvSv9FGKtnw1GkJDrBNJ3yxk0xEpK1S30BmJeHedIIAqB6MDq4weR93Af-f60VbXeykvlYqAybQBYQ9fy_QCC2c9yGAix3KXSaF-3Fky9D6KgjAUzfisbPWxwFh2Cbla9BhhS_QIeuXJwl4LA6_HE6ZHSZRqVeM9KrlSXNjP9yNw0P5nUjUBi1Ko66QhYLThXHZeomk9iau5G4sHTkeCWfniXEcB4wbF1sa1BNOirK9oEtXX9PwVfyOwwgSHMALfETqSC_ToJzJLtr-XbXO6O7hg-4RxFaKLtwSHvske41MqK0ToRPf7B7JrMTSQaaow7acNAIiyJd-ed445vashUkVVFACodZir75TWMtOjE2Iu9ZixrqZBCvDcqEtHk2wyMMxLoTD3WUPr8jGlc_narre3hsPEwC32uQG7fOhTJFl-XUQEuQGHtn2PNjj799cv5E9qCAbURZR2UpDgmWWpKPGkLzV914BYD0Ahzr8y9KHRfOkUbnUZ4peeacqoIANHtqG9EPTSVJ0Rx9khnFd9VQ7rykpyyGOhHz7-5Y6Avcbz6XBdbsevpXYn4qYZfJ1BwXifkiH1l50U7FX5kR0As9-cUH0rLyG17KqAZ1mxavT7SC3gB2vwGg4YYEelXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e472a6477.mp4?token=DCu-ZEaw9U3ZskN0Wp4dNa97XuRHcmH6lcHJXEP-hnx0NHvSv9FGKtnw1GkJDrBNJ3yxk0xEpK1S30BmJeHedIIAqB6MDq4weR93Af-f60VbXeykvlYqAybQBYQ9fy_QCC2c9yGAix3KXSaF-3Fky9D6KgjAUzfisbPWxwFh2Cbla9BhhS_QIeuXJwl4LA6_HE6ZHSZRqVeM9KrlSXNjP9yNw0P5nUjUBi1Ko66QhYLThXHZeomk9iau5G4sHTkeCWfniXEcB4wbF1sa1BNOirK9oEtXX9PwVfyOwwgSHMALfETqSC_ToJzJLtr-XbXO6O7hg-4RxFaKLtwSHvske41MqK0ToRPf7B7JrMTSQaaow7acNAIiyJd-ed445vashUkVVFACodZir75TWMtOjE2Iu9ZixrqZBCvDcqEtHk2wyMMxLoTD3WUPr8jGlc_narre3hsPEwC32uQG7fOhTJFl-XUQEuQGHtn2PNjj799cv5E9qCAbURZR2UpDgmWWpKPGkLzV914BYD0Ahzr8y9KHRfOkUbnUZ4peeacqoIANHtqG9EPTSVJ0Rx9khnFd9VQ7rykpyyGOhHz7-5Y6Avcbz6XBdbsevpXYn4qYZfJ1BwXifkiH1l50U7FX5kR0As9-cUH0rLyG17KqAZ1mxavT7SC3gB2vwGg4YYEelXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان چفیه‌ رهبری
🔹
خانمی‌ که رهبری را قبول نداشت اما حالا میزبان و خادم زائران و وداع کنندگان با رهبر شهید است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/665591" target="_blank">📅 13:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665590">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
استاندار تهران: اینترنت قطع نمی‌شود
معتمدیان، استاندار تهران:
🔹
هیچ برنامه‌ای برای قطع یا محدودسازی اینترنت وجود ندارد. با توجه به حضور گسترده جمعیت، ظرفیت شبکه ارتباطی و اینترنت در مناطق برگزاری مراسم تقویت می‌شود تا مردم با مشکل ارتباطی مواجه نشوند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/665590" target="_blank">📅 13:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665589">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7d3be04f.mp4?token=dDU9VlEUJZis7pMhj7txvQV37kv57DH7nEqb05KB5BdtID6Mc5byr-bwEyC3Q0QOQqAS8zJAoJLqc07jeeGUCtEXPjbv1dLh8VY2T8Idr4tMGS5ME3CeZrjGy0BGXUrPYrpVoQ4lWPyLZ3unvluOMnPuDLfFOjlDFWaEqtPHQN26RfwiA4jXEjdmXj_O8zaVPdISDw3xdFyVtPKFPMNcOxgSbu_JF3U53Pr5oq6hvig6DolILxswDdJC0UAnh9copccgBRBtImz_Nxpf_o67evkU2vj6UNMuoZyMx9lCICxnjtEIJKnpjvo73LuVt9Y_9qZNQ2tcGD5dhkRqPBO0xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7d3be04f.mp4?token=dDU9VlEUJZis7pMhj7txvQV37kv57DH7nEqb05KB5BdtID6Mc5byr-bwEyC3Q0QOQqAS8zJAoJLqc07jeeGUCtEXPjbv1dLh8VY2T8Idr4tMGS5ME3CeZrjGy0BGXUrPYrpVoQ4lWPyLZ3unvluOMnPuDLfFOjlDFWaEqtPHQN26RfwiA4jXEjdmXj_O8zaVPdISDw3xdFyVtPKFPMNcOxgSbu_JF3U53Pr5oq6hvig6DolILxswDdJC0UAnh9copccgBRBtImz_Nxpf_o67evkU2vj6UNMuoZyMx9lCICxnjtEIJKnpjvo73LuVt9Y_9qZNQ2tcGD5dhkRqPBO0xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محله به محله خود را آماده میزبانی از مهمانان رهبر شهید می‌کنند
🔹
سهم ما در میزبانی از زائران و وداع کنندگان با رهبر شهید چیست؟
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/665589" target="_blank">📅 13:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665588">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
سخنگوی ارتش: مذاکره جنگ در سنگری دیگر است
سخنگوی ارتش:
🔹
دست ما بر روی ماشه، چشم ما به روی دشمن و گوش ما به فرمان فرمانده معظم کل قوا است؛ هر لحظه اراده کنند وارد جنگ با دشمنان خواهیم شد.
🔹
مذاکرات کار مسئولان سیاسی است. آنان وظایف خود را دنبال می‌کنند.
🔹
مذاکره جنگ در سنگری دیگر است.
🔹
در تأمین امنیت مشکلی نداریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/665588" target="_blank">📅 13:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665587">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyENBaQkUf5z1LROTBFPLF7UmLS9Q5qbiDl4ciQf557gEZLgv_bkv2FrzIhnjTmmwtqw9JpTsFWp7GcuJiLtY3jlDiwqdefncgyC2iYlsrUnrqeZr8kEhjosY0fwTEKYqxY3c2st6m4N_kxY_u5CxucbbzJ7nwFsVrd3Aupxp9XiB4HjI7zTyypt5mTd8xk-_jRAz4KQZYC1rsqnzj4wcT97IzkmQnEAE5_OeW5uk_jnRImttOc3xpRy47RTHr2Pmu2bFmS4VFsNatss7VFv6sVIGBzxCfGG2iOtC8NW-U78Hmsz5Jd0sD4Z3kOqLnnSsUCe8UW-hCZzCnDfQIP8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قتل دختر شایسته ایران در ۷۲ سالگی/ قاتل ریتا جبلی در ارومیه کارمند بانک است
🔹
پس از انتشار خبر قتل یک زن ۷۳ ساله در ارومیه و اعلام دستگیری قاتل از سوی پلیس، اکنون جزئیات تازه‌ای درباره هویت مقتول و انگیزه این جنایت منتشر شده است.
🔹
هرچند بخشی از این اطلاعات در صفحات غیررسمی شبکه‌های اجتماعی منتشر شده و هنوز به تأیید رسمی نرسیده است.
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/665587" target="_blank">📅 13:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665586">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
برنامه‌های رسمی مراسم وداع و تشییع رهبر شهید از شنبه در تهران
استاندار تهران:
🔹
برنامه‌های رسمی مراسم وداع و تشییع رهبر شهید از روز شنبه در تهران آغاز می‌شود و پایتخت میزبان زائران از سراسر کشور خواهد بود.
🔹
مراسم اصلی در روز دوشنبه ۱۵ تیر برگزار خواهد شد. تمهیدات گسترده برای ساماندهی حضور جمعیت انجام شده است.
🔹
امنیت کامل مراسم با مشارکت نیروهای نظامی، انتظامی و امنیتی تأمین شده و زیرساخت‌های تهران تقویت شده است.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/665586" target="_blank">📅 13:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665585">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMD3v0xqCc_GfTgbspM7-WL2w_c-G52zZ90gZ3tjteibsegQzT8RYs2MUZ3Mwdx8oNQdnOEkyZpi8CRL1-7qv5Qzh6T4KcFhFuCz0hnEBM8IjZg_NzeAVBeEeFNp2vzwln7nnj_0k9f1GOOCYAm7q6IUQfYIKBB1Eq8Xv4GANZQv9KpzLmw3P3qsc-dsObfjHd6ANvRJHWX83LsmvPlUoEnJgU7pRysHUryoCUf9KmreF66IY85f5vul9CP1y7p7PiNKoVe2BH93ofjApn4OM0irqAWcKKY0k7l_EqIFq-LgVC8Wj20SHT-0QrXyu8BehbX82u6r7e_XreMlD9Omgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرفروش‌ترین خودروسازها در آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/665585" target="_blank">📅 13:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665584">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b19dd71f2.mp4?token=YKKgwMYUWrDW8S7kzmG65-rJD4dApEkavdWZqVflnpb2rmfoC9lBJjXsgYKD01v8ZwTT8M4PoqAVQej-i3bulz2-YI7sAobu4EMv9rI2pd519JhhldXyJHYT9tUJMWWU9q5h5ZpT7VL0-4oX3awuh1T4rRm2v7IrCaoZGm19k2K8EdaZ7b15XXEqbzM8q1T95pG4ojFKkp2zfgMs0yTQBF_MtzH4xi3X2wnjNn6qUJr3mIFHFSdIrH0RUIkJ5i2_0GQpjjTkScEWjp_MsVErvnIty1RymQ_UmYorZ_4IcyQAMYTnJga0nMg0EwdXOE_W5dxQXih_yhi6ZGwzULjk9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b19dd71f2.mp4?token=YKKgwMYUWrDW8S7kzmG65-rJD4dApEkavdWZqVflnpb2rmfoC9lBJjXsgYKD01v8ZwTT8M4PoqAVQej-i3bulz2-YI7sAobu4EMv9rI2pd519JhhldXyJHYT9tUJMWWU9q5h5ZpT7VL0-4oX3awuh1T4rRm2v7IrCaoZGm19k2K8EdaZ7b15XXEqbzM8q1T95pG4ojFKkp2zfgMs0yTQBF_MtzH4xi3X2wnjNn6qUJr3mIFHFSdIrH0RUIkJ5i2_0GQpjjTkScEWjp_MsVErvnIty1RymQ_UmYorZ_4IcyQAMYTnJga0nMg0EwdXOE_W5dxQXih_yhi6ZGwzULjk9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیوارهای تهران هم این روزها داغدار هستند
باید برخاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/665584" target="_blank">📅 13:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665583">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
هشدار پلیس فتا درباره کلاهبرداری‌های سایبری در ایام مراسم تشییع رهبر شهید
🔹
پلیس فتا نسبت به دستکاری دستگاه‌های کارت‌خوان، ارسال لینک‌ها و پیامک‌های جعلی و آگهی‌های دروغین فروش بلیت، اسکان و خدمات رفاهی هشدار داد و از شهروندان خواست رمز کارت را شخصاً وارد کرده و خدمات را فقط از سامانه‌های رسمی دریافت کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/665583" target="_blank">📅 13:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665582">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8619df2273.mp4?token=pzfR58eZ1XSFar4OG9VCEyVJDo8vqK3YgHvlP26R_kQz3zT16UtRGMOf7nmVW8Pvk0QM7h5whLvZNZgWu1F0j0AdV4f2tMCD0PbMwoNslSLrPR4jAHt8ADR54aeMg8jPNbi0ZCUp9U_3lR5LsGXzU3H8MDvI2-T0vnuqapbYALnS73Rq8is09gZzW1_T_8l59wdxL8jiGa3jLfWLONOlbBQUTywD8yMzu1-q-Mu46xztwxPkbYWFkcIajB9S6JQTfPDXG3LEq2OUP0EEkOzZ064wdOspr69nRZ4tO-dbWdm4IBcGvdwZIX__diJciIjUlv4FbehQNM4iqaHiECKvcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8619df2273.mp4?token=pzfR58eZ1XSFar4OG9VCEyVJDo8vqK3YgHvlP26R_kQz3zT16UtRGMOf7nmVW8Pvk0QM7h5whLvZNZgWu1F0j0AdV4f2tMCD0PbMwoNslSLrPR4jAHt8ADR54aeMg8jPNbi0ZCUp9U_3lR5LsGXzU3H8MDvI2-T0vnuqapbYALnS73Rq8is09gZzW1_T_8l59wdxL8jiGa3jLfWLONOlbBQUTywD8yMzu1-q-Mu46xztwxPkbYWFkcIajB9S6JQTfPDXG3LEq2OUP0EEkOzZ064wdOspr69nRZ4tO-dbWdm4IBcGvdwZIX__diJciIjUlv4FbehQNM4iqaHiECKvcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از وقوع آتش سوزی عظیم در یکی از محله‌های نجف اشرف
🔹
رسانه‌های عراق از وقوع آتش سوزی در محله الصناعی نجف اشرف خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/665582" target="_blank">📅 12:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665581">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB62ds73BPlRcjZkFjYlhhFGoNqX-nKfAzdwcdzUBCpcMi1QzAWDZ9nzd5iiV3L-0VsySGDodeZDZFojmj0eFoeBETNVHn2d5frUgJqQjIXWt6G3-UwUm2bp-eOYFWVDyH1B3wFKLTC5KqtMoRiOBH8H-5j8JV5Tbt9xIfqPqekGZ4brRAE0prCRDT17f1pry9PMQogHbI28xiychUK17F0TebBMSdlo3Kv0BBJU9xu7qRFnDZj9x-2q4ghdC77MSBItxvq5eFgg1-_f9LIGXfEJM2k2fnx9k7is8fo8mSs_3Uj1J0GZWIUqnOa3e8vIQVaP6bn0f2MAViC5h98lQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر لیوان نوشابه؛ ۱۳ دقیقه از عمر شما کم می‌کند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/665581" target="_blank">📅 12:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665580">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
انهدام کامل تیم ۵ نفره گروهک دمکرات در مرز پیرانشهر
🔹
یک تیم ۵ نفره از گروهک منحله دمکرات که با هدف انجام اقدامات خرابکارانه وارد مرزهای شمال‌غرب کشور شده بود، در عملیات مشترک اطلاعاتی و رزمی در ارتفاعات مرزی پیرانشهر شناسایی و به‌طور کامل منهدم شد. سلاح و تجهیزات این افراد نیز کشف و ضبط شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/665580" target="_blank">📅 12:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665579">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
الحدث به نقل از منبع آگاه از مذاکرات دوحه: آمریکا به ایران گفته که پیشرفت در پرونده دارایی‌های مسدود شده، منوط به پایبندی کامل تهران به یادداشت تفاهم است و تغییر در وضعیت تنگه هرمز، نقض تفاهمات تلقی می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/665579" target="_blank">📅 12:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665578">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cfe108375.mp4?token=jgnkLHB8Qg4ubGiCDgNvvJI15uEXKPdwlQSiS_yezqvc_J4IJLQOpAhJ_lqgwGWYObYKlqW-cMDRY6rnaXIwwsMOTKJCfEtK97B1Ao7U7wz2fzrPTTD4bvf7cKgPV0c6tkEH0bw0d7KEf4ug42DU8eIyCXazjbGzCd9BhekZljAyzNmQPqKjq7fF4QI3qmGzCZGHzhc2liVC6x-5eCuo5kfIk6bE8T_AjAwnR75-Qytmgf14YB8KQ45LltvroIoPbJ6kWS2abAKZffocinSZFpAVxGZuEIw-ZSwGY8G2RjKXM2Ke4VcIupKklvc11f1o16gp1LMiVo5muqtYuebUGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cfe108375.mp4?token=jgnkLHB8Qg4ubGiCDgNvvJI15uEXKPdwlQSiS_yezqvc_J4IJLQOpAhJ_lqgwGWYObYKlqW-cMDRY6rnaXIwwsMOTKJCfEtK97B1Ao7U7wz2fzrPTTD4bvf7cKgPV0c6tkEH0bw0d7KEf4ug42DU8eIyCXazjbGzCd9BhekZljAyzNmQPqKjq7fF4QI3qmGzCZGHzhc2liVC6x-5eCuo5kfIk6bE8T_AjAwnR75-Qytmgf14YB8KQ45LltvroIoPbJ6kWS2abAKZffocinSZFpAVxGZuEIw-ZSwGY8G2RjKXM2Ke4VcIupKklvc11f1o16gp1LMiVo5muqtYuebUGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونالدو از پنجره هتل محل اقامت تیم پرتغال، طرفدارانش را غافلگیر کرد و برای آن‌ها دست تکان داد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/665578" target="_blank">📅 12:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665577">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4764cb20.mp4?token=DbeYoS81MUiYlxs1z14YLSuJJE7NJkOkFtG2C1QbZjBUMDA0VRpniIeVsKe2_lecWpFiUyBKUIGFKOXyhbV_qe-vHh5bRHyf2vEUtRa7qeJdGI8COiTZnjhdP794JgwnIRqi6TW0yGvCnLSbhMMIflBcHvhLI1CLEtVCoVhdK4GHwxNu6yHaocxLlQWS5pLdwztXv8SeD4ppANKim-3KQMsHg4JG_4LcY2gL8yjPpeookMJDAKcCGPdwAsh_VKi5eRWjhK9V8Gc5Ae2LXCLCBER0aSBMSM9_yob7Z5O_GRatOa2h1yxCYbPtdd-5Vu1pesiGQxPdfXKJkZkpN01BTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4764cb20.mp4?token=DbeYoS81MUiYlxs1z14YLSuJJE7NJkOkFtG2C1QbZjBUMDA0VRpniIeVsKe2_lecWpFiUyBKUIGFKOXyhbV_qe-vHh5bRHyf2vEUtRa7qeJdGI8COiTZnjhdP794JgwnIRqi6TW0yGvCnLSbhMMIflBcHvhLI1CLEtVCoVhdK4GHwxNu6yHaocxLlQWS5pLdwztXv8SeD4ppANKim-3KQMsHg4JG_4LcY2gL8yjPpeookMJDAKcCGPdwAsh_VKi5eRWjhK9V8Gc5Ae2LXCLCBER0aSBMSM9_yob7Z5O_GRatOa2h1yxCYbPtdd-5Vu1pesiGQxPdfXKJkZkpN01BTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دیشب جام جهانی ثابت کرد تا سوت آخر، هیچ نتیجه‌ای قطعی نیست!
▪️
قسمت یازدهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/665577" target="_blank">📅 12:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665575">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b2cd5d1f.mp4?token=nmVoF7GYWQ3dtIgKuhWG-MIkT7IDLFRprqidrjW5EenRGRm5hwHRHNguN7Gql0xo5BetyaoVqrboMxX97JohgDOA3VZy-DAFJhURDmW9ZZzdvOdbm_QwyA-fy-6VtcgcyfyTMIbUMtJSIeO8OL11nHucOp9MNjx_UMh0_FfxFMRQLoz0VENPep-_50e_mo-7PhpsRBY8isT5XHkQR9FwyO0Gja4GUdNKar2xUab4DtnaSsg2GtXXMvSBAoVyzHbKwO8r9CAOzKFs7dbt8fAFJjOpLIlNbttrUVo-fbkiWM45xW0Jjbd6X3WPXCmarTTETobjXS2Zj6yfhekOyJXs7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b2cd5d1f.mp4?token=nmVoF7GYWQ3dtIgKuhWG-MIkT7IDLFRprqidrjW5EenRGRm5hwHRHNguN7Gql0xo5BetyaoVqrboMxX97JohgDOA3VZy-DAFJhURDmW9ZZzdvOdbm_QwyA-fy-6VtcgcyfyTMIbUMtJSIeO8OL11nHucOp9MNjx_UMh0_FfxFMRQLoz0VENPep-_50e_mo-7PhpsRBY8isT5XHkQR9FwyO0Gja4GUdNKar2xUab4DtnaSsg2GtXXMvSBAoVyzHbKwO8r9CAOzKFs7dbt8fAFJjOpLIlNbttrUVo-fbkiWM45xW0Jjbd6X3WPXCmarTTETobjXS2Zj6yfhekOyJXs7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا Svalbard نروژه؛ جاییکه خورشید هیچ وقت طلوع نمی‌کنه
🌘
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/665575" target="_blank">📅 12:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665574">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fc47TjaU9JWAQOdL6OZBv1tmTo55U0nBlRLG629-RZ1dt6WoZ6mR7no0fSWyXpnRpV1V9nHGN-yn9EzIlCAok2JUiCQ3ICDFn-g2ucqarl8Sl_XXwnDE6mXyAjtmws0qj3wo-BY2irRXi4I43ynPP_Qb2jzPNjQXhQKRv39BEtIobtz5N4xh3QvzDRmjMMop_7hsfdJi-rZ4NyCtUOE73eki3et9jZ9rXbfuyz70QnXE_dE3pMt8T9BRMP3SxrMbhvPK6A5fIXUzmaCDII3hDLvnVcEQqp8IirB4-kkRSwb_koxvyKfFjZTKO4UpooRTdo3GxEfOpjA1O4L_jyccnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امباپه در صدر رقابت کفش طلای جام جهانی ۲۰۲۶
🔹
کیلیان امباپه با شش گل و دو پاس گل در صدر جدول گلزنان جام جهانی ۲۰۲۶ قرار گرفت و در رقابت برای کسب کفش طلا از لیونل مسی پیشی گرفت.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/665574" target="_blank">📅 12:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665571">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/665571" target="_blank">📅 12:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665570">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsOFwYL9lBJxN_h79m24IcDiOjGm5nhnhZAlC3RxH-VZpilLp2sljbl1OIoF4Hhy8t3v5N6cOLMOMcqOdW8bCibVHR6Hsx8rPui-HobPs_14J3eytIHfwb1jSf-_4FFFlWX0BrzOFtcw-KwPyR_2GBu05Y6ayOz9zRwHZhQza49CChM4LwxeJkFy7NS3oN7geRSDI8koqYfuf5PaGTXgCorObDl1-mDtjhtxMy33H5sP2XgUV16zGOZvAClAqsC7MA4M1SMkDfI81HqqPyAim_mIWHcnjJmd-RiBnxup0AlmwbEOaXFvzHv6RTX5WD7knIP7JeA82aDOp1poYvqrdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چگونه رسانه‌ها ذهن ما را تحت تأثیر قرار می‌دهند؟ با این مهارت، قربانی اخبار جعلی نشوید #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/665570" target="_blank">📅 12:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665567">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c23ae14f5c.mp4?token=kpXCFJpKs2pDYYZlrr4d-j-iUxULpzQwgEcDVksqYV_bl86R91tbAJ9dCallEiIrZrnn_WIRZJc66C3je0LW61623f6Bo99j6J7FRYBilcdTfvibleHMpD3AGZ5Qdfp3XTFCoX8qLL-ghYGah0V02I0ltIXACQNjCtFxrdTcpS0U_AG1wwYBolJurXu-_MjwVTbJmvkyF-7A_7g3to2DuQfXw5XMrxWAXrwXT8N09ILvnDPLallufQcYZeI9ic7__0MoERt-y-7fc8d5mDAfTMigF6kb24iWOlqhR_50w6IpDTKGbZCYjlVSlxoCmHXPYA03TTNBkKPgqPlKFNN2mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c23ae14f5c.mp4?token=kpXCFJpKs2pDYYZlrr4d-j-iUxULpzQwgEcDVksqYV_bl86R91tbAJ9dCallEiIrZrnn_WIRZJc66C3je0LW61623f6Bo99j6J7FRYBilcdTfvibleHMpD3AGZ5Qdfp3XTFCoX8qLL-ghYGah0V02I0ltIXACQNjCtFxrdTcpS0U_AG1wwYBolJurXu-_MjwVTbJmvkyF-7A_7g3to2DuQfXw5XMrxWAXrwXT8N09ILvnDPLallufQcYZeI9ic7__0MoERt-y-7fc8d5mDAfTMigF6kb24iWOlqhR_50w6IpDTKGbZCYjlVSlxoCmHXPYA03TTNBkKPgqPlKFNN2mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌شود نروید؟
🔹
۱۳، ۱۴ و ۱۵ تیرماه، آخرین دیدار مردم پایتخت با آقای شهید ایران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/665567" target="_blank">📅 11:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665566">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b5d1b8f75.mp4?token=hWeLckRdtIm6kV7U59mepMqz4zo7CvxKhcrUfL851OkUwPSpvy4vrbnzI_xIldA4Banr9NVbXUwAFM4z8kEZbS2mz4L7Qt6BZWLI7dB4voiIZULKvxY6J3SXGUuO3qkhql6ZN8nyXv0XffMr7jHfQDybjQNU0qOQIG3e-37sKPkpQDNjH8LyNa-L8Kkii2UEIku6An9qFLtAvFyrj1CkIkXIWAnH9s_-QJ8CxoGZbHtN-gVpWtBlcoWnX3UDCPO0Ci2N58y9i7Md0Xtm9H7uM359v1ZtSdtjYXynPLWXFcu2audI4LM2UAtKz5Gb39oIlX7kPy0xJ3zsB4BOF9vDxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b5d1b8f75.mp4?token=hWeLckRdtIm6kV7U59mepMqz4zo7CvxKhcrUfL851OkUwPSpvy4vrbnzI_xIldA4Banr9NVbXUwAFM4z8kEZbS2mz4L7Qt6BZWLI7dB4voiIZULKvxY6J3SXGUuO3qkhql6ZN8nyXv0XffMr7jHfQDybjQNU0qOQIG3e-37sKPkpQDNjH8LyNa-L8Kkii2UEIku6An9qFLtAvFyrj1CkIkXIWAnH9s_-QJ8CxoGZbHtN-gVpWtBlcoWnX3UDCPO0Ci2N58y9i7Md0Xtm9H7uM359v1ZtSdtjYXynPLWXFcu2audI4LM2UAtKz5Gb39oIlX7kPy0xJ3zsB4BOF9vDxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر درباره کولر ماشین سوال دارید، این ویدیو رو از دست ندین!
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/665566" target="_blank">📅 11:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665565">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKXcS9tdKGYrlEJI8SMmzRMk-aVV9_Pogis_Jru07UYNMczwk0PmgHAInlrS6OHYYHil1rX9TUTkwPKRF6fEAnj4lr1T38h8CjmH41So6eINiMpAOXIVT531UfXrdvO0IQmMk-NDDVbcn3K6kadg4SmU71HmwoJiMwhI-mU8JzIG69qChqQBV-VKepHmcgwoLgsHjIWfPzWS-A_uii5Ek-3M0ajPeq6hv1KujnMjF0Yxsv9farAeOslWCeyMWjZ0PhP1Y4M-o_6iTGZNJWr_vblQINB-sAb1w9PYA53ofO6iPPHFM4EAA5ogsTDCxYJhZIjokgFeIZQS1UBA8tp0tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیش‌بینی وضعیت جوی مراسم تشییع رهبر شهید در تهران، قم و مشهد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/665565" target="_blank">📅 11:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665563">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cpswb5snk_zGM7_6rbZEddzVGFMlnQLDj1CPffpCwBN7WYMWOcx1q2_1LvVxTPuqrLMTnJtq4tZQ8_FvoOtbSkkYOag9n6ETmOhB_Dkv6t_m0g6Ip2PkqcAcU0R1GKFJDmR8PcqJ2-AqqWQD90P8shb4IsrsR-Bg7213-GUJnX5XhLp18_sbLP0Wr84y6lKXIJgKqKIw1tAe6qvdm_Rir3pen30K1XkplOEMgA08Uyt7XeyTRawWjxNq9ZvrPPChP9WHgGak8wxhgO3LfMbFYRkI1drseZ5KTPNRHHFYJur8ZecpW4Bu70xYrJPDseVwnvZ4LI1SkmFM8whFznSMzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز ۱۱ نوع چنگال که نمی‌دانستید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/665563" target="_blank">📅 11:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665562">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
مجموعه «چهارباغ» به فضای جدید وداع زائران در شمال مصلای تهران تبدیل شد
گودرزی, معاون خدمات شهری و محیط‌زیست شهرداری تهران:
🔹
این مجموعه که قرار بود به‌عنوان بوستانی متصل به مصلی برای نمازهای جمعه و عید فطر مورد استفاده قرار گیرد، اکنون با تلاش جهادی به فضایی برای وداع مردم با پیکر مطهر رهبر شهید انقلاب اسلامی تبدیل شده است.
🔹
با توجه به پیش‌بینی حضور گسترده مردم، مجموعه چهارباغ به گونه‌ای آماده شده که زائران بتوانند بدون ورود به صحن اصلی مصلی نیز مراسم وداع را انجام دهند.
🔹
همچنین مسیرهای دسترسی از بزرگراه شهید همت، پل روی بزرگراه شهید سلیمانی و ورودی‌های شمالی مصلی برای تسهیل تردد و کاهش ازدحام جمعیت پیش‌بینی و آماده‌سازی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/665562" target="_blank">📅 11:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665561">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f605d3aea7.mp4?token=fPf0CPVfwZW_2mGkPuarW97kBlkU2ylDduDSW6iKJywb9FzRlCeKWSmgtD58Cty-ZBfhxCxjI4cxi1RAdeRzMEaHnbGZ-UMM5a5k8GabsqP3SBJ8wc41ke1iElxxywkV-DK4TAN814A2RMn6N2CpVyDHiJXnX4JZIlajbN5Lyj0xz108rh8YhXtKUJjLxC0fdKHShbVOdnalSzVk-xGh0Dp9WLOV-hVMQMRCiebXbdd9dJrg9ws9YiUvy0TKA026pU0zV3ZI5bHK4NZTSRWUJVHHb4GmAYdcUDwuebmuK3-Qs-_FDV2XObgugylo4l425FzKkSfarVVL8znXtGfD7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f605d3aea7.mp4?token=fPf0CPVfwZW_2mGkPuarW97kBlkU2ylDduDSW6iKJywb9FzRlCeKWSmgtD58Cty-ZBfhxCxjI4cxi1RAdeRzMEaHnbGZ-UMM5a5k8GabsqP3SBJ8wc41ke1iElxxywkV-DK4TAN814A2RMn6N2CpVyDHiJXnX4JZIlajbN5Lyj0xz108rh8YhXtKUJjLxC0fdKHShbVOdnalSzVk-xGh0Dp9WLOV-hVMQMRCiebXbdd9dJrg9ws9YiUvy0TKA026pU0zV3ZI5bHK4NZTSRWUJVHHb4GmAYdcUDwuebmuK3-Qs-_FDV2XObgugylo4l425FzKkSfarVVL8znXtGfD7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱٠٠ کیلو طلا؛
جایزه ورامینی‌ها برای قتل ترامپ و نتانیاهو
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/665561" target="_blank">📅 11:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665560">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d307391130.mp4?token=BMMc4v_90j2V_F2hYQg1Bxn_rBEBfxGddYqRLXOVueXlP0Vbi58P_Ec5sn1A7woN-WrqMpZ6XbgjxAlL3XDk7Kv7p2z2I_YzPLJOVfkS1hckcT8QA3nX_16C6O3isNg1PCBoSTDGryB7ydfRyV0sMGkvpETENT0PB5e5d-50SqoYObsFZeAX1GMefGRV1oe3SVz_vw_NM1rctAnDI8cEruN7DSCgd_ZLdRGE1E1p6xuNBv1odzFo9SrD-oo2iSyVOCIbb4aJrLyd6v7_TFXKRVW7K3sqYHdOQH--TfBeGmdo9zbdyuyq-VFhfNAMeALrP4TZ2E7_1SaKam9JZLwTV4lFa9hc00JFfKWBivQzxXunhsy0WJzjHAkOU4sq4PsgLE2_aemFRKAk643e-Vnbc2-PzIzRpPuaXgQCFq5C0uQEz2aPMm1IW9l5qhRRICUnQmGiQ2DguAtG72sz1veYEdyE1ZB1GrBMrHpBJwaNJ2bF875IRQhdggQFHconc7o5MwRr4ADts9WibjY1ddAMEDhDDiYCdBcS6TvZDzoBhfieQbEfr2HBwQApc37_Wsy_AxpxvukCPuUoxve1OkNXyRNzQtesL0BslZzth5F1Gg4hBOV1ZpiQN5DIxfsny3Ypz87UOYahV7ykhlf53-Xjx_2nlj3i9dMa5JoQ2Nxo-5c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d307391130.mp4?token=BMMc4v_90j2V_F2hYQg1Bxn_rBEBfxGddYqRLXOVueXlP0Vbi58P_Ec5sn1A7woN-WrqMpZ6XbgjxAlL3XDk7Kv7p2z2I_YzPLJOVfkS1hckcT8QA3nX_16C6O3isNg1PCBoSTDGryB7ydfRyV0sMGkvpETENT0PB5e5d-50SqoYObsFZeAX1GMefGRV1oe3SVz_vw_NM1rctAnDI8cEruN7DSCgd_ZLdRGE1E1p6xuNBv1odzFo9SrD-oo2iSyVOCIbb4aJrLyd6v7_TFXKRVW7K3sqYHdOQH--TfBeGmdo9zbdyuyq-VFhfNAMeALrP4TZ2E7_1SaKam9JZLwTV4lFa9hc00JFfKWBivQzxXunhsy0WJzjHAkOU4sq4PsgLE2_aemFRKAk643e-Vnbc2-PzIzRpPuaXgQCFq5C0uQEz2aPMm1IW9l5qhRRICUnQmGiQ2DguAtG72sz1veYEdyE1ZB1GrBMrHpBJwaNJ2bF875IRQhdggQFHconc7o5MwRr4ADts9WibjY1ddAMEDhDDiYCdBcS6TvZDzoBhfieQbEfr2HBwQApc37_Wsy_AxpxvukCPuUoxve1OkNXyRNzQtesL0BslZzth5F1Gg4hBOV1ZpiQN5DIxfsny3Ypz87UOYahV7ykhlf53-Xjx_2nlj3i9dMa5JoQ2Nxo-5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازرسی بدنی «لیونل مسی» توسط آمریکایی‌ها روی باند فرودگاه و خنده‌های ستاره آرژانتینی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/665560" target="_blank">📅 11:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665559">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
♦️
مسیر نهایی تشییع و بدرقۀ رهبر شهید در مشهد اعلام شد  دبیر ستاد آیین تشییع رهبر شهید انقلاب:
🔹
طبق آخرین برنامه‌ریزی‌ها، آغاز مراسم در مشهد از میدان فرودگاه بوده و تمامی خیابان‌های اصلی شهر، محل وداع با پیکرهای پاک و مطهر خواهد بود.  #اخبار_مشهد در فضای مجازی
👇
…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/665559" target="_blank">📅 11:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665558">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpcJU30JW9TcyPaKTVXs7SGT9jtO_ajdGwp7sCjCjCuNN9lhbmmSI-YJG8E6LMkgJ-sjh06kQR7THczMiS7YB3bMp9vMRhCk8uXdlKXsI9p_N_xY_6m2AQCw6ZfWQOnCg5LT-CrrqHcIMKpQeunwkDRiK_112V_JtZkPhKl-byb2SYXLxPH46UerNHvSe5zX25wmd-pkihgmi6B3oX5vZp0N_b7dsez0JnZEHREO6CppXJ3OzYC0vArXijd1m7g6ZnRHfFenSPiOqH91zCD-vu89b2rQCk1lB7qccd4Hf6s30JVqBG-B4mNgochVrOJsb_ySWycF-Qsc7896-v9hnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردشکنی دیدار ایران و مصر در جام جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/665558" target="_blank">📅 10:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665557">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
مهلت بهره‌مندی از معافیت سه فرزندی و بیشتر تا پایان سال ۱۴۰۷ تمدید شد
فراجا:
🔹
همه مشمولان دارای سه فرزند و بیشتر که تا پایان سال ۱۴۰۷ واجد شرایط معافیت هستند می‌توانند با مراجعه به دفاتر پلیس+۱۰ ازاین معافیت بهره مند شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/665557" target="_blank">📅 10:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665555">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JblaX62A-76SkeHAB991yXlHZ7kimX9TE6YgT4kwSqbOocGDV0B2VMCaU3inIvmqDczaU7nHTUhzfgUwmc36uSAUzWPnpAESkvJHfja4ecbXNC0SUxCBdjx1mg8GqoPztMREf6M5-3FrYnMKT-Wi6fsYTd1q5cRY4T8OfCYna19LfdMkI0n_T41OPBpyrG13OTS_qhZugH4G_QGeRq2FEIeawRk6u5ziQv-sdLkXms74SMAUaoDV1oXemMerFpay8FbMCfOwZoEEagMBhk0AfR0-I0w47oYyhtyGPlWqcWhwNcFWAyeOHJgTVO0ALUApk86UL7L1ViglOdnUKqrqUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aCoDsJnbe2lYEZupsiXaKUwZKx5RZBFhPikXOgmBZQLtdvWI-BwL8JnMGcXQyII63ya6A-xu14y9Mp-ii454qMAlEynw6PMgiSGnI2_TSFqk02aBL7-vobjVUnl8oip15CiOmkpf__nGm4zKOCp30Q_1KKsysUTHUBDSms5Hj-I4tB31rSdCsiPmzsbu6FaqgDUrKnqHnHii6pOm2baRkMRCU5Q1zUj2tNsDIB5Z3InmJljUc6gXyqmg30VHzinLy2o6UaQ1WDMc3Tl6dkBJq6a2XehTKMMu_7uAXaD9XDCnUnoD59xdW0RnkrZjh3YP2GDvWR0djY256QTNkjoItA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۱۹ درصد خانوارهای ایران مستأجرند
🔹
حدود ۵.۳ میلیون خانوار (نزدیک به ۱۷.۵ میلیون نفر) در کشور مستأجر هستند.
🔹
تهران (۳۱٪)، قم (۲۸٪) و البرز (۲۷٪) بیشترین و هرمزگان (۸٪)، آذربایجان شرقی (۱۰٪) و گلستان (۱۱٪) کمترین نرخ اجاره‌نشینی را دارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/665555" target="_blank">📅 10:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665550">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kI6GZ5UL4cgYeS9_hjxtHjaCP1IJkz-HlGz3iHUaeB0DeVudUf9Dni4aqefvxfvxJ86h6o8EEJeAHOkI-fQDWM5J5Xc13wpWoHljeotIrgBfPw79Jx8tsXhypcbWmVHmrLNN_tmw6Z-hhwUATe15CgfcxfWbwwBF8PuxD-EzEkO-c3C35WAJC3_qO7b56PZ0EDIvIQKshKlQzX8ePspTcRwaxQ1NVDet_5r7zD-jDO1qSav0-hSQ0F8XKxrAGvxrJswa8j8OyOOD8AHIwXk2JXqXbf55jl55as4BUQNz2MzYCgReq8hEZ_EqvdnZJxwIiROkUlCYDNywtaVjzV3nEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XW-IN-0nzEWJAi45L-o6OWDN7FDbonBNPsfO3v-Is998ch4MA5hKY-1TzKqO41kyYGULodWo7wPuLL_QzpcNfTSVzn66PLKKZoP1BAJTNLgppaTW_7xksVKpQvnw07wkCBAlXD31-YygqYhS9j_3uSdJqi7j-2IH9Oe_MMds1fltPcjipzmkEflwB7-GgpzCo3lfLTFiVPWabFfJ5OvPCH2Unz4ywZ18JcFLKCWL4ikXbZ8V7xN11r0VyDvKlmPS_t9JVapWGHnUhp9Rf66JIszaXuLjy-8G0jU1tiHzb-cK6pvSPsJ2zXfM1pECr_dQJdrh3GykEiXjA8B4AqtTXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dlBDT_SCWaMtZ6uHQkc8O1s2KpmKxfe-nAsWLavwsZPrLvo8kcuvgeK13D0ykDanGPbp7aka0_nNoWR3Yd5n1Vl8CWHr15mOieCKeU7dXrgYIMbAnhq3I8hIy1h8Y4qFmxniaM43ZiVu0FRb04BXHAnGPnfwZ7phak8QtLzwdEOLnHfpejPRJ_QbA1DUG3sJ1F3o1jBw37-7tSc8LAbZiAUP4EqxS0sXs_G8dPQMaSUNbXgTqc0TNjW5hhD5cTxWaRTW-Of_tVPntMxAb6mtMgvZf1s37ZsTWjEUfJdswW7M9h0B6WN09IJgzokJhulVlkdCYTKhJKNTM3tCuaiIMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2Hi5uOHTEZUYsV9H_MlD_Zknqh6JSdR2LhW0as87Nxs2mTzDbQWgsqzecAtnU08PC9JnZwSHHBmsYgwnlZ5VMwpRvTSrBEXF71UEInh8UBEHrkDAzMgN3BKVqtsGLFl6B1OPKUVUbxQCwItTtiGmS2sOfYgnZXtHNGyE9G-6MKPtD509nN7rr0HFBcHdfpBR56Ko7dO3pLI250hhTPdqg1u7etDarIokxDed2388Kl4b6hP-6X0vPSIvqwkLaNZAet7kmZjG0dDkG5v7G0g_R0yLTsLC94yOZdredW6hTu1Y-h7PCQX_DzPuyJpYsFkopFjwuS1CDcQvBo3joX_kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با دیدن این الگوها شاید دیگر سراغ خرید پیراهن ساحلی نروید
🤩
🔹
یک نکته مهم؛ اعداد الگوها برای همه یکسان نیست و باید متناسب با اندازه‌های شخصی تنظیم شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/665550" target="_blank">📅 10:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665548">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
زمان ورود اتباع افغانستانی به کشور برای شرکت در مراسم تشییع رهبر شهید
فرماندار تایباد:
🔹
طبق برنامه، ۲۴ ساعت قبل از مراسم تشییع، ورود اتباع از مرز دوغارون آغاز خواهد شد. تا این لحظه اتباع وارد کشور نشده‌اند. تاکنون برای ۲۵۰۰ نفر روادید صادر شده است
🔹
زائران افغانستانی پس از ورود، در مراسم تشییع رهبر شهید شرکت خواهند کرد و در نهایت توسط همان شرکت مسافربری به مرز دوغارون بازگشته و پس از دریافت پاسپورت‌های خود از مرز خارج خواهند شد.
#بدرقه_یار
#اخبار_خراسان_رضوی
در فضای مجازی
👇
@SedayeKhorasaniha</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/665548" target="_blank">📅 10:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665547">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
بانک ملی: صدور کارت برای برخی حساب‌ها و انتقال وجه از حساب‌های فاقد کارت فعال شد
بانک ملی:
🔹
در ادامه روند پایدارسازی سامانه‌های بانکی خدماتی از جمله واریز حقوق کارکنان شرکت‌ها و سازمان‌ها، صدور کارت برای برخی حساب‌ها و انتقال وجه از حساب‌های فاقد کارت به فهرست خدمات فعال اضافه شده است.
🔹
خدمات بانکی در حوزه‌های پرداخت، انتقال وجه، خدمات شعب و بانکداری غیرحضوری به ‌صورت مرحله‌ای دوباره فعال شده و یا در حال بازگشت است و روند فعال‌سازی سایر خدمات نیز ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/665547" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665546">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhsjSHPOVqWs1ijX4VOGJPdpj64021b9zkRNBw4K1hMfMsOgO0sO44pqHKBwHaR2KMrfohD30SanrEFpIPt-mW6ijfrvp9mvkpfNPer6mWoSEArMQSe1lxJDpP3-lsn3PBZmKqZ8qhUJKmuJLwQ8onFr4eKRUCyg3DyGNm8MibsJLZjxOg6PdmLkW3_wE96fT1iPFa9DzugCp2QRf_N2T5tId4Zp5sjh_TMPgbl-UMM2Y-J6yz7PHTPUPsfmzF68ItWatDuz4B_jLCgjtHtshtzx-Hck-x1W_d61d4q3bZIsvY98M1-xCeC8kS4_-2kkkCMIXywqkEla70WiWrVUCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرمول طلایی افزایش بازدید در اینستاگرام؛
زمان درست انتشار + محتوای حرفه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/665546" target="_blank">📅 10:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665545">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8eda3dad1.mp4?token=CbpH5TwxI9H6fWctsV-f1zDjfEwtwd9kySCrnQ07GxD_M79dPW8_xU5z8vrDbSQ1MzIHuxKNFCiha8S1ZE2ujzs-sQfozsyvXvdQYJfgCRpq1aTKTGJf3uV1fvTovT2MAtbssut_x9LmBMn38RInPE-H2cUGG4kd0kOitF5VD2eLL7nL3FtCKKOjHUeI3Dvx_-5AEWGbS4co4NQC6C4d3V4Z74kkGxLKXj5l5VQRtfETUWSkYvr0_2hrGdv34jOG_bBWJ_hdsN74y1qXeoECXQcGblcF2GwmSRok_nuRGY_eXbHWOXqKYjfBgK_t7b8gPScN-YbvfyKhFgMDQmE7lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8eda3dad1.mp4?token=CbpH5TwxI9H6fWctsV-f1zDjfEwtwd9kySCrnQ07GxD_M79dPW8_xU5z8vrDbSQ1MzIHuxKNFCiha8S1ZE2ujzs-sQfozsyvXvdQYJfgCRpq1aTKTGJf3uV1fvTovT2MAtbssut_x9LmBMn38RInPE-H2cUGG4kd0kOitF5VD2eLL7nL3FtCKKOjHUeI3Dvx_-5AEWGbS4co4NQC6C4d3V4Z74kkGxLKXj5l5VQRtfETUWSkYvr0_2hrGdv34jOG_bBWJ_hdsN74y1qXeoECXQcGblcF2GwmSRok_nuRGY_eXbHWOXqKYjfBgK_t7b8gPScN-YbvfyKhFgMDQmE7lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات بی‌اساس پمپئو، وزیر خارجه پیشین آمریکا؛ نباید به پایبندی ایران به تفاهم‌نامه امیدوار بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/665545" target="_blank">📅 10:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665543">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce95593786.mp4?token=GnoaaBbm7s7wIKBh6F89qjMlc3HRrZkU1Smyd0PCK2na-P3Bcqgk1cC63udPIQ2uUXP2k2XIInit4UgcLf0I_Hw_IpLpANoJZP5Xgb8SBCYWHDvs8PftU924xBAJS9hvD-SzLB5Zuzawp4PquWAojw6lnlgiWj3gQCDEe6yrRkTwsoCtsGQYqDRBbepD_Zr0I_-0ZqQ1t_iGslhnINV8e6WV1zhYSrxDqAvpoIpnSmIvefCWEUiMsYDlGt-79bASLvFjsBG9vvXwruF8nAbWBLha5N07y4kKEnQUado5kaTkLD1p1GfOT3625VN1j3k_jku_p3-lbf9_DJeyT5Ci4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce95593786.mp4?token=GnoaaBbm7s7wIKBh6F89qjMlc3HRrZkU1Smyd0PCK2na-P3Bcqgk1cC63udPIQ2uUXP2k2XIInit4UgcLf0I_Hw_IpLpANoJZP5Xgb8SBCYWHDvs8PftU924xBAJS9hvD-SzLB5Zuzawp4PquWAojw6lnlgiWj3gQCDEe6yrRkTwsoCtsGQYqDRBbepD_Zr0I_-0ZqQ1t_iGslhnINV8e6WV1zhYSrxDqAvpoIpnSmIvefCWEUiMsYDlGt-79bASLvFjsBG9vvXwruF8nAbWBLha5N07y4kKEnQUado5kaTkLD1p1GfOT3625VN1j3k_jku_p3-lbf9_DJeyT5Ci4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ۸ نشونه، چک کن ببین مغزت خسته‌ است یا نه #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/665543" target="_blank">📅 10:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665542">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8982ab33c.mp4?token=k-QGiS09TKc1b2ygJAG7xwITHNcnWDkbDU7Bi2oWrNNwak8JZ9D0U4W6JChsP4mvGHggUFQX2Ot8PtRIg7uYkSujLvBp0_CIXL5o68aLk7vRxfM2dwhRBYH5PYrAv4fZxpIuaINP375w3okwsc9b0fDCPGehRjahgTiaddZ8xIUDRmZq-KJ5SgdCOWvT16-MDZ31wZBZffFnRUKDXRhZ26iekle65PSbc-5-pNtG5XquO_La11M237SakgLVsAGRVcIZKXDPvcKLqFMV70OAuipdVVI-m0njDstvz_t7qcv_HZqsfjDz0NSKSLS_QVSy9l3p62nZi_X-kOl7Mq-0ymKmxxNz_IhOiuiPWTU9THwL4lvkZAA82hRyVS9EUhUIRx-5BgDT__o2QPx3sPym5Vp6Aq1eBCPwa7-_G9lUMjtv858yrTTESQBl0sN55jWNn3Ao-2677eO4kBEeEEWz9Gac7g2-qd2E3l5MUHio620EVJrsQqE-l25_xZ3JOXAwgBFiAa_JDazhbtLphEz4ED9pPQ7LmHH-dgK8aoeTQuzLAxRwGFDa919FGFZ-shRCWGgScApqRXG7ZDT6vwXvmd2pn7P_SAX9rXApljUvvmHHbJCaLtJxyoso_mCFyphlN8th3GLDblUOSQJCO5nYgH9jGRqMuu6DbpU3GpULmyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8982ab33c.mp4?token=k-QGiS09TKc1b2ygJAG7xwITHNcnWDkbDU7Bi2oWrNNwak8JZ9D0U4W6JChsP4mvGHggUFQX2Ot8PtRIg7uYkSujLvBp0_CIXL5o68aLk7vRxfM2dwhRBYH5PYrAv4fZxpIuaINP375w3okwsc9b0fDCPGehRjahgTiaddZ8xIUDRmZq-KJ5SgdCOWvT16-MDZ31wZBZffFnRUKDXRhZ26iekle65PSbc-5-pNtG5XquO_La11M237SakgLVsAGRVcIZKXDPvcKLqFMV70OAuipdVVI-m0njDstvz_t7qcv_HZqsfjDz0NSKSLS_QVSy9l3p62nZi_X-kOl7Mq-0ymKmxxNz_IhOiuiPWTU9THwL4lvkZAA82hRyVS9EUhUIRx-5BgDT__o2QPx3sPym5Vp6Aq1eBCPwa7-_G9lUMjtv858yrTTESQBl0sN55jWNn3Ao-2677eO4kBEeEEWz9Gac7g2-qd2E3l5MUHio620EVJrsQqE-l25_xZ3JOXAwgBFiAa_JDazhbtLphEz4ED9pPQ7LmHH-dgK8aoeTQuzLAxRwGFDa919FGFZ-shRCWGgScApqRXG7ZDT6vwXvmd2pn7P_SAX9rXApljUvvmHHbJCaLtJxyoso_mCFyphlN8th3GLDblUOSQJCO5nYgH9jGRqMuu6DbpU3GpULmyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقش ایتالیا در جنگ آمریکا علیه ایران جنجال به پا کرد
🔹
مخالفان دولت ایتالیا می‌گویند اختلاف اخیر میان ترامپ و ملونی تنها یک نمایش بوده و نخست‌وزیر ایتالیا در تمام مدت از عملیات آمریکا علیه ایران حمایت می‌کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/665542" target="_blank">📅 09:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665541">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/190a5dd598.mp4?token=dspIKAKV78zZi3xGupWf1ZrYTa4EmhcjnV0eWWPsnA3bjcWCKi9tcWC9IzLVFA55V5MN9xSpIvkYuAL9uG-oSOJiGI7pL3zHImi_IntVVdJ94LN0zZBNJQLE8lpdatcTZga7LWK0dMu8z5anXOQ3YtvZ41lSTXsxjYg3BY-2tka8a2BAozsBQ23chrpNY8W-I1giM_Rh9Se0upsoFQXxsQiy6bh391Vp4zp9L0p4tlyJdEWSsSnFcbY1DBPLqZFXbYVSANUOOLyIoXHtjxeCOPQ5MRJxxjvpMGljJHCKBeMGzgN6FBT7QDdnOQN9ylMpmUY2WcnBFlcV7oNz6lwQ8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/190a5dd598.mp4?token=dspIKAKV78zZi3xGupWf1ZrYTa4EmhcjnV0eWWPsnA3bjcWCKi9tcWC9IzLVFA55V5MN9xSpIvkYuAL9uG-oSOJiGI7pL3zHImi_IntVVdJ94LN0zZBNJQLE8lpdatcTZga7LWK0dMu8z5anXOQ3YtvZ41lSTXsxjYg3BY-2tka8a2BAozsBQ23chrpNY8W-I1giM_Rh9Se0upsoFQXxsQiy6bh391Vp4zp9L0p4tlyJdEWSsSnFcbY1DBPLqZFXbYVSANUOOLyIoXHtjxeCOPQ5MRJxxjvpMGljJHCKBeMGzgN6FBT7QDdnOQN9ylMpmUY2WcnBFlcV7oNz6lwQ8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت آلودگی هوای شهر کرمان| پنجشنبه ۱۱ تیرماه
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/665541" target="_blank">📅 09:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665538">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgMB-uT4WkfhXcvzqHvJQs7G1RKm84mYKN7zvPf_D8J3AXeFJ-r1P3v2DzaDd-F9NZjnHajClwbz3RIe6PjOB-701a40eRBvB5ywp-g4xLsSEd9oc55potro3iwJtqUlVE7974VyxBzmJ-OLK5JiPhdetCbB6Z8y3L1nL6B0trwmJbt1FI5sTGE2hS_5KQ6rC-P83CT63ZH7XdmlRQ9b-h3c75t64aYNiLUnq2DDb_ewkCGmBwBak5Kgc0C_oSy2hfx4-kiE6SVeJEG53bz9oPXKaDe1OR4vJ_KC9bbY4QPyvnAv9YepvVMbqB-PwJuqoMsAhj9OkOlNEvvka9lJvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a702236dce.mp4?token=m9Kpftq8x9xUx-qNDhr-XDuvn54ux4653M377ovOnH-CaTSAN5kRyAN97WZqmWo5N-_0XoY9uoNE_46lEjFA8sluNrkx-SD4d_JJNZNAkrDDJlpiLHjdjhLM0UdMxi4tJATsyymXum0_Bd8HjyPsQFD0aa43Ex-jr-ugcNLIVBfDlT-hsDbJb7s_Exp79RYZt-swU_gvS_KYnMc0fUmBC9L_HbgDpljhhBYwIawbtV7CXtdLafWMHb5G2BhHsfx6WrWJG29lFXoZC1S_YMa_K3M7jfG7tpe3xEUxldvQ4riTq3FTuYmIT4lcncsSQReuc-2k8CCWwp6UtiL86pQ4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a702236dce.mp4?token=m9Kpftq8x9xUx-qNDhr-XDuvn54ux4653M377ovOnH-CaTSAN5kRyAN97WZqmWo5N-_0XoY9uoNE_46lEjFA8sluNrkx-SD4d_JJNZNAkrDDJlpiLHjdjhLM0UdMxi4tJATsyymXum0_Bd8HjyPsQFD0aa43Ex-jr-ugcNLIVBfDlT-hsDbJb7s_Exp79RYZt-swU_gvS_KYnMc0fUmBC9L_HbgDpljhhBYwIawbtV7CXtdLafWMHb5G2BhHsfx6WrWJG29lFXoZC1S_YMa_K3M7jfG7tpe3xEUxldvQ4riTq3FTuYmIT4lcncsSQReuc-2k8CCWwp6UtiL86pQ4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شادی متفاوت بازیکنان مکزیکی‌ با ماسک هالند
🔹
بازیکنان مکزیک پس از صعود به مرحله یک‌هشتم نهایی، با ماسک ارلینگ هالند شادی کردند؛ هالند هم با انتشار ویدیوی این لحظات در استوری، به آن واکنش نشان داد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/665538" target="_blank">📅 09:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665536">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bb365f2ee.mp4?token=YL2X-Qo7gdyDaVMIiQhV1i0T9eC_bg7msxlb-GRyZdXPpVP1JZTN4lzmOE6kkk9SvSUtOPh4sTZYuw-kwlwIpbCdyjOVCxbJsKVAYw7uK-44IKhF_h_rvp-17JrLlkcsMpkt2Q5dRGzQExgsX0IJo-nBxXHBnsE_S3MrsGk3Ue7KU1If4K5HuXKamjeok4Mq71vSR-S-yeEtNanVzqzOBRW4FiRgMozlweyvGey6X5Dx7kLhwYCkd4nuiwRiesuLY65zhI_dUvz1Lf5VKQfe7X947Dmfy9L84vt-AHVaVxFmKvu83r_mvGTzq4OpSslilAiv3k2Ccx6Tbs4ogWHldQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bb365f2ee.mp4?token=YL2X-Qo7gdyDaVMIiQhV1i0T9eC_bg7msxlb-GRyZdXPpVP1JZTN4lzmOE6kkk9SvSUtOPh4sTZYuw-kwlwIpbCdyjOVCxbJsKVAYw7uK-44IKhF_h_rvp-17JrLlkcsMpkt2Q5dRGzQExgsX0IJo-nBxXHBnsE_S3MrsGk3Ue7KU1If4K5HuXKamjeok4Mq71vSR-S-yeEtNanVzqzOBRW4FiRgMozlweyvGey6X5Dx7kLhwYCkd4nuiwRiesuLY65zhI_dUvz1Lf5VKQfe7X947Dmfy9L84vt-AHVaVxFmKvu83r_mvGTzq4OpSslilAiv3k2Ccx6Tbs4ogWHldQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پسربچه شجاع بلوچ بعد از گذشت ۵ روز در دل جنگل سالم پیدا شد
🔹
محمدصدرا، کودک سه‌ ساله‌ای که پنج روز در منطقه چشمه‌گل رامیان مفقود شده بود، با تلاش نیروهای امدادی و انتظامی پیدا شد و برای بررسی وضعیت جسمانی به بیمارستان منتقل شد.
#اخبارفوری_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/665536" target="_blank">📅 09:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665535">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06be39591f.mp4?token=GxABFI5NDqgbRL9QBr5y8tdc3X0U1FES0UdiQ90pFLaDhy08t2lDHpgkY1aLl_4l4z43UIMiJFHxbXO8ZM-2-aHqvrnaFVYcR1dnTqELT34otT25XUpb5zdpjcoid4OSPVnZ5QovnSvaqipzIiEuTwMay0lg9d1TvxlPzXtzXnYH8FEelJ28_iK4OCtJovE8n4lhHKnAXLjTaT9U-MHBePqmm39SXP0RKvvSCuJGqtfcE30CWebdazc8whLBTuDq6T2txytFIA5z9coLw9lQLkrr0rk0qZaoQBGKZ-cCBoLE4CKyFigvQafHxYjgXgX60WEjo56I6bgnUvKTXmMpsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06be39591f.mp4?token=GxABFI5NDqgbRL9QBr5y8tdc3X0U1FES0UdiQ90pFLaDhy08t2lDHpgkY1aLl_4l4z43UIMiJFHxbXO8ZM-2-aHqvrnaFVYcR1dnTqELT34otT25XUpb5zdpjcoid4OSPVnZ5QovnSvaqipzIiEuTwMay0lg9d1TvxlPzXtzXnYH8FEelJ28_iK4OCtJovE8n4lhHKnAXLjTaT9U-MHBePqmm39SXP0RKvvSCuJGqtfcE30CWebdazc8whLBTuDq6T2txytFIA5z9coLw9lQLkrr0rk0qZaoQBGKZ-cCBoLE4CKyFigvQafHxYjgXgX60WEjo56I6bgnUvKTXmMpsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
♦️
مسیر نهایی تشییع و بدرقۀ رهبر شهید در مشهد اعلام شد  دبیر ستاد آیین تشییع رهبر شهید انقلاب:
🔹
طبق آخرین برنامه‌ریزی‌ها، آغاز مراسم در مشهد از میدان فرودگاه بوده و تمامی خیابان‌های اصلی شهر، محل وداع با پیکرهای پاک و مطهر خواهد بود.  #اخبار_مشهد در فضای مجازی
👇
…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/665535" target="_blank">📅 09:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665534">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c18700f826.mp4?token=falxWTLklaikYNesSNJDpiR279jXaSF5TVeD1Sa-vMRhZwpzbQ1Etyet8HRlRTYSZgI_kIZD1nEI_7KNqe-5Qnit-zSJijjIg8ZaHG9YI0PXtwCP6emYGQKoff56WNcV8hBZEIJbD58jzPOY5MR2qENiUHlJiPOr0z5k8Cg8UsJSdccdytP0CgOEjb7OkbtiYwr53m3WYPcmmIv77UcwJ7KQRkXCIZVfHbMr3F85b0iETe7eUQj0q971ysJus91bRO0v8NNKfNRKTm-LjMN6PugOxZApL1m8t_6Zb8Df1YJQZa2dAFVG7Rf9K-WoxjdH9mY5Mw_fk6m27q-3DC1Amg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c18700f826.mp4?token=falxWTLklaikYNesSNJDpiR279jXaSF5TVeD1Sa-vMRhZwpzbQ1Etyet8HRlRTYSZgI_kIZD1nEI_7KNqe-5Qnit-zSJijjIg8ZaHG9YI0PXtwCP6emYGQKoff56WNcV8hBZEIJbD58jzPOY5MR2qENiUHlJiPOr0z5k8Cg8UsJSdccdytP0CgOEjb7OkbtiYwr53m3WYPcmmIv77UcwJ7KQRkXCIZVfHbMr3F85b0iETe7eUQj0q971ysJus91bRO0v8NNKfNRKTm-LjMN6PugOxZApL1m8t_6Zb8Df1YJQZa2dAFVG7Rf9K-WoxjdH9mY5Mw_fk6m27q-3DC1Amg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این دو قرص می‌توانند در لحظات اولیه سکته حیاتی باشند
🔹
در صورت مشاهده علائم سکته، قبل از مصرف هر دارویی با اورژانس تماس بگیرید و از مصرف خودسرانه دارو خودداری کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/665534" target="_blank">📅 09:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665533">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aO4-4uAMhl7RxNKO0TSSAdLhz2gWJusqRxulTkdD-2sNmynw3a-WUiacyL-ciihTZFUs13Di0oQepoE-ayukFhVogulpdTde9dKxgdJPjYf7LJCUa5D34-0s9IrUNh2MqjXVR6xRgdbVdGTCMMUQ6TCVvLqF6ESOJ8MAwdHOB3CRxJ_-wrg8wE1_rNGjHsZrewRgXbNUFZIYT5dNfq9ZPf2LP84n995hpzeVxvLFLls82XfqkkDUuDMwktdgzIOlJ98O6ngo-jB-B0_I8t9hv_UXFH1DPv-3ZaVvNPzPfT3FfgDbGsZOxmcELgi2jHyPCZbIug2-V7-GJ-NtpMhVww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای عجیب ماچادو: من رئیس‌جمهور ونزوئلا خواهم شد!  رهبر اپوزیسیون ونزوئلا:
🔹
من زمانی که زمانش فرا برسد، رئیس‌جمهور خواهم شد، اما نکته مهم این است که این موضوع باید در انتخابات و توسط مردم ونزوئلا تصمیم‌گیری شود.
🔹
در آخرین انتخابات، اجازه ندادند که من نامزد…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/665533" target="_blank">📅 09:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665531">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319b62d958.mp4?token=eadBCJu4mJN74XccL8Bl3sWW9-nwarbzyjaxpfqZpjDvLRUmHysciL0atsQc7QZ0Y27iPBGej0aMhQJcmOakh3U68QH7CZhg-KjMQqKR8pLqBjEf0LEK1Yxl8Aek7uNTkhWo12xHLZcuMN3b3jKpfEIO7fqUV_Btw5djB8WBsrdk26VuJV2lihcaxIB6k--LxsBqG16J3dKUgF7oKtWp3EpXchQ3_cwDDoTTJXHJFOVtKgzLC-vS3HwdSk8NKLX6az_ziJMjFEzoXmQliH9uw0gQRe84escmwBxTiyqu1nnq4suBfZ5TH8H3fapW4wtewNAWr0Q86vFso1K_iLcB7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319b62d958.mp4?token=eadBCJu4mJN74XccL8Bl3sWW9-nwarbzyjaxpfqZpjDvLRUmHysciL0atsQc7QZ0Y27iPBGej0aMhQJcmOakh3U68QH7CZhg-KjMQqKR8pLqBjEf0LEK1Yxl8Aek7uNTkhWo12xHLZcuMN3b3jKpfEIO7fqUV_Btw5djB8WBsrdk26VuJV2lihcaxIB6k--LxsBqG16J3dKUgF7oKtWp3EpXchQ3_cwDDoTTJXHJFOVtKgzLC-vS3HwdSk8NKLX6az_ziJMjFEzoXmQliH9uw0gQRe84escmwBxTiyqu1nnq4suBfZ5TH8H3fapW4wtewNAWr0Q86vFso1K_iLcB7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش به اظهارات پزشکیان درباره اختصاص ۲۰ میلیون بشکه نفت به هوافضای سپاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/665531" target="_blank">📅 09:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665530">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62fbc3509c.mp4?token=lIGAjO3jukV1-rm6ZJeqZUBtkfpavujUHPBOFTox0K5SnS5JbmYQMFmzo16qfxHoBCcbYGis8VlRagdGJNRleTnbZ06DXqF08WophKe8x3Jyn5TMtX0ka4ygms9Z_do7aPoim-R18MO4H_i8s_4VdrQL-eJVIohyBSTRQBx9Aw19ebwCIa1k6hpR7DEpZYRBC8hg91xAcUxNyADp8d60DfgJ0LBsJIAUzp5mt3-JGyVHJqAiTy3ReWlWId3CxAVlz6xuX_DViVq2W-xy4zaX25glGgJ-SCvGPMakKnszQsoRPhJWwmW3F3LBDrlKW8Wwewe1Rm1eDwW_BkvL6RHyWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62fbc3509c.mp4?token=lIGAjO3jukV1-rm6ZJeqZUBtkfpavujUHPBOFTox0K5SnS5JbmYQMFmzo16qfxHoBCcbYGis8VlRagdGJNRleTnbZ06DXqF08WophKe8x3Jyn5TMtX0ka4ygms9Z_do7aPoim-R18MO4H_i8s_4VdrQL-eJVIohyBSTRQBx9Aw19ebwCIa1k6hpR7DEpZYRBC8hg91xAcUxNyADp8d60DfgJ0LBsJIAUzp5mt3-JGyVHJqAiTy3ReWlWId3CxAVlz6xuX_DViVq2W-xy4zaX25glGgJ-SCvGPMakKnszQsoRPhJWwmW3F3LBDrlKW8Wwewe1Rm1eDwW_BkvL6RHyWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترند جدید درمان افسردگی در تهران؛ بغل کردن درخت با هزینه میلیونی
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/665530" target="_blank">📅 08:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665529">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6_lNuORZmFvIKzzaeDcnVMRayI1Q6vq7yRMBjhLAdXX5HwkReZAzdf8DQibVSVrllEBCH9HEEdb3xsg-tGvZ2fNy9cg79lxdxZvnI8kykjFUzjRdD6H41z7Y5r3DmIvDtoygqPN2XZRbSVe9uh7DVCyxvvIjFRXv88idqax-eZcC_hV3nVFbTYiQOXBmrMNWE3bXTIieAgporyW7laNlaDw4_k1oJUMsEisuLH6k0bVol-BIE3lsqQ41C7I4m7MOLBSLIIgDHCY6GspVeH7hwBbhqKZyCPeOgSfQnVKNVlM4StTX4MZ3H6AVja2t-cdR3lEwYvOVAPFapbnQhKWGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی پیاپی قربانی می‌گیرد؛ ۷ سرمربی تا این لحظه برکنار شدند
🇪🇨
اکوادور - سباستین بکاسسه
🇺🇾
اروگوئه - مارچلو بیلسا
🇳🇱
هلند - رونالد کومان
🇨🇿
چک - میروسلاو کوبک
🇰🇷
کره جنوبی - میونگ-بو هانگ
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند - استیو کلارک
🇹🇳
تونس - صبری لموشی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/665529" target="_blank">📅 08:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665528">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fe1b73c3.mp4?token=uP-Bq3okO1uaNhjqpOseXSvLhamY6BAb_QmHp-PjiCwp96iGzTAbzhqOtLeoYpuUHjvREg44CwepRYh4aCJY4sIUlnidWKwi3SSGMvW4xxvLy2aVu-STy5ajcoxf2AfDKVufHfL2O4Z6igCvuZvl7Pfi7gXiTWJVZj1jTL8Q1bXUcIAMTgBEO7mgG1llfjw0a0aEQZRPTD2zpwzvocavas_ENrR7hPtkH6fNCsU1wyiqPQNzLSTYptyBztLcGiI7htRgKg1SYzWS9Ycgoieob2Ks8WlW8onVRD6-hu_ebFe75SFfvdDw_oVLDTmsuW-r8bpmy_W6oTlRJHR2Z9fv7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fe1b73c3.mp4?token=uP-Bq3okO1uaNhjqpOseXSvLhamY6BAb_QmHp-PjiCwp96iGzTAbzhqOtLeoYpuUHjvREg44CwepRYh4aCJY4sIUlnidWKwi3SSGMvW4xxvLy2aVu-STy5ajcoxf2AfDKVufHfL2O4Z6igCvuZvl7Pfi7gXiTWJVZj1jTL8Q1bXUcIAMTgBEO7mgG1llfjw0a0aEQZRPTD2zpwzvocavas_ENrR7hPtkH6fNCsU1wyiqPQNzLSTYptyBztLcGiI7htRgKg1SYzWS9Ycgoieob2Ks8WlW8onVRD6-hu_ebFe75SFfvdDw_oVLDTmsuW-r8bpmy_W6oTlRJHR2Z9fv7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگترین موزه آجری جهان در خراسان کهن
🔹
کاروانسرای رباط شرف؛ شاهکاری از معماری ایرانی در دل جاده ابریشم
#اخبار_خراسان_رضوی
در فضای مجازی
👇
@SedayeKhorasaniha</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/665528" target="_blank">📅 08:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665526">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85797dc071.mp4?token=XmaQzgIC5O5rZRg5VSK5lMOLV6dhiSJGbr4ovzfkFgTyjffoxen2x1Z0YexMq02xzG2d_Hg9CScHJSgM58HpevPMWUdv5ZO33W5VBzOniSgqAQKlV-TJAGpCZeWQ2WGdGPAbJwGgMu4-RSQsTjHXIJwnO6KZUIqUvVStwty8aHkbh5GRPyxQLMcNxAUmTGtH5hP5H0Mjz_FCTDSX9FHlyYu1K7Lhlu-FR2ksUNSaqK5ROKZoVsTL1O4Zptdqm8i0rHDV5lAYyH0JQrfep8JrK9VmqS-8CobMPNrQV2prMWiiYSZZZlyfF6MYCGeCJ2_H9T6-4RXvDd-RwRMZzOdMRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85797dc071.mp4?token=XmaQzgIC5O5rZRg5VSK5lMOLV6dhiSJGbr4ovzfkFgTyjffoxen2x1Z0YexMq02xzG2d_Hg9CScHJSgM58HpevPMWUdv5ZO33W5VBzOniSgqAQKlV-TJAGpCZeWQ2WGdGPAbJwGgMu4-RSQsTjHXIJwnO6KZUIqUvVStwty8aHkbh5GRPyxQLMcNxAUmTGtH5hP5H0Mjz_FCTDSX9FHlyYu1K7Lhlu-FR2ksUNSaqK5ROKZoVsTL1O4Zptdqm8i0rHDV5lAYyH0JQrfep8JrK9VmqS-8CobMPNrQV2prMWiiYSZZZlyfF6MYCGeCJ2_H9T6-4RXvDd-RwRMZzOdMRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم بلژیک به سنگال توسط تیلمانس
🇧🇪
2️⃣
🏆
2️⃣
🇸🇳
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/665526" target="_blank">📅 08:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665525">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
قالیباف: ۶ میلیارد دلار ما در قطر بود و ۶ میلیارد دلار بعدی را آن‌ها تقبل کردند  رئیس هیأت مذاکره‌کننده:
🔹
می‌گویند چرا سوئیس رفتید؟ خب من رفتم آن‌جا اوفک را ونس امضا کرد تا پول‌ها آزاد شود‌.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/665525" target="_blank">📅 08:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665523">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a222302c5f.mp4?token=Fko3pwPBlwEFCAitpZOaCKHgnZm_lbVrwX5r7IIdbGX4IuAJWE6oDhxdqD8McYYernfCydflsIycgqhaCLqH2qCY8Lt65b0rXrzb0dbQCJaiuaucElKI50X6CNG8UG0fs10WEJRlKchwhRaejaE_ZWKVIwdyOlRaVrqQmD3slb1ITHwiFiQRm0UFFL-NtviiTRQ-No_IRSSnOEA3hz6idhhv7mg3j86dN6cdhoKdL9Vem0MFv0Lu710b6lnKWldT75lAUGIF-KJwpjPHLcpzu3lYc8h-eyap6HyKK4hwcnbkXJ25CV3p3hoEaRiKt7vjxXMalkVAqcpbsFAMaqlETQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a222302c5f.mp4?token=Fko3pwPBlwEFCAitpZOaCKHgnZm_lbVrwX5r7IIdbGX4IuAJWE6oDhxdqD8McYYernfCydflsIycgqhaCLqH2qCY8Lt65b0rXrzb0dbQCJaiuaucElKI50X6CNG8UG0fs10WEJRlKchwhRaejaE_ZWKVIwdyOlRaVrqQmD3slb1ITHwiFiQRm0UFFL-NtviiTRQ-No_IRSSnOEA3hz6idhhv7mg3j86dN6cdhoKdL9Vem0MFv0Lu710b6lnKWldT75lAUGIF-KJwpjPHLcpzu3lYc8h-eyap6HyKK4hwcnbkXJ25CV3p3hoEaRiKt7vjxXMalkVAqcpbsFAMaqlETQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۴ حرکت انفجاری برای تقویت شکم و پهلو که هیچ کس بهت نمیگه
💪
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/665523" target="_blank">📅 08:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665521">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7bfdc0c.mp4?token=D0k_P5deyWuIdRZ6Gt9DL1bVCWyhM22HcHrcEqpBDLqCBPb3BLC2JPFE9ARRGwJSzBQK5oi9GXkkPS75yahvMSDWEuKDyFOyvGawQON6HuW_Ymb5p0_CrhDIIl3508d6JAsHmDWNqPCamTDgDaVYMV0TcPdeK0HmYS_MQo8WqOvMjbKpvxBHP5QYZyI7epfx7rW2zL5GcVqDs3eA_BdYUuzCIGA7oUc8tk_-4Z5hRNVqyHRzfp1Ynw66mj2a6aBRbUN0Ptaovb5skj92S2_rcLfaWgujJGWhQoQvTtNf8uyAczNp4Tvvtq89bxaRDWBBEWEg6LzLOwLjiex0pE2ltQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7bfdc0c.mp4?token=D0k_P5deyWuIdRZ6Gt9DL1bVCWyhM22HcHrcEqpBDLqCBPb3BLC2JPFE9ARRGwJSzBQK5oi9GXkkPS75yahvMSDWEuKDyFOyvGawQON6HuW_Ymb5p0_CrhDIIl3508d6JAsHmDWNqPCamTDgDaVYMV0TcPdeK0HmYS_MQo8WqOvMjbKpvxBHP5QYZyI7epfx7rW2zL5GcVqDs3eA_BdYUuzCIGA7oUc8tk_-4Z5hRNVqyHRzfp1Ynw66mj2a6aBRbUN0Ptaovb5skj92S2_rcLfaWgujJGWhQoQvTtNf8uyAczNp4Tvvtq89bxaRDWBBEWEg6LzLOwLjiex0pE2ltQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بستنی اورئو خونگی
🙏
ساده، خوشمزه بدون مواد نگه دارنده
مواد لازم :
🔹
پودر قند ¼ پیمانه
🔹
خامه صبحانه ۲ بسته
🔹
بیسکوئیت اورئو ۲ بسته
🔹
شیر عسلی ½ قوطی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/665521" target="_blank">📅 08:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665520">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
تصویری از مراحل نهایی آماده‌سازی مصلی تهران جهت برگزاری مراسم وداع  #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/665520" target="_blank">📅 08:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665519">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1kdJ0uGotgyReR_S7j6nTj6SAGX9_MV6aUpG_Adz7RJYc6OVLsWyJHWr85ZNZbIWzE2T420dz_-h8cfY2UQnB6ZXkwvN8Shu9TapJjPAZd5yUCNFFB0YOdmg7cEe2TQOfbbtHL54HqJetMmDnOW17lQd4ZbmlckDW2kJjjZ2SHHWpRZW1sCxLkdgkuq3BhN58tp4LWWJdLNVL__WdBSPmnHZDUx5K775eSU7m7AW2d_RMJskFSUisiDmGpkUf54IWxufi3uqgNDAjErlORVKHD1faFfXdHt6XYXFEG33_XCIAGkLPZdAtfkVXADXu93D3z6MI4I5pouAI3Z18Ei0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امن‌ترین کشورهای جهان در برابر حملات سایبری
🔹
در دنیای امروز، قدرت کشورها تنها به تجهیزات نظامی یا اقتصاد محدود نمی‌شود؛ امنیت سایبری به یکی از مهم‌ترین شاخص‌های قدرت ملی تبدیل شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/665519" target="_blank">📅 08:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665516">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn-_WMZHjw3gLDF1AbUPrJKKDZakZQbVOETMjxbyv9tSnDXAxzupj94sRh5ywF2YLqg_ue9PztKpuxkw-HCKm3Vs-fA-Xv65EIGCUBtkpQ73WXV0SMafFUrZjRjlAslsF7z6JeHXwxW5mWVlsA0I0cHj8JER6xhoJowKX_fVsE7-_1NKjcBrCRxxEK8tGL5AKqEEobITi3pjk9-ueGAjHRtRy_1G0YEpY25RtDcrWowSbgkMXIl-Caa7TUN0tEApgUdnp6Ac_AGk-tgdzrG5bexV7ozLe6ZTRmoBFXZ-h6JES1NsfU_tihbS0jslUOUnqBVKk9RTmp77FABHS8_Zwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از آخرین روند آماده سازی مصلی تهران برای تشییع باشکوه رهبر شهید انقلاب #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/665516" target="_blank">📅 07:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665515">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIQYGSPIJOkU7J3XyQU8imrgQPckhYMF4URklRUyvfU-9ubcXMQpp-FPH6clc84Go3CgDpm1tTt_-6O4YWS44L-rLNueq8PMLDZM8oslflhAMdb6ftJA_B7duzMDh3QzZKEZAtpmD8jSN9aYuJ2_bhHpi7C-MGAMlroGI2zILA-1cQ2GsuK3lH49nqaVF_1Dbw5bkHJMXG8yeuuyoFTIAVQQs7yrsfVf4VevUT8PTNxLXX63KnuB1Yn311MPUagermxHEbN8V1tIOoBjSxJrZJoaxJAYC-I6UFmVNZP11mJfBM3H53yHDupijlSUTEtjFnQQHOUeaLJYobc_z4KzyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/665515" target="_blank">📅 07:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665514">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04d6c89253.mp4?token=vqoNrogCtSSY3wY6ObfwYrZTaLnT5ZEtK_qHKo0ypKWfKBdT1PBM-Z_qCTMPHNoWVud5g2P9XZdS46jX9JHoxhQpYUAZ7-41eRhXYAi1-gyA1YWUGwEaJiMnhmemAYV6z6INs1HGeIcWdC5GDm4g9UUkO8nZyrg4r_aEHZpTb_o09frIwchindyRq-OfQC8wsBMmzjv641kNVZ55aI4dmG6FqjSquCJP9VnI9DupiPfN5OBGJUSYG2K0pLZxASVE_RUP2aUGhQNR7mtMfFIXShDP4suiLgtJw7KylChiI1OWjCHMexveYPEifCq6jkAAKZNkGRrSmPqNkAQwKknYBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04d6c89253.mp4?token=vqoNrogCtSSY3wY6ObfwYrZTaLnT5ZEtK_qHKo0ypKWfKBdT1PBM-Z_qCTMPHNoWVud5g2P9XZdS46jX9JHoxhQpYUAZ7-41eRhXYAi1-gyA1YWUGwEaJiMnhmemAYV6z6INs1HGeIcWdC5GDm4g9UUkO8nZyrg4r_aEHZpTb_o09frIwchindyRq-OfQC8wsBMmzjv641kNVZ55aI4dmG6FqjSquCJP9VnI9DupiPfN5OBGJUSYG2K0pLZxASVE_RUP2aUGhQNR7mtMfFIXShDP4suiLgtJw7KylChiI1OWjCHMexveYPEifCq6jkAAKZNkGRrSmPqNkAQwKknYBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول بلژیک به سنگال
🇧🇪
1️⃣
🏆
2️⃣
🇸🇳
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/665514" target="_blank">📅 07:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665513">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
تهدید ونس، معاون رئیس‌جمهور آمریکا: «اگر آنها(ایران) سعی کنند برنامه هسته‌ای خود را بازسازی کنند، اگر دوباره سعی کنند به کشتی‌های تجاری شلیک کنند، این محاسبات ما را تغییر خواهد داد.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/665513" target="_blank">📅 07:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665512">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
شکایت ۱ میلیارد دلاری از فیفا به دلیل حذف ایران
🔹
لطف‌الله کاوه افراسیابی، شهروند ایرانی- آمریکایی و استاد سابق دانشگاه هاروارد، به نمایندگی از ۹۱ میلیون ایرانی شکایتی ۱ میلیارد دلاری علیه فیفا، جیانی اینفانتینو و مقامات این سازمان تنظیم کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/665512" target="_blank">📅 07:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665510">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07348fb68b.mp4?token=Ktv8itJtwaDq8L4UDeqSL6Scja-l3npB5np_xYwwcwxvU7UjJnXoYmRPkuUGhnNCCZvqTsy4OqEwCc-TNpmS3GvT0qRZPHY1WHHW_-S2lZvrOwpXzMSztbaAsoOE79xy7_gXJ70Oc-PVv_ddv_9btw_DT7uUGju8K6cw1QL4F_N3tDlNCk8YYIIxYTDdDBtt7IYOcV_K6qGR2Q2stYsQauX3l8xbL-em-U8yQq-KcwVBZd2xSaaSxv9G85a7WqOMCWOJa12cqjiOlYeLZWJK3NCJBoVK7z0Mw93otJ6ysb4_swF7ny0l_xmKKK_aMdQzhUL-kSi8pDLF5WZBFEX5vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07348fb68b.mp4?token=Ktv8itJtwaDq8L4UDeqSL6Scja-l3npB5np_xYwwcwxvU7UjJnXoYmRPkuUGhnNCCZvqTsy4OqEwCc-TNpmS3GvT0qRZPHY1WHHW_-S2lZvrOwpXzMSztbaAsoOE79xy7_gXJ70Oc-PVv_ddv_9btw_DT7uUGju8K6cw1QL4F_N3tDlNCk8YYIIxYTDdDBtt7IYOcV_K6qGR2Q2stYsQauX3l8xbL-em-U8yQq-KcwVBZd2xSaaSxv9G85a7WqOMCWOJa12cqjiOlYeLZWJK3NCJBoVK7z0Mw93otJ6ysb4_swF7ny0l_xmKKK_aMdQzhUL-kSi8pDLF5WZBFEX5vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول بلژیک به سنگال
🇧🇪
1️⃣
🏆
2️⃣
🇸🇳
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/665510" target="_blank">📅 07:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665509">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
نقشه راه حضور در مصلای تهران برای مراسم وداع با پیکر رهبر شهید انقلاب #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/665509" target="_blank">📅 07:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665507">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K12jm8ZzuebCExSBNYn51XA9HS-gakWMhWtEQvKgiDlICc3Wf7mKaMX3ON18KMKxLWlf3D9qRek8DvnbmBV7ST3tThb_t2EG9QAZrb1MEiZTypUvathaMyNwNWbjE6PGgcDApbAEq9z1hxT-n6EJCLsmCWQkCp6OJzhX0BK8ckdq3jdhbEhFbNBStQnFWwjdDJAZb-6be25DdK-2kWiekjplVjtztJaBZRJULBuUFIKA5geRVTUzyaD8rz4Y0GDyDxt2ewUf0vzmACiKTgGw1vQSNfiCrbuJLrUCSj35i7KyWgIf8WV1vx-EjTrWqVlZnU5WzbNLzy2_jNv1QFUhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۱۱ تیر ماه
۱۷ محرم ۱۴۴۸
۲ جولای ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/665507" target="_blank">📅 07:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665506">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/os95eWi6DrYpoBZpn501bgnk2Qgl3gTnhBJX_BXWIXWNZaEHqDRn3QeFaPHUYQ2CAdlMHmzXLub-fo8MMeRCrAHJo-w8_h_xilRkAKiRG-yTpk3Y64S6EK6xjNBuJrvhaFW-Bp7mdTVKqiOxStgdmFY3j4sg03-DjqnZxRtNG0T4yl-x5AJFiiwYRf4NGv6C0To4wbMwqB0ADFEwe2dK3ay5CrkI0NRDDQZAm3j1vRKpfmYg_xNR2QW2bti3qj29EStmwngvNdUFpJqJkJzrz7U9_yy-g74R7e9NX8jf5fTbLNB-QdoX4kQCsXsiP-3NpJptWgfM9PdSd-b2TeF_fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
پولت را پارک نکن!
پولی که راکد بماند، فرصت رشد را از دست می‌دهد.
با طرح درآمد ثابت کارینکس، سرمایه شما می‌تواند در کنار نقدشوندگی مناسب، بازدهی بیشتری نسبت به سپرده بانکی داشته باشد.
🔰
سودی بیشتر از بانک
🔰
نقدشوندگی مناسب
🔰
سرمایه‌گذاری با ریسک کنترل‌شده
👈
برای دریافت اطلاعات بیشتر کلیک کنید
📄
#درآمد_ثابت
#سرمایه_گذاری
#کارینکس
💎
با ما همراه باشید
اینستاگرام کارینکس
|
لینکدین
|
تلگرام
|
وبسایت
|
اینستاگرام آکادمی</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/665506" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665505">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromباروبندیل</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbvN2nsg7Bf9fHEmLqtQ92crxboR7iVEo3dDdskI1aEtkof_0HxXY2fc2OKSEr5QQU8TODazp6-AqazGb9lZnbPNmKV8WtER-mLFDdNg4FfdYxz2wa21QQp8rQ2V7xrbR6d0tNMDfX-1P6RxaXWf2vWi0wkwllKlc7ERwUMOBEjzWFPao4rFoBT7KzPhu-XGOzCpFlrNaMuzRZ9BmMUpYegXtjZBKHB2_ngTSHv-u4UnoublZEXtVC4SYrajEJz5eI491g7iq27h_E_hh6gPNGz4rp_mbAqogbBQ7UP3TDWy17yrCVhNlKufHdt3GpSCjm7rcN8Tu_RuiVUm_t7kSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
باروبندیل‌ت رو 4 قسطه ببند
باروبندیل
بزرگترین و تخصصی‌ترین فروشگاه کیف، کوله و چمدان
🔹
برای خرید از مجموعه باروبندیل، امکان استفاده از سرویس اقساطی اسنپ‌پی وجود دارد.
🔸
امکان خرید مستقیم و حضوری از فروشگاه
🔸
ارسال سریع به سراسر کشور
🔸
تضمین کیفیت و قیمت
باروبندیل؛ همراه استایل و سفرهای شما...
@Baarobandil</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/665505" target="_blank">📅 01:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665504">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
وزیر دفاع آلمان گفت که برلین خروج کشتی‌های خود از ماموریت مین روبی در تنگه هرمز را بررسی می‌کند/ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/665504" target="_blank">📅 00:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665503">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRQSMLHdVZzwagHX24LElI8HNwZvcrNFiwR3w4ap2gzShtiNxhh8Zz4KqRTeH4KtCM6L0N-9wWU37kxm55ZxiGaSES38UgKy9Eh1GpnGNhtcfCCzmkQlsZ12LJFIwMu7eFPcQ5xocHWiCgFP0eoXinr8cGh-K3IYbsGfWN6FqGGqc51HGIpnbUpzoWet6NBrX2NGi4LUWEv1RJYnWsO08ihMJHZkohfncogm0nFz8NasxviHMTy8oj2SVQ3eg4hl7hJU-L4_-24U5Aj2lH6TeuKyfUg6Io24c8fv8dmeOlXEmBJG9Szi-B1f7AKRcFYgdutClmPk0Bxc1JO1e5aJnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایرانیا سر شوخیو با باراک راوید خبرنگار آکسیوس هم باز کردن
باراک راوید:
🔹
این روزا یه نفر (که فکر کنم ایرانی باشه) داره خودشو جای من جا میزنه و از یه شماره آمریکایی تو واتساپ برا آدمای مختلف تو اسرائیل پیام می فرسته.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/665503" target="_blank">📅 00:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665502">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa5a9c7c5d.mp4?token=tQq6sIkzOzEzTNa16cU5BIHOuOB9bprhvHXryNxmr0fdO16UtuuSH6GP1PIFnpVmSPh_tq3x6KcnI_2A-Nl3JHAdQs90oyIz3kUAuFqvsy3ihPvGKKyYU4w7-5YDKAzsj1Ceq6qwjphlnneAkmJsfKgtitiIbuKsbFqSLWR50m5BxcEpx2cB1nLw8jfuCdVhElzcEhLxr1UepOWWoqVNpwl9t0Ub64IJOgY4F5UvZgZlwhV6IxBBBvdsH8ZOecCTqEjNsYSMB3GyWdZ1Gc9ba3w20w0UTzyyT5xTpw9poDycmPee3XqHsxhuLSEDpgiRlFDnxzug4esb41C4GM5uRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa5a9c7c5d.mp4?token=tQq6sIkzOzEzTNa16cU5BIHOuOB9bprhvHXryNxmr0fdO16UtuuSH6GP1PIFnpVmSPh_tq3x6KcnI_2A-Nl3JHAdQs90oyIz3kUAuFqvsy3ihPvGKKyYU4w7-5YDKAzsj1Ceq6qwjphlnneAkmJsfKgtitiIbuKsbFqSLWR50m5BxcEpx2cB1nLw8jfuCdVhElzcEhLxr1UepOWWoqVNpwl9t0Ub64IJOgY4F5UvZgZlwhV6IxBBBvdsH8ZOecCTqEjNsYSMB3GyWdZ1Gc9ba3w20w0UTzyyT5xTpw9poDycmPee3XqHsxhuLSEDpgiRlFDnxzug4esb41C4GM5uRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع غیررسمی: مقر احزاب تجزیه طب در منطقة «ديكلة» در اربيل هدف قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/665502" target="_blank">📅 00:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665492">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHb6S9mVnZhitrgjk9krKYo4hcYeK8ady4CAGWeOyGoCpUOckHGlh0j3pXjkAApjxQ4YS0rCv6fOBjCz7HDGg871FJMgFbTeFbkDAtWJj8mIYLcBfWYWA_WZQC6Gj62lZ5PZO3veGsBByqvXt5f3GVFMH_nBaP8CtnRUr_v0wI90k-v6KWiPV0PWT_sXWvKksRbjLFrW2aAOdzxBHQtpXXrMRvGXq2MZprzkRZCBw9d-YUO1MCGeBU4ML9Bq8kj6YIn64coP3JNWZ4RYH7QY5_3ME5EkRgWea0mQB9D5UIvsZYK8BkFAi81yP1hlfRFMixpPHOtlmRu5OywuwM2qqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RbyzXI9lA8otjORQbLNKkmcJyEgl52IW2Wk6fmJssxiqBbsINdyio1zW6q3WpOPMUaQzRjA_gdYdlHJQW8MHmqamk6pYgm7jFhbmEm2r3VVDb6rLaxmWoGTgItuVYTpAm1ER5W0WBuNhU4w64ikvlHoLHp3JfGTSm-B7bapggBpT1aSt2oePj6msz-mRErAttE_Y9xY0xDM1S7-2oryC3o7qcVoTw6Gh7kwUfZcXjtdHroEw02feMYQV3Z-2heh1jJ_KjkNfB1b8Gl_0upfSXuvTP6jef67K1IO5HMzJIg-ZmXFmmAa2mDYpGiYnWzil-bKRL27fVvAE_ScnYIgUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbsBmnL8_GQkirNRSYkyM2Nuf1s0__D6vWt6XpF8xXiVh0Y-DL9qZmEFY1otZ8fD49K74Id2LvPAW61ymiVRkj553XLcG8nXN_DTqFDPZIk1NFSuq_a7wIGWWNswMOaFe8s_Yp7cOtiB3mKIVwud5NxFFcG8pWIx4kjLAKw9sr8O8RrYDfGyaJrMVMMhCbMWiVPjYGY7QShT9aVl_PqVc43jG1OM2JS_VdgMZ0jnEJVb5ku82isJRzspjv_68RrXDKOYoMpdjADfW0gCjEEJLT7v5MiII8tWqZVr-Z9dPl5Z8n-TOOxpeeA6hnboFLWaeAOVXWnO2asN4JDGBd3yjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5ez5UnAnex8VLb6zZxG7xJ8KS9lXSfAb8sy9LJtw2OY-DJV0IsuM4gG97OHBEErbstC9_jk59Oou_8POXOiaBOIAig_bK0QbsQUW9B_RsN-E7c41uB8pmFIiG-jJk6GiBNWE_fcJHl2J96fvfUFnMWmPNQIrfO_Ce5NYR-GDAL3Q12J-Fr-Jw2J55Se-aAbtVl7uPo1gtzfLZP7aVQ-k6L6awfAgOuWJre-mMiA-uMMiQlda8s6uCDGQrRdYajmop3R-VDZ8Xs6puqzv764l_GsTTRgjVQeqvpIjCYTU_W8Hc_goVqqU0IM2h0jXRSJ2XoRcenxz_MitJHRjnoyYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ns2SxFeZmkUZrnSiHAR-hk-XgfkIQb9eLgyYobWqQB4_gslmlSH3aydtcTWKS-N4b1A_a3zSey29eLNsidD9JFCRlFAJJg1UwLEkkSv_7fIEmZCsqIGa94Y7D6jt0yYFgdBvnx5Koldd87210IturiSk8GF0E0De5rHE0MuAuI8itbHA-upHJ_ja5pdYTvog6QEhRM8lC9wXKPS9z-CbwUg14ck8Kd35P6FtLyPcRoWXo7XniGvBpN_hcEPIxe9qpJgTtGik8NZQOwZ9jffKhqOwM8lk2sUSa8DAc9uEn6wRIQtcKhO8J7AFnpNc4SKtjvgGabPTOUh2ojy4qD_MYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qpRJ-TQMh8wVKWK3ZxjLeWytFkAxeE8JzDPaRAVf6xrYLy6MuV9GI8GY21qSD62Z_t-QGGWfRI8uA6a9t77c8NfksIbUkRxz7iHx35GUud_ebiP3iLkL4ZHbkyW7Tl86J6GZJGk1P-5HT4iLnlCHAoRAVGfITN57RCHqohBUtgunuE8AIKues7agDk6WO8OBA8WjzyrJB_h3O1UxG1u16wkV3n6_0jrkB9h-ylXDb_5K43dZOj77Waw1Pgww-qCABTl1XX7_QbCJtEFMYecJINbnHK-qpuazZHgAf9mDtXDOQEDeibP3qENziykt1e-DryC6-MlDsWYrhC394x2wpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzXfEC3FB3aW2ZCDmYBBOYIxjzkAhtR7hN_nbJBxzv0mEpD-bMHEDwKhG5sQEFzgnLZHeyecFFNwSCmFCfUdTsQpviE6Cm_Ve9zZF2Mtw27dqoukEhSCXR5irSvZVSnROjytsJAay05vRk7T5sdx30dBBvmQ6YzKZXc0BgleDTvsyZZhKxHRdzGyfJMU2Tx_-jZoAmKjL9FIYtIXqUAQOjQa-GE4MvLfzR7bDuuZSgHHDlU9chYs6navaQk5M2jnXxcWorISclA-91qWaCElPy5OAxwbQy2hBB1hTtoBceo0Br0F5qlOpPcufOlLinhmuAq6iH11lzKdRAi3PQmMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJN4bg7pf6ctrcFqdIuYqOfSjZynVjT9qjbLh0XFH5g2FYQNufZj2LdzK_nPoNB3jvD4nsSA7idoWOoAqcukwj81ElXGHeY0SZtzmP_ALw8gcWudg9nnU8dpxVB-4IdKBAlQDf6nUgnFQBMoYNeDYKKGvMMGk_RJ-gTkTawHWXWQIHTmZHG5SCYHlKaoDkZ31URyd3iaCnn_h8-Bmd7ESfzMcIfevXH66mgyEmt2ZG7Nxj0gkNSgnngJ8zLNK0DVUP7NOnGJ8kbieR6VHIGfhitG7CE99YnMPL9nzz8_WReQFK23b_1g38wLN1T3A7P_PkrW-LEP7qAUp1-DBtVhaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xlh5p49ml4T9Na-sCShpaoA7LkOkdyicM7gbv8TbXXuUHiPTuiBcsj-CbShrc7-VFiPjjNwTQSEd6JuA0in-Iyu4QLX67NMtWMBGSdL5OarUTs-1pGuAwuo_1BNx3Pf7g6iWpUfqdIfKOvEK648t6H851pF6D1hNFoURsbwj3iZyfqPim5WWrQvsxpIWKY-O_kRlbIVqIwxZbxZ-Mk_cdJrlJAxK5TWtN_gaUkl0MMUG2WFRkflvlFInUNgSMAszPEYo2KqTbzJFMdBGBF2h6gVhb2dNNYfp2shHMNZLV-SMnT8Q6FOnSNzWDWSKZYPDwd17BtWSv6H7jkfzc9vXQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZZiLdOkQx10gscMpcUHACSfxM4Lpty1JcPG2kuJSMgPom2dh8eb3zqtQ0oJqjXO2FmWHkvyUxG8yZQIjK6bWAEfOCN6RaWJ4u3Ee09OxHYAZPo3nx0XiDzY5TYaBHWq79gnHUeHTFi2QKLYPuusHs4TlkCcTorFfIkGt0SkLnH9TjuMh3zGE1Hl9Ln7_oTozsb0-a-lBK-zEvK37uqKtVBeNAqTNFXEl15KESJqWgBjY31BGr8zu0d3-kKJKBuZoEz0zhFmsI7PbqjHXcTghulIm5UxZmD1Rje-U78C1hZtbS06kSB7SRrzpoDFJ9v5B8ZqWugpRXErme7rzcCWiaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
طیف جادویی انواع رنگ ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/665492" target="_blank">📅 00:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665491">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f12a6b4bc.mp4?token=beTc1WK69TVQcFrtdmbSX6WNLuzsIKvDYpcclFsvY7uAlYGEMo9aOOqIwz8Lp24a6a5b_tG_tSOST8bPGmIC6qNROp2da--9L0i7yBRxV6ASwOAvgAY-qry38QKzHnP-18jZFcy9eEGsXSCYqyaArgMXO1Xt-oEuIrInIucOEBtd4_p_A0axzJBtm_ZrOSIIDyBGczE85dCvfvUIpauzKwzwZqvlKLUV-Oh3RBoryuLL0PX6QxxJ1C5R464TiH6muL3f0a9Q02HH-n8bi0SBHKCDON3_0fNBRC4iuhG3u3jq2JdsMxZ-CxBVLum8L9L_W38RAT5frERiPvi4C6voCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f12a6b4bc.mp4?token=beTc1WK69TVQcFrtdmbSX6WNLuzsIKvDYpcclFsvY7uAlYGEMo9aOOqIwz8Lp24a6a5b_tG_tSOST8bPGmIC6qNROp2da--9L0i7yBRxV6ASwOAvgAY-qry38QKzHnP-18jZFcy9eEGsXSCYqyaArgMXO1Xt-oEuIrInIucOEBtd4_p_A0axzJBtm_ZrOSIIDyBGczE85dCvfvUIpauzKwzwZqvlKLUV-Oh3RBoryuLL0PX6QxxJ1C5R464TiH6muL3f0a9Q02HH-n8bi0SBHKCDON3_0fNBRC4iuhG3u3jq2JdsMxZ-CxBVLum8L9L_W38RAT5frERiPvi4C6voCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم سنگال به بلژیک توسط اسماعیل سار در دقیقه ۵۱
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/665491" target="_blank">📅 00:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665489">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MD6RbEhG3WUANFXgKDts7639e5jhR9vIg3d6r4zP3VPi1pwykI2WXcumOMWjYkXPKLSr3shb47a4X35dMtGDzrAkrH-uO8HKtMdFAsgjV0GDtTBVCbN9l8FuvFDMg4_MLBA9rTjyHjnMyAYhr8kK-ZBvRw3V2NM7kThprbg84-pYACyljmntg2DH9MhaRtW147s7m09RyJHTe8lzLzfkXBGxe9Cdl0TYJymVwcxe6WXu2a7PZ9kdXq5kM5OcnPCSOI-4oqABIfsmSeEUrvs-cwNjKWqT0EqEUj2BNLCMSJL2m6FdGH_8wSTAXCKhtukGm6nb1mLT1bbGjW2T8UKdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع غیررسمی: مقر احزاب تجزیه طب در منطقة «ديكلة» در اربيل
هدف قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/665489" target="_blank">📅 00:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665486">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/621185e0cc.mp4?token=p8A4aD6mZFOfhSwGTR-NSU9nb2OffPYBE4CGLEWMD1tkbjFvxwhSEZx7fyqyBDArhqqtxqLAvnWwOMPELIuHpPahuiIERlMtwh-bk8ywazotlrNdTC41ZYnQsW8Oz3Ely9v4PDOvrE5sM66IwS9k_L2A7SWC6jxjQfqkqq4bUoyOGfgdRovIZCObsJhaDxvHdG3QHs0WHqx1kby28-yQRBmajOgehwVS56k9Za4qrChn0dpA2k0f-Z_4Qxqrj1z-Mmj6q_gDC-7Fdp2Kf1DGU_lN5NjXWocVM4X37do9ag4jAwkVl5-ZaR1AGe3ZQjwS2Muu6xLNQIO-f5SGFW6uWjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/621185e0cc.mp4?token=p8A4aD6mZFOfhSwGTR-NSU9nb2OffPYBE4CGLEWMD1tkbjFvxwhSEZx7fyqyBDArhqqtxqLAvnWwOMPELIuHpPahuiIERlMtwh-bk8ywazotlrNdTC41ZYnQsW8Oz3Ely9v4PDOvrE5sM66IwS9k_L2A7SWC6jxjQfqkqq4bUoyOGfgdRovIZCObsJhaDxvHdG3QHs0WHqx1kby28-yQRBmajOgehwVS56k9Za4qrChn0dpA2k0f-Z_4Qxqrj1z-Mmj6q_gDC-7Fdp2Kf1DGU_lN5NjXWocVM4X37do9ag4jAwkVl5-ZaR1AGe3ZQjwS2Muu6xLNQIO-f5SGFW6uWjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش رسانه‌های عبری به تشییع باشکوه و تاریخی امام شهید ایران، سیّد علی حسینی خامنه‌ای؛ ایرانِ پیروز و قوی پیام «باید برخاست» را مخابره می‌کند
کانال ۱۵ اسرائیل:
🔹
مراسم تشییع رهبر ایران، رویدادی عظیم و بزرگ‌ترین تشییع تاریخ این کشور خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/665486" target="_blank">📅 00:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665485">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8v_sNjkl1jPEV7CWVjtUXO2t4v_H3eRd-Y05O1JrkZSpWUhjcWxosbkZVI-fEULAFfYD-zDkbmqrlVaaGhCxJAWA295pDqI2OtfMDwhiQkLuJhbImQ2ExifwgdDcE5O4-Qr8PjdaSKuOfn84nXCHsQhqVDHizncfe8BfBXOkhWQP7_IC4EOXnguMNFJ2omrAUGSBsSjArXq2yaZqssc5Xzva1sS91qK8xXjB_huiRz5oWuBNuBHC987Ojj2y15ZpkqTW5wfKRSqk_7s8T0PxCwVP40jdbYtI1VqyC4WusCPkg9GOysEONi71SSwHYakdkyixM5QqvOo99dxHoAfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه راه حضور در مصلای تهران برای مراسم وداع با پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/665485" target="_blank">📅 00:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665484">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه قطر: طرفین توافق کردند که مذاکرات را در دوره آینده ادامه دهند، بر این اساس که زمان نشست بعدی در اسرع وقت پس از پایان مراسم تشییع پیکر آیت‌الله خامنه‌ای تعیین خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/665484" target="_blank">📅 00:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665483">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31a770eab7.mp4?token=adGeUAsgqUmYki1awdpH18pTGp8aOPIPzBpT3uYSGYe4XIlJmD8p_jlQLVywaa49XI31U8mjKgUNkEna-YfJjAJu-1dR6wgVqJ0ozyWZkqCQYs6Te_eiGGCUBLKJzla5K-jT4Quj7vYyeLhk7IorQNsjKl0EnDGFFoJlZSzJL07xYSpIIXnOZRT4wZ6K1XawweNfVRTTxa_th2QTTLYSxvv2dUgy3P8H3RdM4b5DXc99nguklsOZzd0RbBUr1NICMkeHEdGRZD5xBRVETu8aZZtWCoOAZ1oTXTlGxHjT6AgWb7xIaefSV3g2YyYD7AvujHsbLdpv-ghIt4lpZaK_4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31a770eab7.mp4?token=adGeUAsgqUmYki1awdpH18pTGp8aOPIPzBpT3uYSGYe4XIlJmD8p_jlQLVywaa49XI31U8mjKgUNkEna-YfJjAJu-1dR6wgVqJ0ozyWZkqCQYs6Te_eiGGCUBLKJzla5K-jT4Quj7vYyeLhk7IorQNsjKl0EnDGFFoJlZSzJL07xYSpIIXnOZRT4wZ6K1XawweNfVRTTxa_th2QTTLYSxvv2dUgy3P8H3RdM4b5DXc99nguklsOZzd0RbBUr1NICMkeHEdGRZD5xBRVETu8aZZtWCoOAZ1oTXTlGxHjT6AgWb7xIaefSV3g2YyYD7AvujHsbLdpv-ghIt4lpZaK_4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترکیب رنگ جذاب در کابینت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/665483" target="_blank">📅 00:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665481">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
بغض و گریه سحر امامی هنگام یاد کردن از رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/665481" target="_blank">📅 00:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665480">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-jngHLCdbjAnq0tI_AkiCpNiq2-J_114jwROQc1KMJrjn9ZGlygYs6ANLn31WoMkWByeShGc9W0OQX53FckaoYcDm9P5Lp3GQ-MQHbut1D5WOXwfxz1STl6GPl6V3Sbuki8-KxY2DSH-0z2mzZuNv8RoY8q9dvLMF6kkzn3MBmBCs6hYQ9soA356sVlVagPkL-336lF2eqIj75O0-fAPgChYs3D9ClHx7YT40CzXC596EU5eQYJA_5EUPXxcQgS9Tve2mo9wKgksSRbgiicwRjx_Qrrlf7hw5CzOO2jpPH2eLnTiAk2oecfcJPBOeJRzONoHIgv66UmDQ3u7muECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/665480" target="_blank">📅 00:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665477">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf6b1a1d85.mp4?token=kWuKVezmfuChMX2cazo9GKDsLE4-K9x-0oaGmiGAxe92Qw3y3E937JvOV7YtUYItgp-RWyeN8lA-GAic6o6QRNB4aBC3ivxDrXWTkWr9qFHCD6Ihm2ehAuVXuhG-gA6KIeVyXX3i-Nis3WjOvE4BW6ZBy9-L4FRsAfU5nCtqLo471ZWq_m1D_g1fYI4WZU_4r_txkMDEPJ05uIcSYGVGtTKVCwDvTdDMgEBJpTfFHyWSBHLlpnJ-2vDef7zt4yBLO39Mup67g5rOVw67S03FVSvt_c6JzEyg5BZrLrv75sb5TntshqeNSEyJPE-yTeOOMd7V3xrxeZeMMRMAq_TC-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf6b1a1d85.mp4?token=kWuKVezmfuChMX2cazo9GKDsLE4-K9x-0oaGmiGAxe92Qw3y3E937JvOV7YtUYItgp-RWyeN8lA-GAic6o6QRNB4aBC3ivxDrXWTkWr9qFHCD6Ihm2ehAuVXuhG-gA6KIeVyXX3i-Nis3WjOvE4BW6ZBy9-L4FRsAfU5nCtqLo471ZWq_m1D_g1fYI4WZU_4r_txkMDEPJ05uIcSYGVGtTKVCwDvTdDMgEBJpTfFHyWSBHLlpnJ-2vDef7zt4yBLO39Mup67g5rOVw67S03FVSvt_c6JzEyg5BZrLrv75sb5TntshqeNSEyJPE-yTeOOMd7V3xrxeZeMMRMAq_TC-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیارا بلژیک را غافلگیر کرد؛گل اول سنگال
🇧🇪
0️⃣
🏆
1️⃣
🇸🇳
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/665477" target="_blank">📅 23:59 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
