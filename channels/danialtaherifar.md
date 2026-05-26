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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 01:19:54</div>
<hr>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 174 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 313 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pjo23T3WfQyJC4_Y0FsQyFDLsI4vcqkFJyxNYEz9Ky9cgjJqbai_LwtqjS1cUw5MYlgCQmRuJyPXCt95YGV9qaj9J8yeBib6-mxvcvlnFBD0_8au9DuO233fBc1-Gj6Qrg1Nm1MHvQzzfkpC2fU5vUKwN0cr1_slmyw5vmD8nUTVU4_E5qWye7sNW-rGzjVfd-0JgyCsxqhNTtR6WJnt3wQXo57sPkKVQukt0vuMW7OTKOmtyubjO2XXbk_UXp9BmVhn5ljwfVTle-cFWqfwzG9MVXzg4B2RKvKw9u9e7TS7NjpVCVf9C8OXWM4dH_HDoIkQx1G69tVlMvBQnP6HXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 407 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 752 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJuyrNgW8fxxjYgFzPlovu2IQBBwC1oRdKh-Xat0MU39eINtfriJaHNDmDRpzDVXzrmKW5N39mwA90F6rmze3q7X0EMFXZCkHOZgP-Je8mdc31oC_4HTOqTuubzbXoKLWS83_yV1rcBulH5uwRtlRQaHCeGXGC7BP7fKPSvpQ975Sn6XMjMobNQjOCEzgeG4uOFVV0OTXuMndl_mMNXf4goIj2ie0XceGZwqFHVm_1rgD3x9kWCzDx9PiyYMWZGhbKSOuMgZGrMCh8Jqlj5onlrcu7ufOEENl7qsuDJo3bGSYh2VVkdrcyra3fYCrR62hlcKfELCxEk7H-CFprj2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 691 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 791 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hsxo16ccJbCmXLxAoNXCYX3nDNk9yFJY2UuBfa9MOy-_Kg8OwGpJK6BcSj8cy5kPV6JUvnd70BvJR7HXdvjCpWaW37dNpWjfFAVwyZ6JmeDjhAIoQkreXmRl5lteSn1QpKLe2d3JoRs7dhUWZWx4QYw1huT9zoc7gelfTiJi86XYV-nMJpTT-rWHNa_RjHna_bnMZhKRJsMMrNfq4sMgBtWJ5npjsxYan2KMYlc3zCNbsxr-8vS689hCCScKRTquIfOLkaJBS3PGAbRWvDRd6eCnm-uz-L9Tyw1bDonO-IgAKzx9jVnz1by-e06sKltrPfJhqc8jd9_sATYWXcsoyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 856 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 992 · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNl0H07k-xDmEHMsNisnUOQe3mVPcvJExT-uwz0HCDbx7frrAi48rhvJTy89ggzl2SOIxQ-T7PekYwEx1DP8XaMOdPxFIFDjzt7GdP8kh1Eppv5Hx5Eol4Up-lmULYeqmT3yu2L0z421aPkHEesWj5weUchQV1hhHAkvXRuC1LaN03gfC4QJ2BP7Q0hl2dhW7RpOJbYhVxbtIxnsi2BN80GxjrIDx5e9H5d9b04eVjVWlocE9lySTWGBQZ0TtB0FFFACxZ0VJ6vyY8fWIT7bJCkRoKboqDMmv5w1d7EhKdVaQi9EadAmDB2u5gbFj3JeuYm-PbObamKuzbj-nRO-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 813 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 824 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 753 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 930 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEcZJgNSG6XfZZbJttl9o6tBdO7BDMolXTuwwEYzl_ToQnyrW4sy1cX1L3B7qU1UGooEr-6C06gXEVZbnpyyR_5eoNxUbPxj-O8UHAi6TjdeViQ8E-JUN0ny6hFVROzBdwo-0jAawti1F_WT1kcUoXq41sS1nhPymUSRJrhzwvnSiglj40WSN2thJqp6anr8CHF6aSkmGbFMdh3Bb2rUUZZ544xDuRYdDpz3gQ_LayeixpI3I1jN0ofWZnn9niIBvWXlmo_YBctyuTmNe-YQr8ZP3bHc0YVrocTxO-5uG1RiglV-s9MmdbGz2ZjOD6yBIF_HrbytV67ZD9Iw7no2rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 981 · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
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
<div class="tg-footer">👁️ 930 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 809 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 653 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 868 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDB99zQ-2wMsiwMCr_9SVo8WmqtBdvmuVUyvHEqUOtZQtdi1U4-gBcMscsIQKsEySBVWZmG0a7Ic_EIIJgwU1EQT0iruLTEkKgUw2SKmJ3GVFYyglNAneylTapJzBQtSYOauKoPDgRN6NDjfNlLjFYHUC4-M9_hPLK3R9rpYSk93bDGGV5U_w2HeKgayLziXs_f2hnU4EwRqlmkVB1JjW65Mtmu1NVBPtgRzOgVP7wTyP-Tg1kymukjFwAUT87f1hWDCaueZIvT78q0gJngHYWBqQtL2qOYoOlKLPea0rPMx0zZWQ4R61jucZHt4g0jvpLFN5LGQjYbSXovblRqaYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 852 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXt01-AT65D94QBswy9rMyKl_uqXQKwran97CkT9tCYu8zVfsT42k-9jVV0i72fWdvvDIQce8LmJgJ2AksgK-vr_KhxAZ7Twtz2WiInH-lVngZ14i6_TsbNCJd2LNs3d8nI7BV1OjECKllE0osjE0vgQCFTWohWbRz4ruWiCtvW73TgxdS3fzoTJKWgLd5z1HSCq9BxBIGUoSnPOqCsSEk9lF1M63Mg10nPUHr9H7Jo_dmSJcF91HcHxIbz1X52zJvB32ES7oqxjcvBOBsNLwqtlPdyobTho3VN31jPLp7X5D99_61ACo97oeX4hkTO2uPTQiDfl9xSZDLtl1VkocA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 824 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7QEkYpLwuqevpSxRBRJdv4kdC30Oq0uH6c1iEwoRvXfyUm-aqStmoihJksfCLb6NBduM9xPJThaMejD26-PIxZmSb0mXpOgvh_TfPscxrUHEojcVwBkdA90wuFTnJt4h0Z5XEmXtcq-L2ZPhLkawLQaBbAXi51Tscks8x68hNcodVqZsYOWuis9-B1MyNVJZ822DCaXpB3yUOg6tN1psXf4iuv9HxAbYJhxbFDj97vxjzMosZDAnnSOtpr05k9UXUHmW3WfN2NJaKj6KqdgtfLBFcnV8ddtuE6aE-hrL1qE37gZb5XM6vBBcynN6nHQ3LYAuyIhbxUbkYb3-DD6kA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCSdr1zF2DyhJrJdL06IO2wP-6JjI6t4jAh5b0PJHYAd7wcOgFPnAowEUnbkk5ybv5cLV_vrybA5rvfeCE2LrRVWGK22N0xpY7Ip0bFF4LeLv1Cq_olONMWh6sZDBUnq4jlEwX3Nlvc9ma4wqkxKZePZWHOfLdANi7BdrU2evrFYGa-TawPiBrwaD60umsC6S94lHeH9sXvlb4ou29ZYderNPeX6k15TMZkBKcQN7e2zvoCM-CsnkjEnyGDqmFQ16hHsRSS_d4gBOiNCuOvq30krk-PiviFW8dwwuTXoDJWYAxMKIqPmmUFYTjpQjKo6zDxCVWbTDYYG9kz_EJckRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NanVNh52y_VFpjs5cRNoDjWW1j_-x81rZlCClkPEQIefQy4x-GBZLoaMLgQqqFDl4rZfH8z0wMETSQDQWxH6gxWIkwYW0Q4wbhVIN0PAfclBZQIrdxb-Zf5xbhSAkO6G6agkRo0AMcZxQJaviVjMiy5Tw6p6kzY8mIdCpHS-Dn-Y8tTbjVwxKvhAVFDEj1rscYZcinwEt5AqvdANbnlUHs066Y-BwalF3BUHkz9fBBJf4_0Iq67_UnpJGAeWSdB--QRBW8bD4rw9t8LepD8RX3rKvyTWfIn3Alex02pnbMlxuOo5t4YjD-efFiNUOkDOLEHNPE597lBKKM-Gna86Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4rTto9OPLROqUkzyESqI_rCV74z7L1cFznPNXb--_D_jKHFEjW9VZYAEXbbzhp-xDvDMbZzVB1Fdy5_lyujVNe_HpaiExD1dHZpF0bHUprDCQRKh7okYhkivNAOLMKj9Nua-jCnSzXJd1ok5KnaVTjr22_MOHjxvhR85ftWJMnnPaT3gCe7Pz9dOH1kl1UTyZbTPnvU33tyYorJCLOCJRZXOS7fmihxTCYrkkFx6j4_L6dbxbYkn_wkvF6g1JeiWIjT9sUBIbnTtC9GRcJci2kOs1_uSd9kFxSpE6T5DY7wmdq4HabT7hskzMrrBOWNYAIGSuSmMippXuhjTRAsJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1KAnooPqYxN35MSf_jwJDO-ItxnzbZpyDDS9XJs7SIPk20leTO4oi3I-fivTBVhSwTD4sAmTNvKraoQqYKnKDGEuizk4RFdYdtW7eCxeUxlh7wHyuDsSrlv0JryjQtP-SmB3pPQZifIB-XV_Bp97TE1mEkdavBexoLHNY57S0RmkuSiX0Tr2WN1cZUydctnDybbF5e-OtNiA25HsaKl3dST-E0EFhOiv1Tt60Z_MBWdIebpL5wgJZCd7IzPOe18GRbRFvhJRUM0mIkz2KCSbWEwexEnr_0utp3PAqFX61kappi15fF2c78vsuHDO0e0Um2xLov0QOg3IvaHzHOa_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ynj8ilg9BmU7ZSYhECPAl-Dj29RfcBCoHFQI3lW_KQUfo8rVBtvHEulzxhftuJrpgGIj05k2Q4sQ1QjVRa2q2CPaoP1bgMcis5ZIqSE6NCT9OqbEf8VsZ27Y5lssaI4IvRJRy3oRsGlH6Io9g2mTRseQlvwGTGlieeiqiqbMa0jHm2jYI241K3cJSjI11PgQlLUpx8G9UTEQNcYGrHqxcrFo3XkYrNRyC4QMHtx0rQwtt74adqPy4iy9PKTW58vqAIRTILxnP5Ps3HxqvKTEKe1NK_HQv10myABH8mKcIvaU18Fwh20q0nBuyU526h9uMM3LTxhv-DyqCeliMrHdiA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=EnuW8RbJSAYR47Ceq8qKdnIk1EjJrWzs207aMO18QaTOda1KdJFNDtYKCmxoYzcfhSiDDTIwCB24rCZEBxP1MhXquQHVoqoBkyWuM9Hna3x9r0y2Y-nbH9CjWHSldjV_y5RYau_B9rdQiFWzT9jO6gJJluS-E0--SXZ2l4jufay8pBgw_TqFYMHjgZ287jquJqP-k1BlE30PfvAYR0JsCm8pvQ4j7ggLmNzKsQJzYxGSTNcZcSlw6vn-NIaUAqXQzzayxOv2iL0WLxpOGOdspjXeklBJ2vl0-dBdkEwjYIm6uFSfXP1O-b4_vXZB4mZ29KzHvA3WowY2TzwptDICrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=EnuW8RbJSAYR47Ceq8qKdnIk1EjJrWzs207aMO18QaTOda1KdJFNDtYKCmxoYzcfhSiDDTIwCB24rCZEBxP1MhXquQHVoqoBkyWuM9Hna3x9r0y2Y-nbH9CjWHSldjV_y5RYau_B9rdQiFWzT9jO6gJJluS-E0--SXZ2l4jufay8pBgw_TqFYMHjgZ287jquJqP-k1BlE30PfvAYR0JsCm8pvQ4j7ggLmNzKsQJzYxGSTNcZcSlw6vn-NIaUAqXQzzayxOv2iL0WLxpOGOdspjXeklBJ2vl0-dBdkEwjYIm6uFSfXP1O-b4_vXZB4mZ29KzHvA3WowY2TzwptDICrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLr2PTDCPdCJYLTZoxp00-RjeVqZq8aoOsczfmUcHa0maPZ5O3S5Ztv5-mkzyN53tgkt331U0T9isJbVSIXVVUAvn7Byd_xaCPsZ24LVzcrHoMGwGT79biTHD8MQeyUHj5n4UBv8TKZG4HcjJhKlkkNm3Q5OEndkMvfQB9DlLYl7ZWAz0r0AnGVwWa-5NFvZYWUEwpvO4BfOaaPrmhCjChLsF6c5LHcEo_ZecYzJ0XcnDmrHK7wU4FQ7pPiO7p_ipnpv7HbooCdQvzr8z4K0l1-BexA4j1LkJDU4PyyB0Cv0gFXSrKgQw9mZ5tI0KtxbCRD-SR8fO4T3uXmJgdD__Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGfB8HG9WVrJDA0zDWwxWj_J9ofQZJjb4_bvZupQE8mBGuEPbND3tEYC9833vYv8b5qE7ebWhH8v-35CnhPnfkwqUo0DTRdzaKvQ0RlntNuWji0J63FH0A-7SAofS2GDf4Kzs7iwS3NknzY7eNq1Szbbv4mQCmcyRDH7M1JuYL1q-yDPSVF8ZgQ4NUuMwlpq_5ie96rxmGXBDD3-I2i7ranBtdICiXvaweLGLs5Faq1lz5gp4zfQWi1zlhQsKfo1QBctfCygAyuASxrOzrzim2DjQpT2fW67__RGnnicaGxtJYngiWR0VGJzLy9LseshpHQ204_eIXshJ0RchuCSZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4gAzYdRlys_xAiDRzsR5rkhY4KkY7IqCSmW0S-pNNbcLIo7GG_40oH3UpjhfuC-I5QNz995EAI4Qx7Z7_z14Hl0GLERXBdg7dNCwOSsRGeqEiOF3g44ZsJB8nQrC8wtm26EV632ygtQpXzjoEChtRz50qrDwQSsKw1CSTo_nqXszkqZlL0ZqT9ZAn0x1y9hSlpG1Jr6TQPFwrMgaDQK1W64ijJ88_Fj70pNmH9Hy19PULmLif3wJ9xNBBVPGQDfZsb_IliChAGKGDUIdVh4o3nictw16FDjxasc78TympwWa1lJKjJo1NFDLncYVzFw5Q-xpDlVQuhpaiGbbdjnPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJd5-uwIlV003u2UtQ6pOMfB6cXpyzt_8zaa83KE6AVp7wnAApXPvAhpypf1vqoHF_XbR6kPGesGGbwVd867-TNBofhEpi6l_z47jv2WS-NZg1Qhz1Vngk8RGGY1lHYcAJrWdBXVatZQTKy0GdR6SD4gG567EeMNlyo4wfY6RJtL-zEW2pR4BOX4poY0loMx1QcIUHGHXT6d8fbyvOdlujNmEkoOvtR2bUYWIheDxhlJ3OKvv-JsjqAcGVVy7S9XV9ZwcLaXj-B2-Ykahkk1RFJHRXsdJZfZIImrnPqkMqLOFMFFhCpZbPeuLETxXS2EnTDQgodYnEAxn2HmHUtfYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uR9rKkJT7OqxmhnSRBj8dpBJt-ipRfdh1nBCekU0WAfjnfTUUfQDHFMXM_g4t9ogdJN-tvp7W8HV75BpLwH3-I2CVLol-8L-thYbh1UflgFZu3QTyRYrs1itSi5-DtaX_rd6kQ-bsRuZRXv1BVHqgK7cq2sh5GAODGGbcmCzwTX1JuM0JXEK-tuorbzY4NRGNCxaLjWrb5BpaI-6Cf9qowGJxLGHAxMIqAWy6yO-UFZ27WrvGywJPfae-6le7wufZ0MHaX_rJ46co7srxB_9r6BAikBjiBqs7OHahdRGmfhkVijJCYVkVkRWHxiipbXTBRMiXPvDiCsVusDdyUFl1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAp-u-C6ocbVThvbCUqijSFxMkMsEXN_Jp-_uCjMqwpzzvW2rZISseh5Oq5aWv8Gt0qp_DxiiYmqDkr95SEUnHLfHoRxQ-O6qhZXJw6RnbTO2UfBd40--T3-IlXHi8MauIOEv6DTb-KZdvgHk6bmtPN3nKIZTxg8P0LGwgFFsI6F-95KrFJQAoUWV8enBPGDgQVgopsKMGUsrESNDJ_1vxRT9q1hFfIWR662v1M9TmT-MfTxT7n0ppW1_nw1lHzkZEvaE1Z3b55nCcyYMEFrOmY7EJ5rqJPeJdQD9Ci1kiAJnjswESW19n6DpCyd3LL3rVneBK6CUEBG43pnZIBNBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bn0p1DGVvNbI0xR9eb4sf51npvB_bRSIAaqZQNFqbQBefZWXQ6_ajYgV9U8KqiTC48KD9bxcWNdEhdFDrCFLa-la52m-eImy3OYNZTAJEemJOuxCtcAhr0TkiHVFgmbT8tuAELfrqCNlWXSGLZ30OyS-_CBRJbxkry7XKFEXkFicWzM_6hlNNXToWWDPxBRNuimjunkcUELTnfZKwYxx5NTAkBCMv6lJm2bXI1rkzM2NOndNhSRqzZJFXNZ_5HjgM6M9bKJzxYN4W2qdC5Ga4m17mO5Fhx2waj7zBJjE9lSFmRsZH-WkzqFCfLanm8OA3C3DpIMdOlDconERr5Pi3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SXBSXPUKS7f7qMum-LrWPqMhr2EovIcLcnPwUm3_-FQ7TjNQJNyaigwWx8Bnt9kTHHIXFIc7dV7gR-uSQYjFhNcDG_4ei_CTxDvDJ4Hk1-xo9Zmy6OqgQxDUEVP3sqEhqrjiybQyyP8g16sDsHReWIGAqLGv84anqzr5iHiNRSK11U7CB_Z_BOgf4XSSDBT_wCzkcs2UvqjxcQVr3rAgm-BMOJxMOUmT8aNUY7JmnyvZKENptjMBjKQ71U9c4qIHaZzdyNiHFcD8WPah7VyuPt2q754Xb-SqHQW_nXO2qzcrOuRpR_ZBFatLfgbZ-gZmZOPXM4-MdMb5mr-2g67YLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1ObOkiSlYqsV7G6kFFywHliWx0-Wocpk4iFSS_EFOjyIko-TiQgi508A99Ymve3bo0fkFjnEQT-RrNcizbGgUNgkv3UOBMI--yxQEozpI5cDRc446Whun3Jn7m8szH1MsS1c2-IwI3UkxDO1iElTLsfARzHA-0k0R8Lf2-DBe0NoJyr8vfmgu6pQv3j8_cNPd4JZpqPLDob661JLlwjptm4bVZqFXY8c46ONdhNFg2Zagi4qOUcuG7ppDk16U4rEfc2xcBcMbG5P-tb5OV4IhJ1XxFbq0ldR7IcHDD9CR79BJMNgbsYj6kZRTHmX1OVKiDPxX5xK-d16ZcR8aPD4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eN9tdoY1I4Bb-QvzHMnzuoqgxgxtIYlwfECFCTIEBXxWefqmAxKk6pDoBBTtg6y0PA1Ip2CQ-RKAPE_bBltTWhpL0-td4wWShHNtBP3oo7__Nho_HWyG9T4ZwLRfRVjgxzYjez6MTg5kLkqGvNZAkc5WOUC87RbwyljHl9m8tOEpvdEWwjZZXZvKnCYyq3mmOBja6WiOXukr4LskVxsQbtRAFsYQSzEHL2N9VtZaQyNya2M2q1pTMOgLMKlL2y0jzB1TscWw6olUrrLRF_g7sFt8F4epGg1VrOvos84BEq8T6JHyM-Gv9VOfEak33dCZtALwdYrPF6LlFdKonM931w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grR_tGvSKW_X9xnjxLZUIFkFUIHZHnfY9-xIFmFHX5fDvJguiNv8PqJ6GHEgcsTo7v7IHJhxocVQ1-iQ78sof_JhaehdcxZ7UAisOJeGVwdPdOx5fGkYO5WgOflGDucxE27lS8AH0Q9R9rH-FQoazUQnJVPv8Pi_Dqhi0YNy4MfZawrbMDoxfIULoqSM9xRkv0ngmHllnwPI23IyLWvivkNWcqwCSJqqjn4AxgbDDG_umjMjtBrPzpddmrt3UCp9DrGYCqbSPtIRQw-05NkmTJjI_c3e3W4j2fWnyXAKfCwAsyDPRRxmWLhSWluyfTzqB4Tvq6_QHS9iznhlU46NKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ENGycbCIjINcNt82mTjdK5RmDhAgcglT-Ro4C6isNmfHRj8vhT_aW4sQJdS5bvpwukfQzNEO-1j8NV69CU8jGgIce5ETv8m5iOQIzRarx1Q6BcYyXO7WJ0MI1hGUV4UV9jDHxMjIqT3o4F-EyOqPdGROC9oJnn4L5XGgpSQe-fpRBkNcZw1Felw3JA2shXsq-SYCSL5kRitKrRVbxmdbWgoHvxhY_3nn3ewHjlkjv90GEEIjjae0EesJnHh5H8hEphAf0Pd5zjMuZHazrEktbE4HJZZiGce6rbtHpnxkfbf7WUZN7sLAPgQrh63mUUgC6jtTt8WtZXA3A9iTJxsgtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHswdVbK8fnVVcLsCuZRFknUqfF0ohbj-1dBqF8yMjswZm9dTtSzNUXOU9a_no8KgbBfnyXqHhWuPaweSjxl-s0Pjh4yTwcp7jVTHnJ3pqfxGRwf08wkh209F6Jgnz7rlk_9VRFXtGLYXMOCOSeVm_w_uPAcuh_7F3j1UJ86AjB88E-cm5lvEi2RSPK-4uG9ud3ydsdEyjlgSmMzPo3W6Ca_xq9ZEHLdUNSRlzngZKlIdffkNcCgG2pN33mVQ0XUO4JxarvBZXVS3GA_7HtQ13tQbbqHQGO1V1orJrVOdMKFIqZGOYpiTZSp3NS1AcMN4wEHaUFdYXOfDWOsZfEDzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZipWCLd7CoXlHt3Ym2eO7O75xjd0PSlv8sQ6VrTmiJhjTZXv45jIhmcFMsOzpWJv72cw1qHvAuI69MnChtaElg-D6mLiPqwHU5E57KzWrr0neXJWvjyuU6vXDhli4IxK0nvFEGCW_RPMLtunroSobbW2Y052Bw8FnAAqmTWm4SJiRNhcQkcc-BhRjzEP8jm-eq20Y3YLJcCONlrQIoQxqU5R-u6mrcG_VuSdO2GjubS-J92fdw-LBCje7IX1LI-H_iHdlF4a4XEW5jpv40YJo5FydjW3gk-IhbpQ8zMng0Z_GEuxJoBPZP_D_fyn0rG_tGnGBVETw9t1Mipqpo-I-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dM84jnx8G4kElDYg1fe2fueR6uEpbfa9Rr2teAwS_VABxJjw4GG7ZMLqpDGmutx76llvoYE01ZAvgjlk7j198GKFVh3qHxy0j7Xi-bybdU24hNezGBczyaYFspHYXv3zPc6WPmqwjIlcwn6ONqLtvgwsASs1-WQEW6WajXhnMti168KyXqOij3UlY-rVaQHF-wbCU3lLuGChwMaqS_UM1mFqrTOYoFD01f0Z_IHuBOc9PtXBi9EmCktf_v6xSYbqLnWZbJ98PmqI71GEQ7A2fevMmGLkHYwnpfG1ks7s97Xap8Um7F29NgGUwNchwngUB2lPp_MiLWXjRlQvBKMmPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRSW7ZBkrch_pi-rNGM5ASqp4hCczXLUQ_HbLMw9zLPFS7M_2p925w77Of3H2EALl0kOLxlC0WuIQEDzm-r3HY7Mjh366w2utjw7oyTbODSlHPUDP8KEtWh1aw91pfLLA7w0IE5v0BGvqNWp-UWp3zvRlrZ2ck9wDUl5u8eCZsCxUJW7uWQ1QNjkULsVZnj6Jgd23vs3lVHmtAkVeWEWLANCm0VoayrUZJn_RSSvwzQL7ZZ9AJF6VvfosZZY15pgwdqSbHia4y7noFVrxL9nrC5pwqWRagcvKUe_hEeuGsJu7AQI3xvNmbnrFC3bQNEaapB1pum6OuCdo1DeXePI3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCBsKn5sTdFcZSjiPFsVJqVSrmZ1iUxBnmmdMkkl39rHmuNLHgYzx0Gk0tGTj9pxVfGuWbD4uDs-uVSUL0rLgS6ml1f8xyBTXg7gHE5W-r77bdwdBYBcceoBbCasjeSwApPcJxx0CPYj97o4_H2qlJ82_p9Q5sSXeII7fDG6Gl9tzjpGrk6AbBp5EFbmc_syrVkMMerJ-JWpzd_rmxgzH6d4zQcfp89Jl1kT4m_tnfIcy8VLxB6vALdFCqVntA4fjAYbwp67X9QQhRtzU8Dlcx2o2n3O87suv0RBgjTCwvlAOf4hPVHMnGpUWlsZ4rmth9I8VMwVA3BeYmxabgmd3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQ6910MAC6LD9lOpqVKJsY_5k4fGst9feUUIkOA8D7-iAsYq-IwKVBWSAVx4PG3OjUeAA8MuP_YnfijY6kBLdkDQgzFh3lMIwLFmuUxUPu62IanImBsyllsmGQIcj6iBcyNZYD1IzdLRc9sWCOdR1Cz71fT4gkEfVc09Anrb5KHS_QbHGVKUd3fHnCPcTEkdxW8RzLx7Z72zc04zQdBX-SFw_9rffYCN7DF7IntHlKthZUwEEVFC-FuDOPHmGmbiqTwy7tsIi9Kt09zxpPEUXTjS-D5GIDAPFPdIdL8ApV2klE93juRRya5nweyxK9tOEUb6YM12mqZ47lCl8CtoRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xs8dk5fhXvIxX472x3ZNMk_YSXdJMFpStbccDge_E7QFMB3wskuw_z6CSx2c3DH7XUPz1MauvWmbhcDOfwImgQB29pVTi0hHQWDd8R-Y3C6C6LZFKna-QThslCva-ZjYrSrt3c6W4ESFugo-k1EFKam_toTPBhPaXg5mGskb151G9tDinvzz3AX2DQGDtju_zfbZ__r4I5CurUZUYQgdkwTGL_VH_GAVmys5gQsxGWBAIFyEEfZ7o1nIGMJS7v3rjNDMBxnimnzfIGdT27rDfdQW-FykgNfkLq3WbQUotzomhNKnOeBBjOATZVWYzv658v1u5kPMPDiNqAvG7jkuSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAyh5IeMf9uKP7_d8ogaxGFNn6CePqhxFrYAbV-0nNIIfqxf23WrI50x5pI8mRnjT7gZPKpkHxoLJTgUCYqu3DO62IFcztBA0wfwEpMArfrugKxvz828UIArMzkaHKDxlUGJFg8jCxKnK5mZXvvIpLEN0QqMdoUGu_2Dg6uV9x_VBpBTRRAgioDO3Xgy_3wSN6KCJ69Bw7vr6NfXNniXqYNEnkFbKny7F1P8WT66H9COHNqDv0MDYCXMnU5EP6jraYWAqXHl-JopnZY4VidvE9KBbcZ0zmjeTuM09LxLauQFALkfAWtU2OLr-enDNfbK-5aqETza5iaaQa01d2QL9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8n9qLXyxMI9QzmZTWLs_xflGptPCXvrtKwvI7AYt4oT2XyBDFCl-04ZCEYI2Fj-P6lSI8IZza9-rvY1qa5OSCzX0PiM7ZPq_ZdfvjX4kalpV-A1hZoEGrlErUDj5tL7GityOpcpkK9bH9r-iWo0uhF4eSLMCUugzJyAPXzYlVxftuN8cp2pVkEmw6qKG4XcxGPN99z1H48n6hc-ptydHYlm0iqPmc36Xu6u5_clUuPl9bt8RjjlPFa-9KeAgu_v5azxPknL9qkfWaIoctSknZFwtR-uOHMrEROWRjfD7riGCxiNj67fIoPzKsKeka3LXGUFfMbW6N7cIoht9WzEgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWiR9_Jwyd8xH3L0B_D0D8GWPoagH2FWAKIvAm0J2klQWBtsE8qMG4GqXxBixbvn0AdrJ1TgW5BfwDE5E8Q7p7RJ1s6RXLCljpyYnY3Aze_41ITKMf8MxTRhkCy8JyXpNLQ_weFCGB6C-4wf-k1WKtiZ-WPixR2oT5rBg7CKgdlo33gAQYgMOsT7vr4YH1eSjSmMzV5kH38vbfaheNxdbPkk45jPg7JzV_s2AddmUYFinuZmHBpFziWB-QAVDq_QAd-inNx4jQDsawXNws83Mz5kNDzWB1NaoyRxS8Sjd92wP9JCtRXX953y-2tRKB5_4njL3Mu3UolHfVH4qcpEsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRwzyzpTIjvlvSz-lvJtWKT3Wb580Tb1wv9-AFUrfnDHyyf6qmEbmTwp1sQGBidI-ILZ06JGGAC_ZA22iX5CEzx7KdT5SnBQ077GvVtr4s3gYg676qhrag-lqoXjGdZBKeNsrbbDnqHbSPd0m8sWaLQ6k3qbOGTdU_z_n93Ao7b92_aZu6g3NdCXHy-fm7uzpsePRaTg21UNMtwUXWwmCKbbU_02HayZQJ35FgdUUGl_lyXgevLaiP89X8euvZ2z0kcW_L4LYm6IzF1uOnLEJh3i4dJlgq6P6zi4-mse0aUZ0OoJvfGYx4UbWrtK6Tyfo8xbmXyO-tSad_L-JX02HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F0UWBU84SGLTRNs5wlMj-RI-o5RiPRwz4KGCzzgV3sh1gTj0dOG_745gUOGorK3zGr3jEoJuGpj7yc3eAgVLJqdFAHOrSITAI6XsrGeIyRDYDx_2xbqDVbA4qdclHDpAZMPCMlcx7wPXBnnWKCIvjmA5y2-58rkQOjzcMIDU1evVf3IPe8JbN21cuFDEIG10ZIvTXEQ59LvHTAR5i_WPdX86JonI_IDMtb0oz5bk99Acllpfk4WVA-GXqXKy1d5h9xYgx85WUcUp_2QS4xgjtU2hH-7aIhozmlGO6d_AKmwY9sD96uavWxBjoH4MBdeamlGabDEwZ6NMH1TBiw4R9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrkzssdCbOY_bwPF7lnZxs9NhVMR2Lz9M0kRKBdUkeGvZAc5qeDR28VOr6xWum9xG1zPgYdJuV9BT1AdhWiVn1Sthjz7xU5C0BJ9EVy1IFSKMsFzqXexwiOpOsXaKJNywmIIgz-dlgbInitukbSKnGG6_6o5KVS7Hxvz2rbnMcUcGYSx1i8YFb48k5HeehL7kJz-YQDESwWQ7IUYteVkEinFmRQffU_nHefKLGhNbqBJopmE_YA4pB5I7t3p2F_-C8Eeovl7Z89usoL0c_7IAmjl7Hm5X7G2Uv6EkTVprm-8lf0Iwv3pFNtazTnEc1mf8yf51qoTphF4bKSpgPBQ4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3hgx1oWJfSv2Vuha4Fn0sbowKwO1tulga9V1sRTG8CT37CY5VZVMepEIHvxWpBUl6IUjorW73XyL-FzlP_Q7E-O0gJ3rTl-c8KGfntCGqDRZX0xWmdU_kOvlDY1z_EVJDkUWdXQ3pq7yWpXDAcdPTgwAofEYio73UTE9P2GOToV0LQox0JUQI81hPknlE5mFrcqZkV90q_b55krq6GXrBOwHXnQKrKz1w1EcFyQiVqLNap7SNmIKnDwczLJ5m7jFuGYnxgV8dDuEzK36ojNApg3BYbIH5uOgZ4IfiqyGZssBBrtjrmuPkW-5GUkVZ6Pv9iuf3NGdyKNmHehUjQy-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndTc-RgJNOv9DUwQXRigbNSpS1yjZyUrdddB0DsvPPRMEcCRJHXgKrYHzX6ge53g5V8e7xb1bAkZSNHhflFOTenC_4vWXAfE2mxZx8EMGr2NPhPOG9RIFMo9hdzLmxKtVVeOe5t-IxnodZtiz9eGOZH5BsPCKNRs401YLhdv0-YUiMOF2FAU1nTvcwfjWUioAtXP1_IrWz70LJlJXK-ld66PQhCM5Z3cXTxrIhr1GNlkqoqtOy6mpegqSmEx8OzYofssHoITSpQWZmKm0a4rM_PztB2mp2KYHbW_DWOohtimTLoF0715SsPL82ds-wMm2GgptN8QLHTJOKePkUWn8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ro1LKuGAs0cjI6o8UWH76rHzxbUCocCOv932cyFqhuRntH8hoGUk6B-9cU4HfbV5wFWAWMkWNL6FUq5s0uObuLSC8HRatYWMWMnc4ICZ6gLGRjEKaLRxI7PAmvksNIriDTAWdxWy_SLqN56p5Z8bQh0k99JKnYd1acFn9_oVtfJU-0CfZw1W0q_hWMOValN4QQ9zXgozuxNMFV8P3CiZpbnN68jna8ThAT5n7UCsgf35PSV8X76dZrx3kVqfTh6ADZSduDNYl-KJAEls1z3OE1h61Zdjj2O8j_e7QZGkhGVpNFNbjAQO0uoA1YS3fvtimbBTaPb2UHkTQiIDcH-XZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O0DjV2epn-8ryE_9iFLnCuIFX2oO9WPUeytnXTZYrJ63Y5d8F_WydE8cBRGmyxgU4oTu-yuWmDnScqo7o9dcD8D000nz27PcTxIGDxADh-EsF0L-C8r8-tZ0Vf84cR8wRowByN7hj4fpYtYk8Cd1FfdICjeCfAaug0dOKMIi8UDtmM-L2ES7JsR-dq8-RMuVdM5Zdvb28UhGSElicTCnGtyDS2kffQMdwMW4fajCq8jgAcRhbtXP3IlKCUqfVqdX_P7jiYMmA30rUK9LGMKjrKmT4YB6V40fSdeh__xzDq-NPvgxRBDgmkQB78482vwKWs_ycr1BSgbGG1GtwatDzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VCmfwKOrO8-FDRCvk8zkQ9lKELUHjzxV6QVQdCamFc-QybgIKdlOcJ4LbcMH0GOAJeLKhzRW7_lFr_IiT0kzCDBZJoQLbCmhi_YSMkxEl2J9zbQXJgULwUiSH0ypXz17BY96zfz9aBfLqOLgtfF4iAseLO0myyI0ZUW341wFqW-AQxR55M7F_5FbuW6-bmyccEobw9FbWjA-Ixavrpa0iOc9iregxYF97_6w0G0hM2_32r3nL_ePLRjWIIQzjxKvBzc5cXG9iWRUGHc1U-n9hyyn8_SSPNeE6_djzZWKvSVk_7jK91-oG9lY6joJRaetp4u4PAEGGVX6XweE3tV5yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GaUZfX-ga9nZJ_rzuTH3j1d9aLRACeCwv0kcvlTd_AciE0XFjSJuG3ZDpNyv6x1aQqXEDXA4Ichyjv4Jw82n-0OElIUOpvyYpZOEGYMMUTexQwuOGWb_QLLnTfMQcAXgu01fRE5GBaia0NX3gNjXuSg4lejq9BKfSUQUq7SdFewymMSRp8k5R7ERjDvOz2Bkl6GLmMn9U7zqA0KA_8PLpDMaSqC4KM3hPVULuyvng39S47dTR3YFjNjqAibKulutugz31DaukTG4v1YF-jwQtNy2AyvfREYb7KNDT1fy7QQtYoVruWIN8uFguBI3jGLBzF0tQMP11X5ggGri3vklWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XZ16nCLSRwq9X5_NWAGpyHYqzWDAh2Vnisptb_whceiKOvdD6pflBaDbQzqRsBkeAtGIfHngQgMsvKwVBB8bvcDjZDG9aGxo_hrijfXU7WGNDZO2JMPEmBfR2QiWrxziEXzUbMy17PJUJjUktwGYX01kHtmiKiNZeQQtAckn1A3GE6Fe4qzQiCtTTuHT3eNkeBB9Vr3XJoyqWwdSJV8LgaL6F48BJI4C4vWACrAYFFL5pT7oJZQeYw7ssYaa__R_qcjrjueMWBkYa3tHXARfRZdlgu3mG5_mCEEoM8ESGadj7rt4ASkF-B8d0ORkJu5kjtc0HR5j_hP-8_XsJS1d-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oh12NgUUPdbhrCmjReISSMNKKDV0tHKu8vWoe9jhEJPQs7qhfptWouaNzkSxERDT8dgZtgc3Gre0M3PWvDBFc7jQLBJ7_TCdzpsXH3twTTqq5zBLy7aAO--w6DClrZnpNMUy9xpeUNE8BscNbKvvsEwzzENR7qh3sSQfOfgsdbsfcCjdIhRbi3lChAQNtEYtYD4fQ61A1EDqweLdGVc60G9ZqYL6DiocwVKiLIBAUiYSPHgK-bpZvdF2z8DV0F7yLTrQK8Orf2JpBODJNyLK99H-oI-ZRVQVmithOeh8HTKywj7RImcjgB-VEUhsFz0LNKPYAiXF6alsqCQX5NJkAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mVZoA_3gDawmLF-W8IgQiq78MN_qgxqu5_FD20lrBHdXrZpTelqWLEpMDFA-rG9iQy5U6XXuHEMsH21eFu2NlRYFxYNxzlnu8LUV3TefF6EsBBsxdD2ZYjMnpew7JloYTY9KZw5zcvccQQmGf5QyJe3qA4Hj5cADLwQYAMleVFRe8RKSHU3yq0ChcZlwkF0oYNhhamvU6SHn8REN5JIfc6xVCy49DIGUiNKiTvWXgoe7NJBqhLUnJgf_y7KaBVn3QKH4ckdgQmUMtCQIaITRhYGzNwure-nmJ2lLnaBlgJclLhND2-5HZtJFkSB2z1s2uWImnog11RrhHvwlxZh5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqmNWPR66XaIxD7PbYBEJyOP6WN3XRxIIYw-dYvbojw2MiSKzS-yN-yfrQ8vFx1vzLTCHbKNUEo7XEgFovKL21cQYXS3U_qgtWBrggHkhIxoKfkoNV75jGOPdwoVaJ90cFEFv-p7FPCnN_P568P9pLgVOR1iYl8DHwBHdV7OGCkjFY-p8qDa2zRDPXRPwulwHXFqtG2TaZfPT-FWbGvIz0GjI_-JWz6sYZBH7gDBg1XJKBOnPGKed87ukH968IZ18zzGsrProaXCdkvCzGrFP5dNjE6VVVaaKccN6HrU70YlulVn8WJCFO6rsJLLfoibnQ2CP3KFu1hFzSQ7YrmJ1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZRvBiYftUuEj2-NGbzytr8_cE7vcKS5GGcsMaJ418wTXjGNwkiSNhrmHxRYcsyP-vQ1N_JLpA63ihyq6SG8xTD-oF43vlx9cLcczbHPJXwA3dpBgzBFv4mWJ28O6RIS_hkK9NzvvsQDWwfIEnVUiVRCZz3GROL7JBvy49FIRNHHVMOlz7b5uCC_anueKFhsKxKTUE5BioLg-Us67fh4n2WBhbsuJCuNTrUosZBs9sDCCpZ3-FMIrBCNHY64siTAVlhssPu50K_taKYTO0C1CfiBCdpVW0jbELB62nHVs-2wU1UNp3lTRS70TWif_8KDhJhM9iH6GQAJZyEa7Dcu4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrDOp7ESC6vfpje1nHhuhmV9pCW0ccMP9mHnTF9s1kZXRlsIOAEmzBtZ3Q_E9iBcJ3OUn9TYPNHpoo1BHlysWONdF-GD5jyA24UMj9jZyA4p39-OmpWtrbWXl_v5xdXrMt1o9JdLw3pT_DFK9iEjtWJZHP1F0FalCd4xVSTZdWo06rDUdBaodeYs1gqDxZys3MtkpuoR2wyXLvpgGOlSEfHb8oTfd3kULRCNFDutdXWWH00zlSSA42QdqYCJuWbj-1vKrC9_j8K9mc53Fjvi_W-Vob4OZk-g5qBoCpCKXoEW3j1NmseUhDcRcwI4BIn0BF_Fs5-_7tvgVauIqUHzkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4orcCIy5As-fy8XvVSTBfUOm9thAFE17JYB361DaCqDhbqaFRM1udKw6I__h9qqHEUmYzP-4Ea5z7jciSchA35uNPmpmuHPzb4gEWxx7XrQiaHC9O5Z3ybazjL_qMhKbR-5AvJzpFtEhNnK0DB_ndqhuo6C114LKFlHQhEF7h5v_aExMcFVoV9mkNty9Grxv19NMMcjGKssMTKUmZreM9Zq38ftVnYtWJ-L6u7GC_ar-nhP_wfjCo4A7r6mgxLYoT8vqXyQa67tscrPAkuvs26f4ffgWw76VOWJyHn-WeSO6uaHtNaoOUn_wEb4O_GyBfcBZ-6qRB8nIySMk5BKhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nY6M4EZr-hDYQS8X4h9KP26_1J6CFBtWmM8glCZ7yMI_22Axv5tRtq8UJ-amfEwOqNFFTOaA-ZK7QNa5e-L0ZZrW_ydFakfFiU8bVWil8PfE0ei5vA0_3dJ6DbJqbwgErZ3BRowZm4wMXa0uwbcgkeM8oeJkcGrf2B-Qu36DSZ0yZ32rmf_0rR8HnypROCuTfwGx0nIAoXbxQ23HtOTmr_-dj9NUl0ihZUyeZUi8HMno81_Tza8laYKiUJVs_MRKNzBeX2C8gkd6L6h7i9eTAM92Ey4FL9uUehX4mfAfle_cKHvbapA9NsHkfcPEF7ahQcjYBqoeJQRxOK6Dsi7y2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sJk4PpSKzm1_VRXVYFgQsxoBtC9qDrmub61WUrlvDISW4jH18Un7rLNSVkdNZEG8I9g0pjXLM9d205ZujDSXzHOg0WLbsLMcDLqaaOgfuHjg9NqK0fxEVUIwN92UgbQjyn0eigXYC1KmX3wSbn6QvZS9_po4lXpIcyhR2bZNBAFo4lEEyixKyuG5gtj4K5I0UdymjO7grFoaZr1nRSPxigsXAYEaGvuegEVieZqoR4NN-FTiGgAv1p0pfe7dk8MvbfTQnx1z88aSyxRuuymW3utepEQcKmp4VUMq06fiKwdcilNdKnEAjv-PeNBhRHSr5ndZKkYR0S7KQiSVIa5sAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJx7ij-drXW9kgIBq6_H-4_o_23SL7yz5Lq2SgUHKfXCJPhQ2louh9Xwz_9zaeaefQs4sZJIRUyAkP-JnaVGg7xX9gX0cXFDuoFcS3i95FtDqivkDTVS9phhVzl0ln5cNFoKpu6A2V0fBBmfSdkvezA9EtZ3RvvYMILyNKBz6jOUDXIDXld3f6fXZBIX7TfJUUVGxNxKoR2zGHbJHtI5zfjLxmfKPywgNcTJCGrzPDEqYmE-dvQhKxRNqrL69r9ghYV2OM70JXciWMelh0VMW_iU_i1fMyYC6uZgp0IYlrfkaRNkS-GUbf7MTFTgzaASM1FYFCuH-6G44IReelLiZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwNokEuoO3M1lXMmMvrWdxP3Unq_aLVyxy_dxmIzfZCgLfzfq9n3QbEP-XixcuRQtIPdVBxLLq4EBMsVxOhiBrvBKaSJWLgPVrta6wFHlzdhO8rOylN0QCGDNV2b1eZiE5kF2t1838bvPDBZV0QWo1iYWlKI24MtcxhVFaOd8Z_fiBHThFshC53CGcVo6jJX7_a_YNCCDFYSpTb5mNdfSBvkSuGP5DkfVWK9CF1OH4c4ny1m2MLuCz4n4QI7jGb2ptvJVvHcmPFk_r4Y3WgktIw4rRJRKXqDt4hMn_43PStWRPpf3RmPgSNvaXiTiDipwKrqRYAq8WG8xUBdEut_0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVhz9XXVS_KcjF5am7JOq6sdHgBBaL64q_A0XaU0QfS_r27LUTTSfP1vymDYxtIrTycz6LWsNPVa3yrJM3VVH6ZKGFLk9UdKy48XGelVjHxKqG9cXBOfRmr01SrZMBL0upUBYpq_j1ZfZ5Rsx9V9V_5mI1r2UV4y5f9Hpj8UPsIyJ-z27cg66bdMkqsDu-pJqx1Lp1nZ_mvRZxtLHl8WTz3Hy2aB0IOfXiMPwi5gpG_dqg_MdhdPsM1GURrr1wiBqiRg2qqPL69xqwm5K4Xtq71MeTNJDeNBIce3VW7Jzy8nxcw2CoWjZ0gpFB4svybcodKrHYO_gGOieTFSlbG5-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZmRf9ZA_HmvWYoQP8IwFoQHDUHVTd5UmQkKPZFIB127jW1r0jgoGBUJCa9uYw9O_AIvrEfuC6SvztBZSzFbXABfdmzZQU4yaPCC2i3etfXlKuAFyQBeQMR6UxfxTCwznd4sLljZyU27aDzsAUfi1_kK-VtoqVfFje32j5dBMM6y8sqy7Gqd1ZN2aicadJlrifnejhV10gUzV5fWcZrL0Q_xKN-CHjl5hcDntTY3clkeJ6EPyhH6VO3TFcFH0zgtgy-qplW2snHjUn0C7YtQQs-hy2i0lDGSikWcVjPjSCKQoA2m7PABOPTn0-ClsnZQ2wpmgxkItLobK6RD4025Nw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=fTSmgIzhU09B5g-n5Q3vP6rdvmt4FItZaV_rAkERIr67bFMAoAu0bpmesZlOi_5NliBlFTyJXPeuuwwJjDNq6Uejxag9E9uh7pBwdPt_9CooRxWmLrPGz5LHxhFFpZvltW3IdzBzqA0hECLcVPPGwN7S8Cq47UsIF0nqmy0D61i3e0ALOWQ1afbGBdO7h44l7EIB0Soh_B51sWVQCfmHUo7knbNh_wDsBuiU02uzAsbwjvPEb5L50LXAKHXqEp6QYW9KXC4-6-B5bN8XZ2_FNxfBAcJZwdMDu9RszE6aEUUGpJscn-Xx-hTaaa0U0v7AddJ_G3EhOIyCBadASW_azQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=fTSmgIzhU09B5g-n5Q3vP6rdvmt4FItZaV_rAkERIr67bFMAoAu0bpmesZlOi_5NliBlFTyJXPeuuwwJjDNq6Uejxag9E9uh7pBwdPt_9CooRxWmLrPGz5LHxhFFpZvltW3IdzBzqA0hECLcVPPGwN7S8Cq47UsIF0nqmy0D61i3e0ALOWQ1afbGBdO7h44l7EIB0Soh_B51sWVQCfmHUo7knbNh_wDsBuiU02uzAsbwjvPEb5L50LXAKHXqEp6QYW9KXC4-6-B5bN8XZ2_FNxfBAcJZwdMDu9RszE6aEUUGpJscn-Xx-hTaaa0U0v7AddJ_G3EhOIyCBadASW_azQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NztgiMZTUdiaVX03L9qxk71V3lpv_ocqhY3Atc2yVa9ANvvFT8WJ5jQhs4RBkybonu-_k95hwLMzvMNQSd2nKzkqWlF3faph5X2FOqg9Pf5h-IeGHxoszUwVc2Hsk2cua5fp7cqnZ_Pa2QCf0fww_xuV07wiUfIEqDJWFXwCHHKObx3lz0Isqk3vL55NcMNKFXRCjw8RnuLIXtIU97sPEt-Dfa4G6N-0GAImwsbAaNvdDMlL1lsgW-6e40mwyt81nRoWYlOjSQ_Hw5OQmRwDQLoUAyUPzlbCT6gyE_yAyF1i6ABJgmpv8x3EUutsaVsSAr1Gyqm_wo2ea1yTAo3IHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCO8hRmBp3tsN0m3RQGd83DOirsKMUd7tbkziw23AMt1G1GAMS7QhGprcIuV2DB7p9-qX5MNXsGVL10sCUOXbi8Mnguf_iTDud2K-V09hHmSKiIavveVJouwS_ofyPohFFBxTw1N5pjnbq3pftQ3X6F3PXN2kzc7lR3-1AaDjeoRGmpa_JxovIj5QtJIc4w5f9KcIMROFtEw6A92g9IPCMsrCiQOReGZqGSIKShb-SuaH1W3STRPR5WLRo2OYUYC2eVG9WJJhQSdVKZMu3KPGyH5SY0-S3ThDl4fgeylOIBxXxbSN-7rwhpDONaRU7PlHVwHMrVfT3AYcUBMYoShEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iqiWJU6Hu1yAmxcQyFxv6vToyDrlI1JT_KpOmF8VU2Yqu7eYqbiiIzkozBtLlWFauk6VpmqYs2GwMd3_YcET8zL4DRCWBraf5YckreBliG1GSd2q4wfOGtMqsknCDL4NKDpbPM1t4GlJrDoXjuTVc1axHQ-rhryPzrVYhZ4aFEHNsrl8bMwUzSXNQMTqYgIbP1K-mdSW5BTbQBGOt_yqw-Mn3eNQFu5SqP0YnMfmggZ4FTaOfZwiCjimiXs6AflRS3N0fxGHbVSQqwwsPLZl6O6Z8c_6DRnlp4SbAs865aD9XL9HTis6inavUhS-zZ7Uun5JEbp1GTNnwMsVqfcPbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SrD9bAvrEzEmOJXC_EZjwTYB08cOKJbGr5A20WZkeOWQB0_0mf4g3Mv_bFu9fkNZY5ptjNH0Vi-fg_FWz_EkrWLbtEZlg2E7Q9mjmA1s6u84EgdSIb7B0jXZVYoOvuXdJpcNZvkRkWaVBQ2H0p5Ox9CulddPv1mTEjCnJYqL9ORmWPGFNFf22MaP_bbf9ZWZ7qNxID3gChbkiBP3BJAv5DFrduD-oqHAe7xmRViXMKT8hZSiW5xs9dHgZ1FzllCEpSwPKDMKYLXRg_YO4PIagfuF3bOd74sF6FLOpTQ6liVCVvV4E032PR0585CcSBAkOxu-cMdBS5nxQQQrAjt04g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k9IWNWr2zFvgywoqgYWkt9uTHScRQBdPrLUSeRxZtFeaVHc3Biu3B6mU3OiinZvpwT-cdT-ZHXgH6l18nJCYNjAGjWg4m1z9bYrcS5s6fhL55yxuNS8goaMxWsacl3bBxj5Obu9r8fik87g-TPf2LfVSlSYnbQw6Ti1Y6eHgDoqGPBDXF6fjDfUBsTBBEZSAEu2cDLIyILaNizM21929T9WQ6k_KiCj53-PJLR4ecMlFH9jsMQzUcuveOzvVUKttaW1RN2g_h6G0Nub8hJriWO69Zwoz8vPFu10agDmMwzM6_S8EgK9UQOH5M36fHA-Fc7tcmIQ3MexP3TqJWoG4Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HgAq42vp226suruO7MckCKhI4sgvCbLlayvj6XAi1Rq_v6No6BU_ysgG839HVPsDuqVUf-WOI1_jYIyMCisbcKhFCsPtWWS0XsNK972VzXZrtHOsfMXtDOjXcDBexIZLCqdUl7bHuRpFnvRcMfiD0XqHXGiA2B8b5oDGiYjs4_UTFc1xP73N6YIRzOKqhclZG_MkWKkiX8r5S29SyQdKyanWm_OtaNzmlyOMpdrLaht3PWkt2huiQZ_6_Yw8BNIwDQbNWxvuXKS-U4ONeX6mQPw5w9j7oVykf9bQYjLYXn58taw1JiveWydJ8IIYZARvM1Putc9VhcR0-D2CLTJQeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpjY9t9HyKf9lajsdDtqNcLuOf2Gb6Dwc1e5Bnls056G9EiOmR4Rd_zKXsY8Pfwdpa5c-pV3I-UqfuhMmd8X6jbSuUcwhU2jsApLArQy7Bd80-yR__1Mt6yIJY5Ysjzt4_Y8IDs7Ym_ND94tCx8iABBDVDp35Hl5oETL3Otov6qCaKY02dFxtZp10HUC53OUCDKlzt1m7F8p_l_hqlDNntKNXmNFQXCbbGS-hgN4wju3AvXQevoxOLa1t88e8L5XkTq1Fol366nUw0DnlfbYdFjkdiD3hI6nFZ06QRA-Sioe4MalUamkxhCFCD7FqyyzcvCdbfewK2G0rATPCLrGEg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=fT-DxDCtVrnEN2XuuY9rmnZu0C91keP07t0dKdowRq3cYYRzjrtQtJkf9XlEUgsWoP5ToKAzO-OpLqhMhvoa_mswPhfUDslE0zZraGI1Bh4jZAnGeH0vo9jYD_8wTvykRdCf3UArj8Dz4Hk631DqJOOQUnS2Q4B2F2KeIqXAhy4P9-P-FCUwHrx2xccrD5uy_xKI-rO9f5MoloyFGdK4DkvxhbPBC3GoQdrJ0krBnCiDJ1O0HueN_706un0N1tapTkNcZQyVGMG0v0oxdDITYOHIwzhDkB0HeXUdxMjG3XLigthvn6v80EVeNqoApWtPnE4vRRw5pdGQseWCUMNHRKTeHYmN4bi1as7sllfCtJFR6iJt_6PVeSTSVyOGtTy84C_Swt6kkdq3FzNRtavChc0ptbfOpbVrkoXwMMKBwbk1rlWQvqgnV2azU6DzC4fbdu8zKm6j836ZF7IDHdLD_jfnE_ESbvAXGPsUKy3Pg14gaUkQYkd44HV9qSo4_3ggVkSK--z3wPhX-oNHcvNRP3zvyf06p1yZet3-xk5u7DKbd0nDPl7xJQ_38R_tfSYv9XimL4ovrS1fH4nko_utOt386HFD6ukXMuVrEDw07lNiF-gzI7NHIvhuHe2zFafIxtY0D8zZEk86nJ8RZUgkFAQXRJeDNVVEVPKt9L1nXaI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=fT-DxDCtVrnEN2XuuY9rmnZu0C91keP07t0dKdowRq3cYYRzjrtQtJkf9XlEUgsWoP5ToKAzO-OpLqhMhvoa_mswPhfUDslE0zZraGI1Bh4jZAnGeH0vo9jYD_8wTvykRdCf3UArj8Dz4Hk631DqJOOQUnS2Q4B2F2KeIqXAhy4P9-P-FCUwHrx2xccrD5uy_xKI-rO9f5MoloyFGdK4DkvxhbPBC3GoQdrJ0krBnCiDJ1O0HueN_706un0N1tapTkNcZQyVGMG0v0oxdDITYOHIwzhDkB0HeXUdxMjG3XLigthvn6v80EVeNqoApWtPnE4vRRw5pdGQseWCUMNHRKTeHYmN4bi1as7sllfCtJFR6iJt_6PVeSTSVyOGtTy84C_Swt6kkdq3FzNRtavChc0ptbfOpbVrkoXwMMKBwbk1rlWQvqgnV2azU6DzC4fbdu8zKm6j836ZF7IDHdLD_jfnE_ESbvAXGPsUKy3Pg14gaUkQYkd44HV9qSo4_3ggVkSK--z3wPhX-oNHcvNRP3zvyf06p1yZet3-xk5u7DKbd0nDPl7xJQ_38R_tfSYv9XimL4ovrS1fH4nko_utOt386HFD6ukXMuVrEDw07lNiF-gzI7NHIvhuHe2zFafIxtY0D8zZEk86nJ8RZUgkFAQXRJeDNVVEVPKt9L1nXaI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjcq73AORX2PoD1A2fdAxSl7FDRPCMFDFOYqPrfIzzc8dDH5CP4HDvajVjpgWuB-zRMHxpvsCw5epze8chGH-esVwRnkJe0Q2HhX0eurgbwnSz5-Nx3yHlE8znHnpo8B2ygqa5XgtZHc1zg3L-DOsIK-sT77V9hB1d5zbqr4Xgn8EEGU0gK__I4sHJ4DyRUIpcf-qd47tChXO-cj8sRccmjnSvVc8H10eQXKZYq6EO-5xOepguFEAhNTfPFKkO0YiVvQw_6TLdNlXPC9q-3mXn1Kc9l05yZnzcwu_ZcDctkYfMe_Jxyok0lhhS5hw61mOrOQi3U_kcmXGA02SsPYvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GydUN5kNsOtbHtEEooDYaVtJ7PDx6tD3zBuK8vUfqNDMtayQ6PrXxlQv5xs2oiDUw2gDt5vDMxYDHyOsbjd3CV4n_YXZ36yIoisSYkR9aAhAh7C_-prpyPMCgKL1NT2LdFZkKIT0Eg1A4E2E__CXX7HhMeuAn1UjlxqD1-5yzTFJi-PrNj1EVh5DJNjca7UCbMQcplJlgN-4FySkLAKRg2DAqjHVkFH1AXTHj9J81UhBTsCJW1IWPUNaHtYYtS_u7q05Eboy16aQWW_4oQE89aG0xVSnxkur4kAQnSj3hCEhWM2xr3EI93pkSXnmet-Gnu7ndMSTSDYVN0_DIm-5UQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FqIdLlXSFvo8GGM5D3QN7bRVJ1ev0Al9iTwzpfvUriavh5Dw_lNK64xXk12m4P4vvWdpWUPiu2Ya4UyFzsUBkemHTsWHsiyAPFR6exuxo9r8IqqpIur-8pv46sZgQF2ADG0py0UlErEw_P0HAQWktBjwGRPKZZVlJU8iQKHkUkx_M4rsPAk6fjClPHFp3QZkYfV3c596SCOU2CSt1xALYBlD7ujSRQcnRG0TrCvKL94vyXAjKNIcFU6_5-0VarN455Bor2vHiouaEsiY9pfqxJQmQ4-mqU8J-SAiobO1lSoT3Zef00Gbt0BIuCifm-n3wkZ4yMEMExAfSOP3PcjujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHkGtcbQQkdTKE6KemEvp9l4qwnzhzyonrQyHeDo6gBoOYea5Je1w5lp_fC0Xhi-fe0pVJv35X3VBLOrko3Lbt0A_xriNZ5JLlqrPPz-ZotUsdkDK0dGIJc6SMeppwZiRFMuf_V5QgOtS79xGfmnhlOOwiPY_xj7Ig-cbOhocyeK922gusaaxIzm1s4oHIB9nm4j01-ZRALF2oFQ9mwHvosxOPTMLZOAl8biblTeGRwQt8aRvXh-6EO8uN_oFdH8kf_hGbROY-EdPKG5ab7K4EGlytsWqoWd8cwUYIAsAcREsrAbJJ-Imudt77Ob7fhBZZ9v6Mz-KwgKceitusf1qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4eGhG26DFae54KTMCU7PmtOG13opBc15KWJOZdRoqWHaPL7rJMO3ZyL6cKqTEUHMlPzrGUbTceLyGB0-jd1LQ-jI26ufBfTZlh9xyQmu6tZ83vICYKLtj15nfchFX_ouTjiwJIOIwNPACX231nyGLYCsPK1l84x20kLh9p2jLUFMI1ZgEB6MKqRJ7xNicdERWrq-JdJQhQe6MWfb8NTtLF5v0oZqy-PKosL2oNYOMVFqmTSZYR6hCRFzufuK-yUTmY83xVq9QKPjlCJEh6f6onkqKNdRF-dLf6EsFdnPz2VZ4d_pmQ8Fm-IaeDGSlJoVUedaQPbvkZ726KK0H-X2A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RVqMUZJwBMy11zM73rkrQGeyT-smR5CcM8Rx7hcKtS03rEATI81LnPtDFWvU21B83RVCfuuJQwtLAwGixHfrQA9dslPa_56BvirsgSVqc95Va7pJ8d2adp2OKD5KB2fL-TNhG5bmcgZzFeKcjbOqIZqIYQzDTEShksp8NT-8BbnzOdtgW85uH9j5petfbPFT_ZQR_eZdZfX4LPlflNJ10WOBWBsV1S3Nsu220D3A8edhw0NL2eA2if0iHYZQv4-WGmhbtJMi8MPd6xQSL3I7NWhTZ7ew8Tc3wP0h5E4FPiPaRmLJ1vlO-tsJ4H45oQK0maC_X1uAG-JVbHascc4Dak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RVqMUZJwBMy11zM73rkrQGeyT-smR5CcM8Rx7hcKtS03rEATI81LnPtDFWvU21B83RVCfuuJQwtLAwGixHfrQA9dslPa_56BvirsgSVqc95Va7pJ8d2adp2OKD5KB2fL-TNhG5bmcgZzFeKcjbOqIZqIYQzDTEShksp8NT-8BbnzOdtgW85uH9j5petfbPFT_ZQR_eZdZfX4LPlflNJ10WOBWBsV1S3Nsu220D3A8edhw0NL2eA2if0iHYZQv4-WGmhbtJMi8MPd6xQSL3I7NWhTZ7ew8Tc3wP0h5E4FPiPaRmLJ1vlO-tsJ4H45oQK0maC_X1uAG-JVbHascc4Dak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFLJHDs9GChB_7J-1NmUbY_3QHlofKk8Mf7EBfY85gkBUqp4zDOo4tglNAjks7BDKRCtoOcF_JfSDoOCKZ2wUJY7FRiUw3vliytDQ_Yac7YvgMyCEj4OZl6K9ctzDW9SHtrB2J92zSp9KVOGs1g7ncxDMdnkgTsDrFOJQuo7lZTyGxIqPjteNtuR6_nw-MWeZIlUSXgAisf-qGCoCK5gnmWLGcpjNjN2i14dlSNv7KZO0UaTh3hssTmrJvuQ2qf1SeNRn8FArhDW0OnoXY2K5exIy1ietvJ4x6R2VDr-DiC0lon-p2ttpkQoPWhkNdm-wX9l2DXmca34HNs-cnAgGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1dcGIOfoGEdLfarg3oCBd9ng-v-49AD7RA812PhYbWinCpdmh98FFR0C9bTQTAErn2n4W1ZvkrJTtGbGaq2mgHgFwmGj3c0DJ81mYIggt3Xt5ADSCIZcWx6D3XfLfQLK3Cf7zL0Q4-YLFC9HdUOyClhp4c9t-kVOBDA5iiuTs71gZZeXHR90yyllHe_Byv6RoLdT9ucP70Xos9aD_I51Bou0dlFWPbp1062LxEnqDK2zb0R8DPQCJUI7VZKr-o3P83TKsJAR50ehlrnyrppx-CsfTZs-S1CtY4xQ3t37ww7g06N9xe5VGyeHlhNZZ_V0ud0w9Ea6BhTcIMsnlIpzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbRsqeYvkfpqET9pR5ooJb1LxWl6cGAs3cEywNw3iiCK0XrlnyhzrkjdakYCHQT5VPydQhwawYQnrOZxe9Gy-AZhoX8tKcw46_kfObgt_3-SxB_AsFTfPxdFN3XJXi_DnDxcldmGeqxU7HAcyMtHCU-wyKq9o_4Xg-Tta4JBiABkfm8048VVaXEAoKOgLLKD8mXD2pht3s18ZYIbFQzjYnkrKP4xwFpdbDfjhlNfXNit1D0tgqVQDQtOLxzPtvAiNuspR_n6F50mIjPUnOSL-uUg0_U69o-wu1ZyVKlTauUcpM__fJUKD5A9F_y98AKTJM953pzIQByIBBQTLLRRuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZIGtB2R5dspLwc2GkumIpuf4NDR51j2JdQZ1SQ5auPbLZs-ch0OUbW4y6O_-LE--8V2tWFQBxz_MapRr-aqDQ4UP7wACXjwGtlsEOiAf9eHu0j9xVX7wAHhe9b9gSOaEPFMAyEJLrHy_EDae44tTCMitdfpJDDaExXK7q_GJBsVDCAaWwyCgDN1YjaGi0hXoPIqEjNY1wHgG7FsBSlhuT4FD9gCgLtV7fWC3S_PttsQ4gnBkUuf0nyfq0u3c1ABuEuAlXuqsVV2JtU626OuuyRRhq2lckb9zXKeBP7ZnGBQr1_FbYzVgI6ebH_IPQTscmPKvitNLfndik-LL7uoHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3axcFxkV0IoQWcx6_8ao0vAeSBoy-atjYbnYH40RAD2CEVIqVv-9vuDyPZ8s8yhJ8AwkjBLQbyBbAoY3W90urF8_8RepBMpixxK2QE-yehLALN77G0B08akaqldNLpgFP_VEoUbngt9GFt37xmBrxDGR76E9XRSweUowOZR7ZsJKs6fBgexXUm0yzWHi9c54XFnGac53cZYCAyRkQ2uNpqBrKP93KSjCWxFu7QKj5w7J0jd0IOtohG7bf16d9VPiKLXenCmEtnUNqd83PMyGXrKO5Z6MyJ9PQQYsq7m-sFFecyKskcCJPWQtklwOGiMSqDKxSkLgQpYP12VqT0C5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yv3kXlo8ozJnQQDCc3BoiWr_4GwkLljVlw3k6glASdaLUha2mEZCaCun7u80hY8rvGr9M67ObAfXDcnhX6jfGThUPsax3Uc4USnJPgZp38taammxuP2GAIuLYzO5gR57LAm0tBjUtIp9zSQ_Gku2q0RI0rWgmGUikDfU1_mopwoIv00j2YX8SsAdaMHs-Rr7bEPUavxrX9mckcOy1bQ-8gYBjeUKq-VhT5jpbkWD-rJSR-mu-kTQX-PByRtnT9cDfB4OrL0pYu_G-Kjlqf20VjemyliAJhcHHw1qmz_29LUttlVn2W1iiRdOR4YsTL0J_X4eom3a6bk_3XbYhCVJPg.jpg" alt="photo" loading="lazy"/></div>
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
