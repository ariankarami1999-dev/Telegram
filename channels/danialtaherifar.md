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
<img src="https://cdn4.telesco.pe/file/QXrD74LnHiZ5L4kJwjVb-sEeH6R0J4QcO5fdVo9GUNHXdQ0hPKD1G0ye-OgLGn2Qc1tWCiBKuus-_ZS98UrWTJbZgvhkrCDDBkx7mBjAHcVnbylP_sslpXlXQhayYvP_Bf0A-H9JSCLQEaeP9CPyIZsyN77HzaF2FyA-1-9DzNm9BVKA14imGjksTvNexV7n2DTRb3I9_Fmj0X42M8P6rByyzSdfy3lv-M1Ik0xWH9tzu9bKqYBJQOFJAPmGUaH5B0FCtvxt3Ef4KVcY-4qy021JixqV-2UFXkM3J67wyoDWNHYaH7cjk6yT9C0yMVONaqDS71TGFbV8PW9VRgr9JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 21:10:54</div>
<hr>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 142 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 304 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pjo23T3WfQyJC4_Y0FsQyFDLsI4vcqkFJyxNYEz9Ky9cgjJqbai_LwtqjS1cUw5MYlgCQmRuJyPXCt95YGV9qaj9J8yeBib6-mxvcvlnFBD0_8au9DuO233fBc1-Gj6Qrg1Nm1MHvQzzfkpC2fU5vUKwN0cr1_slmyw5vmD8nUTVU4_E5qWye7sNW-rGzjVfd-0JgyCsxqhNTtR6WJnt3wQXo57sPkKVQukt0vuMW7OTKOmtyubjO2XXbk_UXp9BmVhn5ljwfVTle-cFWqfwzG9MVXzg4B2RKvKw9u9e7TS7NjpVCVf9C8OXWM4dH_HDoIkQx1G69tVlMvBQnP6HXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 393 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 743 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJuyrNgW8fxxjYgFzPlovu2IQBBwC1oRdKh-Xat0MU39eINtfriJaHNDmDRpzDVXzrmKW5N39mwA90F6rmze3q7X0EMFXZCkHOZgP-Je8mdc31oC_4HTOqTuubzbXoKLWS83_yV1rcBulH5uwRtlRQaHCeGXGC7BP7fKPSvpQ975Sn6XMjMobNQjOCEzgeG4uOFVV0OTXuMndl_mMNXf4goIj2ie0XceGZwqFHVm_1rgD3x9kWCzDx9PiyYMWZGhbKSOuMgZGrMCh8Jqlj5onlrcu7ufOEENl7qsuDJo3bGSYh2VVkdrcyra3fYCrR62hlcKfELCxEk7H-CFprj2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 683 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 786 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hsxo16ccJbCmXLxAoNXCYX3nDNk9yFJY2UuBfa9MOy-_Kg8OwGpJK6BcSj8cy5kPV6JUvnd70BvJR7HXdvjCpWaW37dNpWjfFAVwyZ6JmeDjhAIoQkreXmRl5lteSn1QpKLe2d3JoRs7dhUWZWx4QYw1huT9zoc7gelfTiJi86XYV-nMJpTT-rWHNa_RjHna_bnMZhKRJsMMrNfq4sMgBtWJ5npjsxYan2KMYlc3zCNbsxr-8vS689hCCScKRTquIfOLkaJBS3PGAbRWvDRd6eCnm-uz-L9Tyw1bDonO-IgAKzx9jVnz1by-e06sKltrPfJhqc8jd9_sATYWXcsoyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 853 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 986 · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNl0H07k-xDmEHMsNisnUOQe3mVPcvJExT-uwz0HCDbx7frrAi48rhvJTy89ggzl2SOIxQ-T7PekYwEx1DP8XaMOdPxFIFDjzt7GdP8kh1Eppv5Hx5Eol4Up-lmULYeqmT3yu2L0z421aPkHEesWj5weUchQV1hhHAkvXRuC1LaN03gfC4QJ2BP7Q0hl2dhW7RpOJbYhVxbtIxnsi2BN80GxjrIDx5e9H5d9b04eVjVWlocE9lySTWGBQZ0TtB0FFFACxZ0VJ6vyY8fWIT7bJCkRoKboqDMmv5w1d7EhKdVaQi9EadAmDB2u5gbFj3JeuYm-PbObamKuzbj-nRO-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 812 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 822 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 750 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 772 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 921 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEcZJgNSG6XfZZbJttl9o6tBdO7BDMolXTuwwEYzl_ToQnyrW4sy1cX1L3B7qU1UGooEr-6C06gXEVZbnpyyR_5eoNxUbPxj-O8UHAi6TjdeViQ8E-JUN0ny6hFVROzBdwo-0jAawti1F_WT1kcUoXq41sS1nhPymUSRJrhzwvnSiglj40WSN2thJqp6anr8CHF6aSkmGbFMdh3Bb2rUUZZ544xDuRYdDpz3gQ_LayeixpI3I1jN0ofWZnn9niIBvWXlmo_YBctyuTmNe-YQr8ZP3bHc0YVrocTxO-5uG1RiglV-s9MmdbGz2ZjOD6yBIF_HrbytV67ZD9Iw7no2rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 976 · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dK3CsTYoWNR-jGvp4LqK0Xl7WDgjbUWt1WF2j6XSewEeDMCHfXafmKlBCTCCtPRWIgXBzSxoQ22Vmy44CCNL0uzhtFezuLLNKEMqse9h0P8TEWLK0u1N-MMDgo4maVhthA0BXe7paA6zZ5LCOnTPmf6CQrRpuXO6OoS04qS-4ZCo2YblwB9YaZu3H18cwzAOZcIXDi-R5ps1DHrv33Eb14qjRNDRzuEqNOsKefvQw0HYTjoQGR7nLfBH6-uQcoTc-lT-eHlyxJ5NFKiMg8gTyf--hygC25zd9LKAF3bDDRT3ueSlxxM3Ye4lacIEY_LJiFhpBBX_NOsXVPCpkgMP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwfQ1vxHzHrxYfaVUCM8iOPRsT0smZHe_I6a3QeJoep9g2UK3ESyEKvNd6v-iNCedlx62Ce55SWsUtT1t0RyVcerpkro67MRCoVKx09mDrd4sd2rvyj1idDxfP_hDNSxvSmZKvnYABXnMTmbOEbUYk-qP43P-jnFDFaXUM4Bjj_QN-C-ZNccuel_X5VOAU_seb4UN23arDPIXJGmXmE8Boklb72G-wHDWPFFyspHsrAHLz-s851qQmDNLA6ShGa3kBqB32ag7Qew9TP6frSMStjfdHZq7GtFNo0NXA_kXqdqqIFGiFKFziFnCWKwL6pI4q4ddilQERu6tkOMQtTqeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuCTDU09T2rYbVBV1bnsTV_4r9o8dopurxTjE_z8X9CUtnFNVUwKuvCqu0LVue7OSD8TKODupPyHEB2RvYLw33Bdnzir0tdW1mFAR4k3jjRWJEPc3gu2YPWGhPfZq-YxL7aKr9Y2d-Ez5R5AyQuxqr1bEcUQOaFKyrid7_HIfNiRh2beE4VdPKJWAVv89OW1eVwJ-rYRa9ENHRji_K43STzpFP-SyxkvWgzvRB8iWtLT5AjneqAbm9gpabfZhM0ihvbEAUDN_GVLWDozvVB0LzJjjiNjoDWEuuwcXmbVIchSANwb2yqZwKwaEfU9GnMV0MKkidp63u2FSy5GnfhC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 855 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 929 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 808 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 652 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 867 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SODr28fG90K9VOsV4M1eHDR1OGwgz--SXMz0RVXJ2pk0MrOxTJaJ4fyNv6Sioyo5q7AETU1UjCMsmjtunkVkBMbFgxMLegqXPtBRfd0Jw5kBl01Bra7xLTyUxWkL5tdkBb_tVdMaKIXm79Mmw5zLgVK0e2i4Mv7LdTy5W5dsrizPOYfJ0Fy_GFa8HmitODJNn_3XRpoN4jIez6vC5QKjKdAe1BJrBxKsQ8TGy205beZ9rsIBqEwikWF7AqAiy2W5i3PdKJ6_VS0dsWicjmYpiZK_RhtnSNJZhlTjepQlMDjnEciBTPchIiWDCiIMfpAsSAr5C0FT8AQzNiXoOvOKYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 851 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 803 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 753 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Buiu2u2I--I_Fvie9p8wTfH1AA2L_dA-dhOVWtL6oa_GV0p4pmMs2Z0BnMN5s9fQubN8SzAlXmR2uo7PxcFrZaJ0VxQpAMoJ4vdJYCwQkoDSSvZiPVNjXUXJb9deN86ri66bMpunyTPIlOmnI04dwHuPSivG5CogXGZoZL_NKDECWXLnP3XPd01dkRGPYA_sjXiHsMMWvLiuw8mgRZgp71e1XNrR-3JQGQHRrcoCUfyd1djZ7TAjYkL2N8zFU9QsUcyy_QxLWgA0pC0jvk7hQEJ4e2uGhLRXA89sZd2qtKVAcPUTui-ztHqrtHMCtaOZuW5aI5OVjOtp--A_MKaFLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 823 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 673 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pe6SnwBewy7tPAxlVrrRNAb8JBjNv27wnvq4eTTFy9XP_pwPIQsw_ZcgHghDECPsmktWuoSsjOkJ1ZWQldONRqvu60QGyx1858EVNj2AJEkh0K1pxbAHq847MHnchg8j_ylX2uLUhUz1fF3nG6RUH-KEjTsleV9bLVDS9T5FjfzshAecmCKB78bTbZltLUxRYejHwEQn6YXPURtGo4Zo-JUCddX4L_KiriWjJqkBfBVhZOmnRZXoarPquYlPnhevy888aAxHnju5b2tjYH2Et4I35aumNlEXNUDW4DV9TQwr8VsWG1v9b_dBp3xnL0Vvhp1LJOa-A0UIIS4QHejcUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 872 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/McpUPZk6fEPf86Zp6TB75-I3WUaEcEmP9HbVR4-405zxmEGdZDiwI58Tk_38X2Okti86CSaG3XDA_GVrQdFtGWigzl40tWwabdIzXrF38b2ReUrlBpwWJX9VuYFIY7tUb69KoClZRYdEqVpBOMmx_sidO9p5CJoHCqjXoPuuH0zocch5Zk0xglzBh74qee9xFGyPhKmNOYVarON5ZW_y2SadBRxAfbrclz-Klgc3RJUiUsMznIoM8sUYqwfUI07CuDOGIXwvApYr7T2CXO08EUaimhQnPAuFsscGyquQY1Lt21M6ujzysxgsscCVDhU5IcVG9yyRMrnM9uysImNpmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a53c3tgHy9ety8t43GuWqKBNRs3koCLBn7MYpW5-pliOGDGnkqo80vCARIzKP6qnUfqM9U5a0of8VIlhxQoUV5I4VqDJRVx1QLJIWlb31E8AORccyPh4aQqLRw7bIGRr4OBRXUIDEdWzSdnjXRsbupiJy2OxQenEz92ZzHhCr2wjceYQ0k-wyNzGBrokMvkWeK5AA8J184KosryqGcr40eZBS0kVr2JIIiwbc1vISNjQ0fkHnlDblBKH3i_5jZIPafrQNSXj4q1JC2RKm32E-PAoQri5yX5fslczOY3AkxODfG31pbiq_pvCsGUE3FSnGYMAUdEWehuXEinVNmucvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDi7Nr19GaZAjUD7Ri6N12vK5xQw5Pc3T1zBVQto9-S8pjzH4CLpZ9BCGQqk4EEBwY9QiNR3lvyv0kSaYNhaQ6wj8xRbxGXXRuXb3ufnk9bxqUBM8H4Wrj5h2jMfUdGjWAv7FaRwrS5F70R3XFG47dvqCyjbzfQV9iug2YSKonZBUeco_PWcawXRyGtWgDq7-jORUmBoC2Mp6DvddGGyPY66wcElvWni7F23o3vU6SeKLaS63L5HWEcV6odcY-lkkha_-djBFVFx3XAMgOZcmH1ewbuGaKVJB_W1cVsz4Z6-lcOJLHDZdCc6aZglBS8j0-ZwBxdnCJ-_GzzPzPBKGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IL4bkhIQAWD-cdzPZG5SlLv6sZTWgKFv7hryJu1Eo3A0CLV4p3Ejbd52uAio8IMeGRU4Oanz0v7uMaohs3DArnUOVpONvMgpALGIUyiEK4saTNjCkvhYI_sDjS4bwgdFwSLc0SyHFzCJy3CkJXP-b5aIyCGlxHMFWOJaZNVMNImWQGdSilumZiF2GEUyLrZfSYIGOMj6D-nJI03RT-J1QISMHzJ-8I8b6HNfms88k0rj_JJamxC-CclTF-LPPjJ86a2DaUtnSOQlaMCbK2J5m5rx5CrOHw4FeQ2BRwoMvK4wFtquxkaaju9W9c3NtAcEJrDJ7L3nnAdEM1k0aOBeYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 945 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fb6KRlEK9IDU6_ik2RyZ8d7I6hK2TOvXSJHEbC-IW_M8OPJyDQxd5hiA5kNIOeD4N-zNzELk5BNhP3t0XQocMpk-lkaSPFs16Ac6k1oTUP87rYMdso6KFWs53k-t0XIzdhRfvGAeu4RiPS7om4gD5ZzM39PNlW1-ZFT8x2yZXrjmwkt2uPVoTuGf6KYJIyrBsnOv3ogjtNw9EMND4bJl9pj7pKdu4pkUcUUQusCQOwjn6V-VpETi82yH3hjG4Bklm8eHJJEo02WLBwWBH4JRbTjim6wour2rOPq5m-tCRRETHKsvpSxfJSKF5DHFJS_kyeGCVhydpQUg9oy2_EwN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 868 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=NL9l_IrPuYJdgNjbReaQ_RiK7SU3B1ip_L1ewIGnnMWmiScXdIQ5TTcvikhyTW30pzEFPVW4mxXVhuZE5wF8aFYzncnN4_TSZsjQBWZYLPBlzX-qzEdBDZ8AceUc3EPEMeUJ2ooa6uuK79892hZYT35yEqHXGwVqsvpm4RRwayDt__OTehKcHEUm1xhyk4OMHSUQ3ekaFJ4UT-dfyr1hNPz-T6_-rz9bBi_xmHoLxnbD5oRatAqngkU6Cq_1Q50QvxiW1SIfIyRN9iKrmovsaw34nNKno5zefUTwklxiX96JE3iRKgrWqYma1QzGIdFl42yNhewYwcwCDk3BwoRX0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=NL9l_IrPuYJdgNjbReaQ_RiK7SU3B1ip_L1ewIGnnMWmiScXdIQ5TTcvikhyTW30pzEFPVW4mxXVhuZE5wF8aFYzncnN4_TSZsjQBWZYLPBlzX-qzEdBDZ8AceUc3EPEMeUJ2ooa6uuK79892hZYT35yEqHXGwVqsvpm4RRwayDt__OTehKcHEUm1xhyk4OMHSUQ3ekaFJ4UT-dfyr1hNPz-T6_-rz9bBi_xmHoLxnbD5oRatAqngkU6Cq_1Q50QvxiW1SIfIyRN9iKrmovsaw34nNKno5zefUTwklxiX96JE3iRKgrWqYma1QzGIdFl42yNhewYwcwCDk3BwoRX0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rfc2Nr8JWn3I2QtZWfeAl5U8-8Jxrefw_dVJaz5awlw68Bq0zdNAG9YTEzhR4VWabiGTsWiJe0glEAT2CY2RBnb0aDI4v44GQYqVaKC4SAF0J652MY5ohVPoNr6R7ejsISms3nj7rjgZIVjsjOok5YdiXZ_hcgYDtxmsPk2wH9ozwRvTkOdGEDMUaiWXycUJitjLNXibq-U2eGyS05JWi6P7HEL39II-Lt1zCcCBWXgK5RfL5UT8XtEkbEYQc6-RTKDPSgZiEyiXUCtZZ5Zla3EgL9KgTv-cVyIsrEWBh_ZuQgjeAAsSf_QSGy8YzsWfE2aSH3zC25QzaeWjrpTLxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrrpQdqjz69VN5F0ref2fySbi22LPJOF5SJO4cSjG79s5O4NM_jaAW1rsCnU4Z3hZgt0KQ0oVTzhr3oe9JERfVzXzm7ztr-5c7NlIUngK5L4hX7uN8j8Dyjgwrgh28jBiyWtAcZVc1RUNcNZp2OnpYE866MRulTkc6iNekPL3_t9ixrCAc26q2NUDGbNOSTX5fUS3u2po_VEHstG31958yNQQyO_nlESHbBuRIlx2ak0mLFTeoAZyeI5qKbC8l27u8AKh7jxni_54s9YNWatVLfBrTZtYu6hmUdHf9XWjABXU4IDMJE0Y-2-QPApckJ03bxqrV6A-T6J2P5VQZnpCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 775 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4K3YRT-xzfiIh5GSRfcXBqMNRM0ZNoKwCNk24Qcgu7CYeSNYTwFVr28iUpnBe2unKVbSHv95rMww4DVcr5WakoO-Ve1oqTZz98YdKEzHjl_d2tQ3TRq6a-FcfRFOeOirkkVXjVwN47X-miriq3IVNw4UBpWvXYbYzbNSEW0QQeIciRkBJTycOsLWsF0TFVnKO48ehX0iS3n7S364xc_OQlSiUkFN6TsNoxMn883dNVxG3bABsosqSenIKJ-xWsKTne1T_sK5Q2HOJWZhkahlgLl-ZzRQipTJSp9CzaHrQONt_7epufXj76Cz8lsNYuoGO-8gwgIOhByM9koKwLENw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VBLZmVUA2fqEdoUlDzmUJ8Mmc96NeadXJeCz3qOAk3iNClLWtFqCuQTVnhUEvymD_El-WiiRgXz6xSx30f2OiRjVY7a2WNJm6lAYv36FgapBOFnzX1kaM4p09lbfdiwmaDsWIEc1G8rXltYp6qUYlvI_BdJWJCuRhp2l5KDbesLuMO0aJeHin17jKSWl1uHnvGGJVdGIKUngNiorQcF6ibt--fQ3kvhNm8jeGSzx8EU4h379uo5PE_ZxpMSeBXHkW-W4tvMhK3zJ3qLT8DnJpKAafRd8vy0wUMLNGHXcg2WkOlzeyVAho-rJmf4CA-S2apYdI-Tl2g6mKoai9cSEHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJAy2bAFoX32JjmKVAp6PhCgfHkxuFKhbMKa4vU-a-Ubx3SzoAYn5k9IwLkVUmrkFEnTh061OncVFcq6-UJpDCniwyAonxDs82X-qfzNROk6dZ497al8Wl9y7Gg40CCXTe96itnUccubnNPUQC_4CcCXQi7wOCLSy8TMerVsJ0vNRMz3OnKx7Vd5jCpH72D7_gFijcTTfM6GKsSqLQTEA7yfiYJa3Ap0kae9TZVKsBxifHq1FLqbNnIhK4AZ3cFc_qdcykCtxHlt0GdQZ9ZMl2zXaXcAdhRgpwM6BKcGmNWNTn6py5rboq1Ov7eSISkw11g8LuonDLXAkZk0UsArUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDpK6J2pJvUH3MRJrEmNhFO8AQHmAW-69oOV7-hCQM1Wey-dpKJHmrKM64GDntOxCwbmUhI_AuK2D1SYQGkVTdVymXVQj6rABQx3cZ5myROhGGUB959DOnPgHRrsfNk-kBsQuxjLKGT4UwxBclalsdsk-5Mfei-c8mWMXGMKH2jLrs9weHfUY9SKRHYQHr3V3LmmRUqu5U0umxVskVMb56vfrgtBz91guzgm8Hqs2uV3W5q8sUlFVoQrCZYvWCN00_PBHAnWuEQbSf8TlRcSNLJUsVRiNCd5CM_94dWbS8qo3XqJakZIfPTMQb37jmTjTv7CByJ-Zga3-T4mi3bSZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oeVcd-LJP1y6ta_8yCObpbC5nslSOdvOTD1f3d18ibRFcqT7AX4uIoXtyKU-zCbHF60_erkByo14umLbx9cTiAzucW8rRlI0MNJUhBT7gZcTvAFkAb7O6m76WjKx3Ot7WAa_Jl0iPpONeTjqHzUk13mpooBXAKt4OMa0qvSGMiziLOzl2wDAA4iIaz4STqWq-iM86XvnTa5qRlBRl-FgH8L8jqqkS_I_AjTGQTpgjoBEUNdCdBLW7jHPr6hhRKTqGadtv_dp1gqrSQ4VHbrw52DXf9sTYSdz7Q10ROqTdqL_VAyEQ9RbD4zi2K2j8pNRBO_SPwKpMc18EYHqZVCEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WxUjiCLePN6gfhvaiMpOl4jl-y2erGRISFmrRlKspQOwwvj5V_eq3IaBQuvbU-tqkI99dDahvCphCjWYCYuEmf3uE9ymzupmTPy-KSxVdPiYb8vs33RsZYAXtxmk7IV-rp3P58dc0NcbX2E0UF4eW8BYB8K89yHvjfeel5gz6NGq4z4xVEgIKBS3Hp_g1hSxs3PBQZkauiioqoZxUZAsmVx9hsyY9xr4itFHXndQ85AwwEdRsS4utoX81kFxz5VkMABaKRYlZJwufvy41pQAKoKNeo7gD_u9ERSO_3JK30sOW7sxMOHOOOoB5650rsQ_SuMzf0xiyW8hcIBGe_GE8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvB45EN4szGeLWP7uWgHF98Rpjv7GQ9zMNhh_CabzYiJ4ypHFrrAxJQy12HAB2zmlIUWw5qLB_PLcjJu3zT_xwwQa6_YuJXEpO4xj8zVlhpTHfS0qQZ6i_PmgfMh7FoFf5Eikc24LmL5cxE_3_ZIif6wwkEghFMmWaHcM26ZdRxWZ3E7ixVvw42O_vt-4_8NZB1R4wQfdH87XXazyGoLFBPgQqqTJoDPmuCln7QwdjTdPvksMjJg8vGJ0TYqCfixkzcUQjThlLhYHb4SWXjvQTwZvHx91sERPxo3jWFwH6PhTx_6N92sp1bb0whMhwkDvin4aXZYbpJTZdWBHNyc9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 816 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 718 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBUOBUPmw3Du-OgIc0ztmphHBOS370KGM7e5id3aWXJHLiP1AwOTWWQdx1Td_GQtXzwQGPv3CrrILePMCsT1Psb4kNYXqo549tRlqfBImLNUNc8KaMQDDUaoCFTQpN5znSSWY5qpKiPCb5EeJUc03gU16W6mlElgdBwryO4cIB9qT6Z4xPuzRVvjMDjmqvIj_4aPXhWVZ5KjA4jmlXQAuI-ibdjkHAEQQ9KivNzS3Zp2SksR3vt3BnuX_0bb9QjplSTRKrMKAIy9k2X1mIlC5o8eWOOgDPg7ar44mr1RZ_SvwQ9Re9q2q5ik7RoCZVZ6WNcHev6csdCtmPPc34TNag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 820 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVFvRdBfjtW06P-XNAJbyJrWS2BOR2dD1-C6S-8-hoHIv2fwu-gRFrFBfIjde4H5fcQ5WGC6X3NWnuIP6kPNzREhec9YCiv8skZjvr0bMcnqoPwkv4D86qwqmKGBwukBW1Bf5h9Y9oo7mZqf-8XvWBjrXNYZ4HtVJxWg5ZlcGbhSa1gVI-Gjh74C_TSrRjjzoD6cM1l8tkWDf6WLfr2LJzUh4Oy4ZqHpkxMgHwOwvEdIoCIROCDFh5Fs0faAFVuNz2sAsf6oS4thzKG0n6MdeXXRV1KkQ4IJacoL_5gJKfNZxrIaPgueMAYcvuAkjbgIrh7H0PHxz__gdQ3cfh8dTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj2y922jm3nOiOlv-hlS4ElqvF5YRZ2kv9lY7ISqKFj0spGB5xeDBMPCbJv6mK0ZT--_g0E-aldPDFmrDiVcUcuKXDetoTjXkPo9aQnWiFrRdhHX-fjQpAD95Pd8ASS0Mh6pCaTPM0OkL-yWHR-NIZ3ZSaOBd0HzIAcSmEoycN7BIjfOh6OUOcbx5iP846KmEax2exFWF0Nx51HKT_B4AdUgKFe3fC84bJakUV-IwUsd3FzCK-y6CogsTJgNu8rlMzWGX2Zx09IaD25R-XK3wju8ewCg_lxe4A-ywQ_tIk5QcX9T-5THD6IGF7FAqbNd-ivtoMm1xufVacfVgb4Exw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smO10WYLBVtLwYF9YyCrVlu5SnzUGPQ2Lo0z38FNT3snVR_dLBjRgk9rmsqIUI92igNOxF1JHpV9pDr0NToJZdeboPRnksd0L55d-m8yZ5hP9OImNSRry-RxrZIrKdi8-b2_P6Vj1HqYF-_pDUvGgmB5X7q4kgJQtdBACyo7AFwLLH3CvcuUjE3RR33swoIEJz3XZ_xzxqjH4oiWWvbZ-KNYJK0XkOJMFawPSySQa0PT7pljCqbcHtyBqslPi3oQY8--HNjep1Lje1ylMNNFantE0pSH1HjMg1epzOZ39HN_Y9xCvT0YCkj_lOKOvCGi3czE-jBHq7RBQLrkNUtHvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kAuU9Yf6wT4PFTsdKJb7d_LuCyGtdR0iUSqzuxglRWR7iVIzRP9fOMwJaHNzKcK6nSMdH6cGKU62odFPKrDifwuVSTvRio1VCnB2WsiL1d9VqutQPyxGWccUXpfxCcv9dTRitzSVBriRUiQtqaT9m7Xjb4rfOMWhGVbDDx6LWRNC58woiaPZiIiFMDKqGZG_G9cIntMESNk7Wj2esgJvOs6aTsmQLKJty2BfMjcR1t7kwDZg3ewm5gH40p8FkaH-EEnZfsrOC66W6akbP5RDwucOADflzdQxwwZSKFBh-rnBh1BHwgp4i3G71tvlMXi7Km4kDQ3sHjFLKZ6gBrudbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5PAKkLWL8gEr4gYNs6rOzNBEqoBK7IqM41icRMj-nfnzTDAPZUa8alNJ4Ju4F3qO_J3DxLW9mf4y8fGwQixc7_aRW93Evqt9SeO3C8uj32Ja4PdjoTxpBXElEQrV9t0gXFxdFC81ty4hkfiC4G5Y-RbtomK0VISveFbL0vw1YUVqfCAuEcYG9EgUMR2QONjfzbJ7bA4mfwY6aI-zRhYZs2NDBXEQ9UWQ6VUs6Cc89jXzmvDt4UfMNYoQPQUWIMHdRjaPw2z9cHAZlyJalJewx5VOBa912IafN-OGBT8V570gMHHDfO2_5JyHH98Pyu5CDmglUViX6cGlh2YJFa1Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZt2xQYO6IGvEudf4EhwOMMrlowhu12JyID8FhH2siqonVYEBvIyVf-rfYiwhKr2XF7i6qjom2i8bqVg_C2ZgG4jUEhGHkHbaZCSNyGn6Bmg_zMTezHfwLxdLrwp_8jK4TSL5jAfFs-Fip4ZOO7IbznBKnbISvdg6FpYoSzDiILi-pA5NaZ7YzD3O8v929JauhaLn5-bniVzhQdcc1X-aQYUDJXqqhwfhN6MFQxn1qZkKzYJIC4My83roML2FSv65z4HSiNfWOYGtFH453q5Mu-vo3TIP-rhB45Do0i2Zw2du8iARxxVdlKEn_nJpIW1tyXjdzc7rO2j0MnpBuWVZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLv3sK-pFcB_q8KV6GX3ZsnLtgsGLuZrlJD1eUp1YHmehnR1hHbipIA6kooZvkeLX46TWBhMH_hWw2eNK4NMUL05LhPjjxzzPqNGMCyaO6B7zJaJrqVkJfgGHD_FlrGGkekF4Ikom5ruwQAGtJ-CNuUg9LSg3C8UHbIDvXwOcH3kaHp3ATWMb9l-DWjKNidqMjX7O8P6laHioXR_0j5DXzhyGK1fP7e5dt08YUkRur7PkMGMpo5XVVneN3W_f92upnMqq9uvMoNHcVvjxjkSqYTdPKFTQP35g11y-CExaEcFcpw2vIzWjr-UYlG3WAghWt7HJR3z3EvMqfCOTzaYPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zh2jl_nBrLM3KnzuhdeGg1q-0IyHvsuP6QyCfUZERNBhEiZdvt-o64jU54RoqoSMU_e5z22kugBO2NohN4smTqe3nQE3-IxTY0J2p6OvkQFK-4g_y-C9YgdMYep5HyPMOmy49K4sL8hAx3x9cTpt4vM_KaOfrUZtin1mlz79lG9wJ8p1hp0480ffukOsao1DI2_EZ1ZsWzafkCbKUhkzO_R5AGkw-DqVvfmIFFj0vouwBe4rikBBGmxNYDaCSBbl-jCVojX5OpRwafbYWxO0oO6RgmCpWd-C3m_SUTjG2cFG_X2ueoj6vzp9jabga4XYjxPfb3eD3maRLj9l4Yhwdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGFgVyOGap0p9oLxZ1wI3XXtfppRUtl9xHKImwwNeDestDagbeaIE5GIBQJG5ReFWyziB2ps7_czSr2oOjoz1o03I9MAWZzzT997AKD_2NwBSAL65ED5YEdeGq5e0rwdRjrf0-pCMAgFfLs0U9X_d3To_Knwc3T3Areo5_YDYTJtU0r8X3hwAkY6ZHUYrUDFRkFgA9VfSw8tUZde7syaWo-R98KHkIIAZgTvA0ktA1jgqrrBQ-mOnhverf49ERDTFT9Sj5mrFPrV-fBqdo4OD0YQl3tIAHWoEfbyTT9ymUcwtdF7E_eAiWH32kmMttNyQZNmLlouuhOCulgSlRN7ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtlqcWVhEMO_QdyZ4dBO5xRgqJ16l4ckWuvFPNkNvsrW2FigiiQEvoCPV8u9h-hdm1RChvzCpDYFPYL8d9PaAzIROstlbda_Y55KVy6d29gwuhg0OByBlkwHP-mL0iwtA3y_enCpIbD6-XYQToEcTjjVlgygcQNefl4h9YE3wEkpcuHNkWNlLBnJTamj19wKz4YSdJ8g0GlUnXMMPLtNN5GWnR6uHZc_1mkqKA1LFQqrViVzu_E225stwfGvuGw7iaNoHaXbwjY2af_-GMYzn5pTum558xaUcVvOLENKZjS1vuOkI_ARF4tSvv3JGPLnTjBUc7M9eRmu6t0BuUhe8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k420XpjEE6pH2JeE4ZQglOR3UoqzJ7Z8dTAHseDMt1SbUlijp2ySzcESEhgndjpQOByukNVC7LvQBE6hYi7txFOrXe4ZkeBY2-KT87Hva7F7RhTsx_8TQAg4_7MuWfBx2d2V11pslv45JBpnhhFXbC6YMXgBXspDxqaUgbxDElt3bxviPWjrtW92foBwgXJhAOT-oNdA0l2Ds54D4AS_fCA3FkNgzRxcy0RarzIVM4b1S546wgN1JuDcgNoBqInc4cKV7QtvlFrf-wZJk--K-vBl10lFZdBWzs8lhSygw4MOzICgl90zBppAOmy3bGLkxya6B41ATtVXoazI9gHfjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqw8y5h9rDkcSrihJzkcMMrJP8BMD4rqWg9EWE5BTy-syfdo9ffI0x3bpRr-xfKsRc3dNXKe3LmalcPVFgoR3p68oqEGvCCeJBk_ghG3KRbGToz6CvbtnZ9G46JXfZOsMvU-1qw1uIuqH6U1HvOQJcLaxHM4WZ-Agx1Js5R7DbEaggAVObmTwJ9dseUuY0-JQ0nBfNHa7Wtav9PbwV4zEgOoRIG91pLxkX639d3bjhZ-R3RNjsqGC66K6BIF7azaRws4ZtLpNWPkKF5WconBjFyi16n7ki_ehuH-xLoOFBgyqaOTmx5DnK0F2H0boHefZNoAzeZKYHgk6k5zqbpLMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUF5Z89mZbxPX_qoHi4NSswNQ97VufqPzo4d7f4wf0BruRvELVePsJXT0COuoCOOmvGslNng26CWedCDuiZHAsaYRYLWDLeSiFPEGL0Lon_4qT94ktC_tYQXdmym3EtHKq7QjDwA655iLYIPFavLTZIXBwPdYUuEzE6D6QhVl4L0DhwXEUCjIrR7Q8uoea0UIj7_Y51xa-gqXwnIUSOuYdSbC-JFfglCJ-li7rpIT3oOL6C_DJjbn1invIxYMKTafYPx0KLB1t9AXn1SnqY_hgM3T56CGhQwOsuN03Yk9jRrHJMcBpw7MOiQF4pkd161WyLWRIlsy24xM6aMK0nAxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxZ2C7e1aA5Pah_K09w2bs75bqPG2EmGHfHpkyr2gafQi8-116e7Ki7ZTvXPNAH2Q7Lg2c54QKBNPBKVrYqb6oP8puylrJeCS5c3RMC0Dm55zkJwFufpdnSdk_XqJl3Tf5ZHd9waU8KR2FphdtVp1S35rnmE1bKx10S7thxi-c1YaybhHsnOgaOzxxL_ifDo0oMz_rk8B-iYz8M620uhmMo0ikpAqM8dDeW3vEWAJrs5DHwYN0HEmDnFOLEAGkOqyKK2eiNJtEP6gU3Ag9RdKr9K-I4spkTD0SgASGpb-dwc7S38s6SB7YlE5vEcrgShyIWYKSjz3eWBl5GMCDGYsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_QWp0PwEceTSF261CPA6m35KtudP-rWppTMNSjW08UVfvadELgXF95QH4C-gUViTL7ferDekzAOj4fpX9UOFl4A3I4ilenV8DLxEqJU9Hf2OOFVS9yf1bAXY1u4zCRXtUFBy11AqLQ2IMSgqxybkNOeTi3t5WbtecJsEMO8PaabZ1OBfyiAcFRlN70pDsWGTE9k7we-K9ePlkx8dMe98eObWrETEsBOpOzteJ1n2SWmE1zMmDkuoN0dtk1fkRLWzPyGNSL3ZZ-qIUkA8wNcwZNL1cNlh1Js8RBT8tA7FTw7d8dZYuZBssGDuyYMQRUctL6JMpgCF8x8bA7VpBzofw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNY3bNjw8odz_5CnSgPCBL8sEv5KGXvnNjhU2QIMxF6UdmWM2MKDmWH1XAgeWfqExRstg_cFJKShEWsf3L8kW-KMbSTljQQJhFI39KUVUhlr60o_cOmNAvw2axKYUp1zfWJZ65cuNrHzJyzkDNAJlJmM0vEjfF0xP-e4xFctMQQj1sCJB3MSTwEzKUOeqhIxoivqUApLGq2meq3oktY7KWe48fOMQdMlbbSfCtjZEVVzGlJin2MfFEs0pSXyVy_-2qc10WfaAHfDERbVQzUaLGfXa2RraEYbE4PEKaxIBamgNHA0F3dAl1oo8UsHAY--kirB9oYjiFJtqxA3HgprUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQnJkPewWjPeOCZe5jqM5650l5588ekoK8ZNPcazg-GIXwwGjjR3ddV4Y-UxIplha4kxXNhVMFw9oFHydTZ38DnRI_l38MhcQtbTKhUGkKx7XUskD9tUEPT8xiN9Mikdy-dNezBzQAxetJ3DUWTZkxkQuUCLN5s4oyB4lscyNFOa8JB2CDnWz9iYZph6utdQxMs6lPPJzigtuYG2gwECKh0zRCwAPS-M56bN7zYw_eQuKoGP-t43Slq0EIE82QZVDnpt56UidD4PiwJBR9b5Pk4tkcrfLWgn6iIzhjpWs865xPvQxMEbYTXiM50ajKwBVGJl5-9UEkFbEx9n4ENRwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7myHS7-__xoBFkmNlgrijzqw71GVlffkKGYms7PxQDHzCoKIk1hMX047_ekqoNKvR2dALVD1kzdmV2Hug5M-cv0E7_vk8-QjUDssUDpGaINCLlRAX-BnUSv6GDONyEe58EDqaj6NgNkUeq26boWY0OvyCrP5zGKoankBaDRCakJhvCi325t8mLS-8VgT3LT3-EjApkiayIcPYr0oQjt1oNqG4ZRO13JMbEB-gvYSKU_g2BT2f0NbFXR7LfynNhEgOv7XSenGbdw7UU7NvCQxlXH5qKpOpQQ98kWM5-dL-3I5wagvdPhsx14H5BLUw9ZjJ2jLdNFMO7LanGqMEGTjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmGGciVHIsHNrYhgokQi9HlPCsucITKX9qK9-bxA7NmtlHSSHkIPqlQg6O-EUl8TEZxnECv91N5-gcMv1DesXNTnHSu3iCCZ_thB1cLKScvszx9SLnNitVp1n6404fGuO_5izR5aeN73pbeMGSM-1PWiEq5y8rtxoojJfZoTZtdD8X9alz5YCGlzv3H2gNsb8ma7lEO5GGP0XEU7cfJeyuBPVW-HO__K75hhYZ8qpVatjXHtUlN3AVKLTuWv5mlhM6RPn1JLFgnXVO25ZMrLItxUPb5FtB8Uuvy_n_i5zDNro9IfLZfh5K0u5oDIaMjGIePe35n7ehwRj_n-WrrP3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYCk2kQf7CcdS5KJQkfN5BcoW0XHiDr-sA-xPRav3FQ6hu2ZnqEPdtdHLDx-IQAgK8Ns31rwzZqu7VqU_djQLvhIIfRIhKYFo6k6d7aiztD5dmMEbMBbsHa6RR5qGGH8RTmXdNiixZnzDRZSm3Nlu0LZiAGfV6z-jz3prxNwVEuN074bkviIkij2lT5ak77xgDYkVSrnwr8DDmtP0uA8fOf7TfmKxpJ1JkOa33duJ1k18KBHk0HiRxwEGmEorWmE8Jkun3t-4X_spJXj934X2xPaW5B_aj_qe046duzszy0k015R7LlNW9NHcvevKIenLL1jQNcqUTUr98KRsADJsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OfcALmJP3of8PkPhpwVzaYR9_L2mfKxeHYL4099BnaYEjwCDsmSxrBvnWxYUGpukgEUTta1o13CZcubkXzN2NYuNLoEBFu_dL87TgavfEENbntM-AU4u3V3tHltgVc0ZVRdATVUDOSWA72Lt4HoKg3rv3SpREfZdiN9PtuXkiGP_sKtSTeYSQHUkoJr33xFLcJ2ueLR3W1LXj1jAt8TUMHv6_SCyb3BXpkPejmGtEM_-b8UNMSqtMW8cP20S5lFBNdsqhVwiV20lGPt1uVcWaKaCGXjWGl3wevZK0469gaLzGUnpRJcbrA-VGcOk7A7s6x001zV24F1Jw8iJviUJ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mP4WeHXyG3XXljaYKkGnYQX1RotkjSqyH65iisqS-sc4qQHPSIvNbFtfXSNr0j0LZgKWthjlPiiaoHaqJ7EYGycgasywsT5qBzJYSEPaUGPjlUlq2DV6eEtWFttF_uow988sjIRsTNKqDRKJMX-TFY_imKV69qIL6LyQmo4mfklnembEgPnbFSv4ECpYyqcOrbj0_hmF_Rxz6SI9uHjj7v2sVaO11vZWoc-7j2d5-0iBtSHx0bmKyLiDjn7QCfMBGyUtgOPT8TCyRpoIZZSSvqMVgMKP715X8-H53q7Le5wE22in89eH0CbSApArVjnehvE6pEEr1v8JefX4g-E3LQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRAuRkpmnZkPVcxZEUPFW33GxqxnB-jqs_jYIM9bwSv-0WOYwkAzSJigjygAgOZ2RF-6UcaHFRLJ-2lQDuaOqFkHZwnry-RM6yshwVBwbKLxaSp8dqRJsrL8srxT7HSYVy9jVODHwqrQxmjZ6Kq5kk3zJqhJTwAWijI_ICGadW6MAYz4OYk0bfIvDdN2Bwweccb5M4JmLJyhfj0Q9HeKEQPQF-awKQTb83uYAW-6xLeD_UbPGJV3GI3UX6pDu6SvR2O62pULab6llu0VtRk--IUasvg1Dk_-GxVBYen38BJYDwtPAG3vFZyo6S99Rn-XFgyVk1b7cRVZjkOMP90IUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EM42YODBBdCAT8SsS0YvBzAmUMaGgdibUL537Ls5k-JLtAiZ3BfcPgPvqIb2zghZ_ChEc1DNK-LID_wFHAgglErYzO_RvjIoTg5AztqlKQSmeYSRLhqXRvcsZ77LZNhr85xBDiDe5Fpvy2ajR1RRGPjIYwO3tUZRuoLn1VFvghxHVzKvsETu7mGSH9HNFqpgoSerHjHUzopuENYgsVEwZcvjd0xCKYf65XchWhC4_F_34g9tQBJNTuMYz1eKBDjUL7HJryBSS1fvH7CmFos__ChKqU_HO0rfNo-Gs7nS3InccdW2_aJO5RGPcqy7xCH78ZLl35yBsnYnXzd84ochHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzHbohqYamGUCQlTzua1tmDSA3EObz6kUBvHnfXDs9T9OHo_hnEXA1VzPotFxbKwDGDVrSaCwJuPLA7bPl6jeF7N0iIaCK1h7jD-CWBZDQneeEuXVbxbm2sXEivrZzWVIMwxGUzpPtHDKV3bEelzo4TYVBj1DG4jzQ-HwH3N31jG6VGO60w56EX1u_ZIIlHivfAfRdXnaXeoxxtSsRrid_T1LdiUjVHDXy5XJPuAsIWM63BeUrSzLEv4hwVb9NuNp6-tVVmtoj26y_919qiOa1ptithIfBi8kVOxlC7Y5TB_fAG7MHkv_qNZXzZ_K-2GTPMgTHMIU83__VNtRMMJeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q2yjwhA7w_Om764i7cDoRYLwsT2fh1cZ9uoLGN1UbdxfBjwfk7u8Jqtz0jqL1Ry_HDu3-qjTHS_LlLtTtt2b0BtXacqW5OaD90oebLh1yM-iqu9SmX1HWGQnWUixKy5TayvoJYYCFtI0yiBH3g5CJYUTPNsMiYy_k8iw_fyiHaBYGiem0zK2PiRBiJ83M8M_qltW5h81keB0yOx-T0wM153Fz_xr7qBDbLq8109ZE1ZPp1pzzlp4hvQrGduRaVKUHR9LX-DSy4fKKAZQmQ9unlgcqidUFFqv2-y_21kpEuCzWb7fYo4kDjjN7BKT7BiJLu5zFjFfE7863XzuTsU6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bpHMOSkFAucgxp_nLOUlBkJKh3nJ4rgdWZBBBtXgNOlWB7hbEE0IFE2pXovQqYAUuZWmxdBwh6orXPI3Pkc9LyWLu1o7ooVZfvi7_VhA2e8z8wvLIQny403lCwtopoFeMMaID9P1VSly6FKp3cxkgqvlsmCKvI_0yKeKVCgZcq5ufkhfG7ytji68RwuL8zo6P-BSTyv2ZCNu6mpU5vdtZjIP_L8_Kr12dYRo0pIawHp2N3TE56xO65-Qu0f-j3hZN1NhZHXKF031R-LSRM2VvktqAPkT4DUleKY2tGD-lOHA_SCeG0wJuHU_pmRGBmFvslnNKqWJZU6ctZM_Fj17dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUbyk2PPdWYPt48w8BftQgvmtnhu7BwFogZthonGYwHg2Wf0Xvev_V4_nrMB-CiIt5O4bmby5rBl-cuQ_eN0HR2OcxhEi6K7M6a4b_ZcjJ-dZQYarGbaZYjPGQZNLK-BnwbuUEBoiZ7Sp_1Doro2WwuddY8ip_qwXF-EvoQiVzAtFxatg7Gl-d2O-ImwspXySzOYDgoc_kv2PfE-y3UiH1ADcz-T6egHj_cm48KEePKjlcsIlF0Dmw8AsXnEeZM4x0Mc4io6QD9MnrGgcQIc5qC6pn_DDPvGeqQP9QEjH6uBXvRgSnB6pqAexMRwR1Hjj9JzLGLg9s6gXM9YVjct0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrs7CwNkXDNPN93WRSp1KQlo8lZtMBHImXh7VL4eBDVToJ-n-QqeVy_cQ9lhdkNffLVf6nz01WV-ElBM-F6M7LGlA5HCo_wii8APbTI_YSv0NPEOqCYl3lQy0c4iHFAusDDk50LjThXI5QT2DehXdhTQkG-IfaPWBpCdoTvRzaWNX1yurQSB_uoMJlAPlFFG292kiViSTKTQKTa1T0x33D3eUXVGX2OmMf-6qiB2Jr973rs3mNh-uH-rJscAspJt-xrm9NjCnbMKHWHdL1FZHLzakz6rMNxaJ8r_l0zSDWce6B7CMatrdhMGm2ciFLRId0oVvaaA_yWjySLNYeCXUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3CMrhJl_f2e-Ef0V09DaadaP0Cx-Co1v-E0BW-1u-5-heQGnbT1ks52MMYpuRYWHGMTkHfTUWnYXDd850RyNEwcOQrrJU7VpJQpji78cp5m1GsDwy7QqxGeU_i3vk5BhbqVNPXBDNM4Sj-G_zV_S5FiCB2-Wa8GHnICPTfS0q6xpT7QJMQXLqLiwI3c-V3RoGIwTyCaxB-YpfzP-F-0T77tR5zquDrVAAQU6bNZjY7Q5f6EKFUlnZAY7sjGDTAs7htH7YuFvk8MMKYWrBjqjkTsT_b_bXXWEZi52bcSOGdsSoiehHLMTRVxOccMDr8QrWJyeKtEIplNqcd1aeCrMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 769 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OHVJFk45Ay6dPFfNHyhibjYSHen7p-XfJXVf9IaFQWwxQN9NmImeZcUl4T8GqJLhzlzUWY8tkZmzeRTuNSiMXtfOfaST9kO9TH9D_hq4QrtIlEYevGo8bFJtS0Y450TpZYe1st9sPRU_1vDAOnANemT5kCyfG-TqAtm5zw3qgxfw9tdMMU0B_DWu49u4zVzX-jTiQY8kH-lnt-drFeMFxvMojFF_B0LTyjz_-LLwwpyWHaUMBvkI4CS02rHvBVklLpq-TzipTB_1PEKmE38u7Kg1mC2RViBs9nOHgaNxtPqUmWdZHKMg79l3MhbBSXQccNvX-P-xv95tC-qR8q2vog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JtWk1EP-FDZAJoij1u6IvTxIitFNGNqsQYA6apjxx6JXQFtQaULp0D11sFYYj4dXQ0_HT5UqG2_xiQb5b721GorabCWKrEawfbRBYVVzweyHNYZp0GKRHT14PpaBNjXdImesN7WwIgwoI4vwMnLm1ekWyhcoIN-ngKVchFWaQ80Z_ifWSXaMs_rvhiuHA8KhH84OhjBw3NGUqrkDTKzlTzb0NtABMsVr6xDgFqfU-DwIRzXdbhLUzDaHelfT0yDCa5NRRl8pWHLYlwNpbEpBnMIc7jo2UK28EVhwLXx7JKE2mtIqnXq1G5imiMLv4FZR6dgi6uq4fX7HElxbyTrrOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZAcNU9X808GKWzl-GTROLHUW3yVd8cBoEr10ON4UUsssq0Ij6bLaT8do0jxth1K_8bMK8c00oaU1OSY9gEarrLH_HXSyrPxtEDTXHH36wCTm252B8DuaczEJ-l3vp3SPxuh-NIPgBM8ZER35itN9H-McSrcKG7CyFBJc4p-Sn99Cpq52YjbukbfUPTfCE9WHxFJQ5AS39TxMoAe80idiQgsS8jyk-z1OtBTp2eigztYBVaurLDq8F_G7UHpeVjOWt2NS_9P9DUZAIoQsnMqFdmYK6jzotesQaL3X0RETBEiQeS8FRtJ1ATKaz2UBWLJTqiDhUiQ9vM7wpf2lewhXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bup9g_3Z2nXdk6y56k4Uddz354YxoKbC1VBFZHrrAQyXNPFkxPkNndvZF17dSq_N1B11U05FYIwZd9mkOS5tIKWiFJzcgUwu6AeDsaRkC8EGoDc8vvU2i_Q-kpCRMrvCpt5SODDEktw1CMLnidiqGHKZhzxGa-JINKSY4CnEYGRDJf39I6ZCwUohPwh7V0IB0yR5THrphoXXQhXYEyZSPQbG5NFXet05GHcYUb8eaFiyx2KHC-9eViIVP2AAHLpPA89pm3f4wl4OkiwaW2JNBtgcBui44OpLcGUi9iv5D-AD-wS5G9BGHg2EC5bYfgW9Ds_jewlp1dlzNM23smAfuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 662 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1bQvMTGuc2xG0wY5Cu9Z_Hdk-N_HnQpRUidQZF7LR0-1wVnYaPSEmuA5ciZPv6yG9iZLHE8OVS9HHlisZAtEa0ve_Dxpz3IFUBmtGIIQWWFqBntooAEfDpHCBdzEQtl6lRqDZMGEJ8zHk_3Gxig-y7TtuAavznSgdEFi2OhusShOiyEJqj2RfXDsSIN0FMgt2VMdLT0yU2ZbJtjaGFHFMq-ITnPQW0SqZbEj8QXdL-L2DaKdfN5uCHG0iqoLEH0X3l0Bd5S__cOTWfM7BC2f6uinT-jE7E38f4adv0OAAoUWvdcrteA-2amEzKLfDeyV_yUJwHHvoDSdR_nVn6-ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgpfCGIYAR1LUw3feTKjzbq7C5n5LTOxrg2tkPeB-QcNS7DTXlXJ0VQ48L1-UI2IblkX5zpo3U160TAGP7cZNvpuCNkjrosWaz_GPBuqxsxXQ8F2LNtYQsk2CUU3eTIWckgNDMREs8dPLzHiUXCAgsJp4l4LjH0MS8Hu4GnFJKAz85sB28eIdbHaoUStGYzThLooqa3BFa9iGrZhD0vSHeJBnr1lCDmeuXVgKBrzps_NEhaJnREmbSO3oLJ1nDGwlc1pKJHJqr49hlfiOv7z67GyHHXsUr_eKUVAD_wRg3MDpShhnIp-95WDdU5CHrM19B1KWkqSjfvbqWju4RpGxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=eQ0JQcyzf3euKx5YyRZCeB-aBoHcnq00e9Q0resPmzK7_cgeNkPS56VnmUHx9UerONiStzaut2wDH446UqEaL4jtC_RtOgipKkJYvhOTy1ZBKxc_phBs6FuQMHyTHl3OUlaltdSxu4jbJSWDfeeoa5jEstdTZn4ZZpHn3dnFliKZPImoXEv4Mso0gSnaRAY9p8C3338HaeGh-fCHc8-usbu-T8PaLIFG3RfkEB7vajwu8db3tyOhyFw7LlIDkdmAKspjeGSUJ3AVZKIN4T_VNhI0sXMzRmY7Dh6uBb98T-FMv8aE1QlH2XT6GxVkC-fHoJ3m-OHjEBWKc5i-fSmASw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=eQ0JQcyzf3euKx5YyRZCeB-aBoHcnq00e9Q0resPmzK7_cgeNkPS56VnmUHx9UerONiStzaut2wDH446UqEaL4jtC_RtOgipKkJYvhOTy1ZBKxc_phBs6FuQMHyTHl3OUlaltdSxu4jbJSWDfeeoa5jEstdTZn4ZZpHn3dnFliKZPImoXEv4Mso0gSnaRAY9p8C3338HaeGh-fCHc8-usbu-T8PaLIFG3RfkEB7vajwu8db3tyOhyFw7LlIDkdmAKspjeGSUJ3AVZKIN4T_VNhI0sXMzRmY7Dh6uBb98T-FMv8aE1QlH2XT6GxVkC-fHoJ3m-OHjEBWKc5i-fSmASw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9TMCAXmossZVsa-c7L0zoqDVh6ceFiKvKKDYpDHEWtQ1cRgpBAQoAVtqVJ35aktyt8gxKS6hrCnjRDz-0HDdqzVowfZZA3li5GSoV7v2QMIbXws3flAmqztMsEp9s2vKSQtbkIZo_4q-3czwF_DU81rtwzuWZePeNJQ-2qZOjL3vAi8TMe0sIjX8TgezWzNXzhM_UxYLZNS-4BnrxqGFgAUc_3LtFr9Sn4CDIixUCaexyLVPaG39C6kAg9NkODW-2EYc97vz4l07VqhlzOXjABECvoV-onSz0AkCI40Paqiyx9Yplc7sj3T81j76NjILK9LBb3KuwEYBmudDfImQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ziqa1ge8x7xVdlDiS6EMv85uC4d_Jn3xaH5R__36f5lhTs7df_A_cgNJUNkD_g_-oK8ttZb_Fz0waoFVO6dcFYrRuSGRP6T4mCglg4AH-YRTz3OsQagAXpu7LYlMdnJ-IND5mVIe-XRuZAMKQVUPfpBmGkI2EcW419aYtux2OcCR6S0qbta2yKsQSuud-dwrzofyEX8aA0NjfzmpX2h7VyrOAvtt2PM_a7T2q7oU2Gis0BgLP9NJ2B8MKqwCOTFDU3iSKi4dgFUDkdCKd_vw5ZXinv7rjBob2GVgxDIfSB1l8Aiu5g8CMZoxaLW8HLM7Eso7tlwoiEOK7Y3hBIh64A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/beozLLDGE1vVtc6On5__krHBX5f1RZxYlHV4ROw9w76hrFKPe3b-0lotw2gs23tkRVcc-PAq7ZVzG-pCnmr6tURqh7hD4T7_MKtNWvugAkQb3CR0Wpa2i0r1t_TgUyEEM5s1hsLNl-gaCL404XdohJfEBErcOBt8Lw-u6XIm9xeTTaySIw82l72CBvUlhBaQtqBZtIvw4WGoWSO6VnYKfHoxR8Oz-y3qHv7cyN9O5AyVzF7j1cX28j096WVqvR2RrIsYXwu-3F-FNzzElSQjxjYviwnO90sIZTaG-PmDUHJFFH7d6Nb8si2uxObxrOldKwx6GAopEsku-28K6zCutA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPghVDjmaY8RVSCPnKN9f_1fuOkr7FwrywrX7SBNlevTd0l1uj0Nq-njpk9QCG_hMWEX87KAUq7FSgvuUAmwNBejrc9x3qmLFUfSlnpdXnl1WhxBRGEN9OG-grlj_9pMVuQJLLBsKNh8tqjXLsDRTan7d_oWKhuxO2gGMQdWDaZQVYyrOqfiyA0Bp2ZCmtwzktDoXGsEyl7REvbJ2mL4AluxplF0PnS4liDCedHVL7-Gz94P-4tXywgPs4y_arIaBsVJr2fByUq7lEaqn1kQEnfoGoxzd0RVRguWDnXMQ-qnnMCkIAZQ5GiLMMK2snoCvL0A1rx-28nsyAfNGBjp6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJYffDfuk2AyO0lUcV_zspt5tpOY6p9-VDuiFS2Up8Rsk8ayGGur-PmJNp51sf60yXGkFQ9bVajuvLBlMoqKMWKCLbJrEqKHanEe3gcGchEFCoOhhD3utwwKwOMKnDPKcajgsv5eGn-HOJsP3q46TSnYGuvJhgQKp6cRBCQEwNdDk3X0VsCO1JP6aw679805QiRoB7ByJuIpDIEzfxQ1OWk9iAblJpaS0-KhPb7vY6luVoqV5E-L3s9Ql_jV89IfNCiW7oqeRw-ul_B8dF9Vk1DDAks5KCuPvjpJpqmxwJJ-p5PaCLelDuBM87nrNtlVlPfEUKac3kxT4nASNOw0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/caWidyHG7_jlHE_5a7o3qf6DcK5WhOBUATeEN35_Oy3p6Mdzu2ltIISL9U6ijhhD0eQ1ZqiU8ZQfLmJoki5aLchYbelgRLDuUmHZocdf7lchv9wbiJf5U_QArwV-ogawEK_7fDp0UL962gnYKedRLi1ele2ZnfXQncL3ES5e5Fun-hvcQ8Ghqozje5XTQRHr87U3sHDLxyzMJ9X016-8sq4ZlEOG1CqjTTCnhOy_pbhCIkQcMD8tisGKk1AHnUpflLIpG-3x5SE3boIIQHUDfrFIZRCSEAaessdVTw8cP3Z88aloxW-8JZHVONy_j1mEV77wFzmjXXn_pg8r1DsjWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nV3RXWDDqV1INz_vNaYRmr_yILV0XpohXcwaOT1yyPaODWLMKclrW6YLPImzrv6XqNThg2xl1L4Y1Me_yEcM7yJni8j7xwX8Kgqw7Wlca-kNSDkz73FOmMzzbuQ0gRJ4c11wfY9nn2WUghLBh87O1s2mg77eqUJA9w9Om8waye9YY5tqjkqY_CVASF1N_UEU9J_jU2UUxInw97K16rukRgQalnW5ylXsrmSPr_FqCtV5VHksxjgEtoylQOl6qtnwQpQDHZM6UwPeti5zr7q9HJo8WDDZaLN4q1zKLO27cBanVkWSXN61XPncMgmyLeirnGSl_swS_txnYfaABoBSlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=lxeYy43XWmH3QLQBH3PWnE8hELAazZI1HMryZhBLqekBfxubFQZ3CjXp4Twr8zqrvDsW0Yjr2NIl9ahLbeAJNzEK9ag1ayeVcyksMY1MvmoPZR94Wn-wFaPMg7oHfYHxjlsDIxVrwYg1AZ-LKX4tiAB-B3Di2JARQ-Q_x_SNmCdx_urXcKOGsN6rz_2Je5JzXvnaa2FSjk_nvL0p-T49miX_BgJnOtNogKFhwc_UVJDC_aOB_WjvgZlMmz0hbefMM3GlRmaonK69aZyai2OlkTODM3fO16QznTHu7yn77ni4C8kprzlODY_kTIQjJXDE72rxZRtAihFdaJ6Jmxm4FFMltCxo6mwEL68dGK-e9LFBMg7ojvbAqWO4SyDSAaOcFsEyJOVd5RyeocHCEDV2okvoVAH7Jb-73liRbxbZnNmDYYS5DM94rvgSshEqdNxeT0oaL9SliKYCofQUPgaHo5JFXSc6EPg35xrR9wNByxsnXLs17wB-jZOtCJMglTsPO5IqidDi_66IziYAwQ1WDdkOZS5PzLwhYvkwAprLgYJ0y83nSA2NMR6zaKTjMSzBzk0FL8eTLvWcBdKCn-v11QeCck3Q7bxQfrUnXVAba0R6qKsJrOlN7VD-YGKwxtfBiFySfvkViXN9HW5h8DX8S6T4bCQiEt7eQlXh3BniHNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=lxeYy43XWmH3QLQBH3PWnE8hELAazZI1HMryZhBLqekBfxubFQZ3CjXp4Twr8zqrvDsW0Yjr2NIl9ahLbeAJNzEK9ag1ayeVcyksMY1MvmoPZR94Wn-wFaPMg7oHfYHxjlsDIxVrwYg1AZ-LKX4tiAB-B3Di2JARQ-Q_x_SNmCdx_urXcKOGsN6rz_2Je5JzXvnaa2FSjk_nvL0p-T49miX_BgJnOtNogKFhwc_UVJDC_aOB_WjvgZlMmz0hbefMM3GlRmaonK69aZyai2OlkTODM3fO16QznTHu7yn77ni4C8kprzlODY_kTIQjJXDE72rxZRtAihFdaJ6Jmxm4FFMltCxo6mwEL68dGK-e9LFBMg7ojvbAqWO4SyDSAaOcFsEyJOVd5RyeocHCEDV2okvoVAH7Jb-73liRbxbZnNmDYYS5DM94rvgSshEqdNxeT0oaL9SliKYCofQUPgaHo5JFXSc6EPg35xrR9wNByxsnXLs17wB-jZOtCJMglTsPO5IqidDi_66IziYAwQ1WDdkOZS5PzLwhYvkwAprLgYJ0y83nSA2NMR6zaKTjMSzBzk0FL8eTLvWcBdKCn-v11QeCck3Q7bxQfrUnXVAba0R6qKsJrOlN7VD-YGKwxtfBiFySfvkViXN9HW5h8DX8S6T4bCQiEt7eQlXh3BniHNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cNV6e5E1XnE8g2AamUA0D6chU6Yr9-hnYbU7CsEl1qmtgq2fzxEGjOzKbpdgCxwpi5ZN22p-QH1PPjF7wcSPNzk0WXC6jGlDzlRMD0z00Hl9tvtcqmxM_DSW9FYuUOaDIehYSyvfxtRkaIcuHTow42TSnKmh_UgbJMYa_VDN9hXedOhDc0IJq1gZc0MNgOW7xO4KvHNE5o-uW_Ye9T1Yi0HiCn4GrneWYIOYIHE03i57i5nYJPzP_eeW7G7nQbRt0qE7-sZ5bsJ1EnRg65r5SdYshkoEn4C6jHK9oyViy2jAi2RCSLAfHh71x_sFzPDbi8AqT6QGKvbXkfxOO4koag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q3fKhqtBpOmQtzP-AgHBJeTshvEEVdTP3xswbNRSQbxP9_1QOwRbHQ8CBlTHoo_UnTTl0oH4iV6QQxa34YdrvFO1s0XH81nQOfQUiJknJNEO1kppywp198mKW37mS0m-mPJWitD7vhLcG52LQNllFlO3HLj5uOXaE5CzvkbXI73e1u_1XiQNoDE844Tuz6Fxuzer0FToyIgGAh8U8XZPu8PnwhCmVfWwnkBQOLVtK92UGeBBxFpGsDQeAEK2y57vJ_8q1siwTlds3AJ5mBd0_x9kwZlNh6nkVXe87NegFVgaNw0buNTO2IuY3e5JAxr6sCi6UCPJLrtLk025fwJEYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTwDbYnRM7zzFIzDojjEaVKMAo5WY2TVqm-3e-O5q3yu-mhifYSkk5YFdOB5fToRopVmE5Z5o7witJCiE6DN0WHZnjYWdT-47gcFHelbwLugRutVZOL43m06FwTPE46C6WL_rIGZIZOWyODgmguosMvNEuEtYnSg_for8evElMMY8XBLpRn-61LkLBkN8jAFA4frIORhHYhp3iCfseeHntWG95fyjCtdOIwaLWyaT-tNLJEgG8aOxAmj1O7t_bztIij-_Va-hc4eRT194rFs76fJgEDeF7TNpxlzv1XW050pHB7JKHISbYxS5TAKXj2-x94WvHImp6pvacObsqt6mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b8IywYh7mbllnDB6KfFoo1Amc5mBZ7f6r4Dxjralj-xtb6icf2eZwmfx2bQV-09PpIAzPrOCAZQKIGsdjC4H65hRj3npT_qsmy_2oWPqgbuZ9IJJq7WUyNsW1T3rLz0oGWEple9kVGMU9PpnrNvelL5D8UdGST-b2z9Wd4UtGLLHILtUbkufP0KiqpyEL7L11c_iy6ULYz531XRPzqnQNSpngSAlzbc1tVB4auj6qx497rpra4goIfiWJOigc8c9wzXNhZ_xh_-1wIdwSHhWRyZu2A58-8cVUVxK-Ug0bztXvlp3rTLb__jSqhoB8-zNFv8F5GyP5huc-8jy4MmZ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmBK-kAIJYQITokuY4XFAymM4KftPFkwFhaSh3I_cOEAdkfbJaRQ7K7opKegeUXbm24Rw4UvFbPaeO_Vo7qvEy25o6GFURp33AuuUmM1nvaHl1VmcHPU_cnNX-IOLOfeq2nRP8EMcPNxwd-hSsEmiiu8ybodUMNbSIY6GCxV9uD4lPnfsyQFja6xd9RDEMgxQNIDNQf4z8KPPaKkrl_chnHghdkNPqlO8sUb64qGwtXiGTaEPdNEwpEQOMJdqwfFsKpbF8NY35MakfJz15JmFCA6_DOthfY0av2aUElkEayyY6AJuE50AS7rvPFInC3rQweFxH-nFHZnOZRFq6oO0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUVxG_jozvOnJ0gr1jEIu5IpLMChmX0xy7GQvNoigDQTs496RMg8pXYBnKXBUanuGuIJ2yOJwoP6vasyIuESt81xC0jjThD7wJN7JiF_FeaTCPsiZXN9LiZtlMkRhgKj2gnshfNhw2HYp6lCwCVeUBi9dXRD0SFI2kYFvw5bjE4fA2Xd2TAChaAgS-GgtrNQ5Eb6Y2gisllFdhvNwGBmvZo7blhGbo6nCCm7wj3uoxTfqEtfcx0b60esQvw0hG60aOdgC103jaloz_5oIOPMDniHrIanPLlc5lIlKP8VOfXBXiUTMg4Uob-wI6qsU6GDSNrgprQ8HAs46rmYcFeGJIuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUVxG_jozvOnJ0gr1jEIu5IpLMChmX0xy7GQvNoigDQTs496RMg8pXYBnKXBUanuGuIJ2yOJwoP6vasyIuESt81xC0jjThD7wJN7JiF_FeaTCPsiZXN9LiZtlMkRhgKj2gnshfNhw2HYp6lCwCVeUBi9dXRD0SFI2kYFvw5bjE4fA2Xd2TAChaAgS-GgtrNQ5Eb6Y2gisllFdhvNwGBmvZo7blhGbo6nCCm7wj3uoxTfqEtfcx0b60esQvw0hG60aOdgC103jaloz_5oIOPMDniHrIanPLlc5lIlKP8VOfXBXiUTMg4Uob-wI6qsU6GDSNrgprQ8HAs46rmYcFeGJIuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeDadG6r05a2rn8MW7Qz0Jn7pWFkUoPi68fSXlJi69vKEc-TAg8JGCtLbPs_JK8w3zJUUGiAInPSZmaz7VmQuqfoBX9x7cXxkjCs6glT_Xag2l7uzCMJaHSv1eZolzsl8UaNYN6xLmmFHrHbluw8ll16LREql1E98h9fVXEHydnFWP4yN_R9aVX7GjqRrODDsiFA8O06Imyt1ro1FbJRQum55z5CmAZsxqVbMdmM9EGwE2XoO71uubonf_q4mYUrxjRj07-Ei7toPnT0EN91nQJV2ogK-CdBNKNZa_vgCgVUgrLH3ucIbpPNhws2ZEXMyTbzEioduqegt0NwbtlYgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnBzCmk_CWKL9cF0WkT9fC6sxFSpEMEcyUTw0jMSr5z1G-X1J5XLu1woBwFzLV70bBOt7B12rSWKKvCGhjAH_Vp33MmjfmaFNrAv5IfFyW8QNAfvnQyU-fVf_Ooa5thRkd0ibu90RZxD3RzbkfpqzGlB9osXQ9nX917B2f0hxBUMzIUE5HomrAKqV-IQqfH4YRJLIC1AWgZn3grjo-2i1Mm5WnL2-EySd9DPjtA1PXhuSXumywHtSBzCzGl7LZDghcTteFjy10C2qwTfmHaDVHz0D5tLuDYqaNbEEk1M6KeVAhjW2mywQNCUPTUG0H0DcJdAfGiZvx38ccySzoePoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ezCVCk7B5hflRtETxow45vMp8RTqWmEkFq_WCKkNdGDytCd16knBeSYATdKGlbI5uWMUzRvSwA6ZZMiSdqIdepaeNF7uJ3uyWkk67pFtQEtqF7vTk0hYe9OInO3flmXgWTOJUXPdZJqX4T8yfRkLJ5VRapQYDS8B5ivRFgI01A98qcH4jw6VCBc25YTVt8mb7d0qsvI3aVzs21IC4ETG1KIetEUEYixxq6D6ft07urA9nKBCmvcb8zGTh4P_bgtNm9h4ZZvGI6WGHRdOqdfvzKaqegJr8himNVGO8OTw9dmNApyGgGGK1OJPUiYzikhnq0QWOQU_N4KRJ6QZRDXSpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KOPKSf2Q8MiVjE8NLukA_MEYVwG0m0vcI59wAHGE-Rju5jXdLVsnebGETG-qP6jiMe0Tk-hHzWQ5TY_xcCj23KQOYmIfU6mBf4nsy-_3xW702Fr0u9P-xJvsN47kL3ju5KrZmZB146yk037vp1bbNoHDovYfaUL_BfUmKCXcC1IIJsk_N3bpEzJhACyyzNeyN0tc3ans0vc3W0-NkbamrPxMcYCh7GHBUQi-2HjxV41aIaaM_4gbZ12kuvmQz0odDdi2TUSbz3lVXEQRZB9fvyrygw5OzMKM5UZu21v-2gd7Pje3LRtVhz7mLyfT3P8GabdsCHBG-x7dqRt9me5V3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iw84q70cuvSmjpVfYUy_cqS7ws7Sa_lRYJH2kOXaTloNpxihe0Ps5PzFxR4WzEI-kVuWCE_niOj0wBAleZ4h_741S5pBVZwgd9SATvmiy3RN-slY6B-WIZKDJ-RhPunSRkcYKGDWwVCio-QeYmVQllpA2Plswdz16xGaAq2K9oJe0HKGYrtU-1qwc_1gZxUI2uYdB87U6cOmsqqGEOjxkI-SZc7n9kPRIgHHsu1AfbaiHB9ou0-NUnKDafvw4GU7vyjXTlsvB57nfve_1fmM1-VOiyMTsqAoISzQQZY8_Ckfod936FbfU2GY5GI_xbcDhXhW4qnfLNQfyNYltJRyag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEaUJ-9aPFgfoUm35S662Mvlul8MUzZG6vwh6muGWUP9X1PQItWOAoP4lILVSjksvDWQw2X9yKFJN3nHwQPzzJk34fEQHu_b8c6zaaL3XQGgqLU9U1LlTL6K870IG8-bsOiwa7WqhjOS4asvsAqJH7jS2zUyeJR74T9JDoNof0Wi-qv_baAa35XClsZy2LBpVTvFCV6Xqf3AT8lePIoSYOX4hVq2pxSRlYknk8mJFZxyaRkm8BN5fnOtbvwLWKsVYRlgOwwiL3qEqqydjHqLW1ovt_rtLV5ADXk6DjLQCYZK_aQUARZRYdCvU7vBdsugXgyQYOYsn11cBBcau1kWxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
