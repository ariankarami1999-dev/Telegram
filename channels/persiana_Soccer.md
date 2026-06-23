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
<img src="https://cdn4.telesco.pe/file/t81a61ha7dw951owfe-wfSmRb9ArlCuFugppRJp3lToPy1Kddk_m6kP_ADQy4Jf6-nBZDGs9AAUICR0xxDtRbC_vLH29K1yN8RzLgbF5WCQMVqV4JwUvinF_IWroRHPpt8wIMBC_fwELPtEl4WRw9JQ8qQbl4DCBfFKTTfbK7cKQ133McaeC46uG9yhWj2ZXLJ6ej5PMiD29mTZ9BIa4LAoRE83f6CK5XwcvAenRA2MwDDeajnCykUgIGDFDQ4_23qP-Yjlxz6sh-t_1plwtJx06QqCtmhoRK9gbn50wAshSdn2i9RAXPx4VDZw3PgYNMMi_Zps2LTLuPrT7pn128A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 311K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 20:30:22</div>
<hr>

<div class="tg-post" id="msg-24146">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJTIZFFyqDackxs_Ap9Y8gl9w-f6ZKUJwgZJGWOAORX8tUilO_adwdoqvoZ8bPCFG7mIlVZU9ZSDYnOwiHj1DRQxV76XdI5sHCv5Vq4pZKdBBIU-6NEG8VquYJnhbTNZ6gChTNnNadTXIaQ1UMa2IQcRL90sTdKlwl31yd0gu303cDcddnrFrNRsKa8r6dKVZ47jXeYXD-Qz3Wg0NWpVmWWcG8-MbWLpGldU7BTSqEymq8RYeRZ6QV4gyFJtg03lf7a3dVKLJQG_SyzszalXscRwjiaeB9Qheuqjy5wctrsKRB81HFeeNHjM2FJNahuEceQbqRDs6VpQ1rrrd0pvLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس دقایقی پیش نویس قرارداد رو رسما برای دراگان اسکوچیچ ارسال‌کرد تا باامضای آن اسکوچیچ باعقد قرار دادی دو ساله سرمربی سرخپوشان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/persiana_Soccer/24146" target="_blank">📅 20:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24145">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heBR88bjuIccDJFcuFnFxKZTEh35ti9FqB2nP30wSj9-LDfdS4KQt2JybYKsmr2W492_Cetw2JnjsJWP8O2vy7nwQLl2MpcDPRuchIxzEiHZCLyGCEz5P7fAPYFVApXb8x-RpLUC4FVQf4z4gfHrFNI2efCivZDgFPWWfSznXD_qEofizZS3SWbeZDP0uBFcRBuUlBzZzQpQR4Qc_d4ScpUST_1AerSGno_PqfXthMw0Cdlb2vHbATCLuclCRKi2iN3j9PkFAAqq9vk9APgBQ-adH0xeC0wJqM9ZzIsZ2I4br9KV8HmkR7mWa57gIogdqFacXB66oWbSjhi_8WcCRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا؛ باشگاه استقلال امروز باارسال‌نامه‌ای به باشگاه شباب الاهلی امارات خواستار جذب قطعی رضا غندی پور شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/24145" target="_blank">📅 19:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24143">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7hrkHKV3koEc3KicXdJv13vhkZGGru6_RHDwfejsqT1vVi_QhT817YpVwrL-b0czD08u4cs6_8yNumZP9OafBRe8OmaVCkV6xwtB2oxIMsFCHqsFjNymwkEiwDvtUdnM3095HBqPETYeEWQgznqlQO_dHrh1XmZ4DZRRqFMCZ8eR4IZfxgBFceoR_JMDlBH8qMkCWghECsLomR0c4W7GQxnYKLssWYjEVI5qeNhA5tLKtWHInTeYG2dAFJMLN-_sMFGfhzX77yCcOcnf1ZWz5-BqZtfmHjEm44Qd2CTFrVCMhGgmQBu3m8NPR8T8LWqCo0vixk93KUmCtoRJL8spw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m629BVl4aQT4V_OoVFNxI2m5FQtYdx1O2aLqi7lj_gb48AY9aubMuT6OSb-ls9lKTYtKUg8yjFC7L-kXAN3nXzU9Lqqc4G3sSD1OwxaDzl0R3a4R5G-aKhOfyI7E9gKbEmWyBR6Go4S57skrfRm6DbO01-B938ycFd_SqrlG7AcJym2MPpOFTukIGUUZqGCFwgEQKumz3B0FmPGyTv64YiIOCtaPJAO576Zkbqj6XB-ncrbv4E1IUnHllPMGY2kfnuLKbk70UAh8WjSy9MoAE1WwWi1hazuhe2Ib4vW5gboDPo4WIwaL2jc-XErtMWBqIIDWt7ogxmjrZRPXCFxUfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/24143" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24142">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3fgcs-YalJaM4tkCDoKAX4z7XfkEGUzb5CMko2mIKxC04vzZqHI9_ykz11LyuGRkxni-OSFbv7tJhyMDkFpnhch4uXnSO8SCbWCVrBG76N9TKRgONOR1P7Tw_HplD1oKbvgO8-OBCO74VhJeDATfTGuyGP94MRIx8Cbj7pZ2gq8MlOPei0MmUx-PdRZ2qV9KjdQoWiOF-enU2TXTI40sVpq_zjWFmDA04CQM3swZMpLUZs4ukjAUX8o8o-CU0EJo6_yg7tGU7gWzeOXPriKwvDF7JEXlLUnVlaDY-t9S05q_vFwXR7fPAVjoZsiiPkVi7KnMp67eGstT_8xvLyN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/24142" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24141">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA6993l6G-hORO4goUIigGrTcwz0NFlha1w7ITcD-ul-99TOQrjt0oznV32Fktr8wxqGS32_FBaNLDKnuS62DKsA84mOMYQ_98pa9QOkUXpRk6v1Q7QnH1W5ufCfCp8STESkMJLlC1Z7ZHYfarKouGoJ171DOa4HhRLrE9pd1WJef1c5FAjEpXO4aqTY_KKfqsio7WKjsCux4fCadNoequWRw3HntyqW_PWWZg-DQFYkppbx-qVOQyPSx95fivngd29uDYJXl9GmSDcMrcjdmpW971fDaAEie2SMiAGh1r9QFYi9reyCK49m9kNq7gOmg4kB0Xtrb_vdpIuUrA4uVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
برای اولین بار در ایران
🇮🇷
تا
0️⃣
0️⃣
1️⃣
🔣
سود اضافه روی شرط‌های ترکیبی
🤩
ده تا بازی میکس کن، سودت رو
2️⃣
برابر کن
فقط کافیه بازی‌های موردنظرت رو توی یک میکس قرار بدی. هرچی تعداد انتخاب‌هات بیشتر باشه، درصد بیشتری به سود بردت
اضافه میشه
🛍
🆗
تا
0️⃣
3️⃣
🔣
سود بیشتر با 3
انتخاب
🆗
تا
0️⃣
5️⃣
🔣
سود بیشتر با 9 انتخاب
🆗
تا
0️⃣
0️⃣
1️⃣
🔣
سود بیشتر با 10 انتخاب
همون برد، پول بیشتر!
میکس حرفه‌ای بچین و از ACCA Boost
نهایت استفاده رو ببر
💵
💵
📺
تلویزیون لایو برای پوشش بازی ها
💳
واریز و برداشت مستقیم و سریع
بدون واسطه، بدون معطلی
🛫
تسویه در سریع‌ترین زمان ممکن
🎰
همین الان وارد شو و اولین شرط ترکیبی‌ت رو بساز
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eG2
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/24141" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24140">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=kBexNI4uVbkqonrG3Ac8OrGFTA02_axG5u_djrRYCvA42f0QohO5A1AMo7HBIGglBq-VDEtJ6jS2NgxUP_frPuF03H-vS5b8PdKQvQfjizhK5rll9QLcpfLoqBKRNeM8VzogFXCFV8Tc9QGbGY1D3Rin5kZrg3xvKJb7T3w4ZVgU_Sc1ZvBk_s2fCOks07lM2RvLcaNCWSb-xM_TlKDWtx9HdBdwSGYm90uMkUxHWidT3oLPGUaleIxNn4m7j86eGqW2K6JNx0MSnanBJNidp6S_VKXwd8Pycp3bUpQpSZweJVxj2Z0uYpgnp6nab0F661sYEVvhCRcbwbuB9kk5yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=kBexNI4uVbkqonrG3Ac8OrGFTA02_axG5u_djrRYCvA42f0QohO5A1AMo7HBIGglBq-VDEtJ6jS2NgxUP_frPuF03H-vS5b8PdKQvQfjizhK5rll9QLcpfLoqBKRNeM8VzogFXCFV8Tc9QGbGY1D3Rin5kZrg3xvKJb7T3w4ZVgU_Sc1ZvBk_s2fCOks07lM2RvLcaNCWSb-xM_TlKDWtx9HdBdwSGYm90uMkUxHWidT3oLPGUaleIxNn4m7j86eGqW2K6JNx0MSnanBJNidp6S_VKXwd8Pycp3bUpQpSZweJVxj2Z0uYpgnp6nab0F661sYEVvhCRcbwbuB9kk5yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه ابوطالب حسینی به مجری شبکه افق که به مهمون‌هاش کفن‌هدیه‌میداد؛ فقط خنده پشت صحنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/24140" target="_blank">📅 19:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24139">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGbsabvE6uffl7ENLEZ0-tpXcQWzgHlKmn2AXFgE7Iw1OyN-XdzoEyL9qrGP02Z6DPkzPJRRkYSfWmMcFT6XshIFiX9REFub80BCGiPDFgFXLBrNTk3Srsygg7XhooY8A3yEV4umaTWGabBDu51pKyc3SgZhKrXZDRqkar7hYgx1WuoQiSZgpu0e2Z-5jFfwpb5KMF5YQgTNG1yRtcILhZwTzvNYJe6UadXcTQHeRxJ6Gtdd1yj67d3GQWQiRGCT5xHLNzIDB2O5o5Nr8tD-0SZnQBRppjBKWOqLspp4s4vs9BJHcSiMXXTTBKyKJVZLkJn8gA4UX6NiYLUPhccPzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/24139" target="_blank">📅 18:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24138">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1BgN--q2txIqlPpgxgg3VFdy8f_v5YhYsflVN1srrUCsh5cxWmKxkFe66BSnC-hYVOSwb3bN3HhZ3qwIqeCR3Aps275CDsdNsLz4X_zf_33zMPcZiuP_HM2kZLWizw-TTP_C-Hfk_RfMmE0VcMLq989NMGMaF7FdQfu_15izCdlBzoPRl3Kwb6en5uKlqfzZD-Vg1g4-tAJ_819FXMNQxFqPp1W8bsh7VJcRClvyVJIkdjZwMPxqVXc-3LA5nOwzzKO5PrC6in9NFDzmXSxY1zEmol4ZP-mItdP8GQC8Ro-jlIYY_fZZSeqC6AtVdM6i5pq5wWchoAfNDmhmxVPvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
بازیکنان‌تیم‌ملی آرژانتین اینجوری از گلزنی لیونل مسی خوشحالی وذوق‌میکنه. از اونور کریس رونالدو گیر یه عده‌آدم اسکل و احمق و تازه به دوران رسیده مثل ژائو نوس افتاده. وقتی رونالدو داشت تو رئال و منچستر آقایی میکرد تو دهنت‌ بوی شیر میداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/24138" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24137">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/to5Fkj-8eOisV1OJSPxogOLe3J6SknYGweLu4gkblOM1SHQo0c0LKwaWnZardh5orMlN9ovHLqKnhCOvkDDdSXV1we6kyHXe87wu19ftrlmIkEXTEqNBRwu9bKzveeFj1UILx3tm9jNlE5RXxD0XmkC1MOkk1Ir6QSjlUXyXhj1AwPOxZAPYZk25FEzFeXHbIlsreaaXhfTlWchHx-vErSYCFoEHx-MmS7mHesGccfPfhO9Lye4wwirVJ3oNMi1wL0HB3gmnmFlwCPc5UMcb8NNQ6_iqXQ9kSRJYQHAI1weZCIebTPeN0gPNEfnY1jIfVB4n4-T1zsb9KQOcJloZaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال دیروز با ارسال‌نامه‌ای خواستار جذب یوسف مزرعه وینگرچپ تکنیکی 21 ساله فولا خوزستان شده بود که‌مدیران باشگاه فولاد رقم رضایت نامه این بازیکن رو35 میلیارد تومان به آبی پوشان اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/24137" target="_blank">📅 17:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24136">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zo_RDBCwe2NzzLGkGc7-8BvxaT-Usq7AxgPo36WHEFjVaYCl7YFFRLWEv9oHhEYq93ruXK4pgDwFSZhtRJd5BwngEE9lSgLUBlOE20QJ1vMZda-HY5AMMmO9H2U9KtFgAyh6AXn6unq8vyi2B4hsH3nJWTmSh96F7LBeeFOMOUKyB-sIrDkPKhLDWEY14fFJ4tBcjNZ2qkVHOywHE23sWOZFqsawZU-bqqLYqtJ7-MaEtkKz1P6gfgRGiyOb2XYkZu99ZkM2TJXu0cJtDJOjqxUKb2ZVdRSJfkZGcpPaIAA-CR92Xc_MB5XoYLTkbK9tJQSJbQf1zLq_9-dzRGQCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/24136" target="_blank">📅 17:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24135">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoCDMwdKPSjlUPWL7adVK9p911HEDUwe-zNqDGSPyBQtGIblUPtr5f7XW2B2nsFlP1JDpy6baOFOed7VCO9q4-tLOuvJ7s0Rjg8T9XDCcYIeb_Egji4_oM3DI2hHhTbdeEQ0S7T02uxS2V76a5-kcPYpn-ezl1ljVneKcTQW3f3tGXnSqfV2Elq8-07YuUbPQpku2eHpjst2KNOnDktMSxd8LiyxjFYum4Irin_wkWjBljphzEpveaonOaVlzjjolA83HWPPri3QbOxwwwRnLIJc8s_sS4W9guthhyQptEi6NRv4sbSRgMtd6hElD09HMAVYCCuPTUKAZrJpvoa0DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/24135" target="_blank">📅 17:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24134">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHSC5VQGLLz7WH5RYJXweVm2J4ZaMMrl3pGC6cCaafLu3kSfMasZwVkm7sdJCGMeKA8qvAdxYv2RFJJk1c_x0uzrjWPCr19RZhExdRBtJgudbdmndQv2bTFJ_wTrtyJFN2ljdyIpYpOiIgoRxa8yVPB_9xiTAzvqEdMMaA6fF-0OGp8bwOwotO5aqM5EhZNHSWqTZw1-Oa92bCQi2uQ8XI-CqGeiTi6i1y0BhaZHAmBnHhH31QMXIXWXkQJO30jW2xriNjT84GsATNzRyuISPBgBWRaeN_A-cWPnq-CNzQ0489N8Z_6PxaGi6XgKqsT4tgR3MUxJ5-oRgIbDd150CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/24134" target="_blank">📅 16:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24133">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇦🇷
🇦🇷
تمام18گل لیونل‌آندرس‌مسی فوق ستاره 39 ساله تیم ملی آرژانتین در ادوار مختلف جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/24133" target="_blank">📅 16:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24132">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⚽️
تمام گل‌های روز گذشته رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/24132" target="_blank">📅 15:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24131">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=lZIN4n4ImoL5J2Kx9bMsieh-yhmw4h4mNvrGvcdJvS9tdpYTygFKlZ_TRolbMDR9Q57KXcpnF9brXXsMpe0HmUmt4445quzYQtRSRZoWXbJg0OLFq2vOfcAyF106hlv5ZRGspnnaAgZuadwtObxCt5JGK01hAPDJcwoLmLtkFTynMbFAeJAVtiZtAXKtwmnaqNGLnNqN6b9Juf-D_HsSWgKFy9c-y_V_EG8bGUT2A8U7Ha5h10mb3NGcdA5BC7YJkzorHLCBmupW_a--DSCfta2-vXLGcU37-57UJmP_MUDNpudSCNXRzhZVHsZUZce0d6rlKNdDQgiaZlxIrH-KFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=lZIN4n4ImoL5J2Kx9bMsieh-yhmw4h4mNvrGvcdJvS9tdpYTygFKlZ_TRolbMDR9Q57KXcpnF9brXXsMpe0HmUmt4445quzYQtRSRZoWXbJg0OLFq2vOfcAyF106hlv5ZRGspnnaAgZuadwtObxCt5JGK01hAPDJcwoLmLtkFTynMbFAeJAVtiZtAXKtwmnaqNGLnNqN6b9Juf-D_HsSWgKFy9c-y_V_EG8bGUT2A8U7Ha5h10mb3NGcdA5BC7YJkzorHLCBmupW_a--DSCfta2-vXLGcU37-57UJmP_MUDNpudSCNXRzhZVHsZUZce0d6rlKNdDQgiaZlxIrH-KFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
زلاتان‌درخصوص‌لئومسی:
من تو دو تا جام جهانی هیچ گلی نزدم ولی مسی تو دو بازی پنج گل زده! براش‌خوشحالم‌امیدوارم همینجوری‌ادامه بده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/24131" target="_blank">📅 15:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24130">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKfTRWJJg5DCs6mITT3Ntdcai-Va53n6L7YJzdKe3WQvLtDzQUsjQw0ZhwKFAE0Fczj3oq0jRJYDJKVQq1Cu1dxoJIr0nkz_s0oXoeey2th3sSvHsiPew1FbltP68IBA-9tbd2t3AKyoFjmFRt9hWD-5OqUyO66mmCbCjLQpv-TZYCkIVtP--fSQgLMh3uZvdx1j6JJAlk1xJd6to5nsOXc7DEA9EJyq_1U1orDj6AUu4Xe582wbBm7iEpJd1uxafwmibK48SYC4wmk7GSXFGc3zK81qtHu1ZlMFc2seZZhySH72IqQQlJEE3Fuk2gQeXO6Xf7CWc0JxF3QHyLdfAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
فرمانده روبرتو پیاتزا درتمرینات تیم‌ملی والیبال باقدرت هدف گیری 100000 از 10؛ عالیه ببیتید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/24130" target="_blank">📅 14:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24129">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_UNC4P5iBhAWjrjbn8o8zt8AF1VCD-Sq_IV07mibhsoWbUlT_UvEJ3tBJ5109EqWIf2qvpHQnJOT5ztGURTzjYbRdTViTxSpOUKsFxTj5qG3nZFBzc8JKP1JWRxNlN_RGrK8RxGwjr2eSQJOBBf34O9XWMN9zTwuG2fKTIrFb6VIkqfDLyZNY5UVIzLP7ALnyVU42J6xFeJfeNPi-jCuGzD8VwJI6HLzCRdq6WCzTChat3sMKINX0Id_-M2O3czTeW-zkCdE4GDvcZaxT2Bq1KY2nQXCYJVROfYVDQsQfhDi-PT9JvOa-CA8N4OUnA9-uiM-YaI3vjHa07r_qnfdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/24129" target="_blank">📅 14:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24128">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyWIvp6OCl7OmmrxjsFDOEzvOGXHU792AE7qRGvtZ0QJzAU2n_jQ1kkXQ4FRD-E48ekKIA32a2E1b-74Rp8wQKwOfUWdCQ6rMxRtxQRNcSqqLouwfR7h2rl3w8yvepm1CCclKHUi2souH_Lhgi7kxMED6pqM__YUi9wCXXDkBCsCB2FB3RelDH39n811GKH3CrRZHQ84we5-2W2Jmmi1UOdhd_P8QtPdCKyCJSwMEhEDfP_D324zFgpv63Zbcb8FrTsfBytcIRCrbJR_v2sQwo4JRqBUSAHN-1ZHG60HGBwbFdATEZ94GH8iqCkHEjN86j8vNQqEBI6Il8Fm-xaU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/24128" target="_blank">📅 14:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24127">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=vxIn7tLy4HRdKDIMNPb3DsWcOXKQYFaVg5f1E7DGVHIHbYtFrJkNLueXdVnD3XM8xPcosIxlGbmrf6unwcqfZ6Lpda7gpIUKOCQLZmLrQDYs3typteSFiUUrmVfHcRFZsOzUu1aW_peengL7Ov_rjG1OB5ujVMVf7UrXzKMyfKqKSYbeMkaCXiMCITBjDMgb7Tz10gUeHOOpIpAXTIXRen-D9R2PkZWL1tvkqMXaFri1Co0pjyek9avcOUP-0PuysGr4PiQk_JZf0HsvBykrLH0TMW7Yem6ALZbPEKKDkMTWQt2RU_PbPMwiTJh0-0-t7o-dWPtYAIidVazb-zFwFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=vxIn7tLy4HRdKDIMNPb3DsWcOXKQYFaVg5f1E7DGVHIHbYtFrJkNLueXdVnD3XM8xPcosIxlGbmrf6unwcqfZ6Lpda7gpIUKOCQLZmLrQDYs3typteSFiUUrmVfHcRFZsOzUu1aW_peengL7Ov_rjG1OB5ujVMVf7UrXzKMyfKqKSYbeMkaCXiMCITBjDMgb7Tz10gUeHOOpIpAXTIXRen-D9R2PkZWL1tvkqMXaFri1Co0pjyek9avcOUP-0PuysGr4PiQk_JZf0HsvBykrLH0TMW7Yem6ALZbPEKKDkMTWQt2RU_PbPMwiTJh0-0-t7o-dWPtYAIidVazb-zFwFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جادوگر غنایی: هری کین رو برای بازی با انگلیس طلسم میکنم، قصد ندارم آسیب جدی بزنم فقط به اندازه‌ای طلسمش‌ میکنم که نتونه موثر باشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/24127" target="_blank">📅 13:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24126">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMoL_txJovA_wf7xb6Eklj5MVlJZJj7zYjitg62l55qvJU-SmTcnFsRJHg5KagI5hZj8NESYR3wy3w1vJP_Pxr7wCeYxf4wqpdikG-LK2gJoLCRytqsoOASv-fHlxbVO9C6IaazH25Jm299gvs9KOPnyg67m5UdEEj1auuTlsLX97we_ftp1qArvvTJB1-NFMSH80_EZ-fZBpMrbVD6aSvKtwW4ydkIuHO0uje89z61K4xOKm60LiN4clwgCooHaOWNgLci9JK3UfL8IO5IZ_LKJicEBLya1IP0gqz0qOD_tei09lh9zgnauYSl8PoDR6L04zanF-sjHHBKP6TbZzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سه ستاره جام جهانی 2026 تا اینجای کار؛ رقابت برگ ریزون لیونل مسی 38 ساله با دو فوق ستاره جوان فوتبال جهان این بار در جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/24126" target="_blank">📅 13:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24125">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyL-ohdiVxnOWJQwY2PGxei1vnSxixHmio7LpF0z5MtvILZJoKqjMSc3ti6MkUKjDGzAFyPsXl6i32T2eptlwhHCKbA4tRSSinqHKnC43L-WlOfl793iTcDyamv7CVHRCQcHO291OYYodvO1OUQqjq1Yq4S17MIUxaU1BcCHabZuKT4sihjlrHwIbg0WO3_5gr1xQBpQp5poUNJcM1EwAsDeCHOXNHXW2P26eLN7dK6B0zw8512keqbh8wcc1cLP95M3x5KdocIqZMaqxuYys4EdgvpgtdJnNV6tEhPZl_pCsFOxmoC7b0yTtKzwa7nWtkaBg9JctMjMRKnokQIatQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از خبرنگاران در نشست خبری قبل از بازی انگلیس-غنا از کارلوس کی روش راجب باخت سنگین با ایران به انگلیس درجام جهانی 2026 پرسیده گفته اصلا یادم نمیاد. مطمئنید که من سرمربی اون تیم بودم؟ من یادم نمیاد به انگلیس باخته باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24125" target="_blank">📅 12:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24124">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk3goMFE4DHUIrNM-wJaEn3nHP25gxYcxN76KAGbMK7vj6KmAjoZG4l3rO3iJ_gBRIka90D7C75QQ1ULWgrqNjlIMlVJ10lAB2ttGUoB2Xjh7gLExR3SNAM9tqvOGkOlIRI90C8Ct7pVK0l29mVdQ8V8s27jj0ADxeydyym7Fa9AQf2-JDoD7iBnDv9LMNbjF9jL2C73cWTQ8IlTBuIqgpMDen41BzCdUwvJ07cYYw-HDSZ1aB7obnQK7C69BiOTB9LzUxI7Z0oz4_4vt_jEFBUWc-Cal0f3AOxo_3964wivDILlfS-Mo59ict6HtpMBQ1DAN_jnJMptGrtqe726lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24124" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24123">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6mIYG3rfG8_Isfi8XXJSVUgBHctdP4XkqqY17_moElxukY_S719EIj6btyhJSa3JzQxoRd50xh6A3Spr8KRCBjDvzVVq2fSVOFLiy4d1xcjvn1DNxZQtR7y3Fc27kT3O4hQocwgEjdMfZ_3QzCcrFilXFI0luWQ3P_p8hn9EfMdDe3bQa0Z52ZxBzTWDDEOt7BXCL7S2IwmH2ZGIEpa2LKcjvznjV-NxvegUF0zHMMToL-rqC7crNOpB7SS4b0iDRd2oxyTZYTGbH-TVCpUfGmN0k3gB_bseVomvvH__vlQc1i1el6NVLiuh4hG0ETAtISTBg7KtsNknET-_e9Vdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24123" target="_blank">📅 11:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24122">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma7MNF0VUXczy6sf_bi0n4RViwyqRBAt6bPC8Iq48qpvrNYuPtNuAccnGv88f3znSLHhYyUzNu530IW_tUd-o__oslvQGXPQkE9C9CKQQMZ_I_7nH9DIQqot_GsH9z0vw3oM4hEBKhbbo3Hjkemj2SC9m7Vw4vJK1zLX-1L0yHmzd3ELkReTEnFTCuOEHzv_AUzd-plc3JgIAGtmfgigewpM_7azvYWc_5okdy48ZTrx1vfSMEw4ScBkkgT8W6ePU_aBvHjxjNssRS-ul_t-PKOAdLYz6JzBvGzO_0NdUJpXQyuaUZNpjlJnEPPWvArpaGQuQGROpje86qj-b7FpVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سه گلزن برتر رقابت‌های جام جهانی 2026؛ ارلینگ‌هالند هم بانروژی‌ها داره غوغا میکنه. دو بازی چهار گل‌زده. اگه هالند درتیم بهتری حضور داشت که اسکوادش بهترمیبود و هردوره درجام‌جهانی حضور میداشت قطعا الان هالند رکورد کلوزه رو زده بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/24122" target="_blank">📅 11:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24121">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMjMa3yC6lGMS4j1SkFPQD6nQ9sHEBfUzSg0-wokJ0eT27owlKrVfeBXz13zQjgEl0D-EJl8c9BIlD39AXRKT3cvx_dpQTSerxauYmzShLg7b6qAIDOLOQevwKq_FEWTcR4OryPjLO7ALxEqmHLWJAS6d1WyxxoH4rTQR5FQpikJoDXSFIvU4Go_PhcVzdU7WECGL7rJ6O5Y-RYJYkJVVW72DibkUD6ppA0NEBg-kXlMddE8jQhRKaFaMADhaRgxvwodDnspS7FX9Q9KztqHE5vqcE1eEsh7Bn8CcUpSMRkONDp4GNokjYuaTIOILWfbX8_lpWxXrZAt4eoJDkwDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24121" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24120">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858e98f07e.mp4?token=L2HL9-TFSqxzeo1TGOA4e-hEJZL0pE0prf6gp4YLSEMcaE_ToCvpGLwCF09zaS4D6NrO-n8a0M3g-PU1ydKvWY5NR4ceCTxA7-A2wfiAANbLhFrlvKaBGtfn243bO3KZQyueFTn7O4lCWw4C6jiP-HjYEQ78io2TLIf2a8NeOVhZmUb4k0TJLK_6rONF7-hDh589B9vaaUNOyHLsE-g4U8mU_3MyPm7_seC8PGP2gDN0yJ53TfbT3LvxJkhZ-y1DyrnMaD_pnA3taloQKLFG2joIy64c6PO1dHckq6d7WbndYCrWSRg-YgGuY8ui9ZABxw439jgLhwRG0HW9lEzSWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858e98f07e.mp4?token=L2HL9-TFSqxzeo1TGOA4e-hEJZL0pE0prf6gp4YLSEMcaE_ToCvpGLwCF09zaS4D6NrO-n8a0M3g-PU1ydKvWY5NR4ceCTxA7-A2wfiAANbLhFrlvKaBGtfn243bO3KZQyueFTn7O4lCWw4C6jiP-HjYEQ78io2TLIf2a8NeOVhZmUb4k0TJLK_6rONF7-hDh589B9vaaUNOyHLsE-g4U8mU_3MyPm7_seC8PGP2gDN0yJ53TfbT3LvxJkhZ-y1DyrnMaD_pnA3taloQKLFG2joIy64c6PO1dHckq6d7WbndYCrWSRg-YgGuY8ui9ZABxw439jgLhwRG0HW9lEzSWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌اونور آب واقعا عجیبن، از دخترای کشور خودمون بدترن؛بدجور روبازیکنای ایران کراش زدند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24120" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24119">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACpJR-r_-fYc4UAWRuuPQt2ZrKDp2kTtGaqOrbRGApBGV5W03YLCsU2cQ4uO-EyWTpeLt9fFYSkV1l4XG3KlQtnYkkaOFc1dje5WhTr99MB3ubOdXHuk7_HL13whA9fgoZUbNBCMmYudvxKgLz8JBgrNv3wr40WLzjl39AEe6rK_1TqdgcCsqoShCN9bx4Vwg7BXf4ArgWYIKSTW2NWXJtJPlW6XVSkPlBVdTy9wKcUb3iU_-3IdUffqV015zY0z4HshjdC61W7Fv6W5-mVt0YrB-6Wp7K9yFPyP8gqg7tpiB_LD53Hl2uKYNUZu81T62c7PzdJmQdOkOY_2gFOY6Q.jpg" alt="photo" loading="lazy"/></div>
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
کانال اخبار و هدایــا eR2
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24119" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24118">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWcIQ0EtlLVdgciU5Y1KpoER1JYoEEWWKAkfGgA4d_hVv0DRwVZiy9haAGuamru8KZKlCHPBQ4dtHwRxf3CJzizq-nm1yP4EyLMroLshriykFAEJS46-IFNHyOuop337_Y5iC_CD6MZKAHLqERAELVofx0w-kTSWPG3kAQryPVii-biF7ZLIv1wk7MNbmyYE3OYSEULwYRn6ZlDvrNC1HKKHqPSVhoypS9zm8A6Rw7DFcp1ij0r4jN5GtPvkU727UB178VcImVD0vnkzedsKXGhblNoXIp599FzJJFw4NLok2eg6UGBN0lAn_3xUPom2qfRj2RPknl0sR2uDXDgxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛پرسپولیس 5 تیر بمصاف چادرملو میره و برنده اون بازی روز 9 تیر با گل‌گهر مسابقه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24118" target="_blank">📅 11:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24117">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_tIUqFmzcLBy3QeT4Mj6Pu3239La9NZKj7X1Dr4yaxwfk4MZGIU5AfuYH1jvUHu1k2bmwpxd4MGUNZJYA_jTHBOUze_gkUV_0z90RTIhROpqn2h14yC2wTufna9vT4DCZrECQKBG6t3X2hIqWyb9D0GsD9CrLhEZ2ObXbzwBB7kG569SLuX-_zqhM1PD5sp5P-iuNb2v0qa1HmIsImDn9Xdl9GChnWfEgaEbqUhHPXZ3_WwF6YsTsJsSsnGQQsbpJ4cGNbyWgcPdqSHmJPTXsWxiCL43a22hiuc5Wtclp0-D3ULbXjuMdBF8jolCbgnCRKTHTVonvXNnm8LLlHzGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه تراکتور منتظر فسخ قرارداد اوسمار ویرا باتیم پرسپولیس‌ است تا با این سرمربی برزیلی برای‌پذیرفتن‌سکان‌هدایت پرشورهاواردمذاکره شود. اسکو در پرسپولیس، اوسمار در تراکتور؟ باید صبر کرد و دید اوسمار ویرا برزیلی…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24117" target="_blank">📅 10:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24116">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbn4KrNPGIhW5Bx4Ts2I9rp6bFH9BAc94vzAbURxHB7i4Mx8OE3YskqSkgSmt0Ii8-IUveH1Iq3F_8sfs9eOOTuseNuqKBckTYRiAYA1YDu-fBqNhzTWkpqmlDrzChdhubkju_Q8EpAuKfh4BRNIbTv2mA4QYpbmN-HwVtvnRYTawzA_TAA63rVmAeXmZn4of18l_74riUmgUyPOE8YVxBqPLsEsl2PVgnuMDdMc7u_XK3O6oljR1L5VFYoSM6C5Yqs5oYyahvpi1K07_lHYexwvQ1pWtFKRgdGaJO-Jd8CNZ_HQYLklIb_HQ503tH8wIRyrwN7MrI3OwhUqmSH6Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال زیاد دراگان اسکوچیچ کروات روز دوشنبه یا سه‌شنبه همین هفته وارد تهران خواهدشد تاکارهای‌معارفه‌اش بعنوان سرمربی جدید باشگاه پرسپولیس در هتل اسپیناس انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24116" target="_blank">📅 10:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24115">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7529e6e9.mp4?token=KsU_TcWRQdk5pamTFT23MLedlcFQTwSCB3ThSfqK4t9g0cohUXuIVClCiEuJbx1OXC99aGDH0aVF63QeLzdS8ltFWfCeYkKuJ1uYJw_PDDTFuM4ZFqNAVuXEIYoFrZ3iWwhUe9v7mGgio7N1RyLWPDQUuEYl4mswFr288NgBu2Me_qXRUo6FYEpUgzt6V8TC9P5BfomdxasWL_66xuLYHMGZw4_2D18RaxQS_p5gC0d9FjESsw68ziKppnAFpjvqt5EPTM-lv6uBQ5N796iTfrGQ_niHCWDHQuPF-K0YPiJhdH5gb3tLWVfOc5A8OyXH_gOlx1Oy4V03tXhVlF9AXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7529e6e9.mp4?token=KsU_TcWRQdk5pamTFT23MLedlcFQTwSCB3ThSfqK4t9g0cohUXuIVClCiEuJbx1OXC99aGDH0aVF63QeLzdS8ltFWfCeYkKuJ1uYJw_PDDTFuM4ZFqNAVuXEIYoFrZ3iWwhUe9v7mGgio7N1RyLWPDQUuEYl4mswFr288NgBu2Me_qXRUo6FYEpUgzt6V8TC9P5BfomdxasWL_66xuLYHMGZw4_2D18RaxQS_p5gC0d9FjESsw68ziKppnAFpjvqt5EPTM-lv6uBQ5N796iTfrGQ_niHCWDHQuPF-K0YPiJhdH5gb3tLWVfOc5A8OyXH_gOlx1Oy4V03tXhVlF9AXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌از یوتیوبر‌های آمریکایی وسط بازی ایران در مقابل بلژیک عاشق یکی از دختر‌های ایرانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24115" target="_blank">📅 10:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24113">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec5bb65aa0.mp4?token=ZQy3q-XB7Zg0XrpB1Zoj5EBf9WHreWZZUOGGBSQkJIxvGrFcWSixGd-HDabB7_NfzAtcgcaNOdR0HsTq2YDP5lcUnswSvrDN605DRpwVMR8Uea_YtaGoMIBY0ppHGxHr40HrQDirM6r17uFtLWPQcm5fGznzx8tbo9_BLXjrbIMU6yzS3IxkBu8S3s8ybpNFaIygVRGfYMxNaO3W9KQXLjK_aH1xuXmUmd9O1YBB9VAFIug06lVzEfZD4vKbWSWtpkmrpxQohqwnzC8G7fnJTloqWUbKD2m4o612k2tgZkT7199h6yxMlbu2ynQN8zxFPvX9epFuYoyDOwANHvS_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec5bb65aa0.mp4?token=ZQy3q-XB7Zg0XrpB1Zoj5EBf9WHreWZZUOGGBSQkJIxvGrFcWSixGd-HDabB7_NfzAtcgcaNOdR0HsTq2YDP5lcUnswSvrDN605DRpwVMR8Uea_YtaGoMIBY0ppHGxHr40HrQDirM6r17uFtLWPQcm5fGznzx8tbo9_BLXjrbIMU6yzS3IxkBu8S3s8ybpNFaIygVRGfYMxNaO3W9KQXLjK_aH1xuXmUmd9O1YBB9VAFIug06lVzEfZD4vKbWSWtpkmrpxQohqwnzC8G7fnJTloqWUbKD2m4o612k2tgZkT7199h6yxMlbu2ynQN8zxFPvX9epFuYoyDOwANHvS_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
عادل دیشب باز هم اللهیار صیادمنش مهاجم ایرانی لخ پوزنان لهستان رو به ویژه برنامه اش برای جام جهانی دعودت باز کرد هم به لهجه‌ای گیر داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24113" target="_blank">📅 09:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24112">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT4abD00-rKD20N919Zaq0aXHCRKEdmdeWxEdgkLD-2_bRB7dxpiXMpZPFVrbFDlGkMnYYJULtdlvbkrWOP_Ip5fTlVAZhNthVO24kdWajU3FJ6I1v2SfKXcao2nNCvCSLMWquFpt_FtKaj0mheDWt2J9KchJNlLGKDu-O3H-GgzL_svxPGoCwJpxFKO3L104XWJuREVj0UJyEdGoe07AmE5_Ex5LKXYNTVkAM2yJv1fJCE-YYOacuHVAKrxBDlyLmfQ1xc1Z86cp7m0oBeIxDAyUYiBZlUwW0vctNtVhCA40aKb7cIOAs-v8rQ5axM2ER6v_ZYBHEtQ6DAcIBGBow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24112" target="_blank">📅 09:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24111">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xgbc0l3nnmX2Bd_YJeKYVPbu-nJ4ipBn0gPJjJem7hj_I5ghmGlePooxwByTvUmqd8FAWoPKHc_UBApcCByMgvP-NctF5vY9IIECcD0oWjUFENkWvVTqlR3JkrJkPsYPjaKnNbtLm6cVD-rgOlpOlA_YSOjweCGyizhX5bmQwo3tWyIsErJyoWKiHC9h1ZrS72oEJDQCQ-B66TiINOd02xyXxPHK-4PxfOTHVDu9BfdVHy8zzyWyglP30lDmIlhUc15rMxiiMxXAxc56Kzw9e1ZlXlfTanGNDAck6UwyujabNxpHdMrmvducrTJxeNkzCtv6548lvSOIIqQ5yL_XAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
فیفا برنده‌اصلی جام جهانی؛ مروری دقیق بر ترازنامه‌ مالی ۶ دوره‌رقابت‌های جام‌ جهانی نشان می‌دهد که بزرگ ترین تورنمنت ورزشی جهان، برای میزبان‌ها یک‌قمارِپرهزینه برای کسب اعتبار، و برای فیفا، یک دستگاه چاپ پول بدون ریسک است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24111" target="_blank">📅 09:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24110">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5G4eIACdgcYR4MbXMlit8K6YrgtFPuLxqpwMyBLVnk5N92vQB0GXQKHfm-ReUmzyXfLs5UiHEchOsWcGlYBvq9z4wkfgOwr5Aw4JCTmJuN8kBpMKiBXZkY_Y4bnj3yzso41C9VgOcStdSqoxdkKmGk-ltjX5TPEBjK2Cvht_b_t-s9sRslA-5eFcfJEGpKV8Ad3EAoFTcrE3zcacy_ZLw190_ko73g79tu0Br_LFA_tEVEr494Tf8fOhLAgs7pEBuJrPZi-K2SovAyyzpX07LPqzAYNKdBNwiAeFHfyblKbbVnrBs8zx7tpUH_0UCEJcAaiLTBUPBWZMsq9kpOejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌برترین‌گلزنان‌تاریح‌رقابت‌های جام جهانی بعد از هتریک لیونل مسی و دبل کیلیان امباپه
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24110" target="_blank">📅 06:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24109">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⚽️
گل‌های‌‌بازی‌امشب‌فرانسه
3️⃣
-
0️⃣
عراق؛ صعود راحت خروس‌ها به مرحله حذفی با درخشش امباپه، دمبله و اولیسه مثلث خط حمله خود؛ کیلیان امباپه بااین دبلی که کرد تعداد گل های خود در تاریخ جام جهانی رو به عدد شانزده رسوند و بعد از لئو مسی به رکورد تاریخی کلوزه ژرمنا…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24109" target="_blank">📅 06:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24108">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVi2rD9dm7zqTbzI4gSccNKgrMw-uiAMeKv4lY9TuKCX5lQeN6bAe-wO96GXkB-WyxyzdkYxK4Z9L2t4QxKw1Juc_6pcJRn-MfcjYmN0eIR1VUIjzoiCIBAPP227j8R2DRo0XrVewyp04MEIoXkshRpcgdR9TZRFdkPGU0IX4QWZH4DuFZLur4cpdic2VWi6mBw-KPwOZUelMu3rb6DoaAoXZ-Y-QSulJtfIBqYeS3PIye72JJh2RF0blk7wc_Hk66r2R_OGn_oKufoILVMaZ2-cYVciTKnnd-bS3QPF98AZmi_B4TDf3yQGoikGiZW2dpKUCpRfgui5ov96Pmdw-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های‌‌بازی‌امشب‌فرانسه
3️⃣
-
0️⃣
عراق؛ صعود راحت خروس‌ها به مرحله حذفی با درخشش امباپه، دمبله و اولیسه مثلث خط حمله خود؛ کیلیان امباپه بااین دبلی که کرد تعداد گل های خود در تاریخ جام جهانی رو به عدد شانزده رسوند و بعد از لئو مسی به رکورد تاریخی کلوزه ژرمنا…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24108" target="_blank">📅 04:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24107">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دو تیم عراق
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24107" target="_blank">📅 04:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24105">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fcp2LGGro5dIkgplpHyCwev4qw4-mADTLMxYsti_mqL9SUDhu8Re5gMVmeoWBQSx26B7VwdT0IrNTMyYeS3AzhMoteREttSoP-3MPmp2F_SENaaQXqEva8_1CtU58beFCQRASsyZqI_8SaljMi-Ic42O7xVS3bcEZNywW2xEb1hK0aZAsUkb8towAdAPrFD0dsulZjENvl02P6ESuE7yoa7UEafN_rO_vgnUTADThrmTMb60axuWE5s4f-BU1t-0Wkw2FUr928oiayvk4i7O62v4OfFXjixLDBNmmxBH99ZBGw1wMAdlfgN7T6fl-EHfWmdodOqwcV7FMWQT_bOPOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رومانو: شماره 9 فصل آینده تیم بارسا به احتمال99درصد خولیان آلوارز خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24105" target="_blank">📅 02:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24104">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1DQyyA7BiCG1EZZQ-robWaiKRea6hMiZnmGpTyDNaLFyIvYEETYz5Ac9fBwjR6OBUGBsmULeApz-8Glf98J8SLC-9ftphMmSpFr0JA9VDEjX-z6nA9slNN5gtXl4OPog4zaVVTzTIxgV2yUiA7lJPAz8rA4DUJZJX4mVcS_sq4z_E3WtPfI9HYXSvJZrLN7qGz1KMCdlmN9nnBlSG3oDFVluHyAvbLyG7E7H4YkiMC5wkpOpXqRRfOuFfEUYjvKt_dpBNsZR-glTqrJz1KeAEy_1VgNUTVIfHBc15U9I4_i7Ti1Eu42bDvMezLY061kpVs-ZuFgG_t7ypeRintrVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیشنهاد تراکتور به مهدی هاشم‌نژاد: 3 فصل 250
🔴
پیشنهاد پرسپولیس به هاشم‌نژاد: 3 فصل 180
‼️
ستاره ملی پوش فصل گذشته تیم تراکتور بزودی تصمیم نهایی خود را برای فصل آینده خواهد گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24104" target="_blank">📅 02:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24103">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rtq9Qlifw0ox6cts2nqGgLBfbQlbZx7hbTlzhbif02iWZWqAi9SZnCU9Mumui7izYwlaI3AlhxwYsXxMCYCffSMerhpfgzp-y3qpk54kN1Qqs0FCOtQqkGtTvgncz7CIyIU92S1jbgIQy5HSzXvx9aXXLQ3pg6LPE0tdUVVLzAUw9jO6RE8IwnDwWfxx2vIiSKTnhVBZlSFZmgXvGCHzkj3rQIJM0oCr7tv_uCCtQwBpa_KvNqRhbahUvM67yH0tSRDtPLPRUCBLVtzqyJyw5ooI-LmVLkQEwnJNtAs3HrV5lde_VmzF-V0hBuXI6axjUpfNYZ3pT5nfTFe9Oe12PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
فیفا برنده‌اصلی جام جهانی
؛ مروری دقیق بر ترازنامه‌ مالی ۶ دوره‌رقابت‌های جام‌ جهانی نشان می‌دهد که بزرگ ترین تورنمنت ورزشی جهان، برای میزبان‌ها یک‌قمارِپرهزینه برای کسب اعتبار، و برای فیفا، یک دستگاه چاپ پول بدون ریسک است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24103" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24102">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ad27d0d3.mp4?token=mjGRjTanqqho9v6zuN0kxYDPt70JpOhB7fFzw81I2Nm9PKOC2ZQVkLIJbBWbwEnmQnjvq7dZbvFDSfrpc5McIygwA99Y-Eq4iLUsajBvurhwnJVvkcDXrHYYmDoyNDjLnvbJBkktJJYWyxavnZLmYnCJ-MrcXtWn50sbCY_T6I9Qjv0hZBlbAtfcKG_t-Mj9h4Lm8iq68gefcp2RAODdXc0NnShVfQkC5pgrn2paGu9zOuAhIrIPeZi-RQDLuYzGKlw6zpba_VmqiUg5BaodezC0G_7rA_VRtu19XnIdMgCm9Bk1d_lkpWjyuPPDymgQ1UbQzNQfZq6M4p8t_Zo1lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ad27d0d3.mp4?token=mjGRjTanqqho9v6zuN0kxYDPt70JpOhB7fFzw81I2Nm9PKOC2ZQVkLIJbBWbwEnmQnjvq7dZbvFDSfrpc5McIygwA99Y-Eq4iLUsajBvurhwnJVvkcDXrHYYmDoyNDjLnvbJBkktJJYWyxavnZLmYnCJ-MrcXtWn50sbCY_T6I9Qjv0hZBlbAtfcKG_t-Mj9h4Lm8iq68gefcp2RAODdXc0NnShVfQkC5pgrn2paGu9zOuAhIrIPeZi-RQDLuYzGKlw6zpba_VmqiUg5BaodezC0G_7rA_VRtu19XnIdMgCm9Bk1d_lkpWjyuPPDymgQ1UbQzNQfZq6M4p8t_Zo1lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمله سنگین زلاتان ایبراهیموویچ در ویژه برنامه جام‌جهانی: من فالوور ندارم، اونا پیروان من هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24102" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24099">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKpVHmHokKgDxUxpjBCKsjcbTEPu3Kya0jNWQBNqyHx4SV9bclV2awS-Z3NpVwyVGtMV7gqFnrCLbAPmrWUIWa4IHHa8QQcayMK4nlHDSpfublECENQ30MygViod__e0TFZFURVdEQmDfqfmYkR9GL8BqvnFaPvi0h9BCfMbYiXpGwjYHkD2yF9oDLcg-u18Q5BeJaaw5kUbw-hzrL9u6mcE1LwhpzAt4_qSZAJfnW9SJyNwTC5WOR_NBjW4d5Dy5mGJLAZOmWi1AD6zhR0qt9Cd_TWz68VuNXaFpXqrwUy61z2SC0EVgyWjSC4JaPU0ZdATF95T8EUIU2j0bWmWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛ خولیان‌آلوارز درخواست خروج از اتلتیکو رو داد: میخوام به‌رویام برسم؛ با افرادی که باید داخل باشگاه صحبت می‌کردم، صحبت کرده‌ام. بهترین گزینه برای آینده‌ام، انتقاله؛ رومانو هم گفته: منظور آلوارز بارسلونا هستش و اونا به توافق شفاهی باهمدیگه‌رسیدن؛ رابطه‌سیمئونه…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24099" target="_blank">📅 01:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24097">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGCrhbBoG0SiLXpZHzN0fpjQew6-_0rbTa75bOjMpW6YOJIrED4Cow1HB3mGit2fzSyBsUrz4C0hogQ8-yBpOyVBaujv8ZBr0bSgcOJfmIGV1FUau2jzIYTINglggn7qI9xNz5N9-TD9q40GvYDuc44q2y34O2pQ3zcP-y0GTum1wum_lnAT_KD_QniCTm2X9i-776kOzoONXd0uywKuqcjpORoWL578utERpemvi2LAdb8yzDM2qEBI1NsynfwX_tPGyMuf2oTergAi2jWHz_SQt5fOhqeMmK4MqiN2VnYau7OomF4O-PjYczVThGYSFGNPBQMsLBxKX-1Eaz7o3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اگه فردا دراگان اسکوچیچ قرارداد خود را با باشگاه پرسپولیس امضا کند بلافاصله یکی ازستاره‌های خط‌حمله تراکتور رو جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24097" target="_blank">📅 01:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24095">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f709c9542d.mp4?token=jBf6CFF0jyhAbKv51w8hYybXE48Mr2ACz50qabbc4aqqBEExR_BojbNrKn_Yoe5EKa8wPx7NlithK94C44hU_ay5DJBanAinP6m7xD6ZzBEqp7VOdmmZmjbYCO9UL17pnabTUDKfS2wdhw3GHm-yDJ79kdrmLTm1IENRZMeSKSXM2TO4cFC55-3hRGTTvAyXmlj4riEA3lbG3HILETy0DXJGYP8jvCTcs_RxcGLxrV_9dDb0q0cRoGxuijGcMsNzt9wESN11VHN_GDNU2rEkpi-p3NpY_KJTsQLKpPlFgwGpFWMOqxMNyzKaTVJm_s2rUqEGgFSDDlHNph2Z1avzYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f709c9542d.mp4?token=jBf6CFF0jyhAbKv51w8hYybXE48Mr2ACz50qabbc4aqqBEExR_BojbNrKn_Yoe5EKa8wPx7NlithK94C44hU_ay5DJBanAinP6m7xD6ZzBEqp7VOdmmZmjbYCO9UL17pnabTUDKfS2wdhw3GHm-yDJ79kdrmLTm1IENRZMeSKSXM2TO4cFC55-3hRGTTvAyXmlj4riEA3lbG3HILETy0DXJGYP8jvCTcs_RxcGLxrV_9dDb0q0cRoGxuijGcMsNzt9wESN11VHN_GDNU2rEkpi-p3NpY_KJTsQLKpPlFgwGpFWMOqxMNyzKaTVJm_s2rUqEGgFSDDlHNph2Z1avzYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
#فوری
؛ خولیان‌آلوارز درخواست خروج از اتلتیکو رو داد:
میخوام به‌رویام برسم؛ با افرادی که باید داخل باشگاه صحبت می‌کردم، صحبت کرده‌ام. بهترین گزینه برای آینده‌ام، انتقاله؛ رومانو هم گفته: منظور آلوارز بارسلونا هستش و اونا به توافق شفاهی باهمدیگه‌رسیدن؛ رابطه‌سیمئونه و آلوارزبسیار سرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24095" target="_blank">📅 01:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24094">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6f0643b9d.mp4?token=V2IDDlzLsjFHLe2ZNVHuOpGzpLnh4UFqK1WjWcOdx_FhoN99woPHdnOUM2XrbgqILJpRsCSamd_NB1zN4XTATVVim3lk5vJahZGdPsFWMtfVTbKi9lIAev0CsqCrOVlEepmYmBJ2rwkMreQBG9Yjefc0oii1_52kGxc8TqiBXWanFRBSAJRepOStgtnxnnrc4BRZA7LQ2J8A5R4xD5Y7xFpq4_wNAu1iOT9TxuWLwlGW8aMyaW5JSF8iUCylNOErTDQ3N5KiJmfINLs6CRnGAvQ9PmqUT9PLKhd8eFPFP4TOy4uHWyOO_krnumsi3XmrFHwjutyMEGdryW-2LfsafQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6f0643b9d.mp4?token=V2IDDlzLsjFHLe2ZNVHuOpGzpLnh4UFqK1WjWcOdx_FhoN99woPHdnOUM2XrbgqILJpRsCSamd_NB1zN4XTATVVim3lk5vJahZGdPsFWMtfVTbKi9lIAev0CsqCrOVlEepmYmBJ2rwkMreQBG9Yjefc0oii1_52kGxc8TqiBXWanFRBSAJRepOStgtnxnnrc4BRZA7LQ2J8A5R4xD5Y7xFpq4_wNAu1iOT9TxuWLwlGW8aMyaW5JSF8iUCylNOErTDQ3N5KiJmfINLs6CRnGAvQ9PmqUT9PLKhd8eFPFP4TOy4uHWyOO_krnumsi3XmrFHwjutyMEGdryW-2LfsafQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
صحبت‌های لیونل‌مسی کاپیتان تیم ملی آرژانتین در پایان مسابقه امشب مقابل اتریش در جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24094" target="_blank">📅 01:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24093">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrslCFeQLLsJinS51WObqTz2YC-Getlkc2V7MuFsnIlz0n2U2d4ZCm9EFudf1rSDCrzFg4_ak459Kbhhyubxi4ZyhFkOKcjpVN2PkO_hqQrcPybByL2WrT6cCymHRCjq-HxvC-rskwm0onEGOnWNhHml0ZJFe7_gx4YsCq8RUUT2CpTuKPFXDCwjYkAwKzH3AnAzBfvmctlWXwlWpQ4mkmmHyOr2AcybR8q3zpHThsyqYrZ4fbV7STZC529GyRZjGYWKgiCHkH_7l--SOPCa2hRSgrNY2NNfO7FVzMHPj-es2zJM289d1L43aQxxwad6GGDbE5shLwUIFg7Nvks2aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از مصاف یاران رونالدو مقابل ازبک‌ها تا جدال مجدد کی‌روش و انگلیس در مسابقات پایانی هفته دوم جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24093" target="_blank">📅 00:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24092">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfhIRusuRPZOi8xU6rCCa6KInbIBJZDOwG90IVApfg6tbRd2AWGgGMijcamExnG7LHOE6uNt2fEQdUZCnXTJN3P7yxLOskiOToEYbrOvn-lXRgQ8LmmGoS9UvTyl-c9Z4Vdr8UjBS_s4xKFuosYqtrpHKfVz8IiZvplP0UxA3tIH5mXmnYg-99qu17qKiQ48-wV6JrD19rUoRv3x_GpbeNKopGLg3Zsn-xe2r5BfEuN-sOkBU6RAKWddIcpwhJmzmpEntyIu6NaQuEtGWPAD6fDtV6oFi7tHrOaZvwKLzJCgTLfTUsGIZBXqYxZyel8JvtwBeaDRH9JFygNEEQ1M2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از درخشش ادامه‌دار مسی این‌بار برابر اتریش تابرتری‌مصری‌ها با اثرگذاری صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24092" target="_blank">📅 00:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24090">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urT8OPA0Bf6xJfKNXZOkbsiO74bQiFvWZKTowt30Gtv_pcU5UJLoJjhg9mI6gwbEzx3RC9ZcJRRd-q_3N2xfbwLoWtLi7QZg_zqlHxjVY1LcaWDJmA2pTmCMVJ0A-lw2oIqhC60l_3xw6GEapld7pUGv2rgdjTpeDMuMXUfC-Uux4rAwscvomEq_JVifvkXfpag_MmOzvLmzfo7KgM6LAG0i93eDdwAbhvO20712aV6C5paLoEius6XXOmHAg7pU3TtLtylmKNLSJV1eXQrxdpZXyn_aNJcF_1hojYfV6om0t_dSMkEhtCPjHO4fI-HY8P9xP1OMjf3g4k6vL-3kEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بادرخواست بختیاری‌زاده سرمربی استقلال؛
عارف آقاسی مدافع28 ساله‌آبی‌ها در تیم موندنی شد و حتی به‌مدیریت باشگاه اعلام کرده در پایان پنجره قرارداد او رو به مدت سه فصل دیگر تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24090" target="_blank">📅 00:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24089">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvaHdMVyO7ZLY2Y6LG_UXM7JsIl1arE5WOaRxhNiG6N7MfX57-_pVgihLN2EgBgg1kGlOWpNBHJR19cHTI0Xebjy8nIbov0yIvEMMsqmmyW12S4rhhfvWaY_aX9MfFAvBD0AQKhHWCgz6pMUq9Zisk8MfkohA-xvpxNXpV6uhzkUrdn0CxW4u1Zb1Tv4fdWQ4f93KOQ7XYgWAslQLyiZKEKRFdr1adqkB722L06WATJZGMoehiWQbmSRefR2e7JdD9BZgPXVxMOHOXm2kTWfd3yk3r7lX8lTcaCVS83XZ0MJdlTyelsmGh51F0UDf5PjuM8w8CGilWpxSZjH-hJyRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تافرداشب مدیریت باشگاه پرسپولیس تکلیف سرمربی‌ فصل‌پیش‌رو خود رامشخص میکنه یا با اون دوشروط دراگان اسکوچیچ سرمربی‌سابق‌تیم تراکتور کنار میاد و او رو میاره یا با اوسمار ویرا ادامه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24089" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24087">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YrL58iWxGFoFpdXEitlYrqsRPFdEdesZxKLxDmxzM3mXS3qXhrWL13TFIj3UojoEXK-4JW1DCc1R9dyS3X7SllK5hqCIYvV4fMeia6qHsO87h0VozuVfLd7qGjjipVJVT68symnr9oSYMT3ewVIRJtqVsPKdzqOoKZzRnEeCgK9CcdECIYdR0Mh53pc7V227vQNnJCk60HFA-8cOa17TQ4IBjLdcNZ9mh4CgNOu4bsEXuPCnamkEewH4z33mP9SL2jBlqNT2bbvKrqHkIo5_87AvlVmS7LqxY6zyxJdghDVFfkRnUETQE0W_tbeKuPGRYVk4v0tc8iiX0fRhS6DRdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q_wEf4RCi3LpYoHMmp2B8DLSGhYCC-lQwklahGUw39Wk5os_-48BSsFuSYMITUQgIjb8y9wo-nUKbuHmeZkwBV3cA-zpvsis6rE7V0yAkZpluEZtwY0XFCroKAvD5v2BP1rrbCwDeTnlsybvwb52CXnMKj8g3Yl4NlQm0OIqhxIqI-8GaMw0OQQ5S4HG1CORo7IdPke1l5YtvlWmPAXe4hiSfsnpENWpE9fij-zivGdTJswgZrT5S8TB7o0BGX-hRpugPRfj4deIs1_8f_7Ik4Qr2kb88dUxY4fcQ07GGT2twMLWVvPPiWQvtMvLI58M3wpSYzckUrlM2XNhTur_LA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
چهار تیم ملی که تا به امشب به مرحله بعد جام جهانی 2026 صعود‌کرده‌اند؛ آرژانتین امشب به لطف لئو مسی دومین پیروزی اش رو بدست اورد با شش امتیاز مقتدرانه به مرحله بعدی‌رقابتها صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24087" target="_blank">📅 23:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24085">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7535185668.mp4?token=lMfFpqktjpWgBtB6aZFcXx9kZEEGbe0-aGua0zmOffzRMEQtGEpm1FaH7Ju6nNIpGaAmTk7eCYPfc-WfcUNWilKISF6baj1lWc8zOSBxiFp6rY-6v0vgzfUsq_EYttdCxa62I0_xD3L-bXqDJJthDk9mNjP4tNev3u-OFf6X7a5BXjXnY9Wo4VjRWPDs2o3-IcNmJUA2-hlAwrocoJaP408fJREj80EmnVwr2SN19F9a6qJe_LHxE5eEt0_1RoUbyU8BZxj48jZuikfmWyVzlBhKaWsgqeQfCKf4Ua9SspvgvsYoh-czS6QAv6bYQ0r9fFxhPL9QzY73Oqsnd5kJ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7535185668.mp4?token=lMfFpqktjpWgBtB6aZFcXx9kZEEGbe0-aGua0zmOffzRMEQtGEpm1FaH7Ju6nNIpGaAmTk7eCYPfc-WfcUNWilKISF6baj1lWc8zOSBxiFp6rY-6v0vgzfUsq_EYttdCxa62I0_xD3L-bXqDJJthDk9mNjP4tNev3u-OFf6X7a5BXjXnY9Wo4VjRWPDs2o3-IcNmJUA2-hlAwrocoJaP408fJREj80EmnVwr2SN19F9a6qJe_LHxE5eEt0_1RoUbyU8BZxj48jZuikfmWyVzlBhKaWsgqeQfCKf4Ua9SspvgvsYoh-czS6QAv6bYQ0r9fFxhPL9QzY73Oqsnd5kJ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24085" target="_blank">📅 23:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24084">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWbzOj8bs2n90oggWHysu5fb4P5ETxF6v-Fn2fpkUWKEtLdfhJhMCpYWrDwMzuAUppYJGsMQF1DNHhv9zDQm9COGGorp2Z-z4Tm1h7eQamla9CLMzSeY2YOHP-WZa61ZiA3EvP1uqriS9AJ4J6QwgsgJgq_LziCLbcukPDjDtFKPUCOOaCQje6VFPrKMppNFdt_Hk5qSiinu0y--WmC5xQS7_XPQe_Wn6eQ70dA04suY2uqBKf2pjKBU-ogcvD6BmK_e1bkqPqClTClP0Wnmqshmfgc2Qu-StaHwTzTBfaYcoWS_tjTH1CnII08ZrpuNYOCbrqDW5vjcQVZ6JjnRJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24084" target="_blank">📅 23:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24083">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Um2_njqp5T_Ixq52Y0gwvzZhTf3Vp0pgja1MKZ2fDwaQ0_PKxnTSf9avfgDDS5LxfUL6L2FRv4mirN4b4NRFH2xAqtm1g2kbFkldgmUupumyqBPu9V6Rip81NWDnm8Pvmtc3wRrobAx4nZWyQnV5wx4Jwe9NTmk7E7EzBSA7xFr-pZfZW_8AfiVpFvM9WPbRW0w-kDyIr3Ll0BxG9z-PlB8Qaa2r661x-RKEheSuPxkJpNzwW-KJr2l6upsoT36Csly-p5l4mCtdw5fzNFCm0Sj28Nwwc84arTsnI6ZL4innz_WTRwQOXxo4lq3gIl05lgiMh6T0F6mk1zhYpp6vMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24083" target="_blank">📅 22:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24082">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcJAAYC0_K8fyogZc1nqc6Rn8E9yTzx-QGpxJ0YqkCmzyBnoSYl-3BXn7FlXhx_X9hhVWceMtqsOs9IL4LDB2VFXWWe5IGJ9U2iM_SDvYOm6wFzEyS5PLXo04RSAAhZ6mX2zdaFvVbA124D3xdtSt1NiFiAjvgxLu6Pj3gUB-DxLzLC4uuguENXd1E4JMfhLXYheWAT-z3kR6UJCJui6UGSjTXgIfQDDBL5GUTxtIe5ueY0NnseOYAmnEhuyrDH1u-ac3Ywfi3owBZYA2jXqdP2UBy9OhkPhSAH0DTPz0UFJ4MrLxpaZ8ltgdQzJfUeZVRo_Ctl1yqLbKA7r1wnDpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
سفر پر هیجان لامین یامال ستاره 18 ساله بارسا و اسپانیا خارج از زمین؛ 6 دوست‌دختر تا اینجا
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24082" target="_blank">📅 22:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24080">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sODJbI47tK4uUPtxmakOdewQ0VMYjivej9MPzKMTgY4KYoXxwzo13s-KGe3nq3z575tIfM8jYufmfAv8ZZthQbZx1oaSJp74WHfa8gilOWQZ12CNN8WtFqeo31e__OTxy_zHfHdt4vvr3Eheh6bRUBV6DydQuQAqjKl8xgBy2JS9ptFZ6p2grAU5k1ULWsYdg-4j6t8Su4aRGHED5tC7ig7W5uFvVi6y_XoOk5UjMRuAScn--XGhN1zR7VUBDUXXSC3OvP_QT-jMfnmsZCFOcTIHdvhrdhgAElhxIFfp5mv06_pkG0xrcqmOJQlK6stE9SfLOlAC0yfa7jx9GFrbdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
شروع طوفانی لئو مسی در جام جهانی 2026؛ دو بازی، پنج گل در سن 38 سالگی؛ این 18 امین گل لیونل مسی در تاریخ جام جهانی بود. آرژانتین تو این دوره جام جهانی 5 گل زده که زننده هر پنج گل این تیم توسط لیونل مسی اسطوره‌ای بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24080" target="_blank">📅 22:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24079">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a48741736.mp4?token=CPwYhsFKnzJlXbNvoE5WYUjlUD3wh0Wy0TypWubEKOlhHXBTiWrdmldkiROiVR51Johm8oxbCmYpjr8awOw91VlgDhzahIWR9rZKmpJMZeYqIrResY7C10cgclfUaZIejrwccKLiR2n--FHaOuvf8vU3ejLXx8ol4kVp-Gf3XSXaLxqBuk0GHZy5-ov9q8ID8xOpRGNcdlI9ek9dc0-5f-hZFYrIdobtYcecrD4PKWWoLhVhgB_3ILE1UTID8wtp95Oy3BV6QCNjsKSWxtNTczFMqxCJ5myeMMcyfSJHBK7MmJiqZPhwpe5-pSO2Qs0h6md-KtbFMdLhcHdDJlQqAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a48741736.mp4?token=CPwYhsFKnzJlXbNvoE5WYUjlUD3wh0Wy0TypWubEKOlhHXBTiWrdmldkiROiVR51Johm8oxbCmYpjr8awOw91VlgDhzahIWR9rZKmpJMZeYqIrResY7C10cgclfUaZIejrwccKLiR2n--FHaOuvf8vU3ejLXx8ol4kVp-Gf3XSXaLxqBuk0GHZy5-ov9q8ID8xOpRGNcdlI9ek9dc0-5f-hZFYrIdobtYcecrD4PKWWoLhVhgB_3ILE1UTID8wtp95Oy3BV6QCNjsKSWxtNTczFMqxCJ5myeMMcyfSJHBK7MmJiqZPhwpe5-pSO2Qs0h6md-KtbFMdLhcHdDJlQqAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24079" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24078">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5beb8a2493.mp4?token=ivrdrHOWHCm9UxC5qGgmfnZMQT0QKGS5lEjjL9sTCqAHfdsX5UPnX_cTfpAnciMZl2t8ZJia3dZ2Wm5mfnNs0XQBLu6x4Je8u8755OZfIj-n_DMgy2WiCPKSUm3T9MBVKuUpsyMxnW9--0hkGat17u-f3VDOVeUuPXb7UQj5JwEjxX8tGJO_tlsh623bc-rtiuQ8NW0XBK6Q2G5d8bkDlr5xQW3tn49uPHLoUebPQgNeU6rczqdGzKSblQOzhJz1IHbcbxWAI1MyeIc72oVZVrvC-Qi6bIrO3Qg3J_JqTIH66hiWUZow3ooKOyF7m4jDHfPNnxpgWajDmpimOadrTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5beb8a2493.mp4?token=ivrdrHOWHCm9UxC5qGgmfnZMQT0QKGS5lEjjL9sTCqAHfdsX5UPnX_cTfpAnciMZl2t8ZJia3dZ2Wm5mfnNs0XQBLu6x4Je8u8755OZfIj-n_DMgy2WiCPKSUm3T9MBVKuUpsyMxnW9--0hkGat17u-f3VDOVeUuPXb7UQj5JwEjxX8tGJO_tlsh623bc-rtiuQ8NW0XBK6Q2G5d8bkDlr5xQW3tn49uPHLoUebPQgNeU6rczqdGzKSblQOzhJz1IHbcbxWAI1MyeIc72oVZVrvC-Qi6bIrO3Qg3J_JqTIH66hiWUZow3ooKOyF7m4jDHfPNnxpgWajDmpimOadrTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24078" target="_blank">📅 22:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24077">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyeEJ15tD8uxB_UguU6mAuJKjOMr5C7WPw-QWKyy3dg7U3cjdQx5LcYaTPJqSlDKZoVp3efnKbiBGxTS3eE5wSeFwHYpmZ53rRyZpMbG6mROxoLU46df5lMQwpWlQUxZrGwEVFvSe-qSLiJh6AMTr-3ipKOjqVEfCXOeqEAKL3IjeU7UajHfJkvjdPbtMGhXttZVhxsq0I1yiVislIseInTzB91jqo9RqS6kYZ_YkqPPWEiDB5PrXg-BsGs9HQag0X8MLgZxPB3qNZYGJvSTWcrzhi7RRfEY924TeEdgJqP80z6U9-n8XzI4GXElBp9Ri-Wa_-vTm0XnQBmHbz5l7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
باشگاه استقلال: سیاست‌ما در نقل‌و‌انتقالات تابستانی جذب‌ بازیکنان جوان است. باشگاه با انتشار این‌ اطلاعیه‌ دست رد به سینه بازیکنان سن بالایی همچون محمد دانشگر و سید حسین حسینی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24077" target="_blank">📅 21:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24076">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4iPkajZcGSb0_vUk_TAovHALy23aw3xd3K6-h5q91GLFyzQCznLlriNDl9EupiLmhqYmfdTTR9gKAYVI1Mqzr8WSFYQUXY9GO18xzg3Q744_IkTpcZaSLgIMWzrbDEewUVsJ7bAbOXre34uhDCDeffCcWlZas7NN09T2hOOD730ZpV9iX1nlhHs6V3IFfvWjDmV_ilP7BRe4h0Wh834I7jGiDCIhUkMaz8Ue4kNuuypwzUf4F9HCzYO2gPE2KOz-O4T9XmOd8yHEV_1jcXeWEskap96P0U5n8TN4FPWoyky4IPm_Aeu6fY1UThLdTcde2RA_hNipE2VjE3TKr6scA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24076" target="_blank">📅 21:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24075">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f39b8ab1.mp4?token=o0CXKqe48OUGRGt26fVnbZ9S-i3tnT1edYguoJnxpX6-aUuKK4NhtZd8uZl2x-RbR6Yiwd1s4Tack85J1OX1SngBODOTzZnReQiZXWvLl_MSnLIXKNWqL2A1k0s_DW2c7X9VbCKdAJ0Sbn38bGO-myaF5qb6wv7ooX1hkHoTohjjDX6ByW5H6a7hE6j_EjhwNgf1dhLw82DfJeWLrz2qloePor9UZ0xT_XNVsK6X2cyt_luqXkM0jI6uleJNKoFP0D3QTkYwW6EfAwgY2rO42fLVj8BqrpuBpAyyVx23G0rg0k_wscp27SoimKZZTncaHmORSErBN9ugemOUUCfeGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f39b8ab1.mp4?token=o0CXKqe48OUGRGt26fVnbZ9S-i3tnT1edYguoJnxpX6-aUuKK4NhtZd8uZl2x-RbR6Yiwd1s4Tack85J1OX1SngBODOTzZnReQiZXWvLl_MSnLIXKNWqL2A1k0s_DW2c7X9VbCKdAJ0Sbn38bGO-myaF5qb6wv7ooX1hkHoTohjjDX6ByW5H6a7hE6j_EjhwNgf1dhLw82DfJeWLrz2qloePor9UZ0xT_XNVsK6X2cyt_luqXkM0jI6uleJNKoFP0D3QTkYwW6EfAwgY2rO42fLVj8BqrpuBpAyyVx23G0rg0k_wscp27SoimKZZTncaHmORSErBN9ugemOUUCfeGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
لیونل مسی امشب دربازی بااتریش میتونه دوتا رکورد رومال‌خودش‌کنه. یه پاس گل بده تا تبدیل به بهترین پاسور تاریخ‌جام‌جهانی بشه. یه گل بزنه تا به تنهایی تبدیل به آقای‌گل تاریخ جام جهانی بشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24075" target="_blank">📅 21:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24074">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b9463294.mp4?token=TRJ2Gv8BkaDm-OI4ROQhucXaEzweWUG8yepkUQ7MHcWChnczWLEGhNwdgqLcT-BIOnNw92K3LLKX0cVxKq6jLUhd8LBhjOOQHq80d_KHP-w1084n9cr425Bm9b2t6nR-fsoNZyS0M9TdKUMPcDdDdPaOLQ8DMVzinGPVzA-tB6A-nHCmKqSy0KTXZEI4PmQ6ohbYHHKrP7XoZeiuxTK9FCgqehxZFv35ABdPV3V347JJtURT6_8Isg9BMLWb1RxhkDv0jR9t9B-Latr2mKoCZRfEjHfUowCo3vUpyJu92xNwDMaBE7GGpzaa27RUHeqbaYOcHA_rl8dOi2K9y88uWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b9463294.mp4?token=TRJ2Gv8BkaDm-OI4ROQhucXaEzweWUG8yepkUQ7MHcWChnczWLEGhNwdgqLcT-BIOnNw92K3LLKX0cVxKq6jLUhd8LBhjOOQHq80d_KHP-w1084n9cr425Bm9b2t6nR-fsoNZyS0M9TdKUMPcDdDdPaOLQ8DMVzinGPVzA-tB6A-nHCmKqSy0KTXZEI4PmQ6ohbYHHKrP7XoZeiuxTK9FCgqehxZFv35ABdPV3V347JJtURT6_8Isg9BMLWb1RxhkDv0jR9t9B-Latr2mKoCZRfEjHfUowCo3vUpyJu92xNwDMaBE7GGpzaa27RUHeqbaYOcHA_rl8dOi2K9y88uWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تکرارخلق‌این‌صحنه‌تاریخی‌وشاهکار امین حیایی دراخراجی‌ها در بازی شب گذشته ایران
🆚
بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24074" target="_blank">📅 21:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24073">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvWmrkNfxgH4siWt1PshEnBrnz1s2FBLke8IBHUDNvNMAlwcdCz-4h_KDOeiHH85Az6jDebGVZmq2_7iQ5IAyIhN9F2QJPI3RGKiFffu6uZyEKn9_MLXJ7pyYd-7D3kFi1ekbp-8GKc75jQ3BksU5Tlto2kALAoCmt5xOFP1nanFn9qdA-EzdwipUAVCIT2LDYSMyvWjA1NiR8D1tHeHIX-2uFIGCMqqZulcLuC8k3c23re1kzzqZDIlz65BiHEmCrxTW2bTPv1CrWRhUc74dMcYG-DdAuBKi12lhPR765qBtfqqOlM8U9Npw1bqrzs2lQLvFHY0-jevhC5LEux1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در دقیقه 9 بازی امشب با اتریش فرصت بثمررساندن هفدهمین گل خود در تاریخ جام جهانی رو از دست داد و پنالتی‌اش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24073" target="_blank">📅 21:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24072">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دکتر انوشه مهمون برنامه جیمی جام اسم ابوطالب رو از قصد میگفت یونس یا چی؟
پامپ که برنامه جیمی جام رو ساخته، ترمز بریده و داره یک کیلو طلا بین مردم پخش میکنه،
هنوز سهم خودتو نگرفتی؟
این کد سهم: pump
اینم لینک :
👇
👇
👇
ثبت نام و دریافت طلا
دیگه خود دانی...
@pump_vod</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24072" target="_blank">📅 21:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24071">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275cd8fdaf.mp4?token=YrzpPxxzMufBu-SKLhUuHWDInGtoNogl-flQ7Fjiw7nSMKJ76wTMxfhCp036qSWnsTduz9mDPiT18OKVoBK6GYiaYLBKb67bxq3An7M51iiC9D-2iTxGOXcKhXjpxftCkpEdG_QYzX2Zg2JfcrRNBQR7uWsvItd8Df74Jr7c1JPi5neHTcOSVMu3Bxb0PvJyKcrH0LTGUUvwe3LeR1E-68kSGGDd0T_QcW1ro6U8cpjTNqSNGsmNuMZQR5Mr9WRyr_a8uJd3IMnPuhyxbZV2kggFnIcBaAWG8rg_U9Tpc2Dsfc-ylvSLb1TxxFkHpItcIT4jir6nnWgPnoPNbn9DVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275cd8fdaf.mp4?token=YrzpPxxzMufBu-SKLhUuHWDInGtoNogl-flQ7Fjiw7nSMKJ76wTMxfhCp036qSWnsTduz9mDPiT18OKVoBK6GYiaYLBKb67bxq3An7M51iiC9D-2iTxGOXcKhXjpxftCkpEdG_QYzX2Zg2JfcrRNBQR7uWsvItd8Df74Jr7c1JPi5neHTcOSVMu3Bxb0PvJyKcrH0LTGUUvwe3LeR1E-68kSGGDd0T_QcW1ro6U8cpjTNqSNGsmNuMZQR5Mr9WRyr_a8uJd3IMnPuhyxbZV2kggFnIcBaAWG8rg_U9Tpc2Dsfc-ylvSLb1TxxFkHpItcIT4jir6nnWgPnoPNbn9DVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
لیونل مسی امشب دربازی بااتریش میتونه دوتا رکورد رومال‌خودش‌کنه. یه پاس گل بده تا تبدیل به بهترین پاسور تاریخ‌جام‌جهانی بشه. یه گل بزنه تا به تنهایی تبدیل به آقای‌گل تاریخ جام جهانی بشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24071" target="_blank">📅 20:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24070">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqJHsj4A5diQlNqdlkpKe1o-tqw1ODOfx4QsSN2Ui51_mUSN3gP2wLhYvrEMPkbZ_7cbeGrqEM1nroo8_iLZWTP1N7ubmkb-G-QSsTE3lRgPLXeUZWmjVKXL0e9UeyLp00IGbHyyq8FEk2xd-S0A76X0g7iBjWjn840RN6yoFCjaLUXetixmMqfv-Lg8a2vqS_u9E-QL_OnCRHRwb_i81wuHLnKbTeR3fT9OCyP5mEJh0iYzRa6hSnieejpBDdeBhvD4RLYnlhQ0Kp9zzJ2OWC-pdZLcbC-Ug1uXp-bTnfBxg7vDAI7ko4LOGMk_2yziCipokP-Nh5E2BoDNWcwBMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
اولین گل مسی تو جام جهانی: 18 سال و 11 ماه
🤩
اولین گل یامال تو جام جهانی: 18 سال و 11 ماه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24070" target="_blank">📅 20:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24069">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=Le0y5HmysXUR6AHbdZX-Vf5TrXbUHHWtLlooL2RUr1avJccfG-zv9x4NRV-nj6NADqQM9OtMxX7XgHs_6WONtR4NnwwF3hGYl5kxpo5azx5uyb47AV9Axxl1znt_yc3GXIKT9oE_5WywUwc5QagaDp3pc-ywWPR7P5-nMS-oavZyTq_anJdT4naQvNd5eNat5673QK3bj7zUTeECTF2bXGvd6J-04fY_HdgU8phDxchGLvhDY_WEG2YtQtN9mg1IyYswAZOl0ShyugIxLPfkxH5bMk9UtSKioezPIf5J8nJVd1cbLYaAdhOkcHhTgjEN3yUa6zIjgd0RSjf70reydQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=Le0y5HmysXUR6AHbdZX-Vf5TrXbUHHWtLlooL2RUr1avJccfG-zv9x4NRV-nj6NADqQM9OtMxX7XgHs_6WONtR4NnwwF3hGYl5kxpo5azx5uyb47AV9Axxl1znt_yc3GXIKT9oE_5WywUwc5QagaDp3pc-ywWPR7P5-nMS-oavZyTq_anJdT4naQvNd5eNat5673QK3bj7zUTeECTF2bXGvd6J-04fY_HdgU8phDxchGLvhDY_WEG2YtQtN9mg1IyYswAZOl0ShyugIxLPfkxH5bMk9UtSKioezPIf5J8nJVd1cbLYaAdhOkcHhTgjEN3yUa6zIjgd0RSjf70reydQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیگو دالوت درحمایت‌از رونالدو کاپیتان تیم ملی پرتغال: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24069" target="_blank">📅 19:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24068">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzwRf8bp33GorfItK0JD-y-stP2VURNbUvjJClDqkKZYbEpiD5ndq7A5icI5OiG1UdhV4FDnMlZ4XObblSbacxWAjiDeidBVtfgJr4qQij2Rbdqs-iY5j8gCH-9kgn9ds9vsuEicLelpukmnB3Y4QVEOv3zy1ZRMQhnjSCAwXpSlHVYc9dw0W9Q5p-pS2YfOwtFS__aDygcDju4UBqfbDE9U1WdUhvB8s9hjQ0WrIkj7PvYd5ZiqJPcDKxiN0Ipm2IosFx0gN5iooXt4DYdBKXFEcW7JDQlgnSmPq8hPzBr8yerC7ZBx2HU2WBlqSpexaqWeTo1QVncstGiCMjQiJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛
شماتیک ترکیب آرژانتین برای دیدار مقابل اتریش؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24068" target="_blank">📅 18:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24067">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eI4IfoPTPheFQ-TKn2NNTVsewcR6u_fwsvOl_ofOyl14l6q2R4boqvfubp7aLSCoF6vjargjQPTdAwJkodZx-79Q8sLx__QbX5EZ-w1QEsQ3eLIFuRZGmA8RH5XTsLN7NlX37QypPZYfYvySX_s-Aucarrq46EH--L6TkYhMw0s19NGOXPIAQD6pyJX-zqNUHtjTJ01Y2WBLGqYt02Y7UMprDKluLi3m-vajNl_arvlWl2RqFlmJOh00SAoYvGMAzk8d2gHKwp2H0dA-8Hok-Len2ONgNZjNm9FSuK_lyC0YXLNubgkuJ-h5ko4efJJqAl5jjpBAr94nZlUgCTWujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24067" target="_blank">📅 18:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24066">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⚽️
خلاصه‌بازی اکوادور - کوراسائو ببینید لذت ببرید ازنمایش گلرهای دو تیم؛ بازی‌ای اگه قراره صفر صفر هم بشه اینجوری‌بشه‌قطعا به دل تماشاچی میشینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24066" target="_blank">📅 17:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24065">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa115feff.mp4?token=fBhH2S6umQcyFIkOPjRnI_wQ65KdxETeSmaO7RjgfGQMyod9Tw0Dew-Q1o_6C0tEuuXYLu_wQnw96_n3s39O1-DOFQIrlt0OV9sMvTKE4BJ78kwVg0oUJI01-LQSiQ8Gy9-lUKAfHnaKELEE8BijVh11D7SvB9xbKMwYtR_tn5ZLoTcHel-LnY0JU4qNFIqdVX6biansGrp_sfURs2WtYfTPdPeab4kkMa4MrwCJcCh8gtAFM8f5VIVRTvQFun2zgwJTttl0Ve1IDlnbdE4DvaBmygjPqXjeos7smuvqk5n2KayLdZcWCoQHtCz9aV9XtUDgUThyAwlml8vIYjgFHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa115feff.mp4?token=fBhH2S6umQcyFIkOPjRnI_wQ65KdxETeSmaO7RjgfGQMyod9Tw0Dew-Q1o_6C0tEuuXYLu_wQnw96_n3s39O1-DOFQIrlt0OV9sMvTKE4BJ78kwVg0oUJI01-LQSiQ8Gy9-lUKAfHnaKELEE8BijVh11D7SvB9xbKMwYtR_tn5ZLoTcHel-LnY0JU4qNFIqdVX6biansGrp_sfURs2WtYfTPdPeab4kkMa4MrwCJcCh8gtAFM8f5VIVRTvQFun2zgwJTttl0Ve1IDlnbdE4DvaBmygjPqXjeos7smuvqk5n2KayLdZcWCoQHtCz9aV9XtUDgUThyAwlml8vIYjgFHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه عجیب از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن به اونجا بود.
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24065" target="_blank">📅 17:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24064">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOQuJ3BbjC4Hbajn3J14DENCXvW5pbFTW_O5obed0xd0CUVVj2Xpyvz22AsvJL6u_jaGYPRZj4RDmX1A4vx4UZZ8S71lmykgclfqWOUjRUWEuiaLLkfitLoAD10Rs5QjrJTHFuee-F5SWva2SvFcoQ7VxefRLlv57bL1V6_3BDrOv3vTQ0yVwEzTM7BUW405ScaaRUeq-PArh6Py5R97LAjC651EDeDNJGvhUbdmKlNn9Mci7tjIAgDb5y68u8R-ykHtk-qa4H7pHTFaLWK9ZelRApJ2Rwd3i4-htrIvWs8rtPhk24VmM_OApj1Itx2-5B1vdvHEEKi_XuIV-vovMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24064" target="_blank">📅 17:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24063">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdbQKv5-a0bzMbdcrEskmg-Hlorwh5dZc5xsCi7ro3aLJ4O63SfV8GCN_JJ46sH_xVr2oM8vxPzvvXZDzaHhzoQRYGW-AfyIibAYW09tuTHr-GMOS5vWOcGVBw2li5IvR4ZyHf7eZ0GRSsRYnyxxZpfLOiRiOueoXgqqPq4qD4jlXBbHPfV5nNkPkJ7USpY9YcEE285ND6HAKJUYKsh5MjXDeAn4KWOiKovLNaoL0qbWskkOBHSM-rC5aYwVyWVI_7t7dKYMwp1zN7C9aJF8Zead7GYjBIEzfzzFje4WJB0l2l5V_tRN2XIRu3UtwlbgxYEEkHcbinu2LmvrLQyxBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
10 گلزن‌‌برتر‌تاریخ‌رقابت‌های‌ جام‌ جهانی؛ لیونل مسی به رکورد تاریخی اسطوره ژرمن‌ها رسید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24063" target="_blank">📅 17:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24062">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivOv_dMO4yXabDKUcQ1eStjF7KUQy-yfQG_By7uuzMxYxXqkyF05nSOcts6qc3hjzKycUCrr8syAkcIu-yUeSWOPzKM1t-eUHxnLDlzkzL0foNMyH_tXxuOAbajg7dWH860JeFpyAwMfq6gCKz_qvYNxM0kw3IWGxuFJ2rauQ1IJYE-qt-7QVYrzhh0ImkE9Fty-gbpVdzx_5mXSam9fIplcJe5MDIEwGySTX55LwECZqtjlD37FCr-IJf42Ip5jijWh3Vbz1BiqnsBZsr_duOOgoLcLZ9otEVrpiXDiOymf0u6zAwN1UjYEvUeNcbeq8nh1u2JS28v7GQiM-y36Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی وینگرآلبانیایی‌استقلال با انتشار این استوری‌خبراز موندنش‌دراستقلال رو داد. مشکل پرداخت مطالبات این بازیکن برطرف شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24062" target="_blank">📅 16:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24061">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f988706b3.mp4?token=OI_UpdMDZK4vOhKUaWKYNMn-FyHsQ6Jaqf_77CQ3GL6Yr4fxy1Uwwe76ypmDiTmYdwa4VVrIw9w-I9r7QnoovujSC1tOzebIphKt0UVDkeWSWnW5wgVSvFJ1w_e1WetcNvKhx11lgf0yAaxg3I6m-LeGzlvzC4e45hqFJ5DN6Owt05yZKdgNSTEOd6Zih6OinnBw9jAfnwlKozr0D8jfR19ObPTP2XN4D1GV4uunBQSZw_0CIWwR9FjgflPbUWP6oLdQjte7_MAyTG3v6qH6TDy3RaUcFs4y3RzDIjaI17Tt6fAQGp61MlvolzaSSzabLrHxmFW_xy9uq2gmXbTr6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f988706b3.mp4?token=OI_UpdMDZK4vOhKUaWKYNMn-FyHsQ6Jaqf_77CQ3GL6Yr4fxy1Uwwe76ypmDiTmYdwa4VVrIw9w-I9r7QnoovujSC1tOzebIphKt0UVDkeWSWnW5wgVSvFJ1w_e1WetcNvKhx11lgf0yAaxg3I6m-LeGzlvzC4e45hqFJ5DN6Owt05yZKdgNSTEOd6Zih6OinnBw9jAfnwlKozr0D8jfR19ObPTP2XN4D1GV4uunBQSZw_0CIWwR9FjgflPbUWP6oLdQjte7_MAyTG3v6qH6TDy3RaUcFs4y3RzDIjaI17Tt6fAQGp61MlvolzaSSzabLrHxmFW_xy9uq2gmXbTr6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
برنامه‌دیدارهای هفته‌دوم و سوم تیم ملی والیبال ایران در لیگ ملت‌های والیبال؛ هفته اول تموم شد که یک برد و سه باخت برای شاگردان پیاتزا حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24061" target="_blank">📅 16:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24060">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPQy0QagbA1PFjUx23df6bVqEYgkyXEIHna2EZ7heP6kFNreoRz01T5KS8MdByPwuRX3nIQsyr9X2nBkt1SXKmsh4Ku9bd6o1puykwxGM6_QUyuPSc1yhq7XfxrliOqd6pzski4NYL_EQ21kaYtdwlG_bNHvdHPOOJ15ZWJ7OcLsGmUNtEmu8QF1_ACIJh0TxnyXs219yuOtwG1W1oP0srm-ObDKs0ZZOUGzqgUWHgm0IMyiPqtIjcmKk5KHbJH0J4UHnUBw0GnFlx-jkV5taj3yj7HHZlh4vsEqmwlw42oC4wcbpPIK_r3Jnjxay5yTbe2ZXdprgJKcAcVOE0uj2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24060" target="_blank">📅 16:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24059">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRGzPV6lNx9xdr6ynNxjxehnkNeLJlXqexiCmemHHl-BtbbV4xke7QKKUlW6dIEKgpuGKKqocVRCuhbGoLa0zX_ta8GbWNCdC1eDF9SbbLEebkT2fT-wGacpSbtoeHMW1FZP4vOKJNU-2Fhw0LZnOZhrtqH-uG-USwnHvWbrLjz1GcazAZL7o1B2YU7tRvYrCpIA0FLfArN1sVfER9uAZXk97el-1JxxEKTktjMiKor3IgaW9A0YQkLCIebdzf4Nwgb0Xf8UVJrHdpAXKQ7mxqb96CjO0iQ6oB0fYmMQKkzwCfflyulVzQasgHm1lEWCx5MjQd8ylv7L-FdTzY9yxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24059" target="_blank">📅 16:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24058">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozHBKUXzNC_w1EZnJTXA7Eexn_Mcsh2X7whnnQZCZGuRYLDXirOGQNxy8pZ9QsAIhzCCZwjhd4e3gLnVuNahMHDRs5BIK5afqHecHROCUZjb6X3j7mYNoclh-TdwC4vT000CxjNiiYk521RyKajudHMQtiTbA4jPFzdLB-YB6E1BuE1SkxM_ZcZm3c_taLzXJY4WdlpsNQUrvM7uj6d4Khq1zJWF2sW8-NFFHycp6T0Ht9Y_wf33NPp5uAWJvNFTXEK2rvT9TJwGbWAfpmNzGFVCT8z9WOOIdsJyY1ekOrq9oBnWo-jK3ovyZA8uMH5u2rmTAPkvbaLOO9_nu2HZlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تمام‌حالات‌ممکن برای صعود تیم ایران به مرحله حذفی جام‌جهانی؛ازتقابل باعربستان تا یاران امباپه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24058" target="_blank">📅 16:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24057">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POxy5Ty5G6b7Eg3gFvS1DVfPDvzGEBIejLaCj2rlp3A3j7hMviTW9TXHek1_6Gn6W5nO9V6VY0eAop6AuyKqiSsvszfUHDd-R6i34HQHCG5p2AOheugWyMMwnm-Jp-9fVOb6VAiLsG8PeGw7hM5gwvZhe1nDh3M8WkRfgBg1RrtMnLfz6SXj8WtjsNBUPiOo44GSwYFgpdsfRlW5qZszdg4OIqkPu4mD5cTZjmhLObp4L0QaESNWihGJ6ZX0g_NGJH69oYAMP8S7fpJiHR-o3YJhuoqe0LvmQ0vKD_6BAIr_-S9LcEdd2iWjwkMyEnSDmuoIMatG_9z0OsOEM74SCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی درمورد عملکرد علیرضا بیرانوند در مقابل بلژیک: این سری خیلی تنگ بود خدایی
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24057" target="_blank">📅 15:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24056">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2fba3c01e.mp4?token=PW4Al-o36oQJSSm5lEhdHg-8jZBPV1dDYLDlO5oScAKYfD5hiYVI4cxbhfYUnov6PjUEfoL08szQXC6_YZaq4kGOEgKtN8LBdGOHLavJH2Iw4FniE0wOPCaoRoxq3H9VpBKTX_xlhvA6o_FRkM1XceMPi90ngUxdKnBDhq-vp_UHn0VKl_5djQUbP9XW8HYGXAHRlmI-tzoS6xsIpavJL3BGBFz9br6amhWw50SgzJ4n3WR6_xOEgXdrHGQwlPsWe0bnIVLkwHLzXh1FqLvwFgVOrFt33JOK7-aM3KPUU8Z-oobL-JnSDVZCfSpQdK4j2vP3cuFdTywEBdOvbc49Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2fba3c01e.mp4?token=PW4Al-o36oQJSSm5lEhdHg-8jZBPV1dDYLDlO5oScAKYfD5hiYVI4cxbhfYUnov6PjUEfoL08szQXC6_YZaq4kGOEgKtN8LBdGOHLavJH2Iw4FniE0wOPCaoRoxq3H9VpBKTX_xlhvA6o_FRkM1XceMPi90ngUxdKnBDhq-vp_UHn0VKl_5djQUbP9XW8HYGXAHRlmI-tzoS6xsIpavJL3BGBFz9br6amhWw50SgzJ4n3WR6_xOEgXdrHGQwlPsWe0bnIVLkwHLzXh1FqLvwFgVOrFt33JOK7-aM3KPUU8Z-oobL-JnSDVZCfSpQdK4j2vP3cuFdTywEBdOvbc49Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد خیابانی چرا اینطوریه؟
واقعا دیگه خیلی عجیب شده، یه‌چیزی میزنه به حضرت عباس؛ لحظه آخر قیافه خداداد عزیزی خیلی خوب میشه
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24056" target="_blank">📅 15:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24055">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5-Hg-AVaIWUWqEaA7X5u85Xo9l65ugWTfqtgyTPgisrJTddzKa1AGOHDeCHgbwsWnWGbxhpc54qe1lwN6Xs5GflVVK45UDBM2SZgw6Q6bPphvX80d3-y9_TL6C7N1V7nHD0zLKWCvrT4Ugm1yPiFipu70ADbX7XVE_byxsye6LYmNVaSBiQInf6oCqiZL6caXj01hgTrx2z13xddngkfl_R_dE70C0ldzZSKJxa-37KBgeZXoHaImQ7mCX16DbiVCbBeQTIdP5kk7k3lnsQtRtH_A0Kjw2L-fY85k_YCeHKhgxd937iz-u6rdZQ-ginmdwXQIyYZun8p5d0gXgNmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
#تکمیلی؛ علیرضا بیرانوند با 7 سیو و کسب نمره 9 ازهواسکورد و نمره10 از سوفااسکور بعنوان بهترین بازیکن دیدار بلژیک - ایران انتخاب شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24055" target="_blank">📅 15:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24054">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6565fae72d.mp4?token=gJ1oY24b6IDDWzctMzZYGS_pzWDFU7Su7N77zeY9KDYLCdjyK-Y3W_1wvuoAF9F0OGfL0GMKp_gs0m2DLGT8qj5-FZLBJmvZFf6RvUzPkS1WS3o9LtVwyKu9OAZf8pccR82Nk3Gidw5xWx19FZsaxNALDRe8FO9VDEKXeLqWdtPl70GtBeMVwGp6bHVcPo8mZ1vzMlMSVW1tv0F7ZmpERo6Q8AjpCp7CXJ8j2N-cgsmal14T0vL1BMOzhttOyA8djMzCy6ncx4BaK4V20P-iIcr9ZrirAZa3ren69wMdjxaqktIeouPs8oIbR-p4v2oz_BJZGl7lEDI5rT-CSLT38g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6565fae72d.mp4?token=gJ1oY24b6IDDWzctMzZYGS_pzWDFU7Su7N77zeY9KDYLCdjyK-Y3W_1wvuoAF9F0OGfL0GMKp_gs0m2DLGT8qj5-FZLBJmvZFf6RvUzPkS1WS3o9LtVwyKu9OAZf8pccR82Nk3Gidw5xWx19FZsaxNALDRe8FO9VDEKXeLqWdtPl70GtBeMVwGp6bHVcPo8mZ1vzMlMSVW1tv0F7ZmpERo6Q8AjpCp7CXJ8j2N-cgsmal14T0vL1BMOzhttOyA8djMzCy6ncx4BaK4V20P-iIcr9ZrirAZa3ren69wMdjxaqktIeouPs8oIbR-p4v2oz_BJZGl7lEDI5rT-CSLT38g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚪️
نمونه‌ ای از وضعیت متناقض جامعه ایرانی درحاشیه بازی شب گذشته دو تیم ایران
🆚
بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24054" target="_blank">📅 15:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24053">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kqohgn11JH1Rsj7hrxbH7Iq-oRdlBDBFpcThCfJGFzdBdR_Gzx0dwGiE_4M7NcIZ9jr9tBKb5wjst1zKDgDsr38ra7_ZYL3f9dU4q-YkJtDucyfWH8fUZKjOc2r_atxMsaxRThTgTinRAODfVxPf6t2rWnw4IUgvqS4Wk2lZHtAygoftgMbGHScInOE5kT6-PiMl8L8TIfchWoEztKvcjCl_XxE3R52Au4nxAYbGKpWTCstA5M1orRC5Hc0A64TuDpQKPgtJlc5bfsPad4osh6EFXiGWCFOgl6dvsDITLuUdHPYXvJMNx2cwmIVXqxFBdKRVFEojG3DPOGCPxjqizA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
استوری معنی‌دار اوسمار ویرا بعد از مذاکره باشگاه پرسپولیس به دراگان اسکوچیچ: خدا همیشه خیلی خوبه... متعهد بودن، حرفه‌ ای بودن، با دیگران مهربان بودن و قابل اعتماد بودن یک انتخاب نیست، اصول شخصیت انسان است. داره به مدیران باشگاه تیکه میندازه میگه وقتی با…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24053" target="_blank">📅 15:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24052">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1Ep7F565AsOYYONFmkotMBbEk62OoBwsifvk-6GAAidHPV2ptULuL8mU2dETMojzFG5nbafb5yAxP0RhWgRuemPJW_Ldx2YLR9UFAWvf0uakYAnUCq8ljjHHktHJODuO9Ar8m_BHAvV17OqAnmqR5nWnVldCn1l1kDz0mhcjeAg7HrtxY92ejo8_FPhry88Ej2fpPZwhDSgAWbH_enPwDKhtgNt8kcpB0GWW9ljz0jCc4lDU7moHYd3bQT7aTAbqRp1AhrNS4XWGnsX78-a7yDwgYIXS3bageJwR4atV3Y89aqwdjxZ8XMYxMlJjR11iwcchc-IgMKFGU9nyDQopA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24052" target="_blank">📅 14:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24051">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJo2AAby9iKdy55oO7r1pr4IJXFOVukHyD9HpXXXHq1tPKD19tfCOI_kJECtdOVHNvVxLovsPLzlmcQFGIcEs0Wp8HsF1XLgZKEmO7ukfXare6VGYpD0M9HnQbADL1RtBPD0HmgoHd-1gkMGdWh9kxhcv3MumNTeOB3Ib97aeT_dOzdlyD4GC9Z29_q1jNVQfIOvrs_4j_OcMVgBL3XGBWivq-5EXvOYQyuAscdllb_M2Y_cdFvMsPxZtl97AXePKcCc1sNwQLizk1HnR08pb86elKyCkZqOBRfJxPfgyvKpQG2iv7KsB7Gt73xQCoEND-vQKI-KCRsB64pV52OfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
در آرژانتین یک دین جدید به نام مسیسم متولد شده؛ این دین جدید که پس از قهرمانی آرژانتین در جام جهانی ۲۰۲۲ پدید آمده در روستای لا اسکوندیدا درایالت‌چاکو آرژانتین درحال‌گسترشه.درحال حاضر 3900 نفر در این روستا زندگی میکنند که مسی را مقدس می‌دانند و به آیین «مِسیسم» اعتقاد دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24051" target="_blank">📅 14:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24050">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚽️
از دخترانی که اطراف ورزشگاه‌ های جام‌ جهانی هستن سوال میکنن که جذابترین فوتبالیست کیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24050" target="_blank">📅 14:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24048">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvgHZHZfKivfSUQ7gis6kHoaOOHJhRtFOoUaO6mJaVBHEAdewr-JiThS10lBySwebpkbFlglIs7jU7znvoWAbvLSXQSFd8wCBBdo40CtLkKd8HZKPTR-cyFMq2-dEhrivD-WwlCctmJC3vyVA3oOTX4zSiIhA7wMSdZ1vMC9JOjRA2SgXuEtL6mXZ_oa0Q4voYfKlZOif1EYlHljqCCyirCDe9M0X7LhUcVPc9WbrsavAlX-O7n5jJ0HHJSRCrATiRzWmXQAAutFp2bO4DXMXC7EORylOVOoCm1KqPvqk15Sg9ScixSO8tfJxWqKkGSIdDgrUjZ5PPY9nr-Tethelg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ علی تاجرنیا رئیس هیات مدیره استقلال ظهرامروز با محمدمحبی و ایجنتش جلسه آنلاین یک ساعته‌‌ای داشته و پیشنهاد مالی بالایی رو برای 3 فصل حضور درباشگاه استقلال به ستاره تیم ملی داده است. محبی ضمن تشکر از پیشنهاد آبی‌ها اعلام کرده اگه با تیم خوبی در…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24048" target="_blank">📅 13:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24047">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLzSUt9RGQopXrQt47UQ5i2te85tE3UCMgVDc-HQR-MmbIH4ksgdwKsXDe3ibMT11Z6348YupW1RllK0HgxHM2lZn_mXHJW2Mr79Z2zm6IJnBGAdLj-6MgZfAiUjhaNh19gfrShyiyDYIhHE9V0VyOgTfEp76eREXZUn6Vrj7Y8foM9PBzatuW1FYHn__bdGRLK5D7DRmAT-CcQxN9PlflLmAZERDaTz3sZ9SdvIrzE8OOQovA3Ov48_mbSQ-2Hs9MPKuu0P6JzinKqUs0f1G_kI6OPzvoCXmuFJuyQ8SXbaESf8kbF5a5Zl2id49rKp0amGhziYP-i_D_DlxgpofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تعریف و تجمید بوفون از علی رضا بیرانوند:
قبل‌از این بازی هیچ‌شناختی ازش ندارم اما عملکرد درخشانش در بازی شب گذشته باعث شد که راجب او تحقیق کنم. انتظارداشتم او دریکی‌از باشگاه های اروپایی بازی میکرد. دیشب فوق العاده کار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24047" target="_blank">📅 12:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24046">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNvsFJE4j4uwkKPNldgLjrD5ECgt62TeCURhbktDAGpuGF_egY2oIjMPwioEYdl6Ny3_Z8t0SaO9rpfm-6e83G3ihEolrUwl6I-teymwTU_OKPEkbzErT8bgLUhHLwtkXytXvRQ34if3tVuhsBmFAuCgifGleM7oPdm1tDvKylRpEVQJ8eiKuQegJEXTsxZhkZKAlePr9RHsMdAumHiGbgrhpW5l1UrY0lc77YbpmqhxurTyZdEGiq0B5l3n9IZzDUelOibFAbc7QVMdqeoKIDr1Ou2opawy4PT1rN2btOrYi2wimxjW7g9Rn89NK5ZpTikVcs1o5J6ihqlpMzkjOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24046" target="_blank">📅 12:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24045">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnCfwtG7HSAU_L_u1xlXSpAi_-B_kJ55GBxhlISsXWd3XtyvJUsI1CnTz0n1jKH4Q_MVOVDonmqkCjT3O81AHdqvMLLF0OTmFyuTwzy5FiRjwB9BVmGyvLU9GwmRR-VqN8Eh53N-39i3PCXrRXxEIk7ajbnhxmxkDJmZsJsuRlZPP6WzqQif16h0PD3uD3BWbHLkXbfntFJT0IC-PULuVa62QA5boXy_i6v49Kbc6PWkUgjGnC3uYDrWPPmk8zFIgmv0V9By0zEwVE1x8EegcBfrlp4bh-w7mmZ2q2c0vvpkkwhRY069ElM2KdZpgvuON9gUTpvySRZMy0nFAuBQ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه پرسپولیس طی ساعات آینده مبلغ توافق شده رو به حساب‌باشگاه‌روبین‌کازان پرداخت خواهد کرد و سپس پوستر کسری طاهری رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24045" target="_blank">📅 11:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24044">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhqMesf6s0-8TZcuJskB9Z2SuY_9FM0SSU0rwTZktAbl2V2yznG7368oWNzUQ04nIOTr11y5BvNCtgDk7k6S3FBNDZEt_DYSdLiaUCx_zGDgOpDDoHzAYsANDHg2r__5rhENX4UpEbeRqJFkszo8Y3vyKmWHAg7pUkpPlnPJxo6l_peLPU5CYe6XP3-8x-PheMNXZOKEqXKF1KZZlfxSWVA8UQcEUQ08ihDtkZMiSOp0Yli9c_bCsyAozhRlhGfjijLW_8MPOco1gwYVhZpuUyjfmTnGlLIX3nbYGCM8GMxO829naIXdluttlSkJIwYXsQMHh3wL5jmjIzmgw5jrYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورزشگاه آزادی از هفته چهارم لیگ برتر در فصل جدید دردسترس خواهدبود و استقلال و پرسپولیس بازی‌های خانگی خود را دیگه اونجا برگزار میکنند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24044" target="_blank">📅 09:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24043">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I82VvGg-QI5XecI2Ve9-3ojwsOtj_HfUH90HkCxT_GPH_QMlTJTgVFJjwPLzsyBvwpk5_36fRcj3Q3FFmpzSfjzDEQFS4n7XpjjmJ496dfZQ3VXz6vBSBmm380dwHxjF5AB6qM2RtcgwqaLK7ELjMzryzehBcMWqRLi5MHs__rYCYiFaJ3kormuliFD9E072Sk6Fz7RBka95QZ-gg5TZsa4HDLJbTTGa-9dDbr_ICIVGmq5_bt0dFBKD-2d94JAqgZuP5-8j5f7Fu-sM8IaL2bLTCbtZiMP0zt03L_ctQd17O1gLY4lYDbQOYjyokCptsdhR4PHkqnANpoIlt1GecQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل مرود ایران به بلژیک از نمایی زیبا و متفاوت ببینید؛ جوفوق‌العاده ورزشگاه رو هم مشاهده کنید.
‼️
اگه‌که‌فرم باسن مهدی طارمی دقیقا مثل سهراب سپهری‌میبود احتمال‌اینکه‌شاگردان قلعه‌نویی‌ امشب شگفتی ساز میشدند و بازی رو میبردن زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24043" target="_blank">📅 09:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24042">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpasLMuwjs7cxNuayg70rib6fsKMkqO_C3QflaCAua9t4eq1jQRIPDRGDKPW7jyF7m9d2cuEKWkwq0rnWg7QbYGNguwgD1Sa9KPM_CeoxImAgntf91xZZqHXUHW4vswnHdkEcLtOXh1WoAjvQZJ3tEKA4U6sIOnVw7opLCV_GmU4S33syHezMo4on9AotfmzwD0g6WrTq3OwW_l125JqNDbAC7W_74Hf7nc-dOL6RWiuEqXhrdpz2RgsE2_cHhMnFxOW0l9kRfOGkB5fPjaVqdxE9xKTkvcZxxSFi8_fmMi7iFpgZPwgDOH_v76gNkadbTHqAhe9Z9k6PiINDvVa-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24042" target="_blank">📅 03:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24041">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSZeBOCkzd8pnsTSfaaIZQ5OW6XhQSVXxIPJgQwynM3mNvlw3UN5fuilG0gyuvv0YCRc3396si5gUptJbpw-AeT_KJCmWdpiHKOwV3mlj8nZxmYm4sUv37fkTjL0aHbeOghKJhpmjZPvX-ZBJfC-Y9runOP_nk80BvIGmbinF192NHed80pMTlSF0v3Vv9rtBkrrF_F--NBsJ7bVCE_o6vEidbOdon0-Tt-wtUqbw9cVaHKoNYumSgHzwSNvalR1R6zyYVepiEnLC0I692bMloXdVs6N0WiagGgfmipfmKnJJ8fsNu2qciSCZ0h5XIS3Bg7X5x2e8bdaszt5p0LM7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24041" target="_blank">📅 03:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24040">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⚽️
گل مرود ایران به بلژیک از نمایی زیبا و متفاوت ببینید؛ جوفوق‌العاده ورزشگاه رو هم مشاهده کنید.
‼️
اگه‌که‌فرم باسن مهدی طارمی دقیقا مثل سهراب سپهری‌میبود احتمال‌اینکه‌شاگردان قلعه‌نویی‌ امشب شگفتی ساز میشدند و بازی رو میبردن زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24040" target="_blank">📅 02:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24039">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e90d0111.mp4?token=IJH_cn0TzHgnLJCrP_yn8U9zsH_Y4YAjcxhzSq5eYKUlvn4GB8n0Nu5sO_bHKCfj9zn0oeEyFniPiiLYRCRFbqyHgQ73aRuye05JnVP2KBc_8I26OnbQPoMNRLlh_Fjv48bZI3So43YI-2uDRzui1MF9aUniddEl5EDGBVt8aDOkQQazwBcd2d-SoP8b-N5ESLqVzOC-g3Aq0mjn3cwdRiG28QgKooZJkPoLzsAhJv3OaU19cb0vW6cXbdoqgQn2r1VkNT7HcaeXHHw1Y4PaviUxKRiaigJnwteXqLlCiI8vYab04zyZQWbnj4fHMjxcwRn1l1RvwREhULq3S3IFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e90d0111.mp4?token=IJH_cn0TzHgnLJCrP_yn8U9zsH_Y4YAjcxhzSq5eYKUlvn4GB8n0Nu5sO_bHKCfj9zn0oeEyFniPiiLYRCRFbqyHgQ73aRuye05JnVP2KBc_8I26OnbQPoMNRLlh_Fjv48bZI3So43YI-2uDRzui1MF9aUniddEl5EDGBVt8aDOkQQazwBcd2d-SoP8b-N5ESLqVzOC-g3Aq0mjn3cwdRiG28QgKooZJkPoLzsAhJv3OaU19cb0vW6cXbdoqgQn2r1VkNT7HcaeXHHw1Y4PaviUxKRiaigJnwteXqLlCiI8vYab04zyZQWbnj4fHMjxcwRn1l1RvwREhULq3S3IFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24039" target="_blank">📅 02:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24037">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzw9jrDCwwSdN2B5cPFaDGrJqrv7LSaahy7Lt0IkzX6ToyRF8q7QRNoRKEj2to6Tb2QAdy4pT24Rwy6hZ6lDrHb9CEaattUC6hOaLDFadwwC84UXkC2orSezfMKFxbfZbmJypu869ucWTsUpdn2gYOfj1kiGEqRBk-TIllQd1BsdY7hN05ckRLMfbHtcoQGcTvmUV_zwkbuhpTrdZHT_IAaKElMyK1simbzefTW-ZvvqM2-S2NM8Mem4Dq1UHAEZtWtWIBCyFE4uPEd-DtKk0Id0I_QqKxQkDjNwpGOPWPjiY1ErtbkmFTkqPzGOVvSA-dVbv2fGeodoWjBkks7rzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24037" target="_blank">📅 01:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24036">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfJDL_4hq5se_qni-LPjg0cldFwHByPsSkFM8ODzdOLJ4-Zm0EdZAn4p8wN32MRxs2_w6A4Tp1yl01xxcmMNVsEqyfwAuM75ZuCgpQef_-U42yxBWd2qt-SCkSRNFhoVW8K1_2KUOnH5ZlvOnNEpzVPk1W6Zui25beOWHrSPsad7LWqedxEJyS2RxliC2Kdh9ouLQzTOEV7dtDjQOwEK20AflEdpdHsTxP4nUdTaEioKEu-qADXfIKHD_AZTVGro3JDJueqsZu5ZTrw-orpf0a6SHUKMFrjKue08SUumdvw9W96gD0CBsVZml8Pfdr4eYndkmDENBy9hcjBUqLiQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
#تکمیلی؛ علیرضا بیرانوند با 7 سیو و کسب نمره 9 ازهواسکورد و نمره10 از سوفااسکور بعنوان بهترین بازیکن دیدار بلژیک - ایران انتخاب شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24036" target="_blank">📅 01:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24035">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d43c42ae5.mp4?token=oLU3AbrJHGsAuBe1bxgpX60mQ0V312z_dg8GYBJO1ed5tBXx72-PY13oGNIe0dZ7ilNjviz0U9fE1wEFpecbk1zver1vHO6PRxzsgCO3Cx3sorLOf8YEn9ZxNLgIELOBX1RVFpC_gd2fccaNnu7E7nuphVX9XlSE-qIz0SC7v9gexd8wIT8SFCSQOOKVyep1h-vqIriVg43e02EtUEckr8KnDzufUDmcA1e0j6sGjmhqIafL1dd1qu0YhnttfOt5unNBsi9tQcJuYUB2leD3n2JpwS1V1LOmKQHkARDDD3V-hs28L1iCUqIJCBDy_0m13Xvqign7BSk-GA8EaFh4tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d43c42ae5.mp4?token=oLU3AbrJHGsAuBe1bxgpX60mQ0V312z_dg8GYBJO1ed5tBXx72-PY13oGNIe0dZ7ilNjviz0U9fE1wEFpecbk1zver1vHO6PRxzsgCO3Cx3sorLOf8YEn9ZxNLgIELOBX1RVFpC_gd2fccaNnu7E7nuphVX9XlSE-qIz0SC7v9gexd8wIT8SFCSQOOKVyep1h-vqIriVg43e02EtUEckr8KnDzufUDmcA1e0j6sGjmhqIafL1dd1qu0YhnttfOt5unNBsi9tQcJuYUB2leD3n2JpwS1V1LOmKQHkARDDD3V-hs28L1iCUqIJCBDy_0m13Xvqign7BSk-GA8EaFh4tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
گل‌اول‌ایران به بلژیک توسط مهدی طارمی در دقیقه 27 مسابقه که‌افساید مهدی طارمی گرفته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24035" target="_blank">📅 01:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24034">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HevtzU3TDDjB7_esVyT9ubzEXlpP7yzFUrxcxm7Sjbz-wkI52_YmPZElz23k0EFNWR9_ymc-ee74J77RHoJCxUFMoiVWl8mY5scxEtwAHaRf3S7TXkokY1GgWR69_EMFhG-ORNfSwGI_ytd1BfLbqkT-_nO6v0NhKU7F-1RwK764PgoSdH4DTHNQduXQPmdjrdUeTl-WX3XLGyVwX6hRoDKCMrDAqncPBmz2uOQ7F21ls1uUA-otVrZJNmQ2vaOwX7e8StXZMptDx2TRWBfNZjsoEGTqAHoFPAZcyhjWj8oNbbtvy7R8BAyVQ5d_S-k8rzCHBdNhHwFo1mJBVgCOPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازنبردتماشایی یاران مسی با شاگردان رانگنیک تا جدال فرانسوی‌ها مقابل عراق
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24034" target="_blank">📅 01:28 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
