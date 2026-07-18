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
<img src="https://cdn4.telesco.pe/file/pF06wY8Xanbe_1IQVyqW59hXFcK5SXkZKfqQWopjYpZV0M7awkWMykDoLDEZqIDTE8gyfQd4tDedFkNG0Sw7k5UXTBaUW4z8HIc7v93nJwN_lPlz3qrOmBgKLgIy8QIIrL0_cpUPI-IGJb52SHsUpu2cYaZhO7XSnNSwJOYVRrHbkbbdblAVb8XhVSPKQfOZ62nz3nvqv5kAKM7nKLb6b4tz6pu18FcP2mXhLD_d7c7rcZqtVI6KOzN7QDjqOILv67e23uexEdwxILLCC35EXKJoVyJXOlv3frNpYoDKa2Tdf3e8L3ljSyDOc5B9I5neluePyzzgXTovhSsC_V3R4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 01:11:19</div>
<hr>

<div class="tg-post" id="msg-136171">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
❗️
پس از منتفی شدن لیموچی و یوسفی ، مهدی تاتار خواستار جذب محبی شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 334 · <a href="https://t.me/SorkhTimes/136171" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136170">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
انگلیسی که با تیم دومش اومده گل دوم رو هم زد به فرانسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 579 · <a href="https://t.me/SorkhTimes/136170" target="_blank">📅 01:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136169">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
گل اول انگلیس دقیقه چهار به فرانسه زده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/136169" target="_blank">📅 00:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136168">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/SorkhTimes/136168" target="_blank">📅 00:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136167">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
❗️
ورزش سه: محمدرضا اخباری فردا می‌ره باشگاه پرسپولیس و دو ساله می‌بنده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SorkhTimes/136167" target="_blank">📅 00:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136166">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
امشب ساعت 30 دقیقه بامداد بازی رده بندی جام جهانی انجام میشه ...پیش بینی میکنید کدوم تیم سوم میشه ..فرانسه یا انگلیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SorkhTimes/136166" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136165">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
غیررسمی: محمدرضا اخباری با قراردادی 1+1 ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SorkhTimes/136165" target="_blank">📅 00:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136164">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❗️
❗️
کاظمیان تا این لحظه راضی نشده بره گل‌گهر/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SorkhTimes/136164" target="_blank">📅 00:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136163">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
✅
باشگاه پرسپولیس به اخباری گفته فعلا با جایی قرارداد امضا نکن، به عنوان بازیکن آزاد جذبت می‌کنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/136163" target="_blank">📅 00:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136162">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
👎
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس برنامه ای برای جذب بازیکن خارجی وجود نداره،و حتی در صورت جدایی گرا و بیفوما!
💯
تارتار از شرایط باکیچ،اورونوف و سرگیف رضایت کامل دارد،و اگر گرا تخفیف نده احتمالا ماندنی بشه…</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/136162" target="_blank">📅 23:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136161">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فووری از رومانو: آلن هالیلوویچ، بازیکن سابق بارسلونا و فصل پیش فورتانا سیتارد در آستانه امضای قرارداد با باشگاه پرسپولیس ایران هست. مذاکرات در حال انجام و روبه پیشرفت هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/136161" target="_blank">📅 23:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136159">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
پروفایل ترنسفرمارکت هالیلوویچ، این بازیکن 30 ساله به احتمال زیاد جانشین سروش رفیعی در پست شماره 10 خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/136159" target="_blank">📅 23:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136158">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
پروفایل ترنسفرمارکت هالیلوویچ، این بازیکن 30 ساله به احتمال زیاد جانشین سروش رفیعی در پست شماره 10 خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/136158" target="_blank">📅 22:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136157">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
پروفایل ترنسفرمارکت هالیلوویچ، این بازیکن 30 ساله به احتمال زیاد جانشین سروش رفیعی در پست شماره 10 خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/136157" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136156">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❗️
❗️
کاظمیان تا این لحظه راضی نشده بره گل‌گهر/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/136156" target="_blank">📅 22:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136155">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2H67P0sbbbENSWwP6vVnQU47s9bOkY1v_81DdBzoegMRntOE6kBDhv1bDj0UdsDBR4On4VfXPeFWkCTdb9SYMiWc5VmlLx2qU2ePxn8EGKmilzK4-WrevvY2onTqyu5pYUo36sg_gk82wIWhsHWUokfO43qZ9PrwXVC0Vd0xU43Xodz7CuhvRoLg7fMT4e-yVH1-vr6z9VciW2fqirsosPLOdr5ECgGQyZ9d1gASpax0TD_ZIYHAQ5NA2VrnIbw_nUsOs8JzQgLneF22m0GaMLOqEFHwTJmEasrqL5uOhvA1FbOqBC429jSCRYO7YoFU9vQJjpvpXAorHTXLwsONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پروفایل ترنسفرمارکت هالیلوویچ، این بازیکن 30 ساله به احتمال زیاد جانشین سروش رفیعی در پست شماره 10 خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/136155" target="_blank">📅 22:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136153">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فووری از رومانو: آلن هالیلوویچ، بازیکن سابق بارسلونا و فصل پیش فورتانا سیتارد در آستانه امضای قرارداد با باشگاه پرسپولیس ایران هست. مذاکرات در حال انجام و روبه پیشرفت هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/136153" target="_blank">📅 22:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136152">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXab0DFIJUeNq3_taUDIRsJ2Ptdgm3HbHoJaHgbwbuuLLe16oLFPtEnRIrUMPvcMkToRunY_6YPu2jbcJXn5DgZEF_yiVbmVwolL_O9WtolJWYsEvdF4qY9wCVm3gncQUn0HYomrNunATY1i3IU3eptV2sG1fIefJ_D4BhsHO-4EzfDTFrjdCtIdP3JbmJFXIGuTa3AFjyfzUqY9O4u7CmQBGPy_YBXxsCgYp_3u4gOQumH1Bi4KpW1vbA0t7zgUlUe2UoyP67VoybnDs2a4pEf77eRtUIV4dv7MBY3USedCN4E-x6LYx-5IFP1rfq3mtwLmBzyV0TbIU8ZxkCc7Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/136152" target="_blank">📅 22:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136151">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/136151" target="_blank">📅 22:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136150">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
✅
تارتار روی تمدید قرارداد میلاد تاکید زیادی داره/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/136150" target="_blank">📅 22:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136149">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
فووووووووووووووری
⏺
باشگاه اجازه ورود به تمرین رو به کاظمیان نداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/136149" target="_blank">📅 22:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136148">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
🇺🇸
ترامپ:
❗️
دیشب جزیره خارک رو زدیم ولی به نیروهامون گفتم نفت‌ش رو نزنید ممکنه بخوایم جزیره رو تصرف کنیم چون از دستشون کاری برنمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/136148" target="_blank">📅 22:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136147">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
🚨
حملات در جنوب کشور شروع شده...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/136147" target="_blank">📅 22:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136146">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
داورهای بازی فینال و رده‌بندی جام جهانی مشخص شدند و علیرضا فغانی در هیچکدام از این دو دیدار حضور ندارد.
❌
بر اساس اعلام فیفا، اسلاوکو وینچیچ از اسلوونی دیدار فینال جام جهانی بین اسپانیا و آرژانتین را قضاوت خواهد کرد.
✅
همچنین ژسوس والنزوئلا از ونزوئلا،…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/136146" target="_blank">📅 22:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136145">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
فوووووری از رویترز: ترامپ از کشته‌شدن دو سرباز خود توسط ایران شدیدا عصبانی شده و دستور شلیک قدرتمند در ساعات آینده را صادر کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/136145" target="_blank">📅 22:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136144">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم خواهد خورد.
❗️
❗️
درباره کسری…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/136144" target="_blank">📅 22:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136143">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❗️
شهاب زندی: پرسپولیس برای زارع که تو ۵۰ تا تیم ملی نبوده یک میلیون دلار پول داده اما برای دو ملی پوش ما میگه گرونه مقصر من نیستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/136143" target="_blank">📅 21:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136141">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
#تکمیلی؛محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود///خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/136141" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136140">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCm-L7rB-W1QYyX7oHNR8IlpVV4E5bFy3oM-VvPySAGQk2UmJsNAEqkI2cJYm9ETPc6NpdBZ3rtmFAJcPEQgYRPjEWNr7gUi5UrhLkOyonmRsv1r7HFNWYrYkgNvSUrD0soBuBrvq6u5BpM6X6ZBIHI5JDHOfiZ3jGOt2slOUWSOVHcI0SdbPLOmDTKqHLsXZ1JMBPu3GKHQcyllM_zX2ZdCTq1Vk-hBT5T8ZGUa7ZT9bwNU4PLBs8gQMIeY5elxhjezfprcjbS0pbvKeCmstitoSSIEtvAvK8fyPBYyWoSAqQTIRapMwV-k1i_jgPEPbbdmvODUbXtFV_QW53dj4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/136140" target="_blank">📅 21:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136139">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
جلسه با مدیران نساجی برای انتقال دانیال ایری به پرسپولیس در حال برگزاری است / قدوسی
✅
تایید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/136139" target="_blank">📅 21:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136138">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
با اعلام سنتکام، دو سرباز آمریکایی در حمله ایران به اردن کشته شدند و یک سرباز نیز مفقود شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/136138" target="_blank">📅 21:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136137">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
فوری/ سنت‌کام:
❌
دور جدید حملات از الان شروع شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/136137" target="_blank">📅 21:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136136">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه ، وقتش نرسیده که از فوتبال دیدن پول در بیارید؟
😉
✅
@FuckBet</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/136136" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136135">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rv_p2c6PaLn5WxFQUqQaWYx3h-vfKtIN8ZcKMLmqhr-UvJsH3_Oc0lakWcdZh84h9MQh7wIBFIHgHKqI-Cqo36zrcA3WySYjpdat3ZsMqBg1fatZuIj_oWeNPxf2DorT9nIPwI37PZtnFHVc-KG76k62Hs4-ukFiOh5KNKAr-D-bxMX3ocfwm5D98wHrskb4xnE4d7m0fmRh61ih3KQOgTxdLXA9eb2-lINIksxiRCGIggLS3VHI9pLkdYKAWR39kj1pFbW_udM0LkZ_q6sfYnRpbejlWpQ-NkgpYcB600laQ3kb6mH54dm4oeWEPRff8KIDa5109bM2AuZuLGw7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
Ⓜ️
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/136135" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136134">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗️
دانیال ایری هم خیلی یهویی یه استوری گذاشته و نوشته صبر راه رسیدن است…
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/136134" target="_blank">📅 20:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136133">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❗️
جلسه با مدیران نساجی برای انتقال دانیال ایری به پرسپولیس در حال برگزاری است / قدوسی
✅
تایید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136133" target="_blank">📅 19:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136132">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
❌
🔴
دفاع راست ها :
✅
عیدی و تیکدری و براجعه
🔴
دفاع چپ ها :  محمدی و جلالی و معامله گری   نظرتون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136132" target="_blank">📅 19:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136131">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔹
🔹
جلسه با مدیران نساجی برای انتقال دانیال ایری و کسری طاهری به پرسپولیس در حال برگزاری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/136131" target="_blank">📅 19:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136130">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
سامان قدوس؛ بمب بعدی پرسپولیس؟
🔴
🔴
ورزش سه: پرسپولیس برای جذب سامان قدوس هافبک ایرانی اتحاد کلباء امارات درخواست داده و این بازیکن در لیست خرید سرخپوشان قرار گرفته است.
🔴
🔴
قدوس که سابقه بازی در لیگ برتر انگلیس با برنتفورد و تیم ملی ایران را دارد، یکی از…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/136130" target="_blank">📅 19:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136129">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔹
🔹
فووووووووووووری
🚨
حدادی و نیکفر مدیرعامل سپاهان امروز تلفنی صحبت کردن و مدیرعامل سپاهان تاکید کرده به هیچ وجه به پرسپولیس بازیکن ( لیموچی ) نمی‌ده و انتقال ابرقویی هم به سپاهان منتفی شده/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/136129" target="_blank">📅 19:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136127">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
فوووووووری
🔴
🔴
شهاب زندی: من به سرتیپ طاهری پدر کسری عزیز و خود کسری برادر کوچک تر من قول دادم بره پرسپولیس اما مدیران پرسپولیس به دروغ میگن گرونه. برای زارع تو ۵۰ تا تیم ملی نیست ۱۸۰ تا دادن اما برای کسی که ۲۳ تا تیم ملی مبلغ خیلی کمتر از این نمیدن
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136127" target="_blank">📅 18:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136126">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
غیررسمی: محمدرضا اخباری با قراردادی 1+1 ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/136126" target="_blank">📅 18:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136125">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136125" target="_blank">📅 18:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136124">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❗️
نوراللهی با دو نفر در باشگاه و تیم صحبت کرده و گفته که من مشکلی ندارم و می آیم ولی باید با کلبا توافق کنید /
قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/136124" target="_blank">📅 17:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136122">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
#ورزش‌سه : ممکن است به زودی یک قرارداد معاوضه به اضافه پول نقد بین دو باشگاه پرسپولیس و سپاهان شکل گرفته و احتمال دارد نام‌هایی مانند محمدامین کاظمیان، حسین ابرقویی و آریا یوسفی در این معامله جای پیدا کنند. حتی احتمال رخ دادن این اتفاق برای محمد عمری نیز…</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/136122" target="_blank">📅 17:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136120">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⚽️
عبدالصمد ابراهیمی؛ کارشناس حقوق ورزشی:
🔴
جذب کسری طاهری برای پرسپولیس بسیار خطرآفرین و باعث محرومیت این باشگاه از چند پنجره نقل‌وانتقالاتی خواهد شد/ طاهری حداقل تا نیم‌فصل باید در نساجی به میدان برود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/136120" target="_blank">📅 16:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136119">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OowUz9tUf_9Pl6lLogqxtkVsz8ecIgn5KvK6RjSk5mydY9imjNQ7K21YnPu71x6jSnZBuCIo2trcAchBQTqnTHInVa47beJqapxyLsDFHYht-7AJligPkxy4z4dIJXouB4NaLcTw4VhlJx8YjMJG8iq2rfeYFeKaQsLcqpVlt2usC8PU4OHp_R-MoB6HJL1--rqE6sCItr93sM5aoJPzGGAwZBimiaMts2B-FLHz5oRL1L0EcwyIXitCL0oTJzBPO_ajrKjItVsEfzeN9uHCfF1yC1u1Sr2Edr-1BTvq5k6Yx5eVFm5bh-s6mWR-_xj0TyxGU7sGDhqQyUdNqKxJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
مذاکرات تیم پرسپولیس با اتحاد کلباء برای جذب سامان قدوس آغاز شد/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/136119" target="_blank">📅 15:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136117">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
کوشکی و اسلامی توسط ترنسفرمارکت بازیکن آزاد اعلام شدند
🔴
از طرفی ایجنت هر ۲ بازیکن با ایجنت جلالی یکیه
👀
نظرتونه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/136117" target="_blank">📅 15:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136116">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136116" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/136116" target="_blank">📅 15:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136115">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/136115" target="_blank">📅 15:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136114">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
شبکه "فاکس نیوز": نیروهای ویژه ارتش آمریکا سال‌هاست که برای ورود زمینی به ایران آموزش می‌بینند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136114" target="_blank">📅 15:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136113">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
غیررسمی: محمدرضا اخباری با قراردادی 1+1 ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136113" target="_blank">📅 15:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136112">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136112" target="_blank">📅 15:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136111">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGu1VwYkj1BQSKVgkj89_LQ4jC7y8fngDXKEpm8jrU4eWrBgol_BDxSk_e-sNoBoKe-RPL1my1sNLo8EPtKeKWP4ly2bCYsVI5NSL284y5ExRDgAKQiFQjFjgDH8CP5kcwZEH4o1oqxAQ0UhHpKOjNFDr79VqGgzd8CdtLAOlKQ1o7fLtJHHzRUB6fmZLNiu8hxP3_ZQzoHaOrUNwUVyuUgXwr3wKxQRmpiodoYpO6rK6xHBrIfqyUCA3P6j-VAsOHUuiVspCZJonkqAIu76mM1hMdk3qCuD5ICmYv_e_RE4swO3_rL3KiDytqaaa3vngwvX6hri-HCnzMFQOx0hOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
غیررسمی: محمدرضا اخباری با قراردادی 1+1 ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/136111" target="_blank">📅 15:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136110">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/136110" target="_blank">📅 14:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136109">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136109" target="_blank">📅 14:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136108">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
ورزش سه: بازوبند کاپیتانی پرسپولیس مدعی سومی هم داره و اون کسی نیست جز احمد نوراللهی که در آستانه بازگشت به پرسپولیس قرار داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136108" target="_blank">📅 14:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136107">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔹
ممکن است دنیل گرا و تیوی بیفوما در پرسپولیس ماندنی شوند!
🗣
گرا در پست دفاع چپ و هافبک دفاعی تست شده
🔹
بیفوما هم حاضر به فسخ نیست و شاید تا آخر فصل بمونه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/136107" target="_blank">📅 14:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136106">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
شهریار مغانلو مهاجم سابق‌تیم اتحادکلبا با عقد قرار دادی به مدت 2+2 سال به تراکتور پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/136106" target="_blank">📅 14:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136105">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
شهریار مغانلو به تراکتور پیوست
🚩
خط حمله تراکتور برای فصل بعد ؛
🔖
هاشم نژاد
🔖
ترابی
🔖
حسین زاده
🔖
اشترکالی
🔖
مغانلو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/136105" target="_blank">📅 14:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136104">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
❗️
شهریار مغانلو با باشگاه تراکتور به توافق رسید./ ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136104" target="_blank">📅 13:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136103">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
طبق گفته شهاب زندی مدیرعامل نساجی هم دانیال ایری هم کسری طاهری مشکلی برای پیوستن به پرسپولیس ندارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/136103" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136102">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/136102" target="_blank">📅 13:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136101">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136101" target="_blank">📅 13:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136100">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
بمب پرسپولیس در آستانه انفجار؛احمد نوراللهی به تهران بازمی‌گردد/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136100" target="_blank">📅 12:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136099">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136099" target="_blank">📅 12:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136098">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/136098" target="_blank">📅 11:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136097">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKRy41nbSt1T5PeZII1gDDIZmU2QaONwLVxPjBXHM5HH_-xwNGDcqs-mnf6mFQt2388XuVY6C-Scis8SBRQk5MxDmoTkKxsiWhYzzRTReA1TbEoUP9aogFkowHqxMEkNMEoSS5jm5c_swSRZpuHMXPR-1eXbwIs49weRkVZQ-KYbf2AC6Ikog1e9qlPv5zryhZ5GeMlLwPGhDVABA8rtB3MF9tAE1f0pPvVn6ORv-2a1lis8xxw0lqQzXT3BeO-si4OlkQC48ehsF_08UeUUepU-oONUSVMbMEOgtE2J9MzdrXl8DeeJXR7gPg1LUFD5ynRk8rywu5ih92an4lFySw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☹️
تصاویر آب‌شیرین‌كن تخریب شده بونجی جاسك پس از حملات دشمن جنایتکار آمریکایی / ۲۰ روستا با جمعیت ۱۰ هزار نفری بی‌آب شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/136097" target="_blank">📅 11:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136096">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
✅
باشگاه سه گزینه برای دروزاه بان داره  ○ اخباری ○ گوهری ○ دیناروند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/136096" target="_blank">📅 11:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136095">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
ترکیب پرسپولیس تو بازی دوستانه امروز
▪️
پیام نیازمند
▪️
حسین ابرقویی
▪️
حسین کنعانی
▪️
ابوالفضل جلالی
▪️
مجید عیدی
▪️
محمد خدابنده‌لو
▪️
مارکو باکیچ
▪️
مهدی تیکدری
▪️
محمد عمری
▪️
امیرحسین محمودی
▪️
محمد امین کاظمیان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/136095" target="_blank">📅 11:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136094">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
برگام
🚨
فرهیختگان: کسری طاهری به نساجی مازندران پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/136094" target="_blank">📅 10:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136093">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
شنیده ها: میلاد محمدی برای تمدید قرارداد با مبلغ ۷۹ میلیارد تومن (سقف ملی پوش ها) به توافق رسید
❌
محمدی اما اعلام کرده پیش از امضا مطالبات فصل گذشته اش را میخواهد و باشگاه اعلام کرده پس از تمدید قرارداد واریز خواهد کرد! و این موضوع باعث چالش بین طرفین شده…</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/136093" target="_blank">📅 10:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136092">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
🔴
مشکلات قلبی محمد عباس‌زاده و خداحافظی او از فوتبال  محمد عباس زاده روزهای عجیبی را در زندگی خود سپری می‌کند و حالا رسما فوتبال او تمام شده است. مهاجمی که سال‌ها با تعصب و جنگندگی‌اش در خط حمله، لرزه بر تن مدافعان لیگ برتر می‌انداخت، با تشخیص قطعی پزشکان…</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/136092" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136091">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
پهلوان علی آقا دایی خط قرمز مردم ایران است
❤️
🔴
با قلب قرمز به این پست تایید کنید
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/136091" target="_blank">📅 09:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136090">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QM9vXKXfXKy4lJmYYn-n0HVKaxGpeGmotMQ22VgISMkgayKEQZmiBstAZ8BUPUkg2jNH5czLNStgw8L8uxO5CDjlNdoYcdwBGVoky6nBBTKtrTnXUyUvlRtNrHnkbs-jmbxhJjxBvP-YoJSbwukigriZaNv4IE_POm6CcAacjmbIrdUjNA6KFhyODPJ4uOoWrtXaRaAwxutsc_sSn-iOGa9HasZXCHmydETZaOWoQa9jal5RdReHvCUwwIr3vxnunzwvh3AseCjwy_2NcKO0iNEhD77yxRkvnwCWHij3jA89CkiNzrizMeRXKdGWL0oqoQ58EeYXd_dEKz4SNt62Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پهلوان علی آقا دایی خط قرمز مردم ایران است
❤️
🔴
با قلب قرمز به این پست تایید کنید
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/136090" target="_blank">📅 09:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136089">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
✅
یک مازاد دیگر در راه است
🔴
تارتار که از وضعیت فنی چند نفر راضی نیست احتمالا بزودی یکی دو نفر دیگر را در لیست خروج می گذارد.یکی از آنها فعلا به سمت پشت دروازه رهنمون شده و احتمال دارد، کادرفنی اعلام کند به این بازیکن که نتوانسته خودش را در تیم اثبات کند،…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136089" target="_blank">📅 09:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136088">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❗️
کریاکو یاگو، مربی یونانی و جدید بدنساز تیم فوتبال پرسپولیس که با انتخاب مهدی تارتار به باشگاه معرفی شده بود، امروز پنج شنبه وارد ایران شد و مورد استقبال نماینده باشگاه قرار گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136088" target="_blank">📅 09:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136087">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❗️
چند مسیر اصلی در استان هرمزگان بدلیل حملات و بمباران‌های دقایقی‌پیش مسدود شد
❌
پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرز
❌
پل «شور»
❌
تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/136087" target="_blank">📅 08:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136086">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✅
✅
یک مازاد دیگر در راه است
🔴
تارتار که از وضعیت فنی چند نفر راضی نیست احتمالا بزودی یکی دو نفر دیگر را در لیست خروج می گذارد.یکی از آنها فعلا به سمت پشت دروازه رهنمون شده و احتمال دارد، کادرفنی اعلام کند به این بازیکن که نتوانسته خودش را در تیم اثبات کند،…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/136086" target="_blank">📅 08:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136085">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
🔹
تارتار کاظمیان رو گذاشت لیست مازاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/136085" target="_blank">📅 08:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136084">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
فوووووووری
🔴
🔴
شهاب زندی: من به سرتیپ طاهری پدر کسری عزیز و خود کسری برادر کوچک تر من قول دادم بره پرسپولیس اما مدیران پرسپولیس به دروغ میگن گرونه. برای زارع تو ۵۰ تا تیم ملی نیست ۱۸۰ تا دادن اما برای کسی که ۲۳ تا تیم ملی مبلغ خیلی کمتر از این نمیدن
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/136084" target="_blank">📅 08:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136082">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8WueIHIUZl7nhrb6kaAfbpkbLULMfX2wVXDkHWQPOuiorqAd8zOqEUyaD1Qiv_x5scAfsRJgFUHPvox48Ie1MleDOWgMiEyWTNgz0dopMp0i-53XFOsS7grdoObdLrdT0CTG40CE2lKfHxoZvUxE0nkqabSKV5nI2CHvqt07hT8JOX4Bua4oNG934JKC3r2-vwlQpsg2Z3UzFquNqqVejszMnvsR48xgq1x6gG5cG1zJfE9SL__aErJMJtH5KbneMXSHvnGPMwh9ddvzNRIQ-W1mYAoW1QErhQ7uAZKbB5-1BZ5AnOTqocucY4rON9aa_Px-kCLpkwH7yNxQP5uJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a229bafa39.mp4?token=kz6t086_fl6tt0oolNdhQG_KZJHWKcU2noc2v6hVvu7cXNDMlmIpd0O_SjMuGgqFFpg_B5uf-FoPusJYLb5aKsrNopQcOFcLHsBDUo59JR0mzMIDwqmyZ4bP-X6g9HMhBJfiQhqv5gCrUw9HQ3po47qjS1zxBloZPbRIJt7lEaTCJrOGTYkp3qJc3QUd0fd4MHLJc3WsbG8DXJO5wgtiyxaoeC-wFljlqlSPtOKJQxKMQVBFiziKulaQQOg-B6K1Uj6Aqf9sYLuZsMdl2YYGk0iTI0Q5ykKCUXhS8b_li_HDFnQEXAdFmQKPlGYY35LJi7d-gH07-p3QEQpLZOntfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a229bafa39.mp4?token=kz6t086_fl6tt0oolNdhQG_KZJHWKcU2noc2v6hVvu7cXNDMlmIpd0O_SjMuGgqFFpg_B5uf-FoPusJYLb5aKsrNopQcOFcLHsBDUo59JR0mzMIDwqmyZ4bP-X6g9HMhBJfiQhqv5gCrUw9HQ3po47qjS1zxBloZPbRIJt7lEaTCJrOGTYkp3qJc3QUd0fd4MHLJc3WsbG8DXJO5wgtiyxaoeC-wFljlqlSPtOKJQxKMQVBFiziKulaQQOg-B6K1Uj6Aqf9sYLuZsMdl2YYGk0iTI0Q5ykKCUXhS8b_li_HDFnQEXAdFmQKPlGYY35LJi7d-gH07-p3QEQpLZOntfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📌
حمله شب گذشته آمریکایی ها به پل سه‌راه‌ میناب به‌سمت رودان
🫦
پ.ن: کمک های ترامپ به مردم ایران…همونطور که میبینید کمک از راه رسید،یه عده واقعا گاون توهین به گاوه بی رگ های وطن فروش،وایسید عمو ترامپ براتون برینه وقتی نمیتونید مسائل رو از هم تفکیک کنید میشه این
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/136082" target="_blank">📅 08:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136081">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
فوووووووووووری
😀
کانال 14 اسراییل: پل و راه اهن و فرودگاه و پادگان ها در جنوب ایران بمباران میشوند تا جنوب تسخیر شود. بزودی نیروهای امریکا وارد ایران میشوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/136081" target="_blank">📅 08:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136080">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E74Bs1sG4rzZ_9vJkKR-7Qt-S8QmncFSfKY_HGx7BLdaKqC8GsWcAhPpMQQQq-nXHBFfxJ3BHdCx7r-4NFYpyo-SPGhkKrDi3jDpSrpkwRi0O9dM1AhQXjMWJ9Z-MWrCLAqA9x-ogmnK_Wp4xVfAxszH5cAmeiNMUlcg12EaAXATrUzAJTY0m5OTc2Ri-AxfxLZJNscY7p-xomMD7VbRtA8XY5YRXoP2dSemhTYLf3TV6dIkMoZ6pflWyKWAzbhSV2VMCjbw-k7NbKVuqrXvmeO8O9TlJDWzxE5mnYw0OCaP1e3O1_PefDAMZckfOG6mtILf2o84pwLYgzP347cmHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس ممکنه زندگی نده، ولی
شادی میده
عشق میده
اینه داستان سرخ...
❤️
‌
سلام صبح بخیر پرسپولیسیها؛
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/136080" target="_blank">📅 08:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136079">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136079" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/136079" target="_blank">📅 02:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136078">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrcuhvRoDoVWJuXVB-AIqEGhyQ9oJSz_e_JMqRwX54A7Ce43aa_bOmWKBaYo0JjQocviHP4Ax7kAIm259W8p0Rsmf62SUsYavZzLkDzR7PYGlzdtud6iYqazFA7_AbAMH9Rzl0TkOG-FwgEeXwmiOSciTE6WjjFZS8J8FQDdmOlm5ZK0z0FrsJBKnnMPmWt6fuTUBxMP_LiZz3QrLqDCb-bM01e_MVOV9GjZWHLh0NfYni7OgliBAux8CvXm8edtJhAD163BKlQo6BXGqszyWb01mnvTo49DkcHqREKAF7YeLIhreXrCt66Wcdf--7847-bK0k8WsUVA0XyGwECJeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/136078" target="_blank">📅 02:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136077">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمهدی</strong></div>
<div class="tg-text">متاسفانه تابستونا دبستان تعطیل میشه هرکی میرسه از ادمین انتقاد میکنه .
اطلا متوجه میشین چی شده؟
🤣</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/136077" target="_blank">📅 02:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136076">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">این اسمش توش کنیه
ما کیسه نیستیم</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136076" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136075">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMehdihormozi</strong></div>
<div class="tg-text">اینا خرید که گرونتر بده به پرسپولیس دم مدیران پرسپولیس گرم دستش را خواندند به بازیکنان قول هم داده شما را می‌فرستم پرسپولیس حالا مونده چکار کنه</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136075" target="_blank">📅 01:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136074">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
شهاب زندی: آقای تارتار رفیقمه آدم سالمیه. آقای حدادی آدم سالمیه اما برخی در باشگاه پرسپولیس مانع انتقال دو ستاره ما به پرسپولیس شده اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136074" target="_blank">📅 01:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136073">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
فوووووووری
🔴
🔴
شهاب زندی: من به سرتیپ طاهری پدر کسری عزیز و خود کسری برادر کوچک تر من قول دادم بره پرسپولیس اما مدیران پرسپولیس به دروغ میگن گرونه. برای زارع تو ۵۰ تا تیم ملی نیست ۱۸۰ تا دادن اما برای کسی که ۲۳ تا تیم ملی مبلغ خیلی کمتر از این نمیدن
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136073" target="_blank">📅 01:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136072">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
✅
نیمه شب امشب صدای پنج انفجار در برخی مناطق حاشیه‌ای شهر یزد شنیده شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136072" target="_blank">📅 01:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136071">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
✅
نیمه شب امشب صدای پنج انفجار در برخی مناطق حاشیه‌ای شهر یزد شنیده شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136071" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136070">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
فوری/ سنت‌کام:
❌
دور جدید حملات از الان شروع شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136070" target="_blank">📅 01:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136069">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
✅
شهاب زندی: هواداران عزیز پرسپولیس، با همون مبلغی که کسری رو خریدیم میخوایم به پرسپولیس بفروشیم اما مدیران تون میگن نه
😐
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/136069" target="_blank">📅 00:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136068">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
❗️
شهاب زندی مدیرعامل نساجی :
❌
❌
آقای خلیلی میگه کسری طاهری رو نمیخواستیم و گرون بود، اصلا قرار نبود برای کسری پول بدن، اصلا ما نمیتونستیم کسری طاهری رو بفروشیم، ما خودمون کسری طاهری رو خریده بودیم و ثبت کرده بودیم
✅
✅
هوادارای عزیز، مردم، مسئولین و همه سازمان…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136068" target="_blank">📅 00:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136067">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
✅
شهاب زندی: هواداران عزیز پرسپولیس، با همون مبلغی که کسری رو خریدیم میخوایم به پرسپولیس بفروشیم اما مدیران تون میگن نه
😐
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136067" target="_blank">📅 00:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136066">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X97sVt4PEfL-lWRuQ8FcFTtsR1IP4MsuAgch4_I1lfJ82FLaSXAlJ-griJkY1e4oJhtQq9hcv4cm_h3-VT9-Zo4QVWsuu_v9eJ_VvRsri-w6pasf-z0C2uyAuqFuyygg4tHTgdqgbEAeepdoamiHlimLOQ7byMQDZk2KRqT1zVtd2mEeOc6X94OQ39fs2Yoa2TP_uc7yEPLWi9zfWZDfnOyIMhBkn4qzOMuU9hP-cMJEfLprlLBQzOTiJaoCMbvDKJFzNCJVzJTg2_Q6zL67Omr43wDQYXCBAG56QKxpYBidoiupl544x6_MfMnc1Uh5og0kp5W0u2yGV23BeIRZAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
محمدحسین صادقی در تمرین امروز پرسپولیس حضور داشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136066" target="_blank">📅 00:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136065">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
شهاب زندی: هواداران عزیز پرسپولیس، با همون مبلغی که کسری رو خریدیم میخوایم به پرسپولیس بفروشیم اما مدیران تون میگن نه
😐
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/136065" target="_blank">📅 00:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136064">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❗️
شهاب زندی: پرسپولیس برای زارع که تو ۵۰ تا تیم ملی نبوده یک میلیون دلار پول داده اما برای دو ملی پوش ما میگه گرونه مقصر من نیستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/136064" target="_blank">📅 00:40 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
