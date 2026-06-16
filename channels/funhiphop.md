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
<img src="https://cdn4.telesco.pe/file/Wb-Ss0AqSTsFYj58dPUV2mO2qoM213g3lwYFUifnSBumLlKDHE83DeGHfF8TFnAFKOrm6PPcb5YO7G011Hco2jdosLJ1D9HGzFljKNFJ7Pgwt-5tB66NiQyyLxNZQwEmpsPeqn48j8nIDGYDniNTAsJwMoQFFiYGW0xXTzGSk7fjNEmkPES2h4Mw1D_kaAliBZ2tJ2XUOUBM02AdhatrewoRlligoo09ekpDESD_9J9LXsrRfwQvLhHaUlRPTNKcUN_Gv9IvS65waEpurPWt-89mvOHkJH3aSxeRZatOcczToWPfXq_ybKdVIRLrXAL3FxAqngUELrNZEx9ZwGOW2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 171K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 21:43:22</div>
<hr>

<div class="tg-post" id="msg-78052">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پسر اسکوادو نگا   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/funhiphop/78052" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78051">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6okJ6oNRDEy-1WHA0RFLRYQ6t_EW5IYV6sg2aiJrEERYJ4NKUrSDqygVZNo1sKKXVf0jFMhxoc7XCofFjlmeuGlxmtOF3dRq-QUZKubwpmufHcMkVuBQeJySYHptPRGZ22lKsCBc-y0ZA0lIx7O6BDIQWqT7PZQFNZIzPI75_8Kg6bSa6loJL-kxmNhsRW2NdCljt3kZxno-SelBFU7OmudTxW4aDJmTYyxr67DjI8u_gkCwCvMWXX-ia_T8U4hFRs1tUW-Ar9hUoEA7rDsYA35DBhVeuudYpkgPy3n3S7y7PKPzcEbqWvZ_xxf_4xQ5nucXn77GD8PdXhF1sp3vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر اسکوادو نگا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/funhiphop/78051" target="_blank">📅 21:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78050">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نامزد های انتخاباتی در اسرائیل تبلیغات خودشون رو شروع کردن
و جالبه که همشون از طرح هاشون برای دشمنی با جمهوری اسلامی به عنوان اصلی ترین تبلیغ استفاده میکنن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/funhiphop/78050" target="_blank">📅 20:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78049">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/funhiphop/78049" target="_blank">📅 20:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78048">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvCk-grKLUpwGIXKRPKlHBWC2_23wxtuBpxNJL8LP94jObq9yDPeLl4Pf6fCeLx3tZTO1_M70eTbhBccYe8dggT9MuTHmlMKxUt5YRRQaeRoIEUlcmKSzsA9AZRMYo1yhpnPoRQvwLtdMxfmR5yZ9S25V-KqOc08XnMdsF8QHhIBA4DKm2CAttj2UtI0lr5SanlD2g_eb3cZrji1UubvUdufJUfPNaU5Olp8CdWWjmK2b24Fy6Idson-iYCv089zKxAh_udjpndd7XFmh-nPWW9uTTGL7qX78y4Op6jtZZAyqAIi2_Na2MpiZ3KlOzidbgoPuPkPqmc9SkYIzBZtZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/funhiphop/78048" target="_blank">📅 20:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78047">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وال استریت ژورنال:
یادداشت تفاهم آمریکا و ایران به ایران اجازه می‌دهد فوراً فروش نفت را از سر بگیرد و ممکن است تحریم‌های بانکی و بلوکه شدن پول‌ها و محدودیت‌های حمل‌ونقل را برای تسهیل معاملات مرتبط لغو کند.
طبق گزارش، این توافق تسهیلات تحریمی گسترده‌تری نسبت به آنچه قبلاً اعلام شده بود فراهم می‌کند، که احتمالاً صادرات نفت ایران را گسترش داده و امکان بازگرداندن درآمدهای نفتی که در حال حاضر توسط تحریم‌های ثانویه آمریکا محدود شده‌اند را فراهم می‌آورد. (لبیک یا اوباما)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/funhiphop/78047" target="_blank">📅 20:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78046">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رادیو ارتش اسرائیل:  ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند. این حمله گسترده با فشار ترامپ لغو شد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/funhiphop/78046" target="_blank">📅 20:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78045">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSoQAuXWJ_pKIT37qYUx6ZzemGpXhbAMOtb3IzQrFFX4oVJu2cuDtPrkWfkSc_gWRC4RKVLJy4w796erXFGtZRlORiDliRHOFzuJWw_sCGtSF-cwGwvDEEJYcyWnxegSfLMC8frjM9QauoHXlLb7XEMzEqQrXmLQcTnoN0HezdwfoXwDMFwDSNsbrD7NcQHwQx4BXlqc3myfpkSs7zMaetS8ZI_gYzEqhhyRlpnqtKOADDt2c3A4PLqX-NQOaM--C3J6RvRHghYC9XjfHjywKfRGm64hDk3MaGMOwUZf8KnI-aRKsEA2LTD7QZOdho3M-z0uMX6x0aLhCzFcCasL5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله شهربانو ازت میخواد همین الان یک لیوان آب بخوری
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/funhiphop/78045" target="_blank">📅 20:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78044">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZVah-eooDnZXFK_qduNu6KqfVcCqEkr-q3KbqBaiTqNCQdWhmPd25iyleg8rPkKbvJxKrwPXs3k0rXs7WYn69Gnv9RBet1kZ-DkWbupnosvWyiYfu_IQJGTvh3xtULxnhFxaUfgVpsIhuiwQ_4Ls2B8dxpd_n4HAcRLPk0DVWaS6qVtxh-KbVgbjMK4Y1KVtlT2Ontc3SO9lIfvfev3uuSc6trt6RQlluw8bqBy3SHavYO5ldXl85lVHU2EzTpLOKZenlIhSIy-u49s6LgP4WWNEZdXkGj6RHDBn-QU_sOFZrFlt8At18BdcecPPglqjQbMRx0S87LTI8ALD1H4Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوکو خدا به دالگت رحم کنه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/funhiphop/78044" target="_blank">📅 19:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78043">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAn2hLrzK735W-6ZS-RPzyawNRTkPjw_MLT_iTLyFLcKt6pU_Tq5lvSQECb6kx2Ux5YgFJpuseMoziE9psBnzYujCX9uZQDrCSR_PcuIRha7FpTVM8gEAt1NwfTbufqLfmGElnJ-gFYj-GtW6NjrNQl2JlNQnIJaii_VVN9J8hlgpmRzqGEEfh1h2mEEh5iAbmmb9JCcfQYWOaGrhxp--rNX8LY-L2En79pS1SEo5Pt43xYlxbx3xqsz6ca2KyOT_jmkW4h2K-iqMhC9WXioeUOOuBbP1shYHrCTa7Uj_xuxHLzQdRGT1VEJ9dzAi29e97HMUeK51X_nMEu0y8DAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/funhiphop/78043" target="_blank">📅 18:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78042">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLx3NXBBe8aD7ntYuNxLU8G2EVqwK5VQxUCqHhoL1c868hVHo9lHFqOzN-EAktYvy4FvONQ34PTsxX2EC1bp8HH-sWdc4gP75-v0BFtRAgbVLTNUeI0ho0vELBnevaeRJ0Ovzea8MeJmeNxl4p5Aoc_BBPtUXTjlldXb4NzyWmo0yYOgV3r2drKRAPZV0jMR8lAZeyksHnPXR9ngqvCUxF9mA7Uvz2LAUiPcqVJJY2wh8MJ5rQ_eMPpKsmVmaXhEccP1J8sRCQ3SErLFw7xN4Dt7VgO-NKWyqsByTO0UgVCoT46zf3O4doDFfGoa3oYgmmi-T9ql_vf97aKGar-mCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همیشه تو قلب ما میمونی
🥲
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/funhiphop/78042" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78041">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/funhiphop/78041" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78040">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjMq2oSlpT2Ow_8gTO2o-Z09mVksn83Eac22qfpGGHX1U73YtCWsgEsZXaBVYXWtLqf_WRSDgqhRToHSniqlFmciE-uGQAG_zDu1cr7-PaOQtGaIhGd_DHKuo9sAyVSmfs8QXPvmhvHHjhHcVYfighQG39BLH47gZZb1_kvx48yuHd_8zcJV-F2CyUhnIHqLUjgRtYXtdsZttwg7bde4OYdXshGCC00E2KgIPQeQwKJ2o7cAiJ27Vti6OEBWIDV8c6qN3LyuwKPj1x8N0_uPLwj3obsmPQa0yPanDugM7DIqdqs-J7MBK_T8uZnhIqP72N7NsluRq6pwj-woMM0mfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g26
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/funhiphop/78040" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78039">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شایعه شده که ویزای مهدی ترابی و مهدی طارمی باطل شده  باید ببینیم تایید میشه یا نه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/funhiphop/78039" target="_blank">📅 16:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78038">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بازی ۳.۱ به نفع ایران میشه اسکرین بگیرین
👍
😎</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78038" target="_blank">📅 15:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78037">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">زندگیتونو بزنید رو برد مساوی نیوزلند</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78037" target="_blank">📅 15:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78036">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شایعه شده که ویزای مهدی ترابی و مهدی طارمی باطل شده
باید ببینیم تایید میشه یا نه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78036" target="_blank">📅 15:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78035">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7f045c16.mp4?token=SelYTSpwXNffNH6q32vOMuPCb_uIhMj1GzrOstPIp9Gq15wgzZFY1hLd7-ey57k4Al09crl80WfcdfNyB7l_KsTbCBBAsEHrqbjfkcK_VWf_TG3Sx2n6Dr7H5umzxUAxY97g3NNRMWda6KfmhV762gJyyZA0wxP15vNmLsTgN1hkYENJqCzv89m1IeX52BCmPVfJ-fIIPXuoN9lvdR8Yl9dIlsl0cuGqKWtuymb99kgVrbz5ak02JzecwE3164AY-QmV4NuZAEZcGWD83FQfea-FCZf_dQ6JbpOlL1FiUGGr2DOS5j3qnsWoQZbIk7Zowqm5AJdbxlKEaeGTLTubew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7f045c16.mp4?token=SelYTSpwXNffNH6q32vOMuPCb_uIhMj1GzrOstPIp9Gq15wgzZFY1hLd7-ey57k4Al09crl80WfcdfNyB7l_KsTbCBBAsEHrqbjfkcK_VWf_TG3Sx2n6Dr7H5umzxUAxY97g3NNRMWda6KfmhV762gJyyZA0wxP15vNmLsTgN1hkYENJqCzv89m1IeX52BCmPVfJ-fIIPXuoN9lvdR8Yl9dIlsl0cuGqKWtuymb99kgVrbz5ak02JzecwE3164AY-QmV4NuZAEZcGWD83FQfea-FCZf_dQ6JbpOlL1FiUGGr2DOS5j3qnsWoQZbIk7Zowqm5AJdbxlKEaeGTLTubew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78035" target="_blank">📅 14:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78033">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXtk02OVHd3r-o89dz3Iu7eryjb9HDLqM4xGjFf5f-JE6I2uLobzwkkSSv81hp3N0T_kzP9akVj6jFO9O_BNTSpswlSkbirttJ-OJnfyjR2zrQpufUMECzp53CxaykxE0D_idueR5hGWz2P6tRy3Gz5lKK5Zs26DvHopkz7PG8GyvdSH1hH4ZPVIuaRO8yM9lzvE4zQxapsj0A-kSQdMnd_8Z-bXBipPYUjYKQ-FvxiOKuJUDxaPTW2GOweMGghaY-ARwL6pEJn9rcQsjj43XtZKFK6h4wm-SjGuLrqGznm2x3FrwCT9F39G7w_vpKyK9ZdwMlwPtfqXtj8_xhaFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=bLk5O_TOHGmVXxnoyAmNMnRwU6bJr8_42yYRITnpN0NFoUqaHZwnQO2zOXh4bZuTJLCHDmIIOJsRpzZ-Bq2sivnwitUvglNcDhwE_--B9kWpvUm0ZZ0rdEutprkUdQs8TWSqBfX8URMsEF4r9Hcwgasag_oIYCUjzxObCOJ3w05bOu2mEFbanEZQw6hw1yfWBK6OY6n7bXCb5q-vsVy0VXz3AwkW4294S7NO1mElwUa1oudBohEo803406jXJ-k8Zm3HV9fm1S_EmRKOlaXfGJFFZN7AnvLGVjRBvzhEUQaldG7tHSucBaj4XBnxVn2PQ8ywkcwcuQ-BIjJaMKLqBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=bLk5O_TOHGmVXxnoyAmNMnRwU6bJr8_42yYRITnpN0NFoUqaHZwnQO2zOXh4bZuTJLCHDmIIOJsRpzZ-Bq2sivnwitUvglNcDhwE_--B9kWpvUm0ZZ0rdEutprkUdQs8TWSqBfX8URMsEF4r9Hcwgasag_oIYCUjzxObCOJ3w05bOu2mEFbanEZQw6hw1yfWBK6OY6n7bXCb5q-vsVy0VXz3AwkW4294S7NO1mElwUa1oudBohEo803406jXJ-k8Zm3HV9fm1S_EmRKOlaXfGJFFZN7AnvLGVjRBvzhEUQaldG7tHSucBaj4XBnxVn2PQ8ywkcwcuQ-BIjJaMKLqBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون وسط محبی هم داشت به در و دیوار شلیک میکرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78033" target="_blank">📅 14:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78032">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/be0lKh13Bt1L8CSRdvKq9CXbYtZTWI6TlLH-KqWAu_JtID1IVZXBzk1dJmFTnwJjt3ryAyjzZKeryKsMFx0sgRKSTPTLPoWVsCies-NEdg1EIjlvKohusHcaSoEKmT-N8fzD3EbuJNuq28F17lMw9DeyYp0-bpVu8Sbd28ETaBaO5V92Bat01bRMB_3wTaRU6l-bpbnaVYRQEFbBxPf3zoPyJ3VJQDSvj9J7YG0Znd68bOJqXXRQPiHXepJgCE4jsTXdZ9lhcOXl744D3YqszTMgsdRFKmJyguYn1GR8mamcqKVbNRt18y_0D3r6b8fsatxXomrQeaqnWKBtzexWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78032" target="_blank">📅 14:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78031">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78031" target="_blank">📅 14:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78030">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78030" target="_blank">📅 14:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78029">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">من به اسرائیل پیشنهاد دادم که سوریه مسئولیت حزب‌الله را بر عهده بگیرد.
@FunHipHop
| دونالد ترامپ</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78029" target="_blank">📅 13:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78028">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حکم اعدام جواد زمانی و ابوالفضل ساعدی از افراد اعتراضات دی ماه اجرا شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78028" target="_blank">📅 13:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78027">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حسینی با یزیدی صلح یکساعت نخواهد کرد؛ قالیباف و ونس توی مراسم امضا حضور دارن.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78027" target="_blank">📅 12:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78025">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hI2vN4yrd-1gv74wIXuJMUO9xNTQmgjNOS11izFZma6_ynfQMOnVqbHnCWwbr7-7SWkXRUh0dbjKgrPQ-maICewj5FPCdYdPXdYQ-XXxMWgwsZlC1q8E3zbTEFDDDrsaDcvBr_v-SwPMqOikwZ_sByoieYU657CD8DLkS_Z6vqG_RvInV0C1z0-kHxhLTk0SBN6zeA8DiStm6mTF7DVBZ81YjRONsXgcj-nZj5sh8dCn2yKSd_EPnH-sdpibwWzfsIUnzaHbdAl1ZjWvQvmR0s2oWQg8vvLIQpd9JKmAUOmI14c0wbeABfoy0Jfrd4I-geeVJIs889DUBdsGEWMa6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها دلیل باخت تیم نبود این اسطوره بود....
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78025" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78024">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78024" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78024" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78023">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4CHoFPJ03sOB9q8hQzk1Cy2DM4KajjqgNPFuryS96VbXV_U0xTTMkcyTIID31RkH9angbD54SCmQmOKAwHPo2bn6ovhacrNMlB973JrAOiK-mtdSQZ4gHTlzZYHBV9AYohWUoYPNAIOOHwfM-CmyXYDioDDbrTHKIA_lFivXFLt6h7N4cpBkfhjPlaRP2Rms0Nq7eI8Feki2S6hO-X_HOpaDUkx3NIYx70ERhc8NZFmgmhGajRamrDk53xg-FUBch-NKl7NV0jslsfUru16iny0H7X39H8mZXTa8EbEAmBTCuZzidqSz-QiakGdN5_QKC-pOemuGpgkNiaCq3RYtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r26
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78023" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78022">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بیرانوند: اون دو گلی که از خط دروازه رد شد متعلق به چین و پاکستان بود و عوارض داده بودن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78022" target="_blank">📅 12:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78021">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بمب افکن بی پنجاه و دو آمریکا تو رزمایش سقوط کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78021" target="_blank">📅 12:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78020">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">۲۰۱۸ بود ساعت ۵ صبح داشتم از گل خوردنا تیم ملی حرص میخوردم، ولی الان تازه از خواب بیدار شدم نتیجه رو دیدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78020" target="_blank">📅 12:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78019">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFnBlU1x_rErgoue55amHUViqvfRYVQ3ix42BGKA-fcEXSzyIeFJKEcvY4TAX9vheiw5WYrbiuZ0JOxduPZhrmWGCwCSRscHBu3zvifZA7JB9bob0y-Jfhv_4xUjiQCoy3PHMhKzvNqDgi0e1Ydwm2xnrgCYOT0_nkGVPkaJsvERXihkuOYGzHDVWgnzoTlcs7AzST0C1vI_jw4vWt6G4P0_iJAbg5-DEJCZ1jJ_m5P9gX8yslgOivBoD9pUJpaYQSFZc9xyE1nb4SqiYHSFHOX12AxfiRij83YChux5hYUfLnLsi5_ujH5NMb3RBQxFHMXnMTKqlXf7XESRuCaWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Playboi Carti
📌
I Am Music (Deluxe
)
📌
I Am Music
📌
Whole Lotta Red
📌
Die Lit
📌
Playboi Carti
📌
In Abundance
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78019" target="_blank">📅 10:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78015">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hhoieRAwoQFy3av7CkJMNb18xRXsVmgDce04d6oz9dC7KbZ4SnV5-xvaVJ0ofWPg5T0M0T7rCaEzBoZAnUUsd-URZr8L4iKa1dk4BYWFNVIIEoVGadH1hU27zeDW-NvFifMbzoiRMz7ejsEDxBxEt5nJyd7zKQ_5dPKWvbBmKNPx5vghy6asTwzNn-8H9_LUywD-zOKZFDK2AYYBsE-Wns_Lrhj1WFEt3AtvjpwJulhKDEZAaEgW8nMwA_8xCTcYj0Z2mMPgLpOHUiKHqa_xgaz9w6foJio5Vrj6BCZwbv7ojvzJ3C2gjiTlnhZh1NIm5FeoGGwH9eteQFcqm4XlVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4XUOYKtAlDO4d0ye52iU5sF_GzuxaU8EZNl1dAFOpB3zJef8sQ0uU3maP_2jtviGtjNT8f7Ag4n208Oy58sxpwDMtEAUgh8s2PP4SmPU2cFx2p1iw8YDw78YtJyDEIdjPBOW3wgnfLYgPZU-Jj85ewSAP1VtOF6VMqsRGLIhDwIAN7jjp4dP_SpBQS9vlLly1-zTJUbRVQqhWHyS5plVtjaT5ZoNdXAGmasT5NGqN9i5GEzCX_5dNLutE2n4xJernb7o5L18yFVRa-WtqYPaLhopiaEaVuCV7_pUBMgee7fO7djheWAVylibkixqJlHf64F-JFmVftWrBU_s2uczw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78015" target="_blank">📅 08:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78013">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اینو یادت باشه که همیشه تیم‌های مدعی قهرمانی جام جهانی، تو بازی اولشون ضعیف بازی می‌کنن که تاکتیکشون همون اول لو نره. صبر...  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78013" target="_blank">📅 06:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78012">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بنازم ژنرال تیم قدرتمند نیوزلند رو متوقف کرد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78012" target="_blank">📅 06:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78011">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بنازم ژنرال تیم قدرتمند نیوزلند رو متوقف کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78011" target="_blank">📅 06:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78009">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شوت سعید عزت الهی از ورزشگاه رفت بیرون
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78009" target="_blank">📅 06:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78008">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حسین زاده جا طارمی اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78008" target="_blank">📅 06:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78007">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نعمتی چقد دلقکه
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78007" target="_blank">📅 06:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78006">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نیوزلند تحت فشاره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78006" target="_blank">📅 06:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78005">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">منو بگو که فکر می‌کردم ایرانیای آمریکا از ایرانیای ایران آیکیوشون بالاتره
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78005" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78004">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">محبی گل مساوی رو زد
۲ ۲ مساوی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78004" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78003">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">از توپ لو دادن محبی شروع شد
با ریدمان شجاع ادامه پیدا کرد
و با جاخالی بیرانوند تکمیل شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78003" target="_blank">📅 05:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78001">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">واایییی گل دوم نیوزلندددد
🤣
🤣
🤣
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78001" target="_blank">📅 05:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78000">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">علی علیپور اومد کارو دربیاره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78000" target="_blank">📅 05:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77999">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چرا سکو ها خالی شد؟</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77999" target="_blank">📅 05:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77998">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آقا مهدی باشرف (
😂
) جای آریا یوسفی به بازی اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77998" target="_blank">📅 05:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77997">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فوری از سخنگوی قرارگاه خانم الانبیا:
به زودی به تجاوز نیوزلند پاسخ میدهیم!!
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77997" target="_blank">📅 05:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77995">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qozxQwWVuPWxXg0r0q3H9U1kJrddmF0Bc_iEm-m_GuE6M6b7Hn6bxiUrYVTMqtCgOL2WNk4NzCbNwmhEX_lHkfn6dG2Ppx69DWkrFvt9MdgfLXneNB6tCu_ja5gNMqc_6CSsJy9heh-8qjfZ1ci4s_UWzf7hmne4vCL9ddhzxoWBdDIcFTGpX6CIpdMPgYclgdlkQtavE16WY0B5U1C2eq2qwzLkdoiggjNHudKTwL2U1Aqqcq_MU4As1G4I-hfXG9esqJUezkzeBki8OPso_-JqK7Ndin5EuQOBtHynbUF9o-xJ_TaUbyIuE4onuKQu0_Izk82quA7hXK7JHghVYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب اولییین بازی ایران که  داخل ورزشگاه بردن پرچم شیر و خورشید هم آزاد اعلام شده ، اگر میخوای بدون سانسور بازی ایران دنبال کنی حتما این کانالو داشته باش که تمام بازیای جام جهانی کاملا بدون سانسور پوشش میده :
• @
TrollSporte
• @
TrollSporte</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77995" target="_blank">📅 05:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77993">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نیمه اول یک یک به نفع ژنرال تموم شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77993" target="_blank">📅 05:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77991">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ریدم علی نعمتی زد ولی افساید شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77991" target="_blank">📅 05:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77990">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گل برای جمهوری اسلامی
رامین رضائیان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77990" target="_blank">📅 05:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77989">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ولی شوتای قدوس>>>
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77989" target="_blank">📅 05:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77988">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">این چه کصخل بازی بود گلر نیوزلند دراورد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77988" target="_blank">📅 05:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77985">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">استایل بیرانوند دقیق مثل‌ بهتاش پایتخت شده وقتی ک سندروم میمون گرفته بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77985" target="_blank">📅 04:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77984">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lh46uswATDSNet7bnfUTKkpJ-V1H2oREdx94TAgeZ8jXQl6LszKTaYM8d_GYw37iQPGb9U3tFRcP2sSMPSi-A_06iOpBMXO57PZsPG2D3BjDUEmQZPzSB6R3GrA_q1w-U9yTmqm3jiixwCc-2xryRUHkSoTb4ayIOibDa6QjnCWTVy4Z6-6UdZL7Yu4Nu2w6ymMQ4i5xWU7qvAfWHrMRqUYjwidOhiW0798qaiAkAnSCztwaHOf6_xGmXqCiKlAcZOecm9n-5v7veYE8Cw3XLBr24XVbpSo-LVGwJ6LamIGDfLGEcrtdtzt5NJ4QGY6lDAB9R8-Ey6Eb5yoiN0rzDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل خوردی ک جاکش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77984" target="_blank">📅 04:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77983">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عجب سوپر گلی زد نیوزیلند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77983" target="_blank">📅 04:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77977">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بازی یک یک تموم شد
بهترین نتیجه برای نیوزلند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77977" target="_blank">📅 00:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77976">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">محاصره دریایی رفع شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77976" target="_blank">📅 00:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77972">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عباس و باقر فقط از زنده موندن آقا مجتبی خبر نداشتن و سورپرایز شدن وگرنه همون روز اول جنگ رمضان توافق شده بود بینشون و توافقشونم ساعت ۹ونیم بعد از ۳۰ موشک به بیت رسمی شد.  - تغییر رژیم هم از نظر ترامپ همینه نه چیزی که تو ذهنتون ساختید  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77972" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77971">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYExP1dKumx0kMlKKURFTDPK_rkGDYMSfz2ckIMyPxkRx06DlObyTZUS0VjX3hd46lW14VRO4gZi9fXpYY_tCqptaw2C77JdwKLFbAHPsGQjfb4NF9xQOE6WwtSooumFEUbIlFHgTRulA5AKWrfHaAA0PFWC1kJJIUYPao_UIiqKxnQvQpI6xMKXfgRxjEjJJ_EyPVLTAZiGHOq9crNzkAAl3Oy5PNx6SuZ66UDKQB1FM36Q1aoDuqUlHx1ObFvY07cF_gLd6EgKaMPpJB-MPw2TV_FwciMXMtV_x3zDjA2berKE6fgj5882k0jPQ0H7gEW2uFzWvcZ5KUhU9NDu6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس و باقر فقط از زنده موندن آقا مجتبی خبر نداشتن و سورپرایز شدن
وگرنه همون روز اول جنگ رمضان توافق شده بود بینشون و توافقشونم ساعت ۹ونیم بعد از ۳۰ موشک به بیت رسمی شد.
- تغییر رژیم هم از نظر ترامپ همینه نه چیزی که تو ذهنتون ساختید
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/77971" target="_blank">📅 23:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77969">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaRBwvTjOZQDdfpGEWIcJ-XvGHKNbpsN-yJt0nl0hritFKFe4UPGQH-nuveHN8weA4xYwCa9rZaOtvvZzzP4KIaP_O0GWjY2hY_LeEjlbU7r7HTsMzZuYEFjYsiz5kRg3oAAQuOW1y6gqgTK9azgvRsCdlGlBWM8lWNON486QO9CCWNFZpR3EJMEDBj22oAt5CtG8vCpdgD9A6TZSOjcCUo7XWOwpaSZ5AnLnN00__n-jgh0x6qcze-tN82dhkVgT2xIi-U8LCpj7OybxJ_PvX6W-N5efpSfUlzcnGTYNglGDxqos7bQZBAdJKCoARKcmDgStEJhq4-oL1QcnBtHZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایان یو واقعا کونیه پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77969" target="_blank">📅 23:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77968">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVo9oLmxj2h3AZyxkjESCk3C6of3vY28zC9dK8cxz8W35rsDIQX1KPK2pkXVG-XVqKusY3VRYNbvarIwFWMkaHvFAf1KZlBvefbO5DPirDeUlWJZHnZJLdhEuXoxf4ET8tp0xNYY6LfW5OUFjEPjw8XSS2_HxZR1gofh1N2Z1_RwIQZKGIAMfnEq7jWTZGPy0LUDaq2dY0ht0xGgnlHzZi8R96zFydQSbI5XjFF6iEoYG7lXOKIWkkF6f0IHTTfI7neJlobA-B759Ixu73GPhXIH27QUJ5_p5SfYR6-22SU6dK9feDAi5guJI8jtYmSMGDoBlc9eUJ_FG0fuxAlXlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیکای قشنگتو بفرست باهم گوش کنیم.
🎵
🤍
گپ پلی لیستمون
🌓
https://t.me/ORGplaylisT
https://t.me/ORGplaylisT
https://t.me/ORGplaylisT</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77968" target="_blank">📅 22:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77967">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">امام عاشورا برا مصر گل زد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77967" target="_blank">📅 22:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77966">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">زندگیتونو بزنید رو برد مساوی نیوزلند</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77966" target="_blank">📅 22:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77965">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">اسپانیا بدون یامال در حد پرتغال با رونالدوعه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77965" target="_blank">📅 21:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77964">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کیپ ورد جلوی اسپانیا متوقف شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77964" target="_blank">📅 21:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77963">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ریدن تو این بازی باعث میشه اسپانیا خیلی وحشی شه و بقیه رو بگاد و قهرمان شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77963" target="_blank">📅 21:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77961">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eh8U8R2JBpZxJpRJ9mCf97iGmEBk6HF5aYb8n2FiBWiWOP7YxDH33o4QDIE3_sfkGREaY6hWQxr4E9HtfYVV88glpLFhGeyD7e-nv3aoNsGqRoLEbktcv__t3v3yTPwfFO5qtEJD_dlB76oD_XQ7keF_aaJ7YGtU0SiiIcCDmyycx0XLSr7jJe38qUK_QIDhPAKPOf3VFTy7JbHI_fNxFVxBu2Vl8Mpdemdp0LPuBBXe5oVuXLOK_PZ_0j0aBVMeRUEKWnN7nJnHB3lEUvxCMjvKj86c2KjEY0biw_YMEf7HJbZHlXyI-4_hKtqXkD-lbDHesd-xfsScumAsjVemyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه جدید باقر شاه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77961" target="_blank">📅 20:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77960">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آپارات اسپرت با ای پی خارج ایران هم بالا میاد جدیدا، اگه خارج ایرانید استفاده کنید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77960" target="_blank">📅 20:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77959">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">قهرمان جام جهانی ۲۰۲۶ خیلی ریدمان شروع کرده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77959" target="_blank">📅 20:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77958">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آپارات اسپرت با ای پی خارج ایران هم بالا میاد جدیدا، اگه خارج ایرانید استفاده کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77958" target="_blank">📅 19:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77956">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فردوسی پور هویسن رو آورده برنامش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77956" target="_blank">📅 18:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77954">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vfx14We3O2k2vAbYacOU1exT-3dVYXPdTWU34ooiZB_xVdHED2hfwGqZZePC9hHkjFEinuL59x8j3VgUygrjFJsYpd5YV23zY88P2XAGXaRHt3TGWKO9xeQqZZAo1mgGyKe1QOeKJXuE2JxQwsBSX5Jd5Fc3ZhOrciS424UvW6LLm-OduHQI_IrZ2UT3m22OTdYTymMuFzb0uDV12p50d_1hbGCArH5PKyGWlHMgsxMUogSaVxQUnJpYmoqoI4Z9z-0WnAPCmGdkPdtNpYpE3HfAwzy5rEoCFZZpohINh0ifbaFsveC0ejU-P--2pvw4fdlJTRns6BHLTYJfALZHrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GK7VGMm_tQ4R06wFUtIzVd8pOeRC_fKjjMKJa6-_GrbzR9iNhOkiIfwbg-569RpmRzx_R1U1WIFjtqmJT04f_mFXPOTG4X4zM4zeii4zJmKM-FCK0vDQCuyqKgeMYNVdEU2scNkL4Om9JWO32jS7r6rUOR2vQAXpT_B5ySICnZer35RjKRss9va99uj8xf8p9qrWykmOVLlHMruOpzAY17NS1NHCAZwEtmD6lIb4ohT1MOqT8hbaMJ8uZfP3y-zT_98IOs6yF7o-khapDF0CUE6aMgSnWp6BrR8dPXMYHas6HzwX9vLJuZV9Ei3CCJQI4kvtywIvbneUV9scaYd3ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری شوهرش همزمان با استوری خودش رو میبینید، خداشاهده شوهرشو نبرده عروسی
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77954" target="_blank">📅 18:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77953">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsU6MKu_lkSqxK9gjOvfQkU6XT-DG1ecE2TK32tLKYJcppfMArPBgP_Q-c9qBZZByBMiyJ9wqFzgMG7-ESMUVhrCIKU6ea-wvbL55ntHWh6PwUwcIlO0OyFHnL1AgTuiAQQvxueRBnDWPcxIX2UHjq4kbWz6THmv0Pebl0Qyjvum3TkjGaJoSKawkwr-U0UvVi1VrdEurejiCIoK8PeJ4JOb3rl4tFCJXfZ5HpEyFIzgjYdU5OYgyEKYBPFANVWOy2CtmgvLaSBX7N4NNcNjk-YjmIrBKkhX9MWDTlpYfrgj-04229tAsfdfu1MN_ehTGSl1ix5s1Ha-wde2RqUfNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77953" target="_blank">📅 18:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77950">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yc2bUdhAkNkL_RTopNOAlgGoDOkO7DGljl31di80mrEWXet2tS0MuX9c1wrG3EO9WOVbyKPjgiWU_sUNQjO6lmpX6Ft_4bAGZDO0VRCo17Rr2_f4sIAczalulEx5L3eBlqUeq3xXxo_yGXTGW1F9fdb110VR5kp6IvB6knL51ixUZke4HgsFedG8Lxc9E-BL1ukdUjaANBfXRWrSkWpmFqeSIca2QR7zQKHdmu-smCw_vV0bJjOuGRxCTSUR_BLxdXlGql3w7NXkp-w5ikJivVswWSHcOS_3LNA9szMhPXuZM1YKuCC8gB31Em4-woMQxRviIeg0E9VZfAiV0hB-CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مونیکا بلوچی ۶۱ ساله
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77950" target="_blank">📅 16:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77949">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2qwshxIU1DIihGfK-Dg_AhsUfTRyJKeIYe-rqR5Dm9-YcQiIKP46mh8KHORh9FWtD5T48pGpLodRycdbwX0uXuKYU90a3VPir39x9hL8kHELOeQkSZkDNdFeaZIU6aVnqOc7n3ZltgTzDxECC3tJD45YRdPSnQgXrK-7ppjorXZKxV4Kx54zTLuEyiDNrFdbLhfsojkcPahC2dktAAJuNHHz9UK5p81IVQYlwZuWVvJ2K6Lj7xgOR2k-ZYDDqazIllQbHjuqKYI7wC5T2IdFSWVht8K_armOMGMPab7_xd1Dd9ilmsdqy68fheJ3PrlLtDHvtqx2LtTsWqRstwGfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
ببخشید دیشب کم خندیده بودم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77949" target="_blank">📅 15:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77948">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SD6eF7R5_msBTw56cuuJIxaDr3avbPn5nLnrVi1uAjpBQ3ENuOqDFYqMiemeuQbTVV2x5XjuiO5GMCYoupOb5-_Lo3t_qAqOkdhygEqifm1V7KlqrO0uQE1xuJNa8-JN1maldbFR8gYIroFVpI1crxRVRUZU-f1zZ_Bup0443UzdheeYJlQzm7orO9gIzZ26uaVFg8WFTG3cKEhPkfMURFyePxR8AsrYpcxuaQlvaUiZDMsH6vnaTYN2lmAixFQchh3bxredo0tWnTYAmmcIa8ypwC6KxzLnhBTHP3jYywCTKZAbJsrLnbQi-RPywXfmm0E322WCKIWReh9_STEmYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو وصلی؟ نه انگار کانکت نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77948" target="_blank">📅 13:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77947">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">در چه حالید دوستان؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77947" target="_blank">📅 13:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77946">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یعنی جدی ۳ روزه چارتا بانکو نتونستید درست کنید؟ بعد ادعاتون کون خرو پاره میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77946" target="_blank">📅 12:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77945">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3DyG4j9WmZGehsf1xeLyTu3Pt3DXjwkJSXUtC78K5jFkfg6F7EvPq_zASReRV6cgWe5u85cb2ZC1RYm23J_ljxsp3DmTq9xZ-1GAY-s66N2yKyswm9hJIdkAdx3gF22VtcoUK2UJXv_2ak1aUFAKN4eKC0vyJM4LQp1FlsVAZHD5oc_onYWz0zc3dfoJSL3i6JYzKtbS8szEWXYjil6knOE_CDr8rPR44s-GXhS28le3eRL68wDTHTIkREOoItnLtWMB1hOXqLgBBmoVxU2Ee_A9MpBqo1BeJe5vF2iQXCASzhERLbDJi1y2MSTQ-3AxvZaUg7J4vVmgyu9W_U9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید آپارات چنل یوتوب داره؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/77945" target="_blank">📅 12:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77944">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">میترسم حرف بزنم رئال منم بخره</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77944" target="_blank">📅 12:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77943">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">میترسم حرف بزنم رئال منم بخره</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77943" target="_blank">📅 12:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77942">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78832f0cf9.mp4?token=Uo3cb18IIQKugJzdPNWBfROJnoYffzYIvYWOpt8Hiv8DL_ipX50mo3S8hThgxjAC8vSnSvICHwQxAv5Vsg_mPkSGtM_OOVGIgWj1yaJZ09uj_ysPG2yybVslybCDHxLtBqBBbFU5jdlrb6uFfAtasWl4yfRC_VdfVVr47JSJweDxge5YQlk3FRoTrMR6_y00UthmESvpxC1vwIqffMx8rwIB_6k4pUBQ_GpP-90iA8CqHOoQ4JQDr9wGSzn6RaGNZHV1bkByDy9gbDisq1IIFQ5rUXluSOD5k_PGFQBtng84c8v-F23UEF0ff7Gwp0bgfz7cd0XtI_lSuKx2WTRzJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78832f0cf9.mp4?token=Uo3cb18IIQKugJzdPNWBfROJnoYffzYIvYWOpt8Hiv8DL_ipX50mo3S8hThgxjAC8vSnSvICHwQxAv5Vsg_mPkSGtM_OOVGIgWj1yaJZ09uj_ysPG2yybVslybCDHxLtBqBBbFU5jdlrb6uFfAtasWl4yfRC_VdfVVr47JSJweDxge5YQlk3FRoTrMR6_y00UthmESvpxC1vwIqffMx8rwIB_6k4pUBQ_GpP-90iA8CqHOoQ4JQDr9wGSzn6RaGNZHV1bkByDy9gbDisq1IIFQ5rUXluSOD5k_PGFQBtng84c8v-F23UEF0ff7Gwp0bgfz7cd0XtI_lSuKx2WTRzJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول یک قیام خونین رخ میده نتانیاهو و ترامپ وارد جنگ میشن رژیم جمهوری اسلامی رو میارن پای میز مذاکره اورانیوم و موشک و رهبران رو می‌گیرند دو دستگیر و تفرقه بین نظامیان و عرازشه و بعد سقوط با فروریختن رژیم از هویتش اتفاق میفته  - ۸ سال پیش پیش‌بینی های مانوک…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/77942" target="_blank">📅 11:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77941">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بلایی که جاستین سر ایلیا آورد :  @FuunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77941" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77940">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دیگه زن مانوکو گاییدین هراتفاقی میوفته یه ربطی بهش میدن</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77940" target="_blank">📅 10:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77939">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اول یک قیام خونین رخ میده
نتانیاهو و ترامپ وارد جنگ میشن
رژیم جمهوری اسلامی رو میارن پای میز مذاکره
اورانیوم و موشک و رهبران رو می‌گیرند
دو دستگیر و تفرقه بین نظامیان و عرازشه
و بعد سقوط با فروریختن رژیم از هویتش اتفاق میفته
- ۸ سال پیش
پیش‌بینی های مانوک خدابخشیان.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77939" target="_blank">📅 10:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77938">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مانوک ۸ سال پیش در رابطه با قهرمانی یک فرد ۴۰ ساله با لباس نارنجی صحبت کرده بود.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77938" target="_blank">📅 10:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77937">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QO731uOwLdAk8_IPH_cABowFuuPCxwZ3DmlRaNAgjMseQRV_jnLOoZLpf_ivE33tXFgkuyBRoHwPCOW4W9f0veTdVtDJlh2cIL9HWhejm9mm46QJHNv1jP7jSPCbfqTfEQp7YgXYU9WkgqoVApjI-JewRYqOr3SkDgNvPGv0Vov3NrJzty1yO-XjfpApO5Y-yUjusYbdVbmewSyNq7W-omrf49T9Qqzw3rTPBDx5YfFpwg5Flbi6Qk2ABNFrQia3WmV0hDvbk2bgqmRo6wbwEVjFpY_QoMEzrQEM733orwjPetJr3EDNZ6xY_ha7cbfpGQK6Xm-OrNunRHZgu5MgiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلایی که جاستین سر ایلیا آورد :
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77937" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77934">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1GWjaMSBpZ7YswX7Ns3nTKVyMBL_UO5ImJhT5_RqoKIUSf5duGO0mdACvnDAvhN1RhYlgdhBQoC0PIz-_qrFRBLfvLrAGMk3GyYuP97VLoglPFplF9q_rcz7ekOC9X7oNfibLJ8fnl8wrQ0FJ0KHHvTqaOuJLAQh_Aym_0vAJsVoe7i27BoSJwUUziCJVCnw8zZ78RIaUz6e9bOHXD-pT93ogoEv0yF79j_6NfwA3hu_y3gdL8AMNnjb_kcDqLmcmVNdrpSs3TXdmbqcSpdtQ94pUnN9sMezJ2xB4ZX_N5XM2lCi_LXkeKQsETjMLV8_81oRJQPlz-sjVcpIXBqrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنده خدا یجوری داره آب می‌ره که انگار با سیناب رفت و آمد جدی داره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77934" target="_blank">📅 09:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77933">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">توپوریا مادرش گاییده شد و تو پایان راند 4 دیگه گفت نمیتونم ادامه بدم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77933" target="_blank">📅 08:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77932">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جاستین بنظرم تا نرسیده فرار کن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77932" target="_blank">📅 08:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77931">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fi6iy4YPn9eCLMeV1y8vrT01HUOQqzwmahEy-Wi3qUF5VgpUYxn-tuLt2HMx8OmvUVJvoCNCZiZiO0-b5B6AKZuzkDDdIXpi8GlXmMnY2Hj5ZglwFZdnazxLGqOIhhilxfvmATqEkpgBNq9ibaQxqMBOf_YCW-oxFlOssKO_xM4hZccstJhwo6BPNAGI_gahP0cvep-JpOeaeNEiwrc7FWH_BCRYBTSnnllN6kVxhAPRG0VOYDA2h34sYYh3Jlk5NScGpZDFq8z9Q2VjbRWirAU3jCyQzNjQJaLJuWPIBogNY80TDEnMYk-w_Fqk-yJbfbo_OUknmTrH-DyJMcNivQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاستین بنظرم تا نرسیده فرار کن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/77931" target="_blank">📅 08:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77930">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گوزیدی داداش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77930" target="_blank">📅 07:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77929">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_Bxg6YSA0LUvYc18RdWY4rPG6orLqF_0KnmmbQg4dVz6nDLsgNsPzsKYQVlxHPSQLUyIKhLE_7tMOuSy13UEzbuq-wGsI3SygIAjX30r38ZKUJLyLFgmlMthC2q7NyeYXuOWU8ncRi41lg-dcFP9veuqJCOKUTMxjM-gqEePvf735lRGD3gjSMcAXenCbZVjJxAnb6srW8ZqLVUZwkcCACOFY7nHJbwOK5cGT9n322izyOI2UCz-4_BJfA4ftr0xuLwC9-bh1XEQt89JQW8FinG75kRwi4gS2mEIm-zuT5v_1E6yBVZpS2Wz3C5fuCscZWl-1HbsifPDTcF2LikzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوزیدی داداش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77929" target="_blank">📅 07:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77926">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeH34DaNUX7n7OuLsoy6ddhPq3COUHAK_HioOjOTiHlyML4X15H3AhcsoDJC0F-7cnw4-wC8JI9xNX4nMBpufGGkCvWeGXyLe-YIzsybXZVZ52lxX7-HLh6PhHbwR2l1jVMWwMJ6Z3JTXv2mTJW5GP8Hra6t0bUKkxFprtP8PsHzRBeywbwr-R-UUTikpLvQDyd7J1KfKha3KeGHeMHG4xZnToPLBoqGvv3tV6Gg_uYkD_XQmVEFpBKPwOntSwHi7rhQFEuT-vA9jTnUZmSizK-7nLP6MueRm3PZvVlwYSgTyzmYvDGufMew41XvNaz7aZuawHPJnTBFSZI3f_OyyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/77926" target="_blank">📅 03:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77925">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">از اینور هم خبرگزاری سوپر معتبر مهر هم شرایط ۱۴ گانه توافق رو از قول خودش منتشر کرد که اونا برا پوشش دادن زیادی خنده دارن خودتون تصور کنید بخندید.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77925" target="_blank">📅 02:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77924">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">با باز شدن تنگه پس از امضای معامله در روز جمعه</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77924" target="_blank">📅 02:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77923">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfW9FeEXvlHy2EOVNorETdEtqzg7v4zEEW3fA3TahTY-wS_Ce91jjAHUhLPUZ2_MLAL6s39Yy7KL4fXp9r51AmfQfKpoQGldZFAj2deeUs8-NtJr8RGmORgm1zrc8nOP9ispn4KPQhQ1_gMdHZLHg0C7-yYE8Dxq97i_Koa6NKjdXrScsTuIZOyg5ieyN9G46uDzx4ARGzwIvjgbSwMDMgZFRFxgOh2mUBoBl46CJtBIowljvXTwM_81GaUU5SuNc5AnE6HT296v2Rn5KSA54gxMxEBrimcaZzIECcweFNTRaCLZUH_57OZ9Q3IjfHJ_D36IfWNw0hG6B36PMTNZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این معامله بزرگ، صلح و امنیت را به کل منطقه خواهد آورد.
بسیاری از رؤسای جمهور تلاش کرده‌اند با ایران صلح کنند و همه قبل از من شکست خورده‌اند. (اوباما به کص ننت خندید)
رهبران منطقه برای اولین بار رئیس‌جمهوری را یافته‌اند که می‌تواند به آن‌ها در دستیابی به صلح واقعی کمک کند. (هنوزم داره می‌خنده خوب به صداش دقت کن)
با باز شدن تنگه پس از امضای معامله در روز جمعه، به منظور پاک‌سازی مین‌ها، نفت دوباره در هر دو انتها برای منطقه و جهان جریان خواهد یافت!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/77923" target="_blank">📅 02:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77922">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فارس: ترامپ در ازای حمله نکردن ایران به اسرائیل، پیشنهاد خروج کامل اسرائیل از لبنان و رفع فوری محاصره دریایی (به جای رفع تدریجی آن) را به ایران داد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/77922" target="_blank">📅 01:47 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
