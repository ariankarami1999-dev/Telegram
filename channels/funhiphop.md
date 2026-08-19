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
<img src="https://cdn4.telesco.pe/file/B2tvN5KzewXHsfZw98k7ZkdD-1vJqawC8j3s9XmBaWAlnwPq4N83pLd42W9pJb7A05T0mXev46VKIAh5IyDTB1DOXFqMZs3sDhoCZRvfmlfuFMulrbBly2nmO_FBUDI5gKz2IC1nzE-j8ge7phG9RffmXnomDCgpe5ZiOuRh4tXOLvEA-tVA2OOKaiAJgbYFx-F-BOfVqcYdEy3GkrQotMGDWhoN12Lex7qH9S3veuIz_xqKCRfWngVcBn6tTpnYF_kF4sKx-IKksYKOewlUH57QAkNc_B9qiQP-fdJZAcKRdGmRfoQuUqC1HnFK1iemhfE2_FZJh25E_n0aGEtGog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 22:30:02</div>
<hr>

<div class="tg-post" id="msg-82368">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
نه خارکصه خجالت نکش بیا اونم بزن
ترامپ :حمله اتمی به ایران؟ نه ما حمله اتمی انجام نمیدیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/funhiphop/82368" target="_blank">📅 21:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82367">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سینا ساعی هم زندس بچه ها</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/funhiphop/82367" target="_blank">📅 21:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82366">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304e080993.mp4?token=f9H1BqopR4TOhztx95lKrXPXC4sLZBTVQ3MRW746pttKiU9RvF1L4rnSd-98loi4Ejtx6A45oJIVsIpllzG2K8FVttxgsmDQjL83k0g0PwlxI99lBM5nwGN4SI6PZGhPrFMZYHeibuG0i8pYvGklTFt0e3T2ysHA0N_U-n5tPvnfNzp2wlLCfwFykA2K6hNIEimXtTk27HQqQnT8mbSUxPDzp8l0zlg0CsXehk0e7ZXpcXp86glmbx58QUV-D27KhLlQ5yOtncsQ-PVtShYDGYkVinDdZ3me0rb4whQl7S-iCmaUCsSeYo0GsAVtVz4RO9YhVNf0Fj4p40rzLemsaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304e080993.mp4?token=f9H1BqopR4TOhztx95lKrXPXC4sLZBTVQ3MRW746pttKiU9RvF1L4rnSd-98loi4Ejtx6A45oJIVsIpllzG2K8FVttxgsmDQjL83k0g0PwlxI99lBM5nwGN4SI6PZGhPrFMZYHeibuG0i8pYvGklTFt0e3T2ysHA0N_U-n5tPvnfNzp2wlLCfwFykA2K6hNIEimXtTk27HQqQnT8mbSUxPDzp8l0zlg0CsXehk0e7ZXpcXp86glmbx58QUV-D27KhLlQ5yOtncsQ-PVtShYDGYkVinDdZ3me0rb4whQl7S-iCmaUCsSeYo0GsAVtVz4RO9YhVNf0Fj4p40rzLemsaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران آپدیت جدید داده؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/funhiphop/82366" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82365">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هیچوقت واکنش بیش از حد ملت به یک سری چیز هارو درک نمیکنم، مثلا وینیسیوس جونیور ریش گذاشته ملت یجور رفتار میکنن انگار فیلم کون دادنش درومده، والا بخدا قیافش بهترم شده دیگه شبیه میمون نیست، چرا نمیکشید بیرون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/funhiphop/82365" target="_blank">📅 19:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82364">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پوریا آدرویت از وقتی نصیحت داداشو جدی گرفتی رو آوردی به ساخت کلیپ طنز و از رپ کشیدی بیرون همش تو اکسپلوری، همین فرمونو ادامه بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/funhiphop/82364" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82363">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLvi5XJ3LXMTx4VmxNVbJi1AM4g6mqrJtOh3Aap79B9j-DRJq_PYPSH0YiDw1s0DzaJonCZLWxuUQN44CaitoTpq-COkn-U_Gc1rNo8d45b_Fl-Lced7cK6bprlFVL_426FtfpyOqgACIBrT4BoUUm_f15vDMBo-MU3tXlBhb2x-CWtrKtY8eYu4Iax0Xlh3HzSN9P-xeOWrExCRXZXMP3Dkp_2ev_YD98c1EluB_LmMOn5dG36ooyyr59RzR6Nr-n9CjDcSJzGX9WX3FrVKhhomzKl5tThUrgk5EFffNsTFcZR14PZMRyyzsfR0gQAiVf6BzshTavIcD1zcgMaVQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناموسا خسته شدم از بس عرفان پایدار با هرکی آهنگ داد دنبال ورژن بدون عرفانش گشتم</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/82363" target="_blank">📅 18:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82362">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ناموسا خسته شدم از بس عرفان پایدار با هرکی آهنگ داد دنبال ورژن بدون عرفانش گشتم</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/funhiphop/82362" target="_blank">📅 18:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82361">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sN8npAXezRg6Y5trWEcOhaFRq477UyhWyiCnZ6qAYBakwnSsa7p6YurJ81Qwh75w-pcslhe-UlH_-hkmUFzHrJ8rcifeGTcUfAVXE1azoCZ-SlO3DWOTu_PI9gW27Y-4XjCaT6aRwehtWhzWxeQK7wE0Rqe5tj3ZTytQgVepmSsedPv4-HD21-gYxtRqHkmQ_cij7IshpC8BP7PWjZLjAjhAepFADrRf8g5g2sxknAnS_tO80vCTWozh1krqjcFERIIU-sXeoM0dxJ4GugGm2Z7VjQWoebFdbCa69gx6-0BVZTYTl1_ksQjF7ZLVvtCw0l7FpokqZdbfiH3A8iovbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات یک سری تحریم های تجاری با ایران وضع کرده و گفته تا اطلاع ثانوی با ایران تجارت نمیکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/funhiphop/82361" target="_blank">📅 18:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82360">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قالیباف:
آمریکا به دنبال خروج آبرومندانه از منطقه‌ است.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/funhiphop/82360" target="_blank">📅 18:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82359">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8fb611ffd.mp4?token=LPU0itcYMRccNNDvQG38EM7TtmSowNt-1RM_FSp_e59w-dnv6RHQCnjnyKGdv-TLKWzcKmOtQhpR_vbITEGBVfXXzQlEsGmUFTTHeHCTiLRPQ6naNpzEM3HlvA7QM3yy91VlC2VEjHqM82hBs_tSUODCu76qbZLMgn7fWS-QpfUe-1Uypvdmk1wEF4urKkUbCH3k2Cox8dgHOBOIHwR69u8y39r_NJZaPT4Zt3YhRqsWUc85JB1bZdBUEbVpDSu71qnBjDLitDqyKX7dKxS7u4mlL8_FlYqioLMlr9RrNcCuYPgi3Ln960AZqoT1tpEpQPDipriGvciMBwULuIzFCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8fb611ffd.mp4?token=LPU0itcYMRccNNDvQG38EM7TtmSowNt-1RM_FSp_e59w-dnv6RHQCnjnyKGdv-TLKWzcKmOtQhpR_vbITEGBVfXXzQlEsGmUFTTHeHCTiLRPQ6naNpzEM3HlvA7QM3yy91VlC2VEjHqM82hBs_tSUODCu76qbZLMgn7fWS-QpfUe-1Uypvdmk1wEF4urKkUbCH3k2Cox8dgHOBOIHwR69u8y39r_NJZaPT4Zt3YhRqsWUc85JB1bZdBUEbVpDSu71qnBjDLitDqyKX7dKxS7u4mlL8_FlYqioLMlr9RrNcCuYPgi3Ln960AZqoT1tpEpQPDipriGvciMBwULuIzFCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهانی شدیم رفت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/82359" target="_blank">📅 18:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82358">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZXifVNnunUY-PL9vvfEnLqZfn01YpTlF3lSVIUg227q1AVJPtac9lyXrC7MwsxQ-vBQ3F3M2DFS4CrOyGtltX6zl0-4NhHPJhUyFL15Nidhgv3p-4ae-b3C1k-We9BxDVwxqXjNLB5J99YuSsGlQCEiaxSfES7NdAot-R7Apt_tRGGwBOX8fs9Z0UUeolTpZZu2vYJHVsJk7yalaXQZNeacLDr9tq8l_uKi2lG_qFnxpOptQQ6zPXirsF9dHmEwuYw8MADuaCnuKKNVK9_i_vJL-P3tqDSVIfIQDADVReeD0OjFmzWRXQObZpBAxO-lrHpJRz60JEs2LSpXj_iIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید - مالاگا
🏆
لالیگا اسپانیا
🇪🇸
🕔
چهارشنبه ساعت ۲۲:۳۰
㼀 ورزشگاه متروپولیتانو
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
⚽️
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۷ برد سهم اتلتیکو مادرید و ۱ برد سهم مالاگا بوده و ۲ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
وقتی بدهکار هستید، بازی تعطیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g28
💻
@BetForward</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/funhiphop/82358" target="_blank">📅 18:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82357">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پلیس فتا: یه پلتفرم فروش آنلاین طلا با ۲۰۰ هزار کاربر ورشکسته شد و علتش هم خالی فروشی بود!
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/funhiphop/82357" target="_blank">📅 18:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82356">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">باختایی که دلار داده بود بودش سنگین ولی حالا برگشته با یه کامبک(دلار برگشت تو کانال ۱۹۰ت)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/82356" target="_blank">📅 16:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82355">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4162625b6d.mp4?token=pCAwSUVvrsw9GJ1tAYRyUw5G2zwwZtYgqhuqU6LstwOAqQO71LlAgksBmZWRDhXpdIvRjRfw5bpAuz-blXrY16Wcaa8SDFj3b8-jm0ujTt0WJIodTVp3b9rVApnyMqbFbYIqm2XHrE_rVL4iPtA6LQBTJo7BJAirilC_iMWEGotaM0UCF-A9aAKOcXsK60971XBB6TK1kkQBCCFZFJfFdwk1wX3TFAaW2Ry4_QBs9XfpgppggmannJ_wg8dBTWN6pAJ9ddYAz99KV8uFwWBQQyftK4Zdg6TN4Wy65z9NKVqMIySTyH7eGC9VJM-U51Bh0HwUltf-ILnTlA3cCaSG5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4162625b6d.mp4?token=pCAwSUVvrsw9GJ1tAYRyUw5G2zwwZtYgqhuqU6LstwOAqQO71LlAgksBmZWRDhXpdIvRjRfw5bpAuz-blXrY16Wcaa8SDFj3b8-jm0ujTt0WJIodTVp3b9rVApnyMqbFbYIqm2XHrE_rVL4iPtA6LQBTJo7BJAirilC_iMWEGotaM0UCF-A9aAKOcXsK60971XBB6TK1kkQBCCFZFJfFdwk1wX3TFAaW2Ry4_QBs9XfpgppggmannJ_wg8dBTWN6pAJ9ddYAz99KV8uFwWBQQyftK4Zdg6TN4Wy65z9NKVqMIySTyH7eGC9VJM-U51Bh0HwUltf-ILnTlA3cCaSG5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زید تلخون رو تو یکی از تیمارستان هایی که توش بستری بودم دیدم ولی یادم نمیاد کدومشون بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/82355" target="_blank">📅 16:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82354">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رضا پیشرو داره رو یه آموزش جنگیری جدید(موزیک) کار میکنه که معلوم نیست کی میخواد بدتش بیرون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/82354" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82353">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xf1vWLLQKjO9b3rNjgasAqpWS2a-n--tCpI3GHOPyetgneKmM_fBLVRpxmvoxdCPLiUYS6udweBgT4IrnUGn7qDy9XWAANN2yW4Q3KMRPJAzSaIPHsJs_DSsZPHFNDofXEI1mOE2JjrOXf7giclZiYI6hF1cpbCPL88ogJ4PGO04pRnnEfEDlDx74dwGU0TlxU7OIzhrkaWnBYAziPB6ciwS-FdC1xhp1UimqICRN7aA8jUgkRF3Uaej-FDM8UVuUI7kI10ltCuGxbxtIarT2ZkCiGYAM5YCfYeYjHXQ2VhJpZM51V5Qq2LhzuC2pLpD35UjpiY1_3f6QDd7zSXxIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به دلی که دریا باشه کشتی میده
❤️
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/82353" target="_blank">📅 15:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82352">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دوستان ویلسون کلی ویس داده ولی از درک منو شما خارجه، اگر معنای فلسفه رو بلدید خودتون برید چنلش گوش کنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/82352" target="_blank">📅 15:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82351">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng0ix_kQpD8a0JDePmkcBxUukkVbceo8tChjJe5PzXqpBLeqncKugW0TkUSAPrWsBmdzAQ4GFkZh6j5oPD9AI-iODHbKm3nuuWuSBNyto6EbjJ-O0gbq8ay9qeEy2lHWkJhhEw1dZZc2s3gyoUKO4ymBkPk6n-bTlzZgGcJQNOjONp9sz0kV0eAoaFyLxYEWLSX_CWnqpQVi714qI9WhwvOyNcJlOs8_hgaOKr_lbA0OHvjO3stKeCPVTdrGrQUFtDsXLNgfS0xeelkFDKTiJYgZKZWtNbSNzhUC_SJIprJErr7t1DNFnWhWvNSjL6MXANBj-DmZj2dVvMhwUNmMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری این زنه که یادم رفت کی بود و حال ندارم برگردم ببینم کی بود ولی به ۱۵۰۰ تصویر مربوطه و داره راجع به مهدیار صحبت میکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/82351" target="_blank">📅 15:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82350">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خب کصخل میتونی آلبومشون کنی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/82350" target="_blank">📅 15:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82349">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb3975ba9.mp4?token=X9V3jCBqHSOCD4pPIJT9Zkr6PUYBvcdeYDV7rOEiBrNiE60oemKySThDeedBpdXVTjbfLHg8FnZj0TdTnKs8MsRz30WZDqPZrUNLMCc0btgcsR2ewn2z6LWCGPhMwFtVHPxsTm64iFlvoFMIkcZPEugA9SvJ97h6WbPFbK6iMlOFjXTf85acBb6pzuZPUkfb22AV1c_BJMy0QoxogM9RZpr2MZhHgOAz_TYNKNEt9OggiX9yAIoYzVkX3Y3qFucBF3IChvm5EyY6AVSnGlI8uPDB8siICEygAVhOsEXetUv6p73mEi71GJ3WGQRGqLvA-YEDywruEZ5Yoj0Merh0fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb3975ba9.mp4?token=X9V3jCBqHSOCD4pPIJT9Zkr6PUYBvcdeYDV7rOEiBrNiE60oemKySThDeedBpdXVTjbfLHg8FnZj0TdTnKs8MsRz30WZDqPZrUNLMCc0btgcsR2ewn2z6LWCGPhMwFtVHPxsTm64iFlvoFMIkcZPEugA9SvJ97h6WbPFbK6iMlOFjXTf85acBb6pzuZPUkfb22AV1c_BJMy0QoxogM9RZpr2MZhHgOAz_TYNKNEt9OggiX9yAIoYzVkX3Y3qFucBF3IChvm5EyY6AVSnGlI8uPDB8siICEygAVhOsEXetUv6p73mEi71GJ3WGQRGqLvA-YEDywruEZ5Yoj0Merh0fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهانی شدیم رفت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82349" target="_blank">📅 14:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82348">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5ZCNpimtU_L2jOITZcBYbhaZ4eou1O8DZP-3arQQnoZ48gXoxbRPYTbXLalIPYiThri2AXIz21nh9EC_y-Z7KQykY6-jzzN7juyq3cVUbHazVVh9m3jYCWn9KoCZGSfR9MfW82KkIAlqUtDkRPqDaNqk_Ro-yzSf8SnqsrYpjmahxb3rC16cMr2SdsqqgiYuivdoKhGv4oFIDlV4fnkte3EsPE4F5IqwH-h3pfPcmR2XTuOWSWJMbv3vUnDaAPSq_qd4tU_LBg5RCaZLT1Vb8FwHRGxyjh4layDY2er4SwiypREbyLd6h9TrmtLXT1JDXjZvevKitc4ZpVm4HU5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82348" target="_blank">📅 14:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82346">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1960c566c.mp4?token=ezxgQwG4Nj9x52xmRpuxdFxVueJOgDBJND0FzL0-P0OC1HM_jJuZrl7_wWcZhZkreQMBRqMMfrNNiYQFI2yVJMHOnBke6knmEoVynMiz7pOBumxXOCq4A0FuCwz6va6BQmvzzpufm4dKSwnN9AtoYG2SPo8IssTIorQtEILivZVAPHiLiO1nBGNIoicBSUj6kYbwCW-uR7iofciGHwjivqLLxBXQUsCIxEWRa9LMQmj0syYpzY1ojcVY59PwDA4OoXUtjcrbJYmA1SbT1JKtxVQMecEazc0-xAXIOZxD1s9Phlnpw6mhrqtQJM4jRgshWbiOxD0qs_EJj08PsBel8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1960c566c.mp4?token=ezxgQwG4Nj9x52xmRpuxdFxVueJOgDBJND0FzL0-P0OC1HM_jJuZrl7_wWcZhZkreQMBRqMMfrNNiYQFI2yVJMHOnBke6knmEoVynMiz7pOBumxXOCq4A0FuCwz6va6BQmvzzpufm4dKSwnN9AtoYG2SPo8IssTIorQtEILivZVAPHiLiO1nBGNIoicBSUj6kYbwCW-uR7iofciGHwjivqLLxBXQUsCIxEWRa9LMQmj0syYpzY1ojcVY59PwDA4OoXUtjcrbJYmA1SbT1JKtxVQMecEazc0-xAXIOZxD1s9Phlnpw6mhrqtQJM4jRgshWbiOxD0qs_EJj08PsBel8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این حرومزاده رو هم گرفتنش.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82346" target="_blank">📅 13:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82345">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDkRXxeloK149QC69Z1_G2vguGdcBqbWRktXkoAowOoJ5dCYGMzrlVgXawH7DGr6HYYhiS0yG2Eoj6RdLyVSrHUu94f46DmWIe2yp83AI2WwtzWyJ_76dUPgWBZe0anIzYbtd8z4XHyHquKWaHNyImAnsm0ONfUI7cMuwwBEhtD499sfFX4QLdQWs6RL7CK7Xl9hyTtT8J1csldeDMwdCxc12lZQTBzBTXp_Gxh3D8sfvPn-VNVD3qPUWxyeisio2_r6v1LSCKP8HLVer48p5lSGDIzHvQsQD7Q32H39AeKeiwnE6Q4tfwnxnE4PHiKTajxpS6NSBLfA0FAzK5qEjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نادر دهنتو گاییدم نادر
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82345" target="_blank">📅 11:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82344">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a33e0eff.mp4?token=DkVUwurUL0UqV2KRWwNz-i1BmtUNEW58kqTjBnQMe_cM7J9J3dBbQyuOHpGYZQjV8fJrVEJM-_RWeQtk7WUuUgoBO3sB-sos1LUdQE9CSdv7-n7rZZgFdM8ZVV-S6Y_cUwDSykB71RYc7mQYgWIiskN3WLkl0b5TypbQpdJoMZVYSo9LHybD-Mdi8VSRGwrJ041GMAZ25Xjx1PvnSdR9QLSC-pTM24INOHoIDh2NW3OI4WcpvqS8CjcN_HeqR-LnX_380NGBlT0k1kRHD3KgZdfQIruui-QpE5YU32tHhSnIumai29BwUkeq9oJwPugawMLbztogOnkrjga7_CkFCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a33e0eff.mp4?token=DkVUwurUL0UqV2KRWwNz-i1BmtUNEW58kqTjBnQMe_cM7J9J3dBbQyuOHpGYZQjV8fJrVEJM-_RWeQtk7WUuUgoBO3sB-sos1LUdQE9CSdv7-n7rZZgFdM8ZVV-S6Y_cUwDSykB71RYc7mQYgWIiskN3WLkl0b5TypbQpdJoMZVYSo9LHybD-Mdi8VSRGwrJ041GMAZ25Xjx1PvnSdR9QLSC-pTM24INOHoIDh2NW3OI4WcpvqS8CjcN_HeqR-LnX_380NGBlT0k1kRHD3KgZdfQIruui-QpE5YU32tHhSnIumai29BwUkeq9oJwPugawMLbztogOnkrjga7_CkFCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادی ترین دنبال کننده لیگ برتر ایران :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82344" target="_blank">📅 11:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82343">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MElWxpZeopwk5kY5gxzFSMUwc3UBgv7bsNs5rxy2m2rkPWgux1acfavDgEim6B7OWmO4u1DORWkN8cgOvEUmb06bgmcdooBlwW-8xQntfSawVneHKa6g4adqgfW22oaMS0bP6WI1yrmsDpnx0Wagz8oFR0RrXNyaZtJ6OksWvwjTf5mRdjfCRoEWkz4M7sOLYOuH0qaHO5KLzGJT144wrdsaDpqvU9WQZ6xXbQg-V-MoWGtPsUCFsquMkTsslipK2uAShNZnLomJl9CPisXenEoytZFHjksgtwNHFNGkY-4VcskGItVOS6-bEHZYwDdr6YqaJudOscMCiSGU37uWwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید - مالاگا
🏆
لالیگا اسپانیا
🇪🇸
🕔
چهارشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه متروپولیتانو
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
⚽️
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۷ برد سهم اتلتیکو مادرید و ۱ برد سهم مالاگا بوده و ۲ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
وقتی بدهکار هستید، بازی تعطیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r28
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82343" target="_blank">📅 11:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82342">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400ac60101.mp4?token=L2ZTVQL4g-omod-xzGkS_09gjWehpR23oQL3P-1INSU2eVqlcFU_E6da47s-hCxNAv6OFDuXmSqFa6RTJvcL65ScWRh2e3Jfj6tWxKmGaQqkP28n_UC_Rym8WNz5kw_3g1XRswiFrOZ7LqhElFiIyNQJ9KdK24NqEcuiwIbXnDWbi3lQaF6arnwLLrm-UcyYuuV1kSUr8ou09ZL5ChHxDaucrRunjl7zUNC-uR3aTXx_-aTRZxM1dMJgNk59zLZSzWm0i_nMW9i6JwEULHmsB5ucsaQ-P6RsoYLkIC3YUTVgvC92-b-GmAEbkrY2WG1JkzVu6hZbJwu9aOZeuMSI9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400ac60101.mp4?token=L2ZTVQL4g-omod-xzGkS_09gjWehpR23oQL3P-1INSU2eVqlcFU_E6da47s-hCxNAv6OFDuXmSqFa6RTJvcL65ScWRh2e3Jfj6tWxKmGaQqkP28n_UC_Rym8WNz5kw_3g1XRswiFrOZ7LqhElFiIyNQJ9KdK24NqEcuiwIbXnDWbi3lQaF6arnwLLrm-UcyYuuV1kSUr8ou09ZL5ChHxDaucrRunjl7zUNC-uR3aTXx_-aTRZxM1dMJgNk59zLZSzWm0i_nMW9i6JwEULHmsB5ucsaQ-P6RsoYLkIC3YUTVgvC92-b-GmAEbkrY2WG1JkzVu6hZbJwu9aOZeuMSI9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باورتون میشه یه روز تو همین ایران خودمون
رئیس جمهور تو دوربین زل زد گفت:
دختر بچه ای تو خونه شون انرژی هسته رو کشف کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82342" target="_blank">📅 10:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82341">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSgBTmSbhnePjMyhnvxyAp_ITYWVBN2C0x_PdSSIjniENo_ZyLCUfYJp0lHgn8HwI16B__hAflyqKlx2WRJnmw3vsMYGdO8eiYhii1ZO-dT7o4b7ShLLPkADLMcoDDOUKHm_F0W0ULW1l0iw1RvtOveWEPQqkgr-DUzlEJvP17blxgyFVxvRwoGEA-meeudTGnOkVqFcJo54kLndnuvud2zS9kTmfmoxl55OuNk5F_9NuJ_L1MjaOen5TTZF3xOPOLhX2nx_NoAyCLtMnpwFvf5ZlAtSnQsfnbpR56oolV-v7whO26Kk5AyVutqz9jeLgQYQ_u-P54zXqoB9oek75g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دراکاریس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82341" target="_blank">📅 01:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82340">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmbOhWBc5MLrUM11k6r6v8T55iKpb9Qgl53gqHq7rZ8jia4DH55G5phef9KnrY6MQ6PwGeFr4Efz6ZdByNP2Qo90cQ-THTFVZTAzmiqtbaCUoXgVkBv-f7EtmMQShdQRaAl9XbaZA0c-YhM7mrhIr3eB0Y4H8UcOti08On81WpRMQWlug0k40Tu4VhJ-bV8dJbuB6sb5EqqAFf-SxDjDz2NzkUyLxx8od_RJEEeMhCay6Du9WAEzYB-mEfnhpifiodkJerGI-S9e3iplEREE0Jv1UgJ6DKkowLvxDASEQeC2mdRdAuxnxMA81dR1udc-rHoTAxgde3qaS2s_tpJXTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والا بخدا همه پایینیو دوس داشتن تو لباس بالایی، آبرو ریزی نکن شیر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82340" target="_blank">📅 23:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82339">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fee2d429.mp4?token=ea7FVvv1BklNp5NjXVPCis3wJXbIT3tamHhZhh3sWml2AAnpxpAGmENCsz3bN-SQZz7de1fA5k8Kr139F03z8Ihd5-GCXuMGqICx-A3FI1K-lc_ubVgTMBPW6wolz9sps9DxTI-Z4y9fu53J7VxXbKbSRA1eBYfrbtb1n1WzJLpUh71JXZq6rkxfIaEC6G1xQ6RVSsIck557gDGjW4OS2sbofPV3FYmc_B9cj4ubRyvZ1Ha8SbjZx67IhPmae3YgYvGKTfF75un7x91YkKznPbxuN0Kd56sQxyAMOcOKJqNGb0wR-sgCRn0kacgZ9_PY08r3m_00DMUyRhi23L_DSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fee2d429.mp4?token=ea7FVvv1BklNp5NjXVPCis3wJXbIT3tamHhZhh3sWml2AAnpxpAGmENCsz3bN-SQZz7de1fA5k8Kr139F03z8Ihd5-GCXuMGqICx-A3FI1K-lc_ubVgTMBPW6wolz9sps9DxTI-Z4y9fu53J7VxXbKbSRA1eBYfrbtb1n1WzJLpUh71JXZq6rkxfIaEC6G1xQ6RVSsIck557gDGjW4OS2sbofPV3FYmc_B9cj4ubRyvZ1Ha8SbjZx67IhPmae3YgYvGKTfF75un7x91YkKznPbxuN0Kd56sQxyAMOcOKJqNGb0wR-sgCRn0kacgZ9_PY08r3m_00DMUyRhi23L_DSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه کافه تو آمریکا جلوی در ورودیش تابلو "ورود سگ و مسلمون ها ممنوع" گذاشته بوده، مایک تایسونم از لج رفته داخل کافه و شروع کرده به نماز خوندن
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82339" target="_blank">📅 22:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82338">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">چرا این بلاگرا که میرن تو خیابون به ملت میگن "میای بریم کافه؟" به پست ما نمیخورن تا پدر موجودی حسابشونو در بیاریم</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82338" target="_blank">📅 22:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82337">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">این یعنی تعویق
کاخ سفید: مذاکرات با ایران تا اطلاع ثانوی لغو شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82337" target="_blank">📅 22:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82336">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سپاه 2 تا موشک ول داده تو امارات ولی گردن نمیگیره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82336" target="_blank">📅 22:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82335">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHxZXkaGheBOpSWCXoqtRWizdav-w3s5t9y4Cnygckio763bfJpLA9g9HVNtFZTiAssl--7PmFEivNxddotPuoUKB95nhudTYkP7JMMH4Vfkd5Djo9rqrIs9LaTzrAIfCV2VYk_KY0CNgrgxbwKDLO3MEcc0rwD8UErXIQLLOt4Tl6fvAbVRre_iU4PiEUo7yqKE3Yszuzem2T3tu7GKi28WaeeJFfe-_YEFvUOYRv--Ja4pHKHf356ibVm_VRwGoATbcxi8SfD8FBkueYgKmZK20RiEngKdoctFeR36u5VJ9Wl0cJ1OwLy2ug7DQ6G3dXIRXl76CvnsdRFmndVInQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ های جدید کارمزد خدمات بانکی برای سال ۱۴۰۵
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82335" target="_blank">📅 22:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82333">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6qevKOxsZHnlVtveYQQMbWcmFYkxXKN_NXMuQ5ZhBDp7jqie8CqqLmOc03CGuG-LJmiYyVHWgeCx8SEOrwYq15WpyQlKU76mnjFFcsrVf30ZXWkQUPFz6VRW6KTuI4nH9wPcfyppHPxS_oAXEgsIeg_V8Xe01bmZZWie45UdcnVnOQXLMReLs5ncXyYLecxNmNzixGbvw2ZltOhy2JWKs-qCxviM5_Xuo90WHsJ4at-L6nSM1kBDY8lkqDVgqAGMDbeSgJzr1hlSyE_hKSpxAmaoF3DoOHFbRmLs8DBJydfkdIx-348FlwQj8y4hkcL1F4dQZyrF_MnY46v4x8JzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AztH2DvH1crR3MpjQcXYp7kDtMGUFrl7OJYPAbL2q89i0_t7l53BkDshIBXtUp7xPMXIZO_YyeLXqF_WjzZclP6qjjfZwyBse6B1Ff_SszwHbzc7ynCWVVY8-ljoEj8e-oYGjW60_9bL7ZwfS5BjWqN_zWr3hB4RZGywsBrdaV2uwnCXoWnp9ezvLN3x3vofxp-0ZzBqCwFeH595JirXfyNmlxZeqH6qij5aCaSYRtRjfbDcFwcqaDla7K2cA65hKJfzJZyY1GGo20nX7-qdimW8zuKAITavlf2Y2oZaMXmxDCxQO4fpiBz3OURW6vU42860G-NF5KMWTQwFPT4yZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد از ازدواج رونالدو و جورجینا عکس های عاشقانه جورجینا با اکسش که هنوز از پیجش پاک نکرده همه جا وایرال شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82333" target="_blank">📅 21:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82332">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7u2fh_4g7N7bKLUvPNvpvhO4xzs9JS93QFSWOEaQg7ggDHJ2lrAHzYSPRz2jWxj_PaozllLPZhFSj-60ZD1nRNFDkDFf4qiHUITUVg3fxDtXQN_ycuwrTPwGzTNzT4FoYrLTVl3LqDr1-CH6mLBcZ5ut6TMAf58e8WkLZvdaMp70udI1ftZW3YktT89xyCsoGNAyIEqGOV69ifdlIdMc65UI0LwRZfrCLCtIafcJi6iM1lrhV6QQu-NrcpAAFWpoJdly18Vm_gE2dbYRCz0IJvaXfgq08HgNtp_WP8OrM0G5TA-G0psxPZX8E5RAMA4l9qZvHvnYyuQ89JBmwRWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلطان وکیل بند شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82332" target="_blank">📅 20:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82331">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fb4KMSUJwd-wQscTP9q9NLPCoZd_ql793RhH1tkoUMb239XPqxgZ8ePWF56Gb4AhmnoRM6CnaqYGhkqHnOsHy9I6tS3JuTDbmrYheTielTV_NRXjR-vhTXOkF-W6L6g7gQnaCaEDhNOKSAINpEjNPpkqBNC9reO3t6PRcmKoeBM5Qbs62pmvT836QMQyQA7RJkdVeWqnosLEs5d4o2glNIO7MwkPV1kPlGiJbAZ7ZNpfC6e3zmjCM6CjZ8kjlztUK7lemBy-Y-Nnem4Ieold5zCVjzuhBAm0hweJRQtdlE-Cn8VjS1_ogMDrv5YJItUIkA93kpfi2Vj-kMV-xuI7XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روبرتو کارلوس به طور رسمی اعلام کرد که به پیروان دین اسلام پیوسته و مسلمون شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82331" target="_blank">📅 20:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82330">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HZ6RAVBFB-HbDpmjxy3D7PfowOtIPT1HG1QT7P5UhhZ-QGZxlxbLycZjrTtEgn6Qd66_Z5xBW8Maky0P05Gq2_OGe607PUADzYYPZ10FzPdTZ52GvymJG19a4xNCDPsYAuadywRGnPS8SLILFU9gCFObw2Hr2cQozb3wPnlin-jh4U81yZRjSS-5PoDuwbkhsLk41-nOZMtV5cE2BOTjJva6-iY5gCqyy_m5zZ4aG4GWhHOw-d1nMzIGBrb9oP8s8nqraGDjI53qjLlLUq7TV6xBPvG4DiEwIyhohw5H6aV0RjpzADVDVm7YdBBJQ74to1lkVu3ZxKhYtzzG13AsVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم بازا کجان؟! همه این پاسورا فقط 250 تومن
‼️
هرپاسوری که فکرشو بکنید رو ما داریم (بیش از ۲۰۰ مدل)
👀
تکی میخرید اما به قیمت عمده پرداخت میکنید چون مستقیم از وارد کننده میخرید
🛍
•
https://t.me/+5t_pd5JM8E0yZDA0
🔗
💬
مشاوره و ثبت سفارش
@Ad_Parsi</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82330" target="_blank">📅 19:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82328">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9efb4780b5.mp4?token=NgwlpMSacmVe6txSwLQDoRBfraXPVW6HX6itx1Z2Qqi95KmoIopUinw4os-lPCE5K2wg_35bymfIwWoNal66TkLr9YqDmxYmLL19d35aCs2nQrYhVZ4YpXa14YAy9-q2kQSegVtAsysovGFA93mP3EH8zbr2aB1METi4RTAfc9G2Uwv-fL9xzMCqxbcEJeR-Mj-HHxzlcWC5n-BubVu4JOBn5QFhSpDOEBx-yXlZMdhD8O7p5bZ6L6ENysIdBgrk8pBgMpcLuaWyDheb7cJcSR1dQK-5eDc125_gheffXekoZSe57tzbMdzJobaxhZoQp8ywgXeNtwtFmsKx7rAT-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9efb4780b5.mp4?token=NgwlpMSacmVe6txSwLQDoRBfraXPVW6HX6itx1Z2Qqi95KmoIopUinw4os-lPCE5K2wg_35bymfIwWoNal66TkLr9YqDmxYmLL19d35aCs2nQrYhVZ4YpXa14YAy9-q2kQSegVtAsysovGFA93mP3EH8zbr2aB1METi4RTAfc9G2Uwv-fL9xzMCqxbcEJeR-Mj-HHxzlcWC5n-BubVu4JOBn5QFhSpDOEBx-yXlZMdhD8O7p5bZ6L6ENysIdBgrk8pBgMpcLuaWyDheb7cJcSR1dQK-5eDc125_gheffXekoZSe57tzbMdzJobaxhZoQp8ywgXeNtwtFmsKx7rAT-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا بابکو که یادتون نرفته؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82328" target="_blank">📅 19:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82327">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvnoZ9L0oc6VBxCe20qQd4rhjhETVz4YRqPcDgysr5ji4tkT0drRpGdUTQuGiu9z2Ak8yCxEqQAuJsUvw5DWu4sX5jVJakKuBiNNOZCmGnn-TtGegX-youSzjyN6-WyfsFMVy5qHwjTsjm9TW8gCRJfvg20QFgJ25pYUJN0IB084jVNFVwJt8oKMWrSVLiHBCm5Ro-xCnDfJrtWWqgjLmV4WF6HDXM63a2B3Py6Fbjtc_oO2mY_m5zPLyik_-UEOgqB3YflWdNF1OjQKGjkZIb5eskijYCYZztKupK58xitfRtIBBUwA1ys9JUXU2vJPDfIJXYcn720v5aAZdagVrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای خدا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82327" target="_blank">📅 18:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82326">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9336e75d1.mp4?token=hyc1N5HZO9MCd9V8MvgwNRiUiyh6r-y34fmR9BsHlfkIzNndS71s8Xyp293jo-Pzx4VdC8ab-mJ3xOgUiF-12f_lPSgNUIgtZxkim82UgIcrzsdIvlBKAsN8hVrrqtl3V8CLKJb9cwy4iFQBbpe2F4Qu4M0J7gcAiCi5pTOvPrwNFkthtnap8j1vbklRrlLkPaO5bsTlEDlaV2jf_bD6AEO0pQ9TwjREiohAhZPgbfTBxfCorICooi3aHXYksHSI2nb8q3zN6x0BlxvF4jM-D5JkxpbvO6c0wtqyYdDJqroGzWznBtGXsg_8yvpox_IMt9NFbgz32GypAxLebdADoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9336e75d1.mp4?token=hyc1N5HZO9MCd9V8MvgwNRiUiyh6r-y34fmR9BsHlfkIzNndS71s8Xyp293jo-Pzx4VdC8ab-mJ3xOgUiF-12f_lPSgNUIgtZxkim82UgIcrzsdIvlBKAsN8hVrrqtl3V8CLKJb9cwy4iFQBbpe2F4Qu4M0J7gcAiCi5pTOvPrwNFkthtnap8j1vbklRrlLkPaO5bsTlEDlaV2jf_bD6AEO0pQ9TwjREiohAhZPgbfTBxfCorICooi3aHXYksHSI2nb8q3zN6x0BlxvF4jM-D5JkxpbvO6c0wtqyYdDJqroGzWznBtGXsg_8yvpox_IMt9NFbgz32GypAxLebdADoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشنگ معلومه سگه پشماااااش ریخته
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82326" target="_blank">📅 17:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82324">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A0vYQZW5dj__5udcPjE-f6AftdUOXd-5mgcFbbC9PRA7QedEaa7M95zWCewJB7IUrNc74Y9o4cJtXCQKJU6KJNGNkuToIBg_vEAWi4EVBo54_bRRdpVuHPiedlBcIN6dtopanK1Iot20AeuZE8XFLrFplybG8E-tgljPAqNnPAk4t7Ep6pGA6dwBXi7tPBS_XCPAf-5KEIcE_R08rUBQhKmeetjVf8Sjxmv_UZ49pcZCJ5rfxxBZauX9CIJSKjiUlu2dp9roWkux_GJ0usbtZ88yhgj05Rlm2Q5vHUCX0Djbzxgf8tpvbLkPHqdX9N5Odk3HqCqKQI3nbwx5Z4dg6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUoJp5Cuu67LmdQSaR4fi3nWIDmnMIY1TtK0_65eI_-hfHf4dxXm861bk9yxOS9yTKGstV0LR3oys-TXxXcLfJX-gkKl9wR-ZBPySwMQNskF3KWUSeFtuyhaEk3rWw1wYuAvEQzdhkMCRbIrJwHOJPVFGHiAgulqyZ7NMd0HFm8RjOomWLeVWx6NwcBkI8bUpElJljLdtI0wGDaSl6IqTTH2tJHAzQcA3aguJytcDLB_8TSOSnSoYlp7uixp8DqssOIWBf_VFME_Ax-vesMaFHgkME3bXKCkTuV2Nz5tiRN7COj_W-EZuiS5ObccR9DACocMqiLUDzE3kB-mBuLwOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جام‌جهانی با ما چه کرد.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82324" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82323">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRRRd-7r1RjC6YOaLW-sSFdjYPqT_pPCrkelCvrMF7BaxTM-4ic0SwandOuYea2PDrH40juAY7QwKw1KzO5UrCIN_JfpsOwAK6menFOrTie1a4LNj_2B7ZBtJppc5Gh0kGnjOhthJK6kWDWKXBNsB87Q8RM3XHKf9OyZycoSiFPxMUMozP5LZvZyv2Ay1DKon-2nnCjABk0jRRhgRwP5EvCD6bD-ZQo_8UDvKnfOkU-iWQlm5dh4HOQHAJsss40kulo_ZxIHQweTRV05TOvxRCZYBKid6Uk04iDR-OxoydZyZLZ9sJeyNtKaBxJcGXMyBPAqeSM-Rf17Tkj_cKaJBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بلک‌جک زنده
🃏
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای بلک‌جک زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت‌فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BJR20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r27
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82323" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82322">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شورای شهر تهران: به زودی اسم فرودگاه «مهرآباد» تهران رو به فرودگاه «شهید خامنه‌ای» تغییر میدیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82322" target="_blank">📅 15:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82321">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">طبق تحقیقات جدید محققین، افراد باهوش هرگز ادمین فان هیپ هاپ نمیشوند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82321" target="_blank">📅 14:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82320">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fk3yQvzvXoREpLf4B6AGkVoLgkDkDQggF-1qst1OYHjjr-kiinEH2Fmo1JlCcqrv_SLTDb4eYOePesfuqG6Y4F8hqytRpAhlGxDRwDNmuO0HJBOzLnYvdcs6KYj0S9-t2aKSVsX9sm6Kgownat7X5QGqjZ83m0vyh5HnnoSpLc98l-5vWc-Q45a6NfXWN61ZXM37O4U9eufEsVjbAo-gBwvGL1D2P3wVQstQ4K6w-pahtFGgnASO9utXBhzCc84YQO03OvN7CHXf2v0VA2TQK8Nu8Wr5FRsB0M2a0z_2s8XfdN1oQoZFPQmFriqKljEKVXREXrd2d4ipag8i9xWFrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی کاپل هاست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82320" target="_blank">📅 13:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82319">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI0jY9UDUocLSOYiZZmoVLh8oKduEerwvW7xYx-okWVImCxeZc58TIhaV6ZQYEZAFr-alQnuMFNkWCTzAP0xewjlaqeHGyuYJBiODIfn2dULGCil4sJQ0oKu2PB5kd9luLyedT6EGgk3P5tG57PTNXdc1_2OSAovUY8k_O0ecty1luL92MRbO0V_pXbmAiaWoZ9e3ULuf-Ecqx0p8xarbVIr274DC6Bu3NClqMC_83k-BpqDIWjiVOpmEtV09wkvSGVW-cVmaiFs6V4jAu11JngYIOT7ooN8cANyGLyedeCNalfH8_k6gtUKF0rU3IalOwohWtfu9RDtSGq5csiihA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۸  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82319" target="_blank">📅 13:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82318">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frombRoKe( Leandro Trossard)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSgNqn76UVh41w3nVmyV-nYNyWOdLmHYQTNBDFeCAQPOPSG57onX6hARZtYyGLugLy2lTaJd29_fQNWG4ZEhCxxcZeKSNOy3iuMGIcS8VdLd27QzMQ_eaJyBpQxJS4TG_LIib9mSOAoWZKXX8vB1YomtixsSsSswYBZxdh_6evBV0C3QERkbr2UkYdWpoQbRjDNW5i5xX081fDL-0_UJI3GFvTNubqYKxYFjVi6YZguTzAjdq85ntTegHDjeWMGzvf4QSHQNPRg-fkfS_UvDWWDhfPQ1aI9i-571WtvtQZmsEdjPQdn1SKBhJbSxua9I4i6QnN2G0S5y3ijPyPD1Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت خرید کلمه (رونالدو) رو هم تایپ کنی نمیتونه بگیرتش
😂</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82318" target="_blank">📅 11:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82317">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsejCvXE7CWzFuGAbuaYnAO_oK75K2O6xkgKpYXpwHxEtRwjbZ3s4RJ8Q44XZYbqmkKUuUIvEhmMUVGDOEj_WRJYCmWb856GTkcEGekCN6rkQWHWPYdnpsSJpZamDijXSgUlBoJLo9d7dsnQax-elZjMmMCbKcVDriyohd5wOzFrzuOEnWgLzJDCE2RZGt_mm9dP-MXgaW8UJem2y1QYaLeQ1sL0KnHGzw3m-l8YNTh2d5D74mDgCunhg7ivLdNTmHdnX5rlIVrSb4KCkkIoIB4pKTpam4m2nmMdBRhLBufsHiehwZStrElAuUBksSCLus-6_3eJgm2nziMxPpleGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت خرید کلمه «مادرید» رو کامنت کنید
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82317" target="_blank">📅 11:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82316">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC58STWIwmnqMs6Q3enUq9r9wvMUR2xeL9rcAYPb0SqVkraSpiu_YHiyKBT94vwSP0MMuOhsvLuCXxOYQZpFbcVd8b5FPRezCSInC-BreyRio4UJmoM9fJ3m19o1gsViDUit2GzUBPnDKI86dyKaZRjhzmJJJsHVHSEbv0V205XyM-ZqN17cgZHJ0yKzcxMEe4fzBNwWQV48YNwGsI5UTZyTaV58ArCbY4ahHGrEezzN3Uc-vE1cOLwCRG-CYh5-95CeJDA7p1558uc0_4Gkd_EDPduCU5PoKPgXNuzdIo-xq1er2at0Kk2jfy4npptfNpObaUK2PUrcpcafSVl2Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بلک‌جک زنده
🃏
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای بلک‌جک زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت‌فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BJR20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r27
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82316" target="_blank">📅 11:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82315">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترکوندی شیر
👇
🫵
🔥
🔥
ماشاالله شیر
👏
👏
👏
👏
و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82315" target="_blank">📅 10:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82314">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حالتون چطوره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82314" target="_blank">📅 02:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82313">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ee8dd4d7.mp4?token=SgKSnkjhw12FMzHZhBe75inuTKfK7GmnUCjPUYebYR4NqMxMR6Jc-rLFmJFVftkNFtvTehfRlRk-wCsgJH43MjPvxJxQxLe-iHu-v4Iqw5-g2u9tBVk3IO-3Djd_2dOuSVfCkaeWx-Iv8tCcRcaht9YVkrbLx7w9mh_p9ThYHCz0vERxRTGQUAToP-443NQuWCMoHO7oyLZekPVC7wzooJdjB0L-jxMvWLg-bl2Q864ew4fUJOMQpIeqeqkP7VKz-_3v4E7D7V27O8D-54N99_gOkUHXE3WHA_4ndAr9-_GCRYStFWHCAXAjHwxX_rd8-R70vDayjpYC5MwZkoMbaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ee8dd4d7.mp4?token=SgKSnkjhw12FMzHZhBe75inuTKfK7GmnUCjPUYebYR4NqMxMR6Jc-rLFmJFVftkNFtvTehfRlRk-wCsgJH43MjPvxJxQxLe-iHu-v4Iqw5-g2u9tBVk3IO-3Djd_2dOuSVfCkaeWx-Iv8tCcRcaht9YVkrbLx7w9mh_p9ThYHCz0vERxRTGQUAToP-443NQuWCMoHO7oyLZekPVC7wzooJdjB0L-jxMvWLg-bl2Q864ew4fUJOMQpIeqeqkP7VKz-_3v4E7D7V27O8D-54N99_gOkUHXE3WHA_4ndAr9-_GCRYStFWHCAXAjHwxX_rd8-R70vDayjpYC5MwZkoMbaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما: ۸۱ میلیون تومن جمع شده برای کشتن ترامپ
ترامپ بفهمه براش ۴۳۳ دلار و ۴۰ سنت میخوان هزینه کنن برا کشتنش خودکشی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/82313" target="_blank">📅 00:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82312">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ1gUNKo1vuYI-o-DRX5PC6lSuutVPQoIq-7dyQtrFPj3Ru6IWyalD7Ml2wXt6mpP0DKvlA6D8fEJj4YmfQBHbz8Zge_CY0d6G6L30L1dBTTjYZg57kVjdvsLG2X0QWGwZ4FETFx3GkA3Ch2_3cnw78D42luQ8p4G2q0hnbwD1yX857ySGHOvJfmXnDQ-FdEmmYU4q--MftvdiLnYmL7J8Pqz51QivAN3CeAWnb4vjKHLpP-cEdz0GH4oIlGFkKaF5n87YhNRxhuHRKdP-kuPWDaAqm04jpVPLSeNVQjy4hllbkRjDhAQnqNXvGgxtwq9qQU5cC1hbkUluD3C-83yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم جلوش شلوارک بپوشی بی احترامی برداشت میکنه میزاره میره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82312" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82311">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رودری تو این جامعه ای که زندگی همه وابسته به فضای مجازیه هیچ پیج و اکانتی تو فضای مجازی نداره و هیچ فعالیتی نمیکنه توش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82311" target="_blank">📅 22:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82310">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWNc4akx9__SD7OKtEkLK7lnhUERiTFA8PRGuQwL8XcZkjBhaDu7z4_DN3RlADOV1dJEwdRZComFZKsFmOY6pqfYJXRk11dDNW2JDs3YoyDq3kZi71qkiyR8uUzVfnY8FyXq42WmBje790l3kzDcltRzEnmUvDlIIYGnF0qDyqY1wiioDnSlLSVZuaxgELTQW4dusQKBKiiPKKclboo8BFojyKQr4ud3wx0J66fBPI1d3B7HUjMf454yYr7QFAcblnEt6FzCMtezu0i2bCaBFA0aFKI674bXGqy2gR0IGNOD-1WzHdpWTT800Tkg5TQc74pwCcMPpUa7t978iz3IIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرانی همه جا مالباخته هست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82310" target="_blank">📅 22:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82308">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mGkRFSTckJhHcjD8rgBlCA28UiDyEGTY5o1UuuVOPERkm0XBkR-t6jW0aFoJP6P-63j7gOzVUa6aMqa89tTLQTADUJBbpnKqK4KUkhWMDH4g256Eb66Lckni_kElCDtiG6-TiEFIsB6GTPvZaLDpWF_021ppgrXe3Spqij5jcQO6fVoW5mV4rz8CjqcjdSZIrOXts5_o6w3t9zb5uC3CmQt4lSZcbMusKIWP1dwVpHW07TeDPLYpSGTzoufUyx79akqVB49_RP7JTpX37AKFMv53XAgsVZehH1r76ZIlGp1yCcQ8uG0tm9lIVmW4TiNxgFo8m_opte87cSYX1caG6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XtoyaKLBNHCLBCsnaPlFlPn38U6ZDnnCZ1qQs1-_aFPBxPnEAmpnRzZOykh70j0wIUpjOOLvPXOFw1YtyM5hYJ0AzCOuUfm3vM_O1cAyk90SJIjUmesGIv-CrDTs9ZiHnlwVou8zI2oar0u6rXyvUbEx5dXwGUHJe1GoKMR1ihC-55KLJ6-JQ0MGpI4E8ObhBTSpTHlTK3IIpQ9I94rKLErU_tMFvFVoD8-YIURM2JPwqtUvHE7glQyDAUPK5EjuvIWYii7iv8B_2EOTqFyQg5Vx1S5Qnz3V8av_VCKCzLoqjsQ8oX1ilHvBvHc05dGFmNR9wp9l2b2B-jhaRw29eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونفر تو عروسیشون خودشونو شبیه شرک و فیونا کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82308" target="_blank">📅 21:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82307">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اسرائیل مثل همیشه جنوب لبنان رو زد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82307" target="_blank">📅 20:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82306">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این چه دیس کصشریه کچی به خلسه داده  Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82306" target="_blank">📅 19:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82305">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این چه دیس کصشریه کچی به خلسه داده
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/82305" target="_blank">📅 18:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82304">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpOKMQVMt0LrgDRQCYpuyNHjuGhYgLiBSkhnWbN9ADb-GdEyd_bBiD-oMo6Joa9-EnUYIOu6GQlf2oLEkj9ewb_eWGpKSxXC5VrLCcwRvBGgk7dvZlIXSrzeYCEyiJz_cPt6sKDO5wRxRB6Zve9Ac3vSbjpMeQWBwhC5TaUMJ4CxQk7vOlAKDfwJA6viEIfv6WSand5r8e_5ZNKErpqXNDHYtdWA6FRYS5LKXDL-lLWzFjDSjJD1UYaogo2TuwD5B1IhQLChzZiMdQJEPOgSK4pfpxR3bqiWKf1kmc14gVThXrHvicuuPNZqOt6uJwoJ7hb8eYNUAyZfyT_CftnlYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لرا پرچم بالا
🔥
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/82304" target="_blank">📅 17:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82303">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U43yUw2lZrO049h75ILRynebMf-0_YTSJefbET1TTPJ6ddkzk93WiiAV0a-T8rs6emEsGqBm9_9vd_yp_0vTR3SFFPjQIIncolR3ATASIoB3B3kmdmXpF9pgReS0LFQzL8tPFlMynbVhyXO2iozrgzoZb_zVwfHss_zJOydD3a-q6oI8f9YkupcxusO3iMM1TSfnX3vFrKm360VsmN_CUs-fgJW-AzXfJEZwEc97_4PVrcofbiRu3XlnFJl4qjGj1qOFEMUl9NgrJB8H4kZBCK7x89h40nY5vkov9Xmf6m3-ADxHNJiI7Th8-IgSVpbStlii22ct7iJxj4-DHwyJaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت تجهیزات و پوتین کماندو هایی که قراره جلوی مجهزترین و قویترین ارتش دنیا رو بگیرن:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82303" target="_blank">📅 16:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82301">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/485f8430bb.mp4?token=alJAgQKMHHCOiBXqtd9GaAlK5FVI79O1MmVrh7epJph0ycdjfCgJIEG4IEFuXc2YCQ3D-F60D4nnR_Joi2_soB2RDmB3MrM5TyT2y7WKQU1Qw0cpU3Pz1LgfsrQkqhOuV6njQMZOteinHFckrzsRCB_dZiHM1icgZJK6lMCrZV-Nw0AbSWgn8MK5BN6g2ZibsVnNqw8aWYR2XB1MHjKDbB6wPFlYPBAScyBYSVG0oKJ5PkNkOhXgomB4rIJullfq0WulQLVBi7DgiwvRdDRzpGqabl2G6-o4NS7OopMT7YJywxfG6vlBE_LnUNUDtGz9kCihvgFcOsxbl6vR3jsACQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/485f8430bb.mp4?token=alJAgQKMHHCOiBXqtd9GaAlK5FVI79O1MmVrh7epJph0ycdjfCgJIEG4IEFuXc2YCQ3D-F60D4nnR_Joi2_soB2RDmB3MrM5TyT2y7WKQU1Qw0cpU3Pz1LgfsrQkqhOuV6njQMZOteinHFckrzsRCB_dZiHM1icgZJK6lMCrZV-Nw0AbSWgn8MK5BN6g2ZibsVnNqw8aWYR2XB1MHjKDbB6wPFlYPBAScyBYSVG0oKJ5PkNkOhXgomB4rIJullfq0WulQLVBi7DgiwvRdDRzpGqabl2G6-o4NS7OopMT7YJywxfG6vlBE_LnUNUDtGz9kCihvgFcOsxbl6vR3jsACQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صداوسیما یه برنامه جدید به اسم «با عرض معذرت» ساخته که توش ترامپ و اعضای کابینه دولتش رو مسخره میکنن :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82301" target="_blank">📅 16:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82300">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSr1d6IgSn_QRZ3V9AoWhy2FEocnLwtPSRTilkfFR7aj3aQ370953sBwFMxoGb0FlgrdLShsrHXIhK68J0xa2enaF7HoTz5i09Mnk3yHzMn8ew_4MbBmhNHEvSbnhSlpC0JEFyJe3CDr8yyz-ECWKNAvpjOxVxgTN5k0QrnS9uy7f1ICGDgygZirEE0YJxi4MUCeX6gIamr2d2tUvOBtqKDhpJ2NSAIN5o_syqP74bNftrUwjs7EBzJVTX9QSGHtuO0aebgXD13RdXNtLoxL7cQluN_0gvsIyot9lG2Y-fWKRt9_9eah3up9YQfueaEl0ArUqFLPWm1EdHedP-18fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بازی‌های رولت زنده
🔘
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای رولت زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت‌فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/ROUL20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r26
💻
@BetForward</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82300" target="_blank">📅 16:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82299">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شایع این پست نوید محمدزاده رو لایک کرده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82299" target="_blank">📅 15:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82298">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXCj9DdfAFa74AYGIxjNood2kvPCccnCBB8LBKh3-kWnTZcBgzPP2fTwpM8CEcNTpKK8KIMXTutJUYifJR6J3uxpOOwoBeJ2S6L6UUFsiFz8l895bOPcfg02fl7ecxkPwp-eXyZZyKVCe_j8SSG7psZAiUFWKZZ1fBBMTcATpeFsIoDGKMXQxK_5zixYHbBZ1cwPUyu0die73EvZpzs94Adi5WnksbPNVdtmPxNxakq2TmGNWY-Vch2OLXY3wlmfQt2hiLrXwfSy1T2fs5tInnttK7uGC0wPwUWfxSy7n4JkFwY4dZkVTIEb4z4iPNTiIo-8G8ihmpKsguDfOka7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82298" target="_blank">📅 15:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82297">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کار کنید حال کنید حال کنید کار کنید و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82297" target="_blank">📅 14:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82296">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDnqP2XY30H7RKzqn_Enxn87BGsXhKdmBfvGt1QCxmm0odpsZ8jLZCjXnSROtUK3MNICMihEKUS0EIovytFghx4gtsPjoEp9UDazThBYyHE_688H8dYZG-Cypt0H3R0bavPAjdBvauKnQrYUOHVmyyzlo9Z8HzjQDJct6dy91Tjcy0Ypg01bSIdAhqHzPFcr5CRK1ZMy5MxrzCKmLbXwapLrlQxkf98g9x880BUXWkz_wYlxVk4xtQG7hp9eEWDpV17M3J69qKSfIcVARD1rL5yt5bZm4diOvYQX9UjA2wp0cVmWUMy5WjUlEx0eD87JCG5cTteFTk_PkZH_IAg_ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرداری الیگودرز لرستان، کف رودخونه رو آسفالت کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82296" target="_blank">📅 13:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82295">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qd9MUBPLeUM7LOY0Ytf-2p2IzCyw3JwDPIAckMGIVwXDVrC-CHHTKW8lG8gpUnb4Xx3NIuxYe9l2udHZaHRx7J8ZRbrlgYuhWTYB2heYCMmHEp663AcPz3fnd4SNojqO5J0Ak6zvXBfzUrIsb27tLYdEwS9FK2VPpbQHYe4AaDvrN70cjE1fmBoGvHt4BwMXzx15v4zdoU1JZF8vWyCOuvcjnzSpDYC4xcVrae5gESwkp3hi26F876yuvlv6nquDFE7m0Fce5MkPmRWnF2Cd0eAT8vUuP6TeePvnF6Dgn4aCwzrhOEcQ53QBFQe8gVjxlbzYLg_PbpIqNEiIow7nCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک میلیون نفر نوید محمدزاده رو انفالو کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82295" target="_blank">📅 12:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82294">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjLUeOiFXednAV04XL2g_IEI2zmLiXpmkVxdQMEq1yYcAX6kN9P0iwfs_b5MVQdxGDCCzx1EDVrXrCi-vTW1KMcK_bsVasQbITjb7cg3bqY2LWDs_uijkJuuA9KPGVKXIR8Vq4wzxk71-dbgDGsdS-yHTZbbIZQZXMmeSc-i6PaFFiyPFR_Th0_99SCFOa8Ndc1uchlj_cV3rpZ5rYHY8RFdLEeKVhVB5DNiJkUCR5OfuuFjM6eeW_I5ZL4Djlk3hcWypbE3rb8gG7qXJ6ybPoRUf879DlSiuEaeRDuSv-hG7lHJTTDBPkt4x2j1YTVzzVwWiYh_g6pas9kkBHhAbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82294" target="_blank">📅 10:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82293">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNqyoRW9dqm-7Wp4uHjbJs-t31sH1JzEgCITzRksLxF8KRbg3c4IMy7_-vlCX10eSx5cx-jqyYH93kXGwkhLF_m0K2bjItLKvEsdtaksojmK7HuxT58XUyXBPZ0uu0dIKhWxhG-Xo3r9H_CetL-YPPlbiXlSaUt1P3N0saFoyH0iJ1zPF_naunBZmJfonJ6VAQMzl__89VjxEoWr8hvpbR18QfmUU_zXn-aFRwvBQECRQy1OuIpF644Xk4EuB7szLgYGE0M6_rIbnzbW83XMJdXdToo7N4KHXS0K8svc0bruul-wrpTplUdLTMaArPW-qc4ZpxrZ8O_vW9KpVUNgiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو رونالدو : احتمالاً این آخرین سال فوتبالی من خواهد بود و می‌خواهم میراثی فوق‌العاده از خودم به جا بگذارم.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82293" target="_blank">📅 10:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82292">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGxgF38NjdMZOplmv-BeXFoeFujIOY_QPThygshQKcZjTNVYO9DoSEEhJn2ob1QYrmMZQdmLb6_zcNoXOTd7IajF43k-KxqkMQnydNGlCOtGYZG_56xVNv6tl8G8pp0pt3zHHQIYGzkBOtrqifhYi5p74kGsKunIEW350TjN-ZlDuc2J2uD3vf6jh6PHIkjL5zB2-Ch21lqoQFvaSh7T5MaXBnHJCDn9kVP3rOcWG9037a2vz8ntHFKIWPrhPlR-PO_ZafP27-t18FjY2eN2TvR6X-0dxWqV7cTWCrINlARe91yd0bCa5T-iebU8BvAMzIL7LOnqMRvdlQJWy6bX6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بازی‌های رولت زنده
🔘
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای رولت زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت‌فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/ROUL20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r26
💻
@BetForward</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82292" target="_blank">📅 10:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82291">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/82291" target="_blank">📅 02:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82290">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/82290" target="_blank">📅 02:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82289">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoLDXVOCdR17i79aY-ObAwnGCFiWuiGvVEG7Cm8KaCKzhOwsFIGvBqyI3z-lTgS-8uhiJPkgjZOPJAi1Ja7lVv6sSpTUq4c38-v8itaCxcNpjJRb5InC2KSKSbv8VmRqERorQPVR6GuGmyPdwkqrKC6V2fNRm5yQwO2UlboQ9-Fe7qDjlVH_29WaxRVrIOsTZzTMmmErrLPkXs5UJRb84wHeDiIIyIMR49qqbYb5NKWEg6OBSv2g_OptPFy45zDccJF3ojLneGhn_UhWps0lMTH9Qg0GpLvQ1M0Sd-iJ5Afmc9CE_lcFzapGbnYciHGeaabMJz8vCHZdYmWj24KxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اثرات تمرین با فران تورس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/82289" target="_blank">📅 00:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82288">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">5 ساعت و 45 دقیقه دیگه آتش بس تموم میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/82288" target="_blank">📅 23:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82287">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHMc1UrI5X7Xog3VA_jqALTOtfX8QyVe_pxRPHM6qEdKZs_60DJ7Ubp-mp-42NNP6tCZFZZhBRfh6sw95ndDysrY9Xzx_LuAWsJFIYFBzq2N5mUcgmmb-CFd6qk7qaTvtPwMb4rsXNzGBGQwaxfvOqAm4u3LYgywUPaim-3X0DFpRPUo0kL5XBXdb1B9sSpdgXyQ6ckX7P70VKzND5bM7TQUQ226TAKb26-WyTLbvixG05NXVLTL23WQOn2CkIK6wPo-vBYNV-Q7Y9oESqxr5OhsaszuDu3mwX1k9I-oDxdM9Ys3DNpcKpdTWEBLI4v4fqL-gNKJbaniHhmjFCjE_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیمی رو معرفی کنید که توانایی مقابله با این خط هافبک رو داشته باشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/82287" target="_blank">📅 22:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82286">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzS3R2nW2e3iYegCNzfK0IBATzx44TEuRLr6-io5lzsFt-a9RMuyEBk3qRg--w7zVlinXsFSjPljuxs5wRm9SMrtUDzop1T0I7rHZy6627Ybcf3_BYvSC3DXd-Oo7-OwfoQs7xoL5roA3otfluLCL_rwq4qWbssoWY8y_kYMXMBC6pe-g-C2pbolrm39mi-e4bQvuuj2moQlf2ibpRBQm-BQgG4uWg4amKUyV6xA3pOZoZPBIDoMmVjF9Yl7qbfm1BdL17wLJNLMqh9sKSfECF1qTKeXQ3Rw-jKD6ncOXlK5DtHDsbht2TQlsSUzrZWs8JTbDFV0tsEm2Zrk2elcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیر وی گووو
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/82286" target="_blank">📅 22:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82285">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRKtU30iW_9VzJECcRk-1chz4c8iwRvQ8due5c3bO8rmYFcniHR0bcntuAePnPfG__DBlRsCPMmsEdXMXlACOfzdmR3h-P6-mejwzaMMA_d6m-AYVdXvfKVN8gS0UJvGn-bMQngVrxTf45gFEoZozigpnpt4XhYlVwz7MLc3DkeIeYYLFZUDKjlfNwDhl2jKkDvGDn1qYOMSG_G1OLScxveYOJTmKGHra1lp5bb1kf_N8BqBO9c7L6ePe-5n-qfjDzL6dyyV9Qo_duIgqQYzF44V3KuBxE9kMrj9fEN_Y_Ha0Vl-BB2ry89Q3Y_27w46pq2HeT4-jIHbutOvxlQDBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخرین تلاش های مردم برای حفط آبرو
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82285" target="_blank">📅 21:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82284">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd9bdf52c.mp4?token=iIfL6fyHumSyb5HsrnjNQdE7z4DUFvLJJGKKibVzZjeU4NVP4vxicSvEc3RyLivzj4FBaoyajVtWCpufMoHKoLaqR-EgWv3QBeoFDHPVND0Ffq_5bFczdJGQVQKL0cgB0eZAjwh4Ys3GG9XBc7i07nrxDlA-A_N5dsgMUJHYTmAEwhdHq6hYiwsf1fleb-Xyy_iO7llbv0gKL6e5odmYppZqH9pO9pflny9W57NJx9_ttoWIlbvC740LQTU9_AcVhx3WDQKWfBMGcBu50Y2VMI_C1PuEpclNVZmMPXmDxRHKV7NcFEoocttmZCNA8to3HAFi01vSXVeEGJtDRtRt-FTOW517tDkUJwe8q5VvVgO7PuTkkUkw4YpGtIZkdVsOOsEBewMjtQpjl6Sk-wh0ybFpoZSb9IbBI79f_1gEwSFjQDwOfk-mspZaMI7fFoX96P_zh2qHXTeumUkgxPbZvLjGDDoBK_FkbOgMUh8oMNO5cb4JemQkESI3qnHzSCTJ8NC91LR4KJaQHccPwnjiqleDfMFxePGz4JLLo4r1k5YRyvwMpq3ygg2sm01R2q_YZq45MQkeQ0ECDOx6HJJmMgp2ulKf23ixzsdue1ymo2fwLjxc5E0Ufp_nS2oH8xbLP327vmpZ_oQWDyIj8EeG9qJ1JvpfEEHlX09ktOGcMfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd9bdf52c.mp4?token=iIfL6fyHumSyb5HsrnjNQdE7z4DUFvLJJGKKibVzZjeU4NVP4vxicSvEc3RyLivzj4FBaoyajVtWCpufMoHKoLaqR-EgWv3QBeoFDHPVND0Ffq_5bFczdJGQVQKL0cgB0eZAjwh4Ys3GG9XBc7i07nrxDlA-A_N5dsgMUJHYTmAEwhdHq6hYiwsf1fleb-Xyy_iO7llbv0gKL6e5odmYppZqH9pO9pflny9W57NJx9_ttoWIlbvC740LQTU9_AcVhx3WDQKWfBMGcBu50Y2VMI_C1PuEpclNVZmMPXmDxRHKV7NcFEoocttmZCNA8to3HAFi01vSXVeEGJtDRtRt-FTOW517tDkUJwe8q5VvVgO7PuTkkUkw4YpGtIZkdVsOOsEBewMjtQpjl6Sk-wh0ybFpoZSb9IbBI79f_1gEwSFjQDwOfk-mspZaMI7fFoX96P_zh2qHXTeumUkgxPbZvLjGDDoBK_FkbOgMUh8oMNO5cb4JemQkESI3qnHzSCTJ8NC91LR4KJaQHccPwnjiqleDfMFxePGz4JLLo4r1k5YRyvwMpq3ygg2sm01R2q_YZq45MQkeQ0ECDOx6HJJmMgp2ulKf23ixzsdue1ymo2fwLjxc5E0Ufp_nS2oH8xbLP327vmpZ_oQWDyIj8EeG9qJ1JvpfEEHlX09ktOGcMfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها دو هفته پس از هجوم قبلی، دوباره هزاران مهاجر از مراکش سعی کردند وارد سئوتای اسپانیا شوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82284" target="_blank">📅 21:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82282">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RScCBV2-N3sSMImoppH5la8DGfgFk9Lb9Ok_PsNJGT41AVeI8cJ6verMN5-hnCBaBdFS9y6xM-BfoUCSLG8_8h_qAUNT2898lDoUdx-3SddNo3HJR_LurVVSTIZhcXrpKNj7SOA6mnMDTP5kPtXHBF2o-K8AuNolGZrEUud2R75effEg1mykUPN9pww3OHaA6FWWUqhZRDdo88rju_6PPV_K3XQK19k_uqt1-Re0PE6LdxHWNpPVA4XHbevj4GaA0i2sMIiwJUPZOu0dvXc2zxwmDSRap8eCjXUeuUxlmtLzHSF_0xXCPSQ-VMPz5oe8mPEPQ8JHf_7ZYY2bDGTJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید چرسی تو چنلش  تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82282" target="_blank">📅 18:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82281">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پست جدید چرسی تو چنلش  تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82281" target="_blank">📅 18:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82278">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tukva_bqmJsjOMzPqCzMlqXFBHCxBnLcG4PLdT85XJaoqTaHwj-_4p2xID65JGgGvGrmdIwIq3QplPgwaogQjkNtCr1oR8ub9__slFdgSCxq8JjdvP6Nj18fjoXs_hkICb7cQ8-wHqdjFjRulCXTNYNQph6Qbydh3mqZHHbTEeU-gpZxlQxpD4A7RZgtG1cTmerb00hG9Rtphj2UjvxeQ2A97wuALqSTVV7CCZfRZAlCNnU_37kp9yZnEcOB1V4WVMeoA1kgcDF39AZlX0Y9KrwfcR7z1PwgwSM3KgXTIGTdHDZtezddImVx_0YHvXjh1kvs1CXqxv4iHW2hyjecVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rImqaGjNIR1KUWP4iHh0a71P0mgGi-_jLqE8m7aawkf2RGi1ekhbF0KodWrqzsMehCYkAmjpuZdJIEptSDR2tDLysX5I95ZNq9agJ8KGERTQ1pAn4cCbINu20zXYfgPhw-P_jgj32a7ZFwzaDmTOWgLFHGxfNTUhZjF9CsPAWYQ13NGcVhIgmiY4lv9BHW5VGphwYxMke8NtE6x3Kw1PCMzCXcLsCFlb9bq44DgYohesHgjiE7OXugm_nnmYooOFaMEU9e2gjnFNqZZz0blYHJExmT7nJ4Cp21GpUfMnSZ_RiMW7Y1cvcp6xXqluBVC2dyoWdK_AsDQpQoLrBeVqJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید چرسی تو چنلش
تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82278" target="_blank">📅 18:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82277">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukXDpB1c5wTqr9sDzua5NmxfGq7gq_KOoASREHoiBN3oFPGmVpUtqHzC8g9CSu0SWHVKsJd0xkZ9GtN4LBdpHbPiTUAJkYw8UEOrH7dyrcmwRLPC55JwF2kMZADz4DaGQ3GNIt9XJH-mH9-EawiU08esrqqE8cvn5S7coOZEiU4E15QOt9gQ5Y_QC4jgTEDlpfy9QQlBwfuV8KIIhH43W257ds11uQmqgRyCZ3jEf6DtJmwzZN1z4rkFJy4lHq3JYLadZkIdJ9aBCmR1Z2YHvju8mfRn38edRw6IUvlPqipdZeFh5KOh6nDk0tSFa1OqndBkK79U4iBr_ERo6_Sn-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامیار این کارو نکن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82277" target="_blank">📅 18:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82275">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">عربستان جملات ضد اسرائیلی رو از توی کتابای درسیش حذف کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82275" target="_blank">📅 17:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82274">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWq5DXfLH_YRs6mMIcjbF88ALe9_PksnqSmLRAsrMP09_rKXg2hRqZAAlJ2WDu5C1_wq1lNgPrm2lBSQNMwhsFG6jfcFZnQhUFDEeogD7L88Oxguy_pty7Etdp4wX2x1OHs9XeOlgU8o-aRFWnwh4R_YIgQ9Qvw20N881oxxkOI0Y0VWsIrrT2KZAQb5ox09LQOosREr0KftjiiHaPkH-XwaY_M7tzSwFw8oDBdYZt1bDEm3cMGLrZXXfpDAviXbObJuZFIg52zEdJUAFh6_vDuAPKchdtby7D9PuUofe8sF07EBhVOqI6GD6SBq67BcDzSKRki4mwXarNahqMaDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82274" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82273">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C035vNPr41kTS6K7Tid51h30CMxUzJ347DM1NXaLb7dBDAs8Cax8ch6mwLzXIM6kD9oad_Hj3Fvw197UhHBOs5mCv3BuygxgMYNQep0vHzUWbGxGz0C7m0T-c4NybCgZAWDD9P3dB8DNwe7rjLzsy6URxEwl9OLDV-AuLhcaAUudEhJtLhp6GAqZediwqZFpgjSSTpzQa0Orq992WLo5hdQdS2LTiuPTcXTIYOTnARZj0nTISnTvPLSFIx7xRZL75tIqX5EU_1xLlvuRYYLEjTQSZYSrk6ZanLrK98SmVdlc5p396AMkQybptG78ZcXsHzH2_mOnkG57xCWnaLPOfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید متین فتاحی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82273" target="_blank">📅 15:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82272">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYvnStHiPnoA8Lyktymf_ROztUNFDhhW7TkJVkNpfU5YRLMzRdF5SHjZEGWiKg3-Ua1_ef2fTkRPDNxg9xY4ALdyF-CzOqdei4oxVWL_z5q-c6xuhP856DGuYDc10FzVikYRE0gbl_Ky4TCyiXNIIag61wR6UBsyuUqBM1g2uMCpytbJCq8nt0_d2cxs-qWW-kIj-mCSBFbR4mNaV0nc95v40J2JARYxITPN4UK29ePpgvn9t2WrYUgvvs9BGq9f8HL3_-MWlj5edHU-FDN2lV6VXUBNRM-a6h1R9GqduUvCX5PajG1JwblABGeALrlzKt6MwoQsRcCCqQq9OAGgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرامو از مراکشیا یاد بگیرید، اسپانیا چون عاشق اسلام بود بهش تزریق کردن که احساس کمبود نکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82272" target="_blank">📅 15:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82271">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNw9avSHmfJir4W6WYSzt6ChjERie28ifQwMXq9l2sD-nqy01M-bPohTVTcrIJfGw8k5H41tTZNahrLHJ5N9YprXlPu3_eZDYJFA7Q8cbDfwqKnRJmnzykcI29X9DC66QaiTSBg__HcNsjbapWEibidmGr-m0G5ZYpX7rB9QPqNOGurds6U7pqeqkXtPXsYx1nBG4sJtBJ5-VnC2BytiVtGOSluhdLDoRUgxhM6Z2ViODEfoXiOYMcqvXth6NpaDIclfyjHwhclC62duVrY-yWE6pTkMJEa1n-iGPokm3EDPVhkbJaDlpnX5Vdj0ghEkmQ8ltp0xOdsAT2HNi7nURg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح اطلاعات و نگرش آرتیستی که خودشو یک شخص با سوادِ سیاسی و تاریخی میدونه:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82271" target="_blank">📅 14:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82270">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فرمانده کل ارتش:
هر ایرانی بتونه یه سرباز آمریکایی رو اسیر کنه یا بکشه 30000 دلار میدیم بهش.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82270" target="_blank">📅 13:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82269">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1569dd1b49.mp4?token=JwMA542lMIp4J9eW_heXlSH3xx9X37rtl1uPFPs9alVKY0HcCIZAhi_y-7RBzqSVeyGciYIhC0_uzhvpReMLqd48VAsAltcR1ta8I4E_3Cze36NWK7uHBNhpPyWMVCcvxvey_cf9yQHiWtfJiBs2M-CylqBgNLIpl0cM0zaOx2_3ER3w7IePVxegkgvvqVPIYvIeezn8THK1IYot1rWKXhhkMtK41RRb6J4jZNK6h-qfpKIE3SnC15QEtxFrlj7a7eiWEDoIvG7OcA1K9u4Gch4rCZd0gtbX2LSE4SqKsB-Zjsv_xvRMvkA9681gpDe-EqGntah8lNHo0l6vK9UQsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1569dd1b49.mp4?token=JwMA542lMIp4J9eW_heXlSH3xx9X37rtl1uPFPs9alVKY0HcCIZAhi_y-7RBzqSVeyGciYIhC0_uzhvpReMLqd48VAsAltcR1ta8I4E_3Cze36NWK7uHBNhpPyWMVCcvxvey_cf9yQHiWtfJiBs2M-CylqBgNLIpl0cM0zaOx2_3ER3w7IePVxegkgvvqVPIYvIeezn8THK1IYot1rWKXhhkMtK41RRb6J4jZNK6h-qfpKIE3SnC15QEtxFrlj7a7eiWEDoIvG7OcA1K9u4Gch4rCZd0gtbX2LSE4SqKsB-Zjsv_xvRMvkA9681gpDe-EqGntah8lNHo0l6vK9UQsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تهی دیشب با زنش رفتن کنسرت د ویکند.
یه i love you هم تو استوریش نوشته که من متوجه نشدم با د ویکنده یا با زنشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82269" target="_blank">📅 12:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82268">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fwk2FyjHbd-AhMw1YOg2e1wU1MrjyoWDTreMAN3IwEeptNKotQI8Fk1yfKZuKtMWASUeFkDGuA1Y3VWr9vaEDo9NXQgdlHV7f4sbxiT1cK9TAHCsZ2OxSTil327AdszEiLEpcr5bLZzv6wR3tHgk1P4VreltSuBXGD6ZsTUNFDHQc4T6MT6NkR6DffhdI63q3Lw8UM5bnOdHM9to4hUCy1AspbWVIdzWzlHBVyDr-ef6OJtuCP3EHjOCRho-nCQrAlHlG1UkcMdjTJvYYVuag6siEvXGpT0MQ9_pDZNOQ06t9TTGtQCw738YJozxIWeLMkKBWe9aJ_g3-2BUjlUy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دیگه کم کم بریم سراغ ایونت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82268" target="_blank">📅 11:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82266">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3TiH3buTmNGhCkbnWw8rbyleOm_lgnxv4k4-1F0SDnLtcmpEuRlj6d2ol8MFl7O53_sg1Z6EC4vN9GICfJVR0xZU9jp1kGyt0Lc8FRxrPmrSpPR8XNjPQ-STiY9nDqrnbJYvI8v0FGtLld7TS7FT33EI1knk9agtEi4Emme3a8L5Oh5wOnvwsxAoPVtItaxqE4__2TJdXjOa9abx5wUXf_PVTMJ28iw6H0eg3-ywmmwp2AAEjlZLdTSEdmSXz4ReXiyNca7vpwRUY1XhejLTCMK72UlI3TBNSJwXlJg6ys7Q5h8ec5G0HSuOYR9JglT0AqFStWi4LnfFkUnReJy4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرام صادقی یکی از معترضان در اعتراضات 18 و 19 دی در کرج اعدام شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82266" target="_blank">📅 10:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82265">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Npk0pY2qES7c3g8m45zK55Srr2-F8PDJbgDQZ86T3huSF45J6PQ6slkvBybqNJ8T2UfHj8IAnlY9Yb45QkorLlhjgVwa4TUutowaWyhNU905t8vOSKQCevnBPv_7YVQMXE1eoPgCddzFJH7M4afeX44iB0XtxAEMP6UiY-6UGpKzoyiJ3kS0XfC9KZrKluLL6uk0Y56UuRmG7sAuHiFuOuIPOGzpo3MhdZwZ6I0sJgor3KQ63sViRpEQ5NGaRTjZoiOdfe1coFnemv1ZgABXWwzL3y2o2PeppLVFi-eEL8uKN9D44cuY9XzHWBYYWzqB9C5p_hfxmwFOJGA4eigJwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی پیشرو سیک سینابو زده و سیناب برگشته ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82265" target="_blank">📅 08:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82263">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CL-GLqidjObPWNjL-l2tMzHR1S2ujmazV2tXNCbFW7eeE1VIaoVAvreGDkv3BJ60g2OoEZJQbKx4VR94vKh_uIvsv9yylKnePyBKaWBX7FkRPPVjt3d772wgUGEAprW7zH7M6v_FpnaIcPm5Vn_KRh8affJiflofL9Fa7NW3Iv5nvVfNqYb-ysHLE11MI1rBPkmI1LeQ96ggufUI0vg7ai9osHsKVCWXgjlwvR3jpZ1ttd5otb1e8glNQcmEonGCF5jaXIJmwqgGZeCbJUUrmMEy0jjOU7WSCslr3laFuYGLeUkJXpbCc4F6rD0U5UIuqEdL5aLfq128VVBM16-hzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دیگه کم کم بریم سراغ ایونت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/82263" target="_blank">📅 03:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82262">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">توروخدا به ملتفت دیس بده یکم بخندیم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82262" target="_blank">📅 02:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82261">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نمیدونم براتون مهمه یا نه ولی دلو فردا ترک میده، اگه دوست خودتونم بود باز بکیرتون بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/82261" target="_blank">📅 00:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82260">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAcM4TCefGq-pi4w4DRmMvRoU9hoPfC4DiTiuYAcS48ET-6Phf4A6dNQFfVVko9HCg5HGojW8-ENeaHQbABVxoXo0j-1SvIYSkN3wdUhn8V_RnsZBdO9FUNpPwz921eWNcNkusfSldJ6zpDktM2ripUz7-NGE_-Q7f5QzoSQ8daEdfSqAK1KCJjr_-kRy-shy1yxh_3iBVy0tAvTBIcTOGTl4I307Pv0O1mYjRr3YnHVuHhX8D2Pbq3e0DRXYYuF7NZ-JEzufgdVtRMVUdTqSGFq0lG8UKBdia-teAcXjIVdkd9xlqHfreaVBr_CLwAgDj86ecEr9TjiB_GSyGbFOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظرم انتخاب خیلی بدی کرده و رو چیز اشتباهی نشسته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/82260" target="_blank">📅 00:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82258">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/atPR3pe0wtOml7Yi32iEI9B3oVHUPPXjuWQtjCicL1ykRzP3teKkRsURLdx1NrqtcfWGe6K75w77pIfNlrerizrA35tVbpt6_RwhHWXBtJbiZzR-TlOJ_M8hFPg-PvTW6YbME6nm_9kj6bGVMmS7gvgIFvU3ucp9XLhWxZnUlsVvXx-cCliFk7ZMF95xxj7R4mrIuNDxenpZvQkbxF58GOa1foDDdED3Id07K8h6m7qyGXoKChVKqxrmfc4nZ9m7sZD6AqJRmS2vIKounKomj50p23w3lvxcnBWWmP_TBK976HVJmKBF_Cc-qv1KnHK9Q_lg3HjD7SNag0QlwvKQxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F6rYnKVAuKvI_9WtcnNJutl6Keqnct8TojAYRnYn2-J5g_2XQSQKhmMBTqQ5VFI7YbUZx5O5sxjrS4QttfUivWEC5Oz602cJS2EJUhf9vxQ9iSlaBiFg_3gcDo0DdLSEIq2m4QOkYsjbcQXa5e8pFhnROH0-yYV0ZZj3KzmIPALjCrY4YBBXFzwyrUV-Kd0HW21UMB3oMZWF3MzZrZZVMbv6mcky8RByuoK8f9gnquzwGy3U1dYPjHVvOi4E4Mqt92M1_eGVYGxad--7dF2sN5fJR72BiJjf-vDXrbImy2xc-KM07rwYI9PsJ2mTjoDTcxqvGH8oyPKkWsCps4kpCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این اوبی میرفته دایرکت ملت میگفته عکس با کارت ملی بدید عضو گارد جاویدانتون کنم و اسلحه بدم بهتون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/82258" target="_blank">📅 00:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82257">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
احتمالا همتون داستان جدید رامین رضاییان با کیس جدیدش (گوهر فرشاد) که چت‌هاش رو پخش کرده رو شنیدین یا دیدین؛ + حالا به همین مناسبت یادی کنیم از زمانی که دوست دختر سابقش طی یه حرکت منطقی عکس و فیلم شومبولِ رامین خوشگله رو پخش کرد :)))
📥
مشاهده عکس و فیلم‌ها…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82257" target="_blank">📅 00:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82254">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ihcPqGszJAq4RXU3BDfrRnq4fY2KoQG32O5l9wlKnO1136u02dbGOhVoD15G7duSJ4WTEfP53lbX9puU4pgK2NVdyQHq0topv5jy-4U-mzcSOqplXEV1oFqPMdLuEwmISXJS61hbWLgpUq50LpPCTVZn-sSafx0Siy-TrbLWuoDcKleW4Y_AwEgfKhpKq-oNKJ2AoFqGDq8LNsnHhXRmbMdyNvzKKLPdLRoeWVOmOI7NT5eFJXNp5_1b3JqFQ6x0R4_aoy5hwfVp1tRiqqc0WXzVZ6M6PGhOE6OhQAI-eyETqk5oQnYlocVlvGtWacoJEgxxi0duBN5MZVR7U4xGOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bElrkN9932l_dzwYsD5nQPFh_fBnr-trhWOxhxiUamMpVlDzWMrqNE3URH3lG6u9nGpsom2HmMiI7rwG-7rrtICuG37h27MehHPYcTSdB6E_Un3Dl6yapYYrB49-SM03Akv7QfDrhoMiPwZZ5KQ9xvsTOeE1J-9gMheGJj4_CBLx6Y6EIHyyApAymPXc5LFshbv8aa8B-QMSrO6OCMjrsp0a-mneUZnPlMpb1dTmm3EGDI_dqYQmqq3V4qim8Ta-AoPqF49MkvTNLwJNQ3-6JqcH3D4yUVHrVWYrIlQx2pUgHjftAT66mFFB7k7WVRbTDWv3Qg9noV8YTymxXRh-2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WHKq6RUvZthxqpLziWLVkCn9xC74RWhsGBzlLmG-dJMsEowH134pC3VH_GC8M3L8ebRmxHnUUxLoqyRdxr5QmdrFcXdXPv58sNmGUmQWJ5m8Mp6kXozfp8G5yojVTSLQliEtLIkk157ORomLyOXdQ6swvXOakU68ztUFL1CQjo0RCK6zT4t0i8WcVgUn2i3LcNlK2kjLVVetBtNSREt2eiNi_iNLZzjeYy_5F8BbLJy74GGQiFxxuxFCczm7pTu5FhDUrGFaDOuYCVvFScokG2oxIaXYn1-ed6ZEw-nvHlO-mXVhK_iDcipDNJf19oVmAhc02HK_qg_MsPqJEEFmUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
احتمالا همتون داستان جدید رامین رضاییان با کیس جدیدش (گوهر فرشاد) که چت‌هاش رو پخش کرده رو شنیدین یا دیدین؛
+ حالا به همین مناسبت یادی کنیم از زمانی که دوست دختر سابقش طی یه حرکت منطقی عکس و فیلم شومبولِ رامین خوشگله رو پخش کرد :)))
📥
مشاهده عکس و فیلم‌ها
@TopTel</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/82254" target="_blank">📅 23:50 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
