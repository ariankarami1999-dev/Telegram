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
<img src="https://cdn4.telesco.pe/file/of0VlTGJj4q3skly5DxL0aqL_DkXW4JU5FPgvO0OHZ3RH_7o6JF9ZaGqqd2WapoGsSOB7PN7A3LJJJ9UJpEtqDUpwF2QCguzQKyTQamkdVg01Fx5QaFc7fuJUuo_7toiMQAFlyQc6kffiuRbFLs46XT1RHQalhfrGCgnuKX64ff4s-bkdW8tO99-MoAuZF67pr0ryxUpeWad9PPem6YgTlkUdYfhVfRMIjizrTvMwrWUuhb-UeMzLKvmq9t5JAx_O8vgbXFbx9nkXGnLJESvlk1FPcDujOrwonWNEW4sCvFCH67fUOOBvOh_hftrn9l86RrKiUY8P7J6Ax-5Dkirog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 18:26:48</div>
<hr>

<div class="tg-post" id="msg-136207">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
میلاد محمدی در یک غافلگیری با عقد قراردادی یک و نیم ساله به  مکس لاین ویتبسک بلاروس پیوست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 218 · <a href="https://t.me/SorkhTimes/136207" target="_blank">📅 18:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136206">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
قدوسی: ابوالفضل رزاق‌پور گزینه اول جانشینی میلاد محمدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 368 · <a href="https://t.me/SorkhTimes/136206" target="_blank">📅 18:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136205">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nBvxG6dZajQuhRE1P3np3c8Kh6ElXo9dEGTuKF6ZaU_srhgxLAUFOCWzXvnI_p7SLLZz8h6towPe43FabMTnMpVH9aFGbgXKaWCSTW5UuwABBZt-185Hgro7YAJcokgwK6NXi_4QqZQFi_H1LxumijcRjCBzYzdwm1FH9pANvWTVocfo-Q4d-tZwhFdHQcoKDFXjlgT0Ow-Hxqar3UXjBQQTuf7Qv__0YlAkFNGRgKCHwbjaTBJZEefIl28e72dbbTwgRih7nVD0c8qTBBl0mu_uHpFPaCHTnR7qJu_aP3UwPKN2tRt7QT8W8TOt_Y-C-o5EO9rLJtjLHqt9eP2T8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
قدوسی: ابوالفضل رزاق‌پور گزینه اول جانشینی میلاد محمدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 819 · <a href="https://t.me/SorkhTimes/136205" target="_blank">📅 18:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136204">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
میلاد محمدی در یک غافلگیری با عقد قراردادی یک و نیم ساله به  مکس لاین ویتبسک بلاروس پیوست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 819 · <a href="https://t.me/SorkhTimes/136204" target="_blank">📅 18:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136203">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUWrH_cZTYXA0dq3ERy5tMPkwcUncitKQ-vo7IWb5GllWuya48Yob_5IS73QaCQf4T1hqJPLlYC3fGRTyYkEyPFc9Wu257_RiwllG5hvYp7LUHwo8Jjumkkn8L4s1XmO81_006oTmTKm19Zwf0bCLz_KzixvUROMmlt_lazIz1Zo8a74QsqXMqai6yXDX4cd0Bp5mo1ArpQ2IyT2P9_5FyI9Joq-lE7YhakwSHFazj31zyIWhvnfA29zcgIR1vb9PbBMuRtDsZj_U3nWzZlRWtg1Pt0iWbdHXAV19qj0ptDk-BCC4tzZYWxqBUxHwd-vMyu1Dg6711mc6TLeWEvUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
میلاد محمدی در یک غافلگیری با عقد قراردادی یک و نیم ساله به  مکس لاین ویتبسک بلاروس پیوست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/136203" target="_blank">📅 18:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136202">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🏅
خب میلاد محمدی هم ترجیح داد به جای پرسپولیس به لیگ بلاروس بره
❌
رسمی؛ میلاد محمدی مدافع سابق پرسپولیس با قراردادی یک و نیم ساله به  مکس لاین ویتبسک بلاروس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/SorkhTimes/136202" target="_blank">📅 18:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136201">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0DJluDGxuKWzkBZgPVJKGEuj0NgnPPol-mSu4feMWpwWycyHzyoaTP5RWJR2ACLU7euUeuln14eMf9PVIJt1Y2V9F1C5vPnXVBGJ8lnkw9O9Rk_DiEKkwk62y0_Zt8JY_ufckaL8ymvqUO-upVGf7IxoOqAus7fO7EgOB5LqDgGyl0WSHEV8lVaRteqCSE_0w63ZJErUV0003_vfaJjfGBD75-0XcRhFqcE85VvPy9WuJ_H6TU62snAbhLnC4yMDCr5qxAvki7v4_ojjz8eQAtxfoU71qrWFSrBQa8FbHFsKqmXOfK3wDBhz2-4PbgBMDua9Xdrs7Cgu5_6D49zsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
خب میلاد محمدی هم ترجیح داد به جای پرسپولیس به لیگ بلاروس بره
❌
رسمی؛ میلاد محمدی مدافع سابق پرسپولیس با قراردادی یک و نیم ساله به  مکس لاین ویتبسک بلاروس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/SorkhTimes/136201" target="_blank">📅 18:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136200">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
غیررسمی: محمدرضا اخباری با قراردادی 1+1 ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SorkhTimes/136200" target="_blank">📅 17:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136199">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❗️
❗️
درصورت عقد قرارداد تیم پرسپولیس با آلن هلیلوویچ این بازیکنان جانشین سروش رفیعی در این تیم خواهد شد. پست اصلی هلیلوویچ هافبک تهاجمی - بازیساز است اما در پست وینگر و حتی مهاجم نیز بازی کرده. احتمال عقدقرارداد زیاده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/136199" target="_blank">📅 17:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136198">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
✅
از تمرینات پرسپولیس خبر رسیده دنیل گرا را در پست هافبک دفاعی و دفاع چپ در حال تست هستند اگه جواب داد بمونه!
🔴
گرا برای جدایی درخواست مبلغ ۵۰۰ هزار دلاری کرده مدیران پرسپولیس برای اینکه غرامت ندن فشار اوردن گرا بمونه اما تصمیم آخر مهدی تارتار میگیره
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/136198" target="_blank">📅 16:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136197">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❗️
آمار افتضاح تیم ملی والیبال در لیگ ملت های امسال :
🔴
12 بازی
🔴
3 برد
🔴
9 باخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/136197" target="_blank">📅 16:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136196">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaAgCryjL06snA22Q3RI8B525fSpoMmssGdAa1kUX8A7RGN23E2pfmJ-tqMz-trX5pdxfxTVzHWCvShKQa9_w1slEc6IbQ4_PIQ4RsKyGB7mmxwK-k_Ov8AST37qGIndeGMOc6VDDMIW4X3k4ixwr1Npcr7BpkFle8jH8H_6y9bXLGYnpIR2Yk7pldoyzAom5MlYEwjwiSDU73k-q5iTwkAPfg3G10qZ_1Ytp-fJRzmSatHd25tORxHJp2XGR6qx-c-jS5e1A5A7jkT--8GtvCQ2NQhx7EuGQJQ5fBD9wNpkgucRVH_7EyLMPsdgiVa89MqNaR6Eu90S82eiHsQ6kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رقم قرارداد دانیال ایری،‌بالاست، ولی می تواند قرضی به پرسپولیس بیاید. او بند خرید دائمی در نیم فصل دارد و بنظر می آید نساجی مایل به فروش کسری طاهری است. ضمن اینکه جذب علی نعمتی و قریشی هم قبلاً کنسل شده بود
✍
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/136196" target="_blank">📅 15:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136195">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
فرهیختگان: پرسپولیس دنبال مشتری برای بیفوما و گراست؛ گرا مشتری ندارد و بیفوما فقط در صورت آزاد شدن خواهان دارد. چون قرارداد بیفوما ۸۵۰ هزار دلار است، احتمالاً پرسپولیس باید برای جدایی‌اش غرامت بدهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/136195" target="_blank">📅 15:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136194">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
برای جذب طاهری مراحل قانونی ش باید از طریق فیفا پیگیری و استعلام گرفته بشه که منجر به بستن پنجره نقل و انتقالاتی تیم نشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/136194" target="_blank">📅 15:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136193">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❗️
❗️
شنیده می‌شود شروط پرسپولیس برای هلیلوویچ نیز با موافقت این بازیکن همراه شده و احتمالاً او در اردو و تمرینات سرخپوشان در ترکیه حاضر خواهد شد.یکی دیگر از چالش‌های پیش‌روی باشگاه پرسپولیس با آلن هلیلوویچ بحث شرایط خاص و فورس ماژور در قرارداد او بود که ظاهراً…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/136193" target="_blank">📅 15:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136192">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136192" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/136192" target="_blank">📅 14:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136191">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tn6_JJtrBs-6yvZPDx9FON7N4w_BLddEZnXPvtd57wqC-px1oEioETtPrupPqLlrPMNnUU9NTg6Q-ztF6yot2bSwYUhUA7sf8Ffy9owF3SJp9CAlp9MoL6bCTFvnbzFUl86d7Vi4VHjYmV4Veoe-X0mpayahTpNyPCcIflR3tpvgEn-z8p13ztmPDBOTmC-HoVGw0ACWqHh5O5PqineZaI9_cENFkixtSVMo06-8Kmv10nyZiPSo1jPIJWRsGq-POgrbhK-cvJ2q_tVJDdcI4YnjGMbEwF1bKicao7eVssRWxINPXQ5EShvhCL9C-orpkojeELg7jvzK2qHXFI6pvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
فینال فوووق جذااااب
آرژانتین
و
اسپانیا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
▶️
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/136191" target="_blank">📅 14:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136190">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
صنعت نفت آبادان با برتری 2 بر 0 برابر نیروی زمینی در رده سوم جدول رده بندی ایستاد و حریف مس رفسنجان در دیدار پلی آف لیگ برتر شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/136190" target="_blank">📅 14:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136189">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
مصوبات جدید سازمان لیگ فوتبال در مورد نقل و انتقالات در فصل آینده:
🔴
افزایش لیست بزرگسالان هر تیم از 20 بازیکن به 21 بازیکن
🔴
افزایش لیست زیر 25 سال هر تیم از 2 بازیکن به 5 بازیکن
🔴
افزایش سهیمه لیگ برتری هر تیم از 7 بازیکن به 11 بازیکن
🔴
کاهش تعداد بازیکنان خارجی هر تیم از 8 بازیکن به 4 بازیکن
🔴
افزایش تعداد بازیکنان نیمکت نشین به 23 بازیکن (هر بازی 3 بازیکن زیر 21 سال باید روی نیمکت باشد)
🔴
این مصوبات هییت رییسه سازمان لیگ است و برای تصویب و اجرایی شدن آن راهی هیات رییسه فدراسیون فوتبال شده تا پس از بررسی تصویب و ابلاغ شود. همچنین گفتنی است این مصوبات تنها برای لیگ 18 تیمی قابل اجرا خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/136189" target="_blank">📅 13:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136188">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
غیررسمی: محمدرضا اخباری با قراردادی 1+1 ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/136188" target="_blank">📅 12:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136187">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔹
🔹
تارتار هنوز درباره‌ی جهانبخش و قدوس نظری نداده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/136187" target="_blank">📅 12:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136186">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⏺
قرارداد محمدرضا اخباری به خاطر این که بازیکن آزاد هست قراره به صورت بازیکن آزاد ثبت بشه و مشکلی برای سهیمه لیگ برتری پرسپولیس ایجاد نمیکند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136186" target="_blank">📅 10:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136185">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
آخرین وضعیت نقل و انتقالات و شرایط باشگاه پرسپولیس از زبان رضا جباری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136185" target="_blank">📅 10:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136184">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
معاون وزارت ارتباطات : با اشاره به تجربه قطع اینترنت در جریان جنگ اخیر کشور به سطحی از بلوغ رسیده که حتی در شرایط بحرانی و التهاب شدید نیز میتواند بدون قطع اینترنت مدیریت شود و دیگر شاهد قطع اینترنت نخواهیم بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136184" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136183">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
تسنیم / جزئیاتی از مذاکره پرسپولیس با بازیکن سابق بارسا، 2 شرط برای عقد قرارداد
🔴
🔴
باشگاه پرسپولیس ابتدا از هلیلوویچ خواسته تا در اردوی این تیم در ترکیه شرکت کند و کادرفنی پس از زیر نظر گرفتن این بازیکن، نظر نهایی را درباره کیفیت فنی او اعلام کند. در صورت…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136183" target="_blank">📅 10:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136182">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
پروفایل ترنسفرمارکت هالیلوویچ، این بازیکن 30 ساله به احتمال زیاد جانشین سروش رفیعی در پست شماره 10 خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/136182" target="_blank">📅 10:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136181">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05254735f5.mp4?token=OB8rSfGRQKUXdY2Ru81bOCekq8dQmHVmNkBRb-WjFgKLfyC4d9aRJ3PVsll_DX9-tvuBkMqLNJ9y-DEefJSIzgfcWRJYwDB20KVGhyq5VemACn3Mr0j7lFmBt9kDKMMUF4W-Bme5ta0Ccl0w7Arn_I9PRsUS9S-SOUHTG-O----IskJdCJvO8Y3h3JJIqO_YtL3oeFR5yEPKopFrF0NmPypJb6Psf8KR2QJfkLnnZV_XTjEUex68I35xPl9cbNIqjbq808Q9ZIs9T0jHbZE3PVOOPb5lKV0DHA2gWLkTjtypYxd2rpfOUPApXagOryVHXeQ26DW99JuJBznuWrBf4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05254735f5.mp4?token=OB8rSfGRQKUXdY2Ru81bOCekq8dQmHVmNkBRb-WjFgKLfyC4d9aRJ3PVsll_DX9-tvuBkMqLNJ9y-DEefJSIzgfcWRJYwDB20KVGhyq5VemACn3Mr0j7lFmBt9kDKMMUF4W-Bme5ta0Ccl0w7Arn_I9PRsUS9S-SOUHTG-O----IskJdCJvO8Y3h3JJIqO_YtL3oeFR5yEPKopFrF0NmPypJb6Psf8KR2QJfkLnnZV_XTjEUex68I35xPl9cbNIqjbq808Q9ZIs9T0jHbZE3PVOOPb5lKV0DHA2gWLkTjtypYxd2rpfOUPApXagOryVHXeQ26DW99JuJBznuWrBf4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جواب تامل برانگیز جواد کاطمیان به سوال اینکه چرا ازدواج نمیکنی: دنیا پرظلم و پر کثافت، پر از آدم کشی، پر از بچه کشی؛ ازدواج کنم که چی بشه اخه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/136181" target="_blank">📅 09:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136180">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
شنیده ها: پرسپولیس برای جذب محمد مهدی محبی نامه زده به باشگاه اتحاد الکبا تا اگه بشه این بازیکن رو از تراکتور هایجک کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/136180" target="_blank">📅 09:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136179">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🏆
فیلم خلاصه بازی فرانسه 4 _ 6 انگلیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/136179" target="_blank">📅 09:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136178">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
مذاکرات مثبت پرسپولیس با قدوس/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/136178" target="_blank">📅 09:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136177">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
شنیده ها: پرسپولیس برای جذب محمد مهدی محبی نامه زده به باشگاه اتحاد الکبا تا اگه بشه این بازیکن رو از تراکتور هایجک کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/136177" target="_blank">📅 09:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136176">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
فرانسه نابود شد .گل چهارم انگلیس به فرانسه اونم تو یک نیمه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/136176" target="_blank">📅 08:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136175">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9y74V1OGCknEjnM88S3TXy8yIDJyuX0HIgjjUVL_lVspr45hsKdCpXvvMxodwvww7nchYex0xNFH5pd2UMqWOQC9MpRNu4N_W6dJpD1EEBNBRq4wpxkC-eWi8592IiQypunEDa0Iv-I5e5Vja4Jujm5ccZ6WnIOHxsY8L4Cw7smF59jMI0c1hajdrBOUgPFZ5HD6MXJ27pjqTxxMB7eOuG6rFZlZLYB03f7SgqxMFVr4-BCWFCYmP-fJJXLEfuHSa7LNJNx2Mp4Z4YMLleiPngJNprd2TqVK1peFpKM1qv0BGTZbi5gWgEZ1n8nVZsix8HIwKESKex0w5UQGRtFuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس ممکنه زندگی نده، ولی
شادی میده
عشق میده
اینه داستان سرخ...
❤️
‌
سلام صبح بخیر پرسپولیسیها؛
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/136175" target="_blank">📅 08:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136174">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136174" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136174" target="_blank">📅 02:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136173">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6w7ZdYS9TP_YyNmyEXwS-rNxARkmu_thUKApTt7sSqUcBe__dCQq9n7PvJK8_Ah1fxW4NRzd-eWugTsU0ljgCYfs4ZU7tjACn38y9cCspOGpwLvWev8zwYy7RUgdB06u7c52ApdUAvPR0oitU0tm-HAJhLIfCuWIOgatFg_OmfbY6mlzMmxbGJWzTAHPHdSIjnXvGru7ucJRqaMvUmd_M_Sbdpwk6Ou7uEHkq-eCsewaV-BynPn9gY6HxvRyVUpkLP_D20dI_FLjproJzIBEVXBElEj4ucubP8-batEX0JLDHlphKaqoX_j6I0N1szncmI143cbsl0QNx2vhB59mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136173" target="_blank">📅 02:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136172">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
✅
فرانسه داره تحقیر میشه ..گل سوم هم زد انگلیس ...فرانسه حتی میل به سوم شدن هم نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136172" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136171">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
❗️
پس از منتفی شدن لیموچی و یوسفی ، مهدی تاتار خواستار جذب محبی شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136171" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136170">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
انگلیسی که با تیم دومش اومده گل دوم رو هم زد به فرانسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136170" target="_blank">📅 01:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136169">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
گل اول انگلیس دقیقه چهار به فرانسه زده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/136169" target="_blank">📅 00:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136168">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136168" target="_blank">📅 00:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136167">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
❗️
ورزش سه: محمدرضا اخباری فردا می‌ره باشگاه پرسپولیس و دو ساله می‌بنده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/136167" target="_blank">📅 00:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136166">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
امشب ساعت 30 دقیقه بامداد بازی رده بندی جام جهانی انجام میشه ...پیش بینی میکنید کدوم تیم سوم میشه ..فرانسه یا انگلیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/136166" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136165">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
غیررسمی: محمدرضا اخباری با قراردادی 1+1 ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136165" target="_blank">📅 00:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136164">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❗️
❗️
کاظمیان تا این لحظه راضی نشده بره گل‌گهر/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/136164" target="_blank">📅 00:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136163">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
✅
باشگاه پرسپولیس به اخباری گفته فعلا با جایی قرارداد امضا نکن، به عنوان بازیکن آزاد جذبت می‌کنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/136163" target="_blank">📅 00:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136162">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
👎
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس برنامه ای برای جذب بازیکن خارجی وجود نداره،و حتی در صورت جدایی گرا و بیفوما!
💯
تارتار از شرایط باکیچ،اورونوف و سرگیف رضایت کامل دارد،و اگر گرا تخفیف نده احتمالا ماندنی بشه…</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/136162" target="_blank">📅 23:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136161">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فووری از رومانو: آلن هالیلوویچ، بازیکن سابق بارسلونا و فصل پیش فورتانا سیتارد در آستانه امضای قرارداد با باشگاه پرسپولیس ایران هست. مذاکرات در حال انجام و روبه پیشرفت هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/136161" target="_blank">📅 23:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136159">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
پروفایل ترنسفرمارکت هالیلوویچ، این بازیکن 30 ساله به احتمال زیاد جانشین سروش رفیعی در پست شماره 10 خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136159" target="_blank">📅 23:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136158">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
پروفایل ترنسفرمارکت هالیلوویچ، این بازیکن 30 ساله به احتمال زیاد جانشین سروش رفیعی در پست شماره 10 خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/136158" target="_blank">📅 22:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136157">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
پروفایل ترنسفرمارکت هالیلوویچ، این بازیکن 30 ساله به احتمال زیاد جانشین سروش رفیعی در پست شماره 10 خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136157" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136156">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
❗️
کاظمیان تا این لحظه راضی نشده بره گل‌گهر/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/136156" target="_blank">📅 22:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136155">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2H67P0sbbbENSWwP6vVnQU47s9bOkY1v_81DdBzoegMRntOE6kBDhv1bDj0UdsDBR4On4VfXPeFWkCTdb9SYMiWc5VmlLx2qU2ePxn8EGKmilzK4-WrevvY2onTqyu5pYUo36sg_gk82wIWhsHWUokfO43qZ9PrwXVC0Vd0xU43Xodz7CuhvRoLg7fMT4e-yVH1-vr6z9VciW2fqirsosPLOdr5ECgGQyZ9d1gASpax0TD_ZIYHAQ5NA2VrnIbw_nUsOs8JzQgLneF22m0GaMLOqEFHwTJmEasrqL5uOhvA1FbOqBC429jSCRYO7YoFU9vQJjpvpXAorHTXLwsONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پروفایل ترنسفرمارکت هالیلوویچ، این بازیکن 30 ساله به احتمال زیاد جانشین سروش رفیعی در پست شماره 10 خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/136155" target="_blank">📅 22:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136153">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فووری از رومانو: آلن هالیلوویچ، بازیکن سابق بارسلونا و فصل پیش فورتانا سیتارد در آستانه امضای قرارداد با باشگاه پرسپولیس ایران هست. مذاکرات در حال انجام و روبه پیشرفت هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136153" target="_blank">📅 22:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136152">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXab0DFIJUeNq3_taUDIRsJ2Ptdgm3HbHoJaHgbwbuuLLe16oLFPtEnRIrUMPvcMkToRunY_6YPu2jbcJXn5DgZEF_yiVbmVwolL_O9WtolJWYsEvdF4qY9wCVm3gncQUn0HYomrNunATY1i3IU3eptV2sG1fIefJ_D4BhsHO-4EzfDTFrjdCtIdP3JbmJFXIGuTa3AFjyfzUqY9O4u7CmQBGPy_YBXxsCgYp_3u4gOQumH1Bi4KpW1vbA0t7zgUlUe2UoyP67VoybnDs2a4pEf77eRtUIV4dv7MBY3USedCN4E-x6LYx-5IFP1rfq3mtwLmBzyV0TbIU8ZxkCc7Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/136152" target="_blank">📅 22:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136151">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/136151" target="_blank">📅 22:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136150">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
✅
تارتار روی تمدید قرارداد میلاد تاکید زیادی داره/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/136150" target="_blank">📅 22:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136149">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
فووووووووووووووری
⏺
باشگاه اجازه ورود به تمرین رو به کاظمیان نداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/136149" target="_blank">📅 22:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136148">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
🇺🇸
ترامپ:
❗️
دیشب جزیره خارک رو زدیم ولی به نیروهامون گفتم نفت‌ش رو نزنید ممکنه بخوایم جزیره رو تصرف کنیم چون از دستشون کاری برنمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136148" target="_blank">📅 22:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136147">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
🚨
حملات در جنوب کشور شروع شده...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/136147" target="_blank">📅 22:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136146">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
داورهای بازی فینال و رده‌بندی جام جهانی مشخص شدند و علیرضا فغانی در هیچکدام از این دو دیدار حضور ندارد.
❌
بر اساس اعلام فیفا، اسلاوکو وینچیچ از اسلوونی دیدار فینال جام جهانی بین اسپانیا و آرژانتین را قضاوت خواهد کرد.
✅
همچنین ژسوس والنزوئلا از ونزوئلا،…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136146" target="_blank">📅 22:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136145">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
فوووووری از رویترز: ترامپ از کشته‌شدن دو سرباز خود توسط ایران شدیدا عصبانی شده و دستور شلیک قدرتمند در ساعات آینده را صادر کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136145" target="_blank">📅 22:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136144">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم خواهد خورد.
❗️
❗️
درباره کسری…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/136144" target="_blank">📅 22:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136143">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
شهاب زندی: پرسپولیس برای زارع که تو ۵۰ تا تیم ملی نبوده یک میلیون دلار پول داده اما برای دو ملی پوش ما میگه گرونه مقصر من نیستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/136143" target="_blank">📅 21:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136141">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
#تکمیلی؛محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود///خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/136141" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136140">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lg2B4ThxExA5mdQS3eTXai41yfWUCJATL72_hxsak9RyyFff7d2D1OTXstEnT2Pttxe7GjJKoAtkojMOxqPJpSAgAJ3HoCVdzfkUbOOC1qgmttZp-sOZQqlnNdCtowys8M_D55jAVuvsSCuKY2GBh2X3Lo8gZf8OGn_Q5XaK6n-kgZOUQVo0-_YZswj7sFZhiQKLEpHUXtOT-mpEPsaAV6OYotAIS1w9QeQdySEvd1lUNbU9Jrlu0H3OKEcjqWrT18UACuId-Sw200fct6imGrfgSPcAzSR5Vdtg52rILMIdVIH33CGjxYgeqYFFTS_2w9dLJurMEIKO411pTb4vig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136140" target="_blank">📅 21:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136139">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
جلسه با مدیران نساجی برای انتقال دانیال ایری به پرسپولیس در حال برگزاری است / قدوسی
✅
تایید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136139" target="_blank">📅 21:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136138">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
با اعلام سنتکام، دو سرباز آمریکایی در حمله ایران به اردن کشته شدند و یک سرباز نیز مفقود شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/136138" target="_blank">📅 21:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136137">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
فوری/ سنت‌کام:
❌
دور جدید حملات از الان شروع شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136137" target="_blank">📅 21:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136136">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه ، وقتش نرسیده که از فوتبال دیدن پول در بیارید؟
😉
✅
@FuckBet</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/136136" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136135">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XDoSOUjv2lNF1fGTvde12wFEFd2uh89H307-_xlgxMiFpNpYnvWL8fdiNjxL3khEIOP4LsqNuHEJj2_21f-9nZmr1aQOgpcoCkGp6m1NA8ls0Hx-B78hs4iYRKLlhO5AvlDky2x1BRQQLEZ6NWoUWkvIVEDsN3ZVqRs_wbpJ2Siu31IGVjS8odvCOV2WrQHvndbblEXn75vuRoBlIS-zzJWjyfHOvCgEuWdFMdzSbrK6LI6gTaEPxnuSKNXUNaYvtI4U_5sjoXXDGcNZ99Bv9VvfFTNGlehwzHdwFsJhIC4QFT6AReIZ9XDq6vC2R7xOuVts3uRtwwzzCQbkYOFDSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
Ⓜ️
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136135" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136134">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
دانیال ایری هم خیلی یهویی یه استوری گذاشته و نوشته صبر راه رسیدن است…
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136134" target="_blank">📅 20:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136133">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❗️
جلسه با مدیران نساجی برای انتقال دانیال ایری به پرسپولیس در حال برگزاری است / قدوسی
✅
تایید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/136133" target="_blank">📅 19:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136132">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
❌
🔴
دفاع راست ها :
✅
عیدی و تیکدری و براجعه
🔴
دفاع چپ ها :  محمدی و جلالی و معامله گری   نظرتون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/136132" target="_blank">📅 19:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136131">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔹
🔹
جلسه با مدیران نساجی برای انتقال دانیال ایری و کسری طاهری به پرسپولیس در حال برگزاری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136131" target="_blank">📅 19:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136130">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
سامان قدوس؛ بمب بعدی پرسپولیس؟
🔴
🔴
ورزش سه: پرسپولیس برای جذب سامان قدوس هافبک ایرانی اتحاد کلباء امارات درخواست داده و این بازیکن در لیست خرید سرخپوشان قرار گرفته است.
🔴
🔴
قدوس که سابقه بازی در لیگ برتر انگلیس با برنتفورد و تیم ملی ایران را دارد، یکی از…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136130" target="_blank">📅 19:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136129">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔹
🔹
فووووووووووووری
🚨
حدادی و نیکفر مدیرعامل سپاهان امروز تلفنی صحبت کردن و مدیرعامل سپاهان تاکید کرده به هیچ وجه به پرسپولیس بازیکن ( لیموچی ) نمی‌ده و انتقال ابرقویی هم به سپاهان منتفی شده/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/136129" target="_blank">📅 19:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136127">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
فوووووووری
🔴
🔴
شهاب زندی: من به سرتیپ طاهری پدر کسری عزیز و خود کسری برادر کوچک تر من قول دادم بره پرسپولیس اما مدیران پرسپولیس به دروغ میگن گرونه. برای زارع تو ۵۰ تا تیم ملی نیست ۱۸۰ تا دادن اما برای کسی که ۲۳ تا تیم ملی مبلغ خیلی کمتر از این نمیدن
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/136127" target="_blank">📅 18:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136126">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
غیررسمی: محمدرضا اخباری با قراردادی 1+1 ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136126" target="_blank">📅 18:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136125">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136125" target="_blank">📅 18:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136124">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❗️
نوراللهی با دو نفر در باشگاه و تیم صحبت کرده و گفته که من مشکلی ندارم و می آیم ولی باید با کلبا توافق کنید /
قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/136124" target="_blank">📅 17:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136122">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
#ورزش‌سه : ممکن است به زودی یک قرارداد معاوضه به اضافه پول نقد بین دو باشگاه پرسپولیس و سپاهان شکل گرفته و احتمال دارد نام‌هایی مانند محمدامین کاظمیان، حسین ابرقویی و آریا یوسفی در این معامله جای پیدا کنند. حتی احتمال رخ دادن این اتفاق برای محمد عمری نیز…</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136122" target="_blank">📅 17:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136120">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⚽️
عبدالصمد ابراهیمی؛ کارشناس حقوق ورزشی:
🔴
جذب کسری طاهری برای پرسپولیس بسیار خطرآفرین و باعث محرومیت این باشگاه از چند پنجره نقل‌وانتقالاتی خواهد شد/ طاهری حداقل تا نیم‌فصل باید در نساجی به میدان برود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/136120" target="_blank">📅 16:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136119">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1FG8ZSGej-lNasDZBRwVgugDZRgK77hSXyfEsfG6EDJP6XHeV5TJSSGsYsyyLr3hrHxk2quZnQ8fyN6QW8NRU0IKV0NR-H2-W8nFofocbPp88HPWXoeVhoVuZZi90vvBlXDxgvWhFtQJpZM3TmyAT0DODpuMkEur7BH78CDrR6glQcQnuynnnN2S0Ag1xp7saUPVlPrg8LoqdbDMlKHEmkE5cng_SrHYMX1hrSMTEqSMnic6cpw524IKTMHXiHR6wahZpBElFDgcn_i3pbqeZxqzfcI1tWYYIcb-hQ5IOqmqbzhzbUeDu07g2SETdsmEyvasxM5VfRX-rx9pE2LjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
مذاکرات تیم پرسپولیس با اتحاد کلباء برای جذب سامان قدوس آغاز شد/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136119" target="_blank">📅 15:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136117">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
کوشکی و اسلامی توسط ترنسفرمارکت بازیکن آزاد اعلام شدند
🔴
از طرفی ایجنت هر ۲ بازیکن با ایجنت جلالی یکیه
👀
نظرتونه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/136117" target="_blank">📅 15:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136116">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136116" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136116" target="_blank">📅 15:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136115">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136115" target="_blank">📅 15:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136114">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
شبکه "فاکس نیوز": نیروهای ویژه ارتش آمریکا سال‌هاست که برای ورود زمینی به ایران آموزش می‌بینند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/136114" target="_blank">📅 15:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136113">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
غیررسمی: محمدرضا اخباری با قراردادی 1+1 ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136113" target="_blank">📅 15:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136112">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/136112" target="_blank">📅 15:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136111">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUsClCr5U3Nnop-CVcUcYtvS3FKb0qACTV1PaX3kxwdIesjyDhU_XKgGZD-AfbhQ0MLWSLrUXDeM4wq2KaygnatCfIwlQD4oxwPHVYualz0pWx_gLCv6ur_LwXsXrt1XSSkqvj17CSMTn5Z2XrccZ5SzF7vCmEzVGyi7bL7Y5_LrO21i-MfLdxBUh5yE6RUTqr-gUWlGCqa7PFojgrdHuBYiGorLHf9oqRhIrx6JFTs0q9PmT4Oa0rb0-sicuq-Gtcr92ffRRslisEceXd_A-VWyrKx2j_R5hJiBQMSB21ALKsHCbMMMhmlpcA3qTkAzg5sCFly6N6ky6CUx1M3PFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
غیررسمی: محمدرضا اخباری با قراردادی 1+1 ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/136111" target="_blank">📅 15:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136110">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/136110" target="_blank">📅 14:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136109">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/136109" target="_blank">📅 14:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136108">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
ورزش سه: بازوبند کاپیتانی پرسپولیس مدعی سومی هم داره و اون کسی نیست جز احمد نوراللهی که در آستانه بازگشت به پرسپولیس قرار داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/136108" target="_blank">📅 14:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136107">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔹
ممکن است دنیل گرا و تیوی بیفوما در پرسپولیس ماندنی شوند!
🗣
گرا در پست دفاع چپ و هافبک دفاعی تست شده
🔹
بیفوما هم حاضر به فسخ نیست و شاید تا آخر فصل بمونه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/136107" target="_blank">📅 14:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136106">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
شهریار مغانلو مهاجم سابق‌تیم اتحادکلبا با عقد قرار دادی به مدت 2+2 سال به تراکتور پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/136106" target="_blank">📅 14:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136105">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
شهریار مغانلو به تراکتور پیوست
🚩
خط حمله تراکتور برای فصل بعد ؛
🔖
هاشم نژاد
🔖
ترابی
🔖
حسین زاده
🔖
اشترکالی
🔖
مغانلو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/136105" target="_blank">📅 14:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136104">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
❗️
شهریار مغانلو با باشگاه تراکتور به توافق رسید./ ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/136104" target="_blank">📅 13:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136103">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
طبق گفته شهاب زندی مدیرعامل نساجی هم دانیال ایری هم کسری طاهری مشکلی برای پیوستن به پرسپولیس ندارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/136103" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136102">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/136102" target="_blank">📅 13:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136101">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136101" target="_blank">📅 13:11 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
