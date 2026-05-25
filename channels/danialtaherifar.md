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
<img src="https://cdn4.telesco.pe/file/QoT5ydiE8Q-P8AABQXcwfgSRhK_9QiBCm0GAsd_YKrRiDqiD7SbiAJZMRGxGBYlm9WOSlxRXw3eFCPBJXvWKjGVqW7Z1ifAbt5SjrUEUr8O1dd-549z0MAZ_j9bMcgpKErUqVgCo5cos6WGK-7UQ8rK7QoGOO1CDqI6TF4At92UxtNWYL-gu4Hu8VjK4uqEZjJjCya7pAxhiqPvxpWiXxL8QBo4eF0zJoaAhvUM_kwHl4Y7m6Hqc0JXQN8DaUjTMBLAFWYht7UFNbRbqLhscWEk2kL_2LxiL9FhmuP1ycmt5rhoPlUg6I2Y_oWU7usW3afeVj7ZKPaNTQS0trQZ2NA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 20:30:38</div>
<hr>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 233 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzVLZY6wYMEXxPonk26ZgJ12jtA380Uw7gtOO0jPvI0fC64XMZuLCI0YAs0f-OdRprHJMfdjxAFSVarpJ0uHACZYa3wOW00JutbuRvAryTCJvbdCmZU4meeQz2lRz_HPcN0-9Hp7uxaBZpzYgrd0ECnc6t6fjsOY9hKN9goYTMGBCATEkBaassyr6OQWgkVxqGyqtVjgGMswpqGS_6RYlrOvDi8kl-8kEkZb4dwZku8XzL4Sc5_Znr_-NvsmSuwp8R9yj2YEeFFUnjLobZvtq60ZSFcJXK3-enzn1G2MOabvfBB4zYhD5sCWNkFLlw6xFcfO3wT2mNgWrZ1CO5Q5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 299 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 676 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9dqqaZHU8izxM5zbW-crZYedCaCr4H8KUHXThZYGBPbCjjj8OH5p94jBM1CDDMwHfZcbl0zSB2ZrNyFda3Aswy3ni4mgZyWht-5aaRY3mwkH_Yh5I7O8mW0x9U8dL6eyAQW7bwTEYJGYs6arzrlqw_rjmm7D_ZDgciQZ3a1tMs8Yi33XKnHSFfHNmGX3TtfitZAIqGprlLs-rY3NkfcxSB5pYv0O1iSlrI_wYPnCi2b4tksmqvhF91ITMo44PrfFGOWo_YoL-Uy4sDKXHxQIoRhBzo75CWqccnqPIzSgCP9RW1QxpoFNIw_AqOkHCLVU-iGQg-CQVLBdntbEv21og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 635 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 754 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgfMJSRL9GTF2L4YCNeMnjfV71cX61G37tHAb3iaZIdyLnnGBmWpERJ65E-eaw07Xw4dYePxOvtdw45lfi0E3nuEFETqWkQvVXugcvUB2Kq9v-hmxGPzvjiGIeNXKNPil1yd_fxgXKXB1caZdamXjR5zFb3Y9i211s3cLVrl-DkYC6n9tTm9-EYHHo9KTbbGuXuGCkaXpAcf7_9De4z0Ld0sq2_Ok_67czl3cEkqbBZaoeaCR6cjJ3NQ4c5HyYaZGJ4vuHrHxN7T1A-9HwQjYvTZ8qGRcEsxE-kdD0yzDQ-Id8uXdEsfeD4s_AY3lFRUqNJskfgVoce26rtFavQWYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 827 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHGv1ouSSqf1vA36iVGen6Smb5-xp1l-6DhtDDx81TE_-b3dwtpDpFbeVR1XP5KpxODE8IDC7AVLSGuEkXzDE_-R-LL781hpoWX9h74q3QpgfT0nozlxss9Mr5AQnU90GMkV3KDyBWXW_7sAy1VRchhGODrYTp5QFEdLNCtIaNB3vhs4HfZzto50-ZcKAdKjQ5ZTF3unkuB5aq7CiwfIrtIfVfHpnTFYcWFNpmIaEgxqTk9PUt7S7wv5n-SKNF16oRgtbUbZKj3kEJ3NBWqh9M5RVl8OUsfGClimf-WHyN1MHspgH2Y0M9PtRx20VCS98m2oXbcP1B-OzGapfQBSMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 966 · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq97uf9NxSUCVj8tG6pmIhmfbmIoqTwlRIQdudA8Xj8DQP_CCT96FgwPInU4z3inANYBshiJx8VySiXloIYMDHX4lT5hxza2fqtpo3gWu1QLVE2wQW1UTxUzVWgPPFsCS64SOxGqTPIM5bBi92NX1NYOIUfAiWK_0cM0_I24DcC76x9732eEohUcsIxUOiieLrkG8gjdNGP6kzsP9fsfOVbrfwKcPXuNGi_Pfd0OlkP2qgs2-NAOEYXu8JxpWj35iqnoAcr51OgrRHGr928H9z6XjUTB8hE-SPnPVvfJHvxMCyz-j02lF8vdl0X3HRYPk2vM2byYjGEuXXFo2a021w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 807 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 817 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 746 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 766 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 890 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8Rf28e5Ku3C9CZvln7f-fWS-kc4VZ5GU-HF1lSr_yJU63cTgKqDwI_TKcfh8x9Wg89JQL1DIoP9lztkbTE5jMPgXsSVDIWnp2lvCWmMLL0OMU0LF3dDfPSy1yRAT8Rwwk8YKP6pdXCMkfj_F-xtRil6NzYZN8oZHXpQUDN7YRMJJ5-v1QEFbQ8pWCeeHH2v4ydtbK2ohmZPUcu3adSck72wGYNNJukQx4l7Kor8-4PxGNqFyo1pSKkk24k-9dkJBiLD4pyYqJcDQSIySEZy9Q4wMoCcn4G57fBa-zj_I6kRVlWxh2Vz2Hrubzld_tngrNiPEOoNOzxljEgqmoXYxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 960 · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOecLlCD6MYO_CG0vmg-x4l-DI2kCTaAi9f1sOjVgbUCQx8Yg7eWD3vXD0vVD7K_VJuKsEIWMgr_VqjyW-xNoqqiX5gat5GmUb5MlRHJsXYlh3LBPCnAbQ6R4UCXwCbYRSiarKrVXgCtn67VrToQogvEjg2BnD5n26-Is1p3FgDuHbNh17ihpzvSKA1_IPsJ8mOym5y0OLZrTc016fmhs2YdIbJ2vZKqn85bGHXXPHMPoLhpK-HH8oBED5WPsmFB1hHIL67-RwswNUrnLr_JikE8hd7F66LeXHb00TVxCoAwjUUKf-_owsvIWy0OVWwfFat7Fm8OGroi5Op4OsNGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HbQ5A8tJNLvCvQrpKDPuH9cNq25v9a5iu45wYdgVX-QMtn5w3_32UuYibEARhQXw5wehaBzFBJ3MSq2bNfs2Is5AQxbJIBX2UEgGHyxYtbIWc5WN9xHFt4432weROp0wW1E8PsisP1yThcTUvLJNL_jsDsQpSva-8_s__ZUXiiuU6LwDtvGnR6OdL0lLra6kRSCjQ0GU6gKO6VRjUEMJ_n43raAeetMyLdD-JmbjADYfKxgP8mJ42hvaazA5hv4ZmwcmQ3p40RRg5rM-LNUQ5gWFcH0koVBPA37CduDK8MlLLZjox-93eiVbszVmurH0E5amdY0OnehDbKZeQq6kyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kK9wW9-FH1FSAvAivvhRvdNdQvZqJeW-uR5orU9s_L3-5AJVU4DafifpUv8XLRPhunsAvngq8novvGJpE-ySJYkUdaPyDYtsSxHHcdqzE0fKR-p25_YNoZnd5Udti5AFuqaKi1MUQPBXVzO6tje_Z56sZEA06Ux2HMFp8fYDg2TCKLAh0rQoWoFTQvQUiD2Mp4CD__bTE7NizIeSp-_JxjjFznxe7VWftp-axevg4_nnIIu4wCw05-oFzBK7JjlREaqNzihUvI9ddzsFQVQMY675cX2mE4bESsKH7zzcAlSif9RSAKJ0IfCHG_4Ujk3j6OUkLkDZnLWzqIfPZy4JeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 851 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 926 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 807 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 650 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 865 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPjpBzodG4UjXnwP1svYXoNj7Ow5Vne_l6321Gg43a137ZZ0DLZy2JNjM9ZH2KSTU3HWwZkf-j-SIXXzqCfEJWmWuREE1BvpxBkEgBeGMWrb78hvoIwQV3zAdmaAtm4WEwHvp6xQXJulQLqIZUUzo8MugwHwOYSpiKbD6iW9pOHfK-hprQM-yqpL0582_kfQ7QHfbuh-Ts9eUGNDp-aqhexT-YZ4wQkUXEOmjkvD8uGAOasaY0MyJdJYlT9HLe9rjcQuijjmEh03DKmj5B-NaHmwoZgMApjkm-8Gs2WuXNYULMInb8ytZ_0tfzyEjh2Mbziy5YJTEdqBabu2kUVKbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 849 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 800 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 751 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyWbMzZSWwjABnF6bbuJpVXKKsX7M_LI9kyu3C_iQzgJIGCnqqPQr-q65tMLzA3a2lRmFmz0C_x3xxQUqrWqejQ0UCe8X14VCyeXOmjj3rXn0HVHxa1rjIKK3_bwHH-2r3XyoM6z_Jax5jkqjcV8iBAmcvgjjii9TRXkGG2IuM8xT8_Uou_I8j3uc-eYNyRamUC4A9DItBrA9D5YzIikjAK_gESKD903aaDciDs43iFFf8G9L9jwalpvmG4azmHkas4vElFtFVOj84cXQXPgVu53evqa5lmWKkPXRJd67Lc0TTKRJ5fkAN7GI3oYcl0KZ3uYm5SESm_ONgpE6krtwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xli8MDosgjZv2oCBM9HThg-5a036r6oV0a2bQiFXLwfoW3eT2pj8z-HFu8dHBFHnosZiT_iRq_iB_M0oE6I5a76PH0aGrJeFEJsDDmNt67gtPzK-W0LtRiCKTWwtRObZR_epGj8zRzwSqr6UD_4kAAmB_xo5PnDrmbHBhtmn2dnvzqv-SJwpFMstPyoXpC4821M5F-chE-mitBJCb9fp_PCs_5PqENKHLtn7HpcqLGc0Z0J0MJfiPGLQRbCqmfUhKFKgrIqaWeA72jXKGEbWX-qCwjWfRjPmOo_d2OV_S_NJW7qnY1n2otkPDHQGOJ_Gzm9rFZQln_PzETUKxhT7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 870 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hu755jdjAs6c9ZovKPILEkA0_ZWcir7RhLEibOdiAvvPF19CtLWrS301Pye_NtEqTmd8j_xeYsTsFWY1ZjWckhe4md_4I0dHs2FwoK6mlqCL1ttFZJxWC4JRUPP9gwUHuo5pDx9FW4yLOT6GSAIjNhb9OIw-gUf_j5qHNbJEsLK0pL7TySmONj_wVoposjr6dea5UgcSjtbncsCJ4gDkSvCtvEsSQHC47GouN_cBGhD1x6Wq2iwixxXnEifqG67Kcl36rSgsDUVAoVw4PRG_Fiq2jnm_4yXkVpnZJjzKWnOanobg7P7gIittf374EbGT1H-C6eRWpUUjW49mwegjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jviKeAj9BcPvf2LgjD20ySv2_VsqpP-QP21AEdP_sulyyBSOD3vFbKqKPvAp0n4_KTQIHl59Qeo1aZKIsucVKPeOSNfIXpuToe6cE3CcBw-ylNEB6BM4TeKASrHVaSzUev6xQCy1jdpQID8EdH-0v6zHX4zMrcchZya__oINVvGFLeiv6n5ef9knrFl7Y8w_B1cupqCwyKjimoRC_RaFtAk6SgOwkhL_zNN9Kusp3iOmfQlD2c9YBWVUVZjXM2RJhtMYXT2mjjSrMBKsfbnEd8Ri4hvGtvc1vUiqm-FYLpsHWjU6zXbJ0qIUoUWZ2pmX2QWogKYgIAB3SQOaq9HBUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pqmbxo2g2640t8vZmVMw0B0snxgyF5tXZyfmDdTYZRj_dsaRRReJEk6pXN-uGMr7bfQxPFV6a8NyQNi585mZR0bo8KHg18A7f0zIqW-kUYJ9sX-KGi16Kru5ptqOeD3eK7j0LrlqM7RQpaL-2JyB1lZK9CWC0A9F0za4CnA3_2JPSZumXXXsBeQ9Wf4Ymix180USGyt6PZC2XBkN8Ocj88KdwqWC60qj4_dby1nmPdeYxdfgeuL0LQeA5gda8klqS0YuBNRFRphA79HKV2tWv50IAv9hT2cNeGST8_VwLFgVoTcVHyK9gelwiT3_vA-AX18XE77dbq9on822gsu3JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrkIZfxqMtNGzPKyZZCKYV_SqqFGpMfwkR5Ei_vc_QSDfuGUKrzul4Or9LOSyvSgYhXqkAgqdPn0sSNM6EB-ug9JRIK-5gWwNmBO6GjziK9NjNIJfydoBT3SOR275q6i7drNKmdtyl9tup6X4s1CGQwXDSpYAJpMoSCoUfmJCCAyDNt7WRGPlezBTrqWmtiu0EhnBSBNrw99Eu7cL4r5rYshaL-HuhLQDTQ4Ni5tyShdXjriq9eq1xpEjlbTT03auaOmG4Ys6KznH820jCOTe3u4vxIisN1OXq0LWP1NtmQLhPVe_I-tv0j-6PBYfeN8p-1EBad_5pmAguqST-UGeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 941 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky4qdxq5ldZvGumxsaNkrctpPQBHKyvZmfxTQHDRYGIUhClYPuQZD3C2qsJcb4gi39Z_w4VjXDQftSyEjUKnPQSgGxAcbth4EJKED2Om15CK34sT2wOKKEP1hfZ9QOmXAggVolPY0cDoZcEyZk7C3mGf4SqwaiML3O4I_8aGpH0nfTU5wVYukV6ZfubtAdfzYrbxWO8oZm7RYyGNJDJ9sSMqA83fu2bRGKI_PulGbsEHpk4TAjH3EaXrNfung_wBY6cttzGZ4xyD1BDXzqnIMxovblO42soJKjiXw762iZzfo61lWS-FYsm4iDOjKiiH2VVgJoKprRFxwY7bUnU73g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 867 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=XS3P6enPddggvJmaep44pOstxsGZLbyAAALnF7ayNK32D8YHVCMsZQeASYVPdV39_DjzWT_jCIn5ukNepSt9GD6qYzyq9J6irNLE747KjuZXTTM1eLQ_FXNY2RhxavkQ9Rv0pmFjuhw2ohW3NP36zX4xXnsUF0xPJElxCD0N9UKsqZyL-c-3j1Cw7LL3Kt9Bb_EdQZf5Gt9BihzqkZJ1V0KmrRL36vQsmsPcauRYbqyESxEFH7zGptg3Mt_JXBcspgwKt25fdNm4Cq8PyNfLTcOXBP0YWiqlkaAEGdK-ewmVmIhHQhRzVpJZQQtPnq7Uy3rWj4oJAe8d6VasKKSFVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=XS3P6enPddggvJmaep44pOstxsGZLbyAAALnF7ayNK32D8YHVCMsZQeASYVPdV39_DjzWT_jCIn5ukNepSt9GD6qYzyq9J6irNLE747KjuZXTTM1eLQ_FXNY2RhxavkQ9Rv0pmFjuhw2ohW3NP36zX4xXnsUF0xPJElxCD0N9UKsqZyL-c-3j1Cw7LL3Kt9Bb_EdQZf5Gt9BihzqkZJ1V0KmrRL36vQsmsPcauRYbqyESxEFH7zGptg3Mt_JXBcspgwKt25fdNm4Cq8PyNfLTcOXBP0YWiqlkaAEGdK-ewmVmIhHQhRzVpJZQQtPnq7Uy3rWj4oJAe8d6VasKKSFVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzFTU2SSDCt_IxbZ7LxPFEaRb6w8h7yHzHhl65a2tHDk-uEfyYnm-FGDZHdAXjwVvTlNR6mbG58_zNeOXXp6u4itXlvj2wUPUa31KP-1VLISJzt4ucsXXRyd2p4B-BPUEGQSlwNg57_eCrPD-Z8erJ6Jihrh6WZNXKgIMFsWcX5C0kahE1Ny3tnU-adADuIKWuOse14KI3lWwylCp7pXbZTNMmcYrMAXkv1BYjOMpNxbdiDD3OU0S3Hhixg4XjqK8ekDMn5wLG_89o4i6Ia3F0OqijQxhEZRhjcXLcSl7EOLyqZ09v0upWNvZnyQ3OZhSPNY4fwwo_oK1apWl0OTSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 922 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6Hxw6vnAfUk_AwTj-iBPecBp9mMgJGPnfsbrrqaggviVDomyKh_tAKl5HXNu7Qv_ZnVcmmdjicm_vrZr_M7qNvAXWd1qMiDepGGKfgMRJGZQtx8ndafQQvWPrmpyY9DLZJawwAg8QR5S_qatGEPd_jYEG4dE5TLxKe58a58ldJdZwbiIWqgSc56-SddZYJydl6tMC6--aTgvNiuvPTp00md8udyPilRs6MAEQToN4JMx4Jvy8uwOuWS0S5GqxN1pbidAi2DKVJDewM91KcOV9QRYWriRTR1ZHRcrkaGmXF9mdthQBrrkDYM5Mlj4-IdiK2Ah7R3_Cie_MPfueDBAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BbOQv0pSMShZaaFrLm1VOWkr5Pg-Ug2wBXRbK-PHX7kDKSJEjsshGOkC2cBFFKWyTPnGVP_CyJ4o2QV83DYSp5CkErz4hoOSwCzTMmQOhWnc-oCnxXHkelZbDNXOraVGSsHA6r8sfpcmshdpe0sSbDyHidg6WHMYg-X-1g8fQwXtHmn7bKghWUh4YsBOQTq1Crf1RL5XPlKbElSn2BqMBRySDPvwk-PiyuPrqVlYTUwnhQ2PXZVDSHkGMr8S3SIC_LV9EaAEdIL0T_RQ6VE4ATrzIiVKkbO_fTe_nB9SOQG0yfTRUpWuWK91LBlgXK1gVjQWwwM5crrXncYJV_hbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_hRAKp1TBBisa5ELPBn7XSKHS3pYzwfGIqm2GIZSitUM6LUXjJPTIE7UZnNTABar-hjixpSCmmPjV2xwnAqOqoojaCldluWwdGAU05_QSUvCBb2JjvOzM5pYCM3cci3YRHc2wCZWws5bGeCddPCm6B_hMxpsE0UPtE3gSZuI7LTqZI9B1_8krB5dEU3IaWBQYSo6eco6NIbrkFNeuEPq-nu0Zx2ad4hgTgEldkizOn1SrRQSgRITYHQCekHnbxMiSbjhBMhgRVRJ5sLvaN1ohAwKqXfhlrbH9iRBvA4x7c7HpcRx_a0k7V2FadmzyrXVI4S7e-WmMJ2CZsCW_AZpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 795 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 981 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiicaFq3yfkAT66dC68E15Xy2CcOkjsRYDpSl0C4IoxV90U9agZQYBl8uxzkSY6VZy-SZ_Y8l5JQ13Q8_5btmLS9mEaQBsFGXmOt-xBFlG6zznU6Mu9JayJUcX5clvheY8ccMzDyirkfsQl1Jpat5goyJHFY8-Aj0XSsDZLDo42xljKEpgNwVTwgcakcbVd7ybg253oxNNhu149R7Lc7cNGNkMLuvGDIHBmojM3bOxaHhEIBpYM7wHkEWTAcYgwMWPEwuWtIIYpU4NMQV0SeGObl-rTFs3kpsCITySiSYcA1c57NSD4NHzEJc_8gUKdHOVd_sf-867Jzc3cNz0ToZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 918 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzhKhvY81NN6pB_aY1yR5SVnaA3-bo4wiBLBph70RvOBdJZAK_ZBJjPiRdhBtS_KDd9l4wvG_7A0iffpd-jQZzWOUppiqVtCd5YBLGXhv93Twgyx9IgTlmoGxao7uEIPYMS9cHrwAYkq-A1geHGC1aA11yCO6Rq5Um8ikaC29QDZNVB4mn55hQ8Gupy9Lt6sQUpMnMq9KEVF_J8eBuLPeaKjxYY2fbdx5P6s-W1xTsQgjvj_pymX42-1fSa7H6M82V1Nu5Vkh7JTpYkjgdP3vDq8_GkY79HuqWJFxJkB3VANtY4AUwWH-hx3HGsPIGrnk329CMnjTvMmOf_9BsTwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 740 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XtCjnN6FowbjRfzDaz_VYkJG3htMrhr1JTFuBIsfiteAjqvw0sQRHNGL45BekUu4s3TUf5ynVvqVaEeeydwziei6r5p_exNP8a16owGmcY9FgyDPe91Vomg5b8bsf5QV2uGxf9iBpW_76yS7gxL0monrUzjgor8auT9dBXdEYPAPjQUn2FeK78lhBt9T_Py468bWrMPzjPOZOtX2wPOp7okFvE2yi0AeKSzr3w14Gf_NNm0_cHo1FHZDDyNOusRoX-sfcbHuTBdMqz0ncytC-zo0aOg1UWr34-B6UUG-f14xzAsAQG3P5Rf1t45GZFKa54yWucb0Z7soo36Wwgjzrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pI13De7ZMNfY_cBW08aTigpSOFpAsPNRP69PULjsgzkgzR0up8_2ZlFMI2rBCvQAow1dkySuFaZBvvsJO_1-5wPnTHaK9sI_3lSiU_Q3PknXL1uYAUoy3bXZjWsYgje_mXGCddKVZYgtCSfs2Xzxyg7foU_uhZoC2iJ1B0ZucJ6k3SFnTXsMSsMSyGm7feWbtbahMbOlK8p6l9g9Dwfrf-PM5Ru2c4KExLmCWhFLUHv7YAHYI0KPnqJXbL60dAvaCfHOMmJFRfCqxPLF_CtzOIau99JgzWp7fxUa-AildFSlcrLdQVjhN741xl4-S65Sfj3ScuE8FX9189SoIv_J6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 749 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYyX0O3LyjwXYtwtD8TB-jHL9QDflh29NVd8vAzMWrYJo2Fa8bt64R1X9XqsnO2z7d_nTqVYdhv0q1MN_H1sZ6JhEIdfjPMIyQu_bQNQCWWMzay4KtCBbr5aCKUmPpKycHNvdvrcKRixWvihu2gA92LJnaemjLRmm3e4oRGzZ9QeHl_QPqJSCQ3gjuJD_GvZoxSnOjBQBlPCDWnv2AiBrRrXQdK5ERfLC_ApmtLQdT9bEjeR94z6T7fByf2teUl-5Hgor8_9So1MLPv0PYxtLbhU8Kw1ilkyTyGL7GDicxb2QvXOlpqIJo0zK0RiJwpKb0sjQaG_TOoFNGV1NNQlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 657 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 805 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 815 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 717 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui5rTTZuryYWmNC20sFxU5eq52a80uuiiBan7k2w0BHQteb9i8diYbniZYsH4z01TTA9CKHD8y6xmDrpcAHWvrH61sHe7XlzRukZ9UAgOHvq1B46VsNmfbTJmIENw1K9WngbdKF19XTQn4ijRugqDv3vrB_87DieU3Dn6mpdMQbGlvrKUlR4C29aaCB4EOPYyliZB1sJl2rs63hYIcVJ_hOBQfc_MtI5SAcKTGCveo7kXn0Bbu_O42G00NrUNn4jbGjFmEV_1d2n3tH8jpsdrFEplhFN_TQfjPzSVBlge57qWjS4c9K_LrKtstwoI-ddytLzmPAGVjPktTKeoJIIXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 819 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvRp8lzs_CPRvYphiB8yIKoC6muWB9ctdtbSz3RRBdZ8GOs1-CfFrWzTxaRDM9wgTVrf2pc06WpkPXORduuN5UUGZoMEr4IawACbjXpI-rnne8XorBcH33MyUtSzqkwGCCqVnY0eIv4n7sRp94R2Q5uzLTc8RFezoeJgXW35-9mxikCr6Dg-Ttt-NKMh1BZTm40lXnBoMgYeFr1cG73kbGJ6NZZgz8ovw7nCDvkR1gWkdIB4W6yaZbDzBJYDV9JvWQ2O5BK-JIE2lHAtMyNSmvDJlzLVbwWWKGXXOhsbiUl4pNLYl1zq1vrKZN0yd8CLEOMoRL_URB3LhEUgnDm16A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 602 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G59e89GRhARYtkSG0_-FpzNbDq6fETpMwAyxHOU7FVFc5XE9Ph3uM4K-JPNfgaA-yIusaPSU0gqs3UMRM3aK-nCy6vrNEEmb-VGdvrRzzzC5b0j1GPQGqPwXfPDBiV77zIbqrMO_dV3RphUwvl0sAQDNM8lxZxHfraJTBDw2WtZ81vGY4LVCnKtOMehCm1CjiusUj9LCx0egownaIQOJZEw_pF_tdyiGxHFY8YOoedid9-PizZZvbCkz5c65YfmSWLfDm9oqB1DlY4uWXx-9qs-DU4jLhmTAhkeTHpogEeqoDIgJ7HX7MXUtBz-OV86H89zoAfm5ubF8cnk6TQhcTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 692 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 638 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UO-abSV20CF6IU9JzOfIv5kJINRh7bPh9XQTi2Q1Ft9A0pCPkmj2wNBai_dR1SlzGq0oI_hLfgfxQ9WwtrYStUlhvJWxia2tBg4UpbFiEkq-9YL-vKoR8S_NG_PCe0MNJt-99C04-_oI-HjBsSEO9sVLYknYrGkNnKU4v-FMbRcJJ0kfPS4YFtJvvms7ZYiTDPQ4j9i_Tz6rlt_r4yHGUyiMBmXWJpzvbGFQeCKxIIeDGHLZUNJ6ixnnRsyPg01GGc9eadZKDEO3pj10mmWTvhkiRtcN-_596Ph8zhlZv6p-Nu9Aff-Urex1vDx2yFyAm_gRl0mjyd83qhaZobwwUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vl9CDQfAutDMT4dUnY-VF1ZP-8aXQArLEe8OJXj25-eMjMMsGrE7Rd5da4V1kgzGqrkz3fbLj_cr0WE9AheOrutxpkLYt27B81CASQPabjycsWte1R39aM1F41l9_BHrr5brtJSaeHMc2OI57n70Z9AmXnW9XpsN3WNLtexcEke3rUcCpanchy3zj1MlWDQKsExsx02gAhaW1tqBE8HtrhS-QmFxOKzkJmVvU3rZc4trDs10WL979oX4J2et2Pe4GfEcABycQh9KDy2tXIIfMVoQ_h_axlKu8I6HmrAa96idaiEKcPZjiURpKUc3VEZlEo084BkoKO20QnTuf4NEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6hlx7FhYRqGlz-6gf9Mg-FeWVaWIycDUdsg39Vc9_rr9kWWaiX54udCdAkEOlXgLeySPNKSU9V4_6xqvbC2vBVHJjnrezOpQXORoX6BE2dXASQEWTIvYf846-0krg8q0FNMnRA6G9gfPh2Ngc_6qbjJj7uZbXiVTUfSW1jNouGlkn8QVQ0jnmtW-MLf0On3RajPFW98JVlfUJATNl4D17rESJLeIzd6v5tYtYucVOuwZOOa4lCbZghXWwwNFJxVhJWRmTI2CK-KXsnmPO4FQQjvdNO4EcEnNRMa_Qb9s-p_kjLU2lXClazsM7FfYXhHw-ggkkpF_P7P80HAhKWKRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pr2Eo0VziwRXK6Bow741RwwNlPBUE2eLt2r2YkGYTqv4BsViPPsw7sPkm-oZPNT9xk6RcglvuzYr-2j8gCUm8FA_TDOvZCE6TRa9AypriNaYqTnnUWzWFub151GsHq_3WcE-Bzg6MFauOQSuFRmN_7Ofn_PsT2EJRDwXjOLNHqLISxm4SPlJRK4ftfYNoQhz92bDUhHJOjNlEQisNXkBHgXs9UnmHvl1QDbGt1yu2Ncy6lEvlhWuO2qiVwAFGjK2z06UGPt7LyN_elZzCLPtTpTCyF0-TATLFmzWNfjZUjbutyR6Zcoz1IzW1wsfPwM-OHQFkCiKD9nwR4Bat10u-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8AVEEMFz-9c3uZcPWMzTqA9BX-InYPWgwv6a6YrETMQxFiRmQXb9EFWF4ElwTTBSDEq0M3rZpvQgH0peLDMHbuuQFabqEF5Q1LEZRsad2dJYHbIFFl5FinOl8L6Wl1merFjyPbjmFGU9s4x5E7cerOBdjiTzZlOcSHiu7V8us92CxUwnyqiRhWu3BqwKeQaTu1LT1xOBZ0w35HHGTeBfiokbg9-TpyZqrRxAZ2UH6zs34KHw5IucueCxk--k_9UgC3U5248CiVvjDnEYRz5i4ZsmsQ0VQ2YqDQ7kyXq_-LXlL4EqBJsTnrXA0VehpBET9jxd5Tu9l5jW7qFmijzxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1hdWeWwWhcW7mRVkqZR9Xig-msWqxVX_qDASv90GIEJw5pFv2Ip4IogSo2jm7sgviuS7RVoEwjGO2fCX-RWIuLZCeoIYdhOmHrfK24U9vELW0Tods_HlhqyeUk7PXM6agYP33cK1MlxcBsv-ZN-0LUZLIVyqTPMaHg9CXZ7lpvA7w9f7UAT-NJeSGOqOVdDJXR9h6xFmaZgu12MU8Sj00TXcndyxcXNvmbmmdT4-xmFBKzz9uuX0-GvR8wLoTOUD3nTkZAWExHi_N6O6vaI9IdKw7GRFNsGgvJ20CsaLL1hhriwMCpmo4HPOl9g49x0gDRjBT1SnUa0ZHAYdn6ImA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 577 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R94TOLEO1QYmdVF6MHVDtEl2pozQQCJGk1tt6lBoaN1IP-nh-qe8nCZsCMbI9klin12gtehUFSBeh4kpFzu_iUdOoy_Kt-onMx6ZtkcH6Hdm-cB-tHScEotGz9Sa3Z8LW2-E7ix42nk5y-vAQiObFHMklbLF1G_SBFfcy8JjrMDKVS4SkzvHfxWNMimMEeh8fXm32wcG9T6fQVhGT6bfx9J_nC3-FYHvMv9mgtsM_Gd6156IIyXWsQVf_P8TKuevS_D0Zope6wG00A4noW4j_Q2ltuFqRni8YwWgXVqgSiGDw2LeDj4pyCqzSZdSn0FidU20ZHiQiSipKODih-p5ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZ6o_dudYmzxRi9_JUCkFbDOlXi8PWaZGT7eiFmIahOd7k5lcRWwMmiQVu33Ker4ZUxSnSDkZMeYH4Eg4qOehKcPhmzd33UOxhDImTAphTwn8PK8kn3kuKIN-wkDXrdY_Lp8BOKQLaRA5wQExiw7HmyOxluAEcBltSstdkvXKfxn7OOK3W1wu4Upa9oKa-P_KVbXRM4rhalL4eQowo3MD_E9T0vAOJDHEBwNgwhbpwa0AfqhBfgkSXCt4lp3GPZ-BjpFVrUhRDGEY0TBDl3wUACtd71jo3bCMmTCM_qkdvfatGp9bH1BFhfakHjAFJJj6V9njuTXTVfchRPGmAl1gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 694 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRaH3WX6lTMH11DGopRQLlh60p9XgWTtRd4Nxu299jRTme5a2BjfCvNe0CO-4tKbA_4SKMzCkHrm9R-kdMCouJYTUWuXXM2ZKlPn5miz6yiRpQUoDUGBgRw2EMLRNDP2ndN6lTMF_o7rjjuXexDUif3yHyZZ0GqjPzlLdiWxe53zjMRXzp2fwN7uxliQp1FHLe8YUfor3wFIkcvS4zyd4gOcUNsZfsALjzJoYahXgs0tEUnnVgNCf8c9MwSQaniz8Sa0YQo5YauvV7It6pFq6FZN16rD6pj1Z4UC7JjEqJv8_9vHeZBivrqASSd4BpKzzH1qKPCCKoG0QqrI9qSEEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U43YWPiINE4Stawv0nKcO_ujfjbfaNqJsxIrd2cThK4DzMDu6YriZ0iYXL5O1VBU8pgoJDwutX8F8fbi9doCD9D2arINx62d_PnP4_nPZlmNz9OKyk9XgOSWCQhFaKFLoEYlftVwD4kfGAhasU-UAahhOTCnEklnzkFIbZ8gdtqHOusUVgG9RsBZ8haGq3xC8x-tDyZqoIRD1fbaHftNMcOHhtw-ogqgjPLZFuH46A3dZtS_MWaTtjgdBVPtbY-PTRQFEo0a4bFGLLjGxNyzwRPOXq-_rH9s4OQTgSJ1keNMKxgf5rjgVWGjHjLpyhc516y0YjA4dC0ASlSzwmVVtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 708 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXyWA0NcUB2rTTUNAKQh0hjtyURfgaXUXbHlMJRA3MJJtQN810-hIDZGT3g1soNuxxlnNJ8k9c6pfQOtf0c0O0fi1V-BfkLWmzzGe9ZztbsojLyMC2YsZDkQ5eUr9rf4D9bxKEkTMyBXreya2aX7xHMbrO641JBIWJcF3fHzSFjaj0t2usrmMil8EZo5_3htKoO0hu_cxOxgat8MkGajhgkquroxEvMl90ORWqoAvTm2mLNY_kydAj85ujf8SAZkU-g0mYtrib8qLr-7IYMZ1UbcRh0ebNsfSkRNDDGBXio-4VY7cfOpxXIf1gd939GwNrwNYWTOQcj2LgOtzzkExQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 606 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvJYtIXKbmfu1p8LaS_RELZGDmS4DSaCj76Bgf7cE9gZrb54PTQuvVTVBKkFGP5doVitOfw7doH9k4MPeqNfUnTfcrYW5VYkt_3qzCbPrZa6zjCvYIa823JMBaIFPv02d8301NHEerem6mbX5HH68RGUg7jtsQ3rcD63cmaNGnQFDqa4RPt-n7tDiWlh-Id-XlHY1WtzwKlrXlQMjdoGDf1Xh4VNMwpXw2tcNRW722iA2sxLO74k4mHr8dX2-zWOYCKwFeW4mH-cy8YoWhlOIS2gam1sAEegPhtqbZA8wyjeRg5dea82OKDW9f1px7hjTmpLCncB66tcIhLqTZwYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 637 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTEGgKDbBz1wZ0UI13jsK3wT9MJtuZwke6xGEn6ftz3me4Bbi7HNPDz7Wb3ybLNV342_hL-kLfC1ysj2z_pft849IKvQ9l88zTNP0CgEZA2o9xcMlLHLa9xw0OCIoxBt4YpxM21CQfWxwL9hvXnrixlhc2S92fdGx3EuH4XzwYyqoC0cbHL5NW_fccbRelM-AmikoFu9OkrJiwpnlz9EMP-v2AqwhE9O_Z4VKMJjNoMXtrYI1l1T7hC1T0Q63Sr2BA2ZJ7k6TdPYv8dLglQEfBUq7sHOJ7x19vk3gvWzHCLNnAuQb0pbozFeXU9dwFwpl29IGlXsPKCxbWCm5fzVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KwV8VFp-yedshymTHgHwxR1puPxup7tTTjqxyxKQeuiQb7xZhQUgzMNxIcc2NuKAWuQyFhx3Z6BZPSCfwslvx0Cq78A_-NX2MZhri56GLKSPQf56rxOrxFbQPYFvpxVSi2nJujZWiFlOJ_oalULZ0WNleKdGR6IQdsUhIGvLRaJ8-7Y2Ae_augvc9c3K5UgJZtF9EOgKqxnywKWrhNxmiy6bviZauqR752Fcq563eus14Y-Can5HlkHWKyd-p17zb37R_cSIwRbejVHy_0ZjEnxIY5Qv85C7AELa-D2vGQ220ciIFaXK-bUURTvJ5P5F-fwyBU7sB26TCjreWNspcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 664 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE7U7ylpioptbEnLdtM_CCSl9oE6BtGgooDgFrHYXrj1iOJT_RfgaHTMU7zkzk7zNmXCcQ8DDtfunIiHIpFJNSuzyD5xtBSjEAUXfzclZ2zhgn_BLkJrZCXp0GYrT4tKwNIYlHyCBbM7rQvnFWwEW6hwsMOs3BJTtPfDVLLYP8oDYrgYcEgFYGn9Shtv2T8_lxSsZ2YvaGkwGPWxfFdtGqGGCQ39UU9998fe6OVWCjQ32i2Iuj8gZ9C_nXYY2xX2EsqvC2WYgdoalEc3Qyw5SMdM2xb5UPiTkKx1d08qydJJkiudj9g39lsTOxbFx5K4i0luNxM7dlPoGE-8TnZWTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 543 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5NKDDPV589yFPWXXmfTuxaipmvrItQD3qEgB4LZUfQT9NRCYCoN3MmnVTEjjCn3sdmhzqcfM6ldpyBJ38sPA3rizfs9O6oanL8c-j2i-m43RWA7Jc76aWXpDEMzdA53J2r9-D_33WVTZddCaLWjuVjMOw5h3lylNigyK-TBBfD6FbmR98bqES8_Gq89ddRa_BdwSOADQosxAx_mBRX7RsRTMUi6fN1WJaHhORI649wsRH1pxcuc9pablTNIGxCoKVCHDiw0f9EUFwNkT3d46iePaTZbPQywHLEC9QSIx0yOnM62b-ooBasnmUSXhEjYUKtDHqy9QZ2bO7BkqJT6fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 542 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhfzTL5pKKBE1JIE-9KSVDO1dF9a46GA0EJot77o3IDDJDuFJvA8PoCq5MGKyNk5hCQET2Jp2RCqlic8RGaWjIFFapNAWwcF79nJ_MekugKmbIOla1xnexh4rLJoX6LApUsLA2EAXonfm_4IXc4HcEKHqyRjFahZvIai4-OQ2m-RkTbulw9kVnj0OaOF0FHPb6VfptRqvKcMLRIhq7NU2Uf_ypYb6eOOsFtOgfhtPm2geYvEAHSscwIFRcFnLJBlPWRL9Q2JZN0XIiqkqyhR6RGKtzRbkcl2r1lsBh3SJeiyH42dhtbjKY61L_1aGqJPl7kIxG5IGp-R-YL3FMxsbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcztRchL-ufHmyjctsucEVdG5CXR-wxVwydb6LQO7C4HDeEb7-jXMK0tLwWe8fnh5TxbtmLXvxkk9loD1FWN8PYJDcx4l7g-0rOjGHYfL7fkobtPuEzw3le8YrUCP9-QwAqnoRgf9DVdnC5Kh9DFsKXtXIGGJcgc4Wtu2acHYAUiMQVDmQNVAHWDrGiyZ_lOJ2dpVJQSlc6gAFFcKVMBdnDQE487X2lF2Ti2HHbXBAIXnUFWWqM9Zp5pm49o-SQfPkKDQV0Sa2CprP6KprAaY3TNgV3-tkIAwfeBVIDbBq2B-hEhdRiflETZDC_HJ5TaiVsH9fUNCF2wShusA0PKQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 679 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 689 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 872 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2NnHZUdFA4BmakRHp5aORKjr-quJnPDnk8JbnwHXobX0-xYnkEkbYwrbOqb4-8pFUSiApAZ1rQEgVR5soK8WzZu3kQfh81QegF7nXydQj4-1uH3pg_OoArpRZF54eCUK3vn0i7mQuaNToh_BYAhaykqJi4X_b3GG1wHG5yYCotxGP1o7HvsAylCmfn7tWFz0Lxc_3-adn2Kbp6pMhlHuDlirf-eFTWLxbBW_lLBnelEIb9RqHMyOuwbOPLPLHYzIyLnqYe45pKV6_tVVF2Ksh4NujZFPTjvYW4x03oh5khgTfh9ToBnrZl07CKgIZqtgNmYE7unap2sbmfpfpf0FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dqXATFNTKIg4kMNOsSnw-Frsj2prk5H7DBX-oZNveYVfGL8lNY8cavPwiWY2FCdw70wAny2SFnxG463eweKSNG69ccAZQJgBP2vez1yFKngvSXEoYwHRcM-z0K_CjTLQs7eFbvsNVjtnUL7dV_l8sYGFNcVLgXNybtiU9iYPCLq_rPMMp61VsTCNTGqCsnpgjskQxCyUkZ6QKMf7MRs8jTO_3gNFr2-rUnPGBfz2T8BGBwrRQfYI-U8cOtOyqMLI2Al-3AzcujPoYKaPVr1RWvUjX62VL3QYI-OQk4pqoCTPxkzjWh-li84xqFsR3NwC5ANmLURXNGZXWA_7MrBmOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 810 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EXFxwsMgcufPXHIwXR8mXSTvpKKdrvotBhqObkkXXzK1Bz6u5bV5zjdnL-oaVv1aCUf5ygoAyJbTJuS2TzrLY6uGDMesZI-rFP2f_RzqSNlaJxhk82hC-rpqakqxmdvQPya7v0dXB2Jw5MAeqwoHSM0JRc9UflDgkicLI6wLa6xftZHrjf-ZJxUMNzygdT5Iv1wNBMhbf1PGIS2OUp2H5qbhVs6sgXaH9ufRCbROqYzt17efiDJjKoHFBO8mxLoxOAQVlS7F3tP2HTPcqpys0Oei7RPG8mfAqRwmpBw56xA3V5aYiZsXOU2ZuTDXAn2mLRzOIrfdLsUpdmYSpNHfcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QNFScpo9NyEmZof-SSrLl2vddmnYk36AiafteFmFtgZtXhlOQdUSpQFCcp6JEFE3b5VMYIu3eG_iPn-HliGU7bsfk3Ll9SITa2f8GXn33GB5S50U3WqMGW2ON90_Sie2ZwYTiRORd4HAJyQ8pHE6Bd9w3X9tp7xta1Hvro2qi2xPst4WFM-3pkPp54JNFh9wrGLcJSV3_LRDtLLmBEjklvtVU-m0OA4z0G_NDzOcvZzCGL-KlOHMKh1fs7X1swu8AX9KxdotT5v4vO-y4V72jWywciSNqS9xmiu4kMmgCd5v8WmDv4V57Y7fEudoTF2W9KOzNOPI8G4Jw9K8qE6B7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2HsrHH55bnYP8BVMNBhK_KtiJcbM_7e9BgUDRtVe5dZc93dZY4XBKB8z4Re1gr4Oy7JN6rbI43cRA1CCM-bQLfRUUQQw7B-EapiwgoPvQYQ3qW0EsDyxd9ACXHXKO0ZHoYn3gd8Ti1Wt5jDm18jgPC4VvF9bvaiV2GUZDTis8FeK-idOha9Gy32Ez9H83g2-qYmL8sssBJrbbWy-u3SzgxIzsZvX_JPF7yekD3IAdrCJK6TyiAvQcB5D_A1d0HvHLFD-9C4fk2k6RssLym4jVmi3K6mW9wQbEc6GF-eoRvUiCMxwjVVfJpTcX9i2kNjEKAMEJL_qiZgTf2UdWNEvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 583 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 583 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tW5kMVmrGgmNc9QP7mHVxWT_a_85UZV_4uKhlUWTSt3TNHNTW5VMUn-XksrbinqxsTK-UuDkqkK8tSfgRUALK-XZZCTsxaU4vX8mYqoT5GADgQmDjSdqmxNFFa1PtGZmX8-tvGeZSicYz_b4hbTeNYKhWSzs3P2zSsbepGg8mSV-OO4qppo1u70Xi5UbS_yxF6cnYkmVmMImV2h7TlwdlwZdwo7mMcp1mcTMK8onZzFDaFrRl3QVeiBl-Nj1oOoB4SaSfoKkqZn0vlXvpf5b1SnZewWZ_zt-dVqsLZlJ4H8BAb_wM3S4Tt8RQgVIlOoXHQdc6b8g2BKTPWtsvvPAkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWagc4zUViYjSOqdOx3f1NKTmyVP7RFBtm1RWwvqjMlyBlabOzM-wamDmTTcg0-PIeMA98kBPWaaQdYc4Lw_L2HrWbpFPINecNP3ZJsxnIz8FZXfOx1P9fr6GB5yD7EQiCjB4EdYA8xIfwJF1Lyj3M5aOtdaAq1A3CHDAZ7p35x-Xx3fzrcQ4KJJIew_nUeIZky3nRHntf7-kWlu8OTwA5p50QVBBYY839jrDoUNY6DaHjfTkr6homfIxwuUH8_uXWvNxE0vZgVc9rhLoWz5bRFokzxXw49Yse65VKAnxb02pNpdIdZ5b9YnOUpNxX9_nNxJgiX01YyAJBX0i0LIOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 900 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgqRNAF7ckJek7hmgNzXBltmMnmg-5V8weM1qwWfr93IK5fpVAprezhLjYPHzgfUZHSkWN2tpFAcsxErYLZX6X86_ixcOGVyGd8PiHQ30s9AL9BOupSTcnZgB3kijfTP2m498RTptD2ra12o-6fqdNj1X05-OMwp8-bw6oPqQmAAtiDJHr865LBXTBt5cPWYMli-khqJO7WiQ5NEBb5EQK60ilzChsiUtNA5Sre_OkNHPPvvFby_wxRZP6rXpV-SPjkwQuU7cteSNrLzHztZcZOzws40LiX-8BEq5a4aL6_hXM7YQSR4x0kOwE8Nc6xkFXOeVnA7qUp-RO3FeDa_kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 716 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkWQ9xIEJiunsZg-WDFHCwhiiF47nRB0Bb9xGvz7ei0VZd_h7OzxvagQy7Oj1f1ysYbF10SR6eF6L3Kw-ptNIDe-g4LDnXrgUpblmKUIRdj9k9GVeN_cZJcq4C7Oj6xv-oj8ppERisseDUmComL4PRO4En8I9UGkzl9Xf-dDHpPnLMw9OaBa4eQGh2DX1usGA1UA9xulRoUfNdXEkLTOJyMu-adZJF7hzhzzyntFmJNj0dRQdrlTSNmBEBAVcxVfTzlkOzJVjO2bYxzXLJ6N0plsvNicyZm_jteAssJ1zOE0sxD1rR_1hXOoHS7i6rkwjxn-6eP9MvoHulKJh_JN8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT-ya_3m1BT4EFvnvAR52hxSjdq-se1GNneMfe_0wMYfOwBhgCqwUCkczStWHqZPMLEoDha1C1-tKY2uEBRk8OUmRZ2vPhcBHtMewAGVUNFlOsFEuNPSTlq_7Bk4V-tCCGfsQq2oxZWed87FB2L5F2wNBJHXW3hzK28yeidzwGapGmpiUYW6PMYKhJAT7oSvBLesFxO9Fn8LhE3NcJYe3X67mNMuwKsQsPwEfFX-abxTpGhrGpXaLdtKnPM9TEGY-qE_bEYJTbYyGXrXC7Lg4JE_HEb-XsQ4o-LVGP3r1Jk8UB8PHPMRY4Dvm51t8FGHTpaldnBqDgYFpU5DLe_sxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 768 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8jet_A_cm_tZCOfJ4U8iQHcH1s6mNlQswEHrEf8sLlkFJCjiN-CaWwPqKMKtVo6PyBy1VIp5XOC5_JfdI41Q7rSWgoWJnuc7YULkUNlkE-N-qpS-5SCLyu0XrS_AV8BTJQhntIif3Zb053fbu2U0qjCwgQyReUebD800Hq48zfCQSqUt4UuceMfkbVvy9x_SpUnqdlfGg0Nb1iJKCH_bUivporGkPmB9-riPDOvDeggi4he7dhnajwKypeD2-7nPr1-e_5wuMgzbRkfOf29OouHRb8W_n7I_O-798Vh_Wurq5x-uqW8rAP6piarndOF_A4E7tr5R7odk7a7AIQ1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MsIfP1lUVFRmkJZ0R9BPv0WszFT08XdnTei5KmEL-Cmjhp8FNahhSXRk5i-W9K7rbQBiOZCRFwWeUg_tqkDdAW4QvuoK_RELOnajKzhDz6uOqYOmHjouPM1j_CbvfBJEYk-WtIpg6WXUxhh2I0VSmknCJ-TRpmJYz4WMSGq9p7XOhEyxKcoaZ4NmtGXLY0UXJziaWw3FAvxpMQPXOGAomNU1Lojxal53NgtgGPrRD94LcoJPp1fHT72mvVTmuthsyvdJ9mzujkQg68iko_aW7gUWwDVZgkdY0lM2_gSPspRKgkDQ1NhxYrpiZ8RJNv8Dzmeuz_mjJDbKovfhcqmwmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 608 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5ADxp0rawt1-mmCsSGIZt6oH8BPEym6NR_ibUm_6KX6j-aAETLUXLBM6ZdZlQU2BLWG_ky8fMI9ZKRYoXdwKwJCJpMaWhyF4MAn3oBQUXioiJOj3R2qpVlI2mpRpfJB7uMhnDPgqNtm8dX5_I_oGPQOV3jG5Mop9rWkI3E1Fn4Vu6n5O79RGp0vWYq66ekSncfk7hkQk9NzO8cIJZYJTkhnBne_9cEtNMkUDSPE2dRubB7qwr9Jmkqs9fi6DPcVAbZJrhBYVbI8yq0RwdaZNwp5GlZmxU2BVTUfYyJxiK8oJ-K5l1vYzjjc0JPwTXT_sGH7M5y3AEBELPbcESX9Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 620 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M78MmlWj__FjrIZsgDReCeg0En1fOht7Ki3xlWrafSGMj95VQ6Mc4FPrzUQhfKxYpzyhb7Izy9omva4nIUgLhje8sgRWCaORhJNX_8PUGpTpB9Jg_jQ8ik96iUa2Z0oIBVZwbrupwlR_ugTP_KPCh8EZqszGwKZHphTI3HH9yXxElY0XbW5Tuyvp1syeoF5kNmDxDu6MEvd3_BWpOuKf17ACBjCt5HAQYhgh8h_Oz8un86uSnt8o32gewcYnXzFhFasYXs86xcgEfgPHxxI0Ld1w4eKRJ6T9c1bnIESV59yvJDR5f6cSigKkdt-wKbnH-9cGifLn15T9gpFUpRF9Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 661 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 608 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 669 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twlqVQcJE66u74TmI_IfW89W_4l0Y2qvRAMtZpeIXpEPT3h-OmjbLyMuiTbIxz3sIrDsBnGQjwUB4Kv8lSLnAS6CQ-S-6cE4O5t9_xdDkfwoPumARqjO5triy-Wrr3liYVClnvflWZZQxtcKngj5tQgrv6wlppNX9jSNPLytM4Z1VJzRiRNre-3T7e-ax4axz-wCq4S0nqHGXiY3wkwt176qgx08Ao0cShLWC-596accu4FHPQiigyKi8lgZ7uiq4qA8Gbb26rxP_sJIgK27b2ueLB1okniRRFs5DlEJiwCtAWsf1B9_VWaWLYk-lJqN3MBAuZmUNRIfP7_ApQwSuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 655 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2pAlgop62qfDBdQ_HGwVBc1NCfGEBtymIsR6jI_0-aeboRJ_E427NYF8N2zPNKG9kfgQWWFJNbLGClEuVDWmunlf3XOisUXO0IelJviTqWfW3tD6pvMJdw7y8-3rUmNh9bkafuXCBUgnd6HmGsj9Xupb506SyYjG9z-pGxXUSIEmE_NUYtuJ9GaJLyuoyJotY78Dt4TQ_vVigmRnLLvQkdJaKxZanNcUrGFB_hZxbnPjqY8BMncUbiHG4XUlUKRXc4qCQRIRSy0pLy7z4M1QPZSsfHoFx_GthTSADu7EvZiUOikVyS5Y9M-Ke8tpSqCSb-ExEUsKbhuQ6ZW8ZY_sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 701 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Sk9pxDqAjr_Q0KNURjfwt95aWOmPS9uUSgYGu6hnfNrYfOQwYvsvdWiHUJZVoaFx9SYv8q1AhVxuxlIrU10tu4Omz5ycFceDiWzrPzuTC-ISHdGiqhfGy80C4qye-YNknNpcUq9M7LBoR6mA41fkLoRLjRThT7bA8bUxX6Cn4BEIFJU37-sA6tha73tSgdO6xfTQl1uZzfopuugxuzTEHpcV0cJDWvfcBcqq1VGSCCJ9TrxfBXXfzHiyK6smHAdJriNYILk3w_jvo2PWlMGa7mXn3bLVDnHFjUpZTMkkYIE5hDWv9fQ2qUJvvESOWyn-d_XpruP3tPjuOytyS28qVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Sk9pxDqAjr_Q0KNURjfwt95aWOmPS9uUSgYGu6hnfNrYfOQwYvsvdWiHUJZVoaFx9SYv8q1AhVxuxlIrU10tu4Omz5ycFceDiWzrPzuTC-ISHdGiqhfGy80C4qye-YNknNpcUq9M7LBoR6mA41fkLoRLjRThT7bA8bUxX6Cn4BEIFJU37-sA6tha73tSgdO6xfTQl1uZzfopuugxuzTEHpcV0cJDWvfcBcqq1VGSCCJ9TrxfBXXfzHiyK6smHAdJriNYILk3w_jvo2PWlMGa7mXn3bLVDnHFjUpZTMkkYIE5hDWv9fQ2qUJvvESOWyn-d_XpruP3tPjuOytyS28qVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 832 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVpDSj8l-QVuQFdpTWq5jaggyFCjPzAxZCTFwPNs8oIUIXcCJfvWsulNLqQhw93TJ3hYNlzyXvh5UDw1YTfrFkj_mc1aoStHzKVVtDvHgbiZIC-gTKGds3EumqRY88DMCM7UbFQyeWk69ycUSvYv27olkj8SP82p2g9x7jkXX8kyCHbFbLKwawobvIPVn02J-4fIsCR_Y4yI0YZC7Sn3yPICO1ML_7R5EtedCX7csTShGKwR1ZCJ6GHhKqm351e8HUenm_ccke-JzKiO4gV1IUcTFUWKkAJy2717cjQE4Y2fOfuI8CitmZZpgyBtC2tpDiTTR3mO-DyIzydCMyqeKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
چطور محتوای خودمون رو برای گوگل دیسکاور بهینه کنیم؟
گوگل دیسکاور ماهانه بیش از ۸۰۰ میلیون کاربر فعال داره! حالا تصور کن اگر وب‌سایتت توی دیسکاور نمایش داده بشه، چه حجم ترافیکی می‌تونه جذب کنه!
😍
اما چالش اینجاست که هیچ راه قطعی و تضمینی برای ورود به Google Discover وجود نداره. با این حال، گوگل یه سری نکات رو معرفی کرده که می‌تونن شانس نمایش محتوای شما توی دیسکاور رو افزایش بدن. بیاید ببینیم این نکات چی هستن
👇
🔹
۱. تجربه کاربری (UX) رو جدی بگیر!
متأسفانه توی خیلی از سایت‌های ایرانی به UI و UX اهمیت زیادی داده نمیشه، درحالی‌که گوگل عاشق سایت‌هایی با تجربه کاربری خوبه! پس حتماً روی طراحی و کاربرپسند بودن سایتت وقت بذار.
🔹
۲. از تصاویر باکیفیت استفاده کن
محتواهای تصویری جذاب و باکیفیت، شانس ورودت به دیسکاور رو بالا می‌برن. یه تصویر خوب می‌تونه بیشتر از هزار کلمه حرف بزنه!
📸
🔹
۳. قوانین محتوای Google Discover رو رعایت کن
گوگل دوست نداره محتواهای غیرشفاف، گول‌زننده یا پر از تبلیغات باشن. پس رعایت این موارد ضروریه:
✔️
شفافیت محتوا (Transparency)
✔️
بدون کلیک‌بیت (No Clickbait)
✔️
بدون تبلیغات بیش‌ازحد (No Excessive Ads)
✔️
بدون اطلاعات نادرست (No Misinformation)
✔️
بدون محتوای نامناسب یا جنسی (No Sexually Explicit Content)
✔️
بدون الفاظ رکیک و توهین‌آمیز (No Profanity)
🔹
۴. امنیت سایتت رو تأمین کن
🔒
سایتی که امنیتش تأیید شده باشه (مثلاً با SSL)، امتیاز بیشتری از سمت گوگل می‌گیره و اعتماد کاربران رو هم افزایش میده.
🔹
۵. سیگنال‌ های EEAT رو تقویت کن
اگر گوگل حس کنه محتوای سایتت حرفه‌ای، معتبر و قابل‌اعتماد هست، احتمال دیده شدنش توی دیسکاور خیلی بیشتر میشه.
با رعایت این نکات، می‌تونی شانس ورود محتوای سایتت به گوگل دیسکاور رو افزایش بدی و از این منبع قدرتمند، کلی ترافیک رایگان جذب کنی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/829" target="_blank">📅 11:08 · 01 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAVfWRq9nQnRi9JBsqh_f8KH3ZJ7i_glJ10qZJkA4vF9E-3UPaVlHleSC-JNJKduvc0aOL7-4_QeE2p2e86RryBIZoJInW-Qy8VMcC67XC4SACxLwzsp5x8AB-tueVGPQ6DuXV-fZaY2pXuOUd48szDTxY9Yy086Q02YmtoPihEHC8j5tt58oU_IjBijuQWSVh-aFa-ll4nKs_ekUBzSuxDS5zXEd4Oj6qQOQQCslYzw9e5Twc0XLbVFDdNm3nh95PvFdAjmm8keloOLRhftgwGchvBHzOOxFCN_DIjoX-uIcCPz7onNzvaKOQWoi_JaBEVPMP6QuPAHu2D-n1wpMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مسدود شدن اکانت آنالیتیکس سایت های ایرانی
⚠️
اطلاعیه رسمی گوگل؛
‼️
اخیراً فعالیت نامناسبی در ارتباط با حساب Google Analytics شما شناسایی کرده‌ایم. بنابراین، ما دسترسی به اکانت‌های شما را به حالت تعلیق درآورده‌ایم، و همانطور که در بخش 14 شرایط خدمات Google Analytics بیان شده است، خاتمه سرویس Google Analytics و شرایط مربوط به اکانت‌های شما را آغاز کرده‌ایم.
⛔️
نکته؛ اگر اکانت دیگر سایت های شما مسدود نشده، در تنظیمات اکانت تایم زون رو روی کشورهای همسایه قرار بدید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/828" target="_blank">📅 23:54 · 20 Dey 1403</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GoogleBot-ips.json</div>
  <div class="tg-doc-extra">16.2 KB</div>
