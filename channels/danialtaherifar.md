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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 23:28:31</div>
<hr>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 159 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 308 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pjo23T3WfQyJC4_Y0FsQyFDLsI4vcqkFJyxNYEz9Ky9cgjJqbai_LwtqjS1cUw5MYlgCQmRuJyPXCt95YGV9qaj9J8yeBib6-mxvcvlnFBD0_8au9DuO233fBc1-Gj6Qrg1Nm1MHvQzzfkpC2fU5vUKwN0cr1_slmyw5vmD8nUTVU4_E5qWye7sNW-rGzjVfd-0JgyCsxqhNTtR6WJnt3wQXo57sPkKVQukt0vuMW7OTKOmtyubjO2XXbk_UXp9BmVhn5ljwfVTle-cFWqfwzG9MVXzg4B2RKvKw9u9e7TS7NjpVCVf9C8OXWM4dH_HDoIkQx1G69tVlMvBQnP6HXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 401 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 747 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJuyrNgW8fxxjYgFzPlovu2IQBBwC1oRdKh-Xat0MU39eINtfriJaHNDmDRpzDVXzrmKW5N39mwA90F6rmze3q7X0EMFXZCkHOZgP-Je8mdc31oC_4HTOqTuubzbXoKLWS83_yV1rcBulH5uwRtlRQaHCeGXGC7BP7fKPSvpQ975Sn6XMjMobNQjOCEzgeG4uOFVV0OTXuMndl_mMNXf4goIj2ie0XceGZwqFHVm_1rgD3x9kWCzDx9PiyYMWZGhbKSOuMgZGrMCh8Jqlj5onlrcu7ufOEENl7qsuDJo3bGSYh2VVkdrcyra3fYCrR62hlcKfELCxEk7H-CFprj2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 686 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 788 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 989 · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 751 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 773 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 926 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEcZJgNSG6XfZZbJttl9o6tBdO7BDMolXTuwwEYzl_ToQnyrW4sy1cX1L3B7qU1UGooEr-6C06gXEVZbnpyyR_5eoNxUbPxj-O8UHAi6TjdeViQ8E-JUN0ny6hFVROzBdwo-0jAawti1F_WT1kcUoXq41sS1nhPymUSRJrhzwvnSiglj40WSN2thJqp6anr8CHF6aSkmGbFMdh3Bb2rUUZZ544xDuRYdDpz3gQ_LayeixpI3I1jN0ofWZnn9niIBvWXlmo_YBctyuTmNe-YQr8ZP3bHc0YVrocTxO-5uG1RiglV-s9MmdbGz2ZjOD6yBIF_HrbytV67ZD9Iw7no2rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 979 · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-mZ-3K5k2XOGs8qCdxaZQoIHp47hdx322YotoQ0gpuj0I2iSfP30iFIQ_zfWp-lVbYIM8VR0101ibu8nILvnUMaXoAayGIllPAR764D5h3UsLLSdPgbPMa1c0zWgKXp0MqPA_WKF-OUP7qYoWIkcKVWUVgOAnoxzktNrUqaCjxVjr52Wj5jPsv-oLpAzubfxzFd5V90Ye66bYjohrMbbE9zaF2w4Lpr04l-t6XNbQvp7LuqyzcnWa94kBUBfVaFfWK8vhe4_o8t-fR4E5Bhxe0l1dgZvHAGmfQ0r2PTT2c0TQXj2Oj36abMEdw_-hI6ew6preu37WSUKCJiOWhiDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 754 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKdLwIAFHwYTLqzsSp4yP2GnwQhjamdMZAHg1fXsartzZgYmctYiuxMK4ei1pGukiDbKRY1Wxqp32kLuG0_KAU0cvVNixPPFf8Dq9lscQXmROq6cWLDe39kK32iP2rDV2_-Wof6yj0oH5cTajlVkj1ZcAf845OqJbgESncqcJo85_J3IeHhqogZGdByBV3zUYeDEVZYDOmL_upsgIMJ6omPb4-oQLy0FVn7ePmBqsLdD1VYMx_qG6rw_jYe5RCdALNZQNZC3Tda_OoztwK9IqSRKje9rqbnXt4v-Bf4HcKdfrUHOkU5I4ZL1v8uLjrn24c9KkwNLc3Sd4V-dFBkiXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOqNhLJrcBbSU7ESVNUOEIe-u1JQSGvom45aO0suu1qwlSmJkp5R1x7bOiQux-6PCaytcSSjdP4FcbQD11qI2ZBCIPKi0c6iAJILFoX72jDaD2VLmtU6vgFP0057WyNeuQiVsQdc3RAjOF0DmEqqxbRB4qS10mRSVSls9SJjVzx-UFXWu3igONcRLonqznpkaAd7ggkcVySLEfFFvJhiSuerEoZ555LgTRx5DvBIcJHoQgFXukEJs8KmzaOuek0U7uO7n-hTZ6gHSgLNsA2Pv0sZky0dFCShK9CWh5jwv4mdJgpMgn_n1iu3eOopiH9FMt_fdmkbbTDNTtk_PzxRCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tz-sFimYWBKOOpCUEbE7v0d6JgIC287GRpFnhlXysikcFuypazEcrL_JBXh5Ol4g-nwCcA3Jc3vADvnz3QG9gMWvwMS2O40_5dF-IqDv8wQBs5fIlr3bOGYs6sOX3rNEAXqXfijtddb4QJ3PRo4mnCS8iUtM-Ey9rnAvNnP_iFLwyeletc29D3liFz2MFHWblpw3H5P_9w3twhrDlLkUjXhbrH5UxHmM2KAFzfdJoaXyt8OGz0jICW3muGBHScNNevX-HTBM5EfzGfOPeYkeNh962mdZPsVF64mlLL4TRytXllDt2-5flpTKgn9bPDF8fiteLVIwjrxyjis93V8TRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ECtVoGKiNGPVTSQhrWzuVVfp1SspWUQrXhaQbQE_judpy-PNhLbp1Z0Li82igHZiZpXgpTNJY2C5cELSjmufW4byw-Fs3pOLovW0Tap1lhGMa2fBhCz1Fues5jN30t1QgZD2WNJRhy746cchZTDFy4XHbd7QAJEhpUs3D-o9Xgu9iIYdMGLo_hoH6il4XR6JJKRe7OHTblEUbSWetf6ez1qnpF4d-s8raRayKpPP_3Xhmt1081lsyYZYBYFRqj8auacrBtwdqBNhk_TmLhMYCFcq0qKrg24yUEqAo7xhR78spmLDUDhry-8OnBu0C082VIkEm2-Txpmi5q-2YEFPpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/INjO-K8eEuBF7Fx4BL1jDRU3AMbDLf8RT7R94nN0mVo9OfXX8nizBFJZReERmHWPqQd9a6nmC3a-17AJhOv6tEGeGcEdjAYrV7nTyVfwfcNdtGj_OFVJ5U1LXqkhCa2_7TDLpLaTNY5pQx0nlTCtb4oI8MLMy6777FVu2_j6CLZFNlQfmcApab6AOU2e60a1c_1hJHhNhaIew3pKa0wGk0H6nIa6Z1ieM2eTDWMm6D3ZIzIf--vX1SUqoBfpvFYM-VutlQM3WvHdn0xYOgwhZRHrpvv3Tj-hwgCK4FpMPYH43DLe45Ftx_tAQt3fQCA0SO3M-bEBElrygbX7kGi1gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vSckOzr2CBJkK7BY5Sk08IuF0lmRsWA01w58Rzc3OIjViC-_q0SExdLfrOYPNYjszda0f43qUOqzrpPEzYzpJKG17JQPJ4VU3v8FEC4l21mNA-O19OLdKbvomjqf6oJuv17RfD9aMzUeeWI-ShliEYIv_y5Om514igylTHe2hmjAof7CBwFvd5wZp0qDsKKNPr-f38YDu-9DUhu4eVvqYne8nbcmT8-2rOFcsoxQuhWKga37Y3W3ZYZJwoqZiMHA63e_EKG37L1-yDPVeR_GQhV-k6JHxvCYDxmT3JaC1ABGU3jx1u6NAK0JvilY7tAtGyLpYn2GyZVMUwJRzKQs_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cpm80RHCbM1Gg2Uskzf0x6NUJX59WRavAlFwZsJBdfgaPG2yLGnUVirCLv7b2pWYQ_HKJ8ARzV34mU_l2ws-93n02XM5ImcDYwpjA6EKnk5eZVkEJFgxXZWN9wUR5QtrqaB7jObGx-y6S1qfvlaLlzLbQ_Yx0X6e9zh0EVgfx_42WW9QMZrwe4VU5_xKA5lho8mdpqrDvd1m_gL68f4MQvCoTzV2o-OP2FkRT27zYg-5CWjI5G6gGSfmp8cy9t1vb9DhBDn1_xWPP_l7jnkQ5xyZbGOMgtFhIsJqswVNIYRhFwGT4t2dzdaXi7pBHQFyvCmRtXuNDVq7WO5qdjfUCw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=l2N6p76SKL-g4Q-GBgIFRYyHd3EtKEbeSafYjGbosUcF8SzxDKl3wTmPjsqAQKkvOzR2B1cvHzYvoFR_6i4H2T1spIN9ZE-QeMeqVJxn3Kqj5vTPyIIwZ9TEHWO0ZiEHka-LgTuXlcwEoz8bRaSW2ogdY1rZA5nHwoQYlqfhGX3SaIXt-udIo6Pu2oNhZDpnFBgMplNw0ZsPCIqPCKEDBJ6hgBhwi96LrMxF24_pL2TLZkyUdXRdqQwwUcEC6AydpYGE2pWwO2QSUr7RclkGjOmIrN4k1gjPUOYgiVcjrO852TgFBqoilHSBq3nxJtjhyuflH-vNmv4JLHikuN0_lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=l2N6p76SKL-g4Q-GBgIFRYyHd3EtKEbeSafYjGbosUcF8SzxDKl3wTmPjsqAQKkvOzR2B1cvHzYvoFR_6i4H2T1spIN9ZE-QeMeqVJxn3Kqj5vTPyIIwZ9TEHWO0ZiEHka-LgTuXlcwEoz8bRaSW2ogdY1rZA5nHwoQYlqfhGX3SaIXt-udIo6Pu2oNhZDpnFBgMplNw0ZsPCIqPCKEDBJ6hgBhwi96LrMxF24_pL2TLZkyUdXRdqQwwUcEC6AydpYGE2pWwO2QSUr7RclkGjOmIrN4k1gjPUOYgiVcjrO852TgFBqoilHSBq3nxJtjhyuflH-vNmv4JLHikuN0_lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrMTYCT_VYhNblX5DwC0irhkQIrEgbHwc3T3h93n77-1xJJYqzrO5hoD9YkPLFHyvdemYanKyh9-eb46Q5KNpJxS9bAw_nG_vh7voF97eLrR4VMnIq1KgsXh7a5Zl33QYGAYdDMKzvJRD4z9BANO6GjgdZp3MGrGcPLNpUyD7wrs4OvtGgfMDFK3HyKRA6Ji3feFV0HEsPbQEbODy4UGE5DMPD_Cez9rDOMPceuIdjsZ9YK1EFGQokkWl_J8BgDlojdePlrBt5hfMvphkeD2qczWa4YK6tIaw87E3kR0Kc0y4IUwoSROHJCngdsAKgpmSYrj34XVdNC5fsR0GR333Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjH_sojBC2O8N0PzuLphRN7mMVxlnoDZyesXuTTjseiE4K3k-x6YtxozksSKgHZFvNNFEu3TQeofd0hh-G7AamTfBquJdj6OdKam-ofDkEKvlMQSdpVrT1iF2aWo2bmlEZMoNSJAYFjLn1BUHz-UAZ6U7yKYj1H9yCdRIP_AsYIEQ_m1a1tJXl7fXU7sLLHzCMmfj64FVBLDMGiWTi5xGo16Mtl7hFiBsLAjX60wtfr3QnW7ZvGnRFOZEjp63lHjZgfO6EZgdiyyBzpXoBotP_1C-Fek-Jm7HxU82Kzc7M3IAs4PyaiEvwI-UqpjINQTe5qEZ93FQpCnn0F9qydg1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HxNoQMifheuujusEOYV1t4GNMcAI6-cB1QsYcI3vcifytrYiDoX506ThVa9qmEpXpW4rL7DjuE03MkiDiGyzxK1CYK8ktoy0KDGIcwJzL4v3Pkt9HqNAfNFl_uGZ4NbnVYlDEXoIQTE2HorXTuFOn8exk7C2zHNprGALq3B6sF62iFAC3zkjwnd0Kw-hFcyODB3L-ceEzdQUJJe0XYnuxZOhe3JFeZoZ5cpocO-OOvPB_FPoWQZn3fZ-C6BX0V0OH1VVt28l5kCXTZ_vSo70zouJdgXGhU_b5LU9Kbt9ZZfL3njcJzkRO0wtkGEFAv1E9IKiDeWVJ000oPAyQLgKVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6l5K8lhLCjDmrFE5B-CVk97h29U0A_TJNPyKFODZ5yfU1CyhVxzP6B0Rw9IGlEg5JO37KPzH46IullRj5S3sw8p5POtGu33m6BT7C3bO5RbewqEFkzdf5Xrk7KCViWdaI2tcjFlqp-ePFfXqmfq3e2L97zZZkB8ExIUl2Gq4ktkrdNc0IVdjDage9g4HdMpl6GfmIUmKYaMo9elgIKgUotxv8L2mwINwlbZFXlxZ8rXtajCVVxBiZyAm440mLX6ECF8qHL52PmK1OY6WzldbbORkXUgoQkFv1O6XhRGhgExjTmuM26l_iWhKtxVu_YZF6s_NmcOe2AGE3SOQ9ptxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnMWQqeX_1p2IdwMzYjs1JVRBo4s1dvz7uMSY00C-oDlclYo6RNvrvdExacXYk_lzWdVSl1NOURoVvX62y61gU8TcXyTqoPa9HsBQmhNxrKsSLmexEHiXqJP0LDQMn0WsBXXtfQEml50vAUq984K7W-P-5lEpY-Sn9JhcqCY01mYtxdK5crwQ-iwdXyv-4TcM0H89PXr1CqcehGDno1U0JgR4QSNgulfwBvNHYAIAF5Bsfbdmad6dtLfbOl-6M_VR2Df2hW-RZxCRZmH0Z4BHN_KF5dlCWQRUtL1gy7-YSWYHaeT-n_YnzeTXsGZnaEa-GkeW8VXdwqKDX3veHn_gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CT71xvpumAbgvl_68LPCZBFrTuV5PTjEbldhyWt0KxwP_nYUchzTniww8RoMPN3kTCrV0da5Orwh7bFm0iRhlVmL6yrgLHrG6oUqYwGbAiT8knb-OlVF7jqI8yNMd-K1_Dfr4HvY55c8Xx4R_3JGIRBCh-IFmhTrHeddbe9Fy5pNutNuvQwJ4Pd7Qa3srXTKQAvoZnNRxalLm3HVG7QEhwoCZeIEC3Rjqs6lTKtxMxltBdSAQ4DH1O-Tc_eBzoPB6R6XofG919bOBfXgLJ7q-sHuoHyOXTpUgepVeOBWAAzbmOK5iGKWB_GdPjJKxYPJDi8faHa2TVj-lokluUTKvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D24Fzbb8baK0WY0prmcQrz9uCEMqw9OquugJSPWiKUwlknNQATXMQnrVoX_MymdFO4KeK0ulMQTVqPCNRb9uJnMsZcqt1UIxKLPOgF-8jdAQD4zblbA6N9xXm-AHF9xwHCvyoYb_x6YmRVFqR7k0HshvnmbZyTvt2QWn2GrmMjqbNtnkE4NZmgiByOQJARsJwaTJ9UKLmagJIT4BwE8wkbf_nAtNn9QYcgV1aYAE4HMwDEqV9Ti0mfrZvXzs4PPPWFkdHj9xM0u1cvYjboTt14bZXrToCbNZitmqtNZ90tgVVgIHuohjltxtG8S9K1fhEHrt3krZP0aSlKEOKTZz6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTjzQS3gAEAm43Xz3Bj8w8Z2IAIsC7Lwnwtvp3mULGef2SeujpFSdiuDxVZE4E68EtsYgjeDzVvwrer8RUuCHJ4oeHVnBN25WznFHNSgXKG6q2u8324n4kqSTkoHsgkcu_AcFyRfHR2BSx6ynbXeVV9OTTBKOPJtsLkJV_l8jbsqr9ftI-oD-TfvbL7CqmZFVPcmtlgkRFA0kEUAqGThwdha3WZEQjZ2Z5nBrvUgAzyXmlJOvqwcsZ7ld7SCHgBMhAcnZqKfts3QPIYC0w6OT5tOF23RPGRiK6hLIPjemCATzONj2mk4Dc60O2FgBtdICeAJMs7FALSmK6CnEtlWSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFkZAFK4-CzX2yTERPG4WC1P-m9LpAoIvQyt7aLkQalYSXp6r5pgOeOjNVMHUYSFRv8b6Q4pjeUHhkLaNzRIqvlT2mL6FBMrrYELRqcahL1OM3TYWhTWWgfrEhxaa3zQT952_RafZWienySx4jVFkunMfOR_-K5v1WZR_HG85CdPiGT3SyTJMVaSd2EG9BhXScGYZWLDVAgrTAkWpyYfUBi4AUHlUKQxSKmefEZ6H7oypne4Dqj9MLB9qCrXBqG-RBvy50IIbZ99tyom_8_liNA9MDzxoLeJW4xAvhd25Tubsowur69SG39ef9oelEWhZ9cshHj7_OjO7eMoPUIt5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0XIePaBsYVUFKJHQHsmD1WpUWWkhy6uY3qSIKUPBo6EYUnlFd1FGh24HHbzmhDHwMUwXCj9HUYIW63OR8qXlAaq6DbWr7k6VvtapRHK74r6-kptF-dHu9HmRrLhldyRhVgM5yTPAy1lQzGZ9rzZxtiz9JyILSid-daeXDCREzddupGDOs1hv-X84KRU3VMUgsQf2M0o3woQdGfc3nadptsQtp-Luc3VXgg8BPYo417FTGNCDMY5QeraN7TvvzO90MWirShNtwmmXE_Ry_LEvb9Ig_n0yTG7Ku-b2SBmSpr-0QDc0tLT8HPGIu4-0gt8LcXQG1b5OLRPTUOfYkig9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaocoNjWY2ONK_2cOSdhahibHRkKT23U4xP4C0P9xVuZKxZ3e3dxa6yzzCpul2TjElXvVgypAOfjHK__YfL3cMEuQEYT6BOA9PyUoG469yB3cV1iWjkU2T7dduUlGGWjSytK1vym68RQQ6m5O_8JmpJs5iTdrHZMXWWOpXFI7EvKP4mkIKAp6eePHlMGEmZm85uKkuEnNuMG_-Hvgv7ADg9oCx-RKhd3_7KkexXas_zM766CuLwHelJvUBbgkzToaelm8WTRy8eZ_KWrJeHWGlsl7dzqNAa9U0Yisni98kNtevHB0JRbTd_r6ky20mKiIhRBoBd7M7-8jd2Y6go6Jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qw8Z96Nj0mgdIc2EF1ZWcCaLZGVPYVwjlV-UBB1XxRcf3_Ugw1srngnGYRRBAh2IG5sJ4tIZSS0PRrnSPPY_9QIRfG5QMD2Cohr59bGPh2ccWfoZxsPoDykiKkJ1GEQ4MCVTtXaDkANQN1nvF3M48obx1Rf5I2KVu8nYnqkVvpvONAdCw1ghPT-qgzhZKY0xkX1__AG5wJD3pn0NwwOwmw8avDX3T5Ufavl9F9LRGZ6kP7RDcfV96VmLBasbialCvxWPeWPiIHMMnvKfpYxbybCfSAhA9nuZ0cJo-PkMDEnOdSl1F-tqj8ygEJekpWHzx8yORuaUJ9LG5-mmDQ4v_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EzIvVpxX5PED353CNIOagBoyVb0UbqbPtmdWsx7Zc-nuXdWUk1BVx9W__1yvt9JoUSD2_mbcQJewDllCOb_Q2Hx4TUuP8TU6d82OFxMV4DKNTcP2V4JfGU30bL33i5BUJ-8Fs5Lmy6Qza2MGiBPluCdpE0ggCECGqOck-bxJPFcCctXxSgT7v9dESP-8S6LdGPq77L4TxQaSH00EJJEY2cEUvTg-dImVJfTShYnjlXcH2ixZs7PexE1E6tvFXDYND7SiWEr0zkL8c6nnUNWkjw4N8yK5vpLDnxG_KchBgw2VPjboJMoNI4JeMYriJFaRyNyDb1iCG-TyMf5ZVAC6-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLAwsrVruNz0TElqCJxR0NRtTAVHtxgJzP7Tte2hZAlDGB8Cf4xL5a5XyVWbNO3E42Bm-FjR25Rs59vUQrLzJ52aWg4g1JSBsE8vEQ8AccPdkXPjjrSawjbBZeReZgF3Yz4jpYC9uK9toGjBvJW8piBa0q0qZj4dF6-FFsbgdqLWWoBbiRKOZaXL4MtBlSXfv4DQS9Ppqs1tt20pBrGbaGf7O03I0217mT6WwlVfr7lnzeVhzERTm9FptJmWW_T5lOwQw6bWqaum_f6b82xWg-MfdAxrRg-dzqwXpQ5bcFrKgl54ZWdKRRx0CXcZgjK_wdOvyWA5ozQm1xlWRxR-gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RDuqAzpkNFHHuy8dLVBAhWN72N3jFMEQmLoC_cgGz_410QKEKad55F9OzvMEQwY-DDu26J9khKd3fm7JUPzlRwpdV8PGSp9v3ERhCtZupgUgiMa60zbaoGIEzXYS0ehAUgLRyXkvyDR1iaVh32WBApH2cKK7RS7UbFugcEEZQCBxg0VEB0Fd4H85okczOYibOA6856ntDA31JFaOxbr9tVuV86Z4bCNBguuCbgX3lX8CUzB1xqlJAe2bLqAXprKpVogb_ni7hiwtR2YOTlppcYAmZ8lJOFCuy4e3HLV9LYbmsN0jPaV6P8SGhro0bhbtWJSl5TgiK-Y9i7aJf7lFpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SoOV9FP0xbzuaU4lJuOXXQM1D9JfAe2UrnPJgsBX-Q15tpOYLVZlS_53AG5McwucjWYxcnUQnHscspQwWVVx3zdtEsmHtewBWzzDfImIt97R8FO10uwS7g_E5il6yPg7aGxzmmBiKhwj6j5k7rp7I3iu5S39gbuxmtBArufgjFAbu0Req8Ilc2jvs0kLDjGPQco6fkjG2-YUgLoBotRWATLZX38YgjgGZN8A8RnlVGLQawT7cs475vePdR5fDoGExP4SZKh5XWD4e5rY7eTjQWjjuP021PufHCc8hYNo2YZ-QsVf803Eh0dgKoTdjEm5Oqvk-Kq2xNYmDiOcy6x8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEpFZjeZplnO4B5P_2j8zoFwfQ81NyxK-eOkYRylNtGDYdrbLVpmzjQ-TBPSe5pnEVtPevt-Xnvl6MRHeHQ7xQwgEQSfG1pW6KR-E4bUhwcueeQEONCpZxD7Y81C00oq1VwSQ3PWaIu7M16ymcDVF38gK-AgzC468v4jM_qrxFaEZOF98G_UMgkYqKhlKFGih8pGks6IUw42xgx7sgWhjE7V_H8u2U_aKxdrcyYhTvTkFdURUDiKwqaxvuq5oovd8aLghZ2MZVScsSrQeH6zfWasBmXVe-e6Xr39eeFuy4FIo4s6rCtl8p1A_NPiJMd9Fq6PMIghDWFij5OM6GZwCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nu60ZUSIWmR_3zICfQBL0sLD5_SrK7is64Up_5KV1PIjiGeRSYM_wT_qF77bmZ1En0YfpiObnql2Nv6KbkscCqcLPsV5TidCQEEpa8aFzWYNrvsEwh94Rr-uVG941OVoGJJ-zp0jYhS7FVbp6SMyG28sM0dG-ccUQlnG-IN32Mj_uNXjhe9xnDHD48yctkmPVBhKgIG1wTOybDbEEo2O27LJIO8LMvXJe7khtnpcsgmxxNUttKe7F2_XHBrMhTKJS6TkUqyvoiTqPoz18otDI7wmINadSiTxF-D1BpDKD2qu4Nb9Cz3I9WZ8LYF0G5BjkhP6xoO5rs2Qzr2UaVfF3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFyZFCa2tj_XOIFZteJCi9TYD8VQ977L1b8lmzjGn4ZvRFY4xfcVzGUhSrYg_OU7nn4f32_3vxpV8I_KVS8fXBu6DwkVu39YHJerPrehS8fRogpjB8k7gf-kKOfXAeQZauxJbJ1to4McMkaV4JftzlDmbdpokxIRcepy3UZgPog6gOqZWCFhzqCuWZgYrxrB7Z2JoHQK3cs6RXWZLy8VtCWFiTzgxmpxIG-593VMMkLpy1KUHEdH8hbaXAftIMAc_J6yTw3QgQNoS6Lo4aqCWJfwINpyLXfgFEeC56rFTOdBEJMW7yuZcKR2E-nzE0AYHv_KF9HmkVgGEydVygpGDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8fPZ7M0qQX1Lhgm94RSRlWpRkwAGbpX98p4fhCyY2M520hJjDSIEyz-Y4Hgn0ubp5nAppTnGSsswAV7HnFwkyhk4ajuITQkULre4l2ZN-_j8ASFv3-HQVEkZllZBwl1MYIXmfTx6igmwEb6R68nqR5zJAAfGSgdGq_B6Od0YS_YF2wSo0WvEyBM1oc-Z2XJ1WI2PHRfXNnoGnMmz9SDHAwIPkIdIc02ahWucCVyB1u2heyqiwTwkgz3SS5hvHbOwlgbLpa0x3DhD-uhe_BrFjbSS3ehhwv-WmH27ZJSajSLU5zfBjIIPYJaSSS1WR10F1B4vJORdhOpcUnFRj5xDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItmrOGnaqrF8QLy9TKEX2siQo9xNx7yTLHbROS4WAref2OOMWbNW_RMcUR74TktfY51oBexOLrLBTW_tx3w5W1AA2aG-l1vYi4H8MWGTQYOZopu7o_yagsLYarJMqA40iD50iqTBd5cizl1LU_56V9hVNubY4v0aC7wL4F6IdpfzKdnpp889qS7ApDslQ9ZCy004tVn2OA_Z_Eia_hXriPzVgOYeNH1VB3iM78D3whgk3JEhApXfSTXYN2dNOT9l7q0cDCJsyqKbbk4e2tRuvoEkNAN24ySmQ6yqsUS2ZBF-Vw50iffyM10vbMeXKih6C4fGkLvkxoz8VSxSngPU2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSUiIfvJvsbEtvGhEP2ppkWMpZ1rsz-KXDV6FQHFV3pRAd5_hO5HQPyRdieHcVW6QTgmvL3CgNcRS3dgnEMcsiE4S1R8CCAyQ6_h-Z-a-ZAKhRsJgp2Zsw_Uf33DP8hRhIP4QCOZTweK06j9m8jexonoZdcbyneYVZ8qsht0etAki2yD4v5vmIEX3tSDVhsv9raJDSaB8lK6EgGsvPfDTyIDLmOy7jHEfX_E-nEhP8_nDBNfYcHe0emQuQLKnsOuxvmvIiHXC40a5jct-sTsOs_F7KX_8iH0cpMX043kW7F3lRGHlREQiBuvHTRl56BeoeUhF_NUnmBdvJARsrP35A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4NrKKULaJQWuQ8LKKIuhfm5ViTWAJyYe8Y_uCap3z70wLwA3hTbC6r7RSbU4ZXbPAnIDMDMYj7SWPGNFtxf1QShUUx50JC1M35yEzDVGXQjA3ZXDANpb5TVHJiyDI8AcL07krKskysrHj2SojeIjjWh25VlpWyAgvk_D8BoWfanQt2Er0mpwy55BbQDLt7-lJUPAIHtiqVEp8m9trX1GioEQh-RJI20Vdnn_EFTsosLutWdmyoenEEWIDbqY4nTCT7B-XBkQKc2jGoLzE-iTU4cqDtZ0eBeN3imfCl04oDFa6lZbSkJDA9afkkeMx6WPM4rXwiAF7Uu1d0fKrAJlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cj0mkRrhK_WFIL7YEJiY6xoJqeEXHVBTPrheoxnzT6pzlB9wMkVESn8KDZTbR2JJdg_TfW8TyO_othYokD0XqkPHnZXaamjX1NNeXsA-c3wR2AQnNKkvWDzr56MqpAHAGqXFdM9aKTiEVrZKnUNLceq-fW_LIkLQ1Zla0bvKAd8OlhsoazIVEJ_eXyS07k2KsEatc_Oa1zWxsN5Y8RWbSi6cv0_G4DZmADTtpKYBuKCO6Q652K3pWBQt8haC0KvAyfzgUzNhJApg3S1lF8Q2OdcqzfNNwtC7qNIhZo8ilbSyhOgtmiOrwbcN3Kz9KYp1annQxLfLwRkuS9PKV0PA8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u3Wnnl-F8xvK5RLMYhF8qo4lUSjFybCJPDACeQOIs5ZRQySC2p-JtJFYUz2FtbPWX0hq9bj7fTYVe3RwYh78CaDcD7xIyba69tAtrUTI_9dL0CWmh_S0lqyJ-OofQsOu3SvWiFanb6J3x0_TjVzfdSOtZ9k6R1uAcUdpDkbhTnJH36SwE2Utmxs5_HXVyrSELjtU6JTnovLL5S2Ei6GzciZNiuVduVFzt1jbbYx035HJqFoTyu6MgJjs1OTPV0WiLnqIlyWA3O8vAbY4LqnYBSZDBK_3eW6pjkcz-iy5e-lseBUmykK80qqiCKgVek4rNCS-6ARCM72-twfzcycR8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qpgLl3lmoh6a0C8ld6GNE_I9RpWTiNtwnXXGJdUlmluVE6-5R6tTVKFwQnq3zpUxVtjfaybP1Q3X9njuU-8y1d2jmr-P--413zhdOQd4RsfwpXHgSu5HUd4yStvQSmPyHvWjIDWS_RIUGCMzIdjJGSOi81LtcbuFr2o2vWY5kIbLRcm6swkoCmnmN40RlsQbkQTnNVLJaBmbguoA9MtMqK-MK5nccEP_K7-QZvmKQI_3XDMd3sFLzE4NXMlTsBkH9JG5EkfUdswA2t9ASeOFTDv-vudf9owQnFiN6ShmOnmkwypbRDG8RULEakR0ZZ4HcmIWqzezXDmXFU9AZDQ-Gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hk1yaI4V5-HEfcb1DyWFWhSZleJQoKbqrN_zBRzLlKirX0ioxXYVHzuhVv5DlHwLNOBMbJ8lN6yuL9bwiK6e0HYItqK7coJc8F5ywaGXAcJe20DzZLV7o3_7U9Uj_1UUUMsc9wlYwLqCqh0wH5m8vaI56d2dJVBhEg8pR5ZyCmv5tAzNwnOLVv85eNEvkrLp54OSv-x9NnV0A-K8NvlssT9gn3verQVmm4msgIbGdWX4zZ9V10XCwCXId2-FzNWMsKTSywzmNcJGcT4MrfWIp6yrS-bHNmRrmTDLIRYOiHnc_EY5T-vxZwWhjle_gIW3t3OX5XFbRPx8D1Gu5yD1aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXZ7baxRGOExeyNF7ONSqE2e6WlRlIopI7nhSqvbKlQNciTrMgKxJzbHPSlqI91q39ixum2bX3aD-EOocERpDzHQCeKEkzZSzjxqqLdVRMFFFTYCpCSBYotAkwYTepo-WozUEgHAhRmrUprr-IPlcQG_S-eLBNq8jcVmHMXIumTWHxjCIhkPA7_e7wHgvyW3l6dOwleWe530g2rhIXx_G_RV0uu4GKEPDgHq57ntcz26h4dvBtoOIoWspTN9TCPd80sFjaSAcgN3KCXkjtgXx7iv0yqlGRvSN9TyUqmfsz_Xe7i1hNadrbo0_KwixnlDYaPafFsLxYpEd26QSV3PqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsYGZF7fWWThmjRS6MgluvZsq9fK1uVUL2rC5IgA465EOiAEBEkDYEHXPlhgooUuy4-kR2fo8X5Ds9RGTuiupftuzzDIEXmI9B9yjoHxZtIXTh_ngBkZjOc-Mdj6YhfURnjkauMfBBXVnXhDuhDMVvclINb9oaYm6magODOKrJHXPmR_0gPawd9bxn7IJxQ5a8TzgnapYnoMYbrXJGyG5cJl7gldZOCfSUqBbdL2zNalIq9s5d6TfFZpaBzjLcogxAGFqlXeioSUmNSElxpfyHt_Cws2kOenE4REGHdgSidtS4imowoeCWOlm3-3bAGvp3AnrfnJJGIBpZXNXDkYSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKhdy9b_q988lWDoEKDpb2wPaTdqXbQYCbCU42XmHjZnoAJQ6Ahj6OcgEP9ddnPkGfIBnQdgiWbTUEq4H5ljt5PjNB04f0ARi0l3-ADd5ZrXolNEQX93dCF01MYMnNszyTpcBYalajtet90BeDVNSe9tNU92ZUFrdxrrERxbP6SlIZ5QcejZaSK5CJsb12iAAs7oPIV5EstNrIg6NBWPt3wXb4rr6UZFZ-FBkSGGG9pUHRYL9XTlttR907ykU58-fRD97p8ZpCN-LYiL-1Zxv4x9Y1HU__QcrQfeeYjHex67VlPklnzLM58LasNx71VzRL7zZxt40tgs3pdzlrvkwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lUSWHfIxkl429nOoP9EW-MSBzuSqYm6e0jx3T6t6I9jFaJMEigj3Mso-NMZpyTKg-BnF7ououqQtJmWeDuQvPxXUQXrwgaYl7EHpklBVQ2JVnaq9NX-VhIDhTCPWx5_6c_WUjrQiVrTcTcGsv0ALV3V3-VsVF51og1nwALkbXDU4HNOz5kzPqAYM2dP625fnkgPJxAfF2Qtc_FItj6-9joxEa6GHkH6q1BJ5Oj9Lx3UbWvMotsEfryufnYrvRHYQcFSjNzsNsjeIdjduxSrLXc8xCMDvsHVogRmL8OQuv8N4GUWqT5FZcmfeXKQYpr6kN4EaPlR3iU0qcFB1KWXUDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHFPPAQ4e_rQfvMeK9qBMu4v6jVIzMkk3oPUhNmiMkEYRf_7iHe3RZHR_WUdcbKVWicElHNNM3t75WKe5rmPNGFaJK6X9qtSJz8tK3zYsJxEjRfZ5Xi_FOg7iUPVmEECd_zkMAdybf7xU8Byh14-0GhXMI0-JcG1DBciiF_kWaXoXw3ClrX4gRl6on2E3dTCqjiYLko6kd3S5DcezgFuFhmG2mNpFqHOyyGfihYu1DJhq_6OlasLh0Xql0-vITcIiDb6l-DnlyR-F6ZsyH2Savzx6Si8KZJ1_6e0dw9pKB14FFqfxaMrbcdgmfFRKjuG-CzebjSz2dCEMuCIu2i5eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TycIwap1PQtBBl7nlwQMNZHTDxyDmkvdFf5tT_KJEp0VBLR6ogmsN_qkg1VyUa9Dc7SoZQdQ-vjggnbsa3nylmQDvEKvUXEY4hFmuP6PUFxeGjSg4wbmMYYS4AMEaNtahmZjwm-YNmPXjUjqeTvQrpr65eUq4nEJnxClv1k2l7wlWayfUhFCcD0M8gBukehhLRlweocxwBmzjY8Jl7Va8VCTB39cIPZqUaOVPiNhDlHY5eP3QQIv4Ec4Dzp11vXqYYw4OG0yZEif4AGcJlI2bugCVY8FsrYH2JmAR6DqMqOaGKwbn2aj_lWpTQMGspwb311p1j_cio05MnjmbKWq_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2ESrSUkXE2hfrHLmjZ2pSsETE-GHQgSbAWlWOF9ZSgrUolckuS8RBzsx30vSTVofCUgn-EDDzSKB9IWdnsGWZBswGDgUHIIKmHPNHNVL1l6x4Fv_AycwfEZ7CpTg-lU-sJLvh0vvqmxj3Df1M2qLdqp5RduHDltFfSThK6cEuQ-8aSJMRO1AOZzavAODnpN4T5k4PPder3bN7lChSqK-yuiJo2O0b4KB_hh4Ppnh2XBgy9aD4H8WHVRN0vbfXkwPxhiVlpuQhlY5ZBvrxmivJtbzfHg9VQYXPV03BD0KE_bN-2VkvKLEOZxRrZHT29_AUFZzEIKIRh87XZitFAQZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWiD0H7pcktHrSYqEAWpZBpC0gjdn9K4Wze6GVgzGbsW-g8MfBN3pm4Q5JYYDEO5LXb3szJYC5Wi8vcsPdPo9onG0jFFiW48oyPFQUK_1BJsFZKtKWiT6qUXTujUVq109-xDhPK9Gl8FCyuwLhsE8kqZGkEVn9zX-vAFG151n4YRUTLM_S6vraSmhVA3mFUrdsX6sLTW1JR0bV1E--9KvASruJ-KWJ_OXOutmHT16leQqmWM0rAUplXj4WSHb2YLcgnRWUfpU2XKLWNv3dLg1z_yBrII196NFraxJHDgv3MG-gzaRfo3RFRy3j4wd-yQI0o7mj3R5NgqnyHETs1qTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IEnwrN_oWkhm0RF0ESqX-75hwiTHACmgvD80XSQL-LPA0U2tno3ITNGhVvBHfxXuiUDxGZw2vu-doiia54H0FVU9-1eOg4e7ybXr5XugR4y3U0MYRFg5z2QRAOVSy3cAcg8oTDAQRmWLEoF0JGFBXTQAc0jgkBf4bkx1FOvFO00ObS0t-7YCZViX2Ll3SZaahp1iU08HDTTFRx-B0-oUk1A8DO23a2fTXDMBPpxwIPwVoXeyg7W59uZFq-nca26AKo1f4hU36y78hbJWDzjo0psP4JetvkWKoRgfAUj-D9tp92RyMCybByHh6VT8eAQT5c70fYZRhw2caML7moY_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/So_KLdeQW0rziWxLgr1JFMAK2cekVfugFM_rY91Z43qKzXdsB28H3S3xI_larFTKBDKsh1wjgUhv9yH8bnlIJr5bFuZIDw7C4Q6-5PcVi1e62FpUadJywAaPHIBMES-xAtP9Oqz5S-sTFSm_BfYruopNhiJb_khxvCGj-V5JTXxl_faj4Vm6EvWuqrwQsiD48yW02clvCoBJmOm8CjSseh-K9TuxnSghOyx-SO3NeD_fFS0jinrFHtwBaowYpGPykIL_uvNy4nwxK3Qi13vzkOD-M5sN_HhbaipQx79dCq13b05T4qkJ6dJOXhL5j_oCGCobohLbJJAePNhNC9LTUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnXcZmKa3SbOr79tJUbORD1x2UnFp6PAFwzfI995YiDVdfC0keoXf4cjZz4L5e8PE1ZXBx53LB9kFjk8FkehHlcbVIZ1C6iY5yQ3MCqIQQ_68WJUEZqx7ON17WrZulsVyrunbbXizOiYKygAfjMJrD-IV95CyJ0f9m3GKFEE5-nStEbZ4ukNU4DesferCWQVcqB0oGcFHYuhoVuAC3t8g6PaapH801jRLFwNgLISyjgIBSYUT4WhaZy3XuAAl5l7YBJiui4PlOAAZdCKKDS3swJJ3YR_0Z7MFaXd8DiLmpLIjfWQaGeGkNpt1C7vU959GHAWscWNrwozpBdhR1_kXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlmixBdDSqKcnyD2JmItKwK1HL1kbBIKXfkd561-aXJCF1nO1vHtCisVxrMIyfD6K1MyzrSToBvPKR_aQFGlYT-qkbLmTnvKnFF2sHoqAmzs-H5Q9DduoHgIjB13s0qaC5-TAmhsSx5BJtbcwDU6S-rG2lvCt7KuDPFK-CBnfd37s1es9xohJxhV9eghWgEXvpmb4LOdIDn5D8EaGY7uQU8TCtHqst5osboxtRo-f4LsTVWBAhKChJHvhgdh1EmErmiWSHUt23BcAWmgNFMnlQOOCEvxWLlis0BSSo6GruP6LX_cuMXsekBo0kZ-2nq0sKZX-DVVG0irij2sAY5qeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZUGVN7LmsCKefU8s3AOeTRjKlnZ4Gvuxu5vvykIHGUXBcnnm440Eco2TulyiyyFkTF3LZFz7BQ8ht5VCj9nVwbbcN_N0PB2NKd3ie-hu-3Qc3A1_WOZDMbSHwRH1JTYdMD8yuJKCp4YjAJPnDFI_HPyRJ_FyPbDASe5skKLGsAoi35hvpbtpx9Y9kyy8BE5Z01wQeZqkg9SUF1MdF7jF5zZygww9W9I8fBc07kexD73oK7PkcmHBG1U8g5GesdPqqT1SYtTtjfGjlzIYNekyiQrDCWEPTNVsiwVWRjIbxAvS4dRHrnu7xS9HVNcP32dmof5TmkrEO1aGM9H7AFTlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJ4YmJKU1iGcNpfAoCploqEtsFPrVe_pvpqKaucS1PqWUug1_Q9e0MRvKKEryiSww8IEu62f9tGCjC34Ra0FfYnLMgGtB_bR-QqPC0KXXgHlWc4iqtIVHX_XWSmRaqszJNva1iqgWKB44_gl246tnVJD541okuvWfWyF_TGY6H7v_ZuJIeZsiS8CYfoYGEkWGwLXR-oIJg-A5czeQtLyUFbqmRT76MTtQfFExAoZ8YA3ddVDCj-4RW-Sc904UYKXBeyQ7OvKa826oyP14OlUcBkU38oKUydAbek52URT5HFgRDpBirU-xEcpFYJjjKuUxk8xFgJoqnz9qF7MauqclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FGY70sK-w-_mUEQT0SIRP62UCFZAdARXYixUIpLeYWWW78AiFfUSwyDqmiDREkZrQfl2hn3JpLegIcPtrB_tZ68tkym-sZCJx4JOHoRz2FbFE63v3ytbKfEqeHpdo7PxnHbgiZ9obWfshPLYfY87-V10Gx8HndIrV8BOreSYABp4dx2q3hw6FKpC2xGJ0ApNcxB5K2MviSrEBIacAR6UcwRaDW5Ol66cDX0yHxBCOhlBkpeiXLYwCPMkwH2KVV03KsAGlrHcxVll1hazks02InL2rP_KlENa6wA1BF8-1_bH4_G-WT64x4K7wtyy70GrB1O2LTvuFxrftjjo-x-oug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8FJH7XUpCHRtJ5lgoOFPCkNy3vNf3-xnzUtiPdjC6h3BUrtr5u-eEUem9WuxQ0OmTllcWypzT332R8HtJQQASs7-RvsArgpDppMHUMbl66H64M5_1Xg_vYzKqTfL9ZN5qVCrBEpnRnhihyDCjMEwoLRLHirHjGekmUp99bkbQda2NBuI62_armvGlHbGetTxi1TI_1c0K6tokiNs4BfGq9SWFl2LR8Uon2ubbQznDlfy23FUm71lSjPV5euAYo_k8X4m22LHzbQVZFhOa8n4aZXlK8KsV2oYgUIoBD5OuufPPwaHLIMs3KgwDiL3u5P2RUiq2e74bVK8omuYswUTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmoRn7-DUXGXS81UN7-tEdP54IuVAhoA5-24H9ws5k_L9S2fsf3exclS7wDX0YoM_mfbIo7_zS5KvCN_2rB-WwmbVcp6UTd6aaKXtXli5OMNdaIjFM4ldZ5ZRXrqsXuhZxd94t690YD53t8v81sPCLRVGtheMKnJ1lMTYAsYlVn3gfXb2e_wJw3EO4nAlyhIaRmb9wcdNivJL0nuAmRZZial8Xc1OL9Z_Dflw9hMPwtln7X4HCjLQkv3d33BHCDzZ7KL3rdNSrGmQSN0BfVGrfeGWSnBG8uNHb9JWoTKaI7LxyMMygJilckDaTR_LAnyJXYz1Xg5yEqLNOmhVcg3Lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwtPCUdYZMxIBOrKMMswIYR-sDS8zkmyHyA-heEqNaupzz-sR3ztDaBm8Etlsdet2N-c5iV33IPk3KPXG_1Mn6qlyJFYlvVbwhNgJgI9cLx-hRBAPMpA7DxG_iCGirNmeRqSMBmgOkiaPKVD-gJL6Z7qqpkox0xSEU-zWC8rIaUc3QYL69LGI8sPXZTJ0OvUMXP93xBv7AqFg9aViNMQyHJElvPNKTdYU4FNLjol3Dvh0nu_Jyrv1Vs3gs31x-hwuKwxBL9qxdp05YzsIvVD03z_iQtEk2Uy1SiwkG6LEB55wNvDUf4-TPLV2P74i32sdO49EBpydmWKozmT4uz7yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnwkQdXGLGk_0kOfeyAV8eL3f0IslGwLcX9QDVWaBiKFF0dOw5L6qn-K_OCkTPrsqDmdyP0Q6KMHdyeKpT25piyVFR7LOeLG0RaWf-wJGrdFhaMVuP8mw2-28ECHTRR7aqt_1g9kms06RAEKKg2eGLNQC3ZPmQMiBM-yY6eVQMYGq8B5nfGSg2HovuzAMQ7PfLdDszrau1iUx-BfblTlA92ICcXzdGl766xv5MzxFGoJ5dfnsRgV0vFMg3CNc7_T6yea-vAn80uMW5JE9_EoDSE5sptLcaFz8FquVXVqPJcUURZlNqZP8bpufeTJeFs9i50k3xXW0dR7-ed_t9kTyA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=ss8X68he7HerhSYHLddSUoUaQY88jfIXkvtc9mmNzh52qbgcW7JEuVSne1Dc5lq0IkF4yP985L1Vh9aYAkyanCGfYUfKT7htkQw02Clrjc_sli4ungZgzXUx9n6yfDjthMY0xCINqg542H_3K1banLOnis2lj2TUl7h-hrKDxhCYC7PchMUhDqJkFrG1M1LfYtzN-7gqJNPslS_ksVU8fJnDIALshd_O5282njl2K2JYu5iCG1ENi7Jk4w0A0VjNCdngR25b-vE6cSp7Xol584SRAa0JW5CnshlkHdS25T2wKg_uksDpMsfXgoL_8zf8jmw_n0eLYw-n7rSH-jf1YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=ss8X68he7HerhSYHLddSUoUaQY88jfIXkvtc9mmNzh52qbgcW7JEuVSne1Dc5lq0IkF4yP985L1Vh9aYAkyanCGfYUfKT7htkQw02Clrjc_sli4ungZgzXUx9n6yfDjthMY0xCINqg542H_3K1banLOnis2lj2TUl7h-hrKDxhCYC7PchMUhDqJkFrG1M1LfYtzN-7gqJNPslS_ksVU8fJnDIALshd_O5282njl2K2JYu5iCG1ENi7Jk4w0A0VjNCdngR25b-vE6cSp7Xol584SRAa0JW5CnshlkHdS25T2wKg_uksDpMsfXgoL_8zf8jmw_n0eLYw-n7rSH-jf1YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfvbYuvs5ek-DWsFSMYM31wsK0dIiWLrm6j4Evht1iLLYTojKbAWbmGHedf24K-jPuuMKTqH2zbQMaLauQpy64ZvwjqZyoiPoZ3jb9RhRTp0HN6bVJMGDQ1p-Qym9a6olbHtpz5vS7zeEJe7BWFkfpaUgHWVTVkVSulpn7gsSyUZF3umU6R4tEbpUX6QOKuk9xp52aGlCTfBGtbKTot8B9rux5PpKE7AcFeS9rey9njoQE76z06DhxQxp29qPdWNWzF6_zWVXUrm4ikqMpx7-CzWrQa72B7d8elRnOf_Nzb_yNfKUqw0--O3Tr0b_F5bbELBiYq9qDqgnktAdIufnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1NAdcCXPMNn_ajvC0YVUtcYdWQjcwgzVEO6APVQLiqmvnkgj8b8FoMou20vSReJ36Aq9Lm9uGQ6RCFhBWvMEZ3tP4W0nOPcuZD9Zz4K4D10A31EFuwyWxvSYedFC6pyahcntSsAxWwrXqHYfG0fk7zZyeihnn-uSw-WoEa_2f8IF12kDdQ0u5psW9Izo-6YGYgvJiwVYN7Kg0EnnYldrQs_QXTobyBWZB5kGXgBDKkUMPNsXfo76VO29iq9diEdl37uzeV3p8BS7AORs-lYECFf7ewUa7xJflyChCUQnPkVFEucvp6kX4Xup6qZjL8pXJOjs0ZgYv7kPTVGUf3yhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfHwl8r9zz6xYwUwgIldgD1jsW0lYGh2h1tnDzvNfBJuBjl9kVrEv_RLD_LGdlD3UmOaGQQaB_KprzT0mnJnCUTP0Jw_kCPwaMAII86A8qtFvzI0ii3H-DD0ipuwPUexOj1Ek8PNTOfViLvTilr838iEKSsfLRj0ZZd_dN3ZJZjggkFFAtkBgz-DTlEtxEPZyfPGryc1v4-ocf2_OvdFkfHPXNQClgTDjiD-ZSYdLazmVAIzIzj4J7IR4p1yLk_13fUJRNBlxQ6P-_3okvaTPZPZWAcUoBztmg9b-s2v3dSwRvTblat5KntnnwH4gxh9rXfS0TYNlUQ8fsBpoKaesw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/poYCyorx_iOkGyoamDBUyIh4V0vsDw_hA195ol0lnMLL-Wl3j8WgZnm2kjuCVWFCq9uhzU9NzIY8THATtT7B4sBoftdM9qg2696T3Y1w7VrfFsvoLgnWosl-cyVAZLzia7269kTuadgnYQJx0fuhByYDxv1tFrg1Bt3RJpGgBE1362Nr8wr-qFK9LR72SBrl0oDMZHUo3P2bxKlaCVpiCeEmuqX8MnYnikqZxKQtCkRAs9T2wh7hiLqAyezsCJ0h5MiI7KvMS53c58BU6ND040CsxGEeE_uXZ8_wbHmGbE9Zv0VsrIDO9IbP-jFyKG3i8lC0Scm-CqQKNDJYxMjzZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBDYHzjPYiHVysMYiL_Za4W7_4rHnrCdkJgo3ybXpZGCgfoBj5RpXbeAZeFgeYkC5Ec3aYcym33kEuHJ-csER8y0xE3_VFZwgSt94DhB_I0lkLnLtS3-c40Mv4qKiuIaDAgTjxXQL4-hsUObApqsHzrDRMO8_9FtyZHDYR258QWGjnniG8zxn7-dYy64yL3RY1IR0iLU3UCxjWbOFeEfSbRvV5N4RLm6tKJ_KDl0N6uEtop5VRi8vTddjaSY2YM2l0SSde2guRE-vft_IrhF9kFTDd0MDiR2_LOzdpS-wqO8InBSMaYpRWF338y12fgcHHpSDegdHuRQzzn2IVE2zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdCscVByxauWb_7BC66_uTTG9ogHetvW7CIl0Ws_WWYk_WCRya70YrKQqpwSRpMz_LbZeYBd2Wz9M0Dv_ydsy0fHEFGujiBDFVa3O0uqsBnVM3xHXV7PKcHzcL_QyQAJsKAUGRhz0OV2XoH1W4NzpWEu6gYLEQDCWJxucJglJpbnZPw_qfozuO8ogUoLlm31qd9_Uvspdq2g3837PKkgOqD87YFsPPSCvqgiVTW1wt21sgVlKjpneRj2Tbisju2QIjJBcsn_EYsIrsJjz438eGGZ-lCYRylTxcoVnnAWsAXdc82O0_o0WWuqtUdQtWUIEbc4xsAblBSIe9C5C62IpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DBuBce7KfObr9e_DGouWnqbwAxz-uZxSA8LCmakW7t-xxjI7eShqX-j0cU0IDimo0GOh54JSHP6kjFIO2w8hiGueEAVdXLv7KKLX_tMhhy7yZg-JJ7Weq-fu4p2Jfqvvk7j8V3x_RI_mtF-SqzLuE5Dmc878blsE4SJ52bh7Gdqp4z4JjG2bVuy4VMEwEsWFOiLiQ5hOg-Obe6s6-lj6BEQbsU6SetPfJzovi6Kj4lcORm--hF_Dabvlj7356zwJiawaXin0SuH1I0bpXtk8-5Ri-h7yThd2_DZxIi0TSTsx9UytBYPA91kh2ajLVyTh-EuXF00GU-6ylO0Cb3x2Cw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=TXeiwfAl-i9Y3PsQN5BCEITEE1vySDMX46wbTeTlU5O3lybEon0CrUN1yb7LuRDGPwhQON7la_8gHk_OK2tZOD-ys1CAMK2uay75XsLRGLtmTd1k8vA3E5jbeM1DPkx3i-jur28YtuX9ZxsAUxIYml4CuaWGzSK_GLu5cxg37h1lvPNQ5PHLMty4i-Mn2mobjnSJEyRV8yp5FwnzR_aTgfl_IuNCeMMQ_72vE9F3iAgC5c1DVtblK4fFAkdj4nnlYeYCG7MgLEOJglNhNw92qpdvBswXavMt_MVskGXzkZVGN5BUpYh8Y6mATF41fTzf_i8MQLQhQihZenxWMlJDPijLPVzd8bNKBQh-TMzsb5KQSP9XFTPOplSj_C5-DvLwIEPBQHWwXDJpc4eirG9M67WdapYfCcMLDf-9zvNv7XOBkoTQ_PaKY8WN5mRFtGV2orG1N4yX3S1Nb4SnGxt_5L72obbsWRiZhglPJI0h2GHkOqx8Ugtb-kHk8Z63Ce1ye17ib4s2IsrJOzu-f2q0PU5jOqplkPT3KaE7bkN4rqFlGVOctyrPGHzDQhUQe3Ai8JWFr23kSMJ3OsQLEzVl2_rUmBRRSmqxIzKupiMD6s0PXtmG7ps0uivT2IKfiR4ZnVVZfVjhk9Sfq5trFRjjQshym4rjZUxOZZVVfQU9Iyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=TXeiwfAl-i9Y3PsQN5BCEITEE1vySDMX46wbTeTlU5O3lybEon0CrUN1yb7LuRDGPwhQON7la_8gHk_OK2tZOD-ys1CAMK2uay75XsLRGLtmTd1k8vA3E5jbeM1DPkx3i-jur28YtuX9ZxsAUxIYml4CuaWGzSK_GLu5cxg37h1lvPNQ5PHLMty4i-Mn2mobjnSJEyRV8yp5FwnzR_aTgfl_IuNCeMMQ_72vE9F3iAgC5c1DVtblK4fFAkdj4nnlYeYCG7MgLEOJglNhNw92qpdvBswXavMt_MVskGXzkZVGN5BUpYh8Y6mATF41fTzf_i8MQLQhQihZenxWMlJDPijLPVzd8bNKBQh-TMzsb5KQSP9XFTPOplSj_C5-DvLwIEPBQHWwXDJpc4eirG9M67WdapYfCcMLDf-9zvNv7XOBkoTQ_PaKY8WN5mRFtGV2orG1N4yX3S1Nb4SnGxt_5L72obbsWRiZhglPJI0h2GHkOqx8Ugtb-kHk8Z63Ce1ye17ib4s2IsrJOzu-f2q0PU5jOqplkPT3KaE7bkN4rqFlGVOctyrPGHzDQhUQe3Ai8JWFr23kSMJ3OsQLEzVl2_rUmBRRSmqxIzKupiMD6s0PXtmG7ps0uivT2IKfiR4ZnVVZfVjhk9Sfq5trFRjjQshym4rjZUxOZZVVfQU9Iyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iAHKmev2YOmxnQATJ8tBTZlJB3ua7bzTzvoOAjWko4IahMNvo7EBE1AYPn9PBD6tWEISYgmzjqEqSLoD-kjmvkGLWaZON-Hh5EyxwlbFrjpMsNiOO_yNQ1sQeIuGLyuEu9J4BWrDHJT4H4uYdVUeWpKCJ3P9TSCHTVBz5ADDQIYRTDD8lP2WLPx4mCglDXAdQ7wFFpO1POa0uMM8moLDycfYycqNc3ftsWYcQb8b4pBZybLDKYddi_evpnJQC_T4oCHL3bm1QsaUfCjWkbvelaQgsL0Ek-IYeNTUL6YeQ5PIQXA6NBaeexXiktw204DIOm0awWpj9QN2l-pxyJdZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M1aVRKUl_zwyfg3Y-u4fraWPbyZ5dKLA2bEWnMjJSSCgP7SoDLjnv7WE_y5wkMV0hMdUfjmwKWSgvKz5GKJDHP0E40XUA7ZAnAZ0XdhqKcu7xYALoiJMIkceL0kd1KsfpkLbMu3dKUtWVwDc7e_5YjIkVW7ZFfjk9kfNrTkwWaIMf81kq0PanLl9qcFz3TdcA5KexNzzicqQb4ilRA3dB_J6fzthm-BwrESBtrEK67zYRgS9uYYaDnmzYitEbFRRVMANB4F2oPlWGqwuwDRtanQ-wWaSeP0NeuAvz51QiBtu_87sq3gGG7TeioIG-S0IsrRGfOm-JhwKfUVdN_CvYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cAVjCS9Lw6jVkM3QEXyFw8xeOLDOa9xID65vGg296S7XpZLUWemkaSX9V_EGErn72Iybxx8Wi_UtWS7RflZFYI50IcJew-O1sHwHpfzaXYl3fVuGSVL8NXIH7oNhHPTmFa-5603vVj6qVM08eCLyQKM-tK0wfXJdQZjpscDNI0cS7O5GSMIydFA49AaJRABVV5TAdQ56fbK5t3bLgiPSmq02i-rGvRgNOYItxjFC4wOj-wDBCaIafaHSWsSv9uXkmLqJWQ_06cVeYGAQEJX27nMA74jUmaJziStuMuVGMT1wHMYTJRa5Npgg6HVvVlhta7WzDcWqfGhUN5WmTb438w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OjcNei_hjoJ2qBeQWxDHqqoGt4WvQ6sVHYzXijjP0GrPA90JWhHq77NjUa9UYJR-__0Ja0oFpHDZywEWPXJ7D95NFlnA5XYZfDCeJQcrQKCeRT2_AeCfWeNlhsoEf-vGuxgBYySbn34VMesUws-ZT_GoCUwoS1dNCR1OUpB78hDmiMSpHxa4IZqCH8tTJA-5pOn6pOyzT-XJEyQFEjBUYtnKilqtN0HHjucmqBLfo_xJPAXAdQpTjt9hxpBCS0aGAUaBWO4SqX1eayGsRugr7uChBsWI5DqL_cW9vOBGsLUrqZdwHrSJCHLxodY8Vr7PaOzn1rp1TI5MsF6CaiTGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RGjrpvrQFHEJ-b5sOHAHZLu_EXJNVzxg8cdGjHgB7-t3JpprzcTtcMP-0yshtxInGGF4n5vFhtgXr1lBO3VG_D7mpnwwRLshOx1LlgyEihx4C2uG8ka0tNgnuatIb0CvC27OcM4y5fu084RHSPZx46Dvn4S1zdqPeUWmef4XIFwl6R6nebrKxOE5Yot2bMq-IFauGUCGYyspkQkCpycmy-88ZDWlEk3XarnoNwvGqc833ZvAfBf3dOEnwO-sZc4PmMbS8Rysq_1qT17dN4NBNWv5vy-e6vraH_lDxJll6KcFq6qUc2COugc5wUxrnSDNpSxGZIefH_ag1rALT0Yonw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0WYycGMR5OLzCvzrc2IPhQU0w668N9PPnc9PlQJt_Rmb_FzThXEg0B8DgeTPVXNkEuVca7gAa8QabyIJqaH3Q0ZjInSp6JCLbNnyFcp7LPtuSEMLoVPPgbt2h8WHpvqxnwVonmFmQvV6-eDLcvwObjsHcsgXY_l-SkZ5qucOBLAxMb4UP1RM4C5PfsOjXCqSfgjEBlNOz_DCgbnxKVGrFWWt7qjtc0VoTEPTv6v0ZxtWAJcMGh4sHos6-88xdCPuIKIhz7ZP7Q2vuG7UlGiMaHty6eMOK54cMKJ_88QR6WNPY-dypaaR9UGFksHZNVo6znQOTOsK2B7_GwWe34dXixk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0WYycGMR5OLzCvzrc2IPhQU0w668N9PPnc9PlQJt_Rmb_FzThXEg0B8DgeTPVXNkEuVca7gAa8QabyIJqaH3Q0ZjInSp6JCLbNnyFcp7LPtuSEMLoVPPgbt2h8WHpvqxnwVonmFmQvV6-eDLcvwObjsHcsgXY_l-SkZ5qucOBLAxMb4UP1RM4C5PfsOjXCqSfgjEBlNOz_DCgbnxKVGrFWWt7qjtc0VoTEPTv6v0ZxtWAJcMGh4sHos6-88xdCPuIKIhz7ZP7Q2vuG7UlGiMaHty6eMOK54cMKJ_88QR6WNPY-dypaaR9UGFksHZNVo6znQOTOsK2B7_GwWe34dXixk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUoG0ayEKIXgCsd3VsgfM2Bw2NEpVp72sJ-qheNiuFFApuLJim7NLCfo3MuP_bMAuK6OPx2Y8EenZFOShYBOVKIBYtWw4W5bO2Up9Hp7gJooQVNqd7HwkCTUbI7mBIxyb_0gZcLb__7yZo4xsgQUg6zvlLqvLO8WYSwrCxg76LUIY_vnJQTXEJoa-mCeTBoDzHr2f-dh1QLjn2-Gmo-wCQW-COXS5fgjSojSuUuBYead3XhAEG_-uCVak8oDcqUu8WOTGctmOYXAV4THrjKg6sjNrSIvUe2ufdkzA_nEn8e_TzRqCWTk9LnkN8fa-44uqFUIYD58GtZuABpnFGIDKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMbRXsS9Aae152iPsdpNCr2FckzisdjemVZ3Xcsn5emokAX-hhKENRvrjfjYi4gWfp1wxW7_Jup5BRcF5Zj5H6OLLtfUFWFJDrWNvRB4iH8JzoU-VuiIm4sCjfc2OPblT3VxnWxb1w1pWWw7PfUIg8wRyYPLMtpC2lA_nA3R5LAyNdN4CwGTfx7A9ULGT9l9AeUzcQS6rJemwSJ6lkpiJOt0Pe5JtVGqfyRloIY_yVYJTh5nFUuwT9JlyXjMzfjIH8Gu_BRzEY1stQFY5thbov-x8p4efiu5w2dskTXUcsixwbqCkfHWIWa3ADO3A8J6Onu2ruvnCtNKE1iVCoxurg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uONSHInisE7I_TH4z_dw87NtsLRvRJY2HgOvveErlIQftycldbIHwTh3FLQXMXF-XQrQ0uG1vhpG_ua33GTTKUtC2ItQzjQTXaBjnUlzdv-bh4K0YLpO13Strrz9ewFhSDuCkmXte69MVbQIZr55A-ky6R7XSp-5e7hd8KfXduRD_TTY3XkcmALIce0Z1wIY_IG8ZTT43I_ifi0bqVezaiyzGINRI5z9uTqy_sDPvzdS0qNvlOtOrcZz3OTPQV6LKEkvqRnw6G6OpK0FjB82GW2-2ycbWjQeQquyTMC91EgMoLDt6_xnH78Olib65cVT3yWjiMF56SyY82FNUK0jIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvdldtTZ9FAgDfquUCyBI6HOHGpI0TaITapfFeRyW2AAg9npJQA7ms16ceyIGwn-b-0wJd-UbZlwcVQrI2u-K3Se_LB58UnwKHyea38rcNRRAM52AlaYTUuFpgyiJKJIQ7UbuvBT8vn0sMMDvyTuA89bJNsGLYZ008eQHoL17fDdFvPKk9CG6HTNxEqLiTJxnee46ys0qd24I--xE9qLH9wPK4WmPK0O8vy9-sbP8qgDSPwxUqIQofdcl_QkBtYl_nun6ZFeriGKKYrU1T1ftupwSUf3-uzkyrNSm1JDbHDt4ylwiMBDLBQu5TPtgp25G615ADMLXLLCh1UP6We8yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fODX6mIhtmi72rjWkX-Uc8plbmpHhBkxhLVwVmB9GzQkoJ5JqFHk5PzAdus2mO0Rk4NUCaeHKTBs19vF_GDbf-J0K8KpCjzksfu1HljjsK6fuO401nvyGtQItmhIh-Ueb_vWED-2mTsWz8pviQq5xDmlOuFOwvQPTTgn2qs2qEyvYeyp1PYVRon48apd-Djz5QdCN8ZApjljwuBPoitzr2K_gq9puRUNqRhqWWSfe4SaFwV5jwFws3_I70-MNWPlszGrzMit3YlBqPtwtBy5v5XhvIyxaAKccFDXz6m-hd5fL-b80wqwV3B_PwtGDbM8NPginqu34JO3c1-YazxgrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R08X3eveCEgYGQH0eeL_njansZlD3Jiy4Lg2E8uknUqaRwjXPBZIMDsQb8-MR9jjeuoWqPizt6YwaHcvYWFjfqqGa6uCLrUW9nSpIzCT3Bm1PfkK8uxdXle80w90hLf3eFuynaBRgCfY5QbY4MX3nG7MRMckJht-GLYfrQT5c9GBkiLTKytxDvtAbuXl6gIPZZdIkjoHkAJzp36WQSchSBUz9P18D_zXVWxXqmEvp3rqhv9F5o0qFKJhNNTiL1p37QTfAjlWGHPjY9V7P42ShxUEFkby_-ezdQKD2qgAcn4AI04QPOdATkg7Zjf6SlTLhuGYva-qpyFIyZ-4XF-DEw.jpg" alt="photo" loading="lazy"/></div>
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
