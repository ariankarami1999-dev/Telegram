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
<img src="https://cdn4.telesco.pe/file/ejt3VVXoSgDvPPpmW07oFM56JQwG74UWeY0JkPlKdgbx5pTL9g6N10btAv3H72hW8xpmxdgyykBPbIm1lYM_IGMxYqMQOvgxAYYRU0sFHJamso4J0WscUb_gMvkNR2LOBD_us-4HwySs-q-n12k9NsHL2gwRcj8kR57-apfI30wPH0S9DP6yRq06f23mjDdSj7_wLkU2fOn24kA_9bO1quwCPqJQ5PhHpQhn2RvRbpZAJ96VtUKPgauYjs6wCd9Ju3KLOQHulov7wFkgee3XnJ2NEVuUx8gKb8JWgPONwDLhxRm3_GoUolpSLXpqbEiJdam-T47U4viScELfmWqU-Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 14:29:53</div>
<hr>

<div class="tg-post" id="msg-453339">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/017513eea3.mp4?token=bhTzv_hqhxw7eB6joJpkwanXzj4thy3LHgo6L2t-Wg2FXtqm114vbwUj5iyNvBzyJ4hHaS6RQlkpe87xMOhhDxtl1R0-4VgQXNcAx8cFahooHM4jmUzm0UFK9CnIUHpaxpD5-eRsCrYyeI1OwCwBWwhb1hoY6l6glZhe7lZLeeYPElUas3wAO6_v1cN0afL7cSH56Nz4Lu5_3Sly3_tDcaEP3SfwQIxqUzD387N0vEwfZEUJzminXr-TtNHOwCAmvqslyMdPiYCt0Aelkd-b6aNKZRFK2pEW5lKidxY9ph5AR6x_mGPwd39Or4h-4Yft2MGro49dAzR4tF3D3pfvSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/017513eea3.mp4?token=bhTzv_hqhxw7eB6joJpkwanXzj4thy3LHgo6L2t-Wg2FXtqm114vbwUj5iyNvBzyJ4hHaS6RQlkpe87xMOhhDxtl1R0-4VgQXNcAx8cFahooHM4jmUzm0UFK9CnIUHpaxpD5-eRsCrYyeI1OwCwBWwhb1hoY6l6glZhe7lZLeeYPElUas3wAO6_v1cN0afL7cSH56Nz4Lu5_3Sly3_tDcaEP3SfwQIxqUzD387N0vEwfZEUJzminXr-TtNHOwCAmvqslyMdPiYCt0Aelkd-b6aNKZRFK2pEW5lKidxY9ph5AR6x_mGPwd39Or4h-4Yft2MGro49dAzR4tF3D3pfvSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقتدار به روایت صیادان هرمزی
🔹
صیادان جزیرۀ هرمز تصاویری از اعمال نظم ایرانی در تنگۀ هرمز ثبت کرده‌اند؛ تصاویری که نشان می‌دهد کشتی‌هایی که بخواهند از مسیر غیرقانونی عبور کنند دچار دردسر می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/farsna/453339" target="_blank">📅 14:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453338">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
منبع آگاه: هیچ شناوری بدون اجازۀ ایران حق عبور از تنگۀ هرمز را ندارد
🔹
یک منبع آگاه نظامی در گفت‌وگو با فارس: تنگۀ هرمز همچنان به‌طور کامل مسدود است و هیچ شناوری اجازۀ عبور از این آبراه راهبردی را ندارد.
🔹
کنترل کامل تنگه هرمز در اختیار نیروهای مسلح ایران است و هرگونه تلاش برای عبور شناورها، به‌ویژه شناورهایی که به اخطارها توجه نکنند، با واکنش قاطع و فوری مواجه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/farsna/453338" target="_blank">📅 14:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453337">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efdbfc3d69.mp4?token=SxfPTD4oLXv997lA2uA7m8t_t4CKOig2xBj8U28CZG-AS3P4w0tUCzjbtbK5luDG0-OWj2ha3LI2EQyXyYJODIJZ4u8dnL3ZGU9j1B4cmR9SyxHcDOVX-Wch2lMaJaq-lB6uZr6u1Sc1-gGDpnREPuvbdPgS4uaqRWjcUBzReATkGr0UAasPR8Xifg_CBWz1F2OGqDYYz9frxYZ_h3rELctZMBY9fHkWDz_OkWiJMBMIJGcPXCUuJMOpuRkn8CIL8_ZoAqmo1MCqeyjrl2gZrK9bZGL0NbBgpVrjYAbSBgXM6fqNXl56Hz7-io-VtXA-GJbZXImXjf4DBv_KRVbgeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efdbfc3d69.mp4?token=SxfPTD4oLXv997lA2uA7m8t_t4CKOig2xBj8U28CZG-AS3P4w0tUCzjbtbK5luDG0-OWj2ha3LI2EQyXyYJODIJZ4u8dnL3ZGU9j1B4cmR9SyxHcDOVX-Wch2lMaJaq-lB6uZr6u1Sc1-gGDpnREPuvbdPgS4uaqRWjcUBzReATkGr0UAasPR8Xifg_CBWz1F2OGqDYYz9frxYZ_h3rELctZMBY9fHkWDz_OkWiJMBMIJGcPXCUuJMOpuRkn8CIL8_ZoAqmo1MCqeyjrl2gZrK9bZGL0NbBgpVrjYAbSBgXM6fqNXl56Hz7-io-VtXA-GJbZXImXjf4DBv_KRVbgeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت علی صدری‌نیا، مستندساز و فعال رسانه‌ای از آخرین حضور شهید لاریجانی در مراسم اربعین در کربلا
@Farsna</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/farsna/453337" target="_blank">📅 14:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453336">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGejz6tPI3VqDrY6A9YBXWgFf0glgcjGCia3ozj4eYy1oB6oguho9RX2Y5_ahcNmH_C77TfZOraE_U6hhH8xq77o-SBBUby8_ODCEIbj6_1FX55qjdlRF-o4s-DAZjsEU36HtgjKmJ8pLPGNWJJwoe-ZpFtYAQBnOBIiIOadNP1_lTqd0tXF6bqr5qGRv2mJKJRkuOYKmCCYGXoaoy8XO_VIh2hVYhJ-Ij98uZ7CZBzTBY4mSb65HlY-qEUdoaqk3KkNP3KKeyadPADAX1VC3zpd6rLBFDrK2qetPbCvwk-NPcXLE3rH-BmYn2YuX7izTBSPTO5-aU_KxSoDOvoCUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاروان اهالی هنر و رسانه به کربلا رسید؛ زیارت به نیایت از رهبر شهید
🔹
کاروان اهالی هنر و رسانه به میزبانی ستاد اربعین شهرداری تهران روز گذشته دوشنبه ۵ مرداد ابتدا عازم نجف و سپس کربلا شد.
🔹
هنرمندان، سینماگران، کارگردانان و مجریان تلویزیونی در این سفر همراه شدند که از جمله آنها می توان به مهدی فرجی، منوچهر محمدی، دانش اقباشاوی، سیدعلی احمدی، محمود کریمی، محمدرضا شفیعی، سعید پروینی، جواد شمقدری، حسین شمقدری، وحید رونقی، احسان مهدی، حامد مدرس، علی صدری نیا، حبیب والی نژاد، محسن اسلام زاده، بشیر حسینی، هادی نائیجی، فاطمه افشاریان، محیا اسناوندی، راحله امینیان، فضه سادات حسینی، شهره پیرانی، محمدرضا باقری و همچنین چهره هایی چون حجت الاسلام شهاب مرادی اشاره کرد.
🔹
این سفر که به دعوت ستاد اربعین شهرداری تهران انجام شده، قرار است نوعی قدردانی از مردم عراق بابت اقدامات میزبانی همه ساله اربعین و برگزاری آئین تشییع باشکوه رهبر شهید و جنگ رمضان باشد.
@Farsna</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/farsna/453336" target="_blank">📅 14:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453335">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-text">◾️
اینجا عشق به اباعبدالله(ع)، در قامت خدمت معنا می‌شود؛ روایتی از خادمانی که در موکب بانک شهر، دل به میزبانی از زائران حسینی سپرده‌اند.</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/farsna/453335" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453334">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/farsna/453334" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453333">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVSSQg_i4XIvJTJUDaG6dYeS5_jZp3cGzuqGIBhZdWhI45-HblJEIIvIxi91QedWxKL4fIK2w00pu_WWcvZqu28lzwYpgDbiavXyRN7gP8PlngxkR1diV5c2yxidLyaYvTtw0-Ws_VxLV6gyQo5vv1JwhKbTNj1KKdtGnxpg_YRtut8WJRtSKebZri5HSWgpyTh_mEKUDFXs-eKlz7J36SYPrhdEe0cAtIejJinmNT9p8mNKBZWOPUiFssL5lZ5TCCVJsDbU82WFfTtBzk9Z4qA1HFtKujoHe9E0cmv704ged-hN6_9aJmgePUjaeH1iigvv2D5IZTrHwg7cN1ohug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وثیقۀ تحصیل در خارج به ۲۰۰ میلیون رسید
🔹
براساس به‌روزرسانی سامانۀ سخا، مبلغ وثیقۀ مورد نیاز برای خروج از کشور با هدف ادامۀ تحصیل از ۸۰ میلیون به ۲۰۰ میلیون تومان رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/453333" target="_blank">📅 14:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453332">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
حملۀ دشمن به محلی در آذربایجان‌غربی
🔹
مدیرکل مدیریت بحران آذربایجان‌غربی:‌ یک موشک دشمن به یک منطقهٔ خالی از ابنیه و سکنه در استان برخورد کرده هیچ تلفات جانی نداشته است.
@Farsna</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/453332" target="_blank">📅 13:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453331">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49f64fcfd4.mp4?token=UrVLzCFbGUK9s_zFY393JbbldBngv6-x38109cca7oIknSBI_Q_DNUvdqyw9AXVhuNlIFSN5eoFpFr7QTttextSb9JNfQ0R5_LBXBORGpEku0MTbcyr-RW6Z0rMZFMZbnIXq5ZHE799JCkHfG0cD2Rl8X_WHsYgUBr0IEDrP-c1DGEDRxx3dGQ5_n_9v8t3lBgcxjrfBnQZzBBUuK5qPuaBAIuLGedl-jtBQ3zQCXLstBPuRJQgtgZaiFk5MeLbYZRZwQW2aLeLyenlksHFKfZQWY8tm-4S2L4ID0oW-4mzxj48P4H8kI6rwuSGSTBnHPe56wImrtgfUc1xpBiU89Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49f64fcfd4.mp4?token=UrVLzCFbGUK9s_zFY393JbbldBngv6-x38109cca7oIknSBI_Q_DNUvdqyw9AXVhuNlIFSN5eoFpFr7QTttextSb9JNfQ0R5_LBXBORGpEku0MTbcyr-RW6Z0rMZFMZbnIXq5ZHE799JCkHfG0cD2Rl8X_WHsYgUBr0IEDrP-c1DGEDRxx3dGQ5_n_9v8t3lBgcxjrfBnQZzBBUuK5qPuaBAIuLGedl-jtBQ3zQCXLstBPuRJQgtgZaiFk5MeLbYZRZwQW2aLeLyenlksHFKfZQWY8tm-4S2L4ID0oW-4mzxj48P4H8kI6rwuSGSTBnHPe56wImrtgfUc1xpBiU89Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سنگ‌تمام گواردیولا برای کودکان فلسطینی
🔹
سرمربی سرشناس اسپانیایی که از حامیان مردم غزه است، دیروز در جدیدترین دورۀ کمپ تابستانی خود در شهر ریالپ اسپانیا، از ۲۸ کودک فلسطینی برای حضور در این اردو دعوت کرد تا چند روزی را در فضایی امن سپری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/453331" target="_blank">📅 13:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453330">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae287dfe70.mp4?token=K0hgMbnIgpmA488xyQ4CQ79_RUIUHDoLLGChAFO-SKtRNeCq79RUSBUF3H-BBr2skzcrOx8FHktB5lKecG_09gCGW4SFROee2GEsNm1nyUVvZ6kK4NHBmlcHZyioI_wptr49OI9UjG5Iani6nDAoE2_9XQR9zMNCb9YxMIP0FvIaFCcY5wKXrxTuFYWEW3d7Xisu434Xo88u7mjc_cWlitjBGgNfGPPZpkoxIZYAH4A5ON9ppMG67wRlnRumDkK2JKxM020wrfx3NbBLbSPqkuHXniSuw5a20B_IAZqeVPMtKBQqjx-bTXgqd1eZ5NeWiLIfj9iTTkUsuXn9aLzBMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae287dfe70.mp4?token=K0hgMbnIgpmA488xyQ4CQ79_RUIUHDoLLGChAFO-SKtRNeCq79RUSBUF3H-BBr2skzcrOx8FHktB5lKecG_09gCGW4SFROee2GEsNm1nyUVvZ6kK4NHBmlcHZyioI_wptr49OI9UjG5Iani6nDAoE2_9XQR9zMNCb9YxMIP0FvIaFCcY5wKXrxTuFYWEW3d7Xisu434Xo88u7mjc_cWlitjBGgNfGPPZpkoxIZYAH4A5ON9ppMG67wRlnRumDkK2JKxM020wrfx3NbBLbSPqkuHXniSuw5a20B_IAZqeVPMtKBQqjx-bTXgqd1eZ5NeWiLIfj9iTTkUsuXn9aLzBMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر پرتاب موشک‌‌های بالستیک عملیات سحرگاه امروز نیروی هوافضای سپاه به مرکز فرماندهی مرکزی ارتش آمریکا در اردن   @Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/453330" target="_blank">📅 13:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453329">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6746d6a78.mp4?token=GlQ314RGfDdFDF1PaPkSDOl1To8qkcw15yvHOR2gAtXpPjWMXzddxlagayCqOykb5vlQFfu1iQ1_3FOVPVnA6MBnjH2nSXCqe6PmeH4BchvPMA7obriGNrHCkdxLziTD4WK8sVZjocrb9VoD5K70zByPe4YZJ35heRFxroq3Pi_uskEeIrMNIqyBhSOoGHXO0czYA7EcufUpzwy4vZgdQuLJBXRzE2lst3pqhI1nz0ONvT5U9uhARnRRQCiDU_RcYns0-iKq1HRdYgGA_56_4ax24w8ELuQLKb-xXQWWp-moCzjiUgAS21g5UE49xmIqveVQ70lOStP1jTI-tIeLsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6746d6a78.mp4?token=GlQ314RGfDdFDF1PaPkSDOl1To8qkcw15yvHOR2gAtXpPjWMXzddxlagayCqOykb5vlQFfu1iQ1_3FOVPVnA6MBnjH2nSXCqe6PmeH4BchvPMA7obriGNrHCkdxLziTD4WK8sVZjocrb9VoD5K70zByPe4YZJ35heRFxroq3Pi_uskEeIrMNIqyBhSOoGHXO0czYA7EcufUpzwy4vZgdQuLJBXRzE2lst3pqhI1nz0ONvT5U9uhARnRRQCiDU_RcYns0-iKq1HRdYgGA_56_4ax24w8ELuQLKb-xXQWWp-moCzjiUgAS21g5UE49xmIqveVQ70lOStP1jTI-tIeLsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلوه‌نماییِ عهد سرخ زائران در مرز خسروی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/453329" target="_blank">📅 13:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453328">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4b3766113.mp4?token=DlfCSgYqBx0W_kEe3J_cyFKUlffNi7o4A1mh0azgNbprcn4iIT6jY1t7ialtGFh5kSvgDHr4OKj2QFgPFgKE1iknVUOW7xqc8LiqZw7LuOG7RtArjE7_z_JGo4v6pfNRb39v_oPJFECGFX0i5I5zld09NljxPCxjaIM2B9toKwf5CREhOI020mWLkL9hh7ocXYKc8TP_j9IJK_4_RRX_ONqRaAkMyzxjl_CNKwvj7nDAIPCusv7YhH_YFv6NU0XApSn-SkDa2iu5IAzK5ifx6q-jRQYz_9Gw9ohbrofDUsMA72H2-NvyjgLA76eUM3o8opCN_AWATLzK7o1PrHZMlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4b3766113.mp4?token=DlfCSgYqBx0W_kEe3J_cyFKUlffNi7o4A1mh0azgNbprcn4iIT6jY1t7ialtGFh5kSvgDHr4OKj2QFgPFgKE1iknVUOW7xqc8LiqZw7LuOG7RtArjE7_z_JGo4v6pfNRb39v_oPJFECGFX0i5I5zld09NljxPCxjaIM2B9toKwf5CREhOI020mWLkL9hh7ocXYKc8TP_j9IJK_4_RRX_ONqRaAkMyzxjl_CNKwvj7nDAIPCusv7YhH_YFv6NU0XApSn-SkDa2iu5IAzK5ifx6q-jRQYz_9Gw9ohbrofDUsMA72H2-NvyjgLA76eUM3o8opCN_AWATLzK7o1PrHZMlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا اروپایی‌ها از گرما می‌میرند؟
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/453328" target="_blank">📅 13:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453327">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3gL1uxi7ihkO_m_PnatnvpRT6nR50itnDPcz96wDJzH_cul7X9_ltSX--5fyUXsdVNV8YTgi_6qD252tPp73rjHx4ZUFxqtEKuh3bzEPDdIumR5pCbUYx_rk2PgV3vKKyIu2yXOZ001iVc-s67-qCsUx0K8inGLlT66ilPxCNHt_BzypGyb5w3487Ggo0hpqzC2Jv0XeN0EUdPgOSubrS0Emu66EGlfZd48FPGDbvVa1iYDvMuByQ8b81RPY3cKxMrJLQ9UZgG0jDfrjxFd5TxpEY1-FmpsTd3Zn5t-xdzURZDG4st0QMShciP4QGjizQCVAOK-ANshYEknf94xzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد ۴ ماهه «کچاد» از ۵۷ همت عبور کرد/رشد درآمد نسبت به مدت مشابه قبل
شرکت صنعتی و معدنی چادرملو با نماد «کچاد»، در تازه‌ترین گزارش عملکرد ماهانه منتهی به تیرماه ۱۴۰۵، از تداوم روند رو به رشد و ثبت ارقام درخشان در حوزه فروش محصولات خود خبر داد. این غول معدنی و فولادی کشور موفق شده است در ۴ ماهه نخست سال مالی جاری، درآمد کلان ۵۷.۵ همت  را از محل فروش محصولات محقق کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/453327" target="_blank">📅 12:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453326">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-7um0GNUaINtY9C9w_pYYhD1BgQkm1Pj5_5fLClJnEaYNjb996wQ3L46VVmoDvFR2-NJpSmSfkZkgaWE97eHbEzgKbZBucAzXOB-grBs5nNHiMjFQQQ_KE_d3EFZ6ZKATp-c0vy2TUVPQIyfpT2nKVKbqjERItydoYcmCZjoNZVW0aaQQredvpdRU_5ErliH36A4wqshfDZ9hvqV40H9g0t5Co6iZRVDHneBPmqCjz1xObCX89wdeE32qJq_1FWyrzAlkfWP6U_Rq8c43ZcnSjuGxV0s1bKq0NmjD8d3yKek0LRNSh3uflmHxSQixrjCjY8-JGpOiSaG_Q8pBj2PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
انتشار اوراق گواهی سپرده خاص از سوی بانک رفاه کارگران تداوم دارد
🔹️
با هدف حمایت از تولید ملی و اشتغالزایی، اوراق گواهی سپرده مدت‌دار ویژه سرمایه‌گذاری (خاص) از سوی بانک رفاه کارگران برای شرکت‌های پالایش نفت اصفهان، کیاصنعت کاران آسیا و داروسازی کاسپین تامین، سپید مطهر انتخاب و نانو بتن امین منتشر می‌شود.
🔹️
علاقه‌مندان برای خرید این اوراق ویژه شرکت‌های پالایش نفت اصفهان، کیاصنعت کاران آسیا، داروسازی کاسپین تامین و سپید مطهر انتخاب تا پایان روز شنبه ۱۷ و برای شرکت نانو بتن آرین تا پایان روز شنبه ۳۱ مرداد ماه سال جاری فرصت دارند با مراجعه به شعب این بانک در سراسر کشور نسبت به خرید این اوراق اقدام کنند.
🔹️
این اوراق با نرخ سود علی‌الحساب ۲۵ درصد (پرداخت سود به صورت ماهانه)، یک ساله، به‌صورت با نام، الکترونیکی، معاف از مالیات و با امکان بازخرید پیش از سررسید منتشر می‌شود.
🔹️
از جمله مزایای خرید این اوراق می‌توان به دریافت بالاترین نرخ سود اوراق منتشره فعلی شبکه بانکی، تضمین دریافت اصل و سود در مواعد مقرر و... اشاره کرد.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/453326" target="_blank">📅 12:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453325">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/453325" target="_blank">📅 12:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453324">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a43f6b5dde.mp4?token=XlGwDGKtr5E_p5BSKtg_RO7vXv-UHHycJNT1uViXw3Xs-4i1R-hftTmwMryjuC-UxqbayG7raFliFJ4tLD0Y3oEzD3WrENQjbGr9JmY6FE29FjmeRrBDXhZAaT-amnBdk2LzNjQZBuUFL90I4g7e5_wqwF19tz4NWsRY3tQvRe4h09ki3Z8eIs4xl9yRuGpPZGtxOXBYpZsINKS7UI_BCx0ALEQQoYpZdtknOt2vdK7xoOKc6zaKs7nY-m4v5nVpIrz8LHhI3X9RvWyhPQf_C6Xdz8e6XJtAvbFQ2tr6HTrGyPGsjw10zmD54YZvaacBmK9qaX4gB7UDlRmyj8J6fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a43f6b5dde.mp4?token=XlGwDGKtr5E_p5BSKtg_RO7vXv-UHHycJNT1uViXw3Xs-4i1R-hftTmwMryjuC-UxqbayG7raFliFJ4tLD0Y3oEzD3WrENQjbGr9JmY6FE29FjmeRrBDXhZAaT-amnBdk2LzNjQZBuUFL90I4g7e5_wqwF19tz4NWsRY3tQvRe4h09ki3Z8eIs4xl9yRuGpPZGtxOXBYpZsINKS7UI_BCx0ALEQQoYpZdtknOt2vdK7xoOKc6zaKs7nY-m4v5nVpIrz8LHhI3X9RvWyhPQf_C6Xdz8e6XJtAvbFQ2tr6HTrGyPGsjw10zmD54YZvaacBmK9qaX4gB7UDlRmyj8J6fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه: پایگاه هوایی و مرکز فرماندهی مرکزی ارتش آمریکا در اردن هدف موشک‌های بالستیک قرار گرفت
🔹
در پاسخ به اقدامات تجاوزکارانۀ ارتش کودک‌کش آمریکا، ساعتی پیش رزمندگان شجاع نیروی هوافضای سپاه، پایگاه هوایی و مرکز فرماندهی مرکزی ارتش آمریکا در اردن را با…</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/453324" target="_blank">📅 12:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453323">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبرهایی از احتمال لغو سفر نخست‌وزیر عراق به عربستان
🔹
ساعاتی پس از حمله آمریکا و عربستان به اهدافی در عراق، برخی منابع خبری از احتمال لغو سفر نخست وزیر عراق به عربستان سعودی خبر دادند.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/453323" target="_blank">📅 12:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453322">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRbiE9SBngzf9hREls25I4Vi08amLUfne0hR4I_J5UYSyy7O2Gjz5k5y_A0waXBaLD4HMct-kO0SK6AYEQ7z8g7MeLvKUz7flJR5JW2bCSz0ONfuY_DqeFEv74Sw-HT8J7x-d0QVyLIjUXI4TF-6BdWS5TRkwDhhrcDobSTQxMGcsnWWIfkft2YrxvcnzrxKspjij1bWpH2RmN4zAVMLhU1FQRb_AfQ1WiVbcwsBOzMHPHVc9LwgSIyLTbjI0mxltCImm3CwUqpOH7zOz5Lhn8TE_k7Qp5k6nX3NGTvoe2tmM1gfEdiAFWsrualtfWkDh6P4yUbRkxTWWNOcNVRMgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۳۴ هزار واحدی به ۵ میلیون و ۷۵ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/453322" target="_blank">📅 12:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453321">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1779427bf8.mp4?token=gl1ZyyotOPB5IVyCU4DWSt7ttn448svGoEaz_W6XQ13XNDdfXBYY6yHn8iCLcL2QAd7Q9pH6ccQw_GdD7JZ2fX91_jFQ6ZjMafTXF65pbYBoR_AcO15OLfdpEr30JiNJtJz6CpHXuSHz7mLtThlpWSKvr6OTpGIQiHRMuTk2AcBzt8aqm8a8XC8lviQhvpbuEX1CYe8twbASWo18nGvwcSs0wUKKYSEgtfqcauog9_m7gN2G1NLJdmM7FumTKTMB5J3Msu2dUh5ozRPxsqDH5q7lTjFwYgMVu3hmcYz-064TPmAWt-ySW8Q1lVv5oG-BoZslERcRuO5sBsy2GCOBe4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1779427bf8.mp4?token=gl1ZyyotOPB5IVyCU4DWSt7ttn448svGoEaz_W6XQ13XNDdfXBYY6yHn8iCLcL2QAd7Q9pH6ccQw_GdD7JZ2fX91_jFQ6ZjMafTXF65pbYBoR_AcO15OLfdpEr30JiNJtJz6CpHXuSHz7mLtThlpWSKvr6OTpGIQiHRMuTk2AcBzt8aqm8a8XC8lviQhvpbuEX1CYe8twbASWo18nGvwcSs0wUKKYSEgtfqcauog9_m7gN2G1NLJdmM7FumTKTMB5J3Msu2dUh5ozRPxsqDH5q7lTjFwYgMVu3hmcYz-064TPmAWt-ySW8Q1lVv5oG-BoZslERcRuO5sBsy2GCOBe4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موکب امام رضا(ع) در منذریه، نماد پیوند ایران و عراق
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/453321" target="_blank">📅 12:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453320">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrAfIjX_u3l1EGY36HJkSFGIp_BmNlisW-NnH6nqtQJ-tAsvpPoidNzB-Flh26h-qrTvhKQ92a3B5lY8qaNwJTDOqX4eer5ctLAnj3-DB4NJPuzSN1d0HsAxsyVwbcC_IYcjRdTqRnUeBSHgh5C_C3aNTBGgAiNIyZmyrSDOMawW9slv_bfUNR4TplmzkdEaXqD8NKdHZoYVLT-fLZt61cxSTBcccqmxmmzgoUBUrJuZoo3j6i6UD3qAJV9yQMFMpHMhZ7hQg2TArAufrBe8_RkNqpxC9CqSnMM7ASQbdVD9oDP9-G7s0VXvOLEgSogxFxrjO7esPHgNqjguPg58Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرهایی از احتمال لغو سفر نخست‌وزیر عراق به عربستان
🔹
ساعاتی پس از حمله آمریکا و عربستان به اهدافی در عراق، برخی منابع خبری از احتمال لغو سفر نخست وزیر عراق به عربستان سعودی خبر دادند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/453320" target="_blank">📅 12:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453319">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/503170d8f4.mp4?token=b4tOunawKW7qqAjr5U2PxBoWQyCQCp1Dq42nUXo3fTl4BFsex9IKGYdribUN9AOi_zrIdEfhmerbpSYWtN7nH7NLd-p5D4mg-xlbXIVwrGZ-5QR_e4BfV_hrRaauHxMThndnGqDVoux5txzZqgaoYiV-jLsfEZ07YZS4A93jW7pqOMQ4Yri5E3FYUF5qOsU95ArxvJRiWDTjRdlm0-Nd-Oq4IMpIKY6LGxsKxOLnvChH9grOwUg-RRvL0u7XvPjlmkrAbs5Yun0SgSHBcO5LgSVMRxTofGesVBR3IGPAWrKZkmJOj16ekxQi5uARh0Gfl8kWPyaZIkzmsJtv9ImxKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/503170d8f4.mp4?token=b4tOunawKW7qqAjr5U2PxBoWQyCQCp1Dq42nUXo3fTl4BFsex9IKGYdribUN9AOi_zrIdEfhmerbpSYWtN7nH7NLd-p5D4mg-xlbXIVwrGZ-5QR_e4BfV_hrRaauHxMThndnGqDVoux5txzZqgaoYiV-jLsfEZ07YZS4A93jW7pqOMQ4Yri5E3FYUF5qOsU95ArxvJRiWDTjRdlm0-Nd-Oq4IMpIKY6LGxsKxOLnvChH9grOwUg-RRvL0u7XvPjlmkrAbs5Yun0SgSHBcO5LgSVMRxTofGesVBR3IGPAWrKZkmJOj16ekxQi5uARh0Gfl8kWPyaZIkzmsJtv9ImxKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس ستاد اربعین: ثبت‌نام زائران از مرز ۲.۴ میلیون نفر عبور کرد
🔹
استان تهران در صدر جدول ثبت‌نام‌ها قرار دارد. خراسان رضوی و اصفهان در رتبه‌های بعدی هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/453319" target="_blank">📅 11:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453318">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1c9ec4b6.mp4?token=OK6wO8vS7gjS6GdZMm5ThozC_n2sgq2C6jW2GwXWh97DRQHyRbE6TZDCBJvsau8e9G2PGsi2V6Xx63IxbZNm4yHFUFxn3G4UqkKNd7e4Fz3bpJlcu-CTvWWDDU0S62GT7rTnwlWCLfMnTvUeZw7hen1_owm5AuACUoyGtH5Z5eNNpTJL4nXMvP2rEAKT33v7JU9sy6XiUAZAP0yFQv2xMGhgSk44Sx-SvSl8hgAI-mA0YutWDvaZew7v5Lhyc0-VzqW60XM5-Tp1YDyL05tULPN17zMvFUV1O6uqfOh7eWBR5eDuoB0FKwOxYUc5vr-FItYDUqv6x-NmcUQJOkO5Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1c9ec4b6.mp4?token=OK6wO8vS7gjS6GdZMm5ThozC_n2sgq2C6jW2GwXWh97DRQHyRbE6TZDCBJvsau8e9G2PGsi2V6Xx63IxbZNm4yHFUFxn3G4UqkKNd7e4Fz3bpJlcu-CTvWWDDU0S62GT7rTnwlWCLfMnTvUeZw7hen1_owm5AuACUoyGtH5Z5eNNpTJL4nXMvP2rEAKT33v7JU9sy6XiUAZAP0yFQv2xMGhgSk44Sx-SvSl8hgAI-mA0YutWDvaZew7v5Lhyc0-VzqW60XM5-Tp1YDyL05tULPN17zMvFUV1O6uqfOh7eWBR5eDuoB0FKwOxYUc5vr-FItYDUqv6x-NmcUQJOkO5Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روسیه: ۲ کشتی اوکراینی را هدف قرار دادیم
🔹
وزارت دفاع روسیه: دست‌کم ۲ شناور اوکراینی، از جمله یک کشتی حامل محمولهٔ نظامی را در دریای سیاه و یک شناور دیگر را در بندر میکولائیف هدف قرار دادیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/453318" target="_blank">📅 11:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453317">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huznrgHXzlLbt8ymwGTFNqyBH18j_eUPseD92_GYfJ-0qA5WHU-iajhxqaqrHKvjr0qSZg2fXHqPkLpDhZRnNE1eduKUt8hjKoWP63DupMGdzi2hdFxcnawPYZlPdl07kSsX6aGXbuXnJTW0BdjO_2W-8amysAr67mppBiFV2KoSGx7SGMiX0ZkTNCZ2IFv7XXJYY-XqS4JFTjdJ3b8vOJhPbHbiHj3ZalRIIP0aocB_Kej_m4E9fG_NOf_tBxDPvuaoNfi8LWxX63Y0TU5pSdHyqhIhGbQHcmSzTWgk7lQAPFYJCQVju9tSRwUbX-KCiLLtY4x4evgw2XQC2koegw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان «فارس ‌من» ۲۰ میلیونی شدند
🔹
سامانۀ «فارس ‌من» در هشتمین سال فعالیت خود، با عبور تعداد حامیان از مرز ۲۰ میلیون نفر، رکورد تازه‌ای در حوزۀ مطالبه‌گری مردمی به ثبت رساند.
🔹
این سامانه اکنون با بیش از ۷ میلیون و ۲۱۰ هزار عضو، به بستری برای طرح دغدغه‌ها، پیگیری مشکلات و رساندن صدای مردم به مسئولان تبدیل شده است.
🔹
تاکنون ۱۴۹ هزار و ۲۶۷ پویش مردمی در فارس ‌من ثبت شده و بیش از ۶۵۰۹ مطالبه نیز در مسیر پیگیری مستمر قرار گرفته است.
@Farsnews_My
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/453317" target="_blank">📅 11:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453315">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqopX-1EXbEG3iNAi7GrJbTMYSsTA29cH5da9lZLAczJWDCfP_Z2KAuoK7rMKSoEu1c_qNjU_iOmU2i8hIfEpaHcZHwogJQ5qB-In7f3Aa62SAvqMpznm6R_PKHmqPnROhzF-ngeqJ_qa1zmqBvA-gB15z-SCoirIqmKBL2C_biLKb2YyAN1xsvbpKcHfYMk3odW5s5HzCIPbgzuRfrX8SUTWyK89mOuniZlVrwiRFNsCb__Twsmpm-k_stAPPi9mdiVkga4IXpgajEQSGqFCBb7iRuF7wH23ZhYF-droXoxNzGzSj-wx3hwWvNLjBlRiPPXT7jzsn82un05q_rG-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهمیه‌های دهک‌محور؛ گام بعدی اصلاح کنکور
🔹
«نوجوانی که در خانواده‌ای کم‌برخوردار بزرگ می‌شود، اگر امیدی به رسیدن به دانشگاه نداشته باشد، مسیر پیشرفت را زودتر رها می‌کند»؛ این موضوعی است که دبیر ستاد تعلیم و تربیت شورای‌عالی انقلاب فرهنگی آن را یکی از چالش‌های جدی عدالت آموزشی می‌داند.
🔹
از همین رو، دبیر شورای‌عالی انقلاب فرهنگی پیشنهاد داده سهمیه‌های کنکور بر پایۀ دهک اقتصادی و نیازهای استانی بازطراحی شود تا فرصت‌های آموزشی بیش از گذشته به‌سمت مناطق و اقشار کم‌برخوردار هدایت شود.
🔹
این پیشنهاد در حالی مطرح می‌شود که سیاست‌های جدید سنجش و پذیرش دانشجو از سال ۱۴۰۳ وارد مرحله بازنگری شد و در نهایت مقرر شد در کنکور ۱۴۰۵، سابقه تحصیلی پایه‌های یازدهم و دوازدهم مبنای اصلی ارزیابی داوطلبان باشد.
🔹
به گفتۀ مسئولان شورای‌عالی انقلاب فرهنگی، اجرای این اصلاحات تاکنون نتایجی به‌همراه داشته و سهم دهک‌های بالای اقتصادی از قبولی‌های کنکور از ۸۲ به ۵۶ درصد کاهش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/453315" target="_blank">📅 10:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453314">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFNN16bO0pCBHR-CCnPj8AI0HipuQAS-7fQtwX0qsVAEktD3eZL1UehwRqqNeriLUQ20P4KqqRQKvw8T62b9Us2tDQGQYhdnRASerdnv42qNxbRCNbrpsS5J4UHokhPwmIH5_BwU8FQHzqgBzqJZbVhb1gj_52mIlpplOn0rqWZDbjAAa4tKmY4wbOgjnQDpPCWauqmLoUQF6LTvre15eQ8CTeRvs-XYC9PEPDzagQCnY3mUGZUUwYpZZpNIsMtsdgjSArPctbesjm0CAvdXcaJNQOnheGuAASexg6pnVvxfwog7DXVijyB9RaPBYt7dtP4li-gsmNKDKvzscHMK-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
افتتاح پروژه‌های ارتباطی ایرانسل در کرمانشاه
🔸
ایرانسل با افتتاح دو پروژه ارتباطی در حضور وزیر ارتباطات، شامل سایت 5G و سایت ارتباطی روستایی در استان کرمانشاه، گام دیگری در توسعه زیرساخت‌های ارتباطی کشور برداشت.
🔸
این مراسم، ۶ مردادماه ۱۴۰۵، با حضور وزیر ارتباطات، استاندار کرمانشاه، نماینده ولی فقیه در استان، رگولاتور ارتباطات، مدیرعامل زیرساخت، معاون حقوقی وزیر ارتباطات، نماینده مردم اورامانات در مجلس، مدیران استانی و مدیران ایرانسل، در قالب جلسه شورای اداری استان کرمانشاه، در محل استانداری برگزار شد.
🔸
پروژه‌های افتتاح‌شده ایرانسل در استان کرمانشاه، شامل راه‌اندازی سایت نسل پنجم در شهر کرمانشاه و بهره‌برداری از یک سایت ارتباطی برای پوشش دو روستای خان‌جمال پناهی و خان‌جمال زمانی در بخش مرکزی شهرستان سنقر است.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/453314" target="_blank">📅 10:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453313">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clQ3QgvebSZ_rPLkH-dk3euSTn3mk5os-ZgoWONC4uo8zJvxNqhIvJuOzfy635Tw6oP9VdLnI75ofCtNNR6nkXo4p7Y3j-Qxc6lSQw5FF2r6_1B3cBfdDyIK-qIdAb6Jvd2WyJxNmn-2lsFFlpPUypA4d2_YjjMp-P66i14DpEC_8F9B_JJABxrQZAiqX1dvKQIjLfPkeFHYXgKiAO4XggpfDgrviRNP7iPMaxv6q_fmU9wVl0Oe_FM04ul1tiKbkNf_C4PcjOGHz2u3fgG6CrkSM03XcXN6HrxGDm1jVHAPvc5r08wR-rXrDqb-xhdojRlguBG5H_OCgUtc266YXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
📱
۷ روش قانونی رفع سوء‌اثر از چک برگشتی
‌
✔️
با استفاده از این روش‌ها چک خود را از وضعیت برگشتی خارج کنید.
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/453313" target="_blank">📅 10:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453312">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/453312" target="_blank">📅 10:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453311">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvWJhAxWuyJaw61AAVdLHt_LlkTxd9Suyd5ziHMY_NbwxTQjK3Dje6nLHri7AYai-NkopLnsBsVUrqOfLM6w_yjyQFSJXlggQkJdbjcgaL064X6Br99PPtuhPJ8QC3P1L_3sElyQfEFwZVL4T-YinsCfZ__bdkNGPW65m7BMNkHwH1Q2Or4UBABmWsO0MjIvVJnmhpTkX_5mIJ9M9nqn8KNzWnmJkF4LMy2owSk6da7vYDVW33Nkq9r_ptuO93kz7WIRA047QB4JoT-pfsG84AhWJlj7lzn6IKu1eGxKAvk-o8jWrcET4uaRgIp_72wSKw-gra5dYgdqV-M8_JTspg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود پیکر خلبان قهرمان سوخو ۲۴ به تهران
🔹
پیکر شهید‌ خلبان مجید کاظمی، صبح امروز وارد پایگاه هوایی شهید لشگری در تهران شد و مورد استقبال فرماندهان و کارکنان نیروی هوایی ارتش قرار گرفت.
🔹
پیکر شهید به‌منظور برگزاری مراسم تشییع و تدفین، به پایگاه شهید دوران…</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/453311" target="_blank">📅 10:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453310">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار خوزستان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abbd5ecb77.mp4?token=RUyKkBwLpdj39n7r2lAETazdsodFoBlL4NwjnsI3pJVgynVjPRO2E30pV__cRzhY7e_FvMiBm7HdUmGXASK1jqgpvo6Ht2K2vGlqiU4hWwxvNvYWHm_ZzAnhoHKS8-uZdASuKbqzl8727gl1JK3LGxLnOS5yiDBc3uqheVV8SLFkSxoIWl0Z-hkiIsmk4z0h3ZD8R2cZaTwOriAl8l9cT7AsCdqPPnUY8edLgEIEiEdXCXB0CtUv0EA5tiZZwZIxl-r5dP7QN-fvCTD15U26rtc7KYyEj0RgYBFeMc5M_jEQD1SqW2hFc-CK-RcQYyDbMvrnlZy3qP1vfmdblZTakTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abbd5ecb77.mp4?token=RUyKkBwLpdj39n7r2lAETazdsodFoBlL4NwjnsI3pJVgynVjPRO2E30pV__cRzhY7e_FvMiBm7HdUmGXASK1jqgpvo6Ht2K2vGlqiU4hWwxvNvYWHm_ZzAnhoHKS8-uZdASuKbqzl8727gl1JK3LGxLnOS5yiDBc3uqheVV8SLFkSxoIWl0Z-hkiIsmk4z0h3ZD8R2cZaTwOriAl8l9cT7AsCdqPPnUY8edLgEIEiEdXCXB0CtUv0EA5tiZZwZIxl-r5dP7QN-fvCTD15U26rtc7KYyEj0RgYBFeMc5M_jEQD1SqW2hFc-CK-RcQYyDbMvrnlZy3qP1vfmdblZTakTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عاشقان اباعبدالله با پای پیاده رهسپارند
@KhuzestanFars
-
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/453310" target="_blank">📅 10:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453309">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">افزایش شمار شهدای الحشدالشعبی به ۱۰ نفر
🔹
الحشدالشعبی اعلام کرد شمار شهدای ناشی از تجاوز سعودی-آمریکایی به استان نینوا به ۱۰ شهید و ۶ زخمی افزایش یافته است.  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/453309" target="_blank">📅 10:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453308">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پروژۀ‌ سه‌ضلعی آمریکا و اسرائیل برای ادامۀ جنگ
🔹
اظهارات اخیر نتانیاهو دربارۀ‌ نقش «عده‌ای در داخل ایران» در دور کردن کشور از تفاهم، درحالی مطرح می‌شود که خودِ او و آمریکا، پیش‌تر بزرگ‌ترین نقض‌کنندگان توافقات گذشته بوده‌اند. تحلیل‌گران معتقدند این سخن، تنها یک اتهام‌زنی ساده نیست، بلکه حلقۀ اول از یک پروژهۀ سه‌ضلعی برای ایجاد دوگانگی، آشوب داخلی و در نهایت تحمیل «سازشِ ذلیلانه» به ایران است.
🔹
نظرسنجی‌های معتبر نیز نشان می‌دهد که بیش از ۷۰ درصد مردم ایران به مذاکره با آمریکا بی‌اعتمادند و تنها یک درصد خواهان کوتاه‌آمدن در برابر خواسته‌های واشنگتن تحت هر شرایطی هستند.
نتانیاهو و نقض‌عهد تاریخی آمریکا و اسرائیل
🔹
نخست‌وزیر رژیم صهیونیستی، دیشب در اظهاراتی که به سرعت بازتاب گسترده‌ای یافت، مدعی شد: «هر موقع که ایران به تفاهم نزدیک می‌شود، عده‌ای در داخل ایران کارهایی انجام می‌دهند که ما را از تفاهم دور کند.»
🔹
این ادعا درحالی مطرح می‌شود که خودِ نتانیاهو، ساعاتی پس از حصول تفاهمات قبلی، با حمله به لبنان، اولین و آشکارترین نقض‌کننده‌ آن توافق بود. اما نکته‌ مهم‌تر این است که در ادامه‌ همان تفاهم، آمریکا نیز همه‌ بندهای آن را بدون استثنا نقض کرد.
🔹
با این سابقۀ‌ روشن، این پرسش مطرح می‌شود که چرا نتانیاهو امروز نقش «نصیحت‌گر» را بازی می‌کند؟ پاسخ را باید در یک پروژه‌ ترکیبیِ سه‌ضلعی جست که آمریکا و اسرائیل برای تحقق اهدافشان علیه ایران طراحی کرده‌اند.
🔹
پیش از هر چیز، باید با صراحت تأکید کرد که هیچ‌کس در ایران خواهان جنگ و خونریزی نیست. همۀ ما نسبت به کشتار، ویرانی و رنج‌های ناشی از جنگ حساسیم. جنگ، نگرانی‌ها و هزینه‌های بی‌شماری به‌همراه دارد که هیچ‌کس به‌سادگی از آن سخن نمی‌گوید.
🔹
اما سؤال اساسی اینجاست: آیا آمریکا و اسرائیل برای ایران چاره‌ای غیر از مقاومت باقی گذاشته‌اند؟ آیا اگر امروز در برابر زیاده‌خواهی‌های آنها کرنش کنیم، دست از طمع برمی‌دارند؟ تجربه‌ تاریخی به ما می‌گوید که تنها راهِ جلوگیری از نابودی ایران، «مقاومتِ عزتمندانه» است؛ چرا که طرف مقابل، می‌خواهد تا آنچه را در میدان جنگ نتوانسته به‌دست آورد، بر سر سفرۀ مذاکره و همزمان زمینه‌چینی برای حملۀ مجدد به چنگ آورد.
سه رکن پروژۀ‌ دشمن؛ از دوگانه‌سازی تا آشوب و حمله
🔹
رکن اول؛ سخن نتانیاهو، مقدمه‌چینی برای اختلاف افکنی
🔹
نتانیاهو با این جمله، در حال القای این گزاره‌ روانی است که «مشکل اصلی بر سر راه توافق، نه اقدامات خودِ آمریکا و اسرائیل، که مخالفان داخلی ایران هستند.» هدف این ادعا، توجیه نقض عهدهای بعدی توسط آمریکا و اسرائیل و معکوس‌سازی واقعیت است تا افکار عمومی ایران به اشتباه بیفتند که «اگر توافق حاصل نمی‌شود، تقصیر خودِ ماست!»
🔹
رکن دوم؛ دوگانۀ دروغین «جنگ یا صلح»؛ ابزار ایجاد دوگانگی و آشوب
🔹
هم‌زمان با این فضاسازی، برخی سیاسیون خاص و سلبریتی‌های پروژه‌بگیر که همواره در طول سال‌های گذشته – حتی در دوران کاملاً آرام و بدون جنگ – مشغول ترویج گفتمانِ «سازش با آمریکا» بوده‌اند، امروز نیز با همان نسخه‌ تکراری به میدان آمده‌اند. آنها با تولید ادبیات دوگانه‌ای تحت عنوان «جنگ» در برابر «صلح»، در حال تحریف «مقاومت» به «جنگ‌طلبی» هستند.
🔹
اما هدف نهایی از این دوگانه‌سازی چیست؟
🔹
پاسخ را باید در سناریوی طراحانِ این پروژه جست: ایجاد دو دستگیِ عمیق در داخل کشور، به گونه‌ای که بخشی از جامعه را در مقابل بخش دیگر قرار دهند. این دوگانه‌سازی، مقدمه‌ای برای شعله‌ور کردن آشوب‌های خیابانی است. چرا که تجربه نشان داده، هرگاه اختلافات داخلی به اوج می‌رسد، بستر برای نفوذ و اقدامات تخریبی دشمن فراهم می‌شود.
🔹
و اما حلقۀ‌ نهایی این پروژه: پس از ایجاد آشوب و هرج‌ومرج داخلی، آمریکا و اسرائیل بلافاصله دست به حملۀ نظامی خواهند زد؛ چون در آن شرایط، ایرانِ درگیرِ بحرانِ داخلی، کمترین توانایی را برای پاسخ‌دهی منسجم خواهد داشت. این دقیقاً همان سناریویی است که پیش‌تر در کشورهای منطقه (از لیبی تا سوریه) با موفقیت نسبی اجرا شده و اکنون طراحان آن، به دنبال پیاده‌سازی نسخه‌ به‌روز شده‌ آن در ایران هستند.
🔹
سؤال کلیدی که مبلغانِ این دوگانه هرگز پاسخ نمی‌دهند این است: «طرف دیگرِ این جنگِ ساختگی، دقیقاً چیست؟ آیا منظورتان از صلح، همان «کرنشِ بی‌قید و شرط» در برابر زیاده‌خواهی‌های آمریکاست؟» چرا که اگر شفاف بگویند «صلحِ مدنظر ما» به معنای پذیرشِ زنجیره‌ای از ذلت‌هاست (تعطیلی هسته‌ای، خلع‌سلاح موشکی، واگذاری نفوذ منطقه‌ای و نهایتاً تجزیه‌ی ایران)، نقاب از چهره‌ی پروژه‌شان می‌افتد.
🔹
رکن سوم؛ جریان آمارسازی‌های دروغین؛ مهندسیِ احساس ناچاری
🔹
اما مهم‌ترین و خطرناک‌ترین ضلع این پروژه، جریان پنهان آمارسازی‌های دروغین است. برخی افراد با صبغه و سابقه‌ی بدنام امنیتی که این روزها در حال مشاوره و تصمیم‌سازی برای دولت هستند، با تولید گزارش‌های جهت‌دار و غیرواقعی، تلاش می‌کنند این گزاره را به مسئولین کشور بقبولانند که «جامعه‌ ایران خسته شده و چاره‌ای جز پذیرشِ هر آنچه آمریکا تحمیل می‌کند، ندارد!»
🔹
این جریان با دستکاریِ اعداد و ارقام و ارائه‌ تصویری بزرگنمایی‌شده، در واقع مهندسیِ «احساس ناچاری» را دنبال می‌کند. هدف نهایی این پروژه، تصمیم‌سازی به نفعِ «سازشِ ذلیلانه» در بالاترین سطوح تصمیم‌گیری کشور است، تا ایران را به سمتی سوق دهند که با پای خود، ابزارهای دفاعی‌اش را زمین بگذارد و سپس دانسته یا نادانسته شاهد تجزیه‌ی تدریجی کشور باشد.
🔹
به نظر می رسد در کنار هوشیاری مردم؛ مسئولان امنیتی و قضایی نیز باید با رصد دقیقتر عوامل داخلی دشمن مانع از پیشبرد گام به گام این سناریو باشند.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/453308" target="_blank">📅 10:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453307">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rH3c6wLoBK1Kk_89iv02zqwg5FFREYIbWT69bvoUaI51JXDv0ZdSF3uktpVvCuIkxQ_00s12ovU_Axs9q-c_SKTjoIUxBXFOs32kCtaqa2LbJCFP_Cmf_Cf2QelP2Ju_TQXNvzdkRYYTlUTuzeC3LaT70Cc5WmM283BmX98pA4UYujyBitMSHAKOTvrlN1Vg1-PY9dLm7v8xqwpEm02RmVXMUBk-LtLFVq4UvRFrF64nlk_XlPDojePytGe96WP_tZSz35F3Q6aJADDu1VrbVAXBhpcovXyJzV4EPLOibwTC1Co1e4OAWGTYsONnnLXDFOqouBa2xiYlc0eNd2tdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بسیج سازندگی: گروه‌های جهادی ۳۶ هزار واحد مسکونی آسیب‌دیده از جنگ را بازسازی کرده‌اند
🔹
بیشترین حجم بازسازی در تهران، اصفهان و قم انجام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/453307" target="_blank">📅 10:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453303">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZL9yWIibNpKsGOgnaDbk2aOGTXOPh_al8-bN1I9tyfJumf685cVzyQ8avFWFMLEK6KCLIYABzHTaPf3fXIHaT_6Hkqse77cz3q57IaktHLyeEazi8ZL51xGqFx5cOu0H2Wr9Xb5f15fMWgQrO23yC672xfu2zJCCUXD7VcECr5EH-ynstrdmMvR3erVfqiI0yyzi3PQo54DSJ3eSHj8lEuBIIw5HiJs96VpSr6TQs5EqzCrPWwwuo6FLOvJQlsphLPNvwOD8gpQ6lgigy94i9NXLLZrfba3oOc0OXOqgrMwBIvaGIjOccvqxNKzsy_xcP270refD_Lkglzhpk5aJaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احراز شهادت یکی از قهرمانان سوخو۲۴ ارتش
🔹
شهادت امیر سرتیپ‌دوم مجید کاظمی، خلبان یکی از جنگنده‌های سوخو۲۴ ایرانی که اسفندماه پارسال خسارات سنگینی به پایگاه العدید آمریکا در کشور قطر وارد کردند، با آزمایش‌های تخصصی و بررسی DNA محرز شد و پیکر مطهرش تا ساعاتی…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/453303" target="_blank">📅 10:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453302">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shc7Gg0hnBaAyLWDDqB7J6ctIAD6huYCYVu93yESqtPNilCOJRLOiqNEtDcoC5uP7Q53ouhQ1vHQhVDq3STVBs9PrafIpXIZQg06wjdE5WVMPYS7gcH6d2J6_oJmGN-0bEBppuzP2ULp7DqdPFUeKC6HoIxzXkNaUGjQr9EK1w_wKv85aSrA75R2pZ__fuwIaD2H6nJx7p4sBTw0fyI6UTrk6NfRCfL3bE2ocj-9JCnP58uhVLcXilz0dpb5zwjezCC2pvCQ_NR7i3yDsojkp5Zs5K5i89y6CPyERR4I3BMF1OmgPTsah-2l4NMqBIoNDHg24T3rL9m-0vgHvcZWbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی‌دلیگانی: طرح مقابله با اقدام انگلیس علیه سپاه تقدیم هیئت‌رئیسۀ مجلس شد
🔹
نایب‌رئیس کمیسیون اصل ۹۰ مجلس: براساس این طرح، دولت موظف است از تمامی اشخاص حقیقی و حقوقی که با سپاه همکاری دارند و از این بابت در معرض آسیب قرار می‌گیرند، با تشخیص دستگاه‌های مربوطه حمایت‌های حقوقی و مقتضی را به عمل آورد.
🔹
در این طرح آمده هرگونه کمک نظامی یا اطلاعاتی نیروها برای مقابله با سپاه و ایران، همکاری در اقدام تروریستی محسوب شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/453302" target="_blank">📅 10:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453301">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e625192b4.mp4?token=FLevlp0MObISNiHBiQmtuJ7E1mWmJ4n1weh-cUBU_RQ7pydjM4TeFj3-aPwdSLNYKb3XLk4dYjvZ1xmHHXUops2EuD4wyeyl_Teyt7JZavXSK1MqJwmYhCm_pTsanT8ToSMGcz38w4kl7BzfkdX1NZrtzZQS_QftzmEQTQk0rT16UEKNFTRoHaw_VgJXfpC_dkiEmMT800VtXlnSjcnowUaFC8bz3xpW3k9bmGAPq85RCFkMva5TMNkEFN8fZLfz-DbsZti6pIkY3Eb-q6id_nI8PQMGQLSy1hjfDMIcwaPgyX5tK7pYdTzLNBGYuNELs0gNRQ643uNgGYCofEwCjliMXDz3XLfWVeInBhqgR5BZn7Cf1bXptmqM3vlLAcFEag7UlL5ngeO9AwYa18mT18JU_Qy7jY6O1KBYUSoBFq-27rJS7k5h_ry4_7CM-cb_hsha8AImC6wyoYJsoCWuCyqdJWtzr_6PGaZhwTFFmK_ljC6N5NwbovFXBUsgAejjGLSAAM42MgaWDrzCBLcnGp3tpQRVTtONmFCbPgYSufg2FZVBX0ucypRcVJIYdg_RSB6vqyP_WXKQOUefhcckE3TPt2LNjrX2eSNUNsN7F3QxZk9_D81V5a9QavqKdlmiGxmll5ZsUKMsE_pd20GkXcEfFbioXQNtmtXBlZmY3SE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e625192b4.mp4?token=FLevlp0MObISNiHBiQmtuJ7E1mWmJ4n1weh-cUBU_RQ7pydjM4TeFj3-aPwdSLNYKb3XLk4dYjvZ1xmHHXUops2EuD4wyeyl_Teyt7JZavXSK1MqJwmYhCm_pTsanT8ToSMGcz38w4kl7BzfkdX1NZrtzZQS_QftzmEQTQk0rT16UEKNFTRoHaw_VgJXfpC_dkiEmMT800VtXlnSjcnowUaFC8bz3xpW3k9bmGAPq85RCFkMva5TMNkEFN8fZLfz-DbsZti6pIkY3Eb-q6id_nI8PQMGQLSy1hjfDMIcwaPgyX5tK7pYdTzLNBGYuNELs0gNRQ643uNgGYCofEwCjliMXDz3XLfWVeInBhqgR5BZn7Cf1bXptmqM3vlLAcFEag7UlL5ngeO9AwYa18mT18JU_Qy7jY6O1KBYUSoBFq-27rJS7k5h_ry4_7CM-cb_hsha8AImC6wyoYJsoCWuCyqdJWtzr_6PGaZhwTFFmK_ljC6N5NwbovFXBUsgAejjGLSAAM42MgaWDrzCBLcnGp3tpQRVTtONmFCbPgYSufg2FZVBX0ucypRcVJIYdg_RSB6vqyP_WXKQOUefhcckE3TPt2LNjrX2eSNUNsN7F3QxZk9_D81V5a9QavqKdlmiGxmll5ZsUKMsE_pd20GkXcEfFbioXQNtmtXBlZmY3SE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعری که رهبر شهید با تولد اولین نوزاد رویان خواندند  @FarsnaTech - Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/453301" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453300">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwHoLVq5I1lP00mue0PN_2vQ54CD4G_kHaOIVm2NLuTKntHm9cmk9MJ4CeoE7U_mu_41Q8e1QsSj0l9RBO_nn6NFfccf0Pp2SmGDugvgBosQkQcegLhLhMUs4PwV2cjBXvARiFhI0YEyOtnIXe7o28YrAFyjTzNhZSrhPOdZn5GL8WmSYXNn48-6w51eRqMq9NKas8E-3rWFnyYXZbSBSsshfzTvAvHPc8p__pRTOT7IbSypJHlIEyOW36yd3utL8fU6ZWKiUD5SZ3n_LDe7VapCLTUghCwsVRTDN_RavKMFIec0UdCM_5nuXpOHRS63zHSWlvc3W-lsUmG0Y02oXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حشدالشعبی: حملۀ تروریستی آمریکا و عربستان نقض حاکمیت ملی عراق بود
🔹
حشدالشعبی عراق در بیانیه‌ای حملۀ تروریستی آمریکا و عربستان سعودی به نقاطی در خاک عراق را نقض آشکار و فاحش حاکمیت ملی عراق توصیف کرد.
🔹
بر اساس اعلام فرماندهی عملیات حشدالشعبی در استان نینوا،…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/453300" target="_blank">📅 09:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453299">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDUYfl2YsR1NrUrc2ShqRkcPVGNhPHMfKkmtBuDGU1uNkx2wC8KVA9lSeZmWZN-0LSB0pCrHRsvP-KBYtq6WZ03LDjV0Z4zxWbwofByaNcFUyxeJ3IbNPaaDqIyqYoYL_wyShV7zq-ovdwzX92YtufN10meqoYn7ca7atmX83y6BMpFePM1MXM8hrN3acN8fXBNVpfEPzqK7gt9r5mJ3ueylkXVr-72JAp-5Apgkrj4QUkBHuGq8lKEeCggrsaGeVl3sHFuHif8DF8POzQ85RIQRSdb9GoRLPKcAi4mCGHs4AZM-32pj-REUnfWHhFGRRGgDja9xdZ767zbN27hXdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز حفاری خط  ۹ مترو در شهریور
🔹
نخستین قطعۀ خط ۹ متروی تهران تا سال ۱۴۰۸ به بهره‌برداری می‌رسد، مجری خط ۹ مترو می‌گوید حفاری این خط از شهریور آغاز می‌شود.
🔹
ساخت خط ۹ مترو، با ۵۳ کیلومتر طول و ۳۷ ایستگاه، با هزینۀ ۲.۴ میلیارد یورو از چند ماه پیش آغاز شده است.
🔹
مدیران شهری می‌گویند که بخش نخست این خط حدود ۱۰ کیلومتر طول دارد و با ۴ ایستگاه، مسیر دولت‌آباد تا تقاطع خط ۴ در محدودۀ نبرد را پوشش می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/453299" target="_blank">📅 09:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453298">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a48f8f6d.mp4?token=QBYJT2SYDmxEqFmNpFw324CI87j_LF8v1yFCUE2EmzkzhUukOocppua2Nub61hfPB7ZrENPJBQbCfJf1qRib-KfuE1uWQV5q3BxHjP-aYrhvcfHQncV8cmFPZhnNLyjraiT_RoFbeqDJoGiByUfGwyEGZ3rqPpT4qhGhpmJ7fiLjNs8WXjT1wicvULj72DVHpbRBtyPWvEKcidPMqYFwpvO2a_gL6Ws3RzMqGHeE6uHyv_v7xZmUfhCfb6fuMEindsTnO-g3nSrcEmj5zPgId7kLMc2CH6qFZ4NqDy6jlPju5JAus1yvyMD5D2P_J8ii7b-zoNzlUOt6YbxOXixwMpoQxrnr4Ud92UK55aRfSHAYjrnLC6bCH-MU0uOCIZoksQ4Hv1afuqhBr-g0k2VwNG7phNe2YuqMkUQYHQ_WyB6CcuKKryauam_I2OaPj_nXKxDflgLS3P6U15S0b049jqpApkJ9ViZJ_lxRBejx_sgjGc3-eAKb990iTwEfoNbWdLQqbPSdp1SiVWIjRd3Wy8RKsTu038trRU6OE3DQP17oxYXLFkCE5XM3tKH60iI4dduCNG79grwtotQN-ZoQtanb5gENFyWQoesTQcEBwTinnDCIbuE_nCOUdFg9ws54UlWQfSh_3-xw2uex7OzO7_hKHatGbRBMANrd1qWS034" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a48f8f6d.mp4?token=QBYJT2SYDmxEqFmNpFw324CI87j_LF8v1yFCUE2EmzkzhUukOocppua2Nub61hfPB7ZrENPJBQbCfJf1qRib-KfuE1uWQV5q3BxHjP-aYrhvcfHQncV8cmFPZhnNLyjraiT_RoFbeqDJoGiByUfGwyEGZ3rqPpT4qhGhpmJ7fiLjNs8WXjT1wicvULj72DVHpbRBtyPWvEKcidPMqYFwpvO2a_gL6Ws3RzMqGHeE6uHyv_v7xZmUfhCfb6fuMEindsTnO-g3nSrcEmj5zPgId7kLMc2CH6qFZ4NqDy6jlPju5JAus1yvyMD5D2P_J8ii7b-zoNzlUOt6YbxOXixwMpoQxrnr4Ud92UK55aRfSHAYjrnLC6bCH-MU0uOCIZoksQ4Hv1afuqhBr-g0k2VwNG7phNe2YuqMkUQYHQ_WyB6CcuKKryauam_I2OaPj_nXKxDflgLS3P6U15S0b049jqpApkJ9ViZJ_lxRBejx_sgjGc3-eAKb990iTwEfoNbWdLQqbPSdp1SiVWIjRd3Wy8RKsTu038trRU6OE3DQP17oxYXLFkCE5XM3tKH60iI4dduCNG79grwtotQN-ZoQtanb5gENFyWQoesTQcEBwTinnDCIbuE_nCOUdFg9ws54UlWQfSh_3-xw2uex7OzO7_hKHatGbRBMANrd1qWS034" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعری که رهبر شهید با تولد اولین نوزاد رویان خواندند
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/453298" target="_blank">📅 09:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453297">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎥
غریب‌آبادی: اگر با عمان به تفاهم نرسیم، مسیرمان در مورد تنگه را ادامه می‌دهیم
🔹
اگر به تفاهم برسیم هم بلافاصله تنگه باز نخواهد شد و در داخل کشور تصمیم گرفته می‌شود که چه خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/453297" target="_blank">📅 09:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453296">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdcm0l4XgctWlKYI0o9vhNg9e_R3vL3PAWeRhX9tlsOjuXwVR6pTD9D0eUbSWk6aXfQ1G1w2OZ27v8OQ7U671YRokkxMp6cRvB6aC9hbRJsbt-U6IEyYl2g7bXt0NXshdranilGCID8X0UMRE0TwU4O0yfzLbqWMryuZowCgyW74cyyc5JeFBXMAvdjcUHpnUs93e7erShdAettOOix9tLlFS0KiMMo7N7SNQMbL4RJ5AJJY0Dpk2deDaTNULhNe4trqvpc4yWG3Aw9NBxT21dUnKi4i-agX1WTFUXY3hZWDVaewKltws_TRb-E6Qfq74H955tizd4C7JfNSyoKm8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمی از آمریکایی‌ها خواستار بازداشت نتانیاهو در کشورشان هستند
🔹
در حالی که نخست‌وزیر رژیم صهیونیستی به آمریکا سفر کرده است، نظرسنجی اکونومیست-یوگاو نشان می‌دهد که ۴۹٪ از آمریکایی‌ها معتقدند که ایالات متحده باید نتانیاهو را هنگام ورود به این کشور، بر اساس حکم…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/453296" target="_blank">📅 09:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453294">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc79f76543.mp4?token=fesPa3UhAit0BXoTnqpaCyR9KjXIkB8EfujJXNd4VJELm0x4NwrtWJrT2RlRkbvojkovYwbTIazC-c1La3H5wXlAm_L-cbbI1v_Pa-FhBOsVbdV7cyBTzqR6QjbXk5U_aopGpvXh4Ig8C6uGqnznABNR4QWcVGkDU3IBWKjTVSxbJ3hB4oU5VkKDHLO_0l5rnqZtxM6NsLAiK6NL4YLOhP85zh4ZDhsKjT4MaNVUMnhswpnAk53WmOX0oNqmtMR4XV2Aa56lr-6I20VWfisP8ejn6c_dSOj4J-KmtexI1yYT0Y5MdV5sHNFqJUXJ6Bt9bvlh5yJ3NagINwkUl6oe_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc79f76543.mp4?token=fesPa3UhAit0BXoTnqpaCyR9KjXIkB8EfujJXNd4VJELm0x4NwrtWJrT2RlRkbvojkovYwbTIazC-c1La3H5wXlAm_L-cbbI1v_Pa-FhBOsVbdV7cyBTzqR6QjbXk5U_aopGpvXh4Ig8C6uGqnznABNR4QWcVGkDU3IBWKjTVSxbJ3hB4oU5VkKDHLO_0l5rnqZtxM6NsLAiK6NL4YLOhP85zh4ZDhsKjT4MaNVUMnhswpnAk53WmOX0oNqmtMR4XV2Aa56lr-6I20VWfisP8ejn6c_dSOj4J-KmtexI1yYT0Y5MdV5sHNFqJUXJ6Bt9bvlh5yJ3NagINwkUl6oe_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زلزله در ژاپن با حداقل ۱۳ کشته و ده‌ها زخمی
🔹
نخست‌وزیر ژاپن سانای تاکائیچی اعلام کرد که در زلزله ۷.۱ روز گذشته در استان کوماموتو، حداقل ۱۳ نفر کشته و ده‌ها نفر زخمی شدند.
🔹
این زلزله با قدرت ۷.۱ ریشتر همچنین باعث خسارات گسترده‌ از جمله آتش‌سوزی خانه‌ها و فروریختن پل‌ها شده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/453294" target="_blank">📅 09:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453293">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آغاز پیش‌فروش بلیت قطار برای نیمۀ دوم مرداد
🔹
رجا: فروش غیرحضوری بلیت قطارهای مسافری برای ۱۶ تا ۳۱ مرداد از هم‌اکنون آغاز و تا ساعت ۱۱ صبح ادامه‌دارد و پس‌از آن تا ساعت ۱۳ به‌صورت حضوری در آژانس‌ها انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/453293" target="_blank">📅 08:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453292">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIejrlL5jAKL6Q6aQ8EjMsQOaPQZFGun-utcPGIqiIukCpUhzAOX0rU5-j9xlnM_cbB7gQMlv6fD_w4jV6pdZpZxRgf9_pJ7lzFJa5VnioLB5mWb_qGkF3TlQZKZtvPDqJRvFSKOD61QZkEMKtZwTsLOgs7Dc3io8rikJN7UY2W03YeOKkSd6hf1HBdGVBnRdCll1z9fe54dnfl7jW8pmF73AZdFWvjGTY5b_IEfYRtAIVNOdDZp56xUeo3eisl69UhemPNOEUv0RBSOFWTBKJu6VC_D0ahWCJZE9r8pUNDMn8IYMWVBZezLgVjj3POeh2PPtL3xsm7j9CxRHfuIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشارۀ دیپلمات روس به عقب‌نشینی اوکراین با هشدار ایران
🔹
اولیانوف، نمایندهٔ روسیه در نهادهای بین‌المللی: اظهارات اولیه اوکراین نسبتاً متکبرانه بود؛ اما اکنون تصمیم گرفتند موضع خود را تغییر دهند تا از تشدید بیشتر تنش جلوگیری شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/453292" target="_blank">📅 07:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453291">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حشدالشعبی: حملۀ تروریستی آمریکا و عربستان نقض حاکمیت ملی عراق بود
🔹
حشدالشعبی عراق در بیانیه‌ای حملۀ تروریستی آمریکا و عربستان سعودی به نقاطی در خاک عراق را نقض آشکار و فاحش حاکمیت ملی عراق توصیف کرد.
🔹
بر اساس اعلام فرماندهی عملیات حشدالشعبی در استان نینوا، در پی هدف قرار گرفتن مواضع این نیرو در این استان، ۸ نفر شهید و ۴ نفر دیگر زخمی شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/453291" target="_blank">📅 07:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453290">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: یک پهپاد شناسایی متعلق به دشمن سعودی را سرنگون کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/453290" target="_blank">📅 06:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453289">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcBLCwm3YSjAcZWqJ-QjIl90-0EpZorAIy5Ab9va3xVo8ut6LW2Uj4rDAago0kg6q5XOsl_G-IDzOBjESEWNPP7gOfZCA6A_SJOfVh1Jn0qXHMkCVl1_DPDwDUj4_2ujL87mv0r76bcyoFN8ekBWQkQ0oklvJgRWVzHaP--tDGDP7lqk4yUEPVPVF-NtWN3UgeWQ-6sLwAkKBYM1a1JzPuCpZANagoWY2he8EqjC3fADpJav4-ymeniCM18YbYpBFNjSyArYz-TH5tUyk4ZYKIC_W7C9UkNb7Bc3wUW6hXNlUlAZYbL0bC6h3U445VNcR5LeF8ETvmUtHW_yr1k_eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احراز شهادت یکی از قهرمانان سوخو۲۴ ارتش
🔹
شهادت امیر سرتیپ‌دوم مجید کاظمی، خلبان یکی از جنگنده‌های سوخو۲۴ ایرانی که اسفندماه پارسال خسارات سنگینی به پایگاه العدید آمریکا در کشور قطر وارد کردند، با آزمایش‌های تخصصی و بررسی DNA محرز شد و پیکر مطهرش تا ساعاتی دیگر به کشورمان باز خواهد گشت.
🔸
یازدهم اسفند سال گذشته، دو فروند بمب‌افکن سوخو۲۴ نیروی هوایی ارتش، در عملیاتی پس از عبور از سد سامانه‌های شناسایی پیشرفته و مواضع راداری متعدد دشمنان، اقدام به بمباران پایگاه العدید قطر کردند.
🔸
اما عقاب‌های آسمان ایران، در مسیر بازگشت و بر فراز خلیج فارس مورد حملۀ دشمن قرار گرفتند و تاکنون، تلاش‌ها برای احراز وضعیت خلبانان شجاع این جنگنده‌ها ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farsna/453289" target="_blank">📅 06:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453288">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌ منابع عراقی: دشمن سعودی-آمریکایی مسجد جامع و تصفیه‌خانۀ آب پایگاه شهید ابومنتظر الحمیداوی را هدف قرار داد. @Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/453288" target="_blank">📅 05:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453287">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‌ منابع عراقی از حملۀ دشمن آمریکایی-سعودی به مقر دوم سازمان بدر در استان دیاله خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/453287" target="_blank">📅 05:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453286">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
🔴
سپاه: پایگاه هوایی و مرکز فرماندهی مرکزی ارتش آمریکا در اردن هدف موشک‌های بالستیک قرار گرفت
🔹
در پاسخ به اقدامات تجاوزکارانۀ ارتش کودک‌کش آمریکا، ساعتی پیش رزمندگان شجاع نیروی هوافضای سپاه، پایگاه هوایی و مرکز فرماندهی مرکزی ارتش آمریکا در اردن را با…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/453286" target="_blank">📅 05:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453285">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‌
🔴
منابع محلی از شنیده‌شدن صدای انفجار در جنوب بغداد، پایتخت عراق خبر می‌دهند‌.  @Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/453285" target="_blank">📅 05:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453284">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌‌
🔹
منابع عراقی: گزارش‌های اولیه از شهادت ۷ تن از نیروهای تیپ ۳۰ حشدالشعبی در دشت نینوا حکایت دارد. @Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/453284" target="_blank">📅 05:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453283">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
منابع عربی از اصابت مستقیم موشک‌های ایرانی به پایگاه هوایی «موفق السلطی» اردن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/453283" target="_blank">📅 05:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453282">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎥
تجاوز دشمن آمریکایی-سعودی به پایگاه تیپ ۳۰ حشدالشعبی در استان نینوای عراق  @Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/453282" target="_blank">📅 04:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453281">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
پرواز جنگنده‌های سعودی در آسمان عراق
🔹
منابع عراقی: هواپیماهای جنگی دشمن سعودی-آمریکایی همچنان بر فراز شهرهای کربلا، بابل و نجف در حال پرواز هستند.
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/453281" target="_blank">📅 04:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453280">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c602a52dde.mp4?token=mTZlpZxjxsBqGtrM25hVu8V5uzddytDHSBfiDEh8fitSTpuT8a9vuKM3zXwpHPCesBRM10YthextEjR8R1Cfbs04mOw2wByJzBzfD8rMDHDveqWbw_700S4VRRFESnSS4oHC4f1eIhTVas2JnZcFDBMlL30VDJHFaSmtlKivl6NNHNnNucJshYsIZTu6ekducLwNj8vtpfQa-ww7TQepiYvf9-xNHlhNYwsAsMJIHTrZMihPvb0Y6M-3qh72ESsT3Saf07Mp1W3aE9DUU5t4wgqBrfPGkQfNY7E9734Ljsnd0kVeYkEnt1G55xZuZvv6O0I41CKIcK6Y4dzjzeGaCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c602a52dde.mp4?token=mTZlpZxjxsBqGtrM25hVu8V5uzddytDHSBfiDEh8fitSTpuT8a9vuKM3zXwpHPCesBRM10YthextEjR8R1Cfbs04mOw2wByJzBzfD8rMDHDveqWbw_700S4VRRFESnSS4oHC4f1eIhTVas2JnZcFDBMlL30VDJHFaSmtlKivl6NNHNnNucJshYsIZTu6ekducLwNj8vtpfQa-ww7TQepiYvf9-xNHlhNYwsAsMJIHTrZMihPvb0Y6M-3qh72ESsT3Saf07Mp1W3aE9DUU5t4wgqBrfPGkQfNY7E9734Ljsnd0kVeYkEnt1G55xZuZvv6O0I41CKIcK6Y4dzjzeGaCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
منابع عراقی از حملۀ دشمن آمریکایی-سعودی به یک موکب حسینی در روستای «ابوعصید» در استان کربلای معلی خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/453280" target="_blank">📅 04:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453279">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تکمیلی/ حملات سعودی-آمریکایی به کربلا و نینوی
🔹
منابع عراقی می‌گویند که پایگاه‌های «الحشد الشعبی» در استان‌های کربلا و نینوی نیز هدف حملات سعودی-آمریکایی قرار گرفته‌اند.
🔹
همچنین در کربلا، مواکب و ایستگاه‌های زائران اربعین حسینی هدف تجاوز جنایتکارانه سعودی…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/453279" target="_blank">📅 04:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453278">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f3b38a080.mp4?token=no2sgAUv-ajtlp6fqPMRDFamTnSKit3ny9afJK0DdHyo72a_q6XpRvR94EWBcnPwgepxkPXPGxDAkbAESrl8KFb0DDPgO2rVbTHBPrdfUvktlrRwEEgg-DuBxxFv0Kaooa8JAaAjCX1G1xYPYyVjvfOMlzb1jKbaUmDqGfUf13o3Izx-KBIwbHrjbs8RIFg80fX8Atw1E7__FoSVjTDzvxgfy5yP-WyHNf2Tj7qGRXqrq6HbmtZwigLE5ZhnYHpaSG9WHYRzJfwVt0AFbUeMeTiv65fPyUHjOL2gEX42hNgF9rog9uA3ejeUtzYGkak9NXQQ2meLJAnl6J5vdbczcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f3b38a080.mp4?token=no2sgAUv-ajtlp6fqPMRDFamTnSKit3ny9afJK0DdHyo72a_q6XpRvR94EWBcnPwgepxkPXPGxDAkbAESrl8KFb0DDPgO2rVbTHBPrdfUvktlrRwEEgg-DuBxxFv0Kaooa8JAaAjCX1G1xYPYyVjvfOMlzb1jKbaUmDqGfUf13o3Izx-KBIwbHrjbs8RIFg80fX8Atw1E7__FoSVjTDzvxgfy5yP-WyHNf2Tj7qGRXqrq6HbmtZwigLE5ZhnYHpaSG9WHYRzJfwVt0AFbUeMeTiv65fPyUHjOL2gEX42hNgF9rog9uA3ejeUtzYGkak9NXQQ2meLJAnl6J5vdbczcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکمیلی/
حملات سعودی-آمریکایی به کربلا و نینوی
🔹
منابع عراقی می‌گویند که پایگاه‌های «الحشد الشعبی» در استان‌های کربلا و نینوی نیز هدف حملات سعودی-آمریکایی قرار گرفته‌اند.
🔹
همچنین در کربلا، مواکب و ایستگاه‌های زائران اربعین حسینی هدف تجاوز جنایتکارانه سعودی-آمریکایی قرار گرفتند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/453278" target="_blank">📅 04:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453277">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
رسانه‌های عراقی:
حملات موشکی و توپخانه‌ای موکب‌های حسینی و زائران را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/453277" target="_blank">📅 04:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453276">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌‌
🔴
سازمان تروریستی سنتکام: ما و عربستان حملاتی را علیه گروه‌های وابسته به ایران در عراق انجام دادیم.
🔹
این حملات پاسخی به حملات پهپادی ساعات گذشتۀ سپاه پاسداران بوده است.  @Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/453276" target="_blank">📅 04:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453275">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آمریکا: باهمکاری عربستان حملاتی علیه عراق انجام دادیم
🔹
ارتش تروریست آمریکا تایید کرد که باهمراهی ارتش عربستان سعودی، حملاتی را علیه پایگاه‌های مقاومت در عراق انجام داده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/453275" target="_blank">📅 04:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453274">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyAQfcu9yXuX8agKufc6d1hkSaDmEXnEH7nSbKKqONydKlIN3GFXoVaeGLESOPeHiwwp1135l6qTqJdfjhklTyxgf6M1HOMpjyvlZBJAy-hmeqJueJGAPbZUR8gUQ9rkK2ao9cymOaqN4KNitB_JJM9f2OOeocfAhm93EUmiMvBaC2mj1SjwI7e7DVVfOQ4KEEj9l2yarAiWLpJtFQ-WGpzgblS22wIgx_pkqK1RJdux-U4rm4c5-9bV_ef6RqTtPKSu9r0puFBuYWz-YuhKK00qQQawyag3Y2ajxuct0fNVztxwbUZ9pIfOdJHXY100-ZETowFmQbJK2CUgaX8HDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وقوع انفجار در پایگاه الحشدالشعبی در بصره
🔹
شبکۀ الجزیره به‌نقل از یک منبع امنیتی عراقی گزارش داد که انفجاری در داخل یکی از مقرهای الحشدالشعبی در جنوب عراق رخ داده است. @Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/453274" target="_blank">📅 03:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453273">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b662c6c6.mp4?token=eqGKngzM0UxU9o2kgHhTo8JkH2rtsV9BSgfDlS9cCExVOGe_pTMmBdA_gmiEN9gU_G4CizM_ADJOAKpcCL4m4SIYQYjd25vAP9YwSZzx5h6pVhCzHye8jWt9gMdyVxHg0gp8p0sWHcXGouO_kyCKPjPwLPYJtqvhNdXOqcjEzrSBuYiz8g7ZLsiv1uECLfEMHHPLFTbL-HoIKaeqqqtGyQeUQE-KT_VHYafd72K_VvjTci3yESyPLCOVVa1K6kfn6WHpahKa5xw3f89ziI7Ei9NwWtZ2-p1HVDNfbYtVxwqO7sEsFgcPVsMMddUO4Qz2A7-oU35SV_7l_nVeQsn_lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b662c6c6.mp4?token=eqGKngzM0UxU9o2kgHhTo8JkH2rtsV9BSgfDlS9cCExVOGe_pTMmBdA_gmiEN9gU_G4CizM_ADJOAKpcCL4m4SIYQYjd25vAP9YwSZzx5h6pVhCzHye8jWt9gMdyVxHg0gp8p0sWHcXGouO_kyCKPjPwLPYJtqvhNdXOqcjEzrSBuYiz8g7ZLsiv1uECLfEMHHPLFTbL-HoIKaeqqqtGyQeUQE-KT_VHYafd72K_VvjTci3yESyPLCOVVa1K6kfn6WHpahKa5xw3f89ziI7Ei9NwWtZ2-p1HVDNfbYtVxwqO7sEsFgcPVsMMddUO4Qz2A7-oU35SV_7l_nVeQsn_lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های عراقی از وقوع چندین انفجار در انبار مهمات در استان بصرۀ عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/453273" target="_blank">📅 03:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453272">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
منابع عراقی: عراق مورد حملۀ نظامی عربستان سعودی قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/453272" target="_blank">📅 03:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453271">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
منابع عراقی:
عراق مورد حملۀ نظامی عربستان سعودی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/453271" target="_blank">📅 03:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453270">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXj24Q-zdrGUeB2Phb876E_M6HLO21p3JIm6h53SGESbLkmp91vKOzApGliJCd2M5fmeOCWr3KZ2bJK1spMfMyWKbakWMVlcsNZZeuo66p3QweFRoSZ9QdCsVCGyc_rI4YGeEl-INsmSilfB2g9iufV-cIZ6FNLSsUaMdMXtIMACM5GPHxweafhhokSWlxP4BqkMM9a4nz1m4wQvEWag57eHwTeJ4Q3V6Er0FSpa5tytwsixvPG6ttw47_fiYwK72do5KQjGRJEJCvU4th8vaf3y7L4_ZcntF3KgBqc8P9i3T0ekyRXeWx-0v4H-2oogxQY4RgUsZqq_T938SYf49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چگونه در گرمای عراق از پاوربانک مواظبت کنیم؟
🔹
سال‌های اخیر که ایام اربعین با ماه‌های گرم سال و تابستان‌های سوزان عراق مصادف شده، گزارش‌هایی از آتش‌سوزی ناگهانی کوله‌پشتی زائران به گوش رسیده است.
🔹
بسیاری از زائران هنوز از خطرات نهفته در پاوربانک‌ها بی‌اطلاع هستند و نمی‌دانند که گرمای بالای ۵۰ درجۀ محیط، چه تأثیر مخربی بر ساختار شیمیایی این دستگاه‌ها می‌گذارد.
🔗
حالا فارس در گزارشی به روش‌های مراقبت از این وسیلۀ کاربردی در برابر گرما پرداخته است؛
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/453270" target="_blank">📅 03:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453269">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae58b9a1ca.mp4?token=HmEbW4G4gjK7TD84kQRv2rb1l2Zqnh8YGFI3j0jINh3yuTzb10oQl7vx48W1Fx8NbYisA8mGbvF6VqMfsQ8MvKuEfDUV_qHU27SF7-WY-sDPKmdheZx-3TNJNN1Dt7gsrcmIoyW7FxKILPm_kmnQqnrVJDOGuB01OshQNVXQUz8adu3LwTXwv4TJUhryZqAfQJLWr5iU2Im63l8M1loB9lq1Ce6S2Xdp5o1bLTvhFdh3QZpwb4nikdSSHXckZ41PRTB6nZPyFy-6WLeG3rXiZUOYCskKv4ONqlMld5Jt8gR2AOvSs7Nx5RNFAXx6ggqkKGRsycqF_d4OcF0qPY8BFEsfJllw8ckYPM_5h1OyGb6WwJHf3hrpEnd7k8Q4tbEgndk1xUwY4Jg-Y8X39LTghI15MCLn3kerqR98-dhJ4XtTZjyZHIQnGOc7SPhLwUkAmQkMBeM2dv4TiQ125X54oKyw3dR-fSdB1TAtF5ykZPICetYLzQ1CiyNcc9Psic39pvfGp_fGazWjd9KJg8EpzIMI-ZyFdHAR9qnWw-89rTOHmF-g8eUMHCVpBDWr36Bfv9FqC5uqtl0rRzNf2sC2tpxBUeyfmCie7lGaIMX1CAbmSz40NCaZ3RBxNXRJTx0mlrj48rUF8QYkvqLO0TKoyC8CAoNkge1rE-813SaAFV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae58b9a1ca.mp4?token=HmEbW4G4gjK7TD84kQRv2rb1l2Zqnh8YGFI3j0jINh3yuTzb10oQl7vx48W1Fx8NbYisA8mGbvF6VqMfsQ8MvKuEfDUV_qHU27SF7-WY-sDPKmdheZx-3TNJNN1Dt7gsrcmIoyW7FxKILPm_kmnQqnrVJDOGuB01OshQNVXQUz8adu3LwTXwv4TJUhryZqAfQJLWr5iU2Im63l8M1loB9lq1Ce6S2Xdp5o1bLTvhFdh3QZpwb4nikdSSHXckZ41PRTB6nZPyFy-6WLeG3rXiZUOYCskKv4ONqlMld5Jt8gR2AOvSs7Nx5RNFAXx6ggqkKGRsycqF_d4OcF0qPY8BFEsfJllw8ckYPM_5h1OyGb6WwJHf3hrpEnd7k8Q4tbEgndk1xUwY4Jg-Y8X39LTghI15MCLn3kerqR98-dhJ4XtTZjyZHIQnGOc7SPhLwUkAmQkMBeM2dv4TiQ125X54oKyw3dR-fSdB1TAtF5ykZPICetYLzQ1CiyNcc9Psic39pvfGp_fGazWjd9KJg8EpzIMI-ZyFdHAR9qnWw-89rTOHmF-g8eUMHCVpBDWr36Bfv9FqC5uqtl0rRzNf2sC2tpxBUeyfmCie7lGaIMX1CAbmSz40NCaZ3RBxNXRJTx0mlrj48rUF8QYkvqLO0TKoyC8CAoNkge1rE-813SaAFV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت مردم پیشوا از ۱۵۰ شب میدان‌داری در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/453269" target="_blank">📅 03:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453268">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رسانه‌های عراقی از وقوع چندین انفجار در انبار مهمات در استان بصرۀ عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/453268" target="_blank">📅 02:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453267">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c956575f69.mp4?token=bnH0f8XNIu3k-8JGksj7Y6Jw2gAzhVu9i_QK_cuFukVDnb7HpURwcuW2oVmmcIZhDxYaDXM7Ji1GU9r1dpSRG7oT7qn7M1eoBfY4g1N7fxXpfZJdiU7WME0eKuYlPEIcx6Gdpj40BGrDz2o2Db3foA-yA9oW61Xsn-UnI2Xkej6uzXgiLnF_0vtcLXYspmjpVT-Z42GvYsH-HocZ7PMuiGFQf7rk_kzeuiIn-kc8pXZFdJ4hMRKR83tfU0KfTZJCFH5wHHAc2uWtU89OdW8SMTYeHc1WbO9fvK5GPnCZp0mDOdH5t7RWLtb9sN-NLkwKgmAeDP8BZw3cacM8iyRl9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c956575f69.mp4?token=bnH0f8XNIu3k-8JGksj7Y6Jw2gAzhVu9i_QK_cuFukVDnb7HpURwcuW2oVmmcIZhDxYaDXM7Ji1GU9r1dpSRG7oT7qn7M1eoBfY4g1N7fxXpfZJdiU7WME0eKuYlPEIcx6Gdpj40BGrDz2o2Db3foA-yA9oW61Xsn-UnI2Xkej6uzXgiLnF_0vtcLXYspmjpVT-Z42GvYsH-HocZ7PMuiGFQf7rk_kzeuiIn-kc8pXZFdJ4hMRKR83tfU0KfTZJCFH5wHHAc2uWtU89OdW8SMTYeHc1WbO9fvK5GPnCZp0mDOdH5t7RWLtb9sN-NLkwKgmAeDP8BZw3cacM8iyRl9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۱۵۰ حماسه‌آفرینی قمی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/453267" target="_blank">📅 02:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453266">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
رسانه‌های عراقی از
حملۀ پهپادی به مواضع تروریست‌های تجزیه‌طلب در اربیل عراق
خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/453266" target="_blank">📅 02:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453265">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMRPah8YCNYqwS7fAEmQ4fa4msiyfjW2j2NO5NyT9N5_7WBEKwzhceTDNSdxM6jXNqCITivqd3L-zRRrRic_u2LYwkMglCWgKURUEbrTVFzq3HtxGykRjJvqTkaEUen2bG2xJxAxnJwxapwQutO9c__saMQy-4spiQKETYtn0ppl2oM8ysGm8Z_c-4iVBhLSJBWx6mZARuOOWlfk91-RPN0txMSlnaxKUtTgX196ogt1rqcuxmoha5ShbXtUXD85GC7fmKOfJNwhqWdbef_bbdYVPbgp2xKEhPmsumZLG_oxS9cGJ5g37kJzXxIBhmywOOMCgRjdfni4CHwks2nLWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکمیلی/ آمریکا حمله به پایگاه خود در اردن را تایید کرد
🔹
وبگاه «آکسیوس» به نقل از یک مقام آمریکایی نوشت: «ایران لحظاتی پیش حمله موشکی بالستیک به پایگاه نظامی آمریکا در اردن انجام داد».  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/453265" target="_blank">📅 02:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453264">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تعطیلی تأسیسات گازی در شمال قطر
🔹
در پی وقوع یک حادثۀ نامشخص در تأسیسات گاز و میعانات رأس‌لفان، فعالیت و صادرات این مجموعه به‌صورت کامل متوقف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/453264" target="_blank">📅 02:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453263">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تکمیلی/
آمریکا حمله به پایگاه خود در اردن را تایید کرد
🔹
وبگاه «آکسیوس» به نقل از یک مقام آمریکایی نوشت: «ایران لحظاتی پیش حمله موشکی بالستیک به پایگاه نظامی آمریکا در اردن انجام داد».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/453263" target="_blank">📅 01:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453262">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0qpbrYc9pnO22oXHrv3QSznzUgTUE2MbXbq-q1UtqXXDWYNN1-MVvMuBzBc1bXGst3JFfWXjuPdES9n7penQyvaxaYdE23wUE5cAmadmFIjEX20r5q_C7Ogh2byS2QKDskL6aqWluCdz-mIK1ezLO7tmRRXRhETRS2eJGgbUtnnVhtGX2EQWtknRD2F3-RrRYgZPgJeRhhiszEm7M2LOiC0FzHdmf1R0QAiPeFwBS3pWc_3diFxo-3tpcD629N09Qa6pAR_waJEqyaKbCsroFRqjNegJzluq0YdtRtdeV9uiNfIvYmxWguVrIxIHLjr7Yi3Smk4FWw-vvZGMx1tbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رسانه‌های عربی: سامانۀ پاتریوت آمریکایی در مرکز کشور اردن فعال شده و در تلاش برای مقابله با موشک‌های ایرانی است.  @Farsna</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/453262" target="_blank">📅 01:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453261">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
وقوع انفجار در پایگاه آمریکا در اردن
🔹
منابع عربی گزارش دادند که در پی اصابت موشک‌های ایرانی، انفجارهایی در پایگاه آمریکا در اردن رخ داده است.  @Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/453261" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453260">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
وقوع انفجار در پایگاه آمریکا در اردن
🔹
منابع عربی گزارش دادند که در پی اصابت موشک‌های ایرانی، انفجارهایی در پایگاه آمریکا در اردن رخ داده است.
@Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/453260" target="_blank">📅 01:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453259">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkX1vIAFje5SVS7VSNQepK0YqXKtkP56D00KQfYrpNA_xx0Erh_g4mlKNPdOT6JUdUnMa6wUn5LKQqP632K3BOcAZiaiGXYHMQeHWydsbioCFjrtbqj8nMkxnF9yIlhC28jyXwi3jZtpEGeKgGVzt9Ol6Edw5S63900BLDT3fsKf35WyWIz13pK3CVFUNoxVenUyMbJWnAQxbMq2lG5VjW8HLodDy8kqeaAVbkRUWCpjag1KcAaOvEN3uBPACQJa2HhNhuHqyj8_HlXB5mGCvn_Uczo6riP7kuKvGq0qlkoKeG_WVxhaoTa5FcLslW44gKTtGWVxi3wlGfG4xFLLsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
خاطرهٔ فرزند شهید سیدحسن نصرالله از اولین دیدار با رهبر شهید انقلاب
🔸
سیدجواد نصرالله: آن زمان من در ایران بودم و پدرم که آمد، گفت: می‌خواهم تو را به جای بسیار زیبایی ببرم؛ یک قرار مهم داریم. از حرفش فهمیدم منظورش دیدار آقاست.  @Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/453259" target="_blank">📅 01:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453253">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOZDm43Zt_e-C52ifj9OfugF_0LLEJ7gMTYFEwiBqB9KBi7NBQ8rwyPMrbZajaiUqDvTclOmd3UDGIZbm_uzC-C-TxuqvBUj2vyjKtywvZ4ZwzwjHQqVTs0dhhDloyfVYUyDos21cBbuCG-mvXtDh1QicTiMH6QJPwKTYKsHlg1fAce249lKkoLW6pLEl8khptJSQJQ-ckpR8lgJ954Zt74aNJrTkG0O61C_VrBD6mVflD-CnJRBqVzr9JzpJ-dq1u_KW00wGlbfLMkEcDihlM4Ky6qYqpmrszrOEudXrd0LNj2Z_TWsQvF88O0n5IUbvOcenmhRtQahuoStfj8iLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rquMfYKdjAKAOMF01ZB14KEW3A40DL-vkYGsN6BWzgQo6RU6jKMZktEJdvweN2E1zgojySfBw9MpRZA5WzhoH4KKeWVxOVCLUfxdYgoVOHdrVrnr_AnZ9_NLIcUQ7DVvKKOu65MDY73mfNqBa6mMUP6fn_EEZrIaVCsrqWJuPIi1Be95ggt4053GYAtH4NYhEUQYYHKpyZNy8DBhD5Iqo-X8ArGNyHSOK5sqJjdPJT7sfRSlbs4YFa1tOftgPM4HpbktnKsEzhSFVuzO4oUz9vURQVvbFavNkAbdwHVxXJYJrxF6wJKVwmC4JUJ0SYjIAr_lcjd_wGPwqFwW4rkJ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKZTDfsWi6sydLg1iqwiPyTzCHZtpK19IM-0_IGZ3ejSCYlbLiDPufpQKtOZ7j-SGMPUfYnA0ls3kCg0_bRYVg1eyjAo0tQnccchVS_20kFuCDtJwvKpRPp3d6P_TDI9epnQ2rzyL1XEZskw5jR6vHORGmRvbFZRsJgE_B5JqaMsYjktLnGNp1fAj8Re4QIe071xpqKd5GxXUK9t7HE5AKgBBBd2dbOJaB6tZheLo5bAOGXfgcjA6eDaIX3rEtUpHWjtbucL4t2_8BUBLdQNEofZKRDiYW8Jj626tZwmJPgSOAELwVxd1J2IwQUv9QKJ1RMKRUgVZLDJXN2I5yXE9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwW5tXAvhUHNFgu6TadtTyhC6rO8Tv7pebovrarPstVWEdQnpGTm3ut4NcG0Qwm34dRTfm70QttU7Sya_Puyk91Og4cBIOD9Ixd2DmWNdFYkKHXroN--uOxiXNpqoz7g0VCW87btirubh4RbskfGALCB_fg_S7oBGVbbxjTXvOSt4OuZun_agpADcwe83bWrykh1b1yPJsXjlLCKumGgEiGuX2r1SJlEz4sen6ztGrSnHfh8iypePHcPkwkF_YOF_kMxjDwOjdUfbqyg1JGfBxl_Cet-X50MwL_cop5HWlvL1fJbH6TeQBWYsGYRGS0iFn7lbgvUBtlmoiB38Derlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnDdrRZVF50z76WOX_rFYL0HfZY4eLBq0GevkiaNXadsaTmEobg5dtpG_E-CruLqIbHH-INNmWSTh84WysguWESLUCM8TOpmxKPVGuYng_tk-CGyGnRfXSSgL86FuY1w_aUS5hyiXp3YwfzjzTphdZBf5S1n5SNNQ7bZ1zp5svX-nBEipTLX46QoZLQQE6r4psA81o7joX_-Fd8-ZAOHDDQzgj7jXCAa1XF4HIsAZws666HemsMu7FjPbIowZs4iZmpjOmTscICmMdVPofI0klgJ8XuHW61idcmxzqcdR2hkA3Nxf5D5P5gfhBVZ7kVAwuq2we8gIZ6an529OXKCFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EyVP_bP7PcNLnXxwXZFHm6ORHiMR1evhgsgACQCAYpCTEr8SAS5Rm59NWkmjjrssK1FRhI6J3c1_od78NXnOUmKoi7xEsVi4QEHtmwQuk1J63GXGpys0rLQbc5cVuEjA-FQilqX9HPSoCEbbo6k2fGQmbnU5bfSpmV8zam04NHuTDv3_lebIoXGybUtu-tvGW6bHeXVsrKM_iTtBapgacWNCxQzouO1Ki5XCYDf-c0Bf2HgOwFQjAfMcF4DvOrn9-K3dANFpqfSsaGrOFZmiwlIRCaTooaObfDK9eJLrUcajl-UhB26RQOnt4xx4usmFiK3ASpZpcoEUj0jFrOBkZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۷ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/453253" target="_blank">📅 01:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453243">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CrtF_Su2SswkeCPZNSi_TSokgHkslZCPW81H43OqumKi5PH9k0BBEcm3hmtc6K7PqrMVLly81kBojdou0odwQR7lqNe3Xk04dQs76USa_GxbU47rq7M01EZlEBi4zSvKwp6y48y1q4qISptwXjPfeUEmJsWtAF7_iguOh0Z-2O2-BIoPTquJVI2FkaGDJ2H3EuHKsnSI97xar1FKIetlMrfq0RWQYkppRg4yteQ2WodSQoPhQBfLQ-bzuu9iPQt_B1mqZB9XszEsEYXnTm6aPJLf4OfgwHL9HKwBY1dGQMBPJPG9k5c_onO50k2stjFUy1-pUiMsKM1_2r1s0tkMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fgCD4ZCFew_hTHU-ltWkd6vzwCuEVtZWCG5aCJrGLpEyz7djBSDKoYHuA_-N45G62DMdfF19lgoukjxKtUCxBZIQQ7M4ewR5VyM8-Pm-RI1hcPbyD_HfRJak5BUOj2wc3e2FsJiugsV6cuanU1yaQLUI0J_03CeSSsj7Cu_u7TjoFcmZEF1KpqDS2n4fOpAsU4Xeh1rWUZTG-jNzaz49dL79gVUvVS3K5CCsnJip_5BdrSz17ZZLUEEfFTFd-PkvI8v-SbRGvM56i0Utwvt0TH5WtDvZamcjZtmcvL2qKWDdnCAGqCfNbOJCgKf7-HRY-bfye0yQjOUIJd6ox3AkgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cB55yRkzDNFnTYX4GQfmlcnz4jRpw2BTZgugM_y2pzYvZZYIKC3L7YOAePkUPCeojXOfJxweG_hLSs8-eh5QrJd---5NYxEX5M7iTQwjNMzUpyxr3hAIfDvi6Rax7aPhTMKwhrGXMf6KMJP3waATf7kZR3rCPz-6mgc993hvbfeqa7WF3VmpxBqvD1YYn_9w-8R6ru_mh1qPyueJ0Pk5rfOrTwoCzVL6C_ls7LtzNLfbr02o8pEj0fEGBx5CA-0WUL7qSlcAABkrmf3XjP8ap0i2WZ36VFg4mPNPjV8gUEFNR2iVy2z6UO5ipjEuBEFQAqAvo_1w008XMIFpaDonCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QISnJV_ydoMJ_3TLqNEqKLdtbQQixN-CXYW_Y76sHiNw9-IQ21bvs-3xu6V1XVpXcoJq-n7QqWtBe0xTOMasHW0kizu7jqcXB0JU6vmDMC-KR-spNdPtX1qs9G9FiVBkjHq1PvuYqVEMQ3rsflVv7aSSvo1DWr_nkyBxiv_7YWNo7m9zzGshFALdsMnEE879y7tNDlyZv7IpEDIIoM8t5lg3oUYA4rDvzXLhOj2E_UWkCrHDTC9mBat5YRyGy9VISCkUN_Pj1o5IaDOFe8Di0GpzSztDufEYem_77ZjuUYbHkkUo1R09qiyY9xnz05619QFe3umOJMYgly3je80zfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j7mWWDVDKCWkJRSF8AeFaT4YRBBmCE-7K_EiFq6fOW_UoAtLqRGTpwl6C81we0dVWind5JxNW6JTmPIrgb5HwmawcP-VxlxphK9bkGvsfFz-8sf9Jc7tNqtSwZstun4IqHY7x8wlnMCKl3XegHGxYQ5-9jjr6UzCXnR9YT2YEAUkmeY0Q_9K5OWrMuXe88suHnQAItAOeBQQL2YZOGW7klFVgm25x9L9P0-Z2w2vzXEcdnJ7uZLUncWyuPzRnT7Pbv3vItjeTNrQFpXbJiG3e4NhdXSXJppr_vtppDAguMi3vMkN09WcGfFKZf4ec6Abu1ewcLQNvThVzmAWqDWhiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZM86LsV1D3uq7AykXIi5B0DYbnCSmMNYuHBq996uREBW0cRORp_xMBd1fsYGdBH6qZ90FlWsp_mIZ5RbHcANvUcfA8yu8cVmcFk7yj9BrN6wDsTcM1Jn3-0HbDZ20P7mBAXH9kdBwWu4yvvvt2TgDrPVTywygXrHcJUNwE1_Osyni0c0cVt-E21lqzL7kY7HWt6i9Dv9_qe844NqdT5z7R6xub1oK_5Mb7r6PKvlcrPjZYTv9gMz6xoldku2BOcqypGq3TtRceAUc81cIzt28tcn95uvfJQvABhMC91BQhOaeALcdhZSPRp-EmrcXI_yzliOOgfHuIy2bmh3egp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R19rK59qeb-wGnY69cXtoxbTkPOU_rzrDqxcMTBru7YBlSuwhCd_k7vQy19WIjI5Qwwp3zwe_8sEI1SHVJwLF5uB4l7GT_j6fEe4SBreoE_vkk8SPTHUdTkqrvj3Z6fXkzaVVk6m-bD-ArfoYtVeuu_07NOZxZmZ_UDA5rN2pPJ3c0NasvPTiLFFNVf36QmQGvpkhwxvpwTY2xVcaCElxqf6ASVgifoo64rnMwjo7amxleDEYhi7x7-q2y0XYqhgA1C9TB22gwmYCwSmY5GGQyaoErsnGuGcNfIiCw7Cv-82FoVva09Z48POXY1bO-fY2UzdY1Rl18b1tf1yfokDKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ab5JtIVIDRHfujT4Djy-RNnAas7GTTNIyIhjTxT4l_aE3bGHeQtUNwUZRZKliJm-ToYi1QMlsHfELk0y8S1JlptUvxGIR60p_Domz4XcAWfjIp5azLgZ0hf15LdVcLLewsHf9qrOcdDonbTYY_4rgZ0NGJhBXi-3TJdfrmJuarcWCS6Fgok0B4zPX4I08dYH7a4BcTUbA9qiZhtWCLcIHOSjdCqeCx3R_ijjnBGKp7I_CsD_z7MU4d8JyxFI1L0twPF246cA7igmhirVycgjzd0OfrJCVQh8qMJX4uhZJuCaxkqlS-dmvo_K5RooFBNXzXM0RqDsnqXJO2kGIs1-aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eg3wSJsVGtunzLwWocIfH-EreREXE5cNU74yj2u5KBtXMRBQcePmpB3oaIhYmzy6KIZmMAwoDVA5ftx7lpRIrvzo1MZkkVeF8ohkx8iteDDqnTDfMCg8FG9ly4DaN52vtgFG2hjFmbFFsGHIDu8Cy65k6zMiJUs51RZUxKXmgqTBy3Y9-9nWG9PJkpI5kzHuCifFyQp4G1ApVDs2ggESLSFMA4Bc_tLH9ywEfHv_pGgdf7jrjQEBc7fa8HI3dT0UdoW2TgVNBRP1imM5zV_5RqBjjPEAFEadAILwpmOILmlZmKMBMKwBalwEkgAsIsZbQPX3AD0bWfPxOuALyjCNNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453243" target="_blank">📅 01:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453242">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
«سردار خندان» چگونه متولد شد؟
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/453242" target="_blank">📅 00:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453241">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn8OUavM_Nm3U4u4Kzy6Uxo5RhCX9OaZvsWZivANVWsdTrWF8kS-Sczq4eyt6oK83dvrdSo2V3hcJT73TP5jLsbPfSbRUAg99rP4ngHosSWV_EKbIBROTe2U1Nr3lCMmzox7ynkcxjGSvSnbmh7ZwSPiPlgUTqKYV8Gk1Qkp43x52Gl3KWK_6NnfN-3-e5sU-NXhwvizOOU0gGUjbVzdxKg6cwOgMpz_NQc50moUB3LYyZGyNTlN6xinuQeHUgYOWx73z_cc4pD42GdCwaBkgRjFAncqVLOsPQkLWym0wIPxj9kz5bOr2-LBNsCzUpN3ePXTFzrD_SdNANWntoFBhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
در این اربعین سفیر خون‌خواهی رهبر شهید باشیم
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/453241" target="_blank">📅 00:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453240">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c620548f5.mp4?token=Fzt0SomIZ4ZQV1Dlnd17Hd3lPjl_ntIBmrGdrsLicCXFeMRwqp1hJx8QHiW4qt0af6HAzzNd47VL6C6kAkGhgevOrm_nmmPsr6ipDZgzheZ-2tyuiLlStNiByUcoyCznC8y_4U0M2SK2dfBR5GN7RvmbdeJO4gXVHL8_I3FKYi8au6pN2YXSrlqxsPAitnUS2q5EYQobOAdLkF6ohQmdtVqJcCJlGqOhvjr3mxxpwGcso--BfZWfK_TZYGsVde5AMZj8zgha0p8_nPY1v4vIwoUQ3SjssVBcrSlvRRx5oD0vbVtDmC_TERZVw_rDXF3QOzvtiYfGt7Q3IJCEEJqpwJ9RV3g3NXypK03WQqRgsyjDKG7wHhfkQqy89KUpfwmJbaw84zqbv8Ls43_EBCJRuH27hJHFwsEZPD87VnNa_0aRKYpzJVDNzwOAv_C6BNiXPh9PzfvvnaVi3YrAFWrs0dxq8D1u0-8IXsCB0MyvwHziRvmWYUlKQhveScRmQ7zBGGYLDfq0ogvAfIIQaYM0v1R2c0CEz2-xWlDQRVDi1jSE2dFdUGhEdsHCYImH2O4LQY-F-ecLOqkzkt54b9abfikUJqwQ_gBQsTgmA_IN1cFnZZbv_uuIX9zE68EqrSn5kj7lgnveqx3J-FFhpPw0Q0JkxVYeHaqIKtZqLOIt85U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c620548f5.mp4?token=Fzt0SomIZ4ZQV1Dlnd17Hd3lPjl_ntIBmrGdrsLicCXFeMRwqp1hJx8QHiW4qt0af6HAzzNd47VL6C6kAkGhgevOrm_nmmPsr6ipDZgzheZ-2tyuiLlStNiByUcoyCznC8y_4U0M2SK2dfBR5GN7RvmbdeJO4gXVHL8_I3FKYi8au6pN2YXSrlqxsPAitnUS2q5EYQobOAdLkF6ohQmdtVqJcCJlGqOhvjr3mxxpwGcso--BfZWfK_TZYGsVde5AMZj8zgha0p8_nPY1v4vIwoUQ3SjssVBcrSlvRRx5oD0vbVtDmC_TERZVw_rDXF3QOzvtiYfGt7Q3IJCEEJqpwJ9RV3g3NXypK03WQqRgsyjDKG7wHhfkQqy89KUpfwmJbaw84zqbv8Ls43_EBCJRuH27hJHFwsEZPD87VnNa_0aRKYpzJVDNzwOAv_C6BNiXPh9PzfvvnaVi3YrAFWrs0dxq8D1u0-8IXsCB0MyvwHziRvmWYUlKQhveScRmQ7zBGGYLDfq0ogvAfIIQaYM0v1R2c0CEz2-xWlDQRVDi1jSE2dFdUGhEdsHCYImH2O4LQY-F-ecLOqkzkt54b9abfikUJqwQ_gBQsTgmA_IN1cFnZZbv_uuIX9zE68EqrSn5kj7lgnveqx3J-FFhpPw0Q0JkxVYeHaqIKtZqLOIt85U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویر شهدای حمله آمریکا به پادگان ارتش در بمپور  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/453240" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453233">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oD7xhwqDRzK7j-A2ydZj42IvmC5Kc-YM5AZ6U0Ma3FYPa-Vpx1zTH9IdsAtjevXPRyK5ZasnRc_VXiAB3iMjNhfM4Jk1vdlHJMGRuq5fon7Kq4Gmh16M5SLzimM8LGPJsRH2794Q4JCS-3Ju7IpYX7ELXN5XxZh03_sOISunVcn8zNuDPLo9Wkbbut4pKyqaTAdvMLCqo1yqHr9raPN0Cj0oHY_rykLv7BczQxVsBLcVItepvDde6Bd0GUkbGZibNEhLzEGUQzCLLxfQcxmsbocTHk3N-roSs6NH7uDBDpERzwIxUBXkTLETCgEhbIaYi-r10EWmwKOZvUq155Kkww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6djLFlP1_eVSoGau08l39T3BRqZSp_L-NrT1X9jIphsKVSNlG1leFNHimUNoW4xTAqUFjsyvugS9uZA3cjc8rl5c6F-vufGwfgniowqmk_hmmTql2DOcia552sxZ9_kkMZAGzVupe4BIvZAqmHmsZwZSWHejOYupzgllWMG7Qu1PHTd8vUrHAuETEqg9cD26AhPnl9P4461dT8HuTLHoCLJiETEHgS-0Xk_q2EHo0HG9YiZVW2je5R6N-hl461Pjwh6rBOD4pfPEp86xbISDT7aSu4LkX90U3d7VfUu36zCesJ4H1BGo9UbXyb5pnIN3kYterR7d7e8ybg0OeAN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1yBfVDMBcLfohXF8r8i9DBQsR9nTsp9MTHAAY7T2151wxgjY2rwmVNMhJxs-YPV2TaZt8BAITkktwuOW3Q6Bc97-HPXwhiEOY4IyKueKZgMpuKU_vucUXQF-ooM_bC6gyu1dM7ZWCLF48iP9IJmoE2sXBol3HApOggpCBY0KjL2o3vGsEmoRSefNHV6gVoN5SxOzB1g-aBbp4SAwD1y4d9I4HxUJlHhw_JKBNKN1Bp18gYk7URyB-DxCTHIMNdIyy2csHjmXNvqt87jhhC_hNjPSEu_jcpBMLydiLgF0XskXwsrs2tx6OlMx4Wop3zgCGRKejgd-ZfDu3RoD9uszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRe1FUndmyCF8nvWPFE4Lqm7_dojrfn_POtAxOKOhp-uYIie85EoZqByTKWYvqG72nA3O7RnHmu_QpyS83NFqerzXmsDcGQjpLBRdo_pxrYBM375qaHwT1brvQu76a-9NpKnpsE3vb_D3v1O29kDfuHBVpwFDeYUj2nPiGj2PB13GD0hgETb4GI4TUfNt30a_OEpt3g6uWYEDaSUK1KKW6KdspWZAbS3Dpud3AAWhKosL1y7t_6TUw_W9E6On53jCZ8acPMOF3gHV8zPuUn3rvbAGo8cpQdN4KYWeLpmtXD0dDnm4HjvzukY66H-eBrLE8HLsp7rb4xkwFdinmE2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9UVUO9pr2MqdzgnqOLdJm3vrGJrHTp8dVpmeUgUXdMrgmzqHHYOzGQ2vWwZTBhNnGFmhN5rg1-0TZGlUaNYeXh2XFw3VF9C6NyPFNyGIYFMBXUcssjfBf9rUlRUWb_mtGFRDO8Q6As4kqrMt1N7jEk_dxQ8OWLhGCoRmTdGsimlOjrG9DcLZrFfvIF0FLuR0vJOd9BsNKxBIt3-NgJebJocuQKb30mqS3lLJzVBIVIALf2z34SIzltrwRp4JUl_epDf3Mx65Zzu3xkyhSHOM4AAlEZ98jkEQIkJq6SOj4-dqoqry1tVkuiOmAedyVVExIb-kMLE9VaxU5mvsQSmxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5S0z8O1umkgbmZKJcl7fBXGv9bIXhca3eJws6QX7-5PSWbTmqe_0Rmo2zMu3EpxkLPFeTJg_MRqAfpqr3ZGOUIsMqAsRuux-D6-cHjRXT_CBn1xt_BG3DSCB24IcEn-yA8w8VTwnbdqV9TS3Qm552hanaX7lTDepnz4vbVcWFuF2KFixzGjA9sSuN0CnELueX_yyKwILXbwz0JHPJO6VuNaYZfQhuJIahxgRaxVKm7cr_hkSvpb5O0qVVwdjQfy-Q4-qBFHoxLsOXTAqY43oNNJ5ctwvItXLMp9GCBzFZu9kWa72XUrutN5YpZCKoQajinKwhF_4TUYTFlKceX7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e-CfCKWgp01EBU6pxN3Epzdmy33PbKgDzVJlCTjiBY6Xau6iSCVedd9zNqhUxW_i6cuujF_6IkUl20vXe1BWXMTwmb84WCT3IFwEV-hYR4j7wrciCH569816CbzOz1-AwBP7Mme4KqzuXEhJiBkiqFJCECw3WaM_D3HB2-Ksubp3vBYBWw9iWHv8AnVYBjxbkag4_ZRr30nkA7rSBM3OICmO06Mk7e9jeVO5Bt0Y3qUsgTDkJmus50Y-ZYbO_GNVXSB-EB38fV3aKBYyWm-XMzocJgGOvkCtV5NE8yzQFeJo3opaQsKcxlgwrCebumQxu0BWytF1YjMsIfESbwmcVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ایستگاه ۱۵۰ تجمعات مردمی در شهرکرد
عکس:
عاطفه گنجی
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453233" target="_blank">📅 00:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453232">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVyKneAOzgysvm3q4EMHl-RYl1m6-D3BUZp2oUrQQyzzitK_LVqfj2XJSoSOUC2DmRHxsst4_XblrvRUixj_fJwIdGYRBVQh0agKoGE5FkOkC0HJ51a3ugDLL9Sk4quNRY0FjNIgtjiRBidrIPckulialjihR7CT4UMPwd7-g32pborrULKEzAlXQZCIGhvhs1rxT2k_oiz6b48RZqpJUbE5SM_ikrmeJNYVtNvjG1BVNkpjC6p_EjtaGx5Ckn9eJbHl--2xsAlyZs57Ne_6BJbTvUgpsn5tRFBXDn1XyqKK_magOa53bFK19_i987SHToSpfPCPS1bczoj4q2_-Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمی از آمریکایی‌ها خواستار بازداشت نتانیاهو در کشورشان هستند
🔹
در حالی که نخست‌وزیر رژیم صهیونیستی به آمریکا سفر کرده است، نظرسنجی اکونومیست-یوگاو نشان می‌دهد که ۴۹٪ از آمریکایی‌ها معتقدند که ایالات متحده باید نتانیاهو را هنگام ورود به این کشور، بر اساس حکم بازداشت دیوان کیفری بین‌المللی، دستگیر کند.
🔹
طبق این نظرسنجی که در تاریخ ۲۵ تا ۲۷ جولای (تنها یک روز پیش از سفر نتانیاهو) انجام شد، ۴۷٪ از آمریکایی‌ها معتقدند بنیامین نتانیاهو در غزه مرتکب جنایت جنگی شده است.
🔹
۴۷٪ از آمریکایی‌ها نیز معتقدند که اقدامات نتانیاهو به روابط ایالات متحده و اسرائیل آسیب زده است.
🔹
۴۳٪ از آمریکایی‌ها بر این باورند که اسرائیل در حال ارتکاب نسل‌کشی علیه غیرنظامیان فلسطینی است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/453232" target="_blank">📅 23:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453231">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9ddf195c.mp4?token=kkJGFSykc5kQoFi8tF6mYr0mI02O0X7mgrFv-qGCxuDLf5smdcX-NDOhzjEWc9CKlQ255j-maCWdLz0CiYzOV8xhbXQVnxi6FLdfnyrWdisgR4PhYxV6Bh0btXiz7aKbHqjnlfHCJ85oXDTfH4yVrNZeZnaht4ybKt9g2B7fq0r54QEqEpeMpI_WVqLn5B8PmU6eWL7pWNRf9j8KexzqkNP_TZuED9i8ZeDCHlTPCi27bNh1q2lqKgcZHM3zPYINjoBbM8uQrL2Eefuu1LFlmLcQ-WHnO59nrKuIkBko7wu7TbocoIqIWAVArav_AkcsAhee5jXW_kSLznpJQ0y4dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9ddf195c.mp4?token=kkJGFSykc5kQoFi8tF6mYr0mI02O0X7mgrFv-qGCxuDLf5smdcX-NDOhzjEWc9CKlQ255j-maCWdLz0CiYzOV8xhbXQVnxi6FLdfnyrWdisgR4PhYxV6Bh0btXiz7aKbHqjnlfHCJ85oXDTfH4yVrNZeZnaht4ybKt9g2B7fq0r54QEqEpeMpI_WVqLn5B8PmU6eWL7pWNRf9j8KexzqkNP_TZuED9i8ZeDCHlTPCi27bNh1q2lqKgcZHM3zPYINjoBbM8uQrL2Eefuu1LFlmLcQ-WHnO59nrKuIkBko7wu7TbocoIqIWAVArav_AkcsAhee5jXW_kSLznpJQ0y4dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری مردم ایران و عراق در عمود ۷۰۷ نجف به کربلا که مزین به دکور حسینیهٔ امام خمینی شده است
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/453231" target="_blank">📅 23:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453226">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1yMPXMnyOfamazQMB7w914O3BJNAjQ8yPzb_F9FP2oIRjVj5PHHU-HhQ9vI1hWEIsQ9EOj3cExgYGLISvd7RUrqWyhdQIC7VGxmt1fxWVSmqJR0hKkrlud63yzj4afY4OX0ZLvYD6mQFLcViMsO3Cf4Bl06l27CGR6t27mul1zY4WmmzkjQGSFBvaOWITmxpNCfgZZNGeffCzNLpdzOdhV4ogLpmjM6ApM3MfD6PDJOO9sxkmEZJHm0D-TFIJTTiRCywO9ZG8u1gXdR4iSr9Eel3W9CxhjoNr5WW5a_lI6YVEDYuFjNdcyuYtaFzuKy-XQAKhyTxcFo3HU0Zhnq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzbS4gmi6AH9GPpP6KxrlywmLJqhY16bb4y8BxO19SwuKdnvYtwGTTlx2ynhv1410UtOBVUNBye0T-7jASoUzWJB53dHnJSMXZc14rAKH106Uso625nQaBrtyWeGqyD0d-9q_bl_4Sj6ltzFpo_TXpYYODeYmziD6qjHG3mBfuIJ2Alk4laKupAyt16zgEmmYnSQQQNIF5GGEUkXr4lgaq1ATVP3ZUHBCvcwuRtNIkMMcHSGS4TGmFoxMjpxr7_gnLO6e5TS8mf5pIWJq5VOXPawiZQcfEZ7fKfbp27CsPch9OSwEte3rhm6EteVaxErS5ixQ8Eo-MocmFI8Lw2wZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BhV160hST7Ovr558PPxGPKbz6HUoD0qnpqsJ-Fy07vUZsjv-nbkI1yCd-N790ooTIub9sQPtPeTkjKDYwnxTz6Zysewb8kJchqrgDAeiyyRC4IQFVXvbZzHdH4q35HHLlIAKO80cEsMULZtgZNOVchpli8zSchBdtu2UuvW2t6nGCTKhu9FIjOe1-FrM1UdTrdwwlDksL7FcInaZgeN32hZurrDOnV-kIL1fc0TH3bMpAgAxV289GpgMq-iKLXk2jfCZ1xk1hoHGeVLW99DfKNY4EeU3ao6pWESCaqF2K4SvOxrzI9NpK2-uKupRWVrV1JdlL4WB9ah1TSlGITL9qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XG7MIA5qCcPxaCQvm2Rg_4iZyv42ppFAye8MijUg5pGka2_Pbe6PopdGeUizfLazvKYOa0rewzyHZC4a7NbkjJaOhzlvCPf_2WohVUuZvXRCS-RLHgTEEKG8V5aNbogc5BPQmsOwSMsfrNjkqFBHizhrUWN2AzFzDM5BzUYQSbE8Wv4V1L1LlLz7rrBeLDGI5T-QgRPbyays0E_gbtvOKTX9hjuEEkBbvfgxWH65CySKSFKSoY5zq_LHtVm7BQzJrn3sQ6S8-569fG89wBbwiG_qAzHnKgwG5C9pMhcdkFh4VcP_Y0nsIpzwHwN0BhE1Dv7tLbgbSDbZVaKE5DBnig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEAOsy1QVdbEBUn49JCbiE82pAyhn3-BFtn3cG1p-cpmSp0OHCH1uiuJlkUvNIC5OOlvnCtkNZGTmisIv5R5kVmc2_AChsdP5iQ0Lq86figgLUfHosY7WWSycGGdATyQExDL8LGp9wFMRbHuXHlOEo_cr5WmgOQ6swvp0rb9bNNRoNTeKxIvMSpmsCrH-g9wogShsbK7Qp-XU3R9kmuQH49vFZy4WrhMxn0I6bwujzMkWFxTwI4-xJo7u2RynuJKlGH5m90debTU6l6KGdTjVVJEsO78fUtNq9aaboOJQJFd8AlMOwkFVf1DwL3jXrcm_gte_17ugHUfYBXaJGmoPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از تجمع پرشور امشب مردم بوشهر
عکس:
احمدرضا مجیدی
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/453226" target="_blank">📅 23:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453225">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be9c7d9.mp4?token=hVMD-CZ8amfa1hP73B2mcFWeTZ79jnWxparG3wDW4S3zEJcLxk9GsfhPBdITbw7uJ5jt-FaPlAFBXJ11ePnrtFlIdg28yp-9VOwbYEbVuPLnbT8oVAIQu188xPjiYdc-vU2ARJ5g8PEWQ5Yhhe5r1Z4CwcQiQUhvebvesozPqSq-SyFjcJHxIQ4Zw30MWAUw17BhX--vuEECclBNSQEnnIWq-vOsTaQlXyNyQAmULvbEpz0-WZwGtoEB6Fbp3kdz0fMj8DokAzzEbS9_oUgvZTcqp6LLT6LCbYz275uoc-huNhF9hpO_EqE7n5BSNYyNuDcX1LGeIkRBdadzQgtZc3jBj1MJSrHtSLFTj6hYP7o1jvmjjLosyBtXo4ElMSNOUzpC10BHDZF6nzQVpVE3O3Hfr4oGgA7OD6SZ1GF3tbU9mC35IUQB_68eRrf88LTvBjBXmRyJMoSDzDk-P3s8xL48g7OGM_Jw9k47WOPwLtORlt2BWUoHX8pFDVPzD2tOHzKueCJ2PydrSq8r3LgoqpF-D91Nh-7FOUE7coQONh4udb6GLU44pYCBRE7FNn4uwzIm96X_-TcRslTXWMA65qB856q2NEE4g199i-hPS4-gzS75v7_gJOHvVp3Q3OsTGs_xnJRHQtIargD0HUocASGhCGsAho0vgMqDVqpSu5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be9c7d9.mp4?token=hVMD-CZ8amfa1hP73B2mcFWeTZ79jnWxparG3wDW4S3zEJcLxk9GsfhPBdITbw7uJ5jt-FaPlAFBXJ11ePnrtFlIdg28yp-9VOwbYEbVuPLnbT8oVAIQu188xPjiYdc-vU2ARJ5g8PEWQ5Yhhe5r1Z4CwcQiQUhvebvesozPqSq-SyFjcJHxIQ4Zw30MWAUw17BhX--vuEECclBNSQEnnIWq-vOsTaQlXyNyQAmULvbEpz0-WZwGtoEB6Fbp3kdz0fMj8DokAzzEbS9_oUgvZTcqp6LLT6LCbYz275uoc-huNhF9hpO_EqE7n5BSNYyNuDcX1LGeIkRBdadzQgtZc3jBj1MJSrHtSLFTj6hYP7o1jvmjjLosyBtXo4ElMSNOUzpC10BHDZF6nzQVpVE3O3Hfr4oGgA7OD6SZ1GF3tbU9mC35IUQB_68eRrf88LTvBjBXmRyJMoSDzDk-P3s8xL48g7OGM_Jw9k47WOPwLtORlt2BWUoHX8pFDVPzD2tOHzKueCJ2PydrSq8r3LgoqpF-D91Nh-7FOUE7coQONh4udb6GLU44pYCBRE7FNn4uwzIm96X_-TcRslTXWMA65qB856q2NEE4g199i-hPS4-gzS75v7_gJOHvVp3Q3OsTGs_xnJRHQtIargD0HUocASGhCGsAho0vgMqDVqpSu5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرشتگان زمینی، زینت‌بخش راهپیمایی عظیم اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453225" target="_blank">📅 23:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453223">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار شدید در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/453223" target="_blank">📅 23:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453222">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
وزارت دفاع عربستان از تلاش چند پهپاد برای هدف‌قراردادن تأسیسات نفتی در منطقه شرقی این کشور خبر داد.
🔹
ریاض مدعی شده این حملات از خاک عراق انجام شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/453222" target="_blank">📅 23:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453221">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03a65bea9d.mp4?token=HBEfK6jtHNQPjX_HV3cYW9ZnhvOsaLL10sWE-mS1RnrLowM4nUGLP6oBKEXxQ4ifFZ7zhf62yfingqyaUgbhSBBZ1DPjswQUQ0Gc7Ho4hw8lVidHcwOFQd2fRHXpQE1rU4H0keMsvoH4INP-dko4bE2B6ml8SbgJ_BMQAqweua94PIpnG6GJUVZSDd7750yazrOy2UDZDMdPnNkUGJM_StHCrJMhhHEvLwaRDtErG96I1hq3YZUODnA5ewypAF5MwnBcpL_vqk6bIn922fcQWYvBGsJzl8vjl-QLeM868-LESUDjJhiFgDNOmjN16kEIpiwEQkozRU6It4-2jBEk5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03a65bea9d.mp4?token=HBEfK6jtHNQPjX_HV3cYW9ZnhvOsaLL10sWE-mS1RnrLowM4nUGLP6oBKEXxQ4ifFZ7zhf62yfingqyaUgbhSBBZ1DPjswQUQ0Gc7Ho4hw8lVidHcwOFQd2fRHXpQE1rU4H0keMsvoH4INP-dko4bE2B6ml8SbgJ_BMQAqweua94PIpnG6GJUVZSDd7750yazrOy2UDZDMdPnNkUGJM_StHCrJMhhHEvLwaRDtErG96I1hq3YZUODnA5ewypAF5MwnBcpL_vqk6bIn922fcQWYvBGsJzl8vjl-QLeM868-LESUDjJhiFgDNOmjN16kEIpiwEQkozRU6It4-2jBEk5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید جواد نصرالله: آقا گفتند درجات سیدحسن هر روز در بهشت بالاتر میرود
🔸
مدتی پیش، وقتی برادرم سید مهدی خدمت آقا رسید و ایشان عمامه بر سرش گذاشتند، به او گفتند: من سید را فراموش نمی‌کنم و فراموشش نکرده‌ام؛ درجات سید هر روز در بهشت بالاتر می‌رود.  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/453221" target="_blank">📅 23:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453220">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7916efa9c9.mp4?token=CMunWSXWgcgzUZwIq0CieCMTN5ocuTLH5D6Ib7eCxpBITzwZgTxLa1j9UZSjIAE6XAZZJv8xEsNaKxE9FY4G-WLkxTfhtpNW0oN48yAcSy00pIDsfQymLE0AvJFQWOi5jdmpSoYU5dfPK4RJtzO_NWYXutWW5faP6ucHJlGx-qtzqHeCwK5LvHdCN2lvmE7aj9DyyjdRVhJXBY0an7p-s2FViz1gDeH_PDOsWcGLmV_HgHXElp3V12Tg7L1Mtg1DofHGbn_DyFLs-D4Kg89pG8aCrr6yR5rrw_rVuO4dD_J_dOc8YdisXRxMtpnDg0ZNPiSdnAKjl_MZMtx_mh4kJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7916efa9c9.mp4?token=CMunWSXWgcgzUZwIq0CieCMTN5ocuTLH5D6Ib7eCxpBITzwZgTxLa1j9UZSjIAE6XAZZJv8xEsNaKxE9FY4G-WLkxTfhtpNW0oN48yAcSy00pIDsfQymLE0AvJFQWOi5jdmpSoYU5dfPK4RJtzO_NWYXutWW5faP6ucHJlGx-qtzqHeCwK5LvHdCN2lvmE7aj9DyyjdRVhJXBY0an7p-s2FViz1gDeH_PDOsWcGLmV_HgHXElp3V12Tg7L1Mtg1DofHGbn_DyFLs-D4Kg89pG8aCrr6yR5rrw_rVuO4dD_J_dOc8YdisXRxMtpnDg0ZNPiSdnAKjl_MZMtx_mh4kJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرزند ارشد شهید سیدحسن نصرالله: ایران و حزب‌الله برادران واقعی هستند  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453220" target="_blank">📅 22:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453219">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1de980eb3.mp4?token=ph9KYK7-4OPe1bV8G2WBqE-QdfC4XZQckqS-sjZ2cWdEi_1qv1eS0V6-w9bIOLRxVMJ1VfZ8hrevlqV2aBSARkZE87s2HUjANTW-bjzNKQUNhmCVw6CSgsuCgE8CAFJP-hn86nKWpb16DZRpiwZloD2OxstEUne4-M1DYDg6s1eit1V76hCFyc3YYpE72J3bVR6_mWoebVsAMeqKuekKTfw1FB9nYmkq0LFlv3ikmrQy6UyxVJlhPTK6QzhUGqvOgiprOVYqdNPqklM8-JRxtPKYLJETRryzW7n1PyVpl5k0DSNU9pQm5dD-AdQ-RpjZEcCWIzZCrBGFpfOK4w1pJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1de980eb3.mp4?token=ph9KYK7-4OPe1bV8G2WBqE-QdfC4XZQckqS-sjZ2cWdEi_1qv1eS0V6-w9bIOLRxVMJ1VfZ8hrevlqV2aBSARkZE87s2HUjANTW-bjzNKQUNhmCVw6CSgsuCgE8CAFJP-hn86nKWpb16DZRpiwZloD2OxstEUne4-M1DYDg6s1eit1V76hCFyc3YYpE72J3bVR6_mWoebVsAMeqKuekKTfw1FB9nYmkq0LFlv3ikmrQy6UyxVJlhPTK6QzhUGqvOgiprOVYqdNPqklM8-JRxtPKYLJETRryzW7n1PyVpl5k0DSNU9pQm5dD-AdQ-RpjZEcCWIzZCrBGFpfOK4w1pJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی: بیش از ۲۰ هزار شخص حقیقی و حقوقی در مجموع دارای ۹۴ میلیارد یورو تعهدات ارزی رفع‌نشده هستند.  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/453219" target="_blank">📅 22:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453218">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd452d0f29.mp4?token=nD-rB-83IRYz59LLyStLSo9PSqOBIQ6z_2j9Y762k7yHbLDsIfFmZGoARFeHXMosjdk9PKANfyqs6irho2qtTypqF8tPucKkC5pK5yMafmM2bT3AQrYlcRdQBnaTKrJGCz3iLH4V58fQ72gI1XmOomCo7n17yAsBp2VYp9VVsy_UmCi1mOm3sAgYG3J5R5vmC-mJDTLnphO_13S8e0ds28cEUNabyjOYiN6QCvAac-ZBV5zhzLJJ91NbbyL_UZgq8PiDw6X4b8SbT26n97wvz90mCfJikUrY1mnFPCaLHmyCrPGo7XcarOENJ4V_NpTq_hOIzZJTKSbL9KbLVaMqmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd452d0f29.mp4?token=nD-rB-83IRYz59LLyStLSo9PSqOBIQ6z_2j9Y762k7yHbLDsIfFmZGoARFeHXMosjdk9PKANfyqs6irho2qtTypqF8tPucKkC5pK5yMafmM2bT3AQrYlcRdQBnaTKrJGCz3iLH4V58fQ72gI1XmOomCo7n17yAsBp2VYp9VVsy_UmCi1mOm3sAgYG3J5R5vmC-mJDTLnphO_13S8e0ds28cEUNabyjOYiN6QCvAac-ZBV5zhzLJJ91NbbyL_UZgq8PiDw6X4b8SbT26n97wvz90mCfJikUrY1mnFPCaLHmyCrPGo7XcarOENJ4V_NpTq_hOIzZJTKSbL9KbLVaMqmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرزند ارشد شهید سیدحسن نصرالله: شهادت امام خامنه‌ای مردم کشورهای عربی را بیدار کرد
🔸
در بعضی کشورهای عربی مردم می‌گفتند ما را فریب دادند، چشممان را بستند و عمداً کاری کردند که رهبر شهید را نشناسیم. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/453218" target="_blank">📅 22:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453217">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d17c0071b.mp4?token=QfdQd2_ftnGO0FieSoVyOGwCEPazfEWL6iNrv1x0XHMPXQZ7dziQ9fL0KOA2p6bB8DVDut_gEjOncl8T5DcezJjXkQ2YphlhaHaQPrxUrgkoUYiquVVJ--g0L7saWAE0I8cZ04PbcrXVZxwAqxykXaFOMAnwRxJQVwMWd-V1sOwyKsRBX53yeTnU7zouRLihMhtwbNyEWu39IFUD4a5J8YYBISZxFFpQjaRXY0ffSVeb4qVq9kfxo2RJLpdBB-ydvoiL4pBinzRz3-uBxT7GtR-fkSF-wJsbsZoxU9n1Q1AnvN7xAecyMNZ5ayXVHrtbI07p0JFYns4aFwPz8WJexkb-a-5vz92TgNBe0_DLZQ9krwIGWfgoXdGZKEoi9FtnSdwHHY6m8WX_-BIAfG34A8kT3LmtGBT1XBmDgwq7kpjqGZ3BRKaj__-OwgGaIWhBDH6Z5pjcnxHWhtrKjzmslLSotVN-wZ4aPBTWkKigBCJL4E3P_d_gb9CRWURShXF4j6tXq-8li2b15EIEbs9arBNPrfjhCV8hw7Er8Pi9dss60fBwq3xz8tD5fnvRNSKSnTaKPCC1Lv9togwjpBY0tgxX1K4mgzXg7XQ1n3P8Rm4X_kqNYmNgEHxOb5KP-WR0kIrBn-0yu1tBuXXRTt8Hju90AO9Zlp61wXqzO8q0NXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d17c0071b.mp4?token=QfdQd2_ftnGO0FieSoVyOGwCEPazfEWL6iNrv1x0XHMPXQZ7dziQ9fL0KOA2p6bB8DVDut_gEjOncl8T5DcezJjXkQ2YphlhaHaQPrxUrgkoUYiquVVJ--g0L7saWAE0I8cZ04PbcrXVZxwAqxykXaFOMAnwRxJQVwMWd-V1sOwyKsRBX53yeTnU7zouRLihMhtwbNyEWu39IFUD4a5J8YYBISZxFFpQjaRXY0ffSVeb4qVq9kfxo2RJLpdBB-ydvoiL4pBinzRz3-uBxT7GtR-fkSF-wJsbsZoxU9n1Q1AnvN7xAecyMNZ5ayXVHrtbI07p0JFYns4aFwPz8WJexkb-a-5vz92TgNBe0_DLZQ9krwIGWfgoXdGZKEoi9FtnSdwHHY6m8WX_-BIAfG34A8kT3LmtGBT1XBmDgwq7kpjqGZ3BRKaj__-OwgGaIWhBDH6Z5pjcnxHWhtrKjzmslLSotVN-wZ4aPBTWkKigBCJL4E3P_d_gb9CRWURShXF4j6tXq-8li2b15EIEbs9arBNPrfjhCV8hw7Er8Pi9dss60fBwq3xz8tD5fnvRNSKSnTaKPCC1Lv9togwjpBY0tgxX1K4mgzXg7XQ1n3P8Rm4X_kqNYmNgEHxOb5KP-WR0kIrBn-0yu1tBuXXRTt8Hju90AO9Zlp61wXqzO8q0NXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌‌وهوای اربعین در عمود اول
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/453217" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453216">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار شدید در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/453216" target="_blank">📅 22:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453215">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCe3B6ObFCP_H-IpJ5tru3L3l0-OIHoRcRMzF622RFhdozsKlVFykhSdXVz25DZ-jWRkvdlkmoVzo3ZK-Dj8uXTMj4lb0SS5IL4edM-krFCCUbnIwhbxnoWcgFSolkyL21tn3z3Capm7Ws-K0F7dbY-5xCpE5IWzFLSZaWmdHs35h5ZmE9gh8Hj-HdKkmR0Tz9zC57JmohRIzyNgrun9hlCgnQPtLH2oJ3bkRQayPWtyO8-j2uME9iAHCk_MBy7IyqywBr3K85PbE22ayoSgvUiMYArxRwHyWhWf297l6Bpy-JUQSxB24t0TBhL6xbh1OLxueDZhshUM2yv_Kwtkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوکراینی‌ها از ترس پاسخ ایران با عراقچی تماس گرفتند
🔹
وزیر خارجۀ اوکراین: با همتای ایرانی‌ام تماس گرفتم و گفتم هدف ما دفاع از کشورمان در برابر تجاوز روسیه بود و ما قصد هدف‌قراردادن کشتی‌های غیرنظامی را نداشتیم.
🔹
هدف ما، اجتناب از هرگونه تشدید تنش است. @Fasrna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/453215" target="_blank">📅 22:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453214">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار شدید در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453214" target="_blank">📅 22:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453213">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d66680978e.mp4?token=ScjTp0KUUNbsckTqmAWjyvieop5arb6XdGT-1RAcqqhtD035EovNlKXcQP5xEFpDiKzO_Np97TFViVwQf5PcRqhI00wsY4ECJDBQaST6_PY-vLyc-YznGS4Qm4S1CHrrcspbxZcpwOF2-ib-h5ZcVG7lp1i7AiV0LXuusB0nA3V8BiaEwj8TiUbhiujpZAC6agcJkkxACAwNC1lZsuK-OyV3mS3cEF8IQAkbaeG4DgV1rzBfYxNGLi6aIRMs-Xht34sboT_2pWS5fm2Fxw_px3Uibyn2H8AF57pN-n1HAi559TTAnSZm3M4RolSqGWBx0tSMGxt8tkNcEKUaLO5vAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d66680978e.mp4?token=ScjTp0KUUNbsckTqmAWjyvieop5arb6XdGT-1RAcqqhtD035EovNlKXcQP5xEFpDiKzO_Np97TFViVwQf5PcRqhI00wsY4ECJDBQaST6_PY-vLyc-YznGS4Qm4S1CHrrcspbxZcpwOF2-ib-h5ZcVG7lp1i7AiV0LXuusB0nA3V8BiaEwj8TiUbhiujpZAC6agcJkkxACAwNC1lZsuK-OyV3mS3cEF8IQAkbaeG4DgV1rzBfYxNGLi6aIRMs-Xht34sboT_2pWS5fm2Fxw_px3Uibyn2H8AF57pN-n1HAi559TTAnSZm3M4RolSqGWBx0tSMGxt8tkNcEKUaLO5vAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این تصاویر اربعین امسال را متفاوت کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/453213" target="_blank">📅 22:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453212">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0254679eb1.mp4?token=lKCZn3kytRziFpyKyKr8VI13uGppjc7w3D2KWAmO7BMngwhyiF_iMlWLKy5oHLkX-YTKIePCQtrJrNECaM-ElhxYvKxQnCcvXIoortSdcyFJ51XjFso-_CZDoDjn_p5WWEQwweeVc9pAJ-ikWTEukti9pe81c_1Nk_xR4VUAEMnyU5M5xyGj2NWLDbWHqqwFx8ZW0FSZHvJM9KBm2El-8fCNyo5ud2pytXg79cjqU6p5e5V9MdG0kp2J-RgRj4JoEok_PBDIcSuK1Zj0mX8lwFzrBjKkh7K7kzGHc7TvVHOb_E7Js-nALdgTMlq0TlYhW3E7B8KQr6hlBXq0GCIg3VWZ3SlUr2oJqUdtdXY1JO_O87YSR37aUqBkTfHpLeLTd_vN69k9FLQ61KXrge0ee1o0zDBRhnRi2wZJx4KIuaS274jsibXQKp1hhMaS0jopelzIJvIzMF1MpK9s5GQ2NOSNPelG2NLUBqZkX1KeX_x8dT9SXd5tZZ_QRaTP64pqpgXh7gJuRWM4QOWk24kt7inSKaxhAbuYAZ8OXWBIAPABe6iiLWFl28SHuEh1gtkICheW22lJjdflEH-7qIX7Cwu3jjmpatpTLamm01DOp0r4d4GPIfERri3yWTtDFk3iaCtxs-3N6xj-eCwjH1NPKjw03sdW9trx2Q7R8faCgQU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0254679eb1.mp4?token=lKCZn3kytRziFpyKyKr8VI13uGppjc7w3D2KWAmO7BMngwhyiF_iMlWLKy5oHLkX-YTKIePCQtrJrNECaM-ElhxYvKxQnCcvXIoortSdcyFJ51XjFso-_CZDoDjn_p5WWEQwweeVc9pAJ-ikWTEukti9pe81c_1Nk_xR4VUAEMnyU5M5xyGj2NWLDbWHqqwFx8ZW0FSZHvJM9KBm2El-8fCNyo5ud2pytXg79cjqU6p5e5V9MdG0kp2J-RgRj4JoEok_PBDIcSuK1Zj0mX8lwFzrBjKkh7K7kzGHc7TvVHOb_E7Js-nALdgTMlq0TlYhW3E7B8KQr6hlBXq0GCIg3VWZ3SlUr2oJqUdtdXY1JO_O87YSR37aUqBkTfHpLeLTd_vN69k9FLQ61KXrge0ee1o0zDBRhnRi2wZJx4KIuaS274jsibXQKp1hhMaS0jopelzIJvIzMF1MpK9s5GQ2NOSNPelG2NLUBqZkX1KeX_x8dT9SXd5tZZ_QRaTP64pqpgXh7gJuRWM4QOWk24kt7inSKaxhAbuYAZ8OXWBIAPABe6iiLWFl28SHuEh1gtkICheW22lJjdflEH-7qIX7Cwu3jjmpatpTLamm01DOp0r4d4GPIfERri3yWTtDFk3iaCtxs-3N6xj-eCwjH1NPKjw03sdW9trx2Q7R8faCgQU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع ۱۵۰ مشهدی‌ها با رنگ‌وبوی اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/453212" target="_blank">📅 22:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453211">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cce6c3ca2.mp4?token=JIBPNINeWCCoD0aD-fJCne4oidZtRm6XP9gxxbgGnzRkQjhX4FzR89J6RFm2beg7Wn3OPCkq_2yZOblx8BX8TOYueIs7I0esigug9ErylEGpe_idWBEvx8Cptel6PKRn-14LgkVI4mEBtpHUjhS-w-bmsSclutpg2Brqg_7khnJmVPh9qQTx_wNxqVoSSDoq99PvnuGr0rYtxoK7-h5yTzOdAgAHSmcf0eNAHdTIgr1fvJ7Q2YCIpZcbhVvZrGSnFA-Lo8sHFp-d3b6R33RbKOWTn4DghXvioYrhb4NCbYdNgX4TZmYH9yaqLb1b1Jh-i5UeA39aLWSsAFpArI-nkYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cce6c3ca2.mp4?token=JIBPNINeWCCoD0aD-fJCne4oidZtRm6XP9gxxbgGnzRkQjhX4FzR89J6RFm2beg7Wn3OPCkq_2yZOblx8BX8TOYueIs7I0esigug9ErylEGpe_idWBEvx8Cptel6PKRn-14LgkVI4mEBtpHUjhS-w-bmsSclutpg2Brqg_7khnJmVPh9qQTx_wNxqVoSSDoq99PvnuGr0rYtxoK7-h5yTzOdAgAHSmcf0eNAHdTIgr1fvJ7Q2YCIpZcbhVvZrGSnFA-Lo8sHFp-d3b6R33RbKOWTn4DghXvioYrhb4NCbYdNgX4TZmYH9yaqLb1b1Jh-i5UeA39aLWSsAFpArI-nkYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه عالم یه طرف حسینِ زهرا یه طرف
🔸
بانوای: محمدرضا طاهری و حسین طاهری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/453211" target="_blank">📅 22:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453210">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daba502cc7.mp4?token=XAb3DPB4WD8WMHSHYwAUStu5APDlb5Vj9F7QZTi5oNxK_UrrEZ87uRNZ_dGRWlyeYyJbvJesh0t_o3eUuWshvHO124cpabIpRXJ8BkQWw9z8C9HqTNY8JV7g5N3Zo2Xr_PAr5THRiizuFVxJTdkIba92zTCzpEsz5ABuuJLSTR5YHu2n-JoGHE3kxtnjMlKA_fZKBYuOF6jzH-9MO7hFK4rMkl0SdNOgIto1LRJ0vV4nbihq2D3S_2UXeIMrEsAgYAJIL02o_CWHZtgygqxCE3NB1v_kLozu_JuhjGWb-BBwjWPqB2tqGgiamwF5cEQtLtHhBHmgXD-XNFLWkpjbFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daba502cc7.mp4?token=XAb3DPB4WD8WMHSHYwAUStu5APDlb5Vj9F7QZTi5oNxK_UrrEZ87uRNZ_dGRWlyeYyJbvJesh0t_o3eUuWshvHO124cpabIpRXJ8BkQWw9z8C9HqTNY8JV7g5N3Zo2Xr_PAr5THRiizuFVxJTdkIba92zTCzpEsz5ABuuJLSTR5YHu2n-JoGHE3kxtnjMlKA_fZKBYuOF6jzH-9MO7hFK4rMkl0SdNOgIto1LRJ0vV4nbihq2D3S_2UXeIMrEsAgYAJIL02o_CWHZtgygqxCE3NB1v_kLozu_JuhjGWb-BBwjWPqB2tqGgiamwF5cEQtLtHhBHmgXD-XNFLWkpjbFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اهتزاز پرچم خونخواهی در مهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/453210" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