</div>
<a href="https://t.me/danialtaherifar/827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
لیست آیپی های گوگل بات، آپدیت 8 اکتبر
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZ59QqJe56Lnkll87tDAcIbyBldQkR-fDyyQK5VsNpbcG4eI5ZiY_OwQLWa0I3_FpHb4__yMLNkGCE60a83EYQDD4JlKW1Z5klELOGyzuiHyZgYRBuFYQfU92UCycqJrQ-vFg57d_8ubmvrMrJLXkLppEV17PG2WPOasI2JQnJeXU6wWpQz9AzoeQY4DbJ6fhww7HmiJZ1lSr0GFj9IbJHOaaUBfX8jjC0E6hK0HxxKinQW1JTIcR0RQ7Do7OKSR5iA2A9i8PYukFl04WaBN6D0Pq5pl5nJX-QfcxuFdbmjkts9-vVblS8HEx4NpN0bToD4quvVpOXWDpTR9TlgxNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F83z_C3nPcg4Ux5CaDP_m-SIB5awKt7AmTbXpVLOThxmHNq1nwRz_lldL1KpBG-naWvKDfIhQQ21dxTkNoITkO9HjzH6IwALX38bke9V4MNaf2jAkLP9LFk_zSMDqFw423zIlZ24iNnTZ9biQ0MI3pA7nOnpuunevyPrZuQ30fEv14sOmU8s3rxnMAeOWu3U-1oj4jsYQZhuiY61hLhRfAX10YPpZQoJQJXnMjcaaGUXcKMdAPDzGH_5FTRMHWbv4W_GFw1cqAtuk-hiBWLHYk4KMTuno9KOp0s8ezPVqk4bHCPuzFKkO3UVVFyJb-G74cKAv38DXwgCF5rknRmC1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
گوگل در حال تست نمایش قالب ویدیویی جدید در نتایج جستجو است
♨️
در این تست گوگل، باکس ویدیو ها و تصاویر آن کوچک تر نمایش داده میشود.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/danialtaherifar/825" target="_blank">📅 11:21 · 23 Tir 1403</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LNOB7P7PZnre4YzWy8OTfpca7ANYn4qPKg7ukidfuPfNRmFOv5gRwC5rWD55vGNWiyi0LuTR0T4JW5qy6eiWO0cDYuEAxMyGYvcE6m0MLZdK8xUqdpzd60ZGPdxhG-L3xGJde9kwmFcB1N-c1jLJu00lt2APKNt7FtLFhoRpzx3Guc431PTvIsPkmWY9k4AUtY_lGd2UEQph40HQQEizlffw0wEIPPMc_VosKwaSouaVk1xVXhNeGqMRll_qfyfd9U_k4vX2_l1fHQHQaRctibM2d1wfl7GVOCLolFdolfLn3wKWFCWSGdXIhr_1RCyc_FnkjoqW1UJ7MetmMRG9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aOyj5_CvEaQj_lgrYdlsz0JMZk1RilrA1NCzy9nIJGrPPNawBQ9RmvRUNVrHg2YlTaWIwjEBUegVH0EyXBN3enOuV44LNTpZTpvuvvNcwFpr3eNVPbnZhzm3KY8c80GtweZEpudxgTrlVO3LD1p6n-9oCLqSmtpLO_NDHrh3nlyQeS6Nvg7uLSOJECF-K6WvXjIi3xG4EcSnGuKWIEpXy4RH-E08gQSN15HBJIPc7wpLDdO_sffkbcheWxZtu5vZnz9dTTmNdiNujg_UjREKjALHHMmbT_z7kE1TlGhvJGco_n6Mp9OeoYuQieLkZ8ITYLUBycUXgqrnY67f0qMjaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcI8q85sgAPr6Ej_2NNOfrR2_atjnEF7Tj2oGuuuVe2N-SzcJh4DQSUHIJwgtSDplb_1JVnDGyiTuITGHFKXG7DqyFs1wzrKrZHf5dbtC5KDamP2d9QxzHM2aK8AtrpBMuP8oKo78bMNK9FnUso0DIQ6JvSlFosk3z6l05ssapC0VdAAZ7jPf8njtNQK9Uu03_lQSa3edTGdCTJtryU7tXuMU9fjYLBWE-jJ2PKc5-ONufecXFzh0pk8me_Vjw_1giSNz4O3lvTbRdWm29qPR4M1VsNPbwH6Jk1EBRWOdpqL1UNvy25CfOs_wn2gBPgSrl1Ftjph2-VakoCOuL_AyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=m-N7a4wKpYxOSxudqm9wH7UX2jA22KqU3I7JmFdab5U8l28WF7e1eVvqwXWHcN5R1s7FtSHoknzB4RtIij_hGhUCGOMLnV-0mQ8hJ-IBMMImSt9sAfLITmHhJ545IVzXIXmcfdOShVE9sOyg2Qo6DdyK3WoT6smm_3KLmLyFw_XeWL24V4824_KBtAiqA6-0hgxydbdR0TwgSMnn7-j2S7GMLP8gbmQ7cFVHX9FiCFRa2wwdO8iyCFILCrHRCox23ezf2kKJVdR6F8huH7ygeCYNf7_T4-mplfWvt_0UUi0qYXVpJ8-Xv_rDQBLr7Ue7ANRVctGBoX_X_YYgjF_39lrvrQdyCd3RrSKM-P1fI689bHIguodUNPiyQBhs7dEfp1uzHmOy706nEHkicg2PECT-0J8cNfA43NeZ8RpxYvhSPRDtM4mF9XrOIRP0r02a-_XaB1vb09SHzKh-3SaI0jEEAUsFUiz0SpAz72t3p4ID9M7RbCZAfM--UCPlwPLQTlgUvweXq8rlT7Qf7_PdqNu7sfBtMlnNewupdWCCwGNhgk6XGFlxmAS6U72VeutTD9SVY9od_KoLf4JLfsRKZGwnOgNHgZx76SakeponKQIFQA5bkOjmw-Yb7pkIjLBXt4MU2FW2VyUWtei2c7bLgnhU2kCtwpsH13Ebbc61_lc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=m-N7a4wKpYxOSxudqm9wH7UX2jA22KqU3I7JmFdab5U8l28WF7e1eVvqwXWHcN5R1s7FtSHoknzB4RtIij_hGhUCGOMLnV-0mQ8hJ-IBMMImSt9sAfLITmHhJ545IVzXIXmcfdOShVE9sOyg2Qo6DdyK3WoT6smm_3KLmLyFw_XeWL24V4824_KBtAiqA6-0hgxydbdR0TwgSMnn7-j2S7GMLP8gbmQ7cFVHX9FiCFRa2wwdO8iyCFILCrHRCox23ezf2kKJVdR6F8huH7ygeCYNf7_T4-mplfWvt_0UUi0qYXVpJ8-Xv_rDQBLr7Ue7ANRVctGBoX_X_YYgjF_39lrvrQdyCd3RrSKM-P1fI689bHIguodUNPiyQBhs7dEfp1uzHmOy706nEHkicg2PECT-0J8cNfA43NeZ8RpxYvhSPRDtM4mF9XrOIRP0r02a-_XaB1vb09SHzKh-3SaI0jEEAUsFUiz0SpAz72t3p4ID9M7RbCZAfM--UCPlwPLQTlgUvweXq8rlT7Qf7_PdqNu7sfBtMlnNewupdWCCwGNhgk6XGFlxmAS6U72VeutTD9SVY9od_KoLf4JLfsRKZGwnOgNHgZx76SakeponKQIFQA5bkOjmw-Yb7pkIjLBXt4MU2FW2VyUWtei2c7bLgnhU2kCtwpsH13Ebbc61_lc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6Mnou7pN2bwu_xjnzfDB4SrCoMqF87IWmcMhjZy3VAiJ6qcW8J7cEp5dwfzhdEyM3mcZsK18u-Tz0eNdiH-ixafNKjkHuUiuQKqMq3aEUz-vQW_zMJbY9gpEb0b7Jp9mTom24rrNf6M-JmtAeDTtX8_0Grr7TuhiXpxSmEJd1jywffmnL7psCKOplAkYfn1vRAR0w33neTTIodRsnUEXoKgP1_Q9kUbrDIYSmfRQroMZKCLwMNn4nYQ-Oh-auoRx4DsjS6DYFcufOZ0AszB00wY4VRPc74-inTkWwb8Y-Sbrv0oZd1jDqUkLvCH_oHDY_C8Bp2f2MDsnzRlMMgL_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTiENbdDtv9kHFR0PNlzL4jUf3-d2ffFQul7UlRq14x_piCYsaVA4gtqBK0CsNpGjVcinQN29liUlnYH8IQc5NfQtHnXQPcNRcTZXPud7MdYVcM-k1wxc4TL70IMaPBqkKEURbEpLlRuOTZgXHY1TgdBA8mWjSb-rCYIkNyWULaDa-C2XUACOm4sCN0sFz28ARDWMff3JnC7r5de0UtkVGIHeAk9nblPhXQVJIUj3My0g33pu5-KPC0bwMwUj4vMw71OdLq4cBoxUExqCvdsI0NL0fLkO_M4TiUcUZvAFKIeyRKnZl6gOm02NOvQlr51USzfJxRV_Hh_hDgfRIMnLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
جریمه های اخیر گوگل مربوط به Site Reputation Abuse نیست !
⚠️
گوگل تأیید کرده است که تاکنون هیچ اقدام الگوریتمی برای (سوء استفاده از شهرت سایت‌ ها) فعال نشده است. در صورت اجرا، این اقدامات فقط بر محتوای توهین‌ آمیز و ناپسند تأثیر خواهند گذاشت، نه بر کل سایت‌ها.
👀
لیلی ری، متخصص سئو،
اسکرین شاتی
در توییتر به اشتراک گذاشته است که کاهش قابل توجه ترافیک وب‌سایت Groupon از تاریخ ۶ می را نشان می‌دهد. با این حال، سالیوان تأکید کرد که هیچ به‌روزرسانی رسمی منتشر نشده است که این کاهش رتبه را توضیح دهد. این اطلاعات نشان می‌دهد که هرگونه کاهش ترافیک اخیر به دلایل دیگری بوده و به اقدامات الگوریتمی جدید مرتبط نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PN0fiMNs6e4wmGyDhg52ME2__mlmk6WOraOayCLDDMe2uIyERm0rbk79IwwzDIyXFpWtCIYwqbnyTlrv7rgY_YxtVt9Rhe-opqRrKkYM_o84_jAV4UkHABKguz9UQ8nffX5SpY3ooykmoXD4HJF0G7yUoGVm_kTJNHTF0Mks7Nn_o-WMINdUr6jFEGSqqarYD2bkNQQ3CyH5pyiSEOeGQJPuuvoE0bNVf3Zr41_9M35EibGTm7RWLecKEnAyQ29enKIP9EQRSmFD7pZA-kD1X1usVRHC-MChVMhJeg3qG__AklyMhBt9edHDhORExpbgZqjgOSzHHdB1oJ1OvSTdVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SLib4wThhk0rhvjokbbdfxC6kf0LMKQ9teWRPSrEuHuLLP6aeNln3Z8FX2We-o6mf1ynxrN9YwiKfcqB3mbLbX_NZFNfoPk1-ExD6SfLxUmWr2lW4PUJbp-hY0wxOGP0QnEOVQYDjfdeMeQ_Hb8_OObmflJKuigdP6B5yYeGlZ8V-wqY4wA4CwyIdMwCm0ziTWeodXIGjvJtNerceYPnBtY5TcOFhWIOxqYpy-AVEwC8dCCTyLkeJGjCwhSaBLCWn00aGU86w70RoHooeyrLiPt0QX5O_u9SImXd5fYy8kBWsouVJBR7NuYg8DSiQVc4JCmNIFgNj2XSVqnjuOsMqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wm5nSa7OXnpTR04wDfGKU0-1rCLgc8LeJMfuNm7x_WXxeeE_N6UQuVoT68uqXGCoGsq_J6rhhQv36GbG9BQqr3WBlIsi_1SPZqbsRDXMjbqC5Ufp6l6Vtboni938aU7qU_CUmx8uNUCz5ydlxnTCkMRst_jNZFuLFbrv-JKXILUsN5Th8tXjms3NhR5Zhj37LSBdn1Pq_cgQ4s1ShoZFRj4-xHkRiQQ8Qt3q7hX5F8r7bFHhVzX1OCxHPtULHrvr6D-E9S900ywYL3srQZll43uRQN406cbei_SDG92l_FuVMHUEypRlKeEipkIIVm_35tGS9tgnNjeub4as8d9v2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😄
وضعیت Google AI Overviews در پاسخ برخی سوالات در آپدیت های اخیر
⚠️
سوال اول:
health benefits of running with scissors
/ فواید دویدن با قیچی برای سلامتی، اینجا گوگل این سوال رو تایید کرده و حتی گفته برای قلب هم بسیار مفیده.
⚠️
سوال دوم:
health benefits of taking a bath with a toaster
/ فواید حمام کردن با توستر برای سلامتی، اینجا هم گفته اره یه راه برای کم کردن استرس هست و باعث میشه آروم بشی.
⚠️
سوال: سوم:
How Many muslim president has the us had
/ ما چند رئیس جمهور مسلمان داشته ایم؟ اینجا هم در جواب گفته بله باراک اوباما مسلمانه در صورتی که مسلمان نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-815">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZCM7KZv6fijsWFDJ0K2u5nm7aWxR8mlyRhfCakemea440qEO64dxMbiaBs7qKw1Mbk5CYJgPBb95nRWbO55hM2mDCuqP24Me8Qbhogv-zXmXjy-ZrxIDb44MxXcoNNdxV4RwlD8QGmiHXfWRrvPAP9_UYy1PJ8Zv5AkWfJ71Hm3cuvK0yn7GaG9jMinZ36CE25OLNAS8iV2JHHa1Hu-OGdFlskGhAMc7ULvtKuqGLygRIC2JG5ZFPpEK3hNw0tgf1buGwcp-ykSPZ0SD8P4rMEjVlxpOEbNnqSK5R6PfdC5jq5dn0ux2IvkQOgZ54ZfaC8cjmGpFHR-QMw9T0Pc_ao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZCM7KZv6fijsWFDJ0K2u5nm7aWxR8mlyRhfCakemea440qEO64dxMbiaBs7qKw1Mbk5CYJgPBb95nRWbO55hM2mDCuqP24Me8Qbhogv-zXmXjy-ZrxIDb44MxXcoNNdxV4RwlD8QGmiHXfWRrvPAP9_UYy1PJ8Zv5AkWfJ71Hm3cuvK0yn7GaG9jMinZ36CE25OLNAS8iV2JHHa1Hu-OGdFlskGhAMc7ULvtKuqGLygRIC2JG5ZFPpEK3hNw0tgf1buGwcp-ykSPZ0SD8P4rMEjVlxpOEbNnqSK5R6PfdC5jq5dn0ux2IvkQOgZ54ZfaC8cjmGpFHR-QMw9T0Pc_ao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
بررسی وضعیت سلامت رپورتاژ با اسکریمینگ فراگ
👇
🔗
یکی از مهم ترین اقداماتی که باید در کمپین های آف پیج خودتون انجام بدید، چک کردن وضعیت سلامت رپورتاژ است. در طول اجرای کمپین های مختلف لینک سازی ممکنه محتوای رپورتاژ پاک بشه و یا نوایندکس و حتی در برخی موارد دیده شده مدیر اون رسانه، لینک‌های داخل رپورتاژ رو حذف کردند که در بلند مدت میتونه تاثیر منفی روی سئو سایت شما داشته باشه.
✅
برای بررسی این مورد کافیه مراحل زیر رو در اسکریمینگ فراگ انجام بدید:
1. در منوی اسکریمینگ فراگ روی گزینه Mode کلیک کنید و روی حالت List قرار بدید.
2. در قسمت Configuration > Custom >  Custom Search / روی ADD کلیک کنید و در قسمت Enter Search query نام دامنه خودتون رو قرار بدید.
3. به صفحه اصلی نرم افزار برگردید و لیست رپورتاژ های خودتون رو در یک فایل txt قرار بدید و آپلود کنید. حالا میتونید وضعیت HTTP status، Index و لینک های داخل رپورتاژ در بخش کاستوم سرچی که مشخص کردید مشاهده کنید.
#اسکریمینگ_فراگ
#آف_پیج
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/danialtaherifar/815" target="_blank">📅 10:42 · 26 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-814">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4-BS2cpKo8xjmVKKfDU3X8wtnkkJrVkPpcdSYsiNRlyAX1JiBY60Gn_QIBVokRgX4yUHbe2BZNismtBvpwYnRCMiPnY2ufguahWfJjMTPqNut0jQ7-u7XGwH2XMDJlC15U5O_ayGj9bfCgpH7zNJCvv7cBMLYUH17loSijAZ7Jhf1r4GytIBudY31ewTpRhjREFIjZfia77qz8E18FWU3Uhd022XkgJJUBjhaji9Uko5AiUQaXWAyFPHfJlaunujuptsoVsP0uBbJ3B3SjPG6YqaOora19xw9sOB3Y9m7F8arcunOPLEVJQl2RanquY0TPYwL7rQN2htUz4PBwUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_4o-eDjfno_13DGkNc-N_N1ioUNi3Pa4a0OQiV5zcpfkNUmg4E7Voh3xEYBdHo3dq6RSZY6_kyIvhinF_Iv6kTk6VBcC6SaZOSff5kZvW3o5vSsyPxOoPi7lPDiA-nZ2oGGGVGKcDXy8_HwE-I95ajY3_aY3I01AwOcAbegnjmJl7J_nhX9m68ghy0k4Zv0vX5uuKy_9_l0rgiRek6x_MIbPp0Ptgjo328E9s-znNPHCbMq0UfBV9ryj8gOedl0EWaWRyqVbVhKHyn2DOpuVBm3XpQ9golgprTRRizoXxqa-qtsgvG0UFZlw3lrZQTfcu0CcrzTTlIFZjDl1GOG1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
گوگل: بک لینک ها مانند سابق دیگر اهمیت چندانی ندارند !
🖥
گری ایلیس میگوید که گوگل برای رتبه بندی صفحات به لینک های بسیار کمی نیاز دارد، شواهد بیشتری مبنی بر اینکه لینک ها کمتر از هر زمان دیگری در تاریخ سئو اهمیت دارند، ثابت شده است.
✅
گری ایلیس در کنفرانس اخیر خود در مورد اینکه چگونه گوگل واقعا به این تعداد لینک نیاز ندارد و چگونه گوگل اهمیت لینک ها را کم کرده است، اظهار نظر کرد و گفت در طول سال ها اهمیت لینک ها را کم کرده ایم.
⚠️
اما داکیومنت ها می‌گوید گوگل از بک لینک ها به عنوان یک عامل مهم در تعیین ارتباط صفحات وب استفاده می کند اما در آغاز ماه آوریل، جان مولر  توصیه کرده است که فعالیت های مفیدتری نسبت به لینک ها در سئو وجود دارد.
🤔
چرا گوگل به لینک‌ها نیاز ندارد ؟
دلیل اینکه گوگل به لینک ها اهمیت بیشتری نمیدهد، احتمالاً به دلیل میزان درک هوش مصنوعی و زبان طبیعی است که گوگل در الگوریتم های خود استفاده می کند. گوگل باید به الگوریتم خود بسیار مطمئن باشد تا بتواند به صراحت بگوید که به آن نیازی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/danialtaherifar/812" target="_blank">📅 13:54 · 04 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">shape-of-design-@danialtaherifar.pdf</div>
  <div class="tg-doc-extra">1.8 MB</div>
