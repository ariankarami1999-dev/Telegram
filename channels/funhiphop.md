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
<img src="https://cdn4.telesco.pe/file/krBPw61ew_PFULRIPrGTKWXpJLL8Evj049T7u27wr83IlK_F-a1Z6xU-duDDJzLhLMnC4d1QN6PJXc7oA3A__MTaNwHJM6EwI9nLrXksWjQxSz5Ier5VHebf8ndT7Qk10SFp_FwVv7WgT6NOcxZZOgAKpk9TWGvPT7Dug7X8Bvt8tffxK1A1LiO81Ggup9J96-QDu1wRwSsV-5wxy_181hpt8s1V8KUoCDrQEQYVUmLHI6z__gIWOMo-qvWHDNxF9VjDOeJTk3VudOCPR78xXA_kZitHoaIur_D0deqH1R7B50k7FqMDDGo4YjAFD2kHC_Eng6FesKxKrkof9qNFpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 266K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 23:40:59</div>
<hr>

<div class="tg-post" id="msg-84647">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7Z35vIP7RrZQXdtDNELk5LYO7kxqZl4S-o75h-UEl9_2czt3_gC4n5ANNLjXDj0550ONFvSpQz54tgqZG3id0-ePque1GtBPmyrDt251T2LisPhmRX0W9crmnAXaT31LpC1zEJivKJ3eQCOnhHJGt574iTtc6amNGF3b7nsMa4el-qZCZ7Jwi2gcNdeMZSVvk-vf5vka7h0cwbciUWlMo_MJ3b7RRlZJ3c5AgVZ0U2ASm60I2HTuWxERNt1zPwAbZb2D96ck-uydXjCbI_zjcaLJLelrDYC1ocJeuaMkZz9UG5zY7CFTmRGNLY8iz29jXUAKSVb2si28AUjuzC_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هی داره یکی بهشون اضافه میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/funhiphop/84647" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84646">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5dODRyPhcBUkUVffPG_n_hArCHDNJQ10QlKd4p-AbFU0m0e5fYuk18rTtbdhwtNp0A-KL3vtIdmF_N3A4IVC5imn8yunLQF6czKPRpgU_4jh8L_Huj5fWo_scmCGyOm2XMxB5fQ8GGyxsrVOiUwATZqCkevNX_uamJ6yoa78JoiOcLvC87_Ay3hgf5PJYFvCK0jIEEKZ-dp4daTYMc0LV3rMbT3FsgLDvzAPYfthurtgwH6xvMPoq_NYH4J9b6QfevJTMhKEZRPCjWJW_aMgBbgD5CzPtuqBjNCiEkF4yDuEMmt6AGPYxtV3shiK47jlWYwB2AaSvZ4sMhdvalbfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان فعلا پست ندارم اینو داشته باشید تا بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/funhiphop/84646" target="_blank">📅 20:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84642">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JVrlyuvhbiQccnH0ae1oew3pPBNR9nBYMTAhTyncAeUAjJ50CZmmw3nfL7TpFs8a2amaNo3oqX3Q8unNwo0RSuLjADmWvhIjmN4JYeT44V2exouCvqpfQdPsmgPDRU7FJiGVIficdAiKwhD1t9jjeDPewGA1KjinzZL1IM9CumobPQQbmQrCEZRwkWo7yk80MJQqxCQmrURcS4PXu8zEGXbdGofN722QVgWnCrVPa1BcgSu44ritxIcUg-1qjVt2bp-8If9V3Gxlc2Me83i8qEkKY1hnRbQFLGxa2xTUL9Z4N4vOKX-vb_BN4HW1iKSEQw6a2-k9LXQYgLdU-hxiFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FE5V5DkGjB-HIh-kipLYEbvHPnfq-bYsTg84IGj7NdpgoawR0ZlJUnMIEqPpaOkUPPs94DYt46WPlto-YwHa_Ne1fBNIerfV9kj-xL_1zZAUCQuDRPXcuq9iFYu5hgZ55YrQ6dfaPrFCHWNbDFaMw-Euy4H8tqrOPzlyqxJeY_cO8YKZ8VicU6HPgsgVdhmgdMbmxmFSKDjqJbBNWZL8DViAMc5ZmjgJb2atrWA5WbGarc8VbTwMOPSCYg-Ai-h5QwN5zv-F-4myHN9N74Zh3oj_3vSH7tv4KDbHMT7X-OYSU6D-RvPVaPIKGEbK6rUEZKas1Dq4ZYsuGSizvVIKCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NF3AUX6UBT9wDzDReIS525A6bULNS2h3qXT4C_WDBEye1AprfGux1oASwwU8fD78xNb12LPkXrGvSqZlchX0AXtG6VOBo0skfLQQKPyW30dEvbQ_zhbjfKGH-H246lvNqXWDymCofVOUruEhnMIrSWBiM6bxURINS7a28htRHdGRXFjYsKpNRwsotb9iK9CRSxZC7CblrR7sS2hiszdzZmn1SSss5p_iGLELr_UALMsllPT6VI6IHQCImOgbfGFLRraJpnbpm3cOmXtflm8y3d1R0hrJ0iwgMjYpahJFQS57TeKHFQRS5pwfpYKCq3fIpQwW9aP_VjMnENTDKe3Iew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t6fulLaETbDhpeK81yNdI-Fa39ZC8MJ8A7pHcI__hcMGAxuuy5PFZiC7IWHV6YjsPrjbhp3KI94APmECK1SjQAkPGyab-eb0QW9ZM1Q_yAzA0hsUuAiXs1Ur2y7VeIprNx8Cnl8diDKZENoRha4y1vbeWsYA4NF-Atk4R5Jm-S38fl-ZUiSDn5X5Zc9Vwy43Bvo11zccTx0u_c3JbkWAXuhT_qBc-dIs02I2MSHgfIl6HAYuPSkaUcdtmCCHX1TnRrqA-FDY6lIUYqN36UkQXceeu2rhl-URLFKDC7eNRoldYE2XlZ_KWSuEGJPxuT-6lCVKx2ZgnhcU6Gx_mCK5hA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همزمان با ماه کامل بر فراز آرامگاه کوروش بزرگ، این اثر هنری زیبا خلق شد:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/funhiphop/84642" target="_blank">📅 20:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84641">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnvvXvniejU55dJr0hOhUqoIM5dXGaMsJQ1GUOYe1MZOt8SFWusYYCozw4o9Q_aFOB7o-5eB2wAB85BT6cMwMyQ04GUHv5bIC9Htlbdo5SfcdyDRdIl7Gen3xGgsSzQWcxDuWY5V8h87AHxQtDLUVPxHfkGEiF8Slbn6SeI5crCqv8R5NQfyIeFGhkuVnMUSMYHC5DrxgxXyfDrM2nIUjHCgsoRKLnfaj2vH7zhIEYZZQi35QI9ZGiDzQ2WbSBD64_fH11D6WIZdEKZIFOGzZf9D9CbCSmwSh8XG7Ooi09f2RDiIGrWdT4sCOc11DAN0iGdjtSccAXYUIISdo1r6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چجوری مصرفمون از خود افغانستان بالا تره؟
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/funhiphop/84641" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84640">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6QNah4nqy5So1zuwx0EgSTixFrB3sGlfL630ZN1I__bh91xApSg_XOGEr_Van2710YQuZ20B7QmWtLjZjXmrjF1EwubrOLwhyzUhTH4AjSSwXEAbVXIi0_CTwNRvKfaASSyn45pIlkMXfEL8HRLIPfUYXflgMy12dQsKjehk0a8tJWy7Sl86NXS79_VCCanapnTzCwymnld2iuH6fxpSXfd5pPpTCvCX-D_moe7_sN0L-UNVmK13COOBRIPIvjfWxIinfgAeYXOQ4nwKBaQTWrL594Lu0hkfHgkwYdyjs3NBxdvpky6R95tiU8HAomfP0pxEoKwzD7VqXOoNhQE_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G17
🅰
🛒
ورود به سایت
👇
✅
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/funhiphop/84640" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84639">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NX9l-lJTjfsi1khJgNTl1Nvku8jyux5mSiHYPphYmnC-7raIB3YA_xpFElFkft_lc8Ld3wPqA4LEn85jbG_9USV2XGkZ7ugZESrwiVe1lXVDww8--w2g0PYQc6wpP9PUz9iVtZWNL5-s1cPD0vKL_9sbp5XJTNzzftJgg4iIehXBc-wgCyHFIwVqNg93Z2L9pt59wFElLZ66URnHK1anfR70sOMKHZXsrpA-zASyCAkeSMI0fA9hdopFYHeJ9M0h20NEjQpqkTrT_TnmlHr2kfBC8S_bDmm8BHC_n-Ly__Q-3EvRgzbAt5-ktIFpQe45HRba6fBGEZGzpC4XGXJfXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا خودت رحم کن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/funhiphop/84639" target="_blank">📅 19:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84638">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqqBF7c8H11Qe__jzBbgHNqhKczPnXJ7xvD5mHi-dOSkLfkx1BEl0v2AjPR6i79UsmNd3gUV-0vMWjd28uji8Nd3qGfH6pzB-8dfDP6GU-D59q4Yik2UFr7XeQwdkKv76r0oZoW3zuz2xkBNKVmJbuTonmkM54L3i1brO9zTjSmRDRQIQL_yQ-sROP-aeMoCQ8yMAVzdVebNnsPVeygFly23I-t1x5WCFmwuF6R__I2T6Ii_G1FuM0B9IG0YnQExrjFVrLm5BniBjsAmx4aokXShYqGotlreRQRcHeQi3WbIdz9_AHYI0_K3jmGVWil6aS6ydcvGgRkBl91BKGSeRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجیب ترین چیزی که امروز دیدم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/84638" target="_blank">📅 19:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84637">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن تمام مسیرهای زمینی ورود و خروج از ایرانه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/84637" target="_blank">📅 17:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84636">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خدابنده‌لو چقد شبیه رودری بازی میکنه</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/84636" target="_blank">📅 17:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84635">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارش‌های اولیه از کشته‌شدن معاون اجتماعی انتظامی استان در پی انفجار مین کنار جاده‌ای علیه خودروی نیروهای انتظامی در منطقه چشمه‌زیارت زاهدان حکایت دارد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/84635" target="_blank">📅 16:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84634">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">میرسلیم، عضو مجمع تشخیص مصلحت نظام : تیبا در سطح ماشینای معروف خارجیه و به راحتی می‌تونه باهاشون رقابت کنه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/84634" target="_blank">📅 16:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84633">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/84633" target="_blank">📅 15:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84632">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84632" target="_blank">📅 14:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84631">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcOpXALEgHs99FJ_Y1ySmXiYWNDDW6XUJOY-dHRz3qnlFjuWYvPkcVy9nLiTPdCBebrFWJaMaMB6sS99kQrnYbMULXjvm5Vw9l86ZVAWZEht5CjTNeYhY7Nm9UX31EaxfqX_3rCmNOVZnE6zps3tVpWPxaOKCQW3VXChMz7qK9BELng0G6_26__BhiKN1bm_AYfOadIUfwfndx1zCuDWGgVLwW2m6w7GArv_XK1WognT2iXoNlJb7Vjpf5FHw3crcXMUY8cWc5cY-qNHMW_boH5mX820T2ymNCo_ftIMuO39VMzi3llc5BO9BZEbieGHGNIHVvEW9Skl38W-4Wi-oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا حاج اقا
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84631" target="_blank">📅 13:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84630">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84630" target="_blank">📅 12:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84629">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84629" target="_blank">📅 12:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84628">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84628" target="_blank">📅 12:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84627">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromᴀᴍɪɴ.</strong></div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84627" target="_blank">📅 12:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84626">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WA82f1gYdI_pbnu0uRe3ddPxJ7S4QSZ9J3p2jZGmRMgL6lb8XIwyjMbMPRpsEG91-tHwqjldBl3usmE9M_hpc0NxHL1qqMnlvpnqisrPmhNfHFWPptxPmXM_5o1igZjNhn5eKIBzEqoYXxMzx5LkJsN9To8EMzCyyel7KemBA10UOwNFWPvq4xchnaoDPtX5yuQp3tz5s9A-qfq2Pt07kkjRRd7VXpj_ngSLJICHQJ8mQRs8zwBpIQ-GCj90NKDs9LTGxJ1lGcbu-hK_onzfimdXKm8Wyy1SKYrrYMdV533Ty7k-e935VCaaMkYEC4PFwtAAynXYSOLV6p3XsMY6DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا فک کن فیت بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84626" target="_blank">📅 12:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84625">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هالند و امباپه تعویض بشن بین سیتی و رئال جفتشون بهترین تیمای جهان میشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84625" target="_blank">📅 11:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84624">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VP8aXjeM-xsRO4exImFRHW20LeI7wFUHi7ZgxK1BKj6_ItGySkkzoTR1nKqQypU3dJrfEsSMYfjEujenFT-KwhlpdkoT9fHBJ8HbKQivXZoVt7_sYZvLnrKnaP5znWUYbzbK8Sfg4yhlh7VPwGuAM9ThoUUiYCkTOtObKfXlrnAL-mr2u_TOvsLvd_HsYToOkog7UiiXm4OjqgSgdh-Q6ZrSP_DzWIdDkigUnU_2s0ZPi1-TBJxk7G1IADMEu-uCm12ltXwA7apax3BZCs5qrm1-vOcOfPmCqNP6tRZlRO9YxShUCXd5caILLzH0ohXIMi9eI6zqERistawcblD2eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس داستانای کیلیان دیکتاتور حقیقت داره پسر
آاس :
امباپه توی رئال هیچ رفیق صمیمی‌ای نداره و اون توی رختکن رئال احساس غریبه بودن میکنه. با بلینگهام بینشون یه جور تنش و سردی وجود داره، با وینیسیوس هم رفیق نیست و با بقیه بازیکنا هم رابطه‌شون بیشتر در حد کار و فوتبال حرفه‌ایه. حتی از بازیکنایی که قبلاً باهاشون صمیمی بود هم کم‌کم داره فاصله میگیره، کلا تو تیم کسی با امباپه حال نمیکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84624" target="_blank">📅 11:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84623">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv_v5HBHOEOfVWV8PLZKLhv-Yy5jq1uJKND5ouqgPb4Obd-qKk4wr6xgH2IzGP1ONtVL9I7Udsgy9dYvTP79tMQzmbasWQiY3H7QBnp2mJyH5RAQae4HZ54hHRaKS_caCEYMhdKaVlhN3gHCpTEa7h-d87PQ94HRe_pTZYg8-Zmd23lKmm-UuzPTz4ETZquU0ZYpRnK1TlumFHkoihL0CRN3tq1bfaBe81U6z_PUIyNdcPVvIGuVM2UZaUhzkYHJbvkqbh3aNJBTtXOhFNYKAKOx8JjMzIjrsmaxekgh5jbjJS4FK9GYwPThVTNJv06z05XKAKOZJ06lg9N5hPMDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مستند تک قسمته ۲ دقیقه ای(یک دقیقش تبلیغاته)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84623" target="_blank">📅 11:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84622">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">عراقچی پالس های مثبت از مذاکره با آمریکا داده، شیشه هاتونو ضربدری چسب بزنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84622" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84621">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ویچرت؛ تحلیلگر معروف آمریکا در توییترش: اسرائیل دقیقا قبل از‌ انتخابات آمریکا به ایران حمله میکند. این پست رو‌ ذخیره کنید.
پ.ن: این یه بارم گفته بود آمریکا لحظات آخر جنگ ۴۰ روزه میخواسته به ایران بمب اتم بزنه که ایران میفهمه و مذاکره کردن رو میپذیره، قبل از شروع جنگ ۱۲ روزه ام میگفت دیر یا زود یه جنگی بین ایران و اسرائیل اتفاق میوفته
پ.ن۲: آیزنکوت رقیب نتانیاهو در انتخابات اسرائیل هم دقیقا همچین حرفی زده دیشب
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84621" target="_blank">📅 10:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84620">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">من جای تهی بودم دیسای قدیمی پیشرو و هیچکس به هم دیگه رو جلوشون پلی میکردم و از واکنشاشون فیلم میگرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84620" target="_blank">📅 09:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84619">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdnI0OIHBI8UpH1-Y5zycyGsEW-dWdII0J7ebhxOoXgsU9C8VtzH1n51pEtn47UVo-QHU75Sev43p0uWr0lA595X3rjlYwlAdm6SiX97xEE83lAR0L3YG5anTQ6NP8zmsNyXME2lHvGPgsgmYEiT0R0yQ5SJS8eVQTusTWztNdhaouPBZjH0Ld4Wz4PSdR3kAlspYu4SjqAYbuZZIbTc5kFuZb-Pi7MCjixEFV8b2IYWLR6-kkpDaK17wUnaT2DTLpMONXuMw0OHM7iuG16HhTI3ByWdgGEvxkO1MAqhdM8MiBqIxiLG--e1I9t0R2fVK9f8romO60OtthyNLHVkvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی کیر تو روزی که با این تصویر شروع شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84619" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84618">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84618" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84617">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5GbIrwM2hQFingIK9YFabpww3kEFthYfsc1rdEu_Yf1kKsKkIgTsnQoPWJcBPq9dI8_YvuMGg_nZi7vmEvjyu9LuqGJE5nQas74T3X6OQmsxN_tiYUA1mvEklGE2WW_cSasNYeUvrydM6-hjgqzoLfyhgR4cGvNxWXn3ojoLl0RkX9UEUH2lnQWrKWhfC5p1N9Ke49QPX8LnvbQ8pU9ZB_tNM2kYogLjHfKYFKBgmpfknue-0I23S8ufYC1cDn29T6S2ZX59qbmMCLkIu-VRXsz3sagMJduQ4xteEQz97MR6aLrXnYdZAOyEH_tnV4CIn9jZM1kLNknX-8lpKhnFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
پرسپولیس - صنعت نفت ابادان
🌎
ساعت 17:00
⚽️
چادرملو اردکان  - خیبر خرم‌آباد
🌎
ساعت 16:45
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r17
🔗
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84617" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84616">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=IGfg7_tiaUeP87fVUgp7jguPkrgyfZhZvUjBn7KWMOjZFUTWYf87C8g6JIt6FqqSktvFcmNocPbJYKJyVfZ31x1SCEAtjtu_3mZY3TksdHhgDWGtjvWi8Zz3Rgcdfc6q9CY9sD0bIId01AqOJsqABvD6OHYNlRxXxpDG4Jmj9k-4HVLyqjjmuX8kbAUVboQDNZWJt6om0fOU3mfRj3fa9gAGtn9VjNlnvhw3cJ4cFPhIdng_CnBONQQ8ni_bmtshEb6TqoH8pyFG5r2RBzrT-HmebKNBxOqbb4zCRgRDByFfnXCQ_7p77_4763wFcv5XqIbl3WpQHfa1s0jUkfEFdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=IGfg7_tiaUeP87fVUgp7jguPkrgyfZhZvUjBn7KWMOjZFUTWYf87C8g6JIt6FqqSktvFcmNocPbJYKJyVfZ31x1SCEAtjtu_3mZY3TksdHhgDWGtjvWi8Zz3Rgcdfc6q9CY9sD0bIId01AqOJsqABvD6OHYNlRxXxpDG4Jmj9k-4HVLyqjjmuX8kbAUVboQDNZWJt6om0fOU3mfRj3fa9gAGtn9VjNlnvhw3cJ4cFPhIdng_CnBONQQ8ni_bmtshEb6TqoH8pyFG5r2RBzrT-HmebKNBxOqbb4zCRgRDByFfnXCQ_7p77_4763wFcv5XqIbl3WpQHfa1s0jUkfEFdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و تهی رفتن لندن که سروش هیچکس رو از نزدیک زیارت کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84616" target="_blank">📅 02:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84615">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZFsORSX1czS3DcwW5hZRseo_1mNuzjvplkaEfj-vFAFlPgKJv4Cbt6BUI_tdOCueLOMLbguoQK51kdsA9m0qrwXBxdcBdHMOK5O9IuAJoWtmUgazCm01z5GyUxp9Pi85z7Dx8QIKO-voyp24nFJsYum6cgbCyaV6pT01_x39men5P1l7TdtzeKHIDf2ChoPSEIj5-o4kvbIq1PLgY6CHcItYBjlkkD54bkw5yL7Ecc7qfFzci3VjRimFk70dbY6WU886AjQ8b4OPQuvgTDNmixnqkiYSQEsu8GsypX6aKY113gNI8jV4BNFJMbf1U-lZcROiryojQLghpfahFV8zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز شیوع طاعون تایید نشده؛ تو ایران شروع کردن ماسکش رو میفروشن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84615" target="_blank">📅 00:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84614">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سپاه به اربیل عراق حمله کرد، احتمالا هدف مقر کرد ها بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84614" target="_blank">📅 23:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84613">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84613" target="_blank">📅 22:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84612">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=UOCwvvGnVqpvDHJuymYs8A2aaWLTzwo-zWl2bPWbrJ-KO6zIsff9CKcmblXUy7ruaj3q52DUybUp-ChuNmK4tqPfZFRDRBKX6Y4BLq3nbSLhJGS8vKPoVfAhumXT-waQ8SHKw4LZHGND94YoFz8uQmxrIjmYq0HI-CvouXMZGArQLG5sdv7LXrEECOXAvMqrb3Pe_4Yu_Dbmw82h6tfI6wdZKKj8smGLVpYLzdp81aV31ax4uGlKCJELrK_udAGGuHLEhjkFBltTEGB_7qPjBkzsaRZBJTg8M9OxPs2MYZJzDPBS0QinGWlFfPwP_848_8sys2CKsFlvdN35rt9P2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=UOCwvvGnVqpvDHJuymYs8A2aaWLTzwo-zWl2bPWbrJ-KO6zIsff9CKcmblXUy7ruaj3q52DUybUp-ChuNmK4tqPfZFRDRBKX6Y4BLq3nbSLhJGS8vKPoVfAhumXT-waQ8SHKw4LZHGND94YoFz8uQmxrIjmYq0HI-CvouXMZGArQLG5sdv7LXrEECOXAvMqrb3Pe_4Yu_Dbmw82h6tfI6wdZKKj8smGLVpYLzdp81aV31ax4uGlKCJELrK_udAGGuHLEhjkFBltTEGB_7qPjBkzsaRZBJTg8M9OxPs2MYZJzDPBS0QinGWlFfPwP_848_8sys2CKsFlvdN35rt9P2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوجی انانوبی بازیکن بسکتبال+۲۱۰ سانتی نیویورک نیکس رفته دایرکت یه دختر ۱۲۰ سانتی و میگه بیا ببرمت نیویورک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84612" target="_blank">📅 22:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84611">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=uKVmqLGMMw1EibTTgvfDuPEJMb8Oh7TI17V05zIClVzukVCBgetXCLgdR0HjZ978KdhFUSXlvaFD5VVHK9ZGh4Fu4fQUTUYEUaSExgR_pyZlss2tdk9NvSEzvX6eP4bsjlJXT5GTtOvHFG7qhOqr_SW_Ys-yMr9oGJVqG-8GTCmEdQtsL7SRZfrNToy7mFvvvINEEnzhxRycL8yUjaX8l6UB3_KitJmSqf1B72osarBifBemBVeRqw7kQ7PQWM7Y1zf3ydXy5KfUm6KUVgexHLRI5qVyzVb64_YoRnWr_4yCr5UvSZ9UzqRZaVh5ddamf5C5HARJ5ilVD3Ye4BOhgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=uKVmqLGMMw1EibTTgvfDuPEJMb8Oh7TI17V05zIClVzukVCBgetXCLgdR0HjZ978KdhFUSXlvaFD5VVHK9ZGh4Fu4fQUTUYEUaSExgR_pyZlss2tdk9NvSEzvX6eP4bsjlJXT5GTtOvHFG7qhOqr_SW_Ys-yMr9oGJVqG-8GTCmEdQtsL7SRZfrNToy7mFvvvINEEnzhxRycL8yUjaX8l6UB3_KitJmSqf1B72osarBifBemBVeRqw7kQ7PQWM7Y1zf3ydXy5KfUm6KUVgexHLRI5qVyzVb64_YoRnWr_4yCr5UvSZ9UzqRZaVh5ddamf5C5HARJ5ilVD3Ye4BOhgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرقت غذا تو یکی از فست فودی های کشور:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84611" target="_blank">📅 21:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84610">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=ef-ZuvDhh_IU8Pa5AALRXjrsbH3NZC1KQ0pQtSAsKSGEAoIcfwMCHgPm_mM16uQprvEj0DdwLZ6Ez_ay0C6DHuT8xy80d5St0UUDFtKT0lLdzpsAE32HwLsgJFCktTngnbGI6-lfBIvqGEDxd2dNfTSNTdPKWI4ASvgL4HmzArIXmlBjJrOq_KwJR6wU6PvEMxdG_G7r01KSbwR8PdMYaRGDK_NXcxjZ3_E8r3c00V9IIS6MDRqDZvzxA--srUbKOR_-dcCMI4uUvrwjC2CN_MxzxYHYMVhAfi-EGPfEzzslRXsNQZ05O-yr2MjJLSUwbi-C87WZxuDRJ-eGGw05MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=ef-ZuvDhh_IU8Pa5AALRXjrsbH3NZC1KQ0pQtSAsKSGEAoIcfwMCHgPm_mM16uQprvEj0DdwLZ6Ez_ay0C6DHuT8xy80d5St0UUDFtKT0lLdzpsAE32HwLsgJFCktTngnbGI6-lfBIvqGEDxd2dNfTSNTdPKWI4ASvgL4HmzArIXmlBjJrOq_KwJR6wU6PvEMxdG_G7r01KSbwR8PdMYaRGDK_NXcxjZ3_E8r3c00V9IIS6MDRqDZvzxA--srUbKOR_-dcCMI4uUvrwjC2CN_MxzxYHYMVhAfi-EGPfEzzslRXsNQZ05O-yr2MjJLSUwbi-C87WZxuDRJ-eGGw05MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من هیچ کاری به این که رئیس بانک مرکزی ایران به وزیر خزانه داری آمریکا سه روز وقت میده و این که دقیقا برای چی وقت میده ندارم.
ولی چرا میگه ۳ روز بعد با دست ۴ نشون میده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84610" target="_blank">📅 21:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84609">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=MZrLwGA54aowFmIZ18EqKNSFPpAfcV1QId7XAixhoT52jbmMH_UIhs8yElSzCNsamndHSAZ0d-XojzmTaLA3hU3jd01NJudqTaikFPqXZ4qXguEAWD77sd3i1idDTL9Cj5MLFD2kNrd7au5DzzJssjyTbJ1Iq7CfQfIm2ABl5iNwvdycVnWw_dMz6d5x-hm7pnezGI2oRBbyvbo-P-A2rAAJZDjS_TTLCcPjzK4jQTK6zhqSvy-HmCHfiupkpFyqsWgVjXt_-6XC9jlO9XpiHTo00nG0xqVvqSrFq4mUyZbQpkHBa3cA5TIndN1Zwcx9mwgh7y4j3F-G5ft9dOI_tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=MZrLwGA54aowFmIZ18EqKNSFPpAfcV1QId7XAixhoT52jbmMH_UIhs8yElSzCNsamndHSAZ0d-XojzmTaLA3hU3jd01NJudqTaikFPqXZ4qXguEAWD77sd3i1idDTL9Cj5MLFD2kNrd7au5DzzJssjyTbJ1Iq7CfQfIm2ABl5iNwvdycVnWw_dMz6d5x-hm7pnezGI2oRBbyvbo-P-A2rAAJZDjS_TTLCcPjzK4jQTK6zhqSvy-HmCHfiupkpFyqsWgVjXt_-6XC9jlO9XpiHTo00nG0xqVvqSrFq4mUyZbQpkHBa3cA5TIndN1Zwcx9mwgh7y4j3F-G5ft9dOI_tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد.
از این به بعد در سراسر کشور، با خانم‌های بی‌حجاب برخورد و براشون جرم ثبت میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84609" target="_blank">📅 20:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84607">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMf_GAGOjmTbKIU3BMdyOQez3ywBRr_B5s6YnWDCT3_UcQeVynyuuI9uTp-UaS0atcSnQpZZATbhV-mDSjYu8NTLC5UbIlVJseZK7QNSz3kFJmHXulJyiSWixXP2riTTmWrigtQPjYLpY3pDZdIjrRZ0rhA47ckxsoLFKJyhZ_5GviociQ90Efqkv210koIC3-OSwBO2NHaeQSVzqr3fs-O1q64AYmq0Ow6uukouPZrz56v3r-w6DWsiju2AtLi3R3f4FiWfmnfW_zLjLWwjAGJtUTHuHMlq_MmVu3uqppIpSJWkhk0S6Ee-8ASalFl8hqUggq9aFgqAD7c6JHqllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان پاشید یه جوری شیشه‌هاتون رو چسب بزنید که ذخایر چسب کشور تموم شه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84607" target="_blank">📅 20:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84606">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJrGkHxt1Sf-zV2IdgOdDhZzsJxpsYktLhYXSEBqMGmK5boRWtFfQEkIDCuMiVEIR9UirIM23VV1dRr28l2ZhTfUKqot-DQzmdmPhyjH--qEok6qDT3FmjLLhieK6y5jl33A2MBClRZcPmMf_P5Vh70SzbPqeaYY3OquKh2RY2GoURXokjffzYirpxNRoMOtiOpWKJUksX9HssgTSmiGP4COupRccUufAzMiJ31PyoFkiirCP360I7fXffnZzFkKePgRk0xxyL595ev8eVOmV863ZK1LMTrBe4-fde1-slivLzIG24mOKMaOuI9T06A3bl-RGjrk5N3lKwEKIV4YIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خخخ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84606" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84604">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V194LHTEz7q-rf_nSEJ-CjsqR2EtFRIdQaZmQL00x3RsIB3bC2sxqvKdBTFm4r2bZ4GnPTp755Lmie5Ml7Zg-44sD2h6oSya4jqXBMs1SD0DH3-se-QEWjh7voZ8rFLk3BdMHuMCERTAkHzHxZ5soqOLamKcFnVJ42MXrxdvYg-8Pfs6EeeR7z7axaqTVKqJXxBuK0GA8KdailWzSqXml8kJD_ew4dZmw89dwcUzI0X0A5xy_PwUCm8tDaf-4eRfMGQ0_ZMzYswivnvXbJCI9C1uVqcDSaZbZP1x10qd_hq5E2voPpcew7XVQPvh6a8TWIaOMLUiplzSmfRnf6wECA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توماج صالحی با رپر بسیجی‌ای که شبا تو تجمعات اجرا می‌کنه درگیر شده.
(به نظرم رپره داره حق پسر ایرانمون رو می‌خوره
💔
)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84604" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84603">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=ejA02eX-aFMeysYzIxCzM-CvRLMo9kRm2jM5d2MLyai6a3J2laCrR_cL2l5oSxg9NBD6CtsaMYiBYKBAJOb-6kO19BKkYpgfUdsDb3HrFnqZD7w_pqVmgH4oPBM0QB--IPbJTHX-OGhHttDBGjPRhwt0YP5D6drsqVGtYHPbjLfnr4IVyTWZjom-EwuImxo09dC5k8zihMvFBSGoPNwqrsJIFN2bRK-3EJ4WxkwFwfJRNZoAM6TUGVxoMzhWrNEvOgOqC9oX0kuvvFU7e10r-RVaPCAtB5KSF4bR67YRsCLb3uD_nQK299lY_1oQk8NAIQ7dSyWhFyo5R2n-dp5AzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=ejA02eX-aFMeysYzIxCzM-CvRLMo9kRm2jM5d2MLyai6a3J2laCrR_cL2l5oSxg9NBD6CtsaMYiBYKBAJOb-6kO19BKkYpgfUdsDb3HrFnqZD7w_pqVmgH4oPBM0QB--IPbJTHX-OGhHttDBGjPRhwt0YP5D6drsqVGtYHPbjLfnr4IVyTWZjom-EwuImxo09dC5k8zihMvFBSGoPNwqrsJIFN2bRK-3EJ4WxkwFwfJRNZoAM6TUGVxoMzhWrNEvOgOqC9oX0kuvvFU7e10r-RVaPCAtB5KSF4bR67YRsCLb3uD_nQK299lY_1oQk8NAIQ7dSyWhFyo5R2n-dp5AzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
روزهای
بلک جک فارسی
در  Berrybet
💸
بازگشت نقدی:
معادل
0️⃣
1️⃣
🔣
از خالص باخت
💎
حداکثر بازگشت نقدی:
۱۰,۰۰۰,۰۰۰ تومان
❤️
🤌
حداقل شرط واجد شرایط:
۷۵۰,۰۰۰ تومان
🩷
بازی‌های واجد شرایط:
فقط میزهای
بلک جک فارسی
از ارائه‌دهنده
Creedroomz
⏰
روزهای واجد شرایط:
دوشنبه، پنج‌شنبه و جمعه
🌐
ورود به سایت:
➡️
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106
🌐
تلگرام ما:g16
🅰
➡️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84603" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84602">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=AnmjVZQns0p7SfAmfbwPd4-sOOIc3qHQxTCMDRFk-F5UyffV-89T-_udk7nTu7MgWE1aeyzU9v8rIWqJhpgqe8zIMcij7FbTu-OtfDvy2ZtZpE_A7LNCPJ1pdD4-HkuzlV0rGj3_R-vdiUQmTLs2s68bNRCDkvDTeeo48Mcn8WXTVfAsOQUqdW7b9fWhues0bujlwN-w9FBFvZDztLOcCsiR3MJN-R_0D4Z4Ad5ogqqGs3c6cOVAvIJujpDp0aqC0_e-h5MfxQWAhGjw5RuGOAbDGYkGBPsUrHdGjf2ulCWUqWs6uaVPHj6U5R41HnNJ8z9h76RF1SD5gFb-oYYMtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=AnmjVZQns0p7SfAmfbwPd4-sOOIc3qHQxTCMDRFk-F5UyffV-89T-_udk7nTu7MgWE1aeyzU9v8rIWqJhpgqe8zIMcij7FbTu-OtfDvy2ZtZpE_A7LNCPJ1pdD4-HkuzlV0rGj3_R-vdiUQmTLs2s68bNRCDkvDTeeo48Mcn8WXTVfAsOQUqdW7b9fWhues0bujlwN-w9FBFvZDztLOcCsiR3MJN-R_0D4Z4Ad5ogqqGs3c6cOVAvIJujpDp0aqC0_e-h5MfxQWAhGjw5RuGOAbDGYkGBPsUrHdGjf2ulCWUqWs6uaVPHj6U5R41HnNJ8z9h76RF1SD5gFb-oYYMtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی رشت رعد و برق جوری میخوره به دکل برق فشار قوی انگار که زدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84602" target="_blank">📅 19:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84601">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد!
از این به بعد در سراسر کشور، با خانمای بی‌حجاب برخورد و براشون جرم ثبت میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84601" target="_blank">📅 18:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84600">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هوا الان یجوریه که همه تو خیابون فکر میکنن شخصیت اصلی داستانن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84600" target="_blank">📅 17:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84599">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حالا من که میگم استقلال یکی زده به تراکتور، ولی ناموسا فوتبال ایران دیدن نداره</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84599" target="_blank">📅 17:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84597">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">محسن زنگنه: قراره 110 هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84597" target="_blank">📅 16:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84596">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">محسن زنگنه: قراره 110 هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84596" target="_blank">📅 16:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84595">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c055QUKmKMVSBmgEEaf7rYsApZf76gCi2if5N8rRx8u_OzWRy6A-2wU5xW1YoRTXyb-PO9Kr3v3eC6Z3Cs6cirjaBjAId20y-Q68975aC7JmnoKRREsDUqPSZS3wWgVbPLfWrd-iv8YvfMBBhwNDLszcb_W_fLXG10VEmvWdDCHBLeFP0A-Lpu6W8oIP9_BiPnZfLXQZbU7ANvD2aSsikqfWqO-wXrD6Z3owHYUHYLZVhVmQcgvxc99YyUP9TlS5uiacz8woT_Inq1hm9V4hZGQd1cnR7kgjC7NAk349xZGKATkzscSJgRbMqjZ1WvaAWqByAy_Ztl7y8iK30u_X3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر دلو فوت کرده
خدابیامرزه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84595" target="_blank">📅 15:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84593">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFDUwgPMpfh-wrCPcled7o88aA9Wv1b6eigpeHkJ_ZDiBngNU-ELU09ttmJtVYySyTAVpGiu_trim_W8rXpxCIczBIzTy3yMqOBwTMbeu1YeQ1E2po9aalJcg5CN4BOEXZII82axtgp8-JrKYFnv7rblWD791zFYeLSuqG1zIf8x1lyT5oc6v41xUENdHDAniaw0hyFluoM4Gibq2Tp1vx309SchusQvUfy3OCztEk2EfAG1DRn587NfDekX3w6ATyULCx_wFiCerM6PUClyRy2YnyxsOnFjySYSCS_cVwuZAf37VvphAk5TzAilW-A8yDWkXeC8HdZd4FW7EJ983Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ps88fi6nOBJnCbaSL0vo8R6Py375yMSKs8H8tzeQn0lv-WiojGVn3b6FYb3Dl509-NhyIdh6tuQDDS_jw49DAnBo-7jJNVUxUNxvwIUiJxE5y-_DTQyze-UETQ1cjWcOgRXDUq0XagkB3RA-vobgMYz5vfC9-6isCPGronzqyxyrFnsLG2m0gaYBkn2J3K3AAfIwcO18HsriryU-7GM54TibG1vqDNJcxRrHnQt5I5Z1p8l9uVltbbvCEd2lhImKWARpoJq1Sa2WKyDVNt2kh07cuhAx4KG34ZDVBTEiR4w9IyhQoQCPU3z4qdPulL8nzuYkV9wHIuYUEfmtaLeaSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشتی ریدی که
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84593" target="_blank">📅 15:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84592">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مجری صداوسیما:
گاو که دلار نمی‌خورد، پس چرا شیر گران می‌شود؟
کارشناس:
اتفاقاً گاوها هم دلار می‌خورند
عالیه پسر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84592" target="_blank">📅 15:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84591">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cac1e3571f.mp4?token=EEFS9JZRylHMRMsV8XFGdgpE-PbxbXYDguLm0-5nndZWlfzGUDKyXsWRT2cRDrVPv62pi_KFGbBRtTd4BZoDkYufZmKEo-eH68rdYSvJcBkC3zM9B4AEnI26kq-Uvo9YTsVewjbeU9DiuSRkoFPze_-zH33IQNhvYqZB-DlgyYEa3PRmQwyBD8VMctqccbrxvqqDb-Brj1GwxuOmtZtKKi6tYG8gjcmRSpzKznSuJO88t9vJC3AztB4qFtPu0u1a-rqj9dEVl8bGEA1ChriBHNXSSfStwLry0IhtnqoplSY-DvChC6LnL-jVDEuuB0gNLTq0dw4uhCEDREsgcn0MXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cac1e3571f.mp4?token=EEFS9JZRylHMRMsV8XFGdgpE-PbxbXYDguLm0-5nndZWlfzGUDKyXsWRT2cRDrVPv62pi_KFGbBRtTd4BZoDkYufZmKEo-eH68rdYSvJcBkC3zM9B4AEnI26kq-Uvo9YTsVewjbeU9DiuSRkoFPze_-zH33IQNhvYqZB-DlgyYEa3PRmQwyBD8VMctqccbrxvqqDb-Brj1GwxuOmtZtKKi6tYG8gjcmRSpzKznSuJO88t9vJC3AztB4qFtPu0u1a-rqj9dEVl8bGEA1ChriBHNXSSfStwLry0IhtnqoplSY-DvChC6LnL-jVDEuuB0gNLTq0dw4uhCEDREsgcn0MXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز، ۱۶ مهر؛ روز بزرگداشت داریوش بزرگ، شاهنشاهی که نامش با شکوه و اقتدار ایران هخامنشی گره خورده
👑
داریوش بزرگ در سال ۵۲۲ پیش از میلاد به تخت نشست؛ در حالی که شاهنشاهی هخامنشی درگیر شورش‌های گسترده‌ای از ماد و بابل تا پارس، ایلام و ارمنستان بود. او طبق کتیبه بیستون، طی ۱۹ نبرد مدعیان سلطنت و شورشیان رو شکست داد و دوباره یکپارچگی شاهنشاهی رو برقرار کرد.
در دوران داریوش بزرگ، قلمرو هخامنشی از شرق تا حوالی دره سند و از غرب تا تراکیه و بخش‌هایی از بالکان گسترش پیدا کرد. او همچنین فرمان ساخت تخت‌جمشید رو صادر کرد؛ یکی از ماندگارترین نمادهای تمدن ایران باستان.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84591" target="_blank">📅 14:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84590">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نیویورک تایمز:
پاکستان به کمپین نظامی عربستان سعودی علیه حوثی‌ها در یمن پیوسته است.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84590" target="_blank">📅 13:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84589">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خیلی دوس دارم صبحتونو با درو دافایی که تو اینستا دابسمش میگیرن شروع کنم ولی اکسپلورم کلا شده کچالویی که باباش داره مسافرت و بهش پول داده تا ۲ سال دیگه برگرده ببینه با پول چیکار کرده</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84589" target="_blank">📅 12:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84588">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRbq2eYTJ2DbZ3HeMyI0tD5zfT8GGiER-erUnQPjLSCJad7HwbBrnl1nHae4hmeWZXovs6wOaaGbX_8G62VFBK_SCfB2Y74pEeLoi6Kpy1tV36NyJnKk7tDdrY31CUAsz1R5YSOISxZ1GcopBnYi0CU4fqW2qmJNV9W7zx6ockTzrVMwZEiBieSi9sPBDoLr5Z9UENld8HuFR9ucnC_ZqFJX1MQsmfukbMIS74FKcZUskt8j1boquAuyt_kP8ofMdGtOVEgOy9dfgW2rLefLotQwdgYPL-OA4pBeYSnoSH3rNrcJmlNIBuj4QZTUqFGnZwv_jRjroHl3wpX9G10bQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84588" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84587">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84587" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84586">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AC_Dy4TGeZE8-ntwpjm_z3LTPsInuGDTJt9G4D--M-81V79MKf6wPgnuBhDxbKgtyDEu7ufRq3DebaRaXGM2d4-F4cliRaZ3KWfxnxwor3EmnVMAdldkj25o_5P7YujmNm9AfHpVHKLsV0Bm4pfUG-584ccP04hG_JQK96L5IoafkmWIVheCaP7WKc1DQK8idWpbMRDVTaBwgqHI89y0-aHep0ku9mPuiUdHNhb9oEJoGdc4e262DVC5NrQ-6svHrGhEGsHI3fOKX1m5il07FXI169N28AwKknIXzvSA2jwSqqMKVeWyE8xQdbm5tq1NiWrRPeJTfSqOZCj8MgaOZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
آلومینیوم اراک  - ملوان
🌎
ساعت 16:00
⚽️
گل گهر سیرجان  - استقلال خوزستان
🌎
ساعت 16:45
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:r16
🅰
🔗
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84586" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84585">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خیلیا تو بندر صدای انفجار شنیدن حالا معلوم نیست چی ترکیده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84585" target="_blank">📅 09:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84584">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وحید جان بیدار شو، زدن</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84584" target="_blank">📅 09:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84583">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4894c49154.mp4?token=b9bNjFLqW5NXoddHv25fVMI-UiR1zrDc4d5HjkDS4UKWL-vrGWpuETUzuT_LSuDu9zKcDsY-qVWnOljO3MHyB1bKtyQca5H3wgTu0EVxjHF2hL2mqMoGyEhpL3FEaCmWoJ2vYSMm-p23ODgJYJ5WBk1npLesi1Mrx9zQWIttdkYwF5cc_u6Hp-mSreiTszgyQoRFgVLDKPya9ikSCrkXbIUQ0H5hTLyLwEiS_0dcZsp8ZCWPyqZ9aJ3SHP91FNf_uTPewmvvOBA8bjCkyWJx2GRfka8pWWlBnxJFseltRzQJSwh_qGi5R-9yoxMYNzPCsvc8n954o11U4LFuyxzZhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4894c49154.mp4?token=b9bNjFLqW5NXoddHv25fVMI-UiR1zrDc4d5HjkDS4UKWL-vrGWpuETUzuT_LSuDu9zKcDsY-qVWnOljO3MHyB1bKtyQca5H3wgTu0EVxjHF2hL2mqMoGyEhpL3FEaCmWoJ2vYSMm-p23ODgJYJ5WBk1npLesi1Mrx9zQWIttdkYwF5cc_u6Hp-mSreiTszgyQoRFgVLDKPya9ikSCrkXbIUQ0H5hTLyLwEiS_0dcZsp8ZCWPyqZ9aJ3SHP91FNf_uTPewmvvOBA8bjCkyWJx2GRfka8pWWlBnxJFseltRzQJSwh_qGi5R-9yoxMYNzPCsvc8n954o11U4LFuyxzZhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ آقای زنوزی پولاشو از کجا اورده؟
- آذربایجان ستار خان و باقرخان داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84583" target="_blank">📅 09:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84582">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSTQu5AlbDZgvqoDkptfLoL6c5hQ1MPaGWxi1q7bUGWK0T7N4tuzQ-ZF6YaMSZRTSGGQcWOEMqfMmQjSThnBSRrSyY_-2fMkyUh9QORbo0EMurJEsBYUDe4PRV0ctsA1fCoZeQ7cLS2Q2XjYmmf1UK24VsjYMO96z19QBy_Dhk7i2rsxG-HLUplcvVxh-aZ2I-309SKhzvuFn__AtUxCUM6GcEYdWLZJbqnZlnR0-AAOd4WI366z8Xk3swV_37vG1HDOSTQabOysZZEy4s3pNL-j2ZGJB5xFtiT8pN1-mTTAc2JVxfKn96fQAIYz3MVlFgWl8GYkRvSQSQWzMEGcIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاوه گویی رسانه‌ی جعلی آکسیوس:
مقامات جنایتکار پنتاگون به سنت‌کام دستور دادن تا آماده بشن برای حمله‌ی مجدد به خاک مقدس جمهوری اسلامی ایران قبل از انتخابات میان‌دوره‌ای آمریکا.
همچنین دو مقام اسرائیلی گفتند که احتمال حمله‌ی پیش‌دستانه‌ی سپاه بسیار بالاست، زیرا آنها دوبار دچار غافلگیری شده‌اند و دوست ندارند این غافلگیر شدن برای بار سوم هم اتفاق بیافتد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84582" target="_blank">📅 03:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84581">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یه ۶ تا ترک کنسلی و انریلیز از تیجی لیک شده، اگه علاقه به گوش دادنش دارید چنل آرشیو گذاشتم برید گوش بدید  Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84581" target="_blank">📅 01:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84580">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یه ۶ تا ترک کنسلی و انریلیز از تیجی لیک شده، اگه علاقه به گوش دادنش دارید چنل آرشیو گذاشتم برید گوش بدید
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84580" target="_blank">📅 00:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84579">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دوستان زیاد دنبال موضوع فعالیت این چنل نباشید، هرچیزی جالب باشه یا حتی جالب نباشه رو میزاریم ما
هدف ما راحتی شماست که مجبور نباشید چندتا چنل جوین باشید</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84579" target="_blank">📅 00:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84578">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رسما جنگ زمینیه
افراد مسلح ناشناس با شلیک راکت آرپی‌جی و تیراندازی با سلاح‌های سبک و نیمه‌سنگین، مقر فرماندهی انتظامی جالق در شهرستان گلشن را هدف قرار دادند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/84578" target="_blank">📅 00:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84576">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015c4e30e6.mp4?token=VPRzB8-j1u7AXw-obwME6BnRcRXmwpXvjs3a91Oy4LHu8GUVAJman1GPw1azPxo81PtcZKJglyHddvFDfCbBy1lXtw9nfTSkN9GLTlxKZOyS96gzVFBbxoQy3TQv-XpBwW-SCzzN_X8PZSKQCMAIqVHZyFCc3oTZ9-rSHD8BXimktKP2nrrXCmfyWdHSGSI7zT_JyGhljxsMvFq2Q_sPMxP8NXKP6eOptRwBo0lBcO-age5FMOCjB8nDFoNIr4QP_Up4vSGavEHPrxl0s5UrTGM5yDU0C6jQLqc5oxrYOJ6biIFfnKQUoqsWbLl7m-iac98xbenDHreC0vy1lyt3Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015c4e30e6.mp4?token=VPRzB8-j1u7AXw-obwME6BnRcRXmwpXvjs3a91Oy4LHu8GUVAJman1GPw1azPxo81PtcZKJglyHddvFDfCbBy1lXtw9nfTSkN9GLTlxKZOyS96gzVFBbxoQy3TQv-XpBwW-SCzzN_X8PZSKQCMAIqVHZyFCc3oTZ9-rSHD8BXimktKP2nrrXCmfyWdHSGSI7zT_JyGhljxsMvFq2Q_sPMxP8NXKP6eOptRwBo0lBcO-age5FMOCjB8nDFoNIr4QP_Up4vSGavEHPrxl0s5UrTGM5yDU0C6jQLqc5oxrYOJ6biIFfnKQUoqsWbLl7m-iac98xbenDHreC0vy1lyt3Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی قیاسی رو با تیر متوقف کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/84576" target="_blank">📅 23:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84574">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0uoj0ETrekqQ32gWkGD9wNragXg4NvU173Pkl-kRGLyfTRizXSTMVDAFYwRjrFbTrmM9qHJHX5TBtMPC3NHQYKPwF7mm7_0-ID5bMupZU__XRkiK1hYI12hrSBmk_srkVrNjL1NVz-KSKuErsfHb2A5eUPAj82YCOmlAWEbwxeSmUN2LbIf-exiZpfqwoPaLqzD3o33AAT37Uf25f_Nk4JDmiiBoy5lfdQ_lZBHFJ5_DfW-O9MFTJcSH5vds5BGBABhXRSAnULx6PvqKXd3J82fxsCuv9lTZEFd9afej3BmKCFw3qC4MBYmCfc5PVVKe-2AZ-NGlNyIMrL7NieuYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYXGaxPA-Xzc-sC3l4xbUlL5Ky-OuugwHgv6kYUEm4yV1qDg5CB7FOBWAEYW9fxTuIQfk3miZadB74Lszt75vOOqTxIcf5bZEHDiQZAI87SEhLKdku0AzBtnV2TfvcKOTFJISsWGt9e-tfMPo-6n01GVft04rzzP3EKViC3tiyJz-JxvrzC7JUHS7rFPfqFZzpU4OZwl0bnrNw18n6NX1TpwIhJugr-FrfoDE0XQ-y-bnWY8KZJmfuHnzj2SFMBSlycveD_AcJBp06uYpjNOFF_5GQDXgFqpBjOdk2ttUUn3GjD_SxD-n0ieg5kYCbx86MNmTCLhn_JfK5y91w99Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاگان و ادرویت دوباره افتادن به جون هم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84574" target="_blank">📅 23:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84573">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐒𝐡𝐚𝐲𝐚𝐧</strong></div>
<div class="tg-text">بلندگو هاشون خوب نبوده</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84573" target="_blank">📅 23:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84572">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3a994e34.mp4?token=LzR0kTuYdhtDSJJlO6jQq6M4I2kbK0j1gXrRH53ZtX6MTsBMDLLyAU0n6iwMlSqpUh6MsJrOxaYGh_6mkhCyZwEUn1iM7_9-cLVjdONcaqfP872BQHB5QrfnqpNhvxNlujwAN1hqWpPMB0QSHohJbBjdRn0_EqrmMFohiEMlreYjAQP8EMoUpPx85-325nrbAQX29IW9E1jLObMA4jxkfAIt38dkiLaM82gLcN7XekF9o59S5txHNvIgUSBBoSRSNDzI4GLQxbHJsKWUS4_By4jEBRJnegtk1c19rcE5W1CpnU2ipgXZ1jFIZfmZpZJm_XowJRn60uPPKBi8IL377w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3a994e34.mp4?token=LzR0kTuYdhtDSJJlO6jQq6M4I2kbK0j1gXrRH53ZtX6MTsBMDLLyAU0n6iwMlSqpUh6MsJrOxaYGh_6mkhCyZwEUn1iM7_9-cLVjdONcaqfP872BQHB5QrfnqpNhvxNlujwAN1hqWpPMB0QSHohJbBjdRn0_EqrmMFohiEMlreYjAQP8EMoUpPx85-325nrbAQX29IW9E1jLObMA4jxkfAIt38dkiLaM82gLcN7XekF9o59S5txHNvIgUSBBoSRSNDzI4GLQxbHJsKWUS4_By4jEBRJnegtk1c19rcE5W1CpnU2ipgXZ1jFIZfmZpZJm_XowJRn60uPPKBi8IL377w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میا خانوم انگار تو کنسرتش خراب کاری کرده و خوب نخونده، ولی خب به کسی مربوط نیست ایشون هرکاری کنه درسته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84572" target="_blank">📅 23:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84571">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35a289765.mp4?token=L1yOw2OOGBGanY49KeRY1rIkcgOdWwsayailPtx876iEI748RkE8A8Lsh_8x-8k1bunyFoL7-nY6Zh3Laqc0hYdsB91WUJ7P7pSQ2NqlbTbNfyw3qZATpVYTfMd4hW6UkndZf9P743vbpA2bLHrI_UHBHJHr6J8PIaK3b6nsk5ePEoK9S8x4iu2VgYn0o75WE2uDL7ue5-KIKnlhvSxlNDf_dOoulgxQDJGeJeRYi8yKmVkL8jShvhXZIvxO-wXRDtcBUfNUUSOG6JrvGM6Nc4VdwlqEG-6S-YDDzLg29mbz-1nB1sFtXCNQ7RkyDG669IX2GtbBBrTYohN-x3KTgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35a289765.mp4?token=L1yOw2OOGBGanY49KeRY1rIkcgOdWwsayailPtx876iEI748RkE8A8Lsh_8x-8k1bunyFoL7-nY6Zh3Laqc0hYdsB91WUJ7P7pSQ2NqlbTbNfyw3qZATpVYTfMd4hW6UkndZf9P743vbpA2bLHrI_UHBHJHr6J8PIaK3b6nsk5ePEoK9S8x4iu2VgYn0o75WE2uDL7ue5-KIKnlhvSxlNDf_dOoulgxQDJGeJeRYi8yKmVkL8jShvhXZIvxO-wXRDtcBUfNUUSOG6JrvGM6Nc4VdwlqEG-6S-YDDzLg29mbz-1nB1sFtXCNQ7RkyDG669IX2GtbBBrTYohN-x3KTgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلوت کنید آقای سامان ویلسونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84571" target="_blank">📅 22:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84568">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udZJqICLBsqnDtLnzwjDi3157gvcicypkZ00fDEJX01jUWxDnNaZiu-SUqbNAojXQYyLVMpmujRlKXEYrXGjDSwo_oH2DiqD_HPz0f_aU5tIRrdotQ4vRwrHAbUTtzoVUi5Cvp6dqGjM3pPXqYd9JJs29Tzff20lvE0PD6D3qVYrQfSFYy3wx_spknpjC841b71LvJYzI9HkdxOXwrVMgeQX-WLQZQD6L9pq95LnXZttimAeDVgfr_1jyVPYd2YRH0ozuul7b2eavxLJL2rTGmBTmgnzpO9QdL0-_wOiA3VglcUeZEsP6ZiKpNBXGL5KROG7ChgbqMLQsB0QoL1LYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت رونالدو برای مسی: لئو، سال‌های زیادی از کشورت دفاع کردی و تاریخی ساختی که برای همیشه ماندگار خواهد بود. بابت تمام چیزهایی که با آرژانتین به دست آوردی، نهایت احترام رو برات قائلم. یه بغل گرم...
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84568" target="_blank">📅 21:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84567">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کیانا عظیمیان خودش یکی حرومزاده تر از مهدیاره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84567" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84566">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/absv758aq5xIdBgHXdcHArkTGK6ZZB5YPHc6KNUrQQWwLBP74F4KpJ0gr2TsJwL_HWllkMepEO71KJQkgYHZ_jmG7OeLevk1LMqL0SORJ2p_CN3kZdU0XQdBKfmQ4IqUfHxLU_AOEtotRFWp1ACbURDIDF1iwkbE6OoF2wkBo07YuDlMdwWnkZFG4gla44ZikfhT4fkferosgPbxrvdXnbp27JnmEU-PW-vvGu5htJLFVDhmGJ7gWU3Q4S38_yOE8b7_jPMrFc7c_2KFytifL7kG8gp341w5DFjNuyjMUiJqMt6zyHaotCU3SBL0lHHEwkv2ZILPsb4r12DK1Vqhhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری های صاحب صفحه‌ی ۱۵۰۰ تصویر خطاب به مهدیار و ملتفت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84566" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84565">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مسی کصکش جام جهانی خداحافظی کرده بودی دیگه بازی خداحافظی چی بود پولامونو بگا دادی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84565" target="_blank">📅 20:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84564">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پاییز نیومده ثابت کرد بهترین فصل ساله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84564" target="_blank">📅 20:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84561">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">HEJAB</div>
  <div class="tg-doc-extra">The Creator & Lickel</div>
