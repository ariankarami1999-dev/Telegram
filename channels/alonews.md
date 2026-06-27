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
<img src="https://cdn4.telesco.pe/file/mztGlRduPcyRrBtusGH3aFM4QE7rNKfGZjDoFiqsmdhof-GTreXVrleH02dbLeAXBcTbYvEsjpiMxAjY65qdRVzC-wy2tsPngoLZdkKBnpXg7XdOS0mRRJ-NHk0xXK_xETHnUYlFZ-isTGKtc2Wh9eDWZpkLSXcG22-QpOuVxWk--L5VaHLTLPS1x6yycXU-yLkpPIW-EG9sMSsCNa5cQYM4BQFn7rxxa8mfmHLbZGZH3hRUsCqrhnkHZrx6VCHnvyTAFFYrXSnUz3WfmY68Q2u1PgCNg7xC4nNW4Tj5Y6Il1Q4pCfuqpLZWlm9PeykVnWKxbaWe8TKM4CNFNzmTXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 936K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 12:39:33</div>
<hr>

<div class="tg-post" id="msg-130473">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
رویترز: یک پهپاد اردوگاه یکی از گروه‌های مخالف کُرد ایرانی را در استان اربیل در شمال عراق هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/130473" target="_blank">📅 12:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130472">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
دبیرکل شورای همکاری خلیج فارس گفت که موضوع اختصاص ۳۰۰ میلیارد دلار برای بازسازی ایران در جلسات بین وزیر امور خارجه آمریکا و وزرای کشورهای خلیج فارس در منامه مطرح نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/130472" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130471">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ولودیمیر زلنسکی، رئیس‌جمهور اوکراین: با موشک‌های «فلامینگو» یک کارخانه تولید سلاح در منطقه ولگوگراد در عمق خاک روسیه را هدف قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/130471" target="_blank">📅 12:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130470">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=F9G_omQwlqhIvz0ecz6D62MbLEpG0WTAbx1viZKPr5d2ONKC6Wq7bpHWdOGz9C6db_OutwrBUWrjQVCc3tJ1h2Sp5YYKnAzzUSiR7OOqqxjEdOcspKvHELt8cAxu2F1QhjdoF0C6HG_dv2Cniq9iGDl3vbvjbSjC7R3a8cItBrVxw76x972BhkI61nAv0nB9wrjTyVxRAxhehzCoWJylAMUT5x0X3Ag2wOUfby2cLuMqjSyV5b0N27VaX5LWSXgpCajiUxxc9OUbQzYZWVt2vQ_nzgfQhDZUG9RmNhu0-L0mU0G0Pxh79IlCNo_ZmpbiF-2rnAm9YDmSfLNdm2jYkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=F9G_omQwlqhIvz0ecz6D62MbLEpG0WTAbx1viZKPr5d2ONKC6Wq7bpHWdOGz9C6db_OutwrBUWrjQVCc3tJ1h2Sp5YYKnAzzUSiR7OOqqxjEdOcspKvHELt8cAxu2F1QhjdoF0C6HG_dv2Cniq9iGDl3vbvjbSjC7R3a8cItBrVxw76x972BhkI61nAv0nB9wrjTyVxRAxhehzCoWJylAMUT5x0X3Ag2wOUfby2cLuMqjSyV5b0N27VaX5LWSXgpCajiUxxc9OUbQzYZWVt2vQ_nzgfQhDZUG9RmNhu0-L0mU0G0Pxh79IlCNo_ZmpbiF-2rnAm9YDmSfLNdm2jYkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از قبل و بعداز زلزله‌ مهیب ونزوئلا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/130470" target="_blank">📅 11:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130469">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
صحن علنی مجلس هفته پس از تشییع پیکر آیت الله خامنه ای برگزار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/130469" target="_blank">📅 11:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130468">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkBp2CicbLbzlWiOIUnOBa08Ujs4HLUgFXtJhGngFmg680apaIa11ikZbXt9B67wG7Jqn8H5XdXOYHS9pOCoRom0Ninrb0QvS11YNtCTXepLU-yAxDM6sby8G431rZYKpKyeuJQz8GZ5L-37P_9-8v5KlWaflUzx3hP_au9D0WtcPnsspCEdA4e1MarOW5RRo7sSCr79xHaB8-fz_IhX5hKDz5bq1xXYfIbuYkl5eErXngB1N41Is0qH9xMdkpzUPfN_B4D8UfCCeVNNEIm1B8qCA-87GG7kx9K8pVFtIiidiz7v0PqwKbEKZJNKrB3y2Q0aj9uFbWgTPPUxCpTEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تورم استان های بالای 100 درصد:
▪
آذربایجان غربی: 106 درصد
▪
ایلام: 114 درصد
▪
چهارمحال و بختیاری: 103 درصد
▪
خراسان شمالی: 103 درصد
▪
کردستان: 111 درصد
▪
کرمانشاه: 105 درصد
▪
کهگیلویه و بویراحمد: 100 درصد
▪
گلستان: 103 درصد
▪
لرستان: 109 درصد
▪
مرکزی: 101 درصد
▪
هرمزگان: 101 درصد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/130468" target="_blank">📅 11:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130467">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh8LfW09T9o-azPlUdys9xtrD9kpgIYuPvzkAxCqTAnoxQwowAqcYYEUZHEST15zA9p9hWF4M0tbE2GqxSz63eH-WjxIo7Z374m7DHX3vGSvhXTp3a-vCRn-Mt_vX7tlYn2J2-F5euL6ZUmnxOknlSVKP0Sj3ukh5Nx86VNFFFbM0XwdBmEu5S1bWElFdm9389cVcMnTTmO-DJLS4u8jqedIf7sx0TSMyRC3q-Th9mGVa5OaOkTHILIhTP1CqvxPR5Nyla8O_E2KvxmJZEuQ_FMybUvEyxsbTXZxfaW5Okczr1__uejIkCOYUQJ0dyg9Gy5VDb13JOKiM_A8rgTLkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ درباره جان بولتون: جان بولتون، نماینده سابق بسیار احمق، نامتعادل و بی‌مهارت ایالات متحده آمریکا، به تازگی به گناه خود اعتراف کرده!
🔴
او فردی وحشتناک، دیوانه‌ای است که فقط می‌خواست دردسر و جنگ راه بیندازد و هر جا که می‌رفت، بی‌جهت مرگ و ویرانی را به ارمغان می‌آورد
🔴
امیدواریم با او به شدت برخورد شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/130467" target="_blank">📅 11:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130466">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
با وجود اعلام برخی بانک‌ها مبنی بر رفع مشکلات، گزارش‌های مردمی‌همچنان از ادامه اختلال در خدماتی مانند کارت‌به‌کارت و دسترسی به حساب‌های بانکی حکایت دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/130466" target="_blank">📅 11:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130465">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbf31c890a.mp4?token=q2pNqKuKzz8SNoA_cqR0LXTmxzOrNrunBFFet3zh_wsY7rTZaMshRAY6UYMR977sSgU1eOn_95eeJl0NbsHtzv0RZvnO_y-Cw2lx1kuI16Dmrbkg4IspCNzhr5upKWKN2UNGnTdT7wpuTNWDhMIF3kD-dX0UAp62A9RtvOMa_NEBx9N31sb_RsjatA0vUDKgCuxjJXudo_fHiDFwbAt21wVEERrnV-ixIcJrA6UQYT854rRnTZAm6XC3KPdYMtWcA_RLSXfnCibxJ1YToQbGsYeT75nm63H3CLOm0FAJ1oEo712KlZL6J1zx-eEwcmm9ngcQCwZuSHNbqIa3du8Zeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbf31c890a.mp4?token=q2pNqKuKzz8SNoA_cqR0LXTmxzOrNrunBFFet3zh_wsY7rTZaMshRAY6UYMR977sSgU1eOn_95eeJl0NbsHtzv0RZvnO_y-Cw2lx1kuI16Dmrbkg4IspCNzhr5upKWKN2UNGnTdT7wpuTNWDhMIF3kD-dX0UAp62A9RtvOMa_NEBx9N31sb_RsjatA0vUDKgCuxjJXudo_fHiDFwbAt21wVEERrnV-ixIcJrA6UQYT854rRnTZAm6XC3KPdYMtWcA_RLSXfnCibxJ1YToQbGsYeT75nm63H3CLOm0FAJ1oEo712KlZL6J1zx-eEwcmm9ngcQCwZuSHNbqIa3du8Zeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صادق خرازی: یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور قرار گرفته!
🔴
کمال خرازی را به صورت استنشاقی در بخش عمومی ترور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/130465" target="_blank">📅 11:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130464">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سازمان حمایت: قیمت جدید خودروساز اصلاح نمی‌شود !
🔴
در شرایطی قائم‌مقام وزیر صمت با اعلام مخالفت این وزارتخانه با افزایش قیمت اخیر خودروساز، خواستار حذف نرخ‌های جدید از سایت‌ فروش شده که سازمان حمایت به‌عنوان مرجع قیمت‌گذار در توضیح اظهارات این مقام وزارت صمت اعلام کرد که «منظور قائم‌مقام وزیر صمت از اظهارات اخیر، اصلاح شیوه قیمت‌گذاری خودرو بوده و این سخنان به معنای اصلاح قیمت‌های اخیر ایران‌خودرو نیست.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/130464" target="_blank">📅 11:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130463">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: ارتش اسرائیل بخشی از نیروهای رزمی مستقر در جنوب لبنان را خارج خواهد کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/130463" target="_blank">📅 11:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130462">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2rHbfB8rgVFh0LkooK3E7_tA8WiO2JIOmODAvMzaNbp8l_7cu38UnptpWdSajwVAwAv5ArGIG3k5aXVSyrfhPvJuYciSdFuLH88_wulawaBlCFalCaA2xG12E4GMZ_TjLhiDveOZTcndMeczUYt8favFbHC-RCLiMVxzfeoeRAo6HEF6vYBj4WfuEh8qWc4JPMtz7Y812VttTVLm1uUrTygywcktKnLtz9yd2-EgXcMe6hzeLusacMAwn2-zfzImkuuwroUfnB_HseMhuRupMsXQGpMseUil19sA_cYIjSd8QvEPtPJKIa0pSUDui5MO7ca0ByD8l4xn_Z4APNRgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: بعد از حمله دیشب، هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود
🔴
منتظر تحقق شروط و واکنش شفاف و پشیمان کننده‌ی مسئولان مذاکرات نسبت به نقض تفاهم هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/130462" target="_blank">📅 11:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130460">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULFCw38VcYOSH1bicGLgCA4k1mxbk1j_gPBJVMLGlWI2-U7NkJMtWTmfaJMEOb3-SylGLQGGuN71cfDANPcQ6mfsUdbVMU7rnY8DrwBE-13LMrGQM2yuUdHhWdhuHj97zJXQeoDb9NQZOf4DqRlVPwZoBm6VHk4sSfXATjD-Bsma_VKqHi_9zqO-p2P_qQWiPFMRoUzl_O7s_7oF3TjIv3DjLO41dei3h_DNGdquCy61yAsY395sfxK8z8u-2PqSPt4b8fzwaWEcnubVz3kq-h67iBlJQtVv7JoFlptIRu3bT7sOkvOmLnCG83xGl7qTWUv3-00EdLU1Ypf_EKhuqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tq65GUsDnpC2S-WgshvHqnJavG6fAMYJ4XugpRXKP4blfqH81t_zC4tAhP_1uuK_5BlEhP-CkTCNxeh8TUdDGYxRprCy9H40nhhGVa_zjOVMHCwTRwCkR53QRyQI9xXL3KY83jH9g0I1N494sPn3iT1Wgw-TY_KEX2qJehOMW6E6zlvE0IzuxmwV23O6fHsrvGai3ERyO9zawESvNSAJOhp2Xj20SCkbc1I01ypkjOKVe4Yv0NBL2O03N309PRJuHRxZfGLBDqKN_JAutQ9CHZvCNLxLty9PcrrLvMw-O87nXkeKuVYuDDPF_0EpuWknqRTwm5qrhzrj6z3duekPig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شباهت عجیب سرمربی مصر به یکی از کائنان معبد آمون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/130460" target="_blank">📅 11:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130459">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/806fc925bb.mp4?token=IMdz2TsQZ96wrKqbzPOOZbfDGjE95LzU5s40tO8PTwiSoTH4nKOX6J_PvPgz3TAo58mej9xkhyFtQi4zFTQvIWU7mDV3YJiepNkuKaxsTQFVozhtgpW9aJy06t0G7w9z23j9UxVjMOT7t0HreFYOf9ghOvmKDj14s5E3hjtMoDvfK-TBktzbdSgZALqEZNFtZ1UjGw0FxWC7igozwRp28n-l6ivrF7_cgY7w6l5HlQyOrWp4hquMXnYKKc9kryT1tFhbnm-yCb9h2xHxjhureiBNSho0VUKzHCxrurkbCs0MZhFmpElpOptfI0tXIff27Wm_D3Wbwx6_eH0b1pIXTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/806fc925bb.mp4?token=IMdz2TsQZ96wrKqbzPOOZbfDGjE95LzU5s40tO8PTwiSoTH4nKOX6J_PvPgz3TAo58mej9xkhyFtQi4zFTQvIWU7mDV3YJiepNkuKaxsTQFVozhtgpW9aJy06t0G7w9z23j9UxVjMOT7t0HreFYOf9ghOvmKDj14s5E3hjtMoDvfK-TBktzbdSgZALqEZNFtZ1UjGw0FxWC7igozwRp28n-l6ivrF7_cgY7w6l5HlQyOrWp4hquMXnYKKc9kryT1tFhbnm-yCb9h2xHxjhureiBNSho0VUKzHCxrurkbCs0MZhFmpElpOptfI0tXIff27Wm_D3Wbwx6_eH0b1pIXTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام ویدئویی از حملات دیشب به ایران را منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130459" target="_blank">📅 11:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130458">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزارت خارجه ایران مدعی شد آمریکا با هدف قرار دادن چند نقطه در سواحل جنوبی این کشور، مفاد یادداشت تفاهم را نقض کرده است.
🔴
این وزارتخانه همچنین اعلام کرد حملات ایران ماهیتی «دفاعی» داشته و مواضع مرتبط با نیروهای آمریکایی را هدف گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130458" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130456">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f8NuMdWoGvXk_McXhSK-G_ZCqWUAoNeDoVVo3Dy3RSttgyHCKC8z03FBRAQRMXFPJUbvPXhCyU5DCMbLV0PF33Pcx466tI0abIEBIxeI2eEX6kzxtY7FzDOTrjzzROWbOfU_mZsDoiniip398G_kgj7GkLpC_uz2ViVLOs-zRp4tiAxYEO5ZhVqC7psCertovGsyzLj9O0-Y6omNwN0M6klnZB70sw5Ubfa4qY9QoPgFoHHClSDEcHfD8jaqsqYusPRjQ_GlwIvj4KOfIqFe7TafrOtxUYZ14y5L486_S1308POMi8dXdqi2oNv7sYoMLrGV0UcrQib_RRImdGCNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHndB_jbEdMWQQz3LEVSMsnePxxmbEZ0hKKPsmvx6Kxa3v1-EUqbVSVS6o9zvm0NNdQBJhpC6VfebVJSAj3advhziMkCS7cVKmTXOjaH0A4AAPd2aqpawE4CUep2y-EDhv1-7PYnUzGfOb74zTwGrrRhJDsJkjpZoYVrNYdTwH10Tq95jkWDK1pSoYvLB4Hfplkbm6m263nqZIQRj7WlIZdXHM1GF0Q46EL9xt5c9ypQlD-ddVzGB1rMmz70hwWCUbHnruPiCtB89RhAJtpMllbdKclcL6SSYdtys4kQ688rffwsAUPaRPGD3ykUpRfIgOfTvizxe0uLqfYClAuoWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شانس ۹۲ درصدی ایران برای صعود از نگاه سایت اتلتیک و ۸۵ درصدی از نگاه سایت اپتا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130456" target="_blank">📅 10:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130455">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
خبرگزاری ملی لبنان (NNA) گزارش داده است که نیروهای اسرائیلی بامداد امروز اطراف شهر مرقبا را که در فاصله حدود ۱٫۵ کیلومتری (یک مایلی) از مرز لبنان و اسرائیل قرار دارد، بمباران کرده‌اند.
🔴
این گزارش پس از آن منتشر شد که اسرائیل و لبنان در واشنگتن یک «توافق چارچوبی» را امضا کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130455" target="_blank">📅 10:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130454">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q30sMcoL0pBtE7iupjoRAZ_WJ2uuNPmEZ4i7b1S1UhTBaujc8YQB4lhFqjwGhATI8WkK3fHpyJkajkr_Hchfr1KmqxgqkAm9Of8XG0nPMo2sxQH6m_BCeMsttXasqADWJGIo9ORUuqvWC04mS6Px48GHMHbQJ0Eftm7OMuW-mpYLKYWv0j5OglLlDMCbM1BYpImNWufYCjmClqT87N_LbEsPkHgYBFc2wSwgKL5xdvNLYR_Tl1no10IO75zfoSbkuBsfkLmBkID0PWS0iuy9cLT7S5f5moKBjPXR_PBJnxdveMDuUt1x3dm34xMiLCCw8mURgYbuWPhupWjTpTiGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده دیشب به انبار پهپادی در جنوب کشور حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130454" target="_blank">📅 10:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130453">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
به گفته مدیر بنادر شرق هرمزگان، پس از حمله آمریکا در اواخر روز جمعه، هیچ خسارتی در بندر سیریک در جنوب ایران گزارش نشده است.
🔴
این مقام مسئول با بیان اینکه این بندر به طور کامل عملیاتی است و هیچ آسیبی به تأسیسات یا تجهیزات آن وارد نشده است، افزود: وضعیت در بندر سیریک عادی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130453" target="_blank">📅 10:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130452">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: ارتش اسرائیل بخشی از نیروهای رزمی مستقر در جنوب لبنان را خارج خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130452" target="_blank">📅 10:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130451">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozJZTxz4CH7-LZzKqVfs7cDY08DxoxuKVlV7L5LOUD25ZnGRkgO1AY640F-wW1cyz_rgLViD8BhhtTXm9BVvV7v2LOFf8F08eKlmKrS7Ow7NMa1ORRxqNkHZTCVPBxL4XxTqe68ucHpSG_VSdgu177PltV3ytIvXrGxFaVqhZcpFXJOhD7JPQD9HtqLEwwLqY9aURQb3hfGa-OQDuO8i_xsD_5S2VKPuR_PTB8eHaU9A6duLvrZk1vWxPcj6M6DMKzLp-y6EcB7pvSGrKO6VOvOLoBtQ9TrszarKkYDsx9vAkwjbHeYGvs4_DiF0rb7Xpk9atbpzOewD6DHNNJVD4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز آمار:‌ تورم نقطه به نقطه خرداد ماه به ۸۸.۶ درصد رسید
🔴
تورم مناطق روستایی در خرداد ماه نیز به ۱۰۸ درصد رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130451" target="_blank">📅 10:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130450">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DG4RdHq3cPmTxz7BW_pZjugOn-Fd9LM0IgrGKsltrCaXMV5Zb3JHBRm3JYOdI3Ml6gPT8cjSmTJcL4iWVEcsawVLLyJC2jyT6QyyGf9XT62Ez3-Oo0phBPEmObywqiLGsp5QfC_VG2nXtQou7zfEtemFuO2O4mMncdjuMUgyY5B0a6gn3U0AoG544Cawi5OsBR_7hpWbbA9gaJqWlOg4yTx8RVO60TakNqMgfN-aWLGpqDgEgBjY6AXG7Bq2pSoexsrBX3r4Pr9gjIHP9oF44NdNBD3EZS9n--mKbNxnYI0DmUByN0LVH9riBHFyf1bXnZjCBriU-gv7BkokiRzOag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش آمریکا با قراردادی به ارزش 36 میلیارد دلار خط تولید موشک های رهگیر THAAD را 4 برابر کرد
🔴
این قرارداد در ژانویه سال جاری امضا شده است و بزودی لاکهید مارتین آن را اجرا خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130450" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130449">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3293127d1f.mp4?token=aHwKoW0kZItrlpnXJOHby21O1-MU6lx2YpT4vAn2nybQlG8_0A0KmVbKMeBaF0a8GBn9VLwGG6Pm5dZyQfjN2G57HBfkjDSSYP1N1kyAd1_JxjaruaZ5EgCS1re3E4Qxa3m5eFYtNw4c4TyaoDP3b90rIra6ErbtRilUf2XJSRp01S38rmFuOFhm9kXtZfwEb2PU6Qef7T7ulbu3LjAsixSLrN-D84FI4IG-vAq1anyYTAknLWeAbVdIDBFh7iCK2wzJvzMmIaFEk0IcAC7EwuAOHq8iwTTXjNwUCooMg-ws8V9NRiIOP7TCZMh2qXOSCzr2_h_fs9R2aOBNejSqEol6UfYCM6NiCHFXHwoq-G1jVmm1gcDZN0hMPjkuyevMqQ-pC1CWpE2Ix8oRcQexO0cvCeMuaiGkSfWz2jAT44fV7aXE_c_ogZIeeQHf7nyrjPQL-27CaEcwCYI41MkoXJIOr32DNNktxy1JR78gGG5fgSRyuLqyap8yP7XyXY0sgMvJLfPVe35y-XBFfK0zeDEw54FxQA1uUjiGDvdR1Tskg7epwqLYsrKrqPktQ6ENkV-WGUYp6DYP0tfeBYArvwROd0M_B1-hQz1FXf7YVmfOge0Q3Y0E3Gfn0RTzAp88OR2wAo2jbyKuD19PpRAxzrGwzYSxOBOwxgYcYCXZdjs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3293127d1f.mp4?token=aHwKoW0kZItrlpnXJOHby21O1-MU6lx2YpT4vAn2nybQlG8_0A0KmVbKMeBaF0a8GBn9VLwGG6Pm5dZyQfjN2G57HBfkjDSSYP1N1kyAd1_JxjaruaZ5EgCS1re3E4Qxa3m5eFYtNw4c4TyaoDP3b90rIra6ErbtRilUf2XJSRp01S38rmFuOFhm9kXtZfwEb2PU6Qef7T7ulbu3LjAsixSLrN-D84FI4IG-vAq1anyYTAknLWeAbVdIDBFh7iCK2wzJvzMmIaFEk0IcAC7EwuAOHq8iwTTXjNwUCooMg-ws8V9NRiIOP7TCZMh2qXOSCzr2_h_fs9R2aOBNejSqEol6UfYCM6NiCHFXHwoq-G1jVmm1gcDZN0hMPjkuyevMqQ-pC1CWpE2Ix8oRcQexO0cvCeMuaiGkSfWz2jAT44fV7aXE_c_ogZIeeQHf7nyrjPQL-27CaEcwCYI41MkoXJIOr32DNNktxy1JR78gGG5fgSRyuLqyap8yP7XyXY0sgMvJLfPVe35y-XBFfK0zeDEw54FxQA1uUjiGDvdR1Tskg7epwqLYsrKrqPktQ6ENkV-WGUYp6DYP0tfeBYArvwROd0M_B1-hQz1FXf7YVmfOge0Q3Y0E3Gfn0RTzAp88OR2wAo2jbyKuD19PpRAxzrGwzYSxOBOwxgYcYCXZdjs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بیل ماهر: برنامه هسته‌ای ایران نابود نشده است.
🔴
جی دی ونس: کدام بخش نابود نشده است؟
🔴
ماهر: ما به آنجا نرفتیم. کل ماجرا این بود که باید به آنجا می‌رفتیم و بررسی می‌کردیم؛ در غیر این صورت، این کار را نمی‌کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/130449" target="_blank">📅 10:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130448">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
پی‌بی‌اس (PBS News) به نقل از یک مقام آمریکایی: ۶ فروند هواپیمای نظامی ایالات متحده، چهار هدف ایرانی از جمله تأسیسات راداری و انبارهای موشک و پهپاد را در منطقهٔ سیریک در ایران مورد حمله قرار داده‌اند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130448" target="_blank">📅 10:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130447">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
مرکز لرزه‌نگاری اروپایی مدیترانه: زمین‌لرزه‌ای به بزرگی 5.4 پاکستان را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130447" target="_blank">📅 09:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130446">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
صدای انفجار در دزفول ناشی از امحای مهمات است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130446" target="_blank">📅 09:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130445">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
شاخص بورس تهران با رشد ۵۰ هزار واحدی به تراز ۵ میلیون و ۲۱۱ هزار واحد  صعود کرد.
🔴
۶۲ درصد نمادهای بازار سبزپوش است.
🔴
در حالی که ۸.۳ میلیارد تومان به سهام، حق تقدم‌ها و صندوق‌های سهامی وارد شده، ۱۵۴۴ میلیارد تومان از صندوق‌های درآمد ثابت خارج شده است .
🔴
دو روز کاری پایانی هفته گذشته بیش از ۱۱ همت وارد صندوق‌های درآمد ثابت شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130445" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130444">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
شمار قربانیان زمین‌لرزه ونزوئلا به ۹۲۰ نفر افزایش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130444" target="_blank">📅 09:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130443">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f4d96d2d.mp4?token=jRsbv92lKRlrqBz1HbMJyk3z1n-LpGcORFaYAy7TyFaA3ePssvwpSlcdXiG53A8trUAsF2bi_n5GX8oA5XHBRAwkkA-e6KOf8-zpKDTzZm79Asl-P2iL4YlBKKLWLW0zOdUfP3AimiBVocp4Qp96ehDoqONGD-VMIzKe-txyWsk6iuTEPZvAU8y9UDz4HZWPR903sRH3RJaZydy_bZsi_TxDnFZGIV5On1s1wPbxxEcYCmElHFdrB3IYt9c7Bxu1R7BPo2MyczPMscG6ZbyG7iExA9Shj4f1fx3nWaSZPDra4lwiNmddkXdxFaRoHvf4tOSrSRRU0mWfHsnb9tml_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f4d96d2d.mp4?token=jRsbv92lKRlrqBz1HbMJyk3z1n-LpGcORFaYAy7TyFaA3ePssvwpSlcdXiG53A8trUAsF2bi_n5GX8oA5XHBRAwkkA-e6KOf8-zpKDTzZm79Asl-P2iL4YlBKKLWLW0zOdUfP3AimiBVocp4Qp96ehDoqONGD-VMIzKe-txyWsk6iuTEPZvAU8y9UDz4HZWPR903sRH3RJaZydy_bZsi_TxDnFZGIV5On1s1wPbxxEcYCmElHFdrB3IYt9c7Bxu1R7BPo2MyczPMscG6ZbyG7iExA9Shj4f1fx3nWaSZPDra4lwiNmddkXdxFaRoHvf4tOSrSRRU0mWfHsnb9tml_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قلعه نویی: اینم یه ازمایشه؛خدا داره منو میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/130443" target="_blank">📅 09:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130442">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qjs94HmXk9gw1pAzNEKA0KNa14HvSMcgaS88dLRPttwqrKAFFVtnFkEvSIBIkXnO-kCy5Idx_zq_DccTNSNDF_8ectbdjcgmUtJzXPUXyd6_Q9sjCL6vHosj4Ft9iAHxlmT389RLh3xbbzH6zo42uN-4h9ljph1-8Im_C1sKyvJPlSO00iqBg6lULb__VM9nyenryzcMm_4NhshbKfzfYfQWuBpUR-je3jnZ87Nz20LjD29pZDrrss0pYhXjiIKfCeWkn-Mta7itNkAg_UPOYpSujWhZKefZwmP2SFidti33VWvN_BxR30lYSgWqK2BioMaxYDtRVRxkfEb_VNxxQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری سردار آزمون پس از تساوی ایران و مصر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/130442" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130441">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
یک مقام آمریکایی در گفتگو با نیویورک تایمز: حملات علیه ایران به معنای از سرگیری عملیات نظامی گسترده و جنگ نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/130441" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130440">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
قوه قضائیه: موتورسواری زنان منع شرعی ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/130440" target="_blank">📅 08:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130438">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2gsCYVtKDBcbkROQDV7p2nkTXDTjoYB85J2nIKpwQ96QBYXjhZCqT41u7D9oVcqW2r8C7WVLvToOtg7-qfjj5UkwT0BfJGih5VWRfpSkGH37gyqTdtqnPLDTBweBuhb7Zdc_2cchKFxmUA20XJrWoobJ6hU-_c8A3FieZUrGnrt4d7IfHPhQ0MzTOjVI0gdcCb7dAo9s4ScqCZJ0hICRMAaIQpZTYN9-HZkdsRpHlcS-DJ6futht9NV4AJYLmtPdEeTUGa3pW4a_ln6nnqnIJiXs4FvjFPVT8QY12_DKMPmqzNg-vU5NsFcCeYJ5vaggsGcIIjw-oN6LnACUX0KPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ونس:
ایران توافق آتش‌بس را امضا کرده است. ما به آن احترام گذاشته‌ایم. اگر آنها در مورد نحوه اجرای تفاهم‌نامه اختلاف نظر دارند، می‌توانند تلفن را بردارند.
🔴
اما خشونت با خشونت پاسخ داده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/130438" target="_blank">📅 02:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130437">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام آمریکایی: حملات آمریکا حدود ۹۰ دقیقه ادامه داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/130437" target="_blank">📅 02:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130436">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXWDduVrkewAnqEyMNHIys__kH7t9dSFsA6UEeYbbigP7Io_J5ieN755hUC_Vj8woYakICbGjP79aYBYeCFouru-TC6drbn7lFCc5YMy_6ZSImrtbRmZT4NohzWYG0WFmnq8iTqtkv5F7VJyuwlIWZ7nnlbJEC_EXqxrdwvaNOYhRJzOU2qEHAfxBJG19KIwwChD48hgJ-S5T3ojgb8qWPINszIz-Y0svo7VbW-z3fXWkN1AE4dZWoCbIfbRCG-CWsdyro41_mqXaNh-CD4tayyhh6f4nuv-LB26rB2i5c23-TMx2eVCIEqgu09oaJDIBwesZSryBHPQj057HIv4eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی از ترس خوارج مجبوری خودتو قایم کنی.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/130436" target="_blank">📅 02:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130435">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ ۚ
🔴
به دنبال نقض آتش‌بس رژیم صهیونیستی در جنوب لبنان، ساعاتی پیش رژیم پیمان‌شکن آمریکا نیز مانند همیشه دست به نقض تعهدات خود زد و به بهانه‌های مختلف از تردد یک کشتی متخلف از مسیر غیرمجاز در تنگه هرمز به حمله هوایی به سواحل جمهوری اسلامی ایران اقدام کرد.
🔴
نیروی دریایی سپاه پاسداران انقلاب اسلامی در پاسخ به این تجاوز نقاط استقرار ارتش ترورستی آمریکا در منطقه را مورد اصابت قرار داد.
🔴
بر اساس بند ۵ تفاهم نامه اسلام آباد ترتیبات کنترل عبور و مرور در تنگه هرمز با جمهوری اسلامی ایران است؛ لکن آمریکا با تحریک جهات مختلف در صدد تخلف از این تعهد بود که پاسخ لازم داده شد و من بعد چنین خواهد بود. در صورت تکرار تجاوز، پاسخ ما گسترده‌تر از این خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/130435" target="_blank">📅 02:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130434">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ونس: خشونت با خشونت پاسخ داده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/130434" target="_blank">📅 01:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130433">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
فارس: سپاه فعلا نگفته به آمریکا پاسخ میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/130433" target="_blank">📅 01:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130430">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U70QlL27dYWCpw6jbzc-pamJ0AarFrNMlxd7SJfVpnmokM0NqHxp2I4XFvSh_f1aak7WU0NdqUiIIJcjcNXrFZkKZ0qXIkeZk2aJUIL8iE3POObphhFE4lCMgvFO-gt4C4CaKhxwwl2p3N_NCkoX3XrCGAqginTGugDw7L8op_ovsKKo576ig0UG32r2AeBrZ1P1eIdnAavdUfdG2QKmqEBXx8TzL8E5Eyx4izm9lgJyylCPi91LRXQH70eVwp1tVWbguui9y_Q9kepPzIaVDUueaZsrBCfHtFpOwkgCqFkSXdBAjO8dExGstLQgT91YdH1NshCUQmPxf0gae16q4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1bf794007.mp4?token=OKpzUATexcUpx8jDZ8n4ijOKOc8kpNZmNPHvJXwb7OTAgKpxULKB4J4M3hOI45gp72cURnOppeGJJpFfWKnqHH01L-U4hLlHxBBNoNA6VNC1bLiASd4H569EHXn-m6UvV81VFLMlZzesD0JA9gzi1pnspHjrO4SIQfBXxljQV3NiIyhy_TF0z5OFhJRQDr5QRVF64xW9uAriUqfqiE4FDwyn1LVWpNEoqdCB5b6I8LoL8UK-E5dnO7ToWgELm8FmEIp-mWK2ZppB7cGehQoQVTz8oEDjOxqjHiNr-DlO4f_1i0aWS3N5CymOptQ-UIo1jtOUWZuc0O9sRUfmaJmjig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1bf794007.mp4?token=OKpzUATexcUpx8jDZ8n4ijOKOc8kpNZmNPHvJXwb7OTAgKpxULKB4J4M3hOI45gp72cURnOppeGJJpFfWKnqHH01L-U4hLlHxBBNoNA6VNC1bLiASd4H569EHXn-m6UvV81VFLMlZzesD0JA9gzi1pnspHjrO4SIQfBXxljQV3NiIyhy_TF0z5OFhJRQDr5QRVF64xW9uAriUqfqiE4FDwyn1LVWpNEoqdCB5b6I8LoL8UK-E5dnO7ToWgELm8FmEIp-mWK2ZppB7cGehQoQVTz8oEDjOxqjHiNr-DlO4f_1i0aWS3N5CymOptQ-UIo1jtOUWZuc0O9sRUfmaJmjig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرکوب اغتشاشات در لبنان شروع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/130430" target="_blank">📅 01:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130429">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
برخی منابع عربی در خبری فوری از آماده‌باش در پایگاه‌های آمریکا در بحرین، کویت، قطر و عربستان خبر داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/130429" target="_blank">📅 01:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130428">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
رئیس جمهور لبنان:
اغتشاشگر را باید سرجایش نشاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/130428" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130427">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0-rPIps_OY1Oy4iaP2EIAHtuhvF-psQMMT7Ft1wtENAa7UxfFMJUvvqNBt7gVfNgsvolh8ksn6KKQzzwu8jUpNgu4owCttUt4Th8ScNllZZZ20AkQbgHA-oO05CKdpNyfoQXploMWlEJ8--5luq08E3E9n-iFWJkQQ6kpDLi0lkiNSvR-IXrOIClfZvQ_q_PyOAQpHWslIEd8eJIAjRIwmxxD8iBz-IQsw8Uf3j1-xjL4tUhtFpbkNEay5p6tQ1e_PKG-WsvURf9DTMJQGpER-mD74QLhvit_SE6BKpUWRK2kA2k4AWOKY8jHpj9o_ehAGTvCnRv63lmKash7vu5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای ارتش لبنان برای سرکوب اغتشاشات وارد عمل شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/130427" target="_blank">📅 00:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130425">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c12144a38.mp4?token=fm8siUt83P-Yx_2Ck78Cf96kTxLPkasPC-7i52FYAwFSncXfdDfllhjKvbeO7ZVlN26EYvpvX2gcQcc8LevKwFHSkw9eki6fO0rYWWSwLypBkfinn5cFFQorUfQpFmMSycely6QaMHqJROjn8PgQcH5JLt53iTR7j_KVRVXop9YYd08rI0HY_rUFaoLdXQAQ0WR8W-L8F63x-Ti-TO04IL7gv0p-hdoghaW8GlCm92E8hguJrtIh240JYv4Zld3DyKKXtJ_ZYYpds5fC0kEWsEbFi3zbPACqn9x9B3dEQsYFeqpYwf9ZaGDzSiVA5lPtzXyAdPvS6m843E1OlSDI4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c12144a38.mp4?token=fm8siUt83P-Yx_2Ck78Cf96kTxLPkasPC-7i52FYAwFSncXfdDfllhjKvbeO7ZVlN26EYvpvX2gcQcc8LevKwFHSkw9eki6fO0rYWWSwLypBkfinn5cFFQorUfQpFmMSycely6QaMHqJROjn8PgQcH5JLt53iTR7j_KVRVXop9YYd08rI0HY_rUFaoLdXQAQ0WR8W-L8F63x-Ti-TO04IL7gv0p-hdoghaW8GlCm92E8hguJrtIh240JYv4Zld3DyKKXtJ_ZYYpds5fC0kEWsEbFi3zbPACqn9x9B3dEQsYFeqpYwf9ZaGDzSiVA5lPtzXyAdPvS6m843E1OlSDI4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از اغتشاشات در لبنان
🔴
اغتشاشگران اموال عمومی را آتش زدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/130425" target="_blank">📅 00:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130424">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ارتش لبنان به سمت اغتشاشگران در جاده فرودگاه بیروت گاز اشک‌آور پرتاب می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/130424" target="_blank">📅 00:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130423">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
خبرنگار فاکس‌نیوز به‌نقل از مقامات ارشد دفاعی بیان می‌کند حملات هوایی آمریکا همچنان در جریان است که باتوجه به حجم تحرکات هوایی در جنوب کشور ادامه‌دار بودن آن قابل انتظار است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/130423" target="_blank">📅 00:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130422">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سپاه پاسداران: ما مقابله با حمله‌ای که توسط نیروهای آمریکایی به جزیره سیریک انجام شد را اعلام می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/alonews/130422" target="_blank">📅 00:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130420">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e331902452.mp4?token=gQK70XgD8rDtIEOsRxzladEgTTrg_soNIgh10kqn5k1haKqzoSzeIEACiZXg6I8UJDz3sDG9Jkr2nB_Dg-QhMO0AmSyJfngYopisfZRP5ofoeFow-gyAcnyL3yQVMd1DIViz5Vpn54Rm0Zb27ArRS_ZrC_tsOMV3GmZFQ6XtqjeCQYhqVXzJwcwVLuC9BDq_jjk66ORdNpUK1s4U_un5IDnAvXgAjyThKLEW9vwgxc-L2nPFYeLQB41SnkIecphhIEHmKJqjsEF8fBCmcRidmXUWPgjjfWWIG8VA-pJv-3hiCa_nzkZ28z-wxUDGat2MzDTIVSVZ9A0pf6frFXzTlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e331902452.mp4?token=gQK70XgD8rDtIEOsRxzladEgTTrg_soNIgh10kqn5k1haKqzoSzeIEACiZXg6I8UJDz3sDG9Jkr2nB_Dg-QhMO0AmSyJfngYopisfZRP5ofoeFow-gyAcnyL3yQVMd1DIViz5Vpn54Rm0Zb27ArRS_ZrC_tsOMV3GmZFQ6XtqjeCQYhqVXzJwcwVLuC9BDq_jjk66ORdNpUK1s4U_un5IDnAvXgAjyThKLEW9vwgxc-L2nPFYeLQB41SnkIecphhIEHmKJqjsEF8fBCmcRidmXUWPgjjfWWIG8VA-pJv-3hiCa_nzkZ28z-wxUDGat2MzDTIVSVZ9A0pf6frFXzTlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اغتشاش و کودتا هواداران حزب الله در بیروت در پی امضای توافق اولیه میان دولت لبنان و اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/130420" target="_blank">📅 00:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130419">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
گزارشات از جابجایی لانچرها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/130419" target="_blank">📅 00:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130418">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
تسنیم:
نقض آتش‌بس و تفاهمنامه توسط آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/130418" target="_blank">📅 00:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130417">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
خبرفوری/ حمله به تهران
⁉️
برخی منابع خبر دادند در صورت گسترش حملات، به تهران نیز حملاتی میشود
⭕️
@Akhbr_Fourii</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/alonews/130417" target="_blank">📅 00:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130415">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
فاکس نیوز به نقل از منابع آگاه: حملات آمریکا به اهداف ایرانی ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/alonews/130415" target="_blank">📅 00:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130413">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_Au69aRJuFPHkU0pyCzcVI1_kZ8tNcVZsyYXUjilxAPH2R8UtAo_WpZSvYWGvL-B7fA6xjiVly9xFZlVnWgHIZt9Dh59ZTFreJgkXVC4KEp0Uuc-Hw9XiVBXjS-hT2HN1uc5Fxpchv6ki9zDN1ktBmFhiUen3Bb9065W3oYQHhw4BHN5LyxM-vMI_s0K2OvJfKy9jih2UYjrbBXUFrCAUpSS_arn5e-L8S_wKp3ePIqei3ejEPiHq45XRdc8potmP1ZMwcM7ZRaTGUCdgXPWMnytiCktvZCKC6x5UNe7A84hem20t3P6SkV_zMtPZBYSy4Q3wW-kMM8YI6dX1A29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی آمریکا: ایالات متحده در پاسخ به حمله‌ای که یک کشتی تجاری را هدف قرار داده بود، ضرباتی علیه ایران انجام داد.
🔴
هواپیماهای ما حملاتی را انجام دادند که سایت‌های ذخیره‌سازی موشک و پهپادهای ایرانی و مواضع راداری ساحلی را هدف قرار داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/alonews/130413" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130412">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
گویا یک دکل مخابراتی در سیریک مورد حمله قرار گرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/130412" target="_blank">📅 00:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130411">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فووووووووری/بریزید اینجا
⬇️
https://t.me/+1RDlZFB3XPtlNzg0
https://t.me/+1RDlZFB3XPtlNzg0</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/130411" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130410">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی: ارتش آمریکا در منطقه تنگه هرمز حملاتی انجام داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/130410" target="_blank">📅 00:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130409">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQw0-iluI-Qd6Tef-Ai1IT2xPeaAHVJkgpAbUJtfVb4Ln3THO_hiOUFQftISHx__ZY2uAqrBy7p7Q-k1Y7WqOXW8emZRfiihNEuowS6zVfRIw_2mZ2SvbuWExF1Equ5ypU3Kqfse8wym5kLsBmKftQ06-3dA2SyFveHWK0R6D9HnHtyPD7vkcD47OeIp-1NXpsNxwsEsN2rxcYiobLxs2dhLUcmYDrodDJW_QHeWwdLIdr6g4PPfgUBe-t8VxIOf_B1hh_0Pk9Su8e0eCjRdMRbaeQvnFKDbn7g_jZECy_rLnBgeV3tZ37yZlnTmrY5aXLg71QApO9NyT8U7VkqJOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چندین هواپیمای نیروی هوایی ایالات متحده بر فراز امارات متحده عربی و ورودی تنگه هرمز در حال پرواز هستند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/130409" target="_blank">📅 23:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130408">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
برخی منابع ادعا کردند صدای انفجارها، صرفا نوتیف دریافت سویا و ذرت بوده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/130408" target="_blank">📅 23:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130407">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری/ترامپ: خواهیم فهمید چه میشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/alonews/130407" target="_blank">📅 23:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130406">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
فوووری/طبق برخی گزارشات، سپاه قصد دارد اهدافی در منطقه را در پاسخ به حمله آمریکا مورد هدف قرار دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/alonews/130406" target="_blank">📅 23:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130404">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری/سنتکام: اهدافی را در ایران زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/alonews/130404" target="_blank">📅 23:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130402">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوووووووری/ارتش آمریکا در پاسخ به نقض آتش بس از سوی ایران، اهدافی را در جنوب ایران هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/alonews/130402" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130401">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سه صدای انفجار در سیریک، هرمزگان شنیده شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/alonews/130401" target="_blank">📅 23:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130400">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tx3Q5ocuzgepeHIoJ3gYeAtS-H7yHYtejLMPrhFnh_jzH8jRfjaEQog8lMkNk27I9sk6H2ii5CN9g1ppvcppXDuBnUK9GvVxU10SFXf3NcuRhdLwOMpr3eYTY65WcDXt7DS3RM2gd31shKZpfi07vzlFuLOSKhXCmvBaQz1MIz3hE6TYSCj7-apoJSmfiM4Y06-KViygLQNsOQYUKl-mS_11AiYQcy3gCwK545JV-Isl7s58rMhbIobdjRmsHtJLp5OFalwDMNp0S6ilzCEVCatM-5Z3Cb7d_zkcLUwRIP789oesMWWm8Ak8XfEdN4xi030WlshZJAyIpabiO648BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این شخص غلامرضا قاسمیان است کسی که یه مکانی درست کرده به نام پناهگاه زنان خیابانی که اونجا زنان رو جمع میکنه تا خدمات جنسی بدن! و اسمشم گذاشته شلتر
🔴
قاسمیان در این ویدیو میگه خودمم اینجا میرم و میام
🔴
صدا و سیما هم یه هفته هست اینو هی میاره تو آنتن زنده…</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/130400" target="_blank">📅 23:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130399">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2nVkN7xid50G6Ec6m9uxIWFDW6wnu_rIr4P0XEDe746vSDeT_Vnb3vLt8Rut-RqYbCsiRnQX0ksSWRzduFb7ZnzjQRQNNjGv7WXICUvbnbti87_fLzhT_2JLEbeog9WW7gqbtc6kDbRc1NgWa-mSo5jr98nXN_n-hiCvqYQ22ZCFHvblBmwX2nTeKxRGyZ_MPA9Opk573ECjtUQZMcJrb5GAs12U4YyvCIHaxsfUfir24Dj27N8IDaaxt_BvT31TGhRTmXRZBeM1qEEJ6UEuXkY_gwP9wJBCvmjNidhDavuZ-OVdFdc2rYMwKHol1Kc6d0mOp__4oZSymcbLfIqYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موکب تنگه هرمز تو ضاحیه بیروت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/130399" target="_blank">📅 23:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130398">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: ما مجبور بودیم به ایران حمله کنیم، چون اونا دو هفته با داشتن سلاح هسته‌ای فاصله داشتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/130398" target="_blank">📅 23:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130397">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی: اگر دشمن خطایی مرتکب شود، جنگ بعدی دیگر مانند جنگ 40 روزه نخواهد بود، مطمئن باشید ما توانایی‌ های جدیدی را به میدان خواهیم آورد و آقای ترامپ بداند که اینبار تلفات انسانی گسترده‌ ای در پی خواهد داشت
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/130397" target="_blank">📅 23:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130396">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی: اگر دشمن خطایی مرتکب شود، جنگ بعدی دیگر مانند جنگ 40 روزه نخواهد بود، مطمئن باشید ما توانایی‌ های جدیدی را به میدان خواهیم آورد و آقای ترامپ بداند که اینبار تلفات انسانی گسترده‌ ای در پی خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/130396" target="_blank">📅 22:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130395">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
الحدث به نقل از منابع سیاسی لبنانی:
سخنان نتانیاهو با آنچه در پیش‌نویس چارچوب توافق پیشنهادی آمده، در تعارض است
🔴
«چارچوب توافق» با اسرائیل به‌صراحت از «استقرار مجدد مرحله‌ای» (عقب‌نشینی یا بازآرایی تدریجی نیروها) سخن می‌گوید
🔴
بر اساس این توافق، ایجاد مناطق آزمایشی با تصمیم یک‌جانبه اسرائیل امکان‌پذیر نیست
🔴
این توافق هیچ‌گونه به رسمیت شناختنی برای «منطقه امنیتی دائمی اسرائیل» در خاک لبنان در بر ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/130395" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130394">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: ما مجبور بودیم به ایران حمله کنیم، چون آنها دو هفته با داشتن سلاح هسته‌ای فاصله داشتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/130394" target="_blank">📅 22:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130393">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
حزب‌الله: چارچوب توافقی که در واشنگتن به امضا رسیده، از دیدگاه مقاومت مردود است و هیچگونه الزام یا تعهدی برای مقاومت ایجاد نمیکند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/130393" target="_blank">📅 22:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130392">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124d0585ad.mp4?token=JDalwuAMrEmCslPVofRg0IN6SEuU0XOtBeGEuovMAKipozKNneDqO_agv2PfnyJ1qsZaA7mXerZGn2DV3gn76R0UkJyLt_9nJd1txPGaVYwLTUJhT6HJEzaO5p1QXDzEOrmdHh44eYV39FHsNsH_xQiJEyDlW62R1XXfYOd71fJieoNiLV4ejwfnUVmLq_yL9-8Nml7DAdDEKy9T_7VIJEzgnKo1VpHVGsVtxLBbn7OJMr6U7I8eBtr-xAol9ShczdMdp5IBGai2Var8hTdfn91WhoqHj9lHx9iWFS-gfvt2FElv48A28Zj_zkEqp8ESxLQm0TgoHF419ejo9Jel6oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124d0585ad.mp4?token=JDalwuAMrEmCslPVofRg0IN6SEuU0XOtBeGEuovMAKipozKNneDqO_agv2PfnyJ1qsZaA7mXerZGn2DV3gn76R0UkJyLt_9nJd1txPGaVYwLTUJhT6HJEzaO5p1QXDzEOrmdHh44eYV39FHsNsH_xQiJEyDlW62R1XXfYOd71fJieoNiLV4ejwfnUVmLq_yL9-8Nml7DAdDEKy9T_7VIJEzgnKo1VpHVGsVtxLBbn7OJMr6U7I8eBtr-xAol9ShczdMdp5IBGai2Var8hTdfn91WhoqHj9lHx9iWFS-gfvt2FElv48A28Zj_zkEqp8ESxLQm0TgoHF419ejo9Jel6oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ توافق اوباما با تهران را «JCPOC» می خواند.
🔴
پ.ن:
Joint Comprehensive Plan of Action
است که در فارسی به آن «برنامه جامع اقدام مشترک» یا همان توافق هسته‌ای ایران (برجام) می‌گویند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/130392" target="_blank">📅 22:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130391">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ: کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که تابه‌حال در خاورمیانه رخ داده است.
🔴
من فکر می‌کنم خمینی (منظورش خامنه‌ای‌ست) و دیگران در ایران از اینکه من سلیمانی را کشته بودم خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
🔴
او یک ژنرال درخشان بود. او مردی بسیار بیمار از نظر روانی بود.
🔴
کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که در خاورمیانه رخ داد. مردم گفته‌اند که بزرگترین اتفاقی است که در ۱۰۰ سال گذشته رخ داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/130391" target="_blank">📅 22:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130390">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9bda5bb20.mp4?token=c3TPtRcy9eEj5Ra8IbyKKEvUxOoyDLZUC6Ixi7-cQC9OC68wMLJWTMHtAOkpJuM8KQekBaHoHiDVDj5HfVredhvjO8939bt627gqCY1b1dBfZxopJKeAiyfDzoKmukYlFfW5GWKZHiCsYY5fp4zrTgpyWDsBHxNeUDxnLKCSZ4s55mU7f4pla1BOxAVV2CDik3XuvaPAaHjeVDdIQ5BhwUGMDma4lmV35jj6WJqaLsrnmsAi-eYAvlktdDPfDarLs-dckgEzUK2HZSNPxifwjYU6PREiok1kaTl8OkGWq1uoy8VwWkMflWPd1Db8_gPtcKReAPkhxW2eSgmyIC-CH20Q3K0okWcz_NfDzzsg2jPoSkLLKfsgM6UuLeYPL3uSUFC2dXOrYRgpBfjmbO3dNPRLCMvnkYFis4ce61qgNRZV-TjuPNJP4UhC-CR6426bkxm--nE90IavKJEaMSfeNeSEoruabN-iRJmq0iEOHAElQdGgiqS67wKpl5VjQgd8SOSDWpmwHZYH1QeEhDipKMftvsJlzN92o-4G-cAdvzBlja0h60cGZXSWRR7jy7chr1gdo7DvvebwGWtW-eNX7eDpyI3pcigkPUUceAtSMAGn8HABEOhiYiPAZcpgI5SLqT_ZSXQe1g4KdWHFtUbqiNC3hzLtfJN6yvo0g7dD4dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9bda5bb20.mp4?token=c3TPtRcy9eEj5Ra8IbyKKEvUxOoyDLZUC6Ixi7-cQC9OC68wMLJWTMHtAOkpJuM8KQekBaHoHiDVDj5HfVredhvjO8939bt627gqCY1b1dBfZxopJKeAiyfDzoKmukYlFfW5GWKZHiCsYY5fp4zrTgpyWDsBHxNeUDxnLKCSZ4s55mU7f4pla1BOxAVV2CDik3XuvaPAaHjeVDdIQ5BhwUGMDma4lmV35jj6WJqaLsrnmsAi-eYAvlktdDPfDarLs-dckgEzUK2HZSNPxifwjYU6PREiok1kaTl8OkGWq1uoy8VwWkMflWPd1Db8_gPtcKReAPkhxW2eSgmyIC-CH20Q3K0okWcz_NfDzzsg2jPoSkLLKfsgM6UuLeYPL3uSUFC2dXOrYRgpBfjmbO3dNPRLCMvnkYFis4ce61qgNRZV-TjuPNJP4UhC-CR6426bkxm--nE90IavKJEaMSfeNeSEoruabN-iRJmq0iEOHAElQdGgiqS67wKpl5VjQgd8SOSDWpmwHZYH1QeEhDipKMftvsJlzN92o-4G-cAdvzBlja0h60cGZXSWRR7jy7chr1gdo7DvvebwGWtW-eNX7eDpyI3pcigkPUUceAtSMAGn8HABEOhiYiPAZcpgI5SLqT_ZSXQe1g4KdWHFtUbqiNC3hzLtfJN6yvo0g7dD4dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
اخبار فیک/جعلی گفتند که ایران امروز بسیار قوی‌تر از ۴ ماه پیش است.
🔴
آن‌ها تشنه‌ی انجام یک توافق هستند.
آن‌ها به ما بسیار زیادی می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/130390" target="_blank">📅 22:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130389">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e369539a42.mp4?token=kDq-G5CdcqC-YWMU1Wkx9bXodAsKnkw71R-I-jYPRuhH3l4-bBHoS07TpK2jV2wk_2jB_EEV41UlqaVBQRzDaBrUvlafT99LYtqobSZbdPgLb5L05cCoEOHnPys2T9DpiUBfAwNi5pZfhcx2FZ6KxcsqjRRAOBQdVwyQG_FwFICIehqwYjAukdvqw60RSxDcpFuokWw4lkkM-jGa8Ty3aMNQpUsb4rYnJn6mjjNmfDn9K4RVWr8GLIFVybOBYjJ179ocBTxncYqjtqcx4tk-QmwH-7HwQz_SplgVjL7Hwilbcv2uzEYmFksK__N5GXt_YoA9CGlTS0EomBC0ROi-Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e369539a42.mp4?token=kDq-G5CdcqC-YWMU1Wkx9bXodAsKnkw71R-I-jYPRuhH3l4-bBHoS07TpK2jV2wk_2jB_EEV41UlqaVBQRzDaBrUvlafT99LYtqobSZbdPgLb5L05cCoEOHnPys2T9DpiUBfAwNi5pZfhcx2FZ6KxcsqjRRAOBQdVwyQG_FwFICIehqwYjAukdvqw60RSxDcpFuokWw4lkkM-jGa8Ty3aMNQpUsb4rYnJn6mjjNmfDn9K4RVWr8GLIFVybOBYjJ179ocBTxncYqjtqcx4tk-QmwH-7HwQz_SplgVjL7Hwilbcv2uzEYmFksK__N5GXt_YoA9CGlTS0EomBC0ROi-Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره رهبری در جمهوری اسلامی ایران:
دیگر کسی نمی‌خواهد رهبر ایران باشد. گفتند: «چه کسی دوست دارد رئیس‌ باشد؟» و همه گفتند: «نه، ممنون.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/130389" target="_blank">📅 22:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130388">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ درباره شهردار نیویورک:
شهردار ممدانی که به نظر آدم خوبی می‌آید، گفت که قصد دارد مطمئن شود مردم افزایش اجاره‌بها را تجربه نمی‌کنند، حتی اگر هزینه انرژی افزایش یافته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/130388" target="_blank">📅 21:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130387">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a205f15b6.mp4?token=Y7j5zWxVceNlI_0aJHmsK1gK6OL2KiY0DHH3nPrrOS-YZexJIlwBMyXiYJoKqj16br2dYqKNLueBcO5y0GIxJa1zsvcCuruRaxxZqgTM92dmf9j0fR09TvADf9JcJIJ3vmm1dZCa7lUHJoj90BIo6PQMke2xx_8RLK1vrI8Msy5isA_cINmimi_suGXRM0VYhetJaXxNvnyEeHsg8hLop6dF8qkSyPc-ak_EpXBaBRJsRjcdJFvky4K3LkKKbb0AGYJDB_p1F_bEyYOYfJ_LhQ6o3Rof54WD6ye1woSfMuM0tvwBnBAl4zFRUMwoOtuSnQPx45SJFzKkpdHQ3yRS-EOPs-HLooR_dpIs0bp6OF-zznXel7sID-ETTl170ZF8p3qKSP0WfVmR8AgZs5o9QLR2AZoyyrjimGeF-qpBRqc-_t7O5jfOqP45JHP6XHc7FnmMvhNDHuxZzPQlz9J8VcKA6AldJyI8HecVgPgt2-UzJoghAP-JI0zSIRVTb8Td5UJMaD0Dy-JCqhrDPkJpCggMvoqG8a0FHm7YWH2AgZ9oyd3F074KWBJaE-L36ZYbfrP0VoXLDz5aebdvk0-shplOgrCmWdRkJ93QCOAjngncH_hQl0drpycPJ8c_tWZQkNuEmxRQ5iNnA4csUrmDguCS2YhagtmARvdIhLEDlNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a205f15b6.mp4?token=Y7j5zWxVceNlI_0aJHmsK1gK6OL2KiY0DHH3nPrrOS-YZexJIlwBMyXiYJoKqj16br2dYqKNLueBcO5y0GIxJa1zsvcCuruRaxxZqgTM92dmf9j0fR09TvADf9JcJIJ3vmm1dZCa7lUHJoj90BIo6PQMke2xx_8RLK1vrI8Msy5isA_cINmimi_suGXRM0VYhetJaXxNvnyEeHsg8hLop6dF8qkSyPc-ak_EpXBaBRJsRjcdJFvky4K3LkKKbb0AGYJDB_p1F_bEyYOYfJ_LhQ6o3Rof54WD6ye1woSfMuM0tvwBnBAl4zFRUMwoOtuSnQPx45SJFzKkpdHQ3yRS-EOPs-HLooR_dpIs0bp6OF-zznXel7sID-ETTl170ZF8p3qKSP0WfVmR8AgZs5o9QLR2AZoyyrjimGeF-qpBRqc-_t7O5jfOqP45JHP6XHc7FnmMvhNDHuxZzPQlz9J8VcKA6AldJyI8HecVgPgt2-UzJoghAP-JI0zSIRVTb8Td5UJMaD0Dy-JCqhrDPkJpCggMvoqG8a0FHm7YWH2AgZ9oyd3F074KWBJaE-L36ZYbfrP0VoXLDz5aebdvk0-shplOgrCmWdRkJ93QCOAjngncH_hQl0drpycPJ8c_tWZQkNuEmxRQ5iNnA4csUrmDguCS2YhagtmARvdIhLEDlNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ با اشاره به پیام کمی پیش خود در تروث‌سوشال در طعنه به کمونیست ها:
راستش را بگویم — فکر می‌کنم من بزرگترین کمونیست در تاریخ می‌شدم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/130387" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130386">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ: تمام کمونیست‌ها بی‌خدا هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/130386" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130385">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aa291828e.mp4?token=hmqZMB6HWT1VX6860kOmeIKPaOetsOjJdQmBvMWIdf3YgEP9ALb708F669EfKXOhdd1VsXJ9RBQXiffTRd_J2waXCkTHJ_mW6vmrm1MlrLofVrtolxIeKXuvdoQc5q-TyljXRFCqCgTTseeO82uRO-lBDsosc-fqu9tXSHlleJc909QsMpievjPhQ9hoxuD_wQDGY2gH2dfZnkSYu2NyZhzDkLzKuCgZ51UlukZHr-n7AQGOs07OGXFHgORU7zEukUoRySiwQtRgmnLnAOETbh5lFIMwJFDwsA9w-AfrPesmMSzDIOlZ21eghVYfNDhC6fnI3xePBYMDh-OvWBE9FngkeTqODxKbJtgEJwyBvSSFyiOYGOqqKAzHtN2Wz8c-PUcEZrJb3v8McLxWparUl67rNwtf9YpkKpZsoHvN_aUVLdw5XX4BgLoFL4WKGxKc_TBaipvJffOHsuwCjNWHE9iZRugIlx2HSGEb7dBk77o5jMp8QEdftafqsdlUV5-9X0P-sj9cCpan2KnC7BfVbaWOufhTH9okCCQ-QEPavgCbi_GrCMbCl4cpRlRFKggrk7RMPrz2ofqaCnnOIAIDsYWJVgGSbFDZjNSYx07bOmRmPxo3V768fevDi4_oUrmghLJ34GNaNdqBMoly0mRiRVwt0_0tDTizAv-HYd915sI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aa291828e.mp4?token=hmqZMB6HWT1VX6860kOmeIKPaOetsOjJdQmBvMWIdf3YgEP9ALb708F669EfKXOhdd1VsXJ9RBQXiffTRd_J2waXCkTHJ_mW6vmrm1MlrLofVrtolxIeKXuvdoQc5q-TyljXRFCqCgTTseeO82uRO-lBDsosc-fqu9tXSHlleJc909QsMpievjPhQ9hoxuD_wQDGY2gH2dfZnkSYu2NyZhzDkLzKuCgZ51UlukZHr-n7AQGOs07OGXFHgORU7zEukUoRySiwQtRgmnLnAOETbh5lFIMwJFDwsA9w-AfrPesmMSzDIOlZ21eghVYfNDhC6fnI3xePBYMDh-OvWBE9FngkeTqODxKbJtgEJwyBvSSFyiOYGOqqKAzHtN2Wz8c-PUcEZrJb3v8McLxWparUl67rNwtf9YpkKpZsoHvN_aUVLdw5XX4BgLoFL4WKGxKc_TBaipvJffOHsuwCjNWHE9iZRugIlx2HSGEb7dBk77o5jMp8QEdftafqsdlUV5-9X0P-sj9cCpan2KnC7BfVbaWOufhTH9okCCQ-QEPavgCbi_GrCMbCl4cpRlRFKggrk7RMPrz2ofqaCnnOIAIDsYWJVgGSbFDZjNSYx07bOmRmPxo3V768fevDi4_oUrmghLJ34GNaNdqBMoly0mRiRVwt0_0tDTizAv-HYd915sI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کلمبیا: من ال تیگره را تأیید کردم. او را دوست داشتم. می‌دانید چرا؟ چون او مرا دوست دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/130385" target="_blank">📅 21:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130383">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ: بنیان‌گذاران ما چهار بار در اعلامیه استقلال به خالق اشاره کردند. چهار بار. من حتی یک بار هم ذکر نشدم. من بسیار ناراحت هستم. حتی یک بار.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/130383" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130382">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ: دین در کشور ما بازگشته است، بزرگتر و قوی‌تر از آنچه در سال‌های بسیار زیادی بوده است.
🔴
برای اینکه یک ملت بزرگ باشید، باید دین و خدا داشته باشید. اگر آن را نداشته باشید، به نظر نمی‌رسد که کار از آب دربیاید، آیا نه؟
🔴
زیر نظر دموکرات‌ها، کاتولیک‌ها توسط اف‌بی‌آی هدف قرار گرفتند.
🔴
مادر بزرگ‌های حامی حیات به زندان افتادند برای دعا کردن.
🔴
اعضای نیروهای مسلح ما به خاطر باورهای مذهبی‌شان از نیروهای مسلح اخراج شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/130382" target="_blank">📅 21:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130381">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e316bf1446.mp4?token=FUnWDAVjV8kYy4GZmfra6GJukLGILC7hCRIW76P72mo-iq7m21NKscx0dpffKWv13ntETftXiaVXPhYnlf6YwfN5olJdepKHi0IbjhVf2lj1iptC_8wI-vETElQUGJngmY0z9tyNe4NxPfpeTOHZPeyXhKCDwrw4OIgABHC-tD_w6OBnQWhMBvbmIoHCh1X52P0kHv3ICm7GES6LpcoUbLDIJ_4xvcKl3_mxkA480zadAHs2j8aGa-4ZvYeUB5M10CnM0gHiER4gvQo7n4tPsTa5s_PNUdgn-PNsJ8-2JHaAsQXcLEEoVgxyT0K-k3HzIlt0RF4n7tsilXvSYiBWXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e316bf1446.mp4?token=FUnWDAVjV8kYy4GZmfra6GJukLGILC7hCRIW76P72mo-iq7m21NKscx0dpffKWv13ntETftXiaVXPhYnlf6YwfN5olJdepKHi0IbjhVf2lj1iptC_8wI-vETElQUGJngmY0z9tyNe4NxPfpeTOHZPeyXhKCDwrw4OIgABHC-tD_w6OBnQWhMBvbmIoHCh1X52P0kHv3ICm7GES6LpcoUbLDIJ_4xvcKl3_mxkA480zadAHs2j8aGa-4ZvYeUB5M10CnM0gHiER4gvQo7n4tPsTa5s_PNUdgn-PNsJ8-2JHaAsQXcLEEoVgxyT0K-k3HzIlt0RF4n7tsilXvSYiBWXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسایی وقتی قالیباف رو تو مجلس میبینه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/130381" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130380">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa0bb5024.mp4?token=CWyGi3hU3RlfGhSU7wXdJP-hrDgDlcIVZtprvXZ9Ik9vRq0BKq99s5msCoHsLE2Vj3FD2Y6e4mETX1xndkTsRMlwfpSyaB5EHoHEuLbrvJSls6MzjSfJ4LgwI6WfSQWP7OX0mqdF4cjbAG7sGisj9oiF4ZaUkF1JaG9k1MXnr82hkA47pCPJcuN-MWP-1ojjPs5XW3W2Nf1G3kfGZhvpI4isJBIjh6oBHJtjygtc7DP1g23jA4IUhLyvpPC7_7Y9WtOHfODKenKSyCAicyuUZKNh0B38Npj1MLyF58DO9Rt7DD7SmNrDmHczmqR3zcmoYm9amXUB-LamBvURG_pYTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa0bb5024.mp4?token=CWyGi3hU3RlfGhSU7wXdJP-hrDgDlcIVZtprvXZ9Ik9vRq0BKq99s5msCoHsLE2Vj3FD2Y6e4mETX1xndkTsRMlwfpSyaB5EHoHEuLbrvJSls6MzjSfJ4LgwI6WfSQWP7OX0mqdF4cjbAG7sGisj9oiF4ZaUkF1JaG9k1MXnr82hkA47pCPJcuN-MWP-1ojjPs5XW3W2Nf1G3kfGZhvpI4isJBIjh6oBHJtjygtc7DP1g23jA4IUhLyvpPC7_7Y9WtOHfODKenKSyCAicyuUZKNh0B38Npj1MLyF58DO9Rt7DD7SmNrDmHczmqR3zcmoYm9amXUB-LamBvURG_pYTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حداقل ۹۲۰ نفر کشته و ۳۳۶۰ نفر در نتیجه زمین‌لرزه‌های سه‌شنبه در ونزوئلا زخمی شده‌اند، طبق گفته خورخه رودریگز، رئیس مجلس ملی ونزوئلا
🔴
او افزود که حداقل ۱۷۲ نفر همچنان زیر آوار گیر افتاده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/130380" target="_blank">📅 21:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130379">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09db5bdb36.mp4?token=DzXLmqWDG59TFsWBAvQpBZigZl4dcAwIg1IExOGJVSMn1jnf07e1ax_QmubnKl2w4xivOmE6XheJLHZqGBeEQv_XkxPoHXU4cvQ8-ZZXliTlJxUeBjLg9YmByU1yur4DvN-N_8JQCk09Rt3toJn8iCMAwR8drsq21eBIrDsQRSwFDhlHYdjxpLTn5ErGeQ5CJwv6twb_JlnsCWtFfV82Cu5DCzMI2z4owZpH0Azk1LsxoVDLs7k5Wd6as9iSyy8JRJTrWuqBIEuq8p0aV_8tB5ixqoJeyccTt9qRB506eyx-u4cC39g9ISZYvk6oolMwCSfLoYxARtUgcbZw-bAXlGzIm4VEzhjxLEmSPUE8EKBhbV1O1oagDqUSDDCcSVvNQHxYutmDoty8_s9vnOg_t7vO1ql31bhGAlygK33SZybLK1b3bWZI5mFxqH-RkTqqxnQmJq0X1Nx3qM7o3rbbU9oSrIowOaFeCNlZdDZ1HVZKPGsoNyoI0jNEqwJcCRx5qwQqdacasqTju1X4ZDdxvs2Ob5diomA_F8PnnFtGvQsMpkV79YrO0bNAFGRbniqWjvvGohV5n1TACRV3eFJ1l3qmU07Cd_I8kMW1GJuAY_oiw73lK6xwkhfhw7aI9rGa3uRdJ6s4EvW4aptlQtPREW0na0aqrnQMizZ1tNQsmTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09db5bdb36.mp4?token=DzXLmqWDG59TFsWBAvQpBZigZl4dcAwIg1IExOGJVSMn1jnf07e1ax_QmubnKl2w4xivOmE6XheJLHZqGBeEQv_XkxPoHXU4cvQ8-ZZXliTlJxUeBjLg9YmByU1yur4DvN-N_8JQCk09Rt3toJn8iCMAwR8drsq21eBIrDsQRSwFDhlHYdjxpLTn5ErGeQ5CJwv6twb_JlnsCWtFfV82Cu5DCzMI2z4owZpH0Azk1LsxoVDLs7k5Wd6as9iSyy8JRJTrWuqBIEuq8p0aV_8tB5ixqoJeyccTt9qRB506eyx-u4cC39g9ISZYvk6oolMwCSfLoYxARtUgcbZw-bAXlGzIm4VEzhjxLEmSPUE8EKBhbV1O1oagDqUSDDCcSVvNQHxYutmDoty8_s9vnOg_t7vO1ql31bhGAlygK33SZybLK1b3bWZI5mFxqH-RkTqqxnQmJq0X1Nx3qM7o3rbbU9oSrIowOaFeCNlZdDZ1HVZKPGsoNyoI0jNEqwJcCRx5qwQqdacasqTju1X4ZDdxvs2Ob5diomA_F8PnnFtGvQsMpkV79YrO0bNAFGRbniqWjvvGohV5n1TACRV3eFJ1l3qmU07Cd_I8kMW1GJuAY_oiw73lK6xwkhfhw7aI9rGa3uRdJ6s4EvW4aptlQtPREW0na0aqrnQMizZ1tNQsmTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل: شهروندان اسرائیل، پیش از آغاز شبات، می‌خواهم دستاورد بزرگی برای دولت اسرائیل اعلام کنم. می‌دانید که مذاکراتی در واشنگتن بین نمایندگان اسرائیل، لبنان و ایالات متحده در حال انجام است. مذاکرات طولانی که امروز به ثمر نشسته‌اند.
🔴
مهم‌ترین نکته این است که اول و بیش از همه، اسرائیل در منطقه امنیتی جنوب لبنان باقی می‌ماند. این یک دستاورد بزرگ است و ما آن را تا زمانی که حزب‌الله تسلیحات خود را کنار نگذارد و تا زمانی که تهدیدی برای دولت اسرائیل وجود دارد، حفظ خواهیم کرد.
🔴
این همچنین ضربه بزرگی به ایران است. ایران سعی دارد ما را با زور از جنوب لبنان عقب بکشد. و در واقع، اسرائیل، لبنان و ایالات متحده به آن‌ها می‌گویند - این کار شما نیست. شما هیچ نقشی در لبنان ندارید. نه شما، نه حزب‌الله، نه هیچ سازمان تروریستی.
🔴
نکته دیگر این است که البته، ما به ارتش لبنان اجازه می‌دهیم تا برای به دست گرفتن کنترل اراضی سازماندهی را آغاز کند. ما در حال انجام دو منطقه پایلوت هستیم. هر دو توسط ارتش اسرائیل توصیه شده‌اند. و یکی واقعاً خارج از منطقه امنیتی، جنوب رود لیتانی است، و دومی شمال لیتانی، بخشی کوچک از آن در منطقه امنیتی گسترده‌ای است که ما در دو هفته گذشته تأمین کردیم و ارتش اسرائیل به آن نیاز ندارد - این را بسیار به وضوح می‌گوید.
🔴
ما دائماً منطقه امنیتی اصلی را خارج از برد موشک‌های ضدتانک حفظ می‌کنیم. ما اجازه نمی‌دهیم حزب‌الله یا جمعیت وارد آنجا شوند. این حفظ شده است. و مهم‌ترین نکته این است که اسرائیل می‌گوید: امنیت ما اولویت دارد.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/130379" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130378">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
اسرائیل و لبنان رسماً یک توافق‌نامه چارچوب میانجی‌گری شده توسط ایالات متحده را در واشنگتن امضا کردند.
🔴
این دو کشور مذاکرات رسمی را در سطح رسمی آغاز خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/130378" target="_blank">📅 21:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130377">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJAONrHYeCvJcJz1tRHZs9s2hGIyWq5D6fdOdjSm-ukh1KvaZUdrmiffQRGDwvLPB33vcs72uykZLlJSDl7OM6JPRpbfxJcEWeozrfz0vhK26xxdkrV_pePDPfMaHOaR7epYVbIyfy0kCksnPEro4DvIwi5ic8SVfTGAzQoXPwupMuEIcysNLlY0emzt7C67RZdjxOvxBqUBE2jwQgY7IpZBk8WAYvRdehb9w9Q8vCJswtCYJQ8KXuCoIr1Qlslo8UTKQtD-qxFneRokxVmHDnJQw-Guk-Fele2c-Omf_HqUjbF1A1E9ng19FiF0e1v36jdC9jkdl9CVhYA6NNRM3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: کمونیسم بسیار آسان است برای فروش. من بزرگترین کمونیست در تاریخ خواهم بود. من اجاره رایگان، خانه‌های رایگان، غذای رایگان، همه چیز رایگان می‌دهم. متأسفانه، پس از دو یا سه سال، کشوری که این اتفاق در آن رخ می‌دهد شکست می‌خورد. همیشه اینطور می‌شود، و سپس شروع به زندگی در فقر و فلاکت خواهید کرد.
🔴
غذایی نخواهد بود، مسکنی نخواهد بود، ارتشی نخواهد بود، هیچ چیز نخواهد باشد. شما از هر نظر یک کشور جهان سوم خواهید بود و همه رنج خواهند برد یا خواهند مرد. متأسفانه باید بگویم، اما ترور کسانی که با آن‌ها مخالفند، یک عنصر بسیار مهم در ایدئولوژی آن‌هاست. آن‌ها حیوان هستند! در بسیاری از موارد، باهوش نیستند اما، در برخی موارد، آن‌ها هستند.
🔴
برای آن‌ها آسان است که پیروان جذب کنند زیرا وعده‌هایی می‌دهند که می‌دانند نمی‌توانند به آن‌ها عمل کنند، و دموکرات‌ها در برابر آن‌ها نمی‌جنگند. آن‌ها به آن‌ها اجازه می‌دهند راه خود را بروند. آن‌ها می‌ترسند که انتخابات خود را از دست بدهند، آن‌ها از درگیری می‌ترسند. آن‌ها به اندازه کافی باهوش یا سخت‌گیر نیستند که با این طاعون بجنگند.
🔴
اگر آن‌ها را همان‌طور که با جمهوری‌خواهان یا من می‌جنگند، بجنگند، پیروز می‌شدند، اما آن‌ها شجاعت انجام این کار را ندارند. این‌ها دموکرات‌های اجتماعی نیستند، این‌ها کمونیست‌های سخت‌پوش و بی‌خدا هستند. این جدی‌ترین تهدید برای کشور ما از زمان تأسیس آن ۲۵۰ سال پیش است. آیا این مسخره نیست که ما در حال جشن گرفتن یک تولد بسیار مهم هستیم، و به جای صحبت درباره مسیح، آزادی و پیروزی‌های انواع مختلف، درباره تهدید دیگری برای بنیان‌های آمریکا صحبت می‌کنیم؟
🔴
این کمونیست‌های بی‌رحم به تمام ادیان حمله خواهند کرد اما، به ویژه، مسیحیت - آن‌ها همیشه این کار را می‌کنند. تمام کشورهای کمونیستی به خشونت به ادیان حمله می‌کنند. همان‌طور که می‌دانید، ما اخیراً به نیجریه ضربه زدیم و عمدتاً کشتار جمعیت بزرگ مسیحی آن‌ها را پایان دادیم. آن‌ها می‌دانند که اگر بیشتر پیش بروند، حمله بسیار بزرگ‌تر خواهد بود و، در آن، آن‌ها نمی‌خواهند درگیر شوند.
🔴
من مسیحیان را در سراسر جهان نجات می‌دهم، حتی اگر ما در آن کشورهای مختلف نباشیم، با ضربه زدن به این تروریست‌ها به شدت و با خشونت. آن‌ها کلیساهای شما را می‌بندند، مردم شما را می‌کشند. این همان چیزی است که درباره آن صحبت می‌کنند. این بزرگترین تهدید برای کشور ما از زمان تأسیس آن ۲۵۰ سال پیش است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130377" target="_blank">📅 21:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130376">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
روبیو وزیر خارجهٔ آمریکا: لبنان و اسرائیل به توافق چارچوبی دست یافتند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130376" target="_blank">📅 21:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130375">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سفیر لبنان در واشنگتن: چارچوب همکاری که امروز امضا کردیم، گام نخست برای بازپس‌گیری حاکمیت لبنان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/130375" target="_blank">📅 21:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130374">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f979ed21d.mp4?token=mrphZym-B-vH5KBfoVSBdaOYGtFHpL4Ps-c3I0So0hh-buVr_RtszvyYNyEwb1IwZUqHekl3ri0A_6Io8x6y2aiCYw9GxRRKZ3pDY5muy0ILounFy_VPekUy-0SCnx_N-jW1k5NmOzZev7queOshPGMp7wwVxJ_Hj0YpE-iEpN7-Rz0bgkWPkp3XAtm3yHDuHmF5qO-LyIge75CSLBuVZBVl6cFVBll7592wn8kivvTW-lkd--MibS6fDX_T4ChLgLtuwSSnTNpWaAyF_Ex2tbzwfKOdmFGcQx95o8AvZuwC5EHFV_IuyNdKsLVLmPta5n4UU3SBQaSpSaKWMgt9Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f979ed21d.mp4?token=mrphZym-B-vH5KBfoVSBdaOYGtFHpL4Ps-c3I0So0hh-buVr_RtszvyYNyEwb1IwZUqHekl3ri0A_6Io8x6y2aiCYw9GxRRKZ3pDY5muy0ILounFy_VPekUy-0SCnx_N-jW1k5NmOzZev7queOshPGMp7wwVxJ_Hj0YpE-iEpN7-Rz0bgkWPkp3XAtm3yHDuHmF5qO-LyIge75CSLBuVZBVl6cFVBll7592wn8kivvTW-lkd--MibS6fDX_T4ChLgLtuwSSnTNpWaAyF_Ex2tbzwfKOdmFGcQx95o8AvZuwC5EHFV_IuyNdKsLVLmPta5n4UU3SBQaSpSaKWMgt9Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان ایالات متحده مایک جانسون در مورد انتخابات میانی:
🔴
اگر در انتخابات میانی شکست بخوریم، خدا نکرده، این دموکرات‌ها، همه شما، نگرانی بزرگ نیستند
🔴
آن‌ها هر کمیته‌ای از کنگره را به یک نهاد تحقیقاتی تبدیل می‌کنند و به دنبال خانواده رئیس‌جمهور، کابینه، اهداکنندگان و دوستان او خواهند رفت. نیمی از شما در این اتاق هدف قرار خواهید گرفت.
🔴
من برنامه حفاظتی را اداره می‌کنم. ما مراقب شما خواهیم بود. ما در انتخابات میانی پیروز خواهیم شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/130374" target="_blank">📅 21:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130373">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
روبیو وزیر خارجهٔ آمریکا: لبنان و اسرائیل به توافق چارچوبی دست یافتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/130373" target="_blank">📅 21:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130372">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
روزنامه تلگراف در گزارشی می‌گوید برخی منابع اطلاعاتی و کارشناسان امنیتی اسرائیلی احتمال می‌دهند حمله سایبری اخیر به چهار بانک بزرگ ایران، کار اسرائیل و گروه هکری «گنجشک درنده» باشد؛ حمله‌ای که باعث اختلال در خدمات مرتبط با کارت‌های بانکی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/130372" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130371">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dy6DuPTd6xEKkBHZopJPCyt5UFu20NZu0qJk-qBe-3qBchdfLM5MBzjSS7JZdeWyXEl1vC1ufEiBuox9Qg4XUBVXteT-8d-oVWDRg5ABkExH1I-tQAnLA3HwlMYXQSvHlG9MDwYVgY-G_SGhXE76nO8ZCz3uVqHagDu2asquHudcsZ8D0n9s4-UEBjRZ2tJoDX2n_Y58scgIEM5xDFXlUkhc2Cs3wjMAn_NPEePlgqXzBkK5TR_pp49t_RL1oBop1qEYXHYsVa4TVyc0nbRBaCRuy5mzwVkB9Z7p4u4sJu7swKc919uSgLQKqCffm46wyNnXBLvFWrgJWFGT-Dhgag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار محبی ، سخنگوی سپاه : تنگه هرمز سرزمین ایران است و هیچ ارتباطی با آمریکا ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/130371" target="_blank">📅 20:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130370">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XD--4lgfn3hVOoMjBS5oxBgzNeHJuXs_Pc0Lsq2adhSv5l_qWncflgnAEP1lXpXha0iUJYv1jy7Raf-p9QrA7yyid7343KN7Q9bCtlNqVdBIBivQaGacOjXw0yXDjOXY3DPZEDbEV5waYXwwckkhbjDyCmUhlS2rctJLAyN1fSIM5yQOoNHshZKdmqicKA-fXPSZ0XVRK5XB6i2AFshlRtSNyGip9_ZVhPC6I-Rm65j7bZjqpSZy2yXF2ojaSqyFiNYW9tq56ZXkqmcfUeHHIrvyufaVAypbJDi6V0w97csmjwnFWs8mZlA820Fi4vZVronKDBs6MDP7aGF6LuC33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از دست‌نوشته‌ای در یکی از تجمعات شبانه با حضور سنجاب انیمیشن عصر یخبندان!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/130370" target="_blank">📅 20:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130369">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ارتش اسرائیل مدعی تسلط بر تپه علی الطاهر در جنوب لبنان شد و گفت که نظامیان اسرائیلی کنترل این نقطه را به دست گرفته‌اند.
🔴
این ادعا هنوز از سوی حزب‌الله تأیید نشده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130369" target="_blank">📅 20:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130368">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نیروهای مسلح لبنان در دو منطقه «آزمایشی» که توسط نیروهای اسرائیلی تخلیه شده‌اند، طبق چارچوبی که در واشنگتن به توافق رسیده، مستقر خواهند شد و نیروهای اسرائیلی تا زمانی که حزب‌الله خلع سلاح نشود، در «منطقه امنیتی» گسترده‌تر باقی خواهند ماند، طبق گزارش کان نیوز.
🔴
طرفین همچنین به تفاهماتی در خصوص مقابله با شبکه تونل‌های حزب‌الله و افزایش توان نظامی آن، و همچنین آغاز مذاکرات آینده درباره مرز زمینی بین اسرائیل و لبنان دست یافتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130368" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130367">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
خبرنگار i24news: توافق لبنان اسرائیل حدود ساعت ۲۰:۰۰ به وقت اسرائیل در حضور وزیر امور خارجه آمریکا روبیو امضا می شود
🔴
یک منبع رسمی لبنانی به الجزیره گفت: جدول زمانی برای عقب‌نشینی از این دو منطقه مقدمه‌ای برای عقب‌نشینی کامل اسرائیل در آینده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/130367" target="_blank">📅 20:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130366">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ : نمایش هوایی چهارم ژوئیه، بر فراز واشنگتن دی.سی.، پایتخت بزرگ ما، بزرگ‌ترین نمایش در تاریخ ایالات متحده آمریکا خواهد بود.
🔴
صدها هواپیما، از انواع، اندازه‌ها و سرعت‌های مختلف، به نمایش گذاشته خواهند شد. من تقریباً ساعت ۹ شب سخنرانی خواهم کرد، پیش از آتش‌بازی که مانند نمایش هوایی، تقریباً ده برابر بزرگ‌تر از هر آتش‌بازی در تاریخ کشور ما خواهد بود.
🔴
پس اگر به هواپیماها، آتش‌بازی و رئیس‌جمهور ترامپ علاقه‌مندید، حتماً آنجا باشید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/130366" target="_blank">📅 20:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130365">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزارت بهداشت لبنان: از ۲ مارس تاکنون، بر اثر حملات اسرائیل، ۴,۲۴۳ کشته و ۱۲,۱۸۶ مجروح ثبت شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/130365" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130364">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/We9PzCegomXYRrEdP2zomVkkOkAvRnd_RVcCiYpA4fczvOEbLwWngLGYKt7Je2UT8d_t1xkHrjA9XM6f-FEmSJ7J1MrF69UYWHWKLaqA-PcW-WLEb7YVrSf6jt8h0Zf3PrI_AORNlZzUSkcBVAw4cH53AQAw56Hdff9vLTYI-3L8AsbQoeRU1Z8NUesEyVeDd3OBRTgO91LeLA_iTdR9WriMlGYsLFHusQQpO3T1YAvrrLVqJwOU3MdIk13DwsTsPfW09HSjTSCYi6_t0USFRCXlzu_qsxGYmmJ6x0FRv5IomBSpPSOAD45YoJJA6DcqVsBZpG36-H-4lhnXnwV9Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / خبرنگار آکسیوس از امضای توافق بین اسرائیل و لبنان خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/130364" target="_blank">📅 20:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130363">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXXhLpCsAhSHNV47PfBZajPfHljflGiWql9Vx31OLvNENlu6iGrNkeTjv6RsBkPDZ55jywVdpXdBnbvr5vHgUQheS33N-auCAu8n9bbUv4iQ2yTUrWsoBhFZA49RPPA4gzCizcFv23vYI0w6yBCsW0LEOzTnbvies0QWW_roBJ-5-jPUi8uRlAL8lOioFIbj960WyXRimStRzbPuxQkD3OajPW2qq3zvAIccRRxu1A-x04FLpphQ3uBp6C5opaWuHlXt03rh_1ZQ6tSqAJDLpTTdMEKUJg2_zIIgUMRcZ2S12ULy0MzsFVlC25LPyn5TUyQNvta0oJ0we-f88rNs0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی، کشورهای حاشیه خلیج فارس را تهدید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/130363" target="_blank">📅 20:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130362">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7O6e63KS5gqPixTttqRDE2bTzFmvlkzhRiWifvbA-lDHwRG-iz6Xmc0BBfrb6UKL7OcNAiOMTwlLTSoKBxWxPhkUGoS-YfNKoGh92mqHF_GQIBjJm4MlhH0zCgWKUOAxJiaYkdk3HUjBkAYpvSmVNo7BsuCTMG_9vPlOUbnNcgzMtAcAAZUYAdgzp15MiOr1MR-l3-QqaHXNpbzBEx52g0G4yWYKWfmx3Zu2JlYiPJseIM06WXGFR0jBX0ATcCv9n_8SraTA8NIu5w1aRKR5NrIhF8iZ4i4E6S_By1vA_wVUM0D6zAvIy-g1uWWH4WodjaK5X53JGn1Sk1siSkw6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال: کشورهای اروپایی متعدد در حال بحث درباره اجرای فوری مالیات خدمات دیجیتال بر شرکت‌های آمریکایی بوده‌اند. برخی از این کشورها به انجام این کار نزدیک هستند.
🔴
لطفاً اجازه دهید این بیانیه به نمایندگی از هر کشوری که چنین مالیاتی را اعمال می‌کند، نشان دهد که بلافاصله با تعرفه ۱۰۰٪ بر هر و تمام کالاهایی که به ایالات متحده آمریکا ارسال می‌شوند، مواجه خواهند شد.
🔴
این تعرفه بر توافق‌نامه‌های تجاری انجام شده با کشور، چه اجرا شده باشند، چه امضا شده باشند و چه نه، ارجحیت خواهد داشت.
🔴
علاوه بر این، اگر آنها پیش بروند، تعرفه ۱۰۰٪ بلافاصله اعمال خواهد شد. از توجه شما به این موضوع سپاسگزارم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/130362" target="_blank">📅 20:12 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