</div>
<a href="https://t.me/danialtaherifar/811" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">The Shape of Design
امروز می‌خواهم با شما درباره‌ی یک کتاب بسیار جذاب صحبت کنم که به نظرم هر کسی که به طراحی وابسته است باید آن را بخواند. این کتاب “شکل طراحی” نام دارد و نویسنده‌ی آن فرانک چیمرو است.
این کتاب فقط یک سری از ترفندها یا فهرستی از کارهایی که باید انجام دهید نیست. در عوض، چیمرو به بررسی فرآیند طراحی می‌پردازد و در این راه، چند سوال مهمی را مطرح می‌کند که همه‌ی ما در یک نقطه از مسیر شغلی‌مان به آن فکر کرده‌ایم.
شاید بپرسید چرا یک کتاب طراحی را در یک کانال سئو معرفی می‌کنم؟ دلیل این است که سئو و طراحی به شدت به هم وابسته هستند. طراحی وب‌سایتی که برای کاربران جذاب باشد و همچنین موتورهای جستجو را جذب کند، نیازمند درک عمیقی از هر دوی این حوزه‌ها است.
پس اگر شما هم مثل من علاقه‌مند به یادگیری و رشد هستید، این کتاب را از دست ندهید. امیدوارم لذت ببرید!
▫️
این متن را Chatgpt نوشته
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/danialtaherifar/811" target="_blank">📅 17:35 · 13 Aban 1402</a></div>
</div>

