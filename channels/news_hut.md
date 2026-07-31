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
<img src="https://cdn4.telesco.pe/file/W-GwR4AepoI8Gx9auHL2O1X5gcndJ8DnGa47vOLyHmIfm061-mSosy22_CxTXjtNpGzuaMTKIG4npt_N0M2-719YHdoBOwgNoY5Fcoql6sAmlJAatBL-GPfBN7P4sqFqnnD4QgIhbFopafN-zSRYIFjn6EBMNIxqdsHU0lzD_2Ul23BfM0KH48_G7m_9rDLPXUjsZK3KeS5Y341cSkSPEgSpTwo8LCHtwvyaqWCJ-BA3MC_x1jyNYcG8wRb6c82yJ0qoKDBn7gf_3yXFnahdPWqZl3Ft31gPMiWhBTF87Sp9T4bFLL7oLwdRWpoL0xaDI2MRTeWjwjInceSOPD2Q2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 140K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 09:26:41</div>
<hr>

<div class="tg-post" id="msg-69288">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‼️
دلایل سقوط شوروی که صداوسیما پخش کرد در مقایسه با وضعیت الان ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/news_hut/69288" target="_blank">📅 09:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69287">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=UWcKrxjq0Fxa9ix5esJWejPd41HDDsXAM92TnJ36hyv_0F830ALPdOfRuw073KmzNPss8NoNkuwX71m3dDJbPZRCAEVA9FcX74kaSsOA0ZLLWSbt0vDGw934QTmVxWvUFdf2QqEEncPaGUQCoxAf72i0pxYY5A1JeURgpOAIRrXH8JtyHtstm6GclSB17lDtfv1kGGyet3lwojQtggFhlHxjSfD593BoQYyyeYyty2uKFGCXVTudbLnBmlMugsKKody4nulo14pjRKN3SBheEJzdfImJJLpKy5NS2mBdKXVC_MiFhF_oqRFF-QBY6HBEPL1X2yxF2dmi76Sk-PT1Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=UWcKrxjq0Fxa9ix5esJWejPd41HDDsXAM92TnJ36hyv_0F830ALPdOfRuw073KmzNPss8NoNkuwX71m3dDJbPZRCAEVA9FcX74kaSsOA0ZLLWSbt0vDGw934QTmVxWvUFdf2QqEEncPaGUQCoxAf72i0pxYY5A1JeURgpOAIRrXH8JtyHtstm6GclSB17lDtfv1kGGyet3lwojQtggFhlHxjSfD593BoQYyyeYyty2uKFGCXVTudbLnBmlMugsKKody4nulo14pjRKN3SBheEJzdfImJJLpKy5NS2mBdKXVC_MiFhF_oqRFF-QBY6HBEPL1X2yxF2dmi76Sk-PT1Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار :
کشور های منطقه که مورد حمله ایران گرفتن آیا باهاتون تماس گرفتن و ارتباط گرفتن ؟؟
🇮🇱
نتانیاهو:
بیشتر از چیزی که فکر میکنی و بیشتر از چیزی که میتونم بگم اتفاق افتاده
.
⏺
خبرنگار:
هدفتون درباره حکومت چیه
.
🇮🇱
نتانیاهو:
خب هدف مشترک من و پرزیدنت ترامپ مشخصه اگه بتونیم تهدید ایران به طور جدی کاهش دهیم توافق های صلح زیادی انجام میشه
!
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/69287" target="_blank">📅 02:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69286">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-HhNPEsLi2snIEG15-fsTWV9QnRPc1jmJcSOgLMbko-hAgZdcxdAtVyjVJvPz9UABvFyWx9kZPd8zVU__GYg1f0kTqg114EHr6U6uJTife9T5m7VLrLV3OdB1IVuImxrbtDnHePsotsLJv30pexnSp2wXDk6udNOkjRmiNSSDE0jAnksJ4GjxdLjRIY8MMK19HzpsFpqOrgEs5Q6FWIX9w51CGQuctrHohEGkDe1qkLVGH9Tz_dqVQf_gBw9FRfPyGAmWDIW0gxexiesJiFJOFuzXyq2Y7q5H0TUCHjHey_ZaeNUxxbkdiOHbXvgnYq8DES6PL7-hzq4ZdEwewzZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
امروز، «شورای صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی دیگر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
این توافق گامی حیاتی است تا غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای یاری رساندن به مردم فلسطین، همکاری نزدیکی با «شورای صلح» خواهد داشت. هم‌زمان، اسرائیل از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به پایگاهی برای حملات تروریستی بدل نخواهد گشت.
این رویداد، نقطه عطفی بزرگ در اجرای «طرح ۲۰ ماده‌ای ترامپ» محسوب می‌شود. این توافق طی مراحلی با برنامه‌ریزی دقیق اجرا خواهد شد. هم‌زمان با تکمیل روند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات‌بخش» با همکاری نیروی پلیس جدید فلسطین، مسئولیت تأمین امنیت غزه را برای ساکنان آن و همسایگانش بر عهده خواهد گرفت.
یک سال پیش، شاهد جنگی شدید و خونین، بحرانی انسانی و نگهداری گروگان‌ها در شرایط اسارتی بی‌رحمانه بودیم. ما به پیشرفت‌های تاریخی دست یافته‌ایم، هرچند هنوز کارهای بسیاری در پیش است.
می‌خواهم از میانجی‌ها — مصر، قطر و ترکیه — به خاطر تلاش‌های مهمشان و به‌ویژه از تیم فوق‌العاده‌ام که با تلاش‌های خستگی‌ناپذیر خود دستیابی به این موفقیت تاریخی را ممکن ساختند، تشکر کنم.
اجازه داده نخواهد شد تهدیدی که در ۷ اکتبر از سوی غزه سر برآورد، دوباره بازسازی شود!
بر اساس این توافق، غزه سرانجام در اختیار دولت جدید فلسطینی قرار خواهد گرفت که در خدمت مردم خود است.
این دستاورد شگفت‌انگیز را — که همگان دستیابی به آن را غیرممکن می‌دانستند — به همه تبریک می‌گویم!
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/69286" target="_blank">📅 02:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69284">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYTlMFlEgL9Ie3lcl17RAvWPVX-EfepAljuvybhvIoAP1HFIaePKAbpWtexUMbiuespyKlJ3ME1a9vPAvueNhbCGoAx0kUzgfcllgGsO4KNHeRB3hsZQrGGWm5J-Cc8ZZ3T4YcsDx45Xo4zwQlMPsOmQOWlUhiGkNdHQz3rMB93H4qCoEVMLj2qZXWYjyyFqF7D-k_oU8nOUenbJi-eEk1rNZMbTroQnN5aliPf6RJFZlYB6jDFGaDcpoRTOklRwd1k_cizqZQ7fxJtfzeFS7wnR0x_9aujvuALwBo1xgduI2b4kWExvX6FG-Sl68HlxVNF-DE__M81kEIlMcpj15w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=NvWC5YefSTi20EDfrIADZ7ZCl7Pa0EobV_kGwInNB7_8zG3rOYM2FBgGuMA1Wre7Zy6UtwmC6Uc1SHaXpvGY67jiSpqJxvY_8lzQE84LQn2-L2SZmg_ZCwDy5PE9UA4yhqeIZ5WZJ0A3R3O_K9YgE2sk0doNIZR376yS2oPO4M_tnYhhb6srQE_U5aCdl_NG_FrX3d8AdpEOi-9jLUDRddnFCLEthoAfguhBvnRnuxSclYIqyDK53eWhzU6renGYoOS3J2DrvPV_1FkPheH1t1JnEyH5igZSVod33aq0uCxco3ef89wbGg3TS1k_o5PmqAZPiTKwpm9GfYuQOmCdog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=NvWC5YefSTi20EDfrIADZ7ZCl7Pa0EobV_kGwInNB7_8zG3rOYM2FBgGuMA1Wre7Zy6UtwmC6Uc1SHaXpvGY67jiSpqJxvY_8lzQE84LQn2-L2SZmg_ZCwDy5PE9UA4yhqeIZ5WZJ0A3R3O_K9YgE2sk0doNIZR376yS2oPO4M_tnYhhb6srQE_U5aCdl_NG_FrX3d8AdpEOi-9jLUDRddnFCLEthoAfguhBvnRnuxSclYIqyDK53eWhzU6renGYoOS3J2DrvPV_1FkPheH1t1JnEyH5igZSVod33aq0uCxco3ef89wbGg3TS1k_o5PmqAZPiTKwpm9GfYuQOmCdog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار عجیب نتانیاهو با یک سناتور!
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69284" target="_blank">📅 01:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69283">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69283" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69282">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromلیوه</strong></div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/69282" target="_blank">📅 01:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69281">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/69281" target="_blank">📅 01:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69280">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">▶️
تیزر جدیدی از سینمایی Spider-Man: Brand New Day منتشر شده که دیدنش خالی از لطف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69280" target="_blank">📅 01:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69279">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-jgn4McnGbfkKBqgKnfRKvH0aLELVdkQLtZ-FX3x0IWzLhlqwFq6v_ue7JEEgEvyLaN8Hs3SnUkUqhcd58I1U89XebJtKgEThqXHdY41QyXh7x7dV_OkPvDEosuqA4T7uyHRVBtdpllzWn975-bTZx7DR29-iw_MSbYA_kbIT3qvX1q5ytWNoqAeW-bMXIppm7u_vn4zi4WPGEs1_D51T1h-cZ1toaGDXalYBk9S7HHPl4KX7lNSNIhIg0iW6c-M-6lkh7K96zJIre0pWyDySHC5nvTPdjku0TAOlY3vFGACLe_h8yDYBV8dFJb9-6pqZ9pVSSO7TVHXZ51U01kRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
«آمریکا هر روز یه جنایت جدید انجام میده. حمله به خونه‌های مردم عادی توی جزیره قشم، ادامه همون جنایت‌هاییه که قبلاً توی لبنان و غزه انجام داده.
آمریکایی‌ها عادت دارن هر وقت توی میدان نبرد کم میارن، با ریختن خون آدم‌های بی‌گناه جبرانش کنن.
ولی بابت این کارشون، تاوان پس میدن.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69279" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69278">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba260d124.mp4?token=ZjXp0E8KdO1mmPySwHypSWf1r6RYcz2i7GfCf0uQgy4eYWMKzeq0UEhVcMHdgpj16KlX3t3MScoZB_3C1UECdWFpGR8et2AdsroxQNc0tvelP27-ATIucuxtY1P1-CBMndEaxevsuLy-2ZnemH2CDy2ztHEyoKRw6kcuLJjAhzapdndt-zp5L1pyys87q-yrb4OnsEG9-5Il7U5gRGyf1Xo3lnzc0ns-b0Lh-waJ6NFZOUm40ies__UxbYZCFY-DjgtV-iJzCNlxJUYU-rNUKfL7vSYQhJL-2-Cybl3ytAQxRrcJsk376UDxA14Xb4Jp_3-ULnFThgOeSo9UokOAFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba260d124.mp4?token=ZjXp0E8KdO1mmPySwHypSWf1r6RYcz2i7GfCf0uQgy4eYWMKzeq0UEhVcMHdgpj16KlX3t3MScoZB_3C1UECdWFpGR8et2AdsroxQNc0tvelP27-ATIucuxtY1P1-CBMndEaxevsuLy-2ZnemH2CDy2ztHEyoKRw6kcuLJjAhzapdndt-zp5L1pyys87q-yrb4OnsEG9-5Il7U5gRGyf1Xo3lnzc0ns-b0Lh-waJ6NFZOUm40ies__UxbYZCFY-DjgtV-iJzCNlxJUYU-rNUKfL7vSYQhJL-2-Cybl3ytAQxRrcJsk376UDxA14Xb4Jp_3-ULnFThgOeSo9UokOAFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام:
یک فروند هواپیمای P-8 Poseidon(هواپیمای شناسایی تخصصی) نیروی دریایی ایالات متحده در حین گشت‌زنی در خاورمیانه، برای سوخت‌گیری به یک فروند هواپیمای KC-135 Stratotanker نیروی هوایی ایالات متحده نزدیک می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69278" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69277">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUEJnDH9HXr0cieQHnodAj_9-BeXy74jdBGw3-4N5KjIkYN_yhL1XjhLr-zQRuJi2iHnzki6q5CvdBIqnKDBnzhtTtRIR-6xxHqfQfLOBD207ftCAiM-NgcW2s2c-QwmHK0soYcJmap0A0kn1VyBa4yBqsI8Gemf0oqSF-q13VLie2PH-P3OA23S_4pObzx_4_1N8MdV9l2_cbi74bR9mdwEpO7u9ar5f6JGoZ06nWHX1tk3wZI9ZQur9_DRVvts_3LqIaeJRd7KQnnzP8heE0-dcvUIg3Cpn9unR3Z8JvgMlRrRUCD9j0H0lm4nX1G56-Dun-oCafeDNmh4LkYBJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آی‌24نیوز:
اسرائیل کاتس، وزیر دفاع اسرائیل، روز پنج‌شنبه به همراه ایال زامیر، رئیس ستاد کل ارتش، جلسه‌ای برای ارزیابی وضعیت امنیتی برگزار کرد.
در این جلسه، تصویری از وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای گوناگون در عرصه‌های مختلف به کاتس ارائه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69277" target="_blank">📅 23:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69276">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89da715482.mp4?token=MizoIJkJDFPq5VVsjSDHPZTgzZUzNt_UeddQPb7MnKPWyFyc10-SJ0MxHCFHunORBi8oLjhYxAFXmz_FEpsExPNMgbbV-YA2bfGvJyXbh1f5NOss-joIbHcVaBxBeHLQ0eFLrtcIM5_b7Wrh1_lQp2rl3ATKEh2ZwSF92eQn_skgzr8xdqsT7gg86au29WzmpvD-bFigEslbYDC_wCBxOgOQV1yEuHnz8KUN9BllTqhjvR06CI8wOX3YcuAlLzj77keog4sSuvjSRH_D9eNoL4bXmYrndWSXB98mCIzBrfIJ_3xCsBJcauWwsQmtIvzB8Apl_L3zhyhLj9KzA_BauQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89da715482.mp4?token=MizoIJkJDFPq5VVsjSDHPZTgzZUzNt_UeddQPb7MnKPWyFyc10-SJ0MxHCFHunORBi8oLjhYxAFXmz_FEpsExPNMgbbV-YA2bfGvJyXbh1f5NOss-joIbHcVaBxBeHLQ0eFLrtcIM5_b7Wrh1_lQp2rl3ATKEh2ZwSF92eQn_skgzr8xdqsT7gg86au29WzmpvD-bFigEslbYDC_wCBxOgOQV1yEuHnz8KUN9BllTqhjvR06CI8wOX3YcuAlLzj77keog4sSuvjSRH_D9eNoL4bXmYrndWSXB98mCIzBrfIJ_3xCsBJcauWwsQmtIvzB8Apl_L3zhyhLj9KzA_BauQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش یه پسر بچه به اسم امیرحسین رو آورده بودن صداوسیما که اینجوری جواب سوال مجریا رو داد
:
مجری:
منو عروسیت دعوت میکنی؟
امیرحسین:
معلومه که نه
مجری:
کارشناس برنامه، خانم دکتر رو چی؟
امیرحسین:
فرقی نداره، اونم نه.
مجری:
مامانت چی؟ اونو که دیگه دعوت میکنی؟
امیرحسین:
وقتی زن بگیرم مامانمو میخوام چیکار
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69276" target="_blank">📅 23:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69275">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=E4JVqhuAe32Exf_E2nbTTHpxaSbBr2p-ZneLycmxxXwYZfNPf-uNPR4Cd1C8fSfkN6VfzPe-OZTI6vcEqhEyYiek1wOi8IJdrKqlXht3cfu9Ioi0IBTsGn7u4jRCjOn2wSSTaRnGJBnezs1QOh_YOR6DDnbie4I61g_YgV00aholN1u--f-mAakEa-WfUsBut9NCNv7ACjNlwqHwbX4mLy1G1QedpxiIKGbJ3fYuQfRDYzp8pPp0nL3CeI7KMYCqAQxPJAqQLZGgMup8wkNQwsvNlkHbw3j__RdT9lJwHNGoHYUJCNUioIKw7IXr2V1JDWpZk8yHTW0_inpOZidHxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=E4JVqhuAe32Exf_E2nbTTHpxaSbBr2p-ZneLycmxxXwYZfNPf-uNPR4Cd1C8fSfkN6VfzPe-OZTI6vcEqhEyYiek1wOi8IJdrKqlXht3cfu9Ioi0IBTsGn7u4jRCjOn2wSSTaRnGJBnezs1QOh_YOR6DDnbie4I61g_YgV00aholN1u--f-mAakEa-WfUsBut9NCNv7ACjNlwqHwbX4mLy1G1QedpxiIKGbJ3fYuQfRDYzp8pPp0nL3CeI7KMYCqAQxPJAqQLZGgMup8wkNQwsvNlkHbw3j__RdT9lJwHNGoHYUJCNUioIKw7IXr2V1JDWpZk8yHTW0_inpOZidHxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نقدعلی، نماینده مجلس:
با وضعیت حجاب میخوایم چیکار کنیم؟ والله جوابی برای خدا نداریم.
یه نماینده مجلس به من گفت از درد بی‌حجابی هر شب تو خونه گریه میکنه و خواب و خوراک نداره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69275" target="_blank">📅 23:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69274">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbPsQsEVkNz9xGHFrVecsYFoobWugQwnqydtiVyE4i8wQy-nEtzORAikhRLOd-kqVBuGfvgIwzxo5PZxfZd8j0FHxOxDEBLLGoSEHxjj9BpGjLf6Kf-6bHJL5vd0Zx_SmvQeMhzWCj6tK_qOJF-EhBx-FssLtLqyRY5-1hA5CsyTjgbjGPWwwl7kMM8C8KCmTB5tYvnYakZFVdI_sPk43YvgjkCxNLEH9QOtE3RlHsmpAhON3URyV4aDFnIjNFLnmlugsF32Be67o7TCDcOVgCXGNQZ79SN2fNyZEsF7n8QXl5oj1QLpwRl_Yn2E6KQPgrqYInS1cYZvBInTTPk1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام می‌کنید؟ به‌به چه کتلت های تر و تازه‌ای داریم امشب  #hjAly</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69274" target="_blank">📅 23:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69273">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhjyFT6gMZv7Z4-rRHzr9Oyel3rjCum-sVWMBAgobXboL3-kApL9ZmkR73-NPMF_3Mvp8LFLvvYh2nByIWOSiMAIsf_s9iCBQ-s1xIZ0lLOKaFhKqbk27VwONs1Hql7PpTs6lM4mPFU2BWEj36tosatrNUIbGzLxoZ69s7K3MFMckb-EfE96JpY3ypw_g6oa5T5q7n5CgzWh0cz_PQroNIu1sOBF3LD_xRtfhqkwNIb-xaENBzBRgyRfmBHl9AaUVTEdj_GAc3289Ef2lipikT-oq3tI70GD0yCPYG-0Lo6QBW3PaoPWBFg39MSB08kjOQJxIVcdGnP8q04pBtULCsOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhjyFT6gMZv7Z4-rRHzr9Oyel3rjCum-sVWMBAgobXboL3-kApL9ZmkR73-NPMF_3Mvp8LFLvvYh2nByIWOSiMAIsf_s9iCBQ-s1xIZ0lLOKaFhKqbk27VwONs1Hql7PpTs6lM4mPFU2BWEj36tosatrNUIbGzLxoZ69s7K3MFMckb-EfE96JpY3ypw_g6oa5T5q7n5CgzWh0cz_PQroNIu1sOBF3LD_xRtfhqkwNIb-xaENBzBRgyRfmBHl9AaUVTEdj_GAc3289Ef2lipikT-oq3tI70GD0yCPYG-0Lo6QBW3PaoPWBFg39MSB08kjOQJxIVcdGnP8q04pBtULCsOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کویتی‌پور، معروف‌ترین مداح دوران جنگ ایران و عراق، دیگه حتی مداحی گوش نمیده
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69273" target="_blank">📅 22:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69272">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcxD3gHylBdltS7-z2FzbdSblFwvrryUX0SCyMOV83nU76OXxeVh8xovRXchGcESvaF7ZXTELAZQ6Q76BZ0TIlgk_JQromIwQicBtSilP_9x3aqaCgRu6U4piVDCUlqmLDfIxFUwlkCzEHphmKlQjSJfSSXXq6LkqhfKYUXy4JaxoHRmF3k9lHFiQwQTmX9OZ02GK_6FQYf5cb3GI_KSiBw1rfWihv4sVHRYnQ2FQUgc023XU4FFUJMy5rm4BpTlv7O-xnR4P9UaQ-IOZguP3f9Nk64RNDuuUhJfVyMMkNtUzEVqmAEuiuylGkXYQRUKRtJNchFLdnKBhWAU2NCIEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :  روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است. طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.  ظاهراً مقام‌های روسیه هنوز…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69272" target="_blank">📅 21:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69271">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o3D_aSjMu6hcimYnpDq_vb_1zcNVKaFw4PBQJoK0dVtOcPd46rzHKTYnY8zXKwRnU_T8IB6kj7zyFzeBeYjpUkHvDRU32q3tRXPBJHKTD6WDp1AVYlyjx21TN2HQU0UgmYk7tXUbJGRXn05IEfyRuIQMRMMzpy7pTQsOx4agmjVX3h79ZDvjpr_qMrDHfEXAnY57gfvmx9qDfXeYJCx2BifI243rG4ek3lxQDXoyiFrtj3yWvHZVgM85pHgD9h37faQ2Bb75bCV_LyecJacFqMurF-Az-pAOgUmCorjCx_yO32uHEO4O_f05sFwjN69FOIZ8SQn5QjKGhY4XNydg6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :
روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است.
طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.
ظاهراً مقام‌های روسیه هنوز نمی‌دانند که چه کسی می‌تواند چه کسی را از اینترنت محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69271" target="_blank">📅 21:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69270">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=aKfwenQoRhZmgr63_e5QNrDWY-CKDiSg4bpq38szTfchGXsnc3JSpd8t6VOMfGpg0thrZ1cs3Kw_hSf7CNUvjSY7PukHmnCTgj-PBlXOR46DostSjhSEbDg2dmLPLsJ7iVCY_3lpyevBpyCf9O5T-yU56Vi8knIRlOIYWsdx89NW4ylQ36juITr37VphfVqZpx3mtU279PZf8VNF93l-QbWisfc_3abGDzUdiEw7Yr0rNT-Nmz_a80UAufuW2c65WGaa5jKkpsDM8Nagt2DBVlQFubAzay6Fz1GnHzdYRG6nEusdTZecUy6wkurWznxaEaEDNmAWGMygBw9rZgp4Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=aKfwenQoRhZmgr63_e5QNrDWY-CKDiSg4bpq38szTfchGXsnc3JSpd8t6VOMfGpg0thrZ1cs3Kw_hSf7CNUvjSY7PukHmnCTgj-PBlXOR46DostSjhSEbDg2dmLPLsJ7iVCY_3lpyevBpyCf9O5T-yU56Vi8knIRlOIYWsdx89NW4ylQ36juITr37VphfVqZpx3mtU279PZf8VNF93l-QbWisfc_3abGDzUdiEw7Yr0rNT-Nmz_a80UAufuW2c65WGaa5jKkpsDM8Nagt2DBVlQFubAzay6Fz1GnHzdYRG6nEusdTZecUy6wkurWznxaEaEDNmAWGMygBw9rZgp4Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
سنای آمریکا به طرح قطعنامه‌ای برای توقف عملیات نظامی علیه ایران، مگر با کسب مجوز از کنگره، رأی منفی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69270" target="_blank">📅 21:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69269">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=MqcDt6-UdhoGF_TnqCIahQXMIk_7IRwOBhMH2cyF0CQyBP55auIpARcusjE7uTy3fduAr_E1nMVx9uYv6PMSosu500dKf5KnYpCNQumrbWcR8VNhazwZMeJ2gjy5Wwi7qE8-VKpj_ZZbL1ew1p9XX-qJecnETZAAZc4NryMufrgMDxoEGuFlvrGWOLvmfGTMq4RA-Ega6Dqc3BY92f0BxKIwoUYQnLD7svEdQ-D3CqPsMlAiu2Ik61mVxKZ_oz962w95a90NX1DGufWVYiZU8Qc25l1i3KM8R4wAMT-5jkZ5ArVlgD7Q756vQsbqyE3iaLfyz6dks0FgmXgJ2yYEag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=MqcDt6-UdhoGF_TnqCIahQXMIk_7IRwOBhMH2cyF0CQyBP55auIpARcusjE7uTy3fduAr_E1nMVx9uYv6PMSosu500dKf5KnYpCNQumrbWcR8VNhazwZMeJ2gjy5Wwi7qE8-VKpj_ZZbL1ew1p9XX-qJecnETZAAZc4NryMufrgMDxoEGuFlvrGWOLvmfGTMq4RA-Ega6Dqc3BY92f0BxKIwoUYQnLD7svEdQ-D3CqPsMlAiu2Ik61mVxKZ_oz962w95a90NX1DGufWVYiZU8Qc25l1i3KM8R4wAMT-5jkZ5ArVlgD7Q756vQsbqyE3iaLfyz6dks0FgmXgJ2yYEag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📚
عمران عباسی، عضو کمیسیون آموزش مجلس
:
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
چون برگزاری آزمون‌ها تقریبا یک ماه تاخیر داشته.
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69269" target="_blank">📅 20:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69268">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=IcADLEpyFDv0Zd1WCJlYSymZk-ST343KSgJOhcwp_SBsPz-NMNC32L1FJyU3kGHys-7hs2y-s5k_yPBpf4qPwGErZYQX7S7hKzFKXpFtFmhLhq-WR-KFlAinb5LEa6PNUrdKvIr1MWnDrBQ1L3t3yb3mCeNLdDaU6eHMZ5CTb7a6Pw8ODuBFqs7t-UtTI74HxtOwS_z9cjnM8uOx1JytI0zynSlHis6H82iVEAA2A67va40Hzfgz6z1uH3oKCyrssqR8F36ym-2BfHD68KxQ7mIz2n9Lgkd2GSTadbQFLmV2YqA6Pld1NfKBgZpmIgBDLuWILs1cUOKJYq9quz2sOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=IcADLEpyFDv0Zd1WCJlYSymZk-ST343KSgJOhcwp_SBsPz-NMNC32L1FJyU3kGHys-7hs2y-s5k_yPBpf4qPwGErZYQX7S7hKzFKXpFtFmhLhq-WR-KFlAinb5LEa6PNUrdKvIr1MWnDrBQ1L3t3yb3mCeNLdDaU6eHMZ5CTb7a6Pw8ODuBFqs7t-UtTI74HxtOwS_z9cjnM8uOx1JytI0zynSlHis6H82iVEAA2A67va40Hzfgz6z1uH3oKCyrssqR8F36ym-2BfHD68KxQ7mIz2n9Lgkd2GSTadbQFLmV2YqA6Pld1NfKBgZpmIgBDLuWILs1cUOKJYq9quz2sOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
حکومت از امروز یه طرحی رو شروع کرده که بتونه فضای مجازی رو به صورت کامل به دست بگیره؛
طبق این طرح؛ قراره بلاگرها، اینفلوئنسرها و بقیه فعالای فضای مجازی ثبت و ساماندهی بشن.
در عوض می‌تونن از مزایایی مثل بیمه استفاده کنن، اما از اون طرف هم قراره نظارت روی محتوایی که منتشر می‌کنن بیشتر بشه و هر کسی خارج از چارچوب قوانین جمهوری اسلامی فعالیت کنه، صفحش بسته و با برخورد قانونی روبه‌رو میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69268" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69267">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=oXrHfeqV2s0UU-Irhs_RNosN-sV1ggQWDORH1ZZhCuiQ2w47Qsb04k__7mvZd1mx7CbrwfWzon9ELPymh9VZJgSNqrQm7avxM7Y2m58Slc37S44jLHUUlKLnEfo2E-fBNp62qQqKKuv6TD8uCzE8vcSutWxvxEO6UjnenWb1GTn1Yo5hLGTPbEDW-R9-rbuWLdQSQzaCtrAhBsY4HRhDmx6lfP0jZJe7kPSaWOWvdlvjj0fyqUGEm2Uu5WhHggI1NPP2HXxP3lW2V8wbyg3nU16SqLF045XmzQph2Hfe1TueT760ohKvd3r_twk8ENE-qwhtVoGaEWH4dZCPGrP4Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=oXrHfeqV2s0UU-Irhs_RNosN-sV1ggQWDORH1ZZhCuiQ2w47Qsb04k__7mvZd1mx7CbrwfWzon9ELPymh9VZJgSNqrQm7avxM7Y2m58Slc37S44jLHUUlKLnEfo2E-fBNp62qQqKKuv6TD8uCzE8vcSutWxvxEO6UjnenWb1GTn1Yo5hLGTPbEDW-R9-rbuWLdQSQzaCtrAhBsY4HRhDmx6lfP0jZJe7kPSaWOWvdlvjj0fyqUGEm2Uu5WhHggI1NPP2HXxP3lW2V8wbyg3nU16SqLF045XmzQph2Hfe1TueT760ohKvd3r_twk8ENE-qwhtVoGaEWH4dZCPGrP4Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آفرود سواری هم تو ایران ممنوع شد؛سازمان منابع طبیعی:
از این به بعد هر کسی بدون مجوز یا خارج از مسیرهای مشخص وارد مناطق طبیعی بشه، باهاش برخورد می‌کنیم. اگه هم آفرود به‌عنوان یه ورزش به رسمیت شناخته بشه، براش دستورالعمل و چارچوب مشخص تعیین می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69267" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69266">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8Gtk89ORLtNLS9KOhO2fyhYYNPReqwGaInFqlxAsf-wf7FpxovBISjdZkqM-lvoMGCYJswhjzhaxaGG3Qwl0f4ZkbHVAhahZPs9oKIRSbikoulEU93ev3n1RCLPwYySdA1DaOvb_fArsBB91Oo30LrZ5yatsXkg6fpWA8fX_cSsU1FPR_LOBXKt0l2SwT_Ske9qWSq63mQ1tS3kxE2Mtwmk_icH5qict3ZpR6ngeSCejZPH7xp15fanjElTjXtWqWw18xYgl7rbSfJp92YsUxB5UrWcTJ8MRgyUZqMz00nWO2PzYv6YNn3O8qebdHQ6jWHV_oVao0ee9IuFOuXe2AG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8Gtk89ORLtNLS9KOhO2fyhYYNPReqwGaInFqlxAsf-wf7FpxovBISjdZkqM-lvoMGCYJswhjzhaxaGG3Qwl0f4ZkbHVAhahZPs9oKIRSbikoulEU93ev3n1RCLPwYySdA1DaOvb_fArsBB91Oo30LrZ5yatsXkg6fpWA8fX_cSsU1FPR_LOBXKt0l2SwT_Ske9qWSq63mQ1tS3kxE2Mtwmk_icH5qict3ZpR6ngeSCejZPH7xp15fanjElTjXtWqWw18xYgl7rbSfJp92YsUxB5UrWcTJ8MRgyUZqMz00nWO2PzYv6YNn3O8qebdHQ6jWHV_oVao0ee9IuFOuXe2AG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده‌یاد مانوک خدابخشیان:
"اگر رژیم مذاکره کنه باخته و اگر مذاکره نکنه هم باخته"
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69266" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69265">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=lVGrkgrwP8pW15USyxGS1c4CrWXTf48X4aWuOYZBd2Axl4po5jUEr_0ffvVzA49LoCmbG0X3Ppxr4b4WXwhntEEz0cfFVH4Y8WW65bcM13IvD1jceo1S0IHI1gZxeq7rxet37AcKSHD3apGr99GKaPBpr0Hh93_Wd3qjZOKjsJs2G8PmMDbrneIyiLoKAbCBmdyyWdN_TT8cbcPtUGb3nrY9wDZFsZSfSwJ99B1evL96K8HU43jSek4iJTuCUCV-jwuw9I0_CYKDiajjzPGuFs_7WbXu5CWHz5t6kYXiCLQsl1z1oJLEM52qiU0PqzFJYEaZrvidzMh8B77M0EedDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=lVGrkgrwP8pW15USyxGS1c4CrWXTf48X4aWuOYZBd2Axl4po5jUEr_0ffvVzA49LoCmbG0X3Ppxr4b4WXwhntEEz0cfFVH4Y8WW65bcM13IvD1jceo1S0IHI1gZxeq7rxet37AcKSHD3apGr99GKaPBpr0Hh93_Wd3qjZOKjsJs2G8PmMDbrneIyiLoKAbCBmdyyWdN_TT8cbcPtUGb3nrY9wDZFsZSfSwJ99B1evL96K8HU43jSek4iJTuCUCV-jwuw9I0_CYKDiajjzPGuFs_7WbXu5CWHz5t6kYXiCLQsl1z1oJLEM52qiU0PqzFJYEaZrvidzMh8B77M0EedDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سنتکام:در ساعات گذشته، رسانه‌های دولتی ایران به انتشار ادعاهای نادرست سپاه پاسداران انقلاب اسلامی (IRGC) ادامه داده‌اند؛به‌ویژه سه مورد زیر:
❌
ادعای اول: سپاه پاسداران (بار دیگر) مدعی است که مسیرهای آزاد و باز در تنگه هرمز برای کشتی‌های تجاری خطرناک هستند.
✔️
واقعیت: خطرات فوری که کشتی‌های تجاری و خدمه غیرنظامی آن‌ها را تهدید می‌کند، ناشی از تهدیدهای لفظی و تلاش‌های سپاه برای انجام حمله است.
❌
ادعای دوم: سپاه پاسداران مدعی است که سه جنگنده رادارگریز اف-۳۵ (F-35) و سه فروند هواپیمای دیگرِ ایالات متحده در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✔️
واقعیت: هیچ‌یک از هواپیماهای ایالات متحده در تلاش‌های اخیر ایران برای حمله، منهدم یا دچار آسیب نشده‌اند. تمامی موشک‌ها و پهپادها رهگیری شدند یا به مناطق هدف‌گذاری‌شده نرسیدند.
❌
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام «ام‌تی نورا» (M/T Nora) موفق شده است محاصره ایالات متحده را بشکند.
✔️
واقعیت: این کشتی تجاری موفق به شکستن محاصره مستحکم (دیوار فولادی) ایالات متحده نشده است. بیش از ۲۰ ناو جنگی، صدها هواپیما و هزاران نیروی نظامی آمریکا همچنان هوشیارانه به اجرای کامل این محاصره ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69265" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69264">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=SQWQxD80COsxZM7kzBEhb4e4VxuMG7T5zKUy4GuPTMiApFqwrZyGZdvt8q8EZSmBiInP1Er4DoyIip8T5GwAlOtqCb1dw13Esw_lf6rjGzGw-Y-WUoCaF46HAmXbq9bVcI1vPT3w6WpI4ZnzbCbIINP2WXd8Vw9AVdqmhCBRylOuuc7RXQPurbuMsLUX0dXSksMZwI30w-2PMwCoThqYRTtQEC48QH6IJjII0pi9MuJPeOiZ1ZQD00-Fd43yo_DAGHgVNSrm50Zagg-THyqJ-P3dGoJGjuk3iu5ZzkP1rgPYi-Wv0bX2fKisFEVBCcd0svou2ZVWiN-k9rr9FCO1ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=SQWQxD80COsxZM7kzBEhb4e4VxuMG7T5zKUy4GuPTMiApFqwrZyGZdvt8q8EZSmBiInP1Er4DoyIip8T5GwAlOtqCb1dw13Esw_lf6rjGzGw-Y-WUoCaF46HAmXbq9bVcI1vPT3w6WpI4ZnzbCbIINP2WXd8Vw9AVdqmhCBRylOuuc7RXQPurbuMsLUX0dXSksMZwI30w-2PMwCoThqYRTtQEC48QH6IJjII0pi9MuJPeOiZ1ZQD00-Fd43yo_DAGHgVNSrm50Zagg-THyqJ-P3dGoJGjuk3iu5ZzkP1rgPYi-Wv0bX2fKisFEVBCcd0svou2ZVWiN-k9rr9FCO1ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر جوون ایرانی رفت پشت فرمون ماشینش ی خر گذاشته رانندگی کنه خودشم داره از رانندگی خره فیلم‌ میگیره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69264" target="_blank">📅 18:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69263">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
انفجارهایی در صنعا، پایتخت یمن رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69263" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69262">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-bylJvyGsbdiWQ85IhiwJm0OD9q3ERz6-uiis0JrKka9YhZL94xx5mJngNv5b1ChVKXLPRKU9kmPR0JyvJZoEwhLcw4qupC2UVIabKJVrSt11ALJ3N5qCrH-eDyH6JZ4CvpnjQOFFTug_euw9HISuKJRqNr7XFPvs_rSnS7FKds8UrKJO5gWwJBn9keLfrpu4DDSmOoIqyr0FC_zR3It_OcY3WToeHGEMgLYFyecWwQoofGuNeyrWuPZNyVU_3rcSjlAEUrqtvdnIsaRAT7S3bZv8JcQh_JJ-JAo92THdWEnYrlesmptAYdC4cUujfVrq7c0wfcmD5ogtocYYdQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه تا از تروریستای مفعول حشد‌الشعبی که در حمله مشترک آمریکا و عربستان به عراق کشته شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69262" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69261">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYj2uDZdxuB9WUMjDEXDk0GODgOnFkyZlYdpKh_2mWAGpLRo4Mr_Y8gHIjk92Iu1o6UjVr6RrTFI0pNam4fd7JY03sHO_eOpPNfXE0AIswyZP3C57slxkqUU65gDGQW80IOQZ6GcpnVSUSMmuzxMvIiE3M_DOF-BKSOOfyLPh-rZKPjUomL9-exu4lqqELKv16WFAOLTSqbXNq-HLMcJbZbycgLEfpTQnZF4BzbMu8gpKRinZzj90hNHfbRq44UB26h0aMtf4BL1WvRpx6KmjJGWoYfpXsVpP2UXeq3oG9sf4JcbSvFTwRR9hpBmrXXqCQXo0kBgek4ooBSboozTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران؛اطلاعیه شماره ۵۶:
دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69261" target="_blank">📅 17:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69260">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=hCOUfUQ_17Vzuw-8NWPN16Q3joZzNjjfpyESUG1BxPjOx5DieO4ul4hH8Z1nihXv0E2tr7ojNq_6FkCT7yvweZmd_1m0uXr8gem0UopsmOJQazjOFf3sRbtnFz-LWFV094gMHcJrdxrbcWgVhOB5P7w5wNMKMGUvx5QT1VuuHAKbuF_hNimU_SD_k97kTLCO9vkbzLU64_HDXJUJejHVVKTVaplPExFFK4Z-xY_TYbdeKlF7akarO4sGOeca75E9vmLjVKoEZP2xXJJijxpKn7gHt85Kuad6MJ4pHJ73vnWCiVVkix8hl7txZ9UgZKpMz163TZIiMuKOcLmQuTvcbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=hCOUfUQ_17Vzuw-8NWPN16Q3joZzNjjfpyESUG1BxPjOx5DieO4ul4hH8Z1nihXv0E2tr7ojNq_6FkCT7yvweZmd_1m0uXr8gem0UopsmOJQazjOFf3sRbtnFz-LWFV094gMHcJrdxrbcWgVhOB5P7w5wNMKMGUvx5QT1VuuHAKbuF_hNimU_SD_k97kTLCO9vkbzLU64_HDXJUJejHVVKTVaplPExFFK4Z-xY_TYbdeKlF7akarO4sGOeca75E9vmLjVKoEZP2xXJJijxpKn7gHt85Kuad6MJ4pHJ73vnWCiVVkix8hl7txZ9UgZKpMz163TZIiMuKOcLmQuTvcbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی وسط خیابون بعد از شلیک دو گلوله به پا؛ این همون شخصیه که تو لایو دخترارو کتک می‌زد و...
⚠️
‌ ‌ ‌
حاوی خون و خون‌ریزی
🔗
‌
مشاهده ویدیوی کامل بازداشت
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69260" target="_blank">📅 17:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69257">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=EiACp6k7Fvx5cPIpvmAzZho7T6ZnaRSQAfL2Naq8uPgFY-rgNJ5MGm_A4DH7F7w3EhaSQdMPBPy7VTE6wx07urPSQNJss62MNoPJ2W6j0PqHy1y-xLso44KE_0V3k0hJh9aWTSy_ddgBs-TUgsctDFrGfqnoEu8arBZpgXOR7z-LkzGZ6t1FLkSmuvh_GuBT5EwULfXdPQQhwF9xHjjgmzyso5_4lYFqgIKkzaOW5NmiFSN9rUQ2Bb7-XVlUXACao8sjMpJBHQQdeHOIhl_JCzd_EEZb9UEDEfdK9cfpOVsyIzhPMmmWFIJXDKMkvKDTTQBupVsh1BzMcTiaQPg9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=EiACp6k7Fvx5cPIpvmAzZho7T6ZnaRSQAfL2Naq8uPgFY-rgNJ5MGm_A4DH7F7w3EhaSQdMPBPy7VTE6wx07urPSQNJss62MNoPJ2W6j0PqHy1y-xLso44KE_0V3k0hJh9aWTSy_ddgBs-TUgsctDFrGfqnoEu8arBZpgXOR7z-LkzGZ6t1FLkSmuvh_GuBT5EwULfXdPQQhwF9xHjjgmzyso5_4lYFqgIKkzaOW5NmiFSN9rUQ2Bb7-XVlUXACao8sjMpJBHQQdeHOIhl_JCzd_EEZb9UEDEfdK9cfpOVsyIzhPMmmWFIJXDKMkvKDTTQBupVsh1BzMcTiaQPg9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حملات شبانه سنگین روسیه به کی‌یف، پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69257" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69256">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=H6Es2S7_TqoIAtsvO5obVB6grslvU_69dsQEVeLZGR7bQMvdUYfNDDqABCMXBCisPM9XhIFLCR9clcIwAtPdtWrFM3e3lsDroqfBfHQuLWvHWyTuq_0urphQIaPU9gDgt5hOfpSGwFOcSJvdZOl7fQflfX6SXGjoWSixv4ePqkw87kmSC2kG2onL2KHAEPkWlm_2oAW1tipbwHqGi_7Nm_oCrjnU9oIE6MzfLMvxwD7pJ8zvysQyw8VRhB27dUfYPFB-epaezJD-bR9hXFYmNu5h6HKFg8PSDoeD-4OLPoLp8ykdGEGyRMWGwhciAQWGyadIYO2PURaww_ca6Jj1JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=H6Es2S7_TqoIAtsvO5obVB6grslvU_69dsQEVeLZGR7bQMvdUYfNDDqABCMXBCisPM9XhIFLCR9clcIwAtPdtWrFM3e3lsDroqfBfHQuLWvHWyTuq_0urphQIaPU9gDgt5hOfpSGwFOcSJvdZOl7fQflfX6SXGjoWSixv4ePqkw87kmSC2kG2onL2KHAEPkWlm_2oAW1tipbwHqGi_7Nm_oCrjnU9oIE6MzfLMvxwD7pJ8zvysQyw8VRhB27dUfYPFB-epaezJD-bR9hXFYmNu5h6HKFg8PSDoeD-4OLPoLp8ykdGEGyRMWGwhciAQWGyadIYO2PURaww_ca6Jj1JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صبح امروز ارتش آمریکا به یک پایگاه پدافند هوایی سپاه‌پاسداران در اهواز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69256" target="_blank">📅 16:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69255">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=TbRQO886i4V_LQVV2kdwevnoS_tC6KnMIGvM08SEdyBaujyDHBSEMUDtuLBuTbtQWBIRXXikAT98whSTx8OlYbZ1KAjZq1RqE7LGpTSi22EC0cItZ-4nkseSGk_v2ERJ4yKhyBCeA4VbPFEaDy3nJ20q2aNx1dOCkqdFQHvG7WyeX_gMjoQi1h--W-2OA6meu1IINN62It0IIrX2z7oZMj58titNXmpI8-hanikW_86UKt_BZ4ZAC-KZaqAZxjvWVmjEGn3fqRhkiMWXX2quA7Yp7vdhT8izgAXfOG3kNIhKETxEgF23X_V3RhU5KaKn_nL116GSbi4g0kA_Ys1LDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=TbRQO886i4V_LQVV2kdwevnoS_tC6KnMIGvM08SEdyBaujyDHBSEMUDtuLBuTbtQWBIRXXikAT98whSTx8OlYbZ1KAjZq1RqE7LGpTSi22EC0cItZ-4nkseSGk_v2ERJ4yKhyBCeA4VbPFEaDy3nJ20q2aNx1dOCkqdFQHvG7WyeX_gMjoQi1h--W-2OA6meu1IINN62It0IIrX2z7oZMj58titNXmpI8-hanikW_86UKt_BZ4ZAC-KZaqAZxjvWVmjEGn3fqRhkiMWXX2quA7Yp7vdhT8izgAXfOG3kNIhKETxEgF23X_V3RhU5KaKn_nL116GSbi4g0kA_Ys1LDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی حرومزاده چهل پدر وسط خیابون:
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69255" target="_blank">📅 15:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69254">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=goEVbw4PE5kL_4Dwed_ysLRCVTvbOoJ8xsI2RQUI02QDg5i3jGNLA5sVjBt-nxCJeTvOPnDxrY_4Fq_DiOANm9m_M03b1sgfL71ZZNGd_ryu3eoV07VMt3wDgCbmiMmAcJAQnOLyGMQja1Om5W5e7Vezk0IXRJ1EakQeYTOvuYqwQwtZCaf41zWS2TQNS3BQiN7c1X-LdLx91stAmr-6RvwmBPv6gE1OtiLbfK97srtMduEXJmmrsSMIPL5cCR3JI7rreLQaL1ryxdFJHsF5piZ69mvM9870JcknyTvWJDC-sKJJWLpEpbtviGhE4rffW1lvk1nmhfsFzD94D7qtqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=goEVbw4PE5kL_4Dwed_ysLRCVTvbOoJ8xsI2RQUI02QDg5i3jGNLA5sVjBt-nxCJeTvOPnDxrY_4Fq_DiOANm9m_M03b1sgfL71ZZNGd_ryu3eoV07VMt3wDgCbmiMmAcJAQnOLyGMQja1Om5W5e7Vezk0IXRJ1EakQeYTOvuYqwQwtZCaf41zWS2TQNS3BQiN7c1X-LdLx91stAmr-6RvwmBPv6gE1OtiLbfK97srtMduEXJmmrsSMIPL5cCR3JI7rreLQaL1ryxdFJHsF5piZ69mvM9870JcknyTvWJDC-sKJJWLpEpbtviGhE4rffW1lvk1nmhfsFzD94D7qtqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صداوسیما بعد از هر حمله آمریکا
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69254" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69253">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.  ۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69253" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69251">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C-KxsF8sYGnQRsUxDIBUz0Muuleo3CGCUUnX7NY91EnrxWjAWfGzFFSepYUk83AJ1OyPOn815_lzkoLByJMIemUubB0jX4B0GwrYgvVreYyhtrKl7wuVACHsNDH6e0lRszO77HHhstLxFYpi2Hy_zpKNkE5FcQaHbVc7JecZty2U0AnLVolwdanc4iI88jJYe9iQUSpxU44MTmIJ4_U2Df6-r6liReddCYNCpuUD2hF4bPQe9bNGHj_-7L-tydOwAwSP7it53K0mlPlwBynl6rTf7GlZwvjd24voB1rJc0Mp2OMx4HXkrDKAx6LF4KLhcclreDgC9EW5CNfPGJBAIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=o2G4gjLhXl9j7ctf6McAaGhxR5lulS1zSjI_HpEFJY6Gd0UTxDUsd9w7Z6YQjgi7IPhx2_i3laC_8eV4yPupMgQAoFI7LTyNulkNWMv-8XOeCW03w1oqc9f22wLrAglRmEN5TaktyWfYgHssAsiLV7B1Am4gExuVrCbIWpkyjYrBPsSNZnwtRAV1Ks_qnPScH64GFfjiJMMLT5V0lYrQuUUVW-aS3NxkcCn4wNHwPb_16gzDx8UjW1Z_G16oEfu4IkHUmyhiBR2K6AZZe4b6XjgpHQQeB22pvaaayrhVDxxwFFFE2wDcy814SaCcQkTFPBbW5fFXTjz1N6519VpHrw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=o2G4gjLhXl9j7ctf6McAaGhxR5lulS1zSjI_HpEFJY6Gd0UTxDUsd9w7Z6YQjgi7IPhx2_i3laC_8eV4yPupMgQAoFI7LTyNulkNWMv-8XOeCW03w1oqc9f22wLrAglRmEN5TaktyWfYgHssAsiLV7B1Am4gExuVrCbIWpkyjYrBPsSNZnwtRAV1Ks_qnPScH64GFfjiJMMLT5V0lYrQuUUVW-aS3NxkcCn4wNHwPb_16gzDx8UjW1Z_G16oEfu4IkHUmyhiBR2K6AZZe4b6XjgpHQQeB22pvaaayrhVDxxwFFFE2wDcy814SaCcQkTFPBbW5fFXTjz1N6519VpHrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مادر جاوید‌نام ابوالفضل سپاهی، که توی میدان علیخانی اصفهان اعدام شد:
خطاب به یه نفر به اسم هادی: بگم برات که تیر زده بودن تو پای ابوالفضل؟ بگم برات که زیر چشماشو با فندک اتمی سوزونده بودن؟
بگم برات که ۲۰ روز بهش آب ندادن؟ بگم برات که فکشو شکسته بودن؟ بگم برات که دماغشو له کرده بودن و آویزون شده بود؟
هنوزم تحمل شنیدنشو داری که بگم برات...؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69251" target="_blank">📅 14:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69250">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇮🇷
سپاه‌پاسداران:
تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم.
همچنین چند افسر و کادر فنی و تعمیرات دشمن نیز در این حمله کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69250" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69249">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa6076311.mp4?token=hWVgGUmx9xuMHJr9UWVDgso0cJFZ6705vyWCXzWA1qxtSD-Hz-eWbm8PfSLUY_0-qb4xlWhZ0AElMH0LI7saqslKolekKZCEk49iH_Jj3F3stb0E-E62kO2yC1skkOSCFWsT7MYmUmU_8y_rD_MrPu48ldU2b1-RjjwHjdizlYOE2g3Akyut4-SLBD4_LKiy5CZi8LeIbAgZpym2Nqi1DetUcT4qnt6bNw0oHm9Nb1Np2i6648q3XTsdQDAqd5jo4LMQdyuEMQOenxbsDySceDoH9-DWpj36LYv4I5U_lVYlSRikGVpKmMARGO6rWLC7SozboLlK6_v4buCyCFJSRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa6076311.mp4?token=hWVgGUmx9xuMHJr9UWVDgso0cJFZ6705vyWCXzWA1qxtSD-Hz-eWbm8PfSLUY_0-qb4xlWhZ0AElMH0LI7saqslKolekKZCEk49iH_Jj3F3stb0E-E62kO2yC1skkOSCFWsT7MYmUmU_8y_rD_MrPu48ldU2b1-RjjwHjdizlYOE2g3Akyut4-SLBD4_LKiy5CZi8LeIbAgZpym2Nqi1DetUcT4qnt6bNw0oHm9Nb1Np2i6648q3XTsdQDAqd5jo4LMQdyuEMQOenxbsDySceDoH9-DWpj36LYv4I5U_lVYlSRikGVpKmMARGO6rWLC7SozboLlK6_v4buCyCFJSRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود دیدنی یک F/A-18 Hornet بر روی ناو هواپیمابر.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69249" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69248">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ksj5yMnYN2sV0x2rXX1aAXIpP7pcPLHVRJ2A-JtHMq8sCmT1EVBtGAb98IgkFHvroPPRGFcJCkP7PpbBEq_PlVditkUoT331Ju6tP4B5MLBNjTzwL6ct_2jalAT2uGU4NtKY_UboG2MfHUZPx15Vif1LRubkAnettIlF7i10CgVgMDld8vFQ-YYY1299IzLX1xIc1DUoiq8kad3PX4qJSQC2Mi_56e8T43ZasACnwH8ynN1j2DdzzO82I61ybIC7cg_WUCAbbgTUGKEn-DWPtN-Gl84t46oekBlo2Ln2MHF9YxLnYVVs2iVyoS7aCHTlQBninYgPhZTISXKt7LLkcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⏺
ان‌بی‌سی‌ نیوز:
به گفته منابع آگاه، ترامپ در قبال مسئله ایران «به‌شدت کلافه» شده است، چرا که مقامات ارشد بر سر راهبرد واحدی توافق ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69248" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69247">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a176457914.mp4?token=tNcqeZN-TWIsV7lxlf1ikVyONxB0L1UWveLJiGsEIxoIjSHXlNAkTCwzXBTZqwJTXkv9XhTyR7WHSHrOavCfobpe8tYwaQR_zffvKubhydszUOPELy_YhnathR-EYGfdwi2TqRRqkuDX2KruKLgD5qVM1c4MWpk4CSsz-Y89LHD8UV_hPCxZbg2dF-ac_TNLG4Q-A8iKWi4lqWknbVHT-4T0tiWqE9CqtzrSGu-k7_GTiRwUFSn16DbfSuvbmxcebUlwnOfzG5-nLYq7mrWx3NW3h71vZLCpP1Q5SxVP7AlWWeeAfwT2jh2J6B5zp2jkwZGjv9tfEfh-3w4t1O7-3LYcwM-D7NTBuFYycR1ZiE-RHrpFTDpr6ptrY3c70SHKcLXrry17_CMKOES_Mx2_VDA8KIcEEuwGYCF3LEOcDsansFLEmLV2RZ-GYIHNUIpgUs7dNpRX5k_h-gZK5ma-O1wCfBW7C9SG5bFvE1X4e31V9VP5tK4Nov60cZj_JlUYITgs7PYlkP5JceuqF-nFsP2p1B27ItuFKOTTwu6KHnY1LQHLjzKCssUFRMwoAROCXqkI8qyArEKXbMdc5zbKdfG1v8xSopUJR-04Zy-st8wjHn6UQ-bNDrRD8lm7R-mAKFF005k_Tn1zPywmPNkYAc3IeKEIbgdIw-bO8xos1Xk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a176457914.mp4?token=tNcqeZN-TWIsV7lxlf1ikVyONxB0L1UWveLJiGsEIxoIjSHXlNAkTCwzXBTZqwJTXkv9XhTyR7WHSHrOavCfobpe8tYwaQR_zffvKubhydszUOPELy_YhnathR-EYGfdwi2TqRRqkuDX2KruKLgD5qVM1c4MWpk4CSsz-Y89LHD8UV_hPCxZbg2dF-ac_TNLG4Q-A8iKWi4lqWknbVHT-4T0tiWqE9CqtzrSGu-k7_GTiRwUFSn16DbfSuvbmxcebUlwnOfzG5-nLYq7mrWx3NW3h71vZLCpP1Q5SxVP7AlWWeeAfwT2jh2J6B5zp2jkwZGjv9tfEfh-3w4t1O7-3LYcwM-D7NTBuFYycR1ZiE-RHrpFTDpr6ptrY3c70SHKcLXrry17_CMKOES_Mx2_VDA8KIcEEuwGYCF3LEOcDsansFLEmLV2RZ-GYIHNUIpgUs7dNpRX5k_h-gZK5ma-O1wCfBW7C9SG5bFvE1X4e31V9VP5tK4Nov60cZj_JlUYITgs7PYlkP5JceuqF-nFsP2p1B27ItuFKOTTwu6KHnY1LQHLjzKCssUFRMwoAROCXqkI8qyArEKXbMdc5zbKdfG1v8xSopUJR-04Zy-st8wjHn6UQ-bNDrRD8lm7R-mAKFF005k_Tn1zPywmPNkYAc3IeKEIbgdIw-bO8xos1Xk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم گوه خوردن نوید حرومزاده هزارپدر که دخترا رو کتک میزد اومد بیرو
ن؛
از همه عذرخواهی میکنم ، گوه خوردم غلط کردم!
بذارید برم توبه کنم ، درمان بشم و برگردم به زندگیم برسم.
اتفاقاتی که بین من و اون خانم‌ها میفتاد رو تو ذهنم الکی بزرگ می‌کردم و دیگه کنترلم رو از دست میدادم.
خانم‌هایی که کتک میزدم، من رو درک میکردن و هیچ شکایتی ازم نمی‌کردن.
اتفاقا مردم خوب کاری کردن که انقدر واکنش نشون دادن؛ باعث شد یک بار واسه همیشه به خودم بیام و خیلی مسائل رو کنار بذارم.
از تَه قلبم از همه مردم عذرخواهی میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69247" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69246">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=CrSU8s-WQo0_tYgQ3bVInTg9NvbwqZVI2iJ-3ghuc_ODXTL1S4ZBzHjH3ccWaR1mofdQZo-1LbVdIEuW6yLQqjEMCkiqhROQXigOLYeMOjmJXgThctdpSc96m1j0Hhqgf5zTNeW713NioHRIJUK7peuL5KRqcPzsVo0Q8OHbvw5Pf3QYvUmTjX6UwPBcSvMd_gV0nkWap0AAnkvX-kvuDCPC6HoWesLRqsACdFxiWM5flSHkBYwkRkC56rbF59_KRE9rM4Yf7fgsNl9Lhrx03wtN8bZadF2yGDWuH4AwKrHB1zAwxQfigjbG2XXQbSOOu9IdPNBwrLdQ3ET7Rg1xPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=CrSU8s-WQo0_tYgQ3bVInTg9NvbwqZVI2iJ-3ghuc_ODXTL1S4ZBzHjH3ccWaR1mofdQZo-1LbVdIEuW6yLQqjEMCkiqhROQXigOLYeMOjmJXgThctdpSc96m1j0Hhqgf5zTNeW713NioHRIJUK7peuL5KRqcPzsVo0Q8OHbvw5Pf3QYvUmTjX6UwPBcSvMd_gV0nkWap0AAnkvX-kvuDCPC6HoWesLRqsACdFxiWM5flSHkBYwkRkC56rbF59_KRE9rM4Yf7fgsNl9Lhrx03wtN8bZadF2yGDWuH4AwKrHB1zAwxQfigjbG2XXQbSOOu9IdPNBwrLdQ3ET7Rg1xPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خبرنگار صداوسیما حین گزارش پرید توی آب و فاز کوسه گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69246" target="_blank">📅 12:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69245">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubMKrthaITLjMmdcLVaSfhBII81bPws0kfUcmub6dUpGKHyfH2g6_ydEjLE2d2Kq0cuV0cyUkGzRyqXBtId8LT75CH_CHJ3bmnp1HGinT-RmGKRASrYTtrJ5VT95Ih5EggDopfwTR7umDWSqQc3OBxetXjZONYhmQFV5jaeSBCqdOYQtjDgO8Po82vdeliiBeSW306rxddhj9zfMTfF2rXNjPGD4i-NMvVfP57UZTpXV0Dp-OgjvF6QTHxAvgumAkyGVotZr3nMtljh7_nlVxUe1-BWNAVlED1HqXVBBPBoiquDWbzkrtS6hs8OM7Q4VJgNMkORfpQOpHLZ4BQIgNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سپاه پاسداران:
متجاوز رو همین امروز تنبیه میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69245" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69243">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uuhnit9uiKubewgznC6EWOEPRiqLZQ84jtJWXnyb0mrZjKXm15I-TXwqLzouN1MADTPRWWqmaiZnAaleq7h8p3327JIz78qSEsk6jmWOzjN9tEQMHxKbvljwbrKSmWhd4dXPP8VWK06oqJw3by0f2zhfDlnBD-2CDfe4zvdFKtS8ozs4Pdqm-mX50h8WX69cCpdxDXO0qc3Ieqscm4JaCMktgx4TKgZxQNn-jqM3-gnjszZhq_GDPtTxpagRdpvGod8WpDA2U4T2YngfsaEYP8jcLmsPb9G_43H_Jonszhf8BBGFX74kNbAx9WDyA90wSH2wadt3FWwOFnpP28Il4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854dca423a.mp4?token=HEWSr-eavLse0nYXRXTra-WHyPxhu8UOwEjgA3JsfhHh2ml7gQMheXliLu9L4FN3Kr-bf6G_Ts5pza6j-DVJg3bdoyfS3gxiozf0T-nqPhBonQd73mrif-oMQdLXOD-69N6WWgJusPdw0eRUV-gPDr_BggDyR8oXYOyNP5xJaiI_M4n9TkTIpqMlhT7zFSmFEU9ysJ4UWkcrk0lFTV3NeGTiRYxaTXd94YzRyT26eGP7Wq46P3aKZZJpServ8pxia_9SiQBJeNSCTcsqVJinZHcJ1Ab9QPwgoIKMHJlRagO7t9purOi0XeODZhwRsHb2LC4wV-hHJS_HW2ZiR-QRpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854dca423a.mp4?token=HEWSr-eavLse0nYXRXTra-WHyPxhu8UOwEjgA3JsfhHh2ml7gQMheXliLu9L4FN3Kr-bf6G_Ts5pza6j-DVJg3bdoyfS3gxiozf0T-nqPhBonQd73mrif-oMQdLXOD-69N6WWgJusPdw0eRUV-gPDr_BggDyR8oXYOyNP5xJaiI_M4n9TkTIpqMlhT7zFSmFEU9ysJ4UWkcrk0lFTV3NeGTiRYxaTXd94YzRyT26eGP7Wq46P3aKZZJpServ8pxia_9SiQBJeNSCTcsqVJinZHcJ1Ab9QPwgoIKMHJlRagO7t9purOi0XeODZhwRsHb2LC4wV-hHJS_HW2ZiR-QRpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.  هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69243" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69242">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=jZRpkjDzvm6GYq-Z4tWGTDDuAzR3WEqnXTvXjuN0p27c0lh96ndA6QdndtN4Le6HUhk9WoalxfNcuS1fFQYXoHn1iQRWWJ8DNxFs5SmHSlLAh9La7g8KQ3KadpebVypcRkC3EbQ9RTZ1zddQU05lAS6i2vodS7CITLg_ushnRn4SkyduUNMqVoGRa4EDJqgKKbPnPaZGgT28ItqODoI9rJuMwWNCkxH7DqkzcQwsiaCDLDyjsubYhaOC7ugMvmhWnWFj5kzKZjdUgTM0HxonQ47ctaUCxoAco5PPTPvw9mnqcqnCS07jxUeUVYehtzXD5ta0mNObz2LYeZIjU6LQ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=jZRpkjDzvm6GYq-Z4tWGTDDuAzR3WEqnXTvXjuN0p27c0lh96ndA6QdndtN4Le6HUhk9WoalxfNcuS1fFQYXoHn1iQRWWJ8DNxFs5SmHSlLAh9La7g8KQ3KadpebVypcRkC3EbQ9RTZ1zddQU05lAS6i2vodS7CITLg_ushnRn4SkyduUNMqVoGRa4EDJqgKKbPnPaZGgT28ItqODoI9rJuMwWNCkxH7DqkzcQwsiaCDLDyjsubYhaOC7ugMvmhWnWFj5kzKZjdUgTM0HxonQ47ctaUCxoAco5PPTPvw9mnqcqnCS07jxUeUVYehtzXD5ta0mNObz2LYeZIjU6LQ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه این خانم در الجزایر و تبریکش به یکی از کاندیدای انتخابات بابت پیروزیش خیلی وایرال شده.
"
منم کلی سوال دارم
🙂
"
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69242" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69241">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎙
خبرنگار:
نیویورک‌تایمز گزارش داده قبل از شروع جنگ، شما به ترامپ گفته بودید برنامه موشک‌های بالستیک ایران ظرف چند هفته نابود می‌شه، بدون اینکه تنگه هرمز بسته بشه و حتی ممکنه به تغییر رژیم هم منجر بشه.
اما الان بیشتر از پنج ماه از شروع جنگ گذشته، ایران هنوز موشک‌هاش رو داره، رژیم همچنان سر کاره و عملاً تنگه هرمز هم بسته شده. چرا ارزیابی اولیه‌تون این‌قدر اشتباه از آب دراومد؟
🇮🇱
نتانیاهو:
این اصلاً ارزیابی من نبود و چیزی که نقل کردید، درست نیست.
فقط یه پیش‌بینی می‌کنم؛ بعد از این شکاف عمیقی که بین مردم و حکومت ایجاد شده و اتفاقاتی که رخ داده، فکر می‌کنم این رژیم در نهایت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69241" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69240">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e988916503.mp4?token=hJ4l8H3naDvQam87iFRDk-2-xQrz8DijbWan5BLXFhy7WgkjVFtWa4OeVLYNDGP-tq9sqHu1TMECu0tUf6yYndbaQ6X60t8x3nwclsYPeCaN00NwVkoSuXbQb65EpD3c49Pe4qolmXekosrlwFSgJXaONsCjoHV_DbMcjnVg-4KKKdlLS0jt8nVOTU6vXiLpUgXaYTFYyEP_D0xUreZrNtAUr1ZSKg0db5WZcPcK4shpXeyBZfwgyKpBzQMp71Kr3a8hCDKO2PPeevqCVs27V74SjUSKE99RR3eBHh6VRpYGAttU9fn7pGkJrg57eqRNm1ibtUZ3ICYv71Nc48tljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988916503.mp4?token=hJ4l8H3naDvQam87iFRDk-2-xQrz8DijbWan5BLXFhy7WgkjVFtWa4OeVLYNDGP-tq9sqHu1TMECu0tUf6yYndbaQ6X60t8x3nwclsYPeCaN00NwVkoSuXbQb65EpD3c49Pe4qolmXekosrlwFSgJXaONsCjoHV_DbMcjnVg-4KKKdlLS0jt8nVOTU6vXiLpUgXaYTFYyEP_D0xUreZrNtAUr1ZSKg0db5WZcPcK4shpXeyBZfwgyKpBzQMp71Kr3a8hCDKO2PPeevqCVs27V74SjUSKE99RR3eBHh6VRpYGAttU9fn7pGkJrg57eqRNm1ibtUZ3ICYv71Nc48tljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سؤال: آیا هدف شما همچنان تغییر رژیم است؟
🇮🇱
نتانیاهو:
هدف من این است که اطمینان حاصل کنم ایران، با وجود این رژیم، به سلاح هسته‌ای دست پیدا نمی‌کند.
این موضوعی است که من و ترامپ هر دو بر سر آن توافق داریم، چرا که در غیر این صورت، با دنیای متفاوتی روبرو خواهیم بود.
آن‌ها با سایر کشورها و جوامع دیگر متفاوت هستند.
🎙
سؤال:
همین دیروز گفتید که به نظر شما دستیابی به یک راه‌حل دیپلماتیک بعید است. چرا فکر می‌کنید ارزیابی‌های شما تا این حد با یکدیگر متفاوت است؟
🇮🇱
نتانیاهو:
خب، نمی‌دانم آیا واقعاً بعید است یا نه، اما می‌دانید، من نسبت به شیوه عملکرد ایران تردید دارم.
آن‌ها همیشه دروغ می‌گویند، همیشه تقلب می‌کنند و همیشه وقت‌کشی می‌کنند. آیا ممکن است این رویه با اعمال فشار کافی دیپلماتیک و اقتصادی تغییر کند؟ باید امتحان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69240" target="_blank">📅 10:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69239">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDA6hjQbVC2fA3A3PtfyMzRT7Hq97EacepPs5R85wpDw07jspHwbS8VC22onsNIGX0MV4S1eju1Aguujl_IzzpT0mAD7I5GM2R7hasHj6jwYNCAF3y9oaLT89TqB8zunhkJTI5LsC0VEZWD1e6JjFqJ_Lm6Y87St3W1mFP9jwqKvFC4L1xR9xOGPZmnU7JGDR3RlfV2NQkZeOeFBMle1SEIdXFppse2bNSc8F_by2hlocwX8Jbl6VlVS1uK9Q_3nYZQ-0DrUQ6_-S2pMH0a7tm1Hn8qF_Rdcy86IMGdL8Yu9KGKNHI1_WxN0mwhY6JZa7qNfxG3hj-m97dkVnnuM0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇺🇸
تحلیل مرکز مطالعات استراتژیک و بین‌المللی (CSIS):
ایالات متحده اکنون تقریباً ۸۲۷ موشک پاتریوت و ۲۷۸ موشک رهگیر دفاع هوایی ارتفاع بالای ترمینال (THAAD) باقی مانده دارد که نسبت به تخمین‌های قبلی به ترتیب ۲۳۳۰ و ۴۵۲ کاهش یافته است.
تحلیلگران هشدار می‌دهند که با وجود تلاش‌های گسترده برای تولید، تکمیل مجدد این موجودی موشک‌های پیشرفته می‌تواند سال‌ها طول بکشد و در صورت بالا ماندن تقاضا، ظرفیت محدودی برای سایر موارد احتمالی عمده باقی می‌گذارد.
سی‌ان‌ان گزارش می‌دهد که منابع پنتاگون می‌گویند این تخمین‌ها نزدیک به ارقام داخلی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69239" target="_blank">📅 10:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69237">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=qdm3eo3mLiT8AMPYsJdQXdV4TlDLBBoF7VzmQos4rfE_ujxzKYF1f7l1YYyTQGp8lHgnjOD4xC3jALB8Sqm6HAWT34E9RSmrAwWviHQWhnwfU2WJh6uR-LWvpdwc8G_dJ5CFa3a2vzgjoZf8V2bsUhnYjtqIgDBi4gwP3bsgwDElzfGUFuJ6VchwW8dAKN4xQXiVCyToWGXozBdIOVZACOkaBMKygjW4_D1S-NuP7vtlIFu9D9KpGnjk7BKUDXTYu3YYCCl_drzXLxzvbIRYc1in1zLAw41RecAcEPqkThcPCcgzhZtwcaFGUYjUt5uzjS27YhTgdnof4JTQUYuycg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=qdm3eo3mLiT8AMPYsJdQXdV4TlDLBBoF7VzmQos4rfE_ujxzKYF1f7l1YYyTQGp8lHgnjOD4xC3jALB8Sqm6HAWT34E9RSmrAwWviHQWhnwfU2WJh6uR-LWvpdwc8G_dJ5CFa3a2vzgjoZf8V2bsUhnYjtqIgDBi4gwP3bsgwDElzfGUFuJ6VchwW8dAKN4xQXiVCyToWGXozBdIOVZACOkaBMKygjW4_D1S-NuP7vtlIFu9D9KpGnjk7BKUDXTYu3YYCCl_drzXLxzvbIRYc1in1zLAw41RecAcEPqkThcPCcgzhZtwcaFGUYjUt5uzjS27YhTgdnof4JTQUYuycg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب آمریکا به نقاطی از کشور
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69237" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69233">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=Hu_HvnGcio7-sRkNdQPTYCFihITT2qiYYW_WwniMSJ6_cAUpBMaMg8651M4LWSvS0TjeUQbDg11TO6p6HlhzBzqpoLn5YEi_MyOKDgZJ7eRfxBmc8RDe15S7Kp-0wXFB8kyya8hXiarTyB5JStioQB0RHybcPn3jbKIe5f2ER_8LxxMBEALTrZPDdsXu3PflgfI4fsBJ96_Z-2WvI5ZjFvJECRbOTLQretwTxsiSxnpHhtEehx_QYbv6LG5Gcnxxf3f-uIFLvtWwUUEFGjwsS1bN-GlTUtmax-DVhtD2_q5yUCN5QFKI7IZTAnCjhsFLumidf2DtWksCbMj3-JpBDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=Hu_HvnGcio7-sRkNdQPTYCFihITT2qiYYW_WwniMSJ6_cAUpBMaMg8651M4LWSvS0TjeUQbDg11TO6p6HlhzBzqpoLn5YEi_MyOKDgZJ7eRfxBmc8RDe15S7Kp-0wXFB8kyya8hXiarTyB5JStioQB0RHybcPn3jbKIe5f2ER_8LxxMBEALTrZPDdsXu3PflgfI4fsBJ96_Z-2WvI5ZjFvJECRbOTLQretwTxsiSxnpHhtEehx_QYbv6LG5Gcnxxf3f-uIFLvtWwUUEFGjwsS1bN-GlTUtmax-DVhtD2_q5yUCN5QFKI7IZTAnCjhsFLumidf2DtWksCbMj3-JpBDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هواپیمای باری C-2A Greyhound متعلق به نیروی دریایی ایالات متحده، دیروز آخرین پرواز خود را انجام داد و اکنون پس از حدود 60 سال خدمت، رسماً از خدمت نظامی خارج شده است.
🗣️
با از رده خارج شدن هواپیمای C-2A Greyhound، تمام هواپیماهای نظامی که توسط شرکت Grumman قبل از ادغام آن با شرکت Northrop Corporation ساخته شده بودند، اکنون از خدمت نظامی خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69233" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69232">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69232" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69231">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=KnbHzkdumHp8ka5Gmv4bZ_-6_p4gIRlkSmgDCOFqu5-6CodaMvA2nIzrU0srbwCymtd4aytgFicsh9gUxmNcoNZwAaodvn_tLLhob8MNSyOZq4ujLQ-9nqdyv_iRHz-5aTDIyBEYd7dpI89CofFSHcIq87VqKWpHdw2AEwEmqDToYpwUSCcBV4OfmAle03lKNYQJYPV114ZNkSkHajFpr38nvZOzW73geP0u2pNy-kihMNzScNCgoZwSqAGEeDWyZ6ZrDCgLbSjpPlUT95EzabS4208pMCkjJeoqzmjxG5sUSNBYs5Fy7TQsf4P70kORjL6zjqDyNB8HZ6olq0cIww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=KnbHzkdumHp8ka5Gmv4bZ_-6_p4gIRlkSmgDCOFqu5-6CodaMvA2nIzrU0srbwCymtd4aytgFicsh9gUxmNcoNZwAaodvn_tLLhob8MNSyOZq4ujLQ-9nqdyv_iRHz-5aTDIyBEYd7dpI89CofFSHcIq87VqKWpHdw2AEwEmqDToYpwUSCcBV4OfmAle03lKNYQJYPV114ZNkSkHajFpr38nvZOzW73geP0u2pNy-kihMNzScNCgoZwSqAGEeDWyZ6ZrDCgLbSjpPlUT95EzabS4208pMCkjJeoqzmjxG5sUSNBYs5Fy7TQsf4P70kORjL6zjqDyNB8HZ6olq0cIww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69231" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69229">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-qpS3PoFRf6VDmdZp5v631U5w-VHGuR5Psm0_7T9UmMlBrHMGRl8U_Lm1xaaNeGm55s1GxvafpZlZR5fo6F4VT04QGuyq41r-tEUu6ZdVfEsBQ2Cpgdm8yh5xtem7PO0jLEqD17VXcyKctBPRVrP0Q6CN_eehmTsvvRJynPdOV2l4HZsBFHf913dLDGhYTgrdASROnz8UFxk_q9MLeo2HU9UoLcacfWjVoVjAuB2AWKIXYJ5WfwFCNgziOodgPanNpoecSsEYh4LOf1uwbuiBM4kHEgYAyR90aRsydZV_bxF8Wgzm2fI8o0CbVR6L0zd-HR1dDOGTIxkWuHLnSxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qSSPMG0cGx5qbxKkIj2YPvF5seT411pW4K_Zw3IXS4ofWXDosnLq7jTJEl8c1ZA2JnfM_iqJY0axkvLb4PGlBqe8vW5MQWHjAhqlcmxGdxLViPvxTXiShCzIvMNUx_Qxv1n6830V367TzGtvPavpzrAuUUVYBcrfihWapqMnmAAOoe_OBgZoUWxzohQ3peCecy3F2IueZSkyr0fChgUJH9zDLtoHshRuJQZgx4kaUPyrbTEJ5c_iT_71Cb9Bfj-mol0fbyoMIBD1rF1FhUUrX0Af-TdSpuZb4n_4tQ5dStSLxhXZGrlrBiL6SedZ17h4BY1yNHehQ7GXo8-mnWFsGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وال‌استریت ژورنال: دریاسالار برد کوپر گزینه‌ای را برای یک کارزار هوایی تنبیهی علیه ایران آماده کرده است که می‌تواند تا دو هفته به طول انجامد.
کوپر معتقد است اگر ایالات متحده خواهان اثربخشی اقدام نظامی است، باید برای شکستن بن‌بست موجود، حملات هوایی خود را تشدید کند تا بدین‌وسیله تهدید موشکی ایران را به‌طور قابل‌توجهی تضعیف نماید.
این رویکردِ «اقدام گسترده» — که یکی از چندین گزینه تدوین‌شده توسط اوست — نیاز آمریکا به استفاده از مهمات پدافندی را کاهش خواهد داد، زیرا توانایی ایران برای انجام حمله کمتر خواهد شد.
- مقامات گفته‌اند که در صورت تصمیم دولت ترامپ برای بازگشت به عملیات‌های رزمی عمده، نیروهای اسرائیلی نیز ممکن است در حمله بزرگ احتمالی آمریکا مشارکت داده شوند.
- کوپر در جریان تشریح گزینه‌های مربوط به یک کارزار هوایی شدید، از حمایت «هگ‌ست» برخوردار شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69229" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69228">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3zvbzdaw4GKW6qZR9EYeamuTEc09Et-p0NiQxlnrw5b6hZpWZA4hpTcgkryP39pGNu1R4CQc1aNdC0_5crOgjvLvTecmS--DtdI8xXgnO17gvCH_DUdG1Wcxdh_FVlFYUVKLchAayB1yuK-7xRagvRCkr3Unk4P71GcC0Ssa3oTh5PnfZIb2YCApNfmarN1W67pipWZP5rSpFu0KvOccn47i7gUxMUbjQBHQZxMjfcr4mjtvoFeST3MSrx0YMxYSNat2rD0_-rO-ZxOFRFckOKg03Nw9qRH-7cmqQywIytqv3xeW1MbKv6_SjCCpwKVaPkgwfPn5rw-o9b1FB9mDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوووری
؛باراک‌راوید:
یک مقام آمریکایی به من گفت که ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69228" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69227">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در نورآباد ممسنی استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69227" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69225">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEvC7nKqyv4_371cyp2azjHlc28Uha08ICjmA62DC_N2frB2bjnkogCkeJmgL77YSfWVBEAAYeGiuUtCa-QkXE42fp8oumQxSxnjDSuY3N9H4vMvzNVRFC2dnMcqbBP0S2LHg1wHbvo5yti4D1dw8l92ITNxWJNR3uU-2UUqHP6fIxe2GVnEw5IP88wsyouEEoND21W3M6gVnzJgGCEBeUqWXJ00KMxoQzIg_-z-eFJ3hwd1iRyT2nrA-5iE0YHEkb1Pm1YZGdbFxRcIpDM3P_Wo2_xZ6c40AEK_MJLBKPXaHEs1ECyDbvaYZRz8Pewki2dROgHV3MlJaOZOSlAECw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بعد از توییت عراقچی درباره اوکراین، خبرگزاری رجانیوز، عراقچی رو ماله‌کش خطاب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69225" target="_blank">📅 01:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69224">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vn09xi4xMLdDP-R8t1AVF22_Fgoni5bOP1kbbqM4jbuDhtPMVHQcrkg7QbPMS6JSBeISC8fbNn6QSPQWCxrLKHu8q6ra4gRCEo87HDsv5czO5osWQNHflHuQS_1IWnGx3ePF6a_pkw7XIi5DtRE9PTyOB-iRvTg51h8W973ja83kvAoC-tcJ6wYAzh-aRlpPdCBfvLjlPCnx01dFHBYtRwFEZW6lc1i-hzgk43cCFr_6dlIMectsugHaRVv-SMz8QiVKrFx8OcV3C5d1gumNLZxfUv3amC6EUlr1iuk0OsBIoxcVqQoAhZ-oxRikjjYJpSmhXpxxzobMs1UfLdXvPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حساب توییتر خبرگزاری تسنیم وابسته به سپاه بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69224" target="_blank">📅 01:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69223">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_X7fEi1uAly44gDtp8_mmBYgtt8aitDpsKFfaxjSn-72Ec7L7eznoOFCbBuFy5z8YY84DWYETxeg2WbNmtagRPn_RTqeL_6DNstj20Nl6jE68rFpwbBPcFlaPAw518G6_eTaFZUTfb4MrI3Qsh9VLNRS09idh3jIe2QKIL9hl8C-jvinmD6vjQTlnsiPPgtTfOF9iuBKMTYjLlkuUeykSyVKIslRKkaEuhQggpO_Z3eH3dvy35Fe29g20ga_WjlDcgnoOcIWDO879KKpVjNBYxToSRIujotRy8JmASKnDeeHCvzQRu62S2Bv9tOcEh6fDhXgnXrEJTozqcGu7Ke9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏9 فروند هواپیمای تانکردار آمریکایی و یک فروند هواپیمای هشدار اولیه مدل E-3B در حال پرواز بر فراز خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69223" target="_blank">📅 01:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69222">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xe87eHgvWVmLBPSCi3PjXDJ6k29YvB105zBuDkAUiVfH2zlj-TAV5o99oQLHtMSs0z8Z2HIhWUQCPr0tB0RuO4PfUNh83c6mJKrgnBPUPdj_kGhLzJx-vQBU6gCNP0cp_oyqhu-ii-84EpvSNc_7gYw99X4D3TKWxNefB8dhVwFQ_fp-5bF1l0obY5PQQ7V3lK_MYXvuv6Xt1eQbC8vMOPA065SqDkR8IysYGeVJ0E7PMdrj5jChyoEGPQAlQ-77LwE1IWxuNR8xPsXTcvJBa4Cq-nNCMnnTTRw4OZ9F5Iy_35_qWFOurm82cLPMclfOj-M49kXHw5STw_XznO50NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شش سوخت‌رسان آمریکایی در آسمان منطقه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69222" target="_blank">📅 00:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69221">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد  @News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69221" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69220">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSsVwvHNau-XH6l_ny98xfcIkeVpviG8t42nHnzvUUps4ejNgOtnDyTWQHQ6GB-PpUIJXyfYI1V--61gAPIYMLQ73zrx90CTTfSBmmXslY6rGu4jGC3UeNaQhxOPUP6V9NSTAvnZbDZDkZZfX2dpBi-1uzFLLbjMqbsTyaY7wYR9qxNJk86_UevCvP1a7S7uglwNi5iZvg-1tCkA4ezGq1bF3VZYa0XLBDeMYQsgFq9Phs87cCBHGwPIv66e4JwZAAI3FURnamyyQf-cCBycO8bQzL3cLdM9T-KrjiEAODax0vFdFjwzihqxctlbpMMevwB7Ey69L7wdrWzKiVoigw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه تو تلگرام یک کانال و اکانت ساخته بود گفته بود هرکی تو اردن و کویت تحرکاتی از نظامی های امریکایی دید گزارش بده؛
لحظاتی پیش تلگرام سیک اکانتشو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/69220" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69219">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69219" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69217">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=pK3rEHtBuM7_BR4udxaRnVhogmSJPsDREf7RIKr4RPJY8-wb16VcyxnLYR1zL1Lg7krEKrDydn8z0KXSAuU3XwPaetfiZfn679D7nEV_mdV6FDM6wOJm8wsIpb01KfW-YLbVBLqNcjWplmpyqvjIaBTktgWUU5lmAjxOk0vlSN45wDHWUl91Hyt2QGXfeH-YG4tPLYizqIRH6hR5SZHFmrgoqFupTulBnkL2RMuw9Onma7Wd4iX-yPziLAWsFWb371InADXVVy38rmr9ao6AJ010-LWIhxw-pCXsXHVK28gm4SDpJ8ixrl87u9ZsFAq7hvP4_PkYBLIf_CFLQHbvNA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=pK3rEHtBuM7_BR4udxaRnVhogmSJPsDREf7RIKr4RPJY8-wb16VcyxnLYR1zL1Lg7krEKrDydn8z0KXSAuU3XwPaetfiZfn679D7nEV_mdV6FDM6wOJm8wsIpb01KfW-YLbVBLqNcjWplmpyqvjIaBTktgWUU5lmAjxOk0vlSN45wDHWUl91Hyt2QGXfeH-YG4tPLYizqIRH6hR5SZHFmrgoqFupTulBnkL2RMuw9Onma7Wd4iX-yPziLAWsFWb371InADXVVy38rmr9ao6AJ010-LWIhxw-pCXsXHVK28gm4SDpJ8ixrl87u9ZsFAq7hvP4_PkYBLIf_CFLQHbvNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی عجیب از تجمعات چند شب پیش خرم آباد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69217" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69216">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند،</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69216" target="_blank">📅 23:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69215">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6df873441.mp4?token=CakTE4dZtWz1JV0fzhnl5J1cqU3aUQHjBgdajn-wz91HhoczONkSBqvcSqNRsNPwf8uyZIGs5gND0fX3es7atVVWC-GmvJiGwEgVnRhvWoNG_-wEsyG6j1pgsBmNoOY4M_5l2rb5AT_GbcXt3OY4Ol5j7nGjFD0jzi9ihgjKJRfQgx-LOddaYb4xAXSLu9JANOHxNaUl5xrlh1fhyB-ByLzEAl5dnVip8oVo09QIW3vtY2lqWD9YZB7wm4c7KKCi36shszPn3zxoYc2lI3S92r_yGMdTJu_jd4_XkIVAwgOQn42Xl_7RlE9uH_H25CXfbZw3kjwzrgNC8DCgNgI0Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6df873441.mp4?token=CakTE4dZtWz1JV0fzhnl5J1cqU3aUQHjBgdajn-wz91HhoczONkSBqvcSqNRsNPwf8uyZIGs5gND0fX3es7atVVWC-GmvJiGwEgVnRhvWoNG_-wEsyG6j1pgsBmNoOY4M_5l2rb5AT_GbcXt3OY4Ol5j7nGjFD0jzi9ihgjKJRfQgx-LOddaYb4xAXSLu9JANOHxNaUl5xrlh1fhyB-ByLzEAl5dnVip8oVo09QIW3vtY2lqWD9YZB7wm4c7KKCi36shszPn3zxoYc2lI3S92r_yGMdTJu_jd4_XkIVAwgOQn42Xl_7RlE9uH_H25CXfbZw3kjwzrgNC8DCgNgI0Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد. این را می‌توانم بگویم، چرا که کار زیادی از دستشان برنمی‌آید.
این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، باید کمی آنها را تنبیه کنیم.
شی به شما گفته بود که چین هیچ‌گونه سلاحی به ایران نمی‌دهد یا نمی‌فروشد. گزارش جدیدی حاکی از آن است که ایران ۴۰۰ پرتابگر راکت از چین دریافت خواهد کرد. ترامپ: این موضوع تعجب‌آور خواهد بود. او به من گفته بود که در این کار مشارکت نمی‌کند. او می‌داند که من بسیار ناامید خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69215" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69214">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=nR3oLabd-LXoZrafNFutRrAKX2tNgJjA20VF_KE2hAizhV4Cn_qJQUHqyhX52zaUR108Md82dmUyCIpYMG_eX59k04EuZIJ3nM3KbN4ZvLc86alZr4HuPz7rJzDEmvOgFqsCBpXzSLtrzEo72hUAvnxsXWrTmT4YDbV-phOGeoctZkj095zt5iwjn3jxuy2CyB_-iJoWoYCL6KARUUQ41trUnREj0s6MBUF7VV-Hlpt-Fup-IbsSAuI9hwTXoYVuxArqUywbgP-_gmBjfnE9ErW_GLcoGZO1INN2upHwcB18yuoJdtdQDZ8hFN_TDC3rACAsDxjfG6vgOXZ7fb3YYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=nR3oLabd-LXoZrafNFutRrAKX2tNgJjA20VF_KE2hAizhV4Cn_qJQUHqyhX52zaUR108Md82dmUyCIpYMG_eX59k04EuZIJ3nM3KbN4ZvLc86alZr4HuPz7rJzDEmvOgFqsCBpXzSLtrzEo72hUAvnxsXWrTmT4YDbV-phOGeoctZkj095zt5iwjn3jxuy2CyB_-iJoWoYCL6KARUUQ41trUnREj0s6MBUF7VV-Hlpt-Fup-IbsSAuI9hwTXoYVuxArqUywbgP-_gmBjfnE9ErW_GLcoGZO1INN2upHwcB18yuoJdtdQDZ8hFN_TDC3rACAsDxjfG6vgOXZ7fb3YYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
این ویدیو رو بفرستید واسه اون تعداد از رفیق‌هاتون که عشق دعوان:
دیه‌ی شکستن کامل بینی : 2 میلیارد و 100 میلیون تومن
شکستن فک بالا : 160 میلیون تومن
شکستن فک پایین : 640 میلیون تومن
شکستن هر دندون : 105 میلیون تومن
شکستن دست : 160 تا 210 میلیون تومن
شکستن سر : 120 میلیون تومن
شکستن پا : 210 میلیون تومن
شکستن گوش : 350 میلیون تومن
کبودی صورت : 6 میلیون تومن
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69214" target="_blank">📅 23:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69213">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687c44382.mp4?token=F9rTfM99VDecBF0eJLSmniendl0jzBV-Ne-FNXBRh0ue1iIbaWnVC28oFYvFsh9tfWWh_BTyp_8CK1KPKk-HUPFLm5_IT1qMyaMh0UtSIS7YJFGRRDtF4c3WEPtEVG0xOEncH38qm4rtVvEEyMfEdfRZ8eO0CbOibI4wqxutUAYqgws0r7uACkp8UcJPA0kA5Kr6x856fSQVJiga7L_EVfPXi6OtrA6boLZFqz6epy_afzQlbuEoULWnTxyLSgwTjUqKxm40TApr_Wr3ZXenteTTjYpgBSJ16vf6UVrY--AHNOeBQKSuQGzz7ntsneN-sIDV_-vlevpOe-A5VDyJtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687c44382.mp4?token=F9rTfM99VDecBF0eJLSmniendl0jzBV-Ne-FNXBRh0ue1iIbaWnVC28oFYvFsh9tfWWh_BTyp_8CK1KPKk-HUPFLm5_IT1qMyaMh0UtSIS7YJFGRRDtF4c3WEPtEVG0xOEncH38qm4rtVvEEyMfEdfRZ8eO0CbOibI4wqxutUAYqgws0r7uACkp8UcJPA0kA5Kr6x856fSQVJiga7L_EVfPXi6OtrA6boLZFqz6epy_afzQlbuEoULWnTxyLSgwTjUqKxm40TApr_Wr3ZXenteTTjYpgBSJ16vf6UVrY--AHNOeBQKSuQGzz7ntsneN-sIDV_-vlevpOe-A5VDyJtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد، چرا که نوبت ماست که به آن‌ها ضربه بزنیم.
آن‌ها می‌دانند که این اتفاق در راه است و از ما می‌خواهند که چنین کاری نکنیم.
آن‌ها دیشب تلاش کردند با ۵ راکت به ما شلیک کنند؛ ما همه آن‌ها را رهگیری کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69213" target="_blank">📅 23:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69212">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ویدیو وایرال شده از یک پژو405 که درحال فرار از دست مامور هاست اونم بدون لاستیک!
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69212" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69211">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkNhCYn34_6w1ecj2VOG_fxSGAkSQesyrRcOa63a1XH536bw7KXKePUp8oJp7fLJNc2p4jp5534wWZJspzmT1UKMifZOWDhazYxttqg-YGtSgDynhuT7lAo8tiFg37JiF9FUfgJ5Pyc5WmvgFo1-yiKmDINY_oe4HqyAhA753DGkbzwrTnb62wm99n6T3mTBiKZNw0LXxawxNfM02TDwC4g2qPZiVwrmFCnHFrNKo947ongrYqfoF8XzMac5bf1gDUL_M3K6ecM3fdKAf6bJ0hW7JoGRLSZYntv10aNBz7yPzwBCaNKiRDyUvhigLmROP-PbkEOazAE_7eB85c8W1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.  حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!  @News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69211" target="_blank">📅 21:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69210">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSngklUXBzDIfTwPdDrDwNm36Rrk-yASqU6dTdE5_TgmOa8Klh3dcQ-_X45GBC_dFKWFDApV_7heTYwX3Mu1Y7LtHA6icVlB8StjuNTPjulTHtwWU4kC-rN_Np06P83M52eWlSGEr0gQH8Uam3ts8OpcUdkboRlMdy9Tceo81_m5yxPah2rE7KyKFXfcf7gidRohhGv9D4-jASh4q1_YmJosFXgOSELcX_mv7IyxawYU98siGOluijPyzi98k25sfi2WukD4b8gCYdl4ECF3q_7t_p3C37QFweqAMEh4zxeylI_Z7PzbWgBbGokPWNEWh9ncZS6QEQiFKSEwGNf-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
❌
🇸🇦
نیویورک‌تایمز:
حدود ۲۰ مستشار ایرانی در جریان حملات شبانه آمریکا و عربستان به شبه‌نظامیان مورد حمایت ایران در عراق، کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69210" target="_blank">📅 21:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69209">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HePA26Q7m4rZ0Qldc7ml8EmyJYTIYIPrhSURUJLTtBM-Wh-lsCG6CU_oAcIlicZWOMzw0N8_EXginc1lHTiFDIRIp9vznN-FWjZWU1nyMwsZMmOv9f5ETlS666PMexxSNyrbRXnR_yvALZFnYoU-mlExdU5jv0wrdNQbwpxsTjNw7hQStOnnvkRkzyFzVPXPD7O3hm-Cbg-2OvCZjOTM60QZfHx_HNaAnnrgXK9rq6ccBR0C1Yx1YdSncuEow0Ubw6ubL81_1sB06zRd420DJKxPSbo3VX7oIvXQ89NQFd_ZaMnniCNVczZGU6v_4-KuORhhE_0scF_d8H28gHtjZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.
حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69209" target="_blank">📅 21:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69208">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=DnCIK9xFPkywTcpVrLxQ4eciE1ybZON3_j6oZNrUa629irDguS9kLY8wp_NQc3r666pDg5sI5l5OE9zjYvK5LE7kcTPFs4Sdr0zq-KgODV_mjWIB9XovEp2bdn6FBiM13JQNxYa_PzvY268EbcFxxGDXUVff2eKxeB7e_etDNf_XGtp04P7X9ddQOfGwoyOL85YTFfhmApUQXrP0uMDWP3vxsrBxn41e6AdjpsPbcHyqF9LAoiextSte-xIlflQoGLRJIg3OfokUJayPPvGU6PuY4mF4L1pjRlqppQcJMIauooqcpgugXGin3h05Maac1pvzQGpQ8YCB3l6s3ptQbjyF7LjQQUs83Pal6kG8PVnGv6Kmwg6MFpl87pymMiKK6kwkaxuVk9kGPVKuXXrCEaZEyvEnDbtRiv-dEDO-Ku2wp98IBjAhWKSBWzd0IzwVDkzyuWkQBEf55UnE4AjYKI61rZP5hK9D-ScOYnb2mu3N5DFD-WmCfyecTrHrZq3pSB68boH_YpIJ1nxzY4wEI0wz0NJ6eqyWXQm2PVGsC8mdhHOElBi14aTZP_yWph9fWvJgoKDDw17iDMzwAYSKH8gnpczhrI_HuCAXT4RKSdmD_PEwGkMm3rLe3HyIAtItSF_zEy38OD7Q3-vSZNxjdt_QMF_CQHhc0JWziahXP9U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=DnCIK9xFPkywTcpVrLxQ4eciE1ybZON3_j6oZNrUa629irDguS9kLY8wp_NQc3r666pDg5sI5l5OE9zjYvK5LE7kcTPFs4Sdr0zq-KgODV_mjWIB9XovEp2bdn6FBiM13JQNxYa_PzvY268EbcFxxGDXUVff2eKxeB7e_etDNf_XGtp04P7X9ddQOfGwoyOL85YTFfhmApUQXrP0uMDWP3vxsrBxn41e6AdjpsPbcHyqF9LAoiextSte-xIlflQoGLRJIg3OfokUJayPPvGU6PuY4mF4L1pjRlqppQcJMIauooqcpgugXGin3h05Maac1pvzQGpQ8YCB3l6s3ptQbjyF7LjQQUs83Pal6kG8PVnGv6Kmwg6MFpl87pymMiKK6kwkaxuVk9kGPVKuXXrCEaZEyvEnDbtRiv-dEDO-Ku2wp98IBjAhWKSBWzd0IzwVDkzyuWkQBEf55UnE4AjYKI61rZP5hK9D-ScOYnb2mu3N5DFD-WmCfyecTrHrZq3pSB68boH_YpIJ1nxzY4wEI0wz0NJ6eqyWXQm2PVGsC8mdhHOElBi14aTZP_yWph9fWvJgoKDDw17iDMzwAYSKH8gnpczhrI_HuCAXT4RKSdmD_PEwGkMm3rLe3HyIAtItSF_zEy38OD7Q3-vSZNxjdt_QMF_CQHhc0JWziahXP9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کشتی ترابری گاز آمریکا نزدیک بندر دمیاط مصر با پهپاد هدف قرار گرفت
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69208" target="_blank">📅 20:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69207">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=EhpngwdnlQyycsrZbSrtwM7JWOxvJl46YuKe77kJRSLqpO2jVWrMrYj8SaSLyh0DDo1hSXLAXW-6f6EG8UllmWgIMLeCkE2EtGF1ZoVfjMY4hoBFEaQcopCaaDgvAB8h5KuPMpEme3lRkzBwdzR5QI8N6BB8Wy1ssFIR0-dxFjpGc9UXqEfKkT3Ji4ZKqvqxfuS2sYTIRB_QflkX2YcDOVmZd5eiPcZZoMXcCQY3AVILMDzh1XmTp8Jj7dtxT5A22Z2NwOWbsDIkn_MOvGutIZrGwNKGo8F4n4zK80yEmFjFF3I1dmCipA19fJEx1SmxXcbMgTkEmyAXz0uOkKZltYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=EhpngwdnlQyycsrZbSrtwM7JWOxvJl46YuKe77kJRSLqpO2jVWrMrYj8SaSLyh0DDo1hSXLAXW-6f6EG8UllmWgIMLeCkE2EtGF1ZoVfjMY4hoBFEaQcopCaaDgvAB8h5KuPMpEme3lRkzBwdzR5QI8N6BB8Wy1ssFIR0-dxFjpGc9UXqEfKkT3Ji4ZKqvqxfuS2sYTIRB_QflkX2YcDOVmZd5eiPcZZoMXcCQY3AVILMDzh1XmTp8Jj7dtxT5A22Z2NwOWbsDIkn_MOvGutIZrGwNKGo8F4n4zK80yEmFjFF3I1dmCipA19fJEx1SmxXcbMgTkEmyAXz0uOkKZltYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نخست‌وزیر نتانیاهو:
«سفرم به آمریکا فوق‌العاده بود.
همیشه درباره موج نفرت از اسرائیل در آمریکا می‌شنوید، اما احتمالاً کسی از موج حمایت و علاقه‌ای که نسبت به اسرائیل وجود داره براتون نمیگه.
همین الان هم با وزیر دفاع آمریکا،
پیت هگست
، صحبت کردم.
اون یه حرف جالب بهم زد. گفت: "توی دنیا کشورهایی هستن که اراده دارن کنار آمریکا بجنگن، اما توانش رو ندارن.
از اون طرف، کشورهایی هم هستن که توانش رو دارن، ولی اراده‌ای برای این کار ندارن."
بعد گفت: "فقط در اسرائیل هر دو رو با هم می‌بینیم؛ هم اراده و هم توانایی."»
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69207" target="_blank">📅 20:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69203">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PF19xvvh0yxCSWE7ivKbY0QH4AMa4UtzXp5602oB9QHZQ7l71jEW8DLNdkn6jzpZ9d5CTLq89R9E2DXyOjtvtsMhtdi5CZKjPhAtLfmrg_Io6hRDLkw5ltggW1RhzGsdBSLQppN3uf0XCzCrEArkYhedf2dMq0GgXTe1ALC2P60OPA9UygO-vhPtfgqjc2QheyHtd2xlQzhiaun--E3KrfOv_5C75CDVvVtnqNgCNpogMj4cJCV3w0QCxX2I5RooCGXaLYHXX9P9Hf-rGyVC-G-MeB4TzEgTMksvotynnM7sC7nhEdS_ZGMIrIcVEnoQHFUu70vCZaTpBx7ocKjXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=SIZ2LW-FawBaPKM3NTQiWgbspDSwsNpQXuy89qusuPuD3_tFj6SR0XTjwuCJjKOP7U8AWK49o9F41xPOFKL4kC3tR7JaMORH1u_H2QQw5qVXxEUouO4g8fo7bSVuSYWtnZQ3dor1OJrtYZJO2ZX-XaGAJ8thTJbxsbkgQS6P4aXpYroJ5bY0nzYqLW1zWpJZDqRAESc7mENUjYddxpO-xyblZ3R64YcmTtxJQEf2OaaMQ006d51c_gxSCS0eWKsyCmP1wiNPgnNxhULWmtJcLtHguoGigVg3lBb8fjldELu7HjgFRYN3UosCZOulCzt9y8eWBGuWmiBzMJL0dW9n9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=SIZ2LW-FawBaPKM3NTQiWgbspDSwsNpQXuy89qusuPuD3_tFj6SR0XTjwuCJjKOP7U8AWK49o9F41xPOFKL4kC3tR7JaMORH1u_H2QQw5qVXxEUouO4g8fo7bSVuSYWtnZQ3dor1OJrtYZJO2ZX-XaGAJ8thTJbxsbkgQS6P4aXpYroJ5bY0nzYqLW1zWpJZDqRAESc7mENUjYddxpO-xyblZ3R64YcmTtxJQEf2OaaMQ006d51c_gxSCS0eWKsyCmP1wiNPgnNxhULWmtJcLtHguoGigVg3lBb8fjldELu7HjgFRYN3UosCZOulCzt9y8eWBGuWmiBzMJL0dW9n9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین با حمله‌ای گسترده و پهپادی، منطقه ریازان روسیه را هدف قرار داد؛ در این حمله، یک مرکز لجستیکی بزرگ متعلق به شرکت «وایلدبریز» (Wildberries) آسیب دید و بنا بر گزارش‌ها، پالایشگاه نفت ریازان که تحت مدیریت شرکت «روس‌نفت» (Rosneft) قرار دارد نیز هدف قرار گرفت.
آشکارترین خسارت در انبار حدوداً ۱۸۰ هزار مترمربعی «وایلدبریز» در نزدیکی شهر «ریبنویه» (Rybnoye) رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69203" target="_blank">📅 19:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69202">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
⁉️
آمبری:
یک تأسیسات شناور ذخیره‌سازی گاز طبیعی مایع (LNG) با مالکیت آمریکایی و پرچم جزایر مارشال، در دمیاط مصر هدف اصابت دست‌کم یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69202" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69201">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=qYiHudfPjABWu9xC4ZHfGYjD9XGRNzcB_sV3vR8qyZi-Acr6tU1gnHeTv3QlyB8qg1Rltyk9GNCTTI9zgaQc2Ij4Fojd97kqaOCjIcFo5xyHbrKM0W7uAJFL-1GdcTAKJgtsrRV09A9ixe-aiZm63jpKGV0UzcsPXFwgkOJ1XGw_TF9aTkOUDPfqOHTdjtMUgxJ9jcn3tb2KoI8fZLYmEekY57emL9fw1NMOZ4QegYa9y3NqR-xqXgiwujSZiUbVcSjR9LEUipmcJX1Cd7k_yyaymzNKsdTxEfcFuqgICfyiQqzivmUtCzJ2rU72hFsn4ZmKxZaBPNdK5Iwn6xDccg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=qYiHudfPjABWu9xC4ZHfGYjD9XGRNzcB_sV3vR8qyZi-Acr6tU1gnHeTv3QlyB8qg1Rltyk9GNCTTI9zgaQc2Ij4Fojd97kqaOCjIcFo5xyHbrKM0W7uAJFL-1GdcTAKJgtsrRV09A9ixe-aiZm63jpKGV0UzcsPXFwgkOJ1XGw_TF9aTkOUDPfqOHTdjtMUgxJ9jcn3tb2KoI8fZLYmEekY57emL9fw1NMOZ4QegYa9y3NqR-xqXgiwujSZiUbVcSjR9LEUipmcJX1Cd7k_yyaymzNKsdTxEfcFuqgICfyiQqzivmUtCzJ2rU72hFsn4ZmKxZaBPNdK5Iwn6xDccg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیت هگست، وزیر جنگ آمریکا، در واشنگتن دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69201" target="_blank">📅 19:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69200">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P52E2XNtsMyL9lJkoPHaNjFxHgMOCf3fM1tgJzH699jjAHNF_T5UZlKiSB2ljQ_ZE8m2gJkKPlFSoxtOVFeE-TFBhbDszvgeOzknIIUPPfV4_RrqyGnMmUV3yuEmMVM44nfL6cbOrlLmYgkC9EViIQIvt9QcZih6eSlyJ4Y792okKWQ9z_fF0dSn6eq_nZC0feB10OqhvIM0mMD2iqxbqJZ3bDlBsyKQo0nXE_RpzY2CUo09e83kRY92umv_VjKoV8wdgybBXNUDjbPtEkpoagn7bHgRN3UrlmZlfELcAZS8DW8nf0XuBOkSIPZx2ihpdKqa2niMZ8C2DCoqV8YcTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنت‌کام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران (IRGC) پس از تهدید و تلاش اخیر برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناهی که از تنگه هرمز عبور می‌کردند، همچنان مدعی است که دریانوردان بین‌المللی باید تنها از مسیرهای مورد نظر سپاه استفاده کنند.
✔️
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه پاسداران هیچ‌گونه اختیاری برای تعیین مسیر جهت تردد آزاد و باز ندارد. کشتی‌های تجاری همچنان با حمایت نظامی ایالات متحده از این تنگه استفاده می‌کنند. از اوایل ماه مه، نیروهای «سنتکام» (CENTCOM) به عبور حدود ۱۰۰۰ فروند کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69200" target="_blank">📅 19:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69199">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇮🇱
یک مقام ارشد اسرائیلی:
ایرانی‌ها سانتریفیوژها را به «پیک‌اکس» (Pickaxe) منتقل کرده‌اند، اما اسرائیل از انجام هرگونه غنی‌سازی اورانیوم در آنجا بی‌اطلاع است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69199" target="_blank">📅 19:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69198">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKypVckndDD2uWSL2mDRBV39H6xUixmIWJZyPle5NdK0pAbS7w-d9d5-UIwxZEEXcMYRYa_WiWgt7u1XYF3HxhFWlGxAdzFHTuyoxNcOamjFf1Dy9Fvg75X14LEzKYjNlMIyr67QVQoWGLIaHXs67Ezt3sK11dLu4i-ss4dCMmKDhMgQhaPStHszKI5TUcWXCdzGkZaHMeKeYjK6qHMReWl_3SrQhkMo8zpptzw1FIlj8qzJ5CRTKvMbNpUVHDZvEwbwPNBj7VZQ7YzG4B12k2JLgOcU_OBDryxxgWvkvknHi9mIfkilTueVq0Pr_7s_zu5Xw9sTksyy2tklsPUahQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک‌راوید:
معاون رئیس‌جمهور، ونس، روز سه‌شنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار کرد. یک مقام اسرائیلی اعلام کرد که هگست، وزیر دفاع، امروز با نتانیاهو دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69198" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69197">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jssStSfpvCcpC-zCJt1c8fLpJKYIBIsbh3lezKTN3Yd-0vyFvdFRuAwjqF7ASCt7wGHZitRrIgy4rx6K4IFtb60G60o2ncuEbjWCF7ED_F9BYHQiGVo-rFIggkrc-g-x3Qojep-9MJgwqjaWxgMnW_ZxIvS2x54b52A65mNJgWpJhPPj6DbimugJkENPgthSG-VNmmZqxMline8LfbA1qM7SLiHErIgb8scwN84uaZar2yo2jQRpQsnHz0TaDnRNCjnACo-PuBAYXNHSbnP4ph3B7uXOSXpRxJVIt7bEf4nv5csrJsh2yoR3vtypWTuZfDg4SV1lXve0ewkgY3vGXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تلفات حمله مشترک آمریکا و عربستان به حشدالشعبیِ عراق تا اینجای کار؛
- 20 کشته
- 32 زخمی
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69197" target="_blank">📅 18:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69196">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oS4E2UN2HcdE4oCc2b8ZA3KQpUApV9dvm9LyoC9eCJEysJLvP5nqsc_9gyY5KBL99KoBzqLeCph9K4oE2up4Rf975LCbX9L7bO9aAO0-0v4fLNBDQyrJHqSTdrsHXmNeKV6MKBVTVpcZe_Xt3SXUBLEdxjNzJZ8DrwfCSVkRXDoIirlT5DdtZOoPI2v2aggeohsKpIDZhkSv8mId82kQcaM6Nicz1nB2e5XsYglo9u6ZuTZ5IakATa8QjOuZlYPZ60MhpSFIyo0m0StZbREXWjU92gT76H0hsT3ju7oT-8BiBaM_kkUQTNujbLVZzNiBsAtTL-i9_LNWbkXbrYqLtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇷🇺
پروفایل عجیب پاول دوروف مالک تلگرام در واکنش به تحت تعقیب قرار گرفتنش
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69196" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69195">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=tcoOBW5NU9EzjNj1qC2pehZDDTBUoeG6youmCvYBE5heJZik1hGFTFoE6FmrlErkuij-1o-D5G1uIKRCr7Px5RhMgEyiUF1Z7EAJujVmz_1BBjKgxaeW-F1F7ExQ3Sjr1aGDC-UoVp32Xl0nvn_y0Kt_DBZ1bum_p5R6CFfC-1oGzQ1MBlx_WohEG2PrX6nMkgu0Odfd1e5tI5WeSkTRSxpLfZlm0kgziiybyTLe_JixV5EoeP6gmbRyRrXzplgPfWr6FwhjInqDUR3PJhEkIbTfEMbBbCq18ZSRabf7rZaG8OWEgqbp24DgvbpMTHnGWMyvITXmjyf5-ywj6px0NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=tcoOBW5NU9EzjNj1qC2pehZDDTBUoeG6youmCvYBE5heJZik1hGFTFoE6FmrlErkuij-1o-D5G1uIKRCr7Px5RhMgEyiUF1Z7EAJujVmz_1BBjKgxaeW-F1F7ExQ3Sjr1aGDC-UoVp32Xl0nvn_y0Kt_DBZ1bum_p5R6CFfC-1oGzQ1MBlx_WohEG2PrX6nMkgu0Odfd1e5tI5WeSkTRSxpLfZlm0kgziiybyTLe_JixV5EoeP6gmbRyRrXzplgPfWr6FwhjInqDUR3PJhEkIbTfEMbBbCq18ZSRabf7rZaG8OWEgqbp24DgvbpMTHnGWMyvITXmjyf5-ywj6px0NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.
هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا رو گول زده و برده خونه
⚠️
ویدویوی کاملش ده دقیقه‌ست اگه خواستین می‌زارم ربات ببنید
🔗
🔞
مشاهده ویدیوی کامل
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69195" target="_blank">📅 17:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69194">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m09AKzT_a4jKHONPULOf-fPPj60yFu1M1mjmx3L3wcsUtQXiGOl6WFzJQhyxDrpFUxdlfIXyCA92qn3WnLq3PkywY9qTivXBvdKeDQ63nzhot9xjkfeV11XV6O4SvQqYWJi6yOwpnGh1VW3eRVJ82Ht8IDvYvdU7CTdJBQdCqvr6rKA--pd7GhjqgyujRwovU46sgp_zjWA0cPyP4hqbK7p04ZSo6MUiUxEH4cqFXg9hKt_OSEl7O_L6ojGvJJ7ixYYgVyI_4ULiH2ojgEa8HSley9rTT10yJQEzP3BHlix7ASFDMcLvRPpbd-4mjaC7X_qXCDhj2YTV1q7mHt1PnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی ارتش جمهوری اسلامی   اعلام کرد بقایای پیکر امیر سرتیپ خلبان مجید کاظمی یکی  از  خلبانهای  2 جنگنده سرنگون شده Su-24MK که توسط F-15Q های قطری سرنگون شده بودند را در خلیج فارس پیدا کرده است و از سرنوشت ۳ خلبان دیگر اطلاعی در دست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69194" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69193">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=c6NelAfxXtfO37a6SAxW5YCS70LZHdHNBweV0BT5SP6Yho02OWJmHgdHpVObSiXmnTC82evI4PHeka-v35Hl3Q-ld0eDx6m5tkKQigfD1uBJzU582vsyx4ehQnENjgKF6TmhnG9fbJhNM8QGxFsBsRdRnAMUFQrTPkl0R9dBx5M0D2hLOfGZhyG8DdUPrJOMKbnoHG0NGB4WZKxL3-h2LsrlkLK5uQ-NoKnIzd_zI3JzZoeZcBpjCwcdz1UiaXU8OcE5uOvZdgUVhRgRjvtVRI0H0Y5k_LiEtac9jrXQtou-ZZ9Zr-QezCWeCTlCcicGLyb0KnWh9Bg--vvagS-0MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=c6NelAfxXtfO37a6SAxW5YCS70LZHdHNBweV0BT5SP6Yho02OWJmHgdHpVObSiXmnTC82evI4PHeka-v35Hl3Q-ld0eDx6m5tkKQigfD1uBJzU582vsyx4ehQnENjgKF6TmhnG9fbJhNM8QGxFsBsRdRnAMUFQrTPkl0R9dBx5M0D2hLOfGZhyG8DdUPrJOMKbnoHG0NGB4WZKxL3-h2LsrlkLK5uQ-NoKnIzd_zI3JzZoeZcBpjCwcdz1UiaXU8OcE5uOvZdgUVhRgRjvtVRI0H0Y5k_LiEtac9jrXQtou-ZZ9Zr-QezCWeCTlCcicGLyb0KnWh9Bg--vvagS-0MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله اخیر ایران به اردن:
این یک حمله غافلگیرانه بود. نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69193" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69192">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=cymAxOKR1wvr0XHXL9t-jsHuEbZastqiH85XoBBXNjqDzyBNOx3IHbZDuz0ID2CVwlAaCPucJl3bsFN9Q-ugbCXIlmc5bDE36CW_IFVeSjJDM4BmaGqKcyNfIaPTTZU5VJUGYdRVPmottYTHtkI6XIn-PEps_04cBB7Pe4j0kfEP6hz7VM1ClFJJgZYQUSUOzyrznQUXpsYAV5f8_1K5DhhzmNTm1oz_tBl-53gcrKSJLSiiGYG9pvxPSacUv4NcbeEdI-VyUq97n53kLbcP8OE05J1AYi9KRILT-jVwVo9052y8Oh6CYNvgxoB6tZyWwOel0-F8OdcoU5O8px3VEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=cymAxOKR1wvr0XHXL9t-jsHuEbZastqiH85XoBBXNjqDzyBNOx3IHbZDuz0ID2CVwlAaCPucJl3bsFN9Q-ugbCXIlmc5bDE36CW_IFVeSjJDM4BmaGqKcyNfIaPTTZU5VJUGYdRVPmottYTHtkI6XIn-PEps_04cBB7Pe4j0kfEP6hz7VM1ClFJJgZYQUSUOzyrznQUXpsYAV5f8_1K5DhhzmNTm1oz_tBl-53gcrKSJLSiiGYG9pvxPSacUv4NcbeEdI-VyUq97n53kLbcP8OE05J1AYi9KRILT-jVwVo9052y8Oh6CYNvgxoB6tZyWwOel0-F8OdcoU5O8px3VEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک آفت جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نیابتی ایران هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69192" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69191">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
در پاسخ به حملاتی که اهداف آمریکایی در اردن را مورد هدف قرار داد، حملاتی علیه ایران انجام خواهد شد.
ما ایران را به شدت مجازات خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69191" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69190">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQBLz6dcE7DJiy9j-uDtq3LuT8f9ehCqZeawXgAPlsiCCiuoj4UK6BvfHd_bXMltALpR8NKW_cZjVd_scb7DyZCzcf8EVIgvsMRHCQ1oEG54pc6xRju6jkywT9WXuVpj86xIeFu7tfMxLCm_DQBzIlR6c6Lm6aLRkHsyta9Ud6ocX6dCOxnEaQwAVTAsjkcn928pWNiPdy10iIWDUjU987PGVUlOA6OS4qmGC2ZRnd9SSScTTGj6cA0FheMak8tAL1A7Nls9r_H3WA5EdWXWJbXw-lkvUAoR32u05SqZpJjufZDvsxv_j46rfuiiRXCCWgTmsnUefYVCFjSn2IyI4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس تنش های دیشب، قراردادهای آتی نفت خام آمریکا ۴.۴ درصد افزایش یافت
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69190" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69189">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=ZHWI4lJP0unzz-R5ocBD-LLZK6t0NUtyqU5zEZdyMxV5frmJMnzZb86WOvJECdpdh_CcnTXdGId2W1QwoGLoVdIoWfncwrsGxmibdkliCN-WNJMAF5Mja8_LdhyYASczlAXNiA-GbrGw9DB5-rFnx6WCRgNeTsOltch0QakXDIpodxoQIbRPmvANLoqrx6Yj1j62pJtS_BTW_vCr1GyO6A_IiLePt9losK6I5IUt5NbQV3QIvwy9Xa2ccJxyj_v3SZl8XMCj3X7tW6YNxgeWSzRmJaJYBipNHha-pgOqrCu0Qhh6DUc0mFH_q9VarL5TSaQ06MZyqRTXocM2OXhK6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=ZHWI4lJP0unzz-R5ocBD-LLZK6t0NUtyqU5zEZdyMxV5frmJMnzZb86WOvJECdpdh_CcnTXdGId2W1QwoGLoVdIoWfncwrsGxmibdkliCN-WNJMAF5Mja8_LdhyYASczlAXNiA-GbrGw9DB5-rFnx6WCRgNeTsOltch0QakXDIpodxoQIbRPmvANLoqrx6Yj1j62pJtS_BTW_vCr1GyO6A_IiLePt9losK6I5IUt5NbQV3QIvwy9Xa2ccJxyj_v3SZl8XMCj3X7tW6YNxgeWSzRmJaJYBipNHha-pgOqrCu0Qhh6DUc0mFH_q9VarL5TSaQ06MZyqRTXocM2OXhK6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم ختم اکبر عبدی، مهوش وقاری وقتی داشت درباره مرحوم عبدی مصاحبه می‌کرد، یه پیرمرده تصمیم گرفت وسط مصاحبه باهاش یه سلفی بندازه
🌟
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69189" target="_blank">📅 15:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69188">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUibDFIeOG7glnVDPygztljz-AnaHIlyoy6TQ5fDe21Lta3Nl239K7rVV5sOAfdAGA6dWt3ZwXYen_WRni6cqGxG_3lE8lk75s3gA8GNkd-Bto4An1NNtzQQ-iaSwI4VLeS5d_5NnL-sAnNgKNVUQAWHFh-X1wXGIi4Dpo2zMeUNhtvcDXdbnm6F7pl2BLD_EsYiMeTjW54iniXxaPfQ2Q8b_jKPXsYwaXmJJx6uoAoAyUqmyBk3-FX2eUml6g2Y-zLeaYfiwPG8U2Sz-C3lVYzv8DNOOf7MWYeBj7JkpLHeO05FuUUVXWLt5w-iO3PobYr17VmvigtSBchK1u9MqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.
۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که در راستای بازسازی توان دفاعی این کشور در بحبوحه مناقشه با ایالات متحده صورت می‌گیرد.
این خرید که ارزشی بین ۶۰ تا ۷۰ میلیون دلار دارد، یکی از بزرگ‌ترین اقدامات شناخته‌شده تهران برای تقویت سامانه‌های پدافند هوایی کوتاه‌برد از زمان آغاز درگیری با ایالات متحده و اسرائیل محسوب می‌شود؛ درگیری‌هایی که کاستی‌های موجود در توانایی ایران برای حفاظت از تأسیسات نظامی و زیرساخت‌های راهبردی را آشکار ساخت.
به گفته این منابع، این قرارداد شامل خرید ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، از جمله موشک‌های چینی QW-12 و FN-16 است.
این قرارداد با شرکت «ژونگ‌چینگ بائوشانگ اینترنشنال اینوستمنت» (Zhongqing Baoshang International Investment) امضا شد؛ شرکتی مستقر در هنگ‌کنگ که به گفته منابع، به عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69188" target="_blank">📅 14:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69187">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KV9L-h-NVmodXClV-lTzWeXdF3h-hfvnGNJqL43VZGfutkozTILFPF-KHJ3XJdY-TtLU7D14RIDSqCHbKV99sweo8kfSy-c1lV2PY5SFEWik4lf3vZkgigQQTZNHIDgNl1oA2uM2lK2lYgAKBAYhJ6ngMxIsBuaqewbOv9f3RwboCYtG4mXXroRL-E8-Q59Ph9liyuLhj32SyebAn527mkAf-6GEL4cqkULNJ3mXv3sDMRW40rCI6miNiR-p2o6k-dkOrNLHjA1OqFuLCym-ndf9ffdWEu9HEOWFseVp3rVJDxLKbyHYg0J3PseUwO0bI34uqxYNkVqPd0Nb7B5UvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عباس عراقچی:
وزیر خارجه اوکراین به من اطمینان داد که
حمله به کشتی ایرانی عمدی نبوده
و اوکراین هم
دنبال تشدید تنش نیست.
ایران هم قصد تشدید تنش نداره، اما
به‌صراحت اعلام کرد هرگونه حمله به شهروندان یا منافع ایران غیرقابل قبوله.
خسارت‌های واردشده هم باید جبران بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69187" target="_blank">📅 13:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69186">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78f023144.mp4?token=XOk7RxI0FYWC9IfPNKAEPbMignGZS4PuNpHwTWmydFjqbZu9_aaf9VTHS-oqBXB8ujHxRmSXAFv2lVHvujt5czXtjlRqYhdijp4yJFAGSu3xrTVFMoKG_Er2CMyoYvHI9MDCjyPXc8icfsSmqJwomOUxMOaZBMpyPDefJLPumJcmbbY-seDQQ9SK3EKHA2EHbBi-dhqYuz-CBFwRaLiQnKhnhmmjV2KXaXi8eXMQyK8GtBlBStvwMf9SWYEQg08E1jTyXYzGBSUt-Pc9bIoD4pD1Rs7cxAZEcpaAieROXVoZhXDw3ixhDIny0D4KUV_ELG7fbEcpH_OW0clOShQPJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78f023144.mp4?token=XOk7RxI0FYWC9IfPNKAEPbMignGZS4PuNpHwTWmydFjqbZu9_aaf9VTHS-oqBXB8ujHxRmSXAFv2lVHvujt5czXtjlRqYhdijp4yJFAGSu3xrTVFMoKG_Er2CMyoYvHI9MDCjyPXc8icfsSmqJwomOUxMOaZBMpyPDefJLPumJcmbbY-seDQQ9SK3EKHA2EHbBi-dhqYuz-CBFwRaLiQnKhnhmmjV2KXaXi8eXMQyK8GtBlBStvwMf9SWYEQg08E1jTyXYzGBSUt-Pc9bIoD4pD1Rs7cxAZEcpaAieROXVoZhXDw3ixhDIny0D4KUV_ELG7fbEcpH_OW0clOShQPJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسیار کسان به این سرزمین روی آوردند ولی‌ همه آنان رفتند و ایران ماند؛
جاوید و پاینده ایران
🫡
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69186" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69185">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIfYpdFRXPv8_MZTsLOKtZ1WGqTb5ecOyZVtbJMDQf9lbF5vSfHeouN2QOE3Ldzrj7ZqI2gufIdA7JmGruNbW1Zt7SYoMZxQCpeQH8ofHIfU5cfdZJsJmQndQ_mJkwxJzwdoaFExRlcZL0wu8qkkPhVChnUNC4PO0ksNzs1JizAzWquG_91FsRdCcn3Ar-hTvLeXJ_qBmT1IRBZdvg03NNyXG5gXP59EXH_HN3FXOEJW3rducPXq7WEPA8s789F46xycQxKpLrrzQiZcslhKwbZ3FrzuazQk7mQBpZx3VlVXH8MKDWOXrUmnW1OswHY7NQcbxEAJIgTDx1LRjrntzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایران پیشنهاد عمان برای مدیریت مشترک تنگۀ هرمز را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69185" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69184">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaQkmv_WugOctyGiF7mtbeMIYe-f38jUove20F2L7uMTQkkj4Vz5um24__yU_G7CcTvQiJ4k0MSKSI5oADIxNxAITrPYqoYfR7rRjhoJmI5vugN8x1wAc_69W70weUljs0wADwnBlh3BnSFFIbxYFNDhdOTStohdcF33jsTtGDFTwWLEL8ou0xgHDJYp1mIJH5U-s1bWfCBKcTaFIsVwpHdTRMsJHdtZ0O2ZYMiavEFQwScP1nBZiUbrSU4Boko_mJYjGGx3LpGNoS6T_rJVJDoVWevoWaqDDHcK9-SV21rkUs8nVLB0dqpWg38mCC2v5W3wE1AQr3fprZpDQ1BFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
نایا
:
موشک‌های ایران، همسر دوم رو لو دادن!
یه زن اردنی میگه موقع حمله موشکی به پایگاه موفق السلطي، متوجه خیانت شوهرش شده
😳
ماجرا از این قرار بوده که هشدارهای یه
گوشی دوم
که شوهرش داخل کمد قایم کرده بوده، موقع حمله شروع به زنگ خوردن کرده و همین باعث شده بفهمه اون گوشی رو برای ارتباط با
همسر دومش
استفاده می‌کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69184" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69183">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=k2jcDso4zsnns8VUiNmnxGxv3oKP9wIZWav2id1p2gNgfT0I7OTjZm2M9FguGGwqeS-kQWaL7hKVq8Z5nmMN_s4rMhJYXJ9BDUeS3MA50CNaqWvFdh5XGYwFPkoId7Dpv1_vDVY4I_Kc3EAfhENxbB_kN4yNFF5PinI0Tk4adsLuqGZVBq0rRdyHn_09jVaCY55jFEG6c8vL_ZUWaFTnmQanCozDCC4hLTwMm8jtInK46caFy_Exyb_V0fpcHOd0sTikafdrqJMv5Jq6THn1qYZ07KxTWeWL0a4StpiZwv8ihDAIQrePANmYVWmz5bueQiuh4sOkD5WDZziK2RDEpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=k2jcDso4zsnns8VUiNmnxGxv3oKP9wIZWav2id1p2gNgfT0I7OTjZm2M9FguGGwqeS-kQWaL7hKVq8Z5nmMN_s4rMhJYXJ9BDUeS3MA50CNaqWvFdh5XGYwFPkoId7Dpv1_vDVY4I_Kc3EAfhENxbB_kN4yNFF5PinI0Tk4adsLuqGZVBq0rRdyHn_09jVaCY55jFEG6c8vL_ZUWaFTnmQanCozDCC4hLTwMm8jtInK46caFy_Exyb_V0fpcHOd0sTikafdrqJMv5Jq6THn1qYZ07KxTWeWL0a4StpiZwv8ihDAIQrePANmYVWmz5bueQiuh4sOkD5WDZziK2RDEpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، درباره ایران:
من نسبت به این توافق تردید دارم و این را آشکارا می‌گویم؛ اما تنها راه دستیابی به آن، درکِ درستِ ایران از این جناح‌های گوناگون است. به گمان من، تفاوت این جناح‌ها بیش از آنکه ایدئولوژیک باشد، ناشی از ارزیابی‌های متفاوت آن‌ها درباره میزان سرسختی ماست.
کسانی که رئیس‌جمهور ترامپ را بسیار سرسخت می‌دانند، معتقدند که «نباید با این فرد درگیر شد»؛ اما کسانی که تصور می‌کنند «نه، می‌توان آمریکا را بازی داد»، معمولاً خواسته‌های بیشتری دارند. با این حال، به باور من، در نهایت آنچه تعیین‌کننده است، عزم و اراده ماست.
عزم مشترک ما این است که اطمینان حاصل کنیم ایران به سلاح‌های هسته‌ای دست نمی‌یابد تا بتواند با آن، تک‌تک آمریکایی‌ها را تهدید کند.
به اعتقاد من، رئیس‌جمهور ترامپ در این زمینه کاملاً قاطع و صریح عمل می‌کند و من به همین دلیل، عمیقاً برای او احترام قائلم.
آنها باید بدانند که اگر به ما حمله شود، با نیرویی وحشتناک پاسخ خواهیم داد.
آنها به خاطر آنچه که من گفتم، در دورهای اخیر درگیری‌ها به ما حمله نکرده‌اند.
به عملکرد امروز این رژیم نگاه کنید. این رژیم به هر کسی که در دسترسش باشد حمله می‌کند؛ به عربستان سعودی، کویت، بحرین، امارات متحده عربی و دیگران حمله می‌کند.
این رژیم به هر چیزی که در برابرش باشد حمله می‌برد و ده‌ها هزار نفر از شهروندان خود را به قتل رسانده یا دچار نقص عضو کرده است. این کاری است که رژیم ایران امروز، بدون در اختیار داشتن سلاح هسته‌ای، انجام می‌دهد.
حال تصور کنید اگر آن‌ها سلاح هسته‌ای داشتند، با جهان چه می‌کردند. این همان چیزی است که باید اطمینان حاصل کنیم از وقوع آن جلوگیری می‌کنیم؛ و گمان می‌کنم ما در این باره کاملاً هم‌نظر و مصمم هستیم.
مایلم کسانی را که به دنبال ایجاد تفرقه میان ما هستند ناامید کنم، چرا که من و رئیس‌جمهور ترامپ در این مورد کاملاً با یکدیگر هم‌عقیده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69183" target="_blank">📅 11:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69182">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=poSLrjrksaJSGfYYLuOQLIsBwpDx9g4OzjEgpk-PcYQZPgkMzRU5udfMLYtw7Iui6yg0JjYorDwrVP4GetO-RC-ZGrOI9lXUp0Rrhxknz9zmZyA_3ATte0I2MiuhFZ6KEUH77Iv8oD9mj7GF66HcQclRgCvv-AR6i6d090DGXQerPmgUnMU40Bu1e7a9csZsPuwPGhmTIHXkDhbsbD2PM8W7SiAofKiLOHshJuhwulOu_f47dIyNJSDWooLJeOOiZai0zyXXO1rA_qiRaU1fzC5CGwv0iO7hdvSIbY1pVtfaAmpvg3w87hyrrBX8kzrhIVKR6jzRsfgCtZzyuuafLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=poSLrjrksaJSGfYYLuOQLIsBwpDx9g4OzjEgpk-PcYQZPgkMzRU5udfMLYtw7Iui6yg0JjYorDwrVP4GetO-RC-ZGrOI9lXUp0Rrhxknz9zmZyA_3ATte0I2MiuhFZ6KEUH77Iv8oD9mj7GF66HcQclRgCvv-AR6i6d090DGXQerPmgUnMU40Bu1e7a9csZsPuwPGhmTIHXkDhbsbD2PM8W7SiAofKiLOHshJuhwulOu_f47dIyNJSDWooLJeOOiZai0zyXXO1rA_qiRaU1fzC5CGwv0iO7hdvSIbY1pVtfaAmpvg3w87hyrrBX8kzrhIVKR6jzRsfgCtZzyuuafLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانمِ باردار رفته بود سونوگرافی ولی به دکتر سپرده بود که جنسیت بچه رو لو ندن تا اینکه با این صحنه‌ مواجه شدن؛
شومبول آقا پسرشون انقد بزرگ بود که تا دوتا اتاق اون‌ طرف‌تر هم همه فهمیدن بچشون پسره.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69182" target="_blank">📅 10:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69181">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CStdqeVMBpRyEV7oZXoNcYQnhLc9y21mey3R9hyVN8AcHHwSsnNUxAqWkzwCaSHubvegAdaVLT9u_oIkh7vSYAAUrWt8zceHs0G7FG6ocrHqGic2RudCLUlzK3_4wpif9Lv20jID2HL_WV7mJDZha3udQzjOuFkq8RijdfzoYNjlwRq1-rg_9oRBnPXgdK7iveAg0dkOIU3Ep_tV0PE_6PL83_5WLFIYz4rn0PjtxGD9Sg0rfBO_xQd_0uDcoC6z58eLSEjkFLqFhFhC4DL3PGjLc7LZII5Ao28X4RYPN5m-cybJW0b9L6btsQNs5fjzarif9Son0SFNszATO6zI9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
سه کشتی متخلف میخواستن از تنگه عبور کنن که مورد هدف قرار گرفتن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69181" target="_blank">📅 10:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69179">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=Uen4DbKRSQWcKxjGuoBEFyZFb2UDmHhO0tz_l2Logi61Joxx2C97cXszVkPgqsxg3GAlhfqW4McKIjXytwD9lPVb6AL8ZYnzZG3dU2BbBAQkOpN9JIuzF-3-9CGL_8A3Mk1_PYqTQs-Owd60peZ1LhFkFhKUt8lDMn9DsGYHbohjJxB4Pre00kDRG-LhNHI4dHoHn02w20kNUdUG0Nf03RwTX6VLtmtqRmivI3m64dKwBNvzQ0-kz0ijeJuQxFy-B2kepAS8Xld86amwxl_RRNZ94uTFL4Tf0KnDHgB_an_TU3BIyjgb7LIIPXurt0_c0cKRruOeQPFdCtyqu4mR5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=Uen4DbKRSQWcKxjGuoBEFyZFb2UDmHhO0tz_l2Logi61Joxx2C97cXszVkPgqsxg3GAlhfqW4McKIjXytwD9lPVb6AL8ZYnzZG3dU2BbBAQkOpN9JIuzF-3-9CGL_8A3Mk1_PYqTQs-Owd60peZ1LhFkFhKUt8lDMn9DsGYHbohjJxB4Pre00kDRG-LhNHI4dHoHn02w20kNUdUG0Nf03RwTX6VLtmtqRmivI3m64dKwBNvzQ0-kz0ijeJuQxFy-B2kepAS8Xld86amwxl_RRNZ94uTFL4Tf0KnDHgB_an_TU3BIyjgb7LIIPXurt0_c0cKRruOeQPFdCtyqu4mR5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کاخ سفید پست جدیدی از ترامپ با متن «کار این جنگ رو یه‌سره کن» منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69179" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69178">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305091e76a.mp4?token=imXSexcS4egIGdbePVueKAGQc3gXmZx3GGEDaN1Ml4TPH7xGRa3MgGGotzcqzHvnVBYpcd5A3olaEF3UDpGIldhgMVt4l72b7LwwnjRL1IWAPwPuHnLlVKII6U6wmGXN3CfYcNP8NsoEchj0Dxs67rZcPm3mRu5fF3j8XpT100t00D22CZ_2zsYKwhddw2q7fdK4unZnv2b1YKLjlof0pCVHKsfbkLpo-avCH7aOYKkARh31-mYJI5ZcXKTRUT6PEi9zCUM8ncNPVYQcFVDcoVkHYm0P6qkXr8NUL_gheS3B7sc7PhCuZXKBMYdMSDSLqUyhY_lWoeEfk7g_nTvIFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305091e76a.mp4?token=imXSexcS4egIGdbePVueKAGQc3gXmZx3GGEDaN1Ml4TPH7xGRa3MgGGotzcqzHvnVBYpcd5A3olaEF3UDpGIldhgMVt4l72b7LwwnjRL1IWAPwPuHnLlVKII6U6wmGXN3CfYcNP8NsoEchj0Dxs67rZcPm3mRu5fF3j8XpT100t00D22CZ_2zsYKwhddw2q7fdK4unZnv2b1YKLjlof0pCVHKsfbkLpo-avCH7aOYKkARh31-mYJI5ZcXKTRUT6PEi9zCUM8ncNPVYQcFVDcoVkHYm0P6qkXr8NUL_gheS3B7sc7PhCuZXKBMYdMSDSLqUyhY_lWoeEfk7g_nTvIFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از لحظه‌ی حملات عربستان و آمریکا به مواضع حشدالشعبی عراق تو استان واسط، که توسط دوربین مداربسته گرفته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69178" target="_blank">📅 09:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69177">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74196ace24.mp4?token=b9gz8xiOY9KRE3Qw2iKcp8Q7kL47tkz24rVxwIfK77N6wkLvwW9XU2wwAk3ofBUkI2QvuysP4cAcSoNxusJTdHp-HX1rG7Ks3YBCUzvAL7S-lZUjvgljT4C6dduV_CzlyvEh9FlSG0BvhzMPOCj3mT_qZAwZOheL1Mfw2zGMh8onnAzyXREsq-lT12L6K6ZCBjDxmQqL4VnSAlAgmk98pioEjRnIWXR9YjBIos8362r-5N_YSrnTBAozSigGXKh6sG14nYUFoG0t2cuhE0wIcOInUF7jy4Eg5-Q_Yv5urDT5S7Qp1LYD_IoLg2ARyAg6M4PHsZqg1aOsUSHQOeuI7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74196ace24.mp4?token=b9gz8xiOY9KRE3Qw2iKcp8Q7kL47tkz24rVxwIfK77N6wkLvwW9XU2wwAk3ofBUkI2QvuysP4cAcSoNxusJTdHp-HX1rG7Ks3YBCUzvAL7S-lZUjvgljT4C6dduV_CzlyvEh9FlSG0BvhzMPOCj3mT_qZAwZOheL1Mfw2zGMh8onnAzyXREsq-lT12L6K6ZCBjDxmQqL4VnSAlAgmk98pioEjRnIWXR9YjBIos8362r-5N_YSrnTBAozSigGXKh6sG14nYUFoG0t2cuhE0wIcOInUF7jy4Eg5-Q_Yv5urDT5S7Qp1LYD_IoLg2ARyAg6M4PHsZqg1aOsUSHQOeuI7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
خداییان، رئيس سازمان بازرسی : بعضی تراستی‌ها خیانت کردن و با پول رفتن!
یه تراستی (شخص یا شرکتی که حکومت بهش واسه نگهداری یا انتقال پول، اعتماد میکنه) فقط 200 میلیون دلار پول مملکت رو برداشته و از کشور خارج شده!
معادل38.1همت!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69177" target="_blank">📅 09:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69176">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69176" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69175">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=gdI4ygttVTCqrxLG1DRYMzGD06qBSKCSw9kNj_OTzu3ded2k5Hn3xC-9oLNqaoscENB_GyrmU15fJ4h76LocnRah6tJj3kmUykQ6K-0_tL_36xUbmzqD-Zp-V4v9_3hBYAwBa48gtvYww7Yrt1Exi2PD0823NvxXnjw13BnDqEeZieAlDIZAEDSkd0KhnuGIUeEx2ojachYnPy5HQTcqJkL8YABsnz0n3o6iIU9i-dfPnTTtMrvE_IkH4vvAW5NzSF_kTQUl5BKXaGltvN9eoVCJGRGk4XlJwI5R50g3-1WQ4DflOQCLDpFN1MNJlHSPtSsKY14KhEAO4Wr2xZjjgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=gdI4ygttVTCqrxLG1DRYMzGD06qBSKCSw9kNj_OTzu3ded2k5Hn3xC-9oLNqaoscENB_GyrmU15fJ4h76LocnRah6tJj3kmUykQ6K-0_tL_36xUbmzqD-Zp-V4v9_3hBYAwBa48gtvYww7Yrt1Exi2PD0823NvxXnjw13BnDqEeZieAlDIZAEDSkd0KhnuGIUeEx2ojachYnPy5HQTcqJkL8YABsnz0n3o6iIU9i-dfPnTTtMrvE_IkH4vvAW5NzSF_kTQUl5BKXaGltvN9eoVCJGRGk4XlJwI5R50g3-1WQ4DflOQCLDpFN1MNJlHSPtSsKY14KhEAO4Wr2xZjjgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم:
تحلیل تخصصی بازی‌ها
بررسی فرم تیم‌ها
آمار مهم قبل بازی
پیش‌بینی مسابقات مهم
نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای
اگه دنبال تحلیل واقعی و بدون حاشیه‌ای، همین الان عضو شو
👇
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69175" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69172">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJIrtiD9IjlxjOBhyNyMJu4y-qcjuPNChVb9Mhmd8T_Gdn3agX5iW-H95-dOZPV6v58j2H6CVrfaFgAxSsarA8FGR39gW1-2Wajp1wX_5VaoQpCx_PXWYKEXDmFosPwarFUgFKL0ope407TKz1IqFS97z2GknEPe-Z-YSBzQyqe-uV270nl6rePm0P10s-RVWAxycoeISbBUsoJUN-ZmxllhrkETWKQlmWXj3jv-RjnS-g-syXPFhmUiSSKa7wDmmFdYAqNs_pc7b6m8TSuQOZRmNSkXAlfb6tzuPmb20TU9sZoZNPT0sTXlqBaAOF9lXaKtD3AwQiCEKWhjVpp6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرقی، نیروهای سپاه پاسداران انقلاب اسلامی در تلاشی برای انجام یک حمله غافلگیرانه علیه نیروهای آمریکایی مستقر در خاورمیانه، چندین موشک بالستیک از خاک ایران شلیک کردند. تمامی موشک‌های ایران با موفقیت رهگیری شدند. نیروهای آمریکایی همچنان هوشیار و در وضعیت آمادگی بالایی قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69172" target="_blank">📅 02:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69171">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-dzWYRYNBqAW5vFmSoZfVBgJo_8r04uAmrTUaNNV7k2uL2cjkjbQK3q3B8z1mHY6mMoslis_kKTEDjeAVx3GaUjjx_EZWLqnrXmkOfy9a0jlK0Rl53jlVF2WbYQHk75Y_R1Q9xKpZl9Z1dxqBVPtdnC_0Enn9lB4fobBOe4pH_QwGBjfMaswVsnbLIrxYY-2YwU9bgaFBcwtewu-G15TE49i4J7pHpmXELy-nEgs8qoFzdZnUQkytKCRUijH9Byv7Z4lANCReMr7YuL820Bz2iMQzhhtCFZP04Bd3_MbshgGGSpAQkZp2ECB8PILld8EGksfjpT8S1n0w4-7DE5tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران برای جنگ تمام‌عیار کاملاً آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69171" target="_blank">📅 01:57 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
