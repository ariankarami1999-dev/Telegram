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
<img src="https://cdn4.telesco.pe/file/qCtE_djD406A_iUK6n4gRggQMhSAUURbq6iunp7-lnFcDClZT5qAYumE6mczQSmpAUheSdJUXcWvmYBikynut9El-uOMrcxL04Fu66Wwon-Y9GBIgGaP9mkQ0VuDpG0kYKgtWTwBgXiyFQHexqYa5mJ0-zT8AeUIMvBNYYmX_GOJoDwarcavHfYUcIYgUcjs5qa3fmS50VZ5R2uKNoguMWsO-Asol5zb4SLBaseXddGTXJBiZD8iPq0He-MnY6l2iq7M4M1uwgNDtnvuwdirJ10HHWS-iMSlPofIA7ll_UfU7FkkN3x6kFThOl6VTxir3qUo-Jo9Z24pBDpXZsPwVQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 252K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 19:40:29</div>
<hr>

<div class="tg-post" id="msg-84238">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FK2Ty8Qu5DdU92bA26_Qp8Cs8oSArXcwBjuvJsCnq6Ve9Ha4qTwP-cHzx334MKrhk8q1ss86RSvdIGqXtilIms-8ghOyiV11GQGPSVg1J1VPZqD4_GIde1sZ418BnPQRkhu_ooRXQPyiK4CWd46QADLLpE5I1Los3-a18SUglzMHOxzGU3nuj1wfMi5z01n2kIduguvzsW5u43jjaEELTGKz8K1s2G9thwGTkzZgkWMWQH2sAd5XonHDD2YYDzN-9_w6YTfoT94kyCCjySYNMs1SGkRV6buKJj_LWnLWqLjv-QJapxaOpFOCwCdi9ASp7lBdbscZF6So2-TLjckcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونم اتفاقی عادی تو خاورمیانه اس ولی خب تعداد بیشماری پهپاد جاسوسی تو آسمون تهران مشاهده شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/funhiphop/84238" target="_blank">📅 19:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84236">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9XjZI2PRiSUf3colBjVORS7fESYy1QNvdR3w6S0XVxCYcdUgOhSNglLgVuFBmpNXkq0tXRD8uBySrvH2PqKd9T1JFw8MoaGN1xY_1XlvNhmuNwnCr3oR0IWJ_fSN4JbuzEBsRYYGvbWxNt2sCHDw-fsTjMVt7Lq7H2roPLzzyr1WMtlxw4gbG2m2L11AIymChahi_9ccL7HLNXVyAvLbfGH8NBQtYf5m7ia7RpGKHwegCRIJhXYevaHNR6fY-lEJp88_o8SQGnTOI42Uc3vDcjSYvalkFhGuwqeQJ33m5hgGTxtwf39rTJTeT5pI2xJCH4F5ohgTd3AgEXOA9PuJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی خیلی بیشعورید
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/funhiphop/84236" target="_blank">📅 19:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84235">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نورا،دختری که کتونی پسرونه میفروشه
😁
چرا از من کتونی بخری؟
چون
👇
1⃣
تمام کتونی هام بالاترین کوالیتی و شبیه ترین کیفیت به اورجینال هست
2⃣
خرید اقساطی ۴ماهه دارم
3⃣
تعویض و مرجوع بدون قید و شرط دارم
4⃣
ارسال رایگان هم دارم
5⃣
به عنوان هدیه جوراب و استیکر پک برای هر سفارش میدم
6⃣
۲۰۰هزار تومان تخفیف برای اولین خرید میدم
@iransneak</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/84235" target="_blank">📅 19:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84234">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1nRKasW9GGWejBgCzhS-nrfO9tcIXSG0wzV4tv_BkFY2C0vz7TWhiJgB150nntC0B_COCmMJZc6QOmDd4qeRU6Yc8LM3SFfVb72-79piIz7JcasRBkD7NJRqkYtJFXQEefmifV8IBtFzC31lqh1wEn5lbd0XDAjvkkdqSRtr9d2V3uUO6ewEDW7dt3up-OlYDk15KF5ZLPpcjHiJiBQ9swTCjSs9kJxABB68oBBH0JT4CoULVV_KnASB6gqsDrnN98FsEyWQOChWh1L3j9sDblg3m3NXDbTU9gZvbIVaMFNhWyDWXR4OR4DnMbasqbCo2z-Ho3MWhAyf97WAjuVlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدای همه دلقک بازیا واقعا دلم برا این بچه میسوزه، شده بازیچه دست چهارتا حرومزاده منفعت طلب.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/funhiphop/84234" target="_blank">📅 18:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84233">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/142f9f8326.mp4?token=ldJlHToWqCmCFugnMoqItHHSLAIkIeLfDzz8E5W_uqS4UrtiH-4DNxGYKFTtsIvju61qBpb1wvBM_4wgc-6oOOXavmJcVDFKcbTeoTNnu3dfoqcOGw6LVp1y4Eiy9PVSoODFU_WCxQg5EidqFw8hx2t8nA3sq-mkV28ydN24FVsgfWaU8_R3SjjacsjaaXlifcQEOKXdXZf2-TfINe77mhjensVQPHd3nK_vo0QGZetPk6u4Jg5BLrL0wcA03bbRBln0G8RpLSUeQwL1EpgWgDZXQcPauq4M5-F2HpaJo1-f_SWQNQi4H5wH1K66IDzmYlPbw81BJI0aGJwtAe7-MCN2VAkGRbfWhTdq7AaziuRtnJnQUHyZxqO0AgCIkX2mIyVmzumFVkpOyXayW44_OQ6IG8AshRukhZCpZweT7OggEhBTTW6XoqphLMisFsHSgdHY3MzdJUMzlcfp_5_qylv6BEAgWYOIn4UZvYXTVxd9fRrtbUsNPTrOi-9BY5zBbj7G7zT3wtbRLrDmx1A24-Oxi_ZFcUQL5mDGiYW30rqeGXZNiKDUgPVPtlMom9HPAT1hYDrI4LLSzywXeWNUmKSCJkMELDBx7PDrJYVPKIDA1V5w0Ys0raz7SJKUY2we6OZrsNzvnY0FZuSRsJBr6FiX0_ZfHxB3e3_7UzGhHMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/142f9f8326.mp4?token=ldJlHToWqCmCFugnMoqItHHSLAIkIeLfDzz8E5W_uqS4UrtiH-4DNxGYKFTtsIvju61qBpb1wvBM_4wgc-6oOOXavmJcVDFKcbTeoTNnu3dfoqcOGw6LVp1y4Eiy9PVSoODFU_WCxQg5EidqFw8hx2t8nA3sq-mkV28ydN24FVsgfWaU8_R3SjjacsjaaXlifcQEOKXdXZf2-TfINe77mhjensVQPHd3nK_vo0QGZetPk6u4Jg5BLrL0wcA03bbRBln0G8RpLSUeQwL1EpgWgDZXQcPauq4M5-F2HpaJo1-f_SWQNQi4H5wH1K66IDzmYlPbw81BJI0aGJwtAe7-MCN2VAkGRbfWhTdq7AaziuRtnJnQUHyZxqO0AgCIkX2mIyVmzumFVkpOyXayW44_OQ6IG8AshRukhZCpZweT7OggEhBTTW6XoqphLMisFsHSgdHY3MzdJUMzlcfp_5_qylv6BEAgWYOIn4UZvYXTVxd9fRrtbUsNPTrOi-9BY5zBbj7G7zT3wtbRLrDmx1A24-Oxi_ZFcUQL5mDGiYW30rqeGXZNiKDUgPVPtlMom9HPAT1hYDrI4LLSzywXeWNUmKSCJkMELDBx7PDrJYVPKIDA1V5w0Ys0raz7SJKUY2we6OZrsNzvnY0FZuSRsJBr6FiX0_ZfHxB3e3_7UzGhHMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جانی دپ
❌
محمود احمدی‌نژاد
✅
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/funhiphop/84233" target="_blank">📅 18:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84232">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/funhiphop/84232" target="_blank">📅 18:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84231">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncgXCVmcPq3XepK7PgkXb7k2_7OBcMpXuduV4vxHqtoRaqNWdWg3HNx6qWQPf4_b_lGLmZTefQ6SwO7jvKlGK9ePtEtucR3lkqN0KaKFw4ER3ZaJ2UI4ohD2u4n1LFMJcogdViP89iNG6782DAfYnl1rbl4AcxhCGlPweMuFXizNWjuIw7yRrj5NFaQ1Jt1fIqsqVu6v7roMaUb3Rz5Ki0pjQbcsVKKN7NC6fzbfNzo5HEZ8hxmHAKlvEbepOe4zQkbxBnbzcDAQrouALNQD7E7CMuxfZoEClDN1bkEECaLO_SxZdABR8LGie81KXqkf2L79PnKEQ5uHAMynVmtTuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👏
یک بار شارژ کن ، دوبار شارژشو‌ این طرح اختصاصی ریتزوبت برای کاربرای فارسی زبان خودش رو از دست نده
🔵
اولین پلتفرم جهانی و اسپانسر لیگ هلند محیط امن و حرفه ای برای عاشقان شرط بندی فوتبال
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
g8
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/funhiphop/84231" target="_blank">📅 18:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84229">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">میگن میرحسین موسوی مرد.
@Funhiphop
| Mehrdad</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/funhiphop/84229" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84228">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بابا حداقل یه خبر از رشید مظاهری بدید بدونیم زندس این بدبخت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/funhiphop/84228" target="_blank">📅 17:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84227">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8jG_5Cj8ysxW4l0fCVOJ8-ChG85OYGrugo2XLtkKL4faw_JfdKBjDsERlvilmVh4SOsj7z6vhBv8uDZpwDJqMnMts1OFRZUMh1xtBdnFEO6hXW8X8Cz1nYApEo7pOERyfrHw-6fCYeLckjMUB4_9Q9rYoWqLvKgvbvwX55f_wesONrWooBh9RXbm4yjApbrqt13jsVlnrNbpL9aiEBnN__N1TwheCTIxOf0Hy-TvHO48V6hpFL1Kn5et0JFIzDC_ZukDtPwb-Fs_BDTxK1QLaA4XT3uuZcFbqWiblQQ5kzoCJL8t3Se2CXwBthGC_pKIOGfB8_l-AvCxe6HOYl-ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبریک به پسر بچه های عشق گوز
برای سریال ترکی "اشرف رویا" یه اسپین اف ساختن که اتفاقات قبل از سریال اصلی رو نشون میده و بزودی منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/84227" target="_blank">📅 17:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84226">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">زن بیژن مرتضوی: بیژن برگشت ایران تو این شرایط سخت جنگی کنار مردمش باشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/funhiphop/84226" target="_blank">📅 17:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84225">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUPO39uL_dXzjxcpg9ylPigvFpsTDD9OSjQy8JP_7YwO8iAVJh5HqhnqdL-yfd3Pm3kV4_9rH8rt0cloGDGv_gJFArB_nvLbxbX6dUBO8wNeA3fYNKLdtb7_XF_As4Zz9x4ddC75pL2PjmDlVpcO1zHA9sCZOsJMLqbaBohKaPKtcRUgWVsvm9Oco3_F3OBW339P1e17T-Tu98dwq2c0OgjeN3LfA5_iHSvQpPSrzI8zqvZ70Yi02kSFBniqYHRjYIqXrkVOVKI-CvKzmZvjvJ7f9-onsr7EVdNDuRPbzZPDydD3IIIFtvFqD2ZghwWhT0nDfZ26HHrEKs6wG_f_AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/84225" target="_blank">📅 17:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84224">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بیژن مرتضوی که چند روز پیش می‌گفت میخوان منو بدنام کنن و برام شایعه درست کردن که ایرانم و با شرایط فعلی ایران نمیام امروز برای اثبات حرفش اومد فرودگاه امام و لایو گرفت.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/84224" target="_blank">📅 16:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84223">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بیژن مرتضوی که چند روز پیش می‌گفت میخوان منو بدنام کنن و برام شایعه درست کردن که ایرانم و با شرایط فعلی ایران نمیام امروز برای اثبات حرفش اومد فرودگاه امام و لایو گرفت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/84223" target="_blank">📅 16:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84222">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آتش‌نشانا دیگه شغل دومشون آتش نشانیه، شغل اولشون بلاگریه
از در و دیوار داره بلاگر آتش‌نشان می‌ریزه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84222" target="_blank">📅 14:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84221">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یک فروند هواپیمای مسافربری که از دبی به مقصد تلاویو درحال پرواز بود. اول از مسیر تل آویو دور شد بعد از کد اضطراری ۷۵۰۰ که نشون دهنده دزدیده شدن هواپیما هست استفاده کرد  @Funhiphop  | Mehrdad</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84221" target="_blank">📅 13:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84218">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2003caf7.mp4?token=lGRM2zXI5JNBHSe5ZmU8P4oVjUHyeLUvWVYT4xnkEymnAI0W7EReQtLt0MSvW7oOqkAUeE3hchlKdVFNw6LiwE5U7ZPbPPE6ul-41OZDrcleLA14NxZ3yQQDhUlKEXzYWQ7YNonWBAFIp0YVP7qym8JPIiNJ1GB59Frk2Gqa8zO0s9x-9aeuhxACbbwAD7MgjdPm9gg5DMP00hKk9G3vehOwlmb5u--gRxNoatKWsJro01hVXEM8woUWG6vcgy6EdOELAU1vRaHLkJjxPe00WgY1x2XfvjFj_lQoXm-96BqNJk7EWBq8I9VdS6rmj5HWxf3SiwdOGuGLh3Fr0L8thA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2003caf7.mp4?token=lGRM2zXI5JNBHSe5ZmU8P4oVjUHyeLUvWVYT4xnkEymnAI0W7EReQtLt0MSvW7oOqkAUeE3hchlKdVFNw6LiwE5U7ZPbPPE6ul-41OZDrcleLA14NxZ3yQQDhUlKEXzYWQ7YNonWBAFIp0YVP7qym8JPIiNJ1GB59Frk2Gqa8zO0s9x-9aeuhxACbbwAD7MgjdPm9gg5DMP00hKk9G3vehOwlmb5u--gRxNoatKWsJro01hVXEM8woUWG6vcgy6EdOELAU1vRaHLkJjxPe00WgY1x2XfvjFj_lQoXm-96BqNJk7EWBq8I9VdS6rmj5HWxf3SiwdOGuGLh3Fr0L8thA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میخوام برم استانبول کنسرت.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84218" target="_blank">📅 11:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84217">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1244f53d60.mp4?token=jmooQPfv4i4maCmm5e1PeuNIFeToK-W45u3IuWWpF_ccPKfG-PgzVIWwLSZ55oAHV_HwrMlrYGf_9WYT4xMtU_AaORhddEnpiOgVWNAA2wHMvT7GU8q3LsovUWzlUgB5gcRarDwCo59rey5pGQnqwodRW8eSDFnFDyz-2LpxjOyV6ks3rdjbqJIBll0nNigEEn8NqQhEz7CXXj1GiCKo-7OSO7G_jRoHdjHuL3K5KXOIOORj8Uu4TESvIYwq-mLf6_0XB1JVgGC-1rpZDQT6qHbR7F4hGg-2WnzLIkVTVXij6mLIvR7cdRi-ZGmanwXiQ8m8Kvs9G7oDJ1f1E3LreQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1244f53d60.mp4?token=jmooQPfv4i4maCmm5e1PeuNIFeToK-W45u3IuWWpF_ccPKfG-PgzVIWwLSZ55oAHV_HwrMlrYGf_9WYT4xMtU_AaORhddEnpiOgVWNAA2wHMvT7GU8q3LsovUWzlUgB5gcRarDwCo59rey5pGQnqwodRW8eSDFnFDyz-2LpxjOyV6ks3rdjbqJIBll0nNigEEn8NqQhEz7CXXj1GiCKo-7OSO7G_jRoHdjHuL3K5KXOIOORj8Uu4TESvIYwq-mLf6_0XB1JVgGC-1rpZDQT6qHbR7F4hGg-2WnzLIkVTVXij6mLIvR7cdRi-ZGmanwXiQ8m8Kvs9G7oDJ1f1E3LreQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پسره برای اینکه علاقشو به دوس دخترش ثابت کنه، رو گردنش تتو زده و نوشته: من سگ دوست دخترمم.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84217" target="_blank">📅 10:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84216">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84216" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/84216" target="_blank">📅 10:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84215">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6LHXwbW5jRa03J6ojpOEQIKRvHZr2hIWrv4DAPYBUUPfjJk0mIhLf67uSKK1go_hPV-ah6sseUamfI1LM07YtYJUeCxptAoxjrCObhnARHgPKWsNEjMiwPrTSUndiutwixxEE1CZQ8-i8im-L7epij3_O1vCnJg3CFNIEqysntEWqiSI0hAJrn-rXyZduvdRJqR0tAYgdrTWX4n-n9cN--J5i5xN1HkqslqtCndHv6_KZCEgHivXeI27CH3cMOwxNATQ_wvYqP0mATou84Tn_Mip8KJXzl9fcaqslzc-wQI1klhbxumX-vjaoz0U96T6vPv8O1x1BMdoEO-LJaE9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👏
یک بار شارژ کن ، دوبار شارژشو‌ این طرح اختصاصی ریتزوبت برای کاربرای فارسی زبان خودش رو از دست نده
🔵
اولین پلتفرم جهانی و اسپانسر لیگ هلند محیط امن و حرفه ای برای عاشقان شرط بندی فوتبال
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
r8
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/84215" target="_blank">📅 10:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84214">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک فروند هواپیمای مسافربری که از دبی به مقصد تلاویو درحال پرواز بود. اول از مسیر تل آویو دور شد بعد از کد اضطراری ۷۵۰۰ که نشون دهنده دزدیده شدن هواپیما هست استفاده کرد  @Funhiphop  | Mehrdad</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84214" target="_blank">📅 10:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84213">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یک فروند هواپیمای مسافربری که از دبی به مقصد تلاویو درحال پرواز بود. اول از مسیر تل آویو دور شد بعد از کد اضطراری ۷۵۰۰ که نشون دهنده دزدیده شدن هواپیما هست استفاده کرد
@Funhiphop
| Mehrdad</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/84213" target="_blank">📅 10:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84211">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5cQfopBbGJBiM_P47bu8GGXnpkM_klJQgZmy4-6XpHxbMXt_KgjHfj0CN3QUuW-6T98E4-Z1-m1B1nSJ0LcFIMPHNYWVN7mNnXcfwuaF8qMSYLXoyjX_9ENCqKwD_w5sb2zfSkQd_bN_XTd7fxwZmFae-hV6rbujEVvR28fzaglSD12r6f3aO4OSXMVtelh1VezzKa9WGUAKwOAchg382-EoMmEG6xM2ph9yErkOuztfR5XeqP6lNNh9ElqZFJZ3e2mbJmtY4bsYuK4xrYTPYSaAsvSUSmJpY8mihiUBWRxy0UiLKo6qOeeELFGOmjYqTl37cbGF6aCkE7AhROsBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dacdc1485a.mp4?token=j0lB4ykzZrErnWrvYwZwHW_eeM_QDq4r5hNe-hyKS7rNS2ikFCtlPt1JmeigPVqu7tJO0-f4hweHd_Fa0QwJxcaMan-Cf8hq9REv4Rvkv2Avn6YbO8ou5BGpzScsl1HLi3FScpZ_Q-eW5ur6FuRCARHe90Jn_XnhjQJZmBget68USPOG4VVYReN7GwSP1nvMB40vIhIWjOqZZWm0C2At6_KJ0nXZp14LkC9Hi4msv5inYOnCh8H30_bNAkRTGLg-qfaPzR0Ql9Y291YaeJT-KHF9uafhyNGpZpGoPnUzlNGCzTwfm2q_8Ywzq2qdcPzaLmmfri4y5hsO_IhQMTO5b0bB74hXrHfFXW2XQWIFl_lZNK5Kq3GQXUxbi9dWMH-j3612JO6jAoEVZar8yZLLLfg2_MtWVaaC81HKXLCVq1P7QP31dfr1k0BAH90ac2vN4UQ0-jQcDfssCXqKx3SudCf4LyAMC46ZKlfAqCFB1QpbVmvgt8MwCY6jHjnAnHHigBODYFcl3b6SwC_IH-llb4wtdXek1oLKnwLZX0vD5KOe7nnI0rm0n4l-Kps2ffjrNdtJYmU4KrAV6DXivLPY9eYaY_foG2XH68FI00mbOH_W_7M5QG1Qn2goz8MbMXIwJT1JJJtkL7VRBhee98aaW1h1HMi39IuZmMelQCYGWPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dacdc1485a.mp4?token=j0lB4ykzZrErnWrvYwZwHW_eeM_QDq4r5hNe-hyKS7rNS2ikFCtlPt1JmeigPVqu7tJO0-f4hweHd_Fa0QwJxcaMan-Cf8hq9REv4Rvkv2Avn6YbO8ou5BGpzScsl1HLi3FScpZ_Q-eW5ur6FuRCARHe90Jn_XnhjQJZmBget68USPOG4VVYReN7GwSP1nvMB40vIhIWjOqZZWm0C2At6_KJ0nXZp14LkC9Hi4msv5inYOnCh8H30_bNAkRTGLg-qfaPzR0Ql9Y291YaeJT-KHF9uafhyNGpZpGoPnUzlNGCzTwfm2q_8Ywzq2qdcPzaLmmfri4y5hsO_IhQMTO5b0bB74hXrHfFXW2XQWIFl_lZNK5Kq3GQXUxbi9dWMH-j3612JO6jAoEVZar8yZLLLfg2_MtWVaaC81HKXLCVq1P7QP31dfr1k0BAH90ac2vN4UQ0-jQcDfssCXqKx3SudCf4LyAMC46ZKlfAqCFB1QpbVmvgt8MwCY6jHjnAnHHigBODYFcl3b6SwC_IH-llb4wtdXek1oLKnwLZX0vD5KOe7nnI0rm0n4l-Kps2ffjrNdtJYmU4KrAV6DXivLPY9eYaY_foG2XH68FI00mbOH_W_7M5QG1Qn2goz8MbMXIwJT1JJJtkL7VRBhee98aaW1h1HMi39IuZmMelQCYGWPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی اومده یه سکانس از برنامه فان ۳۶۰ که ژوله اجرا میکنه گذاشته و گفته خیلی خفنه و اینا کاش قیاسی و ابوطالب اینا جای جلف بازی ازش یاد بگیرن و همچین شوخیایی بکنن
حالا قیاسی اومده کامنت گذاشته کصخل چی میگی این شوخی رو خود من نوشتم برا ژوله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84211" target="_blank">📅 10:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84210">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64cf794cfa.mp4?token=GDLmVEkZ5oE6i5V9_yhwueG0D5LCAJYRLe0tBTwJb1Pd8YrAg4wa4bopncw7xgVgmtgwQbne3V6yaeK-CIUmdtCP5RjKMb_nNxLiqoxJ8ecq5UBUB8vmQKJ3P8-KxKkWzdCRiNCWPzEQkUoNP9vT3jiSNTReSAkruerfqQRxFR_QsQ2n-s1ZHtqyzAibqT179iLc35vSeWPLfionReSSEo8Uyrmk4IjsAXoPxQkOefxsogBp3iPdyi9GkF3kLwMbzEXprACHfZa4x5MM0BoIHvnT9rPQp3XtCNzRlKM9P4PZKzWfyEbpzXT2MS8zV2vQ-N7xb-o5p9_0V98STE2FcA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64cf794cfa.mp4?token=GDLmVEkZ5oE6i5V9_yhwueG0D5LCAJYRLe0tBTwJb1Pd8YrAg4wa4bopncw7xgVgmtgwQbne3V6yaeK-CIUmdtCP5RjKMb_nNxLiqoxJ8ecq5UBUB8vmQKJ3P8-KxKkWzdCRiNCWPzEQkUoNP9vT3jiSNTReSAkruerfqQRxFR_QsQ2n-s1ZHtqyzAibqT179iLc35vSeWPLfionReSSEo8Uyrmk4IjsAXoPxQkOefxsogBp3iPdyi9GkF3kLwMbzEXprACHfZa4x5MM0BoIHvnT9rPQp3XtCNzRlKM9P4PZKzWfyEbpzXT2MS8zV2vQ-N7xb-o5p9_0V98STE2FcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بلاگر ایرانی تو خارج که اتفاقا فن کوروش وانتونز هم بوده، می‌ره یه ویدیو می‌سازه که توش نظر خارجی‌ها رو درمورد ظاهر سلبریتی‌های ایرانی می‌پرسه و عکس پارتنر کوروش وانتونز هم اون لابه‌لا بوده که کوروش برمی‌گرده به این بلاگره فحاشی خیلی سنگینی می‌کنه.
بلاگره هم برمی‌گرده می‌گه زنت ۹۰۰ کا فالوور داره هر روز از خودش عکس می‌ذاره بعد حالا من عکسشو به چهار نفر نشون دادم اینجوری فحاشی می‌کنی؟
به نظرتون بلاگره مقصره یا کوروش زیاده‌روی کرده؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84210" target="_blank">📅 03:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84209">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvUDOJT9YOlAqwOPm18-UqVQAFRZXifWWONbSRKok02DoAKo1kFjHGNTcW_VzbkQR9ObRYcLsoXxX4tHBwrLZKkkoqg3XwLjs0exftdouDnygjcBs6GAty3AviFwktEKH9Pmh8waXcAf4irolYwCic2CvuFpkP_t9rm0x18tasLRoth-csNQK5KTUOVZ60kTehhrwVPXUMeWOWFEid6Bv-g4JaU4hn19OK4WQFmmFANoB9XKx38V8xn776FXo6DrmIRyUUPrXu48pJmRGWVgn7HeqpXhtWzZpm3L4EhiNW-s9Cdi2RcXtNohd7c7maILwtDCrEFqtpRcmtIL7uZf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواب از کلم پرید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84209" target="_blank">📅 00:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84208">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQXEsGlNTHqQyw3MJq7xSu8YrvQlqMBHCZuLode_I0JVa5RDRhgAGmd5czsSPkdbMGSlEt7YQlM30d7GdQ-_wvOvzmTIry9uZ7pFyyZrxvPIKFnbJ9m9qOWLCWpf60F3zdxiR7rzyxq9A3T5rYxr9t0BhTCyoQiBY3W6GJO7cLsYcFTndWD2x_AqHFhjLJ3iInj288P2uLOLjL4qAKfcSSTuE8bfSfHD5vPqHbmi8NLZtrdEGuUXspaM4JTQgL5RjQptXhEzAClKbSsrFS8AGdxgaDXsMI_FkxZjEL-6Vl_Y_l7szwN7vU0bk0mh9lvmBNu5nJo-RJ-otCqnkdrkZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بیانیه میلی‌گلد: بعد از پیگیری‌های میلی دستور آزادسازی طلاهای میلی از بانک کارگشایی صادر شد
خدمت تسویه و تحویل که به علت مسدودی دارایی‌های میلی در بانک کارگشایی مختل شده بود، فردا عصر پس از دریافت طلا از بانک کارگشایی به روال طبیعی بازخواهد گشت.
همچنین طبق دستور دادستان، محدودیت‌های اعمال شده بر درگاه میلی رفع خواهد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84208" target="_blank">📅 00:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84207">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رسام سهرابی جان مادرت وقتایی که جیحونی پنجره کیریو ببند بعد داد و بیداد کن سری بعد زنگ میزنم 110 میگم پرونده هم داری
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84207" target="_blank">📅 00:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84205">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">به وقت سم های عشق ابدی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84205" target="_blank">📅 23:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84204">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فرمین لوپز تو کیر شانسی میتونه با ما ایرانیا رقابت پایاپایی داشته باشه واقعا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84204" target="_blank">📅 23:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84203">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پشمام از یامال</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84203" target="_blank">📅 22:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84202">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-_fjFytvuqIzA2YJ30Rwq59zxDAfJu1sZCDjNhH7GZt_kpnceDm8trwGsTwsL9zdDs1HXgQkAedHlcUibpIr4PSgr_xlsPWRjj_VSKGC-X_y-LDy-TNG8BmzRKKI3x3btjtqhv7BtBhxnyeCNYsxkLYsV5Df1bM71W46DGGf7wcw8zn3AmFIFp7xOsKS2Gc2SpIaS3on8-Vm9SpUwDhNq28krOCc8p92kihQF_dQ-1qcv3Gx7l1IWUKEoUdxzsI_Qn6zbqCIXIw_ycGMSV1p56amlwIos8whoq7k7ADqBL8-AFfcG5nWw0h28tVnBHeTo3bBIKbW9Sw6tJt37n9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز همزمان با پلمپ شدن مغازه های ربکا عکس دوس پسر جدیدشم لیک شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84202" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84198">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یاسر بختیاری در یک لایو ۴ نفره اعلام کرد فیت سه نفره او با رضا پیشرو و tech 9 قطعا در کمتر از ۱۲ سال آینده منتشر خواهد شد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84198" target="_blank">📅 20:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84196">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بر جرعت میتونم بگم رضا پیشرو درحال حاضر رپر هایپ تریه تا تک ناین
و رضا پیشرو انقد هایپه سه روز آلبوم داده و بعنوان یه ادمین رسانه رپی هنوز گوشش نکردم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84196" target="_blank">📅 20:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84195">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یاسر بختیاری در یک لایو ۴ نفره اعلام کرد فیت سه نفره او با رضا پیشرو و tech 9 قطعا در کمتر از ۱۲ سال آینده منتشر خواهد شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84195" target="_blank">📅 20:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84193">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tguMdOZveqBjPq2gfKrJ00m4_uqViPK81y6NeL7UxrCI5-Ul6UwyhGSmWLgvbD6GHmbqD1-U72ndBZg44wynz73EEVRbAkXqjiAYyS6HZc9o3U-Rmd_vX7yQXDu7HdWFWFbuR6ERVPRD5ShESqmFS0J40-fyb38mS3zlhx8XBYay6KDlqYOuCQLgryTi4DBiOVNxc28qcKqfidmBKlJ8xM2AfeHBUNPY52p2Sz0oQReu9ID4iegjcV333alYpuONkCsJS0NaqR2l7ZqaYb22iqaPK0yyEbvRJJ_X4ee8hlk8YSlcnhkWjG021SSaACWoMmhxMXzvY3MKDaBy678G5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا باید صبح بیدار شیم از شیک زدن زنمون فیلم بگیریم بزاریم توییتر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84193" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84190">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سیتی محکوم شد و بزودی حکمش میاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84190" target="_blank">📅 19:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84189">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtFcfD4nWEH5zFSJzasLCtrAaYP0mu5Rp9uXBm_aLLiELnKM7FW6-nuUl8GRVNCs0aDGJNkUWfHlM3QXGjOcUWUTXhMZsTkj9LoIVU4rsDgnv3RpJvddZhzQYJX55glHpkmtcP9Yvqonise4_Ap_UeowHdDSQaxsNhB7f7VIVHLBD-RG8_c72l4QS4T0abNRDzgWv9afo4k3XqQ-DSe8Klahg-p3V1_v54DuTh6qM-nyPouZNNC2LH5kXYnf6cRadSCMMkn9uy7jIO94Km6TQZbkjwq9j9VEuZuSovJLKbc2JxAaE8k5M0O2_qMpYpafxzV9_b9OsQpLUCeiC1vbPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید آرون و کاگان به نام "انکار" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84189" target="_blank">📅 18:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84188">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترک جدید بهزاد لیتو و بیگ شگی به نام "1.6" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84188" target="_blank">📅 18:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84187">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeOVTkvxM2nVfbbozSbn25Z8XCuUPTRGyvxi1Fl8KI6tA6VeyrFiXrJsDuraRaKjsUHB7wmQVELSUdQiAsDq0kiq-HNMs89vQosUPPu3XuF0qbsK9qOF59RvbJpf-mdb9b7t4f4peDcQFP8orng4CV1vCewLR4_csgYTUF0ZKaJXx7Z38HuZnhb31hprjCIDh8zGHPABTm5qNQ3iQIBpfrFbjqpICYlz-asb4J9FYlc8ljt2bi_LoP-x3ndX2h68cXKYpjd6gVimj9EMojG4aFf6huxj0hPOz67MPCkirLEb6rqN1YenhYsvbS81C7oBHsnLHmvfJSj6SSjCKvUaUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید بهزاد لیتو و بیگ شگی به نام "1.6" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84187" target="_blank">📅 18:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84186">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv_0Cld3vKDn3Sio4Xeyw3RkwskwpNzgNPQ0kVoWPUMm_4o6XQNmQ_07uAXFACIttsuXCVEvggj4QlbGcnggAV-lJb_Nt9ZZvM4UObzuspR6Sr4hSk_T9QO8auw3I2fDzIflyS73VQF-MEdk3tMVX5lIYy3gM_CU2HsauO4XxTAxIbSzn7LNC1uYhFrwTDkwUrGLp8lTltjwZpz37pMf8Z7H-ILVt2StYlLnz3cw1WxGm9x2yRSo3XojI5boD65hKK-ZXHP7ZhowTGWZhSZOodKXkfGFKB6y7CwcrU5hRhafjYWiCpHZ-lKCXZqX58z_SFQShmEG1tXXyViMW-HOUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاره شدم این چرا اینجوریهههه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84186" target="_blank">📅 18:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84185">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862ec698b.mp4?token=GX61koqIDD4irOuD-uKJ7S8aDQXbdflp8BarGMW5c97D868XpTJR_KHhixc5QjllbAGZzdNFpeatg4ooJOntSd6Hzd72gXJ3Bq4L0lLJAav8HaN32oux6Nbt-YtX5dJwVGSABloAutfQjV8CqGPauy8yx2fA50wZgI7pjN5sNDGmFWDdB4biJcSckP-66YyCJJAQPztvHkaH5GpCwh08yZQN7M5_KQHofJDoiKKUej84NEu71j0CCQS_q2uR7a0lG_M0q6oMZCLWTmmougcIm-Bz2MFU_FScoAmkT7ThfTbh_NcLRk8pXQkazlpJmVi2kOKRRoTP5DbpPt-FTi8RTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862ec698b.mp4?token=GX61koqIDD4irOuD-uKJ7S8aDQXbdflp8BarGMW5c97D868XpTJR_KHhixc5QjllbAGZzdNFpeatg4ooJOntSd6Hzd72gXJ3Bq4L0lLJAav8HaN32oux6Nbt-YtX5dJwVGSABloAutfQjV8CqGPauy8yx2fA50wZgI7pjN5sNDGmFWDdB4biJcSckP-66YyCJJAQPztvHkaH5GpCwh08yZQN7M5_KQHofJDoiKKUej84NEu71j0CCQS_q2uR7a0lG_M0q6oMZCLWTmmougcIm-Bz2MFU_FScoAmkT7ThfTbh_NcLRk8pXQkazlpJmVi2kOKRRoTP5DbpPt-FTi8RTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی چوپان: یه ساله دارم کابوس میبینم؛ باورم نمیشه دیگه محبوبیت قبلو ندارم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/84185" target="_blank">📅 18:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84182">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ادم اخه طلا رو مجازی میخره</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84182" target="_blank">📅 17:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84181">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">معلوم نیست کی خورده ولی نزدیک ۲۰۰ میلیون دلار اموال مردم تو میلی گلد بگا رفته و هیشکی پاسخگو نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84181" target="_blank">📅 17:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84179">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf73bf24d.mp4?token=rLSl2pyLNsao9__O6lIAxc5lj7xHJtZ8frxfJGOdI8RbBVckYYUP9RzvCw0zenckvtOxcoZSymmeI2DkYasoaBbNJNLpZz9-tIELKqOQf2NejoFJAGoA5S4NWK5nsDktB5aPgY-L64olwJeg0TKjhuFyv9p3eYJ3OYtbloR0xbJZPx40pL_u9QFlEwxYdky2eX5xyzK0j7IdTBLuyz7bR0p5fKvx-e7mu1Leg4cJSffabzwJ0dTF3ocKEdH1_j3MLz58ePFAqgRyUuJaLPudBiSN3dEkcpC4Su9n_OS6TdMaB16bSLLh5ImOcE3iUbpDE31sSd43hUFdnaRxV31xJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf73bf24d.mp4?token=rLSl2pyLNsao9__O6lIAxc5lj7xHJtZ8frxfJGOdI8RbBVckYYUP9RzvCw0zenckvtOxcoZSymmeI2DkYasoaBbNJNLpZz9-tIELKqOQf2NejoFJAGoA5S4NWK5nsDktB5aPgY-L64olwJeg0TKjhuFyv9p3eYJ3OYtbloR0xbJZPx40pL_u9QFlEwxYdky2eX5xyzK0j7IdTBLuyz7bR0p5fKvx-e7mu1Leg4cJSffabzwJ0dTF3ocKEdH1_j3MLz58ePFAqgRyUuJaLPudBiSN3dEkcpC4Su9n_OS6TdMaB16bSLLh5ImOcE3iUbpDE31sSd43hUFdnaRxV31xJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خارکسه حداقل بدون لهجه فارسی حرف بزن بعد بحث وطن و وطن پرستی بکن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84179" target="_blank">📅 16:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84178">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه زمانی خارجی ها مسخرمون  میکردن بخاطر کالا برگ ۷ دلاری الان چطوری بگیم  شده ۱.۱۷ دلار
سخنگوی دولت: خبر خوش دارم اونم اینه که الحمدالله بحث کالابرگ حل شد و از نیمه دوم مهر کالابرگ رقمش میره بالاتر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84178" target="_blank">📅 16:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84177">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">در همین حینی که قالیباف گفته اگه ما نفت نفروشیم هیچ کشوری نمیتونه بفروشه تو ۴۸ ساعت گذشته ۲۲ میلیون بشکه نفت از تنگه هرمز خارج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84177" target="_blank">📅 16:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84176">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZG_xO0_XeABAhcPja_gf3Qq7y6HwKXT8GkknMULUwn-njiKE7-EXo58R67p9mzoC0in4gOCXhuDOxQgGj8FY_Cf-lVEDz8StwvMP0sgmu3Ti-QDQXpz_fvv2grPMV4zJpugoreKWgrTRgYxe7qE4C4-uC1IXGiPzQtgKI2T-5RRSXlzsRpSyu46ikp6Rs2J93xGA5swLA2r2A--SVu0I52fGlnTvHIchnOy3Q9hmFBVPRcy6e2AeLLM1XbRW6GjkXyDPpg4xsWIPhiJ7np4ITpJQRDk1Y8zVLWma1RTCWrPFDbnQaWzzjoT5_L0lq8cagunWjGOzLhn07D32W3hOMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار دیگ ترکراری شده لیر رفته بالا ۵ هزار تومن انشالا تا اخر ماه دیگ ۱۰ هزارتایی شدنش رو جشن میگیریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84176" target="_blank">📅 15:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84175">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تو این دوسال آنچلوتی که سرمربی تیم ملی برزیله بیشتر از سرمربی های رئال به رئال خدمت کرده با مصدوم کردن رافینیا   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84175" target="_blank">📅 15:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84174">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آمریکا بعد از تحریم کل خطوط هواپیمایی ایران، الان فقط یه مجوز یک ماهه برا پروازای ایران و عراق با کلی شرط صادر کرده که توش فقط می‌تونه مسافر زیر نظارت کامل آمریکا بره نجف برا زیارت و باید از همون نجف هم برگرده ایران.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84174" target="_blank">📅 14:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84173">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">به کسی که حمایت نمیکنه ازتون فحش میدید به کسیم که حمایت میکنه ازتون و بگا میره میخندید
واقعا آدمای کصخلی هستید</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84173" target="_blank">📅 13:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84172">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هردو فروشگاه لوازم آرایشی بهداشتی ربکا قادری داخل ایران پلمپ شد و تمام اموالش داخل ایران مصادره شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84172" target="_blank">📅 13:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84171">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M27pMYcqb5ljfFXIwcvfGf-ATY6wFE3p2edcWFGbpEBS0sizcmCkOGCUkNyQJoewgU-5-hj35aKxrCC0a4TDfBTr4-aqcadsheCqGInjQaKzmVBvGABRJA1na5UcWqaJaoLxaTDlTUTRKn62Ss08pi7Q1IF_oS0k46ubGHISbKD-XW_RCzXIM2xqKV7BSmefNwBXyUKLglgJZR-pgLWxIWDS9bZNPjjjcMALvknK55lBiChTEqiUDeye4EN5zaN2P_H9KJO_uYarTy_AeTOEZIIjS6RXAZRs94RG4q2a8vmZXsGeiXJlYr4b7rAwN5kUshel0uWlRFHD2AKWBg_mvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هردو فروشگاه لوازم آرایشی بهداشتی ربکا قادری داخل ایران پلمپ شد و تمام اموالش داخل ایران مصادره شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84171" target="_blank">📅 13:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84170">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
مردم آمریکا تحمل کنید کمک در راه است
سپاه یه نامه زده خطاب به مردم آمریکا: حساب خودتان را از اشغالگران فلسطین که خواه ناخواه باید آنجا را ترک کنند و به کشورهایشان برگردند، جدا کنید، ما می‌توانیم همزیستی مسالمت‌آمیزی با هم داشته باشیم.
دولت یاغی، کودک‌کش، شهوتران و بی‌خرد را کنار بگذارید، امور خود را به‌جای اراذل به اندیشمندان بسپارید و به آنها یادآوری کنید که دنیا عوض شده است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84170" target="_blank">📅 13:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84169">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e6ffd31df.mp4?token=BJPwcQgilwyMPDi1BjKxix2S217tIZMuHmBEgVHKzi32wZ0m8FDINpsGRR_RDj6yTkGkJRoEwn5ZQ6eHx08mQvbv7TDZQPTOXEm_JXV2MnZlxKDWEcV_3NrQQzMy9eFZgnPVJFdEnM6lFywJXylgKTgvt72rm3XricAhEOXkCHCw19mzjjn4f3o4Zt17n-LCCd21Yf_Euii2AXtsQJrZ3bqga9O6bI9IdQyS_8ZAkyeNryFVBaH-WnuC2FYr2bdHxxtirPp_W5UBqJmBHC1HLdBfTRHkezIvPQ8d5BnbdMGenGNbyYn49P7oJ9aYELDDQZe2fVsEq21vaMuvz5uzFA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e6ffd31df.mp4?token=BJPwcQgilwyMPDi1BjKxix2S217tIZMuHmBEgVHKzi32wZ0m8FDINpsGRR_RDj6yTkGkJRoEwn5ZQ6eHx08mQvbv7TDZQPTOXEm_JXV2MnZlxKDWEcV_3NrQQzMy9eFZgnPVJFdEnM6lFywJXylgKTgvt72rm3XricAhEOXkCHCw19mzjjn4f3o4Zt17n-LCCd21Yf_Euii2AXtsQJrZ3bqga9O6bI9IdQyS_8ZAkyeNryFVBaH-WnuC2FYr2bdHxxtirPp_W5UBqJmBHC1HLdBfTRHkezIvPQ8d5BnbdMGenGNbyYn49P7oJ9aYELDDQZe2fVsEq21vaMuvz5uzFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#شرمنده_بابت_پست_رپی
به نظرتون ویناک به داریوش چی داده که داریوش حاضر شده چنین شاهکاری رو خلق کنه؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84169" target="_blank">📅 13:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84168">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تو این دوسال آنچلوتی که سرمربی تیم ملی برزیله بیشتر از سرمربی های رئال به رئال خدمت کرده با مصدوم کردن رافینیا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84168" target="_blank">📅 13:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84167">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdNN_M-c4H8oHzPZugTeIGHZ6qJ_sel5XAz5iBmijzZgfwcqrcTkRqVnPhYdMmNMS5kuBZNoL_3UdDohREANKMlPhcpWn-iJMsq0dskWiC7yc4UDD-VrmSrbKculfvbQ-romzNsfS_6DHHQO-jedXBo1m2Fvh1itxKb11WVxrnsiYftxeFvIoOWF3A5LVx6e2G1v8CNRcSJYTs3w_f9y9-n7Q7qKg3CMwJkjca1gPAlbvnHEYee-xhfq2i_BGNHQljPAM8csyb6BzIDF_buoU8L3EV6i29QyAN-2VzsoKQDw3JILmNAFD7GAcMhLiFPbNEfRa0dgVmE9WM8bdCUBNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو دین یهودیت چیزی به نام تغییر دین از دین دیگری به یهودی وجود نداره، هرکی یهودیه باید تو خونش باشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84167" target="_blank">📅 12:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84164">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سخنگوی قوه قضاییه:پرونده حقوقی ترور سردار سلیمانی در دادگستری تهران تشکیل شد که سه هزار و ۳۱۷ نفر شاکی داشت
رأی این پرونده دو سال و نیم پیش صادر شد و بر اساس آن، سردمداران دولت آمریکا به پرداخت ۴۸ میلیارد دلار محکوم شدند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84164" target="_blank">📅 12:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84163">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ما میگیم اعدام فوری بیرانوند دور میدون آزادی شما میگید بره سربازی؟</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84163" target="_blank">📅 11:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84162">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/398fe520da.mp4?token=fcRJxGgor3G6lYPK8Ih6dgbgy7fP-m0prIkI79z5mQyeXLKEy7ElNN8CnFPBj1UBlUxsHN4txv1ttzMZcWPqB-yKZB9DR3pJwYCubiW-qnU1iVwU-tKwk3cxQKqCGL7ax8TL7QOuDxHzRHNq0DzGxNFlQRY0anoO75I2EYk-VlmlUcrkPFKWbs2VOWFE4Qg1XGzNyPQndlmG7ME6TwlTl4nx5zK-2V9WnUGQ1IuhmZ5aeR5KAM68lAq7V1JjfgDhA5ex8wWQ_IOu07fVLrkerBcu77aUKekartYPoYORz8yRnzrUfIRPLj1LzePmFGwju7TD3jirM1n9Cwm8NP7ULJvzyyR_HxORHJIgZrWjO3YgwYdiT8HfOhKObOH-Kr0TfXuFZ3iJHerqxD4L6oNnTXoKBtRai2BrtOY9EAoRQZmHN6vR1hpnal7PaKTwsJs3R_TJ3ZvpKAaOLJlPCrwKue-Joy5sShfu7OJmMKHUqjB1gWxRQVwPXAI1PDK3gGSW9VGxhscK1ViBKOQWjEFZr3ZUQg_8Lu0hmzFRlc-MqgdWlB3uJzNtCJWtAUxTiKkK_gMKHaVFQaIi3WRFr3hRef6fs6LvUnDq4yDDvILQBsV88f8GHLpc85QTMl9oGE31XIu9vSnwHkM_m-45OrhCuwgVuD9HlWtGjdamSMtu-TU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/398fe520da.mp4?token=fcRJxGgor3G6lYPK8Ih6dgbgy7fP-m0prIkI79z5mQyeXLKEy7ElNN8CnFPBj1UBlUxsHN4txv1ttzMZcWPqB-yKZB9DR3pJwYCubiW-qnU1iVwU-tKwk3cxQKqCGL7ax8TL7QOuDxHzRHNq0DzGxNFlQRY0anoO75I2EYk-VlmlUcrkPFKWbs2VOWFE4Qg1XGzNyPQndlmG7ME6TwlTl4nx5zK-2V9WnUGQ1IuhmZ5aeR5KAM68lAq7V1JjfgDhA5ex8wWQ_IOu07fVLrkerBcu77aUKekartYPoYORz8yRnzrUfIRPLj1LzePmFGwju7TD3jirM1n9Cwm8NP7ULJvzyyR_HxORHJIgZrWjO3YgwYdiT8HfOhKObOH-Kr0TfXuFZ3iJHerqxD4L6oNnTXoKBtRai2BrtOY9EAoRQZmHN6vR1hpnal7PaKTwsJs3R_TJ3ZvpKAaOLJlPCrwKue-Joy5sShfu7OJmMKHUqjB1gWxRQVwPXAI1PDK3gGSW9VGxhscK1ViBKOQWjEFZr3ZUQg_8Lu0hmzFRlc-MqgdWlB3uJzNtCJWtAUxTiKkK_gMKHaVFQaIi3WRFr3hRef6fs6LvUnDq4yDDvILQBsV88f8GHLpc85QTMl9oGE31XIu9vSnwHkM_m-45OrhCuwgVuD9HlWtGjdamSMtu-TU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با یه پست رپی ناب روزمون رو شروع کنیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84162" target="_blank">📅 09:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84161">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">صبح دلار ۲۵۰ تومنیتون بخیر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84161" target="_blank">📅 09:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84160">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یسری رسانه میگن عراقچی قبول کرده تسلیم بشن و اورانیوم هارو بدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84160" target="_blank">📅 00:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84159">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مادر ترکیه گاییده شد که</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/84159" target="_blank">📅 22:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84158">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قوه قضاییه: حمید رسایی به بند ویژه روحانیت زندان اوین منتقل و رسما زندانی شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/84158" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84157">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A394lCyQkbKj1KpmiUycfwtblj8V8fMAgA9QjZ3hftp1B5KcAzRbC_xgL-cl0k-AspwVfQTPTVJMMYht2V4Y8Di0OZuf0yyqHfs4qpFVQfHu3Kv6YpJ-OCzTR9HkBdXobLPydjWhi46rDaPnFK5q4YYZgw60rjL1OysR2d1_SGQgbOmPcFJUcWtQ8Hojx5OBzNBv6jHA8bsvlM4v1jTlFf5m2ENHZKbwp5hSoQlcogHEl6Ov6QgR69vlGRdLfb3loXCVAQRuTTLsLNOBpCY7zTEUgrgqj95VIYDhO5cMwUYfY_JFh623iW3UJavz6QslxArNm0RGmMLZLAdFByEvBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه:
حمید رسایی به بند ویژه روحانیت زندان اوین منتقل و رسما زندانی شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/84157" target="_blank">📅 21:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84156">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BF17SPY_3yF1fMIz9TVr6lOBI6weWDQukCShWPPY6X_uphsn5zAYAf5Bm7Yi_mS-6RZui7-gcwpiOSIDgSQmY0BcUVKX73FYI18axi8-LizrcKhJkvRICa6wK8bgYAlh4NfemocLD8ittIzOaaTM-LaJoeYzAfAGNvPxyEW3PejFYZvOk_tM0881tfxIhTh61sIM89nSujhAvqKtHQN8O_3Fr-rmNMx1FRG2fK6EX5M6uvGf36nQ55gXS23ikZ1Bq87Oc7ZFJm6837bc1mPRESiS0ERz_KTQOpf1Oxa7Tl5DmOUGptj0o1ggR0P-IlD9gLXNhqHf7DV1Knp0ANbVBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من وقتی یبار تصمیم میگیرن رو فرانسه بزنم بعد عمری
واکنش زیدان:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84156" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84155">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oR-1eDZtHH3AhqZo5wctiutBS22cQPQmFmJ9TMs9cmEslZrJ1qTLUNfjyWl9fg81X4OcV6usIB2EocXmxvPj3-p-bbEQf_xX0Kzjb_r8U0pqmDkprPMFzA3ZC_WV_Cjussb_vHNHb1Abl207zYRTRuj9kxVSF1GPUTZf86uEZ0HfgYJ4lUEDPhKToLLQsTsBLIq2eXEbBUz2tnNxOm1_i9o6GkNdaSNPrJNqUAozDVjg4fVX7ivyimYFekvwVvh6UBCL8gTlmOo8qtumw-dRYohrPTqcrGI_50xh_DApenaEJ3SHbs9bGRxHrO_6vvjand9sXVIFv3rUqhNG1dEH5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلیت به دخترا
ایسم عکسش با زیدشو استوری کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84155" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84152">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff9d6bc22.mp4?token=XrU7lhm7C9OF6uBdlcn6X7yCFzeTxcezZTOwUhPJ4-PqkUBEWylakkro4SfHQT-DFCPNW_UVpLwTz6tSDlt-NAKrWZHDmO-T8vmARe_yp4smw14eHqepPLA613CAySkDR1sekRFmwN6z8_sYFlDgmnoy5nnmqlAsg3NiGvtjpI9Z08BtZv5cdv0gtqgo0RWhuTK4pHKZASjp5-kLqyMe3aS4FuSANFsYCLvoKH7nsAKTWlhH2kUadK9_h0lXAvmVDL1WtTLQGXn9d9fZhp84hqc1bQshn2Yd0jvx8IaPGTIIPY9u9xuF3RYE9YUZrTQdumIg9CPG_-5Ohfk5Lm3R1zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff9d6bc22.mp4?token=XrU7lhm7C9OF6uBdlcn6X7yCFzeTxcezZTOwUhPJ4-PqkUBEWylakkro4SfHQT-DFCPNW_UVpLwTz6tSDlt-NAKrWZHDmO-T8vmARe_yp4smw14eHqepPLA613CAySkDR1sekRFmwN6z8_sYFlDgmnoy5nnmqlAsg3NiGvtjpI9Z08BtZv5cdv0gtqgo0RWhuTK4pHKZASjp5-kLqyMe3aS4FuSANFsYCLvoKH7nsAKTWlhH2kUadK9_h0lXAvmVDL1WtTLQGXn9d9fZhp84hqc1bQshn2Yd0jvx8IaPGTIIPY9u9xuF3RYE9YUZrTQdumIg9CPG_-5Ohfk5Lm3R1zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حلال ترین استفاده از هوش مصنوعی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84152" target="_blank">📅 20:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84151">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اسنپ پی روح و روان سالم چهار قسطه نمیفروشه؟</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84151" target="_blank">📅 19:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84150">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آلبوم جدید ناجی به نام "استار بوی" ریلیز شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84150" target="_blank">📅 19:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84149">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgVeAJklj7QIdAgROBYIgv3SfpUvgY3Ek20wfX9Isif6oYhOvS9PW8k-PI0Zhotep4L7U3GdGefF0DcUTiByLtl78cibOMXZw6j3jzPjdkF9XbDtyc6kKC8yWVLUsRi4MPB5V5uIEWHnKnzGp53ucz_XPAvEf2B6cj3kyX89V898pJKf653lptd7uogsZK4GHwF4GpP-AHG7rzPa1qo5PPGZ3xVTKTOKxATJXgf_ljNNBPzjBU579J-O3kl6HLu8lhIhF1Tis2W29y3OwequstA3Yf_wqwYlgtUEj8bC0i_R3DXlKIEAvjrnWExQGNt_Y9iNuBNwRhLIYRUIR1dE7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید ناجی به نام "استار بوی" ریلیز شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84149" target="_blank">📅 19:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84147">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seZs_VcZFXekhFc8-3eUbHcHrXZjenyih3M3x1mWLur6I8ER5wA1MM_tiOUVJ6gZhZhWjMs3nH0vMLJfnNHjFnoNm62ufC7EbVZ60AH7lR6kRY6QeI0ZuhHERSybTZcX9OiDhLUS6viiBF2kSWQUB3ALIViCUovTMGXrBkugt-DWtvp3bgOS6J9azapcdDoeHlw50NvjyoDXGBIPx1JqFkaz1lKKSCWEZY1Wz57Dt1H-bBRASqc34c_hwdAONeSDcuc9YFDB-OgEoqYf_S_BOcW0VamiI-TXWDpb18ZqAWJzo0zZaYLToLZwBnBwyY7tLOxv82IwFIABPP8tanEXIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213569f829.mp4?token=fHKcSYhLt7TaxGqQPnuc5AQzU3A_VroHoRDvmJawsuGEVOn5-JWxKk5fu8ipiR0yK6ZJELF-q1wdcsQka3jjEPGM42cP9iAsWiHxCKd-B14xxmrdTjAO8Rc-ImZk_8dyiOPiaiDv8neRCA2VHmisyidQJF6izG6wdAS2Ledv4ticviV_7y5ELdPiO7wTaQIJh4PPDDGQhgZ4lWjSPz6cWwsIoHs87zTR-u-FgMjSXT1tfjKVTZ9F-kaHbmbo3--LQiQVU80wNhO4Kn10nZaUWLWaFREvFD_c8VMPQOdp85pkm6kL4FTRF64_lbypu1h0A54qrHAT4cSLJnV8dVvf5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213569f829.mp4?token=fHKcSYhLt7TaxGqQPnuc5AQzU3A_VroHoRDvmJawsuGEVOn5-JWxKk5fu8ipiR0yK6ZJELF-q1wdcsQka3jjEPGM42cP9iAsWiHxCKd-B14xxmrdTjAO8Rc-ImZk_8dyiOPiaiDv8neRCA2VHmisyidQJF6izG6wdAS2Ledv4ticviV_7y5ELdPiO7wTaQIJh4PPDDGQhgZ4lWjSPz6cWwsIoHs87zTR-u-FgMjSXT1tfjKVTZ9F-kaHbmbo3--LQiQVU80wNhO4Kn10nZaUWLWaFREvFD_c8VMPQOdp85pkm6kL4FTRF64_lbypu1h0A54qrHAT4cSLJnV8dVvf5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این داداشمون دابمسش های دخترا با موزیکا علی گرامی و سجاد شاهی رو نشون ندید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84147" target="_blank">📅 18:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84144">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">باز قیمت دلار رند شد ملت یادشون افتاد دلار گرونه</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84144" target="_blank">📅 18:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84142">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نمیشه به دلیل تقلب های سیتی یدونه قهرمانی آسیا هم به پرسپولیس بدن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84142" target="_blank">📅 18:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84141">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ولی این انصاف نیست کانیه وست کیر خورد پسر عموش کیرش خورده شد کاسه کوزه ها سر من شکست</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84141" target="_blank">📅 18:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84140">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNo happy</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0tY0SQTrsmwIiEemmjQj8TEm1rWJde1lZ4GPp_Z_PW6wjXnaVdDL1KSmgaoHapoSBhfoXBrE2JMUOud2nYgToBnevylYXBp076AWW-W1opjGjXjmWKlFreTuZslXIztGA-cB6S-3FmmcI3hw0fxhttcS2Q20itqFeH1_eRa-Pf63VIgp-3vu67UpWDwHSI1x3U2yRr0IN3Zl6NOGUaTny4axW5IhPP8m0p8Vp4eSTz6pWNmIyJAl9eYQnu8M5sRCaGrrdOZOrjWRM-fpaUfy0ZRWSKbRcGEup-Awmp7GSggTtWG63M5OTqcCo5GAkUNa8G_J1Z5gZP9jCX0C4YyPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلم مهدی رسیدددددد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84140" target="_blank">📅 18:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84139">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مجتبی خامنه ای: امروزه، برخی ما را به عنوان چهارمین ابرقدرت جهان معرفی می‌کنند. البته، آن‌ها این را بر اساس محاسبات دنیوی می‌گویند.  اما از نظر محاسبات الهی، ما به عنوان قدرتمندترین کشور جهان شناخته می‌شویم   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84139" target="_blank">📅 18:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84137">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مجتبی خامنه ای:
امروزه، برخی ما را به عنوان چهارمین ابرقدرت جهان معرفی می‌کنند. البته، آن‌ها این را بر اساس محاسبات دنیوی می‌گویند.
اما از نظر محاسبات الهی، ما به عنوان قدرتمندترین کشور جهان شناخته می‌شویم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84137" target="_blank">📅 17:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84136">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f73abc8dd.mp4?token=HxOpxUAa_rtiBz6STcTq6wHGY2_FNpGfN-Saxk5BquVdfK5KEi5N_mKzzS86zyRNIv_5nX9pJI9BLMExVnu-T-Vp5G1I4Ao0yCRTQU0Ain97yUHT6N71f1yTBtZ26xMg0kaVz80uKovB3i4ZacY8jrOV6fiSUhdDuGq_1u_trh-MQQRzjEsR7lswWhIPSwgYRaUovxme8-_RnfdVdRROVqndEc_LlD2d0XfuwsfOXOZ6RZDeKfCdKjxMFHtil5O-yLoJLROQU4W7th3uiAq0_ZHrj6MkNJJP7Cmq5CyEaMRMPBJhcqMEgIZ39r2F4Xcr0yR8ZMjAF47NHQg5uN9T8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f73abc8dd.mp4?token=HxOpxUAa_rtiBz6STcTq6wHGY2_FNpGfN-Saxk5BquVdfK5KEi5N_mKzzS86zyRNIv_5nX9pJI9BLMExVnu-T-Vp5G1I4Ao0yCRTQU0Ain97yUHT6N71f1yTBtZ26xMg0kaVz80uKovB3i4ZacY8jrOV6fiSUhdDuGq_1u_trh-MQQRzjEsR7lswWhIPSwgYRaUovxme8-_RnfdVdRROVqndEc_LlD2d0XfuwsfOXOZ6RZDeKfCdKjxMFHtil5O-yLoJLROQU4W7th3uiAq0_ZHrj6MkNJJP7Cmq5CyEaMRMPBJhcqMEgIZ39r2F4Xcr0yR8ZMjAF47NHQg5uN9T8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پول دونیته ها
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84136" target="_blank">📅 17:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84135">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">۶ تا F35 دیگه جهت استحکام سازی پایه های مذاکرات از آمریکا به خاورمیانه اعزام شدن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84135" target="_blank">📅 17:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84134">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دلار ۲۴۵
ترکوندی مذاکره، عالی بودی مذاکره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84134" target="_blank">📅 16:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84133">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">استاد بیژن مرتضوی اعلام کرد که نه بابا ایران کجا بود و نمی‌خوام حتی یک نت از موسیقی من... و از این حرفا.
ولی خبرنگاری که امروز صبح خبر برگشت استاد رو منتشر کرده بود خیلی اصرار داره که استاد همون‌جوری که تو اجرای جام‌جهانی تونست خیلی خفن بین جمعیت پنهان بشه، الان هم داره خیلی خوب پنهان کاری می‌کنه و همین خبرنگاره قراره ساعت ۹ شب یه سری عکس و سند از استاد پخش کنه که ثابت می‌کنن استاد ایرانه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84133" target="_blank">📅 16:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84132">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZphRnGdxtJvfYaXaq1FUtIgVjTSqWph8VaMYY9_G6M_gw1MF-CoS3IxlPRNrcracCHoaZeRU20kEOzC-1JpQXmLvceo28jQblCYzJJ4koZXb1ydKQCek8MyyxEPpXkpREXKmPySB7wVh0NeZ_1BL85X6HZDI6F8ruSsaLNBKeYJ0FfPIIbq15j89cyuMzLxd1JbphO4m5g7RL2-1L6P3_ku4lTaEzb7CDAJtL0Mf90edPlCVFIpcjc3iddzFVa5aKbhbqgCYD7H3FHHEPNQcE8sgUuKTkFsObTu0W-G3XiZzHJsbe-AxCcGzlerFwiroClrfp_HZiwZsvTLfpvk8Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم کشوری که ای کیو چهارم جهان هست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84132" target="_blank">📅 15:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84130">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">به نمایندگی خبرنگاری فان هیپ هاپ سه نفر اول به این بازیکن ها رای دادم
1 بلینگهام
2 مسی
3 کواراتسخلیا</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84130" target="_blank">📅 15:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84129">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee4b03712b.mp4?token=NBlaYedZaGk73GAaVJS8NdhkKKfTCdYbscLBRgFIahQ0ZV3uR9MLoTleyA7APNIFjeiCRXWgT-gHtuR0xTdc_Jpk8O6LZhTpxhqolRlrmvKMdf1hJBuik_kb-L2HyaZMVO2eVyi8nq9j0vOLpeId_I8vwod2hvV3IUwdUesNIKy4vMiJMudzAUsppLGwv0Zezf3YIAJH-zVKJqIIocVv7Hsb3e1ayOYE-4Yc4AmjPldlegGFAkcFkyaH0LRG-GDT4chulqZoAbTdWLulTU20ZKgJ4S8JKeAPbh7XxtAECnh_QFAFyCI5Bla6xTYCl_3na8BYjQoKHdchHagbL2EzNhLvBBVpCx4E_3HP1psHxsGOqRMibR_k9AmEP0JZQ6MKi-i3DvcfmdkEJCVX3qr8i3qRFWG7hFIqwFVm9UQSS_EYph3xqxWS832O-fQXy7s2FH_u1E5Woj1XI5ZQT9hy4nffdGUQQa8NaeHwNIFEeyYVsEQ4sZnXgFSGdGMVSKB0XXKLUJw8-OTZPbNq6xWCopuR-CLU0VUkab4Qa4xEUBBwieDBt3dzKXazEpLPLC53fn0GqUm_e8yKB-9gra9l-OyRZzTybGTuukPHvDYswAeHl8cIJtn_wf1lyv3eqkj2EH7WTXRjUIqeCUOEWEKlfb-y3n7Tyb-2LCzt0ugBrSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee4b03712b.mp4?token=NBlaYedZaGk73GAaVJS8NdhkKKfTCdYbscLBRgFIahQ0ZV3uR9MLoTleyA7APNIFjeiCRXWgT-gHtuR0xTdc_Jpk8O6LZhTpxhqolRlrmvKMdf1hJBuik_kb-L2HyaZMVO2eVyi8nq9j0vOLpeId_I8vwod2hvV3IUwdUesNIKy4vMiJMudzAUsppLGwv0Zezf3YIAJH-zVKJqIIocVv7Hsb3e1ayOYE-4Yc4AmjPldlegGFAkcFkyaH0LRG-GDT4chulqZoAbTdWLulTU20ZKgJ4S8JKeAPbh7XxtAECnh_QFAFyCI5Bla6xTYCl_3na8BYjQoKHdchHagbL2EzNhLvBBVpCx4E_3HP1psHxsGOqRMibR_k9AmEP0JZQ6MKi-i3DvcfmdkEJCVX3qr8i3qRFWG7hFIqwFVm9UQSS_EYph3xqxWS832O-fQXy7s2FH_u1E5Woj1XI5ZQT9hy4nffdGUQQa8NaeHwNIFEeyYVsEQ4sZnXgFSGdGMVSKB0XXKLUJw8-OTZPbNq6xWCopuR-CLU0VUkab4Qa4xEUBBwieDBt3dzKXazEpLPLC53fn0GqUm_e8yKB-9gra9l-OyRZzTybGTuukPHvDYswAeHl8cIJtn_wf1lyv3eqkj2EH7WTXRjUIqeCUOEWEKlfb-y3n7Tyb-2LCzt0ugBrSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رای گیری توپ طلا هم تموم شده ۴ ابان برنده رو اعلام میکنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84129" target="_blank">📅 15:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84128">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-uzh2QbgICb7ZnyU7aptEBW7AA5et6zrJHrfY_xNZO1-rqw0md6RNlaTSglrBVDFUKXr-EIEP-HkSEsyUqSF-cVQnTAh9aGVIjALYwl9plgjv-8_KUQI5tfQ1RTmDLK2GuU83bD8uTWsEAY23B9hJnZ3Wof59EJbMtXzvCxUfkm20eXPD-uuhbgyflyenhNhht6nxVemc4s-KgquOIIVOg-MdV4Pc-RoM2lcfxvXeOrwxR6msaIpNvLMyyesT1mzTXzk4JXWRHXRD6DEPdVpXsy8_i1C7K-KAntWvdFJPZFNewgKnJjIATaqAt6iY7ljDhVOVUW9sVeQUeMxvMrUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما که راضی هستیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84128" target="_blank">📅 14:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84127">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e988dd3baa.mp4?token=HhxttuGhtH40Z6WUeXegj-gN3ny5HkQpt88u-0j13nd3OmKWSGHO3mz2LA4dQlPW7wRbszKOtsbObToHbDnsH4v8xB59y1SGUUswSdtuMm7aNBrn9gWKYhCsem1m-KVibWbgELjJovknUFWWyiI7C6kKjkVQ1fuDSsfotEk5tMFXzLEkqgNAX355wAGwbgigVc53-JeEKj_Xina-tkW1gCeVuKwlW8oMqlDqexitpia9tj54SMCBeixmENJmcVGknu__CTXQCDE3ei14cOMf3S3a4dE4ss1JI5DI77_0_BE-kVMYOWe-vh43vMW5yAV8FIB0UKxUta1TxaFBZDGbDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988dd3baa.mp4?token=HhxttuGhtH40Z6WUeXegj-gN3ny5HkQpt88u-0j13nd3OmKWSGHO3mz2LA4dQlPW7wRbszKOtsbObToHbDnsH4v8xB59y1SGUUswSdtuMm7aNBrn9gWKYhCsem1m-KVibWbgELjJovknUFWWyiI7C6kKjkVQ1fuDSsfotEk5tMFXzLEkqgNAX355wAGwbgigVc53-JeEKj_Xina-tkW1gCeVuKwlW8oMqlDqexitpia9tj54SMCBeixmENJmcVGknu__CTXQCDE3ei14cOMf3S3a4dE4ss1JI5DI77_0_BE-kVMYOWe-vh43vMW5yAV8FIB0UKxUta1TxaFBZDGbDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش امین تیجی به گل کاشته‌ی دیشب مسی و فحاشی ناموسی وی به کیرستانو رونالدو
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84127" target="_blank">📅 13:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84126">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSHmwty01cQ3GVamw1b1RB_k1HayTvNOEx5_m6z_pWvQihvfhBcFhRPSlybFOq6SwtifQCex_wsKrxxaTBzOZsMbZHatKXhFxyTkeAQsdFlna1YlaYVOzI9OjMjEPhS-amOE2fzlXE1Z0w8Mnkh9cSFP02S6Fqnwukfx9remh5BkO4PwSF_gxc3uFnGMQZeF7t9WPFjI2xMBJbVTWV1XyX2kz6mJMxlBedE6LE4OSdsndmmYTMyj7j6RixRrIDbXf9ppujiLawYKtlkLYHAHc-79tpEC2PcP-44q1C8KAOfvWIrKsoojqbFF0lse7KB-c425x0bGkW-H-1kwITiHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخجون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84126" target="_blank">📅 13:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84124">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e46577007d.mp4?token=bCfPsubdu278zoUN94Zykcuk14XLRLWQJVdd1pBk7CXGZdIRP1hQfr1hn6V6dY1EGkLAjv4g0si-0SKaKh_YFIlKys4ebJZwExGBsAhB395Npmv7aWa32LcGIbkT_MIUKm9g97TfKnrcuVMXQgye0uHDGQZF4rPZL6PJa1AOTPYKerAOj9gK0wtbdMLjTvEqsltSMXnZEQqGIwNkKoWOyRwC2h0U21A0vufEA3WcWhhGaf-ma2M9Eay7tfEJNhtNwxR_FpPmiCWNCXD07TldDB8RaYlg9AJGTzOyxeERdN0WoA5QohFUJ3VC8rOCPk1LLf-GH0VEgg2xzyQpsyrJdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e46577007d.mp4?token=bCfPsubdu278zoUN94Zykcuk14XLRLWQJVdd1pBk7CXGZdIRP1hQfr1hn6V6dY1EGkLAjv4g0si-0SKaKh_YFIlKys4ebJZwExGBsAhB395Npmv7aWa32LcGIbkT_MIUKm9g97TfKnrcuVMXQgye0uHDGQZF4rPZL6PJa1AOTPYKerAOj9gK0wtbdMLjTvEqsltSMXnZEQqGIwNkKoWOyRwC2h0U21A0vufEA3WcWhhGaf-ma2M9Eay7tfEJNhtNwxR_FpPmiCWNCXD07TldDB8RaYlg9AJGTzOyxeERdN0WoA5QohFUJ3VC8rOCPk1LLf-GH0VEgg2xzyQpsyrJdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوس دخترای چرسی و تیجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84124" target="_blank">📅 13:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84123">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=jwG5jL_8xDDB-wPXskPnq5LC-kMN4kEIf81lY919JqG248xADHLkHbDoSIQl24breKJeAcNCDe4ZIKPJiA1TCpvKvKzX7WNlzpMBYmpvSbJuUU95EJ1WpHJETP43I25mwH8VQk_QaPAqqk0IPASDu4q2wx1zf6pLbYHfRl4ZR8kg5vFfrT85MGJ3yK_e9GCJ2TwZ6IxWYSMUbJNQFFksSWaIlpttMZjHDssxU0DwYvEjfEJObj7IK9tN4E3F-PV-3AMZrTEOfEMitJ6fv1nLFNmhwGqWq15FGPggxS3iac_Uc5KnKMbpsjUUlFMJT0Q_630qYrAguqGB41LhIeN64g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=jwG5jL_8xDDB-wPXskPnq5LC-kMN4kEIf81lY919JqG248xADHLkHbDoSIQl24breKJeAcNCDe4ZIKPJiA1TCpvKvKzX7WNlzpMBYmpvSbJuUU95EJ1WpHJETP43I25mwH8VQk_QaPAqqk0IPASDu4q2wx1zf6pLbYHfRl4ZR8kg5vFfrT85MGJ3yK_e9GCJ2TwZ6IxWYSMUbJNQFFksSWaIlpttMZjHDssxU0DwYvEjfEJObj7IK9tN4E3F-PV-3AMZrTEOfEMitJ6fv1nLFNmhwGqWq15FGPggxS3iac_Uc5KnKMbpsjUUlFMJT0Q_630qYrAguqGB41LhIeN64g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از ۵۰۰ بیلبورد دیجیتال در خیابان های منهتن نیویورک خطرات ایران هسته ای رو نشون میدن،
احتمالا این اقدام برای آماده سازی افکار عمومی و برای شروع یه جنگ بزرگ صورت گرفته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84123" target="_blank">📅 13:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84122">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ناو هواپیمابر یو اس اس تئودور روزولت CVN-71 راهی خاورمیانه شد
تئودور روزولت قرار است جایگزین ناو هواپیمابر یواس‌اس جورج واشنگتن شود. مدت این استقرار بیش از ۷ ماه پیش‌بینی شده و خدمه برای مأموریتی طولانی‌تر از حد معمول آماده شده‌اند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84122" target="_blank">📅 13:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84121">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwAFJFNYDg6WJjPqSncVZ5BmnqKFue5_-EDdSPJamKtWLOJk_LwdPkl-dvjIbuGKbOw2EtrQBe_Z3d-bY7jZSLYIshU5XPepoY2a1Z7wMvEl2hZk95Zu3f4bJTSN2O6n5CLxEnoGDOLCg6W8KmKlvYU4ggCHYaGimgkTLUwnzS6-dua_pKmMiNCt6NwyoDKZtJlyQ-slKQhuC35biAqxOIn84WV0xCu3fzNwpY915PH_BGstiS5F-H1Qw5lnYZge51sXEkmtk9uWAWioO_v8Jebx6ab9NemdnOdTVLTWKfQwH5ulraanL9MZ2KlrryQXb89TXCqM6FDI72USlXB66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوی جنگ میاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84121" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84118">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حتی تصور نوازندگی بی‌نظیر و پشت صحنه‌ی استاد بیژن مرتضوی تو کنسرت مشترک استاد نامجو و قیصر با حضور افتخاری مینا نامداری، چشمام رو اکلیلی می‌کنه.
🥹
🫠
همیشه می‌دونستم آقای پزشکیان از خودمونه
❤️
#فرق_می‌کنه_کی_رئیس‌جمهور_باشه
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84118" target="_blank">📅 12:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84117">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3_lHCjKYtZzd7qWqvlo1yd9F9I8Do73o7Tr30-GMyoH9lQR95gZkuMRxkp5bZtsqxh5wLXjdBBIkaO_2cNFDFazMnhddyjmXynfOnxACyl0AUdvev-qGN-6ucdJSzr5P5yvl2US5CZLXmgG6MDXiKj9iDZUMvXm_LqR5_N7Iw-tVVjrjh6OADdwM82JVXqq9pOT-TP30Tl1p7sbF44CtpAac5sH--PeYuOq0Gct8fllzHj8-BWL1aMwPV7egcKVJS1k4p9KFjXL5QfIsYjdQK9OzlBJemrmjChgBKtwiwMvd6DDoVpVDIDkl15nZ6dXm4K6P8bS7ZEBCokDKgHwHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری و حمایت هیپ‌هاپولوژیست از کنسرت اخیر بیگ‌شگی که خبر از احتمال همکاری این دو نفر در آینده‌ای نزدیک می‌دهد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84117" target="_blank">📅 11:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84116">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUammC28xBzYU3f4I54FB1P_h3gXFh3Aqf33poiYLUcFj99vc-aVkbSmUZCY_DoaKZ_pVGYNgBF52_Z4NUtst2XG5hcrQfHBoGvbBFcA58S6fAcsdsUA1PvFgSLk4FEuXREsR2ou_l-ElcIPaWJg9sbap2LxzKa0ODmodmenxnH9O6yUzXArPgEkh8F89JszwBgTOvnql2pGOM0fSO8EqZ7uEggwZfJvE63a4OKu8Psgm--v4X_rnoqp3UXUsRuVE2xmSkoE6QSCRZr9waAzXtqgsWanGuVaO9HtSoW5Ou1-oOo1-joV-B9kbGf7ZMIvMEqGalitmOe63s-WgzwZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که نگران مهاجرتشون هستند ذره‌ای نگران نباشند و گول تبلیغات رسانه‌ای دشمنان رو هم نخورند.
دریای خزر هنوز با پذیرش خطرات کاملا احتمالی تقریبا باز هستش.
در کنار کلاس‌های آیلتس و تافل و خوردن ۸ لیوان آب و قوز نکردن، کلاس شنا رو هم با جدیت پیگیری باشید به زودی تورهای فرار و استتار در اعماق خزر با امکانات و قیمت‌های ویژه موجود میشه می‌تونید بدون محدودیت شرکت کنید.
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84116" target="_blank">📅 11:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84115">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ناو هواپیمابر تئودور روزولت آمریکا هم پس از نهایی شدن مراحل آماده‌سازی راهی خاورمیانه شد تا نشون بده دکتر عراقچی حتی تو نیویورک هم با تعهد کاری و تکنیکال عمل می‌کنه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84115" target="_blank">📅 10:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84114">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7_eOdWPnueqVWTJPdvEfZeRTLon9MWOQtWTOhTWFxO96mhQ3VcEu8y3Gphb_E4bdsESk4MGSlC241hE6taW4UftYTY7YTAL55SQPEr9Ix6JU8si3-SWZDTR-2MtibwBuTw1LyxDj6UfDL6gmnpsyOqQAwukZpdUApUKtnWzcZSfqGRfoqRZNpJpIiZQ18n1ci33bFCB7RQjF3KgAFNczNjBbzi7s8kpr_lsEE5k_R7dGtoEbdxB6Iyt-nvh6DabmNO-LG2ytcQtHzDRqc5o0yGo5pKBGC8YBjE7jihcuj6Estp_kTl9cUTWMhekB8ri6ZJrGKSPvYxW8rUTSWihXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر حیف شد وارد مارکت ترکیه نشدی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84114" target="_blank">📅 01:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84112">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سلام بیایید چنلم
https://t.me/+q5Ml6Hl1Af5lMTI0</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84112" target="_blank">📅 00:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84110">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f7eiK8jUODZonKFFqhlvfAmKgt8W_-DyPW547O8RmZFVwSsiKtBAmekZAQaVjnUCTLdu-q1XFG5SiFKU7ta8m8U5yO3XtAaGRZPHtmZejT7e4z79DbE1EyB1na2li_PzOP5rMwVFQjjARqtq4FMBh-eZMi-qM7XjKTHy3zOaExlusSmJJoCTtZ-laTY0VQELHhY6qECZ8qEJ20n9bfqhcxUjJVIxNQ5mbajdl7SJKa643ThA19ZUzRtltnWwiEVkRqHozut3IZoaSuY4_uz4G_JWDIy1AG8xQIi2X0lht4Sp9m7GpzhVqCJ6jDvaEdyZ9yLc7MkDLIqdQtqtVrC1Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iqt7UUckG8Ab_oprkUaRrsXDbF5ZYV3sbdXtrvGgEHCS7h7dCdq8DjZp1ypvP_6j7gdBzeBJzed3bstR1zG-i_C4jcXZgD0u5gZ-B-z8uEDI4NVg8MSPs0sHWnJZAZRkGgBy8uQe0NZ6VcFzc4-tqjdIr3T47x6j_NGYRREEhT5xMyjSKh8tP5c1QyVF2eyLUQr2Rkjeyu60emWt4Mk22tEu0P4A9d6caUY_BHrXFs-nG9zCzMAcuo-opaXaK3Lj0OHsbwVgvSAIUIGbWUExickbi5i1zJ5bTVx7iR57F_eLYPeNAupZk8hHLqtkvZsqHfEpYJJU_2nGLHyYzma_Aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به مناسبت شاتای جدید سیدنی سوئینی موافقید کیری اورریتده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/84110" target="_blank">📅 23:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84109">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yb5EG8fSNjHbmcjPOXgXeIvhI5XNZkuOT1sz0ZC8UFOp17guu9Y5XcJ40VbxegO3_QLe4rqgT1rQze6W3h3hO1O9MoBXMcC2nVu4hxEYO0zjl3THjNLxbYgvcXsdwTdDh1yRzV9UOlKSrQ8Db_DNy0Tgaj3v7MHpFmVNKV0pBdJHN5EX3okjGzIi31wUUr4ka-pnZupp0dzWKGBWj8u9DwQfTulfoFHZHb3YCyND6sTAzsmzKbl2ztBWAN9qypsVUepIVTFVTb-RjgRe2ttJq0lV4sAV1HhAEPBaUNFrtIC-yGuC3sV_R3F8AD0cvbFKFsxxy2hPlMZm2LGJNzwjLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشبینی ایلان ماسک از آینده‌ هوش مصنوعی:
2029: ربات های اپتیموس از بهترین جراحان جهان پیشی میگیرند.
2030: هوش مصنوعی از هوش ترکیبی تمام بشریت پیشی میگیرد.
2031: ربات های انسان نما از صد میلیون فراتر میرود.
2032: اقتصاد جهان دوبرابر میشود.
2035: درآمد تضمین شده بدون نیاز به کار کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84109" target="_blank">📅 22:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84105">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">عراقچی:
غنی‌سازی ۶۰٪ غیرقانونی نیست و برای اهداف صلح‌آمیزه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84105" target="_blank">📅 21:21 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
