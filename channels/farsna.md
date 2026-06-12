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
<img src="https://cdn4.telesco.pe/file/gQQqWhgyXtQWK5_9N8-q6vyUpEBsLNCyQ9iLjf49lGK7xG-CiBaauy06TaP-0AQJslSNIjaWkAb4ImXi5cXdwNNXZmBVZhGsP0UljDZnwtTJROAOpaVjq2TTYnD9X_F_nqGPow1pYVDWeNiWZZ95FRl5RPsPLJOTCm4lY0bKXNmpye3q-EYy4zqHEzXNrU1RWDH4f2ycF1N8TGoY4-5p9i4DSP3ogIvIBvznt-64ixAH6DkbmNnGjZDqWrhwdGdhHhfA8n33h1bDaZlCaRWn3L0r5QmNUMQbHsVSKz5FQKu8agIxpPuePF5u_JTuzNwsdD_N6JEyIaOH16RFloPh6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 00:32:11</div>
<hr>

<div class="tg-post" id="msg-441694">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWf9N8708OU3pZ9KZU0viTVv5ew9qp5FUu1A7mdcnmvuJN92ZpM8jfHoTAsuLGXET4LU7VXk2Eg7BgmF7vGlTSxbliWkppDlK4TL-8C_0Q-7muiUavX-GNpW1frfiFIGym4Y5WU8nQkWMwtRRROUo8ZPcZRq2Jt_pyf-N9koIFPHVO4nE_6WBHMdsLG7YhfCTvTqgQ9QvIQVIM9q-HXQRlTmP1-lKrpvc91CZuG0zktro6Q8rwuDEhkEGtnhzEvfiCfwOJQrARF3KYhvUgWy7tMoFnX_3k1XwyVtR_uWDtyosXIBd95x3oeV0YueTKf7xoBE9Cl223HSYi2FtuhtXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانادا و بوسنی به تساوی رضایت دادند
کانادا ۱ - ۱ بوسنی
@Sportfars</div>
<div class="tg-footer">👁️ 973 · <a href="https://t.me/farsna/441694" target="_blank">📅 00:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441693">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تغییر شرایط ثبت‌نام حج ۱۴۰۶
🔹
نمایندۀ ولی‌فقیه در امور حج‌وزیارت: طی جلسات برگزار شده، مقرر شد ثبت‌نام حج سال آینده زودتر آغاز شود.
🔹
تأیید استطاعت جسمی و معاینات پزشکی زائران پیش از واریز وجه و ثبت‌نام نهایی انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/farsna/441693" target="_blank">📅 00:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441692">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/741bda4987.mp4?token=Qe6wfamvSvWrFtcloaD2UxAkSwkN9nteyH3xT_wHAid6aG1V3orL-6ZPVWGJhuL_2FNqmTAtcY9fyC_I_-s4Is5KXtUNzJGwcT3DejlaPsiuwUI1uFhDM-hNfhEaqsXaDPN1vfTxvn2REcNrWqw1-OkRccJptG4-su1MHAvA0HvGpPuhJpa2j_lADSEAeklJmq1Ao-R3sNfqHHoQvnWKj0UMApfeJpTTsCaVWk4p70ICtIQu6uGGOVqb6BcqCLE_2V4OfF0vpfQnFq-eYtQIJqWjWORgX5oUwM8GzvibL8owFOKctyHQ78xkgd-R98OHNvXew2rNGOZrURv8MD09_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/741bda4987.mp4?token=Qe6wfamvSvWrFtcloaD2UxAkSwkN9nteyH3xT_wHAid6aG1V3orL-6ZPVWGJhuL_2FNqmTAtcY9fyC_I_-s4Is5KXtUNzJGwcT3DejlaPsiuwUI1uFhDM-hNfhEaqsXaDPN1vfTxvn2REcNrWqw1-OkRccJptG4-su1MHAvA0HvGpPuhJpa2j_lADSEAeklJmq1Ao-R3sNfqHHoQvnWKj0UMApfeJpTTsCaVWk4p70ICtIQu6uGGOVqb6BcqCLE_2V4OfF0vpfQnFq-eYtQIJqWjWORgX5oUwM8GzvibL8owFOKctyHQ78xkgd-R98OHNvXew2rNGOZrURv8MD09_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌و‌هوای این روزهای گلزار شهدای میناب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/441692" target="_blank">📅 00:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441691">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhwCBqlrqd7pKxE5DavsjFArwmoW4o0Qid5KnpKMV7-R_y8srJkd-eMNcZM0-komtJttLF9eS7lwZ5EREayMbNN0HbSZllBDLt5AddPzOAdVpYGLsvuuQPLLtSyc8EbWTxVM6wZAzuVtZ3i4KRjHvv5G_3RL1C_6kl9SENOqP0452AlLbtCxcs42C6bIN_4E3vfWj3nQOG3-WAbuCTd6V7cWoHpod6VWaVS2yL_gUrzz1RYobgvdqptYubPsBtWIgMb0AYyho0MEuPb4IASi6Etxi6Q8pMQDX27x2lTkhykxNHCrIb-QqncD3Yu1KP45KR5bRQhuIrDDC70XTyc-_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
امروز به‌صورت همزمان گروه‌های سرود جان‌فدای ایران، به‌طور نمادین سپر انسانی در اطراف زیرساخت‌ها تشکیل دادند.
@Farsna</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/441691" target="_blank">📅 23:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441690">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32598f106c.mp4?token=ch326iqrLP1kwEQT_en5JLVK9fsdUNt16wB_aAafKabT4FNg9_nJ-QIy0gsBaf6Q-xKpYV2jyZRJUF8Rv_IuJ10CHmFG8FPoGreQNdHyTBgKmOknPfGoc5uDHiv1zB1n9IhEsWEH0hYWCntlZsO9xcM07kD-otGbtyZCi4NpLqLQq1fG4TnPc7sDmG_pnlAkU4O_6cCKevdbkyvWeSA7aFWbMeX2WQS2BKn2SbUYJoT-D_MpLxk0BHmrbG-9-3277lfITKF4Dnw8uzNK19sa3ndMzTc-J1a48s9DgBShyO86sR2iuR0cJ-W4v1vLMmSfJsuQts9InvyUPtyVAEhBnrNVRbEXr-WaMmeu3jcaoxSq0S0_28eC4a7Q-iT7keXFY4EtoBT8xDW-ewgTsExNUEV0d0iU5dcN1Z_V6Pr2BBoSJrjGEadNAUKeUoPeaPBY4Vw2bRNg9XwIuZDCeaqcU7W0IIJTv81sdVO4A24hM8J4he-V8KdUaXUrEqCeTDUlMXSklBIhP1iUipzuWrS86DcO5EwnzNQgdAA_FyxkMrHJARHqVz8JpY5O580sn2hPwUnkTMbT0pthsGVFIQulbYY7s9g1lNWajMR4dRbxrLxoOJcfjYxTXDsdApM2K--i2Qc5RAOGkjR5yN18yt4M9IPc8jMZ1ZMR1AWpUzSl25Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32598f106c.mp4?token=ch326iqrLP1kwEQT_en5JLVK9fsdUNt16wB_aAafKabT4FNg9_nJ-QIy0gsBaf6Q-xKpYV2jyZRJUF8Rv_IuJ10CHmFG8FPoGreQNdHyTBgKmOknPfGoc5uDHiv1zB1n9IhEsWEH0hYWCntlZsO9xcM07kD-otGbtyZCi4NpLqLQq1fG4TnPc7sDmG_pnlAkU4O_6cCKevdbkyvWeSA7aFWbMeX2WQS2BKn2SbUYJoT-D_MpLxk0BHmrbG-9-3277lfITKF4Dnw8uzNK19sa3ndMzTc-J1a48s9DgBShyO86sR2iuR0cJ-W4v1vLMmSfJsuQts9InvyUPtyVAEhBnrNVRbEXr-WaMmeu3jcaoxSq0S0_28eC4a7Q-iT7keXFY4EtoBT8xDW-ewgTsExNUEV0d0iU5dcN1Z_V6Pr2BBoSJrjGEadNAUKeUoPeaPBY4Vw2bRNg9XwIuZDCeaqcU7W0IIJTv81sdVO4A24hM8J4he-V8KdUaXUrEqCeTDUlMXSklBIhP1iUipzuWrS86DcO5EwnzNQgdAA_FyxkMrHJARHqVz8JpY5O580sn2hPwUnkTMbT0pthsGVFIQulbYY7s9g1lNWajMR4dRbxrLxoOJcfjYxTXDsdApM2K--i2Qc5RAOGkjR5yN18yt4M9IPc8jMZ1ZMR1AWpUzSl25Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت دفاع: دست به ماشه آماده دفاع از ملت ایران هستیم
🔹
سردار طلایی‌نیک در گفت‌وگو با فارس: نیروهای مسلح همانند گذشته برای ناکامی دشمن و شکست‌های پیاپی آمادگی بسیار بالایی دارند.
🔹
نیروهای مسلح تا تحقق مطالبات به حق ملت ایران و خون‌خواهی شهیدان، پرتوان‌تر از گذشته برای پیشبرد اهداف و آرمان‌های دفاعی مهیا و دست به ماشه هستند.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/441690" target="_blank">📅 23:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441689">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
ارتش اسرائیل: پهپاد انتحاری حزب‌الله به مقر نظامی ما در مرز لبنان برخورد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/441689" target="_blank">📅 23:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441688">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6b06f1f8.mp4?token=JzX2EggXdEUv6y0IOg2bYLxUPvqHcMHnHKE6PhaoVO3DYLD-t9VyDoxTvB0Na6ghQzoWWYa4BE193Nvi78bsTS4-RKRFvk7P3Pp5PD0tb5Hjff0CFiOxm19Up-HfOZiu13NZS6PW92hCNxt8IPbmKQCNUqBkNePOBfEBs5P6KoOvCzi1JgKB-EybxdH0ty6KRA9sEVhP_Yf1nmcSbPf3ZIrGZ4aIuGsqGLqtAeK8i4xENv8lKHGufzm-vaXGZrC9HAZP4XQ7Idrwhxql5HcYfkxaPsNf7MCiN9FqdL0nGaLQuHWb3ykAVmMNju3qal_5IT-417NcQzS9yX357lP-SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6b06f1f8.mp4?token=JzX2EggXdEUv6y0IOg2bYLxUPvqHcMHnHKE6PhaoVO3DYLD-t9VyDoxTvB0Na6ghQzoWWYa4BE193Nvi78bsTS4-RKRFvk7P3Pp5PD0tb5Hjff0CFiOxm19Up-HfOZiu13NZS6PW92hCNxt8IPbmKQCNUqBkNePOBfEBs5P6KoOvCzi1JgKB-EybxdH0ty6KRA9sEVhP_Yf1nmcSbPf3ZIrGZ4aIuGsqGLqtAeK8i4xENv8lKHGufzm-vaXGZrC9HAZP4XQ7Idrwhxql5HcYfkxaPsNf7MCiN9FqdL0nGaLQuHWb3ykAVmMNju3qal_5IT-417NcQzS9yX357lP-SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین الله اکبر در قرار امشب مردم نیشابور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/441688" target="_blank">📅 23:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441681">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KpLcBUc5ka9az3_wAqXoUGY-SYQFrzebBNYFC8nbr92WyjvS1Vg10GerOCsfRsrmTBbOv0kB9Jm2WBfBDjHkxA0JfZxX1rn2dTO0Luidvk0vqwopT5o8dk4iJVa6-CofptvOQrzwI8JwP7rihSMaTa_tEhW8qcLWE0Xykn61AKfIx_TcGS2XXnEQRwfn8tGXfQsATZIdiGd_xwULX4a5s2ki5uz6jFpa4fSPvBGZZ_YiYsnTcGFuc_cmlibv2dq7OCHO82vxarn4eKcg1xS2DKDBUMoUK_CC4IXUqi4dvPdB2XOPALO9lRo1tfUBTz3XFNmYlikLFAo15AfWlUKRUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfK2cC9pIWVThKgLK9GqXRbZwTphen-q2vHFfhjBqFvsI_GazqVHADfKK9psUGHLC4Iut2aORHOa2srPabt_Zy5vBNhnV-8s-m-feUhDq_Gx2lcfodqCm-hQZB2bU-JBXWUi2P282p_dw1l9p6fZQlZUjF9v1l12jUQXhq6DDIbw_otPN-an5fQ5wxN251Ptrn9Jj37gBK1a2HCS08qsYXzc8MaX8ah19dLVpT2kCYDotI_txPnND5muwHf9ECUpxvEXtwg40GEgbLm0_v9fYZ_kMdGFjFJ9Mh7hI46Tjlmk4yyxUxZ3Bqv7J93R81fYWHsGZxOWtZ1ZKzhNjSb1NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoDvQGBnc1pHy7qLUVCf78I1FK0F-NzPPbgvZNS7OHrsh8ZbCmPpaswU8VheXw1lMSBAn_1Mb3o5_cDm5gtpvXadhKxx3lsXl2MUTHpEN-vPSQANpuYcMH4jor5mYLumKDGhxqE-4TY2rw50Ua8dHZcseN-mcgPEG3bgrTvpjwsqJr6EoAEjkSDTrGuzTmXYa0rexoaumqaUyzYeKKUZt9kaEaNtvXI9sT8QIfxPtxxwvnlJZsu6uKonwffIvfd2nbz7eY6Xiq-7vWI--GVq8EkXdFEvlO5-ddyKAxtzxYff4rZfB8YxAwPqpTvaA1ZAPgD8xz86u2x0YNn9zGTQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G25JcnN_3TVcC_5k2Gd8OHxYUzkBrVuwzA-qneH8rP8EfMWN5E8_547yTQT3cPkG8NXKAnmIhRsBUqCUA2lY5-DhRfwQxKWzw5U-6IyCzyV1D9RIjkClDeHcAXm0OZVVUWG0wX3RCpcmHb9EF9YIGWS0f5AkZvGyUMXw3XPeiBeoDhZ11FwR56Uq01xgV8M5uWNCzV6TTQsoVbNwFNZI8rw9JbK0T3bahaVhJSa2t_tOJy7iKHYR3ApaX6c8V-Rl-Y3-MqMRp14k9sGJRK0HZwnISZ_C_31woi5S483gfJEs9Fm2Ra2OqxJ0Qeb2Qheo8v8KHDhdIUAhio0_TiB1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eaGXBQn5P5K8VAZzk_afQ6A5enJTYhnrpGESPcxes2YjP-dpOjyOwihqarVUZhVzSkgIvXEQmaeSQpyJOxCjiXbFGq7cq6sXSzNrzwA1G4OTOTud_gJ8l62-E8Z52YvVFq3MUY9QcJ1NTxqYkmH6hSqBh4ZeW0TfvSQfRzFT21zFr90YeN80ESo7HwYaHJ7-SBvvrCTLJzgWSKnvSlqOV2erkcrnw26iIXvAw17u0PLOZ_oPOlLyTXN5fIwHOcCaHBlEOO5PxVX6kiQ5WoNjJ7D5dzNeOgFUmiTJR7ZEWiBctOPtYYDYPxxMXbQoE6NRVgcngDbDr5J0JKuJ2eRbBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N30Rz2kJjcpPK3qLLTrJrCOiF_5hxyCYE1Y8SB-6sYMPsBQh70fFgBla-RP2UiiFhFjNDPM926V0hNa6dwdbwoKqG6SfsMS0veP_ioGTympEEit-2fjIEAxrMExqax-zE8Y86zY84XHGWptC_HLq3T-AzGS1ExsdevXcjS4coRDJ2nBM4RYSemVS_ia7d5BXxd4yI2Xn5WWjNBF4qYD3EIoU3jHkkXFYbzr-4u-fPhQ_TZxd9vzF9ekeeZ9wlrTP4efMmRICz16FYxFwyvuOQ94hYYcVj8WOhliwY5hyv-U1xwqdkYjtLKUg9q6snoVPajRVmME0lTh1Sn0zLctMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fp2vrHZ35wc7A201QjtprNqIn9z4gAzTUGUgsA1zv9Ad_Ers3FAdI3v1o-Deq-_SEsK2Vu4aYMF5rkK4zTIb-fzL83GQH_qRT3L-nGLTHKEYiXAhCTGQTn2SRG_cueCGQVqY6YQrm3YvoVUuGoNLgyP3Xjp9LtVeJarqtOZjmFv81KDQ2Rqk38qjdmZpSf9sCa27c4npe9pclbz5HybG8fuDBGWQoauCBe7mUmvkGa4zXPOyHDhuLP-hMiUYYcizMwPFm5wngqP13JYfG7BkeOzprJlrsu8Lt4muvHuZGuvIjJ-2skezCLTiJUy-_HMakS89S4CiSPiYwutU3FX7gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ برگزاری مجلس ترحیم آیت‌الله فیاض، امشب از طرف رهبر انقلاب در قم
🔹
مجلس ترحیم مرجع عالی‌قدر آیت‌الله حاج شیخ اسحاق فیاض، جمعه ۲۲ خرداد بعد از نماز مغرب و عشاء از طرف رهبر معظم انقلاب در شبستان امام خمینی(ره) حرم حضرت معصومه سلام‎الله‌علیها برگزار خواهد شد.…</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/441681" target="_blank">📅 23:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441680">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌
🔴
عراقچی: یکی از مقامات آمریکایی به‌تازگی گفته که ما تازه فهمیدیم که ایرانی‌ها با بقیه فرق دارند. @Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/441680" target="_blank">📅 23:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441679">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
🔴
عراقچی: علت جنگ این بود که ما در مذاکرات از منافع‌ ملی‌مان کوتاه نیامدیم و مقاومت کردیم
🔹
دشمن آنچه که در جنگ به‌دست نیاورده را در مذاکره به‌دست نخواهد آورد. @Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/441679" target="_blank">📅 23:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441678">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌ ‌
🔴
عراقچی: فکر می‌کنم نتیجهٔ تفاهم برای منافع ملی ایران خوب باشد و دستاوردهای میدانی را تثبیت کند. @Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/441678" target="_blank">📅 23:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441677">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‌
🔴
عراقچی: یادداشت تفاهم کمتر از ۲ صفحه است و کلمه‌به‌کلمهٔ آن بارها بالاپایین شده و وزارت خارجه با نهایت دقت تمام موارد خواسته شده را اجرا کرده است. @Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/441677" target="_blank">📅 23:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441676">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌
🔴
عراقچی: شورای‌عالی امنیت ملی اشراف کامل بر مذاکرات دارد و در مورد بندبند آن بحث می‌کند و تصمیم نهایی را می‌گیرد. @Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/441676" target="_blank">📅 23:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441675">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌
🔴
عراقچی: در مذاکرات ۶۰ روزه چند حالت رخ می‌دهد
🔸
۱. تمدید مهلت مذاکرات در صورت خوب‌پیش‌رفتن مذاکرات.
🔸
۲. نرسیدن به توافق، به‌علت بی‌فایده‌بودن مذاکره‌.
🔹
بستگی به شرایط آن موقع تصمیم می‌گیریم که اگر نتیجه نگیریم چه خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/441675" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441674">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‌
🔴
عراقچی: در مرحلهٔ دوم مذاکرات، بحث رفع تحریم‌ها، غنی‌سازی و تعیین‌تکلیف ذخایر مواد غنی‌شده و سازوکار صندوق بازسازی ایران بحث خواهد شد
🔹
از نظر ما تنها شیوهٔ بررسی مواد غنی‌شده، رقیق‌سازی آن در داخل ایران است. @Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/441674" target="_blank">📅 23:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441673">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌
🔴
عراقچی: محاصره به‌طور کامل رفع و دارایی‌های بلوکه‌شدهٔ ما آزاد خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/441673" target="_blank">📅 23:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441672">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌
🔴
عراقچی: اگر دشمن بخواهد ادعای دریافت غرامتش را عملی کند ما برخورد خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/441672" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441671">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‌
🔴
عراقچی: طبق قوانین بین‌الملل گرفتن عوارض از تنگهٔ هرمز امکان‌پذیر نیست اما هزینهٔ خدمات دریافت خواهد شد و این در مذاکرات تثبیت می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/441671" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441670">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‌
🔴
عراقچی: شمشیر ما تا همیشه بالای سر تنگهٔ هرمز حضور خواهد داشت و هروقت لازم باشد نیروهای مسلح ایران ورود خواهند کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/441670" target="_blank">📅 23:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441669">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‌
🔴
عراقچی: به‌زودی ایران و عمان بیانیهٔ مشترکی در مورد ادارهٔ تنگهٔ هرمز منتشر خواهند کرد. @Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/441669" target="_blank">📅 23:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441668">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌
🔴
عراقچی: طبق تصمیم جدی ایران، آیندهٔ تنگهٔ هرمز و ادارهٔ آن مثل گذشته نخواهد بود‌. @Farsna</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/441668" target="_blank">📅 23:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441667">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‌
🔴
واکنش عراقچی به ادعای معاون ترامپ در مورد آزادنشدن پول‌های بلوکه‌شدهٔ ایران: بعد از نهایی‌شدن تفاهم، در عمل همه خواهند دید [چه خواهد شد] @Farsna</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/441667" target="_blank">📅 23:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441666">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌
🔴
عراقچی: ذات طرف مقابل بدعهدی است و باید انتظار اشکالات مهم در اجرا را داشته باشیم
🔹
با موجوداتی مواجه نیستیم که کاملا پایبند به تفاهم باشند و این ما هستیم که باید راه‌های بدعهدی را ببندیم. @Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/441666" target="_blank">📅 23:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441665">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌
🔴
عراقچی: اگر متن تفاهم عملی نشود، هیچ مذاکره‌ای آغاز نخواهد شد و به مرحلهٔ دوم نخواهیم رفت‌. @Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/441665" target="_blank">📅 22:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441664">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‌
🔴
عراقچی: تنگهٔ هرمز ابزار بازدارنگی ماست
🔹
ما برای دفاع از خودمان به هیچ قدرتی متکی نیستیم جز خدا. @Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/441664" target="_blank">📅 22:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441663">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‌
🔴
عراقچی: این خطای بزرگی است که برخی بگویند میدان و دیپلماسی راه‌های متفاوتی دارند؛ این دو در کنار هم هستند
🔹
دیپلماسی در کنار میدان بوده و میدان هم در کنار دیپلماسی‌ @Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/441663" target="_blank">📅 22:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441662">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‌
🔴
عراقچی: اگر دشمن بخواهد سمت جنگ برود ما آماده‌ایم
🔹
هیچ شبی نبوده که دشمن تعرضی بکند و از نیروهای مسلح ایران پاسخ نگیرد.
🔹
به‌هیچ‌وجه از منافع ملی ایران نخواهیم گذشت و تسلیم فشار و زورگویی نخواهیم شد. @Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/441662" target="_blank">📅 22:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441661">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‌
🔴
عراقچی: ترامپ هرچیز دلش می‌خواهد را از زبان دیگران توییت می‌کند
🔸
اگر قرار بود چیزهایی که آن‌ها می‌گویند را بپذیریم در گذشته می‌پذیرفتیم. @Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/441661" target="_blank">📅 22:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441660">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌
🔴
عراقچی: بحث دربارۀ رفع محاصرۀ دریایی و تنگه هرمز در این تفاهم‌نامه مطرح می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/441660" target="_blank">📅 22:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441659">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌
🔴
عراقچی: فعلا هیچ‌یک از متن‌هایی که از توافق بیرون آمده اعتبار ندارد
🔹
درخواست می‌کنم که آرامش را برقرار کنند تا بتوانیم به بهترین توافق ممکن برسیم.
🔹
هیچ توافقی نیست که یک‌طرف ۱۰۰ را برده باشد و طرف دیگر صفر‌. @Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/441659" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441658">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌
🔴
عراقچی: صراحتا باید بگویم که این توافق دشمنانی دارد که در راس آن رژیم صهیونیستی است و در تلاش است که آن را به‌هم بزند.  @Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/441658" target="_blank">📅 22:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441657">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‌
🔴
عراقچی: دشمن تعهد خواهد داد که دیگر آغازگر جنگ نباشد و از تهدید و زور استفاده نکند و دوطرف به حاکمیت یکدیگر احترام بگذارند و در امور داخلی یک‌دیگر دخالت نکنند. @Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/441657" target="_blank">📅 22:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441656">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLMlY2ee3ORP81J-bQbSWseWJBPsekIMMuS4FgpXrWaBiEoM2RBR7i72bjEKtSn-o1M1aw4AKK0dtgC4Zfe2W2jVJnplCPIirQEfAK0xlWtxDw8poZHZ3ydoa-ydYK5xF8th4mVzbQnpGYkzi3mKrdrDTX030P4a0DQsF4UQHIwQ_zj2O41GXnSmKwnfVoL_NoyoH5AEwyXWwxxBqLdTyM4t5qpr3ZECAYNTQcyZr56rG7S1j-ze4qttB1WxIjYu0W48JzN1K284azRiw2JxplZGeeV0xRHvcTySEaDF5Q9-xMAyDMNkq9BnVpI__qrPn--kBD1mEhHuXv4wEaPwgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف خطاب به ترامپ: بدون هیچ بهانه‌ای باید به تعهدات داده شده عمل شود
🔹
باید به تعهداتی که داده شده عمل شود، بدون هیچ اما و اگر و بهانه‌ای. برای برای به سرانجام رساندن توافق پیش‌رو، راه دیگری نیست؛ هر کسی درنهایت چیزی را درو می‌کند که کاشته است.
@Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/441656" target="_blank">📅 22:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441655">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‌
🔴
عراقچی: در یادداشت تفاهم، خاتمهٔ جنگ در همهٔ جبهه‌ها اعلام می‌شود علی‌الخصوص در لبنان. @Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/441655" target="_blank">📅 22:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441654">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌
🔴
عراقچی: در مذاکرات ۲ مرحله پیش‌بینی شده؛ اول یادداشت تفاهم است و بعد آغاز مذاکره.
🔹
موضوع هسته‌ای و رفع تحریم‌های ایران به مرحلهٔ دوم موکول شده و ۶۰ روز زمان مذاکره برای این موضوعات پیش‌بینی شده است. @Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/441654" target="_blank">📅 22:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441653">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌
🔴
عراقچی: نتیجهٔ تفاهم یک یادداشت ۱۴ ماده‌ای است و وقتی نهایی شد تک‌تک آن را به مردم می‌گوییم. @Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/441653" target="_blank">📅 22:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441652">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‌
🔴
عراقچی: ما پیروز میدان هستیم؛ مقامات خارجی به من می‌گویند که ایران را این‌گونه نشناخته بودند و ایرانی‌ها شگفتی آفریدند و با قدرت بیشتری از جنگ بیرون آمدند
🔹
من می‌توانم اسم ببرم که کدام مقامات این حرف‌ها را زدند. @Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/441652" target="_blank">📅 22:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441651">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌
🔴
عراقچی: وظیفهٔ دیپلماسی تثبیت دستاوردهای میدانی است؛ مذاکره‌کنندگان متکی به قدرت میدان هستند و این کاری است که ما انجام دادیم. @Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/441651" target="_blank">📅 22:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441650">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌
🔴
عراقچی: هیچ دوگانگی بین میدان و دیپلماسی وجود ندارد و هردو در یک‌راستا حرکت می‌کنند
🔹
به این ۲ رکن، رسانه و خیابان‌ هم این‌بار اضافه شد و ۴ رکن باهم در یک‌سو حرکت کردند. @Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/441650" target="_blank">📅 22:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441649">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌
🔴
عراقچی: همهٔ ما مدیون تک‌تک نیروهای مسلح هستیم
🔹
همین‌طور ما مدیون مردمی هستیم که ما را تنها نگذاشتند و هرشب در خیابان‌ها هستند. @Farsna</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/441649" target="_blank">📅 22:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441648">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
عراقچی: دشمن تصور می‌کرد که بعد از جنگ ۱۲ روزه، در جنگ ۴۰ روزه می‌تواند ایران را تسلیم کند اما با مقاومت جانانهٔ مردم و نیروهای مسلح ایران مواجه شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/441648" target="_blank">📅 22:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441647">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
عراقچی: دشمن تصور می‌کرد که بعد از جنگ ۱۲ روزه، در جنگ ۴۰ روزه می‌تواند ایران را تسلیم کند اما با مقاومت جانانهٔ مردم و نیروهای مسلح ایران مواجه شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/441647" target="_blank">📅 22:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441646">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رویترز: امارات با آزادسازی میلیاردها دلار از دارایی‌های ایران موافقت کرده
🔹
خبرگزاری انگلیسی رویترز در گزارشی نوشته: گفت‌وگوها می‌تواند به آزادسازی ده‌ها میلیارد دلار از درآمدهای نفتی بلوکه‌شده ایران در بانک‌های خارجی تحت تحریم‌های آمریکا منجر شود.
🔹
این رسانه گفته امارات با آزادسازی در مجموع ۱۰ میلیارد دلار موافقت کرده که بیش از ۳ میلیارد دلار آن تاکنون تحویل داده شده است و گفته این اقدام در ازای توقف حملات ایران به امارات انجام شده است..
🔹
رویترز می‌گوید نتوانسته تأیید کند که آیا این وجوه متعلق به خودِ امارات است، یا اینکه منشأ آن حساب‌های مسدودشده ایران در سیستم بانکی امارات یا مناطق دیگر است.
🔹
رویترز نوشته این موضوع به نفع توافق میان ایران و آمریکاست چون در این صورت ایران می‌تواند مدعی شود که پول‌هایش را دریافت کرده و آمریکا نیز می‌تواند ادعا کند پولی پرداخت نکرده.
@Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/441646" target="_blank">📅 22:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441645">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/224bc5b617.mp4?token=souIXMsYp0H_F-2kthJqtEyiCP_kED9pUFtOEpHVgvvPQFD8ZAy0OPR5XX-k8f-G5p1FTxhuYBkJxamA26IannWoQ-JQDeYGVZkyzHlouABuKvtEnrVOkmridcLW2CqOL-NqlNifcl8vkji9d1oa28e5Ipfuxhn2SSLLnIJNqaHrbp6cdc1b0XKY6-Eim0hjAZx7Or2klZX5NdAbr0_se2mveu-hBjNPK-PvD3VCwQ4cjWS73Qmga5ROBmNBomojflch2z5U8YgSTZtPsdslEskB19K11qctOUu4d4R70StaZ_JIFxiMstB8UVOvJ6unSEn53sjCC_aHNXNUxmMqwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/224bc5b617.mp4?token=souIXMsYp0H_F-2kthJqtEyiCP_kED9pUFtOEpHVgvvPQFD8ZAy0OPR5XX-k8f-G5p1FTxhuYBkJxamA26IannWoQ-JQDeYGVZkyzHlouABuKvtEnrVOkmridcLW2CqOL-NqlNifcl8vkji9d1oa28e5Ipfuxhn2SSLLnIJNqaHrbp6cdc1b0XKY6-Eim0hjAZx7Or2klZX5NdAbr0_se2mveu-hBjNPK-PvD3VCwQ4cjWS73Qmga5ROBmNBomojflch2z5U8YgSTZtPsdslEskB19K11qctOUu4d4R70StaZ_JIFxiMstB8UVOvJ6unSEn53sjCC_aHNXNUxmMqwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای ۱۳۰ هزار مفقودی در جام‌جهانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/441645" target="_blank">📅 22:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441641">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OdXLF2YxGMdllRWwtGKUEe4Gj-jCbZz9lRzjLoKJgR32z1AgCtpzwMZGfA4xilqIpOC_k4Il0CDpfghVt9fh28W3qjRqaEykn0aPJ_lIE_5_ls0gU3sC7qJKsevgO_NY2hoeoqXzF1jgbuFFncYr0Low7qj2uR2cWo7v0bcI7DiUeBz1fiizj4h3TStVGfzAUO-sPv17r6qKzoJbx_2sZyTUWqTysGE_xiBLRayVA9XKF-dAcNoFKFEoLPzz4XW0kQG2iuEq5Rgoe9Jvjbtl6z4vyOVsQzTbeO4kOJgz2jP0MDSYRpovzVBIxbHJz9FSKLRjb_0eCKH-MC4TrRaDVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7bmxZVZ-ike4rixyvdeKpYwE0KN5I6kzUd24gngtlmF95kAWJe1TfAXGXl95LKRGbEQLKiKmKs5sOlpU7FveRzHZrDuqPCwzyBwY3rsuijSGNlGOIziviJqWiUTjeiyL59DkRwKEnzGIPMkngTlvxQ9yIWYA03ycJrmxMf5t3exvKFL-CCxYTR9HPMCNtfOJm5Q7BdPoY_6Js2UypNcP1WZrZPjt0XWPiSj6102onTWrioDf07i-HxGLA01TZllIl79-i5uj12h1WJHv7nWrjyRHPHmsFg5wFO2l-xR7uLmhnqtJEeonV34gjuqJDY8cRv4N-MYvnnBpITS3Lu_iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yn7m0lm471tIAnVixSlVEv5KyW_y5mNaZVSk9ZfXDqc5HPa7XsvxIlWlgfToJ3ZffbOlzyill7QOJXFP0-Wp-RzwlcXyADZgIEJM2WyVx1JJissNgpQhJswKm2Wc85rKaJHO27vRo5CkN3mcC__p54FqbP5WDAGzZLuGZ7wEB4MQ3QKxOBZbrZlgQlP1ebvZgdmrOkZGBxruqIIDyIeqT5qZTUj8Xpd0U442VfD5HBWQsmI_BoUVbGFVBkXvHX-63Sh584pwK7q31Bt080GAjRH2MHtF_0PEtUZe_HiNA0w81zbNs8-DDrxDsqBjgAdvh15fk1oPnD5sDC8A9PatTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MooayZQOZ0kzI3WqbwxpcQDdVneJHG-Fflg7b9NoyypWCsWgUGS3dyTB9X8bVpgZKY1gzI8hqpYhS6t4T96BAIln23ncCeSjfnJumLeynMOp5DNOIewIDScI4aP6QOgVsXwmGEPTajd9Oq2oJKYTTT3aCwch8bSYTz2kxgKi2aCA2sLRNuTiErQwCFaJOse9XYK7W994dPvToQWXINqZTrChq4fMn8ipIq8KqBuwlPUfykCekOopFeaRrfm5H7mi-1MgR8jmN1OZ5pRkrExofaDkG0_7C6LYMRuetJnRrYlqsFnv1CAQLN0LZ04hw8rqOdaG0TH685YOOmrXlNdTJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نماهایی از افتتاحیۀ جام جهانی در ورزشگاه آزتک  @Sportfars</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/441641" target="_blank">📅 22:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441640">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5188cff1.mp4?token=LZP0Y7aOjzFKd9g9cZOAP_P4iUCO00lPQ_yv7-gUALQygjOvbe3pxXjDrqUrRmdHXD_4KbjfY9AGe70ik_ZKxcoIQC-fwFdTbq2TejMPAmGOy6uHXs21CteQkLOE5Za8q8vw_eJybLFEqvNW1owNbv6QzciIDjICb9PfK_rMB7SEsjWqkgBej0C1-9R32RulYfOQq7L7xKwGw8xLC73jTpPSy5BHlFgGO4jWbuJ6rq-IG6xoLfe24OdQXAHx2BKisYbeIY-5METIVNOrXTsllkJgv4AY9sD3BMc1HywgjLEi3wYeMFRetTCU6rsMQMwwjbXSbSWjiojWnu8j5jnsgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5188cff1.mp4?token=LZP0Y7aOjzFKd9g9cZOAP_P4iUCO00lPQ_yv7-gUALQygjOvbe3pxXjDrqUrRmdHXD_4KbjfY9AGe70ik_ZKxcoIQC-fwFdTbq2TejMPAmGOy6uHXs21CteQkLOE5Za8q8vw_eJybLFEqvNW1owNbv6QzciIDjICb9PfK_rMB7SEsjWqkgBej0C1-9R32RulYfOQq7L7xKwGw8xLC73jTpPSy5BHlFgGO4jWbuJ6rq-IG6xoLfe24OdQXAHx2BKisYbeIY-5METIVNOrXTsllkJgv4AY9sD3BMc1HywgjLEi3wYeMFRetTCU6rsMQMwwjbXSbSWjiojWnu8j5jnsgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیچ چیز مانع میدان‌داری ملت ایران نیست
🔹
تجمعات مردمی به شب ۱۰۴ رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/441640" target="_blank">📅 21:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441638">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎥
ای امید امیدواران، یااباصالح(ع)
🔹
نماهنگ جدید میثم مطیعی با موضوع دلتنگی برای امام زمان(ع).
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/441638" target="_blank">📅 21:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441631">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEAQ_NzfqdKPo4sovHcAbgHmFFu6Jedj-UMTYvkKWjN1n44NTwZFSFy6pdVlGFRh0tC3pkzAtbPl-smKkxMA98M0jBTLDHGxyyX-6WzQnGbmkOLh9qlTEfCpgRQNeNkzDxxxHa4ApR6umUAvrIvvKJ3Se2cD45shvJRqlhyuOiqFkfqEM4bOSCg5e14gRs5VjtuBBbh7SW6hVoKWT2O5S9c_J6PWwamP9-jHRrLQv8jhB44iLy57NJkyehv9DkLx1n62PE-xdr57GE9YlleW_1zwrdkEPw2AHaHehTafpSAh6lt_17hfiS18kEzLcmwuPngI2is1fBbtdAluIBoG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lurOCKAMxz-PwM3yLbMhQBLM1eJB3yCbK-r3LdnUYqh3YdD4vvE6myTHkDSQlzdEmL5_u-U2jAOaHuZCJyOba7IiIBSpCBSVF8DwrQAZm03pHzvERL5abVIh5ppXqMTRhv4ltL9rm6-_oae-U-VhGmcixSnDk2CUu1B0tE-HzbjPnHKPdFqi0IiHcRFO-eAqkULYZiSuSlatLVKXeq8nANHFzhRDEoYLQnz7D31pgf0f7Qb3vSDQ31k74fynZRZXKWSPpuwKrkM_2uTtWLzL1r5jrb2hrf_k141wkwR-JOsLX3X-xfBTC2RqnOT6iRVTH8s69u4khc2TI0KhqBM3aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bi8SZjhXeCMGTkmx0Dl_MCEHB1VuDuvLbyFgPQk_IXq7UdRAu9-WcCImtMJxvhNyJZ_TBRYixIHoNmr3ezAK9QlK_kC_I6WPi4I32U_J4yIxTkEZ4mr_YTGEvFLAkaeqXxvFmotSyz_EUUeAODMHSHPR5Wu_abk930hcWtYWBfnDjfuFqbAIlhqT9zFgjetUWiPEUNVytgWuJEZOfRRn9izOb1Xa-fnfZriZqSOfRnnvBi34e1Jw3vf6oA16qIjeYYzBn3ihorw_ciAlJq6Ms8mS9nqmyUDrPmRrzVc4kYr2Osbg67FlKqJSC_SxROZDzBA1lATc_xUufaVCLqbz6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XT3FERseBNLDNwPcJmb1psgEvTy0WG0rZtTiHtmUZyp3X3lU-yBzbTqydIllb7LzcJlWODErpuWonL1f466nt4uF6w8QiyF6i7Gt-V16-fuOCa9V1MK2kZ8DL0Vkc8xkh8OHqcmjRNVfHVEbkGTud98YDhdd1tMELDvSzaJKkp0NFTTqQTYstc4GRdJsi_HBQsJ-dGPOeVJAVoMUm0wqH4xlAH57Ry03q2qlKP0GP9e1Jk-h9_GWnrsASDBAp90E18kdoUtpbd59FSdCD1ulxvpuXX8Ou80S_F-T8DU_UvG5OuMDPqrgG-p6wRj3Zo-6KlUpzoq9sTOmosRM3dB6Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PEhHigTCFbVwanweZqYbEDUVFl5kJB9qHk1y0OjY_zeinekOvuUDb9eJNChHzTavct4DN0D0rxOq5Wx9F5U9W5wjdntj6vxC1Pq2dAHp-jWQMG6XSIDn9Z3kxhZGHXie8bTSfXTMhqcU7ZMVfn02x-X2gLA2w6eEeFhk0ZIQwSkZ1oc-8lXUspdjl_m0ONevjrXPXlIhsQRoPSVxXr5LXAuX-KIv9ehCs9BEhUvowg-acOt4dF0ktkJVJYoAFoaBzn7ng2vXKK6ARmC5AxPNUaYbIsVZTBmQVLUQVSbrypSPKpXjyniul9_1dgc3t9_2ewZP6vKTXQ5g0Vkld9E2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/veAwK5xDuWZOjzJ-iPUve0lDjkuaRTzWRyY5BMQYc26dT77dkgqfiCHqUK8KPO2IPCir7kZm180B4eFoNHyyvkoht-r-OGSiv7k07bnRMSwiXXTlwN0YsYdiQ85487f0d1qVOD9_mex7o6XFnk6K8Af1t8U5auzwYPhe2hCKA9ugL6VHDcBMdp2yAIs-hzLIOslRfLr-9iz4_21cdCdK8hVWh7R2HNhWzNJ_-2twtC1fxuVBe66E5tcLHHoa1jOUdw5pouSXRNp4XieR3i5Rvxt_oPCSCIsCVlBUSf9f380_vaW7vq80dG48qWwLJyn8ggwhJViTrFdEOAvC2jsTPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iVIyi4u6Mlr3xfDL1L2GPBcs-lTayx82NKdDddGVQvsu0yDihj3Y1Nz6A91I-apKOCTOrEBCt7twsEhW8tkjJYHrvrtGMibGmgP-CyijqmfZXFN-3WK4MEtkvgxhvnUNDi0XULBEbhfJW-9EkUrXHdTsBCl5-rWdD_otwAtg99ntSdI1ltg1Dgdv1_tklsw9Ff_38TSzXvXPdwVj7D8cRXqwRWPlvGiX9932tPa3zAdBUi35duc87ppMs300-_UsLo_CS1bmCUDboGjJiXS3ql868qxsV2IZnwj2-flL1Yscg9KmqX_pcUAFBFhNnQ7hoLtaBVS-qwrM37uoKSKTlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نخستین سالگرد شهدای جنگ ۱۲ روزه در خرم‌آباد
عکس:
نگار ده‌دهی
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/441631" target="_blank">📅 21:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441627">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">سی‌ان‌ان: ترامپ طرح تصاحب اورانیوم را از ترس متوقف کرد
🔹
شبکه خبری سی‌ان‌ان مدعی شده که ارتش آمریکا در اواخر ماه مه طرحی فوق‌محافظت‌شده و فوری را برای اعزام نیروهای زمینی به ایران و تصاحب فیزیکی اورانیوم غنی‌شده این کشور آماده کرده بود.
🔹
دونالد ترامپ پس از آگاهی از خطرات شدید این عملیات از جمله تلفات سنگین سربازان آمریکایی و فروپاشی اقتصادی جهان آن را متوقف کرد.
🔹
دو منبع آگاه به سی‌ان‌ان گفته‌اند که ژنرال دن کین، رئیس ستاد مشترک ارتش آمریکا در تاریخ ۱۹ ماه مه (۲۹ اردیبهشت) جلسه‌ای فوری و محرمانه را در مقر فرماندهی مرکزی آمریکا (سنتکام) در فلوریدا برگزار کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/441627" target="_blank">📅 21:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441625">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: هیچ‌کدام از گمانه‌زنی‌ها دربارۀ متن تفاهمات را نمی‌توانم تایید کنم
🔹
اینکه دربارۀ جزئیات روند دیپلماتیک نمی‌توان صحبت کرد به معنای نامحرم‌بودن مردم نیست. @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/441625" target="_blank">📅 21:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441624">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: در مورد متن تفاهم ما در مراحل جمع‌بندی در داخل هستیم
🔹
همین الان جلسهٔ نهادهای ذی‌ربط درحال برگزاری است. @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/441624" target="_blank">📅 20:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441623">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: اینکه گفته می‌شود ما خیلی به تفاهم نزدیک هستیم، حرف جدیدی نیست
🔹
مشکلی که ما در این مدت داشتیم اظهارات ضدونقیض طرف مقابل بود. @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/441623" target="_blank">📅 20:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441622">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: اینکه گفته می‌شود ما خیلی به تفاهم نزدیک هستیم، حرف جدیدی نیست
🔹
مشکلی که ما در این مدت داشتیم اظهارات ضدونقیض طرف مقابل بود.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/441622" target="_blank">📅 20:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441621">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">عراقچی: جزئیات تفاهم اسلام‌آباد در زمان مناسب اطلاع‌رسانی‌ می‌شود
🔹
تفاهم‌نامۀ اسلام‌آباد هیچگاه تا این حد به نهایی شدن نزدیک نبوده است. تا زمان تکمیل و نهایی شدن آن، رسانه‌ها باید از گمانه‌زنی درباره محتوای آن خودداری کنند.
🔹
در راستای رویکرد مسئولانه و…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/441621" target="_blank">📅 20:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441618">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۶۴.pdf</div>
  <div class="tg-doc-extra">3.6 MB</div>
