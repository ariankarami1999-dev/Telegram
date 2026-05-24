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
<img src="https://cdn4.telesco.pe/file/Mp9wrrO3WeS1AJKW3i-Sl-YelZGSSCO0Ma_qWI92UwpV6zKtTnVzsJLKNSC54PmEHRm186gzhmCNaWSjmF9HK2wyk_Zqx4-9D2T3PoE067gXlTBXfe-NNrfjbf0WXQGjN2oGA0CWy5GH4zaVbCIagC95555UWBYZyaqvs7O5_O135ahsVaOh4IalZS2NoVsQ1JmVM8wQGEukJnuEIGe-_8lqGLGagbdLI-KKvSWRRqExI6KnrgeDEJlQcCKkvj8U_N-jdOLyQLOjXLY4MoZKgIM1uwyqf5N6khDT0NUG5W4z_cKDABkxZNst8J97-FhcniJl_SA-XX2wvNE4im7vTQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 23:59:43</div>
<hr>

<div class="tg-post" id="msg-132156">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
علیرضا جهانبخش و مهدی طارمی در اردوی تیم‌ملی از امیر قلعه‌نویی درخواست کرده اند سردار آزمون را ببخشد و او را به تیم ملی دعوت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 182 · <a href="https://t.me/SorkhTimes/132156" target="_blank">📅 23:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132155">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
نماینده محمد امین حزباوی امروز پیشنهاد مالی‌ مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 248 · <a href="https://t.me/SorkhTimes/132155" target="_blank">📅 23:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132154">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">📣
#شنیده‌ها
🗣
🇮🇷
محمدامین حزباوی از باشگاه پرسپولیس پیشنهاد رسمی دریافت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 295 · <a href="https://t.me/SorkhTimes/132154" target="_blank">📅 23:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132153">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oylRpp4sAhjdcj_n0nbyrZiDN88-7eXGgTtQZLa8L2MF-PrklV13bHG_WDZ2OJAKGyksF-WEUBwnMD7LRJJAoM_74Ft_cx-0hEv1oirhTRYQDC9wX3xj5u4ND2t6YomNLcaRCjvYarm6VbwSq0lcOD42LI2EEOwywKexoENBn0iAJ3taNp-EbxwbHto7TlplPw21w1pFJbsuVm1bW28oyEI0-7yk63pS1QZxz_NCOQBhtKSpLMcINmX-If1N5c_RnqSnIXBpAeMol4mGDegnBg6zTAs114ouGBXelBl8EvFeKczKIyM5aC7ObcdsuS3k9wcb1ysOFyFb_FJPg6wi6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مدیران باشگاه پرسپولیس قصد دارند درصورت افزایش بودجه؛ قرارداد ابرقویی نژاد را از لحاظ مالی افزایش دهند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 387 · <a href="https://t.me/SorkhTimes/132153" target="_blank">📅 23:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132152">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔰
سرویس VIP تک کاربره
🔰
1 گیگ 190 2 گیگ 380 3 گیگ 570 5 گیگ 950 10 گیگ 1700
🛜
مناسب برای تمام سایت ها اپ ها   جهت خرید از پیوی =>  @Winstn_Churchill</div>
<div class="tg-footer">👁️ 382 · <a href="https://t.me/SorkhTimes/132152" target="_blank">📅 23:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132151">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
جوزالم پست: ایران در اصل با یک توافق آتش‌بس با ایالات متحده موافقت کرده است که بر اساس آن، اورانیوم بسیار غنی‌شده خود را از بین خواهد برد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 647 · <a href="https://t.me/SorkhTimes/132151" target="_blank">📅 22:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132150">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r92Hm4IvdI-kyPV1rWDfbLuP6Sqd9411rBNMuT5pNwyKywFhv6RIfb5Xdxsiv32H-coAlBHqKAQK0vSxxMXON8JU_zDRWLayGajHV0WU6XPC6WNKtdUPqNpsoXaz4hY-1Fscu7XomvdHlqLBIYlTD1a1mN6yb5YvW5sapcUpsIEePxVlQZ4kyY2twBsZO2IXj48nILKCPUu9kVMYA1GyKjYi4hwpf3RO1D-ZNVz3Te2vpYyqqPlM1VGI24TvKZLytQeEe6Ih07rY_HmLMJPkN27P1TUKCU8r4fwfhVnpIaGBD1I3pJlROvapQ-etOswgbqQRDgCDTH6o7y46Elm9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیرضا جهانبخش و مهدی طارمی در اردوی تیم‌ملی از امیر قلعه‌نویی درخواست کرده اند سردار آزمون را ببخشد و او را به تیم ملی دعوت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 693 · <a href="https://t.me/SorkhTimes/132150" target="_blank">📅 22:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132149">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uX6FzSRS_3GXV8sK-5Ux8KYv_q_xI-XBrspnG4QutW34Ab91oF2mHmmuBhRfZwXZ-xvTvG78avjKZTwyIRBOn1oXnOaJSibl3ejT1muz3S6b3x9-fVj7IbVUMmv8dbuDu-oKJKxDL1UPq_tT7NMD4IDw96XlOu6HwVzhlJL6FoXYot7DMt5N5Nb_c6NLw_eeje9EQHgZBrKyN3jLHOT891Yk-e5fVsukQ-o0ULzTSsHglkFXMKJX_NjOcfBDnt6bugw05GzBiprWLZnuTNj_r6XIwmiU2ZI19LckVA9WuaJ7xLdHk4TUHXql4-70Fzkgfd1beAdFpPr3ugfgNeedMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت فعال شد!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 709 · <a href="https://t.me/SorkhTimes/132149" target="_blank">📅 22:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132148">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
فووووووووووووری
🚨
علی علیپور در آستانه عقد قرارداد با باشگاه تراکتور سازی تبریز قرار دارد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 683 · <a href="https://t.me/SorkhTimes/132148" target="_blank">📅 22:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132147">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فرهیختگان: علیپور از پرسپولیس خواسته رقم قراردادش از همه ایرانیای لیگ بالاتر باشه و اگه موافقت کنن بعد جام جهانی تمدید میکنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 742 · <a href="https://t.me/SorkhTimes/132147" target="_blank">📅 22:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132146">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔰
سرویس VIP تک کاربره
🔰
1 گیگ 190
2 گیگ 380
3 گیگ 570
5 گیگ 950
10 گیگ 1700
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 747 · <a href="https://t.me/SorkhTimes/132146" target="_blank">📅 21:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132145">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8eQnWgoT7BMQu5p42GPczoDFYfrUjGMzQT2sWV1LDgftGNrPqNPsT8MO0hvLCEesNIVAGwVx38Oebw2uJHL3h6XKfNPYbBAt-67kpEyDuur4AzL4STEbyFmFtVUp9_YZGqe3oHy6qSoxYixF0lXVjyYoUFAkvrkm56-PGMTYYLj2rxzyynk6RM237ouEP0hkkX8WIqSRzNfdL2GeLsQC6ZrxdYS64zcpvyg-fP7zobnkPCr_V18RU0gRF2DYz68phuifn6U2ou5WaN3B-in7dgxppULUxVMRRyXVtMXCm8-K4EULnkQqNKFyH7VVO9NfMsoItVEyNhuGBsTeZk1mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖍
سایت فوتی رنکینگ ، چادرملو رو به عنوان نماینده ایران در لیگ دو آسیا معرفی کرد
😐
😟
😟
😟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/SorkhTimes/132145" target="_blank">📅 21:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132144">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffe4f5232d.mp4?token=rQICuyLBFknvPajXObe9cAnMXSqLTUo5zF6wbTJxvPpgEMNK2sWUdhFytfPAO08t9Kln98yWD6p16yq4yx6VeJv0ktu6rDbUPhGlxYU5EDU_-uYmOfQXrL63I9XLGNVT2hwURY_DnS01xaZgl7eNbky2X27-cC46OYC7FHuWGCR1irxDSeIns-RLATaJq4VyQdaTcfgyyoUuJRxKjZw98I1g7TMP-hzUAqFAwQzCzMAv9-TP1WlNkm1tMfPwflnsIrc1Pr0-bOFHprYkdD2UD2fPRYBhR5rLOqzD_vfUNUYlcBvvNzxraGl7-UzPr7ZAy3eIg_xwZuOAGxHDmUdLkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffe4f5232d.mp4?token=rQICuyLBFknvPajXObe9cAnMXSqLTUo5zF6wbTJxvPpgEMNK2sWUdhFytfPAO08t9Kln98yWD6p16yq4yx6VeJv0ktu6rDbUPhGlxYU5EDU_-uYmOfQXrL63I9XLGNVT2hwURY_DnS01xaZgl7eNbky2X27-cC46OYC7FHuWGCR1irxDSeIns-RLATaJq4VyQdaTcfgyyoUuJRxKjZw98I1g7TMP-hzUAqFAwQzCzMAv9-TP1WlNkm1tMfPwflnsIrc1Pr0-bOFHprYkdD2UD2fPRYBhR5rLOqzD_vfUNUYlcBvvNzxraGl7-UzPr7ZAy3eIg_xwZuOAGxHDmUdLkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی علیپور امروز تو بازی دوستانه درون تیم ملی به این شکل پنالتی خراب کرد تا شایعه خط خوردنش از لیست تیم ملی تقویت بشه!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 771 · <a href="https://t.me/SorkhTimes/132144" target="_blank">📅 21:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132143">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
فارس: باشگاه پرسپولیس قصد تمدید قرارداد میلاد محمدی را ندارد و به احتمال زیاد از جمع سرخپوشان جدا شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 823 · <a href="https://t.me/SorkhTimes/132143" target="_blank">📅 20:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132142">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a133b9505.mp4?token=uWgNpMwJnt5U10Llph-mGg5Kaq2giQAndsQkpk6PZYeeAKaxuxHpdcyZQw2NalbR5UFVwV6tRAy0KD6wHbMDvzUuZCcnX60rqKh7tzWn9_21cPRZ_c1A6azBRPVzTURW49TdnrZpi5gvrntiBT-1NoxaL7joOdz1sJLCWOEtWVZDUOEKsWT1uDwkKyoY53LJbsnTX6HUPNmm1JfgyWTMzXCQbd9Dg4Q0RCwbXcOHE94Z9M6100OUtOqTwVX1Kh68ZzaPjw9py8BIppgVe_PVN4Vt0kKyCrYh3RMCHmI5afxeRUoabvzzNT69khrpeHSdPj_rRwYyumM2jmT5b8ORZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a133b9505.mp4?token=uWgNpMwJnt5U10Llph-mGg5Kaq2giQAndsQkpk6PZYeeAKaxuxHpdcyZQw2NalbR5UFVwV6tRAy0KD6wHbMDvzUuZCcnX60rqKh7tzWn9_21cPRZ_c1A6azBRPVzTURW49TdnrZpi5gvrntiBT-1NoxaL7joOdz1sJLCWOEtWVZDUOEKsWT1uDwkKyoY53LJbsnTX6HUPNmm1JfgyWTMzXCQbd9Dg4Q0RCwbXcOHE94Z9M6100OUtOqTwVX1Kh68ZzaPjw9py8BIppgVe_PVN4Vt0kKyCrYh3RMCHmI5afxeRUoabvzzNT69khrpeHSdPj_rRwYyumM2jmT5b8ORZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پاس گل امیرحسین محمودی تو بازی دوستانه درون تیمی امروز تیم ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 854 · <a href="https://t.me/SorkhTimes/132142" target="_blank">📅 20:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132141">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQ-PCBgsuiqFaT9SHVn_pZz_g6qnCpTBljhO7sqJGVUbHOcvQOt3b3BYAE2qktQzEhuhMn3zHd4fqlYpQv2Br_pSkNvg3jfB7h4-SjPGWCQzEQu4otz9nMAM6C6yxwkUwWrjyiQ63DyqSMXkJRVFFwCAKW00I_F4onylI_TGFDBdCGPg81FtnAYokH7PeOc0il0wSfAGaLwk0o-GcP4Ubs1ljYecaGukEPZgYLacyZYpJ6saypt24MYtR81zTWXjtHKGkFQb1MQe1ZiksSkvbHhc9eagu9VvzAYtRWs1djyvQjpuxD2TME3x4atbv9qOlHzNzhC8WOEeJGpperkP2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جوزالم پست: ایران در اصل با یک توافق آتش‌بس با ایالات متحده موافقت کرده است که بر اساس آن، اورانیوم بسیار غنی‌شده خود را از بین خواهد برد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 843 · <a href="https://t.me/SorkhTimes/132141" target="_blank">📅 20:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132140">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚫
افکت اتفاقی :
❌
توافق ایران و آمریکا میگن ۶۰ روزه است، بازی‌های جام جهانی ۵۶ روز دیگه تمام می‌شوند
‼️
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 901 · <a href="https://t.me/SorkhTimes/132140" target="_blank">📅 20:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132139">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7Q9SmsfD6US595PKLsJIrlAC7EjAD8W6pXHVjWafsQqWSSvhm8Z4drZc4bC9K4qvY0rOwZ-m5Vr94n7mKZxfdR-XXtVmSZ3r9VUDkSRm3kahFb6a55PFpvQw5U4kqI-Go6zoljoNIyArkONXwWpZRrrHgqfi2rmtl-tOXuiNFSkzIMCgJm34dImv1pDeyoeSss5ru56keBbexvTAC9xzwUGu6SU4oCGdNm153wy3Ilp4LOq9UG1dqigdMeynX40OrGkHvfzbLS612-6WBoiMsVgNdb02z730rD1Yb4ksWZBwXJEYv7qTt-3NuFfGWbB73PYGkulnRumH4xq2kjU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ‌ حرف های امروز‌ پزشکیان که گفته بود آماده ایم‌ به جهان اطمینان بدیم که به دنبال سلاح هسته ای نیستیم رو ریپوست کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 881 · <a href="https://t.me/SorkhTimes/132139" target="_blank">📅 20:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132138">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">😏
😏
😏
بابایی مدیرعامل چادرملو: اگه سپاهان مجوز حرفه‌ای نگیره ما از پرسپولیس جلوتریم و ارجحیت داریم و باید آسیایی بشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 896 · <a href="https://t.me/SorkhTimes/132138" target="_blank">📅 19:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132137">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚫
افکت اتفاقی :
❌
توافق ایران و آمریکا میگن ۶۰ روزه است، بازی‌های جام جهانی ۵۶ روز دیگه تمام می‌شوند
‼️
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 903 · <a href="https://t.me/SorkhTimes/132137" target="_blank">📅 19:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132135">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 220T
2 گیگ 440T
3 گیگ 660T
5 گیگ 1T
10 گیگ 1.8T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 963 · <a href="https://t.me/SorkhTimes/132135" target="_blank">📅 18:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132134">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
تمام اعضای هیات رییسه فدراسیون فوتبال درخواست ویزای امریکا کردند!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 948 · <a href="https://t.me/SorkhTimes/132134" target="_blank">📅 18:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132132">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
شبکه ۱۲ عبری به نقل از منابع:
🔻
اسرائیل کاملاً از پیشرفت مذاکرات آمریکا و ایران غافلگیر شده درحالیکه همه نهادهای امنیتی بازگشت جنگ را پیش‌بینی می‌کردند
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 996 · <a href="https://t.me/SorkhTimes/132132" target="_blank">📅 17:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132131">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
شبکه ۱۲ عبری به نقل از منابع:
🔻
اسرائیل کاملاً از پیشرفت مذاکرات آمریکا و ایران غافلگیر شده درحالیکه همه نهادهای امنیتی بازگشت جنگ را پیش‌بینی می‌کردند
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 988 · <a href="https://t.me/SorkhTimes/132131" target="_blank">📅 17:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132130">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❗️
پاکستان تفاهم ایران و آمریکا را بدون نیاز به حضور طرفین اعلام رسمی می‌کند
🔴
به گفته این منابع، توافق اولیه و احتمالی میان واشینگتن و تهران تحت عنوان رسمی «اعلامیه اسلام‌آباد» نام‌گذاری خواهد شد.
🔴
این منابع تصریح کردند که توافق اولیه در واقع یک «یادداشت…</div>
<div class="tg-footer">👁️ 947 · <a href="https://t.me/SorkhTimes/132130" target="_blank">📅 17:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132129">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❗️
جنگ هم رسما تمام شد ..امیدوارم دیگه بهونه ای نباشه و نداشته باشن که نخوان اینترنت بین الملل وصل کنن ..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 959 · <a href="https://t.me/SorkhTimes/132129" target="_blank">📅 16:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132128">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
حمید رسایی: به هیچ عنوان اجازه نمیدیم اینترنت بین الملل وصل بشه
😐
😐
😐
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 937 · <a href="https://t.me/SorkhTimes/132128" target="_blank">📅 16:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132126">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
رشیدی کوچی نماینده سابق مجلس:   معتقدم این هفته اینترنت به حالت قبلی باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/132126" target="_blank">📅 16:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132125">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
رشیدی کوچی نماینده سابق مجلس:
معتقدم این هفته اینترنت به حالت قبلی باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/132125" target="_blank">📅 15:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132124">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
فوری از سیتنا، پایگاه اخبار اینترنت:
احتمالا تا هفته آینده
اینترنت بین الملل
متصل میشه
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/132124" target="_blank">📅 15:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132122">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🏅
🏅
با اعلام رسمی afc استقلال و تراکتور به عنوان نمایندگان ایران در لیگ نخبگان مشخص شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132122" target="_blank">📅 14:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132121">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏅
🏅
با اعلام رسمی afc استقلال و تراکتور به عنوان نمایندگان ایران در لیگ نخبگان مشخص شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/132121" target="_blank">📅 14:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132120">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZvFxUsIkQMsHedBgOPdEowmNsVkEzwE777r1Mm8-pO1-6DfIMmKYkxL4xtyeLhxoh-_scBBnpMrgFifiWTz3A1vRMh7r7TY533QtcZa-MPttKDo5_pAh43vTRCUMD89As_TVrDsa-D5y-6vUsjfdyGPy0huioWx4DgRaS4_LXiUdR3GHVCSAfySu05I_ctSgDd4aQ6q0KFV5noqfF2rmGfEa1jxIufpkw4SJ2emEClUAerDLgQhS9NWw2LoFHcHsMVBh88r5AbAthFeQNfUNh9iTvASclHsvZQzdaML0PWphSsth_ODFy_63yRC79FQ1xZfdPx__hSV2MULThrJYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
🏅
با اعلام رسمی afc استقلال و تراکتور به عنوان نمایندگان ایران در لیگ نخبگان مشخص شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132120" target="_blank">📅 14:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132119">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c85e6431c.mp4?token=TrxYnTiePue7qQ3S9w9HwTVZEVEe8OXBtCDNADOtZNnWLH1SNT_rJeodDLLzh9JgbCdzY5K0aoOyyE3crzm-Ysg_FvTb4VfNQv4RVBlqinfhpEAsHAuwpgkr2s-IGdfgdUusgcg6RRvVO-sZ6jaeRfknICbYWkqig2WpCYc6aJipFcTrkCA7Znlc5GqFh8mCs-iemOnVW38EhkaIlExJnL4rgdEXl9XMwJSnLQIh5-NAVqo8Cic23MTmkecNdIV9OFoM5vHvIeTnMTTyiDSni0RD3rwO4i8_a6CfRQ6qg7fmFJplLesyVo-W0gZvBpBsIu-Gn0nTWsBFR7wukBX5YRf0Zg7EdHLl4jQbLRUFXcmrNScohrKAPicctXNF77RxLdrMPjo7fXs1ubC8G4y-nZlj74CV-ss2Kn_q0kTx4ngkHacF4l1AU6LIhwsYvBZ0itmkcvPuynYVWgRtdDUlHScvsCMChZL01oFb-pXhhnicjorCxz793Y-jM_2NBWNhd0iJnLmIZMQqZr5ek9R6zvrPPauYr35atkYBhtyilAtV-Cd4YBWqg4bb02kfK72CQfZ8-yltiw1r-40brcx5PkkAtBa7qDJ7-2augBYAr_LthGH39XGjod_ZBYgyLnp1cji5Uh85qpt2SRlxY7Z0HgDD6IMR7j7FObmAZckSEfU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c85e6431c.mp4?token=TrxYnTiePue7qQ3S9w9HwTVZEVEe8OXBtCDNADOtZNnWLH1SNT_rJeodDLLzh9JgbCdzY5K0aoOyyE3crzm-Ysg_FvTb4VfNQv4RVBlqinfhpEAsHAuwpgkr2s-IGdfgdUusgcg6RRvVO-sZ6jaeRfknICbYWkqig2WpCYc6aJipFcTrkCA7Znlc5GqFh8mCs-iemOnVW38EhkaIlExJnL4rgdEXl9XMwJSnLQIh5-NAVqo8Cic23MTmkecNdIV9OFoM5vHvIeTnMTTyiDSni0RD3rwO4i8_a6CfRQ6qg7fmFJplLesyVo-W0gZvBpBsIu-Gn0nTWsBFR7wukBX5YRf0Zg7EdHLl4jQbLRUFXcmrNScohrKAPicctXNF77RxLdrMPjo7fXs1ubC8G4y-nZlj74CV-ss2Kn_q0kTx4ngkHacF4l1AU6LIhwsYvBZ0itmkcvPuynYVWgRtdDUlHScvsCMChZL01oFb-pXhhnicjorCxz793Y-jM_2NBWNhd0iJnLmIZMQqZr5ek9R6zvrPPauYr35atkYBhtyilAtV-Cd4YBWqg4bb02kfK72CQfZ8-yltiw1r-40brcx5PkkAtBa7qDJ7-2augBYAr_LthGH39XGjod_ZBYgyLnp1cji5Uh85qpt2SRlxY7Z0HgDD6IMR7j7FObmAZckSEfU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
موزیک ویدیو رسمی جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132119" target="_blank">📅 14:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132117">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فرهیختگان: مشکل اورونوف همون همیشگیه و چاره ای جز مراعات کردن نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/132117" target="_blank">📅 14:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132116">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
خرید اروپایی پرسپولیس خبرساز شد
⏺
شبکه ورزشی «M4 Sport» که مهم‌ترین رسانه ورزشی مجارستان محسوب می‌شود، در گفت‌وگویی با گرا اعلام کرد این بازیکن تصمیم حضور در پرسپولیس را بر اساس «حس درونی» خود گرفته و معتقد است حضور در فوتبال ایران می‌تواند چالش مهمی در دوران حرفه‌ای‌اش باشد.
⏺
گرا در بخشی از مصاحبه خود گفته دوست دارد هرچه زودتر در ورزشگاه آزادی و مقابل هواداران پرسپولیس به میدان برود و این موضوع را یکی از جذاب‌ترین تجربه‌های فوتبالی خود می‌داند.
⏺
در گزارش‌های منتشرشده همچنین آمده که این مدافع مجارستانی امیدوار است با درخشش در پرسپولیس دوباره جایگاهش را در تیم ملی کشورش تثبیت کند.
⏺
رسانه‌های مجارستانی از گرا به عنوان بازیکنی یاد کرده‌اند که حضور در فوتبال ایران را سکوی جدیدی برای ادامه مسیر حرفه‌ای خود می‌بیند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132116" target="_blank">📅 14:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132114">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRO6vUASBqgBTubGS3iSCW1O2PI5R-CllC7ilZIO0qx70ILMAjTSp6Udm2ZidAbkojO6mSRfVfkw1ZBQEb7uk-sL6r5XfZ1pndsRiSQ3yY9Yo_VG60Fczkqekh87NP6gnzy9jM0LY180l-c9XqfeJbbhTrjypd5UsAILvBslL2NxoIZcFLJCS3i2Yhm5QCboW4lM3cPVBUKDgjt3PBkdc5JlQqxkSbFr9QHwHifYouNNT1l79_GAT0l4F4M7SOmDiauufoJ4uezuyi54wFkj0rUY1xDKcHpoz-WzsIlKL2KytokhyQEbwxtmsdbBH_wUk6y682s-Hydf7i-t4lEBgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🚨
بزرگترین ریسک حقوقی باشگاه پرسپولیس ختم به خیر شد
🔺
شرکت سیما کیش حدود ۱۲۰۰ میلیارد‌ ادعا علیه باشگاه داشت که رفع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/132114" target="_blank">📅 13:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132112">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
ورزش‌سه: محمودی بشدت آمادست و احتمالا راهی جام جهانی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/132112" target="_blank">📅 11:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132111">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
تا قبل 21 خرداد حکم علی بیرو بیاد از جام جهانی محروم میشه / خبر ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/132111" target="_blank">📅 11:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132110">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
⛔️
احتمال محرومیت بیرانوند از حضور در جام‌جهانی؛
💯
حضور روی سکوها به‌جای زمین چمن!
⚠️
با شکایت باشگاه پرسپولیس درخصوص پرونده علیرضا بیرانوند به CAS و پیگیری شدید سرخپوشان تهرانی، درصورت صدور رای محرومیت بیرانوند طی روزهای آینده، دروازه‌بان تراکتور جام‌جهانی…</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/132110" target="_blank">📅 11:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132108">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3XCkLTz_Zjai2MI41V0umk_i_-xwpckWQGMXZ_grqnhZ9y9R80VIcZCM9mGUyfr3FM0w4LzlwrTSBHdV7AW5Np7PvkeUgqa9uoS9HpC529ckbNyUXRR6Z6S3mFbGnRceMrROM-cesf_1tSIEbRcZKSlAYFSERn-Lm075K2bwEremJyPpaV6a4SoWiWiI52ycbbMKCZowTWrFr4AveEiyQPfMxPHLk2H9Gq-hkYB6gmsbP5w_HXuFAiZC9Zniid_UDGWBuCGMJxUpaFSR8ls8rCXoeSJ5Iq22DnP8nXXO2gxJUx3hVEJYX4COniAFkaycArQblRmF32cFu7PsCaBaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این روزا قبل از پیش‌بینی بیشتر از خود بازی باید نگران این باشی که VPN وصل میشه یا نه.
😀
ربات تلگرام وینکوبت دقیقاً برای همین شرایط خوبه چون کل سایت داخل خود تلگرام اجرا میشه و دیگه لازم نیست هی بین سایت و VPN درگیرشی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
میتونی مستقیم وارد بازی‌ها و کازینو شی، پیش‌بینی ثبت کنی، واریز و برداشت انجام بدی و همه‌چی خیلی سریع‌تر و راحت‌تر انجام میشه.
🟣
آدرس دائمی سایت:
wincobet.com</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/132108" target="_blank">📅 10:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132107">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/132107" target="_blank">📅 10:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132106">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/132106" target="_blank">📅 10:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132105">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">📣
#شنیده‌ها
🗣
🇮🇷
محمدامین حزباوی از باشگاه پرسپولیس پیشنهاد رسمی دریافت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/132105" target="_blank">📅 10:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132104">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/132104" target="_blank">📅 10:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132103">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
الحدث:
🔴
ایران و آمریکا به دشمنی طولانی مدتشون پایان دادن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SorkhTimes/132103" target="_blank">📅 01:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132102">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
الحدث:
🔴
ایران و آمریکا به دشمنی طولانی مدتشون پایان دادن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/SorkhTimes/132102" target="_blank">📅 01:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132101">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
❌
آکسیوس:
🔽
توافق‌نامه همین الان توسط دو طرف امضا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SorkhTimes/132101" target="_blank">📅 01:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132100">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
علی هاشم خبرنگار الجزیره: طبق گفته منابع من، پیش‌نویس پیشنهادی که قرار است نهایی شود شامل موارد زیر است:
❌
پایان جنگ در همه جبهه‌ها از جمله لبنان
❗️
آزاد شدن میلیاردها دلار از دارایی‌های مسدود شده ایران
❌
لغو محاصره دریایی آمریکا و گشایش تنگه هرمز
🔽
خروج…</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/132100" target="_blank">📅 01:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132098">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
تاج رئیس فدراسیون فوتبال: طی جلساتی که با مدیران فیفا داشتیم به جای آمریکا به کمپی در مکزیک خواهیم رفت تا اردوی خودمان را برگزار کنیم/ با این کار مشکلات ویزا حل می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/SorkhTimes/132098" target="_blank">📅 01:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132096">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
ترامپ :   من در دفتر بیضی شکل کاخ سفید هستم جایی که به تازگی تماس بسیار خوبی با رئیس‌جمهور محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر…</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/132096" target="_blank">📅 00:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132095">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
فرهیختگان: پرسپولیس بجای سپاهان به عنوان نماینده سوم اسیایی خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/132095" target="_blank">📅 00:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132093">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
ترامپ :   من در دفتر بیضی شکل کاخ سفید هستم جایی که به تازگی تماس بسیار خوبی با رئیس‌جمهور محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر…</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/132093" target="_blank">📅 00:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132092">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcJ5ogmJO_C5r0vGlmDhnF5ndLdw-hcxBi70AIUNiKXwVzhpk68dio56gh0gM1W-hIIcFaLeqx1jjs1z-3vgiqpcNRF5Ud_vZPfuF7Nk06RvLLSVtT984Tr78U6NnwGOsnRcrpmXxTgWNrnIxM97XIq8YbroIFK67Ow2aghFsIRCtiktg5b4Q5nSLhnvLViZ2KAgi90NzADBP0EdhrCBEgCPZcQzr-7REzQiPYguBeA8EAUbteLjAmOrpLeKlfP09NiVtYv6Ik-V7NtWz5nyVo63QFEIEZ8mde_GzQAdokU1aIGh04nROgi_FpuxB8FhMpGI2gZ66dxO8oXi4EVSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ :
من در دفتر بیضی شکل کاخ سفید هستم جایی که به تازگی تماس بسیار خوبی با رئیس‌جمهور محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر، فیلد مارشال سید عاصم منیر احمد شاه از پاکستان، رئیس‌جمهور رجب طیب اردوغان از ترکیه، رئیس‌جمهور عبدالفتاح السیسی از مصر، پادشاه عبدالله دوم از اردن و پادشاه حمد بن عیسی آل خلیفه از بحرین داشتیم، درباره جمهوری اسلامی ایران و همه موارد مربوط به تفاهم‌نامه‌ای درباره صلح.
یک توافق تا حد زیادی مذاکره شده است که منوط به نهایی شدن بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر ذکر شده است. به طور جداگانه، من تماسی با نخست‌وزیر بیبی نتانیاهو از اسرائیل داشتم که به همان صورت بسیار خوب پیش رفت. جنبه‌ها و جزئیات نهایی توافق در حال حاضر در حال بحث است و به زودی اعلام خواهد شد.
علاوه بر بسیاری از عناصر دیگر توافق، تنگه هرمز باز خواهد شد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/132092" target="_blank">📅 00:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132091">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
#فوری | الحدث:
🔻
پیش‌بینی‌هایی مبنی بر اعلام نهایی شدن توافق صلح بین واشنگتن و تهران ظرف ۲۴ ساعت آتی، وجود دارد.
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132091" target="_blank">📅 23:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132089">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/132089" target="_blank">📅 23:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132088">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
خبر رسیده دو بازیکن تیم سپاهان 10 روز پیش با ارسال نوتیس به باشگاه سپاهان در آستانه فسخ قرارداد خود با این باشگاه قرار دارن و مدنطر پرسپولیس هستن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SorkhTimes/132088" target="_blank">📅 23:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132087">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❗️
👈
ادعای کانال ۱۴ اسرائیل: چند منبع معتبر تأیید می‌کنند که ایران با برخی از درخواست‌های کلیدی ایالات متحده موافقت کرده است و کمتر از ۲۴ ساعت دیگر اعلام توافق انجام خواهد شد که به تهران چند ماه فرصت می‌دهد تا کاملاً تسلیم شود
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/132087" target="_blank">📅 23:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132086">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❗️
#فوری | ادعای الحدث به نقل از یک منبع عالی‌رتبه:
🔴
تنها ساعات کمی تا اعلام توافق بین آمریکا و ایران فاصله است
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132086" target="_blank">📅 22:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132085">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
کمپ تیم‌ملی رفت مکزیک و فقط برا بازیا میان امریکا...کل فاصله ما با مکان بازی‌های ما در لس آنجلس 55 دقیقه با پرواز است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132085" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132084">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
تاج رئیس فدراسیون فوتبال: طی جلساتی که با مدیران فیفا داشتیم به جای آمریکا به کمپی در مکزیک خواهیم رفت تا اردوی خودمان را برگزار کنیم/ با این کار مشکلات ویزا حل می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/132084" target="_blank">📅 22:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132083">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
🚨
🚨
عصر ایران نوشت: سفارت آمریکا به طارمی،شجاع خلیل زاده و احسان حاج صفی ویزا نداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/132083" target="_blank">📅 21:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132082">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
روزنامه اعتماد : به احتمال بسیار زیاد در این هفته رفع انسداد اينترنت مصوب شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/132082" target="_blank">📅 21:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132081">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❗️
👈
ترامپ، در گفت‌وگو با سی‌بی‌اس نیوز:  مذاکره‌کنندگان ایالات متحده و ایران «بسیار به نهایی کردن یک توافق» برای پایان دادن به جنگ بین دو کشور نزدیک‌تر شده‌اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/132081" target="_blank">📅 21:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132079">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
بر اساس گزارشات منتشر شده از فایننشال تایمز با اصرار و همچنین تلاش بدون وقفه اسلام آباد آتش بس بین ایالات متحده و مقامات رژیم ایران به مدت 60 روز دیگر تمدید خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/132079" target="_blank">📅 19:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132078">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
باراك راوید خبرنگار Axios
🔴
همه چیز پنجاه پنجاه است و دونالد ترامپ هم میتواند بمب باران را شروع کند و هم میتواند به خواسته عاصم مونیر آتش بس 60 روزه را اعلام کند و او امشب قرار است در این مورد با تیم خود مشورت کند و تصمیم بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/132078" target="_blank">📅 19:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132077">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🟥
ترامپ: شانس توافق یا جنگ 50/50 است امروز با نمایندگان خود دیدار میکنم و تا فردا تصمیم میگیرم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132077" target="_blank">📅 19:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132076">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🟥
ترامپ: شانس توافق یا جنگ 50/50 است امروز با نمایندگان خود دیدار میکنم و تا فردا تصمیم میگیرم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/132076" target="_blank">📅 19:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132075">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
هیئت پاکستانی بعد از دریافت جواب ایران به پیشنهاد آمریکا به پاکستان برگشتن و احتمالا تا امشب این جواب به آمریکا منتقل میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/132075" target="_blank">📅 19:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132074">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
فرهیختگان: دعوت شدن مغانلو جای روزبه یعنی قلعه‌نویی از عملکرد مهاجمان راضی نیست و احتمالا یکی از بین علیپور و مغانلو خط بخورن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/132074" target="_blank">📅 18:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132073">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
دروازه‌بان سابق پرسپولیس درگذشت
🔺
شکرالله آغاسی، دروازه‌بان پیشین تیم فوتبال پرسپولیس، دار فانی را وداع گفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/132073" target="_blank">📅 17:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132071">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❗️
فووووووووووووری
🔴
مدیران فدراسیون فوتبال تیم فوتبال پرسپولیس را برای شرکت در مسابقات سطح دو آسیا به afc صادر خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/132071" target="_blank">📅 16:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132070">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
دقایقی پیش اسکای نیوز ادعا کرد که میانجی پاکستانی موفق شد بر مانع پرونده هسته‌ای ایران غلبه کند.
🔴
الان امریکا کوتاه اومد یا ایران؟
🤔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/132070" target="_blank">📅 16:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132069">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
سردار دورسون از تراکتور و سپاهان پیشنهاد دریافت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SorkhTimes/132069" target="_blank">📅 16:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132068">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
باشگاه پرسپولیس اعلام کرد هیچ مصالحه ای با باشگاه تراکتور درباره علیرضا بیرانوند نخواهد کرد و پرونده را ادامه می‌دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/132068" target="_blank">📅 16:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132067">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قیمت ها پایین کاهش پیدا کرد</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/132067" target="_blank">📅 15:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132064">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
حمله تند وزیر ارتباطات به مخالفین اتصال مجدد اینترنت: این نگاه قیم معابانه به مردم چیست؟ کی گفته اینترنت را باید خلاصه در دو پیام‌رسان بدانیم؟
❌
ستار هاشمی وزیر ارتباطات:صحبت هایی که در رابطه با نقد دسترسی مردم به اینترنت آزاد می شود، نگاه قوه عاقله کشور نیست. ان‌شالله اینترنت برای آحاد مردم و به صورت عادلانه برقرار می شود.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/132064" target="_blank">📅 15:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132063">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
نورالدین الدغیر خبرنگار الجزیره در تهران:
🔴
وساطت‌ها بین تهران و واشنگتن به مرحله‌ای رسیده که یکی از سران منطقه‌ای به طور مستقیم برای پر کردن شکاف‌ها وارد عمل شده.
🔴
ظهور قطر در این لحظه حساس به طور مستقیم و بر اساس اطلاعات و منابع موجود، نه صرفاً به عنوان…</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SorkhTimes/132063" target="_blank">📅 14:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132062">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⏺
نیویورک تایمز :
🔴
فیفا قصد دارد دوباره ورود پرچم «شیر و خورشید» ایران پیش از انقلاب و لباس‌های مرتبط با آن را به ورزشگاه‌های جام جهانی ۲۰۲۶ ممنوع کند. این پرچم در جام جهانی ۲۰۲۲ قطر هم محدود شده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/SorkhTimes/132062" target="_blank">📅 14:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132061">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
عراقچی: به توافق نزدیک نیستیم. زیاده خواهی های‌ آمریکا مانع پیشرفت مذاکراته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/SorkhTimes/132061" target="_blank">📅 14:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132060">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
شبکه CBS آمریکا: آمریکا به‌زودی به ایران حمله خواهد کرد.هر لحظه ممکن است حمله‌ای رخ دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SorkhTimes/132060" target="_blank">📅 14:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132058">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
یزدی‌خواه، نایب‌رئیس کمیسیون فرهنگی مجلس :
🔴
مسئولین دل‌سوز کشور به این نتیجه رسیدن که وصل کردن اینترنت به صلاح همه‌ی مردم نیست و فعلا قرار نیست اینترنت بین‌المللی رو برگردونیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SorkhTimes/132058" target="_blank">📅 11:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132057">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
شایعات: ویزا شجاع خلیل زاده، مهدی طارمی و احسان حاج‌صفی بخاطر خدمت تو سپاه پاسداران صادر نشده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SorkhTimes/132057" target="_blank">📅 11:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132055">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
رسمی؛ روزبه چشمی به علت مصدومیت جام جهانی را از دست داد و شهریار مغانلو جایگزین این بازیکن در لیست تیم ملی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/132055" target="_blank">📅 09:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132054">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
🏅
مذاکره سپاهان با ۵ بازیکن برای فسخ قرارداد
⏺
باشگاه سپاهان هفته گذشته با وحدت هنانوف بازیکن تاجیکستانی‌اش قطع همکاری کرد و حالا قرار است چند تغییر دیگر هم برای فصل آینده ایجاد کند. مدیران سپاهان در حال مذاکره با 5 بازیکن هستند تا با آنها قطع همکاری صورت…</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132054" target="_blank">📅 09:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132053">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
اکسیوس:برخی منابع نزدیک به مذاکرات همچنان بر این باورند که طی ۲۴ ساعت آینده فرصتی برای نوعی پیشرفت وجود دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/132053" target="_blank">📅 09:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132052">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=Ox6lec666IIH0yULTb3osAQPwoLiDsWJZjRxYsbobTmoSy9yNWorzr1Oqna_jWJPNL_G_f14rkvw3zOS6dPISZZE6RVm6pJBVuVERczXdw4QIVgvRg1EevILQVlFJFlSVjNxWmTStJ9hM5xqN1UgA4dp94UEHxclKi1NgSdcmYPunC4R_vXwBl0jU4Sz1EX_dkxz5bf26ALCzqef7zo3W0lbWTqA-gAARYYznMswGJDvTi5Mlh-LnH7yTM0Lh2PDT-YT9dRg4UD7oF8_L7uiRIFT9wzJ6zhQCwBlkaNRuAMasKoyngazLwzkVzflMPO4VDfoZ1mUS-HnuqqGvtgtew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=Ox6lec666IIH0yULTb3osAQPwoLiDsWJZjRxYsbobTmoSy9yNWorzr1Oqna_jWJPNL_G_f14rkvw3zOS6dPISZZE6RVm6pJBVuVERczXdw4QIVgvRg1EevILQVlFJFlSVjNxWmTStJ9hM5xqN1UgA4dp94UEHxclKi1NgSdcmYPunC4R_vXwBl0jU4Sz1EX_dkxz5bf26ALCzqef7zo3W0lbWTqA-gAARYYznMswGJDvTi5Mlh-LnH7yTM0Lh2PDT-YT9dRg4UD7oF8_L7uiRIFT9wzJ6zhQCwBlkaNRuAMasKoyngazLwzkVzflMPO4VDfoZ1mUS-HnuqqGvtgtew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪
︎با این وضعیت اینترنت،
ربات تلگرام وینکوبت
خیلی کاربردیه چون براحتی وارد سایت میشی.
▪
︎هم ثبت‌نامش سریع انجام میشه، هم کازینو رو داخل خود تلگرام میتونی بازی کنی و عملاً کل سایتو داخل ربات داری.
▪
︎پیش‌بینی، بازی، واریز، برداشت و همه‌چی همونجا انجام میشه و خیلی روون‌تره:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SorkhTimes/132052" target="_blank">📅 01:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132051">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
تیم فوتبال دهوک عراق به یحیی گل محمدی پیشنهاد داده اما یحیی میخواد تو ایران مربیگری کنه!/فارس
🚮
امپرور جان لطفا هر گورستونی میری طرف های خیابون شیخ بهایی آفتابی نشو…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/132051" target="_blank">📅 01:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132050">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
اوریه معتقده در این پرونده پیروز میشه و استدلالش هم همینه که در ترکیه ازش تست گرفتن و همونموقع میدونستن هپاتیت داره/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/132050" target="_blank">📅 01:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132049">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">#افشاگری
رضا شاهرودی این روزا داره برکناریش رو میکوبونه ولی نمیگه بخاطر چی برداشتنش.
پارسال توی هر ۴ رده‌ سنی ۲-۳ بازیکن سفارشی و پولی اضافه کرد که وقتی تمرین میکردن سطحشون از همه بازیکنها پایینتر بود.
مربی‌های پایه هم چون دستشون به جایی نمیرسه زیر بار حرف شاهرودی رفتن و توی تیم رد کردن اسم بازیکنها رو.
۸ تا بازیکن هستن که یک دقیقه هم در طول فصل برای پرسپولیس بازی نکردن و امسال دیگه
خودشون نیومدن برای تیمها.
شاهرودی حتی وسط فصل هم مربی‌ها رو صدا میکرد و بهشون میگفت اگه اینا رو بازی ندی برت میداریم ولی چون تیمها اول دوم جدول بودن مربیها گوش نکردن و زیر بار حرفش نرفتن/فوتبال ویژن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SorkhTimes/132049" target="_blank">📅 00:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132048">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
جباری: جای پیروانی بودم خانواده‌ام را به ایران می‌آوردم
❌
🎙
رضا جباری در خصوص برگزاری ادامه مسابقات لیگ برتر بعد از جام جهانی ۲۰۲۶ گفت:
◽️
به نظر من این طرح با همه ایراداتی که دارد بهتر از این است که یک یا دو تیم را به عنوان تیم‌های قهرمان و نماینده آسیایی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/132048" target="_blank">📅 00:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132047">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❗️
فووووووووووووری
🔴
مدیران فدراسیون فوتبال تیم فوتبال پرسپولیس را برای شرکت در مسابقات سطح دو آسیا به afc صادر خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SorkhTimes/132047" target="_blank">📅 00:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132046">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🟥
خبرنگار الجزیره در تهران: به نظر می‌رسد فضای مذاکرات ایران و آمریکا تا این لحظه مثبت است و پیشرفت ملموسی در حل برخی اختلافات از طریق میانجیگر پاکستانی حاصل شده است
🔸
آمدن فرمانده ارتش پاکستان به تهران ممکن است دو هدف داشته باشد: حل اختلافات باقی‌مانده یا…</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SorkhTimes/132046" target="_blank">📅 00:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132045">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
نت بلاکس: قطعی اینترنت در ایران از مرز 240 ساعت گذشت  @SorkhTimes</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/132045" target="_blank">📅 00:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132044">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
اوستن اورنوف شب گذشته بدون مشکل در تمرین تیم ملی ازبکستان شرکت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/SorkhTimes/132044" target="_blank">📅 00:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132043">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
گفته میشه که پرسپولیس به عنوان نماینده ایران در لیگ آسیا 2 شرکت خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/132043" target="_blank">📅 23:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132042">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
گفته میشه که پرسپولیس به عنوان نماینده ایران در لیگ آسیا 2 شرکت خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/SorkhTimes/132042" target="_blank">📅 23:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132041">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
زمزمه هایی شنیده می‌شود که امیر قلعه‌نویی پس از جام جهانی از تیم ملی جدا خواهد شد و یحیی گل‌محمدی گزینه اصلی جانشینی او است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SorkhTimes/132041" target="_blank">📅 23:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132038">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
ترامپ: با اینکه خیلی میخواهم در کنار پسرم برای مراسم عروسی باشم اما حس میکنم که مهم تر است در واشنگتن و کاخ سفید در طی زمان مهم پیش رو در روز شنبه و یکشنبه بمانم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/SorkhTimes/132038" target="_blank">📅 22:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132037">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔖
🔴
فرهیختگان: طبق شنیده‌های ما پرسپولیس به AFC برای سهمیه سوم معرفی خواهد شد
✅
باتوجه به تجربه بین‌المللی باشگاه‌ها، رنکینگ آنها در AFC و باشگاه‌های جهان، شرایط مالی باشگاه‌ها و... در چنین شرایطی و ناتمام ماندن لیگ، اوضاع پرسپولیس به مراتب بهتر از دو تیم بالای…</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/SorkhTimes/132037" target="_blank">📅 22:08 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
