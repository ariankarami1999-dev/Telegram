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
<img src="https://cdn4.telesco.pe/file/KTCIgV_x2mu-Q8PkexSb_7PT62D8pPPw8clpksNsW4dGuMwta6MLaUn-RMqUyyNV_CsiizrSIj1Og9XCkOHzF1es4D2U5XVBHftJypHVvtnvXOkLooDHP6KC6oq7RM2FOFvJWW2FgiBJhSiY_YPM_gk0Mb432sWvBkQC8RtVprqPAi7gf8sgm6AT9reQFu1sYBPksnaa_Fb-1oGLAjiJbAljYPdMKLAiQ9qdla-kf-LOXekAHVA5S60IgIlWIWtJ3gm0LIxlkTMo2OvAo5lmrcHNLCnKf4Fd4UCleptLYYXr0eQDef5F2WcwfFKqaqJOsXYCmrNIwPeQgU6_bdEpWw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 14:07:21</div>
<hr>

<div class="tg-post" id="msg-83097">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ویس جدید علی دایی و کیره خر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/funhiphop/83097" target="_blank">📅 13:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83096">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ویس علی دایی و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/funhiphop/83096" target="_blank">📅 13:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83095">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2b3362cd.mp4?token=hYEjlHzHPwel6_OpVaTTPZgHgndT8-vC3Ttl2IGBhFpzNNLTpLA2-3ilaf5gNir9hwfpeHfAF1rQJeQepJtlIrq6m5AYbLKLdJKSCf_c0r_OzRHpCb2c0A7BgLpffjK4WOCrCB5-MlUZL5rTYWHJT0SIRBnAiyhAn6Q4t_jqAMoHlanlZnMX1G0LniR3dCJK0y5xeLx8oHsSEU0G4ICVVCU6XYqM-uS2fkLZFPYFlh6RYvJluugQREFW7KdWQGSEIQRw6QwCRceZ6Vobg5DeEjS_KRk7z8514EPvnzl5tG9TzlsLWmCW1ZrLlTh-pdQWFO0DpVs7pDicyj9WJ0kzKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2b3362cd.mp4?token=hYEjlHzHPwel6_OpVaTTPZgHgndT8-vC3Ttl2IGBhFpzNNLTpLA2-3ilaf5gNir9hwfpeHfAF1rQJeQepJtlIrq6m5AYbLKLdJKSCf_c0r_OzRHpCb2c0A7BgLpffjK4WOCrCB5-MlUZL5rTYWHJT0SIRBnAiyhAn6Q4t_jqAMoHlanlZnMX1G0LniR3dCJK0y5xeLx8oHsSEU0G4ICVVCU6XYqM-uS2fkLZFPYFlh6RYvJluugQREFW7KdWQGSEIQRw6QwCRceZ6Vobg5DeEjS_KRk7z8514EPvnzl5tG9TzlsLWmCW1ZrLlTh-pdQWFO0DpVs7pDicyj9WJ0kzKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/funhiphop/83095" target="_blank">📅 13:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83094">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رپر عزیزی که دندوناتو طلا میکنی و میای تو خایه های دوربین باهاش فلکس میکنی و به دشمن فرضیت فحش میدی
بخدا نه تو ترویس اسکاتی نه اینجا آمریکاس، بزار درتو</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/funhiphop/83094" target="_blank">📅 11:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83093">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v016_xE2WzqL0a683DkACGNlfMEBNybfgYV71brpgIbdfSOciWekZoe4QOgVseOJjQcWcqp8J9d2vaQBco2F_fmmdOCRqany0FCvaagaXyAFCKMtOfQHrCujCLgK4qeC8D-4VjyCOMvHnu4GhdD0bVlXxHk-zEnKHifUNkLZzDay5NlGllxTv7lt3_YzyANExsH3fTDxhIPb-0b22tOGBUYR2CCWL1Kh1Jy-jQ-ThLoenx5eq6a1YdPyafzELnqUDq2y7ogJraxaCg1JTVA-XeyNgZ3DrjUaKOy4S1nulG3lINK-GgPyNGxZwDo0q8DNz1KtHSqXZ0dTfp8USCjLQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد عوارض تنگه ما چیشد استاد ما رو پولش حساب کرده بودیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/funhiphop/83093" target="_blank">📅 11:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83092">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">#پست_دارای_محتوای_نیمه_رپی  شاه کهکشان راه شیری فتوا صادر کرد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/funhiphop/83092" target="_blank">📅 11:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83091">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vja_UEDASpkQLUl8l-rISH59hWXvUm-aSbPhI2-8g1sJSawT_Mjnm3nlP3oq1PkrEHK_XJvgx21IMVgQp3kw2hb8sXW4OwLvXK02UaequFu98Ph2OCotxrESPMGd30QBugQZlZ8T3Cv8_wICZ_JCuPzZzFF-YCQJRt7Hx3ZAaYq0EY4f5MCSM-pet0phjVMVTAwt5lorSrPwwxKuMH73yfdH0yiRK7Q5GFw8LSCzCLjK_3V6ealCYfnnv_MDiwqldrXgUK9_Yft_XMkk4rL_QDvot2vNbDFP2oddF0nd6a7BDy1XsB4yf5-e-Xat4EBOLUFO8B_Th5fxRFxco-SWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پوتک به نام TiKToK منتشر شد
YouTube
SoundCloud
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/funhiphop/83091" target="_blank">📅 11:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83090">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/funhiphop/83090" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
اپلیکیشن حرفه ای اندروید کمپانی بین المللی وی پاری
🔥
💖
امکان شارژ از طریق کارت بانکی
💖
تسویه حساب سریع بدون احراز
💖
دارای مجوز رسمی Anjuan وcuracao
🫣
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا، ترکیه و...
✅
کانال تلگرام:
👇
💖
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/funhiphop/83090" target="_blank">📅 11:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83089">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJj6xLuRr6Z-pDs3bfuM9RG07VFCroDVA63gjTKKGWMaBhojWcpVLjzRdy8I9-TJ0Qn8VvRYVCaahN9o0aU7dKckY4oXdJpFFXBJhjwMLWwqc5hguQodo1ccoVdD1yu5HBUAvGEK8ZmSsAMShuTZ9TC-2XpWOu0pCUimwccjt2m9nPnMSwEDN_4KKlRdbSaLSlq5HNDjNVZERPpX5PpMG7zMW8TP91Q8kHgGZD3ecY4IIit0oInJgnuTgp-E86VS7a8k0uJ6wePXC9h5X6YgAD84IwoKqR6O7w8t-zAD0MiUdMdc-8ynnnrHMq2BkcmTYyg_GLbOyOlBV3yqijNL_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرط بندی با سایت بین المللی تجربه کنید
🔥
🥇
سایت شماره یک اروپا حالا در ایران
🥇
😀
😃
😄
😁
🎁
واریز اول
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز دوم
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز سوم
💖
75% بونوس هدیه
🎁
واریز چهارم
💖
50% بونوس هدیه
💌
کد هدیه ثبت نام: GG007
ادرس سایت:
🤔
http://til.ac/z5jcpGT
💎
کانال اطلاع رسانی ایران:r16
🅰
✉️
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/funhiphop/83089" target="_blank">📅 11:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83088">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tobI20tTQx7j5TV5V7wEESP8FWkSfFY3GIuOL93KhzhKz72p61MYRrI34W7--bo3m2crnt7TwJbyHt_9rkUVMKZkhqkjmTSqlStTLFp9VJs2d-yi9oap8dTOU4dVTA_EE9yWQPNyrDAMZDSZgVy-9HKxigw3ftMzmDGBI7qjADjFKuzLulpDaAJUbQM9KTbG0NjDQ28jG6om_L8DIgxTlZCIKo0TfO5ssYxNTpQ4F9n5A8OmxaRq-eK7qiYqfrd5zqvQn23Nn2jHCu4skYUYHkDOI4D0pjdpZZEJQB6F8j7_dpbwazLPzUxEw3o0mlw3nTzUbjE1Kc1tARMPZjHhwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پست_دارای_محتوای_نیمه_رپی
شاه کهکشان راه شیری فتوا صادر کرد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/funhiphop/83088" target="_blank">📅 11:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83087">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLFtPDcf2Xn6NeKtKzFfzKxQ1dij5KdZth1EmuiGyT8CdIKIK5eo2rOHOE5PToSoL3CPVsFgX0h1Hi_Y4v9-uc9xukqNbYZ3G9QoLIre3HY5A6i1_HyDCQ2gBSTex_Pl9o7NxbSkW9xfQXCWy_ochhuO94BUpUEO4lKxoiGonjrOFVEpqHhGa3eVaVRnREChrFLAiuRbhZsyn5blACCT6FzPjPp5puvIq1oLZ8BXIL__7gd1Bjxk-Jvg9aV3i6PXsNjnhvEfkRnttXGHRpK5oJUQwMMU58Y-0B0sCVZi48NEqkcstWskYXsmA7b0s3NfClIoXR5m84xpRwapcFEojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحتون به زیبایی و درخشندگی این تصویر
❤️
😍
😘
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/funhiphop/83087" target="_blank">📅 08:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83086">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مثل همیشه درست وقتی بهترین املت زندگیمو زدم فهمیدم نون نداریم</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/83086" target="_blank">📅 03:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83085">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اگه ناراحتی قلبی دارید یا با دیدن صحنه های حساس حالتون خراب میشه ویدیو رو باز نکنید  یک جوون تو همدان به دلیل مشکلات معیشتی خودشو آتش زد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83085" target="_blank">📅 00:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83084">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56316020cf.mp4?token=GkXggZdbn-lRzVLlMbHJnyQ6yy1Wiov5gz1Ut9XG3uQSN1dEv3MdC_hjpf2wnVEh_CCV-J_7A6kGrubhdt4VrZJ7AVDPnBzbU7Nl5oMPIcWzQMN1jQrn7XmCzhIihD7fydDkBfs64PpnoNPtZwj36vspKD2hB5aPKoiVqD-C7oIkYGl9zvP32wFSsdF06OZ8Cz2k15ztVqbeTTik5hfjgIMa3Xa8EO2kr-HsmnVZli8setYVlfu8pt5BrylUv9bTmWtUfdQ-PBhnAlYZGoWUKU_L1ldu9DVVWnnb9ggZ62FpZA-KDUJE_PmWv8XYj7u2NBF6UcSd8ljsKZsffNx2Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56316020cf.mp4?token=GkXggZdbn-lRzVLlMbHJnyQ6yy1Wiov5gz1Ut9XG3uQSN1dEv3MdC_hjpf2wnVEh_CCV-J_7A6kGrubhdt4VrZJ7AVDPnBzbU7Nl5oMPIcWzQMN1jQrn7XmCzhIihD7fydDkBfs64PpnoNPtZwj36vspKD2hB5aPKoiVqD-C7oIkYGl9zvP32wFSsdF06OZ8Cz2k15ztVqbeTTik5hfjgIMa3Xa8EO2kr-HsmnVZli8setYVlfu8pt5BrylUv9bTmWtUfdQ-PBhnAlYZGoWUKU_L1ldu9DVVWnnb9ggZ62FpZA-KDUJE_PmWv8XYj7u2NBF6UcSd8ljsKZsffNx2Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه ناراحتی قلبی دارید یا با دیدن صحنه های حساس حالتون خراب میشه ویدیو رو باز نکنید
یک جوون تو همدان به دلیل مشکلات معیشتی خودشو آتش زد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83084" target="_blank">📅 00:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83083">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrCLzbm0vjfUvmGlcoPEqPgbwSDbCsE-3rSHP0L9ivHqAq5Fcw63jhY_tu2ANo9YitEhI_09NDRS3sL7P3AYBEVTCNFhNUU-zvBUI6gi2DgndYoMgOhbOOzLuoIc0p1H0x_-kAj2uC9e5LBiTuVDcwSeyZEufGW6bYxZd2JhnV2hjoI2qYevY1-ojJaK8LIiFby6ucjwc8Bk_QUbtgMdDYOTsSkerXu2Y68DsSKixxymgvZEwB9dMRAD41M0B4bvOSX-bd15ppQx5B-_Gt3DdvDN2k7FJcEes-Str7KJeDv_jJSNT4TX8f3dQGykTD5kDF2pUvKceJVUBlysIu4ExQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به ک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83083" target="_blank">📅 23:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83079">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ImjA3lgJLrjW3Mm0IwlCV7E770U5U7oRztNGyIsisK6fK-L1BIvbAMU13jNSc0b7XmWarRBZaIae2agF_wdjeknoZbNEW6X-17F-RHCzgiJAVdY2emysPKXBhIj6TfJh_M8qixxFLwe3wmB4RtPyoGlFoR3y6ku1s5Jqo3W9Wusob9cPoB5j9dDZY0U9b3uvaOF4e1mKavNtNNb6ePIK0JRLh1hPJbjgkkJkl0MzbwENL5yqwSZyfBGehqTep4I4y2eBB0qKA8xBBhavysXcitZGF01Ov-oA351BNN4tJQZx1qLq26132wq-D1m5VVEpr7l88XYCsli7N31fns8PRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQjyOsBjsI0b63l3Xx6UDUs8Hdn28PLwmwf5_m2DmrzW1vu7u-gPCONZaltH-zSvp0rhvSTemD1l6xAropDKdI-9zZ1HU17UBVpmZA7tIGF1nMXEdYyiy7n1Kb-W64LS9r38UBvjiQK7mIMfrSozau94KV_A6WDu0GAXAPOL_jOg6Fs3XLCoPEqwEb7IElE3LqPPyz6Zj1WtxrpziNx1L86z1CphmJu2FucU_tTr2zLSVoP6pxDLpdDPpd1j9PGCVN8DOAX01v6yA4sSfsdeYnZ-DXsz-cXbYZBpDiIli_SVIwUj-PLPmEeQrCIpV4M_oxSA3ejSuTCwXsGlplXk1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKJuwSXng0B1MyJyW8FsEWatMzbF2t0eLIWMvETaDOGe5-i9DTwOQB7wvYudI0Tz5AMpV87Kh8ALtMclDZAt_TLHLZG2wNncRhR4ZBfhcIsWAzRPq2nPy7CMmJDekdYIoTle3eWraA3RI7QyBAFhcNs7Q_QYuYBc12bGoQVK1hP9KvmyD7cotiycQoRPW601g6QaFEZ6eDdBX42C8XiqLWKG7TuXyOZvNfzF8XBm5g_wjaUrnZ32LC4lH84dMqaC25ZJgxVeWNwexg2wOkAX7HzhKkXfYGpXa_cItTI6UqTTs0cWL908ibcCDmGPaimImUrIU6LEx5c1faJxeE9APg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSy0SABD_jabKAxcUOVbxzZ7YPQ9PaKewCNPhSKrejY_k91mz6cxzgFBakbZz4gBktYyqf2VDPQtsPrE5PMWeAj5FWwTm8A3auk9TEPvXaFCEByn4eTuyACX3IMNLJG2Tm7PzA-1WASV5Qr7-tp_gwywoNb_57c6aRjBjHPCqUIr41v48nfkEuNqPYOqhFKdGewvymMznnGlM3a7gmQHqyx9AHNjjY8Cpl9vIFSDgsRn8bkHHFGYEEUSlvOA2HOlQ6FRBENUTD9h_inJv57Dycx6brAzFutUzuEiMMo9ElRL_yW1iWzHnFSKloqVEUktS40z10WI79AK8yymyi_Xzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صد رحمت به سلامت‌روان دوست‌دختر تلخون.  ترجمه:
ماه مال ما است
🇺🇸
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83079" target="_blank">📅 22:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83078">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kke0aDMCxzfgsc4K7o_XuRPUzQ-zCvtaBwE9nhKgqY3tSY7Wyxo7Qnyk4Lx7dkALxe3YT4_HCFh31bo44Pj7wIb0EHh8zGrTT0BRBLZ2wChm2LWjEbgcEMX3rPh1k6AGZbICNsCsN79qvNK5rLDZ-ZDzIczJTEae3DwDD0CyVKuvVdIfqo6e-KBGoAv8CPUe3tWcisqvDdodbCgUIbQhIQhigjnRnVMWi0IgVogBhBoHAlY9_ACIuUa1EjE6UVu8aJLPsZwZqIJ1r3iW13Ic4dufZS-GfnMWmSuVxGajyVZP9ogn7Aaw6qvsVQ3LVAPXCwBnxse6g0Id7BD7FGPclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من حتی خایه ندارم با اکانت فیکم چنین کصشعری رو پست کنم؛ این چجوری می‌تونه به عنوان رئیس‌جمهور آمریکا چنین کصشعری رو پست کنه؟  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83078" target="_blank">📅 22:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83077">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4scmUb5IDMuI1TQ20zqcxWtAmlUsXFAfGXG6mxW5IV1IpXJyd5aNWZn-rshgm1dQ1Gcjd3ngWzs251zg5M9-RvXO_rCGBz-0Tmwiy6K5B8dIwzRQU9HAih4C_i6tpF3TTiGTRCTwb18Grp8L8y0IiWv30GYIoN8TdZStPLDS3eIL7etuCzGuSrKb-DTZTXWRlwhbf01JGc9-krhtyy08MObwHvG-ZIA3BM15qLwVc3XmvCfO8R9xVuRFXztfXN0mzPCWVmKMa-x9oi2NKQnBpq9olCIHw79gTVzWRhU19F6ZOm1LAJZB_LFvbMjsmM6F4hDfwqubOrpxhJyFivXOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من حتی خایه ندارم با اکانت فیکم چنین کصشعری رو پست کنم؛
این چجوری می‌تونه به عنوان رئیس‌جمهور آمریکا چنین کصشعری رو پست کنه؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83077" target="_blank">📅 22:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83076">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">از امشب نرخ سوم بنزین ۱۰ هزار تومان میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83076" target="_blank">📅 20:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83075">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2ybRm8_4M50GFYNEKpLedCQVkGZZ8YFLTC8ZZzi6PMLKRGnYyFv72qKzYJtpJIwG5ygpl80WpDCQnt6ejEt9vJpCh7XI1tC52f4nI0q4iNT3LXsHhQhh84bbbB3GhezJfHnd_DdC-KUkiwknQSDCpop9QwZPsODlaiGcGJxumKttqHUbX1Fcz7EZSQ4GngXWXS5GS2jDZzukOcCtKF0GbtIlBL5tSnluTj_8-2XM7YgYlU6WS4tgnhqlxgWoZIthXV--9Q8dKu3_VFZvhx3NsUPKHd4x7oW3W83vq8cBw11QnJS-dcKY1RIusqHuNYaPPYLtgdUr4UvsXaPZpNl9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمین صبا میره براتون نونم میگیره</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83075" target="_blank">📅 19:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83074">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYQt6n_r7meu209e4GAWZOkxnBF5u0sts05P_qJZfRb7XtvLwoeczSdaOoQUBpG_NppScbsN3UWd-JiLZVmothd-TeYiF9L1exEqgWDAmAZReXBnWsNvTMyM8hViV8RVlaZ2c49iSMdzT-59wsTrOe3ruEvO8ob-cZ5Cw_4Fi9FUZkjg3kn1Ly47OTUgzfN1XOwhrI5v8gz2wOkTQ1wJMx8yutFniCLQy-aI1jjMYxle9ZLhsMftoV6uxaKREx83A2b6nMWV2IJhBzixImqH9UruGbp3KN9gT3G7mUZaCh5VAc9KdvZoe41DP7Cq615IXf4orA3EAyQbQHuyxGCu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش به خدا یک هفته از درگیریت با بسنت گذشته،تمومش کن، به خودت بیا
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83074" target="_blank">📅 19:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83073">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کصکش پا پرانتزی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83073" target="_blank">📅 19:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83072">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">منچستر کصمادرت</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83072" target="_blank">📅 18:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83071">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4_KrwsXz7jBAkVfLFDU0cDejHdSAoQVnY2kJ66Vr3ThpsFaX6NwIR-RomvtMI5mhIeDdvZBW4Z89PsDw4uasNZMaG7sEn6tWKRw5KvqEK0GL-THLlfMXgON5dao2okPDmQFR_EBpmw03h4h286FeUeVZw0Af6JVX4gGfKv_0TEemzc5L09FuupnrQR-KlFvul7PFjNQtbyvodiMxqhB1xiehKoKiI_6N1026RmXuuOgs-GrYQFj8bcRwsool6DQaPE00fsh-eofpVgTVXInrDBoUFYSKBE4u5npHjrqQMYqg3IPB1vWBkHMw8m-_2EW-mV8skdKVw6qcdv23tzPEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز خداروشکر گفت روحشون شاد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83071" target="_blank">📅 18:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83069">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فرمین لوپز شاهکار بشریته</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/83069" target="_blank">📅 18:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83068">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUUoDcfjBC6UGI1cNzp1pgN1D316XZP7tYmVe_536w7dz_YmBxJ5TzFCBpXpwn1Ekp57gtb5K7mEYmDa8nAheUTiqe3iL9u11dh9HefS5s_QnN41z5AAUAWzOHeUxv6oWk0nPKKcMaYLeYxjTWs5ubPhtNeXu487ka_I8RgbrEqHGeY07KwfbIxYRxUlyBHlS0jb4iBAg-N_bx5LdiYCpJu2tLlIzqf7xK4CZmQHs1xG5WzFNHHzyTOp3FcbdWJ3g6WiW_n3fk37sEgOZNzbVSjXjF4s0T6T9t8Uxy-b1bkpT1FcztltezFdRzxnTFcHahQfrrEa5rKPRLjxgo2q6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداشم آلوارز نفوذی درجه یک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83068" target="_blank">📅 18:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83067">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORB9t6jlTUIyZBB5DKiJYwWBupZX35PzfPZoloT-QvXDaC-oYCHnkivg7reJkyOIWCWyFP1RVN7DXPmQ67azOCArWEOtjrHCE5mEmZUFAVM0vS0IWdQUnK4bp1N0afFBw4WJqLGo68gCLALp6lgtuOXuM3gTVoFQDGygog5FL3QZwrPtmKkqI17Eh8iXms2T9fnr6Yx2omVUr5PPFZ0xj5OB90QFwPCPXIetfs1wd13LpeP5wnw9hHMYpE8jIb4UOlWMx3uemX-tibsYEO-CQzlbtmBdJRqKN2L1wwV_QlwVXBalBA6d_vIigt7rBzC1dByOVzjDylg9cdv4azTtpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
آرسنال
🏴
-
🏴
چلسی
🏆
لیگ برتر انگلیس
🏴
🕔
یکشنبه ساعت ۱۹:۰۰
📍
ورزشگاه امارات
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
آرسنال
:
۶ برد، ۲ تساوی و ۲ شکست در ۱۰ بازی اخیر.
✅
چلسی
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر آرسنال: ۲.۹ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر چلسی: ۴.۴ گل در هر بازی.
🧠
آرامش ذهن، دقیق‌ترین ابزار تحلیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g15
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/83067" target="_blank">📅 18:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83066">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgMC4Rtk2VzQKqSdRSPylGQKlI11ukHBGpGLpgYZpTh6h5H1PyRpXWrs2Fx7e19Z5sooTWTr2MxrurXgPFU9EgprW4VzHJUCqmbr2AR50tDfBo3Leg2R6PG-5XoG55l5ljea9DHbWoPFb4YDtVJBPm9ZDYsUFb6fze-tCptJ5gIPTxpoa2m8Fz1bnPk9xoQxqiniGd_7OuX4s19Lp-AU7AE4Y-k1MetCTPaIF6mVjuulnjq9NHM2Tocybs3pHCEiR_3cwSN9P3JvoLeBWJV00tLoZB92d9X_F044yWIs6kS-tWihTZMIdF6aKx1jynvQz-gRpaWnIGi2fgmb5BKq_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بریم واس شش گانه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/83066" target="_blank">📅 17:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83065">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKV3Rc7ptvUXicNhqTehBCI1snA9ZKDNB-Ae_-YmV2olx_7gA_gaMnScWvh9wz9Ykc0nbxW6Uw02JFLv35TP4i_SVS0HN1YXU_VCfZMIz9niXLfrMuCxZMPAk1N4shWibmFzZs1mSM74vusZQGyhUO_BCdsejg1QO-Q0RIYil_PTYSCys8lsNYP_oq03yXLNRYj5Nzqf_jk1G1pVcb5u2WpaUpM6r7ROsRSYHcXrqHMVXFzYuJba6sKS3csQDhnIDEwWXucf7ZmEyYSFK0pOS-GUHopK2ryjJmzks7kq-Y5_IZKZQ6SQdC4OMdEEHykvEeA51_-TUuHV7SwZ3bCAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به هیچ عنوان برا تازه کارا ساخته نشده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83065" target="_blank">📅 17:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83063">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuKj6t_cf6zzTC0sWNOy7hGF3UokSvitdbLxv-Jqfy-ut7xI-4oD7uohdI5Y3k4urPe2XElKSNnZKpHtgxXOJEOjgkXIR0rKr6v1UCdCOD6pk6a6utUC2GRy21hrG8R_5UBSmRZmdXSkqcMUFqzO4ZamgDpCUwE1VnRKSijBGmPT271PFwJnzu-NdiQSj_zhs3Cik4pZBfLbjNxAq0T7Us-BOk7onKJNeR4_TVr8aTe_XiFLrz4lGu4ka0-p9ljBrukeQSuLrIukF42odFuibUUzAWFquelwrRzI_99HcJahC_uuwK5iTUZb92In7oOizNbwi3uTbQNfPr8pLuyzoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff0e768cc.mp4?token=azuuZVbtnIELwaSTpbN-7Dj3gRfBE31h68zGFOL9j5h0GYBxpoIKHLBEN_FtmBfO5vmX-JVQI5l1G74rSbo1j65M1cYRZiOEui3ukwt_kxSGv8e_QSG35jsLM_JD0Y01kaQTZwlUgkpHonNZFLZI9sS2pZmR44uGuEUV6GtVYP9t0fnFLNezNoxUPYwAmgLGMkmPJTiXVn8iQzF_rTPnz1iw8zNUcNxH_VQ5EJnM5zO2fvmldIfyjF_zZOp_qc1gyK78fe4R-OWJm8UnlWWRm1etI4qES1jxv5utfOvJCiCUvIYBcPH0HC47dYMhLElYbwpc8a1r1opTyORy_0smyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff0e768cc.mp4?token=azuuZVbtnIELwaSTpbN-7Dj3gRfBE31h68zGFOL9j5h0GYBxpoIKHLBEN_FtmBfO5vmX-JVQI5l1G74rSbo1j65M1cYRZiOEui3ukwt_kxSGv8e_QSG35jsLM_JD0Y01kaQTZwlUgkpHonNZFLZI9sS2pZmR44uGuEUV6GtVYP9t0fnFLNezNoxUPYwAmgLGMkmPJTiXVn8iQzF_rTPnz1iw8zNUcNxH_VQ5EJnM5zO2fvmldIfyjF_zZOp_qc1gyK78fe4R-OWJm8UnlWWRm1etI4qES1jxv5utfOvJCiCUvIYBcPH0HC47dYMhLElYbwpc8a1r1opTyORy_0smyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی عشق ابدی براتون رپ خونده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83063" target="_blank">📅 17:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83062">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ساندی‌تایمز: دو تا آپارتمان پنت‌هاوس لوکس تو پلاک 3a Palace Green لندن (منطقه کنزینگتون) که برای مجتبی خامنه‌ای هستن به فروش گذاشته شدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83062" target="_blank">📅 16:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83061">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">با گوشیاتون تو شارژ کار نکنید که وضعیت بگاییه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83061" target="_blank">📅 16:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83060">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b309c1c56.mp4?token=ks1qYYFZ4YAImxwe4Wv6GQciZSgs_enKOs-unbGwrqhLdAn3Pn3D5FEjky3sbXCrLL7SnlJ5boHOs5hfPFnIAd8cNUS0-wP8rSCaZXmtGstqtclyiqDUKLf_-YzqIlfLddoulKG322Q_ZUL_sgSzcGM3X0by_HSJoTyX86fQxdAUG8klgP8yjy0gXOYfkh1OcGi_qQDPfsV7C_5u-c_m38rqPI8g5wFydvoLZRVaAAoyTRpPqXjdnD35XmbD1dZjVBPrs55WBPFMP45bFUlOLmlW2QhebrQI744qiqpCpKgefMzmWziHjw8dnnGt8MOi6PUeHi7ZBCIW4nT_gnl14w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b309c1c56.mp4?token=ks1qYYFZ4YAImxwe4Wv6GQciZSgs_enKOs-unbGwrqhLdAn3Pn3D5FEjky3sbXCrLL7SnlJ5boHOs5hfPFnIAd8cNUS0-wP8rSCaZXmtGstqtclyiqDUKLf_-YzqIlfLddoulKG322Q_ZUL_sgSzcGM3X0by_HSJoTyX86fQxdAUG8klgP8yjy0gXOYfkh1OcGi_qQDPfsV7C_5u-c_m38rqPI8g5wFydvoLZRVaAAoyTRpPqXjdnD35XmbD1dZjVBPrs55WBPFMP45bFUlOLmlW2QhebrQI744qiqpCpKgefMzmWziHjw8dnnGt8MOi6PUeHi7ZBCIW4nT_gnl14w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک به قصد پاره کردن کون اوبر، تاکسی های خودران تسلا رو به بازار عرضه کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83060" target="_blank">📅 14:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83059">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szK0WTG8e7lG5XjR0GXeMrPDlwbLelktNEbgxFowuXim0Q1wqitHlQmPE0eDtW_XBKNz_QkzcFKECODYqB7pY4STGALrQYFwP8tWBYrGMViNICfihO4Wjyfcu23wZe4jvuo1VYvJgkJXpELB-D6_leUnud60PC6J7JUbcRDxRAxYE2qUYlAS6ghbFAVGZBaR2Co38pzlua67ZW1CA203xfAulk7H1iDR4eeMohFdh4yn6sOuD15fhxYsVeftzyeQYMwMR8navCd9cwou90fEI4R4RyYl4WLIMGswk3ZhZpYDFizzAU1P8tL6ZldFlZhtAaODjJA8W_TzIJBSgwxcuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمینای خبرگزاری فارس واقعا سطح طنز بالایی دارن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83059" target="_blank">📅 13:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83058">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دلار شد ۲۳۰
ایرانخودرو هم اعلام کرده میخواد کصشراشو گرون کنه
عالیه وضعیت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83058" target="_blank">📅 11:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83057">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxJmnHkrZPyfgh28gst7BvWk6wcB3A_4IuGDDqu1ECr21adcw4sidwCtBIjSieUBYms66XhVy-3Lh3FErqI6XXg8_nhBigJBiJ7rckQMJ3UABd1s6_i-5vu4j1tLorAjljZg_UE8_nxiwlZLglCDDz84UO0fdPufYQMx29qljWtamnjMxxpa9MVVdxHkubGfYTOGkkIntam08e5VdCdNMgbCFIDdVu4nBhlv-f-iTUMemReOqrjh9g-RM2XifMvvB_BUkR70LRaIs-FOiQFpFDo-oMC1vo35D1Uh-rOenSBDu9NQC0S-fJVfor82UMuPPHn1_kLmZD7sMAWrZzAtnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردن نگرفتن همیشه از صفات بارز کیم جونگ اون بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83057" target="_blank">📅 10:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83056">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_R7zj7DUKHGi7uA9aK6QB2sRnzW7N5RAEsUkiz7jsjhJrcyBBWAcrLGl2Td66AhOjxmVXgQH6YSB4SAC-1S69T3-1UEuZVZDZpzzFbLm3U9fg1rfH97yC6s53y-mhsiv30CzPQAU_SMBiU07pxZ3yQAZn7nL6Yo6ora1lqFC8XfNioaDf75nSpAW-sN6yCd6ZwM2K1BiMJadlpK53_1Mupq8NvQCiFbJFHjWm4T-yd_-Y43KX-DZoeOspPPLbS27eL1OZ8cAevxLplLPaZY5aBRwfmwIgeidKYU-Y4gxSEsM5uPbNM-XN7RKgItdoEI0zhGEsIHJQU_1rtN2L4Qnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
آرسنال
🏴
-
🏴
چلسی
🏆
لیگ برتر انگلیس
🏴
🕔
یکشنبه ساعت ۱۹:۰۰
📍
ورزشگاه امارات
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
آرسنال
:
۶ برد، ۲ تساوی و ۲ شکست در ۱۰ بازی اخیر.
✅
چلسی
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر آرسنال: ۲.۹ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر چلسی: ۴.۴ گل در هر بازی.
🧠
آرامش ذهن، دقیق‌ترین ابزار تحلیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r15
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83056" target="_blank">📅 10:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83055">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dba858a3ad.mp4?token=pTs2tebI1nCYblQRZp32u_80NI6Y6GDVM0T2XcviWLqTyJDyBndl1kvwjr7bgXX7nWy8gWM_ajcg69W3b_y6So4WgSnCRdS6gDvGW8E33PW8KrrP3cJtFQ97H-v2JJEd6vs-x85gJebMoV5htxg3c3WZ_KKWBQQ1Yyob-biuYbCPKHv_yEf8I8wQcmmTzuaLUPYJe6lF1Ww2sVrsF7wjI-6mJUiWATgjlde45lH-9G2U-fo1qfsSaMIRxBcbisJgGMWw9Pu5vRJ2Ck0eihw9xS6eterIDSVsBldY33-Rz4UmOBIO9xRsRPHg3AwE0kFcbGwAdYA_k2W9Y-GIQQFfkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dba858a3ad.mp4?token=pTs2tebI1nCYblQRZp32u_80NI6Y6GDVM0T2XcviWLqTyJDyBndl1kvwjr7bgXX7nWy8gWM_ajcg69W3b_y6So4WgSnCRdS6gDvGW8E33PW8KrrP3cJtFQ97H-v2JJEd6vs-x85gJebMoV5htxg3c3WZ_KKWBQQ1Yyob-biuYbCPKHv_yEf8I8wQcmmTzuaLUPYJe6lF1Ww2sVrsF7wjI-6mJUiWATgjlde45lH-9G2U-fo1qfsSaMIRxBcbisJgGMWw9Pu5vRJ2Ck0eihw9xS6eterIDSVsBldY33-Rz4UmOBIO9xRsRPHg3AwE0kFcbGwAdYA_k2W9Y-GIQQFfkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابک زنجانی یه ربات هوش مصنوعی ساخته بعد تو یه حالت مثلا ما خریم یکیو گذاشته با کنترل کنترلش میکنه، یعنی در اصل اصلا ربات نیست و اسباب بازیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83055" target="_blank">📅 10:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83054">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/83054" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فحشای خداداد عزیزی به امید عالیشاه.
کصکش پا پرانتزی
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83054" target="_blank">📅 00:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83053">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قالیباف: بستن تنگه هرمز به ضرر ایران شد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83053" target="_blank">📅 00:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83052">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اگه میخواید عمق فاجعه رو بفهمید باید بهتون بگم که قیمت دلار داره دو برابر قد کاگان میشه در حالی که پارسال همین موقع کاگان ازش بلند تر بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83052" target="_blank">📅 23:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83050">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZw6Kt63hp-pL43cAJ109jgFz7b-KqCK0w2BVnUFkqLaYADh0xiDK0YFtJtSxuDnsWSO4k5T-mGSNKPzpio0uU_W8nb3CYf32Jjt7Wpr0PEOzbXDO4bKSpJbex8I1aKzrZVXzEAm-HjIztaYsf7m1oqmuZtlawXHqFX-uDjYy-tWGYztFG68LLckrdaKS0cl0xOkm5-AcqfAdZHSV9uymHAgt2CtNIRAq8IEIl5Qr_k9Fj0ZR18YDcXr5RpBCUIWNdlSNgpxiGNX4Jw1WnA9IYOnKjt99WFBFMQngFIgpvmeZaJv7600GRvxHH1WaY9hRIYU0eNfugzRj_H9e6SqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUybRPYMc7-kvmg-Dygb_ZmVTmUgJM7eYv3KYg6WU44BNDxJg1GpQjokcE6r1xYHq9dDpZSq7iV6ypL8djSnXCTHUh-QCmge3oCxVliX7yFLY79KC35dW0mLGqFrzXe2GhxpVIgKpfMNVYDoGH2Be6q_dPTuYD4iOc3plhCukHu6o6Vi7AocaDwvleP8Vj-fn4I5Tr87PMvTY21DLud00SX3v8perySDoB7Wl3YQHNXGNdEJwbIMXtxdoRnqHB5E5o84ZFTFPhRoH1JTog8dR23hVMGU3st4QLssKx-5ZsUisn796FbPqUoCR0Ox_8rVjX0z_sLBu3c3koXj1hSkag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین تی‌ام و سجاد شاهی دقیقا تو کدوم زمینه یکن که دارن سر اون یک بودنه باهم دعوا میکنن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83050" target="_blank">📅 23:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83049">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">درگیری بین نیرو های انصارلله و نیرو های دولت یمن رخ داده از اون طرفم شبه نظامیای تحت حمایت امارات ریختن دارن حوثی هارو قیچی میکنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83049" target="_blank">📅 23:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83047">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رم عجب تیم سکسی ایه</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83047" target="_blank">📅 22:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83046">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">همین الان برق ما رفت
وزیر نیرو : خاموشی‌ های برنامه‌ ریزی شده دیگه تموم شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83046" target="_blank">📅 21:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83045">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔖
ایونت دو برابری (Double Gig) فعال شد
#⃣
با کمترین قیمت بازار، این چند روز هر چقدر حجم بخرید ۲ برابر تحویل می‌گیرید:
❤️‍🔥
10 گیگ بخرید
💎
20 گیگ تحویل می‌گیرید 20 گیگ بخرید
💎
40 گیگ تحویل می‌گیرید
❤️
سرور اختصاصی، پرسرعت و پایدار فرصت ایونت محدوده، برای دریافت…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83045" target="_blank">📅 21:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83044">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پویا رحمانی فایتر کار درست و مردمی حریفش مالیخین رو تو سازمان کشتی RAF شکست داد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83044" target="_blank">📅 20:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83043">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtXjULyp3SGsFn2EbJGa542A_itP3wFnKUitphrOjiWkA0mVK-juPzl8W3imp1WwzTEZCykEIzO-JpoDZku_ng_n1keulvBg6dnKZsWoO41s4vUwtYdNR5eK8J0jEjqaRPw3F4FYp0-G57CecG5JczgQ3-hZSwh5jhYq4cUpkIqKXhLV3GI5q93jUvMhiy_OUrs3Q9MHnADJnEr4ChCxNc0n1fAQbbtPh7o8zw6btFEd-LhsE_Bc-YZPCH65cAUTbgBiByx26z10vYeInyeUzIuIHHZNqqqJ-9bWm477dTtdtJ6E8bqXqWqjXdfxIhsAKj5mCzZQ50MFphMTeOD8oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پویا رحمانی فایتر کار درست و مردمی حریفش مالیخین رو تو سازمان کشتی RAF شکست داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83043" target="_blank">📅 20:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83042">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دلار از تعداد ممبرا بیشتر شد که
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83042" target="_blank">📅 20:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83039">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nz_VfakHICriXDLQx1jngZgYbSgTd0yqcUqT1vYMzFdZkplrkITGE7Jn5OGueURMqhwrFas3Ym8r92Nb2tvTSbc7N6HDh9xA7M0TK0jWqCyBB8wqHV5dt8bRokcVLmrYMlgcqOsvFrAqGke5pm8g-gJPFTEiCOw8WdZxOF3fnRkBsW-_wWAVTQDwsCEQ_Xy1Kte0CHGvFUrhBWR6Zz3XnY4fznmEmepiKrxQnIBJ26hzeleYNDh6taBKP-sfvLBDgDNd5-1oKtVLG_nXO2R-s1s4rlJyTSpvO_nOZjChNMfZmB9Uftgy9n2ricRucnJHcXTb44ZU9H8_s4jJNBTi8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkSs-stAyEBisIrV5NvpWJxGJ2YI8zk15JIz3trClCvFLOJiEtL9aFTJQerzA7V9SfCAYYoYKpZv-MxUJen8uFXo76I8nG51MynGvyYhcty4ls7QxE0-CkyACiboyHjZcx1tU6OImoFcGJBCcsN9iEL1kVhkjC3B0oMprhDYi6DHd3ZN9Ze2QlEjbfBqmQTpnewev2WraLc5jVe54kag85dBjF5uM8K7tloaA-jCuRIoBfNZ-ufnIvbQPq6qTNGOcHwHtEbUnDS4X4cs459CX3bJVN4PYTFBlxakLfLZneXHjR7wGZ78_whACDAJ1RrShhIfoaNkNKgYpCZkxKB0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q-q10t5kLAoknz852aVuyIS6b4CaIWx9m8_kpo1OGGpyXJlLKMpCJ8ASIqLeHt3ljffsOAnA6kbQ3EFwBVvdfOGX4zbIwTpfz_VKbOrHUnZnAx-fqGnGf9q82c1ZJS6g853IqeuvK8Jjg5PgCT2xOn6_5JDbVErk4dgFWKcysIlbGarlXTtZuZO2NeXbaV2XLEihPwRr4pROsComfff-PrIokpXXgpeVmZY7bVjJSyu2aWuH0nK_9rptdYFMKVXRVPAhoMOgl9yJg11FlneqwwsNhOQU7vgRWK4zC81cnNqofyFPqv_eXCsKHvamlDJToOPt9QmRX57pCGHRJ9nWyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تبریک به فوت فیتیشا
ترند جدید توییتر اینه که دخترا عکس لاک پاهاشونو میزارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83039" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83037">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔖
ایونت دو برابری (Double Gig) فعال شد
#⃣
با کمترین قیمت بازار، این چند روز هر چقدر حجم بخرید ۲ برابر تحویل می‌گیرید:
❤️‍🔥
10 گیگ بخرید
💎
20 گیگ تحویل می‌گیرید
20 گیگ بخرید
💎
40 گیگ تحویل می‌گیرید
❤️
سرور اختصاصی، پرسرعت و پایدار
فرصت ایونت محدوده، برای دریافت سرور تست و خرید وارد ربات بشید
🤍
🐶
@MaMLiNeT_Bot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83037" target="_blank">📅 20:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83036">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b8b1d6558.mp4?token=XgIxKjOMDK9GqFRgyCubpVymXorwDFkd6Ca9gyO25QGx3ENPO5l0_F_JtO7z8lWe0xdmmAEG0xv8ylTENv8kRFEBT4F7RTMTEoq-qpH99oUs1W6CFmK92PYZTNK4fhyV4LA03P8ex7OdF6b4rAwioGSphOTtx3LIjfCAvq29hjYzd7rYDNaz637SVsCeJhE3lZMjtENM0CnVuhYLIGw1E1tvQVtuCvCjIm3yb-uwwDVbZUn_ftYpjLnBcUahL9ZVpPJ0JS6G0Hny0_6j-BKzVti-99cOxYrDeZjYxbmGRv56D_NUYr-WOE_Owp5udJTNw7n-vqjOf5zi9dLzIsRXOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b8b1d6558.mp4?token=XgIxKjOMDK9GqFRgyCubpVymXorwDFkd6Ca9gyO25QGx3ENPO5l0_F_JtO7z8lWe0xdmmAEG0xv8ylTENv8kRFEBT4F7RTMTEoq-qpH99oUs1W6CFmK92PYZTNK4fhyV4LA03P8ex7OdF6b4rAwioGSphOTtx3LIjfCAvq29hjYzd7rYDNaz637SVsCeJhE3lZMjtENM0CnVuhYLIGw1E1tvQVtuCvCjIm3yb-uwwDVbZUn_ftYpjLnBcUahL9ZVpPJ0JS6G0Hny0_6j-BKzVti-99cOxYrDeZjYxbmGRv56D_NUYr-WOE_Owp5udJTNw7n-vqjOf5zi9dLzIsRXOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بیناموس این بمب اتمو کی میزنی راحت شیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83036" target="_blank">📅 19:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83035">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تاتنهام کصشر ترین تیم فوتبال تاریخه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83035" target="_blank">📅 19:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83034">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حاجی یه سر داروخونه برید قیمتارو ببینید دیگه خایه نمیکنید سرما بخورید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83034" target="_blank">📅 18:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83033">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNpmv5Z3KEFGU9CxvM23SKM5xMV4Rugh5Op18SebD9QvmCERVwf0x1a6u2dWz5UGiJrF3VeXCt2XudQQApjIC98wdRlDNLdzafdqOU9W9h0lUwxD-3XeErY30KqXwyenZCHm4lK9I9r83bePOOvqf8yPGExevn4XbeJ8N0OtmT8HAhQlR0FZVl1q-uw98tT_mt-wLm9loopDVgGtMD_NtjB_fn1_v-4NQCzBEqJgThWTfsrbawYQ_WkTje3FBloJB03pofm3X3V0x4_wXVmHdwS3OdJb7nn6fOtsTyWatGZI_PplU8d87o95qeGDeQN-CusHgt60bT0rs_o-4DzoOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو بک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83033" target="_blank">📅 18:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83032">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaso8WEv17ZblO8OP6VAUkkBF2BMVzkvc5yyWn_ezFdMrVXkJfPU6hl5kY4lH1_jqrTWE5y9Q8HscF00ZzHk1kr8M7OIWXinmkqqfSiwFgpTZPAZ-bfAZ9FWhsBjCmmaBWJl8KunEybbQWE-UHmPZ05ZxOHNRMKfh9-U6w3DeV5TfN3sOuPvnMl-4h4rJWQFXGdkpUPMbNIvTORuUFm49G3nPYAydZ3RE0JmFnSZgHLVoXBqbHLcH5fo_DR6w0jCc4cEWteYEKEfDro8exAxrx22MhaP3KODUGhVb1SmaGNbF6A6HjGxmIeK5zR7F7beCA9KOgy1rCPFDGfCINNKLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
صد درصد بیمه ویژه پیش‌بینی لیگ برتر خلیج فارس
🇮🇷
⚽️
با ثبت حداقل ۵ میلیون ریال پیش‌بینی میکس بر روی رقابت‌‌های جذاب و تماشایی لیگ برتر خلیج فارس ایران، در صورت ناموفق شدن نتیجه، بت‌‌فوروارد در هر روز از رقابت‌های لیگ، ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PERG100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g14
💻
@BetForward</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83032" target="_blank">📅 18:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83031">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دالی  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/83031" target="_blank">📅 18:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83030">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گیمرا قراره به آرزوتون برسید، شایعاتی پخش شده که میگن تو GTA VI سیستم قطع عضو اجرا شده، مثلا با شاتگان به سر یکی شلیک کنی کلش میپاچه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83030" target="_blank">📅 18:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83029">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1d45c18d.mp4?token=ZEscLC6LcheHqYg_0rSdGjPtEW-WBr4B7QTAZu7IAyEQwuzSHI9DH5uskTXzXhFKUNecobCl3q4iQr9bLSIStsYYPwF7Mul8er0xHd_AigNyQsnOB8ll2SYK7s-uUKiQUeHHHUsvQwWkRHSg6kAgDya0850KVI6krOUMio8xj0MsSSmnc1XH55euKAD1rHkic8tzhCJc5CmYBgvvSmXa2JLgvIXCChfgaxqpcNGxpcNMc2TUeDty32Z_Y-MQvbmZ0oPFnSHDMUe0AGYUsrRvIUElNJyzGs1JyAnp9hh9uSCd_itD2dDIWnFDF1SgJDPaNliP5cLECoBSOQ8vaRHZ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1d45c18d.mp4?token=ZEscLC6LcheHqYg_0rSdGjPtEW-WBr4B7QTAZu7IAyEQwuzSHI9DH5uskTXzXhFKUNecobCl3q4iQr9bLSIStsYYPwF7Mul8er0xHd_AigNyQsnOB8ll2SYK7s-uUKiQUeHHHUsvQwWkRHSg6kAgDya0850KVI6krOUMio8xj0MsSSmnc1XH55euKAD1rHkic8tzhCJc5CmYBgvvSmXa2JLgvIXCChfgaxqpcNGxpcNMc2TUeDty32Z_Y-MQvbmZ0oPFnSHDMUe0AGYUsrRvIUElNJyzGs1JyAnp9hh9uSCd_itD2dDIWnFDF1SgJDPaNliP5cLECoBSOQ8vaRHZ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اژه‌ای به هند سفر کرده و مورد استقبال مردم هند قرار گرفته که یکیشونم رفت و دستشو بوسید‌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83029" target="_blank">📅 17:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83028">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "ترور"منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83028" target="_blank">📅 17:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83027">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPhOEQFgrGZ_4_r1vz6WmQO5wH5kqJ0ep_0YJWv3ICT5JsKmReNtaoThlK6A92-gblJPKKR0I82nfb2s7IN9KK2ANqmlLTggQ5uaci5C31hl8pEVX7RZHRdPxa0wWnwzZbeOZH7Bc48LprsRxOBccBwayW9pI46mSBXVUJXSC1lPqJTUV1C0rApY4abZsB9FlJtmhe3Eunvr03d9raJVvHr5jdsrGipdmbK6xtm1beCEf7Ze99htYqd7iUF8QuqHq0hwYhUVPtlIInoakDFupn8nzFnZyg5jvCeoPKBHlsy-aoDMq6zVoiQHaKdJvHjG9QkEp-ZGb7IlEaN4J1ERCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "ترور"منتشر شد.
Youtub
e
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83027" target="_blank">📅 17:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83026">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پسر میدونی چیه مملکت از همش عجیب تره، خبرگذاری های یه کشور با فاصله هزاران کیلومتری از ایران بیشتر از آینده اقتصادیمون خبر دارن تا خبرگذاری های داخل کشور خودمون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83026" target="_blank">📅 16:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83025">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuKZ3i-lUlRd12DPpxsoH15H0GxKUsfQDBuxNE3zDOVAH96NJME120cVxNk-Kyw45XxVYGx6P3lUaoAcPMleqWSRLHf9hfqY_6VEfD-8tjosERa6p93qScwbwS4vgpg5PAl8VoJEAR7_ucyS29CNPLYsVr5TneDr0rUjiB8WKa_hIOn0Er3Dt7qRsUgSBAPpdC3r3E-NAKxVmlIytGcGORkhwnPURzYUlLuD2i38p8Ss91ch_EGtIfQjn7ugC3X5HQKiWh_n2BPQze4oV6CedddS1GR-RXUT6s052hx3TM3noUd5pxlSqc4hG1uLA80ycDDZ7xuxdVN4cF6YhOq6Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محکومیت دیدی بازهم کاهش یافته و حالا ۱۵روز زودتر و در تاریخ ۵ فوریه ۲۰۲۸ آزاد می‌شه
دیدی پارسال از حبس ابد تبرئه شده بود و به جای ۲۰ سال، به ۴ سال و ۲ ماه زندان محکوم شده بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83025" target="_blank">📅 16:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83024">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Az6sGdNmyd1cmbFjKcvks8LoHdfAqXHZF-QDNIJnIstM4oj9gUwLW0HTKGHChTCE89k5JceDF985R-Md0LDj15KFCQh6UO8Mfd8SU_5nKvE9H7yeonrV6U0fx3G5LrSGP6JaZ1lJStT5PncCiIppHHCczDS9NStoc4mg5xaqQgsPJw5X50pzGoJqepgKjqP24lm3i4qUk_WQw6OPWNYw3JcZEO8I468bY0DehP4bVncE9IXV486MThGSKDy305tyNIORGofcHsi8hVCMBF8HFrE0upGskCrA4oi3IwO3gRHSZz95opXIPp7D_JCeLArh1UgdkKVSf9CAyrT-NSAlkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83024" target="_blank">📅 15:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83023">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">به مناسبت 200k شدن دلار بهش لوح طلایی ندادن؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83023" target="_blank">📅 15:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83022">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KANTNE2CwfPMBHyP0oZlk_QEWtOfEfrnWqKYyeAEzCR-14I-Rm6tqlYxA7JVaMfNtkPhNhevlMU4xDTMDZWfS8DmZb_tIZarmxUnZjLK5pGUQS3ZtRnFItLt9kMfs26rgwzusA8UQZflCAVBuxAcHrlHgSMfpOsz2mgnyIStI_OtAp8wma8I6eKmdLU0hUuOq7DJNnnDNmnxQ2VU3AMW3cvQPVTZJ1VSu7_Op4PBhUO2qyPiwd-Gv5hopGViXdbRcOxiT7a54WMn7UrhabZkkimrlgKDda7CRfq1CXPDfq5NwI_ZsMn4P1zX50HJfatqEyfEF4hZieaEZ6o-rLMMgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83022" target="_blank">📅 15:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83021">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">البته در نهایت این دختره کفشه رو خرید و به آرزوش رسید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83021" target="_blank">📅 15:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83020">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8CUHue5CZ-fSgdMVqN4Yjv0CIQCsOT7lW2ijk82SMo6fbWJRTr08-Y_uI4hx5kIOrZ5vCc9wwX1-woVWmn8OjdP7s5M0Y2AN5r_h-ahmNEKk_TUEqjjs2XB9AfN_I2PghUjYb-GoMB3rjCeBG3SG8vYXeQcn8rDr_qKSf5C7dU2_M0CVeY2T3xb3aYZjCtl53Hu9IkSx0EDq007nE_cOBrlDhxobij7bSGG78-XMyPKW3MmcxtgwbPej_sHjnEwN4zV88bRxpCndbev2rWlbEvIDUkb2n3dGF9qRTLuymoJ7KYNSQrne3nC_w30itoCPOzwwO9P5Y_TEYEkK2JcZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو این خانم از دیروزه حسابی وایرال شده؛ داستان از این قراره که ایشون واسه خرید یه کفش به قیمت 14 میلیون حسابی برنامه‌ریزی مالی کرده بود ولی بعد افزایش قیمت‌ها، کفشه به 19 میلیون تومن رسیده!  اینم دیگه طاقت نیاورد و پشت فرمون زد زیر گریه  @FunHipHop | چمن…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83020" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83019">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd895d17e.mp4?token=qnJSdxNW3swBwyIxmqNmQqb8fp0XcGkaiyuzu1HsVdJA7Il6jBgL9DwhRh7zvDQPQgGsoHUOpKFnEdKtDIet-tyo70dHSO8jICiSTRKsh1x7JyITOnqO97DeMV8joHw9Q3MrhAha0Nua0K_Wqk3MKE77D_1S8IOQcyxRUnUbmwZ21OG2QB62yU8FBNoCN3dkSm7QU_bz5VS3G5O7aMnpDw35ZiDC4LoK-aavyonBgA6QSjCnHToBZ_sw7UL5nNqaioxyRzuVd5eJh7tDcWCqlho7q4w56nDfFfVnGN39llDO-c14e8-e0akEGxEvOfq4GwT5E6XG2qVSORWzbzv_yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd895d17e.mp4?token=qnJSdxNW3swBwyIxmqNmQqb8fp0XcGkaiyuzu1HsVdJA7Il6jBgL9DwhRh7zvDQPQgGsoHUOpKFnEdKtDIet-tyo70dHSO8jICiSTRKsh1x7JyITOnqO97DeMV8joHw9Q3MrhAha0Nua0K_Wqk3MKE77D_1S8IOQcyxRUnUbmwZ21OG2QB62yU8FBNoCN3dkSm7QU_bz5VS3G5O7aMnpDw35ZiDC4LoK-aavyonBgA6QSjCnHToBZ_sw7UL5nNqaioxyRzuVd5eJh7tDcWCqlho7q4w56nDfFfVnGN39llDO-c14e8-e0akEGxEvOfq4GwT5E6XG2qVSORWzbzv_yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو این خانم از دیروزه حسابی وایرال شده؛
داستان از این قراره که ایشون واسه خرید یه کفش به قیمت 14 میلیون حسابی برنامه‌ریزی مالی کرده بود ولی بعد افزایش قیمت‌ها، کفشه به 19 میلیون تومن رسیده!
اینم دیگه طاقت نیاورد و پشت فرمون زد زیر گریه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83019" target="_blank">📅 14:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83018">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7770ac79f.mp4?token=G7l-7bN7TcVTNq8vwetIOrZZ3zCpah2QwC3a95dKLXvKtPlaZDIjt87dCxTOG9zlEqQI63OV-KfHx-920QUv4xqu8pWaSEzqYQzLDfIvN0VygQzLaAyJx8-FmOWpMzQRDwuJMfspcvutlrjXjwVfN2BXvtDGwJuEmCcX5EqaaaJOPn0Xo3i24kMKjaki4Ym10OKlvf2BzA83UbW3ZIcVbCjJtMJyy42LwzGhvadvoegnnXguXEeZwSTNo0Gz6w1iSllk0KaZV7BQOJSk5eXiqshPt6B7lQG61Qq9fmnBvRm7Gf2HFZElOjpdy_QedxU_YCJei2cf2QV845BJldZYKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7770ac79f.mp4?token=G7l-7bN7TcVTNq8vwetIOrZZ3zCpah2QwC3a95dKLXvKtPlaZDIjt87dCxTOG9zlEqQI63OV-KfHx-920QUv4xqu8pWaSEzqYQzLDfIvN0VygQzLaAyJx8-FmOWpMzQRDwuJMfspcvutlrjXjwVfN2BXvtDGwJuEmCcX5EqaaaJOPn0Xo3i24kMKjaki4Ym10OKlvf2BzA83UbW3ZIcVbCjJtMJyy42LwzGhvadvoegnnXguXEeZwSTNo0Gz6w1iSllk0KaZV7BQOJSk5eXiqshPt6B7lQG61Qq9fmnBvRm7Gf2HFZElOjpdy_QedxU_YCJei2cf2QV845BJldZYKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوزجان بیلان یکی از میلیاردهای ترکیه‌ای و مدیرعامل شرکت موسیقی «Muzikonair» امروز وارد ارومیه شد و قرارداد همکاری خودش رو با امیرمحمد امضا کرد.
طبق قرارداد، این پسر به همراه این شرکت مسیر جدیدی از زندگیش رو شروع کرده و قراره برنامه‌های زیادی خارج از ایران انجام بده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83018" target="_blank">📅 13:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83017">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uF1j4dcIlZJMnuZpgUJ_uagby2D_Lwl7KpP4to_SMqCDUdSLwOb77EWzEijly_xSOi3ePUzdD_F8eTlvTMiM3e0p9ct1ge7d6Ql4ab0r86jcLERWjQE60CwokNRK4bD-x1ntkO8IuKEaYKmj9D--klpc4AExLqyxxaFIKoXcaBH5rgx5WJFaQXLyT8DpHD5v0MVOXQf9AUXOjlEYCYQJdGFBRxDf0YGn0gup8nvWqlvI10AwrvT9a8uKjWQ3Md-e9AvljxEVT5_OcKzZhSroli_ef7pfGP2v48wda9TXnwKQro2HjopPt7xSudZeKOenKr-5vb3q_9KnIZv_9c7sOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
صد درصد بیمه ویژه پیش‌بینی لیگ برتر خلیج فارس
🇮🇷
⚽️
با ثبت حداقل ۵ میلیون ریال پیش‌بینی میکس بر روی رقابت‌‌های جذاب و تماشایی لیگ برتر خلیج فارس ایران، در صورت ناموفق شدن نتیجه، بت‌‌فوروارد در هر روز از رقابت‌های لیگ، ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PERG100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r14
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83017" target="_blank">📅 13:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83016">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دلار نزدیک 230.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83016" target="_blank">📅 13:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83015">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgIU07ZzJ8bGkgX9_VE3qtOfXQipQQHoWoHRKiilfsGjLEKisxxDWcrjFjFDahrtsHOyxrA_hWmL8bi8aw83G7O02ZBbpgWNvimqoFG1wAomBXROeMwGOxdmobbltNXT_SaPuOFVRQoe8Gc7VF3HpgVN3JQNnLbeVTZxv69aF2PM_VVtVYKgPtDLU-lKhv74vGJdCTlMUfIDevB_2-v-qmwgcaI5DxnRzv44IL4jS4wCHI3nn4bqjrw0mhJDSpDO2Caf7mcnGx67wesIc9xaMxfS98pG58qrpOfKuupOQn0yjrWTSQB7v5-UDsTo4ztMccwJVPp2h-mB3vuCpK8kOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیبارو سفت بچسبید شاه‌دزدای اصلی دارن میان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83015" target="_blank">📅 09:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83014">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">چرا هر شهر کوچیکی میری اسمش پاریس کوچولو عه، بخدا دنیا شهر های دیگه ای هم داره، یکم تنوع بدید مثلا یجارو بزارید لندن کوچولو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83014" target="_blank">📅 08:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83013">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ادمین نظرت چیه هیپ هاپو برداری فقد فان رو بزاری بمونه؟</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83013" target="_blank">📅 02:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83012">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16cac9fdec.mp4?token=RG8tYPEuHA2duIya0X8Vjil6YRRDp-N7zyaWdEQiNZoGLaWLQ8LMS0oCNJfZnZ3lI3Ly42hXfWhn4yk2nkjbh9fJpfrw17MBSsjeO1-8FQxUO9m-A805etlnVXW1StTS7hbKzqxI8UK-813tPytGSbrl12ZY1XXO44UIlhP3DBmWuiNvEDQi3QXze7FezlWlHMiqdQVxyJxzbacEwKErOwfcEk8P51liAj3XrEJJ09ETmbRw-ArXggkzptrGShKZ5pc6O7oy3RV5ccZ2S7nx3RzGNOsMzBjmxNqFtCuA9cUZVwNDw7XNkg-WzflW4QfWplFv_duidYR0VxyhpSKcvAf3gbmj_9F1te0q-rKbUjl0UO_5xOUmOWRW3R4yxBXpwiX3mRKpE-kdvOXwe5JgCObdWwVp6nugMnOhYztPT3Rz0XB89wwp5--lMVNNsEfJVs8ytmKtpXMJam1J-E1gDG2pG4K7rJfbNnSywNSpV2AOM0EVdoOxhO0SXgTDGAgRNCB4HjpPLF7yM_Cd1mR-N-fqUMP8ja_0TCnt5zzsYALMblVUJrgXk0MlKz-T0GBC_YxiHGmEZLQA1Ee9xmLIFZVAZYvOzGgeY5u36vpweNdgpe4oJV2Kxz6Yv7wJ3eeLGtL2C7OTxhK3JHCZAkBkbGjpO9ora1E9oTx6EkiGUrk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16cac9fdec.mp4?token=RG8tYPEuHA2duIya0X8Vjil6YRRDp-N7zyaWdEQiNZoGLaWLQ8LMS0oCNJfZnZ3lI3Ly42hXfWhn4yk2nkjbh9fJpfrw17MBSsjeO1-8FQxUO9m-A805etlnVXW1StTS7hbKzqxI8UK-813tPytGSbrl12ZY1XXO44UIlhP3DBmWuiNvEDQi3QXze7FezlWlHMiqdQVxyJxzbacEwKErOwfcEk8P51liAj3XrEJJ09ETmbRw-ArXggkzptrGShKZ5pc6O7oy3RV5ccZ2S7nx3RzGNOsMzBjmxNqFtCuA9cUZVwNDw7XNkg-WzflW4QfWplFv_duidYR0VxyhpSKcvAf3gbmj_9F1te0q-rKbUjl0UO_5xOUmOWRW3R4yxBXpwiX3mRKpE-kdvOXwe5JgCObdWwVp6nugMnOhYztPT3Rz0XB89wwp5--lMVNNsEfJVs8ytmKtpXMJam1J-E1gDG2pG4K7rJfbNnSywNSpV2AOM0EVdoOxhO0SXgTDGAgRNCB4HjpPLF7yM_Cd1mR-N-fqUMP8ja_0TCnt5zzsYALMblVUJrgXk0MlKz-T0GBC_YxiHGmEZLQA1Ee9xmLIFZVAZYvOzGgeY5u36vpweNdgpe4oJV2Kxz6Yv7wJ3eeLGtL2C7OTxhK3JHCZAkBkbGjpO9ora1E9oTx6EkiGUrk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این یارو زیر یک ثانیه از ناله های پورن استارا تشخیص میده که کی ان، زن و مردم نداره همرو میشناسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83012" target="_blank">📅 02:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83010">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=ei-60FillUuld1mcTdHdTwAi5z5dP_Bg9apBhHV3XLwWGrosz41kZSdRUs4MMCDSU565IAiBF-HECtQ5hkrgjVPAbtN9IIB99ZNtETnFPjlpN2v8Pe44G5vqTBYg_KZt84Fr4eLs9ZWF3l5h_p7Xpc9ntLubcY78ZhiVqpZCuddlZyRUFIBD2n1r-uFQRO7HMKXq-A5I6-BSbwZgzjsGJfdlHkhRlGL7XS2qagCh_-pO-TMK0c9NPPIsuOiK5cR-hWCdhXHKnhTEUlZ3k9Q5PiVNTZqspwIDkdXy3tdJdWW7sqhyAXMDORSLtvJ_2ZmzFlHeJP9QLhxYacGJsQbIrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=ei-60FillUuld1mcTdHdTwAi5z5dP_Bg9apBhHV3XLwWGrosz41kZSdRUs4MMCDSU565IAiBF-HECtQ5hkrgjVPAbtN9IIB99ZNtETnFPjlpN2v8Pe44G5vqTBYg_KZt84Fr4eLs9ZWF3l5h_p7Xpc9ntLubcY78ZhiVqpZCuddlZyRUFIBD2n1r-uFQRO7HMKXq-A5I6-BSbwZgzjsGJfdlHkhRlGL7XS2qagCh_-pO-TMK0c9NPPIsuOiK5cR-hWCdhXHKnhTEUlZ3k9Q5PiVNTZqspwIDkdXy3tdJdWW7sqhyAXMDORSLtvJ_2ZmzFlHeJP9QLhxYacGJsQbIrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نگریرا وقتی میبینه ده ساله از فوتبال خداحافظی کرده ولی هربار که رئال میبازه اون مقصر میشه:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83010" target="_blank">📅 00:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83009">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوستان رئالی نگران نباشید
از هفته دیگه که رودری به تیم اضافه شه اون موقع رئال واقعی رو میبینید
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83009" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83008">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdTs9cwhecYeq5ZEvHW-8Tr4JU7yPzO-IawHlBJFy9ZGnUuoJJwOsU0n4Bdj-9_UugJcaW7feGd0O1wON7emCH-Qa8zdbkDyKsrQslIA_5zyg4aycKbwk3FcO54CFgtw9L1TVyDUmrNTiNmXUfCm6yzsGvMiDFJTe03mGlpQPdP7PBucEveiu49NWy0HjsruSnmXV4_JmrCZbM2e6m9zL0Zs8Ltb5jX0YWgLHLYuQtx_Rqg3c_cQDtKlDIBrDFFgbXcYI2R2tGt30DM3WcrVNcNMb3W2ex98-MELJqFo4PRPd8cN-D_QfBvDRtbV78q-znxn83TsVIq_jw1oFpiUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چنلای عقب مونده ای که این شات هارو میزارید چنلتون و میگید ترب فلان شد بهمان شد، کصخلا ترب یه فروشگاه نیست صرفا یه واسطه اس که مغازه ها جنس هاشون رو میزارن توش و میفروشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83008" target="_blank">📅 00:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83007">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ولی لاشی با اون صدای بگا رفته هم بهتر خیلیاس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83007" target="_blank">📅 23:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83006">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">امیر تتلو از زندان بیاد بیرون ببینه حسن بابا چه کسشرایی ازش داده بیرون مادرشو میگاد بخدا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83006" target="_blank">📅 23:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83005">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0641a73955.mp4?token=TGkfda_xMXph8hxHPaTyQPO41CH07J6kHLzYVyrbvoBS3C0Wy14rJb3R3bdBbRGGMbeJ1w01DFbpFa97z2-ym8lR3sTb7fKnAFVwz1WsIwUYrIejqjG1FD6kVEE59oDjElz3NkCMxL-6ihL0JmatmVmpui22CG1LI3m6rO85J9he0Stzj52WNF1Hd86r5ARNmS9HQ5xaJFKRlHJs57OsLQS9OttOp58oBgT3_hQBcs6mJgIYAgEZjC0Tr21gJ8Nyrz5c7UxvLPZ0fpfveLtNsbhicz57WnC5-Il49Dm3aa4F2jOCDI0XLxx4FLJmneVmVawYxv3InKHUmdO4VFJm9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0641a73955.mp4?token=TGkfda_xMXph8hxHPaTyQPO41CH07J6kHLzYVyrbvoBS3C0Wy14rJb3R3bdBbRGGMbeJ1w01DFbpFa97z2-ym8lR3sTb7fKnAFVwz1WsIwUYrIejqjG1FD6kVEE59oDjElz3NkCMxL-6ihL0JmatmVmpui22CG1LI3m6rO85J9he0Stzj52WNF1Hd86r5ARNmS9HQ5xaJFKRlHJs57OsLQS9OttOp58oBgT3_hQBcs6mJgIYAgEZjC0Tr21gJ8Nyrz5c7UxvLPZ0fpfveLtNsbhicz57WnC5-Il49Dm3aa4F2jOCDI0XLxx4FLJmneVmVawYxv3InKHUmdO4VFJm9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترند جدید فضای مجازی دنیا چی باشه خوبه؟
شکستن گوشی و تلویزیون هایی که عکس و فیلم نتانیاهو توشه.
حالا پول اون گوشی و تلویزیونا رو کی داده؟ خودشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83005" target="_blank">📅 23:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83004">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CakXGTYwYJnFUQ6d4dpJNz9RLez-MEKc_lCC67qHLq4a6bMlIUfG9so9r5_s6V1s9RIbWmF7pDtHrETROlrbc-qhVAxbkOyPaFY7Y9Yux0hiMajEJB_x4iBF1h485rTcwzfkG0lZAVNAYX_rO9jr84uY7HmymVKyU_qMLdB12j1QEz5tIoq3qs-tPRtmLUAl3uM7jAV6GerwSjDZirerVbCQxghKFuOX3kuQo7VLt1KJIsUwZO3izJY5G51O0tNrlpp1AsM-Lied38icFFocquwTVCmYESXfgkHmdPlP64hRY-Ret56qcZq4VxJLb4NZPhPtYZPAFHLO7J-_eCGeLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا امباپه یک ماشین گلزنی ها اینو گل نکرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83004" target="_blank">📅 23:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83003">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdfYYCdIk3XWdHZKW81E2XKcx921KKd-FUfVVeKqh158DZpKCYIxxk-g5AReaNu8hf8Lo2nYtD-CDkCTz4S328OZZVy41_AmAYOErkTnPuqWvRG8MZY27YB9dOZhwUo3nxyHq59FxxYItqoEtNxWdye4LwQdEVXDbZk4nnwulIkHi0B5mP1hAp-crEd2kIBOol3zRXqqMDWWyvWkHzTeR4ZLjCSJSikkw6PMNfo-Z9y4WScCwCkHaafMVESE7lf8JkMFBecLlCC5-cmYxYKj5oFxOLQ-C281yfCPN0WxXjUA3wW7dJdVoZcHI0W_er2GTNt8CEGaq6Hu2D3j_sGDkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خستم کردید ناموسا، کیرم تو این زندگی که شما میکنید و ازش راضی اید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83003" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83000">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGePCnani-q5wri_wMZMPGuEyRFcBIee3ZsrH60-sPgDy0AizjKY3PPxE8HBZ5DTahT_Cwzw7_2ZOT_jJ0u1bnwDHZ3FlDKYfNQmay_cVn8lEZIgABE1TKd1We1LL2bFERVtSO57Jtfa6AQcwzUpDl9zlefP2CBfd9Sx_vduZxFz4parZw54MQEDFiWoX0lxTAkJKCfo3ZQfSo40C9yXMwfWwnI-YYfrFWBz3q6DZrRWl-5Svb7UnDTtJeWeIVBig-UPc8etvsw2rcLW7Zj62Hl3oRNgAxH9-bda-kRh1Wd0cgq2RBs8zN9wGZjVUTPnlEHtDxS-kxXGf7E8M3LORw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گاس فرینگ تو مراسم اکران فصل دوم سریال جنتلمن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83000" target="_blank">📅 21:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82998">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یا علی اوتیسم  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82998" target="_blank">📅 21:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82997">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfb0d4b2c.mp4?token=IcKpnzP28w99Wb5ydCnIrVTKmLVFnq_XD1V7RWEotnchEzjDSH7JFsE6WSygUSkfUB36I-CUgdq3J34jL7g_3XIJ3SoooPnb1y9sBeDPG3HuApnODMytbKz9QSG4heuV8q-LOktkKvndZS8LlKxtNDHFKUBDlb6DKRuJXxa8B-YvFj-OWuo8BkEFBxbFkRhM8fOyhmBaZ_q4iuyF1a8E0n3TUpatG2uWXAYtmoMuETxlNwCCQFUjfxTOfMZPVKyFsf-6YDEs1ypz6qNKK2XLFbJXXUWn7m3qgcFoKBGxTP0JPAI9gHkZpGTU2plsSNaC8BAgUtWsJKnSjK9rHamjkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfb0d4b2c.mp4?token=IcKpnzP28w99Wb5ydCnIrVTKmLVFnq_XD1V7RWEotnchEzjDSH7JFsE6WSygUSkfUB36I-CUgdq3J34jL7g_3XIJ3SoooPnb1y9sBeDPG3HuApnODMytbKz9QSG4heuV8q-LOktkKvndZS8LlKxtNDHFKUBDlb6DKRuJXxa8B-YvFj-OWuo8BkEFBxbFkRhM8fOyhmBaZ_q4iuyF1a8E0n3TUpatG2uWXAYtmoMuETxlNwCCQFUjfxTOfMZPVKyFsf-6YDEs1ypz6qNKK2XLFbJXXUWn7m3qgcFoKBGxTP0JPAI9gHkZpGTU2plsSNaC8BAgUtWsJKnSjK9rHamjkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا علی اوتیسم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82997" target="_blank">📅 21:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82995">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKCeyBnUySAZlmX08N9l0fTkgQYn2prH16k6spV9uEgsTMsTSvNJViWcP30BNC4RHUXZfAgQ5KgQqZC9_-zD0RGk4n4XJqIWFceJ_YmLiNIpws74ulf5-KoHJviO3H3K9BYepvYkcVRLXZ81xhUpBdY-E8sue1emDD5ZU8qdPbc8vyCCu13HkZIZFMEDXHFfmgMz33MBOC2tJ88iBCR1R2S6j5LNXAP5j9CD9Rl-m2NMPTwlvnSQBay5IwNlBCinNlHO4Qbe35dzeIUOgNUEPX56dMD5pLey2RhNjpg1myN2l56_5JI8Y1prQcy2FWgF68ubxjM42P8fvDTeS4iYVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FMPC9ZgUlCSnH8c5o_VzvgwpfmunfjyqKItDekPm_msKJl2YWEkoTpBGdZsgGsxup5lurr1rJROufF6Vboa2qMeO_Iaxs8v-MPuRqIcH2R5T0nVqdIwfhMinwfet-NkZk35iHu41ooV3eu8rOWqqxQCBGq_CVrzxphc1lIKM-2C-YUd5ahhSJM88KRxpd4heAqVOLJ0bMXDP6fOawWuoEhckjXVIWecQeYc49w__7yTKzXFLSHhe2ZIKsXVAY7ZHDdFb8hTRu9MJAn1VaZZoBj9PPI29C2L2rl89Y5eOCeuX9hjTFxtBOaP5d5NABkK01e50FaxvIjBjHkXXvpKLvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاگان این گیفه رو گردن گرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82995" target="_blank">📅 21:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82994">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce693d467f.mp4?token=T_YvogKWWO67xPQy9pFWa21lqzGrn6x53Cs28lWpVsY0Yj3r3nvw-fXLJBVgSoE8Pj8naufmC6LkYVyhd7DrpUsOtO22B9aaOmHalZn-cjNOboUJ2w1Cyx5Amm59h1WLTFML1_Qkf_r_VHeHmJENHHxahQcNv-vvfWD547i1pEizqvg1eEA0zhY-FIkiWCVQWDDT_yZwFTY7EidLOJpVb8gy4J00UVNkhqdfW6HL5lFlmOrzpQchFyeaQiFsxBbztHmtXeKgDdPlj7Et-qzupusXFNwvo-lwfdQsrqFOrureBU59btHdIFqIxpPq4M63NrNY2QdLylqkgr-a-Sn2pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce693d467f.mp4?token=T_YvogKWWO67xPQy9pFWa21lqzGrn6x53Cs28lWpVsY0Yj3r3nvw-fXLJBVgSoE8Pj8naufmC6LkYVyhd7DrpUsOtO22B9aaOmHalZn-cjNOboUJ2w1Cyx5Amm59h1WLTFML1_Qkf_r_VHeHmJENHHxahQcNv-vvfWD547i1pEizqvg1eEA0zhY-FIkiWCVQWDDT_yZwFTY7EidLOJpVb8gy4J00UVNkhqdfW6HL5lFlmOrzpQchFyeaQiFsxBbztHmtXeKgDdPlj7Et-qzupusXFNwvo-lwfdQsrqFOrureBU59btHdIFqIxpPq4M63NrNY2QdLylqkgr-a-Sn2pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به لطف هموطنای عاقلی که سطح IQ مثبت هزار دارن، لبوبو ایرانیزه شده و وطنی هم وارد بازار شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82994" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82993">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">از اصفهان موشک زدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82993" target="_blank">📅 20:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82992">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">از اصفهان موشک زدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82992" target="_blank">📅 19:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82991">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">از اصفهان موشک زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82991" target="_blank">📅 19:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82990">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXNfLP2i0I1PEA9l0mOslauByTRdavHMtdrd3S6Gx2sxzuYWsK6J5Ikb1tapIzrLND2ON7BLPqVaXBvOHrEpJ_q-qKzVBh0qU0PmJx1zfgK51RXPpWuNQY41hBrdgsRU1JLjAMV4pxV5RP0RFZWVMX029PEP2LBHnGsQQXMf8LCT0tL6EaxczhohfVtS_5fHDdrhTrQCh2VnJVUonWT5Elqk7dResnq-7GjgIf_lYG__vAlG4IlwRWJE3jJ3DuyUBlLJ0qsqcEMI8Tt0IkBJ4NPJFa0QZ9QojNqsRNKfFWr0g5lD0dUVqieqUqEU_oocxLf1b9Pt2ud7BkiXNR87dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوید محمدزاده از تئاتر "آرش" به دلیل استقبال کم مردم اخراج شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82990" target="_blank">📅 19:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82989">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">برو مارکت ترکیه خب مشتی، یکی از رپرای خوبمون رفت الان یک اونجاس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82989" target="_blank">📅 19:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82988">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9sRtYtOxmOlApWs7ba8drW7hJgxgyT61DdZxI9I2BHmICx8OEdcTIpX-730qBWZxcdM61hwUlFkk8FCUf0gMtEFevFYy30dL-6_4YAeScB-3iU7LC3SrOYGU2NlLABQauICN6aRs-i2_LM8TJ1lLEtwm5mw1MOjx2VS3mxa2_sK6bLi-kxQqybyapPKwK_lhzkusIjb3e8OLrBB-j7Yop7DrHK9P9mq8SFolaPkE-UNvfW0mbk0Q9zqiyomrae0j47NLfx4GkH-pFxygzbo72Q1evAR9f72g6IaCJ-mY-s8C-Y_Z-rVYrPTS7bjvh210aniwGpVN-wFVu0tbjkgmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمینای چنل کوروش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82988" target="_blank">📅 19:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82987">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ed68f76d.mp4?token=AnGeL-q0J6fdtJHGW1aZzmeDGLJ9cKDwajzQuITssql97jL-lAcD-KQMp7Db1L579WWaHkXZ1T4-vf88cY4MMCTEJdTa8gijr7af6B-8obt-6TSQbfhIRjhp698H_4dAR3obYmtqhCoXyqC4Wugv9tWrBpef4JJK3iKB9sY8Kl8X877PLFvTkma_2jtNH6BwTEuyT-i-ZyUq7lyVsZDWThCfJWJwWBiAomC8zhzvLVdWz9XD5RyfkVvcOpUrYnYjmY0qEL7xVX1-_p-GxVV0aFW-9tvKR8MGTzqLB3zc3DLFHHffZHE_XhEKEGuNdOqfStL5NlQQYLZNyBc4MtafOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ed68f76d.mp4?token=AnGeL-q0J6fdtJHGW1aZzmeDGLJ9cKDwajzQuITssql97jL-lAcD-KQMp7Db1L579WWaHkXZ1T4-vf88cY4MMCTEJdTa8gijr7af6B-8obt-6TSQbfhIRjhp698H_4dAR3obYmtqhCoXyqC4Wugv9tWrBpef4JJK3iKB9sY8Kl8X877PLFvTkma_2jtNH6BwTEuyT-i-ZyUq7lyVsZDWThCfJWJwWBiAomC8zhzvLVdWz9XD5RyfkVvcOpUrYnYjmY0qEL7xVX1-_p-GxVV0aFW-9tvKR8MGTzqLB3zc3DLFHHffZHE_XhEKEGuNdOqfStL5NlQQYLZNyBc4MtafOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست پاشینیان نخست وزیر ارمنستان تو اینستاش:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82987" target="_blank">📅 18:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82986">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf87a5e3b1.mp4?token=kVDCoZDuqcOCo5rVixTsqrVnak-IUXQ9_E5MQSaaTy5FXdbu3GJa00NC4xDf3bR3CD1ISbQgUMTN7f5NH1FYNdJx0T3QlBbjH8ujD9ayHawN62d6Fy5-e4DYBVgyM7xvQ3BwkM1zr1L9XNpuIoN-f6roqiy5CTjHztq6k0ov-7tc_43ekCxIx9j4i7LIT0iYUnqbgqtt8JT8BDjsRBRLpMUZiJgz3j7nmtm2J-Lmq5d-yJ6quD3tZF-7RoFCjfGLFton6_PnxmYOtQeWtN0_KRNkzrZnMlQgRP2y4VFnpBtgtdPwiY3Sge_A7LAcUnFRiWNDom-oWNxI0S1ecQjCng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf87a5e3b1.mp4?token=kVDCoZDuqcOCo5rVixTsqrVnak-IUXQ9_E5MQSaaTy5FXdbu3GJa00NC4xDf3bR3CD1ISbQgUMTN7f5NH1FYNdJx0T3QlBbjH8ujD9ayHawN62d6Fy5-e4DYBVgyM7xvQ3BwkM1zr1L9XNpuIoN-f6roqiy5CTjHztq6k0ov-7tc_43ekCxIx9j4i7LIT0iYUnqbgqtt8JT8BDjsRBRLpMUZiJgz3j7nmtm2J-Lmq5d-yJ6quD3tZF-7RoFCjfGLFton6_PnxmYOtQeWtN0_KRNkzrZnMlQgRP2y4VFnpBtgtdPwiY3Sge_A7LAcUnFRiWNDom-oWNxI0S1ecQjCng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آزش آنالیز ببین کاراتو تروخدا
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82986" target="_blank">📅 18:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82985">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ویدیو جدید پخش شده از نازنین بیاتی کف تهران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82985" target="_blank">📅 18:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82983">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gC2FF-5uDHdxEtRKWN2xerD7tSwa3LtyyzWT9P210-veutEE_WdZNR3JDCxO5wTlgiLE8sb02cmLlQ0-9mntRTsSsLz6c0NQS0oPHvdIZdrfPOGsyLV-Ftoabw86k8f-t8GU3_lmyUkrogZaVCZSrPsJAu08ILp3laQiz5WzRfTg5Ax5gKHAWp4-FQCfpw7_dqEmMVscfm5-KP2s2zVwbJiKplXEJtRINzNg3qUe4QGKycVRkRE3XadG_aiVoYzVIS64xsYTBEMs4cUBQ2likx6_xgtjJ7acWQOjxcDjqXo4-w7Ih7uu1ufKEAwY6l3yHkHOyrjtqBHcgv8Hzm5Pbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34b684e1d.mp4?token=dftYb70q8-hr7dPULEW5c9keoVHiz55wIqDS76KO8-mSzIc82ZiPnqdR8J4oh8F-1V9DinrkwXW676vc_bP4_w17lHZcwDsiydh2E7knyTKzRuiwaBQWQodv_3DQb99ST5zrZBUWJVI-B9Dt738nKcmGtwTU2lBaSocUCnwBLppelVWBXsOA6VutkUPD5IETxNFesP49ko7WqyZyvcr_rRmbwKWfPfmPXfpMNfkOv-kFabKxhtMPdaniFbmdNMAvg-HHdQ9ZWfmEzp_isLpOsDXT2soBu9TvZESmvhggK50ZHaJp-AF7_5F0g-AyJTzGllsiaCrITxI46vxMxKuSDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34b684e1d.mp4?token=dftYb70q8-hr7dPULEW5c9keoVHiz55wIqDS76KO8-mSzIc82ZiPnqdR8J4oh8F-1V9DinrkwXW676vc_bP4_w17lHZcwDsiydh2E7knyTKzRuiwaBQWQodv_3DQb99ST5zrZBUWJVI-B9Dt738nKcmGtwTU2lBaSocUCnwBLppelVWBXsOA6VutkUPD5IETxNFesP49ko7WqyZyvcr_rRmbwKWfPfmPXfpMNfkOv-kFabKxhtMPdaniFbmdNMAvg-HHdQ9ZWfmEzp_isLpOsDXT2soBu9TvZESmvhggK50ZHaJp-AF7_5F0g-AyJTzGllsiaCrITxI46vxMxKuSDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید پخش شده از نازنین بیاتی کف تهران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82983" target="_blank">📅 17:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82981">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPnkCzNBtTtlv7SDo1v24WUyAXFXihT80motV7OhDMfu_Jv3teYjWdF3GPsQOg26tl2Xvfe9D4tJqfC8r-F3eMbzmL9ih3KdqvJDgafAA7LlCa8xpzrDXeE6-kKYw5R3xR-NOBFy5LpBj_TteqhWskxkBvCLwB8F-SExf2l4hHYQxlGUatHt1i5xNWJ5LSfn1H-1tbtJs1hn14A0xLKsPOzMCMwijoxbCk7nufTZxCHWJ1HzHn5kMoLWU8yHqv5zze43_HN_7f9xR95zey_kGaUBCYnpCutttjqIkWfbLgyRcYcNdG_aNwbn7yUBix7NHhn0NT7nr-WXuVUcJ1prvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش و سیا به نام “چندتا؟” ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82981" target="_blank">📅 16:38 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