</div>
<a href="https://t.me/farsna/441618" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۶۳.pdf</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/441618" target="_blank">📅 20:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441617">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
ادعای ترامپ: من هنوز فکر می‌کنم که توافق با ایران ممکن است آخر هفته یا دوشنبه امضا شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/441617" target="_blank">📅 20:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441610">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQQymxTowEdrgBj9wJ2v0CAT14YErobeJV6NgtwLxFmsbKH3aBqITZYsokycNg3DIHdZpkZPq34NoHRL-XF69VGcESv_WgJkanItt4RfKAoJy9jGzBJzPcROeNWkhIEPG9QrJEIvOQG9P3yh61JBQe3LAIzYeef1as9oIrBwjO-Y70hPWpFOzpK_0YslR5UM9ADeUw8Sh8SGL6hmLNxYLUVJucWg1USyOVLutzoKLPaZbn8TpWbOlmvOiSeBcaYydaQ8H6IvkTtfcSPcea1dHqSiGCfe2q1DwvjOiJM-hNEkhKghaHjQHIq5vRkfGFFDt5O-TUSYBXvZwf6vHch1lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNLFnJksX9plNRm8csquyTVs9UnY5BLCu34tqw_TFchhVJMYuroC7n04PzSiu-p_OgVd-2e6cMpVhMPyIT93-FesXMu0uWzR-wJ0jb0LasS9uj4_uoqwqPpZMVAN0gj37MdbqQ-hv3gMF4guipTbyzgjcTvIm5koBbML0mUcMVeFGjxCJHYwy-D4UJai3uHpwmmPf0uSJy6XSMwFDmvUYG-BfaWKdlk6uVaj4CUd4lD0NrYXlhrHRXjeYDXkDZlIVE2tKiUZ1oRKwlfqrvvLyn6bPHnX_UJl4ot2X-8ojJSHGnXDSKa9IlAGpZjonfmPpqcjS0e3p5pB-yeiLsfX6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ehy-0XUcPVJgOhL1zcRELnueZgaUULYxtrCKTsgM1SKqSVLKMPkMTD6e8PScYyTAxvTOpLdAwi98TObysIzH7PJ9ygdGUjtZHQN_6XLei1YQWYwnOEElGQ95hwAtQPbONbTo9EdT91Qjj_8Y01jd2DFgNRb0-epebr9Hu7wE5JoSxNxqhIJASTAJQdepQdHygh5qrA_78y5ZSZd9uO-6AbZvwp9RLpo6SexbtNh0FTvqINbEljI50nOCa1mERlDjdQl_mkZEIxN7eiqbF2rWmqbkMOkDSeEzWek1dy2eXEM4Pa5HtWDBAqoT_Us2h1GyyFW9lTwZhuB3-mxp-xQzuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGloCvhtDRe_cVRK8yPLiYeDB9HVD4t8Lb42R_Ucvo5ExRMbnqxq8PWdgA-2cCsIJxh0bT6JRBx-INLftgS1mQZtcrtyRNlXEierg3RB4LNDCGalFKRhVS4IrgaG0IrlblVEtv5-6dQ9WnAgEYqQQaCl2ecjn6tbpXTTMVIcCP9T7ZQSXsJH1hvGJmX5E-etjhSci1bA_YjVA81IVaLRus-za2QJ3qkWL89-f0m5ap7Od0_Gr3K3b2_ByvbzUn8RZolrLYBSdYbDtscAbrzL37RdkOHrfWNv_Fp1y9KD2WqoQKTRfVtZ75nyUAp-hSWPmkvc_o4rEq-GeOw_xyrDog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BmWhpxR0YNAWjhfyWgOC5Ayi03adIABeK1y2-sfOjGkI9wxuXXdLsD9e0PHMS5WZ0LCtmwAgZ1CCoUcoURZfohDCdbLlSRN4LWR8Sa1Y9Gaao8Tev6RooNHNI5X9ezeEm9sJhCN_vGV4ufR8GBAh8ZyWQTMqh3mc_4m_tri27j3MN9Fylvv2atGj7c6yeuAPyH9HMV-js-5cWLR_gh8fi32KO76PCaVHrZhIqD86-UQ7yeUtxZICP8pYasyzp_vV-nAAhKZjKmPan2d4exiBMZ8l-_b-VQa9iLVs5j05ROPJj_LvpUCB1spX-GObIA8u1LQ2tuWhaUV6N3LabiTcJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3ZwLpL1zfnV6lwDQXpkt7EyYJrWbr8cReneCJs3-eygWfzNt2HGkv-IEU5_HFyRVfx_7KdAdUXZ9-2u4KNznl5sG5ZZ7sB-KaZtjmqiw0SKz1RihwvngLzAN8xaI9y4_u2BAUBB0Xxe2fsZg6xM4P4eEGf4wP5sikh-IidYlmVaD_TbEnMT8OLNnzSFhbt2_BtAQCxcTX4S9HKf-zU-NfLrwZP7jcAjhNhN_pNd3kjSMhPIrBZA-q2KVkRE8pqtN6_fieuZHggYBRbNwH0niW06Uw-WoTPp4vTNE0N5Z7IHNBskIcsj_Y_6JDK6p5RiDxVvnDu2sgNXI1UbwYBSKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oez9zW46Xy3prktU9MxiZpCI54y9KGmip3PewJPGhXQ2ZX1cDfDZqMLTr5oyeK-eRvLDnSSIpjN5Vf8G-5sEAOXbeP_i-iChoEFropComA2GxnUyKFDKCp1vxe4yZoysIecw96eJXTny61MtFOupjdqz1BJsdt2ATWgXNuxXvyZAhvrce-Lh9gid2VcVsbqMPJhG1VngSOpBxWtOP9gp7aaU6_NE6bAT4Bnj1C_eVYEaL-mUcNxbYFbJB57yNw4H1sAp48SqQoJ-q-35og9VEps0k4VqYTY0GTqB8RCiORsDDdL9V1aN_93PYvgVgxzO7VBP_460TtG4l1blaM_JrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشنواره باستانی نونهالان در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/441610" target="_blank">📅 20:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441609">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec3df4da4.mp4?token=OrmNs-cQqGeojzec9lF_oyIGe1Qpvu1ptRxHjQzy403fKAJ4YXd5yuVW1cTrd4p7pNK-dr0RHEMrhvEfzsYUV3t4iRO1xjEtFeY1LbpcsCAcC0cPh64m_11IPriIhZ9b2rW1qG53VRQtSGo3QwbVmqa76EtPnXNkbOiv88SBCXDtuUAAb-dlEJFUAQEBmpdZhTn53edbl5BYfIjKkU16wG9VbeG0VqPwg1-7oJL4jIYwdpNNIWU55JJ2DUFcDMNqj32DD3efoJdrfqKNuJsXQCuk4peEwWrLYa1nTpv8lWe2a52xmjjRDM8e0eQitb6GtrI67enalLR9v9cKvvOofg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec3df4da4.mp4?token=OrmNs-cQqGeojzec9lF_oyIGe1Qpvu1ptRxHjQzy403fKAJ4YXd5yuVW1cTrd4p7pNK-dr0RHEMrhvEfzsYUV3t4iRO1xjEtFeY1LbpcsCAcC0cPh64m_11IPriIhZ9b2rW1qG53VRQtSGo3QwbVmqa76EtPnXNkbOiv88SBCXDtuUAAb-dlEJFUAQEBmpdZhTn53edbl5BYfIjKkU16wG9VbeG0VqPwg1-7oJL4jIYwdpNNIWU55JJ2DUFcDMNqj32DD3efoJdrfqKNuJsXQCuk4peEwWrLYa1nTpv8lWe2a52xmjjRDM8e0eQitb6GtrI67enalLR9v9cKvvOofg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشی از مراسم قرعه‌کشی پیراهن تیم ملی فوتبال ایران با حضور هواداران در باغ کتاب
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/441609" target="_blank">📅 20:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441608">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laDs83mshOhvMSLOZzNQy2OPI6tA2FBmMQpMqz35_66w7_w5JK7vVLSOP7cLo5plpgbF_WIBzQlXCh1AAfXx-vNEeMU_DEfcGoItNNKEuXvGkLsV9LMySWdYIpS1xIYtuQDpe5Ye3KAhbuw_sOijfGnuYI-R9iZih44VkMi-PRvb7w8DZ-ocKv8Y1bpfWsVaIS4qSFJHa8k8HdiJ_vcZTiuEbesz1FHnh4QEFoUyj6YeDVivbgSVAR3swepHpydKesDW1q8RuE1gVfrwU2P13wdnDRRLRc_0I54VV-Smi-Jm2quocEVEKxWzl_HOQTr6UKkVVjx26NlGBGsyumNvOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
تجربه یک جام جهانی مهیج در نئوبانک فرارفاه
🔹️
اگر در "فرارفاه" (
https://www.refah-bank.ir/fararefah
) دارای حساب هستید و یا افتتاح حساب در این نئوبانک، با شرکت در طرح "فرالیگ" بانک رفاه کارگران همزمان با برگزاری مسابقات فوتبال جام جهانی ٢٠٢٦، از جوایز ارزنده بهره‌مند شوید.
🔹️
مشتریان با مراجعه به نئوبانک فرا رفاه و انتخاب بخش فرا لیگ با اعلام نتیجه بازی پیش از شروع آن مشمول امتیاز می‌گردند.
🔹️
در پایان هر روز از برگزاری مسابقات به مناسبت شصت‌وششمین سال تاسیس بانک رفاه کارگران، ۶۶ نفر براساس فرایند قرعه‌کشی و با لحاظ مجموع امتیازات کسب شده، مشمول جوایزی تا سقف ۲۰۰ میلیون ریال می‌شوند.
🔹️
پس از اتمام تمامی مسابقات جام جهانی، ۳ نفر دارای بالاترین امتیاز مشمول جوایز به ترتیب ۲۰۰، ۱۰۰ و ۵۰ میلیون تومانی می‌شوند.
🔹️
مجموع کل امتیازات هر فرد و همچنین میزان امتیاز سه نفر اول در جدول امتیازات بخش فرالیگ از نئوبانک فرارفاه قابل مشاهده است.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/441608" target="_blank">📅 20:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441607">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/441607" target="_blank">📅 20:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441606">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vt6GphpSTQfjkUBr2OpcLge3yvhk49kQktbM5C2OjSmD6jbbiUISJsIRApUgIqFMkGxJJfhk_8QaH-quTXxDj8dN_TEm9mpWfrZyzPWNZUMrUm6Wwh0r9tX9Q-WwvNn0NF8oj6O9xO3nS3VPZlBD0PwOlSHR8yhnXI4UimD8rJ7SEtNibPsPYRr0Ev3kxxpvlfEm1gspaiJiNtSHE1CO47J46mRGp_G-iK5h5SuxAZmt7_gVIZ3_1GnTYyXz5mpMmiJ8DYQfl_4XdhISAqsmdL4MooVCB3FUbSaZHgwUFEDUU5YyXHuMqNlVubYpjtqRJoYfF6VQGPqVsTUnFkjH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نخست‌وزیر پاکستان: با ایران و آمریکا برای نهایی‌کردن توافق همکاری می‌کنیم
🔹
می‌توانیم تایید کنیم که یک متن مورد توافق میان ایران و آمریکا حاصل شده است.
🔹
ما از تلاش‌های برخی برای انتشار اطلاعات نادرست برای خراب‌کردن توافق صلح آگاه هستیم.
🔹
پاکستان اکنون با ۲ طرف برای نهایی کردن مراحل بعدی همکاری می‌کند؛ صلح هیچ‌گاه به این اندازه نزدیک نبوده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/441606" target="_blank">📅 19:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441604">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSTII2Cgxv7Z03nOWT2t5YGpaQ4bbwARxNug4Q_GnOcc84N1Izg4Vflc3H_VkQqgX71Zb8shUKOLptAAGIxiBLTuuuyERGaVyX5uhBhBYMPGB_Asnnrk-DBrkDRoLWKG9V6DKSBi04Mfgq5FDehplGtWsi4txsDvvWnBPjlqAcK_HEhPFlj6qadZv0rHVmVazcgzMF88YmXs5NbiGryn2E7Q3wrfcaUJHVGf1F0f2I7ygXvmdJSP6OpIfhnUNtjh3mP689_9E8XpY1y4nvGU6RZSf2rU0SJXYpEeLXNmjYNDPLDVaG8u6_Js5FS7becB_yQVJI2z96UJxKHL2HqsVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e359b1457e.mp4?token=Sv3GzrRmhrV0teBwWpGpIBj2Ago8tP1eqU3s2vnd-d6njhfRDUtruJqexXqfgm7T7hlmKFhLX-VG-tWvbIYA_4JItqSZPv9xOxGyfNdI-ihr7fZTKBSn2kkR3MTamfxJDPK5TpfPGuHg8UB11yrb3hNOAlxiy77IXcJYdHeYTEv9rCcn3BaKzx0rEPa1Yd6WOS8dG01wGWqWiv9VzasENdlQ5Lep0sM1gQPz6CltRKuAaBFD1PRRtApZOdVnGKGO9ldzL4RimMOQIsNwHUpM-QMhf7yiKhz79d55-nr8cwwqP0k_cTd7kNWwaQEveJ6bwsBUxZmo7u0KYsdfMb82rbKzhhjZ8pNUz41izC-HsdL4FdU0kSVjzRskqKb4Bb2mjfgVz60zkn6Q6MWxwHOw59zzn4Ch78-IDpC1JOdXHJsIC0fmeH23Dovzg_hKV5QiYdX4F4sZRTlTC7dImSI4HqjrUbOfp253n7dpt2Gb89mZV1pU4TmG5H3lyX3BssKXtLFODod5cPDetwjt0QezSMaZxYiieWJxvFcH4Cw_60cH7GTd5aMlKOVGOghMxLQEZ7k8_Dq3p2QwsgvnXSpUqXXmSgHW_Nhqk7XLVdQsIMK1GqpzXvubtNh2JNgNvem0bg9uT_7DHRvSobgskUkG1jduwJKjudSIEGd8MYq04W4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e359b1457e.mp4?token=Sv3GzrRmhrV0teBwWpGpIBj2Ago8tP1eqU3s2vnd-d6njhfRDUtruJqexXqfgm7T7hlmKFhLX-VG-tWvbIYA_4JItqSZPv9xOxGyfNdI-ihr7fZTKBSn2kkR3MTamfxJDPK5TpfPGuHg8UB11yrb3hNOAlxiy77IXcJYdHeYTEv9rCcn3BaKzx0rEPa1Yd6WOS8dG01wGWqWiv9VzasENdlQ5Lep0sM1gQPz6CltRKuAaBFD1PRRtApZOdVnGKGO9ldzL4RimMOQIsNwHUpM-QMhf7yiKhz79d55-nr8cwwqP0k_cTd7kNWwaQEveJ6bwsBUxZmo7u0KYsdfMb82rbKzhhjZ8pNUz41izC-HsdL4FdU0kSVjzRskqKb4Bb2mjfgVz60zkn6Q6MWxwHOw59zzn4Ch78-IDpC1JOdXHJsIC0fmeH23Dovzg_hKV5QiYdX4F4sZRTlTC7dImSI4HqjrUbOfp253n7dpt2Gb89mZV1pU4TmG5H3lyX3BssKXtLFODod5cPDetwjt0QezSMaZxYiieWJxvFcH4Cw_60cH7GTd5aMlKOVGOghMxLQEZ7k8_Dq3p2QwsgvnXSpUqXXmSgHW_Nhqk7XLVdQsIMK1GqpzXvubtNh2JNgNvem0bg9uT_7DHRvSobgskUkG1jduwJKjudSIEGd8MYq04W4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عروسک‌های جام‌جهانی به شکار قاچاقچی رفتند
🔹
پلیس پرو در عملیاتی عجیب، هم‌زمان با افتتاحیۀ جام جهانی یک متهم به قاچاق مواد مخدر که هفته ها تحت‌تعقیب بود را با استفاده از لباس‌های عروسک های جام جهانی بازداشت کرد.
🔹
در این عملیات چند مأمور با پوشیدن لباس۳ عروسک رسمی جام جهانی ۲۰۲۶، به محل حضور مظنون که از طرفداران پروپاقرص فوتبال بود، نزدیک شدند.
🔹
به گفته پلیس، هدف این بود که ماموران با این ترفند بدون جلب‌توجه و ایجاد حساسیت، فاصله خود را با متهم کم کرده و او را دستگیر کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441604" target="_blank">📅 19:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441597">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LjU0eU0mRfuIDsNfdK8D5L0-ioIOcSjYXk-jcgrRO-OSA7XLAowa6RHTl39gftZ6ggiSLQrb_gVjYX-X2hRHHcKJrVQnifq_47BN5sgD70SVAYhlBicK0GGPUBf11OMRmwodNPtXVvtAMweHxE4fPxcNKZZ3gwMk_ZBwQy7JO-vuhG7L4MHfj3A7fvr_zuckSqWAWXs_A2BF7TXTAGBCgmYXoOgnH_5WKWCGmxoAOxVv_eVzf0TEDmFvYHXdWlhvtH1-oHe53w5p5B3AcMMBaQwLlhiGtV5sal1b_DM5okqLxMHsj9qWFYmiFG4mWxXGYwm-2sS6hwJdFSopUOIhhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfvH0DoEfYUyqN41-KyjYB_f2gfWci9DAueY1tnRWJNAbEw2Itglb4PPaLsVO9W4QOyN2DwJ08MVKWVHR6B2PCnFhaLkbZQnBjd6y-0I7tWbTmCsfk53PuMexYkGK5LVxgP1tmG6vH659Reeio3KTXNPiE8_SPTAKjY8bAslXcOmMuTRaX0ErcKUVEIRBeNcYQojKRx2QEjfiifp5YqYG0q7FFghE43ZtVu_fS9no2s1uvM5uBeAf7NGYbVc20plO91tyt6i9cVxy_PbStxp44_JExmGi2jDzPxCX6gjGSqkS1-t0QFTaTJjJmWcPMdkVKKfnQyceQb9anffO6suDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZweCJYszCOQZe_ixyZkzjp7AeO7TVdNuTqiYnlhl1rKC6XHuVVurIzifMz-MSYnGS9mhthNO4Q8ah-K4LEVLzy80GEGvQzqQMvN5Xle4L2MTRrNbEmuaw17I-eFzdhGx9xDwX9sZ3Ervooc-Xqo1IVSgd9l0I_Ltc4YFMWy2eJwvgf3pPB27PdJNfGGeZNJD8iYyc_9dcpCI-Xc8pqF9nLPXLKMLryr1RWgaTBC2AwJTdTW11mbP7PdXIjDx4gE-UE5eJvD2-doFCZpBjR5AoC-E8o3uZb69RMNYuWG5JtF8Me_8WcRaQDNws2qya7Jj7Yw6NiYQdhchvK3_sy5c0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eX83B_osu_IvBTJmCRb1fZGP6khwSb2dQ31_ZtQxMyCN3rRuWeqMuwQuEU1gj_k6Zs-DytaD5uJJyYIgY4pB53iZrupw3W9qb5ZnpxC-AUxHdODHSw8nw6HrOGjbSzgShJa-pxBRV8dZ9IrSfZzYfYXH6wAE4mqkGPLh3DYu-sRk1rx3gBeEYTw4K7YhMKWNmA7h4uA8aNlL0w99lGNcVrmq1rj2ARaUEcGWXhS6XujpQs-y-SbchVtXPUZtkIFH-7LWNcDitJtfov64mgavCO5fA2MnFa2B-bTyxHOZtQyhCIjc7bOkautsm2Tpfx7WT-05jokcGQkuYg8b92pkFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mramMaWoO4bozOA-WSavAUZ_tewL3QWIZjmmOHrVzrxaxeheoNaxQuJvH6Iy82zwJCJBOY5qFhTO7OOLoqRkx8UKDwA4uZyqGSlBTM4ZqWswfMVNz9fKsaJEtX9cpFUi71vGhJs3CX1GKJtc9SZTygA9fZXRT_DpA-NNg5rjy_kdiGKXkmBTD5JGYuE_TIYkF5WqhY5XyPP_RvTncCoP0XD7YRFbrLxrbVT8cN5FliQxh9S9MsD155NQXu2ZMIDCj3MwC8Px00rqlXkxUDqUess4bx482oSoja-POdGM723mX6dkV4wzWhjm8kHGhdiTRj_U0mu9g5Uywin9yIdSNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAzy8-ardacTwlb5sSVd_nT0Avd8xdfTXnVSpct6zuYJjcx_Snva0CDTvXUtocsPFgv8q_4ZEf5kZbUPFd-qpPcjNMA0mS_40YzdY2WdJs02mHCLZ5855Kh1y6cXm7FcNFbf5fDENLxRz9Z5oHYNgGxE-N2BJBBRShpqyiJjZxJmuzCB1vZDPDbegiiaZhGROOhRxXYVS2jMHqKvfPlLBUkc-orMcXOfI_sYU2EA5zQXEgkIoW1ahRH3OHAx02VKXf7VUtbe_LXzQcpfiIxU4bkUkEzGdHzsb16iR8VWh9e1kga_WfFIGI_jpDbV_jMjOgtDDs_oHGjjRsDPFqIrhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iij3koWvJxlzkyZO7X3tPXtzenKkPK69IQfarfbgfTcbP4YW2C4H2Jl9iGPJMlWewnM5giMjjoXZRZBMLxOtd6FOZWMQ7AiT0SD1yEBkgHVSBXv2ktgTpHPtjxB67tDH3WiGq3QBvGxO_KRysS8RW5yIFvbaqLllGXmVNMgMpzJMgF5jsCae6kzPSypQbLietJQlxA-odfrc093CJpmMdlgrjmViyE_oTHuSbuCP8eb_YLLd70JXduKuqZMTqOlIpr7SySL4IlPtKUY66qGZxnjqA3xcVA-ouKf4A3fperofRgWlD5G9_J4nFkQoE1_BTQ8NQ0mrkeiEERIIVBsh9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اولین دوره مسابقات فیجیتال
🔹
اولین دوره مسابقات فیجیتال جام خلیج فارس با حضور هنرمندان و ورزشکاران امروز برگزار شد.
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/441597" target="_blank">📅 19:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441596">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">۲ دانشجوی دانشگاه تهران به علت آتش‌زدن پرچم ایران اخراج شدند
🔹
شورای انضباطی بدوی دانشگاه تهران، ۲ دانشجوی متخلف را به دلیل تخلفات انضباطی از جمله ایجاد آشوب و اخلال در روند آموزشی در اسفندماه ۱۴۰۴، به اخراج محکوم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/441596" target="_blank">📅 19:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441594">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmoK-x3nX-oOSaBF9ii8TWy_9BjxuqT5di9wQxosgdd6WXBK_lC4x3LE8vf_4h84Jb6SKOMczNAOSwazcRAlPKQIxW4Xz7CfhFF9ndjmuEQxt_GkUr_XVbQo4tXZ20qxSlsr-IGpZEzIofc6jHPwy5XLuVrZm9ZjN5U6KSgwol3kcSp967Etczw-CPWDlXe5bnZ37NBAjQoY2SMuce5v21lDCbFMM1C_aBfKtEiI1QAMxhQy8t9Uphth4H8ISAgDpXN9-8GPPWqZPWxGUXBefniniY9hQjOkRYJktzm_wQU_i8YvdXP7-Iu7fIXzUhpzJHEQwiaAJNIGOb_yOItoww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: جزئیات تفاهم اسلام‌آباد در زمان مناسب اطلاع‌رسانی‌ می‌شود
🔹
تفاهم‌نامۀ اسلام‌آباد هیچگاه تا این حد به نهایی شدن نزدیک نبوده است. تا زمان تکمیل و نهایی شدن آن، رسانه‌ها باید از گمانه‌زنی درباره محتوای آن خودداری کنند.
🔹
در راستای رویکرد مسئولانه و شفاف ما، تمامی جزئیات در زمان مقتضی با عموم مردم به اشتراک گذاشته خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/441594" target="_blank">📅 18:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441593">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🎥
نماهنگ «ما که نمردیم» با صدای مهدی رسولی به مناسبت نزدیک‌شدن به ماه محرم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/441593" target="_blank">📅 18:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441591">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pa4UtEdVowdPTnDZ9YbWZuVseU-5xHah3_VF4BbTY5wzAmR9l8dhZXyftBTIA1WPC97XFxNkduxYSmTJVjGgy8sXTh6CnjxFQdrCb2rf_0_Vi3sBOHZ-orfJNN4Fnee0jf7vtkphE4pfiqgFZNBDOo5w7KKJ01RN0iUm6RNOw7N7o_5iT6FSpcxiBMRP4umD1l-Wp6YRSjaBQc1VxFJBX_qw29icSuW9Kotd5IK49TNleun5-RE7opy6PBp_Pc0eSn8vg6qNNwUwvCfDinXNHLmXXnni14kC7xpsxLYQUJzxZfJLqGJb20GyZyP45IR4_Ccgj01PHOXyl7wD_NobFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/omRUkcuN3R6OuaMhurrrJQva4NhFFMZWV0II6X28IoaGxVA1oRfjTLLjF8Ls6uGFNfd5T68XhU2UcaZMvpOZw5k9250sehJImTu4-AqDPS0otDhZzb_KWsQVeyWe0ax4l-lvlchi9ypA-UoBBxHQKZD_n5zLsLniqheeCLCgVCdpoxX0vTCifNu_bWoQlGOWvcO2jLNqbxPRQPTXNA-b0GoE1s7dEqxOolxO4Pk3jcZhyBN5BQ4SVW-NX8zxTqvebEOTQv43FY7fuf9arIIdNlkvIexI9EinpOr-iMdYipHKWLRN4xw151uBATdW6c11KT5-g0los4bPSQ3TcLc1rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برنامۀ امتحانات نهایی تیر و مرداد اعلام شد
🔹
وزارت آموزش‌وپروش زمان‌بندی آزمون‌های نهایی پایه‌های یازدهم و دوازدهم را منتشر کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/441591" target="_blank">📅 18:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441590">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glt6BzOdyqnpxH653__avpOgZzxRddFr-StgusmeCdb9dgptuK_XRiVhDwD1cUgkpQj_7dLFYcYjkuc3dDu_vrvp2NmwCi5frTxwihvfBAHC8OBJLr55oZAz03Yl4RHfqkPZZinyk8jSfFF2MBj-tGLf7rWdk6a3yRAiVCX5CtSzCXtBiHbf-9TAlXzmgTaU0ErMwk3HmGhekiDW4VuLWUHKDRCN66a5lGvrsaSbVY0HDcF-34ZWTYPcxU88wo8BFU-FV0IGSJd1YO_Zq7PvDEN6UcH5h89IhuxcOf4MHhgSOTS10AClqJu-EnKCAWgqvE4EkeN_dT8YK8k_fS1IvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ اسرائیل: از مناطق امنیتی در لبنان، سوریه و غزه عقب‌نشینی نمی‌کنیم
🔹
اسرائیل باید توانایی عمل مستقل خود را تضمین کند تا از دستیابی ایران به سلاح‌های هسته‌ای جلوگیری شود.
🔹
نتانیاهو دستوراتی به ارتش صادر کرد تا برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای آماده شود.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/441590" target="_blank">📅 18:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441589">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎥
غبارروبی از مزار محتشم کاشانی در آستانۀ آغاز ماه محرم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/441589" target="_blank">📅 17:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441588">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfjWqHJBDE_41LvmhwsVlKqRHIPLx08X_wrtaj33CSs34QB5YRwMYKeaZglgR_lx2Qiogp9RARL6IE1yUygjbPScmDOZ_5jsqZJYRS0EmQmokyNBDwLiqJthUygXwWz6l6Cw-P8iD1pVY_TiRJrD81aY0_l_bWZxfIeOxETg2pHg2RX4jxSi9kFiR5ANjohU33wvxgfjeVXJRmVKvvMXcMJuqo63ovFNl2U9Czn41Ur22IQnq5I7W6Iw1w4UZA5BYHj5jFrsBpE8imbiPQCP8DGjVu4uyvPB3a2vATkVcZgpby_Ivz32MR-K-H101O8l7zULAZwPC_CLtwFXdYv4LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اظهارات ضدایرانی جدید ترامپ
🔹
دونالد ترامپ رئیس جمهور آمریکا در پستی در حساب خود در تروث سوشال ادعا کرد، «شرایطی که ایران به رسانه‌های جعلی (Fake News) درز داده است، هیچ ربطی به شرایطی که به صورت مکتوب بر سر آن‌ها توافق شده بود، ندارد. آنچه آن‌ها گفته‌اند، از جمله اظهارات ضعیف و رقت‌انگیزشان درباره داشتن یک توافق، هیچ نسبتی با حقیقت ندارد.
🔹
وی با توهین به مذاکره کنندگان ایران گفت، با آن‌ها چیزی به نام معامله با حسن نیت وجود ندارد. شگفت‌انگیز است! همچنین، حمله پهپادی دیشب آن‌ها که کاملاً دفع شد، علیه کشتی‌های هندی که در حال خروج از تنگه هرمز بودند، کاملاً غیرقابل قبول است. بهتر است خودشان را جمع و جور کنند. آن هم سریع!
🔸
برخی رسانه‌های ایرانی اخیر مفادی را از تفاهم نامه احتمالی میان ایران و آمریکا منتشر کرده‌اند؛ مفادی که منابع رسمی آن را تایید نکرده‌اند.
🔹
اظهارات ترامپ درباره حمله پهپادی ایران به کشتی هندی درحالیست که ارتش این کشور روزهای سه شنبه و چهارشنبه با حمله به دو کشتی تجاری دست کم سه شهروند هندی را کشت. موضوعی که باعث اعتراض شدید دولت دهلی نو و احضار کاردار آمریکا در هند نیز شد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/441588" target="_blank">📅 17:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441581">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vOc_02-CtveaQxjYz_Ga-jKHaocTA3xIWUP78v5D85qHcaKe5mvoQnUolsxDOfWHCB0ss4RvsGkOtEkNllISoZR-GPlIoDxV_3app4CH_33TE6Z4Lplu0WC-Xh5TR6keMbWPCEj13VSk9_vlC4ZWMnSkWNSKtu3Nr40m5Nubfq57p3RodJKWYvpdM5TlTzLrzBj6N_I2E6wPGFq5Z698aFzrxOE-kHYE-PzKy4KTpXJhPYjkb3RCm5NaAI52MiUD7mkNZorO937boDa4WHmcrQ1bLtjsqdouygvI1jzJkvQ6sHQSA4PgK6_agFz6kkHXuipOKlh1w2ZZF9lSZAv1pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QWfWAjOs6vxbmZqnPXPgZjkGA-zqOsqbZDUzL3hilOM5MukYb_A9yRBZ9JyMYcxjeforLVFL-gFrXKgBDL_yScW_A-iAbsMLknpFqhZTg4CHNdWWHOknugHW3ekzGVMpMGd7CK2gdqYDhUfgBkfejiie8esRNXP3-0Hdv9XnudgUDYhYWuYomU2PNcRO3rZq11bGPPXCKqh2HR6v-tAN2mzH7dP2x6jaN5K5OyWhVx7Oa5ZvR4qR756ojAPF25C--i2GonYeyxtww0ivGWzfm-Su-A2EA021yS42G92M3TftHFnNVIwtY9lbNLzhKMrU4JVt_aEpGWkrh8gPbeY9xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XZqaMYmamgQfkLUJwL-09DHORjADV4l7mUYQnC_C4EcXBgCyYVGxYJx9_kc8qDfVIHfxtJhp6nHslMz_czc08jy6McYKXTAv8ErEZ9dqSTRipwaeSQV_OOIdrDDRaE7vZkrkqAzPh-uwxcsZ2ztMK_LDxRw0EFF0G7ILlpwbYGCmO8I6yp1ppPJEO2z6YJnIj8QV17Ujp2HpDDYUu87xITVSYGdj5UKCzZ_VVjibtYJnDvAwiWK0vgdxleIz0xmIo0qwz-q82wfjmJrl4_DB2QOwe6BnmNSgEMhz5uHcLOhQVr3oXIUJyeNHC-DFV42snYEtd9j0xjqW2aIgCtRuxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOufgziscK3rzA25FX3wPYlLOEEpZ5rMBQSRNXq5zkaS6r2mzjGtZ2kCjIjeBSVHF4SHvjANalpRU6lXXX7bzIgKC2zKbiFENbq33EnrS5C9DXyh3-LEFl0R5lnR2f8OIBeaN4nWp4JCkBkEl8kO_jrI-autPkN_wf8ylz__Rf-snbUNrHV8LyQ5OkqGrt8_XUNpHNObcHbDJOFIAFvwhbOed4PbJ_WiZ8G3yNXIWv-Rm314_4fNZ29pGbFsOQjE46rxdVOLzlMVdPUnmsIm35JGq-CglEJBBtV7Z8Agc74gauYGFkPon6Ka40xB45TF4BnLmyS3-QltFfZ34bP-og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dnt2QkfxV6QQHEuG_yIISP7PbinMbMOh_L4UT7VfXr7_tn4E3zYheZGot_ajaoAA-0xb0XhHO-s6LY9Aq6JwaMomCgDa1Lh02bt5DBxVXX38VLlUTtxGmnDBPCKGa19bsPLPl6fvsZVAzacsS1w05DCauhol2vt3-4dnDq_Qarmalfx7zoQ0S0cu3ZGZ4jJkTWu6CWTyfWufgsqdl7cBUIehOakDWIzrDHkHwJTBBfyEiwQnElnfRFwG6h8UsCLpNgaFJyQGT2XhgX9G-o4akaArG-S4q1PGcLdlXzKzHmcZrcQyHmKJe23-kr0NexgzYG3eIsLThR0wnaEiSH5kRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDWz7kPhsp9MFEgmM6h0ptCnQIE5JBrychVNmurTjaRWHY4YmgXn4zqWGgt_YhiDggS_aJjh9lhhNQqKBxPCF9DSPYsuriCvx77seOtFD3snn7wkM9UktXbsYo8hdivSXKCke2OYNsr5R4ydTaK7Ab-lcQK5JURR-qZtQExHsvMFQ1l79I6OMXVwdwfNIDd4mwW7YJlwEbKkC-rWTsF8493bZUSDeLD1MITZjvO9qaX6qSZZssq93TO6MUEdHO10qHWzSSHWaLiCrnqg3Xs4Wqz5ccqEVpM2fJXNTWue_78keugxqGsKyqwT5gS09mXksxXldrrfRzQA7ZXwDE57VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkQXc4uuc7GMmxvjUP78XPoWYgGaCAd1qOXDh3S1H_C2xhCO9l6hFTAIeQxu8DWu1CQBjpgR16LnwiEepRQtUSmjG8kuN_yi4CugleWMWNLxH_wmwNmgH_4mavkKwiyb5-86Z7u4IT0z7uEY_nIZISKGIT8iFlyV31MCpG0cAu4Y3wInzmmQ8CQVyWO9WVy59bQSiCVqhaHZ4HI1iqO7RA_lkn4YcCowEuMrTUy86Tu7hmL1VvAohkxewsuqoT2OVRJrwXDdoxKHdEa8uj88QnLrTQGNE8DYPg-iHnBHWPPjW4DhrxXncoelVvfU9Q85rAtNCS5rXTsEEHV1NBC7Sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
مراسم سالگرد شهید سپهبد محمد باقری و همسر و دختر شهیدش
🔸
پنجشنبه ۲۱ خرداد، ساعت ۱۷ الی ۱۸:۳۰
🔸
مسجد امام صادق (ع) واقع در میدان فلسطین @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/441581" target="_blank">📅 17:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441580">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f02e07d06.mp4?token=terazM1hpzqUTcWwGyAKorROn7YCJyhIhXh93fqqgUscnw7Bp_w4CMB_5T_uz1gg_5pAdJRvysIJoLLH2Fj8AbgMueoC5iibsNf9TCqQJCdfGethXAEG9-bwoUS5k8EwDmmZxqa_4wUw5uo7k5Z9aFkM7NqEOlq2xZCNjqB9ZBpkw7yjgCqXban_eoAqyohKsYSkvWy2514hFOCqltqZBBDs0AcL3tIlsRvUVDNcBThShXbN_0i2Y_iytqhzuAwMflJMY1EhyGokmPjD55peLU5msAjGx2LnF3-F73QlhTKIXpwriK3ptRaWbmbihj_LUe0ZcoLaRt29wG6iTfBUx4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f02e07d06.mp4?token=terazM1hpzqUTcWwGyAKorROn7YCJyhIhXh93fqqgUscnw7Bp_w4CMB_5T_uz1gg_5pAdJRvysIJoLLH2Fj8AbgMueoC5iibsNf9TCqQJCdfGethXAEG9-bwoUS5k8EwDmmZxqa_4wUw5uo7k5Z9aFkM7NqEOlq2xZCNjqB9ZBpkw7yjgCqXban_eoAqyohKsYSkvWy2514hFOCqltqZBBDs0AcL3tIlsRvUVDNcBThShXbN_0i2Y_iytqhzuAwMflJMY1EhyGokmPjD55peLU5msAjGx2LnF3-F73QlhTKIXpwriK3ptRaWbmbihj_LUe0ZcoLaRt29wG6iTfBUx4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی گستردۀ انبار تجهیزات پزشکی در کالیفرنیا
🔹
آتش‌سوزی گسترده یک انبار بزرگ تجهیزات پزشکی در شمال کالیفرنیای آمریکا را به‌طور کامل در بر گرفت و ستون‌های عظیم دود را به آسمان فرستاد.
🔹
مقامات محلی اعلام کردند به‌دلیل وزش باد و خطر انتقال شعله‌ها به مناطق اطراف، بخش وسیعی از محدودۀ صنعتی تخلیه شده است.
🔹
علت وقوع حادثه همچنان مشخص نشده و تحقیقات برای تعیین منشأ آتش‌سوزی ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/441580" target="_blank">📅 16:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441579">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2XNwSiU9R18QNNCvKoNsfMijljo5iiFuazSyYFwv7RnGMStmTGvQcWoj-j-hPjxJkCZkkg8zc2fxamzwIUwv2bLfVlAP1j2OXxs9JavkofJwu7AOsbKFiDBwr86ETtzc-Hho0u32GYOoCgiza7wnoY1YSu8cTuA2KpO0_SJd4pczck00KMWhXAiTrH1tRGbr23RYBDOYX7WE6PHWrNbwXGZVwvEU5LvGEZTfIaSe2eDNVcan9SimJGTKKn0No9m3O_0yTdpe9LBSS4hqaXHtPzdNuLm9ppJjELQ1_GBEwkgYtih_GeyRRThW_kStGXnRzcknyp9Xtyn8fwwQ47ytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
پیشنهادهای ویژه ایرانسل برای همراهی مشترکان با جام‌جهانی ۲۰۲۶
🔸
ایرانسل، همزمان با جام‌جهانی ۲۰۲۶، مجموعه‌ای از پیشنهادهای ویژه برای همراهی با این رویداد، ارائه کرده است.
🔸
بسته‌های «فوتبالی‌پلاس» شامل ۹۰ گیگ اینترنت و ۲۰۲۶ دقیقه مکالمه ایرانسلی و ۴۵ گیگ اینترنت به همراه ۲۰۲۶ دقیقه مکالمه ایرانسلی با اعتبار ۶۰ روزه عرضه شده‌اند.
🔸
این بسته‌ها برای استفاده از پلتفرم‌های پخش آنلاین مسابقات شامل iSport، آپارات اسپرت، فوتبال ۳۶۰، ورزش۳ و آنتن ارائه شده‌اند.
🔸
همچنین بسته‌های ساعتی ۹۰ گیگ ویژه تماشای مسابقات نیز در اختیار مشترکان قرار دارد.
🔸
مشترکان می‌توانند با شرکت در مسابقه پیش‌بینی جام‌جهانی ۲۰۲۶، نتایج بازی‌ها، دیدارهای تیم ملی ایران و قهرمان مسابقات را پیش‌بینی کرده و شانس دریافت ۱۰۰ میلیون تومان اعتبار خرید کالای دیجیتال و یک ترابایت اینترنت هدیه را به دست آورند.
🔸
در طرح «پیشواز فان» نیز با فعال‌سازی آهنگ پیشواز، امکان شرکت در قرعه‌کشی جوایز ارزشمندی، فراهم شده است.
🔸
بازارگاه ایرانسل نیز شرایط خرید اقساطی و بدون پیش‌پرداخت تلویزیون، همراه هدایای ویژه را فراهم کرده است.
👈
جزئیات بیشتر
@irancelnews1</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/441579" target="_blank">📅 16:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441578">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3494c4c7ae.mp4?token=iXC_9Agb1580twh4kCpHdWeYX3zu5X9iMGbCLvQ2h-yuIC9MNwU_c9YS4N1fe5eEcEFAULNUlFtHLCjJEXwpTkSutuW1UWqbCcmKWQU2l6WH05ZbB6EZ8YAkjeD_3thmYJt58h5-iY1MutENeUFlvgnvprsrru1FZmApymHiCaFP8eORxlSoiVoesBDfNCT_2ALmThNlQ4HGK3QWEqGlPbrEWB8nO0InfxaAWuJtHkFJqsWGW1bk9k1AvsSu5Wmhafpy-dIJW353inh_jiP38H3sGImvlBlhi9Vhq0zGTpN-qFeAmR9YtOzyLsqTmhk384Fj3NjuR9J1_sGe9KbAnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3494c4c7ae.mp4?token=iXC_9Agb1580twh4kCpHdWeYX3zu5X9iMGbCLvQ2h-yuIC9MNwU_c9YS4N1fe5eEcEFAULNUlFtHLCjJEXwpTkSutuW1UWqbCcmKWQU2l6WH05ZbB6EZ8YAkjeD_3thmYJt58h5-iY1MutENeUFlvgnvprsrru1FZmApymHiCaFP8eORxlSoiVoesBDfNCT_2ALmThNlQ4HGK3QWEqGlPbrEWB8nO0InfxaAWuJtHkFJqsWGW1bk9k1AvsSu5Wmhafpy-dIJW353inh_jiP38H3sGImvlBlhi9Vhq0zGTpN-qFeAmR9YtOzyLsqTmhk384Fj3NjuR9J1_sGe9KbAnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎁
اعلام جوایز قرعه‌کشی حساب‌های قرض‌الحسنه پس‌انداز بانک رفاه کارگران
⏳
فقط تا ۳۱ خرداد فرصت داری!
💰
بیش از ۳۰۰۰ جایزه ویژه در قرعه‌کشی حساب‌های قرض‌الحسنه پس‌انداز بانک رفاه کارگران
🏆
۱۰۶۶ جایزه نقدی ۲.۵ میلیارد ریالی
🚘
۱۰۶۶ کمک‌هزینه خرید خودرو ۲ میلیارد ریالی
🏠
۱۰۶۶ جایزه لوازم خانگی ۱ میلیارد ریالی
✨
به همراه هزاران جایزه نقدی دیگر
برای شرکت در قرعه‌کشی کافی است:
✅
حداقل ۹۰ روز، موجودی حساب شما کمتر از یک میلیون ریال نباشد.
✅
در روز قرعه‌کشی (پاییز ۱۴۰۵) حساب فعال و دارای حداقل موجودی یک میلیون ریال باشد.
✅
کد شهاب داشته باشید.
⏳
فرصت محدود است…
امروز حساب خود را تکمیل کنید و شانس برنده شدن میلیاردها ریال جایزه را از دست ندهید.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/441578" target="_blank">📅 16:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441577">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/441577" target="_blank">📅 16:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441576">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌ الگوی ترامپ و روایت واقعیت از پس یک جنگ روانی
🔹
ترامپ دیشب باز هم الگوی ثابت خود در مذاکرات را به‌کار گرفت؛ الگویی که در آن همزمان با عقب‌نشینی در عمل، با فضاسازی تهاجمی در رسانه سعی کرد القا کند که طرف مقابل تحت‌فشار ترسیده و تسلیم شده است.
🔹
این شگرد که…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/441576" target="_blank">📅 16:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441575">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ادعای رسانه غربی از علت پرواز هواپیمای اماراتی به تهران
🔹
رسانه غربی اینتل واچ مدعی شد هواپیمایی که روز گذشته از ابوظبی به تهران آمد حامل ۳ میلیارد دلار پول بوده است.
🔹
امارات در جریان جنگ رمضان بیشترین خسارت را به دلیل در اختیار دادن خاک خود به آمریکا متحمل…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/441575" target="_blank">📅 16:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441574">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce19e49030.mp4?token=WBvxQhKZVpCC4Rzik5Y-8XZ28pTF789_XpHFxT-0TOdBtP4Grrel0683oZVQZV-4XGaD9aL4Fi1ZD3YcxpowKB7KmqpCsvs66GrolmgKQxIt864zOghqa9Q4pP-xBhKS4liqGM3nM_qDd92BVaZ8oP4TDML4Trghl_g5gR_RB2c9TnKZue5XamgDSQVVN94TVewiLNixTjoY7eZb01D6dv0RbxaYtPiUyZzYBYJNLI0emK3YOTp-Ryiji23PniRWV7IfSXIkI3o80aIhcq0na-yrXDcEpTLKJVqyeetOuqI4dnyEpn2sCCt1_o9vp75wxhT-rmFJ3BR-jiapEhhbzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce19e49030.mp4?token=WBvxQhKZVpCC4Rzik5Y-8XZ28pTF789_XpHFxT-0TOdBtP4Grrel0683oZVQZV-4XGaD9aL4Fi1ZD3YcxpowKB7KmqpCsvs66GrolmgKQxIt864zOghqa9Q4pP-xBhKS4liqGM3nM_qDd92BVaZ8oP4TDML4Trghl_g5gR_RB2c9TnKZue5XamgDSQVVN94TVewiLNixTjoY7eZb01D6dv0RbxaYtPiUyZzYBYJNLI0emK3YOTp-Ryiji23PniRWV7IfSXIkI3o80aIhcq0na-yrXDcEpTLKJVqyeetOuqI4dnyEpn2sCCt1_o9vp75wxhT-rmFJ3BR-jiapEhhbzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از خسارت حملات ایران به پایگاه آمریکا در بحرین
🔹
پایگاه تحلیل تصاویر ماهواره‌ای «سور اطلس» با انتشار یک تصویر ماهواره‌ای‌ از ضربه موشکی ایران به ساختمانی در پایگاه هوایی عیسی در بحرین خبر داد.
🔹
پایگاه هوایی عیسی یک مرکز استراتژیک برای میزبانی از دارایی‌ها و تجهیزات نظامی ایالات متحده در منطقه خلیج فارس است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/441574" target="_blank">📅 15:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441573">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
تیراندازی مرگبار نزدیک کمپ تیم ملی آرژانتین در آمریکا
🔹
در پی وقوع تیراندازی در یک مجتمع مسکونی در نزدیکی محل اردوی تیم ملی فوتبال آرژانتین در کانزاس‌سیتی، یک نوجوان جان خود را از دست داد و ۲ نفر دیگر مجروح شدند.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/441573" target="_blank">📅 15:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441572">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LR2-AO5dKeJOK_SIdqlYJ_mLlFAGoIpKeiJc1fOiphQ0xo0tDt068isvTGPLc7TeX4xNs9CTs62sSfq-ofQv49MbgcAuugXIveZksY0GrzgInjmSvN7RmB5ViXv1d0D19xSlWfOgIgeRxNTisAZ4Sf-98RtwOaXNn2I5eZ1G9K2znzg_JjEIuDaTSz2KWg-irRw1GwbYrKeXLnpfHsbyzcRspHem3kvQLKJLyxOdpq_qDEqghUtfEhAkyTUP3iNyH_WK9PfmmWLew_FFcRev7rPLvpo7MVcivF6MMGJWwqZI9LAQ5JIkk28n4VHbdMg252tPW18zNJTv-TzWx-su2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل شرکت توزیع برق تهران: یک‌چهارم برق پایتخت در بخش تجاری مصرف می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/441572" target="_blank">📅 14:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441571">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اموال ۱۹ وطن‌فروش در کردستان توقیف شد
🔹
رئیس‌کل دادگستری کردستان: اموال ۱۹ نفر از عناصر وطن‌فروش و خائن به مردم در استان توقیف شد.
🔹
متهمان از اماکن حساس و محل اصابت برخورد پرتابه‌های دشمن فیلم و عکس تهیه کرده و برای رسانه‌های وابسته به دشمن و حساب‌های کاربری وابسته به سرویس‌های جاسوسی ارسال می‌کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/441571" target="_blank">📅 14:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441570">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np091ywUPZMfd9vIqhXWJ49ueMmfgke7PnbnqkESW0Fkvv43LjzPjZjYNDIyLLFo9FnQKL0UodJg24m7VulydFVSki2QHyDdGn3T0QVi9xgDSiJQDdgewv_DOfdsxGDuoQGBTC1fzC-OZKDV-YR92z_UYo0Qkcf03vLdGBLaGcH609KmjVH_D9ZiXUN9VniTtLuKwM7Ibg64HNCUe0rrHITfvYj9IaHW1EHPY82jRIkL4IJnS6J46vq2riD8QKSiJt7PLgSuIdA7PK_HUy0vlhjMXJtvEu7vsFhp104ZgGTv3j97aUZ988dt39t8FpWnTiZuoP-G9rs8JZaqZ22_zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرودگاه هامبورگ در پی یک حادثه امنیتی تخلیه شد
🔹
شبکۀ ان‌دی‌آر به‌نقل از پلیس هامبورگ اعلام کرد فرودگاه این شهر در پی یک «حادثه امنیتی» به‌طور کامل تخلیه و تمام پروازهای آن متوقف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/441570" target="_blank">📅 13:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441569">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فهرست چند عطر غیرمجاز و خطرناک منتشر شد
🔹
سازمان غذا و دارو با انتشار فهرستی از محصولات بدون مجوز، نسبت به خطرات احتمالی آن‌ها برای سلامت عمومی هشدار داد.
🔹
گروه ادوپرفیوم:
🔹
Dark Aoud
🔹
MAY WAY
🔹
ALLTEREI (Royal Essence Eau de Parfum)
🔹
گروه بادی‌اسپلش:
🔹
Mar Maris
🔹
The Body Shop
🔹
JANA
🔹
MATERIAL (Perfume Spray)
🔸
استفاده از این محصولات می‌تواند به‌دلیل تماس مستقیم با پوست و تنفس ذرات شیمیایی، عوارض جدی از جمله حساسیت‌های تنفسی و حتی اختلالات هورمونی ایجاد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/441569" target="_blank">📅 13:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441567">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‌ تکمیلی: روایت ترامپ از «پذیرش ایران» در برابر واقعیت میدانی
🔹
همزمان با عقب‌نشینی تاکتیکی آمریکا از اضافه‌بندهای جدید به پیش‌نویس توافق، دونالد ترامپ با افزایش لحن تهدیدآمیز در شبکه‌های اجتماعی، تلاش می‌کند روایت «تسلیم ایران در برابر بمباران» را بسازد؛…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/441567" target="_blank">📅 13:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441566">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22473c5f26.mp4?token=gNUtgrTy0cATP-pP0Vmkr8ndORtI2eo3fw59q3hJsFxghyG_VzBsme_yZPxI4Dvrd9dnWExJNzoYDhVgAq75csugx5bPSn_I5U3AP9jRN5PedZzU2uqndKO7omWXFloiSjQzjx4VOd-gOGTsSFt7v_tzU-K3JTYtrDa1LC6wpceKdQSMVmwcasoR83DBJVFyA-QzL86GzT-Dg-x86gCSZdrvPQ7ZjMpv9-AEXZ-AMCsa1HcJ7SwZxzgPwH9odY78hSLJjVPTB3W8gPZ4WOv-azchRHBlVElR3CrweO9hTrkySxBZICGHbn-zNY2YJE95i0u8O9092nzwQbdSywFJrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22473c5f26.mp4?token=gNUtgrTy0cATP-pP0Vmkr8ndORtI2eo3fw59q3hJsFxghyG_VzBsme_yZPxI4Dvrd9dnWExJNzoYDhVgAq75csugx5bPSn_I5U3AP9jRN5PedZzU2uqndKO7omWXFloiSjQzjx4VOd-gOGTsSFt7v_tzU-K3JTYtrDa1LC6wpceKdQSMVmwcasoR83DBJVFyA-QzL86GzT-Dg-x86gCSZdrvPQ7ZjMpv9-AEXZ-AMCsa1HcJ7SwZxzgPwH9odY78hSLJjVPTB3W8gPZ4WOv-azchRHBlVElR3CrweO9hTrkySxBZICGHbn-zNY2YJE95i0u8O9092nzwQbdSywFJrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت آیت‌الله سیدمحمود مرعشی از مراتب علمی آیت‌الله سیدمجتبی خامنه‌ای
🔹
آیت‌الله سید محمود مرعشی، نسخه‌شناس برجسته و فرزند ارشد آیت‌الله شهاب‌الدین مرعشی نجفی(ره): روزی در تهران با آیت‌الله سیدمجتبی خامنه‌ای قرار ملاقاتی داشتیم که بیش از ۲ ساعت و نیم طول کشید. در این جلسه درباره مباحث مختلف حوزوی، اساتید، دروس و تقریرات علمی گفت‌وگو کردیم.
🔹
در جریان این گفت‌وگوها به تدریج متوجه شدم که ایشان از نظر علمی مطالعات و تحصیلات عمیق و گسترده‌ای داشته‌اند.
🔹
این موضوع برای من بسیار شگفت‌انگیز بود و همان روز تصمیم گرفتم که اگر لازم باشد از ایشان دفاع کنم.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/441566" target="_blank">📅 12:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441565">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtHmCw7VGEYNPbwX_E_LbwNaL16amkIHjc_nmolHM2KODvArZ9QXAe4Iybq1N-C1rqqFgY6nrm4JWPIhd2Q4dPVAtxM1Qm8MNgJZktA_2uYVEgB9z3fAMOtKRHYEv8ZYOm7VBVDncSu09gqNOpuat_RCnSEPjPpZEyrnVntDme5dSvV2RD1Ppswefs2pi5koiQxjvi6CkB8nbhp3Nz-udQpmQ6pNttZyhl_zZzQmmzpA4Ys4oPUYQKTCQa8VD6u4R8xCWBu0XxRUGhpv25LJrJZ9-AygFn9E-_1mCdlCy2g8DDwUA9n_oB0cKO1A8-yD-zt8BCguZJd2EmX-bBzC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: انسجام و همبستگی ملی مهم‌ترین سرمایهٔ کشور در شرایط کنونی است
🔹
در وقایع اخیر بیش از ۱۰۰ شب است که ملت ایران در صحنه در دفاع از کشور و انقلاب حضور دارند و نقشه های دشمنان را نقش بر آب کردند.
🔹
بسیاری از محاسبات و برنامه‌ریزی‌های دشمنان به‌واسطهٔ همین…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/441565" target="_blank">📅 12:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441564">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYn8xgDzwD1Ax5Ftv4-Q0OVUQsP4HRBw4OjdzixYWpmPGltOOQlDNtT01e6Wb9Y0gbn0OM5ZI1Pm0MPxO151bSyzZ6n3w4Rp98gxSiLl4-b_9d4Q9eRxPxjs_pAxARQ-tAnYyZ9vhFgBpoJB6kv9pogJHg6uWtHe4DdX5Kb3M8x8-tyF4UCznRsqe5pVyrUfY5sdbg3ppJCeV9z1QtX_rAX0CEz6sIYo5V7j9pt-DPPrhpRiRPOtnye8FfgAkYm9gfObHZWxjZy_qD2XBWl84MBQJB2ttEUJ_P-RuFuDzdPn9WCFlOWF5efH3XOzRRN7ZCX5bcaRpqmp1OsymQB4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: انسجام و همبستگی ملی مهم‌ترین سرمایهٔ کشور در شرایط کنونی است
🔹
در وقایع اخیر بیش از ۱۰۰ شب است که ملت ایران در صحنه در دفاع از کشور و انقلاب حضور دارند و نقشه های دشمنان را نقش بر آب کردند.
🔹
بسیاری از محاسبات و برنامه‌ریزی‌های دشمنان به‌واسطهٔ همین همراهی و ایستادگی مردم ناکام مانده است.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/441564" target="_blank">📅 12:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441563">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‌ پروازهای فرودگاه مشهد و روند بازگشت حجاج به روال عادی بازگشت
🔹
روابط‌عمومی فرودگاه شهید هاشمی‌نژاد: با فراهم‌شدن شرایط، محدودیت‌های پروازی رفع شده و پروازها در فرودگاه شهید هاشمی‌نژاد مشهد طبق برنامه به روال عادی بازگشته است.
🔸
پیگیری‌ها نشان می‌دهد روند…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/441563" target="_blank">📅 12:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441562">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d5295085.mp4?token=fo9Ubo1aqchutTK9ToCc8QeEU22clhXvMv0rWH7L3_SKRtj7bzNzBSDQI1Qi_rgouVMj-7wPwZCM4I_OODUCznMFtdCTcEQeAkp-35RuIVRuv8mjR8lps6w2f6vJpVy-SbKmfB_cpNgE_tPJT1DUbFP_x0NQgUAwbLjTAEJdSBArfppzuDJG7Y4bZ8xHZxMV0hfYi7XKq_AQaFfS0F3NJPqXAcbI0wOn_1mfEq956I_vDqjghjhw879AGk4HOh6XheYlsJphGRxLTkUmyc1VFUPx2F68cpj5AJKo7BdvJ_2ZNiCpkLHJcu2oIT4eLVJfFk4o2ReSA_CFzVCzG31d6HJ_X-dcZvXU5pQMze0d0Y4QNyLZHicM2hnLRu919Klm-Toak4QXpZH24Wa_UR0eiO9nrNt4X-60KY-E2PGZjZk65Mgjje9fYMmd9JvyNwRDSW8e-J3Ej82tjflEhs5p1fvPFEGhkBRX5UITr_W6cg1J0c-otZzD_PvqW1zPK_myxrx0G8M5eB5ujCw_AfSQ_BDGfvIFHgLxb_fGB9ZZPwo5Kddzd7DD6fpMfTRosNrRMeBzX5H1e2lTy8NfKWg7YG1uYms4qGdIiDHkz8AzQgWG-968NSSngmtzaNew26Hi7JQU_56iEyWKMmwL3Q-CRXrT4w4Kp2_fLmxW6ConK1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d5295085.mp4?token=fo9Ubo1aqchutTK9ToCc8QeEU22clhXvMv0rWH7L3_SKRtj7bzNzBSDQI1Qi_rgouVMj-7wPwZCM4I_OODUCznMFtdCTcEQeAkp-35RuIVRuv8mjR8lps6w2f6vJpVy-SbKmfB_cpNgE_tPJT1DUbFP_x0NQgUAwbLjTAEJdSBArfppzuDJG7Y4bZ8xHZxMV0hfYi7XKq_AQaFfS0F3NJPqXAcbI0wOn_1mfEq956I_vDqjghjhw879AGk4HOh6XheYlsJphGRxLTkUmyc1VFUPx2F68cpj5AJKo7BdvJ_2ZNiCpkLHJcu2oIT4eLVJfFk4o2ReSA_CFzVCzG31d6HJ_X-dcZvXU5pQMze0d0Y4QNyLZHicM2hnLRu919Klm-Toak4QXpZH24Wa_UR0eiO9nrNt4X-60KY-E2PGZjZk65Mgjje9fYMmd9JvyNwRDSW8e-J3Ej82tjflEhs5p1fvPFEGhkBRX5UITr_W6cg1J0c-otZzD_PvqW1zPK_myxrx0G8M5eB5ujCw_AfSQ_BDGfvIFHgLxb_fGB9ZZPwo5Kddzd7DD6fpMfTRosNrRMeBzX5H1e2lTy8NfKWg7YG1uYms4qGdIiDHkz8AzQgWG-968NSSngmtzaNew26Hi7JQU_56iEyWKMmwL3Q-CRXrT4w4Kp2_fLmxW6ConK1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاکسازی سازمان‌یافته در کرانۀ باختری فقط توسط شهرک‌نشینان انجام می‌شود؟
🔹
سازمان عفو بین‌الملل و آکسفام اقدامات اسرائیل در کرانه باختری را «پاکسازی قومی سازمان یافته علیه فلسطینی‌ها» خواندند و تاکید کردند: این اقدامات کار عوامل خودسر یا آنچه که شهرک‌نشینان افراطی خوانده می‌شود، نیست.
🔹
سازمان عفو بین‌الملل در گزارشی هشدار داد که «جامعۀ جهانی باید فوراً برای متوقف‌کردن روند الحاق کرانۀ باختری اشغالی توسط اسرائیل اقدام کند و بی‌عملی در این زمینه به‌معنای هم‌دستی است».
🔹
این گزارش با موضوع «پاک‌کردن هرچه فلسطینی است؛ پاکسازی قومی اسرائیل علیه جوامع فلسطینی و دامدار بادیه‌نشین در کرانه باختری» نشان می‌دهد که دولت اسرائیل، الحاق رسمی این منطقه را به یکی از اهداف آشکار سیاست‌های خود تبدیل کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/441562" target="_blank">📅 11:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441561">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6492bfd8ae.mp4?token=TLOuIkaRURDaqItVSiZuzWfM11pzUQsiGciLeQeFBoWTgYwBbNbEErxKs_l8WXdhgn3wSmBYymJOcplgOzJSnzBMOkW6UywqKczZOpZ577k02DoNZ1ez3T9FKzr9Gayno4q4oIhV6f9nB8YKRiYVfelfo2cJ0TJ8mxxAR7vLhe17UpgFWVEyJBZpGAV0SNAphNa4EOvhn6hintkSnuwGUZF-GF2Az_i8MtDRJA7bhP79DAzRBMOjCoaVo30sA2SfCLuP2VMYYS_9KKf6dCGYFpqOGCd6NQOKSqxFV9RhMU7Ym30Q_WUC09cHz7XYao1otZg7rGARuIcaEVDIAb7x0nVEkCQeTN1jTTZdqOTIFNVHqES_xyzpe_FyiufuLynA0QBZNm9hL4NytSTNNND2ms5HTVV6u1RYCbfvlXwr2PxR2mneEjeQFSmHxVBn9ZxIygqFgnPY85_neEqJ31YSrTh6BAJEQBTJnIN2FKauNd5iq5k1Rp-Dbm86OJzOW5c7bw0h9nZWfUoLH8qs5jxnXX5qg7m_sLreRQFGLoKH_DcAxaC9o9Tgg81BT2ZJrH9VuzIIDJ4rAVT2b_oxk9vBmWMEEU7SCrcKntu6kG8adpm4tbgK8gvzAYO9o8idSoaGpaJ1qxSwkXRo4cdUuOvePKpOHHnN95letd1dVFsbPEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6492bfd8ae.mp4?token=TLOuIkaRURDaqItVSiZuzWfM11pzUQsiGciLeQeFBoWTgYwBbNbEErxKs_l8WXdhgn3wSmBYymJOcplgOzJSnzBMOkW6UywqKczZOpZ577k02DoNZ1ez3T9FKzr9Gayno4q4oIhV6f9nB8YKRiYVfelfo2cJ0TJ8mxxAR7vLhe17UpgFWVEyJBZpGAV0SNAphNa4EOvhn6hintkSnuwGUZF-GF2Az_i8MtDRJA7bhP79DAzRBMOjCoaVo30sA2SfCLuP2VMYYS_9KKf6dCGYFpqOGCd6NQOKSqxFV9RhMU7Ym30Q_WUC09cHz7XYao1otZg7rGARuIcaEVDIAb7x0nVEkCQeTN1jTTZdqOTIFNVHqES_xyzpe_FyiufuLynA0QBZNm9hL4NytSTNNND2ms5HTVV6u1RYCbfvlXwr2PxR2mneEjeQFSmHxVBn9ZxIygqFgnPY85_neEqJ31YSrTh6BAJEQBTJnIN2FKauNd5iq5k1Rp-Dbm86OJzOW5c7bw0h9nZWfUoLH8qs5jxnXX5qg7m_sLreRQFGLoKH_DcAxaC9o9Tgg81BT2ZJrH9VuzIIDJ4rAVT2b_oxk9vBmWMEEU7SCrcKntu6kG8adpm4tbgK8gvzAYO9o8idSoaGpaJ1qxSwkXRo4cdUuOvePKpOHHnN95letd1dVFsbPEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قهرمان‌هایی که در روزهای سخت کنار مردم ماندند
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/441561" target="_blank">📅 11:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441560">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‌ پیام تسلیت رهبر انقلاب در پی ارتحال آیت‌الله فیاض
🔹
خبر ارتحال مرجع عالی‌قدر، آیت‌الله حاج شیخ اسحاق فیاض (طاب ثراه)، موجب تأثر و اندوه فراوان گردید و حوزه‌های علمیه به‌ویژه حوزۀ مقدسه نجف اشرف را در سوگ نشاند.
🔹
سال‌ها حضور در حوزه مقدسه نجف اشرف و کسب…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/441560" target="_blank">📅 11:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441559">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7962256a5.mp4?token=pj6MZGxiv-JaIq9y06L8MrcugTspRxdjfXr4SkqLgjtK5UcLAXx5fhZO-qN05tMAml1g7_1608oYYjFX12Im8bYyFRhfxejmFKjPDLw-FPbneeapr2rfcgZTD9BI9FraCTvFOseE9DPWP9QfG8kbCLK99aRV3kmWI58xwhaaUwRjEEDlbZJT91nSfzqar8Q260FJc8T6ZQf2p_18HOwgNJd3cwMx5sxhq2lo9WQPBq6ColBfgdDTYjZyvTbFpMmL3-OvoHE7fPqTMRrxMaIIFqAPK596D0g-pAiX4qMTWMU1fP-8XyoK5rAqSpptIB9uH5htv6HLPvIU_Hgb2GBBAIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7962256a5.mp4?token=pj6MZGxiv-JaIq9y06L8MrcugTspRxdjfXr4SkqLgjtK5UcLAXx5fhZO-qN05tMAml1g7_1608oYYjFX12Im8bYyFRhfxejmFKjPDLw-FPbneeapr2rfcgZTD9BI9FraCTvFOseE9DPWP9QfG8kbCLK99aRV3kmWI58xwhaaUwRjEEDlbZJT91nSfzqar8Q260FJc8T6ZQf2p_18HOwgNJd3cwMx5sxhq2lo9WQPBq6ColBfgdDTYjZyvTbFpMmL3-OvoHE7fPqTMRrxMaIIFqAPK596D0g-pAiX4qMTWMU1fP-8XyoK5rAqSpptIB9uH5htv6HLPvIU_Hgb2GBBAIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی قوه قضاییه در گفتگو با تلویزیون روایت فردا خبر داد:
بیش از ۱۴۰۰ همت اثر بخشی مالی بر اثر تلاش و مبارزه مستمر دستگاه قضایی در ۵ سال گذشته
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/441559" target="_blank">📅 11:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441558">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPdmFDhgIaG2BMpmYGVP584izmpstBjd3BYoLCuciPj6Rdi-dqPWwhThoVYYOSVi4_RdBIlaPgb7nJFrwPVTRDpa1pp74kdapPz5Q10ZQ3pcaopPjCAoInGfvZSKshNKcB1YUgB9lSexMiHnaUF5PKUVdHQHFt8ZF6dTao7aKRMMdkO_02FKMfp4gsgjJ5WryN3FsJbeGCSPnfehuvzcobb6dqf6urXiqPKfQ5IoiKNr8WSUkVYIODaZOJ3y6WVsiofLbt0KcYWW4wi7YGKO3gZdu3cS-jlmzrsC6M6gulfSKEz3-Mi0dzo51GFNSGkmGqXZZZkvTXxZguDa-tBicQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هنوز ۵ گیگ اینترنت رایگان نگرفتی؟
برای شروع پیش‌بینی‌ها:
1️⃣
وارد اپلیکیشن «همراه من» شو
2️⃣
گزینه زمین بازی (جام جهانی) انتخاب کن
3️⃣
مسابقه‌های جام جهانی رو پیش‌بینی کن
4️⃣
۵ گیگ اینترنت هدیه بگیر و برای جوایز میلیاردی رقابت کن
🏆
⚽️
در «همراه من» پیش‌بینی کن و برنده شو!
👇
👇
https://www.mci.ir/-4S0XAJB</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/441558" target="_blank">📅 11:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441557">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/441557" target="_blank">📅 11:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441556">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b0718a9af.mp4?token=MHFwXZA7O8YlOo9q-30z-cG7rL2dlz5Ml0FU1FEMtW_zkT-C6fpb_bdmiqZj12Bm-88TJ4QtZzCXzCeJNQGKm8MVq2HAPhQArICqPw89ta7wOFQ2DkSFKcq_XKJTNhbsN6FlrVVmCfIEVQ6iGtutyi8AwQK-f3KMJvYAqNakxmmuKnCgwzGTftHjLfD8gWhw-4UJVJz8mWZgyCfOCYfNLpWPnEFhBRrdzqtwy0pWGCGNEl6MNphKS5uh0xwj4ZoF_IpAISwcp2WqJ2nVwe6Qf11PmRxg9eoWmFFaxSTp6SK-__9JUdQAeB26ecsYu_P8tPfn4ol8EJCQxsZCRPwd6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b0718a9af.mp4?token=MHFwXZA7O8YlOo9q-30z-cG7rL2dlz5Ml0FU1FEMtW_zkT-C6fpb_bdmiqZj12Bm-88TJ4QtZzCXzCeJNQGKm8MVq2HAPhQArICqPw89ta7wOFQ2DkSFKcq_XKJTNhbsN6FlrVVmCfIEVQ6iGtutyi8AwQK-f3KMJvYAqNakxmmuKnCgwzGTftHjLfD8gWhw-4UJVJz8mWZgyCfOCYfNLpWPnEFhBRrdzqtwy0pWGCGNEl6MNphKS5uh0xwj4ZoF_IpAISwcp2WqJ2nVwe6Qf11PmRxg9eoWmFFaxSTp6SK-__9JUdQAeB26ecsYu_P8tPfn4ol8EJCQxsZCRPwd6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسطورۀ فوتبال مصر: آمریکا با میزبانی جام جهانی می‌خواهد آبرویی که با جنایت از دست داده را برگرداند.
🔹
محمد ابوتریکه: فیفا با دادن میزبانی به آمریکا در حال سفیدشویی جنایات میزبان این رقابت‌هاست. اینفانتینو می‌خواهد جام جهانی را در کشوری متجاوز برگزار کند.
🔹
کشوری که در نسل‌کشی غزه شرکت دارد و حالا جام جهانی را میزبانی می‌کند تا آبروی خودش را برگرداند. کشوری که رئیس‌جمهور ونزوئلا را ربود و به ایران حمله کرد، حالا با جام جهانی می‌خواهد جنایاتش را سفیدشویی کند تا آبروی خودش را برگرداند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/441556" target="_blank">📅 10:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441555">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38e7322b2.mp4?token=Mq9MTRg3VPoWzxiQJcxy1_ZJLfaov7lbU22VaJn4ool5hTHdHTvyC35yQIHsOE_9OPLTa0MMwA0TmylC9U3Hq2EzuHAX8QivEy16S_feTXAANN6FTn2c68XrZwCF-SLl5wM6XHLGNFsMPqP6W4L_4eLIL1o33SLMe-EchyPEeh7tc6kiDvI5ewvrD7LweRuGTHyNGsPnw8u616_xVGlJ3uWdiJOp7nuNL15xU-A9mO1bXbh_7iIu8ckMFZ7dYplUQk87lt_uBI30Aii8SVPv7xEPujtCyICAR1bdk9-2jCNk3huarR8u04GUj7CtzJkOxhRVlQMem6bCkkgG9aIaDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38e7322b2.mp4?token=Mq9MTRg3VPoWzxiQJcxy1_ZJLfaov7lbU22VaJn4ool5hTHdHTvyC35yQIHsOE_9OPLTa0MMwA0TmylC9U3Hq2EzuHAX8QivEy16S_feTXAANN6FTn2c68XrZwCF-SLl5wM6XHLGNFsMPqP6W4L_4eLIL1o33SLMe-EchyPEeh7tc6kiDvI5ewvrD7LweRuGTHyNGsPnw8u616_xVGlJ3uWdiJOp7nuNL15xU-A9mO1bXbh_7iIu8ckMFZ7dYplUQk87lt_uBI30Aii8SVPv7xEPujtCyICAR1bdk9-2jCNk3huarR8u04GUj7CtzJkOxhRVlQMem6bCkkgG9aIaDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با داشتن این خصلت خدا حتی صدایت را هم نمی‌خواهد بشنود
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/441555" target="_blank">📅 10:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441554">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
المیادین: رژیم صهیونیستی به النبطیه در جنوب لبنان حملۀ پهپادی کرد.
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/441554" target="_blank">📅 09:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441552">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e11b63690.mp4?token=bPcpc_EaSjpVUvrEwjpAvBi4NDqhEDRLtiZz_j7l0TA2MPxcOd-TzjRQXFAZPR_8sMa9mnmH4xO5gQDICMziHEVqOdNhj_F8SDJj4dDAHiZk2aOiwhrKgcdnO-WaZsDK56K2KFnQC5voaKOFh3MpmLZOeUHEWwwsev0nR2Rw0VxweMepvPZQ_bYtadAxI3X9p9bmmPBGfrTPsvQOq4IOSZAJSpserFTgvro7xN5cd2KoePguIzm96LknuSi4XOLV2GSODxY3lDNhPnqUSh8MKkfaKja9LV5rHRhfYIOtiL9uzb7B5pa8Y-7oPKe6LKUfUgRQySliYclMg51TuVhfCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e11b63690.mp4?token=bPcpc_EaSjpVUvrEwjpAvBi4NDqhEDRLtiZz_j7l0TA2MPxcOd-TzjRQXFAZPR_8sMa9mnmH4xO5gQDICMziHEVqOdNhj_F8SDJj4dDAHiZk2aOiwhrKgcdnO-WaZsDK56K2KFnQC5voaKOFh3MpmLZOeUHEWwwsev0nR2Rw0VxweMepvPZQ_bYtadAxI3X9p9bmmPBGfrTPsvQOq4IOSZAJSpserFTgvro7xN5cd2KoePguIzm96LknuSi4XOLV2GSODxY3lDNhPnqUSh8MKkfaKja9LV5rHRhfYIOtiL9uzb7B5pa8Y-7oPKe6LKUfUgRQySliYclMg51TuVhfCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مونتاژ منتشر شده توسط شبکه سی‌ان‌ان از ۳۹ باری که ترامپ از آغاز جنگ تا به امروز ادعا کرده است توافق میان ایران و آمریکا «نزدیک است»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/441552" target="_blank">📅 09:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441551">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHhvGJo4oX6m95dLwfCek8pWgkhTSz-CmXEx02jmGCfdisq7g9OInxNvQxGGAsJg_oYXnrnKggI_5q1Unc2PEcv7sfTNDOOuV2cEeexrVXCx7xXvIMS7vOj-CR9eVofKiMndpyUfhWLWpNL1vd_Jy7KxWPdEpvKSqMpk8Bg4oEVb1W9keArmB5WMvcXBLG93DzFocaTOqf-I8oiUV246NxYnPbSoSKl2-w6ZmAVbjDc08gUzBKlpL1H3UBOs_rQGuEnfjLbF5nAOpQZoTf10iN9vRODT2JxVUE0Ky9W2oRmHzSOcUuyUY84PENeK2BCGQPLBi5IWeO-D-3bQ2zc6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حبس ابد برای رئیس‌جمهور شورشی کرۀجنوبی
🔹
دادگاهی در کره‌جنوبی امروز رئیس‌جمهور پیشین این کشور یون سوک یول را به‌خاطر رهبری شورش در پی اعلام حکومت نظامی در دسامبر ۲۰۲۴، به حبس ابد محکوم کرد.
🔹
این حکم پس از آن صادر شد که بازرس ویژۀ تحقیق درباره پرونده یون ۱۳…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/441551" target="_blank">📅 08:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441550">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKSkrYLLlEwLzuT9v0N9yTqgrzV79vMJ9YDyuwv0NC-dZXjBTGex89I-vr56wI5s3MaSioUpXjPRu00hjlaKIrl00jTl5VpS4GBbg3uf-Ye9mLnMHjkANnTWsBRdfLjVt-izo4HtqrEsRbOexpbjHjMpv5MSy8T-aRegmhP4bn1XzQETtofRYbPFIi_vTZXZA7iSEngUA8Jyg5CSi0w6lSD6zkBsSFVHFA4ux67MWwAPs3i2FHJ0nlDVtowT_5yGRzb-M-90CuQsCpab1FzihfBILAKejICBcoGGUWqUeIO-Z_c2UTeYgGo2QtOreL5USTMSuD1kb0cPMJ30s8cTVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین برد آسیایی در جام‌جهانی
🔸
کرۀجنوبی ۲ - ۱ جمهوری چک @Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/441550" target="_blank">📅 07:58 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