</div>
<a href="https://t.me/funhiphop/84561" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام حجاب منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84561" target="_blank">📅 20:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84560">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0XU8Lq9eC4OoN9Qhe_tWJvyNd_jlI7ZqONEQIZ_ukxygqTfxy0mXp3Z4mOpXcJK35ZGg-3UOBXq9roFPNC_dPsBldzxRADXhwFnxnevcLCmQYVA1m6T3eHbcMlRWvGaf4gbinzqSYBFLHn1hklH7GfMuf3UI5ubFuSAoD4DgJfYlo0o9jOnaMK19oESxqBdZqi4hQ5j2lyAsGn8wQW7bOdWAcuboZJLpVUN0vcwAJsMB73AeO99eRDi3YMkpw8MzbDEAYRD0vlMhixliuI6f4cjZf0v-hC2ZOOODwDnwGV0g5tlsVJUqepu2mJK7Zz2a31EdU3IgBMExrREUGkl8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام حجاب منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84560" target="_blank">📅 20:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84559">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b1e1871fe.mp4?token=MQUpn5WzlHgD_dq70MTISBeTnj4y-T_Mv5iR3cja3QMvavNB5LIux0BwBf8AdN9Dy8E3pKnFyzBOCyBAWLkHb6ZVJm62RaBhiLpWF03R04gRjIx9LqD5Xnmkl37OoQCfWggLL_N0KRV53vfKo69jv8DAZpRDADW6FpEa2705BwTF-RJnCGhy9BL_8mQiuHG8qveuYa63xeb3A_aX1QE4TL4zNMYISp1YtHdZkCl58S3i2ZCAkUGpsFaRiX5pMI_dHlmNPWSPgEySV18JVAjX7DjTmYU9WubbgnXnWAiEOOPeuP0pqBCdWFyOkQ4-pDRGc6NbRC1kOflSvRZ20CAKlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b1e1871fe.mp4?token=MQUpn5WzlHgD_dq70MTISBeTnj4y-T_Mv5iR3cja3QMvavNB5LIux0BwBf8AdN9Dy8E3pKnFyzBOCyBAWLkHb6ZVJm62RaBhiLpWF03R04gRjIx9LqD5Xnmkl37OoQCfWggLL_N0KRV53vfKo69jv8DAZpRDADW6FpEa2705BwTF-RJnCGhy9BL_8mQiuHG8qveuYa63xeb3A_aX1QE4TL4zNMYISp1YtHdZkCl58S3i2ZCAkUGpsFaRiX5pMI_dHlmNPWSPgEySV18JVAjX7DjTmYU9WubbgnXnWAiEOOPeuP0pqBCdWFyOkQ4-pDRGc6NbRC1kOflSvRZ20CAKlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دسسخوش با ۵ تا سرعت پراید چپ شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84559" target="_blank">📅 19:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84558">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emmU81hMIulexSLwIrFPeeM4iUzUQBLVNBndnnFytUa2BO4Kuni5NWN0-Wv0rIZLjrHaXb_Tg7BYxtIXjbiaDYBjZcVdwJFw-YfU_yuwWMugarY-eRqbZTyzMcX0We_iknKbGrEqdmSEYt3z_t-5auPSZj6yWpAcAJVPqC2F9UnEQOZ_tQpGsPdFjBUvHnc-WTP6Zbf04wCRUe1F0LGINgEH75yjSc0MgzP2IlBZyU-nfPLxjC16tF2Z0yHc4CG1U5iUzG2Lz4GFokB1sqhI-mUR_PvGBJNYVD8P4lZs0jbrvWC69RR9DxKUSkrSfhjKjm6UEIYSLGHAaZSmQHE1eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر این کامنت ادمین دومینو بسیجیا دارن دهن شرکت دومینو رو‌ میگان و هر روز جلوش تجمع میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84558" target="_blank">📅 19:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84557">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzuW7o0wXV7GftwxD-t-7GYW_HoY9zL0Ack67D32QGMf4INjlCwtluYtJSlvZldh6cNr-Wgy-zbiSqLpmo-brhep-eltf5fRJ3vs7Nn96QHl1HW9T4rOWzzElBnapWAnLyglVu5jCPtaDFWkqbGt7Z7bQthimI0EwoVurdlaLiMRdHKgmMPxHYgkzZdCq_PCavL0x-Xf2pVLr7CZ5IlrIj4_O2RQcbRmnx7wHMCJ7aHexKNhkpwOcGNjLm3Y7dMMWndsfLkmUvIHf12mdmMSvvp5Y9j-uGHIcLekLudalHOC0XIgx7O6P27oMg9fpDCf7AuzKLQR1RcQSA29JNxttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیم‌کارت با قابلیت درآمد زایی؟ اونم تو؟ بیا برو مادرج
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84557" target="_blank">📅 18:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84556">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546bf4e186.mp4?token=D5nX_k7fglvwX5Z6VtQ_llTkhUxEbr1wgCIQ3KQhjbVuQOLq-xNz022gT4RQOsllLSkhh5q0mtKrZ1h0iW8K1EggX7S-jiHs2pWv7x76esfb-83FkJBjK8-2831LQtvX1E7T9mZgGigjedS7eml_zAyfOeRBAFXN9YV4ZjAJwfR5G05fD6dOZPdjkSzLgB2TqIGEJTNWnYAbty6Y47-2Qi5luR4O4nyLepIOinaQNryQZiz9AXSnCeZw5dSEyvWCxrY4mTZpd4nYxgZ4OTonB6axR3W3STYQFgdytrnK6BKJfN8t9RHxgYaKgLM0izTt3g-bXyZ-9IB-4KHj2XzqUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546bf4e186.mp4?token=D5nX_k7fglvwX5Z6VtQ_llTkhUxEbr1wgCIQ3KQhjbVuQOLq-xNz022gT4RQOsllLSkhh5q0mtKrZ1h0iW8K1EggX7S-jiHs2pWv7x76esfb-83FkJBjK8-2831LQtvX1E7T9mZgGigjedS7eml_zAyfOeRBAFXN9YV4ZjAJwfR5G05fD6dOZPdjkSzLgB2TqIGEJTNWnYAbty6Y47-2Qi5luR4O4nyLepIOinaQNryQZiz9AXSnCeZw5dSEyvWCxrY4mTZpd4nYxgZ4OTonB6axR3W3STYQFgdytrnK6BKJfN8t9RHxgYaKgLM0izTt3g-bXyZ-9IB-4KHj2XzqUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمااااام تتلو همه تتو هاشو لیزر کرده و از زندان آزاد شده
😐
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84556" target="_blank">📅 17:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84553">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yc4vmJOnEvev8A-HhXci8rL0FVDuBqrltx2N431xiZuWvH636Lp4G9kdQLFMnk8Ea5TcQRPJ7SHNcRF0BzukbSMVd1Ak8AX54rFxQwyGLwB9q-pj0gr_oSrX5XXDWukfY_4Z31ozRRHf0Z0Fk7sR7tGW-IkzajGg9-gnnENOnO6329sHXOWhGew0A0BUhNVpZlUM4OjqTjznFYXwcqnEl0yFsOyimdolNfYtu75D4NoB0mf4f7A8mXmjo9s5bhalXjLGIdVAX9-T5r0Bomsfmx5a7gO9Njgp_DjyLux4c0lmUkmhE49S0X_T13BTFtichi1tlKeomyDNmGXmzLsNPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نارین خانم دختر ۱۵ ساله سنندجی که تا سر حد مرگ توسط پدر و نامادریش شکنجه میشد زیر نظر پزشک تحت درمان قرار گرفت و بالاخره حال روحی و جسمیش بهبود یافته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84553" target="_blank">📅 17:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84552">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adnfESjMrk360dR5PFBHOaD_Ks4v7ZMCc6ld3B0xVfcFHchkZaHBSuYF12CM_hi6zWmFowA61UzIRQYQwQfwdJPsqZvobJ2-atp0Uo0VI0ut31TS46xRTbwHaiGws0nrgyRAXYfAtMEcvgRgGIEYoXq06ZYpSsRF5_KVmOMr050BPds0mMRKglc0F0_VEptTsDOFzHkOVEjk0zaciSwNAxFmMLo7QMBVnrd0zz20nn_wVjNXELbmtuAdVDpJ_DRPKn6ZunDte-0YKfzVfByM1E4XP9HP7-fSHzwam6cg955HBsANHCjEvMpWnHMtmZiXG9i1kf5nmlJvl_2FYtrO6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اینجا واس دوستام تعریف میکردم تو مدارس ایران همو انگشت میکنن خایه کرده بودن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84552" target="_blank">📅 16:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84551">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">من اکسپلورمو به کچالو و مردی که عدد روی پیشونیش رو قایم میکنه سوخت دادم، هر کاری میکنم هم درست نمیشه</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84551" target="_blank">📅 16:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84550">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSHZ6Id5_lQHE1S0_VDNNSlWps2BpQOXvkXVTiSl9Qf-PWM-E2LYUn3dyIkmPqs1dVzas5xeq89qi1P05oA9kAlFOj7jCXLJAyHWobVfAQkq2P9BO_6A_dxp9f6fFuEtPWgmZa72PVoJCTpt-AH3Wi28cL1Uc_emHr04iOnDhNPjwdmLZfEQnqDFss1xGxZHPPP9hOy0tCNuJoNTFr2qWLXgxbSfRLiO_UmR7VgCwvPADAi80ixlLKrV9ohrpZLs8HaJ6WmzLfwtdHY9PqPPt-39t8nWuK9UDfp8KzeLnsMj8WyIQe6ivODIq1Lvzlsk5-noGmwlL-pm2bAcMiTjYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نالوتی یه ویدیو با هوش مصنوعی ساخته سلطان ازاد شده کل کسایی که تو توییتر هستن باور کردن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84550" target="_blank">📅 15:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84549">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=JZMVov-mlEwdCA71kf3u9UfHuxoZdaUVpDPIP1_jxG3hZffVIEoC0mc44W5XSZtkfO9k_nVeMtcYqR7WQGQo9e85IQYmou-i5J_NIrh3ShmuUkHgbf180Wqn7F6sZnoDEi6x57HfAHGwZhF-lX6-V_34zuYPypYXxrU3LLDwhvcD3Xo9_RM3FaGVSh_xOb4SEtgPgqpJZ9KGgjZIAArNyxeY9X1Ok15b2I6oHc-jPGA60kuljftOjJRgV5Ch_y4aOPuDM77TzhrzEGdIuor0ts8BflE_8_q8nFLHyJqV_50ernZ6n9l7TeISNBsExVx-VAQPfrxDn5V2QBaLYBCpJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=JZMVov-mlEwdCA71kf3u9UfHuxoZdaUVpDPIP1_jxG3hZffVIEoC0mc44W5XSZtkfO9k_nVeMtcYqR7WQGQo9e85IQYmou-i5J_NIrh3ShmuUkHgbf180Wqn7F6sZnoDEi6x57HfAHGwZhF-lX6-V_34zuYPypYXxrU3LLDwhvcD3Xo9_RM3FaGVSh_xOb4SEtgPgqpJZ9KGgjZIAArNyxeY9X1Ok15b2I6oHc-jPGA60kuljftOjJRgV5Ch_y4aOPuDM77TzhrzEGdIuor0ts8BflE_8_q8nFLHyJqV_50ernZ6n9l7TeISNBsExVx-VAQPfrxDn5V2QBaLYBCpJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانک مرکزی افغانستان در گزارشی خبر از شکست دلار توسط پول ملی این کشور را داد
در این گزارش آمده است که:
سال ۲۰۲۲ 1 دلار = 90 افغانی
سال ۲۰۲۶ 1 دلار = 65 افغانی</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84549" target="_blank">📅 13:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84548">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبرنگار حوادث: تو کارخانه شیرخشک سازی،کارگر با کارفرما دعواش میشه،برای انتقام مخفیانه ۲۰ لیتر اسید توی مخزن شیر میریزه و لحظه‌ی آخری آزمایشگاه کارخانه متوجه این قضیه میشه و از یک بگایی بزرگ جلوگیری میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84548" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84547">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رایتل یه خبرایی از واگذاریش بخاطر ورشکستگی پخش شد، ولی به دلایل کاملا نامعلوم مدیر عاملش اومد گفت کیری سودیم واگذاری در کار نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84547" target="_blank">📅 13:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84546">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=hG14-fXVHc1LVC7NPzo2Ami630AKEVEaSIjrnlUCZyrvorAdwvjXm9SjV-eFqCl5wpJuLBFxqird6p3ZnDPPzPqA2G_FaiZqnCkDSIN75bmgocjZ1KII_mY8gcaC0VV41MvccKvkfi1lfWV0C4xqnOgApQH1l1SyEe9uAQx-omfl9YSZ3dGA-VSm4dMJiL85V85dtWG2euXYbGzz0h4b9XT4PhFrbJrOEMm6CIN1D6SiPBR8Q9d3JSMwdox_eTct-u1C1WwFML6UYbby-c3jZKTfC8k4-Onp1ejCwdY7iVel-oRweeJJSD5X5TkXTjpT0BQ9n9ypeGeJxIfhOTE5FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=hG14-fXVHc1LVC7NPzo2Ami630AKEVEaSIjrnlUCZyrvorAdwvjXm9SjV-eFqCl5wpJuLBFxqird6p3ZnDPPzPqA2G_FaiZqnCkDSIN75bmgocjZ1KII_mY8gcaC0VV41MvccKvkfi1lfWV0C4xqnOgApQH1l1SyEe9uAQx-omfl9YSZ3dGA-VSm4dMJiL85V85dtWG2euXYbGzz0h4b9XT4PhFrbJrOEMm6CIN1D6SiPBR8Q9d3JSMwdox_eTct-u1C1WwFML6UYbby-c3jZKTfC8k4-Onp1ejCwdY7iVel-oRweeJJSD5X5TkXTjpT0BQ9n9ypeGeJxIfhOTE5FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خلاصه دستاوردهای همتی در بانک مرکزی.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84546" target="_blank">📅 12:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84544">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s48Y_gGBgYGQE6Jddk81QXy8L4PBc-W3ghFA5YdbLelWb8903sB-5hgRUNy5Wy7eNwNqVBlMhGW8mEzQosH1kixJ5GufXlsifu9RwSuAi4kCn8Qqco5_m9Kkl-Ay-cUau-8ir1N9rhZk7o4LETAPPkb1-9gttykfw4ThRO1rYVzyth-UkJZ2rbRsEeo1IyeKvz_-LoRlB76hjpc3k4xDd-S9VVyiF7lmZNykd0ivepmg86FKocjoa-LIdfgrxa5SrLvpROjY-qFnGxm1mFokZxEeMLQP3xjU2Qt09qJk-LlgIuYPt6IubH2Z4Hv81RHCQPOCUTeA1xuFhOGkyPmCbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86ab280716.mp4?token=apx_0pvZ_mh14QqDqA4NIWIG9zcWHZQc6uGmpoZ2po63NNS9QguBNc8KRz1dE-bNiaZDan_diNC5maGgze03KThKvG4LqDxkQpJbJwJ38GT--jqnm-aYeFpvy3RQ1TuJYxsdCQ2oFohaPLgmapVel5CXqpRfvZE35QUIvyn3PjyBFnAXj4Kz9ym6h1wzIP52R1lO5vxZswbx_Pc4DCI1Ar5FMWM_VVcsG6QXfMKSsL_TWiiwbuGiserIOQCendYGCsgx1D_wNTPmptVaWFXUJHSsvC5qRoBmHoqd8N_mozFzXjMBGtu_LVc6S9PEqV5aaKf3nNT2JwrK2EzBn2naNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86ab280716.mp4?token=apx_0pvZ_mh14QqDqA4NIWIG9zcWHZQc6uGmpoZ2po63NNS9QguBNc8KRz1dE-bNiaZDan_diNC5maGgze03KThKvG4LqDxkQpJbJwJ38GT--jqnm-aYeFpvy3RQ1TuJYxsdCQ2oFohaPLgmapVel5CXqpRfvZE35QUIvyn3PjyBFnAXj4Kz9ym6h1wzIP52R1lO5vxZswbx_Pc4DCI1Ar5FMWM_VVcsG6QXfMKSsL_TWiiwbuGiserIOQCendYGCsgx1D_wNTPmptVaWFXUJHSsvC5qRoBmHoqd8N_mozFzXjMBGtu_LVc6S9PEqV5aaKf3nNT2JwrK2EzBn2naNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نسیم مقصودلو؛ خواهر امیرتتلو :
خبرهایی که در مورد آزادی امیر پخش شده فیکه و هیچ تغییر در پروندش ایجاد نشده. اون فیلم هم که گفتم شرط عفو شدنش پاک کردن تتوهاشه مال پارساله که اونم دروغ بود.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84544" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84543">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrWjgGsgrLc0lxSK8sJi0jgEwGBamct3sdAzpfXNmldfLADy4t6PsYyYn9HInzv0UjlKgrobS24PuJmrH_MyO6ra47AFqLuRjdrxynBRkLE45RC8zlEgaoanOFxCkgx1014m7G0wchEe66PrzTHdc_h7qPSiqnlkLME7bcJcYnVR_rLWWrnTCzYA3GDG5Yy8YPM0Tnr56iOfC01zgTU2DNXFZDkXhJPo9XtMhSSgH5iwcszIafPP0m5kOsGsEk5mcQR_j8wZ5qc9VfhZPzfjPNCa7PscaxQntsGlVg5pdkZtHy_3pmdRQb7oqiYz1N4a8Z79nfdoaBH-LGJn7Yi66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شوخی شوخی جدی شد، سفارت آمریکا تو مسکو درباره احتمال ابتلا به طاعون ریوی هشدار داد و همچنین
هشدار سطح چهارم «سفر نکنید»
رو صادر کرده و از شهروندان آمریکایی حاضر تو روسیه خواسته فوراً روسیه رو‌ ترک کنن.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84543" target="_blank">📅 11:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84537">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpZ98Znd9RDeygFlnx_3KtEKRYUmLa6uayYlik8p_hGStG0wbSKEkc4KvQmvFJR-MvFpmDq8d5B9d6mqQaIm67DDGSB_hbP7bj0H0xJ-qo3oZNL1f-wrClpaSTsoPhFERgXSCsud-0VFhlFpwOLf1_MiJLAVTMD0-GB7eBW7Hw1x5Xf-F40j7J7SLNE3XCf9GJBc_5BaN0THih_EKfnMXpj7MzeZXWHsdZBCFr0hoJwEACDXzYK8CTAyC5-bEK71taxzaPI4emTnwmNWKIRYbanY5GL9Jms8jBzfaf3sVlmbZJEEmFXfbKw7gVCg-6MLoitX6Al06jjYynfeVN59jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدجور دارید تو طبقات بالا ویولن می‌زنید ها
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84537" target="_blank">📅 11:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84536">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAnCr7rogDhC7380ZSI0w65fpUUgaVfyNtjJCEkmawGDc1QksMxP3Pe24qdrlLmDRcgITYggHNss8U2C8f-k8KmE3sIiZbplj1zK65iZXOG2g4HplgVIbw3no2QjIxHF4izTbSejgODvCMKFjEQbaShQ3PH_t3ZkaGqV9ReqR7xRl40ISXa-wLAXFGHQPTat3JG-k6fRk6M2gtqsBqQRmOeXj6PAU-rBkFUb1dNi05F4y3isHFnfike1muAOMO0zomPwJFhNjpbuZ6rprMSzp3mCwiFrCE0MQyByvV8-AH7MfzQERv8ofZcQ1LI0BanL5O-NqbiXvx5qAg6qpRTcxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام امروز هفتم اکتبره.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84536" target="_blank">📅 10:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84535">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d26406817b.mp4?token=O2ujH_TUvy54Yc-ynaQx5zhmCbnF3CTaLgdAvY-EKU6sPP3i9H3D1qmBCpOq9JlPP3LDICmdqyfMRY_zBVNwZtfoVJH4KibtN8P5cRoLIbYa1h6f2faqF3j6qbU6R7n94AX2-4m8ZKdqFYadLqCSE3uF8WKOnyKUcZaZTYmPCy-e-YGO75BDGkrv8JR3KTyecMrl9e0Xijwzbz8fEyURjK_SKzaslUK5znjbox4bmhsm1zbNDwOEX4fnhP6AinX7Uod7g0XeGCSE_j9fHzZUt5-scCU_Cmjfu8JRtg6vJtneQox3uxGOyu2E71Buu5_JQ06rdMWY4mYmhINqdWqjxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d26406817b.mp4?token=O2ujH_TUvy54Yc-ynaQx5zhmCbnF3CTaLgdAvY-EKU6sPP3i9H3D1qmBCpOq9JlPP3LDICmdqyfMRY_zBVNwZtfoVJH4KibtN8P5cRoLIbYa1h6f2faqF3j6qbU6R7n94AX2-4m8ZKdqFYadLqCSE3uF8WKOnyKUcZaZTYmPCy-e-YGO75BDGkrv8JR3KTyecMrl9e0Xijwzbz8fEyURjK_SKzaslUK5znjbox4bmhsm1zbNDwOEX4fnhP6AinX7Uod7g0XeGCSE_j9fHzZUt5-scCU_Cmjfu8JRtg6vJtneQox3uxGOyu2E71Buu5_JQ06rdMWY4mYmhINqdWqjxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام من از آینده میام
حدس بزن چی شد؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84535" target="_blank">📅 09:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84534">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLrKPkFzy6YS2yxiMha7Vmn-0a0LkhTzq7vkjeydwM0x-7h2w0FqZqLJs8_YmfB0ihrt270FoxXPKCHiqcgJds4LAhDhKg7oRDg-6KHlng1Bugxl9j-gqCcx6QtZYaGuxHk8uIqJ0RczscYUx8wvIJJrgxbCveTBG2AEnq96acEcV5uilkoR5B0xiwDbF9bDEKRi-VJwi-Ej92IePx8EmNBtw5XKdQiQy_mI1P85A7z2iEnZEFH6Yp9cJgK0jGKK3RqTXn1gcWFkGNTjwZDHNok_V1P-btGYprL5ffD5sHbowgdLkYaccZ9WFIQhHgSqJWUYNqgYLo58VY7xXmRUpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی بنین در بازی امشب.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84534" target="_blank">📅 03:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84533">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یکی بره اینارو بین نیمه توجیه کنه بازی اخره یه ۱۰ تایی بخورید</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84533" target="_blank">📅 03:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84532">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کسکشا این دیگ چیه اوردین جلو ارژانتین بازی کنه</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84532" target="_blank">📅 03:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84530">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mlm6AicmTout6Zp3A8zr8EVThsZgO-c2Aq-xWSkt9CADLRHfi1GvF_3lhu7wspVyr4GdD2k_M5qhwTRfR0Cd7rJP3Sc1bemdUDDa5s5QSRQHDJn2-O113wlU7xcxha2abITGpPj4inFwEwwWjA-Ee7zHQTSThkn1ig8thQMufQNqGDyt452Y0JxaKqLlniDP4H_plxFh1VVS0SoA8xIJq_jzOZRMNvjksM8KvjzE0j7g1YX7w9nsWEvE10SlTR0t43cSdviNS-GlxmD4bDDtINJw3T2-VlTStt8fs3PPEfvxhDO9ulENgdwukdK46MUKyk-08-iJoIUrDSp8opLwXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیرون ورزشگاه به بز واقعی شماره ده چسبوندن اوردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84530" target="_blank">📅 02:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84529">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY0z3hvcVK7Jndazg6tWA4z4qOARYnL3fJUSr7SbRS7HzMZlSzOTr31FJ4GBhRqGuLevP27mve2iUHkk98_p1qOD-uxeleCpQ1SFnImN68J7rdE9gO7p0YH7-XVOfBdNbXArUMtzjwOCiwDBIWuzl0625e2QLGvpL_xRj9PfhDpWvOfQBjq3AB-eSv7tqsmexTPxEGVOf9DVc1NBEYb0ISI0BHs6FgdFjwxXND23h0ewv9S3plohzFTgzL6tMitqxFfgzDuMNbWNeWfXFWsoevKiwgN-O0CefmM-JaHaIM2_LPoFeYxbT7qVVz1ofY7iSHbwfFwD9RfRDLHeT2AhMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی تو دشمنی هواداری چی ای</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84529" target="_blank">📅 02:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84527">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PV-obYzMywzsmuQch-CBX1d69zvl3B89JVoAL9oBCK8pzbMg3bDKeSl-UxYkZqkZpk7FnZ1HwnpDSs4_RYZWECB3sr0X5_R3ubKNrFzeCnfgV2KkEBwmKeM3HtW5YURRY-NMp5P-YJphP5TfeuIb4D3Tn1lPbCJvsgVx0KaTlns-5RPpph8JplB5q0RjJ39anNNHVJHZsbVUERxCh_nacxvOCCS5Xk83L7Y9S7G8jlnNF41zW5ReYH3Rgk49OJMvYLrGeMfmRaJYFh-Jr5L_RTE5huH-dowfZZrf6z9ckk6PXIVk3h8ZuKHgLAvUBi-9Aqd8xyb3B1Lpnx11f6lm3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحنه رو پسر</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84527" target="_blank">📅 02:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84526">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اگه خداحافظی مسی هم مثل آخرین کنسرت ابی بشه چی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84526" target="_blank">📅 02:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84525">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شوخی بسه دیگه حاجی، وقتشه بیایید بگید مسی تازه ۲۵ سالش شده و نیم فصل برمیگرده بارسا</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84525" target="_blank">📅 01:52 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
