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
<img src="https://cdn4.telesco.pe/file/fxibIMi-HLzfU5Ye3DlVNumLiD5lXY5fiOBwkNADAy-Kx6hEcbs6KRn37RfYde4nxQ-a4LrhZ7GhaIWaKPnn50WXQlR-WrqqLUW71XrTr4HvAZqZ0f0ud4STxAy9bmt-qxI7DNeai8QClt5p3b-LhpaY-9_ZhWSFKNCw0AeUd3azo6lm02ialKLQsCIGFNc3L5z8FVgElTwbL4nCgr-03zz7zpj9RUIakuz-BS6iZcflH46fBMj4kd3Qg74ZLkCQRqecobXEeXakDgHceEQyGMI9m06KH505iOxSVXuFPhAlNrcxBkmk0PsEGPnnMiOvBXnWq9NIbRwfq9jKVHys2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 169K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 18:51:00</div>
<hr>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تحلیل فوتبال با سامان ویلسون مثل تحلیل سیاست آمریکا با مرادویسیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/funhiphop/78352" target="_blank">📅 18:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مطمئنم که سر مهریه به توافق نمیرسن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/funhiphop/78351" target="_blank">📅 17:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ:
به مذاکره‌کنندگان ایرانی در سوئیس گفتم اگر تنگه هرمز را ببندید ما بقیه کشورتان را هم تصرف خواهیم کرد و حتی کشوری نخواهید داشت که بتوانید به آن برگردید.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/funhiphop/78350" target="_blank">📅 17:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ: جمهوری اسلامی باید فوراً جلوی نیروهای نیابتی پردرآمد خود را در لبنان بگیرد وگرنه ضربه خواهد خورد ضربه‌ای بشدت سخت و طاقت فرسا   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/funhiphop/78349" target="_blank">📅 17:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91dac02670.mp4?token=QmCMbXL5V1X9qnfb2Qcvrt2P1Ugh5II6ZmbyemN8n203hLmqXEUXL-z3O6RwEz2T6F5R8OYPwLK-G7Wl8U4Ul-y7tUIaoRzyKb87JiAZOYuOC3BFmD6YZojfz32ZvtYXZf88TV-JgxQVL_he4pLTP-Jb-51la-bdjF13WCrzerq7lKhaH0jpQEKZ7UzLl-R6hAyjoZCXcHD1_-UXRRzDL9oAJRzWwPbYF0cD2mL0SChkByTpEfhgixps536pOdGDHxxFFnCjsR2HRkNeiS1thvNGrr26x8rCRjqhd_aQbGB7L6MZu_mdshMh0rzE6e-oehryoRfDuzM_SjzOjVrO1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91dac02670.mp4?token=QmCMbXL5V1X9qnfb2Qcvrt2P1Ugh5II6ZmbyemN8n203hLmqXEUXL-z3O6RwEz2T6F5R8OYPwLK-G7Wl8U4Ul-y7tUIaoRzyKb87JiAZOYuOC3BFmD6YZojfz32ZvtYXZf88TV-JgxQVL_he4pLTP-Jb-51la-bdjF13WCrzerq7lKhaH0jpQEKZ7UzLl-R6hAyjoZCXcHD1_-UXRRzDL9oAJRzWwPbYF0cD2mL0SChkByTpEfhgixps536pOdGDHxxFFnCjsR2HRkNeiS1thvNGrr26x8rCRjqhd_aQbGB7L6MZu_mdshMh0rzE6e-oehryoRfDuzM_SjzOjVrO1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس یجوری نگاه میکنه انگار اومده قرار دعوا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/funhiphop/78348" target="_blank">📅 17:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دیت جمهوری اسلامی و امریکا شروع شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/funhiphop/78347" target="_blank">📅 17:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ:
جمهوری اسلامی باید فوراً جلوی نیروهای نیابتی پردرآمد خود را در لبنان بگیرد وگرنه ضربه خواهد خورد ضربه‌ای بشدت سخت و طاقت فرسا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/funhiphop/78346" target="_blank">📅 17:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVlHci3M0elQACSqjHricvKIf8B9RK7A3_fhI1dcpDDaPy5tBiXim3kpnXv7MQEmc0Wr9gJO4B8sNH7GtJzLNHp9uuCbwqtqLGA-nm36oJQEJ2wTOCDNU2xiRUtjBf494ERPInc-7JFOBkGgYG1Ozn2vM_51eY3n19PXOQY2phC6RO4RrbZZlhj_N_NlUSlVg2qESilZAaS5DoSW4j7utGuLeWqJn-UgvRI-nSYjGfkePQB0Vi0SKFcAG9PWtjq8TyX7Ipr9tkHgsU_hCoV-nsyWs21qrubZQHdmi8UoETQASg5T4mSvaBDkW0gCVRJlCpdDkapRwinqN4Jx2CSveQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت صادق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/funhiphop/78345" target="_blank">📅 17:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عباس دهنت سرویس سوئیس هم بگا دادی اخرش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/funhiphop/78344" target="_blank">📅 16:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78343">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c4bf1909.mp4?token=B1V9JvDiTCLEPgvw6PkX4Vmwq_lO2nDwiaTk5cD513lvAZWZhU9-lJDyl4-JcFIJSf4FxMMG8JjzuGXn1cphPaktiSYrTum7fjNbOzLpS0V0qZCU9slvdWV3pnXtNONBxr9lnEE5XMdc3qIrdrQxcfx4qVNP27ximTl20j4eCU2074bv3gkqnik5bUCIr6va9ENEb4HHFqPnosn1quUQaHlYN3AjvCOY4JlraTuDzcDqod2B5CgY6ggEmRkLqRiTPXm5Qi_UUhAKE4kJh0k-LriT2TqfePqzpje8Z_XTl0vbRAvgZY-Bzps3IVRQ01lzcWKiVpiAsi5ohxZdUyeXtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c4bf1909.mp4?token=B1V9JvDiTCLEPgvw6PkX4Vmwq_lO2nDwiaTk5cD513lvAZWZhU9-lJDyl4-JcFIJSf4FxMMG8JjzuGXn1cphPaktiSYrTum7fjNbOzLpS0V0qZCU9slvdWV3pnXtNONBxr9lnEE5XMdc3qIrdrQxcfx4qVNP27ximTl20j4eCU2074bv3gkqnik5bUCIr6va9ENEb4HHFqPnosn1quUQaHlYN3AjvCOY4JlraTuDzcDqod2B5CgY6ggEmRkLqRiTPXm5Qi_UUhAKE4kJh0k-LriT2TqfePqzpje8Z_XTl0vbRAvgZY-Bzps3IVRQ01lzcWKiVpiAsi5ohxZdUyeXtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بوفون و نویر وقتی میبینن نیاز نبوده ۲۰ سال کون خودشونو پاره کنن و چارتا سیو جام جهانی کافی بوده:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/funhiphop/78343" target="_blank">📅 16:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پزشکیان:
نگرانم مردم ناراضی به خیابان بیان و اعتراض کنن. اون وقت ابهت ما فرو می‌ریزه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/funhiphop/78341" target="_blank">📅 15:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اگه برزیل با درخشش کونیا میتونه ۳.۰ ببره ما چرا با وجود اینهمه کونی و مادرجنده نمیتونیم کاری کنیم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/funhiphop/78340" target="_blank">📅 15:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78339">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پزشکیان:
توافق رو گردن من نندازید، تمام فرمانده‌هان قرارگاه، سپاه، ارتش و امنیت در جلسه شورای امنیت ملی با توافق موافق بودن.
دیس به مجتبی خامنه ای؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/funhiphop/78339" target="_blank">📅 15:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوستان یه نکته ای بگم
مجتبی خامنه ای طبق بیانیه ای که داد گفت به اصرار پزشکیان این تفاهم نامه رو قبول کردم
نکته ای که وجود داره اینه که حکومت اگه یک درصد امیدوار بود که این مذاکرات نتیجه مثبتی براشون به همراه داره به هیچ وجه اعتبارش رو به پزشکیان نمیدادن
پس نتیجه میگیریم که این مذاکرات صرفا برای وقت خریدن هست نه توافق قطعی
ممنون از توجه شما به این موضوع
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78336" target="_blank">📅 15:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مذاکرات تو سوئیس شرو شد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/funhiphop/78335" target="_blank">📅 15:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یه رپرایی با معروفیت کیرگوزی میکنن که سر جم ۵۰ هزار نفر نمیشناسنشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78334" target="_blank">📅 14:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نصف بازیکن های اصلی بلژیک بگا رفتن و امشب در دسترس نیستن    @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78333" target="_blank">📅 14:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ولی خب اسپانیا چون تجربه ندارن قهرمان نمیشهط آرژانتینم چون بیش از حد تجربه دارن(پیرن) نمیشه، تنها تیم معتدل انگلیسه که اونم لوزره</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78332" target="_blank">📅 14:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78331">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هلند بوی دوباره کیر شدن تو فینال توسط اسپانیا میده</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78331" target="_blank">📅 14:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ژنرال شماره دعانویستو بفرس
تروساد هم از ناحیه کتف بگا رفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78330" target="_blank">📅 13:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نصف بازیکن های اصلی بلژیک بگا رفتن و امشب در دسترس نیستن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78329" target="_blank">📅 13:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78328">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0Z4Ia0mBFbQoU4BiQIRct01srBKVsqlitBO3qVZB4hiBShUNJkymcEUIpySr8ACfyZsI0lKmyx4vR-MXYwhGqXP6cid_VFtx8lkXZs-3vQfdORlB5YvCuNMe3YkXByw7GL9L9oHZ1UELTOI3L5Qk2KSGelcMAUofxZFmaJ2QLURN7dM82_TwtCihDeBMAsXNxtu1I_P3hojfDNwofObkMSqiT7VBDzJfaY0CaW74kJN7NdCbq5hzuClcq69-1zMYZXlmD1jiTIHqaJ5-KWdOCOn_WZRTUje0S8Uf_d9znUGYWpga1C3uRsV-STRNyw4ug6PawTkKKBtvhXNupVhaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرچم یکی از پر افتخارترین تیم های آسیا در بازی دیشب
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78328" target="_blank">📅 11:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-o0pq1og8AcTidYzCoqg03CCj4k7mFvfrj1GpXTmRLvGwEJ8pLNiFhm_Tzh_RzEzqkkSHRjI8CMX4LxjxqZCiQLL013JFuKqZXmh1HZh8W5nxlBT8t7hdJzhPstfHn4lCEMGhP9fBEySUkU3fbZu2gIumgj_5KYKtbqU-9qU63-OVwt0BodavrS0MjHgbiMHWQU2xW3pe9pIgFCk-iu-zkO3w7BlB1Z1IylGSbUzHJC2p0iDDqUS9roUtUM8xJgZXEj18dRPadFsGgnk0YbQgS-TkafR-zNocB5qOTlfs9BKxVJnJ0IajT-sNDVY-9rYqvnsXldsNwni3j_WwlgJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال توی یک تاکتیک پیشرفته رفته عکس بازیکنای بلژیک رو زده روی دیوار بازیکن های تیم ملی تا امشب بازیکنا تو زمین نتزسن.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78327" target="_blank">📅 11:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOMNbygxrbCCb9pc9N6h4sREr85pSxYPTs3SV_ym4IBlUl3P9fLh5xcqf4tNIdxX9bKiXj4RJLohAjmNufH1AWmYOdKVbWjwMKQkKt82N5_gZzXOfFNowBMbWsWd7s-L4BwwH3HBHGDY1-uQ1MyXxLz8307f-onfJw96FEqF4Z71ascJRZbxS2IgI0Jr5TX-bA2ODWMslZ11_ZjrOFJwM4onpO_Pc6CMD0Oqzzj799kQ0ZFf2QlSdIJdH97SrkHdMA9XHB5AMEyUxVcxma0b4cWHcikb5kJDCDc5l371OugeyGr3LM4Ev7SNbBySlPsjs1uUCLN5tUw-dUPtvKYNUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظرم رونالدو از مسی بهتره، چون ممه های زنش بزرگترن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78326" target="_blank">📅 11:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🤩
🤩
🤩
هزار تومان روی مسابقه ایران و بلژیک شرط‌بندی کنید و
🤩
🤩
🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
رایگان دریافت کنید.
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78325" target="_blank">📅 11:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4SzoDHiyIANp0SOl_sSmXvfpNO0HIJYg2G2KTR-YfrH1HZfbIdDnlKaafxjEXIjf1AjyU7Txx1OKvmgirRiol0j5DrTFUCbmvPmFv3xpYZ1pYDOizErmfVOQFOXTdNPxAKGeEScQxJd1PjrJsAjYdDgmOCenL5Ltrf3bCFyBStRwCpRrBGT7jxwBs_q0Ao6lLilwmuMWL0IfNoLeejsMumgFdmDzqeqyu4QmSNqoPvUakNSn3sHzLf2NkctDWN7neb0cuSciwthicKp5aFssKQFFA-Jt2VwgwkWQIAwHn30U1dWyL41zrL01PfjpDoUM4kHx5uuJJbKmlDCj7xE6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پیشنهاد ویژه فقط برای بازی ایران
🇮🇷
- بلژیک
🇧🇪
🎁
🤩
🤩
فری اسپین رایگان کازینو در انتظار شماست!
فقط کافیست حداقل
🤩
🤩
🤩
هزار تومان روی مسابقه ایران و بلژیک شرط‌بندی کنید و
🤩
🤩
🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
رایگان دریافت کنید.
⚽️
بازی ایران
🇮🇷
vs بلژیک
🇧🇪
💰
حداقل مبلغ شرط:
0️⃣
0️⃣
0️⃣
0️⃣
0️⃣
5️⃣
تومان
🎰
جایزه:
0️⃣
5️⃣
فری اسپین کازینو
⏳
فرصت محدود!
همین حالا وارد شوید و شانس خود را امتحان کنید.
R31
🅰
❤️
Winro
هوشمندانه بازی کن، برنده شو
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78324" target="_blank">📅 11:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78323">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کارتون فوتبالیستا تازه داره رو ژاپن تاثیر میزاره</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78323" target="_blank">📅 09:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78322">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این چرا جهانی شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78322" target="_blank">📅 09:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGKO1v3LVpCDA0647jd_0EjH9IutL-7ivPjUjF_xZnidkjt-Gmq2l-KjMNUUl4gM4hC4RhAheD6nBZY9i92Kj-rsTtKii5YgQaS5P-Ukz3xkvgzR1tEMP-RqsImkmRJVoR_0AAANoKFxLlUUi3UQFS2Y8b_91ztFhbX1nNO2Mb3GdK9QPLfoBWxcif4DxAEgdUt57hGeKTdn1g3rXNjWbtqbsCSOmpiZWGFJ9pIPN6t3ZLty2NtNnjhE286wF8kDh5tAbcfj40rB9bR4giko27RFVW-oXVQSdHaPDkfBhfgBUoHr4yBXroy1V6a-2seKQZLJ3_267j-q2hC_kWo_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چرا جهانی شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78321" target="_blank">📅 08:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78320">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عباسشون رسیدن سوییسا  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78320" target="_blank">📅 07:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78318">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVCwqUfwAH-r-1mi5E087L997Ok_FxISNSIcHU7zyZFT7QsXNirfS1Glok1PqUwhd2QEpdrZVIBZ7r_cErGoC0hXcyDOFWhdSVQje7XGotmDEnqMHP8XV4UZoBTxvkHRGmTQlmT0gZa4qymZdvYw3sZizhl85KcATOLqa_Gj6B6ANRm6LTXRWDBRKx9sjffz1U6QFIByqp6V0WjoTh25avhwjC5uhuBkwdFC8UGyT90CB71lq4qbk3FCbAjj9pK0zT3wnNPCqSuI8CnBgw5V8_tPSs_Jc437RdyYfmTQ3eA0oiDIlPKG56AN0QduVY18sZmwgquQPteG5V0OjZphvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزی نیست دوستان ارتش اسرائیل یکی از گسترده ترین تونل های حزب الله رو کشف کرده که پول من و شما ده ها سال صرف ساختنش شده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78318" target="_blank">📅 02:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldxf7nHsuSFilaw3CDNRYbLAK1Vnqq1T-8tkrH0Ce2AeS58K9HbaQrWTFiNTXLjnpFcOqUvTSmM9yyxZLUQd7abSn43AR0AX-3d1TJYQbZimyK2lVMyJ-YRdDme_0Mq7WU0FpLt_3WxiLEidmyijsgxpksYK1Xlu4yWI7nMvT2ix3Tl4MtQLxmC8F9b4o5fbTFHHfvGGZ2jNDfy-fI-7wWb85G5cTGKdJ98jnFbEYydxUC8VPy-JLQ6DUfEMo5GGDdGXDxNLbZnmPWXC9Fpz7-DKPvd4s4SZIGMyjXyWHJLbHpPm6juU5ZITgFloQze7wThF54TaAhzlvhOrGb4jKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Iranian power
❤️
👌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78317" target="_blank">📅 01:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78316">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حالا جدا از شوخی ترکیه خیلی به کرداشون ظلم میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78316" target="_blank">📅 01:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_V6g0SbjHdmsUr2guy4EGzIbZPmb7MyzXctb1Hq8SqzMUufPAyWUlnsOdQndn3Scy4KHuI6axJj3a5dnJigHfgJeilgSDeUXfRR49bixfRegg4bEpk9-Mc4ElNK8zj20FREvVD1-MGH0ZjdA2JkYajizKtk6aQgpcG6yThq1BC_BF2YT7Jo1g3qWgHXWTTDujxMKJ9fq21l6Uv9lxjnBWMx3S2A6oLnZ-vawpgxlUht1SRvxNsA-YmWHRloXx5jJU3tyOig-dAIntQvtc7g7B5joXAPleie28ivOgJGvM8bWwGmKN1B7iqPzXjQtM4qCHCiCJ747CLWFnxtZ11a5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل برای آلمان دقیقه ۹۴ کامبک تکمیل شد  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78315" target="_blank">📅 01:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یه طهلیل بریم
آخرین بار ک آلمان به مرحله حذفی صعود کرده بود قهرمان شد
پس این سری هم قهرمان میشن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78314" target="_blank">📅 01:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گل برای آلمان دقیقه ۹۴
کامبک تکمیل شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78313" target="_blank">📅 01:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78312">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-NJmJdKs-wtjOemPYnc1oU2miY2ujdjDStprvuDazH5Mp3Qv_ssST9E99Ykzn01dvb4tzi-3CHsSXqnYy71k0AlEgImNlOHXtFKe5dBBUG4fttcL2EV0hoNqJFEfX5jIDl2FgkjyEOn6KsNYbS8cQhPp48JGSX9kjPNsRLPdoj8kkUIIlff6sbOBarAZUNiJGkvGXvOqAggtosTDebO7FJjGOqUoGHF45lrhPhMAPjC_QwrQgsDsFEJeW1-zevu17Nezj-13ChiM5dc0SmgLI8qoWz3qmiJu3fvgmK1Xt-KFHtqAVHR59KbmIf3OBT-P-tPRuFa7DttAuKAH7ASgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمرینات قلعه نویی قبل بازی با بلژیک؛ رسانه های بلژیکی میگن لوکاکو هم از لیست بازی فردا خط خورد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78312" target="_blank">📅 01:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78311">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">آلمان تیم خوبیه ولی مثل تیمی ک اومده جام ببره بازی نمیکنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78311" target="_blank">📅 01:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78310">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آلمان اگه این بازی رو برینه عطشش برای ادامه تورنمت خیلی بیشتر میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78310" target="_blank">📅 01:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78309">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فوتموب باعث میشه گل زدن تیما برام اسپویل شه، لذتشونو گرفته لعنتی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78309" target="_blank">📅 01:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78308">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78308" target="_blank">📅 00:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78307">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">عباسشون رسیدن سوییسا
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78307" target="_blank">📅 00:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78306">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کیر نخست وزیر بریتانیا استعفا داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78306" target="_blank">📅 00:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78305">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دوکو به دلیل عفونت تنفسی، رسما بازی مقابل ایران رو از دست داد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78305" target="_blank">📅 00:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78304">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">المان خورد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78304" target="_blank">📅 23:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78303">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هلند تو این تورنمت همه رو سوپرایز میکنه
یا با قهرمانی یا با حذف مدعی های اصلی
این پیام بماند به یادگار
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78303" target="_blank">📅 22:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78302">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گل پنجم برای هلند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78302" target="_blank">📅 22:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78301">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سوئد یکی از گل هارو جبران کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78301" target="_blank">📅 21:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78300">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حساب کنید ژاپن چقد سوپره که ازین هلند مساوی گرفت
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78300" target="_blank">📅 21:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78299">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">الله اکبر گل چهارم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78299" target="_blank">📅 21:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78298">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گل سوم برای هلند
سوئد پاره شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78298" target="_blank">📅 21:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78297">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گلر هلند عالی بوده
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78297" target="_blank">📅 21:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78296">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سوئد زد ولی رد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78296" target="_blank">📅 21:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78295">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اسرائیل آتش بس لبنانو که پذیرفت الان شروع کرده غزه رو میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78295" target="_blank">📅 20:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78294">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هلند گل دوم هم میزنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78294" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78293">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هلند گل اول رو زد به سوئد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78293" target="_blank">📅 20:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78292">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j04LQhSIKu2SCOU2p_1TMjctmsTZQ6Bt24oA-nGe7UYmRP8mLVgNb_zmSj9TqaQbUD9p0MA8ilELmmWyTAY-HdQOwr1RCmOLeiCvVg0_08E9kb8udWbUz7v-XB-AbTVaMU7H8Bse8B0eH5icAbhUmL4lPIDXmoMea6RJvmyQLuMuon3iJC5f7zTSCkm8ypf1_yrLQcoqC0qeOugr758mnBGjSewjFZrtKZ8d7gb2SXAW7JLhogI7x0mJy5zpGPuXf_jd-BR4GbQkUf005Ud9lj1v25hD3zDQ0MrU9LuOeIU5uSYd1PlkkWuc7ddv4UsfU77WM6uw2moXE8v_Mg6wuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه هم با باخت امروز صبح از جام جهانی حذف شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78292" target="_blank">📅 20:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78290">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CcjqCwfRn8Bapgu80j3fK3I49-2ZSZq-HB6R6ONiCO3MwakDtS189MORuR00yVGcY8KQYrqOFqkWeCiULsQePVNA6UCvlyu3GhTncS3yPqO026OJTfRJu8r-cMsxiSFmSTe5W7DOVtiJzXVCeNTV7kmJAgHArQmcat9IQCtNLtus7MMhk502J4yBfjamyLHIp5HgS_QU9dpnIcvDVb3KiIeqggS-FRCjeKfOggH1HwWebrUM4wU49NrcuWdpKYFSfExY1CiLPNj0RprXUJZ_k0ovh3G2AvGjkzu9xjXcSvuzDnsuKVap_ExD-8cauX_j2mEDb1ife_RGehJPDe19rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URK4t5F1u77_D4Q9V4zOGUf0QUahC3rPBGMITbv9RdYfmNyDJOlueGX2vC09FOlQQOtkbhsALRAtSTSb088P7x2EyMtbL6nihRvneKleIgio77r8L5mz5kaYlZyZEdIjIejGa630jLpz0vbK7T-JUvFsZhDiC27CuKwMrJ5fYEhSVABQ_VsJOvdp8okfHM2yeIPORK4MqABbiCKjiWrKe-Wa-8BlmUivKrh3ejYqmdmAznoOkGxOASdPRAg-uvtUi-iWlpr0BGuapqhR_pYxJ3ItY9Fqpaay1_lrFfttdW81L4j11fVYzyOB4DDsTuoMWB4v4JsPWgEQuYxEStPlDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب دو تیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78290" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzQZRvXkg0_BJuxcI0pizGsT7MB6ltmvcTCV-hNTLZxuyLsyjL9zro_7SGUCKW4VYzpwI09F9HpIS-SuvCYnkfAcpYdo39NyOIUYnwh77mmukphIK1XTV-sIG_fr5VzF0yxqLisKIZCPIM-xDnZm6oSoreeYC1iX1_kQ09zVHRfKpBxXKgGgJ1hBWif7eQPM1hhtw5Wo-Ga6xv2voVQvKquJ8EUa602kFs_7lKuzqBbqtpG0UT1i1TS0W4ewYNAXJnF2ZHXqaozq2XjM0lyd67LoeY8JfAagShY9EFK073Qp1feOuImIH93_SjsOUD_R4TZpSoKKztoiXIRDWTslDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78289" target="_blank">📅 18:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78288">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePO2XUkuiPic_JpOZCHabNVVFky56ltDispLcUhAeCAdrXO9oXR1H5Wq5jNz9lyrYectf1NOGTU5snDB-iQSZONfffPKcWSpTsoiuyiN9IZ76J2MjpzfQWiicI0u6z5y1kfvKxFA1W3KyXyEqgx28CFSp-yhsMdPRLlm2gA7BMh7EitakcJ3zYpEo_ew71RdxbFz-hFIajXXxvgIlluAJ8ewDMsrLuAV7ZLw1htK5b4uDzrKGKEynP-TFfaPtFYOL_yFLyntaaZNZCusuZIDSVEf0BUQiJA0nOV_wBreMwpv0uCIqJdixPC5uIpJKTSQwo5urkAUuL3cfmxUMKmj7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداشاهده بمب خنده، فرانکی دیونگ و تیمبر تو تمرینات هلند شاخ به شاخ خوردن بهم و الان تیمبر مشکوک به ضربه مغزیه و دیونگ هم احتمالا بازی بعدی غایب باشه.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78288" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78287">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
همین الان وارد شو و علاوه بر
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه اولین واریز با معرفی هرکدوم از دوستات به وینرو تا
🤩
🤩
🤩
🤩
دلار درآمد کسب کن
💰
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78287" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78286">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9PFuKma2aDYaJc5lYjKDypPuVEqNpZXhWWqPIUm-FpA9vOU_5vpVlh3QCCOlpl9CDEd19BbC74rVAuEacZsvwatrqR_1CdIvQgIPEXR9uAB1dN3AN_hLALK8SEVygBzvEbNuEcd2WSQcYSTft9fduVO_uxN-yTaulNMHzqP44KnmR1VF97xxDZn_7HnbeBBVbkXC90zCEoUUa-6p6v-E45zCAkDHdl6hrv1YVh9mzs_WT9WVsKWhNhVElRxV7VyFudvOa1oF3G1WiCK-c0t2FH14OC2qFuMxOkqg9scN1abSVzWytq7B-pwcn1f4-1FEBEjsGM2g_mLhfwDg_Foiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این پاداش پول نقده و لحظه‌ای به حسابت واریز میشه و به صورت آنی میتونی برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
G30
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78286" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9F8meWlqBpJkvRqLOEKRW8wC24JOYHJP7NBpdw0SqGW7RniVkvlIqZDgIqvwV_KVH4dQYCY2N-EFPNtz3cjrLrl_rCFcUfaMoTIMH2ue_DrL0mO55T_52gcr7P-dIm8JDbUHRjS3Jv-2SnCupHN7I5AwcVRKHbnqOED7r3M6zF7GtQA8JS2xW-S7Q_gucTD6Bjz9Bo0T30TDqiMGgZgC4Przo_r8vywnkW4FXVNOqVpFuoG6iMvPgS2HWCMM4HbtpnOEJkoc6NIIbOmB4tC-ZZLSZwIf4VKsLpzvODHYiaX9tjp5dFHncBkq8QGx5wluVwR-IVdnjJpa8MRIzv7Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه نتونن تیم ژنرال رو متوقف کنن حریف احتمالی تو دور بعدی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78285" target="_blank">📅 17:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-yg3EWVd1sTDBKmz46Y1Odyw0dXCe_rab0WhYBjS2G3CVvKghYP2EvKSrXsV22_lECTbs7o2Dn5tumim_bfNgWCuZRkzfC3HaDDCym3I48fu9nvISDwLH2v2RbzCbQymrpG98rdS5SXI_0EbMuTA1j1ZIOnEjwRGyUXkmwEeuTHB5yNg1zte96HBYXrcizRuYEFChnDr8sfoZm1twf-5a-U7hnRRjDbAgP_0Ii4WzxmwIKCakV95GUHGlZsxTrkZLDc8zTUMS--y0VqN2fDesb0Q71-D28q-THYvoawXwElr6kQG60F8iUE-opgwQaVfGrzmIrqFcAZLQFsrNIpQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فعلی تیم های سوم جام جهانی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78284" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78283">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مکزیک به عنوان اولین تیم به دور ۱/۱۶ صعود کرد.   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78283" target="_blank">📅 17:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78282">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9cYbsJhXsRNvCL1aXjhcp6cutTTDdC7OhU0W9WEQqgkuMTJdDwWTYgwArdso6Er5aTVOqve7vTS-p4QCFd7XCooIlUYEeOLPJgzROZN-Kl1w02leTSpYsqCcWlZ5xPmLQhiGzNTeg7JJ0BVRyyk33xs2eiGFSZjcFhKy5Lrl-1NMClTrfbc1zH45bdjtWcP1BlPgJkOEVYa9BzzzIB69cPSNwWltn81DEw80_9dPU4wMkbcL3F_PC-2_KEXQ7Vn-CKe-csOjzHaULo-Q-oHe4QIC9qO4U0cMKDotz7qk__tbqD0cyeHYxQSDJS6lYeS2k23tNLz0V65tRjz0ML_Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم بالاخره افتخار همبازی شدن با بهترین بازیکن تاریخ نصیبش شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78282" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78281">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سخنگوی وزارت کشور: کسایی که به مراسم تشییع پیکر خامنه‌ای بیان، به صورت رایگان تحت پوشش بیمه قرار میگیرن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78281" target="_blank">📅 16:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78280">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سپاه حوصلش سر رفت باز تنگه هرمزو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78280" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78279">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سپاه حوصلش سر رفت باز تنگه هرمزو بست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78279" target="_blank">📅 16:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78278">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دولت عراق مجوز استفاده از استارلینک و صادر کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78278" target="_blank">📅 15:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78277">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxN77M8EbkLtgMbMrD7p7iPEbOotbcymRfDJItsN4SgOBMbSN2js4-eX7LGjFnztURuFdZzYfbCrbMsMb7IcnbphlxG8Pkh88IY2aHepZyfnoF3myzCK65sdEXq84x1sWdWEd9pCuKqc8UN9_Zux8H69j5vo8rP2IiY2dX6AIAr98lhZUvIWVo8viOhSWlK-YciAanu6kOf3t3EESFXgWNXeQfrkpMsFTiAPq1hmIVMXHuoq6FrssVx293nqIICe0AeQheFCDNEyBd27lYwu0zsnupJWSixyBAgdt28ymIiVichG1rSRxF7lYHujPBmMGGTqhqCFlRzu-EcR_cSYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدینیو و طرفدار گمنامش
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78277" target="_blank">📅 14:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78276">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb_8B6Eo4Kc_YveYwaEIme5d04NKKfPFACCF1p909D8c_PMfqvUP2jiu-C1ndcUEEgTF_zjHr1MwvYI3hnN2r8vy8rNNYw7RtUlHlKm1poAde1nA9vdK21LrpOuSyYJo5xi2K0D1xiYPcil_XK-noqIBHq1exti6S6EvTalS2IojO3yB9eyabucVQMdePwpW4ZK23tuwCH5Z0LcCFK1oiH_qo5jY0PJK6cDoQRufs2JFKLCwaCosBwfu9ZROi69HlVHww9K8TgXiLSqWW_43l2ZZg5IpId0Sco48CJxFzaRmtdGLfgA0jbm2isZEfuPhJX2URe_BtH85-FS535eDjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باهوشا جواب بدید
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78276" target="_blank">📅 14:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تو جنوب لبنان داره نسل کشی و زمین سوخته سازی انجام میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78275" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78274">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXaeNJnrz-PQ6XPJxf1SgvNyyeXKYYdY7tY00TqeqiOcQwPUG14PNYXP6kE9Q5WuvJVJOAmWNnpT6e1r-gaYz3dZcEhCA-oXILSz78VUx_40FQKkhHDIklBYjW3oBb1gHLxpq-t7NKBAbzNJWk_vNYT--t-jbNl15_zZiCDMivalGKdL5g4qvZCXQTuAVwKi3Fyw2J8gdXPnhQVltI-V_xqmVkB9loaCsE-9oB3IDSiaTmckToU4CeummytVj0UnBpLEgBdX3tApSBIgVEe7De3OZNVO7Vqjj1Fxan0hbDn9yR4rBxDklIDqSN3GbwFMceyUXnoGb1NBw1ZjfjgfYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخواید اعتراض هم بکنید لااقل یه متنی بنویسید که با عقل جور در بیاد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78274" target="_blank">📅 12:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78273">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaZLjZSj7VHJhczo0SEmvloTA8_uuAvKeKFZj01IEMEs87wB5qv8loB3NdnEh4thxVy_68AwK1WRptLLpP03tyujwJbzMpIXG8pL-BtF9K5u_9W3NLJ3Di33jsJf7SRzFj-gzlumAPfqfZ2crJ_QOum3IMZ3awcQ6QjAMXGTWYXmAvH30QyHFojtpK2Znm0NwqXx8eOeqVTBI26KW0JLftIqWgF-RAGT5KGk3PFvaMsufNr_aRMcjIj0_tdxJI1TY5pechbhlXq1D7hnwE1KhtpxFfS2E04JRegG1L7J4ELZiqmQtMcHHTozXyi71THFlAvSjuc_5U3TfG3Mc_cPbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تیک‌تاکی ها هم کم کم دارن آدم میشن
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78273" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78272">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کاربران جدید،
0️⃣
0️⃣
2️⃣
🔤
شارژ اضافه برای اولین واریز
💳
وارد سایت شو و هدیتو دریافت کن و با خیال راحت پیش بینی کن
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78272" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78271">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzEbGp9ohCGGDeDCyqyN8Fbg6JmxDHJtYtyLb_JlnfO2ekxzGzse7MMXcP45a3iT-zOD1Sex0yIozKI2kOqJHUoOcT8W5Ut__WpxrUyLHtO5YomvYOpIuoUbL9GKufjv8G3WVtSsza1HEC6yOcn1pq6IrmjDRIQKiEWi_5h60JONxB2jM9ACqDqLEGjQHDVsexPLX97-aXOZrNIKmqNSpi65lch-8VPbLMGB2p7feat3VCNBBjzFgXNIcYAtabwcdnop6Hh3H5_PjGCfA9YnVIj87ultxxoFaAAQtuhMFjKjvs2JoCtQTqpdRsCAt458kEaqKfEW9ynVFSjFx2doTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
R30
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78271" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78269">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نمیدونم چرا بازیکنا برزیل نزدیک ۳۰ که میشن با هر بدنی تبدیل به شیشه میشن، من دوسال پیش اون بدن رافینیا رو میدیدم میگفتم این اصلا مصدوم نمیشه، حالا ماهی یبار مصدومه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78269" target="_blank">📅 11:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">الان وضعیت جوری شده فنای مسی دارن از پرتغال تعریف میکنن فنای رونالدو از آرژانتین
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78268" target="_blank">📅 00:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78267" target="_blank">📅 23:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گل دوم برای آمریکا
پوچتینو تیم خوبی ساخته
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78266" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ دوباره مصاحبه کسشر کرده که به خاطر اعصاب ممبر های عزیز ترجیح میدم پوشش ندم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78265" target="_blank">📅 23:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78264">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کشور جنایتکار آمریکا گل اول رو زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78264" target="_blank">📅 22:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78263">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بازی استرالیا و رقیبش هم داره شروع میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78263" target="_blank">📅 22:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78262">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGjOcE29cBS8MSGVh7tVef_nj1oIDMJ6nYQLZ1RQliYOjMnBsS7JgcV_4rK-3kP34LN_I-OwoJdX03EQccHsiOiptHe8cXOJKCEN97fQRlx8oWbWJpI-mmyYNkj9Jds6cTIjDjbqK9mvUhgKWJMvWQkR3pFtgYn3EObOwH-TUvb49_SoYjcjxddcydwC4kSqpjVJoCVlJqMGHG_RBGiVpJLmalaiEKgKI_7yhkRb-5oKfXqLnsCH6N1vASxpUd8ZlAIxXKKXxRbaBM2MBm9lwtXXvOAtR9PRzYfqooQjRn3Y_rGvsFhdbAV85OfhGjv2aPMWvuCjc68DBCXmFllYiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین رونالدوی موجود در جام جهانی 2026
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78262" target="_blank">📅 20:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78261">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj1aZ6k66Jov9RjZFBlBCXmiigKBj5dMlFvhhPd4Thmlfvk5zgQdFYR_RT2uu8NdMDrp8OMDOjbPl9XSyf6PZgf702QE81kWAMPYkIByxlYlw0ealqT3tz0yHrJN0_RFE41ztAzn9h4it7hoc4bl5HYkHVKYhBoBFqvBZu7zDyKKT3GXbXJOeHdFcERvN435-0r4VsKWN2g8jNVL-V0HMHSFeGoTYuX1dlAUzOX0YzP937YWbIi-HQX_Ps5hWrnolFylMiM29Hvh7RVaTF8Wh3Idc5HrEFLQWTz6xq396Fs1Rf8um-H3BD8NTtYcp0QpbMbXPhz_ZaKdCa8ZrqF2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید کون میداد تا بهش 10 بدید؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78261" target="_blank">📅 20:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78260">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فنای رونالدو به پیج کل بازیکنا تیم ملی پرتغال حمله کردن دارن فحش میدن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78260" target="_blank">📅 20:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHQToW90fl7ELlOIXhP9avIWQGyJrEb_OGTtVRASmsGuA9a1W452g1a4SyH8-1LEEz_N4E_WGYbDYaj9dYskn3_vAruW9ymuA2V20abvQ3SgG2RsEBhlagRsD7355xmNffhHwbAeQfjhVd_PiCaBPV8uKfoqls5V7fgg--c0HVkTLlV14SthlYRiCHUEtVwDDo4BAEFyDvnTBANav3CQqRDaZEQVsNpTdc-urHb6paKqI-Q8MH4_F3Y7aQ_9sUEEuriZr9MrZPk5_44PULHzVygUnY_iP6CuWXnA3sV1bYphp3RP2-Ts5i1rvCMeHZNUPISGLE-eq0pIlp47yjHJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید شایع به نام بلاتکلیفی منتشر شد.
Download
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78259" target="_blank">📅 19:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78258">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شایع ترک داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78258" target="_blank">📅 19:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78256">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7q4QR-mV3e52v9j2II9GekMX3xInyDhEt--fTaYXEN71bAHpzNjDDioT7Ju_csgL9eu4afx6B3j--hsouVtrrtB75Wjg60dF_UK_auy64QXb1rYcM1NaFJoQf7vaokOGXK-5fFyt_M_jPrkP6Ruz4QpyhKWGP-FutZD5cNAVUO1jhmof9sivRfCB9a2nBMRO_WjLCu0GJEl_ML3QGY2lBObjkD9KX9IZx8Buu4QbAVFe6wEHK16kXY04OzrOKjs0dVC0Z5mZJqmdTcILPHFeFpvCD74c2rDI6h5a-3y_h9sepe1EAsCtjqKuQ0pgNfqrFrXSXCQHqYsT1v_z1CMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حنیف عمران‌زاده: یه شب تو باغ با برادر خانمم مست کردیم تصمیم گرفتم از فوتبال خداحافظی کنم، به خانومم گفتم یه پیام تو پیجم منتشر کنه که من خداحافظی کردم از فوتبال، فردا صبح بیدار شدم از تصمیمی که گرفتم پشیمون شدم ولی رفتم تو گوشی یهو دیدم همه واسم پیام گذاشتن داداش تو ادامه مسیر زندگیت موفق باشی، منم دیگه مجبور شدم از فوتبال خداحافظی کنم با اینکه دلم نمیخواست این کار رو کنم.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78256" target="_blank">📅 18:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78255">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRAioHaoIAmBClMbd-urGB1gNEanayU24n9N7QvUzDWM9gHoMfN6o9Yb_xGZIW7oDGRl5BNCCL8J6RtCuNRZ4U9m1eYLWeYFh6_AVFQQZZSL_dxYwbSNj8PQNzONUdTWeqCSFaq8GonGVeR4TVKd_u8ysBkWFjv7ugNea0PRboiWSq086jaYpSRqeo0q4dxuUk1xabkc8dvNtcvCBMr8haDtLwoHZ6ltFAYzlKz6RqoeLwKT3skmPab5OO-2eKxcZTWeC-V6yx5iAkcXi0-5eYkPsFM5vIndkQeyREPwx9_mkG__e3zO_7BHWtpvmSHFv7gRyIEFVAlosfDXptqY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مردم.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78255" target="_blank">📅 17:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78254">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVxCjlbRMu_FXjejzZWaWGuLwoFCbq25Bxdl9sg7ImCilpBHHEiOY4OfuEVzrGjMJlCLWdmF5LvNjz_n3omIK9dSmrh_0rzdKFFV2iOVYckFqukSJVHXd0RPfcW9wYqI5BiYVCOVy_QoETJy-kuIG2NCRVXgQX73UuH-uyfETHpslKmIftIfoocvllInv2yGPiGmcrD66T9fI-bXYLOJuoBeSlNhH5IGAzJQtC_u9iQNuYn3rcPfUXCbZdcPcw9Qy9sRU-85T6yAyMTp7zx4K0njnaWigDs2bqGU8s8WA7r_keb2MHUgzgq-yHDbryRnuzwcYz9uZ-K7mV-9yPuBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مردم.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78254" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78251">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMKwi2LrJ1VJFe2rbEvQOdsgNx5ky4SEF86HlMb87623GDTwaDAzO41dDyiIhYwXqm-JFQmHa1YzEc05rOFRz3sJDv2dO6VtU1Oe2hyi99tDsKuDBczuqIRko8v1bJt33sKXfV07gxIEAI5Q3cXmU00sufPJXifGKwrCoNuNKGu4fy0FdUUnCbsZvXaym92corPbC9KT4WDzo9XohZDRIVW6PzmaqSEJNpS6JptAwIMYecgQdLoBN5LcTcIPyrjVc_ZJWCRvut768PdMhvUXIz14P9uDkVc1l0WJIyoWbMcEN7yyQZmiCT0mg5k-JmDmqYI0D2A3UnU38QzI2XF-Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژوتا یالا از قبر بیا بیرون پاس بده دیگه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78251" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78250">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntdGAad4usQIj6xa8TWazUpBKTnACsaOOKmZR6Rh7dzOgBEWGQFKqSeuqIwkTW34jg92xxkd2Y0VoxLGO6nr006JFJmhyN13JjUk-Io23gI_vyREO5foOfT6FsFCAkUrCAzwoHpQaCwA-qgrPRe65P0YGpWBU9qSC3dJBNErNnr6rqYuPta90-ICN6qwmpo4COs33PLzClQ4kesZ1UfPhgu5g_lk95iKZ4O2T7bcdqrOW1mqDie5ttnhknilul3k_BCSDslQ4hwfniVDn-UiXwiAfZOUHR_d7EUxTOZlQU9v4Qgk0ViThqd8xg-J-lJLnFd5R3zNCPg2762EHJBFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکزیک به عنوان اولین تیم به دور ۱/۱۶ صعود کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78250" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78248">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJVNklANZELzDHo_mZhOfPdrfj7EDQUR5Yof2PbNu7dK3l9BYMjUlV-rVCGq35ARaf_bH1a-G0DtNkkOQ3-2__Pc5-wts0zRZf5wSbBP1vmrLthmPbXHWtSAA-K2Tr8FVF22Z6jjKBtgDJT3MCoQ9qC2liF6Q0_eq0ClccpfQ57jmCeRD25cGr9mGIPvAug0_sXjezaIfS3r6Tm8RUzSEkPPa3tDSRgJqXtJgCnwfN01xEnScDdkRyGR4REmZBQ3NaywO4bsPD4D3X2gS_9SUx0nzs0umx3mVxEzV5y8nHR73-EAkG8z2DfqC0xZ3--gZo2FMG6DUkn9OVBHtHbvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در واکنش به لغو دیدار فردا و کنسل شدن مذاکرات:
«ما از روی استیصال به دنبال دیدار نبودیم؛ این ایران بود که چنین درخواستی داشت. آن‌ها تمام شده‌اند!
ما همان مهلت ۶۰ روزه را تا آخر اجرا می‌کنیم.
هیچ پولی هم دریافت نمی‌کنند؛ حتی یک سنت!»
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78248" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78247">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk-X1XBXiTXYVGhGyI6Ag2ZA893k7IVH8m8lYjsk-SCp7s36py6RxdNLmqGJ8wo25RBx3CF1j1FQOO9lFxSpKCbAkehi1fv-NMIvcV_CxAtn0OHRBzDsWxvs5M5DsDhQA44smG8TTD9ETvOcFtcKFSIkOz5O5d5RMBqEna5PrOKgX9MRpJ1H5cHPbzttIEziBeWyf8lKKGf0IRRPK7weFEjQ_Z4xG4007pRC2HUMpKoDpCjJDhIsDBgtuaf4STvlTvD5TSvXjP-O6bWVum9GmBW_5X8hC3JOBinUcbYtQSB5gWsXn6sBxcbQO9bluySe1c4nR2wmSZHXlcfEOMbp9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید بهزاد لیتو به نام "Late night drive" منتشر شد
SoundCloud
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78247" target="_blank">📅 15:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78246">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نتانیاهو: دستور داده ام، جنگ در لبنان با تمام قدرت ادامه یابد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78246" target="_blank">📅 15:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78245">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اسپویل از چند ساعت آینده:
ترامپ میاد خایه مالی میکنه و میگه اسرائیل باید حملاتش به لبنان رو متوقف کنه وگرنه باهاشون برخورد میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78245" target="_blank">📅 14:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78244">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سپاه باز تنگه هرمزو بست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78244" target="_blank">📅 14:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78243">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">معاون راهبردی پزشکیان: تجمعات شبانه باید جمع شود. آنها سلامت روانی جامعه را بر هم می‌زنند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/78243" target="_blank">📅 13:05 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
