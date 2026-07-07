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
<img src="https://cdn4.telesco.pe/file/djxZJL032Xjs2Lwb5RTCxPXPPL9rgtkBICFLTe8nQTjXAN0fsk6XzLiJTv_vtJ66LGnY_ea-F5X4WnygEeZ1pjUhuNBCsu7v72T98y4-pot-s3HbCuY00GEQHW4ZgIJBoqHchyUP5lyu8ie7vVrai4dH996zWAp5scvna0PpVMSCsq_ebPmgbgXvAo9nn08P-ta8lJyOxLi6yofK0zxGSMrZ3-s5YVqPsYfNCFVqm0LyqX_3TFcKgtJwgzuY3uXHhNPcjRPAzjIlVkO6P_xg_05sfco92W4OYKMt5W4PizUfX9MppfT0eQLrBZPhVqkH1_QWxVtWB1q60gQRfH3FBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 01:19:51</div>
<hr>

<div class="tg-post" id="msg-448078">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2ba5b25c.mp4?token=oJ4V10S1OQgGQDA9nUOOpZ1LF2Ptuw5oWfigHiDwrzluEx9tH1yvjx4nEXakYHywn1M6hQ2jrt-wpX29VJattFloJ1NOWLzS0UrphWHDvoRpu9en6Ae4JCpNTZdIsJglkzfCUKVgO7LsbLBUNzq0SzAavI090aAZyQ79QnFHA-KJd65AjzBp8M97ca1vIIA19xCtXlkH32WnFnHB-bHtBdcHnaI1NrlGM_jiadQ2o4MtgNza1HS3gJ22RdyO-dl7pyPMfRET_5oTAqcrXKnq8HBARyZ7Q74HQdaAOTqM5BF9DnO9H2q0vwLcL-gr6rGp4NKxNKSPac2RDWwt_TMbnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2ba5b25c.mp4?token=oJ4V10S1OQgGQDA9nUOOpZ1LF2Ptuw5oWfigHiDwrzluEx9tH1yvjx4nEXakYHywn1M6hQ2jrt-wpX29VJattFloJ1NOWLzS0UrphWHDvoRpu9en6Ae4JCpNTZdIsJglkzfCUKVgO7LsbLBUNzq0SzAavI090aAZyQ79QnFHA-KJd65AjzBp8M97ca1vIIA19xCtXlkH32WnFnHB-bHtBdcHnaI1NrlGM_jiadQ2o4MtgNza1HS3gJ22RdyO-dl7pyPMfRET_5oTAqcrXKnq8HBARyZ7Q74HQdaAOTqM5BF9DnO9H2q0vwLcL-gr6rGp4NKxNKSPac2RDWwt_TMbnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزلۀ جوانان عراقی در سوگ رهبر شهید انقلاب در بین‌الحرمین
@Farsna</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/farsna/448078" target="_blank">📅 01:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448077">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e515634f6f.mp4?token=PbLlkH5xYLjYTorbj4vbve4Dy6Ecn1gzhHxriCwbGi4SGYNEquhEcY48pUFn8GSQRtgD0Svnd6Z8eyH0dYjTEVDx9RFvsA1rY6hS815IsFUBcM_LbYs0-U6kFiTArxlewYRO-4qt4exlfazcykkI165rQ0ghQ-plLS2ztA14zOu6xMXkqSawL6_78SCvL58lgXUmaNGh48T4KdAstJhJGXSYINdkR1dRFc-LQhoc-jdZacqXlhGmW5l0Awf6kGJIva2qk9TIWGWUlrFsckrGezSPz3dM9Jm1hHx_ulZCAb5DQ61A_Pa4HLSpTjOcZZYYKpl33fSTYIDs8MN2ROkDDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e515634f6f.mp4?token=PbLlkH5xYLjYTorbj4vbve4Dy6Ecn1gzhHxriCwbGi4SGYNEquhEcY48pUFn8GSQRtgD0Svnd6Z8eyH0dYjTEVDx9RFvsA1rY6hS815IsFUBcM_LbYs0-U6kFiTArxlewYRO-4qt4exlfazcykkI165rQ0ghQ-plLS2ztA14zOu6xMXkqSawL6_78SCvL58lgXUmaNGh48T4KdAstJhJGXSYINdkR1dRFc-LQhoc-jdZacqXlhGmW5l0Awf6kGJIva2qk9TIWGWUlrFsckrGezSPz3dM9Jm1hHx_ulZCAb5DQ61A_Pa4HLSpTjOcZZYYKpl33fSTYIDs8MN2ROkDDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای بین الحرمین، پیش از آغاز مراسم تشییع پیکر رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/farsna/448077" target="_blank">📅 01:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448076">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‌ ‌
🔴
معاون بین‌الملل وزارت خارجه: حملهٔ آمریکا به ایران مصداق نقض جدی بندهای ۱ و ۲ یادداشت تفاهم اسلام‌آباد است
🔹
آمریکا در ۳ هفته گذشته نیز به‌واسطهٔ اقدامات رژیم صهیونیستی در لبنان و اظهارات تهدیدآمیز علیه ایران، بارها مرتکب نقض بندهای ۱ و ۲ یادداشت تفاهم…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/448076" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448075">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🖼
آمریکا نقض دوباره آتش‌بس با حمله به ایران را تایید کرد
🔹
سازمان تروریستی سنتکام اعلام کرد که در واکنش به حملات ادعایی ایران به کشتی‌های تجاری در تنگ هرمز، حملات تجاوزکارانه‌ای را به چند نقطه در جنوب ایران انجام داده است. @Farsna</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/448075" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448074">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_m8YqrK2oO6usbbbl_53tqQxc83pg0BCzCmhxVQYTiezGBz0jMe4XruxqXD2hIN_bZuklwx8WekqKFcT_-s0tsxB8vlfOSrdE0ZBT2P4ObjZ_Ds1d6TmN4ONEkDuSdLyIvSaZKOCXh1Ib049vTtFlBwiQQv01wIxR7dIR4nGbXFTuUrJfK_Gh-1pb2rSa8bhKA48Uw35GKNgWSJ3cpl0heg6ZfudFV5nBRiHqmmYwkSPFA2k_FlDJjcV6kzl0V6_vtKG2NEkvL131toIexvOX3F_RQ40SezBisju0nts1oh4VBoM9CX2LhQqNTj1trdZTEuv0NqzTC9wQDsHEmCzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
بدعهدی دوباره آمریکا؛ مجوز لغو موقت تحریم‌های نفتی لغو شد
🔹
دولت آمریکا به مجوز موقتی که امکان انجام برخی معاملات نفت و فرآورده‌های پتروشیمی ایران را فراهم کرده بود، پایان داد. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/448074" target="_blank">📅 00:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448073">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGTmWDbfW1VB38KPvslPdIo3OU6MPtmgOHc8iFqfahZqHv2xrI9eUuSfBpqld58aeV-412I64PxE9LwBMtEVJPgfjU-c6kOPDKbjrGyGVqvJwlcjikkBllw0p5tnKVgAoPKaxLbdyZesifF6z2rkeItcVuGDJL7VQwFJqAN78TlBSk3p9BjmI6-u3Om2pJ8_vHvBlqwX5LogpQcqmpvslWODit5TM1nXHxx9D58K-nsFi8a3pP1FG2fsyjAtwQD4E3M2LwBBx8h5GpDmHGVZzImxZUT4oI1ky_NFyaSSV3ArUdS3JuH62MouY_oXvf6O1eb0PrWzzdO6wtItntejJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
آمریکا نقض دوباره آتش‌بس با حمله به ایران را تایید کرد
🔹
سازمان تروریستی سنتکام اعلام کرد که در واکنش به حملات ادعایی ایران به کشتی‌های تجاری در تنگ هرمز، حملات تجاوزکارانه‌ای را به چند نقطه در جنوب ایران انجام داده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/448073" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448071">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در حوالی سیریک و قشم
🔹
دقایقی پیش مردم در حوالی سیریک و قشم صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
🔹
پیگیری‌های خبرنگار فارس برای مشخص شدن ابعاد دقیق این ماجرا ادامه دارد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/448071" target="_blank">📅 00:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448070">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
مردم تهران در آخرین دیدار به رهبر شهید چه گفتند
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/448070" target="_blank">📅 00:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448069">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54805647e3.mp4?token=ZTpECbQw4I0hFdKih1qjjvM8QDtn4UbMJqLEYsYOwsT6tkn7jOw5jPaqKe6X-zX4Wk0FpXpXR9xh0gVbeV1pXyJpuk3g16MFl6WyJh45W-Ki4EJFKPHMZ2MKadwmWhq_k3Q9qno91HgYgDxvuxw2IlZ7_S7zVX7peDD6EFKvmpom3GPr92VbOvyhLqDh8NtNR_KGsEbq6XZYs46OuQH5VnPOSL7CBA--1DWucdelGp99UqdS7uMU_xt9UHgkhRDTznUauM980oBX95aIAHNovx_yWxkZuNwpCLaGbe6YFQOoXx45HcS6_bGst21eJSzHpgnyJMBsGMwS2avOL-Xalg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54805647e3.mp4?token=ZTpECbQw4I0hFdKih1qjjvM8QDtn4UbMJqLEYsYOwsT6tkn7jOw5jPaqKe6X-zX4Wk0FpXpXR9xh0gVbeV1pXyJpuk3g16MFl6WyJh45W-Ki4EJFKPHMZ2MKadwmWhq_k3Q9qno91HgYgDxvuxw2IlZ7_S7zVX7peDD6EFKvmpom3GPr92VbOvyhLqDh8NtNR_KGsEbq6XZYs46OuQH5VnPOSL7CBA--1DWucdelGp99UqdS7uMU_xt9UHgkhRDTznUauM980oBX95aIAHNovx_yWxkZuNwpCLaGbe6YFQOoXx45HcS6_bGst21eJSzHpgnyJMBsGMwS2avOL-Xalg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیروهای کتائب حزب‌الله، برای تأمین امنیت مسیر تشییع پیکر امام و رهبر شهید، در مسیر بین استان‌های نجف و کربلا مستقر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/448069" target="_blank">📅 00:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448068">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
سقوط مشکوک هواپیمای پاکستانی در دریای عمان
🔹
ادارۀ فرودگاه‌های پاکستان از سقوط یک هواپیمای باری با ۵ سرنشین در دریای عمان خبر داد.
🔹
طبق این گزارش، این هواپیما ساعت ۲۱:۱۸ به وقت اقیانوس آرام از شارجه به کراچی در حرکت بود، که مشکل سیستم ناوبری را گزارش کرد و بلافاصله توسط مرکز کنترل ترافیک هوایی کراچی راهنمایی شد.
🔹
در ساعت ۲۱:۲۱، در رادار مشاهده شد که هواپیما به‌سرعت در حال کاهش ارتفاع و تغییر جهت سریع است، و پس از مدتی تقریباً در ۱۵۵ مایلی غرب کراچی در دریای عمان، ارتباط و تماس رادار قطع شد.
🔹
این حادثه در حالی رخ داده است که فعالیت‌های نظامی نیروهای ارتش آمریکا در این منطقه طی ساعات اخیر به‌شدت افزایش یافته است.
🔹
تعدادی از رسانه‌ها احتمال هدف قرارگرفتن این هواپیما توسط دستگاه نظامی ایالات متحده را مطرح کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/448068" target="_blank">📅 00:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448067">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bab243fe1a.mp4?token=Mfb85bIj_w0XsY9ANjbTWzsGGokwbn_w3o4ACI8XXf1XYKVXd3LFqnonvb2PITtJDulJ03g6KnMbiONMtGbYqJlZEB9mK71K0IavH63gX6pBriBOkKsEOGyXrfK2Ui8pMb8ASymoB1-1TStcGlTCJZtRVncnuxiSwZmWDIaFKh3Zqj0F1F1NM8x6g1jHNs_utfqvLgaq74thmis0hEu7G9GBsvWNAWrAVQpm5zy1nf-_sOAn626C6mBmNJ1-HCPWElZ1DhSsATqXbf_a4d5lnV4OTCuw1As4DctEZjZNOOCzMO_VDoeO_-rfA8VVUKOxOP6HCq96LjiBG_L3MCdsXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bab243fe1a.mp4?token=Mfb85bIj_w0XsY9ANjbTWzsGGokwbn_w3o4ACI8XXf1XYKVXd3LFqnonvb2PITtJDulJ03g6KnMbiONMtGbYqJlZEB9mK71K0IavH63gX6pBriBOkKsEOGyXrfK2Ui8pMb8ASymoB1-1TStcGlTCJZtRVncnuxiSwZmWDIaFKh3Zqj0F1F1NM8x6g1jHNs_utfqvLgaq74thmis0hEu7G9GBsvWNAWrAVQpm5zy1nf-_sOAn626C6mBmNJ1-HCPWElZ1DhSsATqXbf_a4d5lnV4OTCuw1As4DctEZjZNOOCzMO_VDoeO_-rfA8VVUKOxOP6HCq96LjiBG_L3MCdsXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویر حضرت آیت‌الله سید مجتبی خامنه‌ای در دست عزاداران رهبر شهید انقلاب در نجف   @Farsna</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/448067" target="_blank">📅 00:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448066">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDq_LnOLKrKlaGME5F4dblg_Ze6gqmgLBEgtenW-m0EQrToGezsQZHgBsKqEkSl5EUR3-75OSfM4YDP7yfwqEKEVBr4jot3YRBZqZTC-LnjVUF702_3ooyEyiS_onA0JC8qA_Y2p1LMchdqVYSD5Jmx_z4hmty2PYz9Bg-r_Sxu9Vag4371FyxUYF1h9A8Kwek30BWa7Q0zQ4tsHVkxNT68x4Ea6As7uxxbpYo9JQuN0MTfc2l09uhCG8QuYN-2sx58YtqM_BmgnKos9fA3qhHB1nO_D-n0bNz44E32DKaYcwF_kSr8p22kOw6imGAO4T8YOe5M41I_-FAiwp60NNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حواسِ آقا به این خبرنگار بود
🔹
سرم پایین بود. داشتم می‌نوشتم. توی ظل آفتاب نشسته بودم رو به رویش تا آن ماهِ تمام را بهتر و دقیق‌تر تماشا کنم. اما او متوجه رد خورشید به صورتم شده بود و با اشاره‌ای فرمود: «کی این آقا رو تو آفتاب نشونده؟ برو زیر سایه.»
🔹
آن روز، آقا نگران این بود که آفتاب روی صورت من خبرنگار، من مهمان جوان نتابد؛ و من امروز اینجا هستم تا اجازه ندهم آفتاب، مهمانان آقا را در آخرین دیدار آزار دهد...
📎
روایت عاشقی این خبرنگار را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/448066" target="_blank">📅 00:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448065">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ae004bfed.mp4?token=nStFpgo9Ufiuo3hHpZ8esqGjSUI3wyhiOiiH9BpJTJEnp4yi8uUILBrPaVVlrcpQHO-OS8GU7j1dzuYkmJFWVU5xEd0vXozzpyS6ecdcMWzvZa5EJl69wNKD-wX8E9sbJWUlbAnQC47Jsg8wQyr8cgfV2-zhqFvkWUonjd_pAMc97QvY9eoEZpv3oezdclp6smVdfp6qjUaYbHt5wVMwlS5VbV5M05F2rUul4tIoBFKf0RktwC9IEB_-6MFrGZVxUYLmJPAItowEVs2Ma8hMuEv1ISAp4kuv9RNt22FF63u6EJFqhOYP8eX0KmsiMgR-jNK6fJ6UfHoTa8GV1BAFLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ae004bfed.mp4?token=nStFpgo9Ufiuo3hHpZ8esqGjSUI3wyhiOiiH9BpJTJEnp4yi8uUILBrPaVVlrcpQHO-OS8GU7j1dzuYkmJFWVU5xEd0vXozzpyS6ecdcMWzvZa5EJl69wNKD-wX8E9sbJWUlbAnQC47Jsg8wQyr8cgfV2-zhqFvkWUonjd_pAMc97QvY9eoEZpv3oezdclp6smVdfp6qjUaYbHt5wVMwlS5VbV5M05F2rUul4tIoBFKf0RktwC9IEB_-6MFrGZVxUYLmJPAItowEVs2Ma8hMuEv1ISAp4kuv9RNt22FF63u6EJFqhOYP8eX0KmsiMgR-jNK6fJ6UfHoTa8GV1BAFLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کلا کلا آمریکا، نعم نعم بالایران
🔹
نه به آمریکا و دفاع از ایران و جبهۀ مقاومت در شعارهای عراقی‌ها در وداع با رهبر شهید.
@Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/448065" target="_blank">📅 00:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448064">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amd2t0lrG3QxU5PRbtGlqAgufQC4BATZtLi1lUuy1FQyll2WcBsBfanRNSvWnnCk1GSCcZ0h5h7MLVT60t17lHigmFkf_phZQdWhM_lFUfSHJVdEXG5bedaU0tELUz3N6_gBUQ2jx4g1psyrRglNcUoH09UOGRFo6opUuQA6MoJ5U2F24NpX3fLeCsO2NoBQeDVQRPdLfFSVvA3ls6Kq-OYwv8fT5J33p__kl4ctD607qOVqu_V4M2ssieB2i9MSNMgl-gBwG25zfFEJ-sn61I7xeSYTADvxFbDkgKSr1U_eposj1wkemEkOaRQhX1bZvpuwZt3606oieHBKBSOa4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
| چهار‌شنبه ۱۷ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/448064" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448063">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e1fa65d60.mp4?token=F9oELCZKBG3PQCnO5BBXieEAPWRhVsEB--d0zRTCQ1d4WL3o_qI7UdVUqXkkWYSMax6-NPqj7yBvQOhSyqm467bGh-pXLjAiomdPq6Q-vEV3uZNKQ15KUhkdhVjHoMgVNXuJCpA32c2wQkr27gClcv_lkY3L7O5DUkCVU6_uTDqujOImJ-LhC0j0evrN4mR3Z_PSJXOm1OTwbyUVHapSDqONEHN93NfRVm9Phl0-jTd4FEH69wpAnt3Nm7vKU1pd5orwIbQaMdkVRmUIFrQlACGO_AcFKcJD0dsTN-zSyjpcUVyxKrbo1CrdO7PjHdYgaJWIVlmtE1rysFryoe16FFFRDLON7hMP8xsaIKXYDZK9ZiVRdWHhSPo33Lbz964C1Hpq1YKVFuX7epfzzejjqDf5PZlOY8mLSek9aSsqbrUejotGQTiOrkCCUoYvO_lLIK-AxuVBPdyUi8zKVK7AcKYFSKKT8RKqup-uS0vmnHppGIQdxSQ84Hj4PDxA7hlAkHyoRbdVsUb2-2julNuSC3k19RyoKTEkeYRKxDoo7HqP8GMpi_qg88nqzwfgoppg7Wnu4MZNYIbd1ZoimKc0dW79r_2tVidvdyra4fDkF7P9PhnGje-N7WrLP3wWX8DvgxKjUwmcrvpEI7o4Jc6yQ55XLi1ehpDfBcqIFUfNafc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e1fa65d60.mp4?token=F9oELCZKBG3PQCnO5BBXieEAPWRhVsEB--d0zRTCQ1d4WL3o_qI7UdVUqXkkWYSMax6-NPqj7yBvQOhSyqm467bGh-pXLjAiomdPq6Q-vEV3uZNKQ15KUhkdhVjHoMgVNXuJCpA32c2wQkr27gClcv_lkY3L7O5DUkCVU6_uTDqujOImJ-LhC0j0evrN4mR3Z_PSJXOm1OTwbyUVHapSDqONEHN93NfRVm9Phl0-jTd4FEH69wpAnt3Nm7vKU1pd5orwIbQaMdkVRmUIFrQlACGO_AcFKcJD0dsTN-zSyjpcUVyxKrbo1CrdO7PjHdYgaJWIVlmtE1rysFryoe16FFFRDLON7hMP8xsaIKXYDZK9ZiVRdWHhSPo33Lbz964C1Hpq1YKVFuX7epfzzejjqDf5PZlOY8mLSek9aSsqbrUejotGQTiOrkCCUoYvO_lLIK-AxuVBPdyUi8zKVK7AcKYFSKKT8RKqup-uS0vmnHppGIQdxSQ84Hj4PDxA7hlAkHyoRbdVsUb2-2julNuSC3k19RyoKTEkeYRKxDoo7HqP8GMpi_qg88nqzwfgoppg7Wnu4MZNYIbd1ZoimKc0dW79r_2tVidvdyra4fDkF7P9PhnGje-N7WrLP3wWX8DvgxKjUwmcrvpEI7o4Jc6yQ55XLi1ehpDfBcqIFUfNafc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کودکان پاکستانی با عکس رهبر شهید در نجف سرود می‌خوانند
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/448063" target="_blank">📅 23:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448062">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84b32253df.mp4?token=Kr7asDO5w8PMSubKZvSkOZ2n10gnrHURMvTqINax0VOe-85tdIG7lwZYN81jDS9XD3Z37ObZlx0BqcJUYR6oJWfmrDnbri3qQcECyos0g5DDn26IEKfiDxlhZlfL4G--wLiN0BqhmIrKuKAKQJ28PDsClusFBtk8egfK8R0KaGp-Fm9n9fyEiKAlzGRi1D5GlGRPTlwX8LPWRK--P6VROj_yy40Ws-4Zivbbc1y6Ugmcuu1ZvNPkoT1HsTHdWt9ZVL6LAure8KnmnWz-iIon0DN2XqYwLkA3F198QkiZMMoEF0G-9K8fPDVRUSWxPG2jNCFlNizTjgTijsfTy32_fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84b32253df.mp4?token=Kr7asDO5w8PMSubKZvSkOZ2n10gnrHURMvTqINax0VOe-85tdIG7lwZYN81jDS9XD3Z37ObZlx0BqcJUYR6oJWfmrDnbri3qQcECyos0g5DDn26IEKfiDxlhZlfL4G--wLiN0BqhmIrKuKAKQJ28PDsClusFBtk8egfK8R0KaGp-Fm9n9fyEiKAlzGRi1D5GlGRPTlwX8LPWRK--P6VROj_yy40Ws-4Zivbbc1y6Ugmcuu1ZvNPkoT1HsTHdWt9ZVL6LAure8KnmnWz-iIon0DN2XqYwLkA3F198QkiZMMoEF0G-9K8fPDVRUSWxPG2jNCFlNizTjgTijsfTy32_fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداران عراقی در کنار حرم امیرالمؤمنین(ع) در انتظار پیکر رهبر شهید انقلاب هستند  @Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/448062" target="_blank">📅 23:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448061">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18291d12b6.mp4?token=pXwbaxMpqLEy9fzzUgIHwl7tk2g7d0br0LvJSGvyooOCsunRTwhAyC7VUU4vwj99zKsUoEI1BoR3eCu_mV73ZrnwI2pBw7HQCgYSZK1viZwjQuW3BZt1fm4KhqwzF3W2F6hqQc4KVcqGL0eASjqJPuM2nuMysPgYO54eZKi92pDzUQluQP1Azuh_p3uCr8MqnJ9RcdQYKkqGMOn6_KuP1_w1zV5hIwMniEQPJmX-OMeB5kERH1fgyWsvvCgQXzMpy7_Twwnyq-1BuMvYkqN-Dt71j79HNp0Lbi1-UZjPycXqRVgDsByTorZFHKOkBak_oJUkLBRTY5Jv2IU4nc5mHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18291d12b6.mp4?token=pXwbaxMpqLEy9fzzUgIHwl7tk2g7d0br0LvJSGvyooOCsunRTwhAyC7VUU4vwj99zKsUoEI1BoR3eCu_mV73ZrnwI2pBw7HQCgYSZK1viZwjQuW3BZt1fm4KhqwzF3W2F6hqQc4KVcqGL0eASjqJPuM2nuMysPgYO54eZKi92pDzUQluQP1Azuh_p3uCr8MqnJ9RcdQYKkqGMOn6_KuP1_w1zV5hIwMniEQPJmX-OMeB5kERH1fgyWsvvCgQXzMpy7_Twwnyq-1BuMvYkqN-Dt71j79HNp0Lbi1-UZjPycXqRVgDsByTorZFHKOkBak_oJUkLBRTY5Jv2IU4nc5mHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از کجا اومدید؟!
@Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/448061" target="_blank">📅 23:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448060">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e263d4003e.mp4?token=ENqGYRN6mD0kuiXq8WVkwJloB0NO7RxE1suad5To9yWemKF_3C34lnkYv3-CY822rjXmDaucP8d1BXxF9EodzkNbj_c31zpcOLYvvQe3bdQ8-MWMSOw9Mt7OWHmgaBaWlywPH1EPnCS56TZ79jmtPCFJJpQ3E4xMgMbfgo8nKcspvPPd-jpiJPjzTTgOKbGwkGTHvbBI96rvbNx0vtJPi7xHZ43lEXGtpzNnFULHCAbJKiT8UDystrikR-5J9ZKaZnFey23BJw1xU_6LateR9Bkxm9nWPgdJEXeQxBgLCJnWNYzMH1H4KyktqZL6fzPvJ6col9n6g5uembnpZIMTYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e263d4003e.mp4?token=ENqGYRN6mD0kuiXq8WVkwJloB0NO7RxE1suad5To9yWemKF_3C34lnkYv3-CY822rjXmDaucP8d1BXxF9EodzkNbj_c31zpcOLYvvQe3bdQ8-MWMSOw9Mt7OWHmgaBaWlywPH1EPnCS56TZ79jmtPCFJJpQ3E4xMgMbfgo8nKcspvPPd-jpiJPjzTTgOKbGwkGTHvbBI96rvbNx0vtJPi7xHZ43lEXGtpzNnFULHCAbJKiT8UDystrikR-5J9ZKaZnFey23BJw1xU_6LateR9Bkxm9nWPgdJEXeQxBgLCJnWNYzMH1H4KyktqZL6fzPvJ6col9n6g5uembnpZIMTYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: هم انتقام مصداقی و هم انتقام از اشخاص باید صورت بگیرد
🔹
انتقام مصداقی به معنای خروج آمریکا از منطقه حتما باید صورت بپذیرد تا مسیر پیشرفت ما باز باشد.
🔹
اما به غیر از آن، ۲ قاتل رهبر شهید نباید از انتقام در بروند. @Farsna</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/448060" target="_blank">📅 23:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448059">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eseBM-tjCc1iGFSNML7wf2hL1UlwWP6ax-hOztUJ9qOrVZls12CSTYouAVs9vtthlE3r1_-cct8UCs_Pu9jBjTm8nV5lRWRcrvliw6sSj8Pw_U_x7won7AgVUVE7er52ZK3AztipPIIpiTZLtl7uWrAwBJGqbgVCK9g2UVk9oSas4lgfM89U_shvckdpMbH9Pb15RhcLoizDc4iyiDUYiaPzZ-1BszgjiRCfKW491ILtJGSMJFTcOGeUfRcKPDj5VoDqsEGuHdEmUVrMVDQqpZMxn-2AHSOqmUxR88asVChH6Hdy3L5rlrpkzSsDh50J88QdpJ191lXO76r8n_fp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور مسیحیان عراق برای استقبال از پیکر پاک رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/448059" target="_blank">📅 23:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448058">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b795f6a88c.mp4?token=S5IOnDjgbwg_Mh2I5UzB1arLmtso1fYe8RHC1TqQAtZ26Et-edQBdTcphlI3sfV58VyBwFMNLGyPuR3Fa2yEv9BXmmGeBrJoUKdxRDG110w3yF9X9-oafJEflxK8IYo2th2BAO6QOTlNu3zXer9ylKD5-idbGkjeCgGGNrahgiDY_eSbRq2_pDV_uIFW91pnmbBMl2a22RUvkIRFnbeG1BVmoRKHrdjKvg3iB6H9iEN0Bld2Jqwf7R3N1KsJpCqH23Ve9BNgj0KVOODJD5UfLsffilTEohLbR6eJJrvU-b01katU7VPTJFxKFVeC7sfAzDkiHQtYbw9aroWJBr6Muw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b795f6a88c.mp4?token=S5IOnDjgbwg_Mh2I5UzB1arLmtso1fYe8RHC1TqQAtZ26Et-edQBdTcphlI3sfV58VyBwFMNLGyPuR3Fa2yEv9BXmmGeBrJoUKdxRDG110w3yF9X9-oafJEflxK8IYo2th2BAO6QOTlNu3zXer9ylKD5-idbGkjeCgGGNrahgiDY_eSbRq2_pDV_uIFW91pnmbBMl2a22RUvkIRFnbeG1BVmoRKHrdjKvg3iB6H9iEN0Bld2Jqwf7R3N1KsJpCqH23Ve9BNgj0KVOODJD5UfLsffilTEohLbR6eJJrvU-b01katU7VPTJFxKFVeC7sfAzDkiHQtYbw9aroWJBr6Muw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاوینی‌های کلات به عشق رهبر به خیابان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/448058" target="_blank">📅 23:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448057">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5767505733.mp4?token=d1gK7_ZbOzEDhsmuWTcM7-k19bZZe4jp8J69_70PKGbqDYjNusosJkU-wddU2QA8jIvh88l78IqwKH0X7GpasyvpwidSnsjDz71wuvmRP-om24xuY606TvhH83j52x0fhftDpkiBqRPn4JUVn9d_me-eIr0B9juZYlQkC5qc4vFAVjHFw2NrQKdr85gMhlvdw1-7Kb2r7gc6OC00hS-1e_olQAraZgNLBM031PbBS2J0RHmbknivf-Ag9HNlYX7GKNSpms9PdRRO2KwkCZTtFRrPxrP8FKoT9p9LOd7i_rtXtt1ppPRBs4ZTeO5mEOHh9_wgquuILYB0IxLem9Uw8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5767505733.mp4?token=d1gK7_ZbOzEDhsmuWTcM7-k19bZZe4jp8J69_70PKGbqDYjNusosJkU-wddU2QA8jIvh88l78IqwKH0X7GpasyvpwidSnsjDz71wuvmRP-om24xuY606TvhH83j52x0fhftDpkiBqRPn4JUVn9d_me-eIr0B9juZYlQkC5qc4vFAVjHFw2NrQKdr85gMhlvdw1-7Kb2r7gc6OC00hS-1e_olQAraZgNLBM031PbBS2J0RHmbknivf-Ag9HNlYX7GKNSpms9PdRRO2KwkCZTtFRrPxrP8FKoT9p9LOd7i_rtXtt1ppPRBs4ZTeO5mEOHh9_wgquuILYB0IxLem9Uw8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقی‌ها با نوای عزا از رهبر شهید انقلاب استقبال کردند  @Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/448057" target="_blank">📅 23:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448055">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940ff2ee8b.mp4?token=NWRVFgrU4cUmEu-B-NtcEFrJ-Vk4zV3c9V21y3rrTR1YXfyfd7dSGJVuyX5yacEO-2OEaKR0sPRJaeDUu-GU1USxFE4nr8bDR8coEQ7nu2S9lh43CRx6XPBGLIS8lyAz__uzJ2CB8KVcVeNAdd9XgHTjeI-HDdSl3Ff9c_iet7bPwqGMSlEZtgl1O_myrg6C2L-r3Yu_Xo1ubz6c_hU4yawX0CyDKBDnJvxPNQLTNPIOxaR2m8bpd0H7-PLqEmceu3jvTdlx-2DfsFBwdpUs0hfSX3z_FF9lr6kiR2G6dee-GMtd2sJRavPAI5ajBX8d0xk0LO15n5dNxbkdeNjltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940ff2ee8b.mp4?token=NWRVFgrU4cUmEu-B-NtcEFrJ-Vk4zV3c9V21y3rrTR1YXfyfd7dSGJVuyX5yacEO-2OEaKR0sPRJaeDUu-GU1USxFE4nr8bDR8coEQ7nu2S9lh43CRx6XPBGLIS8lyAz__uzJ2CB8KVcVeNAdd9XgHTjeI-HDdSl3Ff9c_iet7bPwqGMSlEZtgl1O_myrg6C2L-r3Yu_Xo1ubz6c_hU4yawX0CyDKBDnJvxPNQLTNPIOxaR2m8bpd0H7-PLqEmceu3jvTdlx-2DfsFBwdpUs0hfSX3z_FF9lr6kiR2G6dee-GMtd2sJRavPAI5ajBX8d0xk0LO15n5dNxbkdeNjltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: دوستانی که مخالف مذاکره هستند صبر کنند؛ خود آمریکایی‌ها این مذاکرات را ازبین می‌برند  @Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/448055" target="_blank">📅 23:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448049">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H80R8cwgLcnvWvVt10FpgQaXtT5XVaKegkzHfTPP5rFKRfiLEMtsBgMlu0hF9XrsO-qeeT-A6hmdCH01V-eMA9lz1gli1UKAbW599v8UxrqOL8ax7bB8cljiOdiH6xCdf3xjjbWds0KZrD2rda521w0EBGK8VIQPU0n_2IPfepnEeQIUMWP4pHoJTcTnBjoyDSs7Mq-qvcPPVvDoz_KMU9G_LNTcrPVEw0ibEtXxJm9EeUkL2FYO_kwogxB1zSdMmjRJrB6__iDCwXw9WDCCJ2YCwuY17QP3-y9OqG2wHFfvXuzrYDZCWp4ocNCrup92obOrkWcV0v8lMESMvyt_Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EkgSmngaqhB_r0tRKxtNLiBbpwYLc1d67lzmyUjibrF1hv2_z-ag-rWuUvmE5a6D23U5PP40bYlLGK1PLBnySnNDrCPbHNmeeI3cOR1u8FdUYWjus1kv15TbkbpsrQkYrWSlbnMQm1304UBckHhnkPRC2LIid7yUUBAPp_tcuqQ4IEzLyhBhODDAoT89Rhx4IyMb0fGfEhKQqiy51qi3YcFaI80eWCR4n_1LAwPPbU-bnL4tfzBxeY0ffulXaFSWZD2oJOa-tcQDMzXNX9psweV8pUilLhPgZE3POQo40G-6fOZcDlHxGOloH9PRHAnM1sHGCkF-H81UHhVvv5Cjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ioELsRFigNktqtaSDGUbl5wL5GbNxd3o3zdXxn249ebvNHzoI8c3IAaUUrzL2HoS23fwsmmI7rNMircGPvMtFLrcKnpYBdD72XYJN1fBsf4LRF3F7ae5kfe1O6NyZTI-MBxBtZyD7_2TeUuRcezcxsO5eHb-nGtpG_5cLg7CzX9Qn1PjySLf4U9WDmKcPBHWXvgfxUrNwy-aGUJhC4JEaA3Yjru9WUh5n-UgUaCeiBsvKct6D8RMSVgxL767jFHLQ2QDmKugpabJfEo_XMBugicWSJ3B1tDZG3BS_ioXo954cwPtHjQOyKVG8TDxr2PdApyYUnN6mj5uZL0ERtOg7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPcMyrA0uHr-I55oRm6A3lxNEq8M5KQ2Cl_1u1nUyhVr944_7jqnVGOE_0C9CpPp99udRUb_ykbvc_0jbkZMAMLlRUvVwkS4VDgCAW8lRQpNUF6roqhlTz3_-m-pkRUizhVAVVusjW-hsQLiJe_ef3l8lbnPUmX5vnSKlVtW7C27cIkMOXc1Gl3OeBADI87w1DeQvYeLz_eSF0ROat3ADmV-TMvOXCr7Yp4dD3qwVsHN0BM48oepnJpUwbMcwQ6dRNuYrya-QlKa7v2z7c-e9w_aiCRysrKt3oCLP_2lekZRly53L9Ysrg36Lh9jCQfYNzD7pFC659Oc4KBbMyvnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6Jrff2Ygu9x8j2sd79Hz9u2432LowGTl3OlwrlkaRHpEnzKm9nyW2pq7hdQ2d4WmCSLOi2k7BS1uhCTKKfYJGNjL-Q2dZBAkn9eeKp0l3_y_6s046QLaZNrTTW_ZnQCQRM4uqh24RtNYINF2JM2bFxKjGDk1vhvRPdjHmbzKJZxsqy_DRqeK5lGyCAZ69auN5QnbyOGlRxd6t57EpvudkT0OWrnppgQQNK_ii1Dhod3w8EReg6ytKhQfMqab6kc23oo6NztgYhcywvXGNc3FH1yd4mPLvvu8Z3eNfzd92AjwaeM-5p21m2pifqeo1u4esMwowOLmfLHxH4jYD3Jjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال و‌هوای کربلا پیش از مراسم تشییع پیکر رهبر شهید
عکس:
محمد آهنگر
@Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/448049" target="_blank">📅 23:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448048">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d765e01d85.mp4?token=n82YM_tpYVnF9JqxzPv5-nT8Mf_OUlRIGarcAz_gMfsTNQWjcS5Q0ezutyaoWAbU0FzabELLsButwjWhLjdh7-nPzBJKcHY1FoHL5z3wwekt14Jp0-g8llrFw0Lg-IaUiHekvj9TF7fgWMzDTBFCfoqcme56SpfzKequLQv167fDKyvB7Gowfxz5YxnR6lsAJrXEUAmgP4l1RwiFOqexAY2v4Mzy2tK59y2YhZVLtww0PKWxPumo1EczChp7z_6vqzSNPuAVH2wdG8E1e1JtnS1kdMOeKz1PhKG4O1pCvg5m0RlhKOFWrw_9mRDt2eVZEQDs9Pv9vR3a0eJ4OZh7CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d765e01d85.mp4?token=n82YM_tpYVnF9JqxzPv5-nT8Mf_OUlRIGarcAz_gMfsTNQWjcS5Q0ezutyaoWAbU0FzabELLsButwjWhLjdh7-nPzBJKcHY1FoHL5z3wwekt14Jp0-g8llrFw0Lg-IaUiHekvj9TF7fgWMzDTBFCfoqcme56SpfzKequLQv167fDKyvB7Gowfxz5YxnR6lsAJrXEUAmgP4l1RwiFOqexAY2v4Mzy2tK59y2YhZVLtww0PKWxPumo1EczChp7z_6vqzSNPuAVH2wdG8E1e1JtnS1kdMOeKz1PhKG4O1pCvg5m0RlhKOFWrw_9mRDt2eVZEQDs9Pv9vR3a0eJ4OZh7CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲۹ شب مقاومت گرگانی‌ها در سنگر خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/448048" target="_blank">📅 23:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448047">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219dc4d8ed.mp4?token=iLQpR5Q8iStwVB3PavoSehUPmBs3NRh6CVK_JjjNi4gyVfwvfwJkIy4pO2OO2cn9f7TG0Kjard-GJ0RW--J5l66qDO2gBSVU7uzmaZd49rLEnjfFs4mgrEw13Kv-p6VDPJgaM3sYVorpWVJ_f2ceR9ZFLKb3Q-rQ75VpidTQDplfO2u8J2Pk1218G3CVIOFpDwjivRiJyeaMD1sV8e0DthuvICK1-8x8922xnS0pjxzIruAiM00TjNPYGXH1cCHHyIyLYaO4USzBSGQYqnKctKlsV8LxhhMYJc5ZB8am4iVr7iUI7QvVjmQqD9AEJbx1tAZrgr3CfGkR0adSk401HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219dc4d8ed.mp4?token=iLQpR5Q8iStwVB3PavoSehUPmBs3NRh6CVK_JjjNi4gyVfwvfwJkIy4pO2OO2cn9f7TG0Kjard-GJ0RW--J5l66qDO2gBSVU7uzmaZd49rLEnjfFs4mgrEw13Kv-p6VDPJgaM3sYVorpWVJ_f2ceR9ZFLKb3Q-rQ75VpidTQDplfO2u8J2Pk1218G3CVIOFpDwjivRiJyeaMD1sV8e0DthuvICK1-8x8922xnS0pjxzIruAiM00TjNPYGXH1cCHHyIyLYaO4USzBSGQYqnKctKlsV8LxhhMYJc5ZB8am4iVr7iUI7QvVjmQqD9AEJbx1tAZrgr3CfGkR0adSk401HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲۹ شب حضور عاشقانه مردم تربت حیدریه  در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/448047" target="_blank">📅 23:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448046">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a63758a543.mp4?token=EHkmLmAD46fAUxQwAaUHhn86g3ARvErCbfc-H97v_XI59B3KLoQ0zgvGEcx9vqv_-jMzzUyZ198lmvcIwumX99j0OiZdrgGsXLHi7lXXHRQniIx0adYj3R4DIOeYxpgFrtgYg2QxKBn9w6iSPUYvyOJBr3X1B30RzXHkg_Hc0xorQ6HpB_1aeu3t19bQZwx2iOw4DQ5zmNSMe_NWpW3a2Ch_gsCgHrZZWjPUHOA9aaydYRZdJzrVjSV7fWWbW7uyeeTIYVwBwZ5_CgpgKUQ-4aigfzDAXFV1NjRskBif5PpI4UOCt7MCwf0y87U8jo04FTBQ7TPZ3T3jqtbsMTc1wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a63758a543.mp4?token=EHkmLmAD46fAUxQwAaUHhn86g3ARvErCbfc-H97v_XI59B3KLoQ0zgvGEcx9vqv_-jMzzUyZ198lmvcIwumX99j0OiZdrgGsXLHi7lXXHRQniIx0adYj3R4DIOeYxpgFrtgYg2QxKBn9w6iSPUYvyOJBr3X1B30RzXHkg_Hc0xorQ6HpB_1aeu3t19bQZwx2iOw4DQ5zmNSMe_NWpW3a2Ch_gsCgHrZZWjPUHOA9aaydYRZdJzrVjSV7fWWbW7uyeeTIYVwBwZ5_CgpgKUQ-4aigfzDAXFV1NjRskBif5PpI4UOCt7MCwf0y87U8jo04FTBQ7TPZ3T3jqtbsMTc1wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: کاملا مشخص است که آمریکا مذاکرات را با شکست مواجه خواهد کرد
🔹
پیش‌بینی می‌کنم مانند برجام، آمریکا در عمل امضای خودش را پاره خواهد کرد.
🔹
در جنوب تنگه هرمز آمریکا می‌خواهد حضور خود را تثبیت کند تا در نهایت ناوهای خود را عبور دهد. @Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/448046" target="_blank">📅 23:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448045">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e8e5100e.mp4?token=ceeADrTkJJaIkYG0AhjLe-BeCoZoEGZ85kBBWU6biBgkH3GXSxDo4O38MnvmG7xlMeDKBZzQ4BWWm4-UzQf8cXRZdVACNyFCpx5X2_5QcD9G0bAXQmXQ64xqD2NyGEFlDHBjKHRgrxu6VSHriGtpFQtoErVc52Ihq4Pv0H0ReIIVAzo54L-Azo91YwT6hWKG966UnKvMIhK5LbrI64646TiQ65_NKAiKXCYld8DbneyAdy8RvPs_23Pm6wrht_A4yMc6rR1wKkl4dlj2Az0_dcjnXJ_6RjxTc_TSkq7WXxNaIV7OoIx6FK42xhBdp6gYj4N26cclg4X9FKOFlkg90Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e8e5100e.mp4?token=ceeADrTkJJaIkYG0AhjLe-BeCoZoEGZ85kBBWU6biBgkH3GXSxDo4O38MnvmG7xlMeDKBZzQ4BWWm4-UzQf8cXRZdVACNyFCpx5X2_5QcD9G0bAXQmXQ64xqD2NyGEFlDHBjKHRgrxu6VSHriGtpFQtoErVc52Ihq4Pv0H0ReIIVAzo54L-Azo91YwT6hWKG966UnKvMIhK5LbrI64646TiQ65_NKAiKXCYld8DbneyAdy8RvPs_23Pm6wrht_A4yMc6rR1wKkl4dlj2Az0_dcjnXJ_6RjxTc_TSkq7WXxNaIV7OoIx6FK42xhBdp6gYj4N26cclg4X9FKOFlkg90Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در بازار منتهی به حرم حضرت عباس(ع)، مغازه‌داران تصاویر رهبر شهید را نصب کرده‌اند
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/448045" target="_blank">📅 23:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448044">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ece5de56b8.mp4?token=NDsA1_C1P3hEIIgHGPGx0qDqz9a_CXcUniw0MriyKVWjPSMp1Ytl6089qQVKzrta7SbGiB9wo55j9nW5UnYLP5YO3ybCv_w5ZntcRLWbkAc5oXzk2k--txfNYRC1Zk4-TJzlhmDHFuhjn8coP9MyzNoOA8-AAS6K_ANYG_vw_Fmw_FQGkDdlILjzu-0HYmqR_qAzrtxpAlgNmlrWfjP41zPzKJ6iYYwqsDxYn4KFWlCjCeM5hhDff5LjxDW77naD-nW6tgJNK440kZCZEIkIGYuivLqCDsijGrMUbenknvKlR0ZVWzOyq80rATeYB3QRbX5y3yjmIALow13Nxce1Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ece5de56b8.mp4?token=NDsA1_C1P3hEIIgHGPGx0qDqz9a_CXcUniw0MriyKVWjPSMp1Ytl6089qQVKzrta7SbGiB9wo55j9nW5UnYLP5YO3ybCv_w5ZntcRLWbkAc5oXzk2k--txfNYRC1Zk4-TJzlhmDHFuhjn8coP9MyzNoOA8-AAS6K_ANYG_vw_Fmw_FQGkDdlILjzu-0HYmqR_qAzrtxpAlgNmlrWfjP41zPzKJ6iYYwqsDxYn4KFWlCjCeM5hhDff5LjxDW77naD-nW6tgJNK440kZCZEIkIGYuivLqCDsijGrMUbenknvKlR0ZVWzOyq80rATeYB3QRbX5y3yjmIALow13Nxce1Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: کاملا مشخص است که آمریکا مذاکرات را با شکست مواجه خواهد کرد
🔹
پیش‌بینی می‌کنم مانند برجام، آمریکا در عمل امضای خودش را پاره خواهد کرد.
🔹
در جنوب تنگه هرمز آمریکا می‌خواهد حضور خود را تثبیت کند تا در نهایت ناوهای خود را عبور دهد.
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/448044" target="_blank">📅 23:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448043">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40fa9b3e9.mp4?token=MIoto-UjuQ_5o53WCIqDOm98aSQu2oSEfks8BWovk132Qt2edn-42twJ0WreR-beX4tlJ6u-G_cstCuYCEHXiVO2NVciS_sRRZwQfWMbJ4HcOTFmriAFwrYQiJ_89Z4v3p3_zHOpEaM0j4wQI8JVyG3g6F5A8OwzUzxPESgPEAyt8V2-kVX6raX1oFpuN9dOboZLFPdUOLOjyAF0jxXE6nBiP1RvAUa68jg4NvKWxga1YSqsb-eVZaJo5TNcl66r-Iz3tGnvGWNWk8N6b9gdzSJoDsfOCxGhapNMTBuZFNi4NfWS1QdSi3wB-gamVf-ybrwXuwUhx0WiMIgBaCndoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40fa9b3e9.mp4?token=MIoto-UjuQ_5o53WCIqDOm98aSQu2oSEfks8BWovk132Qt2edn-42twJ0WreR-beX4tlJ6u-G_cstCuYCEHXiVO2NVciS_sRRZwQfWMbJ4HcOTFmriAFwrYQiJ_89Z4v3p3_zHOpEaM0j4wQI8JVyG3g6F5A8OwzUzxPESgPEAyt8V2-kVX6raX1oFpuN9dOboZLFPdUOLOjyAF0jxXE6nBiP1RvAUa68jg4NvKWxga1YSqsb-eVZaJo5TNcl66r-Iz3tGnvGWNWk8N6b9gdzSJoDsfOCxGhapNMTBuZFNi4NfWS1QdSi3wB-gamVf-ybrwXuwUhx0WiMIgBaCndoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم در حماسه ۱۲۹ میدان انقلاب: حرف ما یک کلام، انتقام انتقام
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/448043" target="_blank">📅 23:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448042">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693fc7bef2.mp4?token=UFdZ7Fb-0U3wwacJbqgcoa5Wd337h9Wh5VNErrI0ypls2t_JysLA5iipe1xj7G18vTxzAt02Z-RqaLGEVur7WiN_gsC2euX0a4E7uCF79n9Bc5kXNN_x-6SLItKIQHYwOB2ciNBWAeyRa_sn8OoL-8uJ0m_evRzXdGZKoUj6H3hAe8Lq59Pwl6sgXS6uTgJq2E_s-XHPYL_xH3MR7j3imDMpEzy0Psp7vRfClMNdTg29mwM2zkd1lLOfUIRxyNcrZQq--OHebBw3TzFcOhjRH_zlzRH4TQkEP1cmSJAAVDLpvXi_LjUzeh-6nn6GqEjhPo4ZqBbYDyymkskm75yjG0xFaaa-jB8kS_AZYcaIRmQGijRS5p2rGfPD6REru2TC9GZVzp71KZ7CW-5jsnyRJ-70911i7bI1vU9HF9N7ZJS0nFOdSuBFePF7oQjyRXDd4maZaeE0K0K9JlhNHSqT2hhX68Kw1aqtMwtDJ9Gkl1Wo0mgU9_LZhPzsN7r4YAKd1B-3b-fp_ZJi2BwBLIb_u_eGp_c23-ob8PCHPU8TwvyADtj0r6HXdkmG5g_uR9Xmb6CG1uAWUpFP5Kx9XWEqAgiRAF6S2eEap3x4fweLOqe8dIIjDQQgpHvuK2bFixUBxRy7CgGNirdMalSZ5oHGUQx7fjTp8XqEzBPLnX_86Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693fc7bef2.mp4?token=UFdZ7Fb-0U3wwacJbqgcoa5Wd337h9Wh5VNErrI0ypls2t_JysLA5iipe1xj7G18vTxzAt02Z-RqaLGEVur7WiN_gsC2euX0a4E7uCF79n9Bc5kXNN_x-6SLItKIQHYwOB2ciNBWAeyRa_sn8OoL-8uJ0m_evRzXdGZKoUj6H3hAe8Lq59Pwl6sgXS6uTgJq2E_s-XHPYL_xH3MR7j3imDMpEzy0Psp7vRfClMNdTg29mwM2zkd1lLOfUIRxyNcrZQq--OHebBw3TzFcOhjRH_zlzRH4TQkEP1cmSJAAVDLpvXi_LjUzeh-6nn6GqEjhPo4ZqBbYDyymkskm75yjG0xFaaa-jB8kS_AZYcaIRmQGijRS5p2rGfPD6REru2TC9GZVzp71KZ7CW-5jsnyRJ-70911i7bI1vU9HF9N7ZJS0nFOdSuBFePF7oQjyRXDd4maZaeE0K0K9JlhNHSqT2hhX68Kw1aqtMwtDJ9Gkl1Wo0mgU9_LZhPzsN7r4YAKd1B-3b-fp_ZJi2BwBLIb_u_eGp_c23-ob8PCHPU8TwvyADtj0r6HXdkmG5g_uR9Xmb6CG1uAWUpFP5Kx9XWEqAgiRAF6S2eEap3x4fweLOqe8dIIjDQQgpHvuK2bFixUBxRy7CgGNirdMalSZ5oHGUQx7fjTp8XqEzBPLnX_86Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از اولین لحظات ورود پیکر مطهر رهبر شهید انقلاب به فرودگاه نجف
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/448042" target="_blank">📅 23:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448041">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f995275a99.mp4?token=qJa3R8ja8ZiC4suhpKFXkXMc2C5coVexUhotCdPmAZ_4zzL0aNm-Uxt_gKhqC_Rb5qvSTSSCLA8qlTk5nsVC-BwkdZTsWg_yUja61TCwTpAzGl_POFGXLaTKWSJyQbRJuBDB3IHO3IDKmA7ChPY9gmTabO5ILfzCJVSWuRQlthOK9862XpcSEtdsrBoRzMJl-JzQ7G_8KjdIdxNnhCLqGDvMMfU0dHEyStHdWhFaE1cNtyQxg7MhO9C-0XthXS46cxOa2fWX5NAx6gnUbC18In38heUPI81yUTYMT0P_-XDgQZXbv-VnOE5GLtcRrQQ4ezvAEkrbFkJ42Z1oF70XIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f995275a99.mp4?token=qJa3R8ja8ZiC4suhpKFXkXMc2C5coVexUhotCdPmAZ_4zzL0aNm-Uxt_gKhqC_Rb5qvSTSSCLA8qlTk5nsVC-BwkdZTsWg_yUja61TCwTpAzGl_POFGXLaTKWSJyQbRJuBDB3IHO3IDKmA7ChPY9gmTabO5ILfzCJVSWuRQlthOK9862XpcSEtdsrBoRzMJl-JzQ7G_8KjdIdxNnhCLqGDvMMfU0dHEyStHdWhFaE1cNtyQxg7MhO9C-0XthXS46cxOa2fWX5NAx6gnUbC18In38heUPI81yUTYMT0P_-XDgQZXbv-VnOE5GLtcRrQQ4ezvAEkrbFkJ42Z1oF70XIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقی‌ها پس از انتقال پیکر رهبر شهید، جایگاه وداع را بوسیدند
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/448041" target="_blank">📅 23:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448039">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8923d543.mp4?token=VWGpm4QBbSqJQN8QSVvDhIKTBh4ZX9zkRAIYY2AfZkcS_uLWDCNrTApb4O-sJ93DmWQPWvU44QdQxCpdT807V98L1emQgH-UItHCipUBzLFHhlNXdtEJuGNRqe5y9TzPC9GoFHk4o7ZeVdSBRJ3V31jUWPx9nx9hz9PJ9Pk5Da-S_yy2eH5nsIUOOgy-_ig9fgbqZ6qQnKuaI6Ppbm_mI7Xp0vG-dscu50NzH-n3m6in9DrA9i3cSCUwq7fw_ULteTrEmWeixNsvjjzJSN32fBZxF1Z6Grkk0Fw5ZvPTICBm52DP0Nkijw-11BDbdgNlMmgIimxFkZ6dikO4MuFxQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8923d543.mp4?token=VWGpm4QBbSqJQN8QSVvDhIKTBh4ZX9zkRAIYY2AfZkcS_uLWDCNrTApb4O-sJ93DmWQPWvU44QdQxCpdT807V98L1emQgH-UItHCipUBzLFHhlNXdtEJuGNRqe5y9TzPC9GoFHk4o7ZeVdSBRJ3V31jUWPx9nx9hz9PJ9Pk5Da-S_yy2eH5nsIUOOgy-_ig9fgbqZ6qQnKuaI6Ppbm_mI7Xp0vG-dscu50NzH-n3m6in9DrA9i3cSCUwq7fw_ULteTrEmWeixNsvjjzJSN32fBZxF1Z6Grkk0Fw5ZvPTICBm52DP0Nkijw-11BDbdgNlMmgIimxFkZ6dikO4MuFxQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر به‌سوی حرم امیرالمومنین رهسپار شد
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448039" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448038">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">واکنش ایران به ادعای قطر درباره حادثۀ یک شناور در تنگۀ هرمز
🔹
سخنگوی وزارت خارجه اتهام‌زنی قطر درباره حملۀ ادعایی به یک شناور مرتبط با این کشور در تنگۀ هرمز را سؤال‌برانگیز، مغایر با اصل حسن همجواری و غیرقابل‌قبول دانست.
🔹
بقائی تأکید کرد ایران به تعهدات خود برای تأمین امنیت و ارائۀ خدمات دریایی در تنگۀ هرمز پایبند است و از کشورهای منطقه و شرکت‌های کشتیرانی خواست از هرگونه اقدام مغایر با تفاهم‌نامۀ خاتمۀ جنگ خودداری کنند.
🔹
او همچنین هشدار داد تردد شناورها در مسیرهای غیرهماهنگ یا خاموش‌کردن سامانه‌های ردیابی امنیت دریانوردی و ایمنی تردد در تنگۀ هرمز را به خطر می‌اندازد.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/448038" target="_blank">📅 23:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448037">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6635381d0b.mp4?token=Ak7Q4fgc0iRSf9IQ9OMUe8eq1gbxOe-YH0QBd-uNr_rt7DGFn_eiO4hJjdFE9ycRvLehoiPhnAVfDbSPJjVCgk8OQSHR6zPhW8JAjLhA03YSRY1Ubva231l592Nbv85WFfHi8BUiZ5Po8P9dY6ZQr5aLuGhizVhFPK00b_F9l25pBAcG4qgpU9tzO9H4B7r6RoiiLp9_hXepmyMocVvsIIW4hczRNQEoqi1DG8Svt5t2pMa8HD-M9_T6TF4L3ZkhbCxAC6E1g2iEHcl9s-CGm7hazdIlxZi50dJ7FXP2yftvUvsCAKna86JFJu4vCn02T25x7w0AF7mBHbUL6TNAEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6635381d0b.mp4?token=Ak7Q4fgc0iRSf9IQ9OMUe8eq1gbxOe-YH0QBd-uNr_rt7DGFn_eiO4hJjdFE9ycRvLehoiPhnAVfDbSPJjVCgk8OQSHR6zPhW8JAjLhA03YSRY1Ubva231l592Nbv85WFfHi8BUiZ5Po8P9dY6ZQr5aLuGhizVhFPK00b_F9l25pBAcG4qgpU9tzO9H4B7r6RoiiLp9_hXepmyMocVvsIIW4hczRNQEoqi1DG8Svt5t2pMa8HD-M9_T6TF4L3ZkhbCxAC6E1g2iEHcl9s-CGm7hazdIlxZi50dJ7FXP2yftvUvsCAKna86JFJu4vCn02T25x7w0AF7mBHbUL6TNAEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بامان‌الله یا ولی‌الله
🔹
وداع مردم عراق با رهبر شهید مسلمین جهان.
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/448037" target="_blank">📅 23:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448036">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
قیمت نفت پس از لغو تحریم‌های نفتی ایران به بالای ۷۵ دلار صعود کرد.   @Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/448036" target="_blank">📅 23:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448035">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13cdbb7d4b.mp4?token=VmG4cWydVxJtKmE-VKV36Op868zlqoPfKLcrjvbqKUeVtF8EIQs2UMUs6IhELN7blemCSqAMV7a47WEYVytlKJWAFAFxqYZoggRc2iK_tArtbKupgKRMHKFD_Bw-7mFUmJGIdCcp1ZZLX_N9lSCCtDrgi4cCs6B95R-tAMq5oBFMLzcJ8xkKZrt4P5ua5iJx1oayP2v5mue_iQGD4P9Se7_SzbrqPqr49qv6XEsjmT8fdX4Jkq9rCvB4oiD0gXmDNbg5K8TQ2GYBlczcBUX-_nUgNqSoq1CCJNYoa470YKBSABB4gJv8Rcl-w4qDy1fEU7GM49oi89haRhlmZYcDvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13cdbb7d4b.mp4?token=VmG4cWydVxJtKmE-VKV36Op868zlqoPfKLcrjvbqKUeVtF8EIQs2UMUs6IhELN7blemCSqAMV7a47WEYVytlKJWAFAFxqYZoggRc2iK_tArtbKupgKRMHKFD_Bw-7mFUmJGIdCcp1ZZLX_N9lSCCtDrgi4cCs6B95R-tAMq5oBFMLzcJ8xkKZrt4P5ua5iJx1oayP2v5mue_iQGD4P9Se7_SzbrqPqr49qv6XEsjmT8fdX4Jkq9rCvB4oiD0gXmDNbg5K8TQ2GYBlczcBUX-_nUgNqSoq1CCJNYoa470YKBSABB4gJv8Rcl-w4qDy1fEU7GM49oi89haRhlmZYcDvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقی‌ها با نوای عزا از رهبر شهید انقلاب استقبال کردند
@Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/448035" target="_blank">📅 23:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448034">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d430649a0.mp4?token=ZI5QBHqo0la0-vEvNnYIHEZMS4P7C5zLiMZCHWCQxC4g0FYtyzMVE7Z7bM3pyl-n-YOKHVGQt4pdfoTk46Il-of-rySLi3lN6n9zawHnzCn0eQiuCqnYDsbfLL3YPgrMLyk3OLHTCocVZYA-EBCl5Yi3q5O1GJS8Rb2oNA3vmUbqgWk0LzfywttxRcqHUpfDgI9eKxjN040F7W1_bcWrQiYJqOIQ0jcJASDVQrd_hSJblmMkJcTEH2UzQODsWLoNNn5FwAlUIVUgeyfZDrAeA-btwQasI46hRYNY5JHAs_myTbSJQP3DhAJrUXfy2QOGeZaFVmVa1TZ07Ae0lUZo-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d430649a0.mp4?token=ZI5QBHqo0la0-vEvNnYIHEZMS4P7C5zLiMZCHWCQxC4g0FYtyzMVE7Z7bM3pyl-n-YOKHVGQt4pdfoTk46Il-of-rySLi3lN6n9zawHnzCn0eQiuCqnYDsbfLL3YPgrMLyk3OLHTCocVZYA-EBCl5Yi3q5O1GJS8Rb2oNA3vmUbqgWk0LzfywttxRcqHUpfDgI9eKxjN040F7W1_bcWrQiYJqOIQ0jcJASDVQrd_hSJblmMkJcTEH2UzQODsWLoNNn5FwAlUIVUgeyfZDrAeA-btwQasI46hRYNY5JHAs_myTbSJQP3DhAJrUXfy2QOGeZaFVmVa1TZ07Ae0lUZo-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مقامات عراقی برای ادای احترام به پیکر امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/448034" target="_blank">📅 23:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448033">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/farsna/448033" target="_blank">📅 23:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448032">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWDgB3BzWsJVrEGDLOjQoGdqikW6bZyrZPuob63cZFP3Ha8SaZbU5tULAbIZo2y4eIue4ejs5u54GlkIWjAqrq0F6Ep954tQtO6nyA_vGU3fshGB_uvSmobuKraqkDbheNNFLbsQ_wu-nQHHh7WSEsvZbEzWgm_yIOC73lUxH4RIEAKNFAraC65BoJZMAJHf2v6nCaTO7K2zqP7PpgcrWJkJ1VQQJyjzwakMiSQXstSAMKt-5u0TZgdIZcYuFbtR96MvVNOA06Ma_iSo3HxbPg49YqG_sjlc64pIOS7rWta4b6uk3RhBWoBM8ncOZkLRoRqZwH3WmUl41XdbxGUszA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
استوری مهران غفوریان به‌مناسبت تشییع رهبر شهید در عراق: حسین جانم مهمان داری
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/448032" target="_blank">📅 23:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448031">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd55bc01e1.mp4?token=PRH2Drn966IrOuhSA5WakPzH9A6YCGDXJX8UMqcZ3EsjmMQR-DDr72LKHmwnWf9zpzeuZQ3bunQ-gBRIlnwii_VRo-ta_ldDc8JFL9BDkQm1JRp8Abq8z54Uj0F_pwxt8TZCaOuPh2Dbmbjxqa-PuToL42q1qZBfDFPF1alwRi3G7k2YTIZ2iJjZxWFw_uamOkTNNtpu9JMnV_6uiw07yw3fJHwKy9EIfzjobOMRxmL7yUzyhgN_EAzHsVpWj8jhN_b5OBYMFxCpHn0aKOel0y0tbFr7Kd9htNpTxNgii82dLA9yqiJxP3g5SxOZdCW-fPOHQWNd1VYhmOlWt4DnNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd55bc01e1.mp4?token=PRH2Drn966IrOuhSA5WakPzH9A6YCGDXJX8UMqcZ3EsjmMQR-DDr72LKHmwnWf9zpzeuZQ3bunQ-gBRIlnwii_VRo-ta_ldDc8JFL9BDkQm1JRp8Abq8z54Uj0F_pwxt8TZCaOuPh2Dbmbjxqa-PuToL42q1qZBfDFPF1alwRi3G7k2YTIZ2iJjZxWFw_uamOkTNNtpu9JMnV_6uiw07yw3fJHwKy9EIfzjobOMRxmL7yUzyhgN_EAzHsVpWj8jhN_b5OBYMFxCpHn0aKOel0y0tbFr7Kd9htNpTxNgii82dLA9yqiJxP3g5SxOZdCW-fPOHQWNd1VYhmOlWt4DnNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
أین خامنئی، أین...
شعرخوانی عراقی در جوار پیکر مطهر رهبر شهید انقلاب اسلامی در فرودگاه نجف
@Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/448031" target="_blank">📅 23:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448030">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe1348d52.mp4?token=AHpTIEYKelNblZdzfhiqm4KWTL-VHhjPTZZtbSVZVnoMIQlnNplFHD7jjlKv2jJ8m_TDdZnGHLzkAnnVP8AoY3t9x-zXVVfeRp4XrblJO3R36etlajkJ8Mdfs0wTM2IdR0FKehhkdNqjqDg1n_hCAZ848Ljs8r4vYwlmMEOjp4lmddDL8T8Ic-uZZg2bRyLhucw10Ff_LCzZfFuQbTjAjydcoF7MBBiRr9MKhVbwM6HgNrzSW46yAHtlWWYgncWTzVqvpMs-fbvRizWE_RrOq503JB3lYOluGst3C1XI4H6Y7SEMAFMwgT3TDl3ZQ6jDPhq5IwaPt2J868h4mhpLQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe1348d52.mp4?token=AHpTIEYKelNblZdzfhiqm4KWTL-VHhjPTZZtbSVZVnoMIQlnNplFHD7jjlKv2jJ8m_TDdZnGHLzkAnnVP8AoY3t9x-zXVVfeRp4XrblJO3R36etlajkJ8Mdfs0wTM2IdR0FKehhkdNqjqDg1n_hCAZ848Ljs8r4vYwlmMEOjp4lmddDL8T8Ic-uZZg2bRyLhucw10Ff_LCzZfFuQbTjAjydcoF7MBBiRr9MKhVbwM6HgNrzSW46yAHtlWWYgncWTzVqvpMs-fbvRizWE_RrOq503JB3lYOluGst3C1XI4H6Y7SEMAFMwgT3TDl3ZQ6jDPhq5IwaPt2J868h4mhpLQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرودگاه نجف صحنۀ عزاداری برای رهبر شهید انقلاب شد
@Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/448030" target="_blank">📅 23:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448029">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2b2478ed.mp4?token=sorHYOnz3qESCZaz8CEdEEsMarynzozUIbRU6q6sy12R8-sSXGBOamnvTha6tVQSMhDkGBdh4nxqxwBUK-WEAWcCAdp0AZZnSXAXxgAZNg3CSiW-uMvGI6ZYdiqa-XlQLjfCEN13cndHP244ytD_TuSsqBqUPBqwHAcCOsq8yjaTXc0j0h82_LZYAYStbcHKy9WtW1uQbuSz5WyiT3Su_ruY_mbGxXRq7T6zs3PMpZ9HFJtyAch5M5Ulianq1TXnAFihGNdG5_EI-vHh67yWQ8aN8oK2aXSnp7I_5jBH-N6bLcOohbF40HGbh_1RORlRwSSWVErmBrMGv2UujUyE_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2b2478ed.mp4?token=sorHYOnz3qESCZaz8CEdEEsMarynzozUIbRU6q6sy12R8-sSXGBOamnvTha6tVQSMhDkGBdh4nxqxwBUK-WEAWcCAdp0AZZnSXAXxgAZNg3CSiW-uMvGI6ZYdiqa-XlQLjfCEN13cndHP244ytD_TuSsqBqUPBqwHAcCOsq8yjaTXc0j0h82_LZYAYStbcHKy9WtW1uQbuSz5WyiT3Su_ruY_mbGxXRq7T6zs3PMpZ9HFJtyAch5M5Ulianq1TXnAFihGNdG5_EI-vHh67yWQ8aN8oK2aXSnp7I_5jBH-N6bLcOohbF40HGbh_1RORlRwSSWVErmBrMGv2UujUyE_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تسلیت و ادای احترام نخست‌وزیر عراق به فرزند ارشد رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/448029" target="_blank">📅 22:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448028">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea3d66844.mp4?token=Li94qmjb-Ake1jmp7edNe2s1WTEGm1zNPgMeod0JL436_uUPxYkUshONgfXRsRCj-0eDTMQAWze6PXkMzCJ5ZBNqkwmThbTKPP8KLkYUezIbINraaRugIAPD1BifG2yicbXrediVCnUyKnGOv_NvD6lSpb01oM50NsMeKVm-8rOuEaOPibYhfIbTJkOPYSbWp4P-OkdGdiNa0NzLtVJf4WZr3pyYfc1QMHdd0d57KNwolGzHLadYSjgEnY8EkjJyvbvkr-zNlXv7L9905wGgxktyQM3SHEi_j9PSNpiI_1Q7sDYQ5yPUuJUbaWQflrwxC4IwMjg83MVlnGMtXqZveA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea3d66844.mp4?token=Li94qmjb-Ake1jmp7edNe2s1WTEGm1zNPgMeod0JL436_uUPxYkUshONgfXRsRCj-0eDTMQAWze6PXkMzCJ5ZBNqkwmThbTKPP8KLkYUezIbINraaRugIAPD1BifG2yicbXrediVCnUyKnGOv_NvD6lSpb01oM50NsMeKVm-8rOuEaOPibYhfIbTJkOPYSbWp4P-OkdGdiNa0NzLtVJf4WZr3pyYfc1QMHdd0d57KNwolGzHLadYSjgEnY8EkjJyvbvkr-zNlXv7L9905wGgxktyQM3SHEi_j9PSNpiI_1Q7sDYQ5yPUuJUbaWQflrwxC4IwMjg83MVlnGMtXqZveA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان و نخست‌وزیر عراق به استقبال پیکر رهبر شهید انقلاب رفتند
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/448028" target="_blank">📅 22:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448027">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10b0927df8.mp4?token=G2cwo9f-GrgZiTfMn2ViA-ke3zi6LPtOVAZe3oqYor2ckJTslnLkOVAkfJUPZGROO38zYfno3iQCRZ3f-75XJ6arQiNDmAQuLRHWwQVVMKKVuRkpUpOvBZFGT-SE7k70ZQxOXfYBQeVbX3325WLCpHbcl8wKQyM8R_6J43lMqKZKeL2t_bTyT1fvV82ZtMRWlh8CtvQSTkRLaDChajAWLFOxgqKRaX4MBS_cvHv_y_2PRaMSmBCWbwam4n3yXdOdjm4N5bIu56a3pFM0wrLFl5Xm6FLXnCxet6vW4meiH2G4R_iybtDdreJdCqaJmdfmHDUgj6BJ3nUEtNzVZzSWcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10b0927df8.mp4?token=G2cwo9f-GrgZiTfMn2ViA-ke3zi6LPtOVAZe3oqYor2ckJTslnLkOVAkfJUPZGROO38zYfno3iQCRZ3f-75XJ6arQiNDmAQuLRHWwQVVMKKVuRkpUpOvBZFGT-SE7k70ZQxOXfYBQeVbX3325WLCpHbcl8wKQyM8R_6J43lMqKZKeL2t_bTyT1fvV82ZtMRWlh8CtvQSTkRLaDChajAWLFOxgqKRaX4MBS_cvHv_y_2PRaMSmBCWbwam4n3yXdOdjm4N5bIu56a3pFM0wrLFl5Xm6FLXnCxet6vW4meiH2G4R_iybtDdreJdCqaJmdfmHDUgj6BJ3nUEtNzVZzSWcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احترام نظامی عراقی‌ها به پیکر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/448027" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448026">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22140a29b6.mp4?token=p0GgM4JZELk74F1s6wSPUgt76apiB6opoLGs5Cbj03Kgur3zMsNRZxw4uAl5B_sFLpcwQ33XpmzBDlEMcavVD3PBUe8GMT1lgvCIWNX2pOOGQhlyAgkOT84uPN6vQqxGobuohyuNP3jAI1s9kraOdFKd1ID9La94p2PFQ2TSdi-0xi4McvwtplcULepxqxD4rSR28_kVp_mHYp2RYrIEzl--_1JHUNkBBW5IMUO-VqF4mG2kBH9sBr5oEw6muuuCJFH43GX3HwCgOZUnwo28JoNRhqR6vDJFXHewgcCaS3z7HeHAC-s9_3PZMjAxa3HbW0Z48wD_UYAh7GoOeV3SyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22140a29b6.mp4?token=p0GgM4JZELk74F1s6wSPUgt76apiB6opoLGs5Cbj03Kgur3zMsNRZxw4uAl5B_sFLpcwQ33XpmzBDlEMcavVD3PBUe8GMT1lgvCIWNX2pOOGQhlyAgkOT84uPN6vQqxGobuohyuNP3jAI1s9kraOdFKd1ID9La94p2PFQ2TSdi-0xi4McvwtplcULepxqxD4rSR28_kVp_mHYp2RYrIEzl--_1JHUNkBBW5IMUO-VqF4mG2kBH9sBr5oEw6muuuCJFH43GX3HwCgOZUnwo28JoNRhqR6vDJFXHewgcCaS3z7HeHAC-s9_3PZMjAxa3HbW0Z48wD_UYAh7GoOeV3SyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال پرشور عراقی‌ها از رهبر شهید در فرودگاه نجف   @Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/448026" target="_blank">📅 22:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448025">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhMXVljo93PNY0UZ1IzD4qLhxUVbGl28NVmvUyKogt5Isc81UNTNfRoHR2aXnx5e7nViLYEw-66vSpm6s3G54hEQ03vn9ZNpnsUvFU4rk4hvdWudwFkKoR-HkUXMPVYBBDvoo2Q60rdDiMLpNi55-SlJvj2orycxvg9u-R-GQj5Z7C-CAggwBxHzZXhb7xqNiSdetf9LAbd6iq-Ix0VQlZ06YHquwj_ZWnIshEVuQldi0AXA4oVKSdQbiHBE3JYpI44P3hqIsmUznAfts5cgj29Bi36kK2xk3zNakDslE0PBDETQh-7YLIUJat9tY44csLGXOxs0-FSoi9hMAquXxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مخبر: فریاد انتقام رهبر شهید به مطالبه‌ای بین‌المللی تبدیل شده است
@Farsna</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/448025" target="_blank">📅 22:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448024">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddUiyakdySfncu_4oSgQ3SbvPDND_YRUrC7_QmClDC5-eBqtSSUyUmybwYaCgf7uFrcg7Xu0w3nQiOmoxpVxJlWwnE15U4P0OlQpV98orWFbrHBvfv0OU0DWg0H04Lx4KpvlbgmS4amyVXznnYklpc2f26xDPM5YTRasa0lgyym0NDdTY24OrQm75iVWv_j6ipFgpdukTQMqkf97YojpwCVtlEQPI5ufpSR2_8aMJezXzuu96DWAg-I6H66gQ8SJNp1Sbi34HQMTCivYqDjAr5nulaasa_qwiAFqRytT66nMUs-6uXQ2AjcbA1E1FWWxFRt2V2U6ceSPsjCYFAJAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
بدعهدی دوباره آمریکا؛ مجوز لغو موقت تحریم‌های نفتی لغو شد
🔹
دولت آمریکا به مجوز موقتی که امکان انجام برخی معاملات نفت و فرآورده‌های پتروشیمی ایران را فراهم کرده بود، پایان داد. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/448024" target="_blank">📅 22:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448023">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16f13a76f1.mp4?token=FO16MMhpZwwroo0qSOoxwkFP5eEgUkviOFJb9VNIkLGYb48NwQjxrfb1dWeYpAQEgom14NmXPLJc80aNTc_tekETfisVXtGdHYhRHlmLYe2j0EYqNVUPVBOcD04r5Pv5FPdrNvbuNe-WDjolz7YBXrC4w8uk66I7LKSld5Fah3jdXkTUZeDGkJ2wZU3N_5dvTQs7WPNMAaHznR1KZGp53Z5isamFf5jxsrRnM26Ep1j4URa7-EEVlZrM3gWEt-HW4_h3ojyGB3W_Ut8m7As2R4G5heDoE-dl2B5E2YCiLcwvfZ-iI2OPJqtiucQcNPPOVfEgOGBlox9g8DUSiVwk5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16f13a76f1.mp4?token=FO16MMhpZwwroo0qSOoxwkFP5eEgUkviOFJb9VNIkLGYb48NwQjxrfb1dWeYpAQEgom14NmXPLJc80aNTc_tekETfisVXtGdHYhRHlmLYe2j0EYqNVUPVBOcD04r5Pv5FPdrNvbuNe-WDjolz7YBXrC4w8uk66I7LKSld5Fah3jdXkTUZeDGkJ2wZU3N_5dvTQs7WPNMAaHznR1KZGp53Z5isamFf5jxsrRnM26Ep1j4URa7-EEVlZrM3gWEt-HW4_h3ojyGB3W_Ut8m7As2R4G5heDoE-dl2B5E2YCiLcwvfZ-iI2OPJqtiucQcNPPOVfEgOGBlox9g8DUSiVwk5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رئیس‌جمهور و وزیر امورخارجه در فرودگاه نجف برای ادای احترام به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/448023" target="_blank">📅 22:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448022">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27d4cfe38f.mp4?token=aJrSUaxUhmOPaoYUaM7uuucJUfBEe98zkXa1W5aWAvmS19fs1dI2T5pOPXY1ugRFlBY4s8lnSpQsFGVauUKXYkyCkqytpFym50c3T9vjXMkMscQvuDZVtEc_S0HftmH-KtV6T7HX9JITEZ6lNEg-jIQu2P5XeUp343TQYNJCEhA8lBwGcIk4CVylouPTSxx1Xbo8BGXLWv5U3MqZrefzVtL7S9agTu4Yu7XZhWMaujdQDncTwCnfYKoGxovEZp21QF7_mHtvI2M_Pp7zJ62WM3rf_Mb_EYZ7rury6lRuxG2yPN2-uTEDS5Tf5jvpb4dkNGo8QAFxI3uGz3ZZCXavaFtirO8qZ_OLAO3haYGBE3Zj_1lBDOz3Xb8HsBn4M4WZkS4qIEsdcl98pUTBWwd0O3_COKfZ1mwdL3NXyheE2UU_BHoB1hICIgAPz6uOYASV9VUV2D028k3s03d5T5jkI3WOuKET0wjjPHwqKWv1B_tgzOFpKsyRbAablXUyzUN7NdDTGNf9LtIbXwwP2qCBpE9hR3zq9yrxKFk3MXpg_wwLWQjQikOj_PWOzFctAiJuYpUtE9SFuhj8ILeKb_An1rqUMUAhiD2nOWPuq1Mt-BhcjpyMn84vL1n2IbVXJO2jMF2GIPGxowZYdG4QhdmzccVBZdhrrjL5cCJS95ni-Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27d4cfe38f.mp4?token=aJrSUaxUhmOPaoYUaM7uuucJUfBEe98zkXa1W5aWAvmS19fs1dI2T5pOPXY1ugRFlBY4s8lnSpQsFGVauUKXYkyCkqytpFym50c3T9vjXMkMscQvuDZVtEc_S0HftmH-KtV6T7HX9JITEZ6lNEg-jIQu2P5XeUp343TQYNJCEhA8lBwGcIk4CVylouPTSxx1Xbo8BGXLWv5U3MqZrefzVtL7S9agTu4Yu7XZhWMaujdQDncTwCnfYKoGxovEZp21QF7_mHtvI2M_Pp7zJ62WM3rf_Mb_EYZ7rury6lRuxG2yPN2-uTEDS5Tf5jvpb4dkNGo8QAFxI3uGz3ZZCXavaFtirO8qZ_OLAO3haYGBE3Zj_1lBDOz3Xb8HsBn4M4WZkS4qIEsdcl98pUTBWwd0O3_COKfZ1mwdL3NXyheE2UU_BHoB1hICIgAPz6uOYASV9VUV2D028k3s03d5T5jkI3WOuKET0wjjPHwqKWv1B_tgzOFpKsyRbAablXUyzUN7NdDTGNf9LtIbXwwP2qCBpE9hR3zq9yrxKFk3MXpg_wwLWQjQikOj_PWOzFctAiJuYpUtE9SFuhj8ILeKb_An1rqUMUAhiD2nOWPuq1Mt-BhcjpyMn84vL1n2IbVXJO2jMF2GIPGxowZYdG4QhdmzccVBZdhrrjL5cCJS95ni-Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان ۶۹ سال فراق
🔹
زمستان سال ۳۶ به عتبات رفتم. فلسفه‌ی این سفر این بود که مرحوم پدربزرگم میخواست خانمش و بعضی از بچّه‌هایش را به عتبات بفرستد و مادر من را هم جزو این مجموعه قرار داد. منزلشان بودیم که به خود من گفت: «من پول سفر مادرت را میدهم؛ به شرطی که پدرت پول سفر تو را هم بدهد که تو هم با اینها بروی؛ برای اینکه یک مرد همراهشان باشد.» خب طبعاً جایی برای اینکه خود آقا بیاید، نبود؛ زیرا آمدن آقا به این معنا بود که همه‌ی خانواده بیایند و این امکان نداشت. نفری پانصد تومان خرج عتبات میشد. آمدم به آقا گفتم و ایشان هم قبول کرد. ‌‌‌
‌
🔹
این سفر، حدود دو ماه طول کشید؛ از راه خرّمشهر؛ یعنی همان راهی که در سفر کودکی در سال ۱۳۲۴ از آن راه رفته بودیم؛ منتها در آن سفر، از طریق قاچاق و با ترس و رعب رفتیم، در این سفر، نه، خیلی راحت سوار ماشین شدیم و رفتیم شلمچه، آنجا در مرز _هم مرز ایران، هم مرز عراق_ گذرنامه‌هایمان را دیدند و بعد، بی‌دغدغه تا بصره رفتیم و از بصره هم سوار قطار شدیم و رفتیم بغداد و چند روز در کاظمین، چند روز در کربلا و چند هفته در نجف بودیم و بعد آمدیم سامره و برگشتیم ایران. البتّه من در نجف بیشتر از خانواده ماندم. این کلّیّت سفر عتبات ما بود.‌‌‌
🔹
هدف ابتدایی من از این سفر بررسی حوزه‌ی علمیّه‌ی نجف نبود، لکن وقتی حوزه‌ی نجف را دیدم، شوق ماندن در آنجا به دلم افتاد؛ دیدم نجف، جای درس خواندن است و باید اینجا بمانم. راه ماندن من در نجف هم رضایت آقا بود؛ خانم همراه بود و به نحوی میتوانستم او را راضی کنم، امّا کار اصلی این بود که باید آقا را راضی میکردم. مسئله‌ی تأمین مالی هم بود؛ طبعاً در نجف راه درآمدی نبود و من هم با شخص خاصّی ارتباطی نداشتم و لذا باید آقا من را از مشهد پشتیبانی میکرد‌. برای همین چند بار نامه نوشتم و به ایشان اصرار کردم که بمانم ولی آقا اجازه نداد و هر بار میگفت نمیشود و نمیتوانی. من از اوضاع نجف اطّلاع داشتم امّا پدرم سالها در نجف بود و سختی‌های زندگی آنجا را دقیق میدانست. البتّه شرایط شهر نجف واقعاً برای زندگی سخت بود. الان مردم نمیدانند که نجف ‌ماندن در آن زمان برای طلبه چقدر دشوار بود؛ مگر اینکه طلبه شوق خاصّی در دلش داشت؛ حالا چه شوق دنیا، چه شوق آخرت. برای من همین که در محیط نجف، همه جا درس ‌و‌ بحث و علم است‌، شوق‌آور و خیلی جذّاب بود و دلم میخواست بمانم؛ نشد.
🔹
از جمله، علّت دیگر اینکه آقا موافق نبود که ما به نجف و بعدها به قم برویم این بود که بچّه‌ها دور نباشند؛ ‌‌‌به‌ خاطر همان محبّتی که ایشان داشت، دوری ما سختشان بود‌‌‌. نجف که نشد؛ برای قم هم من اصرار کردم و نذر کردم و ختم گرفتم تا بالاخره راه قم باز شد؛ الحمدلله. اوقاتی که من میخواستم به قم بیایم، یکی از دلایلی که ایشان برای قم نیامدن ذکر میکرد این بود که میگفت: «شما شب که میخوابی، لحاف پس میرود، یکی باید بیاید لحاف را رویت بیندازد!» این‌قدر محبّت داشت.
شهید خامنه‌ای به روایت خودش
@Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/448022" target="_blank">📅 22:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448021">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f61042e6d.mp4?token=iH03oW6ZPllxpUUX8Gv6z2JGkBIuDxnK5ASmMpCzSWcqY2Yh6UipN0485WL3fQT4RqFqdmosvJJ6niksRV8zRauxX2tf9BiWCM8y8tCHhjHA_ncpqyJnzfSUBEpHOU0vpl7meFM1HLVVQ4RDosbYRHc1c0dN90sToo7j3-AkR0OYVfY58JeRKCJjec6WC40MRLJ_0-BGfI1CVOKtpgmnfcOcw76ovm1NaG1wFYhkGYSkWJpw-rfaDFk14wm_yQkjqZXhFo3BMCZ7CuzKbgjc1gV2vRQ6sERn45ePLMr9BuTgv7GMhG6kmjCGK1DBcyIeKVKS0ePC32KgvqG9EvA_LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f61042e6d.mp4?token=iH03oW6ZPllxpUUX8Gv6z2JGkBIuDxnK5ASmMpCzSWcqY2Yh6UipN0485WL3fQT4RqFqdmosvJJ6niksRV8zRauxX2tf9BiWCM8y8tCHhjHA_ncpqyJnzfSUBEpHOU0vpl7meFM1HLVVQ4RDosbYRHc1c0dN90sToo7j3-AkR0OYVfY58JeRKCJjec6WC40MRLJ_0-BGfI1CVOKtpgmnfcOcw76ovm1NaG1wFYhkGYSkWJpw-rfaDFk14wm_yQkjqZXhFo3BMCZ7CuzKbgjc1gV2vRQ6sERn45ePLMr9BuTgv7GMhG6kmjCGK1DBcyIeKVKS0ePC32KgvqG9EvA_LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نتانیاهو: مهم‌ترین هدف مذاکرات، پایان‌دادن به برنامه هسته‌ای ایران، خارج‌کردن مواد غنی‌شده و برچیدن سایت‌های غنی‌سازی ایران است؛ البته موارد دیگری مثل جنگ‌های نیابتی و موشک‌های بالستیک وجود دارد
🔹
اگر توافق به این اهداف دست یابد، تحریم‌های ایران برداشته خواهد شد. اما من هنوز چشمم آب نمی‌خورد که چنین اتفاقاتی رخ دهد.
@Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/448021" target="_blank">📅 22:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448019">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oesv42XsyjLZcP4prRCIXtSRqiaU11usgbd3rOY0kvzA_Iqc3EnsAS8x2EHSDZwiha-XH0aeRmzfgLJvoIar6ugStXT3ohCtLQCRIAcLoXBajOcfW8zZA2KuCPe5JuKXQOfRmXy98n8_wfvTGES3PPxUAZvkjYwW6KcUEXmTxactyUJ1g1nuuO_MaZaJTPDEfgpLveBTMb5x0tyZ9cLdoiSw7mGnoPUSrEjFNQMMGJmxI0-77mmY61hZAQ-VRKE4kYJ4FbFH09U3r-NF9rA5RDreNdzZSOg7qh0LaZE4CVQrEi5LU3K2IGC0cuZmtqJswLQMx1ilmVwUnen8_dK1kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حال‌وهوای اطراف حرم سیدالشهدا در آستانۀ تشییع رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/448019" target="_blank">📅 22:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448018">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
مجوز خزانه‌داری آمریکا برای معافیت صادرات نفت ایران از تحریم
🔹
وزارت خزانه‌داری آمریکا مجوزی برای معاف شدن صادرات نفت و محصولات پتروشیمی ایران از تحریم‌ها صادر کرده است.
🔹
دولت آمریکا در بیانیه‌ای گفته که «تولید، تحویل و فروش نفت خام، محصولات پتروشیمی و…</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/448018" target="_blank">📅 22:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448017">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ce828acd4.mp4?token=OrogvVz_spJJFKr9fRrT2yptinky3jzdX_LwejHXP8FgiRY_40IgbEAlsE-dR3e4uqTfvf8IMPTRtfrh__vDAIyjZNzaSBNK0rBKSLv8sWt71-srdsxLp4jNsb_PB5cXkVWAEuzU4vPqaZm6lblhN0FPVpqB2aU5L0soJJJDkMC8FmdD2n3GQfCw9EhROfTfURjMQX4O0s3TJxxlGgTbtl3WkitrQVUhOL_ZBssRCihNGjM0yhk5lOA_7U2sW2pzDt9ulzlneHZBH4sPKHteaWCmgD7pr9e7zP35PGxhjCaf5yHPqS0cD9FZpITNTUlEXE5Absur6iJEa7dgij5x0oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ce828acd4.mp4?token=OrogvVz_spJJFKr9fRrT2yptinky3jzdX_LwejHXP8FgiRY_40IgbEAlsE-dR3e4uqTfvf8IMPTRtfrh__vDAIyjZNzaSBNK0rBKSLv8sWt71-srdsxLp4jNsb_PB5cXkVWAEuzU4vPqaZm6lblhN0FPVpqB2aU5L0soJJJDkMC8FmdD2n3GQfCw9EhROfTfURjMQX4O0s3TJxxlGgTbtl3WkitrQVUhOL_ZBssRCihNGjM0yhk5lOA_7U2sW2pzDt9ulzlneHZBH4sPKHteaWCmgD7pr9e7zP35PGxhjCaf5yHPqS0cD9FZpITNTUlEXE5Absur6iJEa7dgij5x0oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقی‌ها پای هواپیما به استقبال رهبر شهید رفتند  @Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/448017" target="_blank">📅 22:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448016">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f2af20dd.mp4?token=POnx91Jur1in5MCtfUaYEenqOOX0SVlWITrfoGH5Im-ivjfwoLwhvkWlnogpAlwX44mpCkIbqKKyCK8N7NgzzfHC_vKfP3uuarZ4MwUHq9i0jVu7EZjXifiVn5O92tWPJyvCCu665jYytR_KZszuVjwvVid09gSSYQS1nQFk28H4goVrurbv_dewOpwXL9zxv_GjjuDIvj4SsPgNiEqin8F1jhcq9auUwtJ8Z_Xk63eeIe46jwhTzP8XCUX_k7pthONwtqzQ3RhgrMHX4awFY3wKUbN3RGCCdJgefzHgz0xWYDEzUvpVTykb4Mk4BetXweoAOQVorf6JR5yh5KZK84WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f2af20dd.mp4?token=POnx91Jur1in5MCtfUaYEenqOOX0SVlWITrfoGH5Im-ivjfwoLwhvkWlnogpAlwX44mpCkIbqKKyCK8N7NgzzfHC_vKfP3uuarZ4MwUHq9i0jVu7EZjXifiVn5O92tWPJyvCCu665jYytR_KZszuVjwvVid09gSSYQS1nQFk28H4goVrurbv_dewOpwXL9zxv_GjjuDIvj4SsPgNiEqin8F1jhcq9auUwtJ8Z_Xk63eeIe46jwhTzP8XCUX_k7pthONwtqzQ3RhgrMHX4awFY3wKUbN3RGCCdJgefzHgz0xWYDEzUvpVTykb4Mk4BetXweoAOQVorf6JR5yh5KZK84WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای اطراف حرم سیدالشهدا در آستانۀ تشییع رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/448016" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448015">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64905c135.mp4?token=vq7ZynfXbxTdq4EGWQy6BA8mwqElW1LNqhYWPmQWubL4BsICZQG5kxceFrEUuIsgUZGh88ANiz3TswtdJLe-Yh0LYfP7szplsa6AQR-ARQxo-Oi63dSFA3q2I7e-cyF8o9PBWfocgl4peP31Q0ZSemwvgt85-307IftTOXZzyqwFKypWuLFlrn2waNEFcOTVhJlL8NrVe1EM4xWmPy5bzPW-jQmwR0aTIbJhkH8txLDYbSIQ3Vj4omchYzEQfy6AjUpMbkGb4d0Vtx_giAkDeAk95wcD5wlb3xM8DVE7_7bsdMgccOt0yJ3EFPi4xheZLOP42sz8oO9mMvWkZoHENg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64905c135.mp4?token=vq7ZynfXbxTdq4EGWQy6BA8mwqElW1LNqhYWPmQWubL4BsICZQG5kxceFrEUuIsgUZGh88ANiz3TswtdJLe-Yh0LYfP7szplsa6AQR-ARQxo-Oi63dSFA3q2I7e-cyF8o9PBWfocgl4peP31Q0ZSemwvgt85-307IftTOXZzyqwFKypWuLFlrn2waNEFcOTVhJlL8NrVe1EM4xWmPy5bzPW-jQmwR0aTIbJhkH8txLDYbSIQ3Vj4omchYzEQfy6AjUpMbkGb4d0Vtx_giAkDeAk95wcD5wlb3xM8DVE7_7bsdMgccOt0yJ3EFPi4xheZLOP42sz8oO9mMvWkZoHENg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید از هواپیما خارج شد  @Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/448015" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448014">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70799d097f.mp4?token=qngnL_0IFVuk6JfcopQeIZul_iyVO3fP-eXcxfkUAmKVuI7robUjMmoSTkQrZ3nX_H2uvAJbxVPdU5uW0jEXno2_00QuP5TyN8E7YLvrM43wKO9bcxoI0ltGCP9tsk5P8BM5V40xWDGlxdoW_G0POVdEi2l2EdD2sElrSeN_HE4kjKQH40IMtV9MrbesxY5qDzCyGG5ZsSFvIzl0yuLfLMhj95mjiTxRlu45Jbo0WdqY1ZyF1SDsh6IWImu-Dryxi39zNV5B7K39zO69zKXo0ZT3toHlhmZItDfwcoQMdUi318CF5ZUaSotRYyKDVF1TZzgXy-5Nb7EhHg84eWwd2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70799d097f.mp4?token=qngnL_0IFVuk6JfcopQeIZul_iyVO3fP-eXcxfkUAmKVuI7robUjMmoSTkQrZ3nX_H2uvAJbxVPdU5uW0jEXno2_00QuP5TyN8E7YLvrM43wKO9bcxoI0ltGCP9tsk5P8BM5V40xWDGlxdoW_G0POVdEi2l2EdD2sElrSeN_HE4kjKQH40IMtV9MrbesxY5qDzCyGG5ZsSFvIzl0yuLfLMhj95mjiTxRlu45Jbo0WdqY1ZyF1SDsh6IWImu-Dryxi39zNV5B7K39zO69zKXo0ZT3toHlhmZItDfwcoQMdUi318CF5ZUaSotRYyKDVF1TZzgXy-5Nb7EhHg84eWwd2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از پیکر مطهر رهبر شهید انقلاب در فرودگاه نجف اشرف  @Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/448014" target="_blank">📅 22:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448013">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4baaee3840.mp4?token=C75u4VpTTzQGuF8pVFQ4qei6f3D404Y0tyVIbXDRC3l1m8aw_mNA_VQcchVHrjpYuLpSNSyOh-p4H6r0JcNHpwoqAjVr-I6A8BA2aWAPyI0iG-NdEy4NSvDhojWIXW9Evo-9aERO8-zptNWMju1MefxI9p3JwUxzWEiAhRaZdBMAnn8Sr3Pm5z8U11B45huXOgG_4Kq3k1VCKG7QWy8mXv__VRt4IoBCBaF4XiMuq2hta02TIbOHD_4CHijP99p_vdMUtihy_IyHfzk9C3q4f4yH-aionS9YiANMINFmtVKy0tN6WLRK5XCErnn0ReIK5Pcbaez9AKj6aP3n3fRrMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4baaee3840.mp4?token=C75u4VpTTzQGuF8pVFQ4qei6f3D404Y0tyVIbXDRC3l1m8aw_mNA_VQcchVHrjpYuLpSNSyOh-p4H6r0JcNHpwoqAjVr-I6A8BA2aWAPyI0iG-NdEy4NSvDhojWIXW9Evo-9aERO8-zptNWMju1MefxI9p3JwUxzWEiAhRaZdBMAnn8Sr3Pm5z8U11B45huXOgG_4Kq3k1VCKG7QWy8mXv__VRt4IoBCBaF4XiMuq2hta02TIbOHD_4CHijP99p_vdMUtihy_IyHfzk9C3q4f4yH-aionS9YiANMINFmtVKy0tN6WLRK5XCErnn0ReIK5Pcbaez9AKj6aP3n3fRrMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواپیمای حامل پیکر مطهر رهبر شهید و خانواده ایشان، وارد فرودگاه نجف شد  @Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/448013" target="_blank">📅 22:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448012">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e02673568.mp4?token=u_gCJuNf_fYHABKW7HwCsRbVcQBUi3BEpszzmvVoR54VGhaZUfGeNCOJq-DMmvEqT007XifSQOmCdEFb14z3gbatbMBJ1tTkwPBvCAhinI6o7-WSSIuYuOrJ_QS-5zMgFlZQj2lreNZr7TADLcVvgPRXtkl4Eg0Yb8tyacJ3GbGA0SsXPYikddKtlCMSYlZpZfU--sbyPQumVXsIdSlmEfhDDvmiQ39z7J48go9k5Pyxu0HrZEVGHZ1nqV79kDuMfSS2e3zdDGNG5d0D6Ah_WTHZoVRMTqk1LOwyZunEbZDJZUqzl9Q-wdxW-K1y8e4RGp4zT40ogZJJkDtDY8l8-RcO6eueEsAZrmSm2OTwUNfoqmr_5pSGP2oIxhyuo3wCy_2zcZy84Sn_5kxfehBudzMt4o3F_jbxHanNsjtZK27GnnkE8ikiFpIyu8nDGbMPlWN23_YkTMhCjwth2rzq_DoQrLJsR9km8kfABCSP1S-YzMQVeUznKFV3QQTF0VdVSpsnMPBqT-OW1wK572lMRNh6o7JRm_BMs9MfoI7za26GkZ6eYNnrpEU3KNirFDjBSxjIFxIDvMgv5o_nziiuomGhCz8hLhlvyaksIxarNMNEjJYkGYGq_fZRsNzJDGkt2B64b7UCn47wjuLY-b_fQ5xIWKaOADx_7zCDnkF4BEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e02673568.mp4?token=u_gCJuNf_fYHABKW7HwCsRbVcQBUi3BEpszzmvVoR54VGhaZUfGeNCOJq-DMmvEqT007XifSQOmCdEFb14z3gbatbMBJ1tTkwPBvCAhinI6o7-WSSIuYuOrJ_QS-5zMgFlZQj2lreNZr7TADLcVvgPRXtkl4Eg0Yb8tyacJ3GbGA0SsXPYikddKtlCMSYlZpZfU--sbyPQumVXsIdSlmEfhDDvmiQ39z7J48go9k5Pyxu0HrZEVGHZ1nqV79kDuMfSS2e3zdDGNG5d0D6Ah_WTHZoVRMTqk1LOwyZunEbZDJZUqzl9Q-wdxW-K1y8e4RGp4zT40ogZJJkDtDY8l8-RcO6eueEsAZrmSm2OTwUNfoqmr_5pSGP2oIxhyuo3wCy_2zcZy84Sn_5kxfehBudzMt4o3F_jbxHanNsjtZK27GnnkE8ikiFpIyu8nDGbMPlWN23_YkTMhCjwth2rzq_DoQrLJsR9km8kfABCSP1S-YzMQVeUznKFV3QQTF0VdVSpsnMPBqT-OW1wK572lMRNh6o7JRm_BMs9MfoI7za26GkZ6eYNnrpEU3KNirFDjBSxjIFxIDvMgv5o_nziiuomGhCz8hLhlvyaksIxarNMNEjJYkGYGq_fZRsNzJDGkt2B64b7UCn47wjuLY-b_fQ5xIWKaOADx_7zCDnkF4BEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوگواری مردم مشهد در رثای رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/448012" target="_blank">📅 22:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448011">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318332762c.mp4?token=JAvgyHmPwdwp0-4KG6k_efakIzTFLWYDsQqNDr2KyJGFMt-ubhJx_uir5QfuR15vusdThGeAknalgtYuIzdpaynpUccsvNLper93rpLIb51o1RxORAPjtOItVXdb0RkvTD8uyVT5NHxm582Qh2tyhru-2haUZn7QA9_T2nHqAy-x6-iB0ocw6nZRWhh4BhZRsilhccfXpzj6sU4A9IustBM3xkj7ZH9UJ_EfMDwXupee9JbW9ymyTsna253kD_6d2iyYBccresNGEqQTMuI_6BWr5jgXT6NqeMYm-ifAKrIpRN-WMa7dj5RLwcg1X8zBjPuDjAYfmpsG5_QdYg5xtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318332762c.mp4?token=JAvgyHmPwdwp0-4KG6k_efakIzTFLWYDsQqNDr2KyJGFMt-ubhJx_uir5QfuR15vusdThGeAknalgtYuIzdpaynpUccsvNLper93rpLIb51o1RxORAPjtOItVXdb0RkvTD8uyVT5NHxm582Qh2tyhru-2haUZn7QA9_T2nHqAy-x6-iB0ocw6nZRWhh4BhZRsilhccfXpzj6sU4A9IustBM3xkj7ZH9UJ_EfMDwXupee9JbW9ymyTsna253kD_6d2iyYBccresNGEqQTMuI_6BWr5jgXT6NqeMYm-ifAKrIpRN-WMa7dj5RLwcg1X8zBjPuDjAYfmpsG5_QdYg5xtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین شعار «لبیک سیدمجتبی» در حرم امیرالمومنین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/448011" target="_blank">📅 22:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448010">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e7db79979.mp4?token=CJWXqp_GwKjOXsQ4e5Piz5L9kbsPwmHOgNjsOzwqkPsGj02b8wOi12hXA7jM0nXS5HA6RyXJtPNHPp7ikIDrZWmwyAGCGfDAL3XprJuu-3jp0M9PfQakQrxcp9pQouKMpe5bl9HOw5ocn1qOoNV84-Xfc9smsm9PI0hsRpAS_opezy2ntLDhPALb0oeibJpO2mDpvBNEvbI3iNUX4suHoJ3KOrjZ7LO4MM9ztwd4LuODHkJn5IzuHEkqHDwS4zEhhrGFHmoIXsWUlEw9VI9_qTt0rvUui9N9zUxMsJYwet3z-aYTmd84WQUa_XvZ2WCQbDOSCdlc1F1ykiHrpsuqehgK-7KJvMp1zoDcprLAnb3UdpECZTbG_xCBlgRAPnFm_UydL0eJ9TZ3mZw0Uw7tzh9gU8oGTLEotCQPtJAGWMOSlX7qbB-MYNgQ8ob3rBFRGWCjEm83rtKjnZPPso1jZ1zAmNoalRqUMN4B3lp5-obQF2Sj_KCRxi74c2b8TCCZuTPIjBWoJRkkbG6s0UMTtBb5KBfgHA6fGyWaj6fhV-kZg3FEnZq5QpKktdAtckZlLJK3vUXGY9HGvVbfR3ojWhYh4p9_zoAK_kATYbyStDKLhlP4SFMPp7F5BCdUOl7WSRdRagJAVkElpN58Dcn_2dRmcOPsmMzZwgEqS_bmeOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e7db79979.mp4?token=CJWXqp_GwKjOXsQ4e5Piz5L9kbsPwmHOgNjsOzwqkPsGj02b8wOi12hXA7jM0nXS5HA6RyXJtPNHPp7ikIDrZWmwyAGCGfDAL3XprJuu-3jp0M9PfQakQrxcp9pQouKMpe5bl9HOw5ocn1qOoNV84-Xfc9smsm9PI0hsRpAS_opezy2ntLDhPALb0oeibJpO2mDpvBNEvbI3iNUX4suHoJ3KOrjZ7LO4MM9ztwd4LuODHkJn5IzuHEkqHDwS4zEhhrGFHmoIXsWUlEw9VI9_qTt0rvUui9N9zUxMsJYwet3z-aYTmd84WQUa_XvZ2WCQbDOSCdlc1F1ykiHrpsuqehgK-7KJvMp1zoDcprLAnb3UdpECZTbG_xCBlgRAPnFm_UydL0eJ9TZ3mZw0Uw7tzh9gU8oGTLEotCQPtJAGWMOSlX7qbB-MYNgQ8ob3rBFRGWCjEm83rtKjnZPPso1jZ1zAmNoalRqUMN4B3lp5-obQF2Sj_KCRxi74c2b8TCCZuTPIjBWoJRkkbG6s0UMTtBb5KBfgHA6fGyWaj6fhV-kZg3FEnZq5QpKktdAtckZlLJK3vUXGY9HGvVbfR3ojWhYh4p9_zoAK_kATYbyStDKLhlP4SFMPp7F5BCdUOl7WSRdRagJAVkElpN58Dcn_2dRmcOPsmMzZwgEqS_bmeOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین وفاداری مردم مراغه در پاسداری از میراث رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/448010" target="_blank">📅 22:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448009">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85d55a0961.mp4?token=rH9h27daIQ-v8puH34IavWw6qOF1dVO4dvXt9KnkRSdNS6OrIeDFhbgTTCV8Sh0vT5d6uLPlSOdDOnBRlGWD5K2SjDTLapu-nGgllfIOdVK33BVKtr219H9r7_Tl9Kz7mUaOjz70r23XGlKcBXLvmucQHQreVw3W43jI5HOEZdeo2VWDBGIq_fwy4H16kC7rEll5t5AMEMFrnguF3sPI52j4UnIHHYxioE27YUQ3vevbG4xRZzSJryCibHUlAffzHfpOJbJD91DwtlsJ2Rd5H0GVS6JhE1MNxOqNw-KOySdEXJWvt8mndSWWPI12V88TRUXfnIoUvVQWsC7VEuCsvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85d55a0961.mp4?token=rH9h27daIQ-v8puH34IavWw6qOF1dVO4dvXt9KnkRSdNS6OrIeDFhbgTTCV8Sh0vT5d6uLPlSOdDOnBRlGWD5K2SjDTLapu-nGgllfIOdVK33BVKtr219H9r7_Tl9Kz7mUaOjz70r23XGlKcBXLvmucQHQreVw3W43jI5HOEZdeo2VWDBGIq_fwy4H16kC7rEll5t5AMEMFrnguF3sPI52j4UnIHHYxioE27YUQ3vevbG4xRZzSJryCibHUlAffzHfpOJbJD91DwtlsJ2Rd5H0GVS6JhE1MNxOqNw-KOySdEXJWvt8mndSWWPI12V88TRUXfnIoUvVQWsC7VEuCsvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریایی از جمعیت میلیونی برای آقای شهید از زاویه‌ای دیگر
@Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/448009" target="_blank">📅 21:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448008">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f38ca023e8.mp4?token=BOaX8QuebBsiWk6sO5EGsiSQI4wDN3pRbOdV3bqrVtVdwm8ky9rCp6aYIv22rwFdEoK2XqfqCJ4CdnRrLaUJrOwY7eag_fFFdEHPiDanBfSQiOQsFMB0QpgcFB59jO8jXz1zMYZrGwtlTRolaoxWmL1lqScdTCvbTL1K3V57TZooEP301KeQbzRoGs_NpGJkif4Dmp_4A7pWCbioLXnHzju1lHv7JdeRifOsi7bNid3M4D70GtPlqgFnej_kC5koTt22KB7tyaI71YuYjF-fWVbYJmTBh9qNpBHxrOogakKU2Is70liVO5lQ6kjlJ3SwPDkhq3ZPSjZqbCQWFxKoKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f38ca023e8.mp4?token=BOaX8QuebBsiWk6sO5EGsiSQI4wDN3pRbOdV3bqrVtVdwm8ky9rCp6aYIv22rwFdEoK2XqfqCJ4CdnRrLaUJrOwY7eag_fFFdEHPiDanBfSQiOQsFMB0QpgcFB59jO8jXz1zMYZrGwtlTRolaoxWmL1lqScdTCvbTL1K3V57TZooEP301KeQbzRoGs_NpGJkif4Dmp_4A7pWCbioLXnHzju1lHv7JdeRifOsi7bNid3M4D70GtPlqgFnej_kC5koTt22KB7tyaI71YuYjF-fWVbYJmTBh9qNpBHxrOogakKU2Is70liVO5lQ6kjlJ3SwPDkhq3ZPSjZqbCQWFxKoKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزلۀ عراقی‌ها در صحن حرم امیرالمؤمنین(ع) در سوگ رهبر شهید انقلاب
🔹
مردم شعار می‌دهند «یا حیف تموت العیاله»؛ یعنی افسوس که عزیزان از دست بروند.
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/448008" target="_blank">📅 21:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448007">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8107af020.mp4?token=emXmCyXVFYVF-Yvmprgyz5b4EgBDo8Hg5Uq6oOWISfXa7543xoX9cIfVikVvEKj4zhR2HTFujEFhNxW_5E7rE2_ZjlpTH8UyKwfps8pf-6HqyE8BBdjiHWvq3nKE2kxEU8jvgG1zsiNDQJ9X2Kv27m9oORMsX-2lU1gDuLLvZyI5UBIjtG0vg1Yy93x3YLlEhPfQQ6xQKoLC2YGPv2r9r0EyP4H7ps6uN9uak23llvX96WfoXXnJ0NKW1KDZUNxZmuWdwVW5E4-urf5CCsHczZvxpeKSADuYGzSn3dme9klAiVD3w15LBd7U2sc3Nc9T6T-Nig9-ZA8tpmYvjW5J66nmm-89p5E6q-pR4X8UtWB7Sy_-ebo3nnXKQsz_NBvHafe2CSOoXjrxeLLLR5QymhYAik9I-qXqVzFbyMYeMk-sKyUuwAD_E6Mowalm22D0ky0R8WP6M88M_DjvratoY-5Jb7wsaASJY7L4-t5bsLrZPyUimrjYwOsZjeyx3l1lGkhaWR_HecPNqKKeEYs7fUWqcYsecEM98wfPqy5NEtSihiVRWsBrG61QI5rwl4-5GbVKPdGgfBzH6VjN8hz4_xcf3FEOd7zZjH_hCi2FgeMZVfxa77RWMLpAQUDZ5aAFAUhA-cTAPfMThqNZVQEme0_-x2sL7lL2Spyhf4HEva0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8107af020.mp4?token=emXmCyXVFYVF-Yvmprgyz5b4EgBDo8Hg5Uq6oOWISfXa7543xoX9cIfVikVvEKj4zhR2HTFujEFhNxW_5E7rE2_ZjlpTH8UyKwfps8pf-6HqyE8BBdjiHWvq3nKE2kxEU8jvgG1zsiNDQJ9X2Kv27m9oORMsX-2lU1gDuLLvZyI5UBIjtG0vg1Yy93x3YLlEhPfQQ6xQKoLC2YGPv2r9r0EyP4H7ps6uN9uak23llvX96WfoXXnJ0NKW1KDZUNxZmuWdwVW5E4-urf5CCsHczZvxpeKSADuYGzSn3dme9klAiVD3w15LBd7U2sc3Nc9T6T-Nig9-ZA8tpmYvjW5J66nmm-89p5E6q-pR4X8UtWB7Sy_-ebo3nnXKQsz_NBvHafe2CSOoXjrxeLLLR5QymhYAik9I-qXqVzFbyMYeMk-sKyUuwAD_E6Mowalm22D0ky0R8WP6M88M_DjvratoY-5Jb7wsaASJY7L4-t5bsLrZPyUimrjYwOsZjeyx3l1lGkhaWR_HecPNqKKeEYs7fUWqcYsecEM98wfPqy5NEtSihiVRWsBrG61QI5rwl4-5GbVKPdGgfBzH6VjN8hz4_xcf3FEOd7zZjH_hCi2FgeMZVfxa77RWMLpAQUDZ5aAFAUhA-cTAPfMThqNZVQEme0_-x2sL7lL2Spyhf4HEva0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پنجره‌ای به آخرین وداع با رهبر شهید در شهرِ بانوی کرامت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/448007" target="_blank">📅 21:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448006">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cazt-CzlIZHAqlBSs6oHw9gDeS10VW7eKyK60JsCMaYdjGFmnQWx4PkvDaBD0MH9Y8u8zKTnN_HmgfpdTKKIsDTA1stHxtfNd5Bc9cerZe62zHN3EZQvCvefjYH8CoseuE7GzkCml1PxLnpuvS6LGzu_on3fUKiqioUeJ4NZ1pjnjsImlbfe5XryH8EZOAhP4VQI6xy_dF2ToMojT9TkBH6pBeb0bSVwJiaouARS4b73teZ13j--yXFtm1L_sCwIIi3OWC48tg8PyRDReyFSBAPgiNb1WQweDouzg2R_iALOEqocKrCEsXMb6lPljqgDlvdvLpAeWiURQPOWhCcPjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
محل قرار گرفتن پیکر امام مجاهد شهید در فرودگاه نجف برای ادای احترام
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/448006" target="_blank">📅 21:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448005">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aw0KgF0YyoVvs3b2-7C5Q3Yq5NHonlA9NPrLvCeGK13kYDPRMi41KAnzX255fPxPM36ZyLO47yYiC9qRObXBq1dt-eD7-XGh1IdcG4t1bEZV0w8XJbyTJyumyiF6m3cV3r55MzIcHpbAWG-kton9V6HmJ0N07R2_SUMKTB6MYqhrBCJUxp4WKWRJa-WNesu74IBJKUvCyaPyWVRM-P9lykTSktUlV46cXIQEKH7NxBM2RU2feYxIYb861jrBx_nqmBxc1a9zSlCcDEhlVYWS7r0vsjnd3GwbqMOdBkt2GHgNdxJrKvgRXnq0_2rQXbMOwICGyK_HmBTwSp6W-XVdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی: موضع ایران در حمایت از مقاومت تغییرناپذیر است
🔹
مشاور مقام معظم رهبری در دیدار با هیئتی از انصارالله یمن: محاصره یمن باید فوراً پایان یابد و ادامه آن غیرقابل قبول است یمن امروز یکی از ارکان مهم جبهه مقاومت است.
🔹
پس از جنگ ۴۰ روزه، آمریکا دیگر جایی در منطقه غرب آسیا ندارد و موازنه قدرت به سود ملت‌های مقاوم تغییر کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/448005" target="_blank">📅 21:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448004">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d084af3bf0.mp4?token=oRjxxqAIoRAnmpB4tmb6tMpxAlRx3zFRIubXASpOCZImygz6aXwrpJC2jE7KogEsiASO9Lkgazm4opa6NhTSqJE-KOBr0SoPyukD1SrblRoZcFXFxsrXMfx1TKS7xVodmHTL6wA2l3NUlxf7U5BNlZWc76uVfL87I9JLA8lg13H0VTDyMh7gnxQQiu-dd8f2JpbUSGPYB5Oy4WTS1koakaSqd3SOoCSpJ3mmTu6as6vtZyz_tVPOCAQxko0hmOUq7bgoeFK4iJ_iBKdJpXwiRbQDURfemutLhuxURjQaL5vyZZRd42Dlse--9JB0sra8KG9DzNWY37i3Ks727YxsQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d084af3bf0.mp4?token=oRjxxqAIoRAnmpB4tmb6tMpxAlRx3zFRIubXASpOCZImygz6aXwrpJC2jE7KogEsiASO9Lkgazm4opa6NhTSqJE-KOBr0SoPyukD1SrblRoZcFXFxsrXMfx1TKS7xVodmHTL6wA2l3NUlxf7U5BNlZWc76uVfL87I9JLA8lg13H0VTDyMh7gnxQQiu-dd8f2JpbUSGPYB5Oy4WTS1koakaSqd3SOoCSpJ3mmTu6as6vtZyz_tVPOCAQxko0hmOUq7bgoeFK4iJ_iBKdJpXwiRbQDURfemutLhuxURjQaL5vyZZRd42Dlse--9JB0sra8KG9DzNWY37i3Ks727YxsQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
استقبال نخست‌وزیر عراق از پزشکیان در نجف  @Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/448004" target="_blank">📅 21:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448000">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OzPc-IKSTj4fltMCaApzDqsoXWNAXb8mMhhlLPhZmCpfpJSHu06aNKBtxniD-OYT7NCTgcXnN5sBwawa4-4-xo5UbCrmj_0Ewi3wUnU7fkwfMzfprRACfTKdu-LkXQMJwbmB8r-cRFj_HhcHU35eW1Wu3eflHPF2k5p5bp1ZQmlncQEzLzfxBdfrUl34HGL9nDwfBwY1VRL0Amnpt6zbBeC597_UoUUzNoVvHFwSx1Li9zTGmbXy4-BpccgnJOLoPSPvUMS4uzZK0VusqTVrGnd9yM4Z2FDeohy-kd0k1Rs2Kkqy_aTHbVARL42Exy0QJhNC-uvDChMAxQM206_xbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RKu3rSHCAKs0k4iWqvGXdn26vy7qdhDG5xIrUyf5EeMfQVueNTuETdyWaCmlyse3PAzuA4Clz9II5nxKKNAIKzmPeKCy26UHSYLFi-Af8vcEOQziiK9jVsSCozx3tTt0nurm8v2F-XzXyxahrW5XTg9pth6zFkmMCcnGusWnFORdpU6WiGL6iV_zp754xnlm7hZESQ6hfCKxs3i7i3w6vX0H9LXskAp1S_HuOd4bLZYDVc7lsKO6v8jG5yWmsGUZSrkRoY0X97HRouUIfzEyJbIEbG1n8Wx_Yo6WIZ3L9T3B_Nja2aJpgn_U56Z7zYFh8kVXYnxXVgbo8cZ357JO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qXekt2SItnqzRXCAyDqQ36g3DqMvfcY72KXX1xov-6MLDIMD0HV9Zp-f9zAiG6Le-FXHYzB_rTp3-WlemqeRSZxAbsNPxUqcoiSsT37uuTq2UJHHCM0jF5x1wz_7onfK0XphBDPxjh33wNFIj2oYQ4Igd_costNYhuJ4lVB4tmXWNtPVddXCJO3cmdhviW0f9gEvI6RYdSK07rmkV86IH6cImBEPvLPbJGhYgE23r_0G9IbEG5lUuuQfCRvk4UX2UombZLW_hxK0WjADK1FF5xphQowUKmsn7Lf0OWX-59sUNGwFtXp5kLkM7NGDZqwOYbdmSqmOWbF2Adzzu4b2mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXZiSU2pRqcy-FFHzr-MszVZQZwlK6Numox2AoPQrYHJdbCr3C_9MMahrST0GsfdGlgQqZUEmiXNfOdO0c96zXczf1IpKsnd8gEHoH4rjMDr7C2A4VkAZKRax-NiJBdS0RwX-PXp__-0IxWpGV9DBldsN6D5yjxTB__cN1TMBiVW_qF1N7z5tkE3vr4H3Wis2AR_ZZmpqM9rqamGbZ17qsY-8iJ2xV10t9I8JJIdv2Gw-js6sUfR7N1_4HW7QlsGOCxsj9DfqRbHM2WbR27UFiF12D--_j_kpN9fPxqdsebF-opYmyb0oxezm6VQJi-npiC2bGQXmkZpJsFYyeo4KQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
استقبال نخست‌وزیر عراق از پزشکیان در نجف
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/448000" target="_blank">📅 21:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447999">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r18plKdfha5Y2POrDdLpEF5NNijuuBEtT3e6mUwHcx2MtBefBmgLKb6F9k69qPrZnY33k_DRQ1QVnw9XAAe_AyOf8lqaKVLHprcOyBUdtLVqt3BTLoP0oS_MUY4QnH9aJ-_w58mx1eCgSKFXF0IuwlsDyCm0TjVjzbqSkhIRXaelQz_dZE2zRnf86UjX3YuaqCAQkl4tA6N3r8ABaX3lxN735Uf_2JHXO5a8WVXWlyAjlUAJon23iuD5XSDdi5sgvg8eEbuJxfoFs4TjTjviwjIl7cYweMIGTXgODZj2slShyq73BMcN43rX6vEihwjK1ieyBuFunngNsB_di15qnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
آرژانتین گل سوم را هم زد
⚽️
آرژانتین ۳ - ۲ مصر @Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/447999" target="_blank">📅 21:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447998">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef9fb8bb1.mp4?token=ttKkEbYyz22UCHEOgPvjhjSaIOlh74BzFDvnye-IHXbgbDhtGlldQmrxeoBSYCgyaX6CgrnPublESP6qEg_7Q3jNfrFATEmhVA3mY254_9jTSglUUBDNUceVT-xEa0OM8siIYvDeBpCvf8uWXjkNRCEj2dVzUfjSt9JPocEeNiPrCbUxvh25oiyk1m5wiI-qrEWhch3xaCaP2JCJ4Pmh03ELsnI9r1IJzD33sxZNbbe-JKpzzoXBAJmpC2-x1sDm_bRrzkEXN4QQg9MazMgvN1sSlg58ZUuW2QMOh-cq00cWk428urzb0PWijYCkPJyNELa7fupYPzMrdpTzCH7ypQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef9fb8bb1.mp4?token=ttKkEbYyz22UCHEOgPvjhjSaIOlh74BzFDvnye-IHXbgbDhtGlldQmrxeoBSYCgyaX6CgrnPublESP6qEg_7Q3jNfrFATEmhVA3mY254_9jTSglUUBDNUceVT-xEa0OM8siIYvDeBpCvf8uWXjkNRCEj2dVzUfjSt9JPocEeNiPrCbUxvh25oiyk1m5wiI-qrEWhch3xaCaP2JCJ4Pmh03ELsnI9r1IJzD33sxZNbbe-JKpzzoXBAJmpC2-x1sDm_bRrzkEXN4QQg9MazMgvN1sSlg58ZUuW2QMOh-cq00cWk428urzb0PWijYCkPJyNELa7fupYPzMrdpTzCH7ypQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ای مظلوم تنها خداحافظ؛ آه ای تهمت‌ها خداحافظ
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/447998" target="_blank">📅 21:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447997">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8857572e4b.mp4?token=sNubdeDapJXNPHeElK5v7tx40NwkvYEeXwyoOoC4xpS2jKuiMmQ7vqJkrxhj30qQoMlzBIfM3gH5U3kPJFO_KDEPjN0cp-W7A1ZztisQAtKGmASR9CcBom0AD8KcqLlsr-zvUAVhT0tbVkD2TIFder8dn0NkCnj_bT5F3Ce3vwfaWcpL4OFvuLKa5UtcjE9GF-ObeFGU7prnRcRXvtD4WcrkFHZHvKTgSYPrNlXWlPO4nUn4B36ySYaZZqGPvK_kKwRbQDwQHGvN1Vv8li1q-_w8JzxQf-int7Rz19RAia9rOsDG9V6uUMYqD7fLNS3TRH_obVipZkqvJLwAPYbjUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8857572e4b.mp4?token=sNubdeDapJXNPHeElK5v7tx40NwkvYEeXwyoOoC4xpS2jKuiMmQ7vqJkrxhj30qQoMlzBIfM3gH5U3kPJFO_KDEPjN0cp-W7A1ZztisQAtKGmASR9CcBom0AD8KcqLlsr-zvUAVhT0tbVkD2TIFder8dn0NkCnj_bT5F3Ce3vwfaWcpL4OFvuLKa5UtcjE9GF-ObeFGU7prnRcRXvtD4WcrkFHZHvKTgSYPrNlXWlPO4nUn4B36ySYaZZqGPvK_kKwRbQDwQHGvN1Vv8li1q-_w8JzxQf-int7Rz19RAia9rOsDG9V6uUMYqD7fLNS3TRH_obVipZkqvJLwAPYbjUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسی آرژانتین را به بازی برگرداند
🔹
گل مساوی آرژانتین به مصر توسط مسی در دقیقۀ ۸۴
⚽️
آرژانتین ۲ - ۲ مصر @Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/447997" target="_blank">📅 21:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447996">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faef8f323c.mp4?token=WecsnWxMvjMflmss_seDQry1iyj-8c6lDHwr__4BwdtYI9XcejVkviU3Z7DDSv1NbZBhK1_dtLL02oT2461VQ1FUFh22um1taQwxlU7IOHz118j0n65lc0fuDXqPdY9RlKYUhSdqRHKAnhh8UY2T9PdKinT0JMioKaEPWnWXR6cK2foTAaqV1G3yHUFEKyKIMy_Ns573CFDT2U6P63PxzFxiBtG-Vr7XEZt69jWbDZ96CD9TXt_e_aVoFRMwE_YA7R5pN3tXxBpwFqXPnQFWpMwCj6TMCz-JzjOAnSo63R_WqWqhSEuyH5bcaEdR-p24t_x82GkFoZkjk_1RzXpIxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faef8f323c.mp4?token=WecsnWxMvjMflmss_seDQry1iyj-8c6lDHwr__4BwdtYI9XcejVkviU3Z7DDSv1NbZBhK1_dtLL02oT2461VQ1FUFh22um1taQwxlU7IOHz118j0n65lc0fuDXqPdY9RlKYUhSdqRHKAnhh8UY2T9PdKinT0JMioKaEPWnWXR6cK2foTAaqV1G3yHUFEKyKIMy_Ns573CFDT2U6P63PxzFxiBtG-Vr7XEZt69jWbDZ96CD9TXt_e_aVoFRMwE_YA7R5pN3tXxBpwFqXPnQFWpMwCj6TMCz-JzjOAnSo63R_WqWqhSEuyH5bcaEdR-p24t_x82GkFoZkjk_1RzXpIxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحبت‌های زائر نروژی-کشمیری رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/447996" target="_blank">📅 21:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447995">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae1c24d01e.mp4?token=qbw22V0X2CEIVr99Pwbmvh4PB5qfCHJNFTZPWl5VVaDYjK4UvH7-_IG7DcJkk49HNMTnYaT7f9vAYaUEqOQK8rfVgbqKUFsskD6Mt5_sn9MwueSrrDeCBMM3Ywh4rihHwznq7Ua-ed3ZXVgTOod001-sc4sQZQKSj8hLvkLGYY9zjzS4p99dZu1fFQPWCjj4UOFgr9HVWtf05zX3SxzTzLRp50lMJs5x303-Yec3g4dnyjEez1mOlvexH8doLpVOqdqTjz5IyIZjl_ssxjS58ge63lZapztnJO7g92V1zDGOGBWhA9YXzGtY9EwSHcIoKobJMwljXcgX8F-vg_LGvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae1c24d01e.mp4?token=qbw22V0X2CEIVr99Pwbmvh4PB5qfCHJNFTZPWl5VVaDYjK4UvH7-_IG7DcJkk49HNMTnYaT7f9vAYaUEqOQK8rfVgbqKUFsskD6Mt5_sn9MwueSrrDeCBMM3Ywh4rihHwznq7Ua-ed3ZXVgTOod001-sc4sQZQKSj8hLvkLGYY9zjzS4p99dZu1fFQPWCjj4UOFgr9HVWtf05zX3SxzTzLRp50lMJs5x303-Yec3g4dnyjEez1mOlvexH8doLpVOqdqTjz5IyIZjl_ssxjS58ge63lZapztnJO7g92V1zDGOGBWhA9YXzGtY9EwSHcIoKobJMwljXcgX8F-vg_LGvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول آرژانتین به مصر در دقیقۀ ۷۹
⚽️
آرژانتین ۱ - ۲ مصر @Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/447995" target="_blank">📅 21:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447994">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f63256cf94.mp4?token=qJ23PZEdaQ5BOS9kC123k27x9F-liWWr0K-saHxQirJzw1DedCe0t89NlN7pIvWwmPgqMzrrt7JrDaOts9MTHqCpjKKHNOats15EoBHzJe8vZl9uEuwmP6Vf8RCUGtWggZA8QF_ELI_BZthgTdc9IhQRPAAzcoCf5ISjvjs1ecYz_1acXylqTd_R9ZXrxYCYTPFjzBHt25oekfpdmrMTx1PVaR89QhzuEUC16MmCl6-wu_8EUeGnffgvpkeVsROtLszOsZd7W51Q16nx36od4XVL9ZVqoy99C53gJikKCoyyJkArOwbM5AV5uSR2xQjS4HFCs3g9FW9aMDhcapaAdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f63256cf94.mp4?token=qJ23PZEdaQ5BOS9kC123k27x9F-liWWr0K-saHxQirJzw1DedCe0t89NlN7pIvWwmPgqMzrrt7JrDaOts9MTHqCpjKKHNOats15EoBHzJe8vZl9uEuwmP6Vf8RCUGtWggZA8QF_ELI_BZthgTdc9IhQRPAAzcoCf5ISjvjs1ecYz_1acXylqTd_R9ZXrxYCYTPFjzBHt25oekfpdmrMTx1PVaR89QhzuEUC16MmCl6-wu_8EUeGnffgvpkeVsROtLszOsZd7W51Q16nx36od4XVL9ZVqoy99C53gJikKCoyyJkArOwbM5AV5uSR2xQjS4HFCs3g9FW9aMDhcapaAdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصر گل دوم را به آرژانتین زد
⚽️
آرژانتین ۰ - ۲ مصر @Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/447994" target="_blank">📅 21:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447993">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f09c78366a.mp4?token=lcgS1nc792Mik7XTJkWbrG_KTNx49C9EbC0gv6TH5iEiEhD4snlV9da8qr2hbCQutS3W3GQF-f7pGChIHc-5nx9l84ACUozkUaNZx8k-5CI5KWvi2dEYLwvsNsug1B-JRwWd7nQgd1rV_Hvx69Nod3gWjzs7_BRXIRNcSCuvSUFBdFtKI0729s7mY2GvB3fvhJjztDS7cr4870J4H5-In9ijFvi7Ddiw3h-TYgeFUbUuYrA4s3xHwd_Qn0Q90QkrvKb8y_3r1UXVF3aNINDjHJff1v79pT9g3-mTtRm0wznY0YQgBd7ip1HoyJsIPcU3Rci3gOzRPrYsFxIW9cfIKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f09c78366a.mp4?token=lcgS1nc792Mik7XTJkWbrG_KTNx49C9EbC0gv6TH5iEiEhD4snlV9da8qr2hbCQutS3W3GQF-f7pGChIHc-5nx9l84ACUozkUaNZx8k-5CI5KWvi2dEYLwvsNsug1B-JRwWd7nQgd1rV_Hvx69Nod3gWjzs7_BRXIRNcSCuvSUFBdFtKI0729s7mY2GvB3fvhJjztDS7cr4870J4H5-In9ijFvi7Ddiw3h-TYgeFUbUuYrA4s3xHwd_Qn0Q90QkrvKb8y_3r1UXVF3aNINDjHJff1v79pT9g3-mTtRm0wznY0YQgBd7ip1HoyJsIPcU3Rci3gOzRPrYsFxIW9cfIKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشتیاق مردم عراق برای آخرین بدرقهٔ رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/447993" target="_blank">📅 21:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447992">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5686de84ab.mp4?token=nlVVXNR5-dbPCdh8_tdku5nCXf8AYq-Nw2ZuLVCnfCOLWtJJiEB8lkVIofBCQ99RgbOaUzNVjImHBMp502i0VkMzF7r5C4JLC6NsGFc7p8eHvdNJ8OHtEUEIp4YGu3uUMpv0Z0DyBVh6o1yXwRQ3wgJpSUy3eMWpU0VhxNNAaL8zRGpGI1Wu6A38NsfyZknmf93mFkcJflY91VaZqG4OwDlSq8fRIroZqrJQDO9BqIYuGG9C1foH4BcUirb1TToAcH52m-1WSB5Cu6Si9nx8P-FsUU_CHaO_DRgIeBhJ5ESAr2oq1lMv-96fKOtY5zIh2jzoeDIGUaD7HQNmNjfgGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5686de84ab.mp4?token=nlVVXNR5-dbPCdh8_tdku5nCXf8AYq-Nw2ZuLVCnfCOLWtJJiEB8lkVIofBCQ99RgbOaUzNVjImHBMp502i0VkMzF7r5C4JLC6NsGFc7p8eHvdNJ8OHtEUEIp4YGu3uUMpv0Z0DyBVh6o1yXwRQ3wgJpSUy3eMWpU0VhxNNAaL8zRGpGI1Wu6A38NsfyZknmf93mFkcJflY91VaZqG4OwDlSq8fRIroZqrJQDO9BqIYuGG9C1foH4BcUirb1TToAcH52m-1WSB5Cu6Si9nx8P-FsUU_CHaO_DRgIeBhJ5ESAr2oq1lMv-96fKOtY5zIh2jzoeDIGUaD7HQNmNjfgGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقا از تهران رفت؛ دلتنگی ماند
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/447992" target="_blank">📅 21:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447991">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2bb01bbe.mp4?token=SgZR0Z-w2p7JpZNty7Tz7u3f5vFpF7LUEsVTx5jfdBoYbpaZx1zTLyjawKH_jslDG3tzp04BHlrpJzl9SHCl4sowzjVoXugglP8gmO5H_uFcyMVebhU06AXH1vQbiiBv6XEKBAJ04n0fmOE8-7oPlH5D8JQ1KVaVynOZYacmZ94fBpkSAzYzIwLqOU-hAEbrFQA6Q_VyS3J9xkBnrIcSwjsJbl93dZmp6jhNpANpPNWyiY4NLpApGxJ_f0nxs6d94AzkWhSd2e9braGR9gTIvGpZTmtHYQ89NXP-12VAwV3GimcrxJaG2c70tfO0OSUYGuc_7iFHdAPJ867YbY5YrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2bb01bbe.mp4?token=SgZR0Z-w2p7JpZNty7Tz7u3f5vFpF7LUEsVTx5jfdBoYbpaZx1zTLyjawKH_jslDG3tzp04BHlrpJzl9SHCl4sowzjVoXugglP8gmO5H_uFcyMVebhU06AXH1vQbiiBv6XEKBAJ04n0fmOE8-7oPlH5D8JQ1KVaVynOZYacmZ94fBpkSAzYzIwLqOU-hAEbrFQA6Q_VyS3J9xkBnrIcSwjsJbl93dZmp6jhNpANpPNWyiY4NLpApGxJ_f0nxs6d94AzkWhSd2e9braGR9gTIvGpZTmtHYQ89NXP-12VAwV3GimcrxJaG2c70tfO0OSUYGuc_7iFHdAPJ867YbY5YrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواپیمای حامل پیکر مطهر رهبر شهید و خانواده ایشان، وارد فرودگاه نجف شد
@Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/447991" target="_blank">📅 21:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447990">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a92aa8d628.mp4?token=akS3wJxdQ89xQfy9UMGCaL6hw3Skw8323YsKgYOkPO3TSl7F_Aa3epeWo5OpJ-GLZcyVYGGRHVZp4WvarBDBWXhdFsLjV83_-m2a2ICRnJkwUUVE7bLiWEvb19ihPfM4zj3Twts3r9iwkxOvSoUU8pfeQ89xXFU_Pvx29rHtARsAHtCw-Wm1D_GTSXQTzvxaPf6X1lPN7O9Leh4u2xln6doZYPmCRAeVh-PXMG1f8cHbUxOE7c0ZWpTizp5jZ8l8_gQHHgDLuLE-YF4jEplONT0-yYDpbs9CPCJ0N-iee1tHDDPbVl0FxgCzRd8kYOgKDNWSwLEn0_YDsCJzEnLhyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a92aa8d628.mp4?token=akS3wJxdQ89xQfy9UMGCaL6hw3Skw8323YsKgYOkPO3TSl7F_Aa3epeWo5OpJ-GLZcyVYGGRHVZp4WvarBDBWXhdFsLjV83_-m2a2ICRnJkwUUVE7bLiWEvb19ihPfM4zj3Twts3r9iwkxOvSoUU8pfeQ89xXFU_Pvx29rHtARsAHtCw-Wm1D_GTSXQTzvxaPf6X1lPN7O9Leh4u2xln6doZYPmCRAeVh-PXMG1f8cHbUxOE7c0ZWpTizp5jZ8l8_gQHHgDLuLE-YF4jEplONT0-yYDpbs9CPCJ0N-iee1tHDDPbVl0FxgCzRd8kYOgKDNWSwLEn0_YDsCJzEnLhyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
آستان قدس رضوی: در خصوص موضوع محل تدفین پیکر قائد شهید، آستان تمامی تمهیدات لازم را اندیشیده و پس از تصمیم‌گیری نهایی توسط بیت شریف ایشان، جزئیات آن به استحضار ملت عزیزمان خواهد رسید.‌  @Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/447990" target="_blank">📅 21:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447989">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76f00a1bf2.mp4?token=Cvx-vBhlzwTyjJr7CTvqCfHYK3z2UKDRT-bMRdu84RE1xO4RGjwtWkMM-eu5bCIhH7uZk7QFs8ZjtTuX0GcsMX6ddfaVW3JsrzN2k_xBSyrFizCSYnH1NTb2EWltJKrE-ggZm3qG7bAXbrekJ25nUNNH5dWd-4FLHS935Kmq13JsLEHvPBiLHjblwQZiVJ1c0b7Zq-61K3krY5XF_vkG82ANQo7ZYgp0uhN-q1Jobz0BSVmlvpNsVbl-s4lagtWtgckD9Yzp71G9PRQX_r0e9EsG2MdrG6qTHwDTAu7BJ2wLbwFDrEt-a7ZiCKUQFzj01jXAxKZRhCh8ItNbDobgrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76f00a1bf2.mp4?token=Cvx-vBhlzwTyjJr7CTvqCfHYK3z2UKDRT-bMRdu84RE1xO4RGjwtWkMM-eu5bCIhH7uZk7QFs8ZjtTuX0GcsMX6ddfaVW3JsrzN2k_xBSyrFizCSYnH1NTb2EWltJKrE-ggZm3qG7bAXbrekJ25nUNNH5dWd-4FLHS935Kmq13JsLEHvPBiLHjblwQZiVJ1c0b7Zq-61K3krY5XF_vkG82ANQo7ZYgp0uhN-q1Jobz0BSVmlvpNsVbl-s4lagtWtgckD9Yzp71G9PRQX_r0e9EsG2MdrG6qTHwDTAu7BJ2wLbwFDrEt-a7ZiCKUQFzj01jXAxKZRhCh8ItNbDobgrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم مصر به آرژانتین با کمک VAR رد شد  @Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/447989" target="_blank">📅 21:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447988">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58ed26b37.mp4?token=dRKDb7SKmjw_8xpIaews64Fq9uGrvj1wmIQtX9GEP45TNOnPqJGBVKE0b7eWn0TrS2FAO6uL7s-ni0OpGSkErQKa_3gBIDIhd6UjkrqgPLR_QrDLRDylC5XPKJhUbeqmqRjSKH_3xeqB-THrWI7QPXAKohamfcQqfWhMoV_PDbysmRx13htdcFgrtpWvBjRW_ak7piWj59xD50s403FqO80Omuok0YWC74A5yBvR-3BkSfND45fEixa-L8TJEudFm0KrWrZYhokJ8qNGdRjCzyCuwQkdCO_jGozjEo0hZsyA9cBOqogDtA2Abb8Y6n-EN_NRct1_WJSupXb0UHSUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58ed26b37.mp4?token=dRKDb7SKmjw_8xpIaews64Fq9uGrvj1wmIQtX9GEP45TNOnPqJGBVKE0b7eWn0TrS2FAO6uL7s-ni0OpGSkErQKa_3gBIDIhd6UjkrqgPLR_QrDLRDylC5XPKJhUbeqmqRjSKH_3xeqB-THrWI7QPXAKohamfcQqfWhMoV_PDbysmRx13htdcFgrtpWvBjRW_ak7piWj59xD50s403FqO80Omuok0YWC74A5yBvR-3BkSfND45fEixa-L8TJEudFm0KrWrZYhokJ8qNGdRjCzyCuwQkdCO_jGozjEo0hZsyA9cBOqogDtA2Abb8Y6n-EN_NRct1_WJSupXb0UHSUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امروز دل‌های عاشق از سراسر جهان راهی قم شدند
@Farsna</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/447988" target="_blank">📅 21:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447987">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d4f9113c2.mp4?token=JrIW0zibhDeDQrFHEwmf88TWGCYv1QuF-jkgS7fY9Jw3vmkUcF55zUBoGVC-CJIq0HaCem_UAmEH7na5hieuyh6GfcQerZwU530-9Q6CMDBdNMahgWpvFcpOEF4xlq7ozhlek5qMESjai5I9l2PnvoQp5nTv40FcKMM9T0MpcfVQrts_IvJubVLeH1yJ_c3DU3WA2IM3F_-tXDH3xI380I4v542ZZSSAuwKBmSJvIz9fD0XqeGwFR_Ka5rPSnoTjNMqr7UmnOrKIQImCGxd-reEjnj2LT7ptp2F5DUcbHd6N1ekbHq1cJdsJ-oQ0VkJKO_3IzqsVZcWKrGDVRzXFHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d4f9113c2.mp4?token=JrIW0zibhDeDQrFHEwmf88TWGCYv1QuF-jkgS7fY9Jw3vmkUcF55zUBoGVC-CJIq0HaCem_UAmEH7na5hieuyh6GfcQerZwU530-9Q6CMDBdNMahgWpvFcpOEF4xlq7ozhlek5qMESjai5I9l2PnvoQp5nTv40FcKMM9T0MpcfVQrts_IvJubVLeH1yJ_c3DU3WA2IM3F_-tXDH3xI380I4v542ZZSSAuwKBmSJvIz9fD0XqeGwFR_Ka5rPSnoTjNMqr7UmnOrKIQImCGxd-reEjnj2LT7ptp2F5DUcbHd6N1ekbHq1cJdsJ-oQ0VkJKO_3IzqsVZcWKrGDVRzXFHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این نماز در حافظهٔ تاریخ ماندگار شد
@Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/447987" target="_blank">📅 21:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447986">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbc3fd34b6.mp4?token=CV5w1pId1lrIcsfRgv18hLra1YV2AcyC-2KTX-l1q3UBmK6tBS1s6taH3JlaylAT1dIn_Mg-N8jYM2OEsVu3QD7rySlGpi4LNuD29_YZZ0mWrRzrEHQ1T8J2vsjR0HxXU5BHWjKyP_B43zw3vR4SotBs7qYkVuuQW1iS790ToiGSK_OIoHPcS5T30x62d_2XjTCRkXVDZsz6FlWtuZmcNCVBovI3FBORcKTsXb2qxh3J1Wv69_GllnbTp7vI92y8uz6qtfdTVka2dHGnaOqYhS_6-mAp5eu97khnC5mjSckRYuYhrHvoSA2IkzbQPvl1z3jtqC7hiXqIiTbWgMI5VUY9C1F_XGbS0zipJjdhEsBuuRTLzrnk27_15_xbpSp2b2vS4PNsY6sU-q1H4E8RWTdpzf_o-Wt9FQuzzt5q_PEm24OIG4FOZh886jniHzV5T0g4GzlvbaCTZk8wnYXaTJ6LOCJ5O0OBI7s8ZiVB0-yxybzaqb6d-nuRueOhKJNz6WH454qtDoqtaAKFeBDpx7_CCYwANP1YfMrOhq90QX0Zu8hZnrWcBA-0VYjSOAAcND3ZQrRI7HGoxgWgiEVDR1Urhn2S5PDdDAA5permrzRsFRSprCWycmFqCig-DHam0zVzVsX31rZdjB1nS4BFomGqCIcyVXspGd52HieYxtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbc3fd34b6.mp4?token=CV5w1pId1lrIcsfRgv18hLra1YV2AcyC-2KTX-l1q3UBmK6tBS1s6taH3JlaylAT1dIn_Mg-N8jYM2OEsVu3QD7rySlGpi4LNuD29_YZZ0mWrRzrEHQ1T8J2vsjR0HxXU5BHWjKyP_B43zw3vR4SotBs7qYkVuuQW1iS790ToiGSK_OIoHPcS5T30x62d_2XjTCRkXVDZsz6FlWtuZmcNCVBovI3FBORcKTsXb2qxh3J1Wv69_GllnbTp7vI92y8uz6qtfdTVka2dHGnaOqYhS_6-mAp5eu97khnC5mjSckRYuYhrHvoSA2IkzbQPvl1z3jtqC7hiXqIiTbWgMI5VUY9C1F_XGbS0zipJjdhEsBuuRTLzrnk27_15_xbpSp2b2vS4PNsY6sU-q1H4E8RWTdpzf_o-Wt9FQuzzt5q_PEm24OIG4FOZh886jniHzV5T0g4GzlvbaCTZk8wnYXaTJ6LOCJ5O0OBI7s8ZiVB0-yxybzaqb6d-nuRueOhKJNz6WH454qtDoqtaAKFeBDpx7_CCYwANP1YfMrOhq90QX0Zu8hZnrWcBA-0VYjSOAAcND3ZQrRI7HGoxgWgiEVDR1Urhn2S5PDdDAA5permrzRsFRSprCWycmFqCig-DHam0zVzVsX31rZdjB1nS4BFomGqCIcyVXspGd52HieYxtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاش بی‌وقفه جوانان عشایر عراقی در دل شب برای استقبال هرچه باشکوه‌تر از رهبر شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/447986" target="_blank">📅 21:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447985">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2f0s3vqRIVEGJRxRQbHnegaUbXX1l5h-uQrp0UcQPAJd98zf2wnFwJDx45T10aRLJdm2VBKIWWNv1q82wHzhMRzrReT608ipNYo2u0IdzfFwGfUrz3TJ1Aptgp_5pPxvbnOVzOP1SYgTYKq8P4cUUUoi-25Dhhik9SFsSpJQxlgVRsEY2UkJwsI8Kx06-KDnm8WUiX_jn5y76deWmwysOxTG6eSc1o3reJRuCq5kDs-FFVebYRjqNL_jYIQVxL65jY778jMN4Aiid_kCGDlmH6jgBI1K5Ga2AUMRPCk_IiRdB_pWzMh0r5pKjROVvxlP820kceqEImIHey0B3Rj7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: به فروش اف-۳۵ به ترکیه فکر می‌کنیم
🔹
رابطهٔ ما با ترکیه بهتر شده و ترکیه از خیلی جهات، بسیار وفادارتر از کشورهای دیگری بوده که فکر می‌کردیم به ما وفادار بمانند. @Farsna</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/447985" target="_blank">📅 20:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447984">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92c2e88cb.mp4?token=tE5bjerELOP2xa53TOPN_Lt51ZHETWLoXoT3jruzpMX9Pv4BWLyicwZ4OrdQPOyrcM7GfN2ntjD3MNoldIgUNHpng55vvyBTEBum1OnLhBvhgXdVQYmUiYZKUfkfR4cpWkDFfrIo3c4V4WwNVrO-JFabncPGZaYvq6gJrxqX6lFqw1Gf2c7HyZ4rMMED-nUQSOcN38_0ysU_721gA74uk2lChKb6-D2wENzHUq4-jNyvboZ-niKTSEzUNfc5ntcsaI2M3qn6GWDGfuylIUeYgwtciyvi-UZQ2wlBhi5qNJVNo4eilrYqxRP7gsvIIOXkJvl-umPhkUF_M6O8pa8bDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92c2e88cb.mp4?token=tE5bjerELOP2xa53TOPN_Lt51ZHETWLoXoT3jruzpMX9Pv4BWLyicwZ4OrdQPOyrcM7GfN2ntjD3MNoldIgUNHpng55vvyBTEBum1OnLhBvhgXdVQYmUiYZKUfkfR4cpWkDFfrIo3c4V4WwNVrO-JFabncPGZaYvq6gJrxqX6lFqw1Gf2c7HyZ4rMMED-nUQSOcN38_0ysU_721gA74uk2lChKb6-D2wENzHUq4-jNyvboZ-niKTSEzUNfc5ntcsaI2M3qn6GWDGfuylIUeYgwtciyvi-UZQ2wlBhi5qNJVNo4eilrYqxRP7gsvIIOXkJvl-umPhkUF_M6O8pa8bDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول مصر به آرژانتین در دقیقۀ ۱۵
⚽️
آرژانتین ۰ - ۱ مصر @Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/447984" target="_blank">📅 20:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447983">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbb4602b4c.mp4?token=bjiQK51iJYQS6kevfzASvarOSKJcCZPHwYLvXnk97R2oVESyoitRPe3UMioFTtZAVNZotVdd10wCR7FdjP1FlEGOSpHbNTnWkaAScHhp3tL96eD9aPyjS0XeYK9ktN7EKmpPtgtoXbdwKj3d2XHquR3JbovKmFL6rN4YXXaQYIL9svzhIDuIP3mZRCxpUVhzHZK0rMrUE3Wj3pLgBh4YuuVTIcPfsJBBo93Sj2YmRTIhf7D0VJFKiVWjTCCfawRxfN0TT5fpWaO6rzTTwX6CS78VjhU6wuFBL0Tj9GqqW0ltkFlDQRMCyXxtKW-Lx-aj-l9PyQJgzt0WcMseOM4BGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbb4602b4c.mp4?token=bjiQK51iJYQS6kevfzASvarOSKJcCZPHwYLvXnk97R2oVESyoitRPe3UMioFTtZAVNZotVdd10wCR7FdjP1FlEGOSpHbNTnWkaAScHhp3tL96eD9aPyjS0XeYK9ktN7EKmpPtgtoXbdwKj3d2XHquR3JbovKmFL6rN4YXXaQYIL9svzhIDuIP3mZRCxpUVhzHZK0rMrUE3Wj3pLgBh4YuuVTIcPfsJBBo93Sj2YmRTIhf7D0VJFKiVWjTCCfawRxfN0TT5fpWaO6rzTTwX6CS78VjhU6wuFBL0Tj9GqqW0ltkFlDQRMCyXxtKW-Lx-aj-l9PyQJgzt0WcMseOM4BGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسه‌ای که رسانه‌های خارجی نتوانستند انکار کنند
@Farsna</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/447983" target="_blank">📅 20:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447981">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e75b8ebc9.mp4?token=YBjN_9YufsBec-mA4BTAfDU1h3hGtejEtYSUstjzoWA89DOWjZc1iMUTpnX9fNk3SiPe6SQ83EXYcW2ZMXZxhMutzvSW2uBsxxKIx6RJkYpnsRcnpZkJQEb3Mt4O42XvT9IQmMIEJ_nHSAQhnKr83_jKfxkst0s2lDYpFgzKYcdpmwtO8Z74VI_-wN6CCgp_PsctkRVUkHrK1SItj8k9yHQyTYUjT95YhQGpaa4tT3Xt7tY815Vfh25yCd54ymHcqKyZYL2qLxg_rQfF67Xg5yeOgBzfsL08zP3zGK8TYJ1dLvijH2nJ5aSktekaAam5WTKATG7hERoK6It89Quc8xw8b3uD3Zy2xhkljudkr92gNEpWpTT9ifnatndl5fq2Sx6fSeGucElO5AaLdhuUd8FuE7oCr81a6JPzBtU-v6sNMeklhcN-tFMRvpLnZD4gqc0oRS9zibBNMAyPEngUTK9_zYY-aiypKvcCdz1zJAF29nFqpPxbofBGvEA8I6UjOA1MH_NHIYr5IsEkdN6iQNjVD1jMPx5Tco-4xdTABDcIxnrtr4Kv-qw1Li2K65DCzwwkk7SCwtRtqa4_Kui376P5XlJOPSPxyagNxhYCKyn3DximdYXtoEYbi4Tzqq2FUG6x9utzPRs6KTQil-OaH0u9rt507fTRsLYnalYqYyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e75b8ebc9.mp4?token=YBjN_9YufsBec-mA4BTAfDU1h3hGtejEtYSUstjzoWA89DOWjZc1iMUTpnX9fNk3SiPe6SQ83EXYcW2ZMXZxhMutzvSW2uBsxxKIx6RJkYpnsRcnpZkJQEb3Mt4O42XvT9IQmMIEJ_nHSAQhnKr83_jKfxkst0s2lDYpFgzKYcdpmwtO8Z74VI_-wN6CCgp_PsctkRVUkHrK1SItj8k9yHQyTYUjT95YhQGpaa4tT3Xt7tY815Vfh25yCd54ymHcqKyZYL2qLxg_rQfF67Xg5yeOgBzfsL08zP3zGK8TYJ1dLvijH2nJ5aSktekaAam5WTKATG7hERoK6It89Quc8xw8b3uD3Zy2xhkljudkr92gNEpWpTT9ifnatndl5fq2Sx6fSeGucElO5AaLdhuUd8FuE7oCr81a6JPzBtU-v6sNMeklhcN-tFMRvpLnZD4gqc0oRS9zibBNMAyPEngUTK9_zYY-aiypKvcCdz1zJAF29nFqpPxbofBGvEA8I6UjOA1MH_NHIYr5IsEkdN6iQNjVD1jMPx5Tco-4xdTABDcIxnrtr4Kv-qw1Li2K65DCzwwkk7SCwtRtqa4_Kui376P5XlJOPSPxyagNxhYCKyn3DximdYXtoEYbi4Tzqq2FUG6x9utzPRs6KTQil-OaH0u9rt507fTRsLYnalYqYyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امروز مردم قم آخرین دیدار را با آقای شهید داشتند
@Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/447981" target="_blank">📅 20:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447980">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd17f74433.mp4?token=ejspwi2sPgBMrITTfAo6ys4dsofZ2gOqj-fJwa4v7L4O1i0LYVK4GXwSQ0T9AQTVDEQO3sQ5pUllAZ0dpuHm4BDjIKLThi8HAHSsVh9P3Sjl2LM9PyaYCskrivzG1WRFW0I7kpJGY-EQyz7JkscVfgSc2uqbj76l4OH48b9tzdbpkm32B75L-X6UwpojAo-rWcAHitQH9J1FTBNRfi2bJRPu-Y0TEpFsEDAQyh6pAgS_6EXuTJEBR-5NnaiJ5VzYVbUegGBFSabhwzO6dYY3a7wxknN6zGmSi0wXn49C4BIhSvICWCtRDOp3lKgZahAGa3qpFNXv9Y3ln2MT-VmqoIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd17f74433.mp4?token=ejspwi2sPgBMrITTfAo6ys4dsofZ2gOqj-fJwa4v7L4O1i0LYVK4GXwSQ0T9AQTVDEQO3sQ5pUllAZ0dpuHm4BDjIKLThi8HAHSsVh9P3Sjl2LM9PyaYCskrivzG1WRFW0I7kpJGY-EQyz7JkscVfgSc2uqbj76l4OH48b9tzdbpkm32B75L-X6UwpojAo-rWcAHitQH9J1FTBNRfi2bJRPu-Y0TEpFsEDAQyh6pAgS_6EXuTJEBR-5NnaiJ5VzYVbUegGBFSabhwzO6dYY3a7wxknN6zGmSi0wXn49C4BIhSvICWCtRDOp3lKgZahAGa3qpFNXv9Y3ln2MT-VmqoIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موکب‌‌داران در مشهد آمادۀ پذیرایی از زائران رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/447980" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447979">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15dd3f7562.mp4?token=rcKdpis9lv5HiY4w1_TKrg-jYpFsf_LkYlXfttMq4MgDlAOKATI3sOG0tpinQ0tmne9PBck14PzJeamPyN8sl6Llp8rpDKzBVPlygn2qzOiAlAp6UUhGkQXJy7fUtQNgnsZbX5Ds6SMPyrHLThqjWC9gBHaQk7KGTv4CbRadATU8_umPwzYvtbdyliZOmvwxIlS0PqB0M_Gsorbw4l-N7LkWtHIBiD8WOcJY7rPihvS9T4WBUt-lSOjlsJrkVZ-wyRVqYNe4TCRzws-YNTdA1d-aoRnQdnaHODNY4KYZlA6ITDsduxL7Dh50osWIWr1b3tbbtNix-7hoYOYf7gjQTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15dd3f7562.mp4?token=rcKdpis9lv5HiY4w1_TKrg-jYpFsf_LkYlXfttMq4MgDlAOKATI3sOG0tpinQ0tmne9PBck14PzJeamPyN8sl6Llp8rpDKzBVPlygn2qzOiAlAp6UUhGkQXJy7fUtQNgnsZbX5Ds6SMPyrHLThqjWC9gBHaQk7KGTv4CbRadATU8_umPwzYvtbdyliZOmvwxIlS0PqB0M_Gsorbw4l-N7LkWtHIBiD8WOcJY7rPihvS9T4WBUt-lSOjlsJrkVZ-wyRVqYNe4TCRzws-YNTdA1d-aoRnQdnaHODNY4KYZlA6ITDsduxL7Dh50osWIWr1b3tbbtNix-7hoYOYf7gjQTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: به فروش اف-۳۵ به ترکیه فکر می‌کنیم
🔹
رابطهٔ ما با ترکیه بهتر شده و ترکیه از خیلی جهات، بسیار وفادارتر از کشورهای دیگری بوده که فکر می‌کردیم به ما وفادار بمانند. @Farsna</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/447979" target="_blank">📅 20:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447978">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70aeb849f.mp4?token=Zn1D7i-04fHBOvH3G4hHB0WW0l_c30aHSs1If-8wF0Qz5R1XFLdqXMPSwm_cIbVc_FhKD2athC5LIW1TXBUVtYC6DYU0ZCyQ4HlVVeuUSAB2Y6muPMPXJ4ysQJO9CQHxFjg-VKHJfSLLWbr4PUt1LnQdOwnJuaILy8iHIVDAgTKg1cpjHy5SdOxagXZ78ueJi5YjMlPt2X3s0b2sQ51jkk6CnPtGqIOWKQao9pnnFQ7lYoWuM2op_c3q2btQL9Grns52nMsqwXni5XgTeCImVDivUH5IkvBepNBXmQoKXoOU1NvrcgL-hmpWs1kV6X_Bz-ZpKNL34tGdN4gwHHkFMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70aeb849f.mp4?token=Zn1D7i-04fHBOvH3G4hHB0WW0l_c30aHSs1If-8wF0Qz5R1XFLdqXMPSwm_cIbVc_FhKD2athC5LIW1TXBUVtYC6DYU0ZCyQ4HlVVeuUSAB2Y6muPMPXJ4ysQJO9CQHxFjg-VKHJfSLLWbr4PUt1LnQdOwnJuaILy8iHIVDAgTKg1cpjHy5SdOxagXZ78ueJi5YjMlPt2X3s0b2sQ51jkk6CnPtGqIOWKQao9pnnFQ7lYoWuM2op_c3q2btQL9Grns52nMsqwXni5XgTeCImVDivUH5IkvBepNBXmQoKXoOU1NvrcgL-hmpWs1kV6X_Bz-ZpKNL34tGdN4gwHHkFMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یحیی قاسم، عضو شورای فرهنگی انصارالله یمن: یکی از مهم‌ترین اهداف رهبر شهید ایران در موضوع یمن، شکستن محاصرۀ یمن بود
🔹
مردم یمن به برادر خود، ایران، تکیه کرده‌اند تا این محاصره را بشکنند. @Farsna</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/447978" target="_blank">📅 20:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447977">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18d5597dad.mp4?token=tp17VZQ0CA-M7JMP2om31nYzU2yKHXfHvV9hIUDNXyEholjHFnOJHQkGYQSm5Wi96X6i9qAvgJl46aNKG2NwjFBwyzFnBRgLXdT6aSpFNqxz4EidD0GFJNfG-KyxbOs-kfW8XFS2ofyKk4Py0sFdNZlWueSntQbkz69PAeUGVeh_U5mkmvnb_Kk1Sp15GtOGhAKm3n8updvbV0Q4EYgb1KHEttOJNV6AYD5qdHDYqNCHK-re5pgV_dLgCXXsKTBUjQgjaeXIdwITHfnuAM2nxRUxCSFJL3A0bQhH3r2yysluIBwZS1yHtJFwNFkJnqiCp1N7TZZncd7OErg4pQdR1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18d5597dad.mp4?token=tp17VZQ0CA-M7JMP2om31nYzU2yKHXfHvV9hIUDNXyEholjHFnOJHQkGYQSm5Wi96X6i9qAvgJl46aNKG2NwjFBwyzFnBRgLXdT6aSpFNqxz4EidD0GFJNfG-KyxbOs-kfW8XFS2ofyKk4Py0sFdNZlWueSntQbkz69PAeUGVeh_U5mkmvnb_Kk1Sp15GtOGhAKm3n8updvbV0Q4EYgb1KHEttOJNV6AYD5qdHDYqNCHK-re5pgV_dLgCXXsKTBUjQgjaeXIdwITHfnuAM2nxRUxCSFJL3A0bQhH3r2yysluIBwZS1yHtJFwNFkJnqiCp1N7TZZncd7OErg4pQdR1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دختر عراقی ۴ روز قبل از تشییع برای خدمت‌رسانی به تشییع‌کنندگان خودش را از ناصریه به موکب‌های نجف رسانده و رو به پدر مادرها می‌گوید فرزندانتان را برای تشییع بیاورید.
@Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/447977" target="_blank">📅 20:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447976">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2a4596c0.mp4?token=E-5F_qCgz-dO1FbRfOyeSLhlav_J7qXZWegD1F6S73LN412W_vy2qsQwXsDFmQfhb5rWoyKmApr_pOp7rYNw2_hdXzpzSDaNZ-_Q9cIF7QxVE2FBvhKqSiVk_a04Rp5RnmAMiShYXoUeky-G-VnSMKu6TDBuYIpsu35zZzgCTYHsbpyq_IXnSKwHMfyBKdhAEBL37eeUJm5KIylQ14BhK3ti9EvTsh88XsdBHKH5gUrHsW0zzmjNeLGld-14QeKLV5Hd5N9V8sbD5iwJSKd9_W2ElI7IV0MxOF0VdXzwzrwbAwuqaDwyqR38-NAS5FB3Z5eiEeChTUzKyIVSGvwmRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2a4596c0.mp4?token=E-5F_qCgz-dO1FbRfOyeSLhlav_J7qXZWegD1F6S73LN412W_vy2qsQwXsDFmQfhb5rWoyKmApr_pOp7rYNw2_hdXzpzSDaNZ-_Q9cIF7QxVE2FBvhKqSiVk_a04Rp5RnmAMiShYXoUeky-G-VnSMKu6TDBuYIpsu35zZzgCTYHsbpyq_IXnSKwHMfyBKdhAEBL37eeUJm5KIylQ14BhK3ti9EvTsh88XsdBHKH5gUrHsW0zzmjNeLGld-14QeKLV5Hd5N9V8sbD5iwJSKd9_W2ElI7IV0MxOF0VdXzwzrwbAwuqaDwyqR38-NAS5FB3Z5eiEeChTUzKyIVSGvwmRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودرویی که قرار است در عراق حامل پیکر مطهر رهبر شهید باشد
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/447976" target="_blank">📅 20:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447975">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e0d8feab.mp4?token=j960xYbJ1T4a6CeO80Vjnri2Rbu64wMdqO7JyFgSbA49RjRwJpiOkzebRxMsLTIlgx2Gsm3Z210CO4ETBIFyCrlwjPN1T3x062wkxDo6aIa95O9xbwmhVGATbTBDS7xdzngAea2d0aXVRlxoYNyn-KSJ37FdmyyI_PDrMapF32oB7gDsae7dimq7KH94bPd-w0M1Mi-oPWtHzmh-EkQTESbhCDU0YDdLAMWadJObwVaYa8sWaL_pnf_190qU37TCFjdQW4eLA9tGbOfFkvRmYrCsgX_HP11wP0nNs4ByR8WzLYwWK5yPpsJAPC9TyIPy-nwqvGSOzruazMWoqfBzXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e0d8feab.mp4?token=j960xYbJ1T4a6CeO80Vjnri2Rbu64wMdqO7JyFgSbA49RjRwJpiOkzebRxMsLTIlgx2Gsm3Z210CO4ETBIFyCrlwjPN1T3x062wkxDo6aIa95O9xbwmhVGATbTBDS7xdzngAea2d0aXVRlxoYNyn-KSJ37FdmyyI_PDrMapF32oB7gDsae7dimq7KH94bPd-w0M1Mi-oPWtHzmh-EkQTESbhCDU0YDdLAMWadJObwVaYa8sWaL_pnf_190qU37TCFjdQW4eLA9tGbOfFkvRmYrCsgX_HP11wP0nNs4ByR8WzLYwWK5yPpsJAPC9TyIPy-nwqvGSOzruazMWoqfBzXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: اگر عربستان یک‌بار دیگر حریم هوایی یمن را نقض کند پاسخ همه‌جانبه می‌دهیم
🔹
صبح امروز (جمعه) ساعت ۵:۲۰، چند فروند جنگندۀ ائتلاف سعودی با نقض حریم هوایی یمن تلاش کردند مانع فرود یک فروند هواپیمای غیرنظامی ایرانی در فرودگاه بین‌المللی…</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/447975" target="_blank">📅 20:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447974">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a5827943.mp4?token=bm3LhHdMGqhH4ouA0otYZv15POJemjSDgcO1xELR4DzDud_D9X7kHBHYNHgiIScl1JhIpnq4QfTCWl93janCFl5KCTeyMPD3Li_E6IZaW84MXjlTC0ZIBMFeVGn1Q671xBEdKtXfBXEiIGDFfCEZelseAEOgj9yFUNgv0wwzcaimmVpWvTVx3HJUEIYHLkd_IoKN3JnAqip4NKEkAKZD3z0zZH9QdkNPLRnFWJ_KDa0or15AEGu3IQFe0p8XQ2inyvXSLddncXq-t3Wnyo5BAUHuIj8Bbk8xHNNT9KkEuW3RQxwCKmRPEkaO5WYLJuaeeg_MQ-h0HQGRlYwK0mRm4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a5827943.mp4?token=bm3LhHdMGqhH4ouA0otYZv15POJemjSDgcO1xELR4DzDud_D9X7kHBHYNHgiIScl1JhIpnq4QfTCWl93janCFl5KCTeyMPD3Li_E6IZaW84MXjlTC0ZIBMFeVGn1Q671xBEdKtXfBXEiIGDFfCEZelseAEOgj9yFUNgv0wwzcaimmVpWvTVx3HJUEIYHLkd_IoKN3JnAqip4NKEkAKZD3z0zZH9QdkNPLRnFWJ_KDa0or15AEGu3IQFe0p8XQ2inyvXSLddncXq-t3Wnyo5BAUHuIj8Bbk8xHNNT9KkEuW3RQxwCKmRPEkaO5WYLJuaeeg_MQ-h0HQGRlYwK0mRm4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراحل آماده سازی صندوقچه شیشه ای حامل تابوت رهبر شهید در عراق
@Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/447974" target="_blank">📅 20:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447973">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00947cfef.mp4?token=bTys1SHMFZp0mLtzuHmA4Ofz0Xv2bwehZUM2XXjAjT2o4V3eur1jsr9w-x92ZZIcFfm1N8AgV6Jh28ysX-yWOVEtyr8ibJxewx3PJHWZll_-Okpcp8gTczmP1Z-ru_ClFzDjnkeELYrjXE6kBPLLaVK7u8mlvDIS5yMY6sC88okQorY13moVDue-az8xN86oBaBuDtbBi9nz7HkCkK0oDnHeYI8VUJM-HkQQxy_mjNPiIIZj3NylNU9iArpdjx8LyXDz824av2yIBO-YUKiH4-BMzgNZ1HYxXIrOal5hSDQyT2IrCSJ5JmqTOtv1QnTklGtLBfMAsr8DT3_PLr_vLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00947cfef.mp4?token=bTys1SHMFZp0mLtzuHmA4Ofz0Xv2bwehZUM2XXjAjT2o4V3eur1jsr9w-x92ZZIcFfm1N8AgV6Jh28ysX-yWOVEtyr8ibJxewx3PJHWZll_-Okpcp8gTczmP1Z-ru_ClFzDjnkeELYrjXE6kBPLLaVK7u8mlvDIS5yMY6sC88okQorY13moVDue-az8xN86oBaBuDtbBi9nz7HkCkK0oDnHeYI8VUJM-HkQQxy_mjNPiIIZj3NylNU9iArpdjx8LyXDz824av2yIBO-YUKiH4-BMzgNZ1HYxXIrOal5hSDQyT2IrCSJ5JmqTOtv1QnTklGtLBfMAsr8DT3_PLr_vLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعید حدادیان: مردم با پرچم سرخ حاضر می‌شوند تا به همه نشان دهند که خون‌خواه رهبر خود هستند.  @Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/447973" target="_blank">📅 20:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447972">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3198a22e34.mp4?token=WilEX5NI9mfFSLXPAgmFE-t8C59A5r7ada8t2roziO9Mbt18ITA8JhL5nmn895R72ruf0XOJ2AmpubJpm4bfmQxUu9iNopFqH5KIxp9jahHVyfvFF7HxJ9RNA4hUWY-qZqFnUCh0Rhmn0XvCKvG_NyjWrJO9ts04UYRPTO8BtpyjlZaZWPQPZGWjaTqt_-5CjwiBhzl2rs0-of500Ko8j6I5_0sHQ74f5DDz3QwaYODuYEh85PkEl6lZxZ99VW7CsxagJ11Q9POR7lwTgNpErYN0Q8BEyH8qsr5NH7QdKo0MbEzftyQuHnbc9YHhLAbNgiN1XB3bm9JR0Y_syxARQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3198a22e34.mp4?token=WilEX5NI9mfFSLXPAgmFE-t8C59A5r7ada8t2roziO9Mbt18ITA8JhL5nmn895R72ruf0XOJ2AmpubJpm4bfmQxUu9iNopFqH5KIxp9jahHVyfvFF7HxJ9RNA4hUWY-qZqFnUCh0Rhmn0XvCKvG_NyjWrJO9ts04UYRPTO8BtpyjlZaZWPQPZGWjaTqt_-5CjwiBhzl2rs0-of500Ko8j6I5_0sHQ74f5DDz3QwaYODuYEh85PkEl6lZxZ99VW7CsxagJ11Q9POR7lwTgNpErYN0Q8BEyH8qsr5NH7QdKo0MbEzftyQuHnbc9YHhLAbNgiN1XB3bm9JR0Y_syxARQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعید حدادیان: مردم با پرچم سرخ حاضر می‌شوند تا به همه نشان دهند که خون‌خواه رهبر خود هستند.
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/447972" target="_blank">📅 20:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447971">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b592877158.mp4?token=OL2YJcSFrAuDGLFudvSm2_nklOH0Q42agNCLRWYA8A2j6BXlgK5ISjAUk2YOQyJ0HpNfVCBYwBnNmnk9qn4k8ODe2XdAPqoM2SBqOMKcwLSfU-NGDsVqP4bsgq82khi2_k66yDCnmzXD7_CsyMUH8TUz-z5SBeGvrFF3LyGATDnc2vVBHMHW2p8eKlDMrLvgGir-ugdo8ftZZoWmm40VURDEXtzuJsXDFVKavGYVVQm2nKv3rVSj_I8Q1RpvkUC_JG2JlK5MZGmmfIZmvgK5odwh27PtYVOFykwRQFMYg3A08aUiphTdBLViynG44Sb23wKzGfdYKV-wv_JpIKXYZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b592877158.mp4?token=OL2YJcSFrAuDGLFudvSm2_nklOH0Q42agNCLRWYA8A2j6BXlgK5ISjAUk2YOQyJ0HpNfVCBYwBnNmnk9qn4k8ODe2XdAPqoM2SBqOMKcwLSfU-NGDsVqP4bsgq82khi2_k66yDCnmzXD7_CsyMUH8TUz-z5SBeGvrFF3LyGATDnc2vVBHMHW2p8eKlDMrLvgGir-ugdo8ftZZoWmm40VURDEXtzuJsXDFVKavGYVVQm2nKv3rVSj_I8Q1RpvkUC_JG2JlK5MZGmmfIZmvgK5odwh27PtYVOFykwRQFMYg3A08aUiphTdBLViynG44Sb23wKzGfdYKV-wv_JpIKXYZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی ورودی حرم امام حسین(ع) برای تشییع پیکر رهبر شهید  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/447971" target="_blank">📅 20:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447970">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e687be21dc.mp4?token=j3NIBngAU5S3twxoKGzOTsRMUwiLIvyOPv0B7Ug89jPUf3GmtjY0aLgbd5AdEGayN8v1SdboaPXXGy6wstQZAAl-BGShv8_JpVRg84DqUW_iZts793RsyVMuxPk7kOzzVcCsW_t7ozGmqBx0xz_JVyPMGqW8GuriSavUXMy2l0UvAOkuBLjjNKDeqW9PqTEK42x-InRXKt9HHLEd-_bn9He3BctN356JDIg7xvJNYjVEic_oUkDpqjf9PIpcL4taD1bMe2AzhtvAuQbLLpyi5STrr3wrbln2X5olQOPnF3vkXvW44Jn9bHf2ijuKXj0ACEg2a8xDMPtouUI3BYqz_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e687be21dc.mp4?token=j3NIBngAU5S3twxoKGzOTsRMUwiLIvyOPv0B7Ug89jPUf3GmtjY0aLgbd5AdEGayN8v1SdboaPXXGy6wstQZAAl-BGShv8_JpVRg84DqUW_iZts793RsyVMuxPk7kOzzVcCsW_t7ozGmqBx0xz_JVyPMGqW8GuriSavUXMy2l0UvAOkuBLjjNKDeqW9PqTEK42x-InRXKt9HHLEd-_bn9He3BctN356JDIg7xvJNYjVEic_oUkDpqjf9PIpcL4taD1bMe2AzhtvAuQbLLpyi5STrr3wrbln2X5olQOPnF3vkXvW44Jn9bHf2ijuKXj0ACEg2a8xDMPtouUI3BYqz_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هر قاب، نشانی از یک شهر و یک روایت از انتظار مردم عراق برای رهبر شهید امت اسلام
@Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/447970" target="_blank">📅 20:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447965">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XPCZoOrnMieTqv9c2Bn2SZEqf_dWl4QYnLbFr1hRwdrm0bnlQE_erDW0CGmH2Elr-6u5S38fwTUfSt9opxrydHeIzyqQXRr7lxk2ECVCGitTd8vkR8u3a15wFexTWFoRWzgYI_Ypv15OEnTEnIcQxc9fRQ-RWVfMKE0_TQRaUsdkypJXdpcdtbDhAFoFyn6oMnb9NXxg66_2rbXdTl-QJJIJB32xzM4o-WAkWd0JCZ3I1Yl_Bv5ni78nHsDQpu9Rn6GgzfZ9E3_8f-cAJnT4QONKVQCzAU2h4A6c4DkR3-ONMmgCHI2RJnixCvMqiKZtrNrFA8fBAG_SJkvcfw7Cww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qfk5OWUdFPfOuxuZRlI-Cxe4gZJyWRcuAEsCFzfah1jeP4D34cfuGLjFvI-NG_EUYtbQjFC9It6aDFWh1wyXnZP-KCVX9wLpo2LXgGKSYIvvNgIuYDL_3DQJJbTrJwz9P_JgN7CSWRrTlePZHw2UjJqsjBnZYr1ZOpENURp4GB7qrXJE9mmrYjVaWYUX2xeQ2ZFf-4a5pasvAGDZ8XhLPrblleNAMnr0wXQ8i-_FM0f6lEdcHsTEzPT2qAFPUS91q8X0E4ShPrsm0bJ4loz3cE6HuG07J9fojBvlwEYoglkSp5NF3nM11of6seuwqoK1wGI_qcwX6G-utMmU3YFt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxhnEwSLYITdfyNQMsnEYribmZPtmLMmAU6P3r_vtzfBQpQ26QfatR7O6cK5tUFWaGqKf9QbnJ75CiQCLaQcKclApxmsd4IV-ejd4bQSUbN79f_6FhYm8RSMEtfHDkGEHieov0qDW2s-5yTkopKvqpfVEp69GX6_MZ2RE-ujVivLf7wNUrAcyM1B2vFENC1XXwzIwV7BpZexCpU_hiGyGF6gRfOPOznCZZIzFbiPl6ux_aPGHnthrNwfSq9KOIRVigW1HF6Eh8eGGZxYhcfr6vKB9W3WZPjT4P5WvBBlqpUEYZbcabxV5B6oJvwZwIocyw8hWQamgMcPo5E6CrnyvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbZtULvNl8DZKw89CUkAcWgPjVKZYj9JRGZeJo-3SBwm4CM02yp6uJJkW1_F49K0MN4JVkE8hdvJPuuKelYXkWWH0n-0_OCyFMausLbf4o1QaYNZpGXgnpQ9cSifrAE2yQkYmq0k-0tEIaHgYapEjWsJqaoR6bkWMOSdTDBXHWt6_ZxpqwzO3j3vsPhDrXj33qqrM5NnHpJjyZJ9U9XkKFEWKGfabDjGK-dn_7gMBWcvK_ZWqYE5hEHriYBEo1Ra-n-ELHE30JrdCWU92ijJwbGag1V26fbM42JVtxON3CN6LB-30B1KuQjQRqtAmIRVQHNy3vUhWq-Nz9hZVCN6BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/adsNI3t2gUCRdA5_9hy6TL4_NpwClglLOqMZKf7sQFtGJFCSZnujTShdgU2rlth_m1W0HxUGGR27AkE0VlXd0mP4wO-OdLamjuR-U9SXcv8iDLmCCOV0xQZCY1M5s-FrkVFA42HPIcRmV4aLIcf3uXhZIdF7msz5DEa6uikIEGMLcJRPISG0ZspW69cLeojhk30XC4os-lo8Npj1Wdx8i-sj37HSihnnMqOy7YldQGymxznRxhMt2Dg7vO0AV9pS34-h7asmDLd5i3hTtmz9GbgFzolLPx7aWdd6vRBt-GZ_jGaVIsfWqlDVjYQYuS0ouZv20SVKsBfAK9Xo2p7Lmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرچم ایران در دستان عراقی‌ها در بین‌الحرمین
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/447965" target="_blank">📅 20:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447964">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حادثه برای یک نفتکش در سواحل عمان
🔹
سازمان تجارت دریایی انگلیس اعلام کرد یک نفتکش هنگام عبور از تنگۀ هرمز، در سواحل عمان، هدف پرتابه‌های ناشناس قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/447964" target="_blank">📅 20:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447962">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/273a807c5b.mp4?token=Zzg4xh58u-UJDxNyE_aGHmqOhCFLp7VM9iIuMwMniD5WATwsd1_7VRe9FF_cEpLAmu-WqcONIErEk_ZB-N5fi9pdcSi0n2Fl28L30ECqeN24uYivU03YkhUz1hqrbC7CrNfWcuqcdBeOKarlRrlKf2FTFvLF6TDJF8tBmPUrVJqnrBkE5YewltNydy2H-W6KhO7sxn9yYxz_o5sMZ6me6W-QLaGY8cWukwJ0F2A4Hq8EYQSwqf55IWuF2PILSYrLgt8z8DR9bhWXweYAplrpqCTDww0VACoBAYZofl8ruiFpfFRQ6iU-i6nEzeMvcLLskbXFmCKwwioS30mSGZXEsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/273a807c5b.mp4?token=Zzg4xh58u-UJDxNyE_aGHmqOhCFLp7VM9iIuMwMniD5WATwsd1_7VRe9FF_cEpLAmu-WqcONIErEk_ZB-N5fi9pdcSi0n2Fl28L30ECqeN24uYivU03YkhUz1hqrbC7CrNfWcuqcdBeOKarlRrlKf2FTFvLF6TDJF8tBmPUrVJqnrBkE5YewltNydy2H-W6KhO7sxn9yYxz_o5sMZ6me6W-QLaGY8cWukwJ0F2A4Hq8EYQSwqf55IWuF2PILSYrLgt8z8DR9bhWXweYAplrpqCTDww0VACoBAYZofl8ruiFpfFRQ6iU-i6nEzeMvcLLskbXFmCKwwioS30mSGZXEsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از طلبه‌ای که در نظافت خیابان کمک می‌کرد تا کودکی که با پخش سربند خادم تشییع آقای شهیدش شده بود
@Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/447962" target="_blank">📅 20:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447961">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efadf61825.mp4?token=VXvTtxPOxtWzb941tvd91E2Ir2NlC8R8WOfHzVU40muX87wt52CwvGzosexwoahE5bYoXJ38VJjwBefNxiMZGaSS7UCu7qR8nXReEOWPRelrp25fuXAOezejHd7TRzq-Lq5Da6OXIct-ITTNA1IoD0VkwpVXxeY6R-BHwXzVo8ueM1OTrQ4QN58iLaEwfT-pOA-4OjhXKq4pq_69H2h9oHVMiuuGoxr2P40_70rFVoLcVjq6VePHHgV53xDs8n93X6G2Terkyewf5FP-5MrryxmIIs0Dc7AZZu9a36st4xRCh2hWgH4kNx211UCwcbxsY7JBxNZFxB2hI26D0ffFVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efadf61825.mp4?token=VXvTtxPOxtWzb941tvd91E2Ir2NlC8R8WOfHzVU40muX87wt52CwvGzosexwoahE5bYoXJ38VJjwBefNxiMZGaSS7UCu7qR8nXReEOWPRelrp25fuXAOezejHd7TRzq-Lq5Da6OXIct-ITTNA1IoD0VkwpVXxeY6R-BHwXzVo8ueM1OTrQ4QN58iLaEwfT-pOA-4OjhXKq4pq_69H2h9oHVMiuuGoxr2P40_70rFVoLcVjq6VePHHgV53xDs8n93X6G2Terkyewf5FP-5MrryxmIIs0Dc7AZZu9a36st4xRCh2hWgH4kNx211UCwcbxsY7JBxNZFxB2hI26D0ffFVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول مصر به آرژانتین در دقیقۀ ۱۵
⚽️
آرژانتین ۰ - ۱ مصر @Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/447961" target="_blank">📅 19:53 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
