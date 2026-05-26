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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 07:01:12</div>
<hr>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 247 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzVLZY6wYMEXxPonk26ZgJ12jtA380Uw7gtOO0jPvI0fC64XMZuLCI0YAs0f-OdRprHJMfdjxAFSVarpJ0uHACZYa3wOW00JutbuRvAryTCJvbdCmZU4meeQz2lRz_HPcN0-9Hp7uxaBZpzYgrd0ECnc6t6fjsOY9hKN9goYTMGBCATEkBaassyr6OQWgkVxqGyqtVjgGMswpqGS_6RYlrOvDi8kl-8kEkZb4dwZku8XzL4Sc5_Znr_-NvsmSuwp8R9yj2YEeFFUnjLobZvtq60ZSFcJXK3-enzn1G2MOabvfBB4zYhD5sCWNkFLlw6xFcfO3wT2mNgWrZ1CO5Q5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 306 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 681 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9dqqaZHU8izxM5zbW-crZYedCaCr4H8KUHXThZYGBPbCjjj8OH5p94jBM1CDDMwHfZcbl0zSB2ZrNyFda3Aswy3ni4mgZyWht-5aaRY3mwkH_Yh5I7O8mW0x9U8dL6eyAQW7bwTEYJGYs6arzrlqw_rjmm7D_ZDgciQZ3a1tMs8Yi33XKnHSFfHNmGX3TtfitZAIqGprlLs-rY3NkfcxSB5pYv0O1iSlrI_wYPnCi2b4tksmqvhF91ITMo44PrfFGOWo_YoL-Uy4sDKXHxQIoRhBzo75CWqccnqPIzSgCP9RW1QxpoFNIw_AqOkHCLVU-iGQg-CQVLBdntbEv21og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 637 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 755 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eA9_Z-znUMo6rTwgVcQ0WaBy292ZVPP1gBMzWpsqKtT4Qg9jrjKUIX1nRpT-Qyw5-QErW0t5s5CbMCvwy4A5jiScu8DEc-eCtQ_PR98k8lorfXEvmwTNHo8m3m-bKDphqTYTUtNgRDssykNnTOs85Xxb_XI_gw3WvAG3bsWY6c6huRnqQOwLqqAUxl67mNLnjIvB_GL6dZeZ4fo1KRor3iX7hdJl09n-L4n90zcMXdUmNd_xXKOs659ZnSieLzKP2k7Jq4OXDfbTJMxfGXIS1JPaBWK0yeWUH4O9g_cohY9WNnc7MuAsb-s788U9UMr9eeRsFs0XM4xxYiWlD6IWoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNl0H07k-xDmEHMsNisnUOQe3mVPcvJExT-uwz0HCDbx7frrAi48rhvJTy89ggzl2SOIxQ-T7PekYwEx1DP8XaMOdPxFIFDjzt7GdP8kh1Eppv5Hx5Eol4Up-lmULYeqmT3yu2L0z421aPkHEesWj5weUchQV1hhHAkvXRuC1LaN03gfC4QJ2BP7Q0hl2dhW7RpOJbYhVxbtIxnsi2BN80GxjrIDx5e9H5d9b04eVjVWlocE9lySTWGBQZ0TtB0FFFACxZ0VJ6vyY8fWIT7bJCkRoKboqDMmv5w1d7EhKdVaQi9EadAmDB2u5gbFj3JeuYm-PbObamKuzbj-nRO-4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjn7pBGSNvTZjzYS4KcdpWjzp2Rkg1toHBgDQFCqCupd1p_pkPVrFBF6Pv6ON_uFiS5qEqxRI1Rw9zFOQm4iBm2inl7W-YWVOcONJHPPQJfhQI1c-5kDzjX0v8s5oTi3bQVIeRjG4a56RdGprEe1PT_vliPyZT129Rd_7wtt6ZmqP9zBAZJAcLAZIdjyuqN63bsKHuvSM5grdt9gOriDTOnzY3KjfEx1cHR9lnKsD_b-JAs__6O__R6ijXoZInXACg7PGbljvB8ABzqGYSYTsmi3AgormPVy99GoEKBAMSm4kCqJ1QLarzw1dAcKIm6FcG5ytC6s1iXfMB0XpugH-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hz3I2JzhIMsXLSM34JrRgrKyF2xo9mW0i1Hz4DRH8VijhPD00hiXHoARpJQsKzYvvMU7MsQeiUjaTMIiZCCZmT0SXDL-EKfMV8-_17Ds3ixTpQRxavwVU3g9fEVDeN1AdAx_x1uSOI203lceqG0O3QBWvOga_qvTprnOpkuY388hnxZ9p26H7xARmeQLxptGGD8epqrct5ZinAwpODK0vujtTY0QECFd0qGAdTIPRzYCfDIRvacCpBN_KGSzVc-XRJOc0DDXbDMOcP40OdaXi03068aw7JrJuEcuMkTfjDu51oeP17SWlc19quuGOJEt7YR8k6Le9y2r07l93FVD_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HDGFDU9pD4RYuxanp-Mwqj-l--3UkIqDiJETb2RMum1y2k_RG7dpXNw4TlPJQgv2O8iD-kV5aG9w45CV0Q_5yH99cUB6VVR_0kafJclf6SYqSRAEcUT7A-Bp77ymgdKBVxNePD4P4fK7xsJcPajWDUdvxihpNFTQSQWL8cP9vSa3yI-eccUrIUFBSqr5Ai2Z3TxaZG0KqQxDzQD9UjNz96tT9hH7xmG0DsaOhlRQSdCYj2pHQNJgZL4a5Y6dcEPuJ2J0zyd8eLFb4vy3FdAzAe8AiyoA5aq4rkez7CroJC1jMjJ8WNJ-OZkg-tvV686juRxfeNgKn5-YwImvKF6UGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0uJmKKZAr8tLrRJw1H17VzIVPql6kWasHTMpCO0QrcYCGe8jzZnqz8T2Cyz6zWDkaCmtMSp290IwCZjbFpvRhW5jQiPy7QASgcbpzcil28LNNmrzIqLr9IK6RbCRqZ1Tzq2HVQV4dbKzRNU9nLBHMLNx6GXzJY303zGtKTpKQ0bVFTLfE1xX2urhZMfRGey7bcumwTlcSZFuWvJDlfSkeDUy5rgvRZo6YeHmln-UFoXsny726Yl7xzThOHIqolMN5Z1fritF3j13TVP5gvPzyEibH59qip55PQ3XbnDQfSy2Bcn63Sp73NeMt_cVFy6Ps9QdVUR_FOoQvIgLY6q0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPJPdI7QC2dp1_Pjy3_cYPPrOGeP1LIOJIXfqLBzqOXQq3nPOp0jsFaLg3EaRjx2OScb4D44uSJu0nPBcFQKPFhEJly7CQ5EIaNFoxGM722N6uy1wycyR684MDsZyqzrk2xNlKVAR_NM9li06N4xpUZoIi49Dg5SPCyRJf1PFXFfPucmG9ZTql2746t0en_PNq4wCUnCUi_Tbt_Vz6wsoiWeFgOK0uYy9Qy7kfcgFlGmDiAzRgHixPqIojaGhYp6Il1Wlm8A0q6-_4HIY_HIuqF5ANZxQhiE7T2or-wj4ckiSm-rAwZznm4fNvQOrQrsZ7s8kAHZPDkuJN1jzMzdtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adTelbiI4iTs0R99zN5mNYrTb_KPUBvJT5HZy-2xN2ubO1fEk7na-fgr81xMxNBdCqty7yExNRAkr1IdH1sB2a0Hc_YFY0auxUVt4FHHkdrLhdG7S1WUMN8g8IGjsLtgxh7wnCAh8RVZ914kCYybWyNlMudcRAEikI0pFzu-3wnamIO3hHXT5u18o4ap3BrUq1fmRD8rHc5vccMpprxOspYdFgTiJnp5SbBsVyEyDEbWpVETswsZ0I-7Y7vM0FI3b3mvCKAiFmiRCuHpQpB-W57877kc4S7Y2qltdNy1Kwclnx-C-jpzcICqLrKOkYCkTWWS43jN2UOVt5ybYlXKZg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=JU5M-D88Yy-jsl4idmQoG_wDoHwtclDtRmnHDKX1xUmcQCcsyb5MbjDS9QqGxozWejL5RZg2jDiyIo45HuZCLp1CpGsdnHSGYMLfqiLS-fGQ85gNpbEzc__fbOzxq4fzR_Sjf0Y0QuBqK6tyjckp6ggcr83kiiqfslpAmh6f1xLEFXr3tNiIv9-ZMF2Jf70OghfKULSyNnyElcy40eTNMdgE_xyrfvKmf5ORBjHOlIs8gBSzEFMLa4hr8sLRHVtSq1X87BvhYQSAAw1_z3lxTDplwi_GdcifHkJitdXOth_vZAinmq8NfKhLmrAeq7eNmCkvFXs2jRIekAM-hKWtSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=JU5M-D88Yy-jsl4idmQoG_wDoHwtclDtRmnHDKX1xUmcQCcsyb5MbjDS9QqGxozWejL5RZg2jDiyIo45HuZCLp1CpGsdnHSGYMLfqiLS-fGQ85gNpbEzc__fbOzxq4fzR_Sjf0Y0QuBqK6tyjckp6ggcr83kiiqfslpAmh6f1xLEFXr3tNiIv9-ZMF2Jf70OghfKULSyNnyElcy40eTNMdgE_xyrfvKmf5ORBjHOlIs8gBSzEFMLa4hr8sLRHVtSq1X87BvhYQSAAw1_z3lxTDplwi_GdcifHkJitdXOth_vZAinmq8NfKhLmrAeq7eNmCkvFXs2jRIekAM-hKWtSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YH9lto3V-c_8oeTHwt_vYVQYzh3qyzv8_JdDRHTPmhUnftwXy_utrtEVT1VUsfQKNbjUvZD1DbEpirQz_JEtn55PbzXdqvb7bmRn6ka1WBw3AEUv9YGndfxl9rUoK2cFoJkFuso8lynLnC5tQ8QXdMUaLjkr-GKyZ1zc637L5wvPXBuxe8D7T43pKHPi3bnZr5M4eWz3xB-eOaEG7l92EtmMPwcDqO4JgpBkee5ta3XUxiX8SbcRT8QoAEUZH3BTX7O0akDG_eHksTqOvbh_VF4uaEAHU3z1NUS8ki_ou_drwqpp7zC_BJQJBZijT9fNhvASoPbmSVPcGJ3LACfl5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfWGn6x5mJ1azvdf_po5DDTq4ONEP_fk205qHuDbPxlkVOgPq_RnNG4fuIYxjwunl86cE7qO7EES9mzAAheSNUkEp4sl2KmqlrCtHfFMEWjNJCDz4c5aanQgR4j7MmfqrApIboZTNhWVHArX3c9-SJXXA9KGcS4rMOdyZgB6-sMC3_iAOQ0uNEwMu6xpeD2_O_GmSg7xiV0BgS9htqTPwk-pa9ea2A2tX3-oWi1Ctcyr5ApNjR7FrtUZ9gVTpytu1SMrh4P82GgRlm_GENUBF7BKnRKQbKodlTaJvTJRGMMl11YuwUcn7wq0tuw-OlBL4MKrOZ5dxuBp3hsvaDIbHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tlqzCVngZ_Ik2-bVhCFcjnMCUAVIuUYWcPveIWoPCtT5sFmwT_K6GWYRTTV-nGNuljE41vHDqwWhIzYPtB86gfFX4TP1fouQ2dWSUFmxSXqt7WBa9oPAm6ixgoseO7dYPE_HXeseDbvTPZL8cuaI5-2a7fJQWcjG6R0yO6G2QEpZ6PO9mCDsQMuDT3Vokb6AJqK1JWeJZ7MKKszf-UxBkHX2HOj4NrokuRWFKi6Z0Nlkz_Fzq05a3Zrq14VoUO9xcyNOO-KpivoaecqKEyT83rbMUgydvwXBTgQw4F7idyI1EroVonG-hJEi32GLMUqKRGOsCjfE7m0Y460oYY6SOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Af4KuoQx_MpO-XwvovJibWYJDM60G8vL9J_fc8cN0mPSLETjthUtjis2Ym9XrEE-3-gozvUUF-YJvfBhIkFZYLtNzhOZYd1YUAxk4rO0ioIeYLXapkHebMtJinuMGF9I9rlC-x1iJAjyRlI-7Cbw-JDheekEV28e6DN3ekR6RfzikhYVym7JS_NiDD7c4xUSf59axzc2DdYB1ODXHEWNd5VARneVBSxDiNnp0ttRs2g9n0jB2tIg5HLEDPPHTvaxbd-uLYVv72MGVT817mMd24Zo9QQ67JOF5hKz4NhN-T1K3zX6eA8HhlV9OtyzJmuqnKUejNXjzsEhemtqrj0Skw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWMtFkinLAM637Z0Lh0YWH7_2Ixh3gZ0qHJqR2BAC3S2o0LFs1sCpH2EOT8oSK18xZLzM9mVEqOv4ahP5n3ED1W49YVawCF29IoB5rwmQEdM_y7KJ2cLZv6b_x5jCl9KMyLAw5JtJt_cZMbrl1V77ef5eCSOh9zI2y47lWh52KjNs-sxg6ul4gcxLRBVNgTTxwoP-6jrwaiJ05Ns-OMM_CJGfNdlZGfFaD1yGryEo34atAdSyBo8xBrQiQcIHNkdEySfZbeY96bUYqLxr0I4RpmXWvXAznnV4i0uugIxoz_9SE22fnUw32us77hny80fuDhdc929RBEe1NwKjunPqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6rQfB07hb_b3jMTJyRDAGROVyF2akozzthWb7lvE4UXrRvUuBSCLkPgN9Tt-SgxiEpstjqXXjMQRQnMu4s6a131UBZvRrIo811qJgHm48gD3YSO4baULsoNS-6meFRKV_uL75tO18PAUx3cCzyE-P5Ielz7004N9qyMGLhFeq5MdDNN_nMTCjw1vE5Cy6I8q2N-sabqN1NaXD-SOudO9h9M_Y9VIKXVczMvzrE5vqB5-u7ZFCh867cx4Z1a7rl1C1EV-maL6_Zeg84tiijaAaSBY9_ni1h-vW0HNB3mTDAGMHsAwNzDYxpzAxnNMR7KR7hCXO1crqYI_nxN4r6bCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mqk8Q92ou_zdMohDfmZT_Lfi-4pCIcgFmpgbu-KWUN4Yum4Oe0sfl8aHea8qb6VED2TI3tISLKfBlx9LyD9Z7UyW5X3FGTclt-_Wig87rvWbU_tgzuR-BvioS9HTOip7FTMKFKEn2O3-60FbX0OxSG6AGY1YwnBZDemuYitcuwgPlzSsIdwGlOj1T1XfIR-Knlc9fc3aauTkqw-qBIN_nKTZixJ4bWg9TSEmvpTL1cLEs8vuBCmzzI68XjDVBEL_oJ7LaoKbGI_W_OyTvaJl_Z5ba9oxmsvXDM0L_hmwSpQYe4TGlJ1ZMgkQWWh4R6p_kiyyQaE9jV8kKvYGWzjuJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L7Ma78gCccsKzEoq92h9TcZdrAcQmwkjGHCxlHQs1ZGy2yXcJawCiXMa6e7m9cGoSb1dg74aot3liyigadxYv51fip53dL9obpF9zRitdM32MhvqV4z47pKNAlQx2d9iWvMAswMEn0_w2YLUJ8rVbVBsD5gIGUoSVLnGHWZ-jxdKtPrJzDJQZbJQq2vz5MSLRsakNWX8YYyS4-XGXO63nPEj63N7OgQG_YawpVl9YJXIgH7iHFwSpqnSU1BIWEB71_uT5THHdsy7N0uTllxccpLLdfa8UEuSeI2y7Y0eNsIJEZULkHaufDSfJF8Jh2m_G950JbHEh9r7hcOSlEmDJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 658 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3_U3KqKvwBq9WZGWB2QyhBS8rNbopa_Xp4ubXVsulDerRdESK7xh4ycIUO3rObHTDTERonEE4rVmUoIX5Hd7huNpvvaFEMEM9JOU1uAmExZEDZxTMbXTpeEVDuPor_zP5iClyL86s7fLN_q2ajN4yIMuAQ1eJUGNTW0AKN7uyJcJnxtBs0npHbFfrO7UK2MTqX5Okiggz4LiZifdockGttyzA-P0zGo6RIjZG5EZ0j4s3hTTw3aTrSO28xIf_UyS9iHWxuRQaNG09PqzKAqhatFAMMSK32XFgS-HAVFw7QLV6A8Mpr-kY3bG1cpMAAtR2Ydtke5nRteAWZV9HiV4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtxfKOfEmWfy99A8Gn0BcUGxjU4QldS4QSkk9emc3UgATigFTh8Rfc6a6JUdU3mvAgFNP-VXE1HJaHwOfKo8GJp5zJlW9M0QlOSYPwq6FOPBFLbGxPEvcca5Bp323JufinJff4QuLHYxREnTsbYwxXFPw6c2QOcN3ql1J57ZWfvV-AKJc9WVzBCwm8tklVdPLU8RerftKVtdIBJ6tAb-B6fkpXZO0EERqAXkZ4KYEuvhDlztKBoEWfehRMJSquFJTu0JTNa9iUGGxhppYaWi_7s0hHHWrwa15M_Ooh5LeOOxXgvXcTiyMmYQ09YPAIe7kz3ux3D_yfXCVn74Ju0dSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqmBqrtAWCNzSPuX2FHgdw5Mtm8Zk9RdSUjapYKWiodb87bBOgcLEib0mDHaWsLFKXtwRAP1b4DAFw7q7STRbOnNBF4OtWd0XPyZE5T5SX-tTuc6KjmSLbutIIgIeYg7PZwLpUo1pmbQWTnLLvKmmAsQwCKn4Jq6Tyoo-BXx4rus2qF7OdpwKEDCe9slW5es_CGmHZWNOk8EEg6z-_aDMRFh2Mor7RUx6mT5EYRaQ7qhWViwHP7NjiArz1UyKOGkkRR8hXkIB2IOnwi3c0CLW_67xe8d4sFu2LcGxun28M5z7elDxfsPE-nfqWdREueenAnBJlruElnc1WiIRTN-FQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QGzzTN_rjJ5Hvc4H3MuXXwzdgyGqPbGy8ac3ZAYgSx_AB0V-F8ieanlqYo-QZfotVrIFXQPW9FRJDMIcU4MIMHhhwY7GkrDdtj_ACu8TuSNwzANQcgALYgAJpo3c5dvSSsaXKIInsVE06Q3aUwQCNWd38nX-czkcomAQK6WmDTgRzcbzuUxWwllLtn5PA9cgi5rKADqGbqaovx_gedWNDEu9KNS2PkCcgcGbzZ0rXKbAWYWNGtSL40eEE0Vic7XrQuxIjC5EY4RZMo1eZJtr8BCA7jJOnBWO7ZJ0uHW_8vXHOra6yPW-pJ6L8SLD5kJ7aMtQvZlhxXlxF7PT7KwD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NrKaItL0J2uuOxUklebikc92gwIlCvCLbpxeW4sQjVKoueuUTSDE8p15kaJtd3OQzO9bBkKlk1_xMg4e73VrRlkqsQLLHrSH9QmgsOfk15PPC_A_kOMY6f-MmF6lqPYyTtdpRasqMn9gsCz-4j6x8ETFquU1ekuMjZevC8C28WwJ0BST7Q8vRxly4dkiLVMypk4bfbesmh0P58MVjJmOHp9eaYGEO2wCnyRMvIP4w1BW5kz-GqaiuvpFufG3EuVbsN7KzADgO7ndqAOacapfAZ5jxP4WUoF4L7VE2RvSArHAC1sZlUoLi_Qay0S9iuTizAkvteNTCBaMc4Bn81MzNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6hlx7FhYRqGlz-6gf9Mg-FeWVaWIycDUdsg39Vc9_rr9kWWaiX54udCdAkEOlXgLeySPNKSU9V4_6xqvbC2vBVHJjnrezOpQXORoX6BE2dXASQEWTIvYf846-0krg8q0FNMnRA6G9gfPh2Ngc_6qbjJj7uZbXiVTUfSW1jNouGlkn8QVQ0jnmtW-MLf0On3RajPFW98JVlfUJATNl4D17rESJLeIzd6v5tYtYucVOuwZOOa4lCbZghXWwwNFJxVhJWRmTI2CK-KXsnmPO4FQQjvdNO4EcEnNRMa_Qb9s-p_kjLU2lXClazsM7FfYXhHw-ggkkpF_P7P80HAhKWKRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LFLtPRML_iTjfB8Sd9z_1gCRLy8DUgD4nMAg8xhOF29uV-Em2NlA8_0ldetwGtvfHHwsUykpXbxW-g8IS9cH5s92_XID9wAFss-SWz9nKNsYUm9HKBX6JXDvftbQAHYpXByN7TYGvcdIlKAedOs04hdUWpmrlcDLKdva2YUOyYRww6hYqBOjnhW2eUhf-IwhnhgGCUVpwMfwa1ar29N0BFp7__VCBJ9dpl9i1rVwyzV-ra5L8RC8fu-2pTR3xx5mjQWXVeEESpJlqkN8goDIVppA8MANBr9TWDVywmuBWA-gxvvYnrZTIFc39-kOSYPcFoZ_FWZUmm9qW_kqxjEbyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyvfsbN_B0KMz8eSWxpcZUhFVCSXBP5mHJ8Dh4pFzd-vx60TFEGu5JsUVj3w5SwJJGPYCO9OUTw6er48w88yXGrh6mGp2PUl5w89N01lnZM2OoR4HebaLWx-hqmzfpGi3_ygKUPjTLZOXXx_gYN0YdRQxWEddGmc9Rn3o1nGjR3xQ-wEcs_HYhgf5vIys19y4j5TPxIlY5341Qt1ALFm25OaD_vKdcthrb5eewXc70z-36jgH6A3RgIXJpyh3Et3awI_2f9ZIILF48gDvT3PO1iuBkksSrbdYTm4xzQ7Zx-wOI_oFp6A8xvvvB6-24vZmEV08E5lW9zWBgy7Pc5ZpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCkQCh7E-lD2RvPEpxjJSQKNHWjOk4UefaqKKEPSvMcjnffhYvx5v5-zxfPv_sFneLAYMkqPcRaFDB358nUkK5edBIwq3kzlg2riblSlHoPFzKl1TiufWzZFoXg1Cqjgnvt9QdbSlBeq0RR8fipKaqd3t8dymyQf2UfnCz1K32ukhOyo_5RwlxzpeTmIY9cYTMAPdZPQ6jn8D-VaRgS-jJ5WNRIf1DluU4eJXY_P6Aj-GLKk0I4C3vX5y2NH60usyPoNYbccBuk7Mz95N75euQ8ce5pVQ3cIAwQLl-nrPNjecSwdQ8ICf5NscO1VqHU2B_LeZsepkFsDoKXFpi7N3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yc5j_WkT_eWlhDYVF6JPcJ3-0F_R8n_dK5l8l8zSocBCBr2DLUWo8C6p90Gtnc6Bo2hl20loWQXsuJGUYSZx7Y62ICSOz1gIw6rk7ZhvwleKPIV6YNDii_oK5BguDuI4xBXodCV4-FrUUqiqiXRhVaSywhxVnxt7dwHGmi7-aCabB3o4QhMllZhO0YB0WLpfx0ygWN25bB3JLmykXfHj51YwcuHyVHH_pcGJ50RaoOSelcKQfZvRGBNOnwh99K_V1u7h0PYfnQLuTlVh7YyKy2zI-fs9qs_FqZzv_TP7yGlrSEfez5fryVogoVGfK8kuFbswHdnRlhTrAubVl04I-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3fpVkmSQtJRvqKSeF2IA6AjdZIR6HX1GHznwKapdITZs_EEe-pm_jmfo_apsRn6qaN6xK5c_bp7zAN8ANzUdcPzhWDQ5W2BrNI_wK0WidZ7cUtPUJ9fsI3Mew7dkxUi6X1rzP1LcnEM0CXE_z7QDnOv9yfgb2GokCZ03xmFHakQjBdVASX9SIWoProLR5gnAK1LGwrw83MypRqtGcA9dTpKzoDE6LxJ9cSw03IRcOVhonhmuj7iBsS39L-RAdrrNuBACadHQULs88J7_d4Cjk5fa4ojH_PBgIebZgTtt-PUSYicxvzvG3qerGdQTpUMgPHYuowr6Z_fVx8QYquq1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 709 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDINgNaM2xULaDYroRiWwW-SefYyu2cOMNyT4gHResiodsIn52mVx7Ju78rkFc4oE91q-W3pnMoUNqfhuupXYW-3nkY8roYKFU81fx9l5JlC3TXnxt4Y2qT_QZfN4fH_dLkNiwTB5pS2bDzJnMx2okgG2TXVsKBX8pjQ4LhxidXesKg32ZzvJq_YzIYWYBEltP2QePjLrQqF4Uq8LGeWZjrXaAaNfUYkLRYqOVbdBCBkwMS4cntcud6GhKgraiijvK7GaVbaslqtuTyYxMI79HFbraR0-IZWS1RHt7GbpKORcvmEqhT6xN_nHuWsBSslQe60dPtrn4oNdRcc1Jyl5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 607 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_hL208EZn7PYL1hSRzzl3UASeGK4mzaJrZOUydUkMK6xMqCvS3Exp3XVxNeIA9W-4IPLq1MT72R_tBrxVZWoCUKvBHEk_UrLnxAxch5TSl2H5Ls3SM9JAEKE-hJCnN_YXTd-SWjFBPDoCoLK6hO71JPHOjv8kZbogKH3mGS0jMTk8G_Hs9gV4TMEJsXnNcnjmaDtTWEBCLvQi4tsEdQiWaCGJqjcC5PaCKSYzrjE0oZIJdnrksv1rMamyEtLnFX1aD6zmzaRWzktUhEFTlgTv_UjXVzRf0KS_6R__zuybKsUM-lcGXNz4eR7D8hheF-xT1YKsrQN0WO9kNw7q_mRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZAwnPp45lndocf94AuHgOsKdwV7gFrAPQVeCmrm2c7j8mYLaXttzY_BxJ9N-BRygl3B44qKWkgFY2Tf_skcneqKSkAoT_9e2k_AYpBZ90itUJ5WUS06pvCIPMqDy0TVo7Nxt9Gl_3Q1YXvodt7xEgclj8Rv_NjSvQquBopggSLPSMZsInjnVTkwDoJZ9tCgMtVc5fDpUlWJzedJxMelISnHcoXENtlrny4F3bX1YJogc5Sy98eheENAu3rA71n1YqGoD7uJia82kMW86DVdIKO_e4sa9Ob8TbciuGUBkAwfZXNCylGZawo84L0HKY9Yb8t2zmg_0I14L775WsUSpOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tsI3UuC8GVNiFTS2TIIFVhNrJTB326Por7CkIOZZwBCes7XFFuAelxnojhP6f60eZaAFh2eMHh7qVpzDmznlmSpVx7rR98-V5k7q_EGI5KX-HR6AHOWaMSpUZk1-DCWUvQuM8Bjdh3icAmXGnPFYhRNgzUbG99xD35S0X0L9DXO2qHSL1p0gaPQ-dJd2qFqVW2Fh8Y7ixSVEMw69KHScFv3Tl-MGeqKltXD4DROjFWyw7ECjweCHlr6Pu-QNO18WJJGwszfe2ERBy2a7RXjprwgZjM-kcYvy8XmCQBzfeC7mdBOlkJUBZ_Ek_s6r5ESWDzYbCGUml031XxyTGSP2ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbuE-4OPgBlyoVbD3OjN9srutaFgAZ6FDGvYxhYI6Nl9ankVVfJOJIEl4n8RjiT1aAMnOrSERLY6dLfut3Xm_ppiR_2nb-xm_O23yzIanBG6YGor5YGgIDtxw5MSml2bq9pRIrV5oOLoEN4WJRmsBMqPIJMGedgmhm_S1vhWtajw-QiWpCh1R0PZfJec8Mi5CxnishqkDK2lpZEar7o0IibTdYMqpj3YGXfI4yULKtIp2dNzPgZd0okdGmSEKDD91Z89XSEqD1CL4WtaHKGVsnAZSobfDqMvYrtNqTZWMyYfp9DIM_XuVMWRu4iiDp9XiNwqkk3SJ4nlP3WlMWE28Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtCH5TFEyzK3gEV4yytLvaHw9BwUlzfzlt9HTCvXoVNs-ZOUUuK8bPw0EuEpT3JV-448Z9BSLN0WEHhYO0F1Y-MH35yozuwnCBCm9T6pJkFpKEcRJo0RDeb_xkT_b6xt4vIOa7GvTOzCIg9c_2tkiUu0Ffyxp9J4ZxkrKDuNyS-9ENsEk1so0uTo0ODy5z5C3z0B05i1BvCMdPS3XVKb6kbLcW3SQbUjy1PhxOXPzhHq9meX8R0eYjKELsTqfCKbe3gcD0vf_QjhkSUMBG4VgRlFelSyko_bU810ZFqrvA1msCzJ6i4yuwTV52hQZicz0mTMQsrctnJ7SVKn1Y2-eA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 667 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7KrkyNWABF_ua2Z_Q40NRUKX3hSEJHGhtkxX2bsyXHywvf7zSbu2qcexTNG8yehex77GUHZdBBGo_RCB-ukmXNsnJHxCYUmbyKISeB1VexGvozEJ19nGU-d5EUIPwnKLxjgwNsYGO6UBaZBoaycYSZ30MZhgXOut6lRJff9lE2d-WAHv_eSBJLkM72Ps83CRaNBMilJT5pdHhU2ZxkxE0UqYVJc-f511HksGMLT_agKy3LiwhziLh3S8j1VBoHzahmMOoriSzgGkqyrVCr7iLBPnIuw76GTrKdkjwkJAwvnG15V97xPkwZhQvDVKZV6yKkF0QT-249sbqfLX89FyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dOxjnKS2dyGgR0rWQXCIYLFDBHYj6tBbETZO2-ADoX8VBOQUZwc3KYZre6yZCCrR0XHK1N2TCRCPV3nernBdADkI7HUCpUa_h8gfsO5hCLESSpDna58DR60r6xTJFqRw5ii01NZTbJx_MxkY2EvBIVM8sRjgvBjnndI19KeYDch08-x7qu1NZzwQ3FdSzZCvvCnNbHs5eEqx50BgxLZNezSW5-JktQmtitwp0uQH1TtSNv_vlKWcwxeEFebAUUozbw0h3IYfmaTwopUjdM3hh2Ea2-BW57s6c8TCAHFmgd-mCp2y6ofM9BmBT4Ng4omGh4a2uD4fcGXugUB6DoQv6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XDaYYARlo1QhtpI7gMq8XGjsAyfeGelA8-faIlrJqrGTDucr6T5SGiOucE9MDhgzHiZCFAWYC9XoVU1CJ72hcLm-4bwEKz7km78nBORsPOPDViS08gp781xEQUpAKBcNn7YggWvRZu9aQGx6pbPoK-Xr3dD4tiU46bGeZE6d2Nq3Y-u6QHynjK3lmRtnrOuSbL-wOwk8-OpimNOtsfzDPBAK5m5ds6uZHVQEEbO4oKD-ccIIpCGwQrKaCRxULFV3qarp7dCXm6n4qwtW4rcdbjyvLtZ5NTNMHEgqvSqmT28_NQ3Un1Ap38ZI1F_z9q1SqTVgecyiUakjqv-r0TJ5gA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmHjC3qmvPk52veDDOJ-lMleZ32v_RdOcbBzLqa9ILqF49__VVL9nRCAHhJ3Sne30NCwJUahf9KopsxPFWxZvjmyyPwWw86DKbT5KZBxzbwdpxcsVC7ccXVnRVj75nz4MD_vqAdcghQE64ZAqqJEUS4Tk01MAV0Q45wB9fYScjns6HL9siVWIyKbLEFLJADtrtGHSmzvHPPdipeM05gUVkYtqsfUpeztGmj6DqY_o6UL73YrazokzggP_WFJA1SZfzqYvGG-OjL7zbm-iGTcjtdsdKdDm5ZME6z98t6tp10dijhbS-rp1WUfiHTnwjg_XSH8G8UE9llYVMEqTwdWYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AtiOVoD87ml5FD0ftXfgajbSFh-FAMwBokMznpuNR99PChvAh6aAeFpzPVDJEiFmnpvQfx3c2VEGjH5G5TTFiXnysxhBOf7FNmyBDADnpvl7-VbSgelyKGLn9iQduc9102WEH6IX0pszOzERTIq8ig83bIv_scQIIZ8b9VumXYJ7Ak757on0lMS2qR_UDbKbjTFqvkn0b7CSpIcCv0gltoN_iq00qjOSOgIjMWOVBw09JH1VzP3FxstK9ZoWv_yEbPnHbW3-atmFruTwwXQRMrI8sxY3WPaUPUCXdBvuqLEbAZAkMY8IYLq1WDt-vD1w5bBs4Ql7tnkpArhQSIr8_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlloYHBxrt91UqMz0XT-z6RGK-69mLOuuBbI3hEdeig13VE_EtIp-6vc3yX5wWNGcsjUeIfs-39IjNBklyWXg5reNLmcq3NXjzTJcvpTxpJtF0Oqyb_-gjGfNSyNNF2E_qbbEJhdQgj3O0UDkQmge5JCueTo53Q61L3J6mpyL53oumq6YZyzS_WsfdpOsj4HWHRtmrpmtOIJ8DeZ7bqZi0HLsSWl9EBmUj-3HY6V_lueUH086-xljaK5nEq0w4NW4tQ9Gu4UoUOCIrvZovh7ux6QvAl2Nc-j7PV0wDRb9n1aOD2GuTxSDedB_E2znpNH6O85HEls9RK7dlAZLpd3XA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diKxSejbeh0WedaLFu4H5pVig1VghP7voZQ5pC9vMMj__FG3heTwSXfjM8mRwb1pWy5o18nB4ZcaMzo0uUXwLg7d6ZceVoA7EJJNW2V-DSHY5s3UvjcmMH7xYqsbpj17RTD33uGJvsx0XIeAjo4BqO6-v2bSrD9CHoyEdp-N8eAY5wuaWKvmoQ8afgkf_Xa6qPv_Qmhc4DH6IDHSOUmMu7NmYTAvOp34D__9102hjcrrwjCAwg8uPI7eml9ZTkQQmjR3WAryjvEK8AG1HmbgtTuPCUNg4I5KQg2IpFcwq2zLWnGxmTkUFCZNaU3vBwiwU9owowrYwW_xhgDxPcONjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FRHLrQAt8kKeyeNt92cA6uzUrrAwAElw3JW1coYll8nt9EbYAN9PV5uBIHJKI4hqNgkG3qkHJEoot9tdm5ufrYTzWZxXCuJ24UR3vd7NI5vLCXvHb0x_fBWdHPlt6CQ5sszfcuipvkzzv8Cvdeck0P68izDL51NLX-m_hWzumU6XLRC9FoxE7kPqI60oBDAKNXMDGcDACIma9GkRBEa3ydDWBIITVFTL9tuyGqO19RMt2HLdDMK8hR_IUmlsTq60AtZgStqOGel0iuhCnAtO0Auh2thslPz9-8jpf6ZhrupSfEm2Lz-4sNvqosJ5VPHQrjVhY-NYmMOomj8II_gORg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eric8vLYCAk3H3y7t9uOSsWlcSV9NW-kHn-uKQYVZroQ9q__qvzgJe9qKfQzz1tM0C9tJFBUB7PGhO5mqqpDK2tRtGJnhno2mNHjFxvaXi6sQIY3MMydQPLyF7LwCmcPFCkHnI2FNhi280sv2SbvkxnoQN54PaNsb1TgNt9pri9aPGuTxr_ZnvmB-17U4HIx5ePM-EjiuFT9jmgCsc9vm70T6TgtylqItmLuJDM5jMxXSEcbB5tKuq1SgkbzwDCxO6XR8DgzAOqAb1zk_4qGeJ9nOaThuRvnK-AcuOU5Zhq_fs1_yOnuiqsygRR-DvyHVFToQFGPev1HlfM2002LTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTr16a4BqmMtqj3xEd0kSyL77UmcD9fRkdgHKGPuW1h1EUlWCUz9FdK_jwfospFCF7ObOj9VmLvoAIx3yNjD2GziVUDxILG7-95vKsy5wGgKjI8T3nT228yEW4nRNsEZ8jjvRy7EWHLRDsXJKkANH_nkN9BwRFL28vukNH_43D7gpuznD_tsI5PAOH3XlgGDKgL3ILIEQt0dv5P78cwKzXySJiJx7hTEgQzfQmDUn53T1U-caIpns4XJVNn4sRZRqABh-9gErAs3m0ssPPbAonmM5xe81isJNYG1k-yWryGxYYJzbZG2RH9XG63QXIEmu13M-YoeS9j4EFSiSFzz6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBp0li8JpsbWNHx9xlj51CEo6-IPtTydDNsbL852mc9kWgiUW5uJ7G4BCacqWQ9Q6-zOgoGplpopOqCmNt7AQgE7VeDpQQNHE1Ch7nGZV0vyxqNtqW2izBjvzsqzliau9eGN4T21ObQgqo-UNGR9f-vXH_vbE05grzMa_qzpHLsUzQoOO4xMQCaLL07RVZMdGqfQnYUrhP3rImdsTLWZRC5T3PgLtWln9IKGzMXtbrcvT3FocHJy5U59GhWnQG1mW-4_E8hpK5-QWj-tdFxThG6r8rT3ndrT6-v2oZHyjlfe1ssQq_XdgmChAlyYRtzwysamOJbTBy1hCIE1c246Uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yvk6wV-774TT9HCx6O_J43ieucyhQQlgvR2Ph1CUk3XlVOxDwRCGuvloOvomUW_VftMP1Lf05AyjiM93WxEI_Cmg-Ce9fNqq91eVZn3MMHgzV2sIZO_4f2nDPwTsKlDmjLlFs0B9Ss4Gg0Wk4bpVmgW11bQCRZgynHeUPoqKBvAU4OZqGrpI7IjohyFJqE0EDqqt5XzOwB6kqT9yEgEBMZxTV5b3hMqpC2JnipR5NWSFORv2AyeX_3fS-aXo6xbqYXAO7JwjvkOak74M52eQLIWkbbXfn0rsotqM3qYgaT8j84cuxMK_Ws9FW6XFETPbFt6ITJj8KLB-rz4T-jDgJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HCr1S1RAJcSuUYOJIMvOYNs4df2gB1tXEivzOEbm3MGUqHzCvOZ2agr8V1WsagKuVHX-gBjsd9UFQmnxEVkPmX6XNo-KyXUlFU4tVlN7QiFkokjjjnCHfBj_3Lms960jlAuSExbMZFiJl5l_vmCPSJ6rwVQR3A8SPe4DwIrlH2STu98p5tdpv8Ggv3FVLuDrlM5livK2YBV9S1zCs8VE2hLYLa9nFm7wnX3E2oPcrEvp9bfyzK1N0hjutdpuJvYD6BRdhwI9A2paJXCIrbYyF04nmVcRO2-lEmh93al6hF0M2XOtJTTWzAiiHA-TnuPEWSTwTxaLto5PO5Z1qdVMbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fab7fvvunTfQIICY49vDPgTrAKPNchgFaW3qoaUeXzmVu8j4RirA04U0rq5ru79Xb92uUhzz_inquCAfUBOLse4Kv9cVkR2USVyH9aqiUiXL1kdrx1NKHWustSj8pVkvB3EbsiQolujENt1nru7YXu8LeNOI_stor12TVPOK9cfmbI0SJZV0tD355ntyDNiZspmZDf-By-lYTXalmSRBPdZjsUGcuPKnjE2-dLqJuW6SD5XBxjl32UAh1s3pm932CsmCNBMZRVGU33fpaYE0ShiaYTp-iqL-MXCj35VxPjagAJxcPfTQ1I2yvbluVnzXaz46h-odWSrFK3Xl5Zsomw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQUApgiKReQpfhj8k71XWj2kVAKCUN3qXRvSAtqsKDwhOUzjXtd5oFcGw9QWETkv_8zzio3SoV4SBTrdNYuXuGS1hMyEYyiarr92P2TGlVliZHH999UNfNAkAXY-RcBd-h-r_rS6iMVGcbTfuzZvCWqzc4AiGbCgTTy9Aid40e6XpjTi_qyIuXwR9g2vm5Kf95C-5zbf9wEzXVJlXmO3tHV5aVmRWWjlEcHkYaPPCb_a0E8rTEi4KKYlTDwuE-syAQXNBmO_W1HMyEsJTKy--usTnBoadTsnuncTSOJk995O6VLMY0iad4fx74lLq5iPF3mkRTn3AUIICHPBrMCutg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xx3KpFj5s4zN7c3iflOjQj1jUKpYghERI1MAzkqtC4Z_8HNtN5POeYqWySv0ePNdPqurErucw1LGtv4S_vQlvR9X67kCWHxj3xIB5VWIlats8YSg0-Qu4brHw4YQ_h4q4a9KwdW_qzukqtsdMK1SPUAO595FP2l1SvOXHlRMtRu0x_Lp3LQN6XkKzWkc1ZbjmHYt7neaYjEPTOPLLut9sbwEJRNIyvFcLfmDFIh4UFPiXa731AuOKCiuY05ifmVT6gSpmxT7iRj515kol32z9Pvn4fPnCbiDAsGaTs4UlR8qCxYt5v_-d8wfU0bb93uJ2_WAXEXsN83KgjpBriqb7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BakbgEZ1U8jUH6KIVJvEh8RUxkrJuHp9Oz9eTehqMGUZTg2dQtKMCg-cqlXN3HeovIU7VnJXESalG8WJ72_WrvzMNL2Yc3BsJlijq8ItDCYayaDPUbx0k5B-_tC6C3n7o3oErrkjM7tplDgp4nDRUmQrU5NqIplsVwnZM2XaNIqtvZpCjngyYL5LZrTUCjUmasa1yIGUeHzNR615TpiQKSk9APq7f7wQjjLD_wdVB3dklND4wKf8zAn4Pf5I1D7qIEtCmxT1nde6-fYHZkSckjnA_nUOLBHEMp2IftCx16ru_3FikasiO65f27uzDB697CsxrH5vHYsIA13QB-GgvQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=PICSetbY4xx07wPhuMPPHVT3588FxVwNVaGsE1_V92kVuryQFB1icDMlsHTLfl34Ty4-OLFGmvTL3mIMixIQcnfd2ov78TFhE71ceUaW4ubNv0GGcxek7P1wiES42anzN5hv5GuMEQLheOOd6ihyx3OLIZyQwKakreTB_KJTpMAVT-rKWhXhbHNShps35tl9NhQe12TXfCi4o8lxb9sYTg_rhpcsaWP9SpGYeNu6eAHGGN0LghMZmUQs72JaQQd_HJk-zz_vlLTirOiQwZ1VMIKrpP6Wk9eJBm4lNeyM0JRpB4XGUnFCVFGwdqCVlQCvvmc_4iLulJZTBn6xRRueuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=PICSetbY4xx07wPhuMPPHVT3588FxVwNVaGsE1_V92kVuryQFB1icDMlsHTLfl34Ty4-OLFGmvTL3mIMixIQcnfd2ov78TFhE71ceUaW4ubNv0GGcxek7P1wiES42anzN5hv5GuMEQLheOOd6ihyx3OLIZyQwKakreTB_KJTpMAVT-rKWhXhbHNShps35tl9NhQe12TXfCi4o8lxb9sYTg_rhpcsaWP9SpGYeNu6eAHGGN0LghMZmUQs72JaQQd_HJk-zz_vlLTirOiQwZ1VMIKrpP6Wk9eJBm4lNeyM0JRpB4XGUnFCVFGwdqCVlQCvvmc_4iLulJZTBn6xRRueuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0yXau1u7VoCgPb251sEk93T0uXmKqildmY2_lg3F_40zn8CcB1xN2K8tZ7Pxe_ksDZrPRNCWRiPsjKIW46e9dwbPGg7qkFhFgMnHbV3mnqEqsTO5yeh9PsD707rhytok5iZFo7njbxT9GJIga-hzIHI6v3mRrPcnmn1Oc7BKCHjNEP7bc-BbHr7etFPKkpYN63nHKEu9uCkdq4EQqJ8pB-CqlyizNH6UV6-2_rlSSogueLBC3thwhLBgbW-CqHUUHAiW0eea7e7P2xP2vwFaYQHwh73zDyEpsdAdztNcC_9MtsUrJ2CZ8JEK35tEGXPTpFmAU_mRXE_9Mxopw_wng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxKPgm8oT5TM6PBP5Fc71qaxTICy9cyaM_Pn9QiWPcazNp77IWSGM3hWFsurHmUZzT6rPlOI7LGOlRlYJ7f090dWITCIOn8b9TUDEkB5iYTG4-R8GnKAKtW10n9YDdKISBVv7VMxMR97BOsa7JB1_Bg4b_7O1dda2BZys8SRt797VON7yO5oYKgkdu5vYcvsYBIds4okiRnxOvYwxPxasOHDPkzVRKMWqWJvmPpBIb7aYVpEI7bLbf1Y5WOZhv_faWy6Sy1OOgG3ajyFPpbG7TN8qHQoQGgqFZSgI0RHtd_c-P-_-Yh4aqscgfiL5mRQLfTPKWhHKmpJLMFRW9l4tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m5CXxa8Xh5zyjZUOfMGorJ7OhquoPA05p6HFubf5hI3c2W93ddqYxtc-Osi4_QNr7wWsXP2Utp8i9tHnz31R4_smpuISQ9WuOOrvpWOwD400hwSYwi6t5r6Cy3UZe1E9FEj-0yr-RdMJyHbVi7IZrjjlpGPOQbPS0u8BuQhQngVe5UZ6JSNr1DoqztDKG57PuCiQCu4-3BmAGaFPcpsFpVGiKGY7cs8JfAJExfUofQvT6Lfn3sgkW_3_fHGjwTi2tMHVGHjGqIW6tUmtaU_yCD-Wp1MMjaJfBB4ZagBNI-bT6Z6MVsECULzqTbYY8-7uJbQDFTqoVyx0ZMi3RwwXYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AoCmcoDhSoK-hfCUbOF_gADZ8uc02k8Hk8iwkwH5UgLflrwm67C-g5voBlrO7IdJzdTFlvTLg8kiodlr8Cu4WikX8kwlOCKlR6rMJm7Jy4YzLZFGr6eoJt9CX7alP1rPRDhQQ4bnR9ncmpfnl4unEBUm9iWfeUI5kRLj3c1OHSDLbwyiZPb_1inNPQZm6bJwvl_PLLGop2aT8RwqSXo9HMq1dhZGQciygqRgQAwMtBYWxypCNwThznLULA_cOrcuSybt1luIJ2hq_V4OUhm_yw2J9S6twB7XR50dyFuHCO82XSV7pM91IY-Ib3sQyPTTfcGZyaovq7Z1N4Ls5tAPbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/et5URsHIR_L3YhEeHARXMa2ZCyFtVcPLHZM7MwPrPZNPhQS68xcaO6U2PAy56mGppiFMy6shs6IM5bcv7b9t4X5C-BFpBHFy2QcV5iUHbRRBTzbek9zKP5CVG4LRfy6wdgZV_2sTFEvI1oVtaWX5JZDHDuWVAqK-ePK6zo-DwuO_leDm3WI1rCIQ-fI2YvCIHyu-BA1Inam8bXKk1tXqnj1qQf_3yRQPucl2_zTqecgvElIZ9_d7-now17jhJ0O7aOn1r4yeZ_v4EjV2Z1kJ29SikMlKypx-67UAWMjSS11OWGaUxpBS-uDY4sTq21nKBhdSz_onfnAZ3br6Cr-6_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6M3o4oY6BPyjlRF8X-lq4-2s5pFKvy2s3cUaHkqmLY1Mx3ujvAo65aqzWbrYyK9zFGDzYP4xX18BQhaTLPH7SaoRwyZzy_Vy2NbNRtX6XncpBwaIVmvCqFp0MVHyHlhx8h-wzVZKxFbKpQ3uxQgZSYaz4acBOA0lL_SZQM_FH_xKSTW7mzgU-SvNefVNT98X-v8WZIXyPKL1k5lP24v7a29AbjrgKTMqZFFNAP1oP0g7DvxeHW4tIu1NfGiHpUvkQl_zbI5JGA0ORFlmChuOl8Si-yHXWJR6v7DvxQqI2yzkpS9AzWhlOf6ZaHF435ku8xbq4sfH0Fib0-jkvRCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hYtqUPoUySfIrOrlqft0dAxTbgFomGOQn8TkykqS0rAWau9AKYrPHFr6J5jnuRnv3ue3FpT-QC3LpDOBe1OXWociaBDhMd4IUBnuw5W361e4Mjk8WzT55yIO215zU7L9YK64-HaIQJYrb1CcqQwLie1BCBS_AEA95TushcZ-7xzO9IaFVGQx26rZExZ7p3dNPz_OZGgGTfetEPmlbcOvu49CczzpMSIj1cQYGDIS4c2mg8-OA160LEJvq2LxBMn8C4r2xQfi1GlCDiuWTem6FjuTF50cTjE4EyNNPgf-CQKdUSLjGBzPUxHuE5Oz6zgOEAtqqfxWf84jrDD5SbQcbg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=nIdhFu5W6_L1meNF8i3ytVW4SeJDYVNK68qD7zXLOMjpOHbj9CrezWk2ovVcMdeFJ3ANNJLsQnBUWKVh2hcGYqfH1XtbeWz_o26wR79T6XpTA4ccveKSEiseHrNXdScrz7t44iFLpr4mrs8LENrJxZJeDVbi4FAIjnDjYubb2GfW5Wmel0oqLuUHLpdooX9jj5TDukHFCaMpetz6gTlpliOfTbcfm_G28_ryuzGSlgzBaKdEGTMhIXYcLkfvYI4K86zNcguBUOLWOd90YFjPmjSfdJ4DsAYXl-YYIgaYcHATpwh8OgIpX28u-9k2w6GgNhZ8mdQVUlnG11cHbnN6-A-J15t7QErN2cP5dbcoPy3ZLj0ZCiBZoHoG0leqqZ6tS63GWwvqfUII62SS4uZ3NpvVXzfqhL5LZLYL7iWGDr2zdTk_4cXo65o-Z5nDTYGJFkt84wnqcnga-s4doTkdiZG0WvtR9D8x3NowZ-jo4BoHqFytMhLt0p5arSVuMqQHvS0jdPe2grqeucS_5YtKZxwJVTcEcSwhR3jWlC0eIHnLdN4bsSAU2zxJI_etAGbXN1Ymy3HwHie5Uqq5BIeznhAvRf3G3q6-OaqMEihjGQPITLbgopfI7YAYZv1yAK3-W8YP0V025UME0hUTsfAY5PrkbxDUr-FXyAYmXQh_Y_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=nIdhFu5W6_L1meNF8i3ytVW4SeJDYVNK68qD7zXLOMjpOHbj9CrezWk2ovVcMdeFJ3ANNJLsQnBUWKVh2hcGYqfH1XtbeWz_o26wR79T6XpTA4ccveKSEiseHrNXdScrz7t44iFLpr4mrs8LENrJxZJeDVbi4FAIjnDjYubb2GfW5Wmel0oqLuUHLpdooX9jj5TDukHFCaMpetz6gTlpliOfTbcfm_G28_ryuzGSlgzBaKdEGTMhIXYcLkfvYI4K86zNcguBUOLWOd90YFjPmjSfdJ4DsAYXl-YYIgaYcHATpwh8OgIpX28u-9k2w6GgNhZ8mdQVUlnG11cHbnN6-A-J15t7QErN2cP5dbcoPy3ZLj0ZCiBZoHoG0leqqZ6tS63GWwvqfUII62SS4uZ3NpvVXzfqhL5LZLYL7iWGDr2zdTk_4cXo65o-Z5nDTYGJFkt84wnqcnga-s4doTkdiZG0WvtR9D8x3NowZ-jo4BoHqFytMhLt0p5arSVuMqQHvS0jdPe2grqeucS_5YtKZxwJVTcEcSwhR3jWlC0eIHnLdN4bsSAU2zxJI_etAGbXN1Ymy3HwHie5Uqq5BIeznhAvRf3G3q6-OaqMEihjGQPITLbgopfI7YAYZv1yAK3-W8YP0V025UME0hUTsfAY5PrkbxDUr-FXyAYmXQh_Y_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LeLerQCOMDQeOInp0j1T8g8W9f52H3QY07w8ponDDe6Gkz6IZlEgDhRqaFHSeYw-WL9n9GkxXxqSJZl6BuEdynbvDpfpARobXREYMO8NNf-RJzli6CbUGbyp7IXy2o_WmVAnhbnN2xt0ekf9nZ5AUdVndYIsVAEXLwx8OdXnk8zZgVaPZKG6TRg0x1wriX_F6u_4oKV4Rxley2RRjU1T-orEA7KwQ__D4CAFSM-ikTcr06RFRzVBJol7Fo6MzcxKJXH2wioJbwfqH8y0G-s96LYGCmB7VoMV5vZAIyUI7zyAhKTBowTaJDlyvuKp652hjSahz2RkB1J5rk4b4COwzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/evcux5QBEPk9O7SlHR5ENqFZeQJiGYPBTDUJDc78tIIGZvAsKxV6LxKS4sbWBRmAkr0sNqKa1gVBSiBsG2Klp1GlDoT1ix3EOWA0Lv7268g_POWwehDlRqXllRYb8Anv9DKCOdEXMkTJySOal1yR7pzldrtXizVqN6vSKChf8M70S-ZTqs_p8sF-xyuw2N9z9NdGDsKQTSmgB4QGg-Pciv5dEZV0KEUsxW9Qr_6VOG0ACqR6vY6ujgnD_mt8fIcs74lbejx-w7jA-XjaIHsbOyNy_LfPrckGl4ZaEK2IxYP1J32qpu_fjydfGtvqS9hszOnA2ndCvnS8QuKuWltIhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aypBzlVtndWRJNuBKgvhifDlivv5AZ_KrNz3rHVaWWzk5FwC9FGz38THmfY663Tznx5tFKHyjNVsGd4d02kLx0KF-eDElwziD-VFQGQK3Z_9IuiEAM694S-RhM7cfsE4xTW14mDmpemqBGCYsXSc1aX9IQ3daZB9Zh75pqZRib97MA5H1Im2F9TBYwL-OJXlrJVmn1qKv9k_Tq9XiUqcDjqkh9iay2jZ15LHz482I9m0w0Q8xvSVg2mseFkc3q_0McT2kIucoSkY8BeaRk17YF-eO-r44rhabLHcbsX7cdCn61mc5_TAWomf-4W7pBa3kB8NlNJt2-9WBTgVjmQWFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dPpIKULcV7YPuiNeFYIw-7nRaEV41r4hR_rKPk5aw6VqMLq6R8BNeAHU2HpY8jPzM6JJHvKxPDR05RfLA0m-XNHyTvZlf857qNf-NlypLc34-v-RRo7BBt0k2IRwnm5eEia7s5k8TRqKHDARMZDo0YrPolYy8_mvKAeinUSTdilvSbq0vrUqJNrtmHdXc9pKXV1_LLf2ituFYKvC56v5j0c4SbNY4fJ-RK9DORqvgAvhfUN5MS2ayqDIiliKfxe1lkVjg0VvhCGVO9Cjqrbac1Zz9O0Nzrx4dnXvT7cAdCkqHs-CGzW44flg-XUT-afpjpIKA9fmqhkVcc3p22KyZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOR-Xcq0G7dFS-Pg0jo3dNJrEug5yNXUSbQUyvdrW_kpt8Z5wyqRWnFOfYo-bqFAOK2IDkfPhGfoCQu2OrTHc_LgkgwVN_EEWsAHjXclA0NFtoHk04BZxJ8_aI6db4mIiH8uxXl3xcftk5XGL5nivxkpEA7vJjZuBnro7Jt2jitCq5Caq-Ps6YqbSGPqZPvHsAbQLOa4O8JKviKV03ONCejb1R5VLPxDmVnemcNv3PXMBob37qxCBzhyXKZsjGA8KU-gbVsSo3qUWj1LdlMg2NiLj3Ie8997r0k08SJ8oF5C1SeGcteld_V4FeCXR0dYbtljR2n2dF9DzMiqKBkOOQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0V33Emt9NAoMw-nWt7Hardba0sJgFhgYHmx7moJwDuF1dNeAz3klWWhcH5etq177Fql6qy-f6DqmHivqlnuC4S-gB6UT8hXzUg4TGGERYpZ4dtZHdSE87CwyOwGz7s6GmPO_wgwKZwbTdM16z69mH5fTDTAbMw3Daj-3_JsLEoDik1SrBWZaKLj3R-Z9ZzicxnnxzL36l1eJJs1GC359jeRkQg_CVBshGOBRoyBEXy4IBbCcDxdedM6DHSh93Vv6-uzH4aDZenKIPkI5NiXDsuDoNCH5lUCCkL8e05iSSmC63ieZ2ubOYoI3VLuhlO1ZUzJfspdZRE-OL3k23Khh8Jo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0V33Emt9NAoMw-nWt7Hardba0sJgFhgYHmx7moJwDuF1dNeAz3klWWhcH5etq177Fql6qy-f6DqmHivqlnuC4S-gB6UT8hXzUg4TGGERYpZ4dtZHdSE87CwyOwGz7s6GmPO_wgwKZwbTdM16z69mH5fTDTAbMw3Daj-3_JsLEoDik1SrBWZaKLj3R-Z9ZzicxnnxzL36l1eJJs1GC359jeRkQg_CVBshGOBRoyBEXy4IBbCcDxdedM6DHSh93Vv6-uzH4aDZenKIPkI5NiXDsuDoNCH5lUCCkL8e05iSSmC63ieZ2ubOYoI3VLuhlO1ZUzJfspdZRE-OL3k23Khh8Jo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMp8DWX5k-lixkuu35fTtQx7jqd_CK_QFOSftBkzEzCk41LNwtW965EYWso2dmZuT7cb8Cg8NWwbU5pYTrv5x5tYbkCGwQIHJ36zSLVLwHeLvHTqnUqHg8zSJfU8gVGU3yMkFfgd6PgFAQe73OjHe1VNfUKFbllbj6OofTJOKiqPI0F_AjkTrLabxOZ9c_hH-2S4wQaDzdTpGXlb60XNLEEGd2Sv7IHQKpEsonZeygzMoNqf5toYa9eX6ionPlhpFg4SzZ21qaK13Bo1OHpfPPVRxVCudMkmcg2CDG5cAv3Y2ANFRhJtBLNB2EoZxuD1LtChc7zoo3eWrM8kxabPGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjMRwzeOrbLol2yPB48Bp0S1PZoj5eY-h1BJhbqRV75saxvHAo1Wxpcl2XS7mvwGjE1g8lWhEaHh-pZF6QBuQX_v5iFxrp0p_9Vab-UUn7RO6HFIuhKMv0mbpXHRHLw3PpAjLrpOWhLrMfaKTcsXWzT9sOic5N5dM-LQbvWo4sKECMh59yJFGV7lC48JzH9jOeklwYI3qn44PYzVRbw2HxfepMl34VaJSJf__42Fbo5aeyxJqfPoDbVWjB81sKbXCLaTiVulLMWPJOKBerReI1VYg3RkaV5we2VeuGQASkae1P6gqnGatqDfaDT57TMlxuapNgmcYHyEgpz-0kwDQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQ7_tAoN4yOCSEkEYRCUksAqP9mqmyF98zZZB9R172NsJzIJ1FcJyJp1pGpofulLmk-kVCjyBSxeJUwJHESwRbxg4tWl3AFGLMQB2JnyoHUEl_Slmv-C12M4sMJETt6v4LWHl6lyxF5JTJd0COtmGZlhLbdwN7rIyMCrUMJZz6BmOrDWE5m0TIz5QLnFcNrCvnhhYyI-ojPrzgSh0VQ7eKf_owX3aNB9gP_Kc5AmIvPdHLYLys-RCUYnuOWzLi13dFKlBjfg1YlL4Nz-RUplXcxqNtf9UHmCUi7WtbAaMQFis7trpNjjIrxdchTjY3GMXHxHuPpJvEhbaYqjSHKJCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uih4OWEnnZTYOYFZkcnvHqzea9LUu4kXY6zo3_vM_241EgfVlPdVgfAd_cc_lYAine5zdSvB0Q8jq4cl0rDlsRhYZNfeoJeU0SQLfofPtWifZMcuFzNgIitTIgAHOi46lTfE0SKqnkptW1DBmN3nDZryUQhPxlLqaz8nIN_YvcJ8mRuJBHhpbcSCxQcKORxYTQvAE6R_7IKTf08clP7O1vvMV79QbYyYlqZzYrx9NnymSDhchcVSSmhlwBSUWc40e3YvUIho6053-hUUNSKHa_JeQvy55gA7CK7KYegeVCWxq_JsjWAw5LIUR5TPpnt9aTW2OIUqI4gFBSnl2OkqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QfrrYPRaR620kGK5rz4mfxg4O4buzF_G3DQq0_CMZL1_h1KDQVC9vu3xbaEZEKon1TXyNYokU-Tb77Y2-g57oWzcgfV-r9PBuY0EkKSiLQSel1aJhcqu631UO0H_MERE5HyK7dI7LTVEqYtA5-7ADf2S2RRA_49gM8dhNB_yUR-8oD3fzBYFzCS-vBJ7HbMQd_Kyfbfscj-PigvwOgemp1gdHcJY1UwENuekiVVhc5JCd_O8aKAn9e9r1OWq4ScYJcdqfw9tOslCY8-t3Xa63XgW9if7Wqo9tLkvNRpxS57dzqdi53UgGTiUaDqjbvdsNCuoi79POHHoT1tq0LTRjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8OL_W8FhU4JkN_QcJ5oIST0z4EmougW4kqje7ORhk1x-q04wJn5yUxKNNdKMx85fw3g9VoiClwrfOpjq3e0Tffc9ohG2X3jbLxnOG2KN-XgRPVPKKYtObv8FCQNblUpS9Ow5Q4eZ11-J6T3wOLc4k_OQiheNec4cAcicQOmWMbdtAj5qbFzeVqtz5FDwO7EjtknyIJDABepxfw2YI2c70z5QBw9cC3xygGx9pb-rLjllqfm17uSOHpPXQZ4BTdSMeGy_OqlHFfBabiirXafEhJuFY_6CIn0QdzkUoVpo3porgWdVTER44EwPVBSqm75zhQ3ewatIPhNKtqRUkTFCA.jpg" alt="photo" loading="lazy"/></div>
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
