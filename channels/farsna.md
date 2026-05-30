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
<img src="https://cdn4.telesco.pe/file/pT8HOGHVuCVSfA5O-723fw6kpoBl_zlCm30uJ__4aq07XKyHAZh9SjpYLjFjtll4F4LTJfiBn22HgYke_GzCNqRdkDDdDTrgLwcJcwxx929aTM4veEqnFxDTxcQYPpLE0N5gpIM3qBoJqG1z-74Etd00uR1zth_QbD8SuneDCjTurAQIk20U8P4S2YL2BwBlXnT3vRBc3VBIGA4eZElLGtHeWdJOkOEexcTwTgomf2t-WuPB7lL50YsooApRwHmMuxL0fsO86Of-MUTdzud54dz6sDRNP84C22rqSXD86h_qRvfOcNsoE8kaBHXhnVlzGaoL5ReJ01G2m1Z8kCrX0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 16:36:06</div>
<hr>

<div class="tg-post" id="msg-438797">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMBLQxxSbzQPkaQeIBc53QVcMyntK4gZvUXCTyi-4NHyVZEvybY8tKpZU8zfX-zhjoupECmXZu5HdGc7EmNEbaZVut_MyvXPb4_rB6Agzr3Y-u9h0L57C_HT_9Ldg9FhFk--I-0JYqz6ads0y0ZjfqJF6hL-hw_v7cjSkFQxC9WUEqMklNrFJM_GV6UrUt89nFIW-nGwAVSCuGCLW2Ke1Qt6TtYPq60czcyR_nCeEZYZfj48i3vWkwcOCq7xTTvu0flnwNfEC6vDF2tdTBeR4a8HMW5s1hdYeR72yL8wIb1G-3BWTdMRLE64h_ghTQuKyH0QGcBc9XlMr-Ww3N22Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا دانشجوی دانشگاه شریف بازداشت شد؟
🔹
بررسی خط خبری رسانه‌های معاند طی چند روز گذشته بیانگر برجسته‌سازی یک پرسش از سوی آنها مبنی بر این است که چرا یک دانشجوی دانشگاه شریف باید متهم به همکاری با منافقین باشد؟
🔹
پاسخ به این پرسش با بررسی سوابق خانوادگی علی یونسی…</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/farsna/438797" target="_blank">📅 16:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438796">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ff6a2b530.mp4?token=d5j95dBj8nnliUihVWsl3lkhMpz4wyVsZEyBcugShTHMIIZnn4pMxZGdp63yx7HA1RjMbfrtUOgEbDOFfD_TdheZ6JSPmKQrUQ3xRviHXzAbruB5oSIpOJhvUSi_YRP647absTAg1kdRw8jHUMim3r3W3GsUohlkfRN-b3RrQe2ES7aIgC7ZOQHBHy_puOl4ROP3y0tOqDnMikyX91aqtGMRHuq5fqURbpW2WluLXhizh2FDWvGAfpJK3q1fZFO0BlfoDPNphntxXeWvYHQIuUGRFATpnma4pUQ87bY_kUiaqt06ddU1JicFi1QmnOP1mLf0fuiscMYco1GnYMVA8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ff6a2b530.mp4?token=d5j95dBj8nnliUihVWsl3lkhMpz4wyVsZEyBcugShTHMIIZnn4pMxZGdp63yx7HA1RjMbfrtUOgEbDOFfD_TdheZ6JSPmKQrUQ3xRviHXzAbruB5oSIpOJhvUSi_YRP647absTAg1kdRw8jHUMim3r3W3GsUohlkfRN-b3RrQe2ES7aIgC7ZOQHBHy_puOl4ROP3y0tOqDnMikyX91aqtGMRHuq5fqURbpW2WluLXhizh2FDWvGAfpJK3q1fZFO0BlfoDPNphntxXeWvYHQIuUGRFATpnma4pUQ87bY_kUiaqt06ddU1JicFi1QmnOP1mLf0fuiscMYco1GnYMVA8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیت‌الله ‌محامی: توجه رهبر انقلاب به سیستان‌‌و‌بلوچستان استثنایی‌ست
🔹
نمایندۀ ولی‌فقیه در سیستان‌‌و‌بلوچستان: صدور چندین پیام و اعزام هیئت ویژه از سوی رهبر معظم انقلاب به این استان، در سطح کشور بی‌سابقه بوده است.
🔹
همان‌گونه که وعده داده شده بود، هندسهٔ جدید…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/farsna/438796" target="_blank">📅 16:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438794">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هلاکت ۲ تروریست در چالدران
🔹
فرمانده مرزبانی آذربایجان‌غربی: حمله عناصر گروهک‌های معاند به یکی از یگان‌های مرزی چالدران ناکام ماند؛ در این درگیری مسلحانه،۲ تروریست کشته و تعدادی دیگر پس از زخمی شدن به آن سوی مرز متواری شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/farsna/438794" target="_blank">📅 16:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438793">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4132519ad3.mp4?token=pl-7cYoAuPwMUT-XfgWLixQFJ_L_R93rFSNmBXubhka7IIZWicbXZDKx92PJJw0lhkBu7TEOVV230cbolFyxwco7CkH4wMZK2BQu0XRGBva1BjyQcIAL77umCznbe7qvUdkUIkebxIfNpsR0p0uFi68Lui2_6D84FYUpum7xigWvVqjYWq4LpURSpdKbu72UdE9M4ULQwtwEUuIR1t5aDaRTuMyPT_HrSPkxUY0mJWqqRRnrfKclQ5NaiqwvTmiPtKCZ5YAf3Av6tXVT8QAqc1SQaCLVXJEN-N5hXJD2fSVG9qvJcAGXpc4y4WaKWP7QZ6xjERjITobkWD-8Qx-m1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4132519ad3.mp4?token=pl-7cYoAuPwMUT-XfgWLixQFJ_L_R93rFSNmBXubhka7IIZWicbXZDKx92PJJw0lhkBu7TEOVV230cbolFyxwco7CkH4wMZK2BQu0XRGBva1BjyQcIAL77umCznbe7qvUdkUIkebxIfNpsR0p0uFi68Lui2_6D84FYUpum7xigWvVqjYWq4LpURSpdKbu72UdE9M4ULQwtwEUuIR1t5aDaRTuMyPT_HrSPkxUY0mJWqqRRnrfKclQ5NaiqwvTmiPtKCZ5YAf3Av6tXVT8QAqc1SQaCLVXJEN-N5hXJD2fSVG9qvJcAGXpc4y4WaKWP7QZ6xjERjITobkWD-8Qx-m1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نیرو: مردم می‌توانند ماینرهای غیرمجاز را معرفی کنند
🔹
ماموران وزارت نیرو بدون اینکه هویت آنها مشخص شود، به گزارش‌ها رسیدگی می‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/438793" target="_blank">📅 16:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438792">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3738784b50.mp4?token=k3sTh_CrxStqVA23ejff98wDV-xu14a9CwThGGxOChuZ85ERqv9khyDrfkM0aM_UIg0J7_mrtutWM3g4m8-j4bYasuffzOlALxKtzGHxkKIfzRY4btShXfsvlvJ57S4FSYz_NZPE7kzRNNWlQO0gf1P7UyzOrec3DqiTkWtJF3WeoJTlaO2VltGxyw4I089iglpr4URx_7x6NqSyk5AIT6ZvKFo83xIEcqN4Mvn3n-vVl-XcL3gF4IKHe30ROIGZgyasSQ8J5GRTEWhib-YYkuAoMptm8ExLSL33KDfZErzLgf9InYjpNKbhGObXl1akpBeAQBVHe9Cu8WRjl4OKQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3738784b50.mp4?token=k3sTh_CrxStqVA23ejff98wDV-xu14a9CwThGGxOChuZ85ERqv9khyDrfkM0aM_UIg0J7_mrtutWM3g4m8-j4bYasuffzOlALxKtzGHxkKIfzRY4btShXfsvlvJ57S4FSYz_NZPE7kzRNNWlQO0gf1P7UyzOrec3DqiTkWtJF3WeoJTlaO2VltGxyw4I089iglpr4URx_7x6NqSyk5AIT6ZvKFo83xIEcqN4Mvn3n-vVl-XcL3gF4IKHe30ROIGZgyasSQ8J5GRTEWhib-YYkuAoMptm8ExLSL33KDfZErzLgf9InYjpNKbhGObXl1akpBeAQBVHe9Cu8WRjl4OKQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نیرو: مردم می‌توانند ماینرهای غیرمجاز را معرفی کنند
🔹
ماموران وزارت نیرو بدون اینکه هویت آنها مشخص شود، به گزارش‌ها رسیدگی می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/farsna/438792" target="_blank">📅 15:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438791">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c06fbcfb22.mp4?token=TZEHAPP3vjLNYpgWL19_IU0LbNYQ0nHIquYsSM0vh9sfEAJWcZ_L8mCJYlxhTQxg9g3Yn-FLcMh2cBSVwQWrRPA0G4yRpDbyJMvqXY7MeDIewbBL4KA39qPxemmzfPKGQe19woN3wZiSOz6a5UILhBFIdqn8xR6Dzc15-4h0ILhWreR71Mr_dGPe5M6TLP5S-oL5CN9pGyKp35JDM2kG519G5XkoJBNgla2zVEgsSE0fOaNrp9uJpcMq7uuSAuomisCmon6mwgdK9lWSIQWUkvQz9qHKeMWrVw7zeFXDCPlUFz96OOtHoKxRCwKY5mC0wd4rFXJm9PboIzL9RNpYHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c06fbcfb22.mp4?token=TZEHAPP3vjLNYpgWL19_IU0LbNYQ0nHIquYsSM0vh9sfEAJWcZ_L8mCJYlxhTQxg9g3Yn-FLcMh2cBSVwQWrRPA0G4yRpDbyJMvqXY7MeDIewbBL4KA39qPxemmzfPKGQe19woN3wZiSOz6a5UILhBFIdqn8xR6Dzc15-4h0ILhWreR71Mr_dGPe5M6TLP5S-oL5CN9pGyKp35JDM2kG519G5XkoJBNgla2zVEgsSE0fOaNrp9uJpcMq7uuSAuomisCmon6mwgdK9lWSIQWUkvQz9qHKeMWrVw7zeFXDCPlUFz96OOtHoKxRCwKY5mC0wd4rFXJm9PboIzL9RNpYHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شبکه ۱۲ رژیم صهیونیستی از اصابت پهپاد در نزدیکی شهرک المطله در شمال فلسطین اشغالی خبر داد
@Farsna</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/farsna/438791" target="_blank">📅 15:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438783">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZ5OhnRdvZccU7oPZqt70waa3-0Dp6Us3vUApSRvFjJZdHbwim4yNGQfUWD-05nsKSU6nMP1h6sg5Ei-fp-5fdLqVo__CoW9I_F55MlEwbIElK0x8V7yt_MZDJajGsWkCSkb1vf6FkYpq2hWhZsPqcPoRcamiXsPAL6ZlPHmS3_ZKDCZCbWrBPh9h49VLDno7GW_w46R0K0pohL5NBIe1CxABE1pPQjj49xG22Jyuc0qHtGMFPbkrdz4j0AK1nxlzVDCrAmP4UVEduh-ZkSwCYxDzh13cFcCPodVYTfyRqclNXKIOl54ldyfHmJyALOaAlKkzz8VR0bWH-xg9jeJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسب ۲ مدال آسیایی در ۲۴ ساعت توسط دوندهٔ ایران
🔹
هانیه شه‌پری ملی‌پوش دوومیدانی زنان که روز گذشته در مسابقات دوومیدانی قهرمانی جوانان آسیا در ۳ هزار متر با مانع نقره گرفته بود، امروز نیز در ۳ هزار متر بدون مانع نایب‌قهرمان شد.
🔹
شه‌پری در این رقابت رکورد ملی ۳۰۰۰ متر جوانان و بزرگسالان ایران را هم شکست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/farsna/438783" target="_blank">📅 15:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438782">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2adbe067b.mp4?token=tE5fDb8FyLp16XyiqosMCF6wTCuX1eoS_Turlj7lFsQL9bb2U9wQTJO3rTEa6-Tul_8JsBoGwG7jleLsxf30m5HXy_UmpFoX78I8N26GwWCsJWGygONGzC3LG3DPeHO07CJPK1Qt1XST0Ac2FDPTS9nWZHROCkF0s-5sAxHMUR2i10zSoSeauVDLCVQMBdVqOax31aEtYKD2h_W5NPFZj8cRBq5xFc-HB-x7zu8E5vQf5AfJvgqBApI-m1WnBOSDcdRCtII_aGqTqsIZIwKwx1o3FHKsXne8A6aKQYVuElb9gH2gxUDLlBDJjbu3LarqqWwmPQJjJF8WPB7Y3XIzBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2adbe067b.mp4?token=tE5fDb8FyLp16XyiqosMCF6wTCuX1eoS_Turlj7lFsQL9bb2U9wQTJO3rTEa6-Tul_8JsBoGwG7jleLsxf30m5HXy_UmpFoX78I8N26GwWCsJWGygONGzC3LG3DPeHO07CJPK1Qt1XST0Ac2FDPTS9nWZHROCkF0s-5sAxHMUR2i10zSoSeauVDLCVQMBdVqOax31aEtYKD2h_W5NPFZj8cRBq5xFc-HB-x7zu8E5vQf5AfJvgqBApI-m1WnBOSDcdRCtII_aGqTqsIZIwKwx1o3FHKsXne8A6aKQYVuElb9gH2gxUDLlBDJjbu3LarqqWwmPQJjJF8WPB7Y3XIzBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هلاکت ۲ عامل اصلی آشوب‌های دی‌ماه دره‌دراز کرمانشاه
🔹
۲ نفر از عناصر اصلی آشوب‌های دی‌ماه سال گذشته در منطقهٔ دره‌دراز کرمانشاه به نام‌های مجتبی ویسی و میثم ویسی، روز گذشته در درگیری با نیروهای حافظ امنیت به هلاکت رسیدند.
🔹
این ۲ نفر از عوامل اصلی اقدامات…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/farsna/438782" target="_blank">📅 15:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438781">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انهدام مهمات عمل‌نکردهٔ دشمن در بندرعباس
🔹
سپاه هرمزگان: عملیات خنثی‌سازی مهمات عمل‌نکردهٔ دشمن در بندرعباس از فردا به‌مدت ۳ روز آغاز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/farsna/438781" target="_blank">📅 15:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438780">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o84ozzuhr61Eh2hJ5XBAGGflTnF76dYuDdzyTzdMk6V8Mvzqj8v0Arngc5z6hjUOfUvc3zYJ46kH5ewUuGnip2uckgA-oea3cXZaddqPsdhSMQQJk2HixqNpkY2RLFHQz1AESKXbnp1fHpwGcPGwLloHen6TX81OPuB2lE2smsagaGI9iQAhhfMqwUESUR95omlU5cgYQ_72ORzRD_tt-XAecvRfuBn6bGoGXw6IjG9j1PoT4yWStOnW3CSm0689jWYV4R0FLr99OR61CO3cLAQY80zed--sFR-hBae7TWM2o5vDc0z2AVq40JpzgTpuqQgrshP7p0k1zGkxhJNQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در پیامی قهرمانی تیم پسران کشتی فرنگی نوجوانان در آسیا و تیم بانوان در مسابقات والیبال آسیای مرکزی را تبریک گفت.
@Farsna</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/438780" target="_blank">📅 15:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438779">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5144346269.mp4?token=HK-1qWwQ8Q0CgTqge6EOAPEYqPS1lGaUvN7xGhELQplZaGMDjPqgmtPb8qCyHbwehEgvOU3nYyaKV9Qzkh1A40OddKuTXs22utGm7WIo7klYoys1GbDw3Kmayrl6Vfiw2hl2YlsoCshh9ik0lnyQmyVm1iDUfRxBuVHYob58lyoR3E2eKSxDB4F_GIqii3eHwhBxwH4XU4cHut67kIqw11tcILYEq73hGdLuUgKYRj38kCRQ_fGKjPvogiYipfQDVoSZN8vUsyrnJ8DkDEWR30oFgmWs5QglPgUDQ_rsDo7pqM5GEYE7oe-825Dtr9EZwbfJ7wHFcJDcBsFDbqKllA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5144346269.mp4?token=HK-1qWwQ8Q0CgTqge6EOAPEYqPS1lGaUvN7xGhELQplZaGMDjPqgmtPb8qCyHbwehEgvOU3nYyaKV9Qzkh1A40OddKuTXs22utGm7WIo7klYoys1GbDw3Kmayrl6Vfiw2hl2YlsoCshh9ik0lnyQmyVm1iDUfRxBuVHYob58lyoR3E2eKSxDB4F_GIqii3eHwhBxwH4XU4cHut67kIqw11tcILYEq73hGdLuUgKYRj38kCRQ_fGKjPvogiYipfQDVoSZN8vUsyrnJ8DkDEWR30oFgmWs5QglPgUDQ_rsDo7pqM5GEYE7oe-825Dtr9EZwbfJ7wHFcJDcBsFDbqKllA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از فروش برنج خارجی در کیسه‌های ایرانی تا فروش برنج‌های معمولی در کیسه‌های برنج مرغوب
@Farsna</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/438779" target="_blank">📅 14:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438778">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eff7c2ccd.mp4?token=OgxmX_GdLa3hg4pRuujiR_YNdQXO4ht3SshR_J6sxlE0-TxuMZPSoa6pERLZqVhe2a_HMcQ1Eki8VM5uD6pQO_MUmd-R-44rr8AkTGPzAeJxnaO-D8w0SCiIdr5tgOtswFmY7xs6vKgzHkFwirPD87nwbArB4K3rQ5hOlxPkLu4Ro3AccEVN_CxqFsZiDBt9fx8H1z3EV4iE6XeDe4bzlWWbDAB3DmaKcwxsAeXtyIelONOSjMFWmV5mapgQnYyiDTDSBfT62zDpZ8iElq8l8B8uACBpubB8e3ekvJb9NzUyDilYfKHpAAG5mrkDa1ZdhEf9HO0Jz2qExGuO9y9v0IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eff7c2ccd.mp4?token=OgxmX_GdLa3hg4pRuujiR_YNdQXO4ht3SshR_J6sxlE0-TxuMZPSoa6pERLZqVhe2a_HMcQ1Eki8VM5uD6pQO_MUmd-R-44rr8AkTGPzAeJxnaO-D8w0SCiIdr5tgOtswFmY7xs6vKgzHkFwirPD87nwbArB4K3rQ5hOlxPkLu4Ro3AccEVN_CxqFsZiDBt9fx8H1z3EV4iE6XeDe4bzlWWbDAB3DmaKcwxsAeXtyIelONOSjMFWmV5mapgQnYyiDTDSBfT62zDpZ8iElq8l8B8uACBpubB8e3ekvJb9NzUyDilYfKHpAAG5mrkDa1ZdhEf9HO0Jz2qExGuO9y9v0IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وام ودیعهٔ مسکن از اجاره‌بها جاماند
🔹
با وجود افزایش چشم‌گیر اجاره‌بها در کشور از ۵۰ تا ۷۰ درصد، دولت سقف وام ودیعهٔ مسکن را حدود ۳۳ درصد افزایش داده و خبر می‌رسد که سقف تسهیلات فعلاً تغییری نمی‌یابد.
🔹
امسال سقف وام ودیعه‌‌ مسکن در تهران ۳۶۵ میلیون، مراکز…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/438778" target="_blank">📅 14:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438777">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g38snRLO5ENNz1CXoxdD-snM-0h4qa6iLIfCAmTU5DTnXoEqS506tYfivN3U-NBNIYPCuYWpr8YexCdoTyT4BnJ_YYxlFU4eRNxXcPqNExSECG6fzF8-CLUQwuKxWl0AfkQ0j1z7I52BiehPO8TPm-UWcd0Mx4BeKmBqMGkTsyH22VCEhvEyhBhivFMDljRtiGph2N6zxUmflTseidOqp0RpsJf6yduGlfywQrvdRBefphADC5VGTDF3wqjk5J3vPhmT09ctvz2wBm9kFRaH-gY1aEg3-lchFzia6RIJ1GIBM-OBEu3MX254WA6cZwYLQ4J9KfVXqjQr4PO5hFCGpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚙
حمایت از دانش‌بنیان‌ها در صدر برنامه‌های بانک صادرات ایران / اهمیت سرمایه‌گذاری هدفمند و بلندمدت در پروژه‌های زیست محیطی
🔹
در جریان بازدید قربان اسکندری، سرپرست بانک صادرات ایران از شرکت دانش‌بنیان ایران‌دلکو، بر ضرورت سرمایه‌گذاری بلندمدت و هدفمند در پروژه‌های زیست‌محیطی و فناوری‌های سبز با هدف ارتقای کیفیت زندگی شهروندان و توسعه پایدار تأکید شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/438777" target="_blank">📅 14:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438771">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Py0SE3RVIAJAeLOdQRa8vUmbIyESgEfQWPVCovEGfE979qMw-C4CGrz_RIsTlwineQVlyt6UH9wW8FOYHFOrU17wSL13XhB2yJ5HPIimkCRdYoNNNK6NREvZ3c3bXZmXw1jzkhFGycczoYUTarVrkeSzvAWmn3FyH-zlrZjg0Mq0cLdEblFgZZMHhefi2749PvhEZNtlx1zCYAuOrfXEFnV1Ih6EydR4PEeFLrmUcHRovrAbZ0yt5vrxt2zKth-Vlm4IAnxegv_y9bqpNacLxH45nA1BZ1AahrrifJ972MBQVk6P0mddNfl8z--JIG6ELTa4VU0jY45SmpRKTn6NPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ND2K9hQxFzytj8BOAVTMb9zkB2H8gKBP7RQg3Gwi6t8gZl5twsWzphHgGg4QwmhTkCev9T6IKMv3LOJJebTYi3X6QY0s7YPpEOmuvOy3ffn2RJtGk2Tc0yBbxeahajJlmk12w2R0PbZWAkix4NoiMR70yVwb9oGfaPsI2FmPcFL0ZiGFaO5QyHtAjUE3go16rqVH5AI7a5zYyi_BCp1iP6hxlZEEhjsJBCGoaVWPQcEuWj9SQS6I0AcXsySWUTju7VJetKdQ-b3B195h7e-dhAiQepUp1UEbXUXCls9e5jMvPsLg5Fk350DZdUHMiBwojZWBWgaDXflR_fHXIYgVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RhmiNA3AbPtiOxgVETyJNyMLj-s6cB-6PKB3LOrOYxzRIJtl7qiCesZ6hKfCZ7a6r2iwKje3aw75LbIFVpovX8ygCi07Vsp-KVF1-bLXT5KAFFQYxNzYuFoibLD40VyfXDmuFd9uSvH5OBwtEYeSD-xxf5Aisa-TF7fRsYvX3x1e2StNR2Psb8fB4opvX6dTAknt0InoHTjCC2GqORMceH9jpU7tFW-cWOo2D7jzQGFM_DOaidHYXExGQCcsHA56p6kKqIUNCsLCEj66LKuC_3_uPHmdrr3fl7B05sNk4r0lLxXpjdFfsjM70THCIWTB8DHrk6BTCfJDaT_vRH8nkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ug4kZ9FjEhP1R4WUOcqdEXvFBvjMDING_bGJc3XMa4HDNEU1eB0fTW2LEUY8L5qPN4qkC2vgamOT0TJz8ffBpzzcsjUAVNYMNdnNPx9HTVOJcbei_V1GxTHIlvx7DJGOAGmSIVT6mMMs14LKNgcHC3DzYnsGOiCw929wDFF8HeWcXCktsKh_mOTmgWRZw7cOQ56bOG20KINPr076N9YTpmW4BijSiH7Wt4En_2AA3eWccNp8SeDamVm3xm_vhZntt6LfuAcRy4vGikfQEUapfKg5DsC_uqmACtE62IzQ-IKz-KNQYzOSp2Mq5ugNBYevwnl7AGh0Hg_1Ao4O5EgFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4IkD45MVNx_TEl92H9BM9WXmI7TJ3QPxV0yeyYDf2N3iGNh_1x_ZuuYoF62ltbJzaQm7qPIOBQd820Vofb2-bGF5xjXNjo4yklyc2XqDP-RcSaYmg5Fy1c9blrXhBj5F1gmUvt3oXhmg14oLO7z2aPcqhNsgljZ07ygDwkKTu4Yefg9e9Mg1Yg7CzUMkL5jkXsikt1R2fU3LTVyJT8DCLN_uOnAdLAFviNr6u5OsVfAGDVKUOJJimvDpzRMSBgMeraq7FFAwaSH_taKPy_LSI7Z9kcumE45il4YPWBcRfGiNympz3w1x09iUBMrp5pGEUgldE3ao9LEqLrQxlOQzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKvzkwT25gr0euUja-lZzB5gLDoiT3SWGCvxznQ38cHzzSrrm7jt6LPXfqN69VzRMeV-Ci9YtiXAq1yLiAUW4pXM9IeKQbpqWT0zvXLGqGAXfTtPKq9clZ-TWwOs4nzH2saUL4jtqNj1fKuPLxEy_t3mHbMJk6derAA3tiGgwr2ZxCZAn25SMZxrmSLyNwtVltLSnGBk6uxHJi_mYAH2PWMNfppXL0sr7YYJn0mNzoHh2eT4o2OsFlMViyIlVYDoDf97lZS3voNG2Us8QIs51OvsG_wUGf-DWiapfrzgI45Zemnhv6NBbiNe857s-TLrsjsHs231m_ySOwvuspsNBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#گزارش_تصویری
🔰
بازدید مدیرعامل شرکت ملی مس از مجتمع مس سرچشمه
🔻
دکتر سیدمصطفی فیض، مدیرعامل شرکت ملی صنایع مس ایران، امروز جمعه هشتم خردادماه با حضور در مجتمع‌ مس سرچشمه، آخرین وضعیت تولید، پروژه‌های توسعه‌ای و طرح‌های زیرساختی این مجتمع را از نزدیک بررسی کرد.
لینک خبر در مس‌پرس؛
mespress.ir/x6QT
◀️
شرکت ملی صنایع مس ایران را در شبکه‌های اجتماعی دنبال کنید:
👇
|
بله
|
اینستاگرام
|
ایتا
|
سروش
@mespress_ir</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/438771" target="_blank">📅 14:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438770">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/farsna/438770" target="_blank">📅 14:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438769">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">توقیف
اموال ۷۴ خائن به وطن ساکن خارج از کشور در گلستان
🔹
دادگستری گلستان: اموال ۷۴ نفر از خائنین به وطن و افراد تاثیرگذار در شبکهٔ همکاران دشمن که ساکن خارج از کشور هستند به نفع مردم توقیف شد؛ اموال توقیف‌شدهٔ این افراد شامل حساب‌های بانکی، خودرو و املاک ثبتی است.
🔹
همهٔ دارایی‌ها و حساب‌های این افراد توقیف شده و هرگونه نقل‌وانتقال مالی برای آن‌ها ممنوع و پروندهٔ آن‌ها در دادسرای مرکز استان درحال رسیدگی است.
@Farsna</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/438769" target="_blank">📅 14:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438768">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc124551.mp4?token=vfg-LO-liRk-S8VG_me9bQsDiXokMWKxEdRbwknQEsa0NjwcAfJL72ntbLsr0xz2D3fus3vn--qWoztziNdZ5ls2mK3hGgGGevTjCfKh2YprmkQN03t2LogFJUYvkNX6IWNICG_cc48wgkEVMYqiWEzLsk37N8qfsX29DG-wsK-T3Pai2jHR7v-4jAozJD0Qh_6m6YHLezPMXvLJTGsH4OXieiJcQyeZroDSkyzgY6TAJTBgOzU27MSUW7vDy2hYwFi2t34Mks3Geo36g5zMWsfnPLNsk21D_UBYmj-nGs3OVng1D7S5LC4ioM7CCMX2ukHxHwTiSRRoWX0OfDXYeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc124551.mp4?token=vfg-LO-liRk-S8VG_me9bQsDiXokMWKxEdRbwknQEsa0NjwcAfJL72ntbLsr0xz2D3fus3vn--qWoztziNdZ5ls2mK3hGgGGevTjCfKh2YprmkQN03t2LogFJUYvkNX6IWNICG_cc48wgkEVMYqiWEzLsk37N8qfsX29DG-wsK-T3Pai2jHR7v-4jAozJD0Qh_6m6YHLezPMXvLJTGsH4OXieiJcQyeZroDSkyzgY6TAJTBgOzU27MSUW7vDy2hYwFi2t34Mks3Geo36g5zMWsfnPLNsk21D_UBYmj-nGs3OVng1D7S5LC4ioM7CCMX2ukHxHwTiSRRoWX0OfDXYeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در شبانه‌روز گذشته ۲۰ کشتی با هماهنگی نیروی دریایی سپاه از تنگۀ هرمز  عبور کردند.
@Farsna</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/438768" target="_blank">📅 14:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438767">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/157ceae8cb.mp4?token=ncU_dNZxLSt_KmVx2CmW6VzG8rnB1BDXcZ7tFahQA6sVIAGMcFRRaWdI0-0N9vQ-nYnAcLZXuPuS7EurAxa2I4HdJqbGspV9xgKP4-9QoO9fGf-ogbc615gWT7SdWkKdqoeU-_K5QX40Yp2JJUDD8ZoRk8PbcSt1mCE7-r9EwIh1l-Mzke4FM35SWQ5lF1hg6xur5g9P8gor1AGppBJLAXF7dpyZwfsccfYHluPK6UBuUT4aDQC7hfhemRyet8SzvsvOu-QVqh5ojpOPZap9ZT9i09Bv9CHKPNZdVYeFrng2WoIh1lhfSPfqJP_JchTBWFtLklf_X8Y3bxeb5MBSlYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/157ceae8cb.mp4?token=ncU_dNZxLSt_KmVx2CmW6VzG8rnB1BDXcZ7tFahQA6sVIAGMcFRRaWdI0-0N9vQ-nYnAcLZXuPuS7EurAxa2I4HdJqbGspV9xgKP4-9QoO9fGf-ogbc615gWT7SdWkKdqoeU-_K5QX40Yp2JJUDD8ZoRk8PbcSt1mCE7-r9EwIh1l-Mzke4FM35SWQ5lF1hg6xur5g9P8gor1AGppBJLAXF7dpyZwfsccfYHluPK6UBuUT4aDQC7hfhemRyet8SzvsvOu-QVqh5ojpOPZap9ZT9i09Bv9CHKPNZdVYeFrng2WoIh1lhfSPfqJP_JchTBWFtLklf_X8Y3bxeb5MBSlYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرکاواهای اسرائیلی هنوز هم از حملات ابابیل حزب‌الله امان ندارند
@Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/438767" target="_blank">📅 14:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438766">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">امحای مهمات عمل‌نکرده در سنندج به‌مدت یک هفته
🔹
استانداری کردستان: امحای مهمات عمل‌نکرده از فردا به‌مدت یک هفته در سنندج آغاز خواهد شد؛ مردم نگران صدای ناشی از انفجارهای این عملیات‌ها نباشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/438766" target="_blank">📅 14:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438763">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مجلس فردا میزبان‌ وزیر راه خواهد بود
🔹
سخنگوی هیئت‌رئیسۀ مجلس: یکشنبه نشست وبیناری مجلس با حضور وزیر راه و شهرسازی با محوریت بازسازی اماکن خسارت‌دیدۀ ناشی از جنگ تحمیلی سوم برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/438763" target="_blank">📅 13:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438762">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxAxmgB5tKvVZnD_1qO9kwpSVX_CJaqO-H3JkRmf5F0wuopd82Vx-an1mdEy4rR22nB4FanjGWWglJ79BZLha1v949nvF3UD3AbZRp4-raoZrLF51r-7MNsnxD-_RyMZ0C5Z17VuJ9v5uJueA-veSL0xF8sCNfc6YECCMqIKaoGtQB37II186OdDsO8hvnh6xPQIB2TbsMNU-BCysWI8d-33brlQw5uD9UQy3Ouhrot0wdovT2cxM5hHtilPmjAoH4cD6N1Nzcz1Qda1mG8YrfIfwnkvgoOwlvSKc5Gazz74Yi7alMPTuj5hTdV5_ufTbmDMiM4aDCwlN8_uI5VAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقیف ۲۳ تن مرغ منجمد تاریخ‌گذشته در اهواز
🔹
دامپزشکی اهواز: در بازرسی از یک سردخانهٔ نگهداری فرآورده‌های خام دامی ۲۳ تن مرغ منجمد تاریخ‌گذشته کشف و از چرخهٔ توزیع خارج شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/438762" target="_blank">📅 13:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438761">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyZd4ibbMJTzhjQMFEfoqMbrJADQAUPYbHWLSu7Nv9G5_NrSzsiDmUWezViDoaEiSI6fj7eAARnXbZYlJrt9PMlgWwPLsB0Ujmmt9_BuCHyavFNY8vJrv7afRav24FMnmtmZh_OInZEhepQzpZcsXVryv6tfBggsS0R071powqOBU_jNNdWQn1Q0wRc1OkVlyeZoLU8_--L6K1nMjybTvYSxM5WiCJtl9nPTtyaU9Cm72-CwuGzxDnHfOhwkx2v2tpVaN18vm55eEN9-kt331pSGXAh2d_7o-1IHYuLUatGFTPwwgclsO_gWPhrv_7ztVvJteUjJRfzGrt6rvXIhOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول‌هفتهٔ تماماً سبز بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۸۰ هزار واحدی به ۴ میلیون و ۱۵۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/438761" target="_blank">📅 13:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438760">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8stocrsLTS8ByM_PB1q8hzlfI2L3zj7DcRn7U-GKfgAsFkrbp80dqfqiFExl7Pe3Yu8xlYUfnHvlFZANQ8Jv3S4UKMdYon6xLViaTBZUQItjxq-kx2nTKPkQdpnxfWklrEN9sJsSLQAfHmiKpfBn7-T5X_7kp2v3klcz546y-IMBfzg6ka5tSlqf7FkQ28hPf-fOaGe2Hm0gAjxbYHGTnGyUmYEH77CT4OTJR37nIG_alVnKZngdqJEFGx3kQTrHZfiDaZxHR_ooQLXQPvSX3YwfEpUx46XTD0Mc11dgsiiRHXkgHD8hnIkKGXIb7KEoLoYjuRfDJIj6oJcIi4Z1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران با دور زدن آمریکا سوژۀ اول جام‌جهانی شد
🔹
بعد از اعلام مهدی تاج برای انتقال کمپ تیم‌ملی ایران از آمریکا به مکزیک با موافقت فیفا، این خبر امروز در رسانه‌های معتبر جهان به سوژۀ اول جام‌جهانی و بمب خبری تبدیل شد.
🔸
خبرگزاری AP این اقدام ایران را دور زدن…</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/438760" target="_blank">📅 12:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438759">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVZSrvlc_sUSjFxAk5j1ayR-5AcajwCflQ3Nad2ahB-_3MsrSQfP0vSxV7GXaK4q7fucW0lZ7bX8Wog4h65KL-Kw9k0GhN24CMmWYtaO680N4GQaDTgxN0TSbdrGfrgbtKYfr737W_ExattSM2IOMLy3gj8Z0H01gb_H7jyT6TlV9FRG2XSAQ-sZSEp3qofXlAy1wbquxByPaUZxC8F7BROiFKHNkBcUxE_vpIxCr6VwOwmg1FDwBCuwf9u5kq3i4aUu5GxzdqSZO8MvyrYWHCDj4zhx1R040pgdfCU4rTgaR_wFp37R21f9jj7gTUUQLiCGH00uXHIq2Ogv8fWi3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پهپادها دوباره فرودگاه مونیخ را تعطیل کردند
🔹
برای دومین بار در کمتر از ۲۴ ساعت، دیشب مشاهده پهپادهای ناشناس موجب تعطیلی چند ساعتۀ فرودگاه مونیخ شد.
🔹
پلیس آلمان تأیید کرده هم‌زمان ۲ پهپاد در نزدیکی باندهای شمالی و جنوبی دیده شده‌اند و به سرعت محل را ترک کرده‌اند.…</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/438759" target="_blank">📅 12:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438758">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmcQdenirc8V2ll7yFb4Eje8wRZ_1h-4ZTyrjxeRWaXQdmLfsaAJkLS04g3zwiqLHPx-BkKfd-dlzEcxvDwhOw4rqbdFs80QG_D1q82toJqep_zRQPwjPZPVbR6-e3qxQf2Bhaht1X_PGfYiIbQCQR7m6sShrGuXU2FVKrYlxdFkO6agDqhgEZ2UVl0pQRdan-PYokajMPcF15rkkbMMZqPJLBET0K1QWFAjPf-MyOKu8OnCaifbxUx-8gXCxLAhwRU8YKVRrEugKmWzLGfVqjmGHGTlE7mjZMN6w5EUFXh0NZBMoYIele5ufq8VxfFTEs8FUR8pwq8AUuOi4HPcvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۷۳۱ تن آهن‌آلات احتکارشده در یزد
🔹
فرمانده انتظامی یزد: درپی بازرسی از یک انبار در حاشیهٔ شهر، ۷۳۱ تن آهن‌آلات احتکاری به‌ارزش ۸۰ میلیارد تومان کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/438758" target="_blank">📅 12:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438757">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجار کنترل‌شدهٔ مهمات عمل‌نکرده در بندرلنگه
🔹
معاون امنیتی فرمانداری بندرلنگه: به‌دلیل خنثی‌سازی مهمات عمل‌نکردهٔ دشمن تا ساعت ۱۷ امروز، احتمال شنیدن صدای انفجار وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/438757" target="_blank">📅 12:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438756">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeMuY-xjOWtkrvH4MNgge8gn5wMjj9WuEWPIPeDin1BvLYLfg9a1zRGVARoiMKTH8aqLATN5qrrRVpylITnCc0tXOaMjzDeAuZKoBHmw0Vj1g_OCz_pSxI_cwV1gAdn-hrOiE_E8aLnQatM2ANcVGrNkSURElTxeDEwPr2IaKQIQimd9FtAzWki38I4cuRUu7gs15xChgF0b7YuyKTaOuvoF0ewh5qs5G-tRqQpLqI4_2cgJD7eKhKkuLhWHv6M-M_bseCmDlxKzaFVoJtEl4ReryMUENJr7iuv5WbqEjl0ms2hZjWahVO87fvCSLHhgbfGL1EbCLa_FgEI2wJzscQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
محسن رضایی: رئیس‌جمهور آمریکا برای بار سوم درحال خیانت به دیپلماسی است
@Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/438756" target="_blank">📅 12:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438755">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">توقیف
اموال ۳۴ عنصر خائن در خراسان‌جنوبی
🔹
دادگستری خراسان‌جنوبی: اموال ۳۴ عنصر حامی دشمن آمریکایی-صهیونی و خائن به کشور با دستور قضایی به نفع مردم توقیف شد.
🔹
تمامی اقدامات قانونی جهت شناسایی، توقیف اموال منقول و غیرمنقول و نیز حساب‌های بانکی این افراد انجام شده و تاکنون تعدادی ملک ثبتی و آپارتمان، خودروی سواری، حساب‌های بانکی و چند وسیلهٔ ارزشمند دیگر توقیف شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/438755" target="_blank">📅 11:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438754">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCv3ZQmgYChSsnnxzLqvpSpg_xcGi8yWJNap93iohh-USkyQFXOruTJOGxMpSWDyu8MaRalvbMsPVjNdb5t0aR2K7RbxvyF9tuv7pHVwKwlnC-KH6MdJN_rMc_omormwdIuebtTU6zqxXio0cno0YJ41NgtirkwQEQ-0WVu3yEflsUNNe02Sltu2QmTBdgTR_YKMdRs0S9o6UXb48_v98A7ClRmu-l_pcL8T_VzxvJ-APqdpQvJ2YJ1mOpBTUCUMHajVT7jPMS05zYF5j0KfVFa7u6OSkDnUFmUkJvBzEKXhso8TVPB0iG6-xXVUfYtP3z3i8WtRgpmsftnw9IgUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام پهپاد اوربیتر توسط نیروی پدافند ارتش در منطقه قشم
🔹
روابط‌عمومی ارتش: بامداد
امروز
یک فروند پهپاد «اوربیتر» دشمن متجاوز آمریکایی‌صهیونی با رهگیری و شلیک موفق سامانۀ‌ نیروی پدافند هوایی ارتش و تحت شبکه یکپارچه قرارگاه مشترک پدافند هوایی کشور، در منطقه قشم منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/438754" target="_blank">📅 11:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438753">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUpqN0BYYSy6X4fpRUb-X9YL6mSLMuzI48SjWFqNwvH5GQM4pZ1l9vJ6fJuemw0ntO1ykijSQ5c2m3CeWhhPxtWuhZIzG_47n3lS5KjlDo112DQ6cJQlfzcVpX_Nchn7o4fA5LN-_WrPnII86kiNBtFduDHCsPWgQ1c6ZiQ_kCF2cLE3-IKXKOmr9a7eR-wBPurnkiXS-npiP9-MmBLZK97g95FlzlF_iFNOFuiQFiZMCS418g6GPhyAjd1gw22lyxeyoYTdO3Y6p0rilDJ9ymKZV7RZUHgGgX0vpxcS5-HEH0mxfv5yNLVnqeBwm_8jy0o94k9pPWjYW7_sYndpAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی ایرانی با عبور از محاصرهٔ آمریکا
به خانه رسید
🔹
داده‌های ماهواره‌ای نشان ‌می‌دهد یک کشتی فله‌بر ایرانی به‌نام کامران با عبور از محاصرهٔ دریایی آمریکا به سواحل ایران در نزدیکی بندر امام خمینی(ره) رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/438753" target="_blank">📅 11:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438752">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCIzfB4aK9zziAzwUW-P_25PjeftBS5MKOVY0UebJwLs4yF3s3Onrmta7FY5PMMls9eC1SfoEsoxcEKdEputiXDnrBvu9IfvD2Lhm_Rl3sgTk0LVjz2kJ7QbU_9TaTyPFPbPF7h2LVd5MyHPf-3RExCjemetLsOtKfwSg0u14w5ckQsM_7mtLwd7B9JskJ5Kwb502Rgll8zWecg1uvBe8UP2IQvYYtol1fRQbEK8KnTO7D1v47MdWKceGHexhpOrym_ZwGDb298qX05DU9PL9SUX7JcyqytfNgP3u3e9GYsGGGOtVw24JsXAMClS1Gj-I3KUD7ojU_7p5qLD58tBGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارت سفر در راه است
🔹
مدیرکل توسعه گردشگری داخلی وزارت گردشگری: تا هفتهٔ آینده کارت‌های سفر در اختیار مردم قرار می‌گیرد.
🔹
مردم از طریق این کارت می‌توانند هزینه‌های سفر خود را در درازمدت به‌صورت اقساطی پرداخت کنند.
🔹
اعتبار این کارت‌ها براساس سابقه بانکی افراد و بدون سقف تعیین خواهد شد و سودی به آن تعلق نمی‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/438752" target="_blank">📅 11:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438751">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FY9p6CfWyS2gE-cI-AQ1lpwMw8yXZxakqA8HYGfISAsm0fZfiJ_1wcEF-o_suSnxh88mnyPlAPaEBnCDY5QOfo0FTssYBFxO5aO6CuVdQj9YxqtOEjOlBWO9GieNPGx5aQZaLKevrN8G1i5I2qhd40fWEFzdg8C14FJ4twzo1YKadsQOmJ6Kb66eOa2xqufL6W3TS1ucwCZozmzIMtm6qsMCaPyw3KeSDTDrvoLEJgkscS1Jz7TDfEB4xMaM9Dapt4y0aetYLwGIvjdjPtDKkrkQ5LkH8GCx6H8h5lKazq-5ZmxGVmL9ylyXRLz4FkzONcUeqxBWeXG2GrCYYD2TfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان جای خالی امارات را برای ایران پر کرد
🔹
پاکستان با کاهش تعرفه‌های بندر گوادر خود و پذیرش اولین کشتی تغییر مسیرداده ایران، تلاش دارد انحصار امارات بر ترانزیت ایران را برای همیشه بشکند.
🔹
این تصمیم درحالی عملی می‌شود که مسیرهای مرسوم واردات و صادرات ایران…</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/438751" target="_blank">📅 11:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438750">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5746a288c.mp4?token=uCoJfx9_9JAcCJ_dwXY_ohbFDfEtSa1XRdb8UIypDSnKlbd9LM7LUth4zRabh6hVJJi3SwEY6A9YJZcfq2HfhiFHd-SiyBNmSXRFA3Xr_sqDLZKfUp_vEjjQP3D37f2VvrDWGheIa505xS18VIGdf76BLvSyrZ-20rc2UMJOKKvYVAwG7tUU3Vn04IoJ5J5Id7VngPazjMrT1uLfTJbn6t-i86SSm1QD5o_R2kGGSBw2xKzKASE_1uVwQWUtXd0ZL_QNsjnspmoa6-28nAkBAZQ0WO0XITvM0mSIT8USOu5Xcl7cbaROhVrUgpr45BMMJrzcnav60c-hbTgpvfdKtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5746a288c.mp4?token=uCoJfx9_9JAcCJ_dwXY_ohbFDfEtSa1XRdb8UIypDSnKlbd9LM7LUth4zRabh6hVJJi3SwEY6A9YJZcfq2HfhiFHd-SiyBNmSXRFA3Xr_sqDLZKfUp_vEjjQP3D37f2VvrDWGheIa505xS18VIGdf76BLvSyrZ-20rc2UMJOKKvYVAwG7tUU3Vn04IoJ5J5Id7VngPazjMrT1uLfTJbn6t-i86SSm1QD5o_R2kGGSBw2xKzKASE_1uVwQWUtXd0ZL_QNsjnspmoa6-28nAkBAZQ0WO0XITvM0mSIT8USOu5Xcl7cbaROhVrUgpr45BMMJrzcnav60c-hbTgpvfdKtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی محمود کریمی در منزل مادر شهید مجید سیب‌سرخی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/438750" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438749">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUyEsvYYJ5j52BveoZ6vlp53CUpqfc_TD1xlCSE_uaqt3HvhyQKxQTdWwKCLKERiqMFN5KVwL5QmtoqPHcEGpqoYmncFzHlSjv3Jzsiecx8bTsvbDkWqsgIo5e_IH91G0eoOQPsyoMOjkUzEpfkVDmsVX__gOjwkS9tlmyz1_XRVTWlehShmj6-H5bkH2GGIjYetHKhpnt3TEltokjntg-XwpMATIqpFPbCAOMU3gzjjci_R5B5PXPZVhNaJTcFYAlRMtpkYwACjwhAZzc9i_kCMOrf4Whme9pUwlL_fM15fEwfGn4tigDxtSGW2xRnRRYmq5qT5ZMnyNi6Ml1ACog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهلت ثبت‌نام کنکور تمدید نمی‌شود
🔹
مشاور رئیس سازمان سنجش: مهلت نام‌نویسی کنکور امشب به پایان می‌رسد و این مهلت تمدید نمی‌شود.
🔹
داوطلبان برای ثبت‌نام باید تا پایان امروز به سایت سازمان سنجش مراجعه کنند و ثبت‌نام خود را انجام دهند. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438749" target="_blank">📅 10:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438747">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">زمان ثبت‌نام و برگزاری آزمون‌های دکتری و ارشد
🔹
سازمان سنجش: ثبت‌نام داوطلبان برای آزمون کارشناسی ارشد از ۱۶ آذر آغاز و تا ۲۲ آذر ادامه دارد. آزمون ۱۶ و ۱۷ اردیبهشت برگزار می‌شود.
🔹
ثبت‌نام داوطلبان برای شرکت در آزمون دکتری نیز از ۳ آبان آغاز و تا ۹ آبان ادامه…</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/438747" target="_blank">📅 10:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438740">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmE8MogJ0SWuHZKysj0XhyhF-hCUss7Y-VrCzF__rwwTtxYPN878Ce2Yl0y7nMWKB_80MFB8w3VmfaxiTvy0QSVXmo4u3XeMSLqYNOhBQHhkOrISTtqDYVMoPME2FtjmsOCKFuqiRzW-9JdjaUxFSOzJclbGJ9eYU97H1lHJIcCWGT1O-wmX2bmIK8gA5JxywCG5IfgXKiPdf_1Dxc_vLrauYZ_obkTMnMuasVHfM_ulJJj3q9-CnxEfq2Lo0TX2vbvxVIm3g7a2WRC30iVOBthdZNcoMtfem5G6AS7FUBi-79niLI6ZRud8FfQU_aN3Xci1M1rIlKl_34lnK4sQAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/agChAWKKIUWUEGi1-_7pOGCnUKGhyFUyyI2OyvM5rqsJTYwR_P2gVlIneJxYUsaPCHIXGuJP9CfFEVehdC1mo64d37gX_UnpM4veSUKC2RXZDz1FLnb5RXNCqSn7R6eRBFRoNWcSr9hHBiwPjd3BtBqKmVWzKhdTK2GF5OlV76IwBFdz4Dp86T2zb76LcwVWaSS2U80xnGjHsUWmQ3mgN0KvxjAyMCXt8-b4NGjkuQDoylFFsoiPBzGKKIyTkDirQxHoQ0syKcGCbpL2L_zXLN0iFBtQrz83Hx7nyMlA2So3u7jg2Yj4p4rUTwS_VYeizgBihGjMvzCSWD-A6b3TKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jqdf2FirN11xaJQHQqJj7LeEfG9hpzDNcO8B03PlRS0Buq1YSdVdDzBoZMfNv9m85z2GhpaObFVwfPz5hE54L-rxVSw5DsB8ymRg0qNLfLSjXyMYqJEo89S9MnL0NLTw7oK6V4AGDGKAtHeRKHnvb7oIcIBWddlb-2TCyjIvKF51MTHqof_fXmia5c2xSHSfSeGvg4S-LNFjDgEqdVJLeOKHO9SVt9ZJoJNW0RnZpUat-wO5KJ8CsQmOWNqdjI3xR7KvFxknNSk-x3QvKnCTqAGOODn_PR7ctQU58AheMJRT4nmTODwgicyM7kEFqKuZ15Fo5p5UA9QLEzBeN9lPOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riIDh9-8x8buivv9g9fGxh-JpZ_MI_xdbqLwVQsqsOcP7l8psv1YCQSec1yBy94m2HLKJmksYkzR5kl5HF-EGmOIQmUd11gzUPfN64hO2i2wedsEbmw_ERdBflwUQBhbm6K2lGfyuQB3DbFr0M8I5tr6lSYs-hu_AUKlkSuF3YIUHQHA_Y7FtJeEc9mWME3Ir8oYCyFATz8v9MWOwZa2kVlSO7enaZ3X01ppWWtxZodkCdF0_nVITP87w0gW_DSSsoMNE39AjDOTtLzdy2uTF-58TV6Vl2kbthNVKsduzGj39Tp5g4jj4fcW5LG2s-KKQcxj1VhP8BmldvXYJIcgqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqKBEWcCGNU4H3vIKIXGSXvKTS13z3Sd3MM5F24PUV-ERJ5odWvnL3SDeTOEjkGhd-0zHcGkoSKKHm35q3SUBqMwfcDWQJAWl9Hy5rJNZr0IhCHi-EJAziaBaImXk6TUIoE5Vond2a8VQSY99pDxDjtv9O-dMR_uxODQpn10CCOiI4Cw_SHGWLxvQg7vScd7iydO9tMiK06CF-NZXAo9hHKFYBLRyQLqGgw87mGzlsZyoC7L2n8lzO69Cp08MazO2LlxbtTW2f9tgtbXcCOZOIY1tj2Q-sQ6h-YH61KxuxAQhNb8-xDVGZTxRkQh_FzS-oPd2Vwtfs04Wx76gicqCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GapsgjkoYvN5WJb-GZqVf0Br_cFW-zAv0hjJv4dXXSuDv8HV_6jb3w7cXQpXShzLnzRIvtDwH5_XHBnbLuWi_uZPbuiwfXD3k3KDU6yjGZeKv-molymknp2sP6HfITcCRGZcXNZwPYV5rp2hsQ8Dnaugh-WEdCPNiAX0NWcwU5qGuo_zyuZwZ2LumlcXsfzs_9Ww8FiqrRLf7gtZu_1jlcqMK8D3Xc2L8xB1B2oNaACbF0lJxyKvvX4gY9k_1wkilHLW8A7x_NEDDQV03sKICdLJO8lp8jTLzvkp9sKjYi30VuXnzz4p4iLtT2OcNgoGH-qIiCI5flxsnRvn6DvTgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLcldDvp1T22nhKdTaYsy03n_yghhI1ypH8TX5A2iwMdeykRAGHQdyk4tko-pwUhTKC7knpp0VDYqGhRkjLj1mA6-WzyQaUwJXXTrfP-yyuRWsKJ-vegKMtxKe7s5QJ4vzL0dxZjzBKaTtKu2LW207mR2sOIfmX_bEVIh7l5LlfLALpY7P-2E2niWl9XMhKYA_7VkOpcmUcZhmkVIJVhd7cvYooBKht_CUTiK26rAMcm3_qzS3rvlLJc8D2Yal_b9DO9izzhDSNb86kRQlGIjxuIQq6XewPmyZ3KqwXiM1-h2jQRadwqwG_xG_E_c1PSZ0cmHhEOKW8Z2r96AA2P-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نبض توسعه در جوار حرم سیدالشهدا(ع)
🔹
پروژهٔ عظیم صحن حضرت زینب(س) در جوار حرم امام حسین(ع) با تلاش شبانه‌روزی کارگران و مهندسان، از جمله معماران ایرانی، درحال پیشروی است؛ طرحی بزرگ در توسعهٔ عتبات‌عالیات که در آینده میزبان میلیون‌ها زائر خواهد بود.
عکس:
امیرحسین ‌رستم‌زاده
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/438740" target="_blank">📅 10:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438739">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">احتمال شنیدن صدای انفجار کنترل‌شده در اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده تا ساعت ۱۴ امروز در جنوب اصفهان، احتمال شنیدن صدای انفجار در این منطقه وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/438739" target="_blank">📅 10:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438738">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lirSboOxXpLt5lm3mX-rzZ3kRTkp_Lsq9pIsCHDiElv53IlhEMaPfPcZwG472yuWTKhU1xiUF52HoOAX80yiQsrSjPhT1_VJ3mgC2FGFRtLE7py_zIyBoQaWS5AmQensE5_2zGuhkco9t7RyGNksrEzMtIvuX_bovgseQ-K0fftO2lwRk7Hqg4PoQvZJhKO8DnplVFO8wWsTJuinEZ5TzfwbQXURnH7MeMauZKJ_ZbBbP-yec-hstaqQ-oPyzVytapz7vh9G9DJBfixCG_fyd99QSUwVxjWCGbuksA-RT4TbyTZk5aSHNl-m4stvrcn7NxlqKuGaTrIvd-rpgvY2IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپاه یک پایگاه هوایی آمریکایی را هدف قرار داد
🔹
سپاه پاسداران: به‌دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه‌ای در حاشیۀ فرودگاه بندرعباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی به عنوان مبدأ تجاوز، در ساعت ۴:۵۰ دقیقه هدف قرار گرفت.
🔹
این پاسخ…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/438738" target="_blank">📅 10:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438737">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bf7dd4b5a.mp4?token=vtgtSWsk9e-U2me3ae1r1JIm9I8zeTyKX-EMQo4MGxlecpysjL6g-rOAsca6suBu4BogPDVbUL1WDT9XyhmpyOnxLiZ0cN02g6opsSiTOcxuxqoEyAM71kGIaYhGe5lmZjY8OGAxYYtGXe4CXoMsS6H8zxcd0Ft6HyQSPnAfr4mMAgadsBkO8lXls66TT5aeJiefrApQ42PmpRb0iCDI7yea5yP0nAYcwLXu9-yG-w7OOEIfVErQEwzLsk1sdk9XKtSMkY9VQLueoHiMNWRJv0rCDzt_jkJZRD2tkcQTGVwfrAM8VpZX3NZtOE6790yxwxT1aKe28zz-vBMrZTIj5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bf7dd4b5a.mp4?token=vtgtSWsk9e-U2me3ae1r1JIm9I8zeTyKX-EMQo4MGxlecpysjL6g-rOAsca6suBu4BogPDVbUL1WDT9XyhmpyOnxLiZ0cN02g6opsSiTOcxuxqoEyAM71kGIaYhGe5lmZjY8OGAxYYtGXe4CXoMsS6H8zxcd0Ft6HyQSPnAfr4mMAgadsBkO8lXls66TT5aeJiefrApQ42PmpRb0iCDI7yea5yP0nAYcwLXu9-yG-w7OOEIfVErQEwzLsk1sdk9XKtSMkY9VQLueoHiMNWRJv0rCDzt_jkJZRD2tkcQTGVwfrAM8VpZX3NZtOE6790yxwxT1aKe28zz-vBMrZTIj5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده نیروی زمینی سپاه: شهید پاکپور معمار امنیت پایدار بود و شبانه‌روزی برای امنیت مردم تلاش می‌کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/438737" target="_blank">📅 09:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438736">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtgfpJRDBDiANDv9o3EBakybGuZqVd5Ld5bLRFdgum5Q9eV51vxke3kYW4NctkZJ3qyJGgUN4t4hWn1D9tX7yVeOdmy2A5q-w0xA0YUvTmMtkV9m2qJ1jfCMF5nDi72XJosS2EqkuzgNDP-EliCKLuoTsGYM5647XR10sZ6X2_mf6YNKA_cKWpPZtR4vOYpUlW6tn8XCOOhwRHQeaFSO8flIt3C-mrjWJX-P0ucg8qVNUF-odmx_Vet2ebL5Zym0WCiz4vdhJDmsR7u8CZ6q3OV5aJcZZOmmOJJh2Q3imc0YR10ND5kd4DMItLyrV5Ki04Q55dzt1qvWVNpxWqnliw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه ویژه کاپیتان پرسپولیس به مجروح مدرسه میناب
🔹
محمد شرفی از دانش‌آموزان مدرسه میناب در جریان حمله به این مدرسه دچار سوختگی و جراحات شدید شد. این دانش‌آموز در این واقعه، خواهر خود که از محصلان همان مدرسه بود و همچنین خاله‌اش را که به‌عنوان معلم فعالیت می‌کرد،…</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/438736" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438735">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNWlFYztNYiTrBkdE2q9ORDbV_eXsoRiG_FDGGgdN0aA8cnjXOy8YFM_exLdbkugz7KKuG0fBdSUzoIWHrYR7e58x1R42Cs0Hi7krsgApb3Pq_ggNWjBL7aZM3nrljd_5qsaeCsiQNt0VpvKUUHwhyZNWZdDpfVHLapBNKFqY5Dv5NxQJwnQu-j-fuosqmJOCuTS131PNNa6qR7vF5uwzy2KqCA-mLHCL0vnfMGmfxO8d-J5z0gOXSCTaHjW-qxpVH6M6n_lq-ATVOy0CkWwnP1ctcL0hwReUy-2Dyrki4gesUfi48erTOjopsPRRy0vgAG8HNtQtWyVUWqBVaaI-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامهٔ تلفات خاموش تنها پستاندار دریای خزر
🔹
در روند پایش‌های ساحلی مازندران مأموران یگان حفاظت محیط‌زیست ۴ لاشهٔ فوک خزری را در محدودهٔ بابلسر و میانکاله پیدا کردند.
🔹
طی ماه‌های قبل شاهد روند افزایشی لاشهٔ فک‌های خزری در سواحل دریای خزر بودیم که مدتی متوقف شد و این روزها باز هم شاهد افزایش لاشهٔ فک‌ها در سواحل دریای خزر هستیم.
🔹
فک خزری جز گونه‌های در معرض انقراض است که در فهرست سرخ اتحادیهٔ جهانی حفاظت از طبیعت ثبت شده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/438735" target="_blank">📅 09:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438734">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfdWaIulayzOGRNQ6Wruv4MzTlmHHCR32X56gFVYTpBJYIME5kfNJ0Zo7AWIlasjj5SQzoi6RNIk8lEvHhDPYUmYreS_IusFsd_lXG-wspHiYldPqyUHgS9kJipfBON6DBMNEec5i82yd-zPPZnTvTlDzn6BpUV16dWUcPZ6Zaz5VZ0_A9R-Pti6S2zCyoXImYNbJOdV2gHto6o1D2vkyIjUtBWEXRVt0G89OUJaq7sI81BukIABx2-h0I9To4n3422OfddkVlBQgzagwxaxtGrwHrb1zYEyEwDXAG5mGn2c2kfzmEgyRLWOC4PwdaslTNRoRGtrei__ab2zoTn-MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعمیرات نیروگاه‌ها، پاشنه‌آشیل خاموشی‌ها
🔹
تا ۹ خرداد امسال پروژهٔ تعمیرات نیروگاهی برای تابستان ۱۴۰۵، ۹۷ درصد پیشرفت دارد.
🔹
تعمیرات نیروگاهی طبق رویهٔ سال‌های گذشته باید نهایتاً تا ۱۵ اردیبهشت هر سال به اتمام برسد.
🔹
کل تعمیرات نیروگاهی در بخش واحدهای حرارتی ۱۰۵ هزار مگاوات است و هم‌اکنون بیش از ۳ هزار مگاوات از واحدهای نیروگاهی به‌دلیل تأخیر در پروژهٔ تعمیرات در دسترس شبکه برای تولید برق نیستند.
🔹
میزان ناترازی برق در خردادماه و پس از شروع گرمای هوا حدود ۲ هزار مگاوات است، رقمی که به‌اذعان کارشناسان در صورت تعمیر به‌هنگام نیروگاه‌ها در این برههٔ زمانی به صفر می‌رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/438734" target="_blank">📅 09:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438733">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">۲۲ عملیات حزب‌الله علیه ارتش رژیم‌صهیونیستی در جنوب لبنان
🔹
حزب‌الله: نیروهای مقاومت اسلامی در ۲۴ ساعت گذشته در پاسخ به نقض آتش‌بس از سوی اسرائیل، حملات به غیرنظامیان و تخریب خانه‌ها و روستاهای جنوب لبنان، ۲۲ عملیات نظامی علیه مواضع و تجهیزات ارتش اسرائیل…</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/438733" target="_blank">📅 08:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438732">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8cf218009.mp4?token=VOgimyJUxHoEiJSWFHeVPOKfvC2rpxpOqqU966wmvjV_mJJdyLW5c53CSWQL0DNiWQM86vzDYFyltd1b7J9UPDp0WyPR5cQoIKgs3jujYb7YHyhWT1s0PPz5RlwmKsd19MCkhbkP5ctYj-jQ8kvwpUCBVsuU_2eqQ07aXlfBr4VFAA0f63C99JAhloUddyFXM7D7MnPW-MIwJg40v7-2HgopdZMReznDPBBc3_5q0cbLqANPVLrKVCzI1kaRroR4QsyLUZAf3zJG_sJiCryNg0TQd8QOL3XpR8XPPpAy8xQON5r29ROd7dkcReYcVLXenP9HNM0s_evbYH0h01FzEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8cf218009.mp4?token=VOgimyJUxHoEiJSWFHeVPOKfvC2rpxpOqqU966wmvjV_mJJdyLW5c53CSWQL0DNiWQM86vzDYFyltd1b7J9UPDp0WyPR5cQoIKgs3jujYb7YHyhWT1s0PPz5RlwmKsd19MCkhbkP5ctYj-jQ8kvwpUCBVsuU_2eqQ07aXlfBr4VFAA0f63C99JAhloUddyFXM7D7MnPW-MIwJg40v7-2HgopdZMReznDPBBc3_5q0cbLqANPVLrKVCzI1kaRroR4QsyLUZAf3zJG_sJiCryNg0TQd8QOL3XpR8XPPpAy8xQON5r29ROd7dkcReYcVLXenP9HNM0s_evbYH0h01FzEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: از پارک کردن خودروها اطراف درختان فرسوده خودداری کنید.
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/438732" target="_blank">📅 08:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438731">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aded35a14b.mp4?token=Xqpd0OLtcfcea_iCvdUrXbq2zY-u2cJ-vSdg_F-_nsZpYPBOKmn55H_w7-ZjtuZslwKK90fe4uhal4H67-R5FMxnlFveJ4Gu_obdhfT6WJQsH3HrJ3Ml7DuXKAgQFXpc6bDaHWysGUotPw9krFyfVLUk_eU4gw2OIwSPcc2-r3xUawNbIpnUPq1dw0hc8tLKvrGH8UTYFX7FNjh8BKVnvX2xc0LFzYNIww9i7N8dJuhmb_2smEJOeoGxTAuLDPpFg5AZNWdaDcGTSSkZ2e-LEPOQ8z_idPtxsNd4LSuLXe-flBCQRlqi8e087oT-s4OBE-nU3DLvu0n70qNbs9T1y3psmNVN4OcSLigdSA5lAu2KXgQ8sR2j-QgBRpNr3UUXefKduM86Pty8LqjnNv436xRMJZQReTI8rQCNzEOofBU3w4YcOBXd6EpGGcXSuSx3pWjfxyUer-NU6u2yRsrOu67soUj8naBewEVrLlrzSFuyIm4gI_jGloXUg6TMYV_VyeSG8Gs6RoDC6LQtrZ5AQc29XfAlVRlgKVXJx9FMywDyhVTatNdV7vFzJMEzQ4ijfpEBMtZAWXmzQeH85KCMTPBnAw_-927Px_068KGMhTeFEMKuvx0d-MTbz-OixVg_wjqtuwqrRBexk9VVHXF8tBIFhG5U_U5lYES9GTef6sM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aded35a14b.mp4?token=Xqpd0OLtcfcea_iCvdUrXbq2zY-u2cJ-vSdg_F-_nsZpYPBOKmn55H_w7-ZjtuZslwKK90fe4uhal4H67-R5FMxnlFveJ4Gu_obdhfT6WJQsH3HrJ3Ml7DuXKAgQFXpc6bDaHWysGUotPw9krFyfVLUk_eU4gw2OIwSPcc2-r3xUawNbIpnUPq1dw0hc8tLKvrGH8UTYFX7FNjh8BKVnvX2xc0LFzYNIww9i7N8dJuhmb_2smEJOeoGxTAuLDPpFg5AZNWdaDcGTSSkZ2e-LEPOQ8z_idPtxsNd4LSuLXe-flBCQRlqi8e087oT-s4OBE-nU3DLvu0n70qNbs9T1y3psmNVN4OcSLigdSA5lAu2KXgQ8sR2j-QgBRpNr3UUXefKduM86Pty8LqjnNv436xRMJZQReTI8rQCNzEOofBU3w4YcOBXd6EpGGcXSuSx3pWjfxyUer-NU6u2yRsrOu67soUj8naBewEVrLlrzSFuyIm4gI_jGloXUg6TMYV_VyeSG8Gs6RoDC6LQtrZ5AQc29XfAlVRlgKVXJx9FMywDyhVTatNdV7vFzJMEzQ4ijfpEBMtZAWXmzQeH85KCMTPBnAw_-927Px_068KGMhTeFEMKuvx0d-MTbz-OixVg_wjqtuwqrRBexk9VVHXF8tBIFhG5U_U5lYES9GTef6sM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۹۰ شب است که مردم بی‌آنکه قدمی عقب بنشینند، ایستاده‌‎اند
@Farsna</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/438731" target="_blank">📅 08:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438730">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44a5ea9dfd.mp4?token=tMZDTpm2fE8FJ-M0sFWFNU80OuYORljsBNR_yGlAR9Tt8mz-vGg2_6oTsXzxA_ddahmo-FNoYeXjr2Z3yftezrc6qZiYebLQszO2hdnXsOu0QLvGAKrGauOw-j3D-ZBEEnS46UKvkfkqSBbTOwBzbBfYMvtt0sN4AFPUSQ2Eklmp6YrlmY6bSdAnIdHzeFBhZDToDmrHrzLN8sJaPt4AV_GdZFY6E3W7N2JsIaUsFYhfai-1Tn8-mRHRh5sf3bwhEFd6EcDSGzAq0MU52tTuV1BkcbERA9UBRUDx50pX2kuus6jZoWkRVq3SVBAvhUSXsQAWEfWfNDCZC-o26yV4xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44a5ea9dfd.mp4?token=tMZDTpm2fE8FJ-M0sFWFNU80OuYORljsBNR_yGlAR9Tt8mz-vGg2_6oTsXzxA_ddahmo-FNoYeXjr2Z3yftezrc6qZiYebLQszO2hdnXsOu0QLvGAKrGauOw-j3D-ZBEEnS46UKvkfkqSBbTOwBzbBfYMvtt0sN4AFPUSQ2Eklmp6YrlmY6bSdAnIdHzeFBhZDToDmrHrzLN8sJaPt4AV_GdZFY6E3W7N2JsIaUsFYhfai-1Tn8-mRHRh5sf3bwhEFd6EcDSGzAq0MU52tTuV1BkcbERA9UBRUDx50pX2kuus6jZoWkRVq3SVBAvhUSXsQAWEfWfNDCZC-o26yV4xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله مرگبار آمریکا به یک قایق دیگر در اقیانوس آرام
🔹
ارتش آمریکا در ادامه حملات مرگبار خود به قایق‌ها در اقیانوس آرام به بهانه مبارزه با کارتل‌های مواد مخدر، به یک قایق در شرق اقیانوس آرام حمله کرد و سه نفر کشته شدند.
🔹
در بیانیه فرماندهی جنوبی آمریکا در خصوص این عملیات آمده است «در تاریخ ۲۹ مه، به دستور ژنرال فرانسیس ال. داناون، فرمانده فرماندهی جنوبی ایالات متحده، کارگروه مشترک "نیزه جنوبی" یک حمله تهاجمی مرگبار را علیه یک شناور تحت کنترل سازمان‌های تروریستی تعیین‌شده انجام داد».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/438730" target="_blank">📅 08:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438729">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c176406e.mp4?token=DuWtrQcS2ObzcuQNW0_A9B_FUW412TifsTMnum106brhLUyzgWO4K7NEa91n-0U8iIkKGLsA6vg9bjU3cmCP6llk65L-nlcfddC2elEHvRZg1ID0Z6Tbt-w8q2xkAJI1XwLDwfMZSOAX2J_Yh8wjI3Qm7Spj1r3GlMJRogJMYaMRQ0zPKYYjLlkPC8nfSr02ffRdbGJhVxbNVd1AzIocL_8kHDZdpIhdzhTEOciQyjW6tkUwUkSt82xA49S8FXbZPA4f1btDf30f20CNjs41pt60v0ig35PCeNgBFD7dj2rBOr5ptOxkdm58Jf8h0klQvzXOEHNCIlEnxUq1yko-9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c176406e.mp4?token=DuWtrQcS2ObzcuQNW0_A9B_FUW412TifsTMnum106brhLUyzgWO4K7NEa91n-0U8iIkKGLsA6vg9bjU3cmCP6llk65L-nlcfddC2elEHvRZg1ID0Z6Tbt-w8q2xkAJI1XwLDwfMZSOAX2J_Yh8wjI3Qm7Spj1r3GlMJRogJMYaMRQ0zPKYYjLlkPC8nfSr02ffRdbGJhVxbNVd1AzIocL_8kHDZdpIhdzhTEOciQyjW6tkUwUkSt82xA49S8FXbZPA4f1btDf30f20CNjs41pt60v0ig35PCeNgBFD7dj2rBOr5ptOxkdm58Jf8h0klQvzXOEHNCIlEnxUq1yko-9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فراجا: زائران اربعین گذرنامه‌های زیر ۶ ماه را تعویض کنند
🔹
امکان تمدید گذرنامه به‌صورت حضوری و غیرحضوری فراهم است.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/438729" target="_blank">📅 08:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438728">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آغاز امتحانات دانش‌آموزان از امروز؛ اکثر امتحانات مجازی است
🔹
رئیس مرکز ارزشیابی آموزش‌وپرورش: سال تحصیلی امسال به‌جای ۲۹ اردیبهشت، تا ۷ خرداد ادامه یافت و از امروز ۹ خرداد، امتحانات پایه‌های اول تا دهم آغاز می‌شود.
🔹
امتحانات دورۀ ابتدایی غیرحضوری است و بر اساس ارزشیابی تکوینی و تشخیص معلم انجام می‌شود.
🔹
امتحانات پایه‌های هفتم تا دهم به استان‌ها تفویض اختیار شده و اکثر امتحانات مجازی برگزار می‌شود.
🔸
امتحانات نهایی پایه‌های یازدهم و دوازدهم از ۲۱ تیر، به‌شرط عادی‌شدن وضعیت با اعلام مراجع ذی‌صلاح، به صورت حضوری آغاز می‌شود و احتمالاً تا چند روز آینده برنامۀ امتحانی این پایه‌ها نیز اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/438728" target="_blank">📅 07:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438727">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رگبار باران و وزش‌باد شدید در ۹ استان نوار شمالی کشور
🔹
هواشناسی: امروز شنبه در استان‌های آذربایجان‌شرقی، آذربایجان‌غربی، اردبیل، گیلان، مازندران، شمال کردستان، ارتفاعات قزوین، البرز و تهران افزایش ابر، رگبار باران، رعد‌وبرق و وزش‌باد شدید پیش‌بینی می‌شود.
🔸
امروز آسمان تهران صاف تا کمی ابری همراه با وزش باد، در برخی ساعت‌ها بادشدید، همراه با احتمال گردوخاک است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/438727" target="_blank">📅 07:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438726">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtXzvIi03sX1VmjjnXz9XFoOwg-dkjKO2Dc41fRgjdpZSJE9_f3T8JjBV1QI63UEgRdb5EP_3u0i84oYlCLn8vyW7MzZZe0xVOj66nM5jxn872Q0-ELWmjjtP4TnwvakgpbMwAeF_F2MdasLS8FQBEQT0bTRcDLt-uXyZhkbovaOt291NLnGXVA1M05h6MGDMUzHfUiYBg5gGMyylYWpCHJ2hNmTmEpM13p2Xvcm81k1-j__UKwRsZy_TmEBkXxTXtzJeLIqT1CAbRoKobbTrbhAeJputIczfhBcMwN9a0j9GkaRYM4G2-CMko4wFgSi5pNOZBt5fOLXUd8tyFM1NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدارس سنگی و کانکسی جمع شد
🔹
وزیر آموزش‌وپرورش: حدود ۱۷۰۰ مدرسۀ کانکسی و حدود هزار مدرسۀ سنگی وجود داشت، که اکثر این مدارس جمع‌آوری شده‌ و می‌توان گفت کار جمع‌آوری مدارس سنگی و کانکسی به اتمام رسیده‌ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/438726" target="_blank">📅 07:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438725">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-2ydkR2OGft2W903badJ4Jo1GTUZEtIGmiEOT5H6_fDKLGbz5Qherf2HuilKah9IkSvzpKpg2z4kowUtKBgUQ3CRrgcZygvhASSf_DSmRzxTSDG9me0nSO1cEv5ZvpyA_H70OJ4IUNGOP-mrr5jI2Q48UMxlG0kGNjMgN_jOj8Cvk_kE0zP9er_erwuWFS22bjgXW6mFQZWJcb5sdinFIRI5wc-5E5hP-QCT-vs0fbQ2FttJ-xQ4Ez3BXjF0lYWn1lP63Ip9H6ct7-QpRjgwPi20sXbWHRubgRcJZOb9TEpsqNz_IhRQnzo5cdNopvjllqr5czZmYkHRptgSsYvkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیر استقلال در آستانۀ جدایی
🔹
مجتبی فریدونی بیش از ۳ ماه است که به‌دلیل اختلاف‌نظر با علی تاجرنیا، در جلسات هیئت‌مدیرۀ استقلال حضور پیدا نکرده، به‌نظر می‌رسد در این مورد قصد کوتاه آمدن ندارد.
🔹
طبق آخرین پیگیری‌ها، فریدونی با وجود غیبت در جلسات هیئت‌مدیره هنوز از سمت خود استعفا نداده اما اکنون احتمال جدایی او از جمع مدیران استقلال پررنگ‌تر از همیشه است.
🔸
هلدینگ خلیج فارس هنوز واکنش رسمی به غیبت‌های فریدونی در جلسات هیئت‌مدیره نداشته‌ اما به‌نظر می‌رسد به‌زودی جدایی او از جمع مدیران استقلال علنی شود‌.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/438725" target="_blank">📅 04:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438724">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🎥
کرمانی‌ها در نودمین شب حماسۀ حضور
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/438724" target="_blank">📅 03:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438723">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPd51HbprXqr462Ch7ZfPAf10VbBmWAjayTPkQS09UoC-uDlAmuq-zdzOpQowBal61CM9G_LUesBm-pIJei22fj3zu_j-MbKM27jLnGJtLi0DHXqqrFHpxUiE2DC4bGy0UD_FbZZQspNwKoO0l1vssCPFd5kvvdSiR5t7yVaYjB4YQmq15VeFffYGmRv6s8GCRdLbT6FCm3a72YVWoE0j38aQfHrZ0tPE2hqsUl5P6sinHvWbKgsGxVw06CE3G4tUjt1wb3o8z9q1iBHI__SZ9Fhx5vL8XFxjfI04rdphOX-d9MdpHeGzyySObXSJcWuWps9imFMGLtPQIJWZ4QuCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم‌های آمریکا علیه یک شبکۀ موهوم مرتبط با ایران
🔹
وزارت خارجۀ آمریکا که این روزها باردیگر دست به تحریم شده، این‌بار به سراغ یک شبکۀ ادعایی و موهوم رفته است.
🔹
این وزارت‌خانه اعلام کرد تحریم‌های جدیدی را علیه یک شبکۀ ایرانی اعمال کرده که به ادعای واشنگتن، با استفاده از روش‌های فریبکارانه، شرکت‌های آمریکایی را هدف قرار داده و برای دستیابی به فناوری‌های حساس به سود وزارت دفاع ایران فعالیت می‌کرده است.
🔹
وزارت خارجۀ آمریکا از اختصاص جایزه‌ای تا سقف ۱۵ میلیون دلار برای اطلاعاتی که به مختل شدن این شبکه منجر شود، خبر داده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/438723" target="_blank">📅 03:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438722">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a761d6e0d5.mp4?token=gBGgqmIbpQcyExr9HoX1twhqHec8MNLD5MNp0gbOP9LENJ7l7OCtkS1hYbBYmT7cdEhE1FH8Q_1mjQH_b7Pz4AYM67IINjc4dgRFiLXm3VYh413p_PY4JnAjhmwlukBwZxU_r8AVpAR4uSyTyF6I1HgQeUzNCkdfZk1X4FGE3ZNuPN1mfP3GV9p7zg4xTgXqY-e6WKsN_wURnzD3h3uMxPH7v6DMDd7ZERJoHFAxZzsmuQtgikUz3Dk-g9HzOGYRw6t0uCSEQfBTULY18dd996-REqghiD6QSjNvJTrZ7bwVZQxpCA6QPMeoL37v0ry4RsarE7DZPyKSJq4OVAazXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a761d6e0d5.mp4?token=gBGgqmIbpQcyExr9HoX1twhqHec8MNLD5MNp0gbOP9LENJ7l7OCtkS1hYbBYmT7cdEhE1FH8Q_1mjQH_b7Pz4AYM67IINjc4dgRFiLXm3VYh413p_PY4JnAjhmwlukBwZxU_r8AVpAR4uSyTyF6I1HgQeUzNCkdfZk1X4FGE3ZNuPN1mfP3GV9p7zg4xTgXqY-e6WKsN_wURnzD3h3uMxPH7v6DMDd7ZERJoHFAxZzsmuQtgikUz3Dk-g9HzOGYRw6t0uCSEQfBTULY18dd996-REqghiD6QSjNvJTrZ7bwVZQxpCA6QPMeoL37v0ry4RsarE7DZPyKSJq4OVAazXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نود شب اتحاد و حماسه در سرپل ذهاب
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/438722" target="_blank">📅 02:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438721">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">مقام کاخ سفید مدعی شد: توافقی که خطوط قرمز ترامپ رد کند، امضاء نخواهد شد
🔹
یک مقام کاخ سفید در گفت‌و‌گو با خبرنگار شبکۀ الجزیره مدعی شد: دونالد ترامپ هیچ توافقی را امضا نخواهد کرد مگر آنکه این توافق مطالبات آمریکا را تأمین کرده و با خطوط قرمز تعیین‌شده از سوی او همخوانی داشته باشد.
🔹
این مقام آمریکایی با تکرار مواضع طوطی‌وار و همیشگی، افزود: «واشنگتن هرگز اجازه نخواهد داد ایران به سلاح هسته‌ای دست پیدا کند».
🔹
به گفتۀ این مقام کاخ سفید، نشست «اتاق عملیات» در کاخ سفید دربارۀ ایران پس از حدود دو ساعت گفت‌وگو و بررسی به پایان رسیده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/438721" target="_blank">📅 02:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438720">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">۲۲ عملیات حزب‌الله علیه ارتش رژیم‌صهیونیستی در جنوب لبنان
🔹
حزب‌الله: نیروهای مقاومت اسلامی در ۲۴ ساعت گذشته در پاسخ به نقض آتش‌بس از سوی اسرائیل، حملات به غیرنظامیان و تخریب خانه‌ها و روستاهای جنوب لبنان، ۲۲ عملیات نظامی علیه مواضع و تجهیزات ارتش اسرائیل انجام داده‌اند.
🔸
طی عملیات‌هایی در جنوب لبنان و شمال فلسطین‌اشغالی، ۵ تانک مرکاوا هدف قرار گرفت که ۳ تانک با پهپادهای انتحاری «ابابیل»، یک تانک با موشک هدایت‌شونده و یک تانک دیگر با سلاح مناسب منهدم یا دچار آتش‌سوزی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/438720" target="_blank">📅 02:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438719">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d3db0548.mp4?token=tqxtviWtcCDpcblbdMj5Yadk2Cjzrz0RWGYEMhGCT4pCsVdoKAfrnd9ccZmLt5ed8oWXJDrUrWzHm4H5cLKHWBQfOnfwCjFiL8_2DBEecuUYEK10dmoTkdTYpbXNCk0Xi7517RB-wElGVVNF55FE-PacHK7qXrSWX9cKFkuoHDPcpmqp3Tk9u17aT8NidKwbfOyqt-cYTdzy_MqmxvpwLBXJFwIhtgVVKulL3KJHZWY9sXIyY640LCF9fKE5xvMW7DSInL0G0coWhSRlWokf_303uVYtZGeenTFpHKdCCljNwk2eaxvVg2w5NDlQrcuXl1NcssenmeHLKx2U9f6OdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d3db0548.mp4?token=tqxtviWtcCDpcblbdMj5Yadk2Cjzrz0RWGYEMhGCT4pCsVdoKAfrnd9ccZmLt5ed8oWXJDrUrWzHm4H5cLKHWBQfOnfwCjFiL8_2DBEecuUYEK10dmoTkdTYpbXNCk0Xi7517RB-wElGVVNF55FE-PacHK7qXrSWX9cKFkuoHDPcpmqp3Tk9u17aT8NidKwbfOyqt-cYTdzy_MqmxvpwLBXJFwIhtgVVKulL3KJHZWY9sXIyY640LCF9fKE5xvMW7DSInL0G0coWhSRlWokf_303uVYtZGeenTFpHKdCCljNwk2eaxvVg2w5NDlQrcuXl1NcssenmeHLKx2U9f6OdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک ریز پرنده در آسمان قشم ساقط شد
🔹
به گفته منبعی در پدافند هوایی جنوب شرق کشور، در پی فعالیت پدافند در جزیره قشم یک ریزپرنده مورد اصابت قرار گرفت.   @Farsna - Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/438719" target="_blank">📅 01:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438718">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">منبع لبنانی: مذاکرات لبنان با اسرائیل در واشنگتن به جایی نرسید
🔹
یک منبع رسمی لبنانی به شبکۀ المیادین اعلام کرد، هیئت نظامی مذاکره‌کنندۀ لبنان در نشست پنتاگون نتوانسته به خواستۀ خود برای برقراری آتش‌بس واقعی دست یابد.
🔹
به گفتۀ این منبع، هیئت نظامی لبنان در جریان مذاکرات بر ضرورت توقف آتش‌بس پافشاری کرده، اما با مخالفت مکرر طرف اسرائیلی روبه‌رو شده است.
🔹
این منبع همچنین افزود هیئت اسرائیلی با خروج از اراضی اشغالی لبنان مخالفت کرده و بر «خلع سلاح حزب‌الله» اصرار داشته است.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/438718" target="_blank">📅 01:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438717">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THYbMuSYXEW-Qrx9YZN5r-PdqYNBCrX8npcAiVKL259ShLH6Jz2SsUUkvhglHKSOm2HXe1EcurZTAi68a6bcV-8UfVagbtsrxw_aeBkYmBdNAWIzoQ0Ly5G-Q-2cOtSH84R3-m5IQxArWjE94AS-Ns-N79PndOBIIi1g_Cv2t-p-UyN_kOUiPu4OVi8TNHOF0OrLFZ1xL6Fdp3eYXJZXqLcZ_ZiqY-DXRZeMELTZIFdLznNhisadFu4GXK8u1MJADKfXAumS35RG3EciUXv1RV62cGUnh5gajueOwwx0z6EZMhIjSnWj4nq2hWj0rFHcF2mosHpN2Z_tloDUJOIo2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان: ابداً قرار نیست اسرائیل را به رسمیت بشناسیم
🔹
وزیر خارجۀ پاکستان: شایعات زیادی درمورد توافق ابراهیم در گردش است. بگذارید روشن کنم که موضع پاکستان در این زمینه بسیار روشن و ثابت بوده است.
🔹
تا زمانی که فلسطین با الگوی پیش از ۱۹۶۷ به‌رسمیت شناخته نشود و قدس شریف پایتخت آن نگردد، هیچ انعطافی در این موضوع امکان‌پذیر نخواهد بود.
🔹
پاکستان به موضع دیرینۀ خود در قبال فلسطین و غزه متعهد است و هیچ تغییری در سیاست اسلام‌آباد نسبت به اسرائیل بدون برقراری یک کشور مستقل فلسطینی رخ نخواهد داد.
🔸
گفتنی است چند روز پیش ترامپ اعلام کرده بود که چندین کشور از جمله پاکستان، عربستان و قطر درخواست کرده‌اند به توافق ابراهیم بپیوندند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/438717" target="_blank">📅 01:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438712">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NZcAOBvzYyjWcYHEE4qByM7UDaN5sG4iSBV9aO5bo0cCwRhZZbwoPHc_4URCiuhrJ-BZkqWgW6Z01ZhBX3jw6p1xy0naMO2igwVB4bQYYXt5jVs8kA0DyiQ-k3Q8u6duaEmPm4142e2X5yrLokJNnvt7t9g1w77pI0oWRZBu_Hpafl32Di2FUCsTktVvcTmzfufvhpvzh9lDGZ68jmdYGWpCBncjlnbqK6FJCgRegGtv65HENCY3sHC83QA5_DEz_NcPgdOti2TYWFj9mCe4DPL7E_kBQln3S2EO3WODpK6lYst-DxVx1c-slEh6b5kBBu4BVaQiLOWyevWC6uiI-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCk6gexFNb8c0XwYLBnX4X6xnHknGCwTo9xzqC2cqCsgRxvstnJUf63mW-7ZgH-ZeH4-9KZtjTabNrRwuvs5WkHBjDa9H367GlBkqzSeAug7oD7Pe5gsxzW0DOIpyxyXUDeQzuew3m-3-hQSUN6ZJa_ZLHa1zOG4YOWxWNFujLEzuXwKtjU487b3opiuM0Rqi11136v7_107RNtaxNdEhinorQP-S_7V-31QNKaCs62G6dY7mJ0rX8vTGu0qde078-QJpM3rcZiriZN4-EK7KGOX0NLetbGJwROHehGBB7X3THcTRdlgNHycfMoK_7fmHIquy_K7E07qdODAwafUPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dc3fNMwK1m5BV4hah8Ju1Pj5hOuZ51tKiBvj4KE8orlErEb5-MRmFMXaaAG71-eJ--e1W8i-yZFhHF37bhRAMxK666dBuln8DaNU1T-t4fE0ZFT6-o5Ngp2wyajcSpL1JohrAdgD-whKagaQ28FroSi5FYQ-6Rv03b-O6teytKX4ye9ACe8Axq4HxQW-tvWUTRbDDaA2xHbR4vejHcfBRtFQ3rnCrHserRL_sgG8mdD2S2LuGvMk53WHBTDh4ylPhbhjA9H-KrUeV5LaDMn85iAZDHvbDF-nsRy0ps6-s27M10UEWmhqXPYXX4CzYPQJBXglgo3AkNCqlgAV8KaEEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUIHZkkjQd8uhD3DzgMEcsNb206rQHdm2xxeiQ1hnyU02_75dyHTvOcNlN6frHAwTJLkyZIE7pvHyVeJvIsNoxPLXJQZ_ZDytOZjDVCFmU4563t1g5CqeAECuhT_8kV3F51mT2ElngNXL9ZHF4DJHiAyh-hli9v2HLlIAVQv1ifNC51lOgDOTtRNf3mEucSZBnripUaa5w5ikoC6oKq1YrXJIvzAz-QebSp1XyVzR2Bl1qdBO_L0hDNK22Elu2No4avJt81g5DfHaeOgfVqnxv6jiRwtue-NDM9XCfDEy1lyAdPyjK74SUjaZFzqpvUP6jqR6v8zW55QDYwYjtulIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mp1cvCTcOY2UzeuSut2DClpUxd3DU3jDmVy7bSndfzk2LYmuQC1YVkQvB4xOyAVK5eolm1bz1Vewp8luZUHQ0I0dYefO-b6TWyrVE1dkp4ylkZ6CDW3N8fcGRQKafGqRvT40EMCOYJJP17Llu1HS1-IHNFdJ8ZPKn85d7ud6ZN98r2WMAlNZUWrY5UX9FZjZG73VoYI9RP_P8GwO89ydFxwgc39BOKZzEh95A-h2ciYsaEFKiA4Zt4AgPG9yp-i5Kj8HxUbwD8bqaGji_cCO7FD7AVEls2EoSjk5ULwBrWhiyFq70xiShTRluzQZXmsnV7fu75KLHfpREkY4f_SE7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۹ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/438712" target="_blank">📅 01:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438702">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r9WtJ3-YDBVGrFLsl0pDK1pvJ3QaodVEDIwYrGqNvoeUazITO1X8Jhk8ZCFVQ7G1Z3rYQgVP2E3ZPC4Vh9MclkeFtb4eNN_dnZG-XglIDM_OhnstWs6nVBRj6NNrotJD4YcfOiLcakxJeVgbCswQNpQh1zZjFyunT4WTiJklIZGl9i5OmOdBYRWKlzgPuVbpZnVDtMj0jkyILLzHYZ1Uh79CW747Fn2FLS8JyNJJxv8vLozsv_AY3cwmisFwHdIJwke7f4rhCRRytpWGCe9xVONBY51_slnfRa1cXpGT-2LxgegW7t4d6pcciRyCcGtDRLUrWfjoGappcAzw20QsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZY_Pledfuos3RiIoIHb0xYK4uhx5fnGlkayQnTAP9hI5gcZDo7kjo54k2_Qtc0TZY-aLh9SD-0QMLgDTsqEpkvvyxEyPDg6vmYb0wofCdCjxeeop6Wq6hyIUDAy2og7e2i0TiCuStXU0PApDNFXOuhtGeMMmuChZsGyZEXH5F0hYcBLj1CA-HNE4sRkVnu42N97UTiHCwO9pEQb01reE3TNq1jgBw3MSbaT4AmgFFrAu550fIpA57dUYLu6UIyPAEhmjvw0ghJJxI5a-oXNLygMw8zMxS2rW41eoZJozc9-5g4pemNI82gfsoWpxbCP0YImAiozH_aFsT6B4vpUHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZMWFLOBJ5UKPtbvLmVmbVnMu3hZJ8Y2YBcHTSQQKnqkEQH0mndSBaZdDEcSilyz9TswPwyfiuBtOTTosbupWncqXJOqOdspbQ_Nxr81V-nT8kBGyeT5GKSoPMhFzFAnhqJo0Tdei9hk5x4-nfZ4qQ5ye0KLyGVZlA_kUt98AYdGuXxFeUPxLlXj9QDQ76dvQpcOJsXLjl2e0bwqpIs4JiUXQyXeC-TfpbICQrs5B_f4gzb0qZNFnGX5SmFwcS9bcZ9bLua4JxPhM-hjmytD4QH92puSG2AC2IHvRQaTY9U5uWt6P1kmTSlsldJ4wzOq20QXa_ntCTOw_pbpsOq72iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGl7Y3QZoF3K-dpshiCVhF7f86R5aWlvG0Bn_J1xRw_UTOP_aIAKEtv3qB1GpDR9Cr1EKX6Xegsgykm0SEr8lK4W6xkGDa6H9CbOnKNOWoQdSdgY5vP-i-sQ_SixUu8aTMMHBO53qTo-ORSOPuDcSnU0RPfkpzc4JRPh-_NYMqgEwKjgbiOsOtTh6wrxrCWJ0JhWYdo0TnaH38QtY_mPyFC7cyqhWBSax7df6IOgZihQYUJuFepoFtTaqCCvO1amQyp3msN-eabN1FsGy8SsEKeTFKQ90lfcQqiWdMlE6Ln_e7lJLAqwUYoU2dPZOji7y5Hc1cAcw7uGFJdhwhGdQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oyICtu37vwQBZI8Lka7PzOFH5QDjdciwVREFB85J_RQhgkLHdXVWf58DcATOYV1exYSP-ACsSDr3YPVh1LmIFV60WPCSaLU99TeH4AgyQSrHVzAcEvE6BHVZf5LHo0b3dVoz-D2AkwQdwUR5EtWPsrZUdy215B1jLr6If3mNIgcKIhkXvDrACsqHEBNQS8KIb8bOYGvGqK8kB8DMez_KsvpKx8_pW1CoDfSGXAkS8fv4K1sbLjKdFZvmPMSmVUIC4tqBvlwaPs-dp5w8eZHpJhPezWIdBC8mOKaPcoPOiCZ-OiEt8DbEoRFUs-AoHn4upwaDAx0ZW7g59qC_MBA_tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkPnw_pHnrXS4smtVn1N-aTj5sZj52nM21k74Z-s-FdXbfBoZFQx2MK1D37oc8qOyHn2TMQnGjE7kjgkVl1V8NVpUpzBdXTMRP9bdzQikNyXSfIcyoJ8FjIBbAJehsEFQ7M_xJjTBq9OWKomAn_KRPGE4BXMdZLtmQCucWgGfppEmf-2yUW3mWdKBLKSBH3u0XihGiqkwhdhy9il0eqW2VMWtPIbhfowRiZpQlt0QWr7HdnkZrmIxJgNbog3x8l0Zzc9GAtHyFWJIler1vmK0ao5yFXZQbUtyLqGv3C9JTSAc3qZzNShsKJafHYURZ4svIkFGhXLICiE9krDSscbvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oArB2-Uw8QTjEM_EKUyo5ocdP7bDEF58LA82BGUcwqmwhO6i1ddDjHXSKA1y1DxUzXHos-ssucG28GpM7xz5lWbqXLd6Z5R80P5KJlBxblYmgabgFGuGa0GdZLKOt2hiHDbb4nPQXAWEoWJYfOcusJK1Tq3r6bJzMWJZafuDaM3wmQIJOwWOWb-ENi9gh19HsUyAXYGG8vnal4GUO0LJJ61hn6XJZUqMw6vax7LEzE0IYUsJfJUg-Zg4oZiTrqay0p_ivdLyWPyqc89UBKPmaKtpxFasJwPo2dxOl5S7yy5rbqbv9tIVc-q7UkFV18lhE7Mg2e_d0wpFlHE6QtSnwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NuWvXfsHXoN47tYzGZyGROVKv1XbJ7EQkRpfCzpKhZwMmWPf1LB_c0Ii0WM8G_lbyzRxwPd5OpMmyvpuPbSLMDqfOUTUbZrUUtovmQkU8r3PGUEuMPlpNwoBRU01E5NLL_fEd016-O5JoIpGsgGgQRGF8VoORZpscZan8KAaTuLXfly2A6E8db8bFIct8XghqQr7r3P1XDH1bQubpiP2noe6FdmuTrJwdJ9ibNev1o_qL05eavYWcIXWGxrXA7dBIDuIePIvWZwda0LVvHuFQARb5MfVUVN64e3QK5oTlepTWvX8BNdS_SzsecSK_-ZO1LW0fQQrIjlTvC9NSym0CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EZi71fd1tLW2tC80j2A3qNaHTK3RxK2qO45a_2QQMORzK1ApK5pC4qHfgidBXqoCfJnoeHqVvliy-N0yfMSi1ecwsegpDBO0at_wJHJSmFc6vmzePIpBEY_NbQKJ-g9ec21BGWRonKELCUrnl2UPyk3sYimWmT-Egt2Sx-BcI3go4tEdj0D8vfMjvTTD0DjGPz64O9pnKHxP-5X5-E79PwbnQlRy30XpBogdcBPRqpQ6UDBlwwSnX7icMBh9r4a6x4v08FyndylUrd9yDhj5PjY60Z5fs_EeZnfSYB8Pe_FxJF4iJjQgA6slQjEmG5YZTMbkESG5gnKhAdwoHwlceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9t8ssAukeQ9NmUmK7citnzd4oB9TVrlk6jdZFH4T9ki0vOn9_IUwSMJ8LMBo5Pi57piiGCNfPv6YrpnX6IA5iMiiilRdVYuA3zd5iWob7AAcjSS1-xRmjkoLLnPQx9ym0aBcRhCc1w8MWlRpAoZTgzIudt8szsxRroORF3_PMnj020oSmPAWqfVhQeBOVAi-YYRIOrwfN2-r8UjpAGoRq55e5u0TzFP6fM4bvnaCpet4vkbK7H0HXbuxzmU5IUN8bCxDuqK91nhEXdciU30RPZ_XlMnhdSYuO5wAT4W3Zi4B9tCXJ1alGLoz3PKXQ9WyVyPCTAI0CjB0rTeG60oDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/438702" target="_blank">📅 01:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438701">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJLvBAr-9WGRU7QdDS2JYpmQ7asOzz0cePsiuPnJ7n2Yg9T-1fQ0LXISznaOhVUSprgxHQtpHNmXOavN7x75Br-oMFagM_w3Mjr36VyXYnGwBOBKsM490VGk2VIQXEewKqyTRuZLj-CFOHyBSFPu3Cz_oKSqMZDlsiRQvBUcVEMzxszMlHPAQw2BmNe2docNriIy1ZRuw-rwoORg9pjIMliIW0Hf0nBBp8trMHwaDWBtedGGdvUVgYPkcF7yMm72Q-8RQHc9cGSTOxlaz8_vOZ7ocbY22CdX8tbSpzB8EY3tY32nrRGa9iRRjAMMp_z361AsYSVpxQD5EEgUjt1dtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهای موفقیت
🔹
روزی فریتس کرایسلر، هنرمند اتریشی، در پایان یکی از کنسرت‌های بزرگش با تشویق بی‌امان و ایستادهٔ تماشاگران مواجه شد.
🔹
پس از پایان برنامه، کرایسلر درحال جمع‌آوری وسایل خود در پشت صحنه بود.
🔹
در همین لحظه یکی از طرفدارانش به سراغ او آمد و گفت: «استاد! من حاضرم نصف عمرم را بدهم تا بتوانم مثل شما به این زیبایی ویولن بزنم!»
🔹
کرایسلر گفت: «من هم دقیقاً همین کار را کرده‌ام! نصف عمرم را داده‌ام.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/438701" target="_blank">📅 00:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438700">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🎥
نودمین شب حماسۀ مردم در کازرون
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438700" target="_blank">📅 00:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438699">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتانیاهو: عملیات‌های ما محدود به جنوب لبنان نیست و به بیروت هم می‌رسد
🔹
در حالی که دولت لبنان همچنان به مذاکرات مستقیم با رژیم صهیونیستی دلخوش کرده، بنیامین نتانیاهو نخست وزیر رژیم برای اشغال بیروت خط و نشان کشید.
🔹
نتانیاهو به صراحت گفت که عملیات ارتش رژیم…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/438699" target="_blank">📅 00:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438698">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3X3I1lcXzSu3mek9aXipDNg8YeUI5bYzzt70kpQYzvWco1SrpTcjujd5M3eofeBP0WW81_fkJuxxudkWKjAbIOST9Nf6xDUjWyD923Z0t2YfH_QQo6nWc7P_Z8_JYkCsq71wY7loLVdkomuLcUPSw2hYX4hp_dMM-sa0lPCvLplONPJtOyMjtnSLOVkdeFxVsyhXOIjCjc8WCOkB3Kv5K65clv6XYGk2l23lQk1E41xmEy0yy1Izrt8tiVYszKTXA-3hUTPk-mfZDLyPy_5oOoTwX_SpN9_t4Lnq0ZWFl0iFcNGpYyq3kgsaC_lizVmG0GeQt5Vin985ulvKx_brw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ باز هم خواسته‌های خود از ایران را فهرست کرد   رئيس‌جمهور آمریکا در تروث‌سوشال نوشت:   ایران باید بپذیرد که هرگز سلاح هسته‌ای یا بمب اتمی نخواهد داشت. تنگه هرمز باید فوراً برای تردد بی‌قیدوشرط کشتی‌ها در هر دو جهت باز شود، بدون هیچ عوارضی.
🔹
تمام مین‌های…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/438698" target="_blank">📅 00:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438697">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EduCZZFPHBEh9lMCAe3tF6szMQ3T3fZNZcUQ3yLc2pqQHJ0FoNDyCuqcDawld17nY3CvQo9ia7Q7dIdqLXyY2qIHNMhs6mvwlqOPGzy1PJsHqZLRW1whaV1BOY7C1LMOviPyztK6PqBTeu4eGve_l2PgnGvyKkBi6mT7ef8ftnpmunf5axIWRH-7zVfu9ufVFGQHTKSTW0RqMccr4LAogiPFk1REXzRqqPSaKapRlGbTk53qoDqvTcdnARoCAlNxJJ39DIZhXAF9tV_V6KSmSeKBMmawWcmHEMyMF6knsygvZ1uw7OftXaA3MB7qGKvzTocJMMnKt1NqMDNNefolzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت‌نام دانش‌آموزان غیرحضوری شد
🔹
معاون مرکز فناوری آموزش‌وپرورش: والدین با مراجعه به پنجرهٔ واحد آموزش‌وپرورش و وارد کردن کد ملی و تاریخ تولد فرزند خود می‌توانند مراحل پیش‌ثبت‌نام را آغاز کنند؛ این فرایند در ۶ مرحله انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/438697" target="_blank">📅 00:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438696">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aae8e40244.mp4?token=bHOlCeF-2xUKApLic5aTbcRDqbPoo8O2VW9M7SCZSv5dJUUH-49f4lyTjXNbj-Q9ThKNWRKF1-TNER1qqYGOa1JYKZaxM9-ruXL9DsDLMRn15bau5h4XHfjhJhnU-1l--qqKvDwZ5PDqhrSCRAhDZf4kAjYgk80RZ9Ww5TgiK0ETX6cZtrA9fbShmEzI_o_6bh8YLCTmFYtKgpwPfOFxp0fCSBGzH0zC-pKLn6oon8au-iZMZHnS9otdLOE7iMmlel2ubaTN-RxlBweTmPHK8U4M35c63wWf57yulrPgnDllpRlh1kn2BW3FtJwbzhcYJ75su4ZJRzn5kkmf24qFGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aae8e40244.mp4?token=bHOlCeF-2xUKApLic5aTbcRDqbPoo8O2VW9M7SCZSv5dJUUH-49f4lyTjXNbj-Q9ThKNWRKF1-TNER1qqYGOa1JYKZaxM9-ruXL9DsDLMRn15bau5h4XHfjhJhnU-1l--qqKvDwZ5PDqhrSCRAhDZf4kAjYgk80RZ9Ww5TgiK0ETX6cZtrA9fbShmEzI_o_6bh8YLCTmFYtKgpwPfOFxp0fCSBGzH0zC-pKLn6oon8au-iZMZHnS9otdLOE7iMmlel2ubaTN-RxlBweTmPHK8U4M35c63wWf57yulrPgnDllpRlh1kn2BW3FtJwbzhcYJ75su4ZJRzn5kkmf24qFGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع مردم سروستان استان فارس در نودمین شب ایستادگی
@Farsna
- Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/438696" target="_blank">📅 23:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌
🔴
حزب‌الله: ۳ تانک مرکاوا در شهر «یحمر الشقیف» مورد اصابت قطعی پهپادهای انتحاری ابابیل قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/438695" target="_blank">📅 23:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2Phf02xTLYOZxMKcj1_9Q88JlptXH7HTXm8i0LDf98sCWqT2-rsygZz21m_S_EGFPnk9kwrdUma5Luf_LyB7zBYvDCcWuVuMddUEgf3HgpRBHD8soTow32pd9-IidLBj4j43SaNvLj_yyQJO2z-iJQsUfz9keaTbrYpKjek1hi3uC6ytjDhKBHoLn5PNqWvmFXEy9LEhRqzfJb0FGkH3EyQqTzg2f7XgNz3SSM1X9dgfg7UhmTiPlVZxmdTAgrVffLlgfrNVe597B3qhg1Xt6cNo6WfFsRvqU5_Y1bRF9X-b9XgKIqGIY_ynHHmVBmvWXw0chK5ATzSqAl5GcHKjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمرهٔ مردم به عملکرد قوه‌قضائیه در برخورد با وطن‌فروشان
🔹
پژوهشکدهٔ مطالعات و تحقیقات دانشگاه جامع انقلاب اسلامی در یک نظرسنجی از مردم پرسید که «عملکرد قوه قضائیه در برخورد با وطن فروشان وجاسوسان داخلی را چگونه ارزیابی می‌کنید؟»
🔹
طبق پاسخی که مشارکت‌کنندگان به این پرسش دادند ۳۹.۴ از مردم در این مورد عملکرد قوه قضائیه را خوب و ۱۳.۵ درصدر از مردم نیز این عملکرد را خیلی خوب ارزیابی کرده‌اند.
🔹
همچنین ۱۶ درصد از مردم عملکرد قوه قضائیه در این موضوع را متوسط و ۲۰.۴ درصد نیز ضعیف و ۵.۷ درصد خیلی ضعیف ارزیابی کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/438694" target="_blank">📅 23:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438692">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlYcdISbgOXp1pmPWuvl5OdLnaYK2A5jq4H-hDJszaWcawyMooeaQcuuq_6jRzt8_cCqyqV4Be4qU6N2Wdz1sySF39kfbQ3QACw-3elDlco9Q_KxtH9LCOte1wKdPomJZ9Fe_Bt4zNjcvzH7_Y6yiwOERFWG02sk4c6nEK6eC72AnxtuueXcQrcjUSvvtctM9fCgG_VyairLbuwQ7MgPMjISGfPCDnzAT4UHLqlqXyUjkmcNqJFvkt2NDm1CQrUWG_LIOL-w_MKWwPCjmcpIMJTeJfp8k6RcRf3oOvsFRH1BkxGjGUGtVi2n8MIJZ7_SmNKRSjiE7NHAG3Ds0jwdMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTC64SY_rmvFR4MyGrWEMMxGs_DNJygESCErWO6Sau6yrOaazKtE2FIpLdqOjH-3wB7yF5qAHZV0-CiMVoKUT_U7wrtuY0qMrIpOsWpkLppM0tr_s0tZHz6XAAjWG9v1I9Y9JVcYPh9leyUrvGmqQNaQCLRv1u7-ECFVCKJtgLXLAVgR7mh7JSAstnEkpTGKTfJ__HFGcZkCsfZDXHuw02pLyVbFgQAC7Cxj9VwmEepQmMr73j76sPuUW62m9OuxHRedalDGyywVCtgPnpOHDvSPhgCws4nZX_F2fEdOhv5WTOcbcfXpz5qBke3dMMObzab3M-cx8cZBXPlxy1OjPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نهاد مدیریت آب‌راه خلیج فارس: تسلط بر تنگهٔ هرمز را که در میدان و دیپلماسی به دست نیاوردید، با تحریم هم به دست نخواهید آورد
🔹
وزارت خزانه‌داری آمریکا اخیرا از تحریم نهاد مدیریت آب‌راه خلیج فارس خبر داده. این نهاد ضمن محکومیت این اقدام، تحریم‌شدن توسط کشوری را که رئیس آن به دزدی دریایی افتخار می‌کند، نشانه‌ای از عملکرد مثبت خود می‌داند.
🔹
علیرغم اقدامات تنش‌زای ایالات متحده در آب‌های خلیج فارس و دریای عمان، این نهاد در راستای تسهیل تردد، بی‌وقفه به بررسی و ارائه مجوز عبور به شناورهای غیرمتخاصم ادامه می‌دهد؛ به زودی آماری از ماه اول فعالیت نهاد PGSA  منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/438692" target="_blank">📅 23:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438691">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbUIcBo_0k18xqJ-g-ywmXj1qOA-NM37v50hfa3Hb1Q41Ht1_-VMj75Qt_nRqOwsV15aXhnoO7x33aQyTakbnmcFhXOFZMUvDkRCCaso-xaR0z-8QIJ1F3j6qItW8vCV6NM_Yhz6kYqUgdZUzz1y5o_GEfFmY6CyUT4eT5TrcEVPwfCRdkofNkM_JYnh5WiXmI7L4_GlZHPX0tN5WMB7_DO6ald_lzPCVwnd0GD2Yx48BexTP8Uj6t1orTqBfuiwDOxSlkVkjT76MqBRVTjkDXgBRsOB55t642YmP2Z7zGNF1Tk4fHSauGC4mA-4r3AAnWNzaXDHdaQeieQ3johTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سرمایه‌گذاری با صرفه‌جویی در مصرف برق
🔹
در طرح جدید وزارت نیرو، مردم و شرکت‌ها به ازای هر مگاوات‌ساعت یک گواهی قابل‌معامله در بورس انرژی دریافت می‌کنند که می‌توانند آن را بفروشند. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/438691" target="_blank">📅 23:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438690">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🎥
تجمع بندرعباسی‌ها در سواحل شمال تنگهٔ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/438690" target="_blank">📅 23:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438683">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_FhYYlj32xMIgRunSfVcg5PDEFXLlIThaTaKaq6Ah-la9IOJJLQKmU8wpLCAoAH73ooE_7rV0ignQNS6xTQGpHT4uhoZLPVmJQ5GEWRrRIMmTTvFwFMpMO4YCTB8FGd1l4Hlg5aYjyQR4ZT81vD8RO5GyR_2O--2cqrr7T3e_GNl-NsCSev_HVlmG3LKfXbVMBi5T11F4L95Yo10o55f5Z-gC_6093lPFlGG45DAnKHKiN3UiONJcpvutTI7mOgBfCuDKpAyGXXS2L2vEGPZMDvn7nRS60ETjF7GoDe6zeTNxcfkS8KIR1RY8QJVnhfOZKa_WZrxH92Ox2NBTNHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m1RFd-MEAOdSih9_gjYkVReD3K0CzWf1RECa2eUwg_c-S73zF4cJQD7OjawDtjXEZS7J_j8JqnlQawDRjrLai4Hr6Cb-Arj14XT4by6tuya7T__MhYxpNcf-Sr7LjfUFvJ7oM-u0IB-eeqq0hDGowjkokPgRGKQ_sunE4GubtZ6uOXe-TqRMqr98Ourpd99c1El5gqUBJAeF3gFFabp5tGm5N1l9saNrFim9nEa3S70hkH3vtxGGcou8V2EYD4IcqdU2OxSeDCLcEa4FxL487m20zk8V5ZUtgnMHoul0zO0TsSPzFiRbbHO_tT4ONhAaeU13a73QUyjODWrrexMdLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VeOSu_Tl2Ukb4qzwERFCvpEIKqBOo6ReLTPlQjKXsSjHXmvjsr0JAAnJURaW5Za9AchafhMqvtVpW0akmDG6GxoL7blEI3cdnH3_AYrDR5F_d3rw9ba0TULME9Pf-eaaft8YZSytdkcvd-_C4rpvaVeL6McigL4ZfJxKkR1HMMDW9JDhzSOyIDJBjogAycS_9H1ebvYf98aEonz6zCHnlDu3BlkTnyzJ_Zv0virWQupdiPwy46qMYNfALc1E6wA839Wl3YHSoNlfu29lQGHHC8_Aj1_dXkSoOmPp_eB3v8RDqURpftLBZnAuq8ozwPF56fFd3Qv8kF9HmpNpw-XA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yh46PWQiZHP0Om96uZyjCgskZ7jRV9UM77nTESPSvMtirfcKqxQwkG6-OUFdvExMpLXRwLbKVAyGBrUZm1Px_lAm4qVoR6EZDIXgc2pz_eSC0xngzQky2G5h-goNk5QmyHq-eg4llIPFNB6_R1x79kfJ_Kj2cDeonif9Id5M33y2h-29eBguGac0tD1WB815H2cjxUCKWG4V8eGUplHBbQKpcUP8GynlKagFC0o0dHyDYSW7LOQhym7lXRyPqpOAea4EpFJ6x0Ptuy2pyI1zYayYyFp6pHFnd2cpX1IWz4X6_nlKnqHomk08kvGB0cKbuODxil7CdLvvBpmsSLRIfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKKp778jgyxLnf-9MXqo-mO6_eGyeRR0hUgda6KNpY4qm7c6blewkdqUHWB-zjNkU3wuI6HPCvGPP9R606bhtzNOg0MzdemxhbLiGJ9q6Aa7F56L8oynXW8zBsfTBXuhuSCD2GHoghio1FM88FxYNyWMZoyK6SovFt7DfPGrVXefsjx7eKoNFdtc0vai0S036aA4u2x8R8s7buAtVJCFayzEa9a4hBB9vXcUwXRBqHNLiRRmlrW-MuCu2kd2qulNBKsqLwYYamcJjhWhKZnq_p5B-iOD-QMomnVaBAWguWzHfJe2ibIJgOWz97xP_4Z4o6m9XtstNdYRhx53fwE1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KyS7-3Z8Q2bjrNKXQb3MJfQh9o3lvkh3VOrTJgYvq_EnppIupYmuR5ZSdeMdIf-5nGgHfUSe5qxgPO51A9AjyFeObO9G-hEVb-moU66eI8DaIOW2bWmHa60gLgf33Y6VwuWH40npofFUXy91DMRKM8JVNQ7tKkkFctIA1H1tScCVcVM0hgh-lZ1LkB1rVA3GcNvtRGSeppNOHIe4ymOOQnPnGWCtnh6aRfdm7I91IG9FP4cWz6nSkaV7AXrY5cxJVJu_td4zqGBkX46x4yqtcDv7cp0uo6Du20rDvBdtx9YmbUcG4ko7-yGQS3Q-r0sT-MrlpcQtOeVCPBRCsOB1RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e41V1aJDeuXUuD_XCWlMKS7DJLVT_eSViB_Bo9Hi2TL4Uxj3yOKz9Qlm32FekW9EV4B-pp29Kggq7hfUnkUcYS233ceuMItfB0O5I3ZVnkKcZbUzSlU1CRMSUYOyfn9fRjNjec8VWQOUBpTrx7lQsdH5QR_-ygsh0JqhyElfnuSbSWR7e8x-6Gwq2Zak4en49KKByyyHRU6YUyTVyYWvOwp0hRgCjhycBvljwgmyvmULCszHaXYWisL7J8ax0p3dKvCUquaeMliVx20zLDPqnLSnjHZlxYVOQQgnUk0QpWrHNCLR6yOru4mlacC0qGaJVve23mGBs9QjwlyFyG7xtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
قاب‌هایی از مراسم یادبود شهدای خانواده رهبر شهید امت  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/438683" target="_blank">📅 23:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438682">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051d3936e0.mp4?token=Op4kzBbBSiB02ZrBKr4FuhQKZ8t7OjPE6R5Pzurh7qo4R3y5vLn_Zohl1C6ddBq2aA6zkRu20vAvMJlFZLlgKMmUHab2LjdPogeIxfDuCue98NoDMAxNaJAM_YvawCaoxMU2BFdnii2fzOjVghNYvfyB6BbTC0z4qIDO2DPtkdbdWMpkBYh5tJ2TtMmrbqPo-VQPq6DP57JtHPr_d-2tqbMBDyjiVVWC8IpASyvpwjFCA9_60o2y0Z_q78HeIAqHsJIXdKXfC5ohYil1we3lOAcRxnT8r6Xj_dHa-51Gw92y0hPKyFpMqu-cUxWBG34vZ3yMa-hilXp704JIbX8KCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051d3936e0.mp4?token=Op4kzBbBSiB02ZrBKr4FuhQKZ8t7OjPE6R5Pzurh7qo4R3y5vLn_Zohl1C6ddBq2aA6zkRu20vAvMJlFZLlgKMmUHab2LjdPogeIxfDuCue98NoDMAxNaJAM_YvawCaoxMU2BFdnii2fzOjVghNYvfyB6BbTC0z4qIDO2DPtkdbdWMpkBYh5tJ2TtMmrbqPo-VQPq6DP57JtHPr_d-2tqbMBDyjiVVWC8IpASyvpwjFCA9_60o2y0Z_q78HeIAqHsJIXdKXfC5ohYil1we3lOAcRxnT8r6Xj_dHa-51Gw92y0hPKyFpMqu-cUxWBG34vZ3yMa-hilXp704JIbX8KCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گرگانی‌ها در سنگر خیابان نماز استغاثه خواندند
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/438682" target="_blank">📅 23:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438681">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🎥
بذرپاش: استحکام درونی، جنگ رسانه‌‌ای و ادراکی، جنگ اقتصادی و تغییر اهداف آمریکا از حمله به‌کشور، ۴ عرصهٔ پیروزی ملت ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438681" target="_blank">📅 23:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438680">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا امروز مدعی مصادره
ٔ
حدود یک میلیارد دلار از دارایی‌های رمزارزی ایرانی‌ها توسط ایالات متحده شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/438680" target="_blank">📅 23:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438679">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902d8966f3.mp4?token=j-F6B0OfB5wf4V2AuzRGog6hzqkcvxY3BfD2tzJtiXN8Co2rXRVtwCT1HRf8K-HLGELdKoSlcolmtggFWhevBgESttGImiWg7COQkaiidet41Y9VGqC3PH3s4MOyn4XZI3ivbd_hJkrHK6c-fYKxJ3RpjLdMME_QXriSk9sxCWM4alLrayXsa-USlRSz9IYfSMzkAG7Zy1SRlMWmDNjqZTtloNj8D0GhEi3uAEwj1v2sckfdqZWM6L3gmKjKlXX8coUwJ1xuch9bv7ZMyCeTqisHSwbCSptuX5D8cjrnvRVIOcCXCX2gZ2o_D5Bp4-tLwMT5SwvoBNy3Y_5NVe9wnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902d8966f3.mp4?token=j-F6B0OfB5wf4V2AuzRGog6hzqkcvxY3BfD2tzJtiXN8Co2rXRVtwCT1HRf8K-HLGELdKoSlcolmtggFWhevBgESttGImiWg7COQkaiidet41Y9VGqC3PH3s4MOyn4XZI3ivbd_hJkrHK6c-fYKxJ3RpjLdMME_QXriSk9sxCWM4alLrayXsa-USlRSz9IYfSMzkAG7Zy1SRlMWmDNjqZTtloNj8D0GhEi3uAEwj1v2sckfdqZWM6L3gmKjKlXX8coUwJ1xuch9bv7ZMyCeTqisHSwbCSptuX5D8cjrnvRVIOcCXCX2gZ2o_D5Bp4-tLwMT5SwvoBNy3Y_5NVe9wnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسابقهٔ یک آهو با قطار در میاندشت جاجرم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/438679" target="_blank">📅 22:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438678">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0AXEqLUEMD6nsCaYLIeAYQnMR4U3Nu2jVjlSVWQorU_kW8fxeyvdaycSXLL611MR6s1n3N6XuukjKCpmdoLcPtsr9WWLAi2O_InS9WDJigqrRigKXMaslLJdBOK_ddE3DWzo68wxmWE2K3QjbUtDAlvRv8gegmlHSg6DQw0D-54qOj4TnPnfACyP6CAzQLEhj9UVnq3r6wrNOqUZBRVb7K3SP5ez5htdfG6tlHjwiR4IeLSug1EEdCQK42GwoTj8t4Uw_pD4GCZQrkisXEqtEDG9RBU2Nd6HyywV60wzQNL8JyynXtHqShrG4uXK727F14pnIiHEgtOVokov7xRIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو شورای‌عالی انقلاب‌ فرهنگی:
امسال تغییری در تأثیر معدل بر کنکور ایجاد نمی‌شود
🔹
سعیدرضا عاملی: طبق ضوابطی که از قبل اعلام کردیم، هر تغییری در قاعده سازمان سنجش باید از یک‌سال قبل اعلام شود، بنابراین امسال تغییری در مصوبه نداریم و همان اثر قطعی معدل یازدهم و دوازدهم پابرجاست.
🔹
دراین خصوص نظر رئیس‌جمهور بر بازنگری مصوبه است و از این‌رو در اثر قطعی معدل یازدهم و دوازدهم برای کنکور سال آینده بازنگری خواهیم داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438678" target="_blank">📅 22:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438677">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b9aba9ed.mp4?token=JxTEPDfs6BP2xLjoCgRQN9PkLgjjzZXzE7WCCqGgalEQgW8StAMh1O3Xn7voRCBYzumjPoYaA71P5Y9yZLJo9VJggVj5PMuaXqt8suonEwORruRYzl2j8V82G-Kqma_NgJKYyGuYW_jpwiNasV3UOpaqPjAmc1CyKOVNg5bhGjqkQLHCNfOm_T2OQjmKJ079Wsk1gNwd6T2DkbsIsanwDEg48QeYkm2JXau6uf08gw6taO5_zChyVsxE22uvGTb2iNEuctHl_3YhIGbgPYa8Y0oF_yq2FQfnvu8noh44RrRU54W98Q3QW38HuRLpEusIqanuEOwKPbc4ciZky3R_iSWHTb6pY1m54OtpgThMxmMBUGhG66UrFnnISKV-U2rvJ0xfhTkJxr7Em7uMUyhTEin-htp00QJ00iLewTrSxFsW6sMZHaTCNGYLAQGpVYMc_GHVMqD1tnX1O9QAsAF9O2_uoxu2AsRsyDdivrJGcs2us6YN72v0pa202mDFVj7N4gPbD3QxI60Uoxw6ldbHjksXbLvy0_lVlRQz8YcRC_RYtbYkg_ySCCMkDI1NtBlcCaj-X9FExBEagcpUuHyUCpqqGMdv06iOILIFJEIPvCHH6Y1WHAtuIYFHuH1OUX-sU4-3rPdtUgXl8_RLoOaDHg0f2ywFwKt6RLnly6KFXV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b9aba9ed.mp4?token=JxTEPDfs6BP2xLjoCgRQN9PkLgjjzZXzE7WCCqGgalEQgW8StAMh1O3Xn7voRCBYzumjPoYaA71P5Y9yZLJo9VJggVj5PMuaXqt8suonEwORruRYzl2j8V82G-Kqma_NgJKYyGuYW_jpwiNasV3UOpaqPjAmc1CyKOVNg5bhGjqkQLHCNfOm_T2OQjmKJ079Wsk1gNwd6T2DkbsIsanwDEg48QeYkm2JXau6uf08gw6taO5_zChyVsxE22uvGTb2iNEuctHl_3YhIGbgPYa8Y0oF_yq2FQfnvu8noh44RrRU54W98Q3QW38HuRLpEusIqanuEOwKPbc4ciZky3R_iSWHTb6pY1m54OtpgThMxmMBUGhG66UrFnnISKV-U2rvJ0xfhTkJxr7Em7uMUyhTEin-htp00QJ00iLewTrSxFsW6sMZHaTCNGYLAQGpVYMc_GHVMqD1tnX1O9QAsAF9O2_uoxu2AsRsyDdivrJGcs2us6YN72v0pa202mDFVj7N4gPbD3QxI60Uoxw6ldbHjksXbLvy0_lVlRQz8YcRC_RYtbYkg_ySCCMkDI1NtBlcCaj-X9FExBEagcpUuHyUCpqqGMdv06iOILIFJEIPvCHH6Y1WHAtuIYFHuH1OUX-sU4-3rPdtUgXl8_RLoOaDHg0f2ywFwKt6RLnly6KFXV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش اقتدار مدافعان امنیت در منطقهٔ غرب استان خراسان‌رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/438677" target="_blank">📅 22:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438676">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b359eeb3f1.mp4?token=OxismQkym7fH0q3R3WFKxDb3lj6TqSUyK_iyQ_oMdnEq-LMRIkhtldzdIDu7ZFdvBlu2nCae7kW5RzttF5P3X06n7WvoDzxp91HW4bDqsuM-OlYbr0Uz6hpByzLbzOmgNy1JA-gDJZsUZcd8pWpgBjX8AFzd0VC9Yv6AU5aFfwnr1P9jKdUddhsC8c8ictEFgsWy-kw2c8cuyUUwtWHNpeCczlmoQFLqM-0GT7zPI6slYcMKvl9FwTtbEv6fgGLWrGiR4qIAJRu3jp6Kak44tk96_hmXFEqaIJG8QgItcTCrA1dhNEaA9NtBXBbYuFus0HXbBbUHU4FmdSKDcn1tCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b359eeb3f1.mp4?token=OxismQkym7fH0q3R3WFKxDb3lj6TqSUyK_iyQ_oMdnEq-LMRIkhtldzdIDu7ZFdvBlu2nCae7kW5RzttF5P3X06n7WvoDzxp91HW4bDqsuM-OlYbr0Uz6hpByzLbzOmgNy1JA-gDJZsUZcd8pWpgBjX8AFzd0VC9Yv6AU5aFfwnr1P9jKdUddhsC8c8ictEFgsWy-kw2c8cuyUUwtWHNpeCczlmoQFLqM-0GT7zPI6slYcMKvl9FwTtbEv6fgGLWrGiR4qIAJRu3jp6Kak44tk96_hmXFEqaIJG8QgItcTCrA1dhNEaA9NtBXBbYuFus0HXbBbUHU4FmdSKDcn1tCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحه‌سرایی محمدرضا طاهری در جوار محل شهادت رهبر انقلاب در رواق کشوردوست
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/438676" target="_blank">📅 22:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438675">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6e4ebc61.mp4?token=uK54b0YOJ5e4QQun4bhGAVypGhG8ro4iBEOMqcq4AcQBbWOwgc-FHm-fokClx9Z0YcAz7Ya-tGRH_HSxbqDQ7dMOTNt1iCcMZFksjEi4z1LHdWIejYHe7OB5RFkfUiwtifkuDQ9TjGiItd87Y4BlwsoOkk-GE1Qtt2NwT6HnFHmTMIB--eWh-qbJOMqLSqh3whcCRKPZ9rlSo5qMHq1L25B5OujttnyFFhNNwzTFAM16zm5Wk0xLi6JUqeuFVf2anxAdPTCY48N8-NP_6thp9340YWcNmBRkcKL9qbc4vs1Px_pj_mi17kzRZ_ykKjwmD_7sZNIgbiiQ9zzLT9ADbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6e4ebc61.mp4?token=uK54b0YOJ5e4QQun4bhGAVypGhG8ro4iBEOMqcq4AcQBbWOwgc-FHm-fokClx9Z0YcAz7Ya-tGRH_HSxbqDQ7dMOTNt1iCcMZFksjEi4z1LHdWIejYHe7OB5RFkfUiwtifkuDQ9TjGiItd87Y4BlwsoOkk-GE1Qtt2NwT6HnFHmTMIB--eWh-qbJOMqLSqh3whcCRKPZ9rlSo5qMHq1L25B5OujttnyFFhNNwzTFAM16zm5Wk0xLi6JUqeuFVf2anxAdPTCY48N8-NP_6thp9340YWcNmBRkcKL9qbc4vs1Px_pj_mi17kzRZ_ykKjwmD_7sZNIgbiiQ9zzLT9ADbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«شاهد ۱۳۶» این‌بار به جمع مردمِ میدان در سنقر کرمانشاه رفت
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438675" target="_blank">📅 22:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438674">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c9039a3e3.mp4?token=TGa_BHWJOYdq-TBIq9LgP1b4jln2tOHA6Tj_3amE6PUk4zdtAhUVXCWzQj_hv2H0No8maRWmqK_HBSinUfdwOcxsTkgT4giw3TQSzRoXhfAH26RjwAj_ddFvLZF_Yl-E4eAIi4frjQMxzMKL771nSYFNElUVMlKzwe2AIyXoE2rMMuvQ3rWpujekGDWil7kAKWO0jZBfWwXd4DRgXGnV1DDIE7D1cGMR5ZM2VRPMmLwKDTM-1RnKdIgeVdlm-b7uGgAPP3Ed1cMCN-_lFQolrlUMYku7GiOtdLTu87Hey89pT3hpSBY2caktTsS-_Lt1CkTTI19cuuf7jqAKh8Kl1Rro4BnGUT5RGPCDmGX7IwS1fVAVfcctBLvrOMJty1GE6Buazbgmpk4sNxZb9nuBtsD9P-2QUQOA2tE30bIkxvEVeSpuyd5fBF4ZGbmooPLM8f9r6dE-h3S9_GeQfQWuuO-YruU8k-jDoYEubHlRXZR-oLjseqxA4tRidx-CLPKZNlVHoy-YFrK4-FqHroCX2a_PG3_MUExDQ4pcSWBccRrRBQPAI6iDcvEFDoGgt4h5WzBLfArB_h0P3Zvj4wDHL_eUVedYsUKqIY4mkc45kDFu3IoWcYJpr3ef09_kYQL4qyjCYvYHbhfKVmaOmku-YezTOpZQR-5IJOccuYtEPB4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c9039a3e3.mp4?token=TGa_BHWJOYdq-TBIq9LgP1b4jln2tOHA6Tj_3amE6PUk4zdtAhUVXCWzQj_hv2H0No8maRWmqK_HBSinUfdwOcxsTkgT4giw3TQSzRoXhfAH26RjwAj_ddFvLZF_Yl-E4eAIi4frjQMxzMKL771nSYFNElUVMlKzwe2AIyXoE2rMMuvQ3rWpujekGDWil7kAKWO0jZBfWwXd4DRgXGnV1DDIE7D1cGMR5ZM2VRPMmLwKDTM-1RnKdIgeVdlm-b7uGgAPP3Ed1cMCN-_lFQolrlUMYku7GiOtdLTu87Hey89pT3hpSBY2caktTsS-_Lt1CkTTI19cuuf7jqAKh8Kl1Rro4BnGUT5RGPCDmGX7IwS1fVAVfcctBLvrOMJty1GE6Buazbgmpk4sNxZb9nuBtsD9P-2QUQOA2tE30bIkxvEVeSpuyd5fBF4ZGbmooPLM8f9r6dE-h3S9_GeQfQWuuO-YruU8k-jDoYEubHlRXZR-oLjseqxA4tRidx-CLPKZNlVHoy-YFrK4-FqHroCX2a_PG3_MUExDQ4pcSWBccRrRBQPAI6iDcvEFDoGgt4h5WzBLfArB_h0P3Zvj4wDHL_eUVedYsUKqIY4mkc45kDFu3IoWcYJpr3ef09_kYQL4qyjCYvYHbhfKVmaOmku-YezTOpZQR-5IJOccuYtEPB4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محبی: از مردم می‌خواهم ما را دعا کنند تا نتیجهٔ خوبی در جام‌جهانی بگیریم؛ امیدواریم یکی دو مرحله صعود کنیم.
@Sportfars</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438674" target="_blank">📅 22:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438673">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21f190dad3.mp4?token=sL87mAZRL9X0fiDD_Q767QcUCx7FlK1kTLgnHLWkuqZetQ-CHGtp9gDKARUb2pBZ_cvZl-J8Vu7YZO0uiAsilePahlqt-msy-xWcpi7PtDEDOm3dk6TcEZcG8LWGec4wrauQZtcC3lKtK1IFTG9NqEN0r3NzMFdF8hIxpUMlU-hnQl2l7A-M4VpGzDTLzA1wTTgUIKUuguMrZy1D3sUqtG0zt3m5Q5ERCrgOS2ynQaHUpQWQueWtIScZ0K8ZCsruCPu9-bu4kJeskKpjPWDBbTFmHd7EpVqEO01ys5WnFWog70_nE4mSXdr1XyD3Blj9IwSxRjSr2E26zsPgzzKHdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21f190dad3.mp4?token=sL87mAZRL9X0fiDD_Q767QcUCx7FlK1kTLgnHLWkuqZetQ-CHGtp9gDKARUb2pBZ_cvZl-J8Vu7YZO0uiAsilePahlqt-msy-xWcpi7PtDEDOm3dk6TcEZcG8LWGec4wrauQZtcC3lKtK1IFTG9NqEN0r3NzMFdF8hIxpUMlU-hnQl2l7A-M4VpGzDTLzA1wTTgUIKUuguMrZy1D3sUqtG0zt3m5Q5ERCrgOS2ynQaHUpQWQueWtIScZ0K8ZCsruCPu9-bu4kJeskKpjPWDBbTFmHd7EpVqEO01ys5WnFWog70_nE4mSXdr1XyD3Blj9IwSxRjSr2E26zsPgzzKHdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع با شهید سراجی‌نژاد در حرم بانوی کرامت
🔸
شهید اعظم سراجی‌نژاد ۲۳ اسفند سال گذشته در حملهٔ دشمن آمریکایی-صهیونی به منطقهٔ مسکونی به همراه همسرش به شهادت رسید و پیکر او به‌تازگی کشف شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/438673" target="_blank">📅 22:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438672">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9ec753f90.mp4?token=HOODlZBq_CmNrUYDVnga8Kejr1X0qyggiSUJ1Wa9CUVkBEllVQfQqd3Ju35Fa7T1kWn_LLzi6ol3DcpYyJm2a2wb343CHai2vTT58cbw_z3JkJ2UEAlM9VK_zms6NLuCfZhtPhGVmg-IAbpTzHrQCoi1Jambelauv5H5FPVTsRH-2tNA2xn0x95OsYRBDQISvdDZZRG6CekfpSzlVi3knemtt1jbq0WrB7_SYNRFbDD5rC_R4kBtKd1sP5bmBCOzYqXllHL55F7yFwOCiUxhpGg1yUaGtopXQ4onFY97ZCpvGDAukxnvJREN-XQI21moP2nhppZ-AC6w20MJl5x5xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9ec753f90.mp4?token=HOODlZBq_CmNrUYDVnga8Kejr1X0qyggiSUJ1Wa9CUVkBEllVQfQqd3Ju35Fa7T1kWn_LLzi6ol3DcpYyJm2a2wb343CHai2vTT58cbw_z3JkJ2UEAlM9VK_zms6NLuCfZhtPhGVmg-IAbpTzHrQCoi1Jambelauv5H5FPVTsRH-2tNA2xn0x95OsYRBDQISvdDZZRG6CekfpSzlVi3knemtt1jbq0WrB7_SYNRFbDD5rC_R4kBtKd1sP5bmBCOzYqXllHL55F7yFwOCiUxhpGg1yUaGtopXQ4onFY97ZCpvGDAukxnvJREN-XQI21moP2nhppZ-AC6w20MJl5x5xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور دشمن شکن گنابادی‌ها در نودمین شبِ بعثت مردم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/438672" target="_blank">📅 22:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438671">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ul-svUyj31Ew84U2Z95NJf3C5oiULdmElx9I4Xlav6i9yBrG-E4yT_bmggf49Xan0ipvTJr-2Ha2ncosb_LXACvYfwe6t2_F1e3Kg3NejHeqfL0DpXUyU5wUpz4N9TMWhxmQKAmAnxkCsgKj6tCzt2Bz4atdkkueESsGeEE1OAJPW_6PDeNB9dc__CKiic9agTxhcuO-Kt91zQ2BG2vWN8TFti10RTuK-mbvNixRzMpXne5esDYZNoSq1YHeQQMeX-KQCgH4PijtyELv_IDJOrvZa4WWY8y3_nXGgAxWFb7UNHphUSzK2k9T8QOw0H1T7CBtDV2NAehCMZ7GHfiSog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقاب اصفهانی: صرفه‌جویی منابع کشور را به سمت توسعهٔ زیرساخت‌ها و تقویت اقتصاد هدایت می‌کند
🔹
رئیس سازمان مدیریت راهبردی انرژی: صرفه‌جویی هر خانواده ایرانی، حتی به میزان یک لیتر در روز، در مقیاس ملی تأثیر بسزایی خواهد داشت و کشور را از واردات میلیون‌ها لیتر بنزین بی‌نیاز می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/438671" target="_blank">📅 22:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438670">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یک ریز پرنده در آسمان قشم ساقط شد
🔹
به گفته منبعی در پدافند هوایی جنوب شرق کشور، در پی فعالیت پدافند در جزیره قشم یک ریزپرنده مورد اصابت قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/438670" target="_blank">📅 22:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438669">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72d408fca9.mp4?token=e-amzalnbwmrppJ3A_YIVpEPyfV7MKsrpv0HRZX1s3XZmxf3n6MvUUnAlrJrZg3HtA9rMCzclrBQQokLiaN3pXoyYH1lnQ2-SuLFIVMf2UwOjUQaQuISCUAuk0pcYzZctXsBHfMCib1djhe7sY846GFyeUOac-9IRwDpxMXsBChojNfoY3_PAbu00xviNdAakjJhLqm2vsUvRmLAk2RxbI5nVAmGJ9qtprlUDIeeGy_sHfL5mLd9xapYlHqUIUZZus3LYR4EBGSu_F0xzc2XOmSFSsAqV8IEcgafoNY8Pf1MbWorjDmffxK50w5xvxSw1iwYQ7l9AZ9zInZotvyi5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72d408fca9.mp4?token=e-amzalnbwmrppJ3A_YIVpEPyfV7MKsrpv0HRZX1s3XZmxf3n6MvUUnAlrJrZg3HtA9rMCzclrBQQokLiaN3pXoyYH1lnQ2-SuLFIVMf2UwOjUQaQuISCUAuk0pcYzZctXsBHfMCib1djhe7sY846GFyeUOac-9IRwDpxMXsBChojNfoY3_PAbu00xviNdAakjJhLqm2vsUvRmLAk2RxbI5nVAmGJ9qtprlUDIeeGy_sHfL5mLd9xapYlHqUIUZZus3LYR4EBGSu_F0xzc2XOmSFSsAqV8IEcgafoNY8Pf1MbWorjDmffxK50w5xvxSw1iwYQ7l9AZ9zInZotvyi5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضدِّ انقلاب با عددسازی پرتناقض دربارهٔ کشته‌شدگان دی‌ماه به دنبال چه بود؟
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/438669" target="_blank">📅 22:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438668">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🎥
وزیر نیرو: به رهبر شهید انقلاب قول دادیم مصرف را کنترل کنیم
🔹
در روزهای جنگ رمضان علی‌رغم حملهٔ دشمن به زیرساخت‌ها، با تلاش نیروها خاموشی را تجربه نکردیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/438668" target="_blank">📅 21:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438667">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c9bba9e4d.mp4?token=vKOthK5_lFnTJi2CqIxnjG08HKgpArMMMfj5nLn4Ay--hc8veLdr8A9P7nPJmV0kzBS836twrDd98gA6MMoyWiDxl8dAozN92xBfuDG6mQVvPDJUZCc6-TpYlwHR_7-07-7vzfxLOsqOKgcrTlNI0rMALC4DdoJRzHZxkAyxBMtRVfRm_MMYNqknhC5H8VBy7-V0Up0CyP8nbnX9___2cLQA4FC0fSEf0-XeHeqCdBUzh6I3E9L0ihkw948n6AAAPsa1lPl0Vib-Me7Bpdgx9qgW8VuLOltn9yARqG5tdYtPipcF42FUtEwpUlqm2snb65fdoP9W-K7vwXAb7OsHBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c9bba9e4d.mp4?token=vKOthK5_lFnTJi2CqIxnjG08HKgpArMMMfj5nLn4Ay--hc8veLdr8A9P7nPJmV0kzBS836twrDd98gA6MMoyWiDxl8dAozN92xBfuDG6mQVvPDJUZCc6-TpYlwHR_7-07-7vzfxLOsqOKgcrTlNI0rMALC4DdoJRzHZxkAyxBMtRVfRm_MMYNqknhC5H8VBy7-V0Up0CyP8nbnX9___2cLQA4FC0fSEf0-XeHeqCdBUzh6I3E9L0ihkw948n6AAAPsa1lPl0Vib-Me7Bpdgx9qgW8VuLOltn9yARqG5tdYtPipcF42FUtEwpUlqm2snb65fdoP9W-K7vwXAb7OsHBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌هایی از مراسم یادبود شهدای خانواده رهبر شهید امت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/438667" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438666">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎥
«قدرت ایران»، پیام ۹۰ شب حضورِ مردم به‌دنیا
🔹
خون‌خواهان رهبر شهید در شهرستان پاکدشت استان تهران در نودمین تجمع شبانه بر لزوم تبعیت از رهبر انقلاب و حفظ وحدت تأکید کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/438666" target="_blank">📅 21:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438665">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjrdP2tuLmBFFd7DrT7swmWSwi5d1OiZmd94dfVuDPXXji6CYcoz00BlAFVnW8OxsHlG7VmVdblH9SGDXpBbsP-1dEQBXUmr4AAhb_oXF0Si0So1heNMo0hRXUb7PygXclhVA9S-IrBUpQ8XAp2Am9X-7y7_IZk93VrBbK0Hipi14BB97F9NKRPfHQ_ihARigX5THKvpH62FkXURTH1-11sV-kKrRmaJYVtYgc19AxFSV3Y5ikGMycjzZEKswlsC9KizRVi45sh-cYpuGgiosE3r6Wo2JD_J14KtXeGciOmda0lRyV5qVFShZG1BqpWjqC9T7094GhAFV7roYs_5iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوان گم‌شده در ارتفاعات آبعلی پس از ۷ روز نجات پیدا کرد
🔹
هلال احمر استان تهران: فرد ۳۰ سالهٔ گم شده در ارتفاعات آبعلی، پس از ۷ روز تلاش نیروهای هلال‌احمر شهرستان دماوند نجات پیدا کرده و جهت اعزام به مرکز درمانی، به نیروهای اورژانس تحویل داده شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/438665" target="_blank">📅 21:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438664">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd01d1fb90.mp4?token=Bil0VaKaSJ2XMgXKYUe59kt8UOdheoHbe677FJuGYR-CyphzAveoSFrlHRk66FZEaYtDp5GkaIYhLeWf_bXIj2S43ldI5E0xPLxvmqsOjOlpXZYeyz3vmzlNTcFcDAZ2GmIunMgDrOn18yLkviJtQpZUqn1P39Y0WYl73wj3rxr0D-PTEjvz2OUwOufpva6P37fbNbN-ZtusAVwqH9R0y8h4ZvQc1f6hoX7Ax_ZRRiZwUbldMfk3MOP0W7tLmc7NtbpS79m6zYdEQI7-Ujo2bCMtjqbT1fdpdCvI1CUlROApFbI9hOooLoydGyPcxKjbwNoPeuiOKK7iPtE3lu1VBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd01d1fb90.mp4?token=Bil0VaKaSJ2XMgXKYUe59kt8UOdheoHbe677FJuGYR-CyphzAveoSFrlHRk66FZEaYtDp5GkaIYhLeWf_bXIj2S43ldI5E0xPLxvmqsOjOlpXZYeyz3vmzlNTcFcDAZ2GmIunMgDrOn18yLkviJtQpZUqn1P39Y0WYl73wj3rxr0D-PTEjvz2OUwOufpva6P37fbNbN-ZtusAVwqH9R0y8h4ZvQc1f6hoX7Ax_ZRRiZwUbldMfk3MOP0W7tLmc7NtbpS79m6zYdEQI7-Ujo2bCMtjqbT1fdpdCvI1CUlROApFbI9hOooLoydGyPcxKjbwNoPeuiOKK7iPtE3lu1VBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشت پرندگان مهاجر به جزایر دریاچهٔ ارومیه  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438664" target="_blank">📅 21:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438663">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXzMoj1kNukoMAeQ0-Jk1PmwVHZtk82m3s9yCdu4vqexDJnXDbxQnEZK_GrP9UzO4XBaV8zZ7CHw786cHcYHTJ0B6wZJlwyo9qthLYAzkCIcF1WfBIBglAnU-ay65mVIFonJmjmR70SdJPtD9URa2I2q86OQGixNG8edK0kMM7tDEu-kfLAXHk57C-9x7Ay_FlHCUyWI6Q8DGBjfDRv1GceD0Dlr_jgmEI8wsHHqmOpjnVedlcvsg6aoSXHLSp0xNzBU4X9GBamLgrLasfbXhoxy4cqAKkkCmMQfDY5LhuuTxB7WrP-zb5DU-4f39Lac2p7dCRBYTGRmmWE0tF4oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گلزار شهدای میناب، میعادگاه جدید عاشقان  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438663" target="_blank">📅 21:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438662">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnGZdhmSNtgdLP8u62Dx5L2J7-pVO7rYiV-QUSRgdfq_sEIS844VCbtmbwrnGSmv8GLUBm98KrrA6ISxKqTQJqxIAUmYZuYKbOq2njy2w_8AE5dhFHvWVIG2v98HmYjzl_L5du3oemmL74XIdgYc8_g8mYUjjKzknE9f-FPxK4i8A82-jgSvMK-q3PZba8Cv8fo70g2riM3fTxEvBwyZkVpd7vc88VSPQBoR0RaLAtLlBfEwwJDUeuk5WhkYZoDOuf7Y0meKlBY1_E6X4LFfc8VZ-NVkz5LncBA12BDtmk2wjOeDt6dc3D3H1UgdSqeh-KUNSCidzGdagFAjG5fy6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی سه گله ایران مقابل گامبیا
ایران ۳ - ۱ گامبیا
@Sportfars</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438662" target="_blank">📅 21:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438661">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‌
🔴
بقائی: آنچه آمریکایی‌ها به‌عنوان محاصره دریایی از آن نام می‌برند، از ابتدا یک اقدام غیرقانونی بود؛ هم نقض آتش‌بس بود و هم اخلال در آزادی دریانوردی بین‌المللی.
🔸
باید ببینیم در عمل آیا واقعاً به این حرفشان عمل خواهند کرد یا صرفاً یک ادعای تبلیغاتی است؟…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/438661" target="_blank">📅 20:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438660">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: ما با زبان «باید» ۴۷ سال پیش خداحافظی کردیم؛ هیچ‌کدام از طرف‌های غربی وقتی در مورد جمهوری اسلامی ایران صحبت می‌کنند، نمی‌توانند از زبان «باید» صحبت کنند.
🔸
ما براساس منافع و حقوق ملت ایران خودمان تصمیم می‌گیریم. این یک نکته است. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/438660" target="_blank">📅 20:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438659">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: تبادل پیام‌ها میان ایران و آمریکا ادامه دارد، ولی تفاهم نهایی نشده است. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/438659" target="_blank">📅 20:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438658">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwYu_j3VJP5EXbTh5wGuju2YlZuPEGCDuNfC4mtTjEeDbZZf91o9U4giYAYGlU5sCACfa6ciM1bhb3pZzkVB548lbMFEbftY-PDy0grH3EoZl1-TMYItPhWhTfAMQyMJr57kckqK3yYy4py7OVWLQ14c_iGjIUbY8KYQaQzlcHomyRwKblo0dD7Sjvc08uTctukD4vAR6PmIuWdmq8R-eXL3y72irPMOG9e73yrEtqNfOwOM2GkyDctnNw1SjBjqylqc5Cm0kWN1f5x-yqfUw7G5jZj_GnfIn8rdKRn2AP9YkKk2oZIJHJs4MXiMZZq9aOD0Lgg2mBXlg0s9gSyyVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو: عملیات‌های ما محدود به جنوب لبنان نیست و به بیروت هم می‌رسد
🔹
در حالی که دولت لبنان همچنان به مذاکرات مستقیم با رژیم صهیونیستی دلخوش کرده، بنیامین نتانیاهو نخست وزیر رژیم برای اشغال بیروت خط و نشان کشید.
🔹
نتانیاهو به صراحت گفت که عملیات ارتش رژیم صهیونیستی محدود به منطقه جنوب لبنان نخواهد بود، بلکه این عملیات بیروت و منطقه «البقاع» را نیز در بر می‌گیرد.
🔹
وی که نظامیانش با ایستادگی اسطوره‌ای نیروهای حزب الله مواجه شده‌اند، مدعی شد نظامیان صهیونیست از رودخانه لیتانی در لبنان عبور کرده‌اند.
🔹
نخست وزیر اسرائیل با این ادعا که نظامیان رژیم، «بر مواضع استراتژیک مسلط شده‌اند» گفت که صهیونیستها در جبهه البقاع هم فعالیت می‌کنند.
🔹
نتانیاهو بدون هیچ اشاره‌ای به تلفات نظامیان صهیونیست در جنوب لبنان، ادعا کرد: ما حزب‌الله را بی‌وقفه مورد حمله قرار می‌دهیم و عناصر آن‌ها را در هر رویارویی از بین می‌بریم».
🔹
صهیونیستها که به شدت در حال سانسور تلفات خود در جنوب لبنان هستند، اخیرا به هلاکت هفت نفر از نظامیان خود اعتراف کردند.
🔹
حزب الله لبنان در هفته جاری موفق شد دو فرمانده ارشد نیروی هوایی اسرائیل را به کام مرگ بکشاند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/438658" target="_blank">📅 20:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438657">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌ رسانهٔ نزدیک به منابع صهیونیستی و آمریکاییِ آکسیوس مدعی شده که توافق با ایران آتش‌بس با لبنان را نیز شامل می‌شود.   @Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/438657" target="_blank">📅 20:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438656">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-50.pdf</div>
  <div class="tg-doc-extra">3 MB</div>
</div>
<a href="https://t.me/farsna/438656" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-49.pdf</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/438656" target="_blank">📅 20:45 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
