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
<img src="https://cdn4.telesco.pe/file/uCWNz2pnJz5EH35UbKCMwoC6VOn5XC1iwJ9mXQskF8EASt3bPY40KFDITAoX_-5a82uOmBV7VLBV8tXdqjWlzQrbhWzBSu3QqUwsGgdFAQ9JyHS91uj91yWqF7xiAGDwMWKNe9gQ00kZg5IMeU4UEYfo58MoibMOL98bk13mRkBxLTVgwdGBSJTE-WX963fEbbpVZabj2TrJ6fVPC2p0I4sGsFtMXXQd3r-5vRwU5qFyvg8QojdzDfotfPvCc7zPG1R0_0R55y0cT3FDYY_e79MEmusYy-G6ZJQcg6VDHkpb-ECXab1TsTayYebsPxK3OP68REJeI-KFb_VMRfNsIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.7K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 14:49:11</div>
<hr>

<div class="tg-post" id="msg-20574">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اسکات بسنت:  پس از دریا و زمین بزودی هوا را هم به رویشان خواهیم بست.</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/SBoxxx/20574" target="_blank">📅 14:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20573">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">راه آهن کشور اعلام کرد ترکمنستان و قزاقستان با تبعیت از تحریمهای جدید آمریکا مانع انتقال ریلی کالا از چین و روسیه به ایران شده اند.</div>
<div class="tg-footer">👁️ 741 · <a href="https://t.me/SBoxxx/20573" target="_blank">📅 14:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20572">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجنگاوران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OT6FnKPwojHihDResFeg2LGZod1D5Mwzxvx-YX8oX_Hu2gu6ub1d5ugyy9nxTzwyJxNgckcQzwJ4bO1b9ug67qiM55BZEtm3hzoidsBrw0ZKtUsb9qHFYdP1AO_-LNWy1W_lk1Rg9zeYtNZ_qjEkf_dzPXfPDCFjVPVgI91U2ap09B6rpJumbUew4BP_5TeZq3Nxy8-oyf5F-NK10Aro__KyPB8oJXAWQqSppt0w__SRBwWR-FByLNBNZLvQ7rVKMu31FeaT89JTmANano_4KiwviCqcQW8ioLjDJiudaFsyoNqed_w72unYtYB8223v2ZNomBq_NxGT-_2gj4zXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پهپاد تهاجمی جدید ژاپن؛ به اندازه یک چراغ‌قوه!
ژاپن برای نخستین‌بار تصاویری از یک پهپاد رزمی بسیار کوچک را منتشر کرده که ابعادی تقریباً در حد یک چراغ‌قوه دارد.
تصاویر منتشرشده توسط NHK WORLD-JAPAN، پهپاد را درون یک محفظه لوله‌ای و با آرایش چندروتوره نشان می‌دهد.
با وجود ابعاد بسیار کوچک، این پهپاد برای انجام مأموریت‌های شناسایی و حمله در برد نزدیک طراحی شده است و می‌تواند به دوربین‌های شناسایی یا مهمات مجهز شود.
از جمله اهداف احتمالی آن، خودروها و تجهیزات زمینی عنوان شده است.
ابعاد بسیار کوچک
قابلیت حمل در محفظه لوله‌ای
آرایش چندروتوره
امکان استفاده برای شناسایی و حمله
مناسب برای عملیات نزدیک نیروهای زمینی
این پروژه نشان می‌دهد ژاپن نیز مانند بسیاری از ارتش‌های جهان به سمت پهپادهای بسیار کوچک، ارزان و قابل‌حمل برای مأموریت‌های تاکتیکی حرکت می‌کند.
#ژاپن
#پهپاد
#پهپاد_رزمی
#پهپاد_تهاجمی
#نیروی_هوایی
#فناوری_نظامی
#دفاعی
#Drone
#Japan</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/SBoxxx/20572" target="_blank">📅 14:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20571">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">زاکانی:   به دنبال برق اتمی برای شهرها هستیم</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/20571" target="_blank">📅 13:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20570">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">زاکانی
:
به دنبال برق اتمی برای شهرها هستیم</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SBoxxx/20570" target="_blank">📅 13:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20569">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اسکات بسنت:  چنگال مرگ اقتصادی را ضد نظام ایران فعال کرده ایم:  ارز آنها در حال سقوط است و صادرات  نفت شان به 0 رسیده !</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/20569" target="_blank">📅 12:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20568">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ایران دارای یکی از بزرگترین ناوگان های نفتکش دنیا بود اما با این وضعیتی که پیش می رود باید از شوتی های زحمتکش مرزهای شرقی و جنوب شرقی کشور برای انتقال نفت بهره ببریم!</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/20568" target="_blank">📅 10:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20567">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftQmjZcxReiEc_BlUUjhEJ4clyvTZJs4Cd5pG6apgnDsxqUz4Zb-8cZnL-FJs8Sg_4O1pwuRUhlHYroeMsTpLvns5izOHaepayFLUUKlmcTOn9l00XS0OmOfRmA0mQzxIqIZ29SagYdhVTPUK9F_FszpJzBdH0hAWaVSsRDvrsDAIAHYGHDyjkD_MNsvxZwi3CekE8wDQ_AU6JUriGapqwknZSHJCD4zxDaY1r0UObrLM8wP1pBo4tkU7e1SjqhlTJGFrM13cWZCZ8-SYKZlTR69gtei072WzgZEo4JmsaCHcZ2Q9M-RiuRWfPJsIDRqJGVFaexaWvcynCB6usKQKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/20567" target="_blank">📅 09:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20566">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF5fOQBT_X2pCgLE_iWbr9iJNUDeZcdY0TtgQFvUJWDHdD7v36H-fS5NK4mt3-avNsPadnyR5O04f0jX8DTrQADBmiBpSQsPi6-mAETpUJ4mTdkI_53T4Fo7DyjUgGeRxBt8BTieNYGIhSntoIVhGM0KEpSA9MWiVC3EiFbAkHC0UB3fzTtKtgVkrc0Jh2tNwmOfooAyI55Si7m8bpGspm-nkPZ8TWwlgvg2S_hEWRVVIbIm3HOI0n2Rl1MA-C1exvKHqB5gBisufixbDZjpryG-USqR6loBoHybc4OngYtv_nIb4wUOuQzFgSeIPT0VsoDgIJ_zFO5W_Ev2U8Rdhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دوباره هما خان سعادت در آسمان کشور مشاهده شده....</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20566" target="_blank">📅 00:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20565">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">— شلیک موشک‌های کروز ضدکشتی از سیریک به سمت تنگه هرمز.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20565" target="_blank">📅 23:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20564">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOh-WxcCy1uHuBULoHWwE1Zzb6ymct1gljYOlHnBZtIVhB3-G4eC6JdV_fQcKBgka590RpPM2Do6SdmZiMr33SYjInsk-elaBm_k5VQMG85Q7tc7oxLsHPY0A4oI8sKxTuvYgDHy7XTI22A1jyxtXLJh980U0MZK8tZlK9mxwMmPE2E6W4pcUGSj4LyUbBOmXkNF5YP2bhiL67LLH08h3sWeYwKG2LGt38oHNLWpbCO2Q8ziX_k5Hg6kQ1sJhQUBGJ1jGleBRcK9Aj92s6bmzYciZnIg9DlUnBveyVgAub46OZVkoNKjKIv_41pe06qMeZRJCMaGKEOUBriS4Rp2vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما تکذیب کرد!</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20564" target="_blank">📅 23:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20563">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">قرارگاه خاتم الانبیا:  حملات پیش دستانه علیه پایگاه آمریکا در اردن که در حال آماده سازی برای حملاتی علیه کشور بودند را انجام دادیم.   |</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20563" target="_blank">📅 22:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20562">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ
:
ممکن است خیلی زود کوه کلنگ را هدف قرار بدهیم ، چون حس می‌کنیم آنجا اتفاقی در حال رخ دادن است</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20562" target="_blank">📅 22:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20561">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzUDuZjwTDDObCSBgKuUf9TRP463p7DRdbXfjAG3CSjs9hM-WENXomZBaSfoJa0uMJDOg0EcPKWY2PrOmUqFXO2XMxhCY-33wQOLu3J50x1yCt7UFx5L4NrkEVdqV8rv5CmJGWhchWohPd1ikNt8IpCbP9I5xo7hlDM62SNVWFkm6JCyuncI-3OFCW7ld28QduI_vq56LlXieYkmSIDYBS2jcaKdPoSxS6_altFAKQHRyEOfX72dAtTrdqVPIVeRnxC8hNB2Wvmke0XPZGLPiPnnV0lupk_8IYtJpvXuDdI42XJP0z8Zyn6PgyIn8AxE18OKR7HtQJLmXCEqdIiLsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش حسین پاک از تپه های علی الطاهر!  به گفته او، تپه های راهبردی یادشده از دید نظامی سقوط کرده اند</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/20561" target="_blank">📅 21:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20560">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">برخی سایتها و منابع خبری از حمله موشکی ایران به پایگاه‌های آمریکا در اردن خبر می‌دهند</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20560" target="_blank">📅 21:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20559">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اسکات بسنت:
چنگال مرگ اقتصادی را ضد نظام ایران فعال کرده ایم:
ارز آنها در حال سقوط است و صادرات  نفت شان به 0 رسیده !</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20559" target="_blank">📅 20:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20558">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">از نبطیه چه خبر
نتانیاهو راست گفت که مسئولیت نخست دولتش‌، تامین امنیت کشور و ملتش است و در این باره منتظر کسی نخواهد ماند(به خصوص امریکا). شاهد، رخدادی است که از ۱۰ شهریور تا امروز همه خاورمیانه عربی بدان چشم دوخته اند. خبری وایرال شده.
ارتش اسرائیل کنترل عملیاتی ارتفاعات علی‌الطاهر نزدیک نبطیه را به دست گرفته و زیرساخت‌های زیرزمینی گسترده حزب‌الله را پاکسازی و در حال خنثی‌سازی است. این مجموعه که طی دو دهه با هزینه مالی کلان ساخته شده بود، شامل اتاق‌های فرماندهی، انبار سلاح، ژنراتور و امکانات ماندگاری چندین ماهه می‌شد و به عنوان مرکز عصبی واحد بدر عمل می‌کرد. در واقع هتل-قرارگاهی چند ستاره.
موقعیت مرتفع آن امکان پرتاب موشک‌های کوتاه‌برد و پهپاد به شمال اسرائیل را فراهم می‌آورد؛ و مساحت و تیپ ساختش ماندگاری طولانی را برای نظامیان فراهم می ساخت. ولی از مدت ها پیش، با شناسایی دقیق ماهواره ای، هوایی و تجسس زمینی‌، بستر برای تصرفش مهیا شد.
این عملیات ترکیبی از محاصره طولانی، شناسایی دقیق با پهپادهای حرارتی و ورود مهندسی بود. برخی نیروهای حزب‌الله کشته یا مجبور به عقب‌نشینی شدند و تجهیزات مهمی به دست اسرائیل افتاد. از دست رفتن این گره راهبردی، توان فرماندهی محلی، ذخیره‌سازی امن و پرتاب محافظت‌شده در محور شرقی جنوب لبنان را به طور محسوسی کاهش داده است.
البته این  ضربه به معنای فلج کامل یا جمود نظامی حزب‌الله نیست، ولی موجبات شگفتی کارشناسان خبره نطامی را فراهم اورده است.
حزب‌الله سازمانی غیرمتمرکز با ذخایر پراکنده موشکی و پهپادی در عمق خاک لبنان، تجربه جنگ نامتقارن و پشتوانه ایران است. نابودی یک مجتمع، هرچند بزرگ و مستحکم، توانایی بازدارندگی کلی، عملیات چریکی یا بازسازی تدریجی را از بین نمی‌برد. نمونه‌های جنگ ۲۰۰۶ و درگیری‌های اخیر نشان می‌دهد این گروه پس از ضربات سنگین زیرساختی همچنان توان پاسخ‌گویی نسبی خود را حفظ کرده است.
اثر واقعی این عملیات در تضعیف الگوی «جنگ پایدار از زیرزمین» در جنوب لبنان، افزایش هزینه بازسازی و تقویت فشار سیاسی برای خلع سلاح یا عقب‌نشینی بیشتر نهفته است. اسرائیل خود اذعان کرده شبکه‌های مشابه دیگری هنوز باقی مانده‌اند. بنابراین، آنچه رخ داده پیشرفتی واقعی در خنثی‌سازی نقاط کلیدی است، هرچند حزب‌الله همچنان بازیگر نظامی فعالی باقی می‌ماند و سرنوشت نهایی به واکنش‌های آتی، وضعیت آتش‌بس و توانایی بازسازی بستگی دارد. ولی حزب الله دیر یا زود ناگزیر به مذاکره و توافق است. دقیقا شبیه حماس.
#یدالله_کریمی_پور
#Karimipour_K</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20558" target="_blank">📅 20:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20557">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گزارشات تایید نشده    از شلیک موشک از اصفهان</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20557" target="_blank">📅 20:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20556">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEKBTtMAqS2__5eGJ31XODem3pU2dLD6L4mFpoBtyQzeXgFjIlSnb_gjKM_9A2HgEfREL098Bh3Z0AKNi7RUDiXNDsiTqUQ7a33KYNRMYmgw3Iiny-rat88x5EXfRbAl9qYf8FEYz5hr_XVD3yqFfhjjs0UpN9ufhqy8XAUmmsVYODRQaIAvies_IglhzXRickUqhSXLiJpnWgv3xEMuaQB6nNITndpHXmUfc32vYSd8eizmbHIiQ9HeYZf8wpYQYOoyL-PSHKPnRRoMuGK5ricc1-9hXDhdLpLFIFKTZi-2lRJVAgbGA8WMiqNjflMUclHrKkm0541AuaJA0bOYtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی اکنون به 48 افت کرده و می توان در این محدوده ها دست به خرید طلا زد</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20556" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20555">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNeetIDHu5owhZDV4Iq4zv1ybTKVS47gdiqz2RulzuRs_ONxSwTua-rYxbhtbbimQUhAx96EstY8H8D0XsreEB7WBOszOOgSzbHmqHqkhc8NnRTUS4QGiraoLLn4mcrQX2uwm15OqVukuFnXrkfdNsEF1Sc9ZfBPzRiYboPBje5Zm-z9_rxfpXK9hLs779pGmNNibmCP63SwejWH6JbpLGaZ5iZXtyg8vX_-OClipyUXMs17wjD2pqfJfdainZC8Fxw8unv4X1FPwR9MftnfdCIAs_l1WZIcC7PySdQ2iJbr0X7KCTsV0Pprpo1OyHGZT62mal7CpX9gDWhKHkZeWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد و پیش بینی می شود دستکم تا 4385 شاهد افت قیمت باشیم.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20555" target="_blank">📅 20:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20554">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گزارشات تایید نشده
از شلیک موشک از اصفهان</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20554" target="_blank">📅 19:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20553">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">از اپوزیسیون هم شانس نیاوردیم !
این قاضی زاده تا دیروز فعال سیاسی بود از امروز شده فعال بازار شت کوین !</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20553" target="_blank">📅 19:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20552">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ایالات متحده تحریم‌های جدید مرتبط با ایران را علیه بانک ترکیه‌ای گلدن گلوبال (Golden Global Bank) اعمال کرد</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20552" target="_blank">📅 18:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20551">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مثل این است که یک مرد مدتها با یک زن غرغروی منفی باف گوشت تلخ زندگی کند و با کلی بدبختی و پس از سالها صبر از او جدا بشود و بعد در ازدواج دومش هم با دختری با دقیقا همین مشخصات ازدواج کند و همان فحشهایی را که به اولی میداد به دومی هم بدهد!</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20551" target="_blank">📅 18:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20550">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مثل این است که یک مرد مدتها با یک زن غرغروی منفی باف گوشت تلخ زندگی کند و با کلی بدبختی و پس از سالها صبر از او جدا بشود و بعد در ازدواج دومش هم با دختری با دقیقا همین مشخصات ازدواج کند و همان فحشهایی را که به اولی میداد به دومی هم بدهد!</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20550" target="_blank">📅 18:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20549">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">این ترامپ رسما دیوانه است!
رفته خودش این کوین وارش را به جای جرومی پاول آورده بعد امروز وارش را تهدید کرده که یا نرخ بهره را پایین می آوری یا تجارت با کشورهای دارای مازاد تراز تجاری با آمریکا را متوقف می کنم!
همین هفته پیش وارش گفته بود تورم بالاست و تمرکز ما روی مبارزه با تورم است و شاید نرخ بهره را بالا ببریم!
جالب اینکه همان پاول فلک زده را هم خود ترامپ در دوره اولش آورده بود و بعد هر روز به او فحش میداد که چرا نرخ بهره را پایین‌ نمی آوری!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20549" target="_blank">📅 18:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20548">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گزارش مشابه</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20548" target="_blank">📅 18:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20547">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارش حسین پاک از تپه های علی الطاهر!  به گفته او، تپه های راهبردی یادشده از دید نظامی سقوط کرده اند</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20547" target="_blank">📅 18:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20546">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حالا اینقدر بچه ها نگران این تپه نباشند؛
ماشالله اینقدر تپه هست برای فتح کردن !
مثلا یک تپه ای هست به نام امین الطاهر که کنار علی الطاهر است و هر کس به آن نگاه می‌کند طلسم می‌شود و فیلم «تپه ها چشم دارند» بر اساس داستان این تپه ساخته شده.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20546" target="_blank">📅 17:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20545">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d58b19c9.mp4?token=a_hKD-KjbZtUX6ZRm8tz3PNNzQqB0Nsc1VSt63IZ0A9w2MeLTlvQpN6cShBG69C9vK1JYRdbiuk9H3pPBvp2SDquYlGrEXWlXTJNmJ10VMifqqOrDEv6hk7fxvaQm35umSdMVbcx4b2GmqXRVfD7D1q3iCTdOLhpDazdWAKOVz1mJcjF4c_KolIGYZUpkAHcd1ynxIxnlaD0GLqLEjg0FuojBOH3KxuuMYugwkkmzjit02wuetewaZvkFBXgRYmi-Nox94S1lKd9Hui4jPMmQul-Arb2MUDzHLsdxc1iwAenzixkOE7jW4tfPqWcHeLLU630ru16-eTIMs20rzWgC5U1wjcCdEDyjWmHK66sbo7K1j-ZPwoLIH_jAMyt9Rfnc0Tj0fLsvjbLgASa_jk6civJD8MOVrCTQxknU25fcxHZA04kAMD7U9GQ3FoooQrxZeM1JfSrvV-4UozCy-KQpV941OH0REIUxXtOkAMTDxonYG_MNzIJ7tgby6EKViJaKn8CKII1wpbdXaQtS-bbOGk6oFW1ATFf74w7wQryh1FTxs_P-UMXCoxD3WWobnINkJ9gMgOXm_JCc4tobqK3jl3V0KBzz7hXkeK-YrWxqWtzOpKxPKUVDZxbDSxvZQ2VKFp-E3JWz9WzEBE_OxaI3Ov0N6Eis3NEQINzJM3BDvo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d58b19c9.mp4?token=a_hKD-KjbZtUX6ZRm8tz3PNNzQqB0Nsc1VSt63IZ0A9w2MeLTlvQpN6cShBG69C9vK1JYRdbiuk9H3pPBvp2SDquYlGrEXWlXTJNmJ10VMifqqOrDEv6hk7fxvaQm35umSdMVbcx4b2GmqXRVfD7D1q3iCTdOLhpDazdWAKOVz1mJcjF4c_KolIGYZUpkAHcd1ynxIxnlaD0GLqLEjg0FuojBOH3KxuuMYugwkkmzjit02wuetewaZvkFBXgRYmi-Nox94S1lKd9Hui4jPMmQul-Arb2MUDzHLsdxc1iwAenzixkOE7jW4tfPqWcHeLLU630ru16-eTIMs20rzWgC5U1wjcCdEDyjWmHK66sbo7K1j-ZPwoLIH_jAMyt9Rfnc0Tj0fLsvjbLgASa_jk6civJD8MOVrCTQxknU25fcxHZA04kAMD7U9GQ3FoooQrxZeM1JfSrvV-4UozCy-KQpV941OH0REIUxXtOkAMTDxonYG_MNzIJ7tgby6EKViJaKn8CKII1wpbdXaQtS-bbOGk6oFW1ATFf74w7wQryh1FTxs_P-UMXCoxD3WWobnINkJ9gMgOXm_JCc4tobqK3jl3V0KBzz7hXkeK-YrWxqWtzOpKxPKUVDZxbDSxvZQ2VKFp-E3JWz9WzEBE_OxaI3Ov0N6Eis3NEQINzJM3BDvo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری صداوسیما:   ادعای نتانیاهو مبنی بر تصرف تپه‌های علی‌الطاهر هنوز به تایید شورای نگهبان نرسیده است</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20545" target="_blank">📅 17:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20544">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی اکنون به 48 افت کرده و می توان در این محدوده ها دست به خرید طلا زد</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20544" target="_blank">📅 17:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20543">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDnRIucqo7EN2O6qKMRvFlmhkHry2qVy4RHr5UIgYkRtYRE82kgGBIufvcrPBE4TujTibzEBmosy9Lfabj0EurgEWFMuVGvs90FdvFsuhsHqnEqriVUjAfxWUtxGTKIujLgszVqcRXzhZQBky3IVV_wFZjYpqAhNxQIERWYIgQHKSYWpagTvrFxADxQOqs2ensuri2eFoMl2nbYdvOi6vj5hRg1Kg2DjmvJI5kjte9bH8uQvDkZGXG9A_FcGeQ05ZG7fB52HsEiBbhDLCRVkiaL8VxEo4uQ4ixWeVIpoTZLkj2vMxVjc_B4_4zNjq_UEFEynpTPF5HOBGypBu5G3Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی اکنون به 48 افت کرده و می توان در این محدوده ها دست به خرید طلا زد</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20543" target="_blank">📅 16:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20542">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">در‌ روزهای اخیر باز اسم عاصم منیر مطرح شده بود!  سبحان الله !</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20542" target="_blank">📅 15:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20541">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/20541" target="_blank">📅 09:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20540">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ظاهرا آرژانتین با حمایت ضمنی ترامپ به دنبال حمله دوباره به جزایر مالویناس (فالکلند) است.  جالب است که به محض انتشار این شایعه، استارمر بحث تروریستی اعلام کردن سپاه پاسداران را به جریان انداخت تا شاید از امتداد شعله خشم ترامپ جلوگیری کند.  اخیرا بریتانیا تصمیم…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20540" target="_blank">📅 09:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20539">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIZC0guW4siG8rP3IQ0prcIlI9MwN1svKHbhuD6NPiMh3sA76RvR_6lXir4hbYxOWcqdOfyslH6KpJRqCCNU1i7JctSSzmd4iHGYhKrXDoJ5pipdmFadRX-wUOjaBa0Txldll21p_JvR7DcrdYzEVAa8mZ2P6U_PHTSoqGfazRxjcHt768c_7ID06Dj9jc_Wakwq1fg4Iq0bL46tPQCVrAb4mh9PAEa8HkzD_lOm1nxGafEblRAvtJyDjyXnBSrZF9K2Mp2SYeTqGcyWQbIhlKquhDcACQnPBoYRECa0d18c8207O6CvbeOrcy1RKps0MnVfXfc3Az0UN6TxgGmVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش خنثی سازی مین ها از راه دور
این روش عمدتا توسط نیروی دریایی بریتانیا به کار می رود که تخصص ویژه ای در مین روبی دارد</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20539" target="_blank">📅 01:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20538">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bK1h_KOWho0bPjPqXzoUyOPaX2PXQ5x8qYElFB1VmcLpNH1CibYeIEWF_MYYTpmWYMKKrMu5zjckv4X5NoZyn5vbWyRuGBLS38SDz7FMgHxCZs9xLQPET89RJh4_dFqMDSe8fmg5suKNZRQtldIFdmHFA5K2i3BJhEvdPCNxm005MHhW9g22svoley3BYFx2bmXxw4N0-0Jq-Km2gwtumtdCEK1k4wOytBnx_GN3SmoexVrOJdUFbcOG0Nv_eoh9_2pf32LXXoHw24Sr1VTYqPJimtNIH8SRcNpH3lSv5yLpXxvh9s2eTex2tOwb266ilVH_7ObgDHRhurt_BtR29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این گزارش های آژانس هسته ای و اظهارات تند ترامپ + نتانیاهو شرایط را به صورت قطعی به سمت جنگ می برد.  مراقب موج‌۳ باشید.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20538" target="_blank">📅 01:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20537">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20537" target="_blank">📅 01:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20536">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5fc46a9c.mp4?token=h2tgnffSdxZUnGz20Dp-IuVG1VizcOqTctEAGEMYernixHoRPDjUfr1WfWtbjl2crAXV0-i9nmdTcQhCDblnKXRPye4RKYjyAZrvLESbM3y9L8niUHn1YvrvSJq1ppzMtj589YWBfqrWYNOirTO9LMDEPvAKFxP_pGxWmK4co6Qi0dGSpnTvF30N-9SntGrj2h7UMon6hr8HlnfyWgJdWrxpQ62efmwvcs0aHSbZ18l3bWO9vW0ZdipX1Nl6XzXGzftOyCd2__uGO7YnyiPNj4WZzYR1mF96v6rK1PPQj2b5oGm0YUpohglur9HY2rhcc3gl9q4bc9QdfkL-VShc8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5fc46a9c.mp4?token=h2tgnffSdxZUnGz20Dp-IuVG1VizcOqTctEAGEMYernixHoRPDjUfr1WfWtbjl2crAXV0-i9nmdTcQhCDblnKXRPye4RKYjyAZrvLESbM3y9L8niUHn1YvrvSJq1ppzMtj589YWBfqrWYNOirTO9LMDEPvAKFxP_pGxWmK4co6Qi0dGSpnTvF30N-9SntGrj2h7UMon6hr8HlnfyWgJdWrxpQ62efmwvcs0aHSbZ18l3bWO9vW0ZdipX1Nl6XzXGzftOyCd2__uGO7YnyiPNj4WZzYR1mF96v6rK1PPQj2b5oGm0YUpohglur9HY2rhcc3gl9q4bc9QdfkL-VShc8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20536" target="_blank">📅 01:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20535">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار سوریه به فارسی 𓂆</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f5a76c78.mp4?token=ogOANPrgQOR7VWzVYPCDr_UnaaYcgXwkkwHcM2kHlYZLIHCCf5xNsQoG6MpWjJAbTHbmL64OrC0X43Dx-oCeq0TZJ4ZwiV4KDKPYry5pKvvktH7wd6Q4zbaNABKFaV-b55rULUhIajLPu0Ygt9gGiD5b7vbLDFMWQR9AMRC6wJmNAvPKfCNHCgYzwPLquVLqQyfCs78t5Iy52WTPapCQwUvUze9L5YkCG867zhX9dKaOmnTchfycAY9_3dLq4Y37IqVrb74GI4P9otArZu-477G3nTIzJTq60IcqAGB4fchtXJzeoteMQurD6eptVzGZyhdZ4swonnsEshjTg8Hpyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f5a76c78.mp4?token=ogOANPrgQOR7VWzVYPCDr_UnaaYcgXwkkwHcM2kHlYZLIHCCf5xNsQoG6MpWjJAbTHbmL64OrC0X43Dx-oCeq0TZJ4ZwiV4KDKPYry5pKvvktH7wd6Q4zbaNABKFaV-b55rULUhIajLPu0Ygt9gGiD5b7vbLDFMWQR9AMRC6wJmNAvPKfCNHCgYzwPLquVLqQyfCs78t5Iy52WTPapCQwUvUze9L5YkCG867zhX9dKaOmnTchfycAY9_3dLq4Y37IqVrb74GI4P9otArZu-477G3nTIzJTq60IcqAGB4fchtXJzeoteMQurD6eptVzGZyhdZ4swonnsEshjTg8Hpyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حالا درسته اسرائیل علی طاهر رو اشغال کرده ولی اینکه ترامپ پای یه کاغذ پاره رو امضا کرده به شما حس خوبی نمیده؟
@SyrianToPersian</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20535" target="_blank">📅 01:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20534">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فشار اقتصادی آمریکا بر ایران در حال تشدید است
رویترز
کارزار آمریکا برای محدود کردن صادرات نفت ایران و بستن مسیرهای دور زدن تحریم‌ها، فشار قابل‌توجهی بر اقتصاد تهران وارد کرده است. کاهش دسترسی ایران به ارز خارجی، محدود شدن کانال‌های مالی و افزایش هزینه شبکه‌های غیررسمی انتقال پول و کالا، توان تهران برای مقابله با تحریم‌ها را کاهش داده است.
مهم‌ترین ضربه، افت شدید صادرات نفت ایران است. بر اساس داده‌های Kpler، بارگیری نفت خام ایران از حدود ۱.۷ میلیون بشکه در روز در سال گذشته به حدود ۲۶۰ هزار بشکه در روز کاهش یافته است. این کاهش، درآمد ارزی ایران را به‌شدت محدود کرده و همزمان با سقوط ریال، تورم نزدیک به ۷۰ درصد و افزایش هزینه واردات همراه شده است.
ایران همچنین با محدودیت ذخایر بنزین مواجه است و یکی از مقامات ایرانی ذخایر فعلی را حدود دو ماه برآورد کرده است. اختلال در کانال تجاری امارات نیز فشار بر واردات و تأمین کالاهای ضروری را افزایش داده است.
از منظر سیاسی، واشنگتن امیدوار است فشار اقتصادی تهران را به مذاکره وادار کند، در حالی که ایران تلاش دارد هزینه‌های اقتصادی و تورمی جنگ را به مسئله‌ای برای سیاست داخلی آمریکا تبدیل کند.
برای بازارها، پیام اصلی این است: اگر محاصره نفتی ادامه پیدا کند، ریسک کاهش بیشتر صادرات ایران و فشار صعودی بر قیمت نفت افزایش می‌یابد. در مقابل، تشدید فشار اقتصادی می‌تواند احتمال واکنش نظامی ایران در خلیج فارس و تنگه هرمز را نیز بالا ببرد؛ بنابراین بازار نفت با یک ریسک دوطرفه مواجه است: کاهش عرضه ایران از یک سو و احتمال اختلال گسترده‌تر در مسیر هرمز از سوی دیگر.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20534" target="_blank">📅 00:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20533">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شلیک موشک از ایران به سمت تنگه هرمز</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20533" target="_blank">📅 00:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20530">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZB_d8nS9hLLLP7Udyjl1Vs9SbvhaCB7f8GrWnu6Q8kl20tHN4q_j9HUvh9fg9tR88iyEx0OfKRL6UB6chKYrL9VXyvYHyXnXzovlq6LwE5_AOc59NMS4evxkQ-fAaniBfz51SpkNoSicpiIdleTUikx9FHovwx2LMhvI5lJO71r4eq0D7p1eRW5pgAvQHCgsG9Bjx8EeQKVgLnpVi9rldnh46lAHvKdIFgpSrLeEZ5Am53kM297ZUnhN9I791G6EK3PeOQnRe1y_asElifzZL-h0bMee3SBtHbWOwh3dffzX4It0eT7zvd57DXR8ky7EW76rmayEilD3PCNKggsKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20530" target="_blank">📅 00:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20529">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20529" target="_blank">📅 22:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20528">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuxekAY_v2myA5j7-DUqM7KVWN6glLbEtKVp1xRisKctzVAxB7HZDIaU50qWU_9-L2aJLfe2U3ZXMKO7XQvd8AJrXDAU1vpFUonruQ0IB6-nU3rqko--jEjXONqJISzgdmkSbTFQMSZBgHKseFw5j_uy4edIack5784j597VKfPaRM5D9laVLN0SlgQ9Ne_CdUeXhd9vVoVxz1DJSYldEJkOiikmmj3Tjdh8PI6agwLrK-ukLIDk1NnduALddeF2R51oZl2TrtAHKmJaD6j0CQhUq4yOhAVoKPVwIykkE4P2jtqahbNArF_kZlp390mEGw_JjV4c5AxiuKoUWBPiwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۸ سال بعد از حمله هوایی ، اسرائیل اعتراف می‌کند که مشاور اتمی ارشد اسد را در یک حمله شبیه به سبک مافیا به قتل رسانده است
در ۱ اوت ۲۰۰۸، غواصان اسرائیلی به ساحل سوریه در نزدیکی طرطوس نفوذ کردند، به ویلای تعطیلات سرهنگ‌کل محمد سلیمان، مشاور ویژه رئیس‌جمهور، حمله کردند، او و مهمانانش را در حال شام خوردن یافتند و سه گلوله به پشت سر و گردن او شلیک کردند. این موضوع را اهود اولمرت فاش کرده است.
«در روزی که سلیمان حذف شد، جنگجویان ما از آب بیرون آمدند – تیراندازان چابک ماهر،» نخست‌وزیر سابق در یک خاطره‌نویسی جدید نوشت.
«او را با قطعیت شناسایی کردند. با وجود اینکه تعداد زیادی از افراد روی ساحل حضور داشتند، هیچ‌کس متوجه آن‌ها نشد،» او  مدعی شد و توضیح داد که چگونه کماندوها به‌صورت بی‌صدا به خانه سلیمان نزدیک شدند در حالی که او و مهمانانش روی یک تراس باز نشسته بودند و از فاصله‌ای حدود ۱۵۰ متر به او شلیک کردند.
«سر او به عقب افتاد. بلافاصله پس از آن، جنگجویان به سمت آب عقب‌نشینی کردند و راه خود را به سمت قایقی که آن‌ها را برداشت، باز کردند،» .</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20528" target="_blank">📅 22:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20527">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">امروز چند بار تتر تا ۲۰۰ تومان ریزش داشت!  به نظر عده ای دارند نقد می‌کنند   تارگت کماکان ۲۴۰</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20527" target="_blank">📅 21:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20526">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8aKo82nyo4yPJo7Ksk6ORdACvpeKi9isaLfb_5xjneTryfuC6d9NpaQpLR1E-u2rgUKmu0w_HSfwhUwjLMkVK2KknDoABIoseF4IzHpSM0J5ZOTaXzu_QVPhvjyDW34AAWj8MAUWBWhidNkHXcoG8L2AQPAgfQ9udI2icFI5thkSTMySLGi8hShMvGQgPdp2uSYrwLbAktfoER5m4wobyQldSGq_Xd3cMsq3dSUPRM3HPmLbQ3GeAhW4Ym0l_LKA3UWisei7L-4TCITcM3XTjoQj9AJz1ky47dLWMapj87YNAxixqh0G0Ok8HOMYL_CH5aMo2vSWWLZzXL_Eul8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا یکی به نوید ممدزاده بگه  وقتی روی مواد هست  گوشی دست نگیره  مرسی  @PiknikAnalyst</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20526" target="_blank">📅 20:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20525">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ایران از طریق عمان پیامی به ایالات متحده ارسال کرده و هشدار داده است که در صورت هرگونه تهاجم اسرائیلی به ارتفاعات علی‌الطاهر در جنوب لبنان، به‌شدت پاسخ خواهد داد؛ جایی که باور بر این است که نیروهای سپاه پاسداران، از جمله دست‌کم دو افسر ارشد ایرانی، در کنار…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20525" target="_blank">📅 20:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20524">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سبحان الله این محمدسامسینگ ما چه انگلیسی اش خوب شده!</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20524" target="_blank">📅 20:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20523">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">قالیباف خطاب به وزیر خزانه‌داری آمریکا</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20523" target="_blank">📅 20:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20522">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwPvralCh-A3VS8bzStJvs3kQAEQIIz7wDS6gqHt3rsyNHXC_H18DZzQ8lWMtSIkBmNr5GiqcDZkL6aSIOxRlSDPHzL712WgtQL7oYv0qqwQfT8ZwxCEgxgg9-IgyvYf6_PtzPFREY3L9_UzyzheCqDIJX9fOSasC7M5YaVlWmZxLRcVI6zIEIqd_0XUokIKi_wpCoK8Crt8_STD7RxTplWHz0PM85wYWsYhNAQ1spZ6R-36TRl6c2k1fYJAUtmyXyeuS6xIBmGfMW7sLy3RCkU1gNHxvWrvyfzLPF_yjtUm_sqFDutQzqs1haD2uq6yrjh6WdPVbycFB_ynS-7CVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف خطاب به وزیر خزانه‌داری آمریکا</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20522" target="_blank">📅 20:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20521">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">موشک‌های ایرانی به سمت کشتی‌هایی که مقررات تنگه هرمز را نقض کرده بودند، شلیک شدند.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20521" target="_blank">📅 20:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20520">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">— نتانیاهو، نخست وزیر اسرائیل، در مورد ایران:   ما با تهدید نابودی توسط رژیمی روبرو هستیم که می‌خواهد از بمب‌های هسته‌ای برای نابودی ما استفاده کند.  من به توانایی خود برای از بین بردن این تهدید برای همیشه، یعنی سرنگونی این رژیم، اطمینان دارم.  این ماموریت…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20520" target="_blank">📅 19:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20519">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">— نتانیاهو، نخست وزیر اسرائیل، در مورد ایران:
ما با تهدید نابودی توسط رژیمی روبرو هستیم که می‌خواهد از بمب‌های هسته‌ای برای نابودی ما استفاده کند.
من به توانایی خود برای از بین بردن این تهدید برای همیشه، یعنی سرنگونی این رژیم، اطمینان دارم.
این ماموریت اصلی است که هنوز پیش روی ماست، اما نزدیک است. غیرممکن نیست؛ در دسترس است.
آنها بی‌دلیل از حمله به ما اجتناب نمی‌کنند. آنها به همه حمله می‌کنند، فقط به ما حمله نمی‌کنند. آنها قدرت ما، قدرت بازوی ما و عزم ما را می‌دانند.
من به طور کلی به دشمنانمان می‌گویم: با ما درگیر نشوید. اگر چیزی یاد گرفته‌اید، با ما درگیر نشوید. ما قدرت، عزم و وحدت درونی برای غلبه بر شما را داریم.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20519" target="_blank">📅 19:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20518">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">۱۸ سرباز پاکستانی در یک حمله چریکی در منطقه زیارت بلوچستان کشته شدند.   گروه BLA مسئولیت این حمله را بر عهده گرفته است.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20518" target="_blank">📅 19:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20517">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">۱۸ سرباز پاکستانی در یک حمله چریکی در منطقه زیارت بلوچستان کشته شدند.
گروه BLA مسئولیت این حمله را بر عهده گرفته است.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20517" target="_blank">📅 19:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20516">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بفرمایید:  پنتاگون آزمایش کمبود تستوسترون را روی مردان بالای 30 سال آغاز خواهد کرد.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20516" target="_blank">📅 18:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20515">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ولی خداوکیلی این آمریکایی ها ترسناک هستند؛ شما فکر کنید هوموی مفعولشان اینطور خشن است وای به حال هتروی فاعلشان!</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20515" target="_blank">📅 18:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20514">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PO2wEEhcCuPeCxqjJTQOTNJ6czmwPu8C9Pxusx-qFOiFl3AWuFYffaBBlClHk2WAdWqEmNNXTTrbqSI0_H0mKcCdqsy0WYcbe7XwwpPgNpsx2jK02EpCzLlP5Mib2nqurggnSHvgxDX1rFskIXyJW9Mww1ko_bZ-j8WpVBaXl2XQgZQ9JkdYBuKE_YpfrxtGEAuNKbzywjAuv3enabPtoeQOMCXgy1xoElGNEqGLRPPfKZ1puqUdsdk8-32iT4GSW_2scb7pD5ecRD9dZLh5HNbj7gqSW_WlJHr4gNlEgffnJrDtAc1J1ka2ixKCX3tPk2bgly2y2yQ5ygBqKH0swg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل دقیقی است. تمایل جناح تندرو تداوم همین وضعیت است تا هم فشار برای بهای نفت و اقتصاد کشورهای منطقه و نرخ های بازدهی اوراق بدهی آمریکا حفط بشود و هم هیچ تعهد جدیدی برای خارج کردن اورانیوم بشدت غنی شده و برنامه موشکی و .... داده نشود.  طبق این  دیدگاه، نهایت…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20514" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20513">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ :  برای آن آشغال‌های  خائنی که از گزارش دقیق عملیات نظامی ما در ایران خودداری می‌کند، ما عملاً مقادیر نامحدودی مهمات با درجه متوسط ​​تا بالا داریم، بسیار بیشتر از آنچه که می‌توانیم برای این جنگ یا برای هر جنگ دیگری (که بسیار بعید است!) استفاده کنیم،…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20513" target="_blank">📅 18:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20512">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ :
برای آن آشغال‌های  خائنی که از گزارش دقیق عملیات نظامی ما در ایران خودداری می‌کند، ما عملاً مقادیر نامحدودی مهمات با درجه متوسط ​​تا بالا داریم، بسیار بیشتر از آنچه که می‌توانیم برای این جنگ یا برای هر جنگ دیگری (که بسیار بعید است!) استفاده کنیم، جنگی که به احتمال زیاد می‌تواند رخ دهد.
علاوه بر این، ما در حال تولید مهمات در سطوحی هستیم که قبلاً هرگز دیده نشده است. ما در حال ذخیره و آماده شدن برای هرگونه احتمالی هستیم. ما آنها را برای خودمان، ایالات متحده، به جای فروش به دیگران می‌گیریم، اما فروش به متحدان به زودی دوباره آغاز خواهد شد.
همچنین، لطفاً اطلاع دهید که دولت بایدن مهمات بسیار بیشتری را بدون هیچ هزینه‌ای برای آنها، نسبت به آنچه ما در ایران استفاده کرده‌ایم، به اوکراین داده است. صدها میلیارد دلار به اوکراین و ناتو، رایگان، داده شده است که اروپا می‌توانست آن را بپردازد - اگر فقط از آنها درخواست می‌شد، اما ما آن پول را درخواست خواهیم کرد، هرچند کمی دیرهنگام!
از توجه شما به این موضوع متشکرم. رئیس جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20512" target="_blank">📅 18:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20511">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUIFv4Qn8t4-GdHtrBFJsUDgDOfiULEDTxWpWkIMJIfVzxg7KzGY81LRqQQeRXp7dmVw_XmaWOKpwm9_nHPhtnOd-eAVzWDM6MPZf80JYz-SL8rMlmIVsmnVf46HaNq0rfe1JGnB3LMRvDUpelx4S4yqbgDKRP-Ua8fgGa-GvJICFhwWBgi9E2s1LfSWgLSCU8jv4T0omZ8JFuxx8PLCMMjt5sYJ5Zrlih441VLZicog_NQD-ZWy3xAh9XZsuYjquc6AXgolvpjX6b0kTNnMylTTNEcF-ar6cEfbLdnEVF0FLCvzRm7qJJZ-QTR0SsypaJo50fZ5TO-iKzFfhNuJsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار باز دارد پارابولیک رشد می‌کند و من خوشم نمی آید  فکر‌کنم تا ۲۰۰ پولبک بزند.  تارگت کماکان ۲۴۰ در گام نخست</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20511" target="_blank">📅 18:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20510">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد و پیش بینی می شود دستکم تا 4385 شاهد افت قیمت باشیم.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20510" target="_blank">📅 16:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20509">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دلار خرید دارد همینجا با تارگت ۲۴۰ الی ۲۶۰ هزار تومان</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20509" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20508">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">#سکه  عیناً مطابق سناریو ترسیمی رفتار کرده تا کنون. شکسته شدن خط مقاومت مورب یعنی سکه دوباره برای بالای 200 میلیون تومان خیز خواهدبرداشت. (برای موج نهایی صعود)</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20508" target="_blank">📅 15:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20507">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">در حملات هفته‌ گذشته آمریکا؛ ۳ خلبان و ۶ افسر نیروی دریایی ارتش نیز کشته شدند.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20507" target="_blank">📅 15:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20506">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ایران از طریق عمان پیامی به ایالات متحده ارسال کرده و هشدار داده است که در صورت هرگونه تهاجم اسرائیلی به ارتفاعات علی‌الطاهر در جنوب لبنان، به‌شدت پاسخ خواهد داد؛ جایی که باور بر این است که نیروهای سپاه پاسداران، از جمله دست‌کم دو افسر ارشد ایرانی، در کنار…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20506" target="_blank">📅 15:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20505">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ایران از طریق عمان پیامی به ایالات متحده ارسال کرده و هشدار داده است که در صورت هرگونه تهاجم اسرائیلی به ارتفاعات علی‌الطاهر در جنوب لبنان، به‌شدت پاسخ خواهد داد؛ جایی که باور بر این است که نیروهای سپاه پاسداران، از جمله دست‌کم دو افسر ارشد ایرانی، در کنار جنگجویان حزب‌الله مستقر هستند.
— رويترز</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20505" target="_blank">📅 15:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20504">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afHOdNbK7G2qVHEiv5EpXb2MQpRbFcvIKd3ZWBJMP_DvnJcW1iFl_u8jJ8Fiuj9n8SnExlBwvO4zookWhiTvxL8GuU2tqCHF2s-Vb3LCbkLzBr6tK2EJ3A4doIAp9avvWDdHd-ySd4Y0aAVZYjoMzmh6BF9w0fA2_rJmZMziZ5CSV6G2QTLcjKZzyuEujHyx4PGOoIbReHzukFpGSdC0vCwhIefcyr0yWOELItvtAR8O-p5284T-yS0s-SVM4jaKMc5ojUoD-WHTXRX0Er0NFJGEAS1jOvq2a1XMtNI_xP71-WbL_NM9aSE9-lenCf6_icKsRxCk9fNKO3Q5GQHdxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستایش ترامپ از نقش آفرینی جدید سوریه در ارائه مسیر جایگزین برای هرمز !</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20504" target="_blank">📅 15:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20503">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آزمون های  pte و mcq  هم بعد از تافل و GRE برای ایرانیان مقیم ایران لغو شدند.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20503" target="_blank">📅 11:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20502">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آزمون های  pte و mcq  هم بعد از تافل و GRE برای ایرانیان مقیم ایران لغو شدند.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20502" target="_blank">📅 11:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20501">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حمله ایران به پایگاه های آمریکا در کویت!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20501" target="_blank">📅 11:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20500">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">📌
نرخ بازدهی اوراق آمریکا در آستانه ۵ درصد؛ بازارها آماده یک شوک نرخ بهره می‌شوند؟  افزایش بازدهی اوراق ۱۰ساله آمریکا به محدوده ۵٪ می‌تواند فشار مضاعفی بر سهام، طلا و دارایی‌های پرریسک وارد کند و هم‌زمان دلار را تقویت کند.   اما اگر رشد نرخ‌ها از نگرانی درباره…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20500" target="_blank">📅 11:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20499">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RADhSTWZ4I2lPKixpovrPsFiWttRJX4qZrlFW7SBXfHDx2p1byLRCO_Yk9YsJURLmYQkb8hZIVWYF-xEEnFHXI-LzechuCcYZ2gmy3mYR7i6APt3ZsTMOanqRu7vIPrq2VFe-Ym11vnUh2SxtdrIe_Zw9xYgs9I1eTrhX4OsOWLLtAOtWXVN5ZtiN31NG9bjqMDSV0dzVo33ZzMdCXLOqZBufjmTEkKB0lQ2A-tY0Iaod1GATJe7AhyepH6kteNEZMfycQHplj9BaVQukLy4Yojfc2BPWL0KPDf4TodHIT1G7UXlo5GVudWhM1QlWdD5LkWy57_if1bfN9JDlvDXKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20499" target="_blank">📅 11:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20498">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGP-Si3UxPlMuJDsCxrlrY1uSZmnjVrIOm5uitAMPUB7ednxntGaJo3vFXKuavqyacytODyaUz-ug0R_YFbqBR8h-7wtH2ZVq9qOBFE_etgkmpKOZwEv32pgpHvd5vYb_V8NklJ6f-S5u84a8J2IayhPhy8O0sEy6skh2imqqmGqFkF4XBVLpr0mfZ6FxXhW4MqrjcDpK_ZMJeiv1HJ4rjSHQeoHIznALXIc6r94c_QXqcRqS2kM9gkG99yxJoWIJJFpOFbTw84qLXcgdDqrBvBkN_oAJKiWXGYUxHEHpG7mi0b2eoYdTAKS6Z0_OhWH1go-oC9u4iPXg8haxQS4bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نرخ بازدهی اوراق آمریکا در آستانه ۵ درصد؛ بازارها آماده یک شوک نرخ بهره می‌شوند؟
افزایش بازدهی اوراق ۱۰ساله آمریکا به محدوده ۵٪ می‌تواند فشار مضاعفی بر سهام، طلا و دارایی‌های پرریسک وارد کند و هم‌زمان دلار را تقویت کند.
اما اگر رشد نرخ‌ها از نگرانی درباره کسری بودجه و پایداری بدهی آمریکا ناشی شود، معادله می‌تواند تغییر کند؛ طلا به‌عنوان پناهگاه امن تقویت شده و بازارها با ریسک بازقیمت‌گذاری گسترده مواجه می‌شوند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20498" target="_blank">📅 11:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20497">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIHqf_Ey35mHOVu_U38Z-FsrXqAl6v-RqL84N4tpT_dnd25gZ1R4XKiaYTCdFr-YIDjzrRtXMRNGw-5WS1hJ9Smd7M-tAl2Vr1YZYTcvFJHCkRABBhreRLlytlJ356_VuuZigiFNw_rx2Hpfiyiy5pEfJeWLybRraNzimoK8PIeHhbvumEPbyXVrUakVzOhU9ztbllUU_UATRrulgKcfVkKfy9mHaNpE6QNuqaOcgAOK5zSDkIg5_ZFlTSPD7Pn5PQCmwkOcnCUIhW4lAKrVFaLOwqTSaczjYc-S-vMeNRT5pDTB-_Zz_Orcfm7wOqaFyqr0NgYQl_9G0mcxqvfImw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد و پیش بینی می شود دستکم تا 4385 شاهد افت قیمت باشیم.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20497" target="_blank">📅 10:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20496">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0447727037.mp4?token=CYgSB3bZrdBciu7FyVtZG5TnASum_fyVvf6T_biDUnIYd7ZvkIUZuxI2kwov8Ek54fTuHSH5lMmN5aqnghKkgeVfisN3cvctCRXY0v_QNHbL6fVQgKTBeejheOxFa-ydfyAa2bEvEUdFwiiZ6q7tWVfN-l5AAAzHlVqZIbkbkBAkrBGnVhrHCV9bZF3Xco2-bSxIFuC5PMeVXRfdDyMNokgopg3WxV50SUcRd3AzpY4Y-exU9ZAYoOA6vo068TnCIhwqDMgec2RUkktpykteOvDKbiIKaFk0Ry87TQJ6-IjV4I1OmyHsy6K4xBeL-9ZCcqLX4hJv7enV8MtdHub1abBu0RsvNJA-rea93CjSIkCejW96tgD6kgzm9Sxx89zzCbIu3BATVLG3tww2Hjo89UOEdX98ThFzzChev2iFUDHAp_ieoJOnfY_2TN71sW1i-uMrGvh4iSOZv19pTTvyrs9Ufe7pb16Jns3SdhuybNXPiSj8P6ivBuUXYaryfVUG2sQfaQeec53p-THQIUXE_u-TF3Y_hul7i1vpQW7URuyQTHDy1HDvBeY-11VahEg9DsOxU4LAmm2zhhGVuQPgIEbtCZ0wzSRyZIL-p9JQIK-c8xJzCSyQop8T_W1hGFuAXSO5ZXp05HIE6iMm4Tg8_6PiXpfbLlzXRSNkdZmv3-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0447727037.mp4?token=CYgSB3bZrdBciu7FyVtZG5TnASum_fyVvf6T_biDUnIYd7ZvkIUZuxI2kwov8Ek54fTuHSH5lMmN5aqnghKkgeVfisN3cvctCRXY0v_QNHbL6fVQgKTBeejheOxFa-ydfyAa2bEvEUdFwiiZ6q7tWVfN-l5AAAzHlVqZIbkbkBAkrBGnVhrHCV9bZF3Xco2-bSxIFuC5PMeVXRfdDyMNokgopg3WxV50SUcRd3AzpY4Y-exU9ZAYoOA6vo068TnCIhwqDMgec2RUkktpykteOvDKbiIKaFk0Ry87TQJ6-IjV4I1OmyHsy6K4xBeL-9ZCcqLX4hJv7enV8MtdHub1abBu0RsvNJA-rea93CjSIkCejW96tgD6kgzm9Sxx89zzCbIu3BATVLG3tww2Hjo89UOEdX98ThFzzChev2iFUDHAp_ieoJOnfY_2TN71sW1i-uMrGvh4iSOZv19pTTvyrs9Ufe7pb16Jns3SdhuybNXPiSj8P6ivBuUXYaryfVUG2sQfaQeec53p-THQIUXE_u-TF3Y_hul7i1vpQW7URuyQTHDy1HDvBeY-11VahEg9DsOxU4LAmm2zhhGVuQPgIEbtCZ0wzSRyZIL-p9JQIK-c8xJzCSyQop8T_W1hGFuAXSO5ZXp05HIE6iMm4Tg8_6PiXpfbLlzXRSNkdZmv3-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف طولانی بنزین در مملکت دوست و برادر روسیه!</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20496" target="_blank">📅 10:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20495">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حمله ایران به پایگاه های آمریکا در کویت!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20495" target="_blank">📅 10:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20494">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZmp0zYvQePXk9LflVF_748hA-VxTU-ZWYDE4SSyXCVB26Of9ZB59JTdcJH_AMUPScqNSEbzGEXCPoyr1dB5TC4rKPLTDvkmM1-sOSw6aOItw6qqmsc7F8r0ZnjE9pxyavW5Co7jRr8IyFomHfuVXELex2bK_PCnu_NfataSG2uIxKGbWkCbw25DO0HV6id99YSMl5n8u-WcQuJ7FVtDRsbjnLFUS9F7jJV7XEiSP-VpdQYkcxiY-1SQuq2DdzCfg5e6E2rs2h6-F72XpSvrTaFJxdeTQWFuGOaNqXBoQ0ntpYBYnJccOPZiVqUBhA3ynpj52X6KXXLfQZPQs_JvNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20494" target="_blank">📅 01:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20493">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انتشار اخباری از انفجار در میناب!</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20493" target="_blank">📅 01:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20492">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انتشار اخباری از انفجار در میناب!</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20492" target="_blank">📅 01:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20491">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جمهوری نظامی ایران.pdf</div>
  <div class="tg-doc-extra">257.6 KB</div>