<div class="tg-post" id="msg-808">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bmkl2cmUVFf6wItfreECYWOR2DnpwLAUPAuZrhwkDTadkt_6JwDq_ZMEpgF6Jo32bzImO5a-cqqjuqNXvoix5tM0pQfAagLl1xtVLt0Hw6pX8G6h2hcE3IbMZw7jiaROulR5Ycl-VeLc6oEUET2IvV94KlylD7vGh8ShSbf6skiUxSHfdhHXGmnb52kuL5pIT3PMDmr0LgbIhxnXuyvrIcH_C1Q1hDdoqH6s1902UNc54jsv9Tzxd8ga25r2JcICk88an5jcPXDEkRejBgCQY2mfjhYP0HfPCsSYPCkuoZJUmEADcQTVpk-DGlPP-8G0eH4jOfTF6PLw6_YVmgswDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KijAmwfjRUE0QhZHVzGGFJhtoG-eqsgPZeTbpB2o17MXYiCvLXznEQFlXY1ld-x02XD_hq7jxSomU9d5efI8-xxTirPfLL6oKU9-VpWceHQZrlt0PL6tWW2aDD98MU64ZijWNzT0cGzeqdB0rTQVhG2a0yqPbq7-jFFnr3-jeS6SfRYPPxq-qhx6KGVq4dtJ3d-lgZkytL1e2p_LVVkPN2neDsOK6fNII8UO81CGg7UsJKhsgaEpOV-GAInz4og-USeoMESx2CUQUjB0gZUIxFWFuPwzVDX--PQCZpy1CeYFUDknQIOXoxRYjhwWCQuXQfwnVr8W6PeeIOzzQBppRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IgU2FkGoanP7MCpBMB3GDel0kC_osPtrACX5-8gJfspdEvIfZKM3LfqQ0CUfEVh4DUE5vuJ16vrMN5qtQoZTEokv5z-355jK-Dm4lsgkmknoKV1RIz8tZyaJ_bp3owxv5DEtpHJo1KzadxBgiKv-InKrTaw6Uqojicj5aaNxQNS0HToUgJUniM0rgq2UTzgYNz4LisaxpGApfiRaQnXwSDxWJ3ibMNpri9PjvZFr-vOFvUkmOg5LY2NKJ-A5irA3oT5r49baRGAsCEYvN3Cx1et_ih_TCyWOMQWA47dN27gVAQlFAYu6Zfx4apFJwjxBaMToa4snX--51gRPOeKFzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن استراکچر دیتای قیمت خودرو در گوگل
💢
داده‌های ساختار یافته جدید خودرو به وبسایت های خودرو اجازه می‌دهد تا موجودی خودروی خود را برای فروش در گوگل به کاربران خود نمایش دهند. همچنین کاربران می توانند در این فیچر جدید فیلتر هایی مانند مدل ماشین، وضعیت فروش، تصاویر خودرو و قیمت آن را بررسی کنند.
⚠️
در حال حاظر این فیچر برای مناطق ایالات متحده در دسترس است، اما  در نسخه موبایل و دسکتاپ نمایش داده می شود.
♻️
به علاوه گوگل در سرچ کنسول، گزارش جدیدی از این ریچ ریزالت را برای نظارت بر مشکلات و ارور های این داده ساختار یافته جدید راه اندازی کرده است که این گزارش موارد معتبر و نامعتبر را برای صفحات دارای داده‌های ساختاریافته برای نشانه‌گذاری فهرست خودروی شما را نشان می‌دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/danialtaherifar/808" target="_blank">📅 11:47 · 26 Mehr 1402</a></div>
</div>

