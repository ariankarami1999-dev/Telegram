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
<img src="https://cdn4.telesco.pe/file/jThnqugnP8x18RGiS_zkUPZ-CIXnZyJ5E0U1Ttm48i-IQSMFu9UTNoprDPgFhFvFrJW2CuEQiun-GUIwGaGS38Bzi0MsWxFX8kPjukh8hYGWYkndBBDj261BmquOY7_OIpigXFxCDbMw1YbNlu-fGZN_yoy3Mf0zWgx-09ZTkKmRmhXVOeNPJ-CePag0DP-GSmC7E1PG5ifMJeQIbIpESvkN8wO7kS97XQ_tLiYewIJlRI6I06LbAfUendvENfNZDtpVHhnpHlW8L3m9o8mVjCX2rO8I8pCeKnn6rS8BFOu3lZaQz1AgDscaBFr1vNWncuXjpEhrbRv9H_HqGBbANw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 169K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 20:29:25</div>
<hr>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ریدم قالیباف: تهدید های ترامپ بکیرمونم نیست  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/funhiphop/78368" target="_blank">📅 20:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اویارزابال هم که به یامال  ایرانی پاس گل داد اصالتا اهل هراته و ریشه ی ایران باستان داره
هرات استان خونی خاکی ماست و به زودی به خاک مقدس ایران برمیگرده مثل اربیل و سلیمانیه و …
دو ایرانی اصیل کارو برای اسپانیایی های آریایی درآوردن
برادر برای برادر
❤️</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/funhiphop/78367" target="_blank">📅 20:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78365">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آرژانتین به عربستان باخت و قهرمان شد
ولی اسپانیا داره به عربستان تجاوز میکنه
ینی قهرمانی اسپانیا منتفی شد ؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/funhiphop/78365" target="_blank">📅 20:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78363">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مهد اسلام داره فرو میپاشه</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/funhiphop/78363" target="_blank">📅 19:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMqSQE8jleRK93j0U4lU8uvn_jz-_dj32tkfTcKsdKA9ElLKZh3-r2m0Fa-6L3KUwaY-pzdkQyYVDNoEEGvPTRi1jhQfctasv1jlA7oMzQyJhQkWTHib7AKsL25v7_UF790UNijV4Zqid_abddEkKZSb90Y2IyTCuv6whgX3iquOeaaEwFDYSj_FuCyLPCFHD8Z29hmYPmo_pAskGwuqytGSXtZWK2FH85eeqR28o248r1DuKNtUXaqC9S2DgVIluGd0-aH1zs1C4bKkz0OCB7OxfICsPttvnnazAIEFtD8NTCk4FPn5Fcn80eLc50H--ZlGwbU78kS9UW52EVyPTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم
قالیباف: تهدید های ترامپ بکیرمونم نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/funhiphop/78362" target="_blank">📅 19:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78359">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نتانیاهو: تا هرزمان که لازم باشه برای حفظ شمال اسرائیل توی منطقه(جنوب لبنان) میمونیم و همچنین اجازه نمیدم جمهوری اسلامی به سلاح هسته‌ای دست پیدا کنه.
ما از جنوب لبنان عقب نشینی نخواهیم کرد و هیچکس نمیتونه اینو تغییر بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/funhiphop/78359" target="_blank">📅 19:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
عباس بیا بگو چیکار کردی چه سوپرایزی برامون داری از مذاکرات
ترامپ به فاکس نیوز:
شاید کنترل تنگه هرمز را بدست بیاوریم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/funhiphop/78358" target="_blank">📅 19:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کونکشا دیگه زمستونم که مدرسه و دانشگاه نرفتید، دیگه دلیلتون برا تابستون فن بودن چیه ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/funhiphop/78357" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78356">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اووووو رامین رضاییان
🗣
🗣</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/funhiphop/78356" target="_blank">📅 19:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQRvw4HWYRAIsxHzr4uG8N-j-l9jY8xl4jAk-SheRhst_cw3wBBtTtcLgvXpwQSjUtIUU4Fx2Cv9XRC6v1-8YUZWvL0ozDOPQF9EQEM2iQppyLjGduTSzRj4bBLHleXoWOJj48VNpS3ODyeRj1mA69gYNLPqryzGrGctVj6E0slK5Oxb50NsdxkLvscbx90x3EMOnkzZvfaW9Uie4Hj4JwLorSOPKDkXLwd8yuwzac3t8dgGHAsoumWohz-nLav5h9DKFVe5i5AVabYFnCMlLENIpMQVAV-dYVOTBq_JrOKt10xF95Sw_jj0Xey502V1H1pEAIuboE28lNBGcoHRgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شده در بازی آمریکا و استرالیا
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/funhiphop/78355" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78354">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/funhiphop/78354" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78353">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYEflhn_cIlW8tSnrrzqr6lFsIg6gcz8TDAQBsdrfzW3RfJjMRoOxOCho63IJw2Qd25o_GH0qGse0YtD29C0ouSmExssdpkJyCP_2GAV3aqoo5YM3XhdHJ7SJFQXyK03wmshpbTr5LoF_k9_Wr4zaFcC2vqdP_7WlvMydXtFKyV-GeNtmYVcCgY63xsCqfeMDC3ABS4j9Tw_aFVACgISlK22MN0AHFB14jajC0ntN7lMdf-EwBZqDoZMT54z2uFW9cIyQPstRr8QIrx7Z4FaRYqi4ijMAqjUcUd7UoAEvgfHQSidJ0x5cpOQW7evgusoPq7003XzTafaiiKUmNEw7g.jpg" alt="photo" loading="lazy"/></div>
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
🅰
g31
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
<div class="tg-footer">👁️ 6K · <a href="https://t.me/funhiphop/78353" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تحلیل فوتبال با سامان ویلسون مثل تحلیل سیاست آمریکا با مرادویسیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/funhiphop/78352" target="_blank">📅 18:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مطمئنم که سر مهریه به توافق نمیرسن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/funhiphop/78351" target="_blank">📅 17:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ:
به مذاکره‌کنندگان ایرانی در سوئیس گفتم اگر تنگه هرمز را ببندید ما بقیه کشورتان را هم تصرف خواهیم کرد و حتی کشوری نخواهید داشت که بتوانید به آن برگردید.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/funhiphop/78350" target="_blank">📅 17:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ: جمهوری اسلامی باید فوراً جلوی نیروهای نیابتی پردرآمد خود را در لبنان بگیرد وگرنه ضربه خواهد خورد ضربه‌ای بشدت سخت و طاقت فرسا   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/funhiphop/78349" target="_blank">📅 17:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/funhiphop/78348" target="_blank">📅 17:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دیت جمهوری اسلامی و امریکا شروع شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/funhiphop/78347" target="_blank">📅 17:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ:
جمهوری اسلامی باید فوراً جلوی نیروهای نیابتی پردرآمد خود را در لبنان بگیرد وگرنه ضربه خواهد خورد ضربه‌ای بشدت سخت و طاقت فرسا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/funhiphop/78346" target="_blank">📅 17:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVlHci3M0elQACSqjHricvKIf8B9RK7A3_fhI1dcpDDaPy5tBiXim3kpnXv7MQEmc0Wr9gJO4B8sNH7GtJzLNHp9uuCbwqtqLGA-nm36oJQEJ2wTOCDNU2xiRUtjBf494ERPInc-7JFOBkGgYG1Ozn2vM_51eY3n19PXOQY2phC6RO4RrbZZlhj_N_NlUSlVg2qESilZAaS5DoSW4j7utGuLeWqJn-UgvRI-nSYjGfkePQB0Vi0SKFcAG9PWtjq8TyX7Ipr9tkHgsU_hCoV-nsyWs21qrubZQHdmi8UoETQASg5T4mSvaBDkW0gCVRJlCpdDkapRwinqN4Jx2CSveQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت صادق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/funhiphop/78345" target="_blank">📅 17:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عباس دهنت سرویس سوئیس هم بگا دادی اخرش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/funhiphop/78344" target="_blank">📅 16:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78343">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/funhiphop/78343" target="_blank">📅 16:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پزشکیان:
نگرانم مردم ناراضی به خیابان بیان و اعتراض کنن. اون وقت ابهت ما فرو می‌ریزه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78341" target="_blank">📅 15:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اگه برزیل با درخشش کونیا میتونه ۳.۰ ببره ما چرا با وجود اینهمه کونی و مادرجنده نمیتونیم کاری کنیم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78340" target="_blank">📅 15:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78339">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پزشکیان:
توافق رو گردن من نندازید، تمام فرمانده‌هان قرارگاه، سپاه، ارتش و امنیت در جلسه شورای امنیت ملی با توافق موافق بودن.
دیس به مجتبی خامنه ای؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78339" target="_blank">📅 15:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دوستان یه نکته ای بگم
مجتبی خامنه ای طبق بیانیه ای که داد گفت به اصرار پزشکیان این تفاهم نامه رو قبول کردم
نکته ای که وجود داره اینه که حکومت اگه یک درصد امیدوار بود که این مذاکرات نتیجه مثبتی براشون به همراه داره به هیچ وجه اعتبارش رو به پزشکیان نمیدادن
پس نتیجه میگیریم که این مذاکرات صرفا برای وقت خریدن هست نه توافق قطعی
ممنون از توجه شما به این موضوع
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78336" target="_blank">📅 15:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مذاکرات تو سوئیس شرو شد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78335" target="_blank">📅 15:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یه رپرایی با معروفیت کیرگوزی میکنن که سر جم ۵۰ هزار نفر نمیشناسنشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78334" target="_blank">📅 14:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نصف بازیکن های اصلی بلژیک بگا رفتن و امشب در دسترس نیستن    @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78333" target="_blank">📅 14:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ولی خب اسپانیا چون تجربه ندارن قهرمان نمیشهط آرژانتینم چون بیش از حد تجربه دارن(پیرن) نمیشه، تنها تیم معتدل انگلیسه که اونم لوزره</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78332" target="_blank">📅 14:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78331">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هلند بوی دوباره کیر شدن تو فینال توسط اسپانیا میده</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78331" target="_blank">📅 14:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ژنرال شماره دعانویستو بفرس
تروساد هم از ناحیه کتف بگا رفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78330" target="_blank">📅 13:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نصف بازیکن های اصلی بلژیک بگا رفتن و امشب در دسترس نیستن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78329" target="_blank">📅 13:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78328">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0Z4Ia0mBFbQoU4BiQIRct01srBKVsqlitBO3qVZB4hiBShUNJkymcEUIpySr8ACfyZsI0lKmyx4vR-MXYwhGqXP6cid_VFtx8lkXZs-3vQfdORlB5YvCuNMe3YkXByw7GL9L9oHZ1UELTOI3L5Qk2KSGelcMAUofxZFmaJ2QLURN7dM82_TwtCihDeBMAsXNxtu1I_P3hojfDNwofObkMSqiT7VBDzJfaY0CaW74kJN7NdCbq5hzuClcq69-1zMYZXlmD1jiTIHqaJ5-KWdOCOn_WZRTUje0S8Uf_d9znUGYWpga1C3uRsV-STRNyw4ug6PawTkKKBtvhXNupVhaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرچم یکی از پر افتخارترین تیم های آسیا در بازی دیشب
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78328" target="_blank">📅 11:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mupVnaddIFVAJ16xSw9fZG13oyg3YGLXrraekOHbCekSm8R1EvAuT05FLeW0vdwH40bOoTEnADBh2HWXAzjgsPoLCeykzdOVtCh6zqD861_GlhXjfuPA9HxT-PDGL3_0RxaNfQPUWbXyML3X64Fmr8WO3jebpvtPBGwkIJGq4rxUipTR77b995ZaI17-e0EiOJSrcnboqf9qt07qWVjfxiQvij16A4b5MNkCxi7HDbBS_XjX_3TVHGTt8IfdZmtF3Ajy-RA8xbfkSPnuYKvYNt4E52iBLkUqiMtzcsfVUZfJwQBctMPtIMx0AO_2dp6wKtQ93sblScSEcVcnZa065A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال توی یک تاکتیک پیشرفته رفته عکس بازیکنای بلژیک رو زده روی دیوار بازیکن های تیم ملی تا امشب بازیکنا تو زمین نتزسن.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78327" target="_blank">📅 11:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnfej3zAS3JRz8l4tMycOUMY-PuFh7wyTPma-WMPIoo9yQdimauzsSSiGUBENPR8bqQLJjysz6pxhfyBAr9zEt9R2TIlWc1E19nf6ZWBJliyzHjuNTY8UpRwsw8KN0j9MkA_bf3H66JuT9DZ9_eIa1d3aK-rpnaJFxAPko3RCZNyauAY4i3erDmfyuAtce137UjnK6bZ51MJOBRE3sGrz36n-RFfrt6Twjcb8M1lMjw3isnwCFp2pPlVl9z4t3MkBvaPAcI2ELVA6deeSqGXaDtGQRE_b08LWdjF1i-ZxkcC6TjnL4vgax8vNYzOl2gKCk9_P7ZuaCDLvThDhqL0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظرم رونالدو از مسی بهتره، چون ممه های زنش بزرگترن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78326" target="_blank">📅 11:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78325" target="_blank">📅 11:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78324" target="_blank">📅 11:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78323">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کارتون فوتبالیستا تازه داره رو ژاپن تاثیر میزاره</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78323" target="_blank">📅 09:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78322">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">این چرا جهانی شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78322" target="_blank">📅 09:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3uHw6cMfSd-VWE0JlOuJaoEG2fVg3ZQ5bjiZdPOA8LyZLlJF0mDhPW2s8dDXOYYj8zKMcGsRO6-CRWuf-yT4eODo9CtcElNaZQnkdjwoYlyu2Iw2ZbVoqg1YSPNoZK925-0wqNABlJmm-8C8adYO9mN8Sk2-oMFYmb6P1atgHFLBixKr1Zc9kfRtX1wlrEUCc-ms2fRd33Juuy7LQerw6SBq_c08bBrzAOWcAymDy31GHcnip-rSTTDQ9hCJeCfRB8QaLHfXWhFYLr8YLplSg7TDepyMurXS6yGhemLwoXI9uuQuuTn_cwf6V3J9pZSynpYJVG2CV5qf1MIB87UEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چرا جهانی شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78321" target="_blank">📅 08:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78320">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">عباسشون رسیدن سوییسا  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78320" target="_blank">📅 07:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78318">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APDy3J-HoebAV8H4rRn8ln_bYtBJKlOtBNpv4eI02rVaRmEpGZcYIMiS1ZBXRfq0R26cevUrA60vxMVLXI6Pj3U2sLVMrS496mAaFNsLPxq1mIgElLsODC3wXN8VwCD03OhQbhEp2DnL4SPAnbJvb7-B0qSPPaeY2TSWHN9PaLMDLt-xDkIvdddST9zVaRKSJBDnRaxwcC-QL-xxb4uZddc0pwQDeXyJNT5Z0dY0xkIp7x-10skr3x21kUFP144gRz_hFsDpc-dvPF3s8BfQf7cwoHYMjVrZL4Xze_B6M-BtB86EzeSmPUt5AXWJXZedMMM9tP1o_UppLPaX8upSEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزی نیست دوستان ارتش اسرائیل یکی از گسترده ترین تونل های حزب الله رو کشف کرده که پول من و شما ده ها سال صرف ساختنش شده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78318" target="_blank">📅 02:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXjtWIWo2utRBVbuGUx6L54VHAKivRNzPmiJlb9i67V03fYE2pycvQSMDXmaRgGjY61qKHbLxj9HAr50m1QTYE1Hk8zDlOalK0mc-b_rmDyMWrgRKXo4yNFU4mAON6w_yjGNmW_pcRn48X3er14lI0SI7_wqfkt9NCqGGOjGqjgZ9wnMTDetByeebV7JQ_gG7e2_8urkVPtbpON1_VA-3TIN2V7q1v9JTfBkn92CCH0UjvIbrgG_LDdPIOc1jpxw3z3GXX3XHEars9_hYQh9BZVFbAmefMLLheGsTqyxn0xveXAdhDt0--q3kOTA9YPrG85SBSA1H88DXjJefbBcug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Iranian power
❤️
👌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78317" target="_blank">📅 01:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78316">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حالا جدا از شوخی ترکیه خیلی به کرداشون ظلم میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78316" target="_blank">📅 01:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQ8SceIyDwgfZr2NctdTZvwEchMT28F4u9Fzlp6TRkebItcFvaa5xG-xo9QLHpj4ZTrSvEuly7VMJl6r5lqdah5TalehC-PKyYc_DAmpPd420QFFZtpwc1EL0FHFKjajpWJW4seyhX8rwdLjF5X3QwVgK102BiTPWbUDwUITbhSXepSzqNKrA2nr0-X9QNlGq_4E-2qbg_Q8StdQoV4JEAptPPsqnv7ZRVOi0ZruBntqcyqCZwQu2NDoRchh6LRPx9tt-46Zoq5ZhwN9ioUmXYCAo1c_sLvDRLN5UiUsjwhGu5d4Yof21rIinG67qEO7y2aPwglsB5S85WBH-F3j9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل برای آلمان دقیقه ۹۴ کامبک تکمیل شد  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78315" target="_blank">📅 01:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یه طهلیل بریم
آخرین بار ک آلمان به مرحله حذفی صعود کرده بود قهرمان شد
پس این سری هم قهرمان میشن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78314" target="_blank">📅 01:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گل برای آلمان دقیقه ۹۴
کامبک تکمیل شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78313" target="_blank">📅 01:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78312">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWq2DJ2mwpPlxg7EiYu0ou1Y7TqOOgtz_UfKmzbyRWRMqx10z-71mUHQRmY4-0lWJhkmL-vhIp13OZsAj_1yxs45C0dQf3cONz6jMbtap0UMKTCPLAwmnd-C9Jp9aQKUm5D217RIDNrLAKhysS2wvckztVy3UNRPyi5gnwP7l55Lf9MRVKaWEvPUhg-UGxRn1gTWM1HS-uU7c_ks1nBDBoiEgc_jPmob69pqmD-3_4i0WycTLCyPnpEXCPunfLn5QR70myxFVKuXf4dttPVQuP1w1teAHDC8_YMatjuujXjUTp11GpXQPj5ceBw2ajqmdbXoStPndB1lATCxytK-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمرینات قلعه نویی قبل بازی با بلژیک؛ رسانه های بلژیکی میگن لوکاکو هم از لیست بازی فردا خط خورد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78312" target="_blank">📅 01:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78311">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آلمان تیم خوبیه ولی مثل تیمی ک اومده جام ببره بازی نمیکنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78311" target="_blank">📅 01:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78310">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آلمان اگه این بازی رو برینه عطشش برای ادامه تورنمت خیلی بیشتر میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78310" target="_blank">📅 01:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78309">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فوتموب باعث میشه گل زدن تیما برام اسپویل شه، لذتشونو گرفته لعنتی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78309" target="_blank">📅 01:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78308">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78308" target="_blank">📅 00:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78307">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">عباسشون رسیدن سوییسا
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78307" target="_blank">📅 00:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78306">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کیر نخست وزیر بریتانیا استعفا داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78306" target="_blank">📅 00:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78305">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دوکو به دلیل عفونت تنفسی، رسما بازی مقابل ایران رو از دست داد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78305" target="_blank">📅 00:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78304">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">المان خورد</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78304" target="_blank">📅 23:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78303">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هلند تو این تورنمت همه رو سوپرایز میکنه
یا با قهرمانی یا با حذف مدعی های اصلی
این پیام بماند به یادگار
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78303" target="_blank">📅 22:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78302">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گل پنجم برای هلند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78302" target="_blank">📅 22:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78301">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سوئد یکی از گل هارو جبران کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78301" target="_blank">📅 21:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78300">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حساب کنید ژاپن چقد سوپره که ازین هلند مساوی گرفت
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78300" target="_blank">📅 21:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78299">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الله اکبر گل چهارم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78299" target="_blank">📅 21:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78298">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گل سوم برای هلند
سوئد پاره شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78298" target="_blank">📅 21:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78297">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گلر هلند عالی بوده
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78297" target="_blank">📅 21:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78296">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سوئد زد ولی رد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78296" target="_blank">📅 21:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78295">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اسرائیل آتش بس لبنانو که پذیرفت الان شروع کرده غزه رو میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78295" target="_blank">📅 20:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78294">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">هلند گل دوم هم میزنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78294" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78293">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هلند گل اول رو زد به سوئد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78293" target="_blank">📅 20:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78292">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujpl2eDAFM3J-trMEUOj59gD-uPCB2S2EobjVejllAjrNamsXzOHmVCN-RXjYyD4EyQzpvnAuclTB17AqHUH7_Xtk8ot3m9c50G1VG-fipFlKVY_rInXc4QG3Li_Z6uxnwZY44v1oyVsFWmgVz7YhKe9Y4g799l3_SD2aZ-t41cNzEHgNE-frxfoC8essu-A7-FKejCrYuLmJUDxwDnFFzRAgPIafYVWn7oOqtufdwyYFcRgnXLeYBElp2ERz8EywyfykOFaDWMEcV0uwc64_AlBtDyVlg8KeEGrY50FrSdBypIPFiVyN0crz_Zg4Odte8OZ5iZ6lBnYotGWvhh_hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه هم با باخت امروز صبح از جام جهانی حذف شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78292" target="_blank">📅 20:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78290">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1nRz8m-SMHfL1HPh7uKtMh-Wm69I30Ox7MZidEu9v6fX3kz_m-JCs7dMfQt-VcMtmpN6rj6Mb30IlHz-sORtWNk2eJI04v4GrYyGFlQFhxOI06nfoAvXTFbA3WfPK2D0l5YHxf2fy1FA-ni5sXI_2UejbMWUTSBBgrVbSapdx3oY1rxijrvS0NlRgt7UtJ8qkLYloLMSls_83vnSydQ30Q2DMbFOu8Z6lfzkv6kqMmhPsa0cqw_DTHYBvSFkqnP_Gy-G58lbPqABrjEUSSWKYW0x3SXPPF6cvhTp8-jEeSkPwFsLuelubIlw6UV9Cz-_wBpR77DUCtofzgmECs2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vt0l_3bnrCSo4vfeq62xi8Xmq3a_xORg7L2BIdlYFrMfF1pOV5yxp3RHUA4xU22JdtE9bHq0H-LKJRyA_oCA_FAvcJ7jzFY69SGFHfx8o3GkJPWabJnzlXeXTkNEyugiai-d9EpAyT7Tmu8ZGqCJ_Fi5lsFtX8wqUBueLUf9Wjc7-z3CgbBzrmKVCdgAXC3dU2ebWUVK0A-Q5JPGFDr4En1jIIusGOad0u_StS3EXXZlERS7yo49Iryy2-tm59tr_dHm9d8phRoFjH8jqhX9l4kYUgRu5CKGwqB6BPjZx790rTHL12gJn-PLxeNZijb5igu0LCfON1YRNXG9yERuyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب دو تیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78290" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akaX5J4jOS6VRLt2rlWKs_vA3Lt2UNGSk-LOZ447Rw3X0xCtO7Bo2or5Fp8FTiIxzoD0GY8wznzy3omD6VdfR3wSRu5bjx7uFqxiptn27o80wtnhwS8nqawvxl5FZ7WIRKN_5CkS-IU-JVLpXkvzB8AX8TQd5jHFJxqVjGT09Kw5DNOaLN4IeushXJja83azD4v_WIpCQ1riotTmW6vQBaCbgIvE3A3LD3_KQ8-IYnkM0s0kxBj0jHKeWHNTwFvm8HEurdNoQ55XpRyaRZO17VW1DkP3xCoPo7l9xqy4W7Oa0Z-ctnEmm34PTYxM1IAoMPHbXdcBeKL-H_K4z4tniQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78289" target="_blank">📅 18:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78288">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMzl1zDknaVq1S_hhUEUdIzg9o8JJb_jEcMxz147w4IOZ5SjP4R5A0hU9PdKJoj-e-rOhH0DnfGWIgnY3tKY1-Kx0ct84HL7IDROnSbbHoCCelaDJ-ZBRo-zR3HjplK0J_Cu2bzSCRWxu1ng7u_q4ynfJyu9eI6wEXZv4TSJcVvJBkESDYi2BGA9_KxbwlPoLB6xH1tr-n_zB2tA_BqLl4zWx5xgd4_xzkS1M6VMDdvmzt5cNvHisDjjt38UNYaM4wjRfy-iX0-nz6zRwW9G86gCjd-UZIG-hkliMOckDBB6zXTjYy1KacgS_k_lK1-kS1Zof59X0b9GRUQcZ0YdBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداشاهده بمب خنده، فرانکی دیونگ و تیمبر تو تمرینات هلند شاخ به شاخ خوردن بهم و الان تیمبر مشکوک به ضربه مغزیه و دیونگ هم احتمالا بازی بعدی غایب باشه.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78288" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78287">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJ1FC0jf5IWHPEGpPKJq5btplkwwdFMUeFqCyhTE8aKcHNOmdeDEDp5uM5SFEeJSAiJhcVMohao2o9ReyRlOuZjBEa6V2I7UWdn_AbTL2lL-N0xA1FDNqmNpONx_zyMz1CSt-DsDOWzzVRizui77UtFq6ukfJipOMdD5bHu_sA7y7zn9OHcnnp4Tdiuvs_ECFbhl7l78TnqjWCIIsWuDojE1jZe1XyRkjx55BOJN6RJfXhxxT0Jz-eM3iasZ0Q1KJdejLkMR61CWjzer5g7oIfLSYGMnRbcKERUbIHhgldyKbxb9CIKlJn8S_dR_FqrKZdDwmu4S2OJV61ap7lT-4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78286" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RON6ElFugwJhycYVlU3FmK_FUWBGESgp0jK2JS2JAQbSYL_wPAOjHKpB7Nj-LnbdW8S4HKAYGLprUgiuqO1j9YlAmXmGlnZHVH2ERaUq1TsmdJ5IaLbR6WCXq699YVu1xw6B-1mkK1HqYCEqHD69qYkoUaOoup7Q0Av2zVgkXAtF5tfYYNOQY5_gwcYgvJGryYmRD843cPsRy9msAUuu_5a6GvDKjN8-Yl7vtIoOgq1gL6eJXviVQ-7hIaXSiTYvWf1lxlw4J2AhkdpbpKOkj2-5RrkKWdLQxECSbwRe0gXMQj6MCr8OinOmKgAehBvzyRVRx7n2VCNKsIjgAgMFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه نتونن تیم ژنرال رو متوقف کنن حریف احتمالی تو دور بعدی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78285" target="_blank">📅 17:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUIRqOy1h0DFbRq_9IvwZJM_gaNE_rhGqndeqHM1anZGyHyT0BkdVHa771MMx8qYlwAvJ3I-nEBQzixvzs9iLL6I3UTqmz5q5kRsGsHM3DUKGE2BZPQJhGNFFTN--XDyJuH-VRnV-0amu3XXoUHy8Ead0un1FZfFLKm9RYpdzcdOqZvbjENkrsZ9-zbTK-SfG4E7IArWLo7AmiH2OzBbnpZUT6Qt8_LbCi8BWaomsALCJxUg_jrQrieBSqsFm_kW_2Pq53rxLT7Lf8G6gszi9eelsa0JYA_zcy_MTEzYmovtEKXguZM0n8xysn31qJh7er74AWNB9oTNNzkvKMU7uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فعلی تیم های سوم جام جهانی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78284" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78283">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مکزیک به عنوان اولین تیم به دور ۱/۱۶ صعود کرد.   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78283" target="_blank">📅 17:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78282">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTP6QIC2K_yaLPvjJOwjt_RGBcB_sGD2joolJwrLGg6pUB1O8uLZWu9O05eJ99aFLfTbIkpOzSwOpOzsRvNaFdfcENpY48xMfj0wtnrUyVJr6TlWembmx9-BdA_nhBSRIQKWm3260GPTOyFpe7KG9xlKXj6Ov5I2710EeyhVVOlZd4ZA3PdpG1gLHTMAvGqc6lhku50PupkkMK3hLKSGI4qpfkpCoqdOSJpLaqDVcCFJihdI1hSNq6Ck_CgtrNfvfqkgLQsXSn50eI6g58bouhd7ENsMrgV1Bm5jtMksBuuMiX1DkHKpu_Hrd-qaxWMJ_DVrnzvs57yV5O0gT_90vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم بالاخره افتخار همبازی شدن با بهترین بازیکن تاریخ نصیبش شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78282" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78281">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سخنگوی وزارت کشور: کسایی که به مراسم تشییع پیکر خامنه‌ای بیان، به صورت رایگان تحت پوشش بیمه قرار میگیرن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78281" target="_blank">📅 16:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78280">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سپاه حوصلش سر رفت باز تنگه هرمزو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78280" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78279">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سپاه حوصلش سر رفت باز تنگه هرمزو بست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78279" target="_blank">📅 16:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78278">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دولت عراق مجوز استفاده از استارلینک و صادر کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78278" target="_blank">📅 15:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78277">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E00T2reWpi9Sx6wrSxBZ7E3L_WNnFNwJIORdK024CO3YD1eVN7ZSS4Y1AoW2oyCQ5mvCOqIzik7SsimZf0RmK4LYGHzxY0uujBuZW9_Awrn1LNFS8Xlc3Eb7TwH8WVoBl_lCJwSZc9O9XhBbGHFbJEpY_jhTO1JrxIFQd0vrHY_NkmVlsYAQdw4THnNyVaaleaOJFecANAfuVmcy77mvvcUeKuAU3kMunMM7l8e-TeeU7ejl1SkqWxBlOwHVuT8LhlWsQ8fDuZUO0JEU3PXk8oYpCue9V_jhr3m9MsZmxmWGxjFGE7hBkG2LqyeYEjcly2Z7t5fexvYejLAVUlT1Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدینیو و طرفدار گمنامش
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78277" target="_blank">📅 14:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78276">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbeOri3I2nIeSvZhUL4x7DioGCP1iyX7kLLAi2p6OGkqhDcXUVVWgDctkgI4XXHFJ9igUQNZ7KObqv7IBDqgU7lgNfY1QFq0NXuDW3Y6IRgfaZgGmraF5VrcpjrDXmPQQ-Icy3RXWD3I7U-xboiCZO-5xagW0n1RsS-OXwzdrj1efXLIIHshjWfX4XjvFuMyd2ur38W5HG4LbFFQFR-AlpHXiAaBSilwJAiWoQzvwsoPu_3yeGiAh-texoz6ZZmwsto5SRUF0b1EP7EcRWKE2c8RZIc4XSaT2qcHIe4637dpaynXQIRzQeqIDec5SfKr2fJQHf9J1HXQwQVNVt4XNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باهوشا جواب بدید
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78276" target="_blank">📅 14:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تو جنوب لبنان داره نسل کشی و زمین سوخته سازی انجام میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78275" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78274">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2W_gIm-5cbLVUQsfXJ2XGjOj_CHGbNFQZSR1D5YmQqfn67V9tXzZ_fiqeJpsiwC-vJ__LtRjBre2zJqblx2YMu35_AUes0jSWIOfngkW3dmXax2zUi-Y8Yj5OPfcjkVFLj_cEypWgxBo2OF4IZYB4ilRMSdtz4MB5dhF-GQw9xENkcXyfY3Zn-4aABfFaMkXss2GcFh3rqThL4A13cs6hvoABE0Kkbd9l1B81eUeIzV_e7j01-1q14aPwYv0OjuDLCQw38Yy9Gmw7kLsFTVrhWNEeg4QAYYYBm6hoUJBwWIpNC5vhxdfWc16avwYfcOhlvthj_U8hYpD5ygNTpmEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخواید اعتراض هم بکنید لااقل یه متنی بنویسید که با عقل جور در بیاد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78274" target="_blank">📅 12:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78273">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iwo9A0ImGK4lAXWW5fo7eixyjufPZ4JYVRfJWKMdc4NJD5BL4k9mjWGfACcsky5iLJSptQVrFC1Gj-e8Zz3MAfFwhWD8TH49uM-K651MhTCK7LBX2oPuTTlZ8YlCRJwRz5S0y6oXIiUk0Te3pMm3lj5xmEvN3rFQRcbxzl8W3DwzI1-iTpe9ozXV_iR1SOG9lCxTwarXbFzjVPFzBJIigti533mBCzHionPLRLRI5zq10Wm4u86sccOs81Y7D0BNPb_vISzynzf-lyIz1iqG8HBfAs67z26eyMRVyY09TTBhv7apyElURx1ogU0g9KIaENZmpLp0_ld0m5vQtPYryA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تیک‌تاکی ها هم کم کم دارن آدم میشن
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78273" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78272">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HURGSOxB6vgZprowAhxpSkXhV5kEfIt4THTc1OnjbtwnKR4e90GpjgymSyTvZCLZp55BkicC4q23dzL-7kCs3VIdq7nd-jdEWscOZhIS8p7OU8IuVkt3ZGYTAxpHuEY8RNcfwX7VjfqqMtTtYeryts_YB8hH_fJ54LZPtzz6mMEzEbDA_1u2EkpKU_P3g7czs0IN-zqnbYLgvHymsJ1qgDzNMjly5U8HX08eE2r119RLHqe6llYQWbRlM9jmG_PbTMngLK3UIeeLCjXlofORJ9aIoQ1hg9Pq1ysnD8Wz3XUqVhorRgiXQo-XpMFwT4BroNR15kGK97FdgJb2i_5P7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78271" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78269">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نمیدونم چرا بازیکنا برزیل نزدیک ۳۰ که میشن با هر بدنی تبدیل به شیشه میشن، من دوسال پیش اون بدن رافینیا رو میدیدم میگفتم این اصلا مصدوم نمیشه، حالا ماهی یبار مصدومه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78269" target="_blank">📅 11:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الان وضعیت جوری شده فنای مسی دارن از پرتغال تعریف میکنن فنای رونالدو از آرژانتین
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78268" target="_blank">📅 00:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78267" target="_blank">📅 23:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گل دوم برای آمریکا
پوچتینو تیم خوبی ساخته
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78266" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ دوباره مصاحبه کسشر کرده که به خاطر اعصاب ممبر های عزیز ترجیح میدم پوشش ندم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78265" target="_blank">📅 23:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78264">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کشور جنایتکار آمریکا گل اول رو زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78264" target="_blank">📅 22:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78263">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بازی استرالیا و رقیبش هم داره شروع میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78263" target="_blank">📅 22:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78262">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkBadIpcBxou92zVg5wpsBMmOi2XlyqlkJEqMHC6hAI18oX16gkGUHpX7ScOUvXtqHcoRwpr3hO2rAIRvNEzGGqh-v2UG4CLudb2oMAe8TFqee4iP_mKIp6nQkoxpCS5DLOl8oHiKHo1Kz5eL33GrRovUrtJ8JgI75yj8COaox7HpBTDP3shJQ0nP-qIi3Tm_AJhLXYcYv0VQYupa7WmyJNM-1b-W5xFjm1Nepaiu7P-pBLOQ-Czywikpsj24uQtwb_qdDZlsPq9pIpkWDQOhq5OMsyclpx_4k-eUQRKZt-VwZ5S23qY4EfF9Qw6ZlLghkG5Iu3EDue1hpr0augs3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین رونالدوی موجود در جام جهانی 2026
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78262" target="_blank">📅 20:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78261">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVmBTL0EGnkk86EBbOpGLqKQQ5L_84Lgt3PU1EkCQN6-99tu7UzwDmdmLdxebxye-WeHhxWrUwEOyAYdZLaZWsBQjG6TlaidhNULQIdiKPby20xxk3DQ3z2bCnXFa9r2rGJUOPGsJkR5F-ajCymwWKWyLKvogtnKRyj-hYazToDYGQGy8Ht4BwYw2PIwp6q-y-ciZSEERj_9y9oZbn9Iuuju_Wij3nMvBv1UeP0PyzQIsO2UWN9Vlz0D6p50YRoZZZurDXJahK4ClUXt6gUHVrjfYLn2GXhra30qTYIFU-_p6_ve3W59msaS4tSjNFGp84zBmO_q_wbxVX-fME_g3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید کون میداد تا بهش 10 بدید؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78261" target="_blank">📅 20:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78260">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فنای رونالدو به پیج کل بازیکنا تیم ملی پرتغال حمله کردن دارن فحش میدن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78260" target="_blank">📅 20:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FV8Djm1MOC-8innz8o7S7ogonnK9QwEa3uwfXuu9QM6ai1DSdulBODTxT3VUyF8ktj38D3e8_T2grByfEVOn2IE8I5j4s1ryvCU7PXT7tpdwyGcZgraCxqHu043WIRYWbN3VXzmvka9HvUp6nQVlnj_R8Vrq8-4SOHfIP6Az6c0vB2I5utQUhRjdamwY3b1z-wiLH12rIA0qgdYLzl2j6dH-1EGHGff-DqrhNQiADi2QGu4OHuY3k3AnhKE0opIT1YB9nc6-FTCZR50H7GEHxvKfLpfXTwJBwRRdKe0ZhJfcpE_qJqHMeNdIt_n1ufSwVmOYAnWpQPYy25Icz6b2nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید شایع به نام بلاتکلیفی منتشر شد.
Download
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78259" target="_blank">📅 19:09 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
