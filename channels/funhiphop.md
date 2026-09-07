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
<img src="https://cdn4.telesco.pe/file/Bc2ppDu7HewdycFybn6C2p5tCxweoGMEVfo272MzeBpQ44qzQFhujPQ1B1v45x1mcTjfE-NGoMlVtoXybXPZmmGrhAjOYgXrjUBBWMUXSuD47oRVIoh3OlJNTchGjfDu0jYRQscJgpThC2CU4ObzozF3omDk9HLvSbz4XZCXj5jkpFYzGDIvltL4DUuSQNAkvdR9NZ10rFMknttZC_ysAO10REmx-BHwnbNpWi8U1Hy7hemOhlaxJB6GCuFb76C1_5Vs8Ysg9aAtvHrp8TfKpB5psn11jSzGhll5lkmOUrSzqSHpWsy4cxf57G32eU1fHnVZP-wxZWrMwoY3Tr9OEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 19:42:49</div>
<hr>

<div class="tg-post" id="msg-83110">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">چرا از کلش آف کلنز حرفی نمیزنی</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/funhiphop/83110" target="_blank">📅 19:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83107">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حالا کاری ندارم ولی آدمی که نفس میکشه قطعا عقب موندس</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/funhiphop/83107" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83106">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QClnlCTqD2QOkhAHhDhTdcLt4t7v5Y0YRvFiEuqhlf5L3zi3xydl7gw4lCSEGsw0VwGlkB6lCE6jvm1ovMW3joH6Naz_T40r6Kf_xyzCyc1v5TN1BppokVGNbka5gbPZDoVF09M83wYMdmgwyyW2dFNFEI6GYjcs9vWFWVz23M0oIOCTi9aoT9fY0bOfn__FPuFV6rNmg_hZ5GoF3xwMumfWYVHfQgGc20Xgd8M0u2xfB68ak5Oq0x2YIkyhi3YutkvIxY2MSd-JVQEOrM4tegSD3yL1cCWx2jp5ntTedyTvpv__dJ1Dwa-8Gss-s-LfJcFyyiDvKS6YS67-Qf46cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقب مونده واقعی این پیجایین که از هوش مصنوعی کپشن میگیرن میزارن زیر ریلزاشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/funhiphop/83106" target="_blank">📅 19:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83105">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQrZj-lFWD6cdfI4tUE58sz0KcQEqJINP8enOUd2SDxd4qqwOHT7OVg_XNzAGG0jGlYl2nYGSeUpWSxRtO2u9_NNYV_Hi4lKp5I7ff_9j0t-raWjm6ADfFJKCP1iigukBQ9GYw-L4bY_vYNwM4VRhhxr1a7dqtYbDMAgtmZk3GsfZT7kBVQLklRIrHL968wpXcJOqHOSK2INQyQtMI3lYW-T5SX7ySFk7c_RGXOyPqi5zjOafryRygZQJ_WQYo__4OdGakO0qOwSiii_kQFghdKOUnFmdovJGOo9AyW0Chlg84xolCynCnQwtSfnAP43qXTNNt1wuexDxtaUv_z54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکت: پسری که اکانت توییتر داره و خیلی جدی توش فعالیت میکنه عقب موندس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/funhiphop/83105" target="_blank">📅 18:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83104">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=RKU1GQ61pbBYH_5kZPYUbzwSGPeS34XlwrqAx1xSe9Q3nCWSWf0LvFOMxhu_zLFcg9VXkg3EqL1nKopaGVlYmpX_Nuqw2O5tjR5r8eEOSWmQGKllNuOAvsQaIvvnpeoRwNU7tGG9aBkG8o_DZJD3dDILB56OlZmuKLIrf6i3N85sLJgSFMKS--l-wbvrGiheAq3CD6cgi4L9sjHl-elQ8kL18PFVSoZ5oMP8HdaveA8aOkpEOEMYPw9S7KBJzy34TZN3CZ8Yl7x1LaPUytL0ZFsGr57jmoCLSO4Mi-ouwA4v1KPYb6fRohCfQhIkdgD6e-oILOk72DK9cXkV8qwUeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=RKU1GQ61pbBYH_5kZPYUbzwSGPeS34XlwrqAx1xSe9Q3nCWSWf0LvFOMxhu_zLFcg9VXkg3EqL1nKopaGVlYmpX_Nuqw2O5tjR5r8eEOSWmQGKllNuOAvsQaIvvnpeoRwNU7tGG9aBkG8o_DZJD3dDILB56OlZmuKLIrf6i3N85sLJgSFMKS--l-wbvrGiheAq3CD6cgi4L9sjHl-elQ8kL18PFVSoZ5oMP8HdaveA8aOkpEOEMYPw9S7KBJzy34TZN3CZ8Yl7x1LaPUytL0ZFsGr57jmoCLSO4Mi-ouwA4v1KPYb6fRohCfQhIkdgD6e-oILOk72DK9cXkV8qwUeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مگه ما اینهمه شهید ندادیم عراقیا نریزن تو ایران و به ناموسمون تجاوز نکنن؟
هرجور حساب میکنم تو ضرریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/funhiphop/83104" target="_blank">📅 18:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83103">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlG86BAFwdGptEfPc-Jx8ZCkVpyW__Kp4mo_DpsIuKbVvIqnSAhVOw2gPMchDRCONCs62Qw6CMLZFoHgvAY_jRUX_ofFlEQsltvnVlquzwgsGkwxj28kAGKGGETpQG_2q_dVj0YyXjg2vS-IaOux53g0SyPcNM-Y9x8BzsVTWBmOC8r_Cp8j4HI6RwLOQnc2K5fxCiJQLCirZR_zb7rNJop_NCaS3zq7K7elImKXuKk_qNzs-amEk2yEKY4JbwWq0ysMsdhmqQofldF7RVkpMoSw-lDoAIXZ8r0Rc6EPgLwi2ZlSgpOVqCJdVOEf-zOsESYZd6b-kPLjyYMPltXNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
😢
سرور فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
🔥
کانال اطلاع رسانی ایران:
👇
g16
🅰
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/funhiphop/83103" target="_blank">📅 18:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83102">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">امیر پارسا بگیرمت کردمت</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/funhiphop/83102" target="_blank">📅 17:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83101">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">شین:
پرتاب موشک بالستیک در هرمز.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/funhiphop/83101" target="_blank">📅 16:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83100">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjjmXWkHit-6Hgnei7X2DGht5HFnCRwefmhlKGGfliq6uzkqkCAdicKr6kE9r4jPqktgZInwr9QdURUEJmfD5lq6gDdJTHFVm7sZgNNq2A8vpHwlVSxMeh31f36IPlkiwgszhLYLs1e6UjsrB9mx8IiQ2ek0TqnAXkqy6TVJthXuclYhyg92fmj3XEIke0wa2pZdJntisoFJnwy_Q6r7oSn_roe1ylND68R57fzkRj1li7iMPWufI0kowbQGBcDW_NMWZzcn3mHrBGObnarCv5S4bKb5Mb9WU8ddFzWRWG2otchU_I7gLBk80QB6uHdVuw23mbD1rSV12b76ySYgyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاگان بد رو فرمه پسر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/83100" target="_blank">📅 16:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83099">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKzJ5nIoBT_1xRw82qwfRO131NUTv6szCxLyACMLdCXaP1MKiceEIkK6fCZsIYUnjmBPUvw6LXpMIrdGzX2Ceu_fomm2ieWUrqYbA9Jmdqo-iFYVQfElIMCXdS7hGSYMR4cF9V8x5nBfkq_wWYqa6mWwffUuTcb8-L4Wzg92Yri3HSqINoLkbFtaWYcKhcn1aRL8KxWN9AtYcCigFuX4YASF7dfUoWhdLb_GQEplrOK5lWTEOfv7i2mhhpU3-izoeHd79v2DMY1Qz21VUmq67IpAf-P8atdbPfP7r2ZwTz4_Xxmc3hxR_7qIRMf2xf2aj8h9d1sQIxYnZFrBjilmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرفان میرزایی، هنرمند و معترض جوان که در دی ماه بازداشت شده بود، دیروز مخفیانه در زندان دستگرد اصفهان اعدام شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/83099" target="_blank">📅 15:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83098">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ناشکری نکنید، درسته دلار نسبت به دو ماه پیش سی چهل تومن بالا رفته ولی نسبت به هفته بعد مفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/83098" target="_blank">📅 15:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83097">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ویس جدید علی دایی و کیره خر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/83097" target="_blank">📅 13:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83096">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ویس علی دایی و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/83096" target="_blank">📅 13:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83095">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2b3362cd.mp4?token=hYEjlHzHPwel6_OpVaTTPZgHgndT8-vC3Ttl2IGBhFpzNNLTpLA2-3ilaf5gNir9hwfpeHfAF1rQJeQepJtlIrq6m5AYbLKLdJKSCf_c0r_OzRHpCb2c0A7BgLpffjK4WOCrCB5-MlUZL5rTYWHJT0SIRBnAiyhAn6Q4t_jqAMoHlanlZnMX1G0LniR3dCJK0y5xeLx8oHsSEU0G4ICVVCU6XYqM-uS2fkLZFPYFlh6RYvJluugQREFW7KdWQGSEIQRw6QwCRceZ6Vobg5DeEjS_KRk7z8514EPvnzl5tG9TzlsLWmCW1ZrLlTh-pdQWFO0DpVs7pDicyj9WJ0kzKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2b3362cd.mp4?token=hYEjlHzHPwel6_OpVaTTPZgHgndT8-vC3Ttl2IGBhFpzNNLTpLA2-3ilaf5gNir9hwfpeHfAF1rQJeQepJtlIrq6m5AYbLKLdJKSCf_c0r_OzRHpCb2c0A7BgLpffjK4WOCrCB5-MlUZL5rTYWHJT0SIRBnAiyhAn6Q4t_jqAMoHlanlZnMX1G0LniR3dCJK0y5xeLx8oHsSEU0G4ICVVCU6XYqM-uS2fkLZFPYFlh6RYvJluugQREFW7KdWQGSEIQRw6QwCRceZ6Vobg5DeEjS_KRk7z8514EPvnzl5tG9TzlsLWmCW1ZrLlTh-pdQWFO0DpVs7pDicyj9WJ0kzKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/83095" target="_blank">📅 13:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83094">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رپر عزیزی که دندوناتو طلا میکنی و میای تو خایه های دوربین باهاش فلکس میکنی و به دشمن فرضیت فحش میدی
بخدا نه تو ترویس اسکاتی نه اینجا آمریکاس، بزار درتو</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/83094" target="_blank">📅 11:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83093">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v016_xE2WzqL0a683DkACGNlfMEBNybfgYV71brpgIbdfSOciWekZoe4QOgVseOJjQcWcqp8J9d2vaQBco2F_fmmdOCRqany0FCvaagaXyAFCKMtOfQHrCujCLgK4qeC8D-4VjyCOMvHnu4GhdD0bVlXxHk-zEnKHifUNkLZzDay5NlGllxTv7lt3_YzyANExsH3fTDxhIPb-0b22tOGBUYR2CCWL1Kh1Jy-jQ-ThLoenx5eq6a1YdPyafzELnqUDq2y7ogJraxaCg1JTVA-XeyNgZ3DrjUaKOy4S1nulG3lINK-GgPyNGxZwDo0q8DNz1KtHSqXZ0dTfp8USCjLQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد عوارض تنگه ما چیشد استاد ما رو پولش حساب کرده بودیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83093" target="_blank">📅 11:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83092">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">#پست_دارای_محتوای_نیمه_رپی  شاه کهکشان راه شیری فتوا صادر کرد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/83092" target="_blank">📅 11:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83091">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vja_UEDASpkQLUl8l-rISH59hWXvUm-aSbPhI2-8g1sJSawT_Mjnm3nlP3oq1PkrEHK_XJvgx21IMVgQp3kw2hb8sXW4OwLvXK02UaequFu98Ph2OCotxrESPMGd30QBugQZlZ8T3Cv8_wICZ_JCuPzZzFF-YCQJRt7Hx3ZAaYq0EY4f5MCSM-pet0phjVMVTAwt5lorSrPwwxKuMH73yfdH0yiRK7Q5GFw8LSCzCLjK_3V6ealCYfnnv_MDiwqldrXgUK9_Yft_XMkk4rL_QDvot2vNbDFP2oddF0nd6a7BDy1XsB4yf5-e-Xat4EBOLUFO8B_Th5fxRFxco-SWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پوتک به نام TiKToK منتشر شد
YouTube
SoundCloud
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/83091" target="_blank">📅 11:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83090">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/83090" target="_blank">📅 11:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83089">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/83089" target="_blank">📅 11:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83088">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tobI20tTQx7j5TV5V7wEESP8FWkSfFY3GIuOL93KhzhKz72p61MYRrI34W7--bo3m2crnt7TwJbyHt_9rkUVMKZkhqkjmTSqlStTLFp9VJs2d-yi9oap8dTOU4dVTA_EE9yWQPNyrDAMZDSZgVy-9HKxigw3ftMzmDGBI7qjADjFKuzLulpDaAJUbQM9KTbG0NjDQ28jG6om_L8DIgxTlZCIKo0TfO5ssYxNTpQ4F9n5A8OmxaRq-eK7qiYqfrd5zqvQn23Nn2jHCu4skYUYHkDOI4D0pjdpZZEJQB6F8j7_dpbwazLPzUxEw3o0mlw3nTzUbjE1Kc1tARMPZjHhwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پست_دارای_محتوای_نیمه_رپی
شاه کهکشان راه شیری فتوا صادر کرد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/83088" target="_blank">📅 11:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83087">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLFtPDcf2Xn6NeKtKzFfzKxQ1dij5KdZth1EmuiGyT8CdIKIK5eo2rOHOE5PToSoL3CPVsFgX0h1Hi_Y4v9-uc9xukqNbYZ3G9QoLIre3HY5A6i1_HyDCQ2gBSTex_Pl9o7NxbSkW9xfQXCWy_ochhuO94BUpUEO4lKxoiGonjrOFVEpqHhGa3eVaVRnREChrFLAiuRbhZsyn5blACCT6FzPjPp5puvIq1oLZ8BXIL__7gd1Bjxk-Jvg9aV3i6PXsNjnhvEfkRnttXGHRpK5oJUQwMMU58Y-0B0sCVZi48NEqkcstWskYXsmA7b0s3NfClIoXR5m84xpRwapcFEojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحتون به زیبایی و درخشندگی این تصویر
❤️
😍
😘
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/83087" target="_blank">📅 08:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83086">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مثل همیشه درست وقتی بهترین املت زندگیمو زدم فهمیدم نون نداریم</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83086" target="_blank">📅 03:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83085">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اگه ناراحتی قلبی دارید یا با دیدن صحنه های حساس حالتون خراب میشه ویدیو رو باز نکنید  یک جوون تو همدان به دلیل مشکلات معیشتی خودشو آتش زد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83085" target="_blank">📅 00:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83084">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83084" target="_blank">📅 00:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83083">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrCLzbm0vjfUvmGlcoPEqPgbwSDbCsE-3rSHP0L9ivHqAq5Fcw63jhY_tu2ANo9YitEhI_09NDRS3sL7P3AYBEVTCNFhNUU-zvBUI6gi2DgndYoMgOhbOOzLuoIc0p1H0x_-kAj2uC9e5LBiTuVDcwSeyZEufGW6bYxZd2JhnV2hjoI2qYevY1-ojJaK8LIiFby6ucjwc8Bk_QUbtgMdDYOTsSkerXu2Y68DsSKixxymgvZEwB9dMRAD41M0B4bvOSX-bd15ppQx5B-_Gt3DdvDN2k7FJcEes-Str7KJeDv_jJSNT4TX8f3dQGykTD5kDF2pUvKceJVUBlysIu4ExQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به ک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83083" target="_blank">📅 23:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83079">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83079" target="_blank">📅 22:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83078">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kke0aDMCxzfgsc4K7o_XuRPUzQ-zCvtaBwE9nhKgqY3tSY7Wyxo7Qnyk4Lx7dkALxe3YT4_HCFh31bo44Pj7wIb0EHh8zGrTT0BRBLZ2wChm2LWjEbgcEMX3rPh1k6AGZbICNsCsN79qvNK5rLDZ-ZDzIczJTEae3DwDD0CyVKuvVdIfqo6e-KBGoAv8CPUe3tWcisqvDdodbCgUIbQhIQhigjnRnVMWi0IgVogBhBoHAlY9_ACIuUa1EjE6UVu8aJLPsZwZqIJ1r3iW13Ic4dufZS-GfnMWmSuVxGajyVZP9ogn7Aaw6qvsVQ3LVAPXCwBnxse6g0Id7BD7FGPclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من حتی خایه ندارم با اکانت فیکم چنین کصشعری رو پست کنم؛ این چجوری می‌تونه به عنوان رئیس‌جمهور آمریکا چنین کصشعری رو پست کنه؟  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83078" target="_blank">📅 22:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83077">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4scmUb5IDMuI1TQ20zqcxWtAmlUsXFAfGXG6mxW5IV1IpXJyd5aNWZn-rshgm1dQ1Gcjd3ngWzs251zg5M9-RvXO_rCGBz-0Tmwiy6K5B8dIwzRQU9HAih4C_i6tpF3TTiGTRCTwb18Grp8L8y0IiWv30GYIoN8TdZStPLDS3eIL7etuCzGuSrKb-DTZTXWRlwhbf01JGc9-krhtyy08MObwHvG-ZIA3BM15qLwVc3XmvCfO8R9xVuRFXztfXN0mzPCWVmKMa-x9oi2NKQnBpq9olCIHw79gTVzWRhU19F6ZOm1LAJZB_LFvbMjsmM6F4hDfwqubOrpxhJyFivXOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من حتی خایه ندارم با اکانت فیکم چنین کصشعری رو پست کنم؛
این چجوری می‌تونه به عنوان رئیس‌جمهور آمریکا چنین کصشعری رو پست کنه؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83077" target="_blank">📅 22:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83076">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">از امشب نرخ سوم بنزین ۱۰ هزار تومان میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83076" target="_blank">📅 20:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83075">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2dxdd6Q_jKUeO6M5bDpMUYGIHjrLDLSxT2ekFo1cL5hjLdz1s7anoh3vBG1VOD4P2XjYW6QGvlWDkTrtya40R9Mamy-04Mgp-5ykPAz5NvZ1dCrHLDNshybFoWXiVGo3d14V8p-Y-XrNnb3QajumEMjMmTn5PLvkAVpuiSdcSYa0c2OqhYJd90VByI8D-26VUKvLdzm2xFboCbIDnkj53bJh943ajqmyrPXMfKLCxHg5BdixWwvAkwG7KWTb_rMJq4KJX5mMUFkJ6xvzsy9yRzJeoQHUim6aeFzwVro5xHGAiD8afUJLGwbdoHeh4xED2w4fnEbXSqM31U2E0B5uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمین صبا میره براتون نونم میگیره</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83075" target="_blank">📅 19:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83074">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXAMpcHbhNO3ede7uX6yoixJJQt2zLQ0Ky-_XPLILFw_vke6fHnRDDMwviWWUIsiRrQBsqDLss9CsqrwiySyCTflEVYAH0yrKKkiq8YL9wkR8Xmd0TejaLI6aCVsQNET5laA8324is3Vf4ubzasitBym79OVS2ul0PSZoxcT6l71TWGf8T4C4WXlMVlOuIYXMlLbo833neqWSaLcG83eIruQC2iXBOb8dXPrMkvcSSoXOvHrwVtopS3Dz3HQA3V2K5fPPP4ut92ye67fLGNiTtYr_tN9FpYlWjEPIwexJV47ChJOEOs1BejhRSQ26EAOOMvHeEKlsIJaLscRQ-a1Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش به خدا یک هفته از درگیریت با بسنت گذشته،تمومش کن، به خودت بیا
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83074" target="_blank">📅 19:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83073">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کصکش پا پرانتزی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83073" target="_blank">📅 19:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83072">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">منچستر کصمادرت</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83072" target="_blank">📅 18:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83071">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLOhKtrEqSK3EqXPVIN-qdrnLERA7ViMtHydLeeQSStOUy0yM5umbpBLNCBEgfdV3I-yYe5Cpeo-oeZmnwtk5rieOeedT31FDEr90fDU6qSQv12FaVljxhtQ6c4GzFASbcgcal4pR7FcV9C53XNO07-IudJ4ufHeLPS-naPitKKOVFfAoi7kWtPeS9UQz6mTobw5ToMQ_RnT8p2p8oK7eAch0VLG6RsdjPyj3XWm_0W5doixV_qVqyNzc9rY1L8fZSy1Jn2gl3kBqrCTxzBwoib17hu7rtkxcBhMwB-8m1S7JfRYC3frzoBGzRZWE0BCf0vz-xEkphmJzEr741Xj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز خداروشکر گفت روحشون شاد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83071" target="_blank">📅 18:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83069">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فرمین لوپز شاهکار بشریته</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83069" target="_blank">📅 18:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83068">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZnIfIjTW0jubKhmjda93TcPT5pOAtPhXVxzJ7I4GuO7erY0FySN1A71iW9jJcIJ-VJ6Ud9udKXYBJdGRntydoI3jYCXSJjmB5FFWaGZs-bCzTEbcoZMFZcW0ONcvg3dvpUl7E289zwN4o-q8wq0XnwaKK4MoPpGMl_GeMtuhEJEnOxU-hbGe3BMdBPd-EVWku5nEHBXqnIVOnZKS2FhYvfAaHvDVSXqTEcs33_Ff65u-dt47REHhecKTMEsNxXyeFx9iuYWD5wTb5QqqEy_jT7bCY7VamI-2ovMrt6xyKCbO3wdCzDaIe3Tb6RFstJ61ibyYgrhzwm3wIZh0YtPpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداشم آلوارز نفوذی درجه یک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83068" target="_blank">📅 18:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83067">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuRzwLhF5G05ZYjiLxLEmGWqAJYtSalprV3QpUbrRNqmZRWRUbYQuBtP_wNycWd2PHEVObIgYVBGNY_xcyB4NqZw3z7OlpSGRuYlknUa5TqbOOsI6BIHnypedCjkbUOf54GDEKf9XZHEYdfYRVVu0h96eN89ul5O73aBIqy23mbiCjwR3xahPFDU8efzIcSHxenuGgONuEFfaeJeX9tvvdi8EKvYyIR--QgX4HEkLWi5eLnchAVnFDBb0BaNz9DL9j-2KmccfN1NlZEft8twQIi-kI7LF9b9hrawhpMJKB0jlmbk4QXHHeXRrjV1uYpzPYNGB-_5gDdwHi6iuDu-sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83067" target="_blank">📅 18:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83066">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXtakQEWcgkodCDwfP6dvlGXa-axYtPRfnjGVVGFZbbjSQ_jKI6dEMsewmwvh78tFdqVkKmga5YP5-U5lOW8oVSovbn1Eq-zcH4C35okPMN28l8T4Qoh_JfDvqZcpVh_hrxP5wjVTZtQ4HDtrm8ZEM-A8VveMXZZzZzduwIotSbCFtnwZ9mmg5Prwtp50e0fi-KBpk-T1NLv5jSZuBDlCVKRmBeCUn7TOSbpsL8yO3FP9QzI8O1bUaZxxlfJB8Bi9mb7ooXphiTmG0LF3wGR2C0cq1J2Gh84VOqKyMaKCIQ6jSyVElrqNzgBtJwHU6yhB_10G-oqNhGRkbhozB1FIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بریم واس شش گانه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83066" target="_blank">📅 17:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83065">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnNgX5xUpj35RdF95l87mZec70QYyjLGXWsjPQLD7yEQzvSH74rspSKgJiu1zqWxGVZWpuc9akgnqEa6GzVUB2TNjFR-X0lVAg1HwEv6S1HHmgrFpIOsoQzfdoSqAzgmq9BHU-mXzwj2WO964WQ-zZvRPL0YNJhqSkrCJFQXvnzYxJfsR26kUkudBDXIpMgmHz8SgXL-NAOJ913zQyD7gy5bVu4TTl9KUwph0PZhDgDnazLIi3hO64_6XMyQSuhByO4YsjlyKWAFS2wqlD2D_iUPMO_FfScG5SCRH9Pr1TrC0iqxHPw19TTNgi0drNekodKB7CaH0hZy_-b4ukXYOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به هیچ عنوان برا تازه کارا ساخته نشده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83065" target="_blank">📅 17:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83063">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAzWV7nnxY-USvLYdVuT7x1aX-YqSmIcYPBpWY2lcqXnB7aKwkmM4M7MzdfAn46PwTraiQKv8o2LxGYCy0wDPrMT7c-KZJEcJqHX-sKzvhQ_afir3Jnx05_y8rFh8mPI7GfJqFERIgYcN9aoXD4jKQaHp9jJbOovxrXEbvz2_fmHFm6npSeWpo4vBDOl91MwiTa8oDXP4TrxpnOm8EZRL-f25bUFWgGZPq2UvGJ3uvYucq4OMvU_WMzcobhgt8Q--leuzU2WyxfxKPuZVXmcAtAmkjWXpTapqzZ2BmhcLF3cCa-w-b8Pbe11ZdW6uuzVY-AAEtLd0zwdauHBV8XHtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff0e768cc.mp4?token=C9G_QMwzGz8lfDtLIKTErOgCDWDHXCC6s_zTwIYva8r86PV5fTDRY9x7-e8Nsmy8C5oSmClyeTgoAwjBHAhcJTB9EKb_iWFQJjuilo9fjBEX5k7njAJQ3l3R3WpD0lcEQ4gEyaG8delzPfz7ToP66Od0aDBgdgwkFu3Jbui7IZSfDhOzwhfh-XVUVv4tspbEBtUw858odsi8m5z3zwDd2u65LSRi87Iwgs6L4RrEzdFvEHJ6QmGAlSBSkpWBUpsoRHnqNhiGNb33PvneaOBH6MhNrG3TekfVt2TY2s7_fCJmxt00iqVkFraaUp4ZDo1-Xk-LpqB-fD981d52ZFoh4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff0e768cc.mp4?token=C9G_QMwzGz8lfDtLIKTErOgCDWDHXCC6s_zTwIYva8r86PV5fTDRY9x7-e8Nsmy8C5oSmClyeTgoAwjBHAhcJTB9EKb_iWFQJjuilo9fjBEX5k7njAJQ3l3R3WpD0lcEQ4gEyaG8delzPfz7ToP66Od0aDBgdgwkFu3Jbui7IZSfDhOzwhfh-XVUVv4tspbEBtUw858odsi8m5z3zwDd2u65LSRi87Iwgs6L4RrEzdFvEHJ6QmGAlSBSkpWBUpsoRHnqNhiGNb33PvneaOBH6MhNrG3TekfVt2TY2s7_fCJmxt00iqVkFraaUp4ZDo1-Xk-LpqB-fD981d52ZFoh4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی عشق ابدی براتون رپ خونده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83063" target="_blank">📅 17:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83062">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ساندی‌تایمز: دو تا آپارتمان پنت‌هاوس لوکس تو پلاک 3a Palace Green لندن (منطقه کنزینگتون) که برای مجتبی خامنه‌ای هستن به فروش گذاشته شدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83062" target="_blank">📅 16:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83061">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">با گوشیاتون تو شارژ کار نکنید که وضعیت بگاییه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83061" target="_blank">📅 16:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83060">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b309c1c56.mp4?token=Vs4wbCQdU1ECMB3ODFAnGH2oFEgmNqub-hLsgNdvPY8CjHkaw4j8EVx0aDKv-lH5Gabdpp4aOQ_EN-WnTzfvCpO55mxCi4q_ezh2UcGYIy8uX_A41aiM6oYbIUph2D9QDxUF_FoQMDhu8zgspHOnIQmtizhUcucpd3GNwGGDRHxaBNDe8m_YGzLDzc8l7bF8WUY-XZTikHDp7IAEynRxcUue0i2eSi_rMkPW_ltOa21qVpzuGfVb00jsHgB1iiVWkPxo1Mz69LT3yquW8JEwdF5X5ax6UqLBC9NiFJafJCmKXEV-VzvSngw6tvv_gfEmFlHlRTADv1EHTRsskfBQ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b309c1c56.mp4?token=Vs4wbCQdU1ECMB3ODFAnGH2oFEgmNqub-hLsgNdvPY8CjHkaw4j8EVx0aDKv-lH5Gabdpp4aOQ_EN-WnTzfvCpO55mxCi4q_ezh2UcGYIy8uX_A41aiM6oYbIUph2D9QDxUF_FoQMDhu8zgspHOnIQmtizhUcucpd3GNwGGDRHxaBNDe8m_YGzLDzc8l7bF8WUY-XZTikHDp7IAEynRxcUue0i2eSi_rMkPW_ltOa21qVpzuGfVb00jsHgB1iiVWkPxo1Mz69LT3yquW8JEwdF5X5ax6UqLBC9NiFJafJCmKXEV-VzvSngw6tvv_gfEmFlHlRTADv1EHTRsskfBQ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک به قصد پاره کردن کون اوبر، تاکسی های خودران تسلا رو به بازار عرضه کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83060" target="_blank">📅 14:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83059">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szK0WTG8e7lG5XjR0GXeMrPDlwbLelktNEbgxFowuXim0Q1wqitHlQmPE0eDtW_XBKNz_QkzcFKECODYqB7pY4STGALrQYFwP8tWBYrGMViNICfihO4Wjyfcu23wZe4jvuo1VYvJgkJXpELB-D6_leUnud60PC6J7JUbcRDxRAxYE2qUYlAS6ghbFAVGZBaR2Co38pzlua67ZW1CA203xfAulk7H1iDR4eeMohFdh4yn6sOuD15fhxYsVeftzyeQYMwMR8navCd9cwou90fEI4R4RyYl4WLIMGswk3ZhZpYDFizzAU1P8tL6ZldFlZhtAaODjJA8W_TzIJBSgwxcuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمینای خبرگزاری فارس واقعا سطح طنز بالایی دارن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83059" target="_blank">📅 13:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83058">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دلار شد ۲۳۰
ایرانخودرو هم اعلام کرده میخواد کصشراشو گرون کنه
عالیه وضعیت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83058" target="_blank">📅 11:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83057">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxJmnHkrZPyfgh28gst7BvWk6wcB3A_4IuGDDqu1ECr21adcw4sidwCtBIjSieUBYms66XhVy-3Lh3FErqI6XXg8_nhBigJBiJ7rckQMJ3UABd1s6_i-5vu4j1tLorAjljZg_UE8_nxiwlZLglCDDz84UO0fdPufYQMx29qljWtamnjMxxpa9MVVdxHkubGfYTOGkkIntam08e5VdCdNMgbCFIDdVu4nBhlv-f-iTUMemReOqrjh9g-RM2XifMvvB_BUkR70LRaIs-FOiQFpFDo-oMC1vo35D1Uh-rOenSBDu9NQC0S-fJVfor82UMuPPHn1_kLmZD7sMAWrZzAtnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردن نگرفتن همیشه از صفات بارز کیم جونگ اون بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83057" target="_blank">📅 10:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83056">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83056" target="_blank">📅 10:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83055">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83055" target="_blank">📅 10:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83054">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83054" target="_blank">📅 00:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83053">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">قالیباف: بستن تنگه هرمز به ضرر ایران شد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83053" target="_blank">📅 00:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83052">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اگه میخواید عمق فاجعه رو بفهمید باید بهتون بگم که قیمت دلار داره دو برابر قد کاگان میشه در حالی که پارسال همین موقع کاگان ازش بلند تر بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/83052" target="_blank">📅 23:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83050">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZw6Kt63hp-pL43cAJ109jgFz7b-KqCK0w2BVnUFkqLaYADh0xiDK0YFtJtSxuDnsWSO4k5T-mGSNKPzpio0uU_W8nb3CYf32Jjt7Wpr0PEOzbXDO4bKSpJbex8I1aKzrZVXzEAm-HjIztaYsf7m1oqmuZtlawXHqFX-uDjYy-tWGYztFG68LLckrdaKS0cl0xOkm5-AcqfAdZHSV9uymHAgt2CtNIRAq8IEIl5Qr_k9Fj0ZR18YDcXr5RpBCUIWNdlSNgpxiGNX4Jw1WnA9IYOnKjt99WFBFMQngFIgpvmeZaJv7600GRvxHH1WaY9hRIYU0eNfugzRj_H9e6SqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUybRPYMc7-kvmg-Dygb_ZmVTmUgJM7eYv3KYg6WU44BNDxJg1GpQjokcE6r1xYHq9dDpZSq7iV6ypL8djSnXCTHUh-QCmge3oCxVliX7yFLY79KC35dW0mLGqFrzXe2GhxpVIgKpfMNVYDoGH2Be6q_dPTuYD4iOc3plhCukHu6o6Vi7AocaDwvleP8Vj-fn4I5Tr87PMvTY21DLud00SX3v8perySDoB7Wl3YQHNXGNdEJwbIMXtxdoRnqHB5E5o84ZFTFPhRoH1JTog8dR23hVMGU3st4QLssKx-5ZsUisn796FbPqUoCR0Ox_8rVjX0z_sLBu3c3koXj1hSkag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین تی‌ام و سجاد شاهی دقیقا تو کدوم زمینه یکن که دارن سر اون یک بودنه باهم دعوا میکنن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83050" target="_blank">📅 23:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83049">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">درگیری بین نیرو های انصارلله و نیرو های دولت یمن رخ داده از اون طرفم شبه نظامیای تحت حمایت امارات ریختن دارن حوثی هارو قیچی میکنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83049" target="_blank">📅 23:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83047">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رم عجب تیم سکسی ایه</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83047" target="_blank">📅 22:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83046">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">همین الان برق ما رفت
وزیر نیرو : خاموشی‌ های برنامه‌ ریزی شده دیگه تموم شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83046" target="_blank">📅 21:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83045">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83045" target="_blank">📅 21:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83044">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پویا رحمانی فایتر کار درست و مردمی حریفش مالیخین رو تو سازمان کشتی RAF شکست داد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83044" target="_blank">📅 20:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83043">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtXjULyp3SGsFn2EbJGa542A_itP3wFnKUitphrOjiWkA0mVK-juPzl8W3imp1WwzTEZCykEIzO-JpoDZku_ng_n1keulvBg6dnKZsWoO41s4vUwtYdNR5eK8J0jEjqaRPw3F4FYp0-G57CecG5JczgQ3-hZSwh5jhYq4cUpkIqKXhLV3GI5q93jUvMhiy_OUrs3Q9MHnADJnEr4ChCxNc0n1fAQbbtPh7o8zw6btFEd-LhsE_Bc-YZPCH65cAUTbgBiByx26z10vYeInyeUzIuIHHZNqqqJ-9bWm477dTtdtJ6E8bqXqWqjXdfxIhsAKj5mCzZQ50MFphMTeOD8oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پویا رحمانی فایتر کار درست و مردمی حریفش مالیخین رو تو سازمان کشتی RAF شکست داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83043" target="_blank">📅 20:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83042">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دلار از تعداد ممبرا بیشتر شد که
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83042" target="_blank">📅 20:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83039">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nz_VfakHICriXDLQx1jngZgYbSgTd0yqcUqT1vYMzFdZkplrkITGE7Jn5OGueURMqhwrFas3Ym8r92Nb2tvTSbc7N6HDh9xA7M0TK0jWqCyBB8wqHV5dt8bRokcVLmrYMlgcqOsvFrAqGke5pm8g-gJPFTEiCOw8WdZxOF3fnRkBsW-_wWAVTQDwsCEQ_Xy1Kte0CHGvFUrhBWR6Zz3XnY4fznmEmepiKrxQnIBJ26hzeleYNDh6taBKP-sfvLBDgDNd5-1oKtVLG_nXO2R-s1s4rlJyTSpvO_nOZjChNMfZmB9Uftgy9n2ricRucnJHcXTb44ZU9H8_s4jJNBTi8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkSs-stAyEBisIrV5NvpWJxGJ2YI8zk15JIz3trClCvFLOJiEtL9aFTJQerzA7V9SfCAYYoYKpZv-MxUJen8uFXo76I8nG51MynGvyYhcty4ls7QxE0-CkyACiboyHjZcx1tU6OImoFcGJBCcsN9iEL1kVhkjC3B0oMprhDYi6DHd3ZN9Ze2QlEjbfBqmQTpnewev2WraLc5jVe54kag85dBjF5uM8K7tloaA-jCuRIoBfNZ-ufnIvbQPq6qTNGOcHwHtEbUnDS4X4cs459CX3bJVN4PYTFBlxakLfLZneXHjR7wGZ78_whACDAJ1RrShhIfoaNkNKgYpCZkxKB0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q-q10t5kLAoknz852aVuyIS6b4CaIWx9m8_kpo1OGGpyXJlLKMpCJ8ASIqLeHt3ljffsOAnA6kbQ3EFwBVvdfOGX4zbIwTpfz_VKbOrHUnZnAx-fqGnGf9q82c1ZJS6g853IqeuvK8Jjg5PgCT2xOn6_5JDbVErk4dgFWKcysIlbGarlXTtZuZO2NeXbaV2XLEihPwRr4pROsComfff-PrIokpXXgpeVmZY7bVjJSyu2aWuH0nK_9rptdYFMKVXRVPAhoMOgl9yJg11FlneqwwsNhOQU7vgRWK4zC81cnNqofyFPqv_eXCsKHvamlDJToOPt9QmRX57pCGHRJ9nWyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تبریک به فوت فیتیشا
ترند جدید توییتر اینه که دخترا عکس لاک پاهاشونو میزارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83039" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83037">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83037" target="_blank">📅 20:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83036">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83036" target="_blank">📅 19:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83035">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تاتنهام کصشر ترین تیم فوتبال تاریخه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83035" target="_blank">📅 19:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83034">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حاجی یه سر داروخونه برید قیمتارو ببینید دیگه خایه نمیکنید سرما بخورید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83034" target="_blank">📅 18:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83033">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaAyR8JAV-OIfx4S8zDE3hMrEeeY-BVkfATeHXEQ-EQXCgiqAYOzFtoOBUgM5Lozu-jxuLYuaezLlTJZxs9jcoGLko_E9lNA09on1v38zmmIoDk2ZYXuETJn0dksQxsCK4uZfgORdnWlLqZVIYiROJQPErNUptKKQ6SxFsWLg2ivwkuD1J4Ah4AX_DKt22hTQu9S5_yQaWv0Mxvu9dkwCivswz05kgBeAU3H6hOWc5iuIFwGGyi0bAVCvfzwLVVkHsmGGS6-K8YaOPUX5QoeOqGOB6GtDbcnNer0-7dJAAL7IAes0DcMBz4kBno0dT4p1woTioIGfgQlvTiseeF9wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو بک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83033" target="_blank">📅 18:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83032">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmbQLvOTxF28mOdZsNg10pS2EPyPD6z_bxBEHtZkWuCA0sessNeXhSJ53jJRPb0q5Wm81vYkzgQ53f7xCl0dJKiynUO8p2S7AoXvw20BAhEd1rCtCEoWUlqs3xhqECHXur0kOdN9vqZp5QnhNf_2SoEPEud4SWZ29e2APh_dATbMQbPBQR89kBpbvouCqm9683vizetNAsr3CD9bnIz_0A6GXPwX8e1HvMuVqiuVa7WT1_fWYd3UDaZFUgqp4hOtplLpLNyhW4a4tYaYHgwy4I_5cduDTu_TUbh50ktlwnJliQ30MJc197lRDym_bYcxYA-Ki-FKnJd5nqE0RiNecQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83032" target="_blank">📅 18:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83031">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دالی  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83031" target="_blank">📅 18:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83030">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گیمرا قراره به آرزوتون برسید، شایعاتی پخش شده که میگن تو GTA VI سیستم قطع عضو اجرا شده، مثلا با شاتگان به سر یکی شلیک کنی کلش میپاچه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83030" target="_blank">📅 18:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83029">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1d45c18d.mp4?token=D2XxGIjSxrXTWGeQZ-VpXmYhCHB9gcU9rB1VakFmF6mwHACPqWdmMJNGsIFof4cCE44k0H8iKzKGaVXizPX15tEetc3GCxj37v1PtuyQSjTs95TPX8gWYDOxdehf-_rQeTCuf8Vs3bzQwiGgqSFtvgiqRA7Qbq_bE_2kvNBRfTlLOd3S3J_Wl4gDlgNv89XSZm9AROwr6nF1pIRjIpMqjDqui4cJ2fLMp0AgAM8EQGOSL85QgvbYTDdNxs3xMp6Z2_ezzOne_SefZSj1307cQBd3Yv659OzkENMESZ7gOuKwdku9zOoUyC3MlJcAavAUcCVtxyAEqfHxQJaAChX9xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1d45c18d.mp4?token=D2XxGIjSxrXTWGeQZ-VpXmYhCHB9gcU9rB1VakFmF6mwHACPqWdmMJNGsIFof4cCE44k0H8iKzKGaVXizPX15tEetc3GCxj37v1PtuyQSjTs95TPX8gWYDOxdehf-_rQeTCuf8Vs3bzQwiGgqSFtvgiqRA7Qbq_bE_2kvNBRfTlLOd3S3J_Wl4gDlgNv89XSZm9AROwr6nF1pIRjIpMqjDqui4cJ2fLMp0AgAM8EQGOSL85QgvbYTDdNxs3xMp6Z2_ezzOne_SefZSj1307cQBd3Yv659OzkENMESZ7gOuKwdku9zOoUyC3MlJcAavAUcCVtxyAEqfHxQJaAChX9xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اژه‌ای به هند سفر کرده و مورد استقبال مردم هند قرار گرفته که یکیشونم رفت و دستشو بوسید‌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83029" target="_blank">📅 17:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83028">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "ترور"منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83028" target="_blank">📅 17:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83027">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkRBDPLJIX_EtgBeMU_0iyc2IzsPOE1k7qZ2iojjjciZ9zLeTWZzB-tCxYsATaU6ToHhs84tW3q6tGxfR5vaiyBg_97kQQvN-vhzHx5JTZHasqM4hxOkc-Yj5dnUWbkVZISw3Bnn_T0B3zOPvw2ZBav2Abv3cJFSShherEJkESA9UQ1V5SjwG5ynJnGggJBXP34D0yqXwkssqYirvq_mBWQY77gHz6UgKGVdd42jjIlmaJgNiSfPXcF7BHJpleYCJ5fwPD5G5OcMkbgGfJ-CoP5cBZ37izTjq8EwEftrzp3bz_p2mHqe6nRjGBJbrpBuEjeTYcTI3cvCBxHtmGVsmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "ترور"منتشر شد.
Youtub
e
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83027" target="_blank">📅 17:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83026">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پسر میدونی چیه مملکت از همش عجیب تره، خبرگذاری های یه کشور با فاصله هزاران کیلومتری از ایران بیشتر از آینده اقتصادیمون خبر دارن تا خبرگذاری های داخل کشور خودمون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83026" target="_blank">📅 16:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83025">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vr83GDcdLhToAtop1AoamPEQ5VPdSfaRGk7X67iplNvUqPCEGFIZYg0X6fItQDg4hTouCRIdHGsH7YnEO8SGLQecpQChdoSomb40-ADqd_Xe41X7zPjZHS55j2Puyp6M95tBxa-xrHZOKc77p4DDYJ8lgAwiCZ71E2V-V1HxYxvvQShEVKy087EM_YNoP7cQeaZiGZcRbxqsMRDmYx4bBayiLEM_p14tc7bBl8XxyBdninUbb3SULuD6jrFXunbAI1unity5YNDB5qb4rLyFOvcOSzAFjOxqKNe9qGgujDESm39hfEwb_Xt1EVM5IMxt3YxcMq6UXA0DSlMdCo20RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محکومیت دیدی بازهم کاهش یافته و حالا ۱۵روز زودتر و در تاریخ ۵ فوریه ۲۰۲۸ آزاد می‌شه
دیدی پارسال از حبس ابد تبرئه شده بود و به جای ۲۰ سال، به ۴ سال و ۲ ماه زندان محکوم شده بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83025" target="_blank">📅 16:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83024">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFefNrQD3WqRrrFjIhR5BPXoOCnkT9EzOWpObxzfMXgrATNpymymB3aR2aMGY_c3yVSdRu-uGCa2giz8_f26X3hRqwQ_dv-T-UcYFTqZq8sk2zcsCEXby__3NmqRtb906Mlr_8lA9g0nTstfPPaJoiTlNDfyqkgOUrWfUFvWwBf9qkjygC9NL5JqC1kCWwQmaenYZG24suKe_Ci7OqZ3y0tAmULMXzgxXLb0DpdBXxNmAA6GGYIFEdCK96sMHIGD9rCSgsG18KxI5IIIOz90k7XOIBraYvbgEQ5Beg-hq4ipX1XFTHNqCDnCouxYSOyUU8bZ1NUhJ-C5eBF4BA9RBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83024" target="_blank">📅 15:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83023">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">به مناسبت 200k شدن دلار بهش لوح طلایی ندادن؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83023" target="_blank">📅 15:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83022">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1NlI-lyvRuKxR4H2_UG2EVjWY2sPFrexs_RdfkI8c6L6kgWu5e0-8f8n9GXOdIa9QvJPEFTUXEnfU7N6TW-h_Npe2uzDjRRJMzETDGZxReILM64jxvwihogJd26XMPuQdozsFa04A_Olnz996SPPdMREeUelEsBLYrOaJbFg5imTbWLw9a46_pQg8qHvfoIQWxUopp-Xs8ydPOK3nDcIEUHz12DrzD_yB7sxRvL7CzoWCIb5mrlwFt3VtKEuOa4rsNNJa3xvbNcNLGq8plZWMAcZwywQM0UT-RJHthIABIukpMqFQ2P2u4tOXvtQYL5IHkkJcyeIL399L9P7Wu-Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83022" target="_blank">📅 15:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83021">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">البته در نهایت این دختره کفشه رو خرید و به آرزوش رسید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83021" target="_blank">📅 15:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83020">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDrxrBSDVyQ7FGjvCwoRrX2Hd8k_gqLoze8syvOSSJMDZEmxl38vGSGCFICHqLdbUAqHe6eoCB91uRgiv1q9ApLDslDjT9K15WFM8hp7vkHc2Tf_Vqof29DXRr6KvCn9w35gtM9n0hXZXUIhNzGGptJKOtOeFhDghP_oTyf0eGmpbR9Lyv0xCUnwAbAIU2ojq9XKcQtDAYPgJL_gjhseTr2Rufiriy4iXNP8e1VgcJ67DvY1hEoBOLco2LBfnG5MW7Mysf8rxJw-6LD3XXLEyX8fTuwzd3w5wOunO668AmBjPagtRU_by9-US5DPWCAfmpYZbcGRxJfhtZvDwVKpLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو این خانم از دیروزه حسابی وایرال شده؛ داستان از این قراره که ایشون واسه خرید یه کفش به قیمت 14 میلیون حسابی برنامه‌ریزی مالی کرده بود ولی بعد افزایش قیمت‌ها، کفشه به 19 میلیون تومن رسیده!  اینم دیگه طاقت نیاورد و پشت فرمون زد زیر گریه  @FunHipHop | چمن…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83020" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83019">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd895d17e.mp4?token=Ei1KKTWAaBx4_X0z49oJ_dEvSfEi2w2qj6JOpNzCDqn0Qd8yjmcLJ33amVqgCbkoFBzmZFxxm-X8OcUr3ytzF_PD4dOe1ynR6Q2vJ1SSzWNRR8txl9agNLyoOWRaNWUTpw1Y-5CFpmgoJHsuuB_uMkiIWXvi1-ECj6wusvvb-B7bUW96I7GfJnnVKNvV9JgdR3fdctNn816WPV1uEBnjL_UCl2_eGjCs14DlxbJQsuesbUOs93Daws8wbWxIek8XdIf_SSRYDt-2Y3ubCCxHp4Hb7KZdSAsx6G4QDf1YJSPI_liVH1lYxYEIjrBV2TZEHPfXDgwOUL61TNmGPEzqcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd895d17e.mp4?token=Ei1KKTWAaBx4_X0z49oJ_dEvSfEi2w2qj6JOpNzCDqn0Qd8yjmcLJ33amVqgCbkoFBzmZFxxm-X8OcUr3ytzF_PD4dOe1ynR6Q2vJ1SSzWNRR8txl9agNLyoOWRaNWUTpw1Y-5CFpmgoJHsuuB_uMkiIWXvi1-ECj6wusvvb-B7bUW96I7GfJnnVKNvV9JgdR3fdctNn816WPV1uEBnjL_UCl2_eGjCs14DlxbJQsuesbUOs93Daws8wbWxIek8XdIf_SSRYDt-2Y3ubCCxHp4Hb7KZdSAsx6G4QDf1YJSPI_liVH1lYxYEIjrBV2TZEHPfXDgwOUL61TNmGPEzqcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو این خانم از دیروزه حسابی وایرال شده؛
داستان از این قراره که ایشون واسه خرید یه کفش به قیمت 14 میلیون حسابی برنامه‌ریزی مالی کرده بود ولی بعد افزایش قیمت‌ها، کفشه به 19 میلیون تومن رسیده!
اینم دیگه طاقت نیاورد و پشت فرمون زد زیر گریه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83019" target="_blank">📅 14:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83018">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83018" target="_blank">📅 13:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83017">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dpcuepbubz6uw4QdlE6PzA8EjpaYDN4O-Pw2MdKdrwY0cbO7FQLNhXW4d5DoTphfVicMpdkI-ZajkeTVmxulpFBiEhHyLn77Po6YG0gkfeR_3MeBQNS0mtWFOcKv-LBjgr4-k75G7-jSSoCEYT4Ugpp4A1bnOfJ4q-9nFAVJpGXTyX90z4SNLodcHLT-_XUlUC_5eWT1T2CYj6qfbNctMvAl9olRnMcAB0QnVTz9mcbqHoV0QQRgn_pFElm41E1QkbXs_t5_e3n5AxMPGS-LlgDc9kMBUEOuvUYLadeIfHC3rVQzPODgQgN5xpt5jQNdfNtCPa9HNvEn5G32RxYSHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83017" target="_blank">📅 13:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83016">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دلار نزدیک 230.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83016" target="_blank">📅 13:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83015">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgIU07ZzJ8bGkgX9_VE3qtOfXQipQQHoWoHRKiilfsGjLEKisxxDWcrjFjFDahrtsHOyxrA_hWmL8bi8aw83G7O02ZBbpgWNvimqoFG1wAomBXROeMwGOxdmobbltNXT_SaPuOFVRQoe8Gc7VF3HpgVN3JQNnLbeVTZxv69aF2PM_VVtVYKgPtDLU-lKhv74vGJdCTlMUfIDevB_2-v-qmwgcaI5DxnRzv44IL4jS4wCHI3nn4bqjrw0mhJDSpDO2Caf7mcnGx67wesIc9xaMxfS98pG58qrpOfKuupOQn0yjrWTSQB7v5-UDsTo4ztMccwJVPp2h-mB3vuCpK8kOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیبارو سفت بچسبید شاه‌دزدای اصلی دارن میان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83015" target="_blank">📅 09:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83014">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">چرا هر شهر کوچیکی میری اسمش پاریس کوچولو عه، بخدا دنیا شهر های دیگه ای هم داره، یکم تنوع بدید مثلا یجارو بزارید لندن کوچولو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83014" target="_blank">📅 08:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83013">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ادمین نظرت چیه هیپ هاپو برداری فقد فان رو بزاری بمونه؟</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83013" target="_blank">📅 02:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83012">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83012" target="_blank">📅 02:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83010">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/83010" target="_blank">📅 00:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83009">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دوستان رئالی نگران نباشید
از هفته دیگه که رودری به تیم اضافه شه اون موقع رئال واقعی رو میبینید
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83009" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83008">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdTs9cwhecYeq5ZEvHW-8Tr4JU7yPzO-IawHlBJFy9ZGnUuoJJwOsU0n4Bdj-9_UugJcaW7feGd0O1wON7emCH-Qa8zdbkDyKsrQslIA_5zyg4aycKbwk3FcO54CFgtw9L1TVyDUmrNTiNmXUfCm6yzsGvMiDFJTe03mGlpQPdP7PBucEveiu49NWy0HjsruSnmXV4_JmrCZbM2e6m9zL0Zs8Ltb5jX0YWgLHLYuQtx_Rqg3c_cQDtKlDIBrDFFgbXcYI2R2tGt30DM3WcrVNcNMb3W2ex98-MELJqFo4PRPd8cN-D_QfBvDRtbV78q-znxn83TsVIq_jw1oFpiUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چنلای عقب مونده ای که این شات هارو میزارید چنلتون و میگید ترب فلان شد بهمان شد، کصخلا ترب یه فروشگاه نیست صرفا یه واسطه اس که مغازه ها جنس هاشون رو میزارن توش و میفروشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83008" target="_blank">📅 00:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83007">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ولی لاشی با اون صدای بگا رفته هم بهتر خیلیاس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83007" target="_blank">📅 23:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83006">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">امیر تتلو از زندان بیاد بیرون ببینه حسن بابا چه کسشرایی ازش داده بیرون مادرشو میگاد بخدا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83006" target="_blank">📅 23:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83005">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83005" target="_blank">📅 23:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83004">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CakXGTYwYJnFUQ6d4dpJNz9RLez-MEKc_lCC67qHLq4a6bMlIUfG9so9r5_s6V1s9RIbWmF7pDtHrETROlrbc-qhVAxbkOyPaFY7Y9Yux0hiMajEJB_x4iBF1h485rTcwzfkG0lZAVNAYX_rO9jr84uY7HmymVKyU_qMLdB12j1QEz5tIoq3qs-tPRtmLUAl3uM7jAV6GerwSjDZirerVbCQxghKFuOX3kuQo7VLt1KJIsUwZO3izJY5G51O0tNrlpp1AsM-Lied38icFFocquwTVCmYESXfgkHmdPlP64hRY-Ret56qcZq4VxJLb4NZPhPtYZPAFHLO7J-_eCGeLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا امباپه یک ماشین گلزنی ها اینو گل نکرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83004" target="_blank">📅 23:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83003">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdfYYCdIk3XWdHZKW81E2XKcx921KKd-FUfVVeKqh158DZpKCYIxxk-g5AReaNu8hf8Lo2nYtD-CDkCTz4S328OZZVy41_AmAYOErkTnPuqWvRG8MZY27YB9dOZhwUo3nxyHq59FxxYItqoEtNxWdye4LwQdEVXDbZk4nnwulIkHi0B5mP1hAp-crEd2kIBOol3zRXqqMDWWyvWkHzTeR4ZLjCSJSikkw6PMNfo-Z9y4WScCwCkHaafMVESE7lf8JkMFBecLlCC5-cmYxYKj5oFxOLQ-C281yfCPN0WxXjUA3wW7dJdVoZcHI0W_er2GTNt8CEGaq6Hu2D3j_sGDkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خستم کردید ناموسا، کیرم تو این زندگی که شما میکنید و ازش راضی اید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83003" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83000">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGePCnani-q5wri_wMZMPGuEyRFcBIee3ZsrH60-sPgDy0AizjKY3PPxE8HBZ5DTahT_Cwzw7_2ZOT_jJ0u1bnwDHZ3FlDKYfNQmay_cVn8lEZIgABE1TKd1We1LL2bFERVtSO57Jtfa6AQcwzUpDl9zlefP2CBfd9Sx_vduZxFz4parZw54MQEDFiWoX0lxTAkJKCfo3ZQfSo40C9yXMwfWwnI-YYfrFWBz3q6DZrRWl-5Svb7UnDTtJeWeIVBig-UPc8etvsw2rcLW7Zj62Hl3oRNgAxH9-bda-kRh1Wd0cgq2RBs8zN9wGZjVUTPnlEHtDxS-kxXGf7E8M3LORw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گاس فرینگ تو مراسم اکران فصل دوم سریال جنتلمن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83000" target="_blank">📅 21:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82998">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یا علی اوتیسم  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82998" target="_blank">📅 21:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82997">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfb0d4b2c.mp4?token=BZ28wCa02WMmwUsaFGytD-sqGnp1upiG_8fBThxgJf_b314-xZiCuHBznt4ylE8jlZ6rBl1gvrXl4cH9d9-iYMPL7AgJxohFBbxlDJfZ_JgxnmbhuA6bjuUeE6z6ZynLx-dyL3qSpR3M3O_bDGmYvo80N_LCyb_4cJZbFqv2YrKSbeeUCzqQ6KR15rl_zLXirg5_55XdBitjk4a1gAxA-xnEOJo0E2qW3W1WV_LZ-4-R2pE8-oOPm_jqUzR6gK3EfeZ2BCS-9m000ishpI9X8fBTZHAVLKfPPmoqQ1IOsjnUplF3DpYwvi6mJwtdC2DZBXgPsMRFRuW4iOcru_iGYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfb0d4b2c.mp4?token=BZ28wCa02WMmwUsaFGytD-sqGnp1upiG_8fBThxgJf_b314-xZiCuHBznt4ylE8jlZ6rBl1gvrXl4cH9d9-iYMPL7AgJxohFBbxlDJfZ_JgxnmbhuA6bjuUeE6z6ZynLx-dyL3qSpR3M3O_bDGmYvo80N_LCyb_4cJZbFqv2YrKSbeeUCzqQ6KR15rl_zLXirg5_55XdBitjk4a1gAxA-xnEOJo0E2qW3W1WV_LZ-4-R2pE8-oOPm_jqUzR6gK3EfeZ2BCS-9m000ishpI9X8fBTZHAVLKfPPmoqQ1IOsjnUplF3DpYwvi6mJwtdC2DZBXgPsMRFRuW4iOcru_iGYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا علی اوتیسم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82997" target="_blank">📅 21:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82995">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKCeyBnUySAZlmX08N9l0fTkgQYn2prH16k6spV9uEgsTMsTSvNJViWcP30BNC4RHUXZfAgQ5KgQqZC9_-zD0RGk4n4XJqIWFceJ_YmLiNIpws74ulf5-KoHJviO3H3K9BYepvYkcVRLXZ81xhUpBdY-E8sue1emDD5ZU8qdPbc8vyCCu13HkZIZFMEDXHFfmgMz33MBOC2tJ88iBCR1R2S6j5LNXAP5j9CD9Rl-m2NMPTwlvnSQBay5IwNlBCinNlHO4Qbe35dzeIUOgNUEPX56dMD5pLey2RhNjpg1myN2l56_5JI8Y1prQcy2FWgF68ubxjM42P8fvDTeS4iYVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v5bjOtEa35wow_SP2e1L7c39ZqUzdWC4haQAhdDnOhor9zM5HamwcSIImjmHaoDf2LxzkW5Qw1p8iPbWM-kMnnzexoHky7awLmw0xSwksQTvTvGL6ECvZc6r921lHPAbW9wJ2gaHdH-1lpK1h5M3n04WMGwmQxJAZxsyZ0B4UmtmtJimIY0mzdFcO8wKiBa7tjI-ejT1Xoc34296MuJ3WhggpIMBmmM2oCidOhN5_WKYbNtJHg3tB0O1dNUCNPILT-36SJ-Q-GIMSTVK2gwTmn6J2J2prXuWv6lEkRtdjPwZIp3zxP1U32HoQocNQRYmbZjkD46v8Ifz2mbeixS46A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاگان این گیفه رو گردن گرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82995" target="_blank">📅 21:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82994">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82994" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
