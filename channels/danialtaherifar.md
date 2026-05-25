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
<img src="https://cdn4.telesco.pe/file/NH1eCgYYCk-t0iDPlm3lHOIMfV2VQT_0EbVl8-uHQbQfSFGS2TFjXKe4B-ETZkywHR9xKj69TvmsXzdtWZmuyx4d1qRhV-W2Iph7hkRgUOPJe5yUP4gdf6YfNaXBu36ZAzBAmnZ0ZCboJ5nmzeSNwJOZEays-tm07Ekl_Qqux3_-0Bk7nl3PUJSx8WEmUQ4EZazCU6Uco3lD_05kC_jjGmP63PR3gwzZBQJ16CIJGMfj_ADcx13voBT_XwZyC5-hJnZTuddQxtXzGtRZyydQ55BNrAzbw3UOZ_jLbVu2tU9BYOFZHUJxB-0SBak0hRpoqyhg4hkCvWBzf1JRedtHEA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 18:07:08</div>
<hr>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 231 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzVLZY6wYMEXxPonk26ZgJ12jtA380Uw7gtOO0jPvI0fC64XMZuLCI0YAs0f-OdRprHJMfdjxAFSVarpJ0uHACZYa3wOW00JutbuRvAryTCJvbdCmZU4meeQz2lRz_HPcN0-9Hp7uxaBZpzYgrd0ECnc6t6fjsOY9hKN9goYTMGBCATEkBaassyr6OQWgkVxqGyqtVjgGMswpqGS_6RYlrOvDi8kl-8kEkZb4dwZku8XzL4Sc5_Znr_-NvsmSuwp8R9yj2YEeFFUnjLobZvtq60ZSFcJXK3-enzn1G2MOabvfBB4zYhD5sCWNkFLlw6xFcfO3wT2mNgWrZ1CO5Q5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 296 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 675 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 816 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqMKojjfXQDLEB8l8QMffmMddng2gmZLWu0jzYisYiHWwYBwou6-DrHgYgx6dic7QArP4Fh9T5szCo9_h4_vaiAU8k6VVgKy_0f9p4vX06DHLLc7rxC_1I5VVsScQgWgGyx5kM-_zqNAYWUZyqyBl8BMeAABTFKG-X8Kglm9ayf4z3ODJBC4CnbhkR5dLuilW9jWuXPwb54kVbIlFjuFAQ8CD_8HLdodk1WvzBH1BjgeGIErkcsjuKj7amCUhcHkfD_vork_HNJ2Ss9NtZzewY-Z3K5y2zbS1vKiSnjOBa78b8FOk9CRnf_ADnWCAPFM-r1YVd4Sd_d3T27KH-7_2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWrVIIqp7XhKN4_X7fPfhKrv_wuYmh8dD16oX7Om3W99MFIlqYnEJ_BkO0fBsXFDKtDySdAUw9rhP9P-WJL0sSCHxrgrQjGHt9eF38IwzhJyTdrhJaITLZcF8akKe5T7YNizXcG4rPq45L0WZmXM1fLJqJRmCOfuMEoS74CB8i14WVLQUupl5JXXXMBB1U7oGpQUVr3XK6oYIaIX8vHqY1zVIIQ10FXY8ni6vuSb3-aykM_6ocsq1jM0rPBwUyzTZB-q2aAupSn2NUXmV2PfW-owKsDdujZdkc4WNzdPRq10zNDglMIJVGaMoQQTGHjCJoaLu3RIlUFDM4LVAVC3VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcl1zgBnHb4I9RzSeZm5STGF5UEgdMOdsivxbrifdeIB-Ujk9woz2MuT2wXJSHWBaTrIjApWzA8Q1reBMFds2SETEsvdUwdifA5FLgRPTn9V8aTkjLY3wXgoiuPM7JvKaN2NO-CU6z0tGY1buB8UQKUdLhrG7eBWR_5fe_YTU6ZUA45trcymHW3sPicYW67QgQlr7lsurerY9rEcm8Z_IUHcmd43axDb0DS_zi-IPzYC3ZaPhWvOidwXd7gbUbYZ2Dt2MFTVLWXw4-gub3IHR27CRo_k0c4q6Y5G4Mt2qodoK0JgiU3Bd7zvt6tJRgKVESXXU_a8wxt4Tg60G1SvYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N9Okbl0TiGr5Vz3alMkILUlS-g0w3NijE-4c1hyXQkV-3BZf9unjRidJs7aRdJTB1ffelMrJDBLk2zDWJLpI_AT3CmhCd0bDdUCKBUuNRTst2ayUjR0wxG-SOgDG3WGxEKDxHlg6te87vBbWYAYujjVcf0eH2RkM6ztE1EGNvX5sOXcHoKHJL3Wy5g4h1eo3CHFVin_DXOqJ7F-0TH6F8m6yJT88AwWI9i_Sz1Q7UIgQXu9H-h6ZC3OjqJ6p8ir93g21zyyus8VcUF7SZa0ee267tLYbe79JeFBHf7f75vOoO3xg6zqvYRsDwk99VVw9usyWatF2EvnYrSvieHtosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZqUBaqc4N643uf9uB84Xhx8koi9m0s5RgoqfOkPrNBpIfoydKlwkV1wVKi5IddDub-iwMw_k0145uucEvB9SzWFt6A_eu1mAEnKHZhrC9XeihWUB5AWf-zpib8or_-hr5SGdEjICCJTwOYHaMmp-38RsWROX-WO12DA0ETpPZKdmFDiTjPbVJF-xxYUqHe7wMEpcCg27T5s1Oqzm2eHE-JH49DfISYYzlHTVIhqy27Q2Q2KVNm0m8zY4NPAl9wGFkOKlAsm6xQZZpckzO-NZsZiQI0cs5hMnIQ5R66KjLkkh2CNNFNByr34nC7xRpBlom3tKGKtshr3tEcijigoXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZ6H1_BC0I_Lm0DY_CXglkMTnrZ0Sm_kHixithXmvdyLqz1m2MO_jBuTpDT-qtO1t-RGROzlZ3US6bWKGNtRn8CtO6c51lPaw2Wu1u6596A-hA9XI5KKA0JU1nB6paE488XvnPMb2d47InE_e7BEhOF8UgQgvHwOn0MpfvA4ykbw7vv4YoUnnKlG6Go__uJOWodtWMjcaczUyTBMZCgQEwuRiHVKInhImrqP-9RUyk1NwXigPgoqxohCV2jiIV49r1aEMx-P4JWspKL6M9AnLuSdtoSwQev9bRjcrNP7K8NKpsVrKs3FDwYhxALJgUp8pAw4FCW7qMAN7B44ipz5mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGXfqlqEfF9bNtBAPw370-x4v0XA-LNaOJFBl5ssqiTou-S-T8acfbrMRtJIJq6bFPrrMjdPSc4YUkxhwIRca95Wv8Kym3zeX1jKH9sr4f6vmJGiHAO43bxrgoU1nHZye6e8RADCPaN_03jkaN6uunCmqK2TCcbAWxi77tzDS2pvdpmUd-CDWjilrGZ2cfNdu1uBz2Q8JE_ffSPbuXz0tnjZC_-w5_3eE6qNXX2wwvYVw306SY8aV3LpxpjrsH8sC0Vsya2aYCHk67FXTrpjs2ZyiDeEihyfh3YUGClGMVQtfDEWZINldNGcaZ53i8AVOtJNWBLwyuZjfkHiwLujUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pls2TJ-LfAX-r-ibX5dwkx_zXSvceLj-o7rOIA7GdUkUq6CXW7O6kKFa3uUQJo9_njdRWY3r8xbmP1JZ8ExRT5x7kmcjiXU7xviy61EtV6aYEO7aIR6vzpAES8XNWS_nmw6J_p5i8oly523hnsdgnldSQX_nMWuNTFP96ahx9JBxXikQYmaOjQiy4A2dGAAQlsv_mAqbWySe9zVU9NQ6STs0khx2i0XTVBreH7eG_0ZjCEL0soAGTBHLyCh6E9jAuo0SLTAAyqCAsvqes0d77m6I0xjnJ87Ksa6BFAGfhWV_uzsOyno7fL5Rm6j0gSH-gtUQJ9XaB0uUTtGME4dO7Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=k4rG2ZULN9w2FP0ONshuWbtz0zgaOVGbTjIqHpmKbht8_UXEXfQPl_gajzB0PKyO8kOxIpkUCS812eMwb_ghM9YBDC303iGZHDkFItEvv9jcRApUMfIRFekn9AVVGr2YVyFRrdzsnJHHY7wmyzd7bqjudZUWMMSF2YQWe4DrviNiusoZMCzUrKdLY9tqhbR0AGPdNkCsMyYcxVkvAmXA4Sh7rzidNH9PTyZsaZo_xZdXDEFvRIym2BJkX9XUgeSHI0XBO1QdHaHuikDH86fW2FUo0XcPvFHfUTSvUWmr8DUFUgUJl5ajaq-h83_ys_-ebBv7xuOTvmYNpd4LuXzTPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=k4rG2ZULN9w2FP0ONshuWbtz0zgaOVGbTjIqHpmKbht8_UXEXfQPl_gajzB0PKyO8kOxIpkUCS812eMwb_ghM9YBDC303iGZHDkFItEvv9jcRApUMfIRFekn9AVVGr2YVyFRrdzsnJHHY7wmyzd7bqjudZUWMMSF2YQWe4DrviNiusoZMCzUrKdLY9tqhbR0AGPdNkCsMyYcxVkvAmXA4Sh7rzidNH9PTyZsaZo_xZdXDEFvRIym2BJkX9XUgeSHI0XBO1QdHaHuikDH86fW2FUo0XcPvFHfUTSvUWmr8DUFUgUJl5ajaq-h83_ys_-ebBv7xuOTvmYNpd4LuXzTPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9yVZYlPC5z9ulJaXuwhsabTcrCEos9S4IYCfmGjVJy1m18sZfoRvsBedJ5wwuXsASGfgj83tEV87dPMSPzqQwrN1HD_xdKMr_Es9_7Cqe0L-lh_agVUD9llSWYPPVTFfXFvLbPAXI1LY7LKMD876N4fq_8JuRGvBgysyXWbePdHw2OUq3MyVtt9KpppBcrcXe3EsPOqUPHlYWEm4TFXG2EfZvhALOgE1_TS3IdYvOatk0DI8SpCj4ndgTdnOPNOKpRYahSqCtDVLLsv5Z1JxC4bVC4ZbPVlKX-qqWmAXGCkXsJx-E-HddLmFLHDlhj7xRNP7lF9iZXQYjdgmBgsBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xu0tfzalHrQywcDO0-ZL0Iph0Q_26cMO0q5nNlNrkxFUNMwUf_76hrEiImCCVSAi6nm47wmN-coQ7i9uoTh_lD97KvrPhpHow0ljxUxfHaFmOVKE7tPF_PKnRtb0yP4MlLp4C5rKeOhq5Ptmt8JLp0PUjgyXr7GdLiEO97kse1oo7l_eV34lFMiaww8usgUeRO5fMrMO_k41Wi-axoqw5XHUqSZM7bQzMInEBVIhmK2nVK6XKy-wbZS35PTNp7QzjKTKV-uB32ux-a3iiv_LdshgPCw43BN8TWo1YfiE4ss5FnspCsZmNq85IMkSE6IwP5DH6hl8CW6SheFJ95t_jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PdOz52Y7KuYaYno-65EYSPrUXX3QLAe5JIhsF_6BgTph6kxQ0FHi04F830QcO9CVRKzZyWkz5Q6tEimu1e2wJwdnq69zX7HWQbGWinkp-4RhCGlWl3pRBbESmmjr4to2EPvgkKaFVXRJhnA45RUJNv7FaF13Fk7JC3_OZ80N2Ab7T2Xa_2OYAcF46LQ9Q7EOjk027AvG6F4Ia5w05-JHMTHe8q65A2rCgux5kZ_DrSwotBWnW2AH0cnrhvp9rwHw-c9_wHw_RuigQZ9PDr8yGiPBoMnYrKb9Ty2dQOTO8IBf5kdOxUj9c-of--FzJZOxJ1ikL_yNWpvauIsj9knwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pia9ztu-O0bUHjdgwhWU64Dk0eKXY2BYLxYhMQgQgtHWWeIgVHxGxj0n4ALq4FSFXcGae4RDbDk7aSuEldu18zo8Hum6J2f3Cd9sm3rOMyNWV5uskST9vM3AatEyi6NqJLdD8VzSidBHAYZd7k2V79Al4kjukLValHNY8Mi3ExPwsBL8VdbcwYLQ-uDhvu6gTiTQy7WrUGh-U3JP79GgX3BTkvHcVGGZKEFXplwcS5hRLuetB-zXvCZns3KH3RulNuWb36wDm8rPvWfp-kTknk0zXHBucef3ODzNsMTGZ8hHfnmrvpaZiNUw2Xxy2vayRW4QFRs1EByKaYYFhyN6-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwl-voBTG7wOlE_D9S2Eu-skG93YtRa4mjfmDsKUI01agarK8v-pPJCsNGGHaG6N9Q45CoouaImFEmDH02P55g957LKr5o1qCOAnSpwUkfbZBeg4h1Pl1BY_makwi1ZOZoTCQ6_VkJgjAf_KIKMJ36ZokaSZeZk4Zt_2YkcBG8g0LilIAFgNXAV-2mzstvTTlcUmWYzBTIubO9qb6-oGWEIfRQV34v0JigBzBe_ZAwCugK-VWdOrGEFvfL5uvGxC9uczPlAz9LXEcp7iXsdvo_bSih4SLafO6_tX1mAzQwGBs3nBlh8LsNp73gBsi9aZxRTjGjDyoZZVuc8BytUvBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orCRjBirK4a-4pDa5WV5vrcudhTOhMrNBQNFPSVrzyP5kdQxyWPPCHyO4crJeyxQU2xDo3a2v-K7HCCpWPEYNgNPdM00CAVLvXee1g-kSkE13ywVFvnys_biUe7a2ILhFoEKESsWRTJ9GxWGu6HafEXnuD0LvWL3crMvSofwioAktXhbj_hRiK4umtNBQcOnCPCPfht_CoRvMkoj-dW_yitbeqM4N9n-skyqY0KBV9zpk9D2hP5RpwvzzROUeo3jwMLRVDgR8Fp7nM8j4WXQY2vFDWV3qkq2cVPI_ypbuZJ82C1SS3kUCwezj5GHrj3UcKKisc8ROYQsps-7K5ne9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kEug_Byxu0W-rb3-RjT0td52AQi-V1r4ICUbSGqs8XdGhxcXvKCfPPh34mrLHO4tOnsNuyDaJS3_0sWg9tPbNe1NiTyvnWuScarGPrE0gVCwz2tS8bGLS9zV_mZ2HAPQ2mMACDFQuiRjdTCrrUpeLyyzbzB6etHF1JCQ_hC8fG7obBdHKjPPZeaiqZV1r0LyViLdUYA3aliFD0MlpAF5udK9vpKEHf6id9IiZOjqCm2DpPXWC2n8Fl9GXbP7ymRAQxFKIyOC26RFHqSYDm5H47LwtEzaoiJie5iSdnGeQ4B-tF2v4dhxBczdIa98pXJHwcId0I__bz9mKIz-lv67UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRqizUwC5Uv2LuPqbJjcuczCfYVd3dTLGAicaP9IY6i4BrpMI5JsammOGFOWguzOx20tmsdt5MeX33z0l-dt8wN-APgA6NRKaNwykpiMqK31XybN8mis1WVtK8H_ARUL8lZV1M0ZLXDX174yO7f7ZeIR4tv95r8PMM8wsfrIHxSpyjxR9hJNb2gGtbvSm-RR6jk5wiIctau6HxOnOE9giraZPFqujBdJDmmv0LgSBFhJHCYD9mXV8jUyI0nBnjC0o4wjtXkA_zvX9-PTcfT79uagbZtZlIEcJMrAKd99cn5uA0gRpwXJyOeAah-8KL0kM3s5-aizXrgKoZVAeQ-bFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLlVUoIyKPPX7n2CfKSm54jLv7r9Ec20NMXk6aTTTnMOQiyxPeUDxuLZWJyXKpEkTfz15K8tiBB0mokpPsKOje1v9Dp9SJUB1OdtstuMXnh7muEc9aOal0HM54wG4sZOdpH5QO_aFKTXYlEhR0pKDHhrTXWaoL5sPTdfYBuPcNcg3Vp1-nuigkDqM_0vb5Pzl9OI2EK0nJHwG2izTHX0qjBxnDYp56cb1XGdRjaGQBn7k13v7MuhWJQ_3lQiVqu6VTGFBzOhmfW6X2FC_HSMBQL0G8oo62nNSTmDBQNC95c45Dc_EVGtaUKD0Y5vq3TSDqeWOYb4KISsiyISRuQdhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDYI3BEq8Qy1wyYNZ1xERC4n7-dHIPvUjA2Bu6mIPvP7sSSDP8NJMTHPlzSI40uNXWMlFK7VdBuuR7jW0K2q-TmyibFKfD-D6gVZl3XtbtP1eP0BP1u2QcRw9VH2A5EJBtjyuUCth3Pr8qMfE28FaXGO5YliGhpAL8iNpd62ImoZbljERwcW3Li6FpA9NVWzUVQl03O6MGyjGyWEnYnPPaN8VaIywCccascOBkZh5YoRPsE9JKH8XxXHbKWUOKCYCDzQ9hP2kYE6Uc6N1MAeADPZf5OcplUO4ojFVtDSHLhAA4A9TSyJWSC1-Eeml-CKYwX0wq66wDcT3OZXS4F0GQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScUvzvZR-TeNMTUTeop-7yZXvtP0EVHbDm2A69Y07sGo4x7JIBBPPpTSWitrcXjJKGrFMSi7tXu7xJJTqxNS_C24OGsW54OCWEkjC8b2bcwk2mM6IVfYaTWSVkF_DUMYPI48oKXHKagwxdg6bZBi13R6G-1EsklK0pfr-St8If5Ti17fmu4V0DahbnObYMVt0CxohoKnoKtK3GvHdwbn4u7qSO074e6sJe68j_t-EIJK0_v0yWJvjuwMQQLfQh0-IZGTCCReGQiE1nRwIr2-x89Zl12JQP7QpDn6Sut6Ho8BjopB4zX-M0GhMWcuST1V98ZqKrae4Ej5T0T-OoWF8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGzF7vSTFVWWyhPVPvfY4zWvDCoH1Wd6Z67c0mvhtgvxlD31pzxjm4Hd49tu639l2AwpmQaCMOfWTEtcCMVQRWURHu47lLi2LrcwKL_AIDio_5G-kHs5fEUwJfcTUGMaDdq33lCynzSqotFtgGaQtM8lSHS7054jkfl5akVDIAuPbinrzNDy3CqPON_BQTY7VMD2Jvo1f7PIxwYbGwi2RhpyWD2cy2Uei7Iqjl0dZWQiRnY00qH5vSatudLh4ZEjpqS2s_MphmQn83WXA3UsKqMIO9fOIe6vb960wSo6Hl3bzRvbw4QttYfsnxSKHc-KfHfQFt7SyXNIyAz-0rbx3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBp0j4DPzkhepKYDLmpteY172gCDZLm6sVMbjzroE2PWYLqGLAQliewMloNFm-jUDHANoAEYOUfivtXZftEg3I86euPe2Ux0hoJE5hUNlOC7rGWy-AKLLQvWcB0NSAdvGOOyALz7kw_AerjpxRcNHGHiUJq-nNrzN9esXuPTRcFl-f_My9-htmIB11bmeUas5Z4qfo42MOjNIpSAkIMGSAFmAJFnFtxVdnCLHkMptisNfC4PQ_CKc_9g_Vi0sl8yPmzBP94Yn1NBGnL8kN7mX1n-bFmNKUslgMhMqoK3uERJmjOacDdwKFynU0Mbn3HGWAgbECO01995reOa2_Ltkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/opMi2kMsRj3lw7hei178DGXCxaS6lq8DW-u7VUMnivL_DL4TV4bXbw7E5Ly82R3Njutm_eavzO2GLT7_7Il4fWBoLBrGAVgIvmNUKXSMJWbRwyEBV_513IEdG8kqExfFRzjLi0HtkxQTZ_9-7eNywiYaHIiolT5h1kYZXvE1qRCqCNUDYbZFPNfdL9BGh0AN6KBdvy5JIcDVJQZSqKAbnBkM1KN15u8Wh2zS_pGpEH3K9AZe-Z7GWj0yaMEZpj58VicikppaTt1p_laGVsyTXUNnwS5ALoOXbkT0Yw7YT-Z2DaltnAaC4-utmvc2WF-2ewjs4n9xBGLb8KMGr0_f2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xk96YSnvKGOgnqRidkSoq7hNX5r23PCgE2TEWhUH3jSJfG1u2EKHPL4cago0Yap6Kipanw9S6FtF8lhfz3V4qEPwGgKNj8SDbsxo2ta8ZHt7x85G8NuDmBQfdEboNA4SC5C5IpffIivuxscWvZ0w3DI_OCNbg4yoFiuTG_OnjrjxvcqMjGHoGd-c5COKNxh8S17SHrXs95n_p3zaGEdVnMkVTZiDNfw7KkZnIClkIpkmGGx4_Lf2RdtnMiUNBwFu8Nc9JdWVfpaK1n-4ssYgdhLU4dBY64pQlLiXEERwRaG6z1U6wpwws-fZUdlnDCtrHgeI9T1jsdxLC0bI8NPRSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Om8b66tEz4M7CEHoZeYZiK7338p8Y4jEl3e0EcJq2g9j9yZ39Ab-JyjlMnMQTb-JMvhVx1x2kzVzEzi49P9Mx3LCs2ML_Lsa0q1NoFw3MWJYdQ7-dOEaAYCgJyhTnCq-J4hfNyExb1nSYk9_oUDdCQjRYOGiHPYQP6FP6-AFmEAf5NCi25joSbdryQqGhVhaJ1XNotrycQnE14xlXFndGwqeJdfd_vdOcj5ePZzKQ_Wm7x1yLIilA1K1c-UqaSdNCjHthWYXK3Jo0uro2x0h5-ESXq6M2J-mPFyxz3M_Wzy0GLuiDbH0N-p5_n99T8asJ0SJ7_8ZOyUmfkQfg3ey1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBoIsy0sMJ73kY-mH6tWLbMbeM4fzQh0RTwkSeZjkHhRwbf8rI3ETtrYQKVErrj-BqiHYX5n_45pGUELtbY9FMHnxanA09Cb61XbQ9wTjfX4S27l-HXuO8GASKQjd2LZobtc9TQvf0SmdclRsJfWzRBHeQxtyNT1c_OaqgUszq1HV-fJq4ne-DJamwm2yVLL5QTck1XpWHtnBy5_Rvd_f2ZWEosfSnXxtIt1fnyN1XR3OeiCZMedxwpG_r9LRb6KBo5jJ8VABSlobCuvhuQZIoUN_MbyJY2BCrWGRdMhP1-H1Pqi1JMvtsrHZLZU9BZSG8ywI6rTpCc92eQsA4Gh3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LInuRjHGEqH1rTYUKcC-Ci5cFyJYkyLiOiWQF7urycFK20ER8qNHwE6-0eHvUX-IrRAUzopTu77acXPnOqV5p0pt1xpwy6hnHxD0doNcrLQdAoR3O_ahNzdpow9ZcLCUEy2gIx5LUk8rGi31GVlIqRbgJceBo9WU_baqy4hzXHBd0Acpvas0RA42fzMJ8SLXQ8i5usJbSpwI56E7iYhl7CK4pQuvlinvUZ18XePrqdJw5vj4iwShpZVqQrMGsbUfsm46uXfCGJWZzkc6BurZZa2HhaP2ABAdFTdOOzJcCpJVWYpUc8pQGGCBbGD_aw9v8YeSxeoPyxg8e-5NJ28YjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TafmOczRTvJI7KtYT1kXGm4nypOfE7itYTlt7HQ4rqmUPsPrtdqYwxar_bVBlMBWlsqMIW0W1ebrJl7RdDqnz_Ex-IZ90sgeLSwnmz3DFgcPfIkx27Voc-VlrPVPVJ51Uz5-dZms5_xw418lJskNQs8nQlYcPXYI6qu8zzCUG-3iwJM_4szTP6AGD4-V9iw1EBvC_KnyxNuxbuOpQ7IwBeDpTcB4Kym_51NLUlijDvj1uIvmN-UoOncVYIUew6VVI22JzW3DCTM0sFAaEot25-vbnJylJPJ1sdlkA2bwJekDsMna81z8Ir1x9wH548OQzWWzPSUHP8oQhgB5iDF_dA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2hEW905ELkBD4MBtKFzUUyKyaQ1xWMUTgf5XxYoNsITvbVjgFjp7Pw05Kma7o8ocR3BGaa-VydQoZyjwYufmsLrLMscHFvuQNDq1Dudd1HSFCPJn2iqxzfn-BYeVrsrhBo3R4buOC7eff-sSBhMufCXzUZEOcDTvSDntn4PqrUXAWvfWw6pt2iN_xSDpR5j4s3TC2puqGbFlrj1ZpIAy6j1kX1V_XZ_3Xk9L7tPXDf4cb_99SClROwemJFxMfIZjf6G5Bzdig-y7VdRsDvhTSSeSgFTqk3sDwZy5DFnAAYvl9jXBReKtvgU8gXpUVKMyKpccLrHIyZwvSOwJ9e7eA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVs-T3Xm_OFo0rReLJuFZTrguG_fh7ajbimPtfC8uvPCbu_AQzrXLbFE9FaltZQ97tEeO4dP_JDvq5lnlHjKK6NrzkYxQMkpx3M9MVHn3rQD15ZtHugLIzNpojABLtVWoQKYi83aFtFpFepilNHJHp-YPo6ZpueyHneGv52wBo3PkQGNBShKv9HtcvahJlROXJPARFR4l-ykou57e2oTcnSDIuqWQKAmUOVlLJqQ-Ej3CtJ7TU4zE1yQOkclBwWdlbjf-qJdojnaATjQ7LQVCy3WI140z71O1LBVQRN1ijiVa4O4Zv3mXwOytsHd9tQz7dPkF7aYKLt3X7rLNtcVFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkmOxVDDJAyfkRtlMCopgoMgrj4H-tDI6iEpmMtvrgBZWdoNI5_8woA60lTx8fyPhQFeqWhGndO3XYZ9ldLdGc1HOELSUfk-Q4V1Ar5tWLbLChHO3ppVP7gLFY4Mv4UFqzoiFuBjYf8s7jtRJeVfn3eFVeAZwqtBkxvgQ0IRRuGfLpcItik7vnXHl8UdtC9IQNwAXUWB_uyYACsb5VvHPSCKLJgPI10V4xXb9JuohtYNyLJKBG0v7DL4smz9OhKOFfCOyWD-9hlIwjPe489LMdfaI9APxQ5gvbDtZ-PZz05f9no7qyNeACzT-ikKJBmbJuJiaHg88T71m46lEQFseQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXNe_dxSygzBj5t3sxECHfUXxLDtSj9ti7QGGWpEAI2g-iY1ruh5J6NvKUkH0X7_D4pk6puR_Ogsh-NZHVrQ9gt-bNtN_wIzUBtJ_mI6pW4DpVnN8EIwmawuYzM68NU1ApznP0Zp-82Oc2i0X83EGxy0KdZUNrmVQteAYMyDMgsMv_9YGTC04js0d4MpF1GZbI8MRWk53q8jZNX9W9LXweqoaNg6aiK4Mz5-eHrPZDGlF_VmOcix69vNqQB_it64PRsknAdkGhKo7eVWAhyA9_BHvSxMFZdNmWN1tMJWB3Yb3OHl6ESZiPlQAbQ5KkmKvmhLT0rWCQfAOZBACgsxIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EsoQh1PPEpQygaNvTJc942lxUftSJ5Bviieb8l493ebXMbj-IhxtpuGJ2Si18nUH-xTZ-Gvx7wdnIIBHZDfAsgW2JidQRyCGPTdtxdZK6fpxBkK8j9oE43s9zpVk0A9xmhWLkjRQkGav7kPnDodra1QKvkRbzvkcoCoEc8_kijGM__FZ2HG4THFGztBNrkjngBpeTcyO3dxPOf9ESu8aw2na6dEz_9itEIdnsrq3J-lxkyPB3vDdE8hu8R12vW51WbpkQqIgjQlRXFRagGSiQXPa7kvn2rp6SSoOYYpzO1b0rG7kJ6na9J6c3FGg8livtDP3o0LhKvjpTDF2criOjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OWG9xmaOlrwG7ooLNjACIOQjQpRx2NYjV5DFLMQH3mSTit_06O67R8mpjaHvhyoOh7GMfpCaHuZ0QfyAZ69dfcBt7K5WohX1BKI6eVkfWhWXdBBB1jZhAZCczzzTTidFk0o1Kc4vJgXy_2s4E6eeIhM1cRNDS5ZHw0Tp77a1XFfixwmUQo3HZrPDZ_Ti4QeDLbycAQ-Ees5kPl_GUA-uzzRVA8gO6kVKTlauuw3zQTL9-TSLfwElDIloReJtFMZlV4nAPbo4cAUhXExpfMbsso6qcYjGCWa_4g7UTnGnlP5o2FnZiSbAv9ixqDkE8wdJYxCOaV3UG4lVTanvh90PWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhiJFHXeXdsmehWuKUSMFFM-hxrhg_-2pwCGktJWfLDE0ZwWVx9OsMnK1zJok5KgfIOB4nqFhbDdzAMLHEq9ZBNIyBPXg0TpiOXOGN--xzac-lVTxmSEm1m_dCTBXkyqsJYLwYYQeKliS1L5LBpjLQQDtBPbWy2oA3S63p07cE-mCNYxXMjQUMVaQIaawjSDMzNIl04k_h3kKYbBb6EX5qVqzJmCVafx-TT2VKfdtVlVyVpPpamyJJSti83_DUaQgMitL1xvqqoxpOTQOMaaCHApcfV9kIAB6nlScJJD0grS8JaX41eKQD6yeda4p_rNd6PkpeP6eF56zbp4-DjCnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMZU4WFMYKTFA1HMPo50dgxyXwze9fya_uOzFAjcp5oitrqMWl51eCr3_A5nuI6ohqjp9YpZNADUZbwzSgpMd2hd1q03Uc6nNw0-oBnynh3xNpKC0hwm_slL7l5GtzRQfB5dbEHMlxYKGKuXQ2EJd9MwGlNNfqqZj5VzRUCSG_Kz2_wcDZIcRn2iP48B_Kq8suYRR_cLcB7Fc6SA5G7SD2cJKMxwtop-Ke2fW8NvhpGm61ww8aJr7pKhBWc4NoHMC8WeiMq5ZwrJrxOn-AOENkM3XcHHyGN8SSyrmbMuB-crY3Wy4zLdeEkqYR8F7MiYhpGQWh_qM29AVSZIrrz-6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbieUBAk5YVdOQuoxHJw6x2kEPHex9jo_8b_85-bnCZn2uLEVSUBTn39rfityrnmGaoTx3Alxtz230C5QmzPtkimDPWFMufuWSlVk2y-l8C5VwIYeCBscsZlXeDcO3qIO3XQgdPajU-75_qTkn2R4AivaeJKXO9FWCx7O85STyWV6-VW2lPeeoB36mpnMqh8nRGfntLfxQPrbt80PEyT77aqS_y35WtIK6QzRpNszmMdUvFeHDPt-o6T_eZ1NesXafSEdLLOLErunNFQqYGmR5tygi1u2Mv92Oc0a_VJ6-1Ud_ez-hadG3Ztmr_jbGBjj9WPGALATKId4wzdR4AV9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWnrVBFZB2oQ6ldsowuYM-2Dpt7iFOkXGeYyx7w3nDsZvBWka4bTBhkVZ6jqLjm2GHEs522YN6GxxKWMi_hXHzIztFaG0xdI_BGrscjECVrBD3hTbkka1raawo9zVCK3Y6rVirxuofhrjh4VKbidnkO6HhTYxa5GqsyP2X_6l7fZXecXX57fLFkx2mvkdByNdjOfZdVmXK33FPWgwDqvYQJAR8JJ2PCYx8lIbH0spQHcxWaz4gTkAAddeMgcC2Rn1cb2CiEamjP5x90_JSEcKohjG9tuTzoSu-HWGOTu625zBIDF9-FdlB6QmbKFNTB6UQO1OajDl8_V3FGAlOG5MA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 678 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
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
<div class="tg-footer">👁️ 688 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSTua_VToyHyPmCwPSFGb0ULQ_lAcnPParkKZMlMZmvK6TNTJR9Tl2zAGDHauGgG4LeVvyjMWtt7V2EUK3dYxNBNotEY2xAIYJhUGTSi8VKB5Rztdn6ChmugCq7sS4A2QeAXuIFCBLAmtumZcbuXbOa99JFP8Z6fKKCJ5sRqc5kDGW3h5DdUTXGjD-qAb_jVurB8SJTlqgAswDcRU8e20DmJOv6PstgxhrRMszn1esR9TyrPMNWHehKFUfPYigBf3CAwJvpG-OCieLfWubJ98xY-thZeHX17bfDWASz6JFhvl5kdgT_EhTasWvtUIVT9-RTZ9JobvtgE0G7nl9X3Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OtjnnA6pU7xXF9lzpwZs2AuJUgpo5Lfs5D8R7-l0CIMRu_TCL-e2COF_41pp9w9HbJgfq_qaAj2D-Huv0gmVaAVDWeH7hpE2ZPbauSd9MBlsPoJd6uJByxiMCsNxQwD_Bt0I2rqXmPoqkfi-GL6CVjUAvtFdOlL5u7z_bGp2qtnIN7mtscTnrwbrtqcL_nGZJT6_aRxUAc79d2ilfw5xTgAg-HKUmYgHy8TJdkLYFTknlHZq1qzuyTY81gcYkJMNNHjfE9NYHEC2ZH-sc0beveCpS1HWcx8QWeSGN2GdzbjaSeFYknK9STEn4i2bZ9r4tIOjW0-RFj2oeUjOpFdkFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgDYcZ1Esdp32U5h5CbYAyDffs_aAp3GIzGBLbHT3zWrth7EXNQMvv3ERFWN09akYGa0wmfSHSizL3et_Ny4otZ8ffv5v2BG6bveQROMziix5U3DjxIZMBJz56TsHJuCegeLj_38X6rVKQeCB5sTYPI4JZsoCLvgfD0lPqGm0yAzcWXMduqJhKRon7wUwVTeksA4RtcmMq9TS3Ss57SBRGV7IwjSXcp8DZsqa8hSzIuqMmuSjAdIY1TDV7VArhjisJa4qm1HDQsbjpLu5c4fk5Z4Qam_zLOLy6axeE_3gy4nVukbUmxvZKpwflcOUGb4LMsQUy2OvoaG1eEpEsmUAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/la67SaSahSYoHa5XF9RntTWV2XyV9wJ292up61HurEXrbRQtxK_aohlSJ5543FiuSRu1rEAJwwuJ-eKyiI0IFjCvy0zzusjTISt6fV7iomJtGTA1jgQEjOvaC1d0oDp3sP3oCJQx--QXGDNQv-VDZnryPLB4VM6FaqrHaAFdWAbbUxDzN6Umn6hBjAUkl-4EyhQ8DF9VlE6w0Na_84pLebyHXDjovY44SHYvopbBtM6BrW5DS2u4RJ9L-YgYgLFST0m5blRdMQ_g6JUXixK5aO63q2bKg_NX61FNjqu4UfTu-fmZgj_9021dzUZgn-yS2EIcXt8PSewHATlkCBuRKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3Egvk6EkVkrNqRUtb4_rcdB6Qls0ZfPNeAbIWaOxEbufFyZwl6Z6wYRTQaVpKtnra1rZFyxgnyxdnEIn1mEIcW-QfPFci_31n1nPfw8ZwhctMNBqfD3AmQYAQjW5s1t_nhSPtXY9JUcQG-Lql2MXZwj-ytRpILkHkjz9e5f9NBYMCgBAMsHqw2TikrYSBgX9yqWcXE4nWygynRSkCVRXCI2A_E6E_txRhDHfvPfgYmIOOO_eHXnXdM63oeG50Oqf-YP1zW2dxQ4-JF2e2ZnphplERx3-337W8UYVtg-PII6HNrd4rHRYxK3hgX0ebAFxzhgUtdDziX1yffk0ViSXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iDlTPfuIKQjlQcAigGRwE5wBvI-5-VZPiolPNGbZq-g-cOyyNJWW9-i0gBA9Go6Fklvcm9UPXal6ct9Ne-ygZOq2NIzxOAJPiN-Z5wns3NaGqr74s-Dq_I-ESZhhQN-Si1zCj-UhZbAwX06oRxi7V00NAqgXQp-I8dPl8opxZEwfxatQZbI5ZeJP2FuZa-86xnyCLljOJhN5wN7XpOuSCQ0w3mFdRvcNP9YCRFeb28i0pXDyvsWt9yJacN4aecpiMizVEce6p_lLqgZsk36gPn5utLcR4ZGdGaXLfEliFRiagTp8t9KpFELf9fTSds3R-oo4jYTDKjHswiO_D9xl2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cX4ARfa4NHuAKwLYmc9nmp8MKt2T69-kuuKKB3SWb3fFFbPLyhwxXnsEFSX5SWHBIcj4J-86iqwLUko3pEnlBnguJw5jv2UrdYj7B0lFbJoFCQqgmEJ15XUGtksL64v79BfdNLhrYYmLfJMH5FNJ-ku0m-VT0ay4_3SKW45IKIPA-l2RJ64utDysPQeZIXX5pInlsetIOYcjJJLi_Kn-PoU8507ZUeaabndam43KrW2d-joQBSlS74BKZrqZPiwEmXBZzQLlDrbkqHjgOD1-nc79vSDX_GLqAkEtgLqGTCRCk5z8vSiqPAIq4TMIwGe6Em-qE2_a3tCg6HnL4HkZug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5tRJP_h48nWlijfLkN0yftwnslREFVL8lb62CMDinWoZVmeauGwqXVXLthT-Tp8-4cqqSbstxNL4NiNbYNdUIYWw8bhFW8PHg6ELPqHtqN4jr6UIv8iqZ678qD_t_ra-R6qbBjOwP4DkcHkvTu_1gBpq67HcbVdJoNs-cgA0i99QtdthJFoVzMJBKaJE-T7aqT2dkQaVpyWPY_litwSyIJeWpSDKGeyoHnrFd_ML1ioN66mKPMwTl3zljvOfvVW2P773rFSbvCvPZjOl0EndrVTpQs-_vMVT6db46coFQNPRcDa8cvTrV1f1-FMGOVSlnCnVSrafN-PFeSP1zo9yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jK9Gm0RRaA2dSjDtrrs9tNB7wbUKO-6gFVkxKUBndJO48Xi2fPKexcy2EaR-Df1npiPnM3ONvL-srSsojIJkTC2S5ofx3cPuHPYOyFvthiJiE2LleA3TlVECtcHyaQNpK7jtl1JAcKPJOpaoq9jvmL7eRKb-bZCcxDJ_Zg1teyUsan0Ziduyirsa7AuDchRdAIFL_XQLN8UZ9kgXMHgCrnDv1liecc1awI95nnAzu5wN4qPQrWwQgKRl2m-rsY27yGzLa_KeCxlcVUT-mly3Nq35mt0oA40abNG_vRtx5ljF0PCw2uuRXkkYNsSfmA75CIUV7RFa8sojLSlLbGgR5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PC6sor6WToEwL-0LfbQ5eoWCQtNYt5QVduV_s8Cp4txvztoV58gP5q4LFUkUck7b0jbSQrHpprFUds015R5aFDj81ZY9NwEDrWB9UEFhJ9QYqoaZ0Q7h-weqm7_ifWv-2MhzT4mxva5M32TFJd-h27k0OumKV5TQFTWgooA8nSjHyYfT2piWlQubUGrDXz4RS9qn1QLHg5sl2s2VGhhlP2a6zsNsUfYDdREA-zeij8nB6OsqNstjPR6PdKdEYP1dDC8-lwRRyKVyBuGv6JG4z3NP1jYQ_bKZWRxpktUHjnVgqhfUQDZDZ9-841CscE4UwtRSdBBNBe7I1KJV7nBGNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uoDWt5gyrJiq7XxYqnw5edZ876cTG7eLxUjk9GlQKgGKqyhaHxZlBMvO3WAy3XC_B-PJTmij88a0e3kNfN251WiR5W2EaJfDNiqJH62p-MCDHdzTaB5NTGBX9g5US1R2uBTbCVFnCXcUXsK1T9RhuG0CuWH0HfxSKIpo0V4cGdBPRQTyFVcIEBMDk8BgV5jL2F79SAAej69ebjm0lHuUQq9XYoO8ZghtuzPoAC7EucCoj_4CeiY5lV8eXgvgwq7H4zKp9qCjpNpq0dpqYqK0fM2Kw7YMjZBr26IqZtiwl9mULlvjrZyPeekobJkGJxqay99vxtQN0wo5H_5kUSn--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBvrzY99dUz4vMeZb1qbn0JUY5w-qjx_B2GpCnlLWZgTSgeoRJvHR2bFBHM8-TlflBlNrN-RXLdQEO6XgzT3gjyUwg4P4Me7tbTi04SXUu9rIxDJrjKeZnS4DpKFRjFtIqu61AqFE9qDPSHY8W13KatwgKtrPVd0Mp4lJv1etw5zGyFgBvOt3VRlnfN9-JJEyftr3dabY5HEU4FPwvXI_dXD222D5xjsIZOCwi-kMGsrBZAqAZfbuBeUPQCaiAJGihSbRc2s65Uh9X27YDu4l1VpBqWJvCaTD-Iuj-44XtyVbUHw3UwkKpY0LNb5m6nA0lkM2HZ59begglNZK6aVcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_efd9gm1e4WBtCr9DmSamMDr5WorWKvwSP1meyTB4bpKrtgAo_vDl0_y67dBAU14nlqeeEZOVIrqEnYaRblji2uF2Wl6LpVYexeHzIYlDHc-HI_zjkLo_AAdjfLO1zR23BniJGuPHnUvdUa1acDaJ0MM7qJ0_b7NK9Opkj0HWoL0oGkY44jU-XerAVcqoIdtRknLNaxleZUaj1zWQkwW0H46eA5sLyXsev3N0ofUXydMsU1kfcwF4xNXuVQxLE2HlDlbztIsS3W0W0QPGx783KoKdvonkfYy4szwPf-L6Y0B0sg9x_W6AmIpU4FozQAh4_cOJ0qJ3fdiHOt9H3e2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slQE4M8BJB1geFXNXTruiDnDG7UR2DZueNdbF5oxL-AbF5XFneVqlINnGCgjDwv91gRmn-sULfemZXQZi4m9L81wM8Icbv95ox4krwwHpzuuVo62YOzPrD4Mif2ncB1yZXH875EUEf1NoKbgZLOu1csHJ09w8H9dkNC4QFwuhFeHJuo6bpLduPFyEOcuEM9b3bGHqUVFzYC2QtMy2SWAFA8pW4azz-QlmrRUjth3UevkgCU5nZ3i26j75_yYdUQur21qaPqA9Xt9pQTJdBqJMb3Wh15aMJWSJsuy8tKpM4YnCEXVWIbJb_iDOFoi7K8TIp1zQ27yQx6qYwPNDpsOsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKNSNwWekNMB34BWMQhevU_BtWTGjV7JMABvuHkXA2RTHFwIOT8qZXtrzOO_pvhWng-hALovgTFLYbsBqfq-iMlfXfy-d6TYCMqEn3lCVWNuLivO6lYEAOFg7XrZgwafo6cQFyXE49TiZfW4LiHMczvG8eJiWGibq9_yvAN7T_VB1cV0uWcjBAO9DGSizUeGmdst9hoLxRI_AtSrXzRYxRyp22OFTwNUd8hMbm9RJvtHPjg8nnUaEarAmTs6pDFR5ys1KWYy88qDbmbZeNz77_NylKU04EzEUpRk0RgvjjIgsFD-L0wrSDcloaDrA1_FULujp_3pnsbso788358h7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKxFePhH0DCGHOjmJUf2cV9whlclR8cQFdjpb2-DE0nSlDQ-afrcQEEG6alHYiy0OObKs6ZIQI2IPsLcalSp5Nu8vElwIf972X2EYOjMoZIi4q4A3Sdr4PPi2Y0qOU_8ju9GaSNVOzLGwN3RDmWy6wM59qkM1af1o8qW7qJZuMJ6Y0UZIo5KR2-zzEoj0eYL_9rA3zY_LMR5qGOp1Z4NVhvYFbbOYpGUPB3Zoh1FJ0md-BA5PWT88oY0GBtDQwqJnbySt3Y2jw6olHJX_nHFNX5EUVH5MO6Nr7JRJS0He9KykWzM8mKoGFDPrVQvy-I-4uFawzoTO5j1CFmZQ1-fCQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=frrGH8KOhjyvPteivcLpy7huX10ohaA2ot95TZv5_ZVRn90dRHddTkMzgmXithjpRf2-Q3GUyRLPJnvMPQacsPukf2UNTR9FV09TFEdDHtzhH924wfNJIw6mFJlv_MSP_KNjPGQ8QjLhZ2h_68PvCa-ooyR4V194skvfdQX_32mTi-WKe5tOxbMke9QDxa1xxnnYzTFVes8rqiV1b3w4_vXSOeQFIDS420J9g55AT6ZI4Fhy4Az3sRHeCLYtfB4ooPvhS0sMVtuy_BefIvZROycoRCoMEbB6CcJcP6IIhgHxJmvEtz_RGznhLJ64mU__vZWl6t4Dz7uMB4jPPcuiCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=frrGH8KOhjyvPteivcLpy7huX10ohaA2ot95TZv5_ZVRn90dRHddTkMzgmXithjpRf2-Q3GUyRLPJnvMPQacsPukf2UNTR9FV09TFEdDHtzhH924wfNJIw6mFJlv_MSP_KNjPGQ8QjLhZ2h_68PvCa-ooyR4V194skvfdQX_32mTi-WKe5tOxbMke9QDxa1xxnnYzTFVes8rqiV1b3w4_vXSOeQFIDS420J9g55AT6ZI4Fhy4Az3sRHeCLYtfB4ooPvhS0sMVtuy_BefIvZROycoRCoMEbB6CcJcP6IIhgHxJmvEtz_RGznhLJ64mU__vZWl6t4Dz7uMB4jPPcuiCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8syNg3nsorMfBlYkNwJZWbN_Sn8a8utF7elsgRSMZioooDaNbdm6AOmKhC43EJOWW5enQwANd3H3Cj6fOkoLAQo4mHW6TUJXlzIcGVLXiMfyJYeG5juAhWH7FEAm-KecEFF1OdQWEkgLrdiJ7FO7zO8TvIc32Ywh91WsXrHkyhkqgPx79f1ghbQlZYSI7uNPB7YMACdgyJw18GL-rqeilEM7T2Cx5WyqxhK7BFXlS1WXhzu3V1crvf-mMEuDmgMROlckdEP4lzZiwSL7iow91OMBQgCTnP0I0dCSEig_yK_SDQPxGpotWhCdy80afVqoEyO64C_OZ25hUxiO0fEZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiEsNDpwgqcADrA0Z23lBDP3rDvVPz8_XdvIPMDpg6WDc7ITXcZ4bPCtO2WAGYVGihCl7VozHVwdiEHIUQHp0NPRkPI6o57Bu-F3HcsmNnLztbfGkOBiKBSQri9hpgd2iG43prrc7o-JXaWtOMQw3PihHM0LiwjIsEZ7JfQ0gmTyogpBFXNVv6Ttc8QMknG9VdBbtT0H68rsVgiHTG2jyfWM6UuY4-9zv4OtF4N2OIq1QHtGz_i-liNQ93rFNbPk-gA0ffYTGTnz0LsPpPXUEZFTm9yrK7CmzmjRI2_2PiH2-zF0DiYL8pKFyseSsNEFVPB9RdDoBR8pL_OoHm8pLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/heVLBybWfFtQ4RvyYop7cgFlA1mOpkGVNJotTYoepKx2lfKHNWR89PqiM8b8nPwow7wBtmzA6sUgbWWJpbsuZ3NJii3IFPxSZHgnAlJ745IV7T6cMUO48l-yBEATNx5GV22csso7WJbjuZ7Acfe4KBXVSIoUPI4nv1QfKkr0J8wXt-awjzdqXgw3tV3qfg5HaJDraFWFGH6qEdDKKD0Ai9caP42AL3TUiP2m0O2X8jO1HozERMWj8Ylw6NiyT9UokbNZYrMor7eJfJ58HRSSXnVp9ESoGQ-0xkR-BY8i_Bsn9ZXuoAg73Vm1lEpwmV0oEOGVBrj0qYYSUMRDjXnjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nBa5xtGn3cbEHoOTWk2liHfx72zLfIjqW-yDYATGEMnQ60DQwe3sugIPI5GSB4Z-oGitRRQh1mvHAkWLUlEQdeIwb9_l-cnnvH3ufn20VN55vKVx5beyMldK0O1OLTd29l4FbbJRN_Zyz8WMSXya_Q2Px_iqDHcZlerO0PNKpr9O_aXtWEqaDJjymgWwjNxw8_cIwTAS_EJaCfdjmHEXF4nE2hJ3dAtKpWuCT-e_IgTFpSL_OaN_wU_okXz-JDXNCfRDPXEcoQ-gu3zpmHp5Le05qAUJN7ehIBmNXIvO3iXXg-J6Ymc9w2tLWOqqEVjaGc02JkK7vxHZBi43Kv2DLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XJGMPGK_qWQNtLEstK9Fk1xfOprcOIOvqXZ94Ob4BqDYhMo8k-t_PZjrPxEI1En6YAuqpZu7Fv1puZWjs5D7mpSAewqyERC0Awz7BS39LHKMqjVzTDPIRIqXwfqhfjv72Fjtl-1QREwtmxK9l0CzfSa5vwzXfQOO3pcigffYotccRSKT4pCEiLMQe_k-e_C4xeGi2E5Qzn0FsDaSvMI--h6-U2PeISkIG16wkmxUhB-YAkWojbPZP3HWr4CG_6KprruI58sikrU5OXNbdrLVOKoxM2I8SWqgDjy08Tqv_WdzvVylUonzzKkquqPIbtcAHnJwh9jRteitKPtqiw5DVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOvDwOX5_hnEg_-iGLMGr6SHtX6CjC0zZbfwGjOtpI9Cqv08JOKEYs_hFhJVVPg5sBz61ppUpifPPFVc53IF3UMqcPmsijmW0ijLvsUcEdbHdql9SCmM-cG4ESXzAK57OI9UGkV15mruMLcYqp0sH2oxUqShSmWXFkKa9MQY2HcJdYYWS91BKJBNfoqmbEM3vLTbViojfWSXelwaZtx_AeaFXwmhlaSgJW9a2Ag_8i57Af8lWmJ4IIKQJAjIynHS8z-jGWdXuIUS9Jp0C6O5AqJI18H6p4PvJ-C2-Ln3TzcfAJY0KBXJq86-18_J_MUK_k5wxfZ1qKxhdSE3uTeEAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JyfvifOaByaA9RODYqHGTNEwVprFByFFMQhuwaP9omhJmmadLggp3vIyV3V0HNtSm_8mVo5GrIeBOj6co2e9xzuItSOxYhPvIjG1exZlZjb4TmrusUa44grDxmbFfRutRYB-sPJcoAoLn9iQRp3CIsGmhqvEUjBSMUlbeH5aPd7KYDfy5YNc-OevV35BBDvruGTNRt45O8osJdBykIYsHGPxTdyeR9j5G4dwdByUv9TmEN5qJcAVOSFoT1QJcTnWX0-M3a62BNDc9pUbIs68g8l01PB9qPGUT43u9bHao6j0tto1ivMDFeX3KIVEdgHoRWnFb6VHUXziPLm64TSnLw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=q00Nj4NyJElrooKkDTHV1EOR10fBz-rNQ1y3n0-0E6W-diouBvzdrb1Nkv6Cq4fVtL9k3teB1EcNJ7St1rMfeOyLf3cjYdY9MUpeCcLNHA_H1-mU7aHqYZwkQoqCRk3lHyyrXDmpyrECgYdvhh-bKxOcG9SbcEg9JA1q7rH84ajFo-8bagbVz5mBlQZEn4zx46kD7S7UIbqiqf40fDgpUsBT8j2UNQSjDrAiYz6vQ1IbZGUcjzOB4-ofw1tE6_qU_6NFQIaw-s5lC7ywreXiWx5ma_y5QY-XC-JdJq-MDyocW-BY2dtD-9IJiLoFkYov5sTW_AkTEiD4QifPdqMltG4G5kkf_gEnhCwzivlf5zmCbdSyi_3e-7tctFm54NDG5KAKz1lUnnSMPqleTILv_pdxg6t1_TpyBHl6uUlDkpASXDUMbrKTeaXov568XZAkIsqNz4fi8eqNv-m9Rxt4wmjg7SPZGiSU9hCI1ljrSQB2y2m0a_8oqSWB6L4qE2udFQCaZCD9F98RNzc-5v2fI6Q3Xih3b8IntJpU9uyhAsBBprMjkHTYX3URIhYhleqf-4ZHm26OfZCwcMomK21E22xjqvfk8gpQWmSxYn4EjDmR3YASZm__XifHVyCfIO7rYe-rpkZPj1e_N7MJeH9HRVd5FhSwqTPWoTsWraLV0s4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=q00Nj4NyJElrooKkDTHV1EOR10fBz-rNQ1y3n0-0E6W-diouBvzdrb1Nkv6Cq4fVtL9k3teB1EcNJ7St1rMfeOyLf3cjYdY9MUpeCcLNHA_H1-mU7aHqYZwkQoqCRk3lHyyrXDmpyrECgYdvhh-bKxOcG9SbcEg9JA1q7rH84ajFo-8bagbVz5mBlQZEn4zx46kD7S7UIbqiqf40fDgpUsBT8j2UNQSjDrAiYz6vQ1IbZGUcjzOB4-ofw1tE6_qU_6NFQIaw-s5lC7ywreXiWx5ma_y5QY-XC-JdJq-MDyocW-BY2dtD-9IJiLoFkYov5sTW_AkTEiD4QifPdqMltG4G5kkf_gEnhCwzivlf5zmCbdSyi_3e-7tctFm54NDG5KAKz1lUnnSMPqleTILv_pdxg6t1_TpyBHl6uUlDkpASXDUMbrKTeaXov568XZAkIsqNz4fi8eqNv-m9Rxt4wmjg7SPZGiSU9hCI1ljrSQB2y2m0a_8oqSWB6L4qE2udFQCaZCD9F98RNzc-5v2fI6Q3Xih3b8IntJpU9uyhAsBBprMjkHTYX3URIhYhleqf-4ZHm26OfZCwcMomK21E22xjqvfk8gpQWmSxYn4EjDmR3YASZm__XifHVyCfIO7rYe-rpkZPj1e_N7MJeH9HRVd5FhSwqTPWoTsWraLV0s4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bpZOrpLJyOXzuhMTll6t4w4yzeZAup42IdTL5Y9sDMq76YPVZqwlFcB43J1lH95r9KKsENdZWBREDp13CiiUS6XPFceSwgs0N-o4IjL3fPL6suhD6ivM3XH5mdeMs4NM2_LIieDnPmEaxHHS2xxkflLJPyeGEaisRH8mcsVX_mdRHWmHLEesjm66G_2rKOM_3O0fAmJE57oHmzooLKQpQ3IS0P-2tQGsdm9u_KqXxlnaiEsa97UsT3K9uHV7D_93NbnRRf7_D8i5IkbElc7Lgp9f61lzxajQXWCIYurZttjeuC89AGNSbH1P6M6z95if3mcDYOh2RuEGlgaeVR035Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NFyHn5vOnOALgYIQzYMqV4Know7XtCGP0KTfFgGZSum-VEyOVhsEaQdAyP_UhZveXzo1mD6X627_DDE4uGhfq3vhx1VJwS9Uf8F9A5ltN519j6yV4OmwWdySZR9obbnuVrsIOj9AYgiNvxFFvMhTPNeYsyOzBUK4xn8rIp5fWkLXEIy3tsc9bwM4GPGA4AK42Av7OeZwJ11bNnrnPcZ7mBAYjWpk1MUng_kJ1LwoK7sdreJyVcCCNQoz7g0htunxMviRcDzPq9wch3iRCI51FyGdJq-l44ANDlkZc-9_xQ69ey9mL5qfv7FXjb51Zs7-5RwQ-xp4mn8vLgSYJYl-pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HOK2IF06yqeqOSIhz6Ax4hCq1d0d0piNwZPuHmrYhw9QgBef3XSafgKK4RhJIOLf5V5uDoshfuTpLdL-ZL8z2iBhH_3G3xngEj0VU50NcryjXiUoWizBC8LHInMPLPcQhFZj9kIbrNqYjg1T79GSkuGGpJUGS6ymXeadNb8-tXij8z2NpdWVwkLtXCl4cX-sWeBfaL6PlvzZzGe67SjN6y3LQP15pLr_00jy-oUmb4gJ-V3B2_50R4zlcsbUkHEAtw4gC1TStIgwTdmo_gYkFyB0nIAJs2C8KP8n-WvzBIqfBTIIzqjEaop3ExbS00J5ClvxkMwyc9kWXqYFkNuwxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LtYZ4p16n28yb1q41yKrEWQwC_o5ZTOD3HltX_u72ibr9hucUcjDpcsfZhg6KBtIyaCqwf5j4uiAyhjQpCgqV8Iaaj-mY9uZDtZn2O_EcePHG1jeSLo65sZWGr-PRHqcdfa7AKfJFt-IisBIkq94Jc4u6qdbDYrHdweqspbPPrKdQneipg4xj4B8EfjcCKjPsxU17I5ipagg13YAyhY5F5y8b8Yn6UHKEMVgtva6if9HRUI_Ki_ZDr7qpB10A6v0MA7T8FS04Z_EEAAyLCdox_jKaEK1-4BHJc9nquKQ2-dn0Pk8VfIvppm6ljuI3ClRhhWRO83fg9iTyEVa2XXTLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPAG7IJ5HpMurYzT5W8b4zGelvyn0xI7VHIZ1gLERg5e3Dzrjlk2gWLBi86QBiz9LvaWRG9KH5dRU8IwrlweQNZ55Fkd4gZD54Iaq9fmAlyfoICMjTkmV8pfNkGZuCwvZMpG1H6W_5FYD0RIgbCDv-8jVARyM-9AkOQRxxjk9UJZXtcExb4whjUP_-f5puh0-HDhv5l4Xok35z7jslxA9RIwOo4yjIVFLjseb0eSXyvKefb78SVc1D0MmjhI0UPu08aokHGUTdI6hHm7c_m11QhJ9oLXmc_OImLbtPy1J6XA5rtH8QSTNGBnSSKUjtsV-WVz6SC6xmD5zMiAvF3_KA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZVQbuxcvNLe_nZZEQpGLqRNaunsLgCbCTknDKKql0fiONMIfdSWd9rY-V2ZyLjgc5W4huno5m97b3fq1o-XzVin7tzsIf_eJb0cI3ANGjFFMsMRA0uhmcc2xd643T9_afHu4QMZH81BkfF38xFjU6G9p4Q4YpNRkBNwFOSup4ZuaHJAP5-JgRKf2hdGJ9D_sia-adROzxRyxGtxp-FKqpa7AsEpqVKQfgkQ3zlGrtI71dpO8PDwA8WxhVvgAORqtfa_bfm_rIcRZMS-grMVGDscXr5eFAAsyqLTRl1970QO7GpYDaPEpkZq9ozmRpJrfLNUFv_SMfn-0lGVMZ1tGjY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZVQbuxcvNLe_nZZEQpGLqRNaunsLgCbCTknDKKql0fiONMIfdSWd9rY-V2ZyLjgc5W4huno5m97b3fq1o-XzVin7tzsIf_eJb0cI3ANGjFFMsMRA0uhmcc2xd643T9_afHu4QMZH81BkfF38xFjU6G9p4Q4YpNRkBNwFOSup4ZuaHJAP5-JgRKf2hdGJ9D_sia-adROzxRyxGtxp-FKqpa7AsEpqVKQfgkQ3zlGrtI71dpO8PDwA8WxhVvgAORqtfa_bfm_rIcRZMS-grMVGDscXr5eFAAsyqLTRl1970QO7GpYDaPEpkZq9ozmRpJrfLNUFv_SMfn-0lGVMZ1tGjY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDZ9okoYfZB4mqBw8KxDgwKUqtMSjh10foInMKjOKH1-60xLLWXkvmChWdC-kvVAJ7rrTiJZZ0CWeLIxxwr0UYFCWTv0rnBSjb1TmPaORV8PNR9xjiqZn4NT8NNed9fJcXwOhD4ulzsR2vIWgUYHl6kbnzO7bTEYbhOLNR2vKhGe9Al5Fcbyu61rCnaklUKUP8StJIkL2KEiewJCcME6SizQCvf7cjk8GzqBdSHjACsWBRStcE-4RhP9mH045ELyn6tTlaLdEKckb9lki3IN8wqLDtZsDJYiW5pFNScM0qIWFC7A7WjPK9-d3GKWFo-dHD-cD7tpV00V9PyQdENQVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtFc0_ksQOrz3Wpa8EhAoei2roCrYr-Qy4bNEm0vj6iovSIXjVlUhp6b8o3V6jvk5SBLIMNq1tePR3UAWeHD6RXqi72x6cgdyIBNfet2nRrk2TTsaC88UyAw79CXX2rFWLzUvq9hpo03CcdK63tpcd1oKMaDYplZziZ2ajNoEXDYi2hTnNlpBQF3AQVlhXI22lhfA_BgtfdAS7ko4bQS_qiohgY4m9R8LLuFPLx3ysuqyirZg3sMxydT1pm1Nqt-9lVAu4F8FYttXohIj4tLNCOFV2AfA_LQ4sOpg0p9a-UXBjIULjeZMdQr_6GrJYHCxcf9JFGSKI8bnLe9vsXMqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n96fOrimfZ2cxqVsNKA-7UuhCMArR1ERkeNVS7M3rOEt2bA_0wHwluoIKcdGNX6_bmdPz02IC9XphxhQULLnx9XbWC2w4CaI5itek5l49MEsDVpAAULEJ5fcZ9swBp0zu7yCStdhGuSdXgtfH9kUBhh6hi2_e0ixZVnUHsg_o2az1qK-ewxh1Yt5caN3H3qD2wtyJF9dVeU82Q1PrAUIAAln9gU9W8iUwUao8PcWxOTFdPEab56fiecXRazUebDdda81gvteLvoVQHvxbTKwiaeJ-WzlCMe2ISgRLRmk-A0kQyK7s0f0ne4PQV7OoZddheT9gR3HV7hWFn7tJQmD0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3OuvQ8tGjMQyMUFkgrhyMvyyPmsuDpmwzYvU6zvm9LZPUWxXAdJPNWZNTW-ARrS-YhovgSA0PjoLrEBAJ53Yx-pKgi3Rs8JlKXvFfB3Iif3J1y0GlTcNC9z6Lg6ZLAUBq1V9SYhG3JAdYhXSUYdChOnsXX9PeiLxlRCU83D4IsK_qcvyWxwenhQhP4EKHtc4ysWeYgj5q00mDZFNxEXlyEPzktHEdcilFdVXtPs-4F7iZY1ECf82xxB73cAVJ0qshc_5p8N7BWNxg-qwH3kG1QiEnvB_287gUvnYrK7VCUPGLtSHCJqxH47s1ALLXq0C1J9H4AZO3tJFIu5edyaDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGkxZ7Dj-4XXV9G1upBa9Nx7gRi1utLqSZXkFZTukJf7sqcma4d4q--Z-U_Y-_dPKfNKKisUhGzmM9IwthPpcn0GSHDizgxnaJeny5NVsB69rgLLHAhQMryGoZ_ZPMRIT9CeBVpMtMVeOAhEXCvuJ3YX1VO883_RL6uhjHTIt768jDhf_1Do13k6VmnVRrE2EeydsyXzxyzN_XtgSCY_InW91V3iNNxOt6-LOcLwUHad9gUc0pl9ABYS3FIvmO1BVa8rDZCST4APvnWGGTRoKidlUz24d7wKJgUm0Nu5QVFFQch2RoZhl-SXumsy0mF2XJ1sPur47vG66EOb7mfZOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnL8psEeWCbAGOoyLmH1QivDHCmXqkv_igyHvKGo9MAftwSsUWqhbaJ0jLnrSUmcL-ifRblFtRlaxzYmK99T563F5AEp0u-AuJBQc9TKFklktGt-DYEd-VsSzRnklUXNaOEZDMLi16JuSy_SL8DM1VSzKKXqUbMal9pfHSufPQW8ntWXxHJnGQvK5Vn7Nmll-KRYpDerz5fpOp_6HQNy2dpLuen4HVyW6dxBr5yT5gVM9YKU5ssD8TK3vVICW9Z8Nyy0agJ52pK0JrpWGF3wNeIozSzHRJ-1HjP1GiSJgo-5MW036AztlyIA1jGSq_Mwguq7N1ZGLaF5P8iyI75pDA.jpg" alt="photo" loading="lazy"/></div>
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
