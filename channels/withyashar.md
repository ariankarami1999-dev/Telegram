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
<img src="https://cdn4.telesco.pe/file/o-kUhHuTEpuTxLvpth1ULdBpnNNrGgjX2HF9LBgg3Q7Fq9P02RxBhLIIgUkeJXJzkpGl1r9INUNsDlCveLyoiVlak2VPubzpkbRcukHUEFHR-j1uMh_VTElygDuaWMAOKdhTpjC2uDtT0QwfHyB4Y7ipG3MzYi3Y614W8_oGrqDxu8qvlYxFz9UlslDriDu7c9F3oeVR1clEv20x8ykABGtxcYAi1oDuakRB36vQvnm5mpKDWkMYEk4ZS1xVldaRBN-4QI7Xo3MksmqTcJ-8bsCLtzhN7bD1DWUFhFfFSnhlk-O10S-P3MFsrQ7_RoimBaUqQveXzKYLFXFGt1JxeQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 477K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 03:46:48</div>
<hr>

<div class="tg-post" id="msg-24625">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffd865ee13.mp4?token=VLKb0y6m9mnff3G8VfT_pOd8KYpe4ybRYZllrE03qJoYeYWjU6i10wCyWba8oV91Mg0sIL2G2tYTbcVpqEs2yeG4OwC3UrKDHMZVr6RhKK1j1Zpy5pWJ8-lgTHwn7lr3RxwEFKvQtJLydF3N3KhY5lbaTS5gxt2z2TYQSqMJIphoW5EcIVtCdU-mNd4m22dXw6JQbs9oH6rvotGqAIp_xFn9eSHgU4PIx61ssBIdpH5RzMgYOkFbC4nlBBruoTy7Inz2pvNJ_lj-ItBDyW_iNUwmRZDpKAUmyfzHmNPFgYmkKQQmh10UEcmIf0aprSeVwwbOoSzhbgqDLpZzo3MDeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffd865ee13.mp4?token=VLKb0y6m9mnff3G8VfT_pOd8KYpe4ybRYZllrE03qJoYeYWjU6i10wCyWba8oV91Mg0sIL2G2tYTbcVpqEs2yeG4OwC3UrKDHMZVr6RhKK1j1Zpy5pWJ8-lgTHwn7lr3RxwEFKvQtJLydF3N3KhY5lbaTS5gxt2z2TYQSqMJIphoW5EcIVtCdU-mNd4m22dXw6JQbs9oH6rvotGqAIp_xFn9eSHgU4PIx61ssBIdpH5RzMgYOkFbC4nlBBruoTy7Inz2pvNJ_lj-ItBDyW_iNUwmRZDpKAUmyfzHmNPFgYmkKQQmh10UEcmIf0aprSeVwwbOoSzhbgqDLpZzo3MDeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: الان تنگه هرمز تو دستمونه، عملاً اونو اداره می‌کنیم و کنترل کامل در دست ماست؛ البته می‌دانم که این وضعیت همیشه می‌تواند تغییر کند. کافی است یک مین بندازند؛بنابراین اگر واقعاً مین باشه، شرکتها حاضر نیستند کشتی‌های یک میلیارد دلاری خودشونو از تنگه هرمز عبور بدن. اما دوباره تأکید می‌کنم ، الان نفت بیشتری از تنگه در حال خروج است.
@WarRoom</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/24625" target="_blank">📅 01:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24624">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ: من با بی‌بی نتانیاهو درباره این حادثه صحبت کردم. طبق روایتی که از او و چند نفر دیگر شنیدم، کمک‌خلبان احتمالاً تروریست یا فردی دیوانه بوده که به خلبان چاقو زده است. خلبان با وجود جراحات شدید توانست درِ کابین را باز کند و فریاد بزند. هواپیما با زاویه‌ای بسیار شدید رو به پایین می‌رفت و سکان عقب آن نیز آسیب دید. یک لوله‌کش اسرائیلی که هرگز هواپیما نرانده بود، متوجه ماجرا شد، وارد کابین شد و کمک‌خلبان را با وجود فشار جی از صندلی بیرون پرت کرد و با کمک مسافران او را مهار کرد. سپس این مرد قوی با وجود نداشتن تجربه پرواز، اهرم کنترل را بالا کشید و توانست هواپیما را پیش از سقوط دوباره متعادل کند.وقتی از او پرسیدند چطور این کار را انجام داده، گفت برنامه «سوانح هوایی» (Air Disasters) را تماشا می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/24624" target="_blank">📅 01:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24623">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c9ea45ed0.mp4?token=lnyvoWQ4r9mFhupQo87EGQa99LQDwfpOoKaX0RIdz2s28BPAjYfZ_33OsvN5yI0hW2DjFlIUJ05FNR4ZRGV1w16bF9gtiTxBo5M5L2xNQLc-LY0eoorfxFalzRbRjVdoQb6-K1h3PdXM9u82L2QRkysxAK09cv4Cdj7EW-zP0lt6ZcSlqNk1dFQLwKkwC8jEezT3-AUZlNFKqGybGclFPsj62RUvMXw5dOjm1eN6mg_019TkJSJLwb8U3stG2juHeGABemvq9zTM2uvVmV1VzgB3Od1QKlRgjTcC3QjyT-4aFHgas3uycAYiruUXyN9Cz8EQxyvQgtfT5BzrUaf11w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c9ea45ed0.mp4?token=lnyvoWQ4r9mFhupQo87EGQa99LQDwfpOoKaX0RIdz2s28BPAjYfZ_33OsvN5yI0hW2DjFlIUJ05FNR4ZRGV1w16bF9gtiTxBo5M5L2xNQLc-LY0eoorfxFalzRbRjVdoQb6-K1h3PdXM9u82L2QRkysxAK09cv4Cdj7EW-zP0lt6ZcSlqNk1dFQLwKkwC8jEezT3-AUZlNFKqGybGclFPsj62RUvMXw5dOjm1eN6mg_019TkJSJLwb8U3stG2juHeGABemvq9zTM2uvVmV1VzgB3Od1QKlRgjTcC3QjyT-4aFHgas3uycAYiruUXyN9Cz8EQxyvQgtfT5BzrUaf11w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار
:
شما حاکمان ایران را دیوانه توصیف می‌کنید. چطور می‌توان با افراد «دیوانه» به توافق رسید؟
ترامپ:
«شاید آنها را
بمباران کنیم
. باید درباره این موضوع تصمیم بگیریم؛
یا آنها را بمباران می‌کنیم یا به توافق می‌رسیم.
زمان تصمیم‌گیری نزدیک است.
این ماجرا خیلی زود به پایان خواهد رسید.
»
@WarRoom</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/24623" target="_blank">📅 00:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24622">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16a58f7f7c.mp4?token=d6xqcVNgQb0WrdHAPk-IJMpoVvwZ4rkVI5QXreZYOASLqS7ocoKTRHvLBiM6ikB5IovACfXU5tWjANGM6eV6-jbLVaUbI8RjOIFbb8QhD-tfebdmObZFSMeyPPKjmK4BOx9uZ96j3sFFdeQgLl7xw4qx8ySzOPYwcl5fq7m20xp5EErpeWWBY5u5VNH8PwbIBA_xx7ozthGQ_8_UrEwfEK2iMC7_FHNajmKmYkSvbdON9nY6x_Z8nM6UqaURto0ngeoEkC81Q0awuNlqksdkSikj-c4nAEhXjgscIhR5RiRQi-Fkz-KevateMsR5BduLeDDJWuH0XAkB0VvVMNA6kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16a58f7f7c.mp4?token=d6xqcVNgQb0WrdHAPk-IJMpoVvwZ4rkVI5QXreZYOASLqS7ocoKTRHvLBiM6ikB5IovACfXU5tWjANGM6eV6-jbLVaUbI8RjOIFbb8QhD-tfebdmObZFSMeyPPKjmK4BOx9uZ96j3sFFdeQgLl7xw4qx8ySzOPYwcl5fq7m20xp5EErpeWWBY5u5VNH8PwbIBA_xx7ozthGQ_8_UrEwfEK2iMC7_FHNajmKmYkSvbdON9nY6x_Z8nM6UqaURto0ngeoEkC81Q0awuNlqksdkSikj-c4nAEhXjgscIhR5RiRQi-Fkz-KevateMsR5BduLeDDJWuH0XAkB0VvVMNA6kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره ایران:
«
رهبران ایران به‌شدت برای حفظ کنترل در حال مبارزه هستند، اما کنترلِ چه چیزی؟
»
@WarRoom</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/24622" target="_blank">📅 00:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24621">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76e3f894e7.mp4?token=WyYq0-LyhRcugtdXymgHnQDea_mw5lDugjCfEghPNP7cParNcWK8OeQZpH1a1wkDWC_Jem4yy7OrGMbN-p32QDJXL_zaytvSyV2g21vUDUuWRyjA3sYP2o5PWlxafE2vidPfT1k713JIQs3VQEbSy5B28gBeb2nHtOHh1YpCuf0dRP9dLMsQSG6yIaz-rIAK7r1ETHxM21_NdX---OcASA50AmDCS33aSdXdwTdX49Ht27MNGC6ThH-h5rMOR1ReW-KWrjqsgIBGdWPDyKBDO9Z4qUhJh26KMp9hHZ_qbwy_1mk3eO0kHPWbSRI-EXatiQ0cHPBi2FO267QMpWSYnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76e3f894e7.mp4?token=WyYq0-LyhRcugtdXymgHnQDea_mw5lDugjCfEghPNP7cParNcWK8OeQZpH1a1wkDWC_Jem4yy7OrGMbN-p32QDJXL_zaytvSyV2g21vUDUuWRyjA3sYP2o5PWlxafE2vidPfT1k713JIQs3VQEbSy5B28gBeb2nHtOHh1YpCuf0dRP9dLMsQSG6yIaz-rIAK7r1ETHxM21_NdX---OcASA50AmDCS33aSdXdwTdX49Ht27MNGC6ThH-h5rMOR1ReW-KWrjqsgIBGdWPDyKBDO9Z4qUhJh26KMp9hHZ_qbwy_1mk3eO0kHPWbSRI-EXatiQ0cHPBi2FO267QMpWSYnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار
:
اندی برنهام گفته است که
ایران در حادثه پایگاه هوایی RAF فرفورد
نقش داشته است.
ترامپ:
«ما در حال حاضر در حال بررسی این موضوع هستیم.
خیلی جدی در حال بررسی آن هستیم.
ایران در حال حاضر
مشکلات زیادی دارد.
»
@WarRoom</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/24621" target="_blank">📅 00:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24620">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93e19363c.mp4?token=e7RRS5Bxc76YN07aGs4pxLhBOSsvilwn9cztcPXzkCB0WvxgwRpiikS8zLx4Rh_VgeKAKve_i8qz7WlIMbpgJeReR4jIp3_wFJO5B9gfXzeN_25fjrljE6wx7ObkZqGG9SSlMsozotUYf8pjHMUA7yFAPEGSCcISPCZTUEFiE7SoNBgCCRUbwJy9sjaoIz1GmlN-xoIQ5buFV1nZCnvndIQpeZaJTMiBJxiK2BWrzB6-6Ct9FpvpB6lBZNs5nXbe2zr0TM8WjR-xIujEdICAV6NTw8HgR2MsmwlnF-AE1hze9CCJGQohUU-rG9ZKxkrpHj1xjyeEumB6RXYTJWVddQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93e19363c.mp4?token=e7RRS5Bxc76YN07aGs4pxLhBOSsvilwn9cztcPXzkCB0WvxgwRpiikS8zLx4Rh_VgeKAKve_i8qz7WlIMbpgJeReR4jIp3_wFJO5B9gfXzeN_25fjrljE6wx7ObkZqGG9SSlMsozotUYf8pjHMUA7yFAPEGSCcISPCZTUEFiE7SoNBgCCRUbwJy9sjaoIz1GmlN-xoIQ5buFV1nZCnvndIQpeZaJTMiBJxiK2BWrzB6-6Ct9FpvpB6lBZNs5nXbe2zr0TM8WjR-xIujEdICAV6NTw8HgR2MsmwlnF-AE1hze9CCJGQohUU-rG9ZKxkrpHj1xjyeEumB6RXYTJWVddQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما ۱۸ نفر از نیروهای بسیار خوبمان را در درگیری با ایران از دست دادیم؛ از دست دادن حتی یک نفر هم زیاد است. اگر به عراق نگاه کنید، ۴۵۰۰ نفر را از دست دادیم، اما نتیجه آن حتی نزدیک به چیزی نیست که اینجا به دست آورده‌ایم. ما در عراق برای نابودی داعش وارد شدیم و من در دوره اول ریاست‌جمهوری‌ام این کار را انجام دادم؛ به همین دلیل آنها باید مدت‌ها پیش از آنجا خارج می‌شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/24620" target="_blank">📅 00:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24619">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c295dc969.mp4?token=gfU8I_kLfy8wgK9qP3qUgIXpPEuZ7b2DX6et3gGSMNKRLjwHdThCu2vU9NTLQ1h_i8E5Bms4f-8xcUnUtGgql74YfkBy5N0RiSTBXs-5X4nFW4ts7jl7LubbhOjkS1UXW8kYcnRrFNTS2Y5rKJXT7q4mD9oB3Qag9HAK6P_HqLHpc-BKTZOzKNYb9Y7_LFhII0OX3cKIelUV_goJk53wjar4ghnM9nIrxfbCelNhZSuFMN600zoWKaeJ37-kYjcr5cp1Xh_zVXNasI4s6QHcOrXEcFDzo4VSQ18ii1eISY4_mlNQjAjqgpAU0KqXtHiRikzxLjI2RPjK1rjiH2g0aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c295dc969.mp4?token=gfU8I_kLfy8wgK9qP3qUgIXpPEuZ7b2DX6et3gGSMNKRLjwHdThCu2vU9NTLQ1h_i8E5Bms4f-8xcUnUtGgql74YfkBy5N0RiSTBXs-5X4nFW4ts7jl7LubbhOjkS1UXW8kYcnRrFNTS2Y5rKJXT7q4mD9oB3Qag9HAK6P_HqLHpc-BKTZOzKNYb9Y7_LFhII0OX3cKIelUV_goJk53wjar4ghnM9nIrxfbCelNhZSuFMN600zoWKaeJ37-kYjcr5cp1Xh_zVXNasI4s6QHcOrXEcFDzo4VSQ18ii1eISY4_mlNQjAjqgpAU0KqXtHiRikzxLjI2RPjK1rjiH2g0aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست: رسانه‌های ما باعث می‌شوند رسانه دولتی ایران منطقی به نظر برسد
@WarRoom</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/24619" target="_blank">📅 23:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24618">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خبرگزاری i24NEWS: در پی هشدارهای منتشر شده , رئیس ستاد مشترک ارتش اسرائیل ، سفر خود به ایالات متحده را لغو کرد
@WarRpom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/24618" target="_blank">📅 23:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24617">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وحیدی: اشتراک چت جی‌پی‌تی مقوا رو از پلاس به پرو ارتقا دادیم ، علی ای حال فردا یک پیام خیلی مهم منتشر میکنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24617" target="_blank">📅 22:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24616">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJDQQBFzLR62SHeliR_lPrkAo83nUnFbI9R124gMfYzGaCDVX-W8xnk4dHzW9LUXh3Lb516I8tcwFP0DJGj1AKir2JE442z1dH792CKNeVrfBgozOvO2ClSdce_wZ8c2f_WhqoM-ypqetc5sPL3UiyuQrmZno3oho60A6MJIsQJbAcXAM75xrErbT4BzAAvIhMkH0VXqcjd55pzyGb8ejMqvgZcPXVkk1TAcvzKlSEjBwM-UtO4B_rTNv7TfohVV51Cdty1lV-CRVTweFw5UkXr1GpHiuK3h6wAHPTwsRBUgtYA1AUM7lVthc3mbGgeH1ZJcZ12SecOo4STLsfcOfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : خلبان هندی ، ناجی جان ۱۷۴ اسرائیلی مسافر در پرواز فلای دبی شد!(پیشتر به اشتباه خلبان اماراتی معرفی شده بود) @WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24616" target="_blank">📅 22:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24615">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">روایت قهرمان ماجرا به نتانیاهو از لحظه درگیری در کابین: «فشار شدید هواپیما من را به سمت پایین می‌کشید. وقتی به درِ کابین رسیدیم، یک نفر با پیراهن سفید هم آنجا بود که فکر می‌کنم یکی از خلبان‌ها بود. خلبانی که مورد حمله قرار گرفته بود، بسیار نزدیک در افتاده…</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24615" target="_blank">📅 22:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24614">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f7a659bf.mp4?token=pA8M30UY3Kr5WfwulU73BevGn1x41DPpGfmRYQ_4Y3XwZvK-NdnKgvVKEwb_wrJFbwtkOPRfEm-zojY_Jxm_bGyg3haMS2ijomrRw5mubtknmCczOslBXQCzZxATvXmA16xkQAKgmcjahE36_uo8cud6Lyc0K4pJMnUs0hAZn0xy0dIX7LyUP3kuZ1ERox4IlZU_kAzC6w_GcLb3pECrwTtWoyeXPLNMxrZ1OpLcY2qk67mbBmKj8PckhH3ahcYaHuFQgIogzCs5D99ylUZbRmfRhWaP-VO-4hMhF4b89igdwDdSluluvAKGPF1Mcq5Gz5ER4m1pNGEzbWJ_x1o-fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f7a659bf.mp4?token=pA8M30UY3Kr5WfwulU73BevGn1x41DPpGfmRYQ_4Y3XwZvK-NdnKgvVKEwb_wrJFbwtkOPRfEm-zojY_Jxm_bGyg3haMS2ijomrRw5mubtknmCczOslBXQCzZxATvXmA16xkQAKgmcjahE36_uo8cud6Lyc0K4pJMnUs0hAZn0xy0dIX7LyUP3kuZ1ERox4IlZU_kAzC6w_GcLb3pECrwTtWoyeXPLNMxrZ1OpLcY2qk67mbBmKj8PckhH3ahcYaHuFQgIogzCs5D99ylUZbRmfRhWaP-VO-4hMhF4b89igdwDdSluluvAKGPF1Mcq5Gz5ER4m1pNGEzbWJ_x1o-fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارک روته، دبیرکل ناتو: اروپا نتوانست توان هسته‌ای ایران را از بین ببرد، اما طی ۱۰ سال آینده توانایی انجام این کار را خواهد داشت و باید خودش این کار را انجام دهد. او گفت اروپا همچنین باید مسئول مقابله با حوثی‌ها در دریای سرخ باشد، نه آمریکا. روته تأکید کرد که اقدام آمریکا برای از بین بردن توان هسته‌ای ایران کاملاً ضروری بود و پیامدهایی خواهد داشت، اما این پیامدها از این واقعیت آغاز می‌شوند که اقدام آمریکا ضروری و مثبت بوده است. او همچنین گفت عجیب است که برای حفاظت از حدود ۶۰۰ میلیون نفر در اروپا در برابر ۱۴۰ میلیون روس، کشورهای اروپایی به آمریکا با ۳۴۰ میلیون نفر جمعیت و فاصله ۶ تا ۸ ساعت پرواز وابسته باشند؛ اروپا باید بتواند در آینده خودش از خود دفاع کند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24614" target="_blank">📅 22:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24613">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c1b577539.mp4?token=pk-yWb9MhAVsDcVadOoSefYGRUytms_8kKgIHHcM8ofeCv0GF92d221fJsZTXb6X2g4gyt36zzFSo6D1YEo3N2H3FcOV0oo_sLtHrly0K5XSRCjeAF-vX1_cNBPqhGKY33C7Zzks-Ud9m64yC_ZC2wVR3blrEyvWSoaHMkNoE9uvsgJ9eEFWY72iY8FrqafKzxKs9BMsxgzKOerJAabhDudvsCewRyefW_rIMyixMsIqeTg0Ggk_WU-N-tWjraFUrNLmiaM4al0U7qIVchGO34X1J-o9kNUu49CReG8RtxkpNNYdGMM5_P0h7dLylepqsgy6hz71yXAA0HCVyYmFtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c1b577539.mp4?token=pk-yWb9MhAVsDcVadOoSefYGRUytms_8kKgIHHcM8ofeCv0GF92d221fJsZTXb6X2g4gyt36zzFSo6D1YEo3N2H3FcOV0oo_sLtHrly0K5XSRCjeAF-vX1_cNBPqhGKY33C7Zzks-Ud9m64yC_ZC2wVR3blrEyvWSoaHMkNoE9uvsgJ9eEFWY72iY8FrqafKzxKs9BMsxgzKOerJAabhDudvsCewRyefW_rIMyixMsIqeTg0Ggk_WU-N-tWjraFUrNLmiaM4al0U7qIVchGO34X1J-o9kNUu49CReG8RtxkpNNYdGMM5_P0h7dLylepqsgy6hz71yXAA0HCVyYmFtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: من تنها رئیس‌جمهوری هستم که حقوقش را اهدا کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24613" target="_blank">📅 21:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24612">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f09c19e00.mp4?token=D6nQwSDm4lv0nx3vI5OWDsekSbVN5RI8wL8z18nNP7FujyTq-L6LzJIc_s-gczFPX_NfK1oytSQJOpS-UderUKbMxzndesK5GoAN__Cpc4hZGgsoSeHXXaEfE-zK0PGLAGGR87Zrrw6f1CSu1LmRZHsrjld1WmXB3Ffvw9Cbiv5M1K0YEGOfOMHLPA30c7u6_Qc5aMR0sb-7A5mTgERWvxUJ85UAMOH2cyfrQmFWhKIfDblz-MM7RbIOLmjHTkEgUYXhz8lAb20d6XQ4eUJ_vxLBAXKR-8qOh9KRT0diryGeHY6DzsHqwdxLRqKVFxa6-_gsyA2uLnaZbjbZKA4MFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f09c19e00.mp4?token=D6nQwSDm4lv0nx3vI5OWDsekSbVN5RI8wL8z18nNP7FujyTq-L6LzJIc_s-gczFPX_NfK1oytSQJOpS-UderUKbMxzndesK5GoAN__Cpc4hZGgsoSeHXXaEfE-zK0PGLAGGR87Zrrw6f1CSu1LmRZHsrjld1WmXB3Ffvw9Cbiv5M1K0YEGOfOMHLPA30c7u6_Qc5aMR0sb-7A5mTgERWvxUJ85UAMOH2cyfrQmFWhKIfDblz-MM7RbIOLmjHTkEgUYXhz8lAb20d6XQ4eUJ_vxLBAXKR-8qOh9KRT0diryGeHY6DzsHqwdxLRqKVFxa6-_gsyA2uLnaZbjbZKA4MFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما نیروی هوایی آنها را از بین بردیم ، در سه روز گذشته، حجم نفت عبوری از تنگه هرمز بیش از هر زمان دیگری در تاریخ این تنگه بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24612" target="_blank">📅 21:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24611">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa854dc852.mp4?token=GDoNBX9-AKN60dRhvg2ZPfEdmc1yzBp1_y8slxd4ZtlErYNyiPkY8_Z5d34xCZ2R1SdzQxSgjkFVP6iYhuTEjwGbXlrDOGy9NyJkUeFa3JfIjr5e6XAbNzoeOpy_GdMrZO5kl3PzYBD-TfRoQoBs56beIT7dGu_vDQmARK0dHyE7cgRWHdyIbekepnssysR_3xCoxwXQ3vHsq-dgfLkwgo9-nHXYSt6DbAQSlAw3BrdX_As3ivw2afW9Mv-oQiRel5wVzj4zmSnG9V8AyI5T2hgbX3DecKTP9_0BTi_ZGBAZ6l82kUxOIY3Fvt1FsMpi3_JLBCo1TaE-AWMvdj4T4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa854dc852.mp4?token=GDoNBX9-AKN60dRhvg2ZPfEdmc1yzBp1_y8slxd4ZtlErYNyiPkY8_Z5d34xCZ2R1SdzQxSgjkFVP6iYhuTEjwGbXlrDOGy9NyJkUeFa3JfIjr5e6XAbNzoeOpy_GdMrZO5kl3PzYBD-TfRoQoBs56beIT7dGu_vDQmARK0dHyE7cgRWHdyIbekepnssysR_3xCoxwXQ3vHsq-dgfLkwgo9-nHXYSt6DbAQSlAw3BrdX_As3ivw2afW9Mv-oQiRel5wVzj4zmSnG9V8AyI5T2hgbX3DecKTP9_0BTi_ZGBAZ6l82kUxOIY3Fvt1FsMpi3_JLBCo1TaE-AWMvdj4T4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران : ما کلا از نظر نظامی پیروز شدم ، در ۶ ماه ۱۸ نفر را از دست دادیم، اما آن‌ها ۴۵۰۰ نفر را از دست دادند
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24611" target="_blank">📅 21:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24610">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d8d88008.mp4?token=DP4TdEp8-CHIH-On9AK_ZUFUX3EXtdwj6z2NtX7B3pPp_bUG8cgLdlTBpUxwVJBaQOROL-pH1gpy0ccxEYFADMc6mu-51Fw6hepBxftUgRT8mnFpbOTAwfr5pD23U49bqQoTJQfnBv_u0sCWPbi8KzQtjo0myqnWttK_Qw2NMfDkQLsn2iAWxR6iKJO5UiRmhdAVB4rUkwolPu2zbb8DOa0a-JkCEQ1F6hZ_RHyHgBW3au4--mF4NbfPKt1tQnzeDAqj0LOeEjqu7Z3RF_czGvnKQHmBOWYBYmN_tWaxnP84rbJfnGdF5uyAISQpC19PjAzndgjNZDAmMpryiO-ABg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d8d88008.mp4?token=DP4TdEp8-CHIH-On9AK_ZUFUX3EXtdwj6z2NtX7B3pPp_bUG8cgLdlTBpUxwVJBaQOROL-pH1gpy0ccxEYFADMc6mu-51Fw6hepBxftUgRT8mnFpbOTAwfr5pD23U49bqQoTJQfnBv_u0sCWPbi8KzQtjo0myqnWttK_Qw2NMfDkQLsn2iAWxR6iKJO5UiRmhdAVB4rUkwolPu2zbb8DOa0a-JkCEQ1F6hZ_RHyHgBW3au4--mF4NbfPKt1tQnzeDAqj0LOeEjqu7Z3RF_czGvnKQHmBOWYBYmN_tWaxnP84rbJfnGdF5uyAISQpC19PjAzndgjNZDAmMpryiO-ABg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما تقریباً کنترل کامل تنگه هرمز را در اختیار داریم میگم تقریبأ چون یکم مین پرت کردن.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24610" target="_blank">📅 21:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24609">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6830cdeb6.mp4?token=r7CKG9XDTxiUDFbVGkvmQbY0jhirkMXTn4V1SDuErWBdujw-f7YBl5m8fmQ6NjCz0CTV_zU-U3M9fKEnuF_nI50bu5FJW6cIUlHiJeUYxqkEQ406_4OIX2-gxIoNVOZcWdT670t6TiBPnCZcfjbP5FYVjjD7Fw5G784N1XNl0q7FyZnZ-a7exCbfk_si-DZ4G0zfhrvyGpEaSJy4SwkWbFLUM587OKW74md9pA1uFFIPzlLh8rsh8jMXqDQ2UXuP5cI8qucPrJPUn-aYdm39lrvfj6R1EsBGIayjoNwz88cCeUu6Clw_z2mtz_iHKEX1VS0BR7nsLGrKKPGrUaz-yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6830cdeb6.mp4?token=r7CKG9XDTxiUDFbVGkvmQbY0jhirkMXTn4V1SDuErWBdujw-f7YBl5m8fmQ6NjCz0CTV_zU-U3M9fKEnuF_nI50bu5FJW6cIUlHiJeUYxqkEQ406_4OIX2-gxIoNVOZcWdT670t6TiBPnCZcfjbP5FYVjjD7Fw5G784N1XNl0q7FyZnZ-a7exCbfk_si-DZ4G0zfhrvyGpEaSJy4SwkWbFLUM587OKW74md9pA1uFFIPzlLh8rsh8jMXqDQ2UXuP5cI8qucPrJPUn-aYdm39lrvfj6R1EsBGIayjoNwz88cCeUu6Clw_z2mtz_iHKEX1VS0BR7nsLGrKKPGrUaz-yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:خیلی زود شاهد وقوع اتفاقاتی خواهید بود.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24609" target="_blank">📅 21:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24608">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24608" target="_blank">📅 21:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24607">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de03a67f35.mp4?token=Ip4bL42B6by3xFLVqjUV2Ky2gvJ6mRcTLru-DlHRUNanF-Tw4Ur4BDuSDYVsa4aCX1ST2X3K7gltwz4jlwtLesOcKRbbNPQCn31yMZJZGjThYXOrCQ-ju-ksKS31-lAxX2EpFPGV8CK7KxDHvQgOZ9ifKg5kGNh40ATIxEkG-7rxKnbyo1f9gsmRUUPXeiVtSiikaWY5l1CjL2wF71r2Ew7S2WeyTvoU5kn2qvPW79H41St-yF0tqkYtCgtdFlfPwGAOPMWgfewrnGHgbMLGnZqdd1TYMbkcZhThwZMhrN51mmDxz7-ic_9Oi5Q_Q0FuYNND-gnk5Q12p9eXCc2Cmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de03a67f35.mp4?token=Ip4bL42B6by3xFLVqjUV2Ky2gvJ6mRcTLru-DlHRUNanF-Tw4Ur4BDuSDYVsa4aCX1ST2X3K7gltwz4jlwtLesOcKRbbNPQCn31yMZJZGjThYXOrCQ-ju-ksKS31-lAxX2EpFPGV8CK7KxDHvQgOZ9ifKg5kGNh40ATIxEkG-7rxKnbyo1f9gsmRUUPXeiVtSiikaWY5l1CjL2wF71r2Ew7S2WeyTvoU5kn2qvPW79H41St-yF0tqkYtCgtdFlfPwGAOPMWgfewrnGHgbMLGnZqdd1TYMbkcZhThwZMhrN51mmDxz7-ic_9Oi5Q_Q0FuYNND-gnk5Q12p9eXCc2Cmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره عراق: داریم با کله از اون جهنم بیرون می‌آییم.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24607" target="_blank">📅 21:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24606">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با قهرمانان اسرائیلی پرواز FZ1073 شرکت «فلای‌دبی» دیدار کرد؛ پروازی که صبح امروز توسط یکی از خلبانان تا آستانه ربوده شدن پیش رفت، اما با مداخله خدمه و مسافران اسرائیلی، از این اقدام جلوگیری شد. @WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24606" target="_blank">📅 21:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24605">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6e044a2b.mp4?token=Y27ihA5tSMocfeo2Ptw0S2KWwBTL-76zj81UOSY5eZo4ck9bvnYNmHFq0VW6TUw3OndMGm06YrR1SoJIwl7Ov1ddmuthu2wmI0f3ZLoqP-uCM52GkMDOCpMPmyi0eVSSBEhJVS-Y2lI1BisF_xCmppP76FQA9On4VWWqjUevZYXUam8AbxlSlFY1fjQG8lvvyBwsX1mdL5f3shRjtKx8KANTTWH8Ed2GOG7qJSNcyicC1qD-Saf1el52Tk_7h3Snb60ZNjxpFC76DHZGExfvfqANUkE-Q5ANTxLLntq5kcN0hwOlSRHM5ecBCdU8Of1-DHTznCynO2na65pXOtBLqk_G9jqg8Y_Na9idrPbu_tCn1s-rKztps5GNpnOfwCl2S7nguqZgv5MDbp59bNoytSwcnmXtweTL1pjoPaRbxmmJKoW6lFEHIUzzK6zL12W6SPLv58lALq_ikcdTepjIOzzERVX3eli1lfYrnFggNDzwlMNanF4bQNDJBSgQEEMH3fOhREvdhaAakH9Cpp-YaaDi5vMvGnhMFKc0Lubv5y5QaVvdS0JOay7tdTJ0nvNR49cLXQHTCGoWbkNTqhIICy0Hj1HiHdgPYdDtQ_2b4DYtYJLyqOhDwSlsFvvyDd6a-gmza8qBXE6n9T9l5XVcnajIry5Phi_lfqp1CjAlDTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6e044a2b.mp4?token=Y27ihA5tSMocfeo2Ptw0S2KWwBTL-76zj81UOSY5eZo4ck9bvnYNmHFq0VW6TUw3OndMGm06YrR1SoJIwl7Ov1ddmuthu2wmI0f3ZLoqP-uCM52GkMDOCpMPmyi0eVSSBEhJVS-Y2lI1BisF_xCmppP76FQA9On4VWWqjUevZYXUam8AbxlSlFY1fjQG8lvvyBwsX1mdL5f3shRjtKx8KANTTWH8Ed2GOG7qJSNcyicC1qD-Saf1el52Tk_7h3Snb60ZNjxpFC76DHZGExfvfqANUkE-Q5ANTxLLntq5kcN0hwOlSRHM5ecBCdU8Of1-DHTznCynO2na65pXOtBLqk_G9jqg8Y_Na9idrPbu_tCn1s-rKztps5GNpnOfwCl2S7nguqZgv5MDbp59bNoytSwcnmXtweTL1pjoPaRbxmmJKoW6lFEHIUzzK6zL12W6SPLv58lALq_ikcdTepjIOzzERVX3eli1lfYrnFggNDzwlMNanF4bQNDJBSgQEEMH3fOhREvdhaAakH9Cpp-YaaDi5vMvGnhMFKc0Lubv5y5QaVvdS0JOay7tdTJ0nvNR49cLXQHTCGoWbkNTqhIICy0Hj1HiHdgPYdDtQ_2b4DYtYJLyqOhDwSlsFvvyDd6a-gmza8qBXE6n9T9l5XVcnajIry5Phi_lfqp1CjAlDTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۵ اسرائیل : فشار جدی اسرائیل بر عربستان سعودی برای تحقیق درباره فرد تروریست در حادثه پرواز فلای‌دبی؛ به گفته رسانه‌های اسرائیلی، عربستان تاکنون اجازه دسترسی اسرائیل به تحقیقات را نداده و در اسرائیل احتمال ارتباط این فرد با ایران و سازمان‌های تروریستی در حال بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24605" target="_blank">📅 20:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24604">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ :
چرا شبکه فاکس‌نیوز همیشه چاک شومر، حکیم جفریز، جسیکا تارلوف و تمام دموکرات‌ها را روی آنتن می‌آورد تا علیه حزب جمهوری‌خواه و البته علیه من صحبت کنند؟ به نظرم حتی زمان بیشتری از جمهوری‌خواهان طرفدار ما در اختیار آنها قرار می‌گیرد. به همین دلیل است که MAGA و میهن‌پرستان واقعی هرگز فاکس را دوست نخواهند داشت! آنها دائماً یک روایت کاملاً منفی را تکرار می‌کنند و بعد در نهایت یک پاسخ کوتاه به ما می‌دهند. واقعاً شگفت‌انگیز است که من هر سه انتخابات را پیروز شدم. مخالفان بسیار قدرتمند و گسترده‌اند، اما مبارزه ادامه دارد!
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24604" target="_blank">📅 20:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24603">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با قهرمانان اسرائیلی پرواز FZ1073 شرکت «فلای‌دبی» دیدار کرد؛ پروازی که صبح امروز توسط یکی از خلبانان تا آستانه ربوده شدن پیش رفت، اما با مداخله خدمه و مسافران اسرائیلی، از این اقدام جلوگیری شد. @WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24603" target="_blank">📅 20:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24602">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با قهرمانان اسرائیلی پرواز FZ1073 شرکت «فلای‌دبی» دیدار کرد؛ پروازی که صبح امروز توسط یکی از خلبانان تا آستانه ربوده شدن پیش رفت، اما با مداخله خدمه و مسافران اسرائیلی، از این اقدام جلوگیری شد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24602" target="_blank">📅 20:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24601">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df0e976c18.mp4?token=R_wVLF_iFxM0I8ukQ453W_pfrDN0j28lt7GGp18iItc8IckA5T-yXRTN6pXCBY2qxcptGGn7MYRc_FZ29FNufXUmaYKvm-78u8OkqXHAF0nss0t9J1akXx1Ihp2ah_MsdcfIn13k1sZX3MD4D-WVg1qZytBtDgdHkFFQ52Szmg2C2KPHXtzsrr5BdGMyFGxj3UTX6DMAmYvDyg0bye4h_iB-xtKcnzlNapyZ2SIOQtm03t-DT0dlvKz5fh6xqjOcHUseuHKK-5PEjEhfYoQY3B2l9BFjBySPjUs5kbbjEjHN5-7oqajOah9A1I_nluIrjfOvSpsrKCcQSi7l3UXdtpURzD3HL0lW4iU1zdtvMjjeBRYheKpBNO5gGehIBpHJNX_U2R9Hbxuf0S3EKwUpEjYMwixS3HVGDGw6FUuOtYn-5JBnHnLntNDHHuzt0NF8pUgmExgFfznheoBGFS8jAB4oMvJl9Zesc5dsOMaSohAZk15_B5sStfegaumhThk8pWaEYtcXEQIsiXrMsXfBRMPiSkK6b7k0xFdZRD0zbGfG-4LnF1pP0sXrWqsOzXI-Zne518lJdpfn4i1EMQjbazkxhV5oP_-JrpGs_2u6bMPzp5MAYRMdM22-Jf7reMVsuxOYnBO1FaZx7c7GvIsDAnObDEAG357IihJ7aCD6m2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df0e976c18.mp4?token=R_wVLF_iFxM0I8ukQ453W_pfrDN0j28lt7GGp18iItc8IckA5T-yXRTN6pXCBY2qxcptGGn7MYRc_FZ29FNufXUmaYKvm-78u8OkqXHAF0nss0t9J1akXx1Ihp2ah_MsdcfIn13k1sZX3MD4D-WVg1qZytBtDgdHkFFQ52Szmg2C2KPHXtzsrr5BdGMyFGxj3UTX6DMAmYvDyg0bye4h_iB-xtKcnzlNapyZ2SIOQtm03t-DT0dlvKz5fh6xqjOcHUseuHKK-5PEjEhfYoQY3B2l9BFjBySPjUs5kbbjEjHN5-7oqajOah9A1I_nluIrjfOvSpsrKCcQSi7l3UXdtpURzD3HL0lW4iU1zdtvMjjeBRYheKpBNO5gGehIBpHJNX_U2R9Hbxuf0S3EKwUpEjYMwixS3HVGDGw6FUuOtYn-5JBnHnLntNDHHuzt0NF8pUgmExgFfznheoBGFS8jAB4oMvJl9Zesc5dsOMaSohAZk15_B5sStfegaumhThk8pWaEYtcXEQIsiXrMsXfBRMPiSkK6b7k0xFdZRD0zbGfG-4LnF1pP0sXrWqsOzXI-Zne518lJdpfn4i1EMQjbazkxhV5oP_-JrpGs_2u6bMPzp5MAYRMdM22-Jf7reMVsuxOYnBO1FaZx7c7GvIsDAnObDEAG357IihJ7aCD6m2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گاردین: اندی برنهام، نخست‌وزیر بریتانیا، می‌گوید «شواهد قوی» وجود دارد که نشان می‌دهد ایران در توطئه تروریستی احتمالی در نزدیکی پایگاه نیروی هوایی سلطنتی «فِیرفورد» (RAF Fairford) جایی که پنج مرد در جریان تعطیلات آخر هفته دستگیر شدند نقش داشته است. برنهام…</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24601" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24600">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نتانیاهو طی چند ساعت آینده با ترامپ تلفنی صحبت خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24600" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24598">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گاردین: اندی برنهام، نخست‌وزیر بریتانیا، می‌گوید
«شواهد قوی» وجود دارد که نشان می‌دهد ایران در توطئه تروریستی احتمالی در نزدیکی پایگاه نیروی هوایی سلطنتی «فِیرفورد» (RAF Fairford) جایی که پنج مرد در جریان تعطیلات آخر هفته دستگیر شدند نقش داشته
است.
برنهام گفت: «شواهد قوی حاکی از آن است که ایران در وقایع آخر هفته در پایگاه فِیرفورد نقش داشته است، اما البته این پرونده همچنان موضوعی در دست بررسی، پیچیده و جدی برای پلیس است.»
وی افزود که مقامات بریتانیایی همکاری نزدیکی با ایالات متحده دارند و جزئیات بیشتر در زمان مقتضی منتشر خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24598" target="_blank">📅 19:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24597">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یا موسی
🙌🏾</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24597" target="_blank">📅 19:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24596">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24596" target="_blank">📅 19:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24595">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccc2d60a6a.mp4?token=gFQ5B3T9S6inPMz7PZgWG3-fD50CxSWluLN28afEwJzievaDdfFRKZkbv3_Mlci9oVsqNKTI-DvYun-uJiVSL7nDeEKWpJvjdeQpMOusw383zyplkJk3D_BikSVA_ouTFSF3z4uQUfpqE4uX5aQ02o4B6_ntArJYyFBhoppw5EA9EU9hc0JO1tLHZlvzRXaBeZc0Npn00yJNXEhrFjixZFwO77-AyyMkUSYySR5ZGLskMAi791tW5-ZJzT0pGoJfAlbyc-AkWbdk5WpES0M8QAXE0bwmlJWps_bWUyz8kOhzm-Z199Kcds4F9XV_7IW6gwOjIIHaxE3BBp4sbt5wQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccc2d60a6a.mp4?token=gFQ5B3T9S6inPMz7PZgWG3-fD50CxSWluLN28afEwJzievaDdfFRKZkbv3_Mlci9oVsqNKTI-DvYun-uJiVSL7nDeEKWpJvjdeQpMOusw383zyplkJk3D_BikSVA_ouTFSF3z4uQUfpqE4uX5aQ02o4B6_ntArJYyFBhoppw5EA9EU9hc0JO1tLHZlvzRXaBeZc0Npn00yJNXEhrFjixZFwO77-AyyMkUSYySR5ZGLskMAi791tW5-ZJzT0pGoJfAlbyc-AkWbdk5WpES0M8QAXE0bwmlJWps_bWUyz8kOhzm-Z199Kcds4F9XV_7IW6gwOjIIHaxE3BBp4sbt5wQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ششصد نیروی نظامی ایالات متحده به پیت هگست، وزیر جنگ، برای «تمرینات بدنی در پنتاگون» پیوستند؛ این برنامه پیش از سخنرانی «وضعیت نیروها» توسط او در کوانتیکو در اواخر امروز برگزار شد. انتظار می‌رود این سخنرانی شامل یک تغییر عمده در ساختار پنتاگون باشد و هگست قصد دارد ۲۰ درصد از سمت‌های اختصاص‌یافته به ژنرال‌ها و دریاسالارها را کاهش دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24595" target="_blank">📅 19:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24594">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0894765b2.mp4?token=mmmmxTsW0WE_JYW7TlmbZkg7JA7hFR2OYr2FiAoXs9w9WjXYHSAEB7Ev9xZYVEUOQ-19hIMoTR3kUDvdY09Wkbsn_mxZBU_zyo-U2C9Ob9fupOKtzSnDENUKWSqOGhwSn9Wr-8ii9vLhmaQ9qTbz-XPxmDRKNUaojuldY2O0N8-6I3NbMfIPbLeGtGEkYh7ewsWdlYBvTIR9XMn8VKY6_eQDpThb6vuKHJI2Drr4spa5plvNXOaOHVP4L1qjzrFZMQ071WPauXhlcGB729NTyjZbeP7JcYnosu4SjzE8rvObEb24tpyW8wJW2Rax1KT_b2FYWUI-Z5EV3yyDSkueMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0894765b2.mp4?token=mmmmxTsW0WE_JYW7TlmbZkg7JA7hFR2OYr2FiAoXs9w9WjXYHSAEB7Ev9xZYVEUOQ-19hIMoTR3kUDvdY09Wkbsn_mxZBU_zyo-U2C9Ob9fupOKtzSnDENUKWSqOGhwSn9Wr-8ii9vLhmaQ9qTbz-XPxmDRKNUaojuldY2O0N8-6I3NbMfIPbLeGtGEkYh7ewsWdlYBvTIR9XMn8VKY6_eQDpThb6vuKHJI2Drr4spa5plvNXOaOHVP4L1qjzrFZMQ071WPauXhlcGB729NTyjZbeP7JcYnosu4SjzE8rvObEb24tpyW8wJW2Rax1KT_b2FYWUI-Z5EV3yyDSkueMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه اسکورت هواپیما فلای دوبی در حریم هوایی اسرائیل با دو جنگنده @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24594" target="_blank">📅 19:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24593">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwNIN-c3OA7FXfB5egC-Ml1CIYjLTLgLNHAtw7wcaDePt_6hTZ-tFjhvPJLzuL92bAjjL64ZDBqJLZz50YWfcYQfJLnarj-YzZubcIArosvkW7evqotE5EQ96TktzRrxI_-GG4YR23TahTR7wkcY5lMyAcDPncFvs7R_G7P7uG2eLeWKXeJnRyA4Rbj9hLT4ujc0gqVcZWy0OzjL9OB4AsDVLx97ZUBEbjjCt4xzkWb7HtAamQONJN90HjoqerI3TQAl5fFxsGwAp11-oiSMLTX5GmuzmHlFnwPlKmZZztz-4Wq52QojbT93YnXydutTI6cACnVZO_AnzIMKxLHBaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز دوم «فلای دوبی» مسافرها رو از عربستان به اسرائیل باز گرداند @WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24593" target="_blank">📅 19:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24592">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آسوشیتدپرس:
پاکستان اعلام کرده در صورت حمله حوثی‌ها به عربستان، برای دفاع از عربستان از
«هر وسیله‌ای که در اختیار دارد»
استفاده خواهد کرد. وزیر دفاع پاکستان این موضع را در چارچوب توافق دفاعی مشترک جدید میان
پاکستان، عربستان و ترکیه
اعلام کرده است. او در عین حال گفت پاکستان همچنان کانال‌های دیپلماتیک خود با ایران را حفظ می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24592" target="_blank">📅 19:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24590">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i630CZACBP1tmQzFnSQXsqzb2ouRNdtm2A7jG6hfzwevIPYPH9hhbWkGD5PGAZZHLVgzCBp4yYaeLNkwrb-27D5qVe8n1lvoNWWCozgrd7oULAC5X8XUxS9xtJlimp79lGTcFZMPZpEQWngNoc94xc5hk58DtJWH5O0QICmmt92B8Vlue19_PRfeioDFsLfz09Jcs58PsYlHc4vyvMuefugFR-pa1GvptZk_7c7pU_Zeir2evQt-qTF-dQghAkDitj1gfpPGpxhssKyxzTOvF1U8dD8FLLLc8lFf5Wh9vwd7GvxZ8Ut-0PrYFcrt341US5WhqfKsII4Ox4snLsNyJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXDh6clU05wwA3WvdVss_ZC30uVuYbyr_wyLwGs4g3u7WY6mEAAHYZPJHGTtR14LgnG6kKtSCJ8_lb-8S_bHKcCYWCrR7PllVI74Qsiw6pj68kEyZmrSD2hRb5wKXhSPgW57tizqxZb7xEHZReGcTJvcpViWseuqe4C8aDfexWsGA_8THMqmAyDsnk9hIMBfBR-UgWQyQdE0aUNS31iipST6Cb71nM9tGq83LtXNVy3KG0lsVb4oHeTEZtwJ67T0TULJEfU683Qp3qLxhXPmxkutqWJzJZtOp2J1Dpu9tCt_l6sz0Ok57BgUUMfsxpmA2OShLnNI-bKw9XgK9_3Iag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : با دقت بیشتر مشخصه این خط جت است
و موشک نیست
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24590" target="_blank">📅 18:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24589">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT5Ul8dObSBUYcj3h4eNf8zWBTDD52SCR_Pq6LgrYhx93pCAiZuIbZV0eME0HOjHYfLTm4FpM6Kzz5lei2LCv_h2iG_zXgdEyESbYrkYZKZcqejjN5MpNv2PK9GU70qtPiOUtmC5t3JdvTxx3frPsrfIhlPLICD4wJJNx9l09cjUnM7V1JjM-H8TKAgtvqOylR-gnJG6u7c8wXuZc2TphhOEXmuBnKX5Kvdedg2Yl_LQ6a6ocOgLdAHfAEoznzn8d-Md0VYeNGDOGHg6ABHStJceNbruyM6UoTJEyZo9tnpM53J7JHy2jsIqx_uV3oltqASejlOI44BxzmpF5gagxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز دوم «فلای دوبی» مسافرها رو از عربستان به اسرائیل باز گرداند
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24589" target="_blank">📅 18:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24586">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e82776f51d.mp4?token=ib--sE83XD12L803ySCWebEDGbLjjDhVLFjRMrAfaPuZT16PuH33UoJ-yp91pM6UWfonSwcVyikgCdZU-KNuiOWycet6F7nSE3kP53r6JmtkgS01m3zl5UX7uOkcAJPfg_8eE4remxwiKEwO90sE6vYb-xfELu_3AX8WqfwS2QKWfI2V9a_q8h9TY_LFyszqeI1RDt1FozCjm2awyB34V8XmpIjOzGsDqwSDnJ9EdZGESqJntDjtu3MFUq7suZuxbKl7PYESHEVMIw1qyoZPcTB5TgcxOzwbyfxUi4dmLhdQ6dyRdX40B7srxeh_Z-wIkN_4XQ8lLmZlWWzrw7O7G4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e82776f51d.mp4?token=ib--sE83XD12L803ySCWebEDGbLjjDhVLFjRMrAfaPuZT16PuH33UoJ-yp91pM6UWfonSwcVyikgCdZU-KNuiOWycet6F7nSE3kP53r6JmtkgS01m3zl5UX7uOkcAJPfg_8eE4remxwiKEwO90sE6vYb-xfELu_3AX8WqfwS2QKWfI2V9a_q8h9TY_LFyszqeI1RDt1FozCjm2awyB34V8XmpIjOzGsDqwSDnJ9EdZGESqJntDjtu3MFUq7suZuxbKl7PYESHEVMIw1qyoZPcTB5TgcxOzwbyfxUi4dmLhdQ6dyRdX40B7srxeh_Z-wIkN_4XQ8lLmZlWWzrw7O7G4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ در تروث
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24586" target="_blank">📅 18:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24585">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اتاق جنگ با یاشار : توصیف دقیق و خط به خط درگیری در‌تنگه هرمز و نحوه پایان یافتن
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24585" target="_blank">📅 18:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24584">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمحمدرضا تنها</strong></div>
<div class="tg-text">داداش .
جای چرت پرت های این الاغچیان
یک قسمت از تام جری بزار شاد بشیم</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24584" target="_blank">📅 18:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24583">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عراقچی: ایران در شرایط جدید، به موقعیت ممتازی دست یافته
کشورهای اروپایی، عربی و آسیایی اشتیاق شدیدی برای دیدار و ملاقات در نیویورک نشان دادند
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24583" target="_blank">📅 18:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24582">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKQygJFDYhLwXuTk5yzvG02u8xAefJENyP4nZdPIuKYVU7P2hDrU_QxBkAGJdBS2JsD4xzPj-xyO7gms8LC9y73kHybghxBFQspavtXtMA620nKqsLCzUIv1Hmwnv1LvEG_kVcUJwKNWHv67-U8_AaqqvFXNlkU7kDLb4m7HgvBk9SyeR8jWUBgOuqxHqgX9oPp4HOX3okjSgbpPjDSp5Lp8bJH1p-kvGALFk3ZZYSm2_rKFecorOa4-VHoBRbhAew6FxcmTFf6MxltzM2ayS9s-pUk_-iwlNUqzLgUTgtEB2JrOCM7iVDIZm4ifIc86s3iJHy3mNPSJX3ANRKeeJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابک زنجانی عکسی از
«
محمود زیبایی
»
گذاشته که طی دستگیریش به عنوان کارشناس بانک مرکزی حضور داشته و ازش بازجویی میکرده، اکنون
زنجانی ادعا میکنه که این فرد عامل موساد بوده و روش‌هایی دور زدن تحریم رو یادگرفته
با خودش برده.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24582" target="_blank">📅 17:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24581">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نتانیاهو:
«این یک
رویداد امنیتی بسیار جدی
بود. در پرواز فلای‌دبی از دبی به تل‌آویو، یکی از خلبانان با چاقو به خلبان دیگر حمله کرد و ظاهراً تلاش کرد هواپیما را با تمام سرنشینان سرنگون کند. هواپیما وارد حالت چرخش شد و شروع به شیرجه رفتن کرد، اما یک مسافر اسرائیلی و یکی از اعضای خدمه وارد کابین خلبان شدند و مهاجم را هنگام تلاش برای دستکاری سامانه‌های هواپیما مهار کردند. اعضای دیگر خدمه نیز وارد کابین شدند و به تثبیت هواپیما کمک کردند. آنها قهرمان هستند؛ با ابتکار عمل و شجاعتی فوق‌العاده، جان بسیاری را نجات دادند و از وقوع یک فاجعه بزرگ جلوگیری کردند.»
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24581" target="_blank">📅 17:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24580">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مردی اتاق جنگ همه جا هست ! @WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24580" target="_blank">📅 16:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24578">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">استاد بزرگ شطرنج ، نتانیاهو : توان هک هر تلفنی رو داریم
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24578" target="_blank">📅 16:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24577">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">لغو سفر نتانیاهو و کاتس به غزه در پی فرود اضطراری پرواز «فلای‌دبی»
بنا بر گزارش‌ها، سفر برنامه‌ ریزی‌ شده نخست‌وزیر، وزیر جنگ و رئیس ستاد ارتش اسرائیل به نوار غزه، در پی فرود اضطراری هواپیمای فلای‌دبی و احتمال امنیتی بودن آن لغو شده است
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24577" target="_blank">📅 16:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24576">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61a612b92.mp4?token=ADsejSipsrzRns13zySBbh0DSTTrucYkE6L0dgUkj-3VrvnHb-uhEC22HYTlle3h8RrDOB1jXI-QfoGfO5rRtgnMENlyN0hX_jFKwy0gLlVBPHUlpE0XdhLAMwUwO2o5MPzJ-_dzL9F-5CUyob3qJnVFi1jkrJL9oFEoWka7WNcpnnqqcpOyEkptuB5igrMfyJGYZN7M07RJM7ao3yszwE5zc0WzCcNWtPJ_oC2YLdzQrtaF6FUSP4LPCpX5BClR75Vw-kKsmrby9LmhRjCwobJhrphTrFZv1gKv_N59lOKNKB3VbvsdG0MWWJsochMn_Yg6APURhj7-63_ftbPnpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61a612b92.mp4?token=ADsejSipsrzRns13zySBbh0DSTTrucYkE6L0dgUkj-3VrvnHb-uhEC22HYTlle3h8RrDOB1jXI-QfoGfO5rRtgnMENlyN0hX_jFKwy0gLlVBPHUlpE0XdhLAMwUwO2o5MPzJ-_dzL9F-5CUyob3qJnVFi1jkrJL9oFEoWka7WNcpnnqqcpOyEkptuB5igrMfyJGYZN7M07RJM7ao3yszwE5zc0WzCcNWtPJ_oC2YLdzQrtaF6FUSP4LPCpX5BClR75Vw-kKsmrby9LmhRjCwobJhrphTrFZv1gKv_N59lOKNKB3VbvsdG0MWWJsochMn_Yg6APURhj7-63_ftbPnpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک هاکبی، سفیر آمریکا در اسرائیل:
جمهوری اسلامی نزدیک به
۴۷ سال و نیم
است که حرف‌هایی می‌زند که هرگز قصد عملی کردن آن‌ها را ندارد. اما تنها چیزی که واقعاً قصد انجامش را دارد،
نابودی آمریکا و به ارمغان آوردن مرگ برای آمریکایی‌هاست.
یکی از دلایلی که بسیار سپاسگزارم این است که ترامپ سرانجام شجاعت به خرج داد و گفت: «کافی است؛ آن‌ها به سلاح هسته‌ای دست پیدا نخواهند کرد.» اگر بعد از نزدیک به ۵۰ سال که به شما می‌گویند قصد کشتنتان را دارند، هنوز حرفشان را باور نکردید،
شرم بر شما باد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24576" target="_blank">📅 16:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24575">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کودن هم بسیار هست..</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24575" target="_blank">📅 16:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24574">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromH H</strong></div>
<div class="tg-text">مصاحبه زن این یارو رو دیدی که باهاش عکس گذاشتی؟</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24574" target="_blank">📅 16:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24573">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24573" target="_blank">📅 16:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24570">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ML379klI3xKZMNGj9KclFQqCE1Lb1NsKTauqBiOOh7DrCj9tg_CPoORJiYtQ6oboCI-UpF7NcaP1J4iULJ0fooBNyDrmr-cUADawSDL_WZw_uAq1fGLE5fCMat3is7lfyMUcdln8trGUg85v2ImsMDGusLwr2y08XJNJZ9dCNBnLoMxeUk159fsgvJMAFVVKdAV2ksxWBuMHOQnEXkvn-qJyiJoOjzeSJ8GSHfKO2UtgpVV788dwNcxeReGOpC9tnsX_zH5rMyjxUB0zaYwkuWLmW_a6Gbce0-qDvja7JhKkfSgGeH9S24hliCuTlWs85OIh9buw3l1L85BbsNhClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af7c379d02.mp4?token=Aiole9vevMWhMA2L-R5yo5Amm7erz-K2TZMgN_LEI7d6RtzZ_wguhu3G_TQoYTjZZX0uJ-Bpam_ysTmkYyZftKton9o6ivUS1QrYHgWecKEPWe92x0jY9lINczDielcUyyXHN0YeLuHcn9eyMvr9tZ44irmvZF-bdameseGyDqTRonuXvWZCLv_j_vzV7YW5s9zNc3MR2CYu9l1L2xRK14aqcSGS63z5kBXyKh0qS6s2pMbWghk3V7TEgZsx16TaqnMU8HXK_-WCv8hajeAbfBcHwiuwce8zl2P1er8E4jDJ3HQ0hEqOBcFY6oHlVUQqyLD6fDeyi7zp9J2K-VsIqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af7c379d02.mp4?token=Aiole9vevMWhMA2L-R5yo5Amm7erz-K2TZMgN_LEI7d6RtzZ_wguhu3G_TQoYTjZZX0uJ-Bpam_ysTmkYyZftKton9o6ivUS1QrYHgWecKEPWe92x0jY9lINczDielcUyyXHN0YeLuHcn9eyMvr9tZ44irmvZF-bdameseGyDqTRonuXvWZCLv_j_vzV7YW5s9zNc3MR2CYu9l1L2xRK14aqcSGS63z5kBXyKh0qS6s2pMbWghk3V7TEgZsx16TaqnMU8HXK_-WCv8hajeAbfBcHwiuwce8zl2P1er8E4jDJ3HQ0hEqOBcFY6oHlVUQqyLD6fDeyi7zp9J2K-VsIqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردی اتاق جنگ همه جا هست !
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24570" target="_blank">📅 16:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24569">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">واکنش نیم میلیون اتاق جنگی به هر‌ خبر بازگشت :
🥚
🥚
ما هدف داریم و فرمول دادم ، فقط بایکت کنید و اصلا انتشار ندید @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24569" target="_blank">📅 16:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24568">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">واکنش نیم میلیون اتاق جنگی به هر‌ خبر بازگشت :
🥚
🥚
ما هدف داریم و فرمول دادم ، فقط بایکت کنید و اصلا انتشار ندید
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24568" target="_blank">📅 16:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24567">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خبرگزاری رژیم فارس:
مدیریت بازار دلار تهران عملاً به وزیر خزانه‌داری آمریکا سپرده شده است
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24567" target="_blank">📅 16:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24566">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مرد خردمند ، مارک لوین : آیا این کار آن‌قدر تحریک‌آمیز هست که آن حرام‌زاده‌ها را نابود کنیم؟ متن تفاهم‌نامه‌ی ما باید این باشد : «ما شما را از بین خواهیم برد؛ فهمیدید؟»
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24566" target="_blank">📅 15:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24565">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کانال ۱۴ اسرائیل : ایران همچنان مظنون اصلی است.
روسای امنیتی اسرائیل از ارتش اسرائیل، شین بت و موساد به طور فزاینده‌ای وضعیت اضطراری در پرواز FZ1073 فلای‌دوبی را به عنوان یک حمله تروریستی ارزیابی می‌کنند.
کارشناسان امنیتی معتقدند اگر این یک حمله تروریستی تحت حمایت دولتی باشد، ایران تنها بازیگر منطقه‌ای است که توانایی عملیاتی برنامه‌ریزی و اجرای چنین عملیاتی را دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24565" target="_blank">📅 15:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24564">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فرمانداری زاهدان:
صدای انفجار شنیده‌شده از حوالی کلانتری ۱۹ زاهدان، در محدودهٔ خیابان جمهوری گزارش شده است.بررسی‌های اولیه حاکی است صدای انفجار شنیده‌شده مربوط به انفجار یک شیء صوتی بوده است؛ این اتفاق خسارتی درپی نداشته و موضوع در دست بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24564" target="_blank">📅 15:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24563">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گارد ساحلی هند: یک لنج ایرانی در ۳ مهر ۱۴۰۵ در دریای عرب توقیف شد.
این شناور در
غرب جزایر لاکشادویپ و داخل منطقه انحصاری اقتصادی هند
متوقف و در بازرسی آن
۵۲۶ کیلوگرم هروئین و مت‌آمفتامین (شیشه)
کشف شد؛ ارزش محموله
حدود ۳۳۸ میلیون دلار
برآورد شده است.
پنج تبعه پاکستان
نیز که سرنشین لنج بودند، بازداشت شدند. شناور، خدمه و محموله برای تحقیقات به بمبئی منتقل شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24563" target="_blank">📅 15:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24562">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خبرنگار کانال ۱۲ : گزارشها حاکی از این است که کمک‌خلبان، شهروند عمان، با یک تبر سوار هواپیما شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24562" target="_blank">📅 15:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24561">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خبرگزاری‌رژیم فارس : مقامات امنیتی ایران معتقدند اسرائیل در حال برنامه‌ریزی برای یک حمله تروریستی منطقه‌ای است که ممکن است هواپیماها یا فرودگاه‌ها را هدف قرار دهد و در این راستا، ایران را مقصر جلوه دهد تا با این کار، موج جدیدی از فشار بین‌المللی و "اتفاق نظر" علیه تهران ایجاد کند.سازمان‌های اطلاعاتی ایران در حال حاضر بر جلوگیری از وقوع چنین سناریویی تمرکز دارند
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24561" target="_blank">📅 14:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24560">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فرودگاه تبوک : خلبان فداکار اماراتی و کمک‌خلبان تروریست هواپیما هر دو مجروح شدند و به بیمارستان منتقل شدند. ما مراقبت‌های لازم را برای مسافران در سالن مسافران ارائه میدهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24560" target="_blank">📅 14:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24559">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کانال ۱۲ :
وزیر حمل و نقل اسرائیل خواستار توقف پروازهای شرکت هواپیمایی "فلاای-دبی" به اسرائیل شد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24559" target="_blank">📅 14:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24558">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اتاق جنگ با یاشار : این اقدام تروریستی جمهوری اسلامی مانند ترور ترامپ برای پیروزی بنیامین نتانیاهو در انتخابات تأثیر خواهد گذاشت
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24558" target="_blank">📅 14:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24557">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اتاق جنگ با یاشار : به کمربندی قاهره رسیدیم
🐫
🐫
🐫
🐫
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24557" target="_blank">📅 14:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24556">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یک مقام امنیتی اسرائیلی به i24NEWS گفت تل‌آویو در حال بررسی این موضوع است که آیا ایران ارتباطی با تلاش برای ربودن هواپیمای فلای‌دبی داشته است یا خیر. به گفته این مقام، کمک‌خلبان که تلاش کرده کنترل هواپیما را به دست بگیرد و آن را سرنگون کند، اصالتاً عمانی است…</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24556" target="_blank">📅 14:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24555">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پس‌از وقوع حادثه تروریستی و فرود اضطراری پرواز دبی به تل‌آویو در عربستان، منابع اسرائیلی گزارش کردند که یک پرواز دیگر از هواپیمایی فلای‌دبی در میانهٔ مسیر دبی به تل‌آویو در حال بازگشت به دبی است. @WarRoom  همچنین جمهوری اسلامی پیشتر تهدید کرده بود که ما راههای…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24555" target="_blank">📅 14:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24553">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">صدای دو انفجار در تنگه از قشم شنیده شد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24553" target="_blank">📅 14:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24552">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی: تهران ادعای پاسخ نظامی به محدودیت‌های هوایی اخیر را رد کرد و از مذاکرات جدی با کشورهای ذی‌نفع برای رفع محدودیت‌ها خبر داد؛ در عین حال، هشدار داد در صورت لزوم، گزینه‌های متقابل غیرنظامی علیه برخی فرودگاه‌ها را اجرا خواهد کرد، هرچند…</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24552" target="_blank">📅 14:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24543">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bKJeKiBZLOVAtjUIrOEqBWcljQILVWRg-mJhHPy8hCyF4-bojaXlRfa0Bp_0vRq3yj6HttCC-koSae276WvPwarQOcR12Py4Og6czcJ1VHXpQim7fhkt3LMsAQvS3QF1y9I7L157ubmJX9j10Ps67oI3JwJrm_wBT-PMvBXJOuaIPasR6ncbODEI4wSM0tREnbZciUxI0C7fRo5cScgzs2G-DI-ZPkxOnH4NEzUN3cpFfATKXBvkc4g8c-fencJ1P1VVrGxlTdUzQ9CpeYkGFAbb8EPvAiUpg0m5BTREaE0ZVGgrKnZ6l7EnfUc4HVHAFs5OX9K9-6isLevMmBzrkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OiuwJwlPszMzqqwP4mv_-9xGsndESqyuPdbnZZMQ59LNumWA1wLejJ7BtcFqQpGbHi0PitaCZLMU3GKeC8JEsF0Y54ytEDtikZlOGDb4eNrMTQ2kd8xDEFDzxsSbNoeRnEFmZHFh0ph3qWWM379C8yHXoiGB3ceys7o4cpX5GPzWRhiFuORVPRarheVrVBQl5AIKVmc40eGQThIgjckgM4gxQ3BFHVBzukbk6HNd-ZiFzSs30dQt9rdiSh1tcrWogFGcTM0J9OQ122DGFFxRQ8xWD7TlrI5UsTTPjtzB4OwCsEvNuqK_yCiL9HvI26-GHvt9BcjOOCY084SHxf9NRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s613rdOMAG80jhycn0r3yAa4n9-DBhYlw4ZxgiWQENzn8rl6hLnkMZHFoCmSKAQWsZJjtGzAivvLdIXM-pBAkn88vaDXf7MPXn-1g9GdqHBbNEin1uxRvFMkSRntrdgievKtaFkhMw2JCwBmNyTDpp6u96cvNw9QX_FXDmHuGj3SQ0HI3wKQX9YsMjbQBx2zl6STdd_bkzx3pa6QH-jjNjWikPHC0KOW3mMVwEEXWjIdqSAnTsf2QrPW_Lh0aFZ2ur7zzGE4zy7TckimZRv6SpVkfRqMh2MG3FqbkKSwJVJo3SfWIGaVNTVL7st9GJxiYk5ukF6oL1nJWm888rFlyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4d3219449.mp4?token=AFn4rqT1L8d6IJd6WM_ZLMJSNfKvwntt4ZFJM-61PH0QgMRzL49tsAKp5yYFmqkb_mYDunMPuNBJaVhSqNYp1nGWN8ZWmH2JOtNIxuwgZ1chKV12nl0P0ftw7Xd5_FDT_AiFbAFU_W2jVlk2x-0MPOwuFBPmGQF5BOP7q3cDtvgNoeht2pF9-K8jnMMgJ4wKYi_95Z8eGcbqkECp52zDSU0Isss9h04cQA778TrHI3ihwwCfJc_KHoV6UsSxoqImlcQcMWbnx484RpX0U8sEKePEDa0meRhD7_RwtrheRCt6aFuY2jduRk6W8P3cIedF7jl1aJK7_2seScIsZ7uLDqi18dxEkzXM-Wy6SPbL75eHnnGNKOv0J65o4SruKzXkZUmOWrFGNmQ_ejPcHICA8A1zHOfjZMFR3E7AFiTXke05hKtWI1khGgO4RM5BTUi3Y7mS7IC6AdZ_ruQHReZTuyZsnxoYZ0RfRSUzd5OFNiLewZQo6usQPAAO8n6ZveoaLoF4-cZpYysmjTw-GFFPtsCmRYuZAUVexy1nxc3SSYDTUmNSYIT7-ZldR3FrWArIHjTLChc5LpzFklzpQY7AIT2o8FIAYl_oW-aDtrBmhN-p3FsIOSFagnPr7vh8JcgZkK1IsZeo3DBZdeg0sjVfyuAEcu8_rJIscPGjz1QrDu0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4d3219449.mp4?token=AFn4rqT1L8d6IJd6WM_ZLMJSNfKvwntt4ZFJM-61PH0QgMRzL49tsAKp5yYFmqkb_mYDunMPuNBJaVhSqNYp1nGWN8ZWmH2JOtNIxuwgZ1chKV12nl0P0ftw7Xd5_FDT_AiFbAFU_W2jVlk2x-0MPOwuFBPmGQF5BOP7q3cDtvgNoeht2pF9-K8jnMMgJ4wKYi_95Z8eGcbqkECp52zDSU0Isss9h04cQA778TrHI3ihwwCfJc_KHoV6UsSxoqImlcQcMWbnx484RpX0U8sEKePEDa0meRhD7_RwtrheRCt6aFuY2jduRk6W8P3cIedF7jl1aJK7_2seScIsZ7uLDqi18dxEkzXM-Wy6SPbL75eHnnGNKOv0J65o4SruKzXkZUmOWrFGNmQ_ejPcHICA8A1zHOfjZMFR3E7AFiTXke05hKtWI1khGgO4RM5BTUi3Y7mS7IC6AdZ_ruQHReZTuyZsnxoYZ0RfRSUzd5OFNiLewZQo6usQPAAO8n6ZveoaLoF4-cZpYysmjTw-GFFPtsCmRYuZAUVexy1nxc3SSYDTUmNSYIT7-ZldR3FrWArIHjTLChc5LpzFklzpQY7AIT2o8FIAYl_oW-aDtrBmhN-p3FsIOSFagnPr7vh8JcgZkK1IsZeo3DBZdeg0sjVfyuAEcu8_rJIscPGjz1QrDu0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تمامی تصاویر و اطلاعات پرواز «فلای‌دبی» که همچنین آسیبی در دم هواپیما  را نشان می‌دهد.
‏همچنین در ویدیویی مسافران در حال خواندن دعای عبری «آوینو مالکینو» («ای پدر ما، ای پادشاه ما») هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24543" target="_blank">📅 13:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24542">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e6e28941.mp4?token=TwC8uCwqOQmhhY3f61shFMiBLVowHdAUCbyFjJxJVgsGEbRGUOJ2rmP5obFDGwZfUZXUMqXRWuGSeIxkIOZbbHkNhutUJ1GUxYmklVWoYGStQ2vAzMMOYleASzUGylzOYcreb3olGMwyT8Fcd_sexWUgD2pUN1xHMBkc00Eqf4hT7-M1oYZ-SkWlr1o9y14hr8hvpf37SFdci8X0rRSKyUo27fvp1LcSGkVrXpG0-GOvr0j8HRq1HJgDVOvUNECPcNkcGYczy-YhIhwZgM1DSYtnFJjHQTO4uaKdYuiUyR0qUqjOLIaWMssB8KAXl7ZtUbiDBWHt-sUDZTpH_omg_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e6e28941.mp4?token=TwC8uCwqOQmhhY3f61shFMiBLVowHdAUCbyFjJxJVgsGEbRGUOJ2rmP5obFDGwZfUZXUMqXRWuGSeIxkIOZbbHkNhutUJ1GUxYmklVWoYGStQ2vAzMMOYleASzUGylzOYcreb3olGMwyT8Fcd_sexWUgD2pUN1xHMBkc00Eqf4hT7-M1oYZ-SkWlr1o9y14hr8hvpf37SFdci8X0rRSKyUo27fvp1LcSGkVrXpG0-GOvr0j8HRq1HJgDVOvUNECPcNkcGYczy-YhIhwZgM1DSYtnFJjHQTO4uaKdYuiUyR0qUqjOLIaWMssB8KAXl7ZtUbiDBWHt-sUDZTpH_omg_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش زنده رویترز : مسافران به سلامت در عربستان پیاده شدند ، پرواز جایگزین در راه. است
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24542" target="_blank">📅 13:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24540">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VvYqMZva0zMMgnwfETMWDSeXZh55VUc_AqtFonf0SYNGGEOk2eQoSlSujiZefvv-nMhFFKQW_FTq4BREGdRuKV00iFnpTAzXrC6Uph4ea9PLlSmkmePWHd0WQooACeGZeDdJmfYPHae9OOUJnjmPFKB4dIKXZzGWug4RR_7AkziYcPKPauVldBaDwE-AB1M8mxq888jAfNZN6J6Z9uV0BQAUXw7ae2ejsORB8PITjQ4uWluwNELlgmtQo_BaVAiwGR9m31cx1L-KKUtSj0lItNqAQl-kCdOrmtaYTx8SsWCWwClAybilIZWRP_sShyqtU8USDjDZteYkGGEhVSKz6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dn4pB4CJ4Yf0mMs7Bw6D5kK5VTJLzEUjtGxEjmCXfqpRNBfd69y1fW3gCBpKTLVp3umobYjuSRbhJmDofs1dYOh0Xv_e8KTUI5AMdmTE-XDSAvlMSm1b-ql6CZRFTkUsQyB1DsFjk-dAtnBatwUA110qOkZFke2rJ9GP840wwLGMFrdZPWjGu79lBFC1gCKbgmw1KnZTriuhERuYG9FFXr1iNXLLUbHMJmz1MUl092K64kDXzq1LSEK7PAtXHQ6Q5iypViDdDxzU2zbjnIT9f6u6oorouITlbwtgIf2SAoH1NA2vEsWM9VpeYotwNxVlMxMnDZOjveo1RH4IXln8Sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان تجرات دریای بریتانیا با تاخیر گزارش میدهد دیروز یک نفتکش در تنگه هرمز مورد اصابت پرتابه قرار گرفت  @WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24540" target="_blank">📅 13:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24539">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">«دو خلبان دیگر کنترل هواپیما را به دست گرفتند»؛ مادر یکی از مسافران از لحظات هولناک پرواز فلای‌دبی در میانه پرواز می‌گوید. مادر یکی از مسافران گفت: «او چاقو برداشت و تلاش کرد خلبان را بکشد.» او افزود دخترش صدای فریاد و درخواست کمک را شنیده و پس از آن هواپیما…</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24539" target="_blank">📅 13:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24538">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">«دو خلبان دیگر کنترل هواپیما را به دست گرفتند»؛ مادر یکی از مسافران از لحظات هولناک پرواز فلای‌دبی در میانه پرواز می‌گوید.
مادر یکی از مسافران گفت: «او چاقو برداشت و تلاش کرد خلبان را بکشد.» او افزود دخترش صدای فریاد و درخواست کمک را شنیده و پس از آن هواپیما شروع به از دست دادن کنترل و کاهش ارتفاع کرده است.
رسانه‌های اسرائیلی تأیید کردند که پس از ارزیابی‌های اولیه، این حادثه به‌عنوان
اقدامی تروریستی
در حال بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24538" target="_blank">📅 13:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24537">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksIAKh4oow24u7PJ8pnEV_VaC1DiusHyrcWS_7Q6j57KfzLq57l1gAn5QbQS2vE0aiF0p37AZsNBH2wVMj8MmHrnfVI2767rRLD7k0MI2fb_lAtZVYm9nLRQYh0yyBTaWHQsu3d-IKgIdqTW8NP3WWznGykdExUhhYY63PBLJXyCz1LkNEwNhJoV13ZoRQ1RGXteJ1nIBzB_Q5hbQq25N32I6a6mpEsb1JF1AkJHNeRaWYRedSkXV-QRnFouRcY9shpcSF7Wq06hKvffKHtDGn8CM2VUbXd0bT3ADzM1rkjx-CYktQ9KPUk05z_ueoouEKJH8H9jEcsfhCwR1ROwvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجرات دریای بریتانیا با تاخیر گزارش میدهد دیروز یک نفتکش در تنگه هرمز مورد اصابت پرتابه قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24537" target="_blank">📅 13:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24536">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سنتکام: مأموریت عملیات عزم راسخ در عراق پایان یافت.
فرماندهی مرکزی آمریکا اعلام کرد با خروج کامل نیروها و تجهیزات آمریکایی از
پایگاه هوایی اربیل در ۳۰ سپتامبر
، مأموریت «عملیات عزم راسخ» در عراق رسماً پایان یافت. حدود
۱٬۵۰۰ نیروی آمریکایی و ائتلاف
که عمدتاً در اربیل مستقر بودند، از عراق خارج شده‌اند و
ستاد نیروهای ائتلاف اکنون در اردن قرار دارد
. مأموریت مقابله با داعش در سوریه همچنان ادامه خواهد داشت و روابط دفاعی آمریکا و عراق از این پس در قالب
همکاری دوجانبه
دنبال می‌شود. سنتکام اعلام کرد نیروهای امنیتی عراق و اقلیم کردستان اکنون توانایی مدیریت مستقل تهدیدهای داعش را دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24536" target="_blank">📅 13:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24535">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کانال ۱۲ : ارزیابی امنیتی اسرائیل درباره حادثه پرواز فلای‌دبی تغییر کرده است.
به گفته یک مقام ارشد اسرائیلی،
خدمه پروازی اضافی که برای آموزش در هواپیما حضور داشتند، توانستند کنترل اوضاع را به دست بگیرند
؛ این مقام گفت «خوش‌شانسی پرواز همین بود، وگرنه ممکن بود با یک ۱۱ سپتامبر دیگر روبه‌رو شویم.» N12 همچنین گزارش داده پس از ارزیابی وضعیت توسط رؤسای
ارتش اسرائیل، شین‌بت و موساد، ارزیابی فزاینده‌ای شکل گرفته که حادثه ممکن است یک اقدام تروریستی بوده باشد و گزارشی هم ادعا کرده خلبان متخاصم عمانی بوده
با این حال، این ارزیابی هنوز قطعی اعلام نشده و تحقیقات ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24535" target="_blank">📅 12:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24534">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYPjJbVrYJnO5DitTtt4jVipfuccC2hWFyao9DdWV2bF0TsmmUeqZZ5V016OVpjbzklak4wymLLe2Sl6Df1PJ3NjLqEGh4k9A-eXEloqrBpI8plEFSRnZB4zeLCQlecbvAcOB9SfBpkvUGeSaQXG6RDG83RseGutJyC7K62ABFXNT38xh1QbSEvTwbSazSQtkoBI7-i9jm-3kcNIom9ifCha8dq05KV8S9nztOzvuKXvjUcpphddmHhIlLoxUzQe3Na5W7sqeQLtjv5MlV1ZxBkIgv1LKQtYQawbbhm9N0RTUo2XDv8-zUzvAs44U2R2jFWLEYN1j55JwXao1U9mkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه اعلام کرد حکم ، علی همتی و مجید نیک‌اندیش، دو تن از ‏بازداشت‌شدگان اعتراضات دی ۱۴۰۴ در مشهد، بامداد چهارشنبه هشتم مهر اجرا شد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24534" target="_blank">📅 12:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24533">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گاردین:کاخ سفید به طور مخفیانه از امارات متحده عربی و عربستان سعودی خواسته است تا اختلافات خود را کنار بگذارند و اجازه دهند یک فرماندهی نظامی واحد برای مقابله با حوثی‌ها تشکیل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24533" target="_blank">📅 11:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24532">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84bc09bb3a.mp4?token=R7fkPVRLQS1889tb2ukwZ5rHPF-tdpVuU_S7yPzQL4KnmRday4WcKtMRgWzSk6esuSr_AgU5HugtJrllydgHyOJ9yOmjkyelzn5PHuRJkp8gC40frKLdU-N-PT5WuPex6rA2qRneauZ55I2y5AwW-o1f4NkXVjtONmq7g-_ogSnV6KGtmw7CrCjCaot38BO4mOopGptfDo_G04FP4FYoQewj7QPxIP-xrochnxwgHxIiSYunU4_CdFICCS5lvYxjZiH1l95jj-h-Nh3Ph-zm63FnwaABe0hJdZvePPvGD3El85MdV1q2uLhQvPKGWNTzsCQ_uJeSXRFURc7S0PlovDdvzcBwTn-mVl4T5sbgt_dghij_7Y6FtreotQFTGDXxKeNnd_EA9QIGdH-X-iS__URNGKXHXCOOLKharHQoAfvwZei7A9rksBKeVAXfaP4Gifx1-xMvwPAU6xI87Ko7_o9cr6BjNENLza4yd-aAlA-0K7uZX5HKif7YVHd2foss2p38vb31td7lkV7MzBfwh6Hd1n-w3h3fq_nOlyWX1ni-QWYIYUWH-oOsLbvHt2cwH1uZIppdZjo77LpI81erTsory1pQ1t3DxvW5EAVoUDZB6xuHs6XUXJ09OrCCQ-GT3l01iS-YGWU3GJLbUn_LptTtnsbQ5kZzu4g07kJCNqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84bc09bb3a.mp4?token=R7fkPVRLQS1889tb2ukwZ5rHPF-tdpVuU_S7yPzQL4KnmRday4WcKtMRgWzSk6esuSr_AgU5HugtJrllydgHyOJ9yOmjkyelzn5PHuRJkp8gC40frKLdU-N-PT5WuPex6rA2qRneauZ55I2y5AwW-o1f4NkXVjtONmq7g-_ogSnV6KGtmw7CrCjCaot38BO4mOopGptfDo_G04FP4FYoQewj7QPxIP-xrochnxwgHxIiSYunU4_CdFICCS5lvYxjZiH1l95jj-h-Nh3Ph-zm63FnwaABe0hJdZvePPvGD3El85MdV1q2uLhQvPKGWNTzsCQ_uJeSXRFURc7S0PlovDdvzcBwTn-mVl4T5sbgt_dghij_7Y6FtreotQFTGDXxKeNnd_EA9QIGdH-X-iS__URNGKXHXCOOLKharHQoAfvwZei7A9rksBKeVAXfaP4Gifx1-xMvwPAU6xI87Ko7_o9cr6BjNENLza4yd-aAlA-0K7uZX5HKif7YVHd2foss2p38vb31td7lkV7MzBfwh6Hd1n-w3h3fq_nOlyWX1ni-QWYIYUWH-oOsLbvHt2cwH1uZIppdZjo77LpI81erTsory1pQ1t3DxvW5EAVoUDZB6xuHs6XUXJ09OrCCQ-GT3l01iS-YGWU3GJLbUn_LptTtnsbQ5kZzu4g07kJCNqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحرکات نظامی امریکا در عمان @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24532" target="_blank">📅 11:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24531">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فلای‌دبی: پرواز FZ1073 از دبی به تل‌آویو در مسیر دچار حادثه شد.
فلای‌دبی اعلام کرد این هواپیما پس از وقوع حادثه، در
فرودگاه تبوک عربستان به سلامت فرود آمده و تمام مسافران و خدمه سالم و در امنیت هستند.
این شرکت اعلام کرد تیم‌هایش در حال همکاری با مقام‌های مربوطه هستند و جزئیات بیشتر پس از تأیید اطلاعات منتشر خواهد شد. فلای‌دبی در این بیانیه
علت حادثه یا گزارش‌های مربوط به درگیری خلبانان و فعال‌شدن کد ۷۵۰۰ را تأیید نکرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24531" target="_blank">📅 11:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24530">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرنگار کانال ۱۲ عبری: مقام‌های مسئول در حال بررسی این موضوع هستند که آیا یکی از خلبانان، خلبان دیگر را با چاقو زده است یا خیر.
قرار است یک هواپیمای دیگر از دبی به عربستان سعودی اعزام شود تا مسافران را سوار کرده و سپس پرواز خود را به مقصد اسرائیل ادامه دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24530" target="_blank">📅 11:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24529">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«
اوضاع تحت کنترل است.
ما در حال تلاش برای
بازگرداندن مسافران به اسرائیل
هستیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24529" target="_blank">📅 11:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24528">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کانال 14 عبری:یک گزارش تکان‌دهنده: به نظر می‌رسد یکی از خلبان‌ها قصد خودکشی داشته است، اما خلبان دیگر از این کار جلوگیری کرده است، در حالی که آن‌ها با یکدیگر درگیر بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24528" target="_blank">📅 11:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24527">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRahat</strong></div>
<div class="tg-text">کانال ۱۲ اسرائیل : خدمه پرواز شامل یک خلبان روس و یک کمک‌خلبان اوکراینی بوده‌اند. @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24527" target="_blank">📅 11:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24526">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آکسیوس: مذاکرات ایران و آمریکا با میانجی‌گری قطر به بن‌بست رسیده است.
سه منبع مطلع گفتند تلاش میانجی‌های قطری برای ایجاد توافق میان تهران و واشنگتن پیشرفت قابل‌توجهی نداشته و
هیچ‌یک از دو طرف حاضر به عقب‌نشینی از مواضع خود نیستند
. اختلاف اصلی بر سر رفع محاصره دریایی آمریکا و بازگشایی تنگه هرمز در برابر امتیازات هسته‌ای ایران است. میانجی‌ها قصد دارند تلاش‌ها را ادامه دهند، اما بن‌بست موجود
نگرانی‌ها درباره ازسرگیری درگیری‌های نظامی
را افزایش داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24526" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24525">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مورگان اورتگاس، مقام ارشد پیشین دولت آمریکا:
اگر جمهوری اسلامی منتظر انتخابات میان‌دوره‌ای آمریکا است تا قدرت تصمیم‌گیری ترامپ درباره ایران محدود شود، دچار محاسبه‌ای کاملاً اشتباه شده است.
اورتگاس گفت در دوره اول ترامپ نیز پس از آنکه دموکرات‌ها در انتخابات ۲۰۱۸ کنترل مجلس نمایندگان را به دست گرفتند،
کارزار فشار حداکثری علیه ایران ادامه یافت و ترامپ در سال ۲۰۲۰ دستور کشتن قاسم سلیمانی را صادر کرد.
او تأکید کرد تغییر ترکیب کنگره لزوماً مانع اقدام رئیس‌جمهور آمریکا علیه ایران نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24525" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24524">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کانال ۱۳ اسرائیل: دو خلبان پرواز فلای‌دبی از دبی به تل‌آویو داخل کابین با یکدیگر درگیر شدند و پس از درگیری، کد ۷۵۰۰، یعنی هشدار هواپیماربایی، فعال شد. هواپیما هنگام عبور از عربستان تغییر مسیر داد و پس از برخاستن جنگنده‌های اسرائیلی، در فرودگاه تبوک عربستان…</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24524" target="_blank">📅 10:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24523">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کانال ۱۳ اسرائیل: دو خلبان پرواز فلای‌دبی از دبی به تل‌آویو داخل کابین با یکدیگر درگیر شدند و پس از درگیری، کد ۷۵۰۰، یعنی هشدار هواپیماربایی، فعال شد.
هواپیما هنگام عبور از عربستان تغییر مسیر داد و پس از برخاستن جنگنده‌های اسرائیلی، در فرودگاه تبوک عربستان به سلامت فرود آمد. منابع اسرائیلی می‌گویند
هواپیماربایی واقعی رخ نداده و کد ۷۵۰۰ احتمالاً در جریان درگیری خلبانان فعال شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24523" target="_blank">📅 10:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24522">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سی ان ان :
به گفته یک مقام اسرائیلی آگاه از این دیدار، نتانیاهو در سفر اخیر خود به ابوظبی، اطلاعات جدیدی از فعالیت‌های هسته‌ای ایران ارائه کرده و از
ساخت‌وسازهای جدید در سایت «کوه کلنگ» در حدود ۲۲۵ کیلومتری جنوب تهران
خبر داده است؛ سایتی که اسرائیل آن را یکی از مکان‌های احتمالی برای بازسازی برنامه هسته‌ای ایران می‌داند. این مقام همچنین گفت
ایران در کانون گفت‌وگوها قرار داشته است.
به گفته این منبع،
اسرائیل احتمال حمله ایران در چند هفته آینده را نیز مطرح کرده است.
در نشست گسترده‌تر، موضوعاتی از جمله
ایران، حوثی‌ها، تنگه هرمز و باب‌المندب
مورد بررسی قرار گرفته است. این شبکه به نقل از دو منبع از حضور یک
مقام ارشد امنیتی سعودی
در این نشست خبر داد، اما
عربستان سعودی بعداً حضور نماینده خود را تکذیب کرد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24522" target="_blank">📅 10:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24521">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر امور خارجه قطر، گفت
کاخ سفید تنها ۳۰ دقیقه پیش از آغاز جنگ با جمهوری اسلامی، دوحه را از قریب‌الوقوع بودن عملیات نظامی مطلع کرده بود.
آل ثانی در گفت‌وگو با برنامه «پیرس مورگان بدون سانسور» گفت هنگام دریافت تماس کاخ سفید، در دوحه خواب بوده و مقام‌های آمریکایی به او اطلاع داده‌اند که
عملیات نظامی به‌زودی آغاز خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24521" target="_blank">📅 04:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24520">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaeY1uakojVXvAzbXbJEk6NU28fLAYiOkSd9mqhKyQVd2Kx7Lr0W9K72Ov21cO6jiO_x21WEemDDDmZAMtWDhL9GTMcMWYsinoJFP6mJ6B5R71OTSghgolaBlyO-tj2OnmBP5J_MNCYt9GXYb-xILxPU28RUKQ4BdDlv4E5stZjBeO5MeJkUvpqaYWKzCEPfsg4sisQaWSVxEYBeBbhQK0ISX1-O2ntGgA2g1m8akNq9uKIe7oD6dv5-WZiBShXxcU-IxDyi5eqikX8zyT_8ZVWq1M-HL4-z2CwQPFugn3XZkhku6zZy_F9nv3KcvQCUpWDStR552xbW2B_ocCi38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث تحلیلی را بازنشر کرد : ایران عملاً کنترل تنگه هرمز را از دست داده
الکساندر اشتال از مؤسسه «بورگ‌گرابن آنالیز» مدعی است که
ایران عملاً کنترل تنگه هرمز را از دست داده
و صادرات نفت خاورمیانه به حدود
۹۴ درصد سطح عادی
بازگشته است. به گفته او، امارات از ماه مه با ایجاد سازوکاری موسوم به «شاتل هرمز»، نفتکش‌ها را از مسیر نزدیک سواحل عمان عبور داده، نفت را در دریای عمان به کشتی‌های دیگر منتقل کرده و سپس نفتکش‌ها را برای بارگیری دوباره به خلیج فارس بازگردانده است. این روش بعداً توسط
عربستان و کویت
نیز به کار گرفته شده و اکنون حدود
۱۱۶ نفتکش
در این چرخه فعال هستند. به گفته اشتال، ناوگان بحری عربستان نیز با ۲۳ نفتکش در منطقه فعال شده و سنتکام با تعیین مسیر و زمان عبور نفتکش‌ها و تمرکز پوشش هوایی و دریایی، از این جریان پشتیبانی می‌کند. در مقابل، او می‌گوید صادرات نفت ایران به‌دلیل کمبود نفتکش‌های حاضر به ورود به خلیج فارس و فشار محاصره آمریکا به‌شدت مختل شده و
بارگیری نفت در پایانه خارک از ماه اوت عملاً متوقف بوده است.
اشتال در نهایت می‌گوید ایران نتوانسته تنگه هرمز را ببندد، انتقال نفت از مسیر عمان در حال گسترش است و گلوگاه اصلی اکنون
تجهیزات انتقال نفت از کشتی به کشتی در دریای عمان
است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24520" target="_blank">📅 03:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24519">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiA9MFpdUaIYoSvVz1pmJlUCFOh9Mi073tioXqKtXDZ93kAK3P0WRuFkJ2zle6FTIfLaJ5zrUm55j6lDoBsiHZFvKt5qwMblSYPRc-uMvb0edVAo9kHOk20eXOlu_tftxiZvOELOM_OhDY0cQUbMjggNoARQb9Jq-Fwdvgnnvus153VGx8yORR8od8Ro01SZHb6lGmQiGL9Ao_PhoNCI9OYyIZwl77vsok0lsSbuT-anFiqqJCDT53-2C2dTcMKYxiGCt06p4R22YR0Vsu8mfuYUt5loBTYgwFB-205sF7iUn3PC2HQt2RzXP6sdf7kl822TZ_YBi0mIQ8voh86FsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی و هیئت اعزامی بالاخره از نیویورک دل کندن و بعد از توقفی در دوحه قطر به تهران بازگشتند. همچنین شش سوخترسان در منطقه تنگه هرمز و خلیج فارس فعال هستند و یک پی-۸ پوسایدن در دریای مکران فعالیت می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24519" target="_blank">📅 03:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24518">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آکسیوس: احتمال شروع جنگ بسیار بالاست
آکسیوس به نقل از مقامات آمریکایی: ممکن است ترامپ پس از انتخابات دستور بازگشت به عملیات رزمی گسترده علیه ایران را بدهد.‌‌
ایرانی ها اعلام کردند تا زمانی که واشنگتن با بازگشت به یادداشت تفاهم موافقت نکند، امتیازی نخواهند داد.‌‌
هیچ پیشرفت محسوسی در مذاکرات روز دوشنبه حاصل نشد و ایرانی‌ها چیزهایی را طلب می‌کنند که واشنگتن نمی‌تواند آنها را بپذیرد.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24518" target="_blank">📅 03:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24517">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRPMp2IKhyE7cSpCDbsxcPHkwHj_1mXwdv_NHqaGfX_lGj7lGe-kJHkqAY6hb4lacOc1o7G57uUMaZJIroas1Mtjsev-Xt21G9XWeZARDGGA90w9-95x7MfIj6TY5RooED9XALetrw21tnlhukphclWW83v6USYN-WmDdYxRaHdIUn6wm69s2wbZUP4FRsHxfUUxrInT2zRQPwjHUgvwPf-sHXT5ta5g7vzzztLBrUkIjtKWcYMexDAmg1ZHffvOMNK2sflY7k5Ko41h7hjfNN9o1LZNXR_0RIVQC5MHZgy-L9FIqwtaMsqpxYz9dDXyjr_ZrG3357EVGdLebXgIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا در چارچوب برنامه «پاداش برای عدالت»، برای دریافت اطلاعات درباره
احمد فرهادی، عبدالله محرابی و علی‌اصغر نوروزی
، از مقام‌های نیروی هوافضای سپاه پاسداران،
تا ۱۵ میلیون دلار پاداش
تعیین کرد. این افراد در توسعه موشک‌ها و پهپادهای ایرانی و تأمین مالی و تجهیزات سپاه نقش دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/24517" target="_blank">📅 02:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24516">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d5adfdf90.mp4?token=ZxBKohlEU-np9izIps8T-25-y8nuv7mw93p6AWY9B6oz90hCoUtBhcq3pgBlA-iBc4e6-xPGp0AxjQ-B7OQkFYs53mtsoi8zRgwcQQb5ZitKwSaoBXeP_Ga7bA9BB00sOWcE6cz7kby8ZjG40CoYc0sCIPmB3oGjiY27ovemHs_FwhnAPSrUR_OH8wjiUzhBTWrrqTqvEpexpVZZDSSRd22Cd4dCcp208ry1o2D5cL4g2AxQMuR64mnMXEHeEQGKDkYIS3yf6te49iPVWUF7dBO74DL0ShTa0Dw7CVueCetVEHOOHYo3q1WWpOj1YEtIvVf8Dvc8-58ISacqCtRy9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d5adfdf90.mp4?token=ZxBKohlEU-np9izIps8T-25-y8nuv7mw93p6AWY9B6oz90hCoUtBhcq3pgBlA-iBc4e6-xPGp0AxjQ-B7OQkFYs53mtsoi8zRgwcQQb5ZitKwSaoBXeP_Ga7bA9BB00sOWcE6cz7kby8ZjG40CoYc0sCIPmB3oGjiY27ovemHs_FwhnAPSrUR_OH8wjiUzhBTWrrqTqvEpexpVZZDSSRd22Cd4dCcp208ry1o2D5cL4g2AxQMuR64mnMXEHeEQGKDkYIS3yf6te49iPVWUF7dBO74DL0ShTa0Dw7CVueCetVEHOOHYo3q1WWpOj1YEtIvVf8Dvc8-58ISacqCtRy9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی مجلس نمایندگان آمریکا، مایک جانسون:
سناریوی وحشتناک این است که، خدا ناخواسته، دموکرات‌ها کنترل مجلس را به دست بگیرند. آن‌ها هر کمیته‌ای از کنگره را به یک نهاد بازرسی تبدیل خواهند کرد.
آن‌ها در تمام طول روز، هر روز و هر ساعت، به جای انجام کار، فقط به دنبال حمله به رئیس‌جمهور، خانواده‌اش، اعضای کابینه، حامیان مالی حزب، چهره‌های برجسته در بخش‌های تجارت و صنعت خواهند بود.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/24516" target="_blank">📅 01:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24515">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مارک لوین : آماده باشید، سوپرایز در راهه
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/24515" target="_blank">📅 00:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24514">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/042e52e439.mp4?token=MedopXZWwJFZ6NqES3vM6eUDGkOJ5jMGW2HDhVCikh_S33dNEVhYvLQwAYt8O_Y9kroA-kIC1_VjiNIW89qef43OEQGrwEllcSIJIvQ0k_VySiM8zLID1mTIpK6x5M1DFCVLdXsI-nK8o2-KeGvmiqyxscjlfxCqf8M0bv6qO_mAQcV5hBmp-a8cwuLNYwNYhIG1PtKuehMzXMmvtFj--oHaieSPUSFdya26i0c0vYPwMLCVyZY1CfN5pQl5dC7geHdpW9yQ6KIn02aoXEZcH74DbH3U0yEnz6JGwoo_iJGhEvrbJ4s12X_PSEtN_5OTklFDukoVamXbYfLgVdnQHS1BN_XRQ4G7yafTVNvt6wb5QI_Truwp4JAmKFbC2hqtBa_IH5geWW5zaITqfO0QWWrq-8Zal4ZG1bc0uVccIkJ8lq4yZT6Kd2TyxVnTDhJitlQJns5mpNde5Fz17vIj1VhI0-6mvuN25NXTjSgUjE_yVTmO8_0i56XBrUqBE1VNeYC0Qr6hyKpn4meIKkYLaXDXW20S0k6qw8N9bp948STqbpbv_6O3TFpOMUf5tx8Emla62m7OZfWRek_26p8p3KWoT01TkMjnh4g1JbqIYKGjbATBB-8w4JmSn5K0E9mQ5-FsTebvpXTj4-tHnLWbqhhLUemY2vo-x9sqgnJL_JU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/042e52e439.mp4?token=MedopXZWwJFZ6NqES3vM6eUDGkOJ5jMGW2HDhVCikh_S33dNEVhYvLQwAYt8O_Y9kroA-kIC1_VjiNIW89qef43OEQGrwEllcSIJIvQ0k_VySiM8zLID1mTIpK6x5M1DFCVLdXsI-nK8o2-KeGvmiqyxscjlfxCqf8M0bv6qO_mAQcV5hBmp-a8cwuLNYwNYhIG1PtKuehMzXMmvtFj--oHaieSPUSFdya26i0c0vYPwMLCVyZY1CfN5pQl5dC7geHdpW9yQ6KIn02aoXEZcH74DbH3U0yEnz6JGwoo_iJGhEvrbJ4s12X_PSEtN_5OTklFDukoVamXbYfLgVdnQHS1BN_XRQ4G7yafTVNvt6wb5QI_Truwp4JAmKFbC2hqtBa_IH5geWW5zaITqfO0QWWrq-8Zal4ZG1bc0uVccIkJ8lq4yZT6Kd2TyxVnTDhJitlQJns5mpNde5Fz17vIj1VhI0-6mvuN25NXTjSgUjE_yVTmO8_0i56XBrUqBE1VNeYC0Qr6hyKpn4meIKkYLaXDXW20S0k6qw8N9bp948STqbpbv_6O3TFpOMUf5tx8Emla62m7OZfWRek_26p8p3KWoT01TkMjnh4g1JbqIYKGjbATBB-8w4JmSn5K0E9mQ5-FsTebvpXTj4-tHnLWbqhhLUemY2vo-x9sqgnJL_JU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفتید ایران نمی‌تواند سلاح هسته‌ای داشته باشد. چرا؟ کره شمالی می‌تواند سلاح هسته‌ای داشته باشد؟
ترامپ: «آه، چون شما رئیس‌جمهور متفاوتی داشتید!!!
کیم جونگ اون
. او دوست من است. ترامپ را دوست دارد و من هم او را دوست دارم. تا زمانی که من اینجا هستم، او در امان خواهد بود. می‌دانید چرا؟
چون برای من احترام قائل است.
»
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/24514" target="_blank">📅 00:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24513">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a35cfdae.mp4?token=n9ubQD1pZu9IMyS57BeGGShL0sc9Tk3XwYR0KGrsX67N3isBQmzLCmhnlDIo9BmfVVCOeAf1SPwGaGpHSEGSHZDEn_xLLJoGgOvDGyDbwQcll-ET21hSSPYnXy5OnkkqQezU4G1VlfzJXRk6cQzuNCTnAJH1z3CNqzXpSHynHM80MmTdlmsVdeq1nDVFg-ifV3vCcACuc5ZRjdzc88tn6_fCIo3duLNuYE6h66QsYCAV8lbg0ON0ji--OuyPsbWttUkJvB0BjpMFu4hhXl002TKgjChW7RBtpnX1Cf8L7YF2lfHNozHNyYEuGuItlWgLMCpJ7t9xjB_nMx-QgT7izg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a35cfdae.mp4?token=n9ubQD1pZu9IMyS57BeGGShL0sc9Tk3XwYR0KGrsX67N3isBQmzLCmhnlDIo9BmfVVCOeAf1SPwGaGpHSEGSHZDEn_xLLJoGgOvDGyDbwQcll-ET21hSSPYnXy5OnkkqQezU4G1VlfzJXRk6cQzuNCTnAJH1z3CNqzXpSHynHM80MmTdlmsVdeq1nDVFg-ifV3vCcACuc5ZRjdzc88tn6_fCIo3duLNuYE6h66QsYCAV8lbg0ON0ji--OuyPsbWttUkJvB0BjpMFu4hhXl002TKgjChW7RBtpnX1Cf8L7YF2lfHNozHNyYEuGuItlWgLMCpJ7t9xjB_nMx-QgT7izg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره ایران و تنگه هرمز: «ما طی دو روز گذشته
بیش از هر زمان دیگری در تاریخ، نفت را از تنگه هرمز خارج کرده‌ایم.
»
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/24513" target="_blank">📅 23:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24512">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/431a4ea541.mp4?token=OLY1kuTOQoLiglnaOqlbrsYQIkcAYeAtPblZ0xFxklBd5Pw30eR3g3rMKynesvBkFbqGCsrf1_Hxb8vnHzRVxoUp9U6BoGc8tI1PAPZKBjD-72XdRkN8ZuXIGw1ilQNqNEmTobzAslpK1OBB7HOC2dy0bRIxbQkoxtdeop1dBqUJMnWaxoTMKMKloNFDORV38mN5ILXpAqXhV5-stcZnsjnC6SfQRVgYPTHjalGIcFUfHxZDp5AeU-jpvUiIGxvsp4Ds3MRxM2ajZXj_VgtKhUczXY1emStKZFtuKk0iJEaRiUnT--3GANkWUW2Iw6-s3b8k6QAFyCmIdzjeMjZYyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/431a4ea541.mp4?token=OLY1kuTOQoLiglnaOqlbrsYQIkcAYeAtPblZ0xFxklBd5Pw30eR3g3rMKynesvBkFbqGCsrf1_Hxb8vnHzRVxoUp9U6BoGc8tI1PAPZKBjD-72XdRkN8ZuXIGw1ilQNqNEmTobzAslpK1OBB7HOC2dy0bRIxbQkoxtdeop1dBqUJMnWaxoTMKMKloNFDORV38mN5ILXpAqXhV5-stcZnsjnC6SfQRVgYPTHjalGIcFUfHxZDp5AeU-jpvUiIGxvsp4Ds3MRxM2ajZXj_VgtKhUczXY1emStKZFtuKk0iJEaRiUnT--3GANkWUW2Iw6-s3b8k6QAFyCmIdzjeMjZYyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره ایران: «نمی‌دانم هنوز قرار است تسلیم شوند یا نه، اما
تسلیم خواهند شد. آنها وضعیت بسیار بدی دارند.
»
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/24512" target="_blank">📅 23:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24511">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMQPtEaDBjqu0TU1xIY-kKORbhg5L0cRlYwqZjBYF8XnlII7_SXbItrw93lnP_c_eCYXIMjP2qExVxmTbnUeN5ZNqLtnPO12zjxdydyhxcgqra1jwIdgMy8FVojiZgqi5Qk4REdeT9Z1XW4dGF1lkZ_RYrnEWZvury7CjuaKa_RbZL-4iVT5n9AyHS-gSLObbd4uBWuV2gLJopaRvMge7hBvlAyvsWEo1-Z0N-u-b8H6PASw07Z9m9B9ehrwmsbYUIeIbUNWz_FlFbuCrAkagqd-m1L0aT--oA4xoerOUqkIZa4uqJNmOvPhcig3EIWsFuHvKqtedU5uUoJXmFQNSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ سوخترسان و یک پی۸ پوسایدون در حال انجام مأموریت در تنگه هرمز و خلیج فارس
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/24511" target="_blank">📅 23:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24510">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wh2UR3sWpXJcV_w0-2dsLgiEebgSwHjxgDNvqd1eEvG0ZXt-55NDg5msjCfPv1KKL8e7O4_-iZpvvnmoLVQNrp_0UmxUlenIxePI0d8DOddYk5kWPx24yx_iauWNTjadh3rXctnr5BKuJLZie_Nc9xov5v7p6BHF2ONgYWOEkJydrFLKEs_pd5zmSMb4WjIB9csiIucZ-iDO0Y5xSHlLeAGB8hOeh9gf-nmyTw1XK18OwFwLrhWdUqu-9EKY94F8DfjH8fpJ67nENAbDnLkZuhBPh0pShU2wOMWTuWRUYBmuvJnfivIpG4W8bdoxt75iZxJAxAuHLtJ-BPQZfXP5Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۲ اسرائیل
: اسرائیل برای جنگ بزرگ تر از ۴۰ روزه بمب سنگرشکن خریده است
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/24510" target="_blank">📅 23:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24509">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دلار ۲۵۶،۰۰۰ تومان (رکورد تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/24509" target="_blank">📅 22:43 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