<div class="tg-post" id="msg-807">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFRJnyIZz_VXehrP2VIpnOL-S9LXdiQznAxTSfT9y2lvjBr0VNLwClm7x8pnOr-5gRyaEIpygsSz9WUHNRuu2e1xpwb0baHthvY-aX18ye3S5wcHOirQ4K0IZpw71atvpB561kOaD2K9rFuwh52AyDWxdwfctOShNeZO_9V3Uq8WmnqVBAVyI-N8D3AuRH9Z09pfoS5GsarJNXijb-CamOcNwhELgmm96M7--Bt3SZlBb88YfSiqzljOq7CJT3dL6Q3mWZdOfrEMwpEIQ3p_ZsZU5D8awKQ5vIuZlxICyQzh-C1-V8fPisOqvmtEppXh4DTtFHPMNb8zP25FKYzW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آزمایش گوگل دیسکاور در نسخه دسکتاپ
💢
بعد از مدت ها انتظار گوگل به صورت رسمی فید دیسکاور رو در کشور هند به طور آزمایشی فعال کرده و محتوای توصیه‌ شده مانند اخبار، آب‌ و هوا، امتیازات ورزشی و قیمت سهام را به کاربران نمایش میده.
♻️
فید دیسکاور روی دسکتاپ شبیه نسخه موبایل است و به‌ صورت الگوریتمی درباره تاپیک های خبری، سرگرمی‌، ورزش، امور مالی و سایر محتواها قرار گرفته است. اضافه شدن دیسکاور در نسخه دسکتاپ یکی از تغییرات بزرگ گوگل خواهد بود چرا که بیش از 20 سال است که صفحه اصلی گوگل بدون تغییر مانده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/danialtaherifar/807" target="_blank">📅 22:07 · 22 Mehr 1402</a></div>
</div>