</div>
<a href="https://t.me/SBoxxx/20491" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">موسسه معتبر مطالعات جنگ (ISW) در
گزارشی
به میلیتاریزه شدن فضای رهبری کلان جمهوری اسلامی پس از جنگ اخیر پرداخته است که ترجمه این گزارش — با اندکی تغییرات اجباری — اینجا ارائه می شود.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20491" target="_blank">📅 01:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20490">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گزارش هایی دال بر پرتاب موشک از سوی سپاه</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20490" target="_blank">📅 01:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20489">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-poll">
<h4>📊 دکترین «دفاع موزاییکی» توسط کدامیک از فرماندهان نظامی جمهوری اسلامی تدوین و تببین شد؟</h4>
<ul>
<li>✓ محسن رضایی</li>
<li>✓ محمدعلی جعفری</li>
<li>✓ رحیم صفوی</li>
<li>✓ احمد کاظمی</li>
</ul>
</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20489" target="_blank">📅 01:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20488">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ: «ما همه کارهایی که در ایران انجام می‌دهند را می‌بینیم.آن‌ها حتی نمی‌توانند بدون دیدن ما به دستشویی بروند»</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20488" target="_blank">📅 22:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20487">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ: «ما همه کارهایی که در ایران انجام می‌دهند را می‌بینیم.آن‌ها حتی نمی‌توانند بدون دیدن ما به دستشویی بروند»</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20487" target="_blank">📅 22:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20486">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔹
خبرنگار: آیا شما سازمان سیا را برای مسلح کردن ایرانیان اعزام خواهید کرد؟
ترامپ: من نمی‌خواهم این را به شما بگویم، مناسب نخواهد بود</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20486" target="_blank">📅 22:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20485">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فوری | ترامپ: ایران در تلاش بود تا موشکی بسازد که بمب‌ها را حمل کند و ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20485" target="_blank">📅 22:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20484">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20484" target="_blank">📅 22:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20483">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">برخی اکانت های مربوط به جریانات تندرو، خبر از احتمال تسلیحاتی شدن برنامه هسته ای ایران بر اساس مواضع دبیر جدید شورای عالی امنیت ملی خبر می دهند</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20483" target="_blank">📅 22:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20482">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این گزارش های آژانس هسته ای و اظهارات تند ترامپ + نتانیاهو شرایط را به صورت قطعی به سمت جنگ می برد.
مراقب موج‌۳ باشید.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20482" target="_blank">📅 22:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20481">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فوری | ترامپ: ایران در تلاش بود تا سامانه‌های رادار و موشکی خود را بازسازی کند.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20481" target="_blank">📅 22:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20480">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فوری | پیش‌نویس گزارش آژانس بین‌المللی انرژی اتمی: ما تأیید می‌کنیم که قادر به بررسی این موضوع نیستیم که آیا مواد هسته‌ای ایران به اهداف نظامی تغییر یافته‌اند یا خیر.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20480" target="_blank">📅 22:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20479">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فوری | پیش‌نویس گزارش آژانس بین‌المللی انرژی اتمی: از ماه فوریه، هیچ بازرسی از تاسیسات هسته‌ای اعلام‌شده در ایران انجام نداده‌ایم، به جز بوشهر.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20479" target="_blank">📅 22:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20478">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فوری | ترامپ: ایران در تلاش بود تا سامانه‌های رادار و موشکی خود را بازسازی کند.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20478" target="_blank">📅 22:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20477">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فوری | ترامپ: ایران در تلاش بود تا موشکی بسازد که بمب‌ها را حمل کند و ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20477" target="_blank">📅 22:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20476">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فوری | ترامپ: ایران در تلاش بود تا موشکی بسازد که بمب‌ها را حمل کند و ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20476" target="_blank">📅 22:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20475">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">— نخست‌وزیر اسرائیل، نتانیاهو:
«حکومت ایران سقوط خواهد کرد. ما آن را سرنگون خواهیم کرد. این حکومت اکنون در آخرین لحظات خود به سر می‌برد.
تمام سیستم‌های ما، تحت هدایت من، برای سرنگونی این حکومت عمل می‌کنند».</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20475" target="_blank">📅 20:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20474">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تسنیم:
کشته شدن ۱۸ نفر در حملات دیشب آمریکا
وزیر بهداشت: در حملات شب گذشته به استان‌های مختلف کشور ۱۸ تن شهید و ۱۰۸ تن از هموطنانمان مجروح شدند.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20474" target="_blank">📅 20:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20473">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ:
حالا که تنگه هرمز تحت کنترل آمریکاست، آیا باید اسمش را به تنگه ترامپ تغییر بدیم؟؟؟ مثل خود آمریکا، این منطقه «داغ‌تر» (پررونق تر) از همیشه خواهد شد.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20473" target="_blank">📅 19:02 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