<div class="tg-post" id="msg-803">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Yoast 20.4 Package_2.zip</div>
  <div class="tg-doc-extra">8.4 MB</div>
</div>
<a href="https://t.me/danialtaherifar/803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
دانلود رایگان افزونه ی 20.4 Yoast Seo Premium
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/danialtaherifar/803" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<div class="tg-post" id="msg-802">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">elementor-pro-3.12.2.zip</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/danialtaherifar/802" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
دانلود افزونه صفحه ساز المنتور پرو
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/danialtaherifar/802" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<div class="tg-post" id="msg-801">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Rank Math v3.0.33pn&1.0.111fn.zip</div>
  <div class="tg-doc-extra">3.7 MB</div>
</div>
<a href="https://t.me/danialtaherifar/801" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
افزونه سئو رنک مث (Rank Math) نسخه 3.0.33
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/danialtaherifar/801" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<div class="tg-post" id="msg-800">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">jannah-theme-6.2.0_NULLED.zip</div>
  <div class="tg-doc-extra">10.8 MB</div>
</div>
<a href="https://t.me/danialtaherifar/800" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
قالب جنه نسخه 6.2.0
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/danialtaherifar/800" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<div class="tg-post" id="msg-799">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wp-rocket_3.13.0.1.zip</div>
  <div class="tg-doc-extra">3.6 MB</div>
</div>
<a href="https://t.me/danialtaherifar/799" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
دانلود افزونه راکت wp rocket- نسخه 3.13.0.1
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/danialtaherifar/799" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
